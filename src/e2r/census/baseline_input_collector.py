"""Collect real baseline inputs for Census v2.

This module is the bridge that was missing in v1. It reads existing local
source-backed artifacts and turns them into Census inputs, while keeping
assessment triggers, source events, accepted claims, and score contributions
as separate lanes.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .baseline_scanner import BaselineScanInputs
from .existing_ledger_loader import ExistingLedger, load_existing_ledger
from .schemas import UniverseInstrument


DEFAULT_PROVIDER_MATRIX = Path("docs/operational/production_cutover_v3_provider_completeness_matrix.json")
DEFAULT_CANDIDATE_EVENT_REPORT = Path("docs/operational/research_brain_v4_candidate_event_report.json")
DEFAULT_REPORT_SNAPSHOTS = Path("data/report_snapshots/report_snapshots.jsonl")
DEFAULT_SEARCH_SNAPSHOTS = Path("data/search_snapshots/search_snapshots.jsonl")
DEFAULT_PRICE_FILE = Path("data/historical_official/prices/prices.csv")


@dataclass(frozen=True)
class CensusBaselineBundle:
    inputs: BaselineScanInputs
    existing_ledger: ExistingLedger
    provider_matrix_rows: tuple[dict[str, Any], ...] = ()
    candidate_events_by_symbol: Mapping[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)
    report_snapshot_events_by_symbol: Mapping[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)
    price_events_by_symbol: Mapping[str, tuple[dict[str, Any], ...]] = field(default_factory=dict)
    source_tasks: tuple[dict[str, Any], ...] = ()
    source_task_executions: tuple[dict[str, Any], ...] = ()
    evidence_documents: tuple[dict[str, Any], ...] = ()
    evidence_anchors: tuple[dict[str, Any], ...] = ()
    raw_assertions: tuple[dict[str, Any], ...] = ()
    adjudicated_claims: tuple[dict[str, Any], ...] = ()
    accepted_claims: tuple[dict[str, Any], ...] = ()
    primitive_states: tuple[dict[str, Any], ...] = ()
    score_contributions: tuple[dict[str, Any], ...] = ()
    stagecourt_traces: tuple[dict[str, Any], ...] = ()
    summary: Mapping[str, Any] = field(default_factory=dict)


def collect_baseline_bundle(
    *,
    instruments: Sequence[UniverseInstrument],
    as_of_date: str,
    repo_root: str | Path = ".",
    provider_matrix_path: str | Path = DEFAULT_PROVIDER_MATRIX,
    candidate_event_report_path: str | Path = DEFAULT_CANDIDATE_EVENT_REPORT,
    report_snapshots_path: str | Path = DEFAULT_REPORT_SNAPSHOTS,
    search_snapshots_path: str | Path = DEFAULT_SEARCH_SNAPSHOTS,
    price_file_path: str | Path = DEFAULT_PRICE_FILE,
) -> CensusBaselineBundle:
    repo = Path(repo_root)
    eligible_symbols = tuple(item.symbol for item in instruments if item.eligible_for_census)
    eligible = set(eligible_symbols)
    provider_rows = _load_provider_rows(repo / provider_matrix_path)
    provider_failed = _blocking_provider_failures(provider_rows=provider_rows, eligible_symbols=eligible_symbols)
    ledger = load_existing_ledger(eligible_symbols=eligible_symbols, as_of_date=as_of_date, stage_report_path=repo / "docs/operational/production_cutover_v3_stage_distribution_report.json")
    candidate_events_by_symbol, source_tasks, executions = _load_candidate_events(
        path=repo / candidate_event_report_path,
        eligible_symbols=eligible,
        as_of_date=as_of_date,
    )
    report_events_by_symbol, report_docs = _load_report_snapshot_events(
        report_path=repo / report_snapshots_path,
        search_path=repo / search_snapshots_path,
        eligible_symbols=eligible,
        as_of_date=as_of_date,
    )
    price_events_by_symbol = _load_price_anomaly_events(
        path=repo / price_file_path,
        eligible_symbols=eligible,
        as_of_date=as_of_date,
    )
    recent_official = _merge_counts(ledger.official_event_counts_by_symbol)
    companyguide_events = _event_counts(candidate_events_by_symbol, "CompanyGuide")
    report_radar_events = _event_counts(candidate_events_by_symbol, "ReportRadar")
    issuer_ir_events = _event_counts(candidate_events_by_symbol, "IR")
    for symbol, rows in report_events_by_symbol.items():
        report_radar_events[symbol] = report_radar_events.get(symbol, 0) + len(rows)
    source_gaps = _source_gaps_from_candidate_events(candidate_events_by_symbol, ledger.accepted_claims_by_symbol)
    inputs = BaselineScanInputs(
        provider_failed_symbols=provider_failed,
        price_anomaly_symbols={symbol: len(rows) for symbol, rows in price_events_by_symbol.items()},
        recent_official_events=recent_official,
        existing_claim_counts={symbol: len(rows) for symbol, rows in ledger.accepted_claims_by_symbol.items()},
        existing_stage=ledger.existing_stage_by_symbol,
        companyguide_revision_events=companyguide_events,
        report_radar_events=report_radar_events,
        issuer_ir_events=issuer_ir_events,
        existing_claim_refs={symbol: tuple(row["claim_id"] for row in rows) for symbol, rows in ledger.accepted_claims_by_symbol.items()},
        source_gap_by_symbol=source_gaps,
        no_data_reason_by_symbol={symbol: "no_current_catalyst_after_baseline_sources" for symbol in eligible if symbol not in _symbols_with_any_input(ledger, candidate_events_by_symbol, report_events_by_symbol, price_events_by_symbol)},
    )
    evidence_documents = tuple(ledger.evidence_documents) + tuple(report_docs)
    summary = _summary(
        eligible_symbols=eligible_symbols,
        provider_rows=provider_rows,
        provider_failed=provider_failed,
        ledger=ledger,
        candidate_events_by_symbol=candidate_events_by_symbol,
        report_events_by_symbol=report_events_by_symbol,
        price_events_by_symbol=price_events_by_symbol,
        source_tasks=source_tasks,
        evidence_documents=evidence_documents,
    )
    return CensusBaselineBundle(
        inputs=inputs,
        existing_ledger=ledger,
        provider_matrix_rows=provider_rows,
        candidate_events_by_symbol=candidate_events_by_symbol,
        report_snapshot_events_by_symbol=report_events_by_symbol,
        price_events_by_symbol=price_events_by_symbol,
        source_tasks=source_tasks,
        source_task_executions=executions,
        evidence_documents=evidence_documents,
        evidence_anchors=ledger.evidence_anchors,
        raw_assertions=ledger.raw_assertions,
        adjudicated_claims=ledger.adjudicated_claims,
        accepted_claims=ledger.accepted_claims,
        primitive_states=ledger.primitive_states,
        score_contributions=ledger.score_contributions,
        stagecourt_traces=ledger.stagecourt_traces,
        summary=summary,
    )


def _load_provider_rows(path: Path) -> tuple[dict[str, Any], ...]:
    if not path.exists():
        return ()
    payload = json.loads(path.read_text(encoding="utf-8"))
    return tuple(dict(row) for row in payload.get("rows") or ())


def _blocking_provider_failures(*, provider_rows: Sequence[Mapping[str, Any]], eligible_symbols: Sequence[str]) -> dict[str, tuple[str, ...]]:
    blocking = tuple(
        str(row.get("provider_name"))
        for row in provider_rows
        if row.get("blocking_cutover") and row.get("provider_classification") != "LIVE_READY"
    )
    if not blocking:
        return {}
    return {symbol: tuple(f"{provider}_blocking_provider_unavailable" for provider in blocking) for symbol in eligible_symbols}


def _load_candidate_events(
    *,
    path: Path,
    eligible_symbols: set[str],
    as_of_date: str,
) -> tuple[dict[str, tuple[dict[str, Any], ...]], tuple[dict[str, Any], ...], tuple[dict[str, Any], ...]]:
    if not path.exists():
        return {}, (), ()
    payload = json.loads(path.read_text(encoding="utf-8"))
    grouped: dict[str, list[dict[str, Any]]] = {}
    tasks: list[dict[str, Any]] = []
    executions: list[dict[str, Any]] = []
    for raw in payload.get("rows") or ():
        symbol = str(raw.get("symbol") or "").zfill(6)
        if symbol not in eligible_symbols:
            continue
        event = {
            "schema_version": "e2r_census_v2_candidate_event_ref_v1",
            "symbol": symbol,
            "company_name": raw.get("company_name"),
            "as_of_date": as_of_date,
            "candidate_event_id": raw.get("candidate_event_id") or _candidate_event_id(raw),
            "event_type": raw.get("event_type") or "source_event",
            "source_family": raw.get("source_family") or "unknown",
            "primary_archetype": raw.get("primary_archetype"),
            "accepted_claim_count": int(raw.get("accepted_claim_count") or 0),
            "source_task_count": int(raw.get("source_task_count") or 0),
            "score_evidence_eligible": False,
            "reason": "candidate event opens investigation only; accepted claims open scoring",
            "source_report_path": str(path),
        }
        grouped.setdefault(symbol, []).append(event)
        for index in range(max(int(raw.get("source_task_count") or 0), 0)):
            task_id = "CV2TASK-" + stable_hash({"event": event["candidate_event_id"], "index": index})[:18]
            tasks.append(
                {
                    "task_id": task_id,
                    "symbol": symbol,
                    "depth_level": "L3_RESEARCH_BRAIN_TRIAGE",
                    "task_class": "existing_research_brain_source_task_ref",
                    "source_class": event["source_family"],
                    "budget": {"max_queries": 1, "max_candidates": 3, "max_fetches": 1, "max_retries": 0},
                    "stop_condition": "stop_on_resolution",
                    "allows_general_web": False,
                    "reason": event["event_type"],
                    "candidate_event_id": event["candidate_event_id"],
                }
            )
            executions.append(
                {
                    "task_id": task_id,
                    "symbol": symbol,
                    "depth_level": "L3_RESEARCH_BRAIN_TRIAGE",
                    "source_class": event["source_family"],
                    "status": "PARSED",
                    "accepted_claim_ids": [],
                    "provider_errors": [],
                    "budget_used": {"fetches": 1, "queries": 1, "retries": 0},
                    "stop_reason": "existing_candidate_event_report_replayed_for_census_v2",
                }
            )
    return {key: tuple(value) for key, value in grouped.items()}, tuple(tasks), tuple(executions)


def _load_report_snapshot_events(
    *,
    report_path: Path,
    search_path: Path,
    eligible_symbols: set[str],
    as_of_date: str,
) -> tuple[dict[str, tuple[dict[str, Any], ...]], tuple[dict[str, Any], ...]]:
    search_by_url = {str(row.get("url")): row for row in _read_jsonl(search_path)}
    grouped: dict[str, list[dict[str, Any]]] = {}
    docs: list[dict[str, Any]] = []
    for row in _read_jsonl(report_path):
        symbol = str(row.get("symbol") or "").zfill(6)
        if symbol not in eligible_symbols:
            continue
        url = str(row.get("url") or "")
        search = search_by_url.get(url, {})
        event_id = "CV2REP-" + stable_hash({"symbol": symbol, "url": url, "hash": row.get("extracted_text_hash")})[:18]
        event = {
            "schema_version": "e2r_census_v2_report_snapshot_event_v1",
            "symbol": symbol,
            "company_name": row.get("company_name"),
            "as_of_date": as_of_date,
            "candidate_event_id": event_id,
            "event_type": "stored_source_event",
            "source_family": "ReportRadar" if row.get("source_type") == "broker_report" else "TrustedNews",
            "source_type": row.get("source_type"),
            "published_at": row.get("as_of_date") or search.get("published_at"),
            "source_url": url,
            "title": row.get("title") or search.get("title"),
            "score_evidence_eligible": False,
            "reason": "stored source snapshot is a lifecycle refresh lead until accepted claims are produced",
        }
        grouped.setdefault(symbol, []).append(event)
        docs.append(
            {
                "schema_version": "e2r_census_v2_evidence_document_ref_v1",
                "document_id": "CDOC-" + stable_hash({"snapshot": event_id})[:20],
                "symbol": symbol,
                "source_family": event["source_family"],
                "source_type": row.get("source_type"),
                "canonical_url": url,
                "published_at": event["published_at"],
                "available_at": row.get("fetched_at") or event["published_at"],
                "content_hash": row.get("extracted_text_hash") or stable_hash(row),
                "source_report_path": str(report_path),
                "title": event["title"],
                "score_evidence_eligible": False,
            }
        )
    return {key: tuple(value) for key, value in grouped.items()}, tuple(docs)


def _load_price_anomaly_events(*, path: Path, eligible_symbols: set[str], as_of_date: str) -> dict[str, tuple[dict[str, Any], ...]]:
    if not path.exists():
        return {}
    rows_by_symbol: dict[str, list[dict[str, Any]]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            symbol = str(row.get("symbol") or "").zfill(6)
            if symbol in eligible_symbols and str(row.get("date") or "") <= as_of_date:
                rows_by_symbol.setdefault(symbol, []).append(dict(row))
    events: dict[str, tuple[dict[str, Any], ...]] = {}
    for symbol, rows in rows_by_symbol.items():
        ordered = sorted(rows, key=lambda row: str(row.get("date") or ""))
        if len(ordered) < 2:
            continue
        first, last = ordered[0], ordered[-1]
        first_close = _float(first.get("close"))
        last_close = _float(last.get("close"))
        first_volume = _float(first.get("volume"))
        last_volume = _float(last.get("volume"))
        if first_close <= 0:
            continue
        return_pct = (last_close / first_close) - 1.0
        volume_multiple = last_volume / first_volume if first_volume > 0 else 0.0
        if abs(return_pct) < 0.20 and volume_multiple < 3.0:
            continue
        event_id = "CV2PX-" + stable_hash({"symbol": symbol, "from": first.get("date"), "to": last.get("date")})[:18]
        events[symbol] = (
            {
                "schema_version": "e2r_census_v2_market_anomaly_event_v1",
                "symbol": symbol,
                "as_of_date": as_of_date,
                "candidate_event_id": event_id,
                "event_type": "market_anomaly",
                "source_family": "KRXPrice",
                "from_date": first.get("date"),
                "to_date": last.get("date"),
                "return_pct": round(return_pct, 6),
                "volume_multiple": round(volume_multiple, 4),
                "score_evidence_eligible": False,
                "reason": "price path opens investigation only and never contributes score",
            },
        )
    return events


def _merge_counts(value: Mapping[str, Mapping[str, int]]) -> dict[str, dict[str, int]]:
    return {symbol: {key: int(count) for key, count in counts.items()} for symbol, counts in value.items()}


def _event_counts(grouped: Mapping[str, Sequence[Mapping[str, Any]]], source_family: str) -> dict[str, int]:
    return {
        symbol: sum(1 for row in rows if row.get("source_family") == source_family)
        for symbol, rows in grouped.items()
        if any(row.get("source_family") == source_family for row in rows)
    }


def _source_gaps_from_candidate_events(
    grouped: Mapping[str, Sequence[Mapping[str, Any]]],
    accepted_claims_by_symbol: Mapping[str, Sequence[Mapping[str, Any]]],
) -> dict[str, tuple[str, ...]]:
    gaps: dict[str, tuple[str, ...]] = {}
    for symbol, rows in grouped.items():
        if accepted_claims_by_symbol.get(symbol):
            continue
        if rows:
            gaps[symbol] = ("candidate_event_without_accepted_current_claim",)
    return gaps


def _symbols_with_any_input(
    ledger: ExistingLedger,
    candidate_events: Mapping[str, Sequence[Mapping[str, Any]]],
    report_events: Mapping[str, Sequence[Mapping[str, Any]]],
    price_events: Mapping[str, Sequence[Mapping[str, Any]]],
) -> set[str]:
    return set(ledger.accepted_claims_by_symbol) | set(candidate_events) | set(report_events) | set(price_events)


def _summary(
    *,
    eligible_symbols: Sequence[str],
    provider_rows: Sequence[Mapping[str, Any]],
    provider_failed: Mapping[str, Sequence[str]],
    ledger: ExistingLedger,
    candidate_events_by_symbol: Mapping[str, Sequence[Mapping[str, Any]]],
    report_events_by_symbol: Mapping[str, Sequence[Mapping[str, Any]]],
    price_events_by_symbol: Mapping[str, Sequence[Mapping[str, Any]]],
    source_tasks: Sequence[Mapping[str, Any]],
    evidence_documents: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    provider_classes = Counter(str(row.get("provider_classification") or "UNKNOWN") for row in provider_rows)
    source_families = Counter()
    for rows in candidate_events_by_symbol.values():
        for row in rows:
            source_families[str(row.get("source_family") or "unknown")] += 1
    for rows in report_events_by_symbol.values():
        for row in rows:
            source_families[str(row.get("source_family") or "unknown")] += 1
    for rows in price_events_by_symbol.values():
        for row in rows:
            source_families[str(row.get("source_family") or "unknown")] += 1
    return {
        "schema_version": "e2r_census_v2_baseline_inputs_summary_v1",
        "eligible_symbol_count": len(eligible_symbols),
        "provider_matrix_provider_count": len(provider_rows),
        "provider_classification_counts": dict(provider_classes),
        "provider_failed_symbol_count": len(provider_failed),
        "existing_ledger_symbol_count": len(ledger.accepted_claims_by_symbol),
        "existing_ledger_accepted_claim_count": len(ledger.accepted_claims),
        "existing_ledger_score_contribution_count": len(ledger.score_contributions),
        "existing_ledger_skipped_not_in_universe_count": len(ledger.skipped_rows),
        "candidate_event_symbol_count": len(candidate_events_by_symbol),
        "candidate_event_count": sum(len(rows) for rows in candidate_events_by_symbol.values()),
        "report_snapshot_symbol_count": len(report_events_by_symbol),
        "report_snapshot_event_count": sum(len(rows) for rows in report_events_by_symbol.values()),
        "price_anomaly_symbol_count": len(price_events_by_symbol),
        "price_anomaly_event_count": sum(len(rows) for rows in price_events_by_symbol.values()),
        "source_task_count": len(source_tasks),
        "evidence_document_count": len(evidence_documents),
        "source_family_counts": dict(source_families),
        "census_assessment_event_score_eligible": False,
        "market_anomaly_score_eligible": False,
        "research_memory_score_eligible_without_claim": False,
    }


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


def _candidate_event_id(row: Mapping[str, Any]) -> str:
    return "CV2CE-" + stable_hash(row)[:18]


def _float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


__all__ = [
    "CensusBaselineBundle",
    "DEFAULT_CANDIDATE_EVENT_REPORT",
    "DEFAULT_PRICE_FILE",
    "DEFAULT_PROVIDER_MATRIX",
    "DEFAULT_REPORT_SNAPSHOTS",
    "DEFAULT_SEARCH_SNAPSHOTS",
    "collect_baseline_bundle",
]
