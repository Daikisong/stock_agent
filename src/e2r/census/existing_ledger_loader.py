"""Load existing source-backed ledger artifacts for Census v2.

The loader does not turn research memory into score evidence. It only imports
rows that an earlier production cutover report already marked as accepted
claim-backed scoring evidence, and it filters them to the current eligible
universe.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


DEFAULT_STAGE_REPORT = Path("docs/operational/production_cutover_v3_stage_distribution_report.json")


@dataclass(frozen=True)
class ExistingLedger:
    accepted_claims_by_symbol: Mapping[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)
    score_contributions_by_symbol: Mapping[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)
    stage_rows_by_symbol: Mapping[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)
    official_event_counts_by_symbol: Mapping[str, Mapping[str, int]] = field(default_factory=dict)
    existing_stage_by_symbol: Mapping[str, str] = field(default_factory=dict)
    evidence_documents: tuple[dict[str, Any], ...] = ()
    evidence_anchors: tuple[dict[str, Any], ...] = ()
    raw_assertions: tuple[dict[str, Any], ...] = ()
    adjudicated_claims: tuple[dict[str, Any], ...] = ()
    accepted_claims: tuple[dict[str, Any], ...] = ()
    primitive_states: tuple[dict[str, Any], ...] = ()
    score_contributions: tuple[dict[str, Any], ...] = ()
    stagecourt_traces: tuple[dict[str, Any], ...] = ()
    skipped_rows: tuple[dict[str, Any], ...] = ()


def load_existing_ledger(
    *,
    eligible_symbols: Sequence[str],
    as_of_date: str,
    stage_report_path: str | Path = DEFAULT_STAGE_REPORT,
) -> ExistingLedger:
    eligible = {str(symbol).zfill(6) for symbol in eligible_symbols}
    path = Path(stage_report_path)
    if not path.exists():
        return ExistingLedger()
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = tuple(dict(row) for row in payload.get("rows") or ())
    grouped: dict[str, list[dict[str, Any]]] = {}
    skipped: list[dict[str, Any]] = []
    for row in rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        if symbol not in eligible:
            skipped.append(
                {
                    "symbol": symbol,
                    "candidate_event_id": row.get("candidate_event_id"),
                    "reason": "not_in_current_eligible_universe",
                    "source_report": str(path),
                }
            )
            continue
        grouped.setdefault(symbol, []).append(row)

    accepted_by_symbol: dict[str, list[dict[str, Any]]] = {}
    scores_by_symbol: dict[str, list[dict[str, Any]]] = {}
    official_counts: dict[str, dict[str, int]] = {}
    existing_stage: dict[str, str] = {}
    docs: dict[str, dict[str, Any]] = {}
    anchors: dict[str, dict[str, Any]] = {}
    raw_assertions: list[dict[str, Any]] = []
    adjudicated_claims: list[dict[str, Any]] = []
    primitive_states: list[dict[str, Any]] = []
    traces: list[dict[str, Any]] = []

    for symbol, symbol_rows in grouped.items():
        existing_stage[symbol] = _best_current_stage(symbol_rows)
        counts = official_counts.setdefault(symbol, {})
        for row in symbol_rows:
            _increment_official_counts(counts, row)
            doc_id = _document_id(row)
            docs.setdefault(doc_id, _document_row(row=row, symbol=symbol, document_id=doc_id, as_of_date=as_of_date))
            claim_ids = tuple(str(item) for item in (row.get("accepted_claims") or ()) if str(item).strip())
            anchor_ids = tuple(_anchor_id(claim_id=claim_id, row=row) for claim_id in claim_ids)
            for claim_id, anchor_id in zip(claim_ids, anchor_ids):
                anchors.setdefault(anchor_id, _anchor_row(row=row, symbol=symbol, document_id=doc_id, anchor_id=anchor_id))
                raw = _raw_assertion_row(row=row, symbol=symbol, claim_id=claim_id, anchor_id=anchor_id)
                adjudicated = {
                    **raw,
                    "adjudication_status": "ACCEPTED_EXISTING_LEDGER",
                    "target_scope_status": "DIRECT",
                    "temporal_status": "CURRENT",
                    "score_evidence_eligible": True,
                    "current_score_eligible_source": "existing_cutover_claim_backed_row",
                }
                accepted = {
                    **adjudicated,
                    "schema_version": "e2r_census_v2_accepted_claim_ref_v1",
                    "source_proxy_only": False,
                    "evidence_url_pending": False,
                    "lifecycle_refreshed": True,
                    "source_report_path": str(path),
                }
                accepted_by_symbol.setdefault(symbol, []).append(accepted)
                raw_assertions.append(raw)
                adjudicated_claims.append(adjudicated)

            contribution_ids = tuple(str(item) for item in (row.get("score_contributions") or ()) if str(item).strip())
            per_contribution = _points_per_contribution(row=row, contribution_count=len(contribution_ids))
            for contribution_id in contribution_ids:
                scores_by_symbol.setdefault(symbol, []).append(
                    {
                        "schema_version": "e2r_census_v2_score_contribution_ref_v1",
                        "score_contribution_id": contribution_id,
                        "symbol": symbol,
                        "component_key": "existing_cutover_claim_backed_component",
                        "criterion_id": row.get("primary_archetype") or "existing_cutover_stage_row",
                        "raw_points": per_contribution,
                        "max_points": per_contribution,
                        "support_claim_ids": claim_ids,
                        "counter_claim_ids": [],
                        "source_proxy_only": False,
                        "rationale": row.get("why_triggered") or "Existing cutover row already linked claim and contribution ids.",
                        "source_report_path": str(path),
                    }
                )
        all_claim_ids = tuple(
            claim["claim_id"]
            for row_claims in (accepted_by_symbol.get(symbol) or (),)
            for claim in row_claims
        )
        if all_claim_ids:
            primitive_states.append(
                {
                    "schema_version": "e2r_census_v2_primitive_state_ref_v1",
                    "symbol": symbol,
                    "primitive_id": "existing_cutover_claim_backed_signal",
                    "status": "PRESENT_CURRENT",
                    "support_claim_ids": all_claim_ids,
                    "counter_claim_ids": [],
                    "confidence": 1.0,
                    "as_of_date": as_of_date,
                }
            )
        traces.append(_stagecourt_trace(symbol=symbol, rows=symbol_rows, as_of_date=as_of_date))

    accepted_claims = tuple(claim for claims in accepted_by_symbol.values() for claim in claims)
    score_contributions = tuple(item for rows_for_symbol in scores_by_symbol.values() for item in rows_for_symbol)
    return ExistingLedger(
        accepted_claims_by_symbol={key: tuple(value) for key, value in accepted_by_symbol.items()},
        score_contributions_by_symbol={key: tuple(value) for key, value in scores_by_symbol.items()},
        stage_rows_by_symbol={key: tuple(value) for key, value in grouped.items()},
        official_event_counts_by_symbol=official_counts,
        existing_stage_by_symbol=existing_stage,
        evidence_documents=tuple(docs.values()),
        evidence_anchors=tuple(anchors.values()),
        raw_assertions=tuple(raw_assertions),
        adjudicated_claims=tuple(adjudicated_claims),
        accepted_claims=accepted_claims,
        primitive_states=tuple(primitive_states),
        score_contributions=score_contributions,
        stagecourt_traces=tuple(traces),
        skipped_rows=tuple(skipped),
    )


def _best_current_stage(rows: Sequence[Mapping[str, Any]]) -> str:
    order = {"3-Red": 6, "3": 5, "2": 4, "1": 3, "0": 2}
    best = max(rows, key=lambda row: order.get(str(row.get("current_stage")), 0))
    return str(best.get("current_stage") or "1")


def _increment_official_counts(counts: dict[str, int], row: Mapping[str, Any]) -> None:
    counts["disclosures"] = counts.get("disclosures", 0) + 1
    text = " ".join(str(row.get(key) or "") for key in ("why_triggered", "trigger_category", "candidate_event_id"))
    if "공급계약" in text or "supply" in text.lower():
        counts["supply_contracts"] = counts.get("supply_contracts", 0) + 1
    if "투자" in text or "facility" in text.lower():
        counts["facility_investments"] = counts.get("facility_investments", 0) + 1
    if "실적" in text or "earnings" in text.lower():
        counts["earnings"] = counts.get("earnings", 0) + 1
    if str(row.get("section")) == "Reject/Red" or str(row.get("current_stage")) == "3-Red":
        counts["risk"] = counts.get("risk", 0) + 1


def _document_id(row: Mapping[str, Any]) -> str:
    value = row.get("candidate_event_id") or row.get("why_triggered") or row.get("symbol")
    return "CDOC-" + stable_hash({"candidate_event": value})[:20]


def _anchor_id(*, claim_id: str, row: Mapping[str, Any]) -> str:
    return "CANC-" + stable_hash({"claim": claim_id, "event": row.get("candidate_event_id")})[:20]


def _document_row(*, row: Mapping[str, Any], symbol: str, document_id: str, as_of_date: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v2_evidence_document_ref_v1",
        "document_id": document_id,
        "symbol": symbol,
        "source_family": _source_family_from_event(row),
        "source_type": "existing_cutover_report_row",
        "canonical_url": None,
        "published_at": _event_date(row) or as_of_date,
        "available_at": _event_date(row) or as_of_date,
        "content_hash": stable_hash(row),
        "source_report_path": str(DEFAULT_STAGE_REPORT),
        "candidate_event_id": row.get("candidate_event_id"),
        "title": row.get("why_triggered"),
    }


def _anchor_row(*, row: Mapping[str, Any], symbol: str, document_id: str, anchor_id: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v2_evidence_anchor_ref_v1",
        "anchor_id": anchor_id,
        "document_id": document_id,
        "symbol": symbol,
        "anchor_type": "EXISTING_LEDGER_ROW",
        "locator": f"{DEFAULT_STAGE_REPORT}#{row.get('candidate_event_id')}",
        "exact_text": row.get("why_triggered") or row.get("operator_note") or "",
        "anchor_verified": True,
        "content_hash": stable_hash({"anchor": row.get("candidate_event_id"), "text": row.get("why_triggered")}),
    }


def _raw_assertion_row(*, row: Mapping[str, Any], symbol: str, claim_id: str, anchor_id: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v2_raw_assertion_ref_v1",
        "claim_id": claim_id,
        "anchor_id": anchor_id,
        "symbol": symbol,
        "subject_entity": row.get("company_name") or symbol,
        "predicate": row.get("trigger_category") or "existing_cutover_trigger",
        "object_value": row.get("why_triggered") or "",
        "polarity": "POSITIVE" if str(row.get("section")) != "Reject/Red" else "NEGATIVE",
        "event_date": _event_date(row),
        "source_family": _source_family_from_event(row),
        "primary_archetype": row.get("primary_archetype"),
    }


def _stagecourt_trace(*, symbol: str, rows: Sequence[Mapping[str, Any]], as_of_date: str) -> dict[str, Any]:
    best = max(rows, key=lambda row: float(row.get("verified_score") or 0.0))
    return {
        "schema_version": "e2r_census_v2_stagecourt_trace_ref_v1",
        "symbol": symbol,
        "as_of_date": as_of_date,
        "input": "existing_cutover_claim_backed_rows",
        "row_count": len(rows),
        "selected_current_stage": _best_current_stage(rows),
        "selected_candidate_event_id": best.get("candidate_event_id"),
        "selected_score_validity": best.get("score_stage_validity"),
        "hard_break_source_quorum": "existing_cutover_report" if str(best.get("section")) == "Reject/Red" else None,
    }


def _points_per_contribution(*, row: Mapping[str, Any], contribution_count: int) -> float:
    if contribution_count <= 0:
        return 0.0
    return round(float(row.get("verified_score") or 0.0) / contribution_count, 4)


def _event_date(row: Mapping[str, Any]) -> str | None:
    text = " ".join(str(row.get(key) or "") for key in ("candidate_event_id", "why_triggered"))
    match = re.search(r"(20\d{2})(\d{2})(\d{2})", text)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    match = re.search(r"(20\d{2})-(\d{2})-(\d{2})", text)
    if match:
        return match.group(0)
    return None


def _source_family_from_event(row: Mapping[str, Any]) -> str:
    event_id = str(row.get("candidate_event_id") or "")
    if "-DART-" in event_id or "OpenDART" in str(row.get("why_triggered") or ""):
        return "OpenDART"
    if "-KIND-" in event_id:
        return "KIND"
    if "-KRX-" in event_id:
        return "KRX"
    if "-CG-" in event_id:
        return "CompanyGuide"
    return "ExistingLedger"


__all__ = ["DEFAULT_STAGE_REPORT", "ExistingLedger", "load_existing_ledger"]
