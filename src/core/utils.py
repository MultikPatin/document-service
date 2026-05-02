import hashlib
import json
from typing import Any


def get_md5hash(
    instance: dict[str, Any] | list[Any], hex_digest: int = 24
) -> str:
    return hashlib.md5(  # noqa: S324
        json.dumps(instance, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()[:hex_digest]


def get_sha256hash(
    instance: dict[str, Any] | list[Any], hex_digest: int = 24
) -> str:
    return hashlib.sha256(
        json.dumps(instance, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()[:hex_digest]
