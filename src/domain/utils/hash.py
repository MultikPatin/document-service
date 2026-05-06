import hashlib
import json

from src.domain.annotations import AnyMappingType, AnySequenceType


def hash_md5(
    instance: AnyMappingType | AnySequenceType, hex_digest: int = 24
) -> str:
    return hashlib.md5(  # noqa: S324
        json.dumps(instance, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()[:hex_digest]
