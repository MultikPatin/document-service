import asyncio
import logging

from libs.mongo.client import Client
from libs.mongo.constants.logger import LoggerNames

from src.adapters.database.mongo.documents import collect_documents
from src.adapters.database.mongo.settings import Settings

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pymongo").setLevel(logging.INFO)

init_logger = logging.getLogger(LoggerNames.init())


async def main() -> None:
    settings = Settings(logger=init_logger)
    client = Client(settings, init_logger)
    documents = collect_documents(init_logger)
    await client.init_beanie(documents)


if __name__ == "__main__":
    asyncio.run(main())
