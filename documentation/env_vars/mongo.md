# Настройка MongoDB через переменные окружения

### Параметры в RUNTIME

Определены в файле `src/infrastructure/database/mongo/settings/composite.py` в классе `Settings`.

### Значения по умолчанию

Определены в файле `src/infrastructure/database/mongo/settings/defaults.py` в соответствующих классах `*Defaults`.

## Архитектура класса Settings

Класс `Settings` в `src/infrastructure/database/mongo/settings/composite.py` служит центральным конфигурационным центром
для подключений MongoDB, объединяя различные компоненты конфигурации через систему управления настройками Pydantic.

### Структура и назначение класса

Класс `Settings` наследуется от `BaseSettings` Pydantic и объединяет несколько аспектов конфигурации в единую
согласованную конфигурацию клиента MongoDB. Он реализует паттерн компоновщика, агрегируя специализированные классы
настроек для различных областей конфигурации MongoDB.

### Загрузка переменных окружения

Класс использует `SettingsConfigDict` Pydantic для определения способа загрузки переменных окружения:

```python
model_config = SettingsConfigDict(
    env_file=BaseDefaults.ENV_FILE,
    env_prefix=BaseDefaults.ENV_PREFIX,  # "MONGODB_"
    env_file_encoding=BaseDefaults.ENV_FILE_ENCODING,
    env_nested_delimiter=BaseDefaults.ENV_NESTED_DELIMITER,  # "__"
    extra=BaseDefaults.EXTRA,
    frozen=BaseDefaults.FROZEN,
)
```

Эта конфигурация обеспечивает:

- Загрузку из файлов окружения (по умолчанию `.env`)
- Использование `MONGODB_` в качестве префикса для всех переменных окружения, связанных с MongoDB
- Использование `__` в качестве разделителя для вложенных настроек (например, `MONGODB_POOL__MAX_SIZE`)
- Правильную обработку дополнительных полей и настроек неизменяемости

### Процесс сборки параметров

Основой класса `Settings` является свойство `client_kwargs`, которое собирает итоговый словарь конфигурации для клиента
MongoDB:

```python
@property
def client_kwargs(self) -> dict[str, Any]:
    result: dict[str, Any] = {}

    result.update(self.pool.client_kwargs)
    result.update(self.timeouts.client_kwargs)
    result.update(self.retry_behavior.client_kwargs)
    result.update(self.tls.client_kwargs)
    result.update(self.compression.client_kwargs)
    result.update(self.representation.client_kwargs)
    result.update(self.connection_mode.client_kwargs)
    result.update(self.write_concern.client_kwargs)
    result.update(self.read_concern.client_kwargs)
    result.update(self.error_handling.client_kwargs)

    # Аутентификация включается только при наличии учетных данных
    if self.connection0.USERNAME:
        result.update(self.authentication.client_kwargs)

    # Настройки SRV включаются только для подключений mongodb+srv
    if self.connection0.SCHEMA.endswith("srv"):
        result.update(self.srv.client_kwargs)

    return result
```

#### Порядок слияния и приоритет

Параметры конфигурации объединяются в определенном порядке:

1. Настройки пула
2. Таймауты
3. Поведение при повторных попытках
4. TLS/SSL
5. Сжатие
6. Представление
7. Режим подключения
8. Подтверждение записи
9. Согласованность чтения
10. Обработка ошибок

Этот порядок гарантирует, что более фундаментальные параметры подключения устанавливаются первыми, а более высокие
уровни применяются после. При наличии перекрывающихся ключей более поздние настройки переопределяют более ранние.

#### Условное включение конфигурации

Два важных условных включения обеспечивают соответствующую конфигурацию:

- **Аутентификация**: Включается только при наличии `connection0.USERNAME`, что предотвращает ненужные параметры
  аутентификации при подключении к экземплярам MongoDB, которым не требуется аутентификация.

- **Настройки SRV**: Включаются только при использовании схемы `mongodb+srv`, так как записи SRV специфичны для этого
  типа подключения.

