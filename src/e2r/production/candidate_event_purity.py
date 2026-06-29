"""CandidateEvent production purity checks.

Easy example: ``005930`` may be a real Samsung Electronics symbol, but a row
coming from ``fixtures/historical/*`` is still not a production-live event.
The symbol and the source both have to be production-eligible.
"""

from __future__ import annotations

import csv
import re
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.calibration.taxonomy import LARGE_SECTOR_IDS


class ProductionMode(str, Enum):
    FROZEN_REPLAY = "frozen_replay"
    PRODUCTION_SHADOW = "production_shadow"
    PRODUCTION_SHADOW_LIVE = "production_shadow_live"
    PRODUCTION_LIVE = "production_live"
    PRODUCTION_LIVE_DRY_RUN = "production_live_dry_run"


_SYNTHETIC_SYMBOL_RE = re.compile(r"^(?:0{6}|1{6}|2{6}|3{6}|4{6}|5{6}|6{6}|TEST.*|SAMPLE.*)$", re.IGNORECASE)
_CACHED_OR_FIXTURE_MARKERS = (
    "fixtures/",
    "fixtures\\",
    "data/cache/",
    "data/cache\\",
    "data/raw/korea_cheap_scan/",
    "data/raw/korea_cheap_scan\\",
    "data/raw/search_html/",
    "data/raw/search_html\\",
    "data/raw/report_search/",
    "data/raw/report_search\\",
    "data/raw/naver_webdoc/",
    "data/raw/naver_webdoc\\",
    "data/raw/naver_news/",
    "data/raw/naver_news\\",
)
_VERIFIED_SOURCE_FAMILIES = frozenset(
    {
        "DART",
        "OpenDART",
        "KIND",
        "KRX",
        "CompanyGuide",
        "IR",
        "IssuerIR",
        "IssuerOfficial",
        "TrustedNews",
        "Report",
        "ResearchReport",
    }
)


@dataclass(frozen=True)
class InstrumentRegistry:
    symbols: frozenset[str]
    names_by_symbol: Mapping[str, str]
    official_krx_universe_count: int
    combined_registry_count: int
    source_paths: tuple[str, ...]


@dataclass(frozen=True)
class CandidateEventProductionEligibility:
    candidate_event_id: str
    symbol: str
    company_name: str
    eligible: bool
    mode: str
    reasons: tuple[str, ...]
    fixture_like_symbol: bool
    source_id_cached_or_fixture: bool
    source_id_fixture: bool
    source_id_snapshot_uri: bool
    symbol_in_registry: bool
    company_name_matches_registry: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_instrument_registry(repo_root: str | Path = ".") -> InstrumentRegistry:
    root = Path(repo_root)
    rows: list[tuple[str, str, str, bool]] = []
    source_paths: list[str] = []
    official_paths = tuple(root.glob("data/raw/krx/instruments/*.csv")) + (
        root / "data/historical_official/universe/universe.csv",
    )
    for path in official_paths:
        if path.exists():
            source_paths.append(str(path))
            rows.extend(_instrument_rows(path, official=True))
    for path in sorted((root / "data/cache/company_guide").glob("*/*_recent_reports.json")):
        # CompanyGuide cache is useful as an alias source, but it is not counted
        # as the official KRX universe size for cutover readiness.
        symbol = path.name.split("_", 1)[0]
        rows.append((symbol, symbol, str(path), False))
    official_symbols = {symbol for symbol, _name, _path, official in rows if official and _valid_symbol(symbol)}
    names: dict[str, str] = {}
    for symbol, name, _path, _official in rows:
        if not _valid_symbol(symbol):
            continue
        if name and symbol not in names:
            names[symbol] = name
    return InstrumentRegistry(
        symbols=frozenset(names),
        names_by_symbol=names,
        official_krx_universe_count=len(official_symbols),
        combined_registry_count=len(names),
        source_paths=tuple(source_paths),
    )


