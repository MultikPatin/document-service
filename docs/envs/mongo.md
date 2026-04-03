# Настройка MongoDB через переменные окружения

Для настройки подключения к MongoDB в приложении используются переменные окружения. Все переменные имеют префикс `MONGODB_` и соответствуют параметрам конфигурации клиента MongoDB.

## Переменные окружения

Все переменные окружения определяются в классе `_Settings` и используют значения по умолчанию из класса `_MongoDefaults`. Ниже приведена таблица всех доступных переменных.

| Переменная окружения | Описание | Значение по умолчанию | Константа в коде |
|------------------------|---------|------------------------|------------------|
| `MONGODB_HOST` | Хост MongoDB | `localhost` | `_MongoDefaults.HOST` |
| `MONGODB_PORT` | Порт MongoDB | `27017` | `_MongoDefaults.PORT` |
| `MONGODB_SCHEMA` | Схема подключения (mongodb или mongodb+srv) | `mongodb` | `_MongoDefaults.SCHEMA` |
| `MONGODB_USERNAME` | Имя пользователя для аутентификации | `None` | `_MongoDefaults.USERNAME` |
| `MONGODB_PASSWORD` | Пароль для аутентификации | `None` | `_MongoDefaults.PASSWORD` |
| `MONGODB_DATABASE` | Имя базы данных по умолчанию | `None` | `_MongoDefaults.DATABASE` |
| `MONGODB_MAX_POOL_SIZE` | Максимальное количество соединений в пуле | `None` | `_MongoDefaults.MAX_POOL_SIZE` |
| `MONGODB_MIN_POOL_SIZE` | Минимальное количество соединений в пуле | `None` | `_MongoDefaults.MIN_POOL_SIZE` |
| `MONGODB_MAX_IDLE_TIME_MS` | Максимальное время простоя соединения в миллисекундах | `None` | `_MongoDefaults.MAX_IDLE_TIME_MS` |
| `MONGODB_MAX_CONNECTING` | Максимальное количество одновременных соединений | `None` | `_MongoDefaults.MAX_CONNECTING` |
| `MONGODB_WAIT_QUEUE_TIMEOUT_MS` | Таймаут ожидания свободного соединения из пула | `None` | `_MongoDefaults.WAIT_QUEUE_TIMEOUT_MS` |
| `MONGODB_HEARTBEAT_FREQUENCY_MS` | Частота проверки состояния сервера | `None` | `_MongoDefaults.HEARTBEAT_FREQUENCY_MS` |
| `MONGODB_SERVER_MONITORING_MODE` | Режим мониторинга сервера | `None` | `_MongoDefaults.SERVER_MONITORING_MODE` |
| `MONGODB_CONNECT_TIMEOUT_MS` | Таймаут установки соединения | `20000` | `_MongoDefaults.CONNECT_TIMEOUT_MS` |
| `MONGODB_SOCKET_TIMEOUT_MS` | Таймаут сокета | `20000` | `_MongoDefaults.SOCKET_TIMEOUT_MS` |
| `MONGODB_SERVER_SELECTION_TIMEOUT_MS` | Таймаут выбора сервера | `30000` | `_MongoDefaults.SERVER_SELECTION_TIMEOUT_MS` |
| `MONGODB_TIMEOUT_MS` | Таймаут операции | `10000` | `_MongoDefaults.TIMEOUT_MS` |
| `MONGODB_RETRY_WRITES` | Включить повторные записывающие операции при ошибках сети | `True` | `_MongoDefaults.RETRY_WRITES` |
| `MONGODB_RETRY_READS` | Включить повторные читающие операции при ошибках сети | `True` | `_MongoDefaults.RETRY_READS` |
| `MONGODB_TLS` | Использовать TLS/SSL шифрование | `False` | `_MongoDefaults.TLS` |
| `MONGODB_TLS_INSECURE` | Разрешить недействительные сертификаты и несоответствие имён хостов | `False` | `_MongoDefaults.TLS_INSECURE` |
| `MONGODB_TLS_ALLOW_INVALID_CERTIFICATES` | Разрешить недействительные сертификаты | `False` | `_MongoDefaults.TLS_ALLOW_INVALID_CERTIFICATES` |
| `MONGODB_TLS_ALLOW_INVALID_HOSTNAMES` | Разрешить несоответствие имён хостов | `False` | `_MongoDefaults.TLS_ALLOW_INVALID_HOSTNAMES` |
| `MONGODB_TLS_CA_FILE` | Путь к сертификатам центра сертификации | `None` | `_MongoDefaults.TLS_CA_FILE` |
| `MONGODB_TLS_CERTIFICATE_KEY_FILE` | Путь к клиентскому сертификату | `None` | `_MongoDefaults.TLS_CERTIFICATE_KEY_FILE` |
| `MONGODB_TLS_CRL_FILE` | Путь к списку отозванных сертификатов | `None` | `_MongoDefaults.TLS_CRL_FILE` |
| `MONGODB_TLS_CERTIFICATE_KEY_FILE_PASSWORD` | Пароль для клиентского сертификата | `None` | `_MongoDefaults.TLS_CERTIFICATE_KEY_FILE_PASSWORD` |
| `MONGODB_TLS_DISABLE_OCSP_ENDPOINT_CHECK` | Отключить проверку OCSP endpoint | `False` | `_MongoDefaults.TLS_DISABLE_OCSP_ENDPOINT_CHECK` |
| `MONGODB_COMPRESSORS` | Список компрессоров (snappy, zlib, zstd) | `None` | `_MongoDefaults.COMPRESSORS` |
| `MONGODB_ZLIB_COMPRESSION_LEVEL` | Уровень сжатия zlib | `None` | `_MongoDefaults.ZLIB_COMPRESSION_LEVEL` |
| `MONGODB_UUID_REPRESENTATION` | Формат представления UUID | `standard` | `_MongoDefaults.UUID_REPRESENTATION` |
| `MONGODB_DIRECT_CONNECTION` | Прямое соединение с указанным хостом | `None` | `_MongoDefaults.DIRECT_CONNECTION` |
| `MONGODB_APPNAME` | Имя приложения для логов | `None` | `_MongoDefaults.APPNAME` |
| `MONGODB_READ_PREFERENCE` | Предпочтение чтения (primary, secondary и т.д.) | `None` | `_MongoDefaults.READ_PREFERENCE` |
| `MONGODB_READ_PREFERENCE_TAGS` | Набор тегов для предпочтения чтения | `None` | `_MongoDefaults.READ_PREFERENCE_TAGS` |
| `MONGODB_MAX_STALENESS_SECONDS` | Максимальное отставание репликации для чтения с вторичных узлов | `None` | `_MongoDefaults.MAX_STALENESS_SECONDS` |
| `MONGODB_REPLICA_SET_NAME` | Имя набора реплик | `None` | `_MongoDefaults.REPLICA_SET_NAME` |
| `MONGODB_AUTH_SOURCE` | База данных для аутентификации | `admin` | `_MongoDefaults.AUTH_SOURCE` |
| `MONGODB_AUTH_MECHANISM` | Механизм аутентификации | `SCRAM-SHA-256` | `_MongoDefaults.AUTH_MECHANISM` |
| `MONGODB_WRITE_CONCERN_W` | Уровень подтверждения записи (количество реплик) | `None` | `_MongoDefaults.WRITE_CONCERN_W` |
| `MONGODB_JOURNAL` | Дожидаться записи в журнал | `False` | `_MongoDefaults.JOURNAL` |
| `MONGODB_FSYNC` | Дожидаться сброса записи на диск | `False` | `_MongoDefaults.FSYNC` |
| `MONGODB_READ_CONCERN_LEVEL` | Уровень согласованности чтения | `majority` | `_MongoDefaults.READ_CONCERN_LEVEL` |
| `MONGODB_SRV_SERVICE_NAME` | Имя службы для SRV-запросов | `mongodb` | `_MongoDefaults.SRV_SERVICE_NAME` |
| `MONGODB_SRV_MAX_HOSTS` | Максимальное количество хостов при использовании SRV | `1` | `_MongoDefaults.SRV_MAX_HOSTS` |
| `MONGODB_UNICODE_DECODE_ERROR_HANDLER` | Обработчик ошибок декодирования Unicode | `strict` | `_MongoDefaults.UNICODE_DECODE_ERROR_HANDLER` |

## Префикс переменных окружения

Префикс `MONGODB_` для переменных окружения определён в атрибуте `ENV_PREFIX` класса `_MongoDefaults`.

## Значения по умолчанию

Все значения по умолчанию для параметров MongoDB определены в файле `src/infra/db/mongo/constants.py` в классе `_MongoDefaults`.