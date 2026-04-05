# Настройка MongoDB через переменные окружения

### Параметры в RUNTIME

Определены в файле `src/infra/db/mongo/settings.py` в классе `Settings`.

### Значения по умолчанию

Определены в файле `src/infra/db/mongo/constants.py` в классе `Defaults`.

### Префикс переменных окружения

Префикс `MONGODB_` для переменных окружения определён в атрибуте `ENV_PREFIX` класса `Defaults`.

## Таблица переменных

| Переменная окружения                        | Описание                                                            | Значение по умолчанию | Константа в коде                             |
|---------------------------------------------|---------------------------------------------------------------------|-----------------------|----------------------------------------------|
| `MONGODB_HOST`                              | Хост MongoDB                                                        | `localhost`           | `Defaults.HOST`                              |
| `MONGODB_PORT`                              | Порт MongoDB                                                        | `27017`               | `Defaults.PORT`                              |
| `MONGODB_SCHEMA`                            | Схема подключения (mongodb или mongodb+srv)                         | `mongodb`             | `Defaults.SCHEMA`                            |
| `MONGODB_USERNAME`                          | Имя пользователя для аутентификации                                 | `None`                | `Defaults.USERNAME`                          |
| `MONGODB_PASSWORD`                          | Пароль для аутентификации                                           | `None`                | `Defaults.PASSWORD`                          |
| `MONGODB_DATABASE`                          | Имя базы данных по умолчанию                                        | `None`                | `Defaults.DATABASE`                          |
| `MONGODB_MAX_POOL_SIZE`                     | Максимальное количество соединений в пуле                           | `None`                | `Defaults.MAX_POOL_SIZE`                     |
| `MONGODB_MIN_POOL_SIZE`                     | Минимальное количество соединений в пуле                            | `None`                | `Defaults.MIN_POOL_SIZE`                     |
| `MONGODB_MAX_IDLE_TIME_MS`                  | Максимальное время простоя соединения в миллисекундах               | `None`                | `Defaults.MAX_IDLE_TIME_MS`                  |
| `MONGODB_MAX_CONNECTING`                    | Максимальное количество одновременных соединений                    | `None`                | `Defaults.MAX_CONNECTING`                    |
| `MONGODB_WAIT_QUEUE_TIMEOUT_MS`             | Таймаут ожидания свободного соединения из пула                      | `None`                | `Defaults.WAIT_QUEUE_TIMEOUT_MS`             |
| `MONGODB_HEARTBEAT_FREQUENCY_MS`            | Частота проверки состояния сервера                                  | `None`                | `Defaults.HEARTBEAT_FREQUENCY_MS`            |
| `MONGODB_SERVER_MONITORING_MODE`            | Режим мониторинга сервера                                           | `None`                | `Defaults.SERVER_MONITORING_MODE`            |
| `MONGODB_CONNECT_TIMEOUT_MS`                | Таймаут установки соединения                                        | `20000`               | `Defaults.CONNECT_TIMEOUT_MS`                |
| `MONGODB_SOCKET_TIMEOUT_MS`                 | Таймаут сокета                                                      | `20000`               | `Defaults.SOCKET_TIMEOUT_MS`                 |
| `MONGODB_SERVER_SELECTION_TIMEOUT_MS`       | Таймаут выбора сервера                                              | `30000`               | `Defaults.SERVER_SELECTION_TIMEOUT_MS`       |
| `MONGODB_TIMEOUT_MS`                        | Таймаут операции                                                    | `10000`               | `Defaults.TIMEOUT_MS`                        |
| `MONGODB_RETRY_WRITES`                      | Включить повторные записывающие операции при ошибках сети           | `True`                | `Defaults.RETRY_WRITES`                      |
| `MONGODB_RETRY_READS`                       | Включить повторные читающие операции при ошибках сети               | `True`                | `Defaults.RETRY_READS`                       |
| `MONGODB_TLS`                               | Использовать TLS/SSL шифрование                                     | `False`               | `Defaults.TLS`                               |
| `MONGODB_TLS_INSECURE`                      | Разрешить недействительные сертификаты и несоответствие имён хостов | `False`               | `Defaults.TLS_INSECURE`                      |
| `MONGODB_TLS_ALLOW_INVALID_CERTIFICATES`    | Разрешить недействительные сертификаты                              | `False`               | `Defaults.TLS_ALLOW_INVALID_CERTIFICATES`    |
| `MONGODB_TLS_ALLOW_INVALID_HOSTNAMES`       | Разрешить несоответствие имён хостов                                | `False`               | `Defaults.TLS_ALLOW_INVALID_HOSTNAMES`       |
| `MONGODB_TLS_CA_FILE`                       | Путь к сертификатам центра сертификации                             | `None`                | `Defaults.TLS_CA_FILE`                       |
| `MONGODB_TLS_CERTIFICATE_KEY_FILE`          | Путь к клиентскому сертификату                                      | `None`                | `Defaults.TLS_CERTIFICATE_KEY_FILE`          |
| `MONGODB_TLS_CRL_FILE`                      | Путь к списку отозванных сертификатов                               | `None`                | `Defaults.TLS_CRL_FILE`                      |
| `MONGODB_TLS_CERTIFICATE_KEY_FILE_PASSWORD` | Пароль для клиентского сертификата                                  | `None`                | `Defaults.TLS_CERTIFICATE_KEY_FILE_PASSWORD` |
| `MONGODB_TLS_DISABLE_OCSP_ENDPOINT_CHECK`   | Отключить проверку OCSP endpoint                                    | `False`               | `Defaults.TLS_DISABLE_OCSP_ENDPOINT_CHECK`   |
| `MONGODB_COMPRESSORS`                       | Список компрессоров (snappy, zlib, zstd)                            | `None`                | `Defaults.COMPRESSORS`                       |
| `MONGODB_ZLIB_COMPRESSION_LEVEL`            | Уровень сжатия zlib                                                 | `None`                | `Defaults.ZLIB_COMPRESSION_LEVEL`            |
| `MONGODB_UUID_REPRESENTATION`               | Формат представления UUID                                           | `standard`            | `Defaults.UUID_REPRESENTATION`               |
| `MONGODB_DIRECT_CONNECTION`                 | Прямое соединение с указанным хостом                                | `None`                | `Defaults.DIRECT_CONNECTION`                 |
| `MONGODB_APPNAME`                           | Имя приложения для логов                                            | `None`                | `Defaults.APPNAME`                           |
| `MONGODB_READ_PREFERENCE`                   | Предпочтение чтения (primary, secondary и т.д.)                     | `None`                | `Defaults.READ_PREFERENCE`                   |
| `MONGODB_READ_PREFERENCE_TAGS`              | Набор тегов для предпочтения чтения                                 | `None`                | `Defaults.READ_PREFERENCE_TAGS`              |
| `MONGODB_MAX_STALENESS_SECONDS`             | Максимальное отставание репликации для чтения с вторичных узлов     | `None`                | `Defaults.MAX_STALENESS_SECONDS`             |
| `MONGODB_REPLICA_SET_NAME`                  | Имя набора реплик                                                   | `None`                | `Defaults.REPLICA_SET_NAME`                  |
| `MONGODB_AUTH_SOURCE`                       | База данных для аутентификации                                      | `admin`               | `Defaults.AUTH_SOURCE`                       |
| `MONGODB_AUTH_MECHANISM`                    | Механизм аутентификации                                             | `SCRAM-SHA-256`       | `Defaults.AUTH_MECHANISM`                    |
| `MONGODB_WRITE_CONCERN_W`                   | Уровень подтверждения записи (количество реплик)                    | `None`                | `Defaults.WRITE_CONCERN_W`                   |
| `MONGODB_JOURNAL`                           | Дожидаться записи в журнал                                          | `False`               | `Defaults.JOURNAL`                           |
| `MONGODB_FSYNC`                             | Дожидаться сброса записи на диск                                    | `False`               | `Defaults.FSYNC`                             |
| `MONGODB_READ_CONCERN_LEVEL`                | Уровень согласованности чтения                                      | `majority`            | `Defaults.READ_CONCERN_LEVEL`                |
| `MONGODB_SRV_SERVICE_NAME`                  | Имя службы для SRV-запросов                                         | `mongodb`             | `Defaults.SRV_SERVICE_NAME`                  |
| `MONGODB_SRV_MAX_HOSTS`                     | Максимальное количество хостов при использовании SRV                | `1`                   | `Defaults.SRV_MAX_HOSTS`                     |
| `MONGODB_UNICODE_DECODE_ERROR_HANDLER`      | Обработчик ошибок декодирования Unicode                             | `strict`              | `Defaults.UNICODE_DECODE_ERROR_HANDLE        |
