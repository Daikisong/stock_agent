"""Raw market-event routing fixture evaluation for Research Brain v3."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.schemas import deterministic_id
from e2r.research_brain.v2_schemas import CandidateEventV2, EventMagnitudeV2
from e2r.research_brain.v3_llm_planner_provider import ResearchBrainPlannerProvider, run_planner_provider_v3
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard


DEFAULT_RAW_ROUTING_FIXTURE_DIR = Path("fixtures/research_brain_v3/raw_event_routing")
MANDATORY_RAW_ARCHETYPES = {
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
}


def load_raw_event_routing_fixtures(path: str | Path = DEFAULT_RAW_ROUTING_FIXTURE_DIR) -> tuple[Mapping[str, Any], ...]:
    root = Path(path)
    files = sorted(root.glob("*.jsonl")) if root.is_dir() else [root]
    rows: list[Mapping[str, Any]] = []
    for file_path in files:
        for line_number, line in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            row = dict(row)
            row.setdefault("fixture_id", f"{file_path.stem}:{line_number}")
            rows.append(row)
    return tuple(rows)


def raw_fixture_to_event(row: Mapping[str, Any]) -> CandidateEventV2:
    event_summary = str(row.get("event_summary") or row.get("raw_event_text") or "")
    event_title = str(row.get("event_title") or event_summary[:120])
    event_type = str(row.get("event_type") or "raw_market_event")
    symbol = str(row.get("symbol") or "RAW")
    company_name = str(row.get("company_name") or symbol)
    event_date = str(row.get("event_date") or "2026-06-29")
    raw_reason_codes = tuple(str(item) for item in row.get("raw_reason_codes") or ())
    if _label_leaks(row):
        raise ValueError(f"fixture leaks expected archetype into event text: {row.get('fixture_id')}")
    return CandidateEventV2(
        candidate_event_id=str(
            row.get("candidate_event_id")
            or deterministic_id("RAWCEV3", (symbol, company_name, event_date, event_type, event_summary))
        ),
        symbol=symbol,
        company_name=company_name,
        event_date=event_date,
        detected_at=str(row.get("detected_at") or event_date),
        source_family=str(row.get("source_family") or "RawFixture"),
        source_id=str(row.get("source_id") or row.get("fixture_id") or symbol),
        event_type=event_type,
        raw_reason_codes=raw_reason_codes,
        event_title=event_title,
        event_summary=event_summary,
        magnitude=EventMagnitudeV2(),
        issuer_directness=str(row.get("issuer_directness") or "DIRECT"),
        initial_evidence_document_ids=(),
        structured_payload={
            "raw_event_text": event_summary,
            "fixture_id": row.get("fixture_id"),
        },
    )


def build_raw_event_router_matrix_v3(
    *,
    fixtures: Sequence[Mapping[str, Any]],
    provider: ResearchBrainPlannerProvider,
    memory_cards: Sequence[ArchetypeMemoryCard],
) -> Mapping[str, Any]:
    rows = []
    top1 = 0
    top3 = 0
    r13_overroute = 0
    mandatory_rows: dict[str, Mapping[str, Any]] = {}
    leakage_count = 0
    for fixture in fixtures:
        if _label_leaks(fixture):
            leakage_count += 1
            continue
        event = raw_fixture_to_event(fixture)
        expected = str(fixture.get("expected_archetype") or "")
        run = run_planner_provider_v3(provider=provider, event=event, memory_cards=memory_cards)
        hypotheses = run.output.top_k_archetype_hypotheses if run.output else ()
        top_ids = tuple(str(item.get("archetype_id") or "") for item in hypotheses)
        primary = top_ids[0] if top_ids else None
        explicit_r13 = bool(fixture.get("explicit_r13"))
        top1_ok = primary == expected
        top3_ok = expected in top_ids[:3]
        overroute = bool(primary and primary.startswith("R13_") and not expected.startswith("R13_") and not explicit_r13)
        top1 += int(top1_ok)
        top3 += int(top3_ok)
        r13_overroute += int(overroute)
        row = {
            "fixture_id": fixture.get("fixture_id"),
            "expected_archetype": expected,
            "primary_archetype": primary,
            "top3_archetypes": list(top_ids[:3]),
            "status": "ROUTED" if primary else "ARCTYPE_PENDING_DISAMBIGUATION",
            "top1_exact_match": top1_ok,
            "top3_contains_expected": top3_ok,
            "explicit_r13_fixture": explicit_r13,
            "r13_overroute": overroute,
            "provider_name": run.provider_name,
            "fake_provider_used": run.fake_provider_used,
            "provider_error": run.provider_error,
        }
        if expected in MANDATORY_RAW_ARCHETYPES:
            mandatory_rows[expected] = row
        rows.append(row)
    count = len(rows)
    mandatory_pass = all(mandatory_rows.get(item, {}).get("top1_exact_match") for item in MANDATORY_RAW_ARCHETYPES)
    return {
        "schema_version": "research_brain_v3_raw_event_router_matrix",
        "summary": {
            "fixture_count": count,
            "top1_accuracy": round(top1 / count, 6) if count else 0.0,
            "top3_accuracy": round(top3 / count, 6) if count else 0.0,
            "top1_correct_count": top1,
            "top3_correct_count": top3,
            "mandatory_six_top1_pass": mandatory_pass,
            "r13_overroute_count": r13_overroute,
            "fixture_label_leakage_count": leakage_count,
            "fake_provider_used": any(row.get("fake_provider_used") for row in rows),
        },
        "mandatory_six_results": mandatory_rows,
        "rows": rows,
    }


def _label_leaks(row: Mapping[str, Any]) -> bool:
    expected = str(row.get("expected_archetype") or "")
    if not expected:
        return False
    haystack = " ".join(
        [
            str(row.get("event_summary") or row.get("raw_event_text") or ""),
            str(row.get("event_title") or ""),
            " ".join(str(item) for item in row.get("raw_reason_codes") or ()),
        ]
    )
    return expected in haystack


__all__ = [
    "DEFAULT_RAW_ROUTING_FIXTURE_DIR",
    "MANDATORY_RAW_ARCHETYPES",
    "build_raw_event_router_matrix_v3",
    "load_raw_event_routing_fixtures",
    "raw_fixture_to_event",
]
