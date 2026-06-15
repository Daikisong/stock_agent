"""Common source connector errors, request metadata, and fixture helpers."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping

from e2r.models import Market, SourceTier


class SourceConnectorError(RuntimeError):
    """Base error raised by source collection connectors."""


class MissingCredentialError(SourceConnectorError):
    """Raised when a live request is attempted without required credentials."""


class SourceFixtureNotFoundError(SourceConnectorError):
    """Raised when fixture mode is requested but the fixture file is missing."""


class SourceResponseError(SourceConnectorError):
    """Raised when a source response cannot be normalized into E2R models."""


@dataclass(frozen=True)
class SourceRequest:
    """Serializable live-request plan.

    Connectors build these request objects without executing network calls.
    Tests can assert URL and params while fixture mode remains the default.
    """

    method: str
    url: str
    params: Mapping[str, Any] = field(default_factory=dict)
    headers: Mapping[str, str] = field(default_factory=dict)
    fixture_mode: bool = True
    credential_name: str | None = None

    def __post_init__(self) -> None:
        if self.method not in {"GET", "POST"}:
            raise ValueError("method must be GET or POST")
        if not self.url:
            raise ValueError("url must be non-empty")
        object.__setattr__(self, "params", dict(self.params))
        object.__setattr__(self, "headers", dict(self.headers))


def require_credential(value: str | None, credential_name: str) -> str:
    """Return a credential or raise a clear live-mode error."""

    if value is None or not str(value).strip():
        raise MissingCredentialError(f"{credential_name} is required for live source collection")
    return str(value)


def fixture_files(root: str | Path | None, stem: str) -> tuple[Path, ...]:
    """Find fallback CSV/JSON files for a source domain.

    Both flat and nested layouts are supported:

    - ``root/stem.csv``
    - ``root/stem.json``
    - ``root/stem/*.csv``
    - ``root/stem/*.json``
    """

    if root is None:
        return ()
    root_path = Path(root)
    candidates: list[Path] = []
    for suffix in (".csv", ".json"):
        flat = root_path / f"{stem}{suffix}"
        if flat.exists():
            candidates.append(flat)
    nested = root_path / stem
    if nested.exists():
        candidates.extend(sorted(nested.glob("*.csv")))
        candidates.extend(sorted(nested.glob("*.json")))
    return tuple(candidates)


def records_from_path(path: Path) -> tuple[dict[str, Any], ...]:
    """Load a CSV/JSON fixture file into dictionaries."""

    if path.suffix == ".csv":
        with path.open("r", encoding="utf-8", newline="") as handle:
            return tuple(dict(row) for row in csv.DictReader(handle))
    if path.suffix == ".json":
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if isinstance(payload, dict):
            for key in ("records", "items", "data"):
                if isinstance(payload.get(key), list):
                    return tuple(dict(row) for row in payload[key])
            return (dict(payload),)
        if not isinstance(payload, list):
            raise SourceResponseError(f"{path} must contain a JSON object or array")
        return tuple(dict(row) for row in payload)
    raise SourceResponseError(f"unsupported fixture file extension: {path}")


def load_fixture_records(root: str | Path | None, stem: str) -> tuple[dict[str, Any], ...]:
    """Load every flat/nested fixture file for one stem."""

    records: list[dict[str, Any]] = []
    for path in fixture_files(root, stem):
        records.extend(records_from_path(path))
    return tuple(records)


def blank_to_none(value: Any) -> Any:
    if value == "":
        return None
    return value


def text_or_none(value: Any) -> str | None:
    value = blank_to_none(value)
    if value is None:
        return None
    return str(value)


def float_or_none(value: Any) -> float | None:
    value = blank_to_none(value)
    if value is None:
        return None
    return float(str(value).replace(",", ""))


def int_or_none(value: Any) -> int | None:
    value = blank_to_none(value)
    if value is None:
        return None
    return int(float(str(value).replace(",", "")))


def bool_value(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None or value == "":
        return False
    if isinstance(value, (int, float)):
        return value != 0
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on", "있음", "예", "y"}


def date_value(value: Any) -> date:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip().replace(".", "-")
    if len(text) == 8 and text.isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:]}"
    match = re.match(r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})(?:\D|$)", text)
    if match:
        return date(int(match.group("year")), int(match.group("month")), int(match.group("day")))
    return date.fromisoformat(text[:10])


def datetime_value(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day)
    text = str(value).strip().replace(".", "-")
    if len(text) == 8 and text.isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:]}"
    if " " in text and "T" not in text:
        text = text.replace(" ", "T", 1)
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    return datetime.fromisoformat(text)


def mapping_value(value: Any) -> dict[str, Any]:
    value = blank_to_none(value)
    if value is None:
        return {}
    if isinstance(value, Mapping):
        return dict(value)
    parsed = json.loads(str(value))
    if not isinstance(parsed, dict):
        raise SourceResponseError("parsed_fields must decode to a JSON object")
    return parsed


def tuple_value(value: Any) -> tuple[str, ...]:
    value = blank_to_none(value)
    if value is None:
        return ()
    if isinstance(value, (tuple, list)):
        return tuple(str(item) for item in value)
    text = str(value).strip()
    if not text:
        return ()
    if text.startswith("["):
        parsed = json.loads(text)
        return tuple(str(item) for item in parsed)
    return tuple(item.strip() for item in text.split("|") if item.strip())


def coerce_jsonish(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text:
        return None
    lowered = text.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    try:
        if "." in text:
            return float(text.replace(",", ""))
        return int(text.replace(",", ""))
    except ValueError:
        return text


def parsed_fields_from_record(record: Mapping[str, Any], known_keys: set[str]) -> dict[str, Any]:
    parsed = mapping_value(record.get("parsed_fields"))
    for key, value in record.items():
        if key in known_keys or value in (None, ""):
            continue
        parsed[key] = coerce_jsonish(value)
    return parsed


def source_tier_value(value: Any, default: SourceTier = SourceTier.TIER_2) -> SourceTier:
    if value in (None, ""):
        return default
    if isinstance(value, SourceTier):
        return value
    return SourceTier(int(float(value)))


def market_value(value: Any, default: Market = Market.KR) -> Market:
    if value in (None, ""):
        return default
    if isinstance(value, Market):
        return value
    return Market(str(value))


def within_date_range(item_date: date, start: date, end: date, as_of_date: date) -> bool:
    """Return true when a dated record is visible for a point-in-time query."""

    return start <= item_date <= end and item_date <= as_of_date
