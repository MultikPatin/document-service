import sys
from inspect import getmembers, isclass
from typing import TYPE_CHECKING

from beanie import Document, UnionDoc, View

from .layouts import (
    LayoutBlockMessageDocument,
    LayoutBlockSingleDocument,
    LayoutBlockTableDocument,
    LayoutDocument,
    LayoutLayerDefaultDocument,
    LayoutLayerSchemaDocument,
    LayoutLayerValidationDocument,
)
from .reports import (
    ReportBlockSingleDocument,
    ReportBlockTableDocument,
    ReportDocument,
)

if TYPE_CHECKING:
    from src.infrastructure.mongo.annotations import DocumentsType

__all__ = [
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


_DOCUMENT_CLASSES = (Document, UnionDoc, View)
_DOCUMENT_CLASSES_NAMES = [d.__name__ for d in _DOCUMENT_CLASSES]


def collect_documents() -> DocumentsType:
    documents = []
    for _, doc in getmembers(sys.modules[__name__], isclass):
        if (
            issubclass(doc, _DOCUMENT_CLASSES)
            and doc.__name__ not in _DOCUMENT_CLASSES_NAMES
        ):
            documents.append(doc)

    return documents
