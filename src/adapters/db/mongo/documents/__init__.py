import sys
from collections.abc import Sequence

from beanie import Document, UnionDoc, View

# Import documents
# from .documents import (
#     InputDocument,
# )
#
# __all__ = [
#     "InputDocument",
# ]

type DocumentsType = Sequence[type[Document] | type[UnionDoc] | type[View]]

DOCUMENT_CLASSES = Document | UnionDoc | View
DOCUMENT_CLASSES_NAMES = (Document.__name__, UnionDoc.__name__, View.__name__)


def collect_documents() -> DocumentsType:
    """Collects all document classes defined in the current module.

    This function scans the current module's namespace and returns all classes
    that inherit from Document, UnionDoc, or View (Beanie ODM base classes),
    excluding the base classes themselves.

    The function is typically used to automatically discover and register
    all document models in the application without manual registration.

    Returns:
        DocumentsType: A sequence of document classes that can be used for
                       Beanie ODM initialization. The sequence contains classes
                       that inherit from Document, UnionDoc, or View but are not
                       the base classes themselves.

    Example:
        >>> docs = collect_documents()
        >>> print([doc.__name__ for doc in docs])
        ['InputDocument', 'OutputDocument']

    Note:
        This function only discovers classes defined in the current module
        (__init__.py). Make sure all document classes are imported and available
        in the module's namespace when this function is called.
    """
    from inspect import getmembers, isclass  # noqa: PLC0415

    return [
        doc
        for _, doc in getmembers(sys.modules[__name__], isclass)
        if issubclass(doc, DOCUMENT_CLASSES)
        and doc.__name__ not in DOCUMENT_CLASSES_NAMES
    ]
