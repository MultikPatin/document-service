import sys
from collections.abc import Sequence
from inspect import getmembers, isclass
from typing import TYPE_CHECKING

from beanie import Document, UnionDoc, View

if TYPE_CHECKING:
    from logging import Logger

from .layout import (
    LayoutBlockCardDocument,
    LayoutBlockMessageDocument,
    LayoutBlockSingleDocument,
    LayoutBlockTableDocument,
    LayoutDocument,
    LayoutLayerDefaultDocument,
    LayoutLayerSchemaDocument,
    LayoutLayerValidationDocument,
)
from .report import (
    ReportBlockSingleDocument,
    ReportBlockTableDocument,
    ReportDocument,
)

__all__ = [
    "LayoutBlockCardDocument",
    "LayoutBlockMessageDocument",
    "LayoutBlockSingleDocument",
    "LayoutBlockTableDocument",
    "LayoutDocument",
    "LayoutLayerDefaultDocument",
    "LayoutLayerSchemaDocument",
    "LayoutLayerValidationDocument",
    "ReportBlockSingleDocument",
    "ReportBlockTableDocument",
    "ReportDocument",
    "collect_documents",
]

type CollectedDocumentsType = Sequence[type[Document | UnionDoc | View]]

_DOCUMENT_CLASSES = (Document, UnionDoc, View)
_DOCUMENT_CLASSES_NAMES = (Document.__name__, UnionDoc.__name__, View.__name__)


def collect_documents(logger: Logger) -> CollectedDocumentsType:
    """Collects all document classes defined in the current module.

    This function scans the current module's namespace and returns all classes
    that inherit from Document, UnionDoc, or View (Beanie ODM base classes),
    excluding the base classes themselves.

    The function is typically used to automatically discover and register
    all document models in the application without manual registration.

    Note:
        This function only discovers classes defined in the current module
        (__init__.py). Make sure all document classes are imported and available
        in the module's namespace when this function is called.
    """
    logger.info("Collecting documents...")

    documents = []
    for _, doc in getmembers(sys.modules[__name__], isclass):
        if (
            issubclass(doc, _DOCUMENT_CLASSES)
            and doc.__name__ not in _DOCUMENT_CLASSES_NAMES
        ):
            documents.append(doc)
            logger.debug("Collect document: %s", doc.__name__)

    logger.info("Collecting documents completed successfully")

    return documents
