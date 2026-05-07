from enum import StrEnum
from typing import Final, final


class RepresentationUuidEnum(StrEnum):
    standard = "standard"
    python_legacy = "pythonLegacy"
    java_legacy = "javaLegacy"
    csharp_legacy = "csharpLegacy"
    unspecified = "unspecified"


@final
class RepresentationDefaults:
    UUID: Final[RepresentationUuidEnum] = RepresentationUuidEnum.standard


@final
class RepresentationKeys:
    UUID: Final[str] = "uuidRepresentation"
