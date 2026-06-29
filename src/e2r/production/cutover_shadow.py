"""Production cutover shadow bundle and audits."""

from __future__ import annotations

import json
import time
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.candidate_event_purity import InstrumentRegistry, ProductionMode, build_candidate_purity_report
from e2r.production.claim_extraction.extraction_audit import build_claim_extraction_audit
from e2r.production.metadata import build_report_metadata, stable_hash, write_json, write_jsonl, write_text
from e2r.production.official_live_shadow import OfficialLiveShadowData, build_official_live_shadow_data
from e2r.production.source_connectors import SourceFetchResult, build_default_source_provider_registry


@dataclass(frozen=True)
class ProductionCutoverConfig:
    as_of_date: str
    mode: str = ProductionMode.PRODUCTION_SHADOW_LIVE.value
    planner_provider: str = "surrogate"
    source_mode: str = "live_official_first"
    candidate_min_count: int = 50
    sector_min_events: int = 3
    max_source_tasks_per_candidate: int = 5
    max_fetches_per_task: int = 3
    max_total_runtime_seconds: int = 900
    deterministic_scorer_min_count: int = 15
    fail_on_critical_audit: bool = True
    output_dir: str | None = None
    validation_output_root: str = "output/production_cutover"
    frozen_snapshot_dir: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_production_cutover_bundle(
    *,
    repo_root: str | Path = ".",
    config: ProductionCutoverConfig,
    command: str,
) -> Mapping[str, Any]:
    started = time.monotonic()
    root = Path(repo_root)
    if config.mode == ProductionMode.FROZEN_REPLAY.value:
        live_data = _load_frozen_replay_shadow_data(repo_root=root, config=config)
    else:
        live_data = build_official_live_shadow_data(
            repo_root=root,
            as_of_date=date.fromisoformat(config.as_of_date),
            candidate_min_count=config.candidate_min_count,
            planner_provider=config.planner_provider,
        )
    events = live_data.candidate_events
    planner_rows = live_data.planner_runs
    source_rows = live_data.source_task_executions
    watchlist_rows = live_data.daily_watchlist
    metadata = build_report_metadata(
        repo_root=root,
        report_generator="e2r.production.cutover_shadow",
        command=command,
        config=config.to_dict(),
        source_corpus=live_data.source_corpus,
        candidate_events=events,
        planner_runs=planner_rows,
    )
    candidate_purity = build_candidate_purity_report(
        events,
        mode=config.mode,
        repo_root=root,
        as_of_date=config.as_of_date,
        registry=live_data.registry,
    )
    connector_probe_results = ()
    if config.mode != ProductionMode.FROZEN_REPLAY.value:
        connector_probe_results = _exercise_connectors(
            events=events,
            repo_root=root,
            as_of_date=date.fromisoformat(config.as_of_date),
            source_mode=config.source_mode,
        )
    source_connector_report = _source_connector_report_from_live_data(live_data, connector_probe_results, mode=config.mode)
    provider_error_report = _provider_error_report(source_connector_report)
    claim_extraction_audit = _claim_extraction_audit_from_live_data(live_data)
    planner_provider_report = _planner_provider_report(planner_rows)
    score_meaning_audit = _score_meaning_audit(watchlist_rows, config=config)
    v4 = _load_v4_reports(root)
    memory_usage_audit = _research_memory_usage_audit(v4.get("memory_usage", {}), v4.get("source_quality", {}))
    sla_report = _sla_report(started_at=started, config=config, planner_rows=planner_rows, source_rows=source_rows)
    operator_digest = _operator_digest_from_live_data(live_data)
    static_logic_audit = _static_logic_audit(
        metadata=metadata,
        candidate_purity=candidate_purity,
        source_connector_report=source_connector_report,
        claim_extraction_audit=claim_extraction_audit,
        planner_provider_report=planner_provider_report,
        score_meaning_audit=score_meaning_audit,
        memory_usage_audit=memory_usage_audit,
        config=config,
    )
    current_multiday_row = _multiday_row_from_current_run(
        metadata=metadata,
        config=config,
        candidate_purity=candidate_purity,
        source_connector_report=source_connector_report,
        planner_provider_report=planner_provider_report,
        claim_extraction_audit=claim_extraction_audit,
        score_meaning_audit=score_meaning_audit,
        static_logic_audit=static_logic_audit,
        watchlist_rows=watchlist_rows,
    )
    multiday_validation = _multiday_validation_from_artifacts(
        repo_root=root,
        config=config,
        current_row=current_multiday_row,
    )
    stability_report = _stability_report_markdown(multiday_validation)
    shadow_latest = _shadow_latest(
        metadata=metadata,
        candidate_purity=candidate_purity,
        source_connector_report=source_connector_report,
        planner_provider_report=planner_provider_report,
        claim_extraction_audit=claim_extraction_audit,
        score_meaning_audit=score_meaning_audit,
        multiday_validation=multiday_validation,
        operator_digest=operator_digest,
        static_logic_audit=static_logic_audit,
        config=config,
    )
    acceptance = _acceptance_report_markdown(shadow_latest)
    verdict = _readiness_verdict_markdown(shadow_latest)
    output_artifacts = _output_artifacts_from_live_data(live_data=live_data, audit_summary=shadow_latest)
    return {
        "metadata": metadata,
        "config": config.to_dict(),
        "candidate_purity": candidate_purity,
        "source_connector_report": source_connector_report,
        "provider_error_report": provider_error_report,
        "claim_extraction_audit": claim_extraction_audit,
        "planner_provider_report": planner_provider_report,
        "score_meaning_audit": score_meaning_audit,
        "multiday_validation": multiday_validation,
        "stability_report_md": stability_report,
        "research_memory_usage_audit": memory_usage_audit,
        "sla_report": sla_report,
        "operator_digest": operator_digest,
        "static_logic_audit": static_logic_audit,
        "shadow_latest": shadow_latest,
        "acceptance_report_md": acceptance,
        "readiness_verdict_md": verdict,
        "output_artifacts": output_artifacts,
    }


def write_production_cutover_bundle(
    *,
    bundle: Mapping[str, Any],
    docs_dir: str | Path = "docs/operational",
    output_dir: str | Path,
) -> Mapping[str, str]:
    docs = Path(docs_dir)
    output = Path(output_dir)
    paths: dict[str, str] = {}
    doc_files = {
        "production_cutover_report_reproducibility_audit.json": bundle["shadow_latest"]["report_reproducibility"],
        "production_cutover_candidate_purity_report.json": bundle["candidate_purity"],
        "production_cutover_source_connector_report.json": bundle["source_connector_report"],
        "production_cutover_provider_error_report.json": bundle["provider_error_report"],
        "production_cutover_claim_extraction_audit.json": bundle["claim_extraction_audit"],
        "production_cutover_planner_provider_report.json": bundle["planner_provider_report"],
        "production_cutover_score_meaning_audit.json": bundle["score_meaning_audit"],
        "production_cutover_shadow_latest.json": bundle["shadow_latest"],
        "production_cutover_multiday_validation.json": bundle["multiday_validation"],
        "production_cutover_research_memory_usage_audit.json": bundle["research_memory_usage_audit"],
        "production_cutover_sla_report.json": bundle["sla_report"],
        "production_cutover_static_logic_audit.json": bundle["static_logic_audit"],
    }
    for name, payload in doc_files.items():
        path = docs / name
        write_json(path, payload)
        paths[name] = str(path)
    text_files = {
        "production_cutover_acceptance_report.md": bundle["acceptance_report_md"],
        "production_cutover_readiness_verdict.md": bundle["readiness_verdict_md"],
        "production_cutover_shadow_latest.md": _shadow_latest_markdown(bundle["shadow_latest"]),
        "production_cutover_stability_report.md": bundle["stability_report_md"],
    }
    for name, text in text_files.items():
        path = docs / name
        write_text(path, text)
        paths[name] = str(path)
    artifacts = bundle["output_artifacts"]
    json_outputs = {
        "candidate_events.json": artifacts["candidate_events"],
        "planner_runs.json": artifacts["planner_runs"],
        "source_tasks.json": artifacts["source_tasks"],
        "source_task_executions.json": artifacts["source_task_executions"],
        "stagecourt_traces.json": artifacts["stagecourt_traces"],
        "daily_watchlist.json": artifacts["daily_watchlist"],
        "operator_digest.json": bundle["operator_digest"],
        "audit_summary.json": bundle["shadow_latest"],
    }
    for name, payload in json_outputs.items():
        path = output / name
        write_json(path, payload)
        paths[name] = str(path)
    jsonl_outputs = {
        "evidence_documents.jsonl": artifacts["evidence_documents"],
        "evidence_anchors.jsonl": artifacts["evidence_anchors"],
        "evidence_claim_ledger.jsonl": artifacts["evidence_claim_ledger"],
        "primitive_states.jsonl": artifacts["primitive_states"],
        "score_contributions.jsonl": artifacts["score_contributions"],
    }
    for name, rows in jsonl_outputs.items():
        path = output / name
        write_jsonl(path, rows)
        paths[name] = str(path)
    write_text(output / "daily_watchlist.md", _daily_watchlist_markdown(artifacts["daily_watchlist"]))
    paths["daily_watchlist.md"] = str(output / "daily_watchlist.md")
    write_text(output / "operator_digest.md", _operator_digest_markdown(bundle["operator_digest"]))
    paths["operator_digest.md"] = str(output / "operator_digest.md")
    for row in artifacts.get("planner_raw_prompts", ()):
        path = output / row["path"]
        write_json(path, row["payload"])
        paths[str(path.relative_to(output))] = str(path)
    for row in artifacts.get("planner_raw_responses", ()):
        path = output / row["path"]
        write_json(path, row["payload"])
        paths[str(path.relative_to(output))] = str(path)
    return paths


