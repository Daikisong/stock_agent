"""Load source-backed production cutover leaf artifacts for Census v3."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


DEFAULT_PRODUCTION_CUTOVER_V3_ROOT = Path("output/production_cutover_v3")


@dataclass(frozen=True)
class ProductionCutoverLeafBundle:
    candidate_events: tuple[dict[str, Any], ...]
    research_brain_plans: tuple[dict[str, Any], ...]
    source_tasks: tuple[dict[str, Any], ...]
    source_task_executions: tuple[dict[str, Any], ...]
    evidence_documents: tuple[dict[str, Any], ...]
    evidence_anchors: tuple[dict[str, Any], ...]
    raw_assertions: tuple[dict[str, Any], ...]
    adjudicated_claims: tuple[dict[str, Any], ...]
    accepted_claims: tuple[dict[str, Any], ...]
    primitive_states: tuple[dict[str, Any], ...]
    score_contributions: tuple[dict[str, Any], ...]
    stagecourt_traces: tuple[dict[str, Any], ...]
    watchlist_rows: tuple[dict[str, Any], ...]
    skipped_rows: tuple[dict[str, Any], ...]

    @property
    def accepted_claims_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.accepted_claims)

    @property
    def score_contributions_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.score_contributions)

    @property
    def stagecourt_traces_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.stagecourt_traces)

    @property
    def source_tasks_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.source_tasks)

    @property
    def source_task_executions_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.source_task_executions)

    @property
    def primitive_states_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.primitive_states)

    @property
    def watchlist_by_symbol(self) -> dict[str, tuple[dict[str, Any], ...]]:
        return _group_by_symbol(self.watchlist_rows)


def load_production_cutover_leaf_bundle(
    *,
    eligible_symbols: Sequence[str],
    root: str | Path = DEFAULT_PRODUCTION_CUTOVER_V3_ROOT,
) -> ProductionCutoverLeafBundle:
    eligible = {str(symbol).zfill(6) for symbol in eligible_symbols}
    root_path = Path(root)
    candidate_events: dict[str, dict[str, Any]] = {}
    source_tasks: dict[str, dict[str, Any]] = {}
    executions: dict[str, dict[str, Any]] = {}
    documents: dict[str, dict[str, Any]] = {}
    anchors: dict[str, dict[str, Any]] = {}
    raw_assertions: dict[str, dict[str, Any]] = {}
    adjudicated: dict[str, dict[str, Any]] = {}
    accepted: dict[str, dict[str, Any]] = {}
    primitive_states: dict[str, dict[str, Any]] = {}
    contributions: dict[str, dict[str, Any]] = {}
    stagecourt: dict[str, dict[str, Any]] = {}
    watchlist: dict[str, dict[str, Any]] = {}
    skipped: list[dict[str, Any]] = []

    for day_root in sorted(path for path in root_path.glob("2026-*") if path.is_dir()):
        day = day_root.name
        for row in _read_json(day_root / "candidate_events.json", default=[]):
            symbol = _symbol(row)
            if symbol not in eligible:
                skipped.append(_skipped(row=row, day=day, reason="candidate_event_symbol_not_eligible"))
                continue
            key = str(row.get("candidate_event_id") or stable_hash(row))
            candidate_events.setdefault(key, {**row, "symbol": symbol, "source_cutover_date": day})
        for row in _read_json(day_root / "source_tasks.json", default=[]):
            symbol = _symbol(row)
            if symbol not in eligible:
                skipped.append(_skipped(row=row, day=day, reason="source_task_symbol_not_eligible"))
                continue
            task = _normalize_source_task(row=row, day=day, symbol=symbol)
            source_tasks.setdefault(task["task_id"], task)
        for row in _read_json(day_root / "source_task_executions.json", default=[]):
            symbol = _symbol(row)
            if symbol not in eligible:
                skipped.append(_skipped(row=row, day=day, reason="source_task_execution_symbol_not_eligible"))
                continue
            execution = _normalize_source_task_execution(row=row, day=day, symbol=symbol)
            executions.setdefault(execution["task_id"], execution)
        for row in _read_jsonl(day_root / "accepted_claims.jsonl"):
            symbol = _symbol(row)
            if symbol not in eligible:
                skipped.append(_skipped(row=row, day=day, reason="accepted_claim_symbol_not_eligible"))
                continue
            claim = {**row, "symbol": symbol, "source_cutover_date": day}
            accepted.setdefault(str(claim.get("claim_id")), claim)
        for row in _read_jsonl(day_root / "adjudicated_claims.jsonl"):
            symbol = _symbol(row)
            if symbol in eligible:
                adjudicated.setdefault(str(row.get("claim_id")), {**row, "symbol": symbol, "source_cutover_date": day})
        for row in _read_jsonl(day_root / "raw_assertions.jsonl"):
            symbol = _symbol(row)
            if symbol in eligible:
                raw_assertions.setdefault(str(row.get("raw_assertion_id") or row.get("claim_id")), {**row, "symbol": symbol, "source_cutover_date": day})
        for row in _read_jsonl(day_root / "score_contributions.jsonl"):
            support = tuple(str(item) for item in (row.get("support_claim_ids") or ()) if str(item).strip())
            symbol = _symbol_for_claim_ids(support, accepted)
            if symbol not in eligible:
                skipped.append(_skipped(row=row, day=day, reason="score_contribution_claim_symbol_not_eligible"))
                continue
            contribution = {
                **row,
                "symbol": symbol,
                "score_contribution_id": row.get("score_contribution_id") or row.get("contribution_id"),
                "source_cutover_date": day,
            }
            contributions.setdefault(str(contribution.get("score_contribution_id")), contribution)
        for row in _read_jsonl(day_root / "primitive_states.jsonl"):
            symbol = _symbol(row) or _symbol_for_claim_ids(row.get("support_claim_ids") or (), accepted)
            if symbol in eligible:
                key = f"{symbol}:{row.get('primitive_id')}:{','.join(row.get('support_claim_ids') or [])}"
                primitive_states.setdefault(key, {**row, "symbol": symbol, "source_cutover_date": day})
        for row in _read_jsonl(day_root / "evidence_documents.jsonl"):
            symbol = _symbol(row)
            if symbol in eligible or _doc_used_by_eligible_claim(row.get("document_id"), accepted):
                documents.setdefault(str(row.get("document_id")), {**row, "symbol": symbol or _symbol_for_document(row.get("document_id"), accepted), "source_cutover_date": day})
        for row in _read_jsonl(day_root / "evidence_anchors.jsonl"):
            if _anchor_used_by_eligible_claim(row.get("anchor_id"), accepted):
                symbol = _symbol_for_anchor(row.get("anchor_id"), accepted)
                anchors.setdefault(str(row.get("anchor_id")), {**row, "symbol": symbol, "source_cutover_date": day})
        for row in _read_json(day_root / "stagecourt_traces.json", default=[]):
            symbol = _symbol(row) or _symbol_for_claim_ids(row.get("accepted_claim_ids") or (), accepted)
            if symbol not in eligible:
                skipped.append(_skipped(row=row, day=day, reason="stagecourt_trace_symbol_not_eligible"))
                continue
            trace = _normalize_stagecourt_trace(row=row, day=day, symbol=symbol)
            stagecourt.setdefault(trace["stagecourt_trace_id"], trace)
        daily = _read_json(day_root / "daily_watchlist.json", default={})
        for row in daily.get("rows", []) if isinstance(daily, dict) else []:
            symbol = _symbol(row)
            if symbol in eligible:
                watch = {**row, "symbol": symbol, "source_cutover_date": day}
                watchlist.setdefault(str(row.get("candidate_event_id") or stable_hash(row)), watch)

    plans = _research_brain_plans(candidate_events=tuple(candidate_events.values()), source_tasks=tuple(source_tasks.values()))
    return ProductionCutoverLeafBundle(
        candidate_events=tuple(candidate_events.values()),
        research_brain_plans=plans,
        source_tasks=tuple(source_tasks.values()),
        source_task_executions=tuple(executions.values()),
        evidence_documents=tuple(documents.values()),
        evidence_anchors=tuple(anchors.values()),
        raw_assertions=tuple(raw_assertions.values()),
        adjudicated_claims=tuple(adjudicated.values()),
        accepted_claims=tuple(accepted.values()),
        primitive_states=tuple(primitive_states.values()),
        score_contributions=tuple(contributions.values()),
        stagecourt_traces=tuple(stagecourt.values()),
        watchlist_rows=tuple(watchlist.values()),
        skipped_rows=tuple(skipped),
    )


def _read_json(path: Path, *, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: Path) -> tuple[dict[str, Any], ...]:
    if not path.exists():
        return ()
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return tuple(rows)


def _symbol(row: Mapping[str, Any]) -> str:
    value = row.get("symbol")
    if not value and isinstance(row.get("source_task"), Mapping):
        value = row["source_task"].get("symbol")
    if not value:
        for key in ("target_entity_id", "subject_entity_id"):
            text = str(row.get(key) or "")
            if text.startswith("TICKER:"):
                value = text.split(":", 1)[1]
                break
    if not value and isinstance(row.get("structured_payload"), Mapping):
        value = row["structured_payload"].get("stock_code")
    if not value:
        text = str(row.get("candidate_event_id") or "")
        parts = text.split("-")
        for part in parts:
            if len(part) == 6 and part.isdigit():
                value = part
                break
    return str(value or "").zfill(6) if str(value or "").strip() else ""


def _symbol_for_claim_ids(claim_ids: Sequence[str], accepted: Mapping[str, Mapping[str, Any]]) -> str:
    for claim_id in claim_ids:
        row = accepted.get(str(claim_id))
        if row:
            return _symbol(row)
    return ""


def _doc_used_by_eligible_claim(document_id: Any, accepted: Mapping[str, Mapping[str, Any]]) -> bool:
    return any(row.get("document_id") == document_id for row in accepted.values())


def _anchor_used_by_eligible_claim(anchor_id: Any, accepted: Mapping[str, Mapping[str, Any]]) -> bool:
    return any(row.get("anchor_id") == anchor_id for row in accepted.values())


def _symbol_for_document(document_id: Any, accepted: Mapping[str, Mapping[str, Any]]) -> str:
    for row in accepted.values():
        if row.get("document_id") == document_id:
            return _symbol(row)
    return ""


def _symbol_for_anchor(anchor_id: Any, accepted: Mapping[str, Mapping[str, Any]]) -> str:
    for row in accepted.values():
        if row.get("anchor_id") == anchor_id:
            return _symbol(row)
    return ""


def _normalize_source_task(*, row: Mapping[str, Any], day: str, symbol: str) -> dict[str, Any]:
    budget = {
        "max_queries": int(row.get("max_queries") or 1),
        "max_candidates": int(row.get("max_candidates") or 1),
        "max_fetches": int(row.get("max_fetches") or 1),
        "max_retries": int(row.get("max_retries") or 0),
    }
    return {
        **dict(row),
        "symbol": symbol,
        "budget": budget,
        "source_cutover_date": day,
        "source_task_origin": "production_cutover_v3_leaf_artifact",
        "general_search_allowed": bool(row.get("general_search_allowed", False)),
    }


def _normalize_source_task_execution(*, row: Mapping[str, Any], day: str, symbol: str) -> dict[str, Any]:
    accepted_claim_ids = tuple(str(item) for item in (row.get("accepted_claim_ids") or ()) if str(item).strip())
    return {
        **dict(row),
        "symbol": symbol,
        "accepted_claim_ids": list(accepted_claim_ids),
        "source_cutover_date": day,
        "source_task_execution_origin": "production_cutover_v3_leaf_artifact",
        "claim_producing_execution": bool(accepted_claim_ids and row.get("status") == "EVIDENCE_OS_ACCEPTED"),
    }


def _normalize_stagecourt_trace(*, row: Mapping[str, Any], day: str, symbol: str) -> dict[str, Any]:
    trace_id = "SCT-" + stable_hash({"day": day, "symbol": symbol, "candidate_event": row.get("candidate_event_id"), "claims": row.get("accepted_claim_ids")})[:20]
    return {
        **dict(row),
        "symbol": symbol,
        "stagecourt_trace_id": trace_id,
        "trace_id": trace_id,
        "source_cutover_date": day,
    }


def _research_brain_plans(*, candidate_events: Sequence[Mapping[str, Any]], source_tasks: Sequence[Mapping[str, Any]]) -> tuple[dict[str, Any], ...]:
    tasks_by_event: dict[str, list[str]] = {}
    for task in source_tasks:
        event_id = str(task.get("candidate_event_id") or "")
        if event_id:
            tasks_by_event.setdefault(event_id, []).append(str(task.get("task_id")))
    plans: list[dict[str, Any]] = []
    for event in candidate_events:
        event_id = str(event.get("candidate_event_id") or "")
        if not event_id:
            continue
        plans.append(
            {
                "schema_version": "e2r_census_v3_research_brain_plan_ref_v1",
                "plan_id": "RBPLAN-" + stable_hash({"event_id": event_id})[:18],
                "symbol": _symbol(event),
                "candidate_event_id": event_id,
                "source_task_ids": sorted(tasks_by_event.get(event_id, [])),
                "planner_origin": event.get("source_task_generation_policy") or "production_cutover_v3_leaf_artifact",
                "forbidden_direct_score_stage": True,
            }
        )
    return tuple(plans)


def _group_by_symbol(rows: Sequence[Mapping[str, Any]]) -> dict[str, tuple[dict[str, Any], ...]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        symbol = _symbol(row)
        if symbol:
            grouped.setdefault(symbol, []).append(dict(row))
    return {key: tuple(value) for key, value in grouped.items()}


def _skipped(*, row: Mapping[str, Any], day: str, reason: str) -> dict[str, Any]:
    return {
        "source_cutover_date": day,
        "reason": reason,
        "symbol": _symbol(row),
        "row_id": row.get("candidate_event_id") or row.get("claim_id") or row.get("task_id") or stable_hash(row)[:18],
    }


__all__ = ["DEFAULT_PRODUCTION_CUTOVER_V3_ROOT", "ProductionCutoverLeafBundle", "load_production_cutover_leaf_bundle"]
