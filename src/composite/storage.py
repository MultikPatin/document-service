import asyncio
import logging

from src.infrastructure.database.mongo.client import Client
from src.infrastructure.database.mongo.documents import collect_documents
from src.infrastructure.database.mongo.logger import LoggerNames
from src.infrastructure.database.mongo.settings import Settings

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pymongo").setLevel(logging.INFO)

init_logger = logging.getLogger(LoggerNames.init())


async def main() -> None:
    settings = Settings()
    client = Client(settings, init_logger)
    documents = collect_documents(init_logger)
    await client.init_beanie(documents)


if __name__ == "__main__":
    asyncio.run(main())
