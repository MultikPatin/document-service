import asyncio
import logging

from dishka import Provider, make_async_container

from src.adapters.database.mongo import MongoProvider
from src.core.enums import ComponentsEnum
from src.core.protocols import InitComponentProtocol

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pymongo").setLevel(logging.INFO)


async def main() -> None:
    providers: list[Provider] = [
        MongoProvider(),
    ]

    container = make_async_container(*providers)
    try:
        await container.get(
            InitComponentProtocol, component=ComponentsEnum.mongo
        )
    except Exception as e:
        print(e)  # noqa: T201
    finally:
        await container.close()


if __name__ == "__main__":
    asyncio.run(main())
