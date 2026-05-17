from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from bson.codec_options import DatetimeConversion

if TYPE_CHECKING:
    from bson.codec_options import TypeRegistry
    from pymongo.driver_info import DriverInfo
    from pymongo.encryption_options import AutoEncryptionOpts
    from pymongo.server_api import ServerApi

    from src.infra.mongo.annotations import QuerySortType

    from .annotations import (
        EventListenerType,
        ServerSelectorType,
    )


@dataclass(frozen=True, slots=True, eq=False, match_args=False)
class ClientContex:
    tz_aware: bool = False
    datetime_conversion: DatetimeConversion = DatetimeConversion.DATETIME
    document_class: type[Mapping[str, Any]] | None = None
    type_registry: TypeRegistry | None = None
    server_selector: ServerSelectorType = None
    driver: DriverInfo | None = None
    event_listeners: EventListenerType = field(default_factory=tuple)
    auto_encryption_opts: AutoEncryptionOpts | None = None
    server_api: ServerApi | None = None


@dataclass(frozen=True, slots=True, eq=False, match_args=False)
class InitBeanieContex:
    allow_index_dropping: bool = False
    recreate_views: bool = False
    skip_indexes: bool = False


@dataclass(frozen=True, slots=True, eq=False, match_args=False)
class PaginationQueryContex:
    sort: QuerySortType = None
    ignore_cache: bool = False
    fetch_links: bool = False
    with_children: bool = False
    lazy_parse: bool = False
    nesting_depth: int | None = None
    nesting_depths_per_field: dict[str, int] | None = None
    pymongo_kwargs: Mapping[str, Any] = field(default_factory=dict)
