from libs.core.enums import ComponentsEnum

from .client import ClientProvider
from .layout import LayoutBlcokProvider, LayoutLayerProvider, LayoutProvider
from .report import ReportBlockProvider, ReportProvider


class MongoProvider(
    ClientProvider,
    LayoutBlcokProvider,
    LayoutLayerProvider,
    LayoutProvider,
    ReportBlockProvider,
    ReportProvider,
):
    component = ComponentsEnum.mongo