### Роли компонентов в процессе сборки

Каждый компонент в процессе сборки имеет определенную ответственность:

- **PoolSettings**: Управляет параметрами пула подключений
- **TimeoutsSettings**: Контролирует различные значения таймаутов для подключений и операций
- **RetryBehaviorSettings**: Настраивает поведение при повторных попытках чтения и записи
- **TLSSettings**: Обрабатывает шифрование TLS/SSL и проверку сертификатов
- **CompressionSettings**: Управляет сетевым сжатием (snappy, zlib, zstd)
- **RepresentationSettings**: Контролирует представление данных
- **ConnectionModeSettings**: Определяет топологию подключения (прямое, набор реплик) и предпочтения чтения
- **WriteConcernSettings**: Задает требования к подтверждению записи
- **ReadConcernSettings**: Определяет требования к согласованности для операций чтения
- **ErrorHandlingSettings**: Настраивает поведение при обработке ошибок
- **AuthenticationSettings**: Управляет учетными данными и механизмами аутентификации
- **SRVSettings**: Обрабатывает параметры, специфичные для записей SRV

### Генерация строки подключения

Хотя напрямую не является частью свойства `client_kwargs`, класс `Settings` также предоставляет генерацию строк
подключения через метод `get_connections()`:

```python
def get_connections(self, with_secret: bool = False) -> Sequence[str]:
    return [self.connection0.dsn(with_secret=with_secret).encoded_string()]
```

Этот метод генерирует правильно отформатированные строки подключения MongoDB из конфигурации, с возможностью включения
или исключения конфиденциальной информации, такой как пароли.

### Построение итоговой конфигурации

Итоговый словарь конфигурации строится путем объединения:

1. Параметров клиента из `client_kwargs`
2. Имени базы данных из `DB_NAME`
3. Строк подключения из `get_connections()`

Это обрабатывается методом `_parameters()`:

```python
def _parameters(self) -> dict[str, Any]:
    config = self.client_kwargs
    config.update({"database": self.database})
    config.update({"connections": self.get_connections()})
    return config
```

### Механизм логирования

Класс включает комплексное логирование во время инициализации:

```python
def __init__(self) -> None:
    logger.info("loading the settings...")
    super().__init__()
    logger.info("settings was loaded successfully")
    logger.debug(f"settings parameters: {self._parameters()}")
```

Это обеспечивает:

- Информационное сообщение при начале загрузки настроек
- Подтверждение успешной загрузки
- Отладочное логирование всех итоговых параметров (полезно для устранения неполадок)

## Группы настроек

Настройки разделены на группы, каждая из которых соответствует отдельному классу в кодовой базе. Переменные окружения
используют вложенный формат с разделителем `__`.

### Connection Settings (Подключение)

**Python Path:** `src.infrastructure.database.mongo.settings.connection.ConnectionSettings`

| Переменная окружения            | Описание                                    | Значение по умолчанию | Константа в коде              |
|---------------------------------|---------------------------------------------|-----------------------|-------------------------------|
| `MONGODB_CONNECTION0__HOST`     | Хост MongoDB                                | `localhost`           | `ConnectionDefaults.HOST`     |
| `MONGODB_CONNECTION0__PORT`     | Порт MongoDB                                | `27017`               | `ConnectionDefaults.PORT`     |
| `MONGODB_CONNECTION0__USERNAME` | Имя пользователя для аутентификации         | пустая строка         | `ConnectionDefaults.USERNAME` |
| `MONGODB_CONNECTION0__PASSWORD` | Пароль для аутентификации                   | пустая строка         | `ConnectionDefaults.PASSWORD` |
| `MONGODB_CONNECTION0__SCHEMA`   | Схема подключения (mongodb или mongodb+srv) | `mongodb`             | `ConnectionDefaults.SCHEMA`   |
| `MONGODB_CONNECTION0__DATABASE` | Имя базы данных                             | `default-database`    | `ConnectionDefaults.DATABASE` |

