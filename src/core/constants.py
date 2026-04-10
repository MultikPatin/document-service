from typing import Final, final


@final
class PostgresDefaults:
    ENV_PREFIX: Final[str] = "POSTGRES_"
    PORT: Final[int] = 5432
    SCHEMA: Final[str] = "postgresql"
