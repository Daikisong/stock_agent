"""Stable identities and hashes for Pro-first artifacts."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def stable_id(prefix: str, payload: Mapping[str, Any], *, length: int = 24) -> str:
    normalized = prefix.strip().upper()
    if not normalized or not normalized.replace("_", "").isalnum():
        raise ValueError("stable id prefix must be alphanumeric")
    if not 8 <= length <= 64:
        raise ValueError("stable id hash length must be between 8 and 64")
    return f"{normalized}-{canonical_hash(payload)[:length]}"


__all__ = ["canonical_hash", "canonical_json", "stable_id"]