def evaluate_candidate_event_production_eligibility(
    event: Mapping[str, Any] | Any,
    *,
    registry: InstrumentRegistry | None = None,
    mode: str | ProductionMode = ProductionMode.PRODUCTION_SHADOW_LIVE,
    repo_root: str | Path = ".",
    as_of_date: str | None = None,
) -> CandidateEventProductionEligibility:
    registry = registry or load_instrument_registry(repo_root)
    normalized_mode = _production_mode(mode)
    data = _event_to_mapping(event)
    symbol = str(data.get("symbol") or "")
    company_name = str(data.get("company_name") or "")
    source_id = str(data.get("source_id") or data.get("event_source") or "")
    candidate_event_id = str(data.get("candidate_event_id") or f"candidate:{symbol}:{source_id}")
    reasons: list[str] = []
    fixture_like_symbol = bool(_SYNTHETIC_SYMBOL_RE.match(symbol))
    source_id_cached_or_fixture = _is_cached_or_fixture_source_id(source_id)
    source_id_fixture = "fixtures/" in source_id.replace("\\", "/")
    source_id_snapshot_uri = source_id.startswith("snapshot://")
    symbol_in_registry = symbol in registry.symbols
    registry_name = registry.names_by_symbol.get(symbol)
    company_name_matches_registry = bool(
        symbol_in_registry
        and (
            not company_name
            or not registry_name
            or _normalize_name(company_name) == _normalize_name(registry_name)
            or _normalize_name(company_name) in _normalize_name(registry_name)
            or _normalize_name(registry_name) in _normalize_name(company_name)
        )
    )
    event_date = str(data.get("event_date") or "")
    detected_at = str(data.get("detected_at") or "")
    source_family = str(data.get("source_family") or "")
    if fixture_like_symbol:
        reasons.append("fixture_like_symbol")
    if not symbol_in_registry:
        reasons.append("symbol_not_in_instrument_registry")
    if symbol_in_registry and not company_name_matches_registry:
        reasons.append("company_name_mismatch")
    if not detected_at:
        reasons.append("missing_detected_at")
    if not event_date:
        reasons.append("missing_event_date")
    if as_of_date and event_date and event_date > as_of_date:
        reasons.append("event_date_after_as_of_date")
    if not source_family:
        reasons.append("missing_source_family")
    elif source_family not in _VERIFIED_SOURCE_FAMILIES:
        reasons.append("unverified_source_family")
    if not source_id:
        reasons.append("missing_source_id")
    if normalized_mode != ProductionMode.FROZEN_REPLAY and source_id_fixture:
        reasons.append("fixture_source_forbidden_in_production")
    if normalized_mode != ProductionMode.FROZEN_REPLAY and source_id_cached_or_fixture:
        reasons.append("cached_or_fixture_path_forbidden_in_production")
    if normalized_mode != ProductionMode.FROZEN_REPLAY and source_id_snapshot_uri:
        reasons.append("snapshot_uri_not_live_source")
    return CandidateEventProductionEligibility(
        candidate_event_id=candidate_event_id,
        symbol=symbol,
        company_name=company_name,
        eligible=not reasons,
        mode=normalized_mode.value,
        reasons=tuple(dict.fromkeys(reasons)),
        fixture_like_symbol=fixture_like_symbol,
        source_id_cached_or_fixture=source_id_cached_or_fixture,
        source_id_fixture=source_id_fixture,
        source_id_snapshot_uri=source_id_snapshot_uri,
        symbol_in_registry=symbol_in_registry,
        company_name_matches_registry=company_name_matches_registry,
    )


def build_candidate_purity_report(
    events: Sequence[Mapping[str, Any] | Any],
    *,
    mode: str | ProductionMode,
    repo_root: str | Path = ".",
    as_of_date: str | None = None,
    registry: InstrumentRegistry | None = None,
) -> Mapping[str, Any]:
    registry = registry or load_instrument_registry(repo_root)
    normalized_mode = _production_mode(mode)
    rows = [
        evaluate_candidate_event_production_eligibility(
            event,
            registry=registry,
            mode=mode,
            repo_root=repo_root,
            as_of_date=as_of_date,
        ).to_dict()
        for event in events
    ]
    production_rows = [row for row in rows if row["eligible"]]
    fixture_rows = [row for row in rows if row["fixture_like_symbol"] or row["source_id_fixture"]]
    cached_rows = [row for row in rows if row["source_id_cached_or_fixture"]]
    sector_coverage = _sector_coverage(events, rows)
    return {
        "schema_version": "production_cutover_candidate_purity_v1",
        "summary": {
            "mode": normalized_mode.value,
            "actual_krx_universe_count": registry.official_krx_universe_count,
            "combined_registry_count": registry.combined_registry_count,
            "total_candidate_event_count": len(rows),
            "production_candidate_event_count": len(production_rows),
            "production_eligible_candidate_event_count": len(production_rows),
            "fixture_candidate_event_count": len(fixture_rows),
            "fixture_candidate_event_count_in_production": 0
            if normalized_mode == ProductionMode.FROZEN_REPLAY
            else len(fixture_rows),
            "cached_path_count": len(cached_rows),
            "cached_fixture_source_count": len(cached_rows),
            "snapshot_uri_source_count": sum(1 for row in rows if row["source_id_snapshot_uri"]),
            "company_name_mismatch_count": sum("company_name_mismatch" in row["reasons"] for row in rows),
            "symbol_not_in_registry_count": sum("symbol_not_in_instrument_registry" in row["reasons"] for row in rows),
            "sector_coverage": sector_coverage,
            "active_large_sector_count": sector_coverage["summary"]["active_large_sector_count"],
            "unknown_sector_candidate_count": sector_coverage["summary"]["unknown_sector_candidate_count"],
        },
        "registry": {
            "source_paths": list(registry.source_paths),
        },
        "rows": rows,
    }