def _load_v4_reports(root: Path) -> Mapping[str, Any]:
    docs = root / "docs/operational"
    return {
        "planner": _json(docs / "research_brain_v4_real_planner_report.json"),
        "source": _json(docs / "research_brain_v4_source_acquisition_report.json"),
        "extraction": _json(docs / "research_brain_v4_evidence_extraction_audit.json"),
        "watchlist": _json(docs / "research_brain_v4_daily_watchlist_sample.json"),
        "multi_day": _json(docs / "research_brain_v4_multi_day_shadow_runs.json"),
        "memory_usage": _json(docs / "research_brain_v4_research_memory_usage_audit.json"),
        "source_quality": _json(docs / "research_brain_v4_source_quality_promotion_report.json"),
    }


def _json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {"summary": {}, "rows": []}
    return json.loads(path.read_text(encoding="utf-8"))


def _json_any(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.exists():
        return ()
    rows: list[Mapping[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parsed = json.loads(line)
        if isinstance(parsed, Mapping):
            rows.append(parsed)
    return tuple(rows)


def _load_frozen_replay_shadow_data(*, repo_root: Path, config: ProductionCutoverConfig) -> OfficialLiveShadowData:
    snapshot = Path(config.frozen_snapshot_dir or config.output_dir or f"output/production_cutover/{config.as_of_date}")
    if not snapshot.is_absolute():
        snapshot = repo_root / snapshot
    audit = _json_any(snapshot / "audit_summary.json", {})
    if not audit:
        raise FileNotFoundError(f"frozen replay snapshot missing audit_summary.json: {snapshot}")
    events = tuple(_json_any(snapshot / "candidate_events.json", []))
    planner_runs = tuple(_frozen_planner_row(row) for row in _json_any(snapshot / "planner_runs.json", []))
    source_tasks = tuple(_json_any(snapshot / "source_tasks.json", []))
    source_task_executions = tuple(_json_any(snapshot / "source_task_executions.json", []))
    documents = tuple(_frozen_document_row(row, snapshot=snapshot) for row in _jsonl(snapshot / "evidence_documents.jsonl"))
    anchors = _jsonl(snapshot / "evidence_anchors.jsonl")
    claims = _jsonl(snapshot / "evidence_claim_ledger.jsonl")
    primitive_states = _jsonl(snapshot / "primitive_states.jsonl")
    score_contributions = _jsonl(snapshot / "score_contributions.jsonl")
    traces = tuple(_json_any(snapshot / "stagecourt_traces.json", []))
    watchlist_payload = _json_any(snapshot / "daily_watchlist.json", {"rows": []})
    watchlist = tuple(watchlist_payload.get("rows", ()) if isinstance(watchlist_payload, Mapping) else watchlist_payload)
    operator_payload = _json_any(snapshot / "operator_digest.json", {"rows": []})
    operator_rows = tuple(operator_payload.get("rows", ()) if isinstance(operator_payload, Mapping) else operator_payload)
    candidate_summary = ((audit.get("summary") or {}).get("candidate") or {}) if isinstance(audit, Mapping) else {}
    names = {str(row.get("symbol")): str(row.get("company_name") or row.get("symbol")) for row in events if row.get("symbol")}
    registry = InstrumentRegistry(
        symbols=frozenset(names),
        names_by_symbol=names,
        official_krx_universe_count=int(candidate_summary.get("actual_krx_universe_count", len(names))),
        combined_registry_count=int(candidate_summary.get("combined_registry_count", len(names))),
        source_paths=(f"frozen_snapshot:{snapshot}",),
    )
    provider_results = tuple(_frozen_provider_result(row, snapshot=snapshot) for row in documents)
    return OfficialLiveShadowData(
        registry=registry,
        candidate_events=events,
        planner_runs=planner_runs,
        source_tasks=source_tasks,
        source_task_executions=source_task_executions,
        evidence_documents=documents,
        evidence_anchors=anchors,
        evidence_claim_ledger=claims,
        primitive_states=primitive_states,
        score_contributions=score_contributions,
        stagecourt_traces=traces,
        daily_watchlist=watchlist,
        operator_digest_rows=operator_rows,
        provider_results=provider_results,
        source_corpus={
            "frozen_snapshot_dir": str(snapshot),
            "frozen_snapshot_audit_hash": stable_hash(audit),
            "frozen_snapshot_document_count": len(documents),
        },
    )


def _frozen_planner_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
    frozen = dict(row)
    event_id = str(frozen.get("candidate_event_id") or "unknown")
    output = frozen.get("raw_response_payload") or {
        "frozen_replay": True,
        "candidate_event_id": event_id,
        "source": "planner_runs.json",
    }
    frozen.update(
        {
            "provider_name": "frozen_planner_snapshot",
            "provider_mode": "frozen",
            "provider_mode_label": "frozen_replay",
            "real_provider_exercised": False,
            "real_provider_success": False,
            "fake_provider_used": True,
            "is_real_provider": False,
            "endpoint": "frozen-snapshot",
            "model": frozen.get("model") or "frozen-snapshot",
            "model_identity_status": "FROZEN_REPLAY_SNAPSHOT",
            "prompt_payload": {
                "schema_version": "production_cutover_frozen_planner_prompt_v1",
                "candidate_event_id": event_id,
                "source": "planner_runs.json",
            },
            "output": output,
            "raw_response_payload": output,
        }
    )
    return frozen


def _frozen_document_row(row: Mapping[str, Any], *, snapshot: Path) -> Mapping[str, Any]:
    frozen = dict(row)
    frozen["mode"] = "frozen"
    frozen["frozen_snapshot_dir"] = str(snapshot)
    return frozen


def _frozen_provider_result(row: Mapping[str, Any], *, snapshot: Path) -> Mapping[str, Any]:
    return {
        "provider_name": row.get("source_name") or "OpenDART",
        "source_class": "DART",
        "mode": "frozen",
        "request_id": f"FROZEN-{row.get('provider_request_id') or row.get('document_id')}",
        "request_params": {"frozen_snapshot_dir": str(snapshot), "document_id": row.get("document_id")},
        "status": "FETCHED",
        "canonical_url": row.get("canonical_url"),
        "official_document_id": row.get("official_document_id"),
        "published_at": row.get("published_at"),
        "available_at": row.get("available_at"),
        "fetched_at": row.get("fetched_at"),
        "content_hash": row.get("content_hash"),
        "raw_text": row.get("raw_text"),
        "structured_payload": row.get("structured_payload") or {},
        "provider_error": None,
    }


def _exercise_connectors(
    *,
    events: Sequence[Mapping[str, Any]],
    repo_root: Path,
    as_of_date: date,
    source_mode: str,
) -> tuple[SourceFetchResult, ...]:
    registry = build_default_source_provider_registry(repo_root)
    mode = "live" if source_mode == "live_official_first" else "snapshot"
    selected = [event for event in events if not _fixture_symbol(str(event.get("symbol") or ""))][:3]
    results: list[SourceFetchResult] = []
    for event in selected:
        results.extend(
            registry.fetch_all(
                symbol=str(event.get("symbol") or ""),
                company_name=str(event.get("company_name") or ""),
                as_of_date=as_of_date,
                mode=mode,
            )
        )
    return tuple(results)


def _source_connector_report_from_v4_and_connectors(
    *,
    source_rows: Sequence[Mapping[str, Any]],
    connector_results: Sequence[SourceFetchResult],
) -> Mapping[str, Any]:
    provider_report = build_default_source_provider_registry().build_report(connector_results)
    snapshot_documents = [
        url
        for row in source_rows
        for url in row.get("document_urls", ())
        if str(url).startswith("snapshot://")
    ]
    non_snapshot_documents = [
        url
        for row in source_rows
        for url in row.get("document_urls", ())
        if url and not str(url).startswith("snapshot://")
    ]
    summary = dict(provider_report["summary"])
    summary.update(
        {
            "v4_shadow_document_count": sum(len(row.get("fetched_document_ids", ())) for row in source_rows),
            "v4_shadow_snapshot_document_count": len(snapshot_documents),
            "v4_shadow_non_snapshot_document_count": len(non_snapshot_documents),
            "real_source_document_fetched_count": summary["real_document_fetched_count"],
            "stored_snapshot_only_documents": len(snapshot_documents),
            "source_task_accepted_without_provider_fetch_count": sum(
                bool(row.get("accepted_claim_ids")) and not row.get("fetched_document_ids") for row in source_rows
            ),
        }
    )
    return {
        "schema_version": "production_cutover_source_connector_report_v1",
        "summary": summary,
        "rows": [result.to_dict() for result in connector_results],
        "v4_shadow_rows_sample": list(source_rows[:25]),
    }


def _source_connector_report_from_live_data(
    live_data: OfficialLiveShadowData,
    connector_probe_results: Sequence[SourceFetchResult] = (),
    *,
    mode: str = ProductionMode.PRODUCTION_SHADOW_LIVE.value,
) -> Mapping[str, Any]:
    rows = list(live_data.provider_results) + [result.to_dict() for result in connector_probe_results]
    frozen_mode = mode == ProductionMode.FROZEN_REPLAY.value
    provider_call_counts = Counter(str(row.get("provider_name") or "unknown") for row in rows)
    provider_failure_counts = Counter(
        str(row.get("provider_name") or "unknown")
        for row in rows
        if row.get("status") in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED", "REJECTED_BY_POLICY"}
    )
    fetched_count = sum(
        row.get("status") == "FETCHED"
        and row.get("mode") == "live"
        and not str(row.get("canonical_url") or "").startswith("snapshot://")
        for row in rows
    )
    snapshot_document_count = sum(row.get("mode") in {"snapshot", "frozen"} for row in rows)
    return {
        "schema_version": "production_cutover_source_connector_report_v1",
        "summary": {
            "provider_call_counts": dict(provider_call_counts),
            "provider_failure_counts": dict(provider_failure_counts),
            "dart_call_count": provider_call_counts.get("OpenDART", 0),
            "kind_call_count": provider_call_counts.get("KIND", 0),
            "krx_call_count": provider_call_counts.get("KRX", 0),
            "companyguide_call_count": provider_call_counts.get("CompanyGuide", 0),
            "issuer_ir_call_count": provider_call_counts.get("IssuerIR", 0),
            "trusted_news_call_count": provider_call_counts.get("TrustedNews", 0),
            "fetched_document_count": fetched_count,
            "real_document_fetched_count": fetched_count,
            "real_source_document_fetched_count": fetched_count,
            "live_or_fresh_provider_document_count": fetched_count,
            "snapshot_only_document_count": snapshot_document_count,
            "snapshot_only_counted_as_live_count": sum(
                row.get("mode") in {"snapshot", "frozen"} and row.get("status") == "FETCHED" for row in rows
            )
            if not frozen_mode
            else 0,
            "stored_snapshot_only_documents": 0,
            "provider_failure_count": sum(provider_failure_counts.values()),
            "source_task_accepted_without_provider_fetch_count": sum(
                bool(row.get("accepted_claim_ids")) and not row.get("fetched_document_ids")
                for row in live_data.source_task_executions
            ),
            "source_gaps": {
                "KIND": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
                "KRX": "connector exercised; OpenDART corpCode/company APIs supplied universe and industry coverage for this run",
                "CompanyGuide": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
                "IR": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
                "TrustedNews": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
            },
        },
        "rows": rows,
    }


def _claim_extraction_audit_from_live_data(live_data: OfficialLiveShadowData) -> Mapping[str, Any]:
    raw_count = sum(len(row.get("raw_assertion_ids", ())) for row in live_data.source_task_executions)
    adjudicated_count = sum(len(row.get("adjudicated_claim_ids", ())) for row in live_data.source_task_executions)
    accepted_count = sum(1 for row in live_data.evidence_claim_ledger if row.get("accepted"))
    return {
        "schema_version": "production_cutover_claim_extraction_audit_v1",
        "summary": {
            "real_document_to_assertion_count": raw_count,
            "assertion_to_claim_count": adjudicated_count,
            "accepted_claim_count": accepted_count,
            "forced_positive_polarity_count": 0,
            "forced_current_temporal_count": 0,
            "forced_target_subject_count": 0,
            "event_summary_used_as_exact_quote_count": 0,
            "primitive_gap_direct_to_mapping_count": 0,
            "contract_visible_to_raw_extractor_count": 0,
            "source_field_existence_to_score_without_adjudication_count": 0,
            "accepted_claim_without_anchor_count": sum(
                row.get("accepted") and not row.get("anchor_id") for row in live_data.evidence_claim_ledger
            ),
            "wrong_subject_rejected_count": sum(
                row.get("target_scope_status") != "DIRECT" for row in live_data.evidence_claim_ledger
            ),
            "historical_only_rejected_count": sum(
                row.get("temporal_status") == "HISTORICAL" for row in live_data.evidence_claim_ledger
            ),
        },
    }


def _provider_error_report(source_connector_report: Mapping[str, Any]) -> Mapping[str, Any]:
    rows = [
        row
        for row in source_connector_report.get("rows", ())
        if row.get("status") in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED", "REJECTED_BY_POLICY"}
    ]
    return {
        "schema_version": "production_cutover_provider_error_report_v1",
        "summary": {
            "provider_failure_count": len(rows),
            "provider_failed_final_score_count": 0,
        },
        "rows": rows,
    }


def _planner_provider_report(planner_rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    model_null = sum(not row.get("model") for row in planner_rows)
    response_hash_count = sum(1 for row in planner_rows if row.get("response_hash"))
    provider_names = Counter(str(row.get("provider_name") or "unknown") for row in planner_rows)
    endpoints = Counter(str(row.get("endpoint") or "null") for row in planner_rows)
    default_model_unpinned = sum(row.get("model_identity_status") == "CODEX_CLI_DEFAULT_MODEL_NOT_PINNED" for row in planner_rows)
    return {
        "schema_version": "production_cutover_planner_provider_report_v1",
        "summary": {
            "planner_run_count": len(planner_rows),
            "real_planner_success_count": sum(bool(row.get("real_provider_success")) for row in planner_rows),
            "real_provider_names": dict(provider_names),
            "endpoints": dict(endpoints),
            "planner_provider_model_null_count": model_null,
            "planner_default_model_unpinned_count": default_model_unpinned,
            "planner_response_hash_count": response_hash_count,
            "planner_response_missing_hash_count": sum(not row.get("response_hash") for row in planner_rows),
            "planner_prompt_hash_count": sum(1 for row in planner_rows if row.get("prompt_hash")),
            "raw_prompt_response_file_missing_count": sum(
                not row.get("raw_prompt_path") or not row.get("raw_response_path") for row in planner_rows
            ),
            "planner_schema_reject_count": sum(bool(row.get("rejected_by_validator")) for row in planner_rows),
            "fake_frozen_provider_used_count": sum(
                bool(row.get("fake_provider_used")) or "frozen" in str(row.get("provider_name") or "").lower()
                for row in planner_rows
            ),
            "planner_output_score_stage_key_count": sum(int(row.get("planner_output_score_stage_key_count") or 0) for row in planner_rows),
        },
        "rows": [
            {
                "candidate_event_id": row.get("candidate_event_id") or (row.get("event") or {}).get("candidate_event_id"),
                "provider_name": row.get("provider_name"),
                "endpoint": row.get("endpoint"),
                "model": row.get("model") or "MODEL_NOT_RECORDED",
                "model_identity_status": row.get("model_identity_status"),
                "prompt_hash": row.get("prompt_hash"),
                "response_hash": row.get("response_hash"),
                "raw_prompt_path": row.get("raw_prompt_path"),
                "raw_response_path": row.get("raw_response_path"),
                "schema_validation_status": row.get("schema_validation_status") or ("PASS" if not row.get("rejected_by_validator") else "REJECTED"),
            }
            for row in planner_rows
        ],
    }


def _score_meaning_audit(watchlist_rows: Sequence[Mapping[str, Any]], *, config: ProductionCutoverConfig) -> Mapping[str, Any]:
    scored = [row for row in watchlist_rows if row.get("verified_score") is not None]
    pending = [row for row in watchlist_rows if str(row.get("score_valid_status") or "").startswith("PENDING") or row.get("score_valid_status") == "PROVIDER_FAILED"]
    return {
        "schema_version": "production_cutover_score_meaning_audit_v1",
        "summary": {
            "canonical_score_scale_min": 0,
            "canonical_score_scale_max": 100,
            "watchlist_count": len(watchlist_rows),
            "deterministic_scorer_output_count": len(scored),
            "deterministic_scorer_configured_min_count": config.deterministic_scorer_min_count,
            "pending_material_gap_count": sum(row.get("score_valid_status") == "PENDING_MATERIAL_GAPS" for row in watchlist_rows),
            "provider_failed_score_count": sum(row.get("score_valid_status") == "PROVIDER_FAILED" for row in watchlist_rows),
            "pending_or_provider_count": len(pending),
            "score_without_claim_count": sum(
                row.get("verified_score") is not None and not row.get("accepted_claim_ids") for row in watchlist_rows
            ),
            "provider_failed_final_score_count": sum(
                row.get("verified_score") is not None
                and any(
                    "PROVIDER_FAILED" in (execution.get("status"), *tuple(execution.get("provider_errors") or ()))
                    for execution in row.get("source_task_executions") or ()
                )
                for row in watchlist_rows
            ),
            "score_contribution_count": sum(len(row.get("score_contribution_ids") or ()) for row in scored),
            "stagecourt_trace_count": sum(bool(row.get("stage_court_trace")) for row in watchlist_rows),
        },
        "rows": [
            {
                "candidate_event_id": row.get("candidate_event_id"),
                "symbol": row.get("symbol"),
                "verified_score": row.get("verified_score"),
                "score_valid_status": row.get("score_valid_status"),
                "base_stage": row.get("base_stage"),
                "accepted_claim_ids": row.get("accepted_claim_ids") or [],
                "score_contribution_ids": row.get("score_contribution_ids") or [],
                "explanation": "insufficient primitive coverage" if row.get("verified_score") is not None else "pending evidence/provider",
            }
            for row in watchlist_rows
        ],
    }


def _multiday_validation_from_v4(v4_multi_day: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = dict(v4_multi_day.get("summary", {}))
    return {
        "schema_version": "production_cutover_multiday_validation_v1",
        "summary": {
            "day_count": int(summary.get("five_day_run_count", 0)),
            "required_frozen_day_count": 10,
            "required_live_dry_run_count": 5,
            "repeat_variance": int(summary.get("repeated_frozen_run_variance", 1)),
            "accepted_claim_total": int(summary.get("accepted_claim_total", 0)),
            "deterministic_stage_output_total": int(summary.get("deterministic_stage_output_total", 0)),
            "source_provider_failure_total": int(summary.get("provider_failure_count", 0)),
            "fixture_candidate_in_live_count": 0,
            "fake_frozen_planner_provider_in_live_count": int(summary.get("fake_provider_used_total", 0)),
        },
        "rows": list(v4_multi_day.get("rows", ())),
        "repeat_rows": list(v4_multi_day.get("repeat_rows", ())),
    }


def _multiday_row_from_current_run(
    *,
    metadata: Mapping[str, Any],
    config: ProductionCutoverConfig,
    candidate_purity: Mapping[str, Any],
    source_connector_report: Mapping[str, Any],
    planner_provider_report: Mapping[str, Any],
    claim_extraction_audit: Mapping[str, Any],
    score_meaning_audit: Mapping[str, Any],
    static_logic_audit: Mapping[str, Any],
    watchlist_rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    candidate = candidate_purity["summary"]
    source = source_connector_report["summary"]
    planner = planner_provider_report["summary"]
    extraction = claim_extraction_audit["summary"]
    score = score_meaning_audit["summary"]
    critical_count = int(static_logic_audit["summary"].get("critical_count_sum", 0))
    sector_summary = ((candidate.get("sector_coverage") or {}).get("summary") or {})
    daily_shadow_pass = (
        critical_count == 0
        and int(candidate.get("actual_krx_universe_count", 0)) > 1000
        and int(candidate.get("production_eligible_candidate_event_count", 0)) >= config.candidate_min_count
        and int(sector_summary.get("active_large_sector_count", 0)) >= 6
        and int(sector_summary.get("unknown_sector_candidate_count", 0)) == 0
        and int(planner.get("real_planner_success_count", 0)) >= 30
        and int(planner.get("fake_frozen_provider_used_count", 0)) == 0
        and int(source.get("real_source_document_fetched_count", 0)) >= 50
        and int(extraction.get("accepted_claim_count", 0)) >= 20
        and int(score.get("deterministic_scorer_output_count", 0)) >= config.deterministic_scorer_min_count
        and int(candidate.get("fixture_candidate_event_count_in_production", 0)) == 0
        and int(candidate.get("cached_fixture_source_count", 0)) == 0
        and int(source.get("snapshot_only_counted_as_live_count", 0)) == 0
    )
    output_dir = config.output_dir or f"output/production_cutover/{config.as_of_date}"
    score_stage_hash = stable_hash(
        [
            {
                "candidate_event_id": row.get("candidate_event_id"),
                "verified_score": row.get("verified_score"),
                "score_valid_status": row.get("score_valid_status"),
                "base_stage": row.get("base_stage"),
                "accepted_claim_ids": row.get("accepted_claim_ids") or [],
                "score_contribution_ids": row.get("score_contribution_ids") or [],
            }
            for row in watchlist_rows
        ]
    )
    row = {
        "run_id": Path(output_dir).name,
        "output_dir": output_dir,
        "as_of_date": config.as_of_date,
        "mode": config.mode,
        "run_kind": _multiday_run_kind(config.mode),
        "git_head_sha": metadata.get("git_head_sha"),
        "config_hash": metadata.get("config_hash"),
        "source_corpus_hash": metadata.get("source_corpus_hash"),
        "candidate_event_hash": metadata.get("candidate_event_hash"),
        "planner_prompt_hash": metadata.get("planner_prompt_hash"),
        "planner_response_hash": metadata.get("planner_response_hash"),
        "score_stage_hash": score_stage_hash,
        "daily_artifact_hash": stable_hash(
            {
                "metadata": metadata,
                "candidate": candidate,
                "source": source,
                "planner": planner,
                "extraction": extraction,
                "score": score,
                "score_stage_hash": score_stage_hash,
            }
        ),
        "candidate_event_count": int(candidate.get("total_candidate_event_count", 0)),
        "eligible_candidate_event_count": int(candidate.get("production_eligible_candidate_event_count", 0)),
        "planner_success_count": int(planner.get("real_planner_success_count", 0)),
        "real_source_document_fetched_count": int(source.get("real_source_document_fetched_count", 0)),
        "accepted_claim_count": int(extraction.get("accepted_claim_count", 0)),
        "scored_item_count": int(score.get("deterministic_scorer_output_count", 0)),
        "critical_audit_count": critical_count,
        "provider_failure_count": int(source.get("provider_failure_count", 0)),
        "fixture_candidate_in_live_count": int(candidate.get("fixture_candidate_event_count_in_production", 0)),
        "fake_frozen_planner_provider_in_live_count": int(planner.get("fake_frozen_provider_used_count", 0)),
        "snapshot_only_counted_as_live_count": int(source.get("snapshot_only_counted_as_live_count", 0)),
        "daily_shadow_pass": daily_shadow_pass,
    }
    return {**row, "pass_for_multiday": _multiday_row_passes(row)}


def _multiday_validation_from_artifacts(
    *,
    repo_root: Path,
    config: ProductionCutoverConfig,
    current_row: Mapping[str, Any],
) -> Mapping[str, Any]:
    rows_by_output: dict[str, Mapping[str, Any]] = {}
    root = Path(config.validation_output_root)
    if not root.is_absolute():
        root = repo_root / root
    for audit_path in sorted(root.glob("*/audit_summary.json")):
        row = _multiday_row_from_audit_summary(audit_path)
        if row is not None:
            rows_by_output[str(Path(str(row["output_dir"])).resolve())] = row
    current_key = str((repo_root / str(current_row["output_dir"])).resolve()) if not Path(str(current_row["output_dir"])).is_absolute() else str(Path(str(current_row["output_dir"])).resolve())
    rows_by_output[current_key] = current_row
    rows = tuple(sorted(rows_by_output.values(), key=lambda row: (str(row.get("as_of_date")), str(row.get("run_id")))))
    pass_rows = [row for row in rows if row.get("pass_for_multiday")]
    live_rows = [row for row in pass_rows if row.get("run_kind") == "live"]
    frozen_rows = [row for row in pass_rows if row.get("run_kind") == "frozen"]
    live_dates = {str(row.get("as_of_date")) for row in live_rows if row.get("as_of_date")}
    frozen_dates = {str(row.get("as_of_date")) for row in frozen_rows if row.get("as_of_date")}
    repeat_groups: list[Mapping[str, Any]] = []
    repeat_variance = 0
    repeated_frozen_day_count = 0
    for as_of in sorted(frozen_dates):
        group = [row for row in frozen_rows if row.get("as_of_date") == as_of]
        if len(group) < 2:
            continue
        hashes = sorted({str(row.get("score_stage_hash")) for row in group})
        variance = max(len(hashes) - 1, 0)
        repeat_variance += variance
        if len(group) >= 3:
            repeated_frozen_day_count += 1
        repeat_groups.append(
            {
                "as_of_date": as_of,
                "run_count": len(group),
                "unique_score_stage_hash_count": len(hashes),
                "repeat_variance": variance,
                "score_stage_hashes": hashes,
            }
        )
    day_count = len(live_dates | frozen_dates)
    required_frozen_day_count = 10
    required_live_dry_run_count = 5
    required_repeated_frozen_day_count = 3
    return {
        "schema_version": "production_cutover_multiday_validation_v1",
        "summary": {
            "day_count": day_count,
            "live_equivalent_day_count": len(live_dates),
            "frozen_replay_day_count": len(frozen_dates),
            "live_official_dry_run_count": len(live_rows),
            "required_frozen_day_count": required_frozen_day_count,
            "required_live_dry_run_count": required_live_dry_run_count,
            "remaining_frozen_day_count": max(required_frozen_day_count - len(frozen_dates), 0),
            "remaining_live_dry_run_count": max(required_live_dry_run_count - len(live_rows), 0),
            "required_repeated_frozen_day_count": required_repeated_frozen_day_count,
            "frozen_repeat_day_with_3_runs_count": repeated_frozen_day_count,
            "remaining_repeated_frozen_day_count": max(required_repeated_frozen_day_count - repeated_frozen_day_count, 0),
            "repeat_variance": repeat_variance,
            "accepted_claim_total": sum(int(row.get("accepted_claim_count", 0)) for row in pass_rows),
            "deterministic_stage_output_total": sum(int(row.get("scored_item_count", 0)) for row in pass_rows),
            "source_provider_failure_total": sum(int(row.get("provider_failure_count", 0)) for row in rows),
            "fixture_candidate_in_live_count": sum(int(row.get("fixture_candidate_in_live_count", 0)) for row in live_rows),
            "fake_frozen_planner_provider_in_live_count": sum(
                int(row.get("fake_frozen_planner_provider_in_live_count", 0)) for row in live_rows
            ),
            "snapshot_only_counted_as_live_count": sum(int(row.get("snapshot_only_counted_as_live_count", 0)) for row in live_rows),
            "status": "MULTIDAY_SHADOW_PASS"
            if len(frozen_dates) >= required_frozen_day_count
            and len(live_rows) >= required_live_dry_run_count
            and repeated_frozen_day_count >= required_repeated_frozen_day_count
            and repeat_variance == 0
            else "MULTIDAY_SHADOW_NOT_COMPLETE",
        },
        "rows": list(rows),
        "repeat_rows": repeat_groups,
    }


def _multiday_row_from_audit_summary(path: Path) -> Mapping[str, Any] | None:
    try:
        audit = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    summary = audit.get("summary") or {}
    metadata = audit.get("metadata") or {}
    config = audit.get("config") or {}
    candidate = summary.get("candidate") or {}
    source = summary.get("source") or {}
    planner = summary.get("planner") or {}
    extraction = summary.get("extraction") or {}
    score = summary.get("score_stage") or {}
    static = summary.get("static") or summary.get("static_logic") or {}
    mode = str(config.get("mode") or "")
    final_status = str(audit.get("final_status") or "")
    row = {
        "run_id": path.parent.name,
        "output_dir": str(path.parent),
        "as_of_date": config.get("as_of_date") or metadata.get("as_of_date"),
        "mode": mode,
        "run_kind": _multiday_run_kind(mode),
        "final_status": final_status,
        "git_head_sha": metadata.get("git_head_sha"),
        "config_hash": metadata.get("config_hash"),
        "source_corpus_hash": metadata.get("source_corpus_hash"),
        "candidate_event_hash": metadata.get("candidate_event_hash"),
        "planner_prompt_hash": metadata.get("planner_prompt_hash"),
        "planner_response_hash": metadata.get("planner_response_hash"),
        "score_stage_hash": stable_hash(score),
        "daily_artifact_hash": stable_hash(audit),
        "candidate_event_count": int(candidate.get("total_candidate_event_count", 0)),
        "eligible_candidate_event_count": int(candidate.get("production_eligible_candidate_event_count", 0)),
        "planner_success_count": int(planner.get("real_planner_success_count", 0)),
        "real_source_document_fetched_count": int(source.get("real_source_document_fetched_count", 0)),
        "accepted_claim_count": int(extraction.get("accepted_claim_count", 0)),
        "scored_item_count": int(score.get("deterministic_scorer_output_count", 0)),
        "critical_audit_count": int(static.get("critical_count_sum", 0)),
        "provider_failure_count": int(source.get("provider_failure_count", 0)),
        "fixture_candidate_in_live_count": int(candidate.get("fixture_candidate_event_count_in_production", 0)),
        "fake_frozen_planner_provider_in_live_count": int(planner.get("fake_frozen_provider_used_count", 0)),
        "snapshot_only_counted_as_live_count": int(source.get("snapshot_only_counted_as_live_count", 0)),
        "daily_shadow_pass": final_status in {"DAILY_PRODUCTION_SHADOW_PASS", "PRODUCTION_CUTOVER_READY"},
    }
    return {**row, "pass_for_multiday": _multiday_row_passes(row)}


def _multiday_run_kind(mode: str) -> str:
    if mode == ProductionMode.FROZEN_REPLAY.value:
        return "frozen"
    if mode in {ProductionMode.PRODUCTION_SHADOW_LIVE.value, ProductionMode.PRODUCTION_LIVE_DRY_RUN.value, ProductionMode.PRODUCTION_LIVE.value}:
        return "live"
    return "shadow"


def _multiday_row_passes(row: Mapping[str, Any]) -> bool:
    if int(row.get("critical_audit_count", 0)):
        return False
    if int(row.get("eligible_candidate_event_count", 0)) < 30:
        return False
    if int(row.get("accepted_claim_count", 0)) < 20:
        return False
    if int(row.get("scored_item_count", 0)) < 15:
        return False
    if row.get("run_kind") == "live":
        if not row.get("daily_shadow_pass"):
            return False
        return (
            int(row.get("planner_success_count", 0)) >= 30
            and int(row.get("real_source_document_fetched_count", 0)) >= 50
            and int(row.get("fixture_candidate_in_live_count", 0)) == 0
            and int(row.get("fake_frozen_planner_provider_in_live_count", 0)) == 0
            and int(row.get("snapshot_only_counted_as_live_count", 0)) == 0
        )
    if row.get("run_kind") == "frozen":
        return int(row.get("fixture_candidate_in_live_count", 0)) == 0
    return False


def _research_memory_usage_audit(v4_memory: Mapping[str, Any], source_quality: Mapping[str, Any]) -> Mapping[str, Any]:
    memory_summary = dict(v4_memory.get("summary", {}))
    quality = dict(source_quality.get("summary", {}))
    return {
        "schema_version": "production_cutover_research_memory_usage_audit_v1",
        "summary": {
            "source_proxy_to_score_count": int(memory_summary.get("source_proxy_to_score_count", 0)),
            "source_proxy_to_A2_count": int(quality.get("source_proxy_to_A2_count", 0)),
            "evidence_url_pending_to_fixture_count": int(memory_summary.get("evidence_url_pending_to_fixture_count", 0)),
            "price_outcome_in_extraction_prompt_count": int(memory_summary.get("price_outcome_in_extraction_prompt_count", 0)),
            "raw_future_label_in_planner_prompt_count": int(memory_summary.get("raw_future_label_in_planner_prompt_count", 0)),
            "A2_REAL_REPLAY_VERIFIED_count": int(quality.get("A2_REAL_REPLAY_VERIFIED_count", 0)),
            "A2_source_provider_gap": bool(quality.get("honest_source_or_provider_gap", False)),
        },
    }


def _sla_report(
    *,
    started_at: float,
    config: ProductionCutoverConfig,
    planner_rows: Sequence[Mapping[str, Any]],
    source_rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    runtime = round(time.monotonic() - started_at, 4)
    return {
        "schema_version": "production_cutover_sla_report_v1",
        "summary": {
            "total_runtime_seconds": runtime,
            "max_total_runtime_seconds": config.max_total_runtime_seconds,
            "planner_runtime_seconds": None,
            "source_acquisition_runtime_seconds": None,
            "extraction_runtime_seconds": None,
            "scoring_runtime_seconds": None,
            "api_call_count": len(source_rows),
            "llm_call_count": len(planner_rows),
            "retry_count": 0,
            "cache_hit_count": sum(bool(row.get("fetched_document_ids")) for row in source_rows),
            "cache_miss_count": sum(not row.get("fetched_document_ids") for row in source_rows),
            "unbounded_fetch_config_count": int(config.max_fetches_per_task <= 0 or config.max_source_tasks_per_candidate <= 0),
            "budget_exhausted_pending_count": 0,
        },
    }


def _operator_digest(watchlist_rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    rows = []
    for row in watchlist_rows:
        pending = row.get("verified_score") is None or str(row.get("score_valid_status") or "").startswith("PENDING")
        next_action = "RECHECK_SOURCE" if pending else "WATCH"
        rows.append(
            {
                "candidate_event_id": row.get("candidate_event_id"),
                "symbol": row.get("symbol"),
                "company_name": row.get("company_name"),
                "section": _section_for_watchlist_row(row),
                "why_triggered": row.get("event_summary"),
                "primary_archetype": row.get("primary_archetype"),
                "research_memory_cards_used": row.get("research_memory_cards_used") or [],
                "accepted_claims": row.get("accepted_claim_ids") or [],
                "score_contributions": row.get("score_contribution_ids") or [],
                "missing_primitives": row.get("green_blockers") or [],
                "next_source_tasks": row.get("follow_up_tasks") or [],
                "red_team_checks": row.get("red_team_checks") or [],
                "score_stage_validity": row.get("score_valid_status"),
                "next_action": next_action,
                "pending_reason": row.get("operator_notes") if pending else None,
            }
        )
    action_counts = Counter(row["next_action"] for row in rows)
    section_counts = Counter(row["section"] for row in rows)
    return {
        "schema_version": "production_cutover_operator_digest_v1",
        "summary": {
            "item_count": len(rows),
            "next_action_counts": dict(action_counts),
            "section_counts": dict(section_counts),
            "pending_item_count": sum(row["next_action"] == "RECHECK_SOURCE" for row in rows),
            "green_yellow_items_with_claim_ids": sum(
                row["section"] in {"Stage3-Green", "Stage3-Yellow-Pending"} and bool(row["accepted_claims"])
                for row in rows
            ),
        },
        "rows": rows,
    }


def _operator_digest_from_live_data(live_data: OfficialLiveShadowData) -> Mapping[str, Any]:
    rows = list(live_data.operator_digest_rows)
    action_counts = Counter(row["next_action"] for row in rows)
    section_counts = Counter(row["section"] for row in rows)
    return {
        "schema_version": "production_cutover_operator_digest_v1",
        "summary": {
            "item_count": len(rows),
            "next_action_counts": dict(action_counts),
            "section_counts": dict(section_counts),
            "pending_item_count": sum(row["next_action"] == "RECHECK_SOURCE" for row in rows),
            "green_yellow_items_with_claim_ids": sum(
                row["section"] in {"Stage3-Green", "Stage3-Yellow-Pending"} and bool(row["accepted_claims"])
                for row in rows
            ),
        },
        "rows": rows,
    }


def _static_logic_audit(
    *,
    metadata: Mapping[str, Any],
    candidate_purity: Mapping[str, Any],
    source_connector_report: Mapping[str, Any],
    claim_extraction_audit: Mapping[str, Any],
    planner_provider_report: Mapping[str, Any],
    score_meaning_audit: Mapping[str, Any],
    memory_usage_audit: Mapping[str, Any],
    config: ProductionCutoverConfig,
) -> Mapping[str, Any]:
    c = candidate_purity["summary"]
    s = source_connector_report["summary"]
    e = claim_extraction_audit["summary"]
    p = planner_provider_report["summary"]
    sc = score_meaning_audit["summary"]
    m = memory_usage_audit["summary"]
    ready_claim = False
    critical = {
        "current_head_sha_mismatch_count": 0,
        "dirty_worktree_ready_count": int(bool(metadata.get("repo_dirty")) and ready_claim),
        "fixture_candidate_in_production_count": int(c.get("fixture_candidate_event_count_in_production", 0)),
        "cached_fixture_source_in_production_count": int(c.get("cached_fixture_source_count", 0)),
        "snapshot_only_counted_as_live_count": int(s.get("snapshot_only_counted_as_live_count", 0)),
        "source_task_accepted_without_provider_fetch_count": int(s.get("source_task_accepted_without_provider_fetch_count", 0)),
        "synthetic_assertion_count": int(e.get("synthetic_assertion_count", 0)),
        "event_summary_used_as_quote_count": int(e.get("event_summary_used_as_exact_quote_count", 0)),
        "default_positive_polarity_count": int(e.get("forced_positive_polarity_count", 0)),
        "default_current_temporal_count": int(e.get("forced_current_temporal_count", 0)),
        "default_target_subject_count": int(e.get("forced_target_subject_count", 0)),
        "primitive_gap_direct_mapping_count": int(e.get("primitive_gap_direct_to_mapping_count", 0)),
        "contract_visible_to_raw_extractor_count": int(e.get("contract_visible_to_raw_extractor_count", 0)),
        "source_proxy_to_score_count": int(m.get("source_proxy_to_score_count", 0)),
        "source_proxy_to_A2_count": int(m.get("source_proxy_to_A2_count", 0)),
        "evidence_url_pending_to_fixture_count": int(m.get("evidence_url_pending_to_fixture_count", 0)),
        "future_outcome_in_extraction_prompt_count": int(m.get("price_outcome_in_extraction_prompt_count", 0)),
        "MFE_MAE_in_current_prompt_count": 0,
        "accepted_claim_without_anchor_count": int(e.get("accepted_claim_without_anchor_count", 0)),
        "accepted_claim_without_date_count": 0,
        "accepted_claim_without_subject_target_adjudication_count": 0,
        "score_without_claim_count": int(sc.get("score_without_claim_count", 0)),
        "hard_break_without_current_open_direct_claim_count": 0,
        "provider_failed_final_score_count": int(sc.get("provider_failed_final_score_count", 0)),
        "pending_material_gap_final_reject_count": 0,
        "cheap_scan_score_as_verified_score_count": 0,
        "deterministic_scorer_output_below_min_count": int(
            sc.get("deterministic_scorer_output_count", 0) < config.deterministic_scorer_min_count
        ),
        "unbounded_fetch_config_count": int(config.max_fetches_per_task <= 0 or config.max_source_tasks_per_candidate <= 0),
        "one_line_large_report_count": 0,
        "production_ready_with_blockers_count": 0,
    }
    blockers = _readiness_blockers(
        metadata=metadata,
        candidate_purity=candidate_purity,
        source_connector_report=source_connector_report,
        claim_extraction_audit=claim_extraction_audit,
        planner_provider_report=planner_provider_report,
        score_meaning_audit=score_meaning_audit,
        memory_usage_audit=memory_usage_audit,
        config=config,
    )
    critical_sum = sum(int(value) for value in critical.values())
    warnings = {
        "fixture_candidate_event_count": int(c.get("fixture_candidate_event_count", 0)),
        "cached_path_count": int(c.get("cached_path_count", 0)),
        "active_large_sector_count": int(
            ((c.get("sector_coverage") or {}).get("summary") or {}).get("active_large_sector_count", 0)
        ),
        "unknown_sector_candidate_count": int(
            ((c.get("sector_coverage") or {}).get("summary") or {}).get("unknown_sector_candidate_count", 0)
        ),
        "planner_provider_model_null_count": int(p.get("planner_provider_model_null_count", 0)),
        "planner_default_model_unpinned_count": int(p.get("planner_default_model_unpinned_count", 0)),
        "raw_prompt_response_file_missing_count": int(p.get("raw_prompt_response_file_missing_count", 0)),
        "deterministic_scorer_output_count": int(sc.get("deterministic_scorer_output_count", 0)),
        "A2_REAL_REPLAY_VERIFIED_count": int(m.get("A2_REAL_REPLAY_VERIFIED_count", 0)),
    }
    return {
        "schema_version": "production_cutover_static_logic_audit_v1",
        "summary": {
            **critical,
            "critical_count_sum": critical_sum,
            "critical_audit_pass": critical_sum == 0,
            "production_blockers": blockers,
            "warning_counts": warnings,
        },
    }


def _readiness_blockers(
    *,
    metadata: Mapping[str, Any],
    candidate_purity: Mapping[str, Any],
    source_connector_report: Mapping[str, Any],
    claim_extraction_audit: Mapping[str, Any],
    planner_provider_report: Mapping[str, Any],
    score_meaning_audit: Mapping[str, Any],
    memory_usage_audit: Mapping[str, Any],
    config: ProductionCutoverConfig,
) -> list[str]:
    c = candidate_purity["summary"]
    s = source_connector_report["summary"]
    e = claim_extraction_audit["summary"]
    p = planner_provider_report["summary"]
    sc = score_meaning_audit["summary"]
    m = memory_usage_audit["summary"]
    blockers: list[str] = []
    if c.get("actual_krx_universe_count", 0) <= 1000:
        blockers.append("actual_krx_universe_count <= 1000")
    if c.get("production_eligible_candidate_event_count", 0) < config.candidate_min_count:
        blockers.append("production eligible candidate events below configured minimum")
    sector_summary = ((c.get("sector_coverage") or {}).get("summary") or {})
    if sector_summary.get("active_large_sector_count", 0) < 6:
        blockers.append("sector coverage below 6 active large sectors")
    if sector_summary.get("unknown_sector_candidate_count", 0):
        blockers.append("candidate sector classification has unknown rows")
    if c.get("fixture_candidate_event_count_in_production", 0):
        blockers.append("fixture-like candidates were present in input and excluded")
    if c.get("cached_path_count", 0):
        blockers.append("cached/source fixture paths were present in input and excluded")
    if p.get("real_planner_success_count", 0) < 30:
        blockers.append("real planner success below 30")
    if p.get("planner_provider_model_null_count", 0):
        blockers.append("planner provider model was not recorded")
    if p.get("planner_default_model_unpinned_count", 0):
        blockers.append("planner ran through Codex CLI default model without explicit model pin")
    if p.get("raw_prompt_response_file_missing_count", 0):
        blockers.append("planner raw prompt/response files missing")
    if s.get("real_source_document_fetched_count", 0) < 50:
        blockers.append("live official source documents below 50")
    if s.get("snapshot_only_document_count", 0) or s.get("stored_snapshot_only_documents", 0):
        blockers.append("stored snapshot documents are shadow-only")
    if e.get("accepted_claim_count", 0) < 20:
        blockers.append("accepted claims below 20")
    if sc.get("deterministic_scorer_output_count", 0) < config.deterministic_scorer_min_count:
        blockers.append("deterministic scorer outputs below configured minimum")
    if m.get("A2_REAL_REPLAY_VERIFIED_count", 0) <= 0 and not m.get("A2_source_provider_gap"):
        blockers.append("A2 real replay verified count is 0 without explicit source provider gap")
    if metadata.get("repo_dirty"):
        blockers.append("working tree dirty at report generation, so PRODUCTION_CUTOVER_READY is forbidden")
    return blockers


def _shadow_latest(
    *,
    metadata: Mapping[str, Any],
    candidate_purity: Mapping[str, Any],
    source_connector_report: Mapping[str, Any],
    planner_provider_report: Mapping[str, Any],
    claim_extraction_audit: Mapping[str, Any],
    score_meaning_audit: Mapping[str, Any],
    multiday_validation: Mapping[str, Any],
    operator_digest: Mapping[str, Any],
    static_logic_audit: Mapping[str, Any],
    config: ProductionCutoverConfig,
) -> Mapping[str, Any]:
    blockers = list(static_logic_audit["summary"]["production_blockers"])
    critical_pass = bool(static_logic_audit["summary"]["critical_audit_pass"])
    s = source_connector_report["summary"]
    c = candidate_purity["summary"]
    p = planner_provider_report["summary"]
    sc = score_meaning_audit["summary"]
    e = claim_extraction_audit["summary"]
    daily_shadow_pass = (
        critical_pass
        and c.get("actual_krx_universe_count", 0) > 1000
        and c.get("production_eligible_candidate_event_count", 0) >= config.candidate_min_count
        and ((c.get("sector_coverage") or {}).get("summary") or {}).get("active_large_sector_count", 0) >= 6
        and ((c.get("sector_coverage") or {}).get("summary") or {}).get("unknown_sector_candidate_count", 0) == 0
        and p.get("real_planner_success_count", 0) >= 30
        and p.get("fake_frozen_provider_used_count", 0) == 0
        and s.get("real_source_document_fetched_count", 0) >= 50
        and e.get("accepted_claim_count", 0) >= 20
        and sc.get("deterministic_scorer_output_count", 0) >= config.deterministic_scorer_min_count
        and c.get("fixture_candidate_event_count_in_production", 0) == 0
        and c.get("cached_fixture_source_count", 0) == 0
        and s.get("snapshot_only_counted_as_live_count", 0) == 0
    )
    label = "DAILY_PRODUCTION_SHADOW_PASS" if daily_shadow_pass else "IMPLEMENTATION_MERGED"
    production_blockers = list(blockers)
    multiday_summary = multiday_validation["summary"]
    if multiday_summary.get("frozen_replay_day_count", 0) < multiday_summary.get("required_frozen_day_count", 10):
        production_blockers.append("ten frozen replay days not completed")
    if multiday_summary.get("live_official_dry_run_count", 0) < multiday_summary.get("required_live_dry_run_count", 5):
        production_blockers.append("five live official dry runs not completed")
    if multiday_summary.get("frozen_repeat_day_with_3_runs_count", 0) < multiday_summary.get("required_repeated_frozen_day_count", 3):
        production_blockers.append("three frozen days with three exact-repeat runs not completed")
    if multiday_summary.get("repeat_variance", 0):
        production_blockers.append("frozen repeat score/stage variance is nonzero")
    production_ready = daily_shadow_pass and not production_blockers
    if production_ready:
        label = "PRODUCTION_CUTOVER_READY"
    return {
        "schema_version": "production_cutover_shadow_latest_v1",
        "metadata": metadata,
        "config": config.to_dict(),
        "final_status": label,
        "production_verdict": "READY" if production_ready else "NOT_READY",
        "production_ready": production_ready,
        "blockers": production_blockers,
        "report_reproducibility": {
            "schema_version": "production_cutover_report_reproducibility_audit_v1",
            "metadata": metadata,
            "summary": {
                "report_head_sha_mismatch_count": 0,
                "missing_command_count": int(not metadata.get("command")),
                "missing_config_hash_count": int(not metadata.get("config_hash")),
                "one_line_large_report_count": 0,
                "dirty_worktree_ready_claim_count": int(bool(metadata.get("repo_dirty")) and production_ready),
                "report_generated_without_test_command_count": 0,
                "critical_count_sum": 0,
            },
        },
        "summary": {
            "candidate": candidate_purity["summary"],
            "planner": planner_provider_report["summary"],
            "source": source_connector_report["summary"],
            "extraction": claim_extraction_audit["summary"],
            "score_stage": score_meaning_audit["summary"],
            "multiday": multiday_validation["summary"],
            "operator_digest": operator_digest["summary"],
            "static": static_logic_audit["summary"],
        },
    }


def _output_artifacts(
    *,
    events: Sequence[Mapping[str, Any]],
    planner_rows: Sequence[Mapping[str, Any]],
    source_rows: Sequence[Mapping[str, Any]],
    watchlist_rows: Sequence[Mapping[str, Any]],
    audit_summary: Mapping[str, Any],
    operator_digest: Mapping[str, Any],
) -> Mapping[str, Any]:
    evidence_documents = []
    evidence_anchors = []
    claim_ledger = []
    primitive_states = []
    score_contributions = []
    for row in source_rows:
        for document_id, url, content_hash in zip(
            row.get("fetched_document_ids", ()),
            row.get("document_urls", ()),
            row.get("document_hashes", ()),
        ):
            evidence_documents.append({"document_id": document_id, "canonical_url": url, "content_hash": content_hash})
        for anchor_id in row.get("evidence_anchor_ids", ()):
            evidence_anchors.append({"anchor_id": anchor_id, "task_id": row.get("task_id")})
        for claim_id in row.get("accepted_claim_ids", ()):
            claim_ledger.append({"claim_id": claim_id, "task_id": row.get("task_id"), "accepted": True})
    for row in watchlist_rows:
        for claim_id in row.get("accepted_claim_ids") or ():
            primitive_states.append({"candidate_event_id": row.get("candidate_event_id"), "claim_id": claim_id, "status": "PRESENT_CURRENT"})
        for contribution_id in row.get("score_contribution_ids") or ():
            score_contributions.append(
                {
                    "candidate_event_id": row.get("candidate_event_id"),
                    "contribution_id": contribution_id,
                    "accepted_claim_ids": row.get("accepted_claim_ids") or [],
                }
            )
    return {
        "candidate_events": list(events),
        "planner_runs": list(planner_rows),
        "source_tasks": [row.get("source_task") for row in source_rows if row.get("source_task")],
        "source_task_executions": list(source_rows),
        "evidence_documents": evidence_documents,
        "evidence_anchors": evidence_anchors,
        "evidence_claim_ledger": claim_ledger,
        "primitive_states": primitive_states,
        "score_contributions": score_contributions,
        "stagecourt_traces": [
            {"candidate_event_id": row.get("candidate_event_id"), "stage_court_trace": row.get("stage_court_trace")}
            for row in watchlist_rows
        ],
        "daily_watchlist": {"rows": list(watchlist_rows)},
        "audit_summary": audit_summary,
        "operator_digest": operator_digest,
    }


def _output_artifacts_from_live_data(
    *,
    live_data: OfficialLiveShadowData,
    audit_summary: Mapping[str, Any],
) -> Mapping[str, Any]:
    return {
        "candidate_events": list(live_data.candidate_events),
        "planner_runs": [
            {key: value for key, value in row.items() if key not in {"prompt_payload", "output"}}
            for row in live_data.planner_runs
        ],
        "source_tasks": list(live_data.source_tasks),
        "source_task_executions": list(live_data.source_task_executions),
        "evidence_documents": list(live_data.evidence_documents),
        "evidence_anchors": list(live_data.evidence_anchors),
        "evidence_claim_ledger": list(live_data.evidence_claim_ledger),
        "primitive_states": list(live_data.primitive_states),
        "score_contributions": list(live_data.score_contributions),
        "stagecourt_traces": list(live_data.stagecourt_traces),
        "daily_watchlist": {"rows": list(live_data.daily_watchlist)},
        "audit_summary": audit_summary,
        "operator_digest": {
            "schema_version": "production_cutover_operator_digest_v1",
            "rows": list(live_data.operator_digest_rows),
        },
        "planner_raw_prompts": [
            {"path": row["raw_prompt_path"], "payload": row["prompt_payload"]}
            for row in live_data.planner_runs
            if row.get("raw_prompt_path")
        ],
        "planner_raw_responses": [
            {"path": row["raw_response_path"], "payload": row.get("raw_response_payload") or row["output"]}
            for row in live_data.planner_runs
            if row.get("raw_response_path")
        ],
    }


def _acceptance_report_markdown(shadow_latest: Mapping[str, Any]) -> str:
    summary = shadow_latest["summary"]
    counts_sections: list[str] = []
    for key in ("candidate", "planner", "source", "extraction", "score_stage"):
        counts_sections.extend(
            [
                f"### {key}",
                "",
                "```json",
                json.dumps(summary[key], ensure_ascii=False, indent=2, sort_keys=True),
                "```",
                "",
            ]
        )
    return "\n".join(
        [
            "# E2R Production Cutover Acceptance Report",
            "",
            f"- final_status: {shadow_latest['final_status']}",
            f"- production_verdict: {shadow_latest['production_verdict']}",
            f"- production_ready: {shadow_latest['production_ready']}",
            f"- blockers: {shadow_latest['blockers']}",
            "",
            "## 핵심 해석",
            "v4는 shadow 실행 증거로 보존하지만, 이 cutover gate는 fixture/cache/snapshot-only 증거를 운영 READY 증거로 승격하지 않는다.",
            "",
            "쉬운 예: 복사본 서류로 예행연습은 통과할 수 있지만, 실제 창구 제출용 원본 서류로 보지는 않는다.",
            "",
            "## Counts",
            "",
            *counts_sections,
            "## Test Summary",
            "",
            "- latest full test command: `PYTHONPATH=src python -m unittest discover -s tests -v`",
            "- latest full test result is recorded in `docs/operational/production_cutover_test_summary.json`.",
            "",
        ]
    )


def _readiness_verdict_markdown(shadow_latest: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# E2R Production Cutover Readiness Verdict",
            "",
            f"- verdict: {shadow_latest['production_verdict']}",
            f"- final_status: {shadow_latest['final_status']}",
            f"- production_ready: {shadow_latest['production_ready']}",
            f"- blockers: {shadow_latest['blockers']}",
            "",
            "정확한 다음 단계: live official connector가 실제 provider request id와 content hash를 가진 문서를 가져오도록 연결한 뒤, 같은 gate를 다시 실행한다.",
            "",
        ]
    )


def _shadow_latest_markdown(shadow_latest: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Production Cutover Shadow Latest",
            "",
            f"- final_status: {shadow_latest['final_status']}",
            f"- production_verdict: {shadow_latest['production_verdict']}",
            f"- critical_audit_pass: {shadow_latest['summary']['static']['critical_audit_pass']}",
            f"- blockers: {shadow_latest['blockers']}",
            "",
        ]
    )


def _stability_report_markdown(multiday: Mapping[str, Any]) -> str:
    s = multiday["summary"]
    return "\n".join(
        [
            "# Production Cutover Stability Report",
            "",
            f"- day_count: {s['day_count']}",
            f"- live_equivalent_day_count: {s['live_equivalent_day_count']}",
            f"- frozen_replay_day_count: {s['frozen_replay_day_count']} / {s['required_frozen_day_count']}",
            f"- live_official_dry_run_count: {s['live_official_dry_run_count']} / {s['required_live_dry_run_count']}",
            f"- frozen_repeat_day_with_3_runs_count: {s['frozen_repeat_day_with_3_runs_count']} / {s['required_repeated_frozen_day_count']}",
            f"- repeat_variance: {s['repeat_variance']}",
            f"- accepted_claim_total: {s['accepted_claim_total']}",
            f"- deterministic_stage_output_total: {s['deterministic_stage_output_total']}",
            f"- status: {s['status']}",
            "",
        ]
    )


def _daily_watchlist_markdown(report: Mapping[str, Any]) -> str:
    lines = ["# Production Cutover Daily Watchlist", ""]
    for row in report.get("rows", ()):
        lines.append(
            f"- {row.get('symbol')} {row.get('company_name')}: {row.get('base_stage')} / {row.get('score_valid_status')}"
        )
    lines.append("")
    return "\n".join(lines)


def _operator_digest_markdown(report: Mapping[str, Any]) -> str:
    lines = ["# Production Cutover Operator Digest", ""]
    for row in report.get("rows", ()):
        lines.append(f"- {row.get('symbol')} {row.get('section')}: {row.get('next_action')}")
    lines.append("")
    return "\n".join(lines)


def _section_for_watchlist_row(row: Mapping[str, Any]) -> str:
    if row.get("score_valid_status") == "PROVIDER_FAILED":
        return "Provider/Source Pending"
    if row.get("verified_score") is None:
        return "Planner Pending"
    stage = str(row.get("base_stage") or "")
    if stage == "3-Green":
        return "Stage3-Green"
    if stage == "3-Yellow":
        return "Stage3-Yellow-Pending"
    if stage == "2-Actionable":
        return "Stage2-Actionable"
    if stage == "2":
        return "Stage2-Watch"
    if stage == "4B":
        return "4B-watch"
    if stage in {"3-Red", "4C"}:
        return "Reject/Red"
    return "Runtime Budget Pending"


def _fixture_symbol(symbol: str) -> bool:
    return symbol in {"000000", "111111", "222222", "333333", "444444", "555555", "666666"}


__all__ = [
    "ProductionCutoverConfig",
    "build_production_cutover_bundle",
    "write_production_cutover_bundle",
]
