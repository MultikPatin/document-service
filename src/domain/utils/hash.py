import hashlib
import json

from src.domain.annotations import AnyMapping, AnySequence


def hash_md5(instance: AnyMapping | AnySequence, hex_digest: int = 24) -> str:
    return hashlib.md5(  # noqa: S324
        json.dumps(instance, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()[:hex_digest]