> **Важно:** Поддерживается несколько соединений с MongoDB. Для этого используйте нумерацию в имени переменной (
> например, `connection0`, `connection1`, `connection2` и т.д.). В текущей реализации используется `connection0` как
> пример, но можно настроить дополнительные соединения с другими номерами.

### Pool Settings (Пул соединений)

**Python Path:** `src.infrastructure.database.mongo.settings.pool.PoolSettings`

| Переменная окружения                   | Описание                                              | Значение по умолчанию | Константа в коде                      |
|----------------------------------------|-------------------------------------------------------|-----------------------|---------------------------------------|
| `MONGODB_POOL__MAX_SIZE`               | Максимальное количество соединений в пуле             | `100`                 | `PoolDefaults.MAX_SIZE`               |
| `MONGODB_POOL__MIN_SIZE`               | Минимальное количество соединений в пуле              | `0`                   | `PoolDefaults.MIN_SIZE`               |
| `MONGODB_POOL__MAX_IDLE_TIME_MS`       | Максимальное время простоя соединения в миллисекундах | `0`                   | `PoolDefaults.MAX_IDLE_TIME_MS`       |
| `MONGODB_POOL__MAX_CONNECTING`         | Максимальное количество одновременных соединений      | `5`                   | `PoolDefaults.MAX_CONNECTING`         |
| `MONGODB_POOL__WAIT_QUEUE_TIMEOUT_MS`  | Таймаут ожидания свободного соединения из пула        | `0`                   | `PoolDefaults.WAIT_QUEUE_TIMEOUT_MS`  |
| `MONGODB_POOL__HEARTBEAT_FREQUENCY_MS` | Частота проверки состояния сервера                    | `10000`               | `PoolDefaults.HEARTBEAT_FREQUENCY_MS` |
| `MONGODB_POOL__SERVER_MONITORING_MODE` | Режим мониторинга сервера                             | `auto`                | `PoolDefaults.SERVER_MONITORING_MODE` |

### Timeouts Settings (Таймауты)

**Python Path:** `src.infrastructure.database.mongo.settings.timeouts.TimeoutsSettings`

| Переменная окружения                    | Описание                     | Значение по умолчанию | Константа в коде                       |
|-----------------------------------------|------------------------------|-----------------------|----------------------------------------|
| `MONGODB_TIMEOUTS__CONNECTION_MS`       | Таймаут установки соединения | `20000`               | `TimeoutsDefaults.CONNECTION_MS`       |
| `MONGODB_TIMEOUTS__SOCKET_MS`           | Таймаут сокета               | `20000`               | `TimeoutsDefaults.SOCKET_MS`           |
| `MONGODB_TIMEOUTS__SERVER_SELECTION_MS` | Таймаут выбора сервера       | `30000`               | `TimeoutsDefaults.SERVER_SELECTION_MS` |
| `MONGODB_TIMEOUTS__OPERATION_MS`        | Таймаут операции             | `10000`               | `TimeoutsDefaults.OPERATION_MS`        |

### Retry Behavior Settings (Повторные попытки)

**Python Path:** `src.infrastructure.database.mongo.settings.retry_behavior.RetryBehaviorSettings`

| Переменная окружения             | Описание                                                  | Значение по умолчанию | Константа в коде               |
|----------------------------------|-----------------------------------------------------------|-----------------------|--------------------------------|
| `MONGODB_RETRY_BEHAVIOR__WRITES` | Включить повторные записывающие операции при ошибках сети | `True`                | `RetryBehaviorDefaults.WRITES` |
| `MONGODB_RETRY_BEHAVIOR__READS`  | Включить повторные читающие операции при ошибках сети     | `True`                | `RetryBehaviorDefaults.READS`  |

### TLS Settings (Шифрование)

**Python Path:** `src.infrastructure.database.mongo.settings.tls.TLSSettings`

