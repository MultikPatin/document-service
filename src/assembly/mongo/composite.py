from src.assembly.enums import ComponentsEnum

from .client import ClientProvider
from .layout import Layout
from .report import ReportProvider


class MongoProvider(ClientProvider, Layout, ReportProvider):
    component = ComponentsEnum.mongo
