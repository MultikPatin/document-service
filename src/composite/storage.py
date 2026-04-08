import asyncio
import logging

from src.infrastructure.database.mongo.client import Client
from src.infrastructure.database.mongo.collections import collect_documents
from src.infrastructure.database.mongo.settings import Settings

logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    settings = Settings()
    client = Client(settings)
    documents = collect_documents()
    await client.init_beanie(documents)


if __name__ == "__main__":
    asyncio.run(main())