| Переменная окружения                         | Описание                                                            | Значение по умолчанию | Константа в коде                            |
|----------------------------------------------|---------------------------------------------------------------------|-----------------------|---------------------------------------------|
| `MONGODB_TLS__ENABLE`                        | Использовать TLS/SSL шифрование                                     | `False`               | `TLSDefaults.ENABLE`                        |
| `MONGODB_TLS__INSECURE`                      | Разрешить недействительные сертификаты и несоответствие имён хостов | `False`               | `TLSDefaults.INSECURE`                      |
| `MONGODB_TLS__ALLOW_INVALID_CERTIFICATES`    | Разрешить недействительные сертификаты                              | `False`               | `TLSDefaults.ALLOW_INVALID_CERTIFICATES`    |
| `MONGODB_TLS__ALLOW_INVALID_HOSTNAMES`       | Разрешить несоответствие имён хостов                                | `False`               | `TLSDefaults.ALLOW_INVALID_HOSTNAMES`       |
| `MONGODB_TLS__CA_FILE`                       | Путь к сертификатам центра сертификации                             | `None`                | `TLSDefaults.CA_FILE`                       |
| `MONGODB_TLS__CERTIFICATE_KEY_FILE`          | Путь к клиентскому сертификату                                      | `None`                | `TLSDefaults.CERTIFICATE_KEY_FILE`          |
| `MONGODB_TLS__CRL_FILE`                      | Путь к списку отозванных сертификатов                               | `None`                | `TLSDefaults.CRL_FILE`                      |
| `MONGODB_TLS__CERTIFICATE_KEY_FILE_PASSWORD` | Пароль для клиентского сертификата                                  | `None`                | `TLSDefaults.CERTIFICATE_KEY_FILE_PASSWORD` |
| `MONGODB_TLS__DISABLE_OCSP_ENDPOINT_CHECK`   | Отключить проверку OCSP endpoint                                    | `False`               | `TLSDefaults.DISABLE_OCSP_ENDPOINT_CHECK`   |

### Compression Settings (Сжатие)

**Python Path:** `src.infrastructure.database.mongo.settings.compression.CompressionSettings`

| Переменная окружения                          | Описание                                 | Значение по умолчанию | Константа в коде                             |
|-----------------------------------------------|------------------------------------------|-----------------------|----------------------------------------------|
| `MONGODB_COMPRESSION__COMPRESSORS`            | Список компрессоров (snappy, zlib, zstd) | `None`                | `CompressionDefaults.COMPRESSORS`            |
| `MONGODB_COMPRESSION__ZLIB_COMPRESSION_LEVEL` | Уровень сжатия zlib                      | `None`                | `CompressionDefaults.ZLIB_COMPRESSION_LEVEL` |

### Representation Settings (Представление данных)

**Python Path:** `src.infrastructure.database.mongo.settings.representation.RepresentationSettings`

| Переменная окружения           | Описание                  | Значение по умолчанию | Константа в коде              |
|--------------------------------|---------------------------|-----------------------|-------------------------------|
| `MONGODB_REPRESENTATION__UUID` | Формат представления UUID | `standard`            | `RepresentationDefaults.UUID` |

### Connection Mode Settings (Режим подключения)

**Python Path:** `src.infrastructure.database.mongo.settings.connection_mode.ConnectionModeSettings`

| Переменная окружения                             | Описание                                                        | Значение по умолчанию | Константа в коде                               |
|--------------------------------------------------|-----------------------------------------------------------------|-----------------------|------------------------------------------------|
| `MONGODB_CONNECTION_MODE__DIRECT_CONNECTION`     | Прямое соединение с указанным хостом                            | `None`                | `ConnectionModeDefaults.DIRECT_CONNECTION`     |
| `MONGODB_CONNECTION_MODE__APPNAME`               | Имя приложения для логов                                        | `None`                | `ConnectionModeDefaults.APPNAME`               |
| `MONGODB_CONNECTION_MODE__READ_PREFERENCE`       | Предпочтение чтения (primary, secondary и т.д.)                 | `None`                | `ConnectionModeDefaults.READ_PREFERENCE`       |
| `MONGODB_CONNECTION_MODE__READ_PREFERENCE_TAGS`  | Набор тегов для предпочтения чтения                             | `None`                | `ConnectionModeDefaults.READ_PREFERENCE_TAGS`  |
| `MONGODB_CONNECTION_MODE__MAX_STALENESS_SECONDS` | Максимальное отставание репликации для чтения с вторичных узлов | `None`                | `ConnectionModeDefaults.MAX_STALENESS_SECONDS` |
| `MONGODB_CONNECTION_MODE__REPLICA_SET_NAME`      | Имя набора реплик                                               | `None`                | `ConnectionModeDefaults.REPLICA_SET_NAME`      |

