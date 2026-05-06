from enum import StrEnum, auto


class ComponentsEnum(StrEnum):
    fastapi = auto()
    redis = auto()
    mongo = auto()
    elasticsearch = auto()
    postgres = auto()
    clickhouse = auto()
    minio = auto()
    faststream = auto()
    rabbitmq = auto()
    kafka = auto()
    litestar = auto()
    falcon = auto()
