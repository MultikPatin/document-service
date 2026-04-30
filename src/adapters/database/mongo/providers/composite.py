from libs.core.enums import ComponentsEnum

from .client import ClientProvider
from .layout import LayoutBlockProvider, LayoutLayerProvider, LayoutProvider
from .report import ReportBlockProvider, ReportProvider


class MongoProvider(
    ClientProvider,
    LayoutBlockProvider,
    LayoutLayerProvider,
    LayoutProvider,
    ReportBlockProvider,
    ReportProvider,
):
    component = ComponentsEnum.mongo