### Authentication Settings (Аутентификация)

**Python Path:** `src.infrastructure.database.mongo.settings.authentication.AuthenticationSettings`

| Переменная окружения                           | Описание                          | Значение по умолчанию | Константа в коде                              |
|------------------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------|
| `MONGODB_AUTHENTICATION__SOURCE`               | База данных для аутентификации    | `admin`               | `AuthenticationDefaults.SOURCE`               |
| `MONGODB_AUTHENTICATION__MECHANISM`            | Механизм аутентификации           | `SCRAM-SHA-256`       | `AuthenticationDefaults.MECHANISM`            |
| `MONGODB_AUTHENTICATION__MECHANISM_PROPERTIES` | Свойства механизма аутентификации | `None`                | `AuthenticationDefaults.MECHANISM_PROPERTIES` |

### Write Concern Settings (Подтверждение записи)

**Python Path:** `src.infrastructure.database.mongo.settings.write_concern.WriteConcernSettings`

| Переменная окружения             | Описание                                         | Значение по умолчанию | Константа в коде               |
|----------------------------------|--------------------------------------------------|-----------------------|--------------------------------|
| `MONGODB_WRITE_CONCERN__W`       | Уровень подтверждения записи (количество реплик) | `None`                | `WriteConcernDefaults.W`       |
| `MONGODB_WRITE_CONCERN__JOURNAL` | Дожидаться записи в журнал                       | `False`               | `WriteConcernDefaults.JOURNAL` |
| `MONGODB_WRITE_CONCERN__FSYNC`   | Дожидаться сброса записи на диск                 | `False`               | `WriteConcernDefaults.FSYNC`   |

### Read Concern Settings (Согласованность чтения)

**Python Path:** `src.infrastructure.database.mongo.settings.read_concern.ReadConcernSettings`

| Переменная окружения          | Описание                       | Значение по умолчанию | Константа в коде            |
|-------------------------------|--------------------------------|-----------------------|-----------------------------|
| `MONGODB_READ_CONCERN__LEVEL` | Уровень согласованности чтения | `majority`            | `ReadConcernDefaults.LEVEL` |

### SRV Settings (SRV-записи)

**Python Path:** `src.infrastructure.database.mongo.settings.srv.SRVSettings`

| Переменная окружения        | Описание                                             | Значение по умолчанию | Константа в коде           |
|-----------------------------|------------------------------------------------------|-----------------------|----------------------------|
| `MONGODB_SRV__SERVICE_NAME` | Имя службы для SRV-запросов                          | `mongodb`             | `SRVDefaults.SERVICE_NAME` |
| `MONGODB_SRV__MAX_HOSTS`    | Максимальное количество хостов при использовании SRV | `1`                   | `SRVDefaults.MAX_HOSTS`    |

### Error Handling Settings (Обработка ошибок)

**Python Path:** `src.infrastructure.database.mongo.settings.erro_handling.ErrorHandlingSettings`

| Переменная окружения                     | Описание                                | Значение по умолчанию | Константа в коде                       |
|------------------------------------------|-----------------------------------------|-----------------------|----------------------------------------|
| `MONGODB_ERROR_HANDLING__UNICODE_DECODE` | Обработчик ошибок декодирования Unicode | `strict`              | `ErrorHandlingDefaults.UNICODE_DECODE` |