from src.domain.constants import ComponentsEnum

from .client import ClientProvider
from .layout import LayoutProvider
from .report import ReportProvider


class MongoProvider(ClientProvider, LayoutProvider, ReportProvider):
    component = ComponentsEnum.mongo
