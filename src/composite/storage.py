import asyncio
import logging

from src.infra.db.mongo.client import Client
from src.infra.db.mongo.docs import collect_documents
from src.infra.db.mongo.settings import Settings

logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    settings = Settings()
    client = Client(settings)
    documents = collect_documents()
    await client.init_beanie(documents)


if __name__ == "__main__":
    asyncio.run(main())
