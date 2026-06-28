"""CandidateEvent adapters for Research Brain."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.schemas import CandidateEvent, CandidateEventType, deterministic_id


def candidate_event_from_mapping(row: Mapping[str, Any], *, as_of_date: str | date | None = None) -> CandidateEvent:
    event_date = str(row.get("event_date") or row.get("as_of_date") or as_of_date or date.today().isoformat())
    symbol = str(row.get("symbol") or row.get("ticker") or row.get("company_name") or "UNKNOWN")
    company_name = str(row.get("company_name") or row.get("company") or symbol)
    reason_codes = tuple(str(item) for item in row.get("reason_codes") or ())
    event_type = _event_type_from_reason_codes(reason_codes, row)
    source_family = _source_family_from_path(str(row.get("candidate_source_path") or row.get("source_family") or "Manual"))
    source_id = str(row.get("source_id") or row.get("candidate_source_path") or row.get("evidence_ids") or symbol)
    payload = {
        "symbol": symbol,
        "company_name": company_name,
        "event_date": event_date,
        "event_type": event_type,
        "source_id": source_id,
    }
    return CandidateEvent(
        candidate_event_id=deterministic_id("CEVT", payload),
        symbol=symbol,
        company_name=company_name,
        event_date=event_date,
        event_type=event_type,
        source_family=source_family,
        source_id=source_id,
        magnitude={
            "cheap_scan_total_score": row.get("cheap_scan_total_score"),
            "price_event_score": row.get("price_event_score"),
            "disclosure_event_score": row.get("disclosure_event_score"),
            "financial_event_score": row.get("financial_event_score"),
            "risk_event_score": row.get("risk_event_score"),
        },
        freshness_days=0,
        candidate_reason=", ".join(reason_codes) or str(row.get("candidate_reason") or ""),
        initial_evidence_ids=tuple(str(item) for item in row.get("evidence_ids") or ()),
        structured_fields={key: value for key, value in row.items() if key not in {"reason_codes", "evidence_ids"}},
        price_context={},
        eligible_for_research_brain=bool(row.get("eligible_for_research_brain", True)),
    )


def load_candidate_events_from_korea_live_lite(
    *,
    candidates_path: str | Path,
    as_of_date: str | date | None = None,
) -> tuple[CandidateEvent, ...]:
    data = json.loads(Path(candidates_path).read_text(encoding="utf-8"))
    rows = data.get("candidates") if isinstance(data, Mapping) else data
    events = []
    for row in rows or ():
        if not isinstance(row, Mapping):
            continue
        if not row.get("production_candidate", True) or row.get("test_injected"):
            continue
        events.append(candidate_event_from_mapping(row, as_of_date=as_of_date))
    return tuple(events)


def _event_type_from_reason_codes(reason_codes: Sequence[str], row: Mapping[str, Any]) -> str:
    joined = " ".join(reason_codes).upper()
    if "SUPPLY_CONTRACT" in joined or "CONTRACT" in joined:
        return CandidateEventType.SUPPLY_CONTRACT.value
    if "FACILITY" in joined or "CAPA" in joined:
        return CandidateEventType.FACILITY_INVESTMENT.value
    if "FIN_" in joined or "TURNAROUND" in joined:
        return CandidateEventType.EARNINGS_SURPRISE.value
    if "RISK" in joined:
        return CandidateEventType.RISK_EVENT.value
    if "REPORT_RADAR" in joined:
        return CandidateEventType.REPORT_RADAR.value
    if "PRICE" in joined:
        return CandidateEventType.RELATIVE_STRENGTH.value
    return str(row.get("event_type") or CandidateEventType.OTHER.value)


def _source_family_from_path(value: str) -> str:
    lower = value.lower()
    if "dart" in lower or "official_cheap_scan" in lower:
        return "DART"
    if "kind" in lower:
        return "KIND"
    if "report_radar" in lower:
        return "ReportRadar"
    if "price" in lower:
        return "Price"
    return value or "Manual"


__all__ = ["candidate_event_from_mapping", "load_candidate_events_from_korea_live_lite"]
