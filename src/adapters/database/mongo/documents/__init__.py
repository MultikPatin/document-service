import sys
from collections.abc import Sequence
from inspect import getmembers, isclass

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

type CollectedDocumentsType = Sequence[type[Document | UnionDoc | View]]

_DOCUMENT_CLASSES = (Document, UnionDoc, View)
_DOCUMENT_CLASSES_NAMES = [d.__name__ for d in _DOCUMENT_CLASSES]


def collect_documents() -> CollectedDocumentsType:
    documents = []
    for _, doc in getmembers(sys.modules[__name__], isclass):
        if (
            issubclass(doc, _DOCUMENT_CLASSES)
            and doc.__name__ not in _DOCUMENT_CLASSES_NAMES
        ):
            documents.append(doc)

    return documents