def _sector_coverage(events: Sequence[Mapping[str, Any] | Any], rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    coverage: dict[str, dict[str, Any]] = {
        sector: {
            "candidate_attempt_count": 0,
            "production_eligible_candidate_count": 0,
            "source_gap": "no_candidate_attempt_in_current_daily_scan",
            "sample_symbols": [],
            "classification_sources": [],
        }
        for sector in LARGE_SECTOR_IDS
    }
    unknown = {
        "candidate_attempt_count": 0,
        "production_eligible_candidate_count": 0,
        "source_gap": "sector_classification_provider_missing_or_unmapped",
        "sample_symbols": [],
        "classification_sources": [],
    }
    for event, row in zip(events, rows):
        data = _event_to_mapping(event)
        sector = str(data.get("large_sector_id") or "")
        bucket = coverage.get(sector)
        if bucket is None:
            bucket = unknown
        bucket["candidate_attempt_count"] += 1
        if row.get("eligible"):
            bucket["production_eligible_candidate_count"] += 1
        if len(bucket["sample_symbols"]) < 10:
            bucket["sample_symbols"].append(str(data.get("symbol") or row.get("symbol") or ""))
        source = str(data.get("sector_classification_source") or "")
        if source and source not in bucket["classification_sources"]:
            bucket["classification_sources"].append(source)
        if bucket is not unknown:
            bucket["source_gap"] = None
    active = {
        sector: value
        for sector, value in coverage.items()
        if int(value["candidate_attempt_count"]) > 0
    }
    inactive = {
        sector: value
        for sector, value in coverage.items()
        if int(value["candidate_attempt_count"]) == 0
    }
    payload: dict[str, Any] = {
        "summary": {
            "large_sector_total": len(LARGE_SECTOR_IDS),
            "active_large_sector_count": len(active),
            "inactive_large_sector_count": len(inactive),
            "unknown_sector_candidate_count": unknown["candidate_attempt_count"],
        },
        "active": active,
        "inactive": inactive,
    }
    if unknown["candidate_attempt_count"]:
        payload["unknown"] = unknown
    return payload


def _instrument_rows(path: Path, *, official: bool) -> Iterable[tuple[str, str, str, bool]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            symbol = str(row.get("symbol") or row.get("ticker") or "").strip()
            name = str(row.get("name") or row.get("company_name") or row.get("company") or symbol).strip()
            if symbol:
                yield symbol, name, str(path), official


def _event_to_mapping(event: Mapping[str, Any] | Any) -> Mapping[str, Any]:
    if isinstance(event, Mapping):
        return event
    if hasattr(event, "to_dict"):
        return event.to_dict()
    return {key: getattr(event, key) for key in dir(event) if not key.startswith("_") and not callable(getattr(event, key))}


def _valid_symbol(symbol: str) -> bool:
    return bool(symbol) and not _SYNTHETIC_SYMBOL_RE.match(symbol)


def _is_cached_or_fixture_source_id(source_id: str) -> bool:
    normalized = source_id.replace("\\", "/")
    return normalized.startswith("snapshot://") or any(marker in normalized for marker in _CACHED_OR_FIXTURE_MARKERS)


def _normalize_name(value: str) -> str:
    return re.sub(r"\s+", "", value).lower()


def _production_mode(mode: str | ProductionMode) -> ProductionMode:
    if isinstance(mode, ProductionMode):
        return mode
    return ProductionMode(str(mode))


__all__ = [
    "CandidateEventProductionEligibility",
    "InstrumentRegistry",
    "ProductionMode",
    "build_candidate_purity_report",
    "evaluate_candidate_event_production_eligibility",
    "load_instrument_registry",
]
