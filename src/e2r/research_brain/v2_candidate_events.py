"""CandidateEventV2 adapters and dry-run helpers."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import LARGE_SECTOR_IDS
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.research_brain.v2_schemas import CandidateEventV2, EventMagnitudeV2, deterministic_event_id_v2


_EVENT_FAMILY_RULES = (
    ("DISC_SUPPLY_CONTRACT", "supply_contract"),
    ("DISC_FACILITY_INVESTMENT", "facility_investment"),
    ("DISC_EARNINGS_PREANNOUNCE", "earnings_preannounce"),
    ("FIN_", "earnings_actual"),
    ("REPORT_RADAR", "report_radar"),
    ("PRICE_", "price_relative_strength"),
    ("DISC_LAWSUIT", "risk_event"),
    ("DISC_DELISTING_RISK", "risk_event"),
    ("DISC_TRADING_HALT", "risk_event"),
    ("DISC_BUYBACK_OR_CANCELLATION", "capital_return"),
)


def candidate_events_v2_from_mapping(row: Mapping[str, Any], *, detected_at: str | None = None) -> tuple[CandidateEventV2, ...]:
    reason_codes = tuple(str(item) for item in row.get("reason_codes") or ())
    event_families = _event_families(reason_codes, row)
    events = []
    for event_type, event_reason_codes in event_families:
        events.append(_event_from_row(row, event_type=event_type, reason_codes=event_reason_codes, detected_at=detected_at))
    return tuple(events)


def load_candidate_events_v2_from_file(
    path: str | Path,
    *,
    detected_at: str | None = None,
    limit: int | None = None,
) -> tuple[CandidateEventV2, ...]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = data.get("candidates") if isinstance(data, Mapping) else data
    events = []
    for row in rows or ():
        if not isinstance(row, Mapping):
            continue
        if not row.get("production_candidate", True) or row.get("test_injected"):
            continue
        events.extend(candidate_events_v2_from_mapping(row, detected_at=detected_at))
        if limit is not None and len(events) >= limit:
            break
    return tuple(events[:limit] if limit is not None else events)


def cluster_candidate_events_v2(events: Sequence[CandidateEventV2]) -> Mapping[str, Any]:
    clusters: dict[str, list[CandidateEventV2]] = defaultdict(list)
    for event in events:
        key = "|".join([event.symbol, event.event_date, event.source_family])
        clusters[key].append(event)
    rows = []
    for key, grouped in sorted(clusters.items()):
        rows.append(
            {
                "cluster_id": deterministic_event_id_v2(key),
                "symbol": grouped[0].symbol,
                "company_name": grouped[0].company_name,
                "event_date": grouped[0].event_date,
                "source_family": grouped[0].source_family,
                "event_count": len(grouped),
                "event_types": sorted({event.event_type for event in grouped}),
                "event_ids": [event.candidate_event_id for event in grouped],
                "source_strength_score": sum(bool(event.initial_evidence_document_ids) for event in grouped),
                "freshness_score": max(0, 100 - min(event.event_freshness_days for event in grouped)),
            }
        )
    return {
        "schema_version": "research_brain_v2_candidate_cluster_report",
        "summary": {
            "cluster_count": len(rows),
            "event_count": len(events),
            "multi_event_cluster_count": sum(row["event_count"] > 1 for row in rows),
        },
        "rows": rows,
    }


def candidate_event_dry_run_report(events: Sequence[CandidateEventV2], routed_rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    sectors = Counter()
    for row in routed_rows:
        archetype_id = row.get("primary_archetype")
        if archetype_id:
            sector = large_sector_for_archetype(str(archetype_id))
            if sector:
                sectors[sector] += 1
    sector_rows = [
        {
            "large_sector_id": sector_id,
            "candidate_event_attempt_count": sectors.get(sector_id, 0),
            "required_attempt_count": 3,
            "status": "pass" if sectors.get(sector_id, 0) >= 3 else "provider_or_source_gap",
        }
        for sector_id in LARGE_SECTOR_IDS
    ]
    provider_or_source_gaps = [row for row in sector_rows if row["status"] != "pass"]
    return {
        "schema_version": "research_brain_v2_candidate_event_dry_run",
        "summary": {
            "candidate_event_count": len(events),
            "event_type_breakdown": dict(Counter(event.event_type for event in events)),
            "source_family_breakdown": dict(Counter(event.source_family for event in events)),
            "event_with_initial_evidence_count": sum(bool(event.initial_evidence_document_ids) for event in events),
            "sector_coverage": dict(sectors),
            "sector_coverage_count": len(sectors),
            "sector_gap_count": len(provider_or_source_gaps),
            "targeted_smoke_only": False,
        },
        "sector_rows": sector_rows,
        "provider_or_source_gaps": provider_or_source_gaps,
        "rows": [event.to_dict() for event in events],
    }


def render_candidate_event_schema_markdown() -> str:
    return "\n".join(
        [
            "# Research Brain v2 CandidateEventV2 Schema",
            "",
            "CandidateEventV2는 종목 row가 아니라 사건 row다.",
            "",
            "쉬운 예: 한 종목에 공급계약, 신규시설투자, 가격 급등이 동시에 있으면 하나의 종목 후보가 아니라 "
            "`supply_contract`, `facility_investment`, `price_relative_strength` 세 사건으로 나눈다.",
            "",
            "## Required Fields",
            "",
            "- `candidate_event_id`: deterministic hash id",
            "- `symbol`, `company_name`",
            "- `event_date`, `detected_at`",
            "- `source_family`, `source_id`",
            "- `event_type`, `raw_reason_codes`",
            "- `event_title`, `event_summary`",
            "- `magnitude`",
            "- `issuer_directness`",
            "- `initial_evidence_document_ids`",
            "- `structured_payload`, `price_context`",
            "",
            "Research Brain은 이 event를 라우팅하고 조사 task를 만들 수 있지만, score/stage를 직접 확정하지 않는다.",
            "",
        ]
    )


def _event_from_row(
    row: Mapping[str, Any],
    *,
    event_type: str,
    reason_codes: Sequence[str],
    detected_at: str | None,
) -> CandidateEventV2:
    event_date = str(row.get("event_date") or row.get("as_of_date") or detected_at or date.today().isoformat())
    detected = str(detected_at or row.get("detected_at") or row.get("as_of_date") or event_date)
    symbol = str(row.get("symbol") or row.get("ticker") or row.get("company_name") or "UNKNOWN")
    company_name = str(row.get("company_name") or row.get("company") or symbol)
    source_family = _source_family(row)
    source_id = str(row.get("source_id") or row.get("candidate_source_path") or symbol)
    payload = {
        "symbol": symbol,
        "company_name": company_name,
        "event_date": event_date,
        "event_type": event_type,
        "reason_codes": tuple(reason_codes),
        "source_id": source_id,
    }
    summary = _event_summary(row, event_type, reason_codes)
    return CandidateEventV2(
        candidate_event_id=deterministic_event_id_v2(payload),
        symbol=symbol,
        company_name=company_name,
        event_date=event_date,
        detected_at=detected,
        source_family=source_family,
        source_id=source_id,
        event_type=event_type,
        raw_reason_codes=tuple(reason_codes),
        primary_disclosure_type=_primary_disclosure_type(reason_codes),
        event_title=summary,
        event_summary=summary,
        magnitude=EventMagnitudeV2(
            relative_strength_rank=_float_or_none(row.get("rank")),
            volume_spike_ratio=_float_or_none(row.get("price_event_score")),
        ),
        event_freshness_days=_freshness_days(event_date, detected),
        issuer_directness="DIRECT" if source_family in {"DART", "KIND", "KRX", "IR", "Official"} else "UNKNOWN",
        initial_evidence_document_ids=tuple(str(item) for item in row.get("evidence_ids") or ()),
        structured_payload={key: value for key, value in row.items() if key not in {"evidence_ids"}},
        price_context={
            "cheap_scan_total_score": row.get("cheap_scan_total_score") or row.get("score") or row.get("merged_score"),
            "price_event_score": row.get("price_event_score"),
            "merged_stage": row.get("merged_stage"),
            "score_valid": row.get("score_valid"),
        },
        research_brain_eligible=bool(row.get("eligible_for_research_brain", True)),
    )


def _event_families(reason_codes: Sequence[str], row: Mapping[str, Any]) -> tuple[tuple[str, tuple[str, ...]], ...]:
    grouped: dict[str, list[str]] = {}
    for code in reason_codes:
        event_type = _event_type_for_reason(code)
        grouped.setdefault(event_type, []).append(code)
    if not grouped:
        grouped[str(row.get("event_type") or "other")] = []
    return tuple((event_type, tuple(codes)) for event_type, codes in sorted(grouped.items()))


def _event_type_for_reason(code: str) -> str:
    upper = code.upper()
    for prefix, event_type in _EVENT_FAMILY_RULES:
        if upper.startswith(prefix) or prefix in upper:
            return event_type
    return "other"


def _source_family(row: Mapping[str, Any]) -> str:
    value = str(row.get("source_family") or row.get("candidate_source_path") or "Manual")
    lower = value.lower()
    if "dart" in lower or "official_cheap_scan" in lower:
        return "DART"
    if "kind" in lower:
        return "KIND"
    if "krx" in lower:
        return "KRX"
    if "report" in lower:
        return "ReportRadar"
    if "price" in lower:
        return "Price"
    return value


def _primary_disclosure_type(reason_codes: Sequence[str]) -> str | None:
    for code in reason_codes:
        if code.startswith("DISC_"):
            return code
    return None


def _event_summary(row: Mapping[str, Any], event_type: str, reason_codes: Sequence[str]) -> str:
    company = str(row.get("company_name") or row.get("symbol") or "candidate")
    return f"{company} {event_type} event from {', '.join(reason_codes) or 'source row'}"


def _freshness_days(event_date: str, detected_at: str) -> int:
    try:
        event = datetime.fromisoformat(event_date[:10]).date()
        detected = datetime.fromisoformat(detected_at[:10]).date()
    except ValueError:
        return 0
    return max(0, (detected - event).days)


def _float_or_none(value: Any) -> float | None:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


__all__ = [
    "candidate_event_dry_run_report",
    "candidate_events_v2_from_mapping",
    "cluster_candidate_events_v2",
    "load_candidate_events_v2_from_file",
    "render_candidate_event_schema_markdown",
]
