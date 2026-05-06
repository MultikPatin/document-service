import asyncio
import logging
import sys

from dishka import Provider, make_async_container

from src.adapters.database.mongo import MongoProvider
from src.container import ComponentsEnum, InitComponentProtocol


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)-7s | %(name)-16s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logging.getLogger("pymongo").setLevel(logging.INFO)


async def main() -> None:
    setup_logging()

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
