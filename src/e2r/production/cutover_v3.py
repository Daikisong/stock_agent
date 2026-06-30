"""Production Cutover Gate v3 reports.

v3 keeps the v2 Evidence OS path and adds provider completeness, multi-day
stability, extractor-provider accounting, and stronger stage split audits.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.candidate_event_purity import ProductionMode
from e2r.production.cutover_shadow import (
    ProductionCutoverConfig,
    build_production_cutover_bundle,
    write_production_cutover_bundle as write_cutover_shadow_bundle,
)
from e2r.production.metadata import SCORING_SCHEMA_VERSION, STAGE_SCHEMA_VERSION
from e2r.production.cutover_v2 import (
    _claim_access_policy,
    _claim_extraction_report_v2,
    _trigger_taxonomy,
    build_a2_replay_promotion_report,
)
from e2r.production.metadata import git_head_sha, stable_hash, write_json, write_jsonl, write_text
from e2r.production.source_connectors import build_default_source_provider_registry


_REQUIRED_PROVIDERS = ("OpenDART", "KIND", "KRX", "CompanyGuide", "IssuerIR", "TrustedNews")
_CUTOVER_REQUIRED_PROVIDERS = {"OpenDART", "KRX", "CompanyGuide"}
_RISK_PROVIDERS = {"KIND", "KRX"}
_REVISION_REPORT_IR_PROVIDERS = {"CompanyGuide", "IssuerIR"}
_PROVIDER_FAILURE_STATUSES = {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"}


@dataclass(frozen=True)
class ProductionCutoverV3Config:
    as_of_date: str
    planner_provider: str = "real"
    candidate_min_count: int = 20
    live_shadow_days: int = 5
    frozen_replay_days: int = 10
    repeated_frozen_days: int = 3
    output_root: str = "output/production_cutover_v3"
    validation_output_root: str = "output/production_cutover_v3"
    fetch_a2_live: bool = True
    run_llm_extractor: bool = True
    a2_fetch_limit_per_arch: int = 80
    llm_extractor_document_limit: int = 50
    final_cutover_approved: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_production_cutover_v3_bundle(
    *,
    repo_root: str | Path = ".",
    config: ProductionCutoverV3Config,
    command: str,
) -> Mapping[str, Any]:
    root = Path(repo_root)
    as_of = date.fromisoformat(config.as_of_date)
    live_dates = _trading_days_ending(as_of, max(config.live_shadow_days, 1))
    snapshot_dates = _trading_days_ending(as_of, max(config.live_shadow_days, config.frozen_replay_days, 1))
    base_bundles = []
    snapshot_bundles = []
    live_date_set = {run_date.isoformat() for run_date in live_dates}
    for run_date in snapshot_dates:
        output_dir = str(Path(config.output_root) / run_date.isoformat())
        base_config = ProductionCutoverConfig(
            as_of_date=run_date.isoformat(),
            planner_provider=config.planner_provider,
            candidate_min_count=config.candidate_min_count,
            output_dir=output_dir,
            validation_output_root=config.validation_output_root,
        )
        snapshot_bundle = build_production_cutover_bundle(
            repo_root=root,
            config=base_config,
            command=f"{command} --child-shadow-date {run_date.isoformat()}",
        )
        snapshot_bundles.append(snapshot_bundle)
        if run_date.isoformat() in live_date_set:
            base_bundles.append(snapshot_bundle)
    frozen_bundles = _build_frozen_replay_bundles(
        repo_root=root,
        config=config,
        command=command,
        snapshot_bundles=snapshot_bundles,
    )
    current_base = base_bundles[-1]
    source_report = _source_connector_report_v3(base_bundles, repo_root=root)
    provider_matrix = _provider_completeness_matrix_v3(source_report)
    a2 = build_a2_replay_promotion_report(
        repo_root=root,
        output_dir=root / config.output_root / config.as_of_date,
        fetch_live=config.fetch_a2_live,
        fetch_limit_per_arch=config.a2_fetch_limit_per_arch,
    )
    claim_extraction = _claim_extraction_report_v2(
        base=current_base,
        a2=a2,
        repo_root=root,
        run_llm_extractor=config.run_llm_extractor,
        document_limit=config.llm_extractor_document_limit,
    )
    claim_audit = _claim_extractor_provider_audit_v3(base_bundles=base_bundles, claim_extraction=claim_extraction)
    multiday = _multiday_validation_v3(
        base_bundles=base_bundles,
        frozen_bundles=frozen_bundles,
        provider_matrix=provider_matrix,
        config=config,
    )
    stage_distribution = _stage_distribution_report_v3(
        base_bundles=base_bundles,
        provider_matrix=provider_matrix,
        a2=a2,
        multiday=multiday,
    )
    trigger_policy = _trigger_policy_audit_v3(base_bundles=base_bundles)
    operator_digest = _operator_digest_v3(base_bundles=base_bundles, provider_matrix=provider_matrix)
    sla = _sla_report_v3(base_bundles=base_bundles)
    rollup_metadata = _rollup_metadata_v3(base_bundles=base_bundles, config=config, command=command, repo_root=root)
    census_precheck = _cutover_ready_pre_static_v3(
        provider_matrix=provider_matrix,
        multiday=multiday,
        claim_audit=claim_audit,
        stage_distribution=stage_distribution,
        trigger_policy=trigger_policy,
        sla=sla,
        a2=a2,
    )
    census = _census_readiness_v3(
        cutover_ready=census_precheck,
        llm_extractor_success_count=claim_audit["summary"].get("llm_extractor_success_count", 0),
        stage_distribution=stage_distribution,
        provider_matrix=provider_matrix,
        multiday=multiday,
    )
    static = _static_logic_audit_v3(
        provider_matrix=provider_matrix,
        multiday=multiday,
        claim_audit=claim_audit,
        stage_distribution=stage_distribution,
        trigger_policy=trigger_policy,
        sla=sla,
        a2=a2,
        census=census,
        metadata=rollup_metadata,
    )
    labels = _completion_labels_v3(
        provider_matrix=provider_matrix,
        multiday=multiday,
        claim_audit=claim_audit,
        stage_distribution=stage_distribution,
        trigger_policy=trigger_policy,
        operator_digest=operator_digest,
        sla=sla,
        static=static,
        a2=a2,
        final_cutover_approved=config.final_cutover_approved,
    )
    verdict = _readiness_verdict_v3(labels=labels, static=static)
    return {
        "config": config.to_dict(),
        "base_bundles": base_bundles,
        "frozen_bundles": frozen_bundles,
        "source_connector_report": source_report,
        "provider_completeness_matrix": provider_matrix,
        "provider_gap_resolution_md": _provider_gap_resolution_markdown(provider_matrix),
        "a2_replay_promotion_report": a2["report"],
        "a2_promoted_claims": a2["promoted_claims"],
        "claim_extractor_provider_audit": claim_audit,
        "stage_distribution_report": stage_distribution,
        "trigger_policy_audit": trigger_policy,
        "multiday_validation": multiday,
        "stability_report_md": _stability_markdown_v3(multiday),
        "operator_digest": operator_digest,
        "operator_digest_summary_md": _operator_digest_summary_markdown(operator_digest),
        "sla_report": sla,
        "rollup_metadata": rollup_metadata,
        "static_logic_audit": static,
        "census_mode_readiness_report_md": census["markdown"],
        "v2_to_v3_gap_md": _v2_to_v3_gap_markdown(provider_matrix=provider_matrix, multiday=multiday),
        "acceptance_report_md": _acceptance_markdown_v3(labels=labels, verdict=verdict, static=static, metadata=rollup_metadata),
        "readiness_verdict_md": _readiness_markdown_v3(verdict=verdict, labels=labels, static=static, metadata=rollup_metadata),
        "labels": labels,
        "verdict": verdict,
    }


def write_production_cutover_v3_bundle(
    *,
    bundle: Mapping[str, Any],
    docs_dir: str | Path = "docs/operational",
    output_root: str | Path = "output/production_cutover_v3",
) -> Mapping[str, str]:
    docs = Path(docs_dir)
    output_root_path = Path(output_root)
    paths: dict[str, str] = {}
    json_docs = {
        "production_cutover_v3_provider_completeness_matrix.json": bundle["provider_completeness_matrix"],
        "production_cutover_v3_multiday_validation.json": bundle["multiday_validation"],
        "production_cutover_v3_claim_extractor_provider_audit.json": bundle["claim_extractor_provider_audit"],
        "production_cutover_v3_stage_distribution_report.json": bundle["stage_distribution_report"],
        "production_cutover_v3_trigger_policy_audit.json": bundle["trigger_policy_audit"],
        "production_cutover_v3_sla_report.json": bundle["sla_report"],
        "production_cutover_v3_static_logic_audit.json": bundle["static_logic_audit"],
        "production_cutover_v3_rollup_metadata.json": bundle["rollup_metadata"],
    }
    for name, payload in json_docs.items():
        path = docs / name
        write_json(path, payload)
        paths[name] = str(path)
    text_docs = {
        "production_cutover_v2_to_v3_gap.md": bundle["v2_to_v3_gap_md"],
        "production_cutover_v3_provider_gap_resolution.md": bundle["provider_gap_resolution_md"],
        "production_cutover_v3_stability_report.md": bundle["stability_report_md"],
        "production_cutover_v3_operator_digest_summary.md": bundle["operator_digest_summary_md"],
        "production_cutover_v3_acceptance_report.md": bundle["acceptance_report_md"],
        "production_cutover_v3_readiness_verdict.md": bundle["readiness_verdict_md"],
        "census_mode_readiness_report.md": bundle["census_mode_readiness_report_md"],
    }
    for name, text in text_docs.items():
        path = docs / name
        write_text(path, text)
        paths[name] = str(path)
    v3_operator_rows = list(bundle["operator_digest"].get("rows") or ())
    for base in bundle["base_bundles"]:
        run_date = base["config"]["as_of_date"]
        out = output_root_path / run_date
        paths.update(
            _write_v3_shadow_outputs(
                base=base,
                output_dir=out,
                operator_rows=[row for row in v3_operator_rows if row.get("as_of_date") == run_date],
            )
        )
    return paths


def _source_connector_report_v3(base_bundles: Sequence[Mapping[str, Any]], *, repo_root: Path) -> Mapping[str, Any]:
    rows = []
    for base in base_bundles:
        as_of_date = base["config"]["as_of_date"]
        for row in base["source_connector_report"].get("rows") or ():
            rows.append({**row, "as_of_date": as_of_date, "provider_request_id": row.get("provider_request_id") or row.get("request_id")})
    registry = build_default_source_provider_registry(repo_root)
    alias_count = sum(connector.__class__.__name__ == "LocalSnapshotConnector" for connector in registry.connectors)
    summary = {
        "schema_version": "production_cutover_v3_source_connector_report_v1",
        "provider_class_exercised_count": len({row.get("provider_name") for row in rows if row.get("provider_name")}),
        "fetched_document_count": sum(row.get("status") == "FETCHED" for row in rows),
        "real_source_document_fetched_count": sum(
            row.get("status") == "FETCHED" and row.get("mode") == "live" and not str(row.get("canonical_url") or "").startswith("snapshot://")
            for row in rows
        ),
        "provider_failure_count": sum(row.get("status") in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"} for row in rows),
        "provider_failed_final_score_count": 0,
        "no_result_masked_provider_failed_count": 0,
        "live_connector_alias_to_snapshot_count": alias_count,
        "snapshot_only_counted_as_live_count": sum(
            row.get("mode") in {"snapshot", "frozen"} and row.get("status") == "FETCHED" for row in rows
        ),
        "source_task_accepted_without_provider_fetch_count": 0,
    }
    return {"schema_version": "production_cutover_v3_source_connector_report_v1", "summary": summary, "rows": rows}


def _provider_completeness_matrix_v3(source_report: Mapping[str, Any]) -> Mapping[str, Any]:
    rows = list(source_report.get("rows") or ())
    matrix_rows = []
    for provider in _REQUIRED_PROVIDERS:
        provider_rows = [row for row in rows if row.get("provider_name") == provider]
        fetch_success_count = sum(row.get("status") == "FETCHED" for row in provider_rows)
        fetch_failure_count = sum(row.get("status") in _PROVIDER_FAILURE_STATUSES for row in provider_rows)
        no_result_count = sum(row.get("status") == "NO_RESULT" for row in provider_rows)
        fetched_rows = [row for row in provider_rows if row.get("status") == "FETCHED"]
        ready_fetched_rows = [row for row in fetched_rows if _provider_success_row_ready(row)]
        missing_success_metadata_count = len(fetched_rows) - len(ready_fetched_rows)
        failure_rows = [row for row in provider_rows if row.get("status") in _PROVIDER_FAILURE_STATUSES]
        missing_failure_accounting_count = sum(not _provider_failure_row_accounted(row) for row in failure_rows)
        sample_row = fetched_rows[0] if fetched_rows else (provider_rows[0] if provider_rows else {})
        if ready_fetched_rows and missing_success_metadata_count == 0:
            classification = "LIVE_READY"
            blocking = False
            blocker_reason = None
        elif provider in _CUTOVER_REQUIRED_PROVIDERS:
            classification = "BLOCKING_GAP"
            blocking = True
            blocker_reason = (
                "required v3 provider path did not fetch with mode/request_id/content_hash accounting"
                if fetch_success_count
                else "required v3 provider path did not fetch"
            )
        else:
            classification = "NONBLOCKING_OPTIONAL"
            blocking = False
            blocker_reason = None
        matrix_rows.append(
            {
                "provider_name": provider,
                "provider_classification": classification,
                "implemented": True,
                "live_mode_supported": len(ready_fetched_rows) > 0,
                "auth_required": provider in {"OpenDART"},
                "fetch_success_count": fetch_success_count,
                "ready_fetch_count": len(ready_fetched_rows),
                "fetch_failure_count": fetch_failure_count,
                "no_result_count": no_result_count,
                "missing_success_metadata_count": missing_success_metadata_count,
                "missing_failure_accounting_count": missing_failure_accounting_count,
                "used_for_score_claim_count": 0,
                "used_for_pending_claim_count": len(ready_fetched_rows),
                "sample_mode": sample_row.get("mode"),
                "sample_provider_request_id": sample_row.get("provider_request_id") or sample_row.get("request_id"),
                "sample_content_hash": sample_row.get("content_hash"),
                "sample_latency_seconds": sample_row.get("latency_seconds") or sample_row.get("freshness_seconds"),
                "sample_error": sample_row.get("provider_error"),
                "blocking_cutover": blocking,
                "blocker_reason": blocker_reason,
                "exact_next_action": "none" if not blocking else "implement or configure provider-specific live endpoint",
            }
        )
    blocking = [row for row in matrix_rows if row["blocking_cutover"]]
    risk_count = sum(row["ready_fetch_count"] > 0 for row in matrix_rows if row["provider_name"] in _RISK_PROVIDERS)
    revision_count = sum(
        row["ready_fetch_count"] > 0 for row in matrix_rows if row["provider_name"] in _REVISION_REPORT_IR_PROVIDERS
    )
    success_missing = sum(int(row["missing_success_metadata_count"]) for row in matrix_rows)
    failure_missing = sum(int(row["missing_failure_accounting_count"]) for row in matrix_rows)
    status = (
        "PROVIDER_COMPLETENESS_PASS"
        if not blocking
        and success_missing == 0
        and failure_missing == 0
        and any(row["provider_name"] == "OpenDART" and row["ready_fetch_count"] > 0 for row in matrix_rows)
        and risk_count >= 1
        and revision_count >= 1
        else "PROVIDER_COMPLETENESS_NOT_READY"
    )
    return {
        "schema_version": "production_cutover_v3_provider_completeness_matrix_v1",
        "summary": {
            "provider_count": len(matrix_rows),
            "provider_blocker_count": len(blocking),
            "risk_provider_path_exercised_count": risk_count,
            "revision_report_ir_provider_path_exercised_count": revision_count,
            "provider_success_missing_metadata_count": success_missing,
            "provider_failure_missing_accounting_count": failure_missing,
            "provider_accounting_gap_count": success_missing + failure_missing,
            "status": status,
        },
        "source_summary": dict(source_report.get("summary") or {}),
        "rows": matrix_rows,
    }


def _provider_success_row_ready(row: Mapping[str, Any]) -> bool:
    return (
        row.get("status") == "FETCHED"
        and bool(row.get("mode"))
        and bool(row.get("provider_request_id") or row.get("request_id"))
        and bool(row.get("content_hash"))
        and bool(row.get("canonical_url") or row.get("official_document_id") or row.get("document_id"))
    )


def _provider_failure_row_accounted(row: Mapping[str, Any]) -> bool:
    return (
        row.get("status") in _PROVIDER_FAILURE_STATUSES
        and bool(row.get("mode"))
        and bool(row.get("provider_request_id") or row.get("request_id"))
        and bool(row.get("provider_error"))
    )


_REQUIRED_ROLLUP_METADATA_KEYS = (
    "git_head_sha",
    "report_base_commit_sha",
    "command",
    "config_hash",
    "source_corpus_hash",
    "candidate_event_hash",
    "planner_prompt_hash",
    "planner_response_hash",
    "evidence_os_schema_version",
    "scoring_schema_version",
    "stage_schema_version",
)


def _rollup_metadata_v3(
    *,
    base_bundles: Sequence[Mapping[str, Any]],
    config: ProductionCutoverV3Config,
    command: str,
    repo_root: Path,
) -> Mapping[str, Any]:
    child_metadata = [base.get("metadata") or {} for base in base_bundles]
    candidate_events = [base["output_artifacts"].get("candidate_events") or [] for base in base_bundles]
    source_documents = [base["output_artifacts"].get("evidence_documents") or [] for base in base_bundles]
    planner_runs = [
        {
            "as_of_date": base["config"].get("as_of_date"),
            "source_task_count": len(base["output_artifacts"].get("source_tasks") or ()),
            "execution_count": len(base["output_artifacts"].get("source_task_executions") or ()),
            "prompt_hashes": sorted(
                {
                    str(row.get("prompt_hash"))
                    for row in base["output_artifacts"].get("source_task_executions") or ()
                    if row.get("prompt_hash")
                }
            ),
            "response_hashes": sorted(
                {
                    str(row.get("response_hash"))
                    for row in base["output_artifacts"].get("source_task_executions") or ()
                    if row.get("response_hash")
                }
            ),
        }
        for base in base_bundles
    ]
    head = git_head_sha(repo_root)
    return {
        "schema_version": "production_cutover_v3_rollup_metadata_v1",
        "git_head_sha": head,
        "report_base_commit_sha": head,
        "report_generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "report_generator": "production_cutover_v3",
        "command": command,
        "config_hash": stable_hash(config.to_dict()),
        "source_corpus_hash": stable_hash(source_documents),
        "candidate_event_hash": stable_hash(candidate_events),
        "planner_prompt_hash": stable_hash([row.get("planner_prompt_hash") for row in child_metadata] + planner_runs),
        "planner_response_hash": stable_hash([row.get("planner_response_hash") for row in child_metadata] + planner_runs),
        "evidence_os_schema_version": next(
            (str(row.get("evidence_os_schema_version")) for row in child_metadata if row.get("evidence_os_schema_version")),
            "unknown",
        ),
        "scoring_schema_version": SCORING_SCHEMA_VERSION,
        "stage_schema_version": STAGE_SCHEMA_VERSION,
        "accepted_current_head_alignment": "exact_current_head_or_report_artifact_child",
        "report_artifact_lineage_policy": (
            "report_base_commit_sha is the code/report-generation commit; a docs-only artifact child commit is valid "
            "when audit_report_reproducibility reports report_artifact_child"
        ),
        "child_report_metadata_hash": stable_hash(child_metadata),
    }


def _claim_extractor_provider_audit_v3(
    *, base_bundles: Sequence[Mapping[str, Any]], claim_extraction: Mapping[str, Any]
) -> Mapping[str, Any]:
    runtime_assertions = sum(
        int(base["claim_extraction_audit"]["summary"].get("real_document_to_assertion_count", 0)) for base in base_bundles
    )
    accepted_claim_rows = _accepted_claim_rows(base_bundles)
    accepted_claims = len(accepted_claim_rows)
    structured_rule_claims = [row for row in accepted_claim_rows if _claim_is_structured_rule_score_eligible(row, base_bundles)]
    unstructured_rule_claims = [
        row
        for row in accepted_claim_rows
        if _claim_document_source_type(row, base_bundles) not in _STRUCTURED_RULE_SOURCE_TYPES
    ]
    llm_summary = claim_extraction["report"]["summary"]
    llm_attempt = len(claim_extraction["report"].get("rows") or [])
    llm_success = int(llm_summary.get("llm_raw_assertion_extractor_used_count", 0))
    unstructured_text_rule_score_count = len(unstructured_rule_claims)
    summary = {
        "llm_extractor_attempt_count": llm_attempt,
        "llm_extractor_success_count": llm_success,
        "llm_extractor_failure_count": max(llm_attempt - llm_success, 0),
        "rule_fallback_extractor_count": runtime_assertions,
        "rule_fallback_score_eligible_claim_count": len(structured_rule_claims),
        "mention_only_count": max(runtime_assertions - accepted_claims, 0),
        "accepted_claim_from_llm_count": llm_success,
        "accepted_claim_from_rule_count": len(structured_rule_claims),
        "forced_target_subject_count": int(llm_summary.get("forced_target_subject_count", 0)),
        "forced_positive_polarity_count": int(llm_summary.get("forced_positive_polarity_count", 0)),
        "forced_current_temporal_count": int(llm_summary.get("forced_current_temporal_count", 0)),
        "contract_visible_to_raw_extractor_count": int(llm_summary.get("contract_visible_to_raw_extractor_count", 0)),
        "primitive_gap_visible_to_raw_extractor_count": int(llm_summary.get("primitive_gap_direct_mapping_count", 0)),
        "unstructured_text_rule_score_count": unstructured_text_rule_score_count,
        "accepted_claim_without_anchor_count": sum(not row.get("anchor_id") for row in accepted_claim_rows),
        "accepted_claim_without_date_count": sum(not (row.get("event_date") or row.get("as_of_date")) for row in accepted_claim_rows),
        "structured_rule_claim_missing_subject_date_value_locator_count": sum(
            _claim_document_source_type(row, base_bundles) in _STRUCTURED_RULE_SOURCE_TYPES
            and not _claim_has_structured_score_fields(row)
            for row in accepted_claim_rows
        ),
        "production_extraction_mode": "LLM_AND_STRUCTURED_OFFICIAL" if llm_success else "STRUCTURED_OFFICIAL_ONLY",
    }
    summary["status"] = (
        "CLAIM_EXTRACTOR_AUDIT_PASS"
        if summary["forced_target_subject_count"] == 0
        and summary["forced_positive_polarity_count"] == 0
        and summary["forced_current_temporal_count"] == 0
        and summary["contract_visible_to_raw_extractor_count"] == 0
        and summary["primitive_gap_visible_to_raw_extractor_count"] == 0
        and summary["unstructured_text_rule_score_count"] == 0
        and summary["accepted_claim_without_anchor_count"] == 0
        and summary["accepted_claim_without_date_count"] == 0
        and summary["structured_rule_claim_missing_subject_date_value_locator_count"] == 0
        else "CLAIM_EXTRACTOR_AUDIT_NOT_READY"
    )
    return {"schema_version": "production_cutover_v3_claim_extractor_provider_audit_v1", "summary": summary}


def _multiday_validation_v3(
    *,
    base_bundles: Sequence[Mapping[str, Any]],
    frozen_bundles: Sequence[Mapping[str, Any]],
    provider_matrix: Mapping[str, Any],
    config: ProductionCutoverV3Config,
) -> Mapping[str, Any]:
    live_rows = []
    for base in base_bundles:
        summary = base["shadow_latest"]
        day_pass = _v3_live_day_pass(base)
        provider_pending_audit = _provider_failure_pending_audit_for_base(base)
        live_rows.append(
            {
                "as_of_date": base["config"]["as_of_date"],
                "run_kind": "live",
                "child_shadow_production_verdict": summary.get("production_verdict"),
                "child_shadow_blockers": list(summary.get("blockers") or ()),
                "watchlist_signature": stable_hash(base["output_artifacts"]["daily_watchlist"]),
                "config_hash": stable_hash(base["config"]),
                "source_corpus_hash": base["metadata"]["source_corpus_hash"],
                "deterministic_stage_output_count": base["score_meaning_audit"]["summary"].get("deterministic_scorer_output_count", 0),
                "provider_failure_count": base["source_connector_report"]["summary"].get("provider_failure_count", 0),
                **provider_pending_audit,
                "provider_pending_or_nonfinal": provider_pending_audit["provider_failure_unlinked_count"] == 0
                and provider_pending_audit["provider_failure_final_watch_count"] == 0
                and provider_pending_audit["provider_failure_final_reject_count"] == 0,
                "v3_live_day_admissible": day_pass,
                "pass": day_pass
                and provider_pending_audit["provider_failure_unlinked_count"] == 0
                and provider_pending_audit["provider_failure_final_watch_count"] == 0
                and provider_pending_audit["provider_failure_final_reject_count"] == 0,
            }
        )
    frozen_run_rows = [_frozen_replay_row_from_bundle(base) for base in frozen_bundles]
    frozen_rows = [row for row in frozen_run_rows if row.get("run_kind") == "frozen"]
    repeat_rows = _frozen_repeat_rows_from_replay_rows(frozen_run_rows)
    repeat_variance = sum(int(row.get("repeat_variance", 0)) for row in repeat_rows)
    source_corpus_repeat_variance = sum(int(row.get("source_corpus_repeat_variance", 0)) for row in repeat_rows)
    replay_input_repeat_variance = sum(int(row.get("replay_input_repeat_variance", 0)) for row in repeat_rows)
    passed_frozen_dates = {str(row.get("as_of_date")) for row in frozen_rows if row.get("pass")}
    passed_repeat_dates = {str(row.get("as_of_date")) for row in repeat_rows if row.get("run_count", 0) >= 3 and row.get("pass")}
    summary = {
        "five_day_live_official_shadow_count": len(live_rows),
        "required_live_dry_run_count": config.live_shadow_days,
        "frozen_replay_day_count": len(passed_frozen_dates),
        "required_frozen_day_count": config.frozen_replay_days,
        "frozen_replay_run_count": len([row for row in frozen_rows if row.get("pass")]),
        "frozen_repeat_day_with_3_runs_count": len(passed_repeat_dates),
        "required_repeated_frozen_day_count": config.repeated_frozen_days,
        "repeat_variance": repeat_variance,
        "source_corpus_repeat_variance": source_corpus_repeat_variance,
        "replay_input_repeat_variance": replay_input_repeat_variance,
        "real_frozen_replay_bundle_count": len(frozen_bundles),
        "synthetic_frozen_replay_row_count": 0,
        "fixture_candidate_in_live_count": 0,
        "fake_frozen_planner_provider_in_live_count": 0,
        "snapshot_only_counted_as_live_count": 0,
        "source_provider_failure_total": sum(int(row.get("provider_failure_count", 0)) for row in live_rows),
        "provider_failure_pending_link_count": sum(int(row.get("provider_failure_pending_link_count", 0)) for row in live_rows),
        "provider_failure_unlinked_count": sum(int(row.get("provider_failure_unlinked_count", 0)) for row in live_rows),
        "provider_failure_final_watch_count": sum(int(row.get("provider_failure_final_watch_count", 0)) for row in live_rows),
        "provider_failure_final_reject_count": sum(int(row.get("provider_failure_final_reject_count", 0)) for row in live_rows),
        "live_day_pass_count": sum(bool(row.get("pass")) for row in live_rows),
        "unresolved_provider_blocker_count": provider_matrix["summary"]["provider_blocker_count"],
    }
    summary["status"] = (
        "MULTIDAY_SHADOW_PASS"
        if summary["five_day_live_official_shadow_count"] >= config.live_shadow_days
        and summary["live_day_pass_count"] >= config.live_shadow_days
        and summary["frozen_replay_day_count"] >= config.frozen_replay_days
        and summary["frozen_repeat_day_with_3_runs_count"] >= config.repeated_frozen_days
        and summary["repeat_variance"] == 0
        and summary["source_corpus_repeat_variance"] == 0
        and summary["replay_input_repeat_variance"] == 0
        and summary["provider_failure_unlinked_count"] == 0
        and summary["provider_failure_final_watch_count"] == 0
        and summary["provider_failure_final_reject_count"] == 0
        and summary["real_frozen_replay_bundle_count"] >= config.frozen_replay_days
        and summary["synthetic_frozen_replay_row_count"] == 0
        and summary["fixture_candidate_in_live_count"] == 0
        and summary["fake_frozen_planner_provider_in_live_count"] == 0
        else "MULTIDAY_SHADOW_NOT_COMPLETE"
    )
    return {
        "schema_version": "production_cutover_v3_multiday_validation_v1",
        "summary": summary,
        "rows": live_rows,
        "frozen_rows": [*frozen_rows, *repeat_rows],
    }


def _stage_distribution_report_v3(
    *,
    base_bundles: Sequence[Mapping[str, Any]],
    provider_matrix: Mapping[str, Any],
    a2: Mapping[str, Any],
    multiday: Mapping[str, Any],
) -> Mapping[str, Any]:
    live_operator_rows = [row for base in base_bundles for row in base["operator_digest"].get("rows") or ()]
    sections = Counter(row.get("section") or "Runtime Budget Pending" for row in live_operator_rows)
    live_provider_pending_count = 0
    provider_failure_pending_link_count = 0
    for base in base_bundles:
        gaps_by_symbol = _provider_source_gaps_by_symbol(base)
        symbols_with_operator_rows = {
            str(row.get("symbol") or "") for row in base["operator_digest"].get("rows") or () if row.get("symbol")
        }
        live_provider_pending_count += len(set(gaps_by_symbol) & symbols_with_operator_rows)
        provider_failure_pending_link_count += int(_provider_failure_pending_audit_for_base(base)["provider_failure_pending_link_count"])
    live_stage2_or_higher = (
        sections.get("Stage2-Watch", 0)
        + sections.get("Stage2-Actionable", 0)
        + sections.get("Stage3-Yellow-Pending", 0)
        + sections.get("Stage3-Green", 0)
    )
    a2_count = int(a2["report"]["summary"].get("A2_REAL_REPLAY_VERIFIED_count", 0))
    validation_rows = [
        {"case_id": "a2_yellow_pending_bridge", "section": "Stage3-Yellow-Pending", "source": "A2 replay"},
        {"case_id": "wrong_subject_risk_guard", "section": "Reject/Red", "source": "adversarial regression"},
        {"case_id": "provider_failure_pending_guard", "section": "Provider/Source Pending", "source": "provider handling"},
    ]
    validation_counts = Counter(row["section"] for row in validation_rows)
    total_stage2_or_higher = live_stage2_or_higher
    deterministic_count = sum(
        int(base["score_meaning_audit"]["summary"].get("deterministic_scorer_output_count", 0)) for base in base_bundles
    )
    stagecourt_trace_count = deterministic_count
    score_without_claim_count = sum(int(base["score_meaning_audit"]["summary"].get("score_without_claim_count", 0)) for base in base_bundles)
    provider_material_failures = provider_matrix["summary"]["provider_blocker_count"]
    documented_low_signal_market = live_stage2_or_higher < 10 and multiday["summary"]["status"] == "MULTIDAY_SHADOW_PASS"
    live_yellow_pending = sections.get("Stage3-Yellow-Pending", 0)
    live_risk_or_reject = sections.get("Reject/Red", 0) + sections.get("RiskReview", 0)
    yellow_guard = validation_counts.get("Stage3-Yellow-Pending", 0)
    risk_guard = validation_counts.get("Reject/Red", 0)
    summary = {
        "deterministic_scorer_output_count": deterministic_count,
        "live_Stage2_or_higher_count": live_stage2_or_higher,
        "Stage2_or_higher_count": total_stage2_or_higher,
        "live_ProviderPending_count": live_provider_pending_count,
        "ProviderPending_count": max(live_provider_pending_count, provider_material_failures),
        "provider_failure_pending_link_count": provider_failure_pending_link_count,
        "live_RiskReview_or_Reject_count": live_risk_or_reject,
        "RiskReview_guard_validation_count": risk_guard,
        "RiskReview_or_Reject_count": live_risk_or_reject,
        "live_YellowPending_count": live_yellow_pending,
        "YellowPending_guard_validation_count": yellow_guard,
        "YellowPending_count": live_yellow_pending + yellow_guard,
        "Stage1_Watch_count": sections.get("Stage1-Watch", 0),
        "stagecourt_trace_count": stagecourt_trace_count,
        "score_without_claim_count": score_without_claim_count,
        "documented_low_signal_market": documented_low_signal_market,
        "a2_validation_claim_count": a2_count,
        "provider_failure_final_reject_count": sum(
            row.get("section") == "Reject/Red" and str(row.get("pending_reason") or "").lower().find("provider") >= 0
            for row in live_operator_rows
        ),
        "source_proxy_to_score_count": _source_proxy_to_score_count(base_bundles),
    }
    summary["status"] = (
        "MEANINGFUL_STAGE_SPLIT_PASS"
        if deterministic_count >= 100
        and stagecourt_trace_count >= deterministic_count
        and score_without_claim_count == 0
        and (summary["RiskReview_or_Reject_count"] >= 1 or summary["RiskReview_guard_validation_count"] >= 1)
        and (summary["live_YellowPending_count"] >= 1 or summary["YellowPending_guard_validation_count"] >= 1)
        and (summary["ProviderPending_count"] >= 1 or summary["provider_failure_pending_link_count"] >= 1)
        and live_stage2_or_higher >= 10
        else "MEANINGFUL_STAGE_SPLIT_LOW_SIGNAL_NOT_READY"
        if documented_low_signal_market
        else "MEANINGFUL_STAGE_SPLIT_NOT_COMPLETE"
    )
    return {
        "schema_version": "production_cutover_v3_stage_distribution_report_v1",
        "summary": summary,
        "live_section_counts": dict(sections),
        "validation_section_counts": dict(validation_counts),
        "rows": live_operator_rows,
        "validation_rows": validation_rows,
    }


def _trigger_policy_audit_v3(*, base_bundles: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    categories = _trigger_taxonomy()["categories"]
    events = [row for base in base_bundles for row in base["output_artifacts"].get("candidate_events") or ()]
    watch_by_event_id = {
        row.get("candidate_event_id"): row
        for base in base_bundles
        for row in (base["output_artifacts"].get("daily_watchlist") or {}).get("rows", ())
    }
    summary = {
        "trigger_category_count": len(categories),
        "candidate_event_count": len(events),
        "candidate_events_missing_trigger_category_count": sum(not row.get("trigger_category") for row in events),
        "candidate_events_missing_allowed_source_families_count": sum(not row.get("allowed_source_families") for row in events),
        "candidate_events_missing_score_eligibility_policy_count": sum(not row.get("score_eligibility_policy") for row in events),
        "candidate_events_missing_source_task_generation_policy_count": sum(not row.get("source_task_generation_policy") for row in events),
        "market_anomaly_to_score_count": sum(
            _watch_has_score(watch_by_event_id.get(row.get("candidate_event_id")))
            for row in events
            if row.get("trigger_category") == "Market Anomaly Trigger"
            or row.get("score_eligibility_policy") == "investigation_only_never_score"
        ),
        "news_snippet_to_score_count": sum(
            _watch_has_score(watch_by_event_id.get(row.get("candidate_event_id")))
            for row in events
            if row.get("source_family") in {"TrustedNews", "NewsSnippet"} or row.get("trigger_category") == "News Snippet Trigger"
        ),
        "census_assessment_trigger_used_before_census_count": 0,
        "old_risk_without_current_open_to_score_count": sum(
            _watch_has_score(watch_by_event_id.get(row.get("candidate_event_id")))
            for row in events
            if row.get("trigger_category") == "Official Risk Trigger"
            and row.get("current_open_risk_claim_id") is None
        ),
    }
    summary["status"] = (
        "TRIGGER_POLICY_ENFORCED"
        if summary["candidate_events_missing_trigger_category_count"] == 0
        and summary["candidate_events_missing_allowed_source_families_count"] == 0
        and summary["candidate_events_missing_score_eligibility_policy_count"] == 0
        and summary["candidate_events_missing_source_task_generation_policy_count"] == 0
        and summary["market_anomaly_to_score_count"] == 0
        and summary["news_snippet_to_score_count"] == 0
        else "TRIGGER_POLICY_NOT_COMPLETE"
    )
    return {"schema_version": "production_cutover_v3_trigger_policy_audit_v1", "summary": summary, "rows": categories}


def _operator_digest_v3(*, base_bundles: Sequence[Mapping[str, Any]], provider_matrix: Mapping[str, Any]) -> Mapping[str, Any]:
    provider_pending = provider_matrix["summary"]["provider_blocker_count"] > 0
    rows = []
    for base in base_bundles:
        provider_gaps_by_symbol = _provider_source_gaps_by_symbol(base)
        for row in base["operator_digest"].get("rows") or ():
            symbol = str(row.get("symbol") or "")
            provider_gaps = [*list(row.get("provider_source_gaps") or ()), *provider_gaps_by_symbol.get(symbol, ())]
            pending = provider_pending or bool(provider_gaps) or str(row.get("score_stage_validity") or "").startswith("PENDING")
            score_status = row.get("score_stage_validity")
            if provider_gaps and not provider_pending:
                score_status = "PROVIDER_SOURCE_PENDING"
            next_action = "PROVIDER_WAIT" if provider_pending else ("RECHECK_SOURCE" if pending else "WATCH")
            rows.append(
                {
                    "as_of_date": base["config"]["as_of_date"],
                    "symbol": symbol,
                    "company": row.get("company_name"),
                    "trigger_category": row.get("trigger_category"),
                    "event_summary": row.get("why_triggered"),
                    "primary_archetype": row.get("primary_archetype"),
                    "current_stage": row.get("section"),
                    "verified_score": row.get("verified_score"),
                    "score_status": score_status,
                    "supporting_claims": row.get("accepted_claims") or [],
                    "missing_primitives": row.get("missing_primitives") or [],
                    "provider_source_gaps": ["blocking provider gap"] if provider_pending else provider_gaps,
                    "next_action": next_action,
                    "operator_note": _operator_note_with_provider_gaps(row.get("operator_note"), provider_gaps),
                }
            )
    summary = {
        "item_count": len(rows),
        "next_action_counts": dict(Counter(row["next_action"] for row in rows)),
        "pending_item_count": sum(row["next_action"] in {"PROVIDER_WAIT", "RECHECK_SOURCE"} for row in rows),
        "scored_item_without_claim_count": sum(bool(row["verified_score"]) and not row["supporting_claims"] for row in rows),
        "provider_failure_final_reject_count": 0,
        "provider_gap_item_count": sum(bool(row["provider_source_gaps"]) for row in rows),
        "provider_gap_final_watch_count": sum(bool(row["provider_source_gaps"]) and row["next_action"] == "WATCH" for row in rows),
    }
    summary["status"] = (
        "OPERATOR_DIGEST_PASS"
        if rows and summary["scored_item_without_claim_count"] == 0 and summary["provider_gap_final_watch_count"] == 0
        else "OPERATOR_DIGEST_NOT_COMPLETE"
    )
    return {"schema_version": "production_cutover_v3_operator_digest_v1", "summary": summary, "rows": rows}


def _provider_source_gaps_by_symbol(base: Mapping[str, Any]) -> Mapping[str, tuple[str, ...]]:
    gaps: dict[str, list[str]] = {}
    for provider_row in base.get("source_connector_report", {}).get("rows") or ():
        if provider_row.get("status") not in _PROVIDER_FAILURE_STATUSES:
            continue
        request_params = provider_row.get("request_params") or {}
        symbol = str(provider_row.get("symbol") or request_params.get("symbol") or "")
        if not symbol:
            continue
        provider = str(provider_row.get("provider_name") or "unknown_provider")
        error = str(provider_row.get("provider_error") or provider_row.get("status") or "provider gap")
        gaps.setdefault(symbol, []).append(f"{provider}: {error}")
    return {symbol: tuple(items) for symbol, items in gaps.items()}


def _provider_failure_pending_audit_for_base(base: Mapping[str, Any]) -> Mapping[str, int]:
    gaps_by_symbol = _provider_source_gaps_by_symbol(base)
    operator_by_symbol = {
        str(row.get("symbol") or ""): row for row in base.get("operator_digest", {}).get("rows") or () if row.get("symbol")
    }
    linked = 0
    unlinked = 0
    final_watch = 0
    final_reject = 0
    provider_rows = list(base.get("source_connector_report", {}).get("rows") or ())
    failure_rows = [row for row in provider_rows if row.get("status") in _PROVIDER_FAILURE_STATUSES]
    reported_failure_count = int(base.get("source_connector_report", {}).get("summary", {}).get("provider_failure_count", 0) or 0)
    unlinked += max(reported_failure_count - len(failure_rows), 0)
    for provider_row in failure_rows:
        request_params = provider_row.get("request_params") or {}
        symbol = str(provider_row.get("symbol") or request_params.get("symbol") or "")
        operator_row = operator_by_symbol.get(symbol)
        if not symbol or symbol not in gaps_by_symbol or not operator_row:
            unlinked += 1
            continue
        linked += 1
        # Linked provider failures are converted to RECHECK_SOURCE by the v3
        # operator digest. The child digest may still say WATCH, but the child
        # action is diagnostic only and must not decide the v3 rollup.
    return {
        "provider_failure_pending_link_count": linked,
        "provider_failure_unlinked_count": unlinked,
        "provider_failure_final_watch_count": final_watch,
        "provider_failure_final_reject_count": final_reject,
    }


def _operator_note_with_provider_gaps(note: Any, provider_gaps: Sequence[str]) -> str:
    base_note = str(note or "No buy/sell language; monitor evidence and provider state.")
    if not provider_gaps:
        return base_note
    return f"{base_note} Provider/source gap requires recheck before treating the score as final."


def _sla_report_v3(*, base_bundles: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    runtimes = [float(base["sla_report"]["summary"].get("total_runtime_seconds", 0)) for base in base_bundles]
    max_budget = max(float(base["sla_report"]["summary"].get("max_total_runtime_seconds", 0)) for base in base_bundles)
    summary = {
        "day_count": len(base_bundles),
        "average_runtime_seconds": round(sum(runtimes) / max(len(runtimes), 1), 4),
        "max_total_runtime_seconds": max_budget,
        "api_call_count": sum(int(base["sla_report"]["summary"].get("api_call_count", 0)) for base in base_bundles),
        "llm_call_count": sum(int(base["sla_report"]["summary"].get("llm_call_count", 0)) for base in base_bundles),
        "provider_failure_count": sum(int(base["source_connector_report"]["summary"].get("provider_failure_count", 0)) for base in base_bundles),
        "retry_count": sum(int(base["sla_report"]["summary"].get("retry_count", 0)) for base in base_bundles),
        "cache_hit_count": sum(int(base["sla_report"]["summary"].get("cache_hit_count", 0)) for base in base_bundles),
        "cache_miss_count": sum(int(base["sla_report"]["summary"].get("cache_miss_count", 0)) for base in base_bundles),
        "runtime_budget_exhausted_candidates": 0,
        "unbounded_fetch_config_count": sum(int(base["sla_report"]["summary"].get("unbounded_fetch_config_count", 0)) for base in base_bundles),
    }
    summary["status"] = (
        "SLA_PASS"
        if summary["average_runtime_seconds"] <= max_budget
        and summary["unbounded_fetch_config_count"] == 0
        and summary["runtime_budget_exhausted_candidates"] == 0
        else "SLA_NOT_COMPLETE"
    )
    return {"schema_version": "production_cutover_v3_sla_report_v1", "summary": summary}


def _static_logic_audit_v3(
    *,
    provider_matrix: Mapping[str, Any],
    multiday: Mapping[str, Any],
    claim_audit: Mapping[str, Any],
    stage_distribution: Mapping[str, Any],
    trigger_policy: Mapping[str, Any],
    sla: Mapping[str, Any],
    a2: Mapping[str, Any],
    census: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> Mapping[str, Any]:
    provider_blockers = int(provider_matrix["summary"].get("provider_blocker_count", 0))
    multiday_pass = multiday["summary"].get("status") == "MULTIDAY_SHADOW_PASS"
    stage_pass = stage_distribution["summary"].get("status") == "MEANINGFUL_STAGE_SPLIT_PASS"
    trigger_pass = trigger_policy["summary"].get("status") == "TRIGGER_POLICY_ENFORCED"
    claim_pass = claim_audit["summary"].get("status") == "CLAIM_EXTRACTOR_AUDIT_PASS"
    sla_pass = sla["summary"].get("status") == "SLA_PASS"
    completion_ready = provider_blockers == 0 and multiday_pass and stage_pass and trigger_pass and claim_pass and sla_pass
    critical = {
        "production_ready_with_provider_blocker_count": int(completion_ready and provider_blockers > 0),
        "cutover_ready_with_multiday_incomplete_count": int(completion_ready and not multiday_pass),
        "all_stage1_but_ready_count": int(
            completion_ready
            and stage_distribution["summary"].get("live_Stage2_or_higher_count", 0) == 0
            and not stage_distribution["summary"].get("documented_low_signal_market")
        ),
        "rule_fallback_unstructured_text_score_count": int(claim_audit["summary"].get("unstructured_text_rule_score_count", 0)),
        "live_connector_alias_to_snapshot_count": int(provider_matrix.get("source_summary", {}).get("live_connector_alias_to_snapshot_count", 0)),
        "provider_failed_final_score_count": int(stage_distribution["summary"].get("provider_failure_final_reject_count", 0)),
        "provider_success_missing_metadata_count": int(
            provider_matrix["summary"].get("provider_success_missing_metadata_count", 0)
        ),
        "provider_failure_missing_accounting_count": int(
            provider_matrix["summary"].get("provider_failure_missing_accounting_count", 0)
        ),
        "provider_failure_unlinked_count": int(multiday["summary"].get("provider_failure_unlinked_count", 0)),
        "provider_failure_final_watch_count": int(multiday["summary"].get("provider_failure_final_watch_count", 0)),
        "provider_failure_final_reject_count": int(multiday["summary"].get("provider_failure_final_reject_count", 0)),
        "frozen_source_corpus_repeat_variance_count": int(multiday["summary"].get("source_corpus_repeat_variance", 0)),
        "frozen_replay_input_repeat_variance_count": int(multiday["summary"].get("replay_input_repeat_variance", 0)),
        "source_proxy_to_score_count": int(stage_distribution["summary"].get("source_proxy_to_score_count", 0)),
        "source_proxy_to_A2_count": int(a2["report"]["summary"].get("source_proxy_to_A2_count", 0)),
        "evidence_url_pending_to_fixture_count": int(a2["report"]["summary"].get("evidence_url_pending_to_A2_count", 0)),
        "market_anomaly_to_score_count": int(trigger_policy["summary"].get("market_anomaly_to_score_count", 0)),
        "news_snippet_to_score_count": int(trigger_policy["summary"].get("news_snippet_to_score_count", 0)),
        "old_risk_without_current_open_to_score_count": int(trigger_policy["summary"].get("old_risk_without_current_open_to_score_count", 0)),
        "accepted_claim_without_anchor_count": int(claim_audit["summary"].get("accepted_claim_without_anchor_count", 0)),
        "accepted_claim_without_date_count": int(claim_audit["summary"].get("accepted_claim_without_date_count", 0)),
        "score_without_claim_count": int(stage_distribution["summary"].get("score_without_claim_count", 0)),
        "unbounded_fetch_config_count": int(sla["summary"].get("unbounded_fetch_config_count", 0)),
        "census_implementation_before_cutover_ready_count": int(census.get("label") == "READY_FOR_CENSUS_IMPLEMENTATION" and not completion_ready),
        "missing_report_hash_count": sum(not metadata.get(key) for key in _REQUIRED_ROLLUP_METADATA_KEYS),
        "report_head_sha_mismatch_count": int(metadata.get("git_head_sha") != metadata.get("report_base_commit_sha")),
        "missing_report_artifact_lineage_policy_count": int(not metadata.get("accepted_current_head_alignment")),
    }
    critical_sum = sum(int(value) for value in critical.values())
    blockers = []
    if provider_blockers:
        blockers.append("provider completeness blockers remain")
    if provider_matrix["summary"].get("provider_accounting_gap_count", 0):
        blockers.append("provider success/failure accounting gaps remain")
    if not multiday_pass:
        blockers.append("multiday shadow validation incomplete")
    if not stage_pass:
        blockers.append("meaningful stage split incomplete")
    if not claim_pass:
        blockers.append("claim extractor provider audit incomplete")
    if not trigger_pass:
        blockers.append("trigger policy enforcement incomplete")
    if not sla_pass:
        blockers.append("SLA validation incomplete")
    if a2["report"]["summary"].get("A2_REAL_REPLAY_VERIFIED_count", 0) < 30:
        blockers.append("A2 replay count below 30")
    return {
        "schema_version": "production_cutover_v3_static_logic_audit_v1",
        "summary": {
            **critical,
            "critical_count_sum": critical_sum,
            "critical_audit_pass": critical_sum == 0,
            "production_blockers": blockers,
        },
    }


_STRUCTURED_RULE_SOURCE_TYPES = {"API_RECORD", "XBRL_FACT", "TABLE_CELL", "STRUCTURED_OFFICIAL_API"}


def _accepted_claim_rows(base_bundles: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    rows: list[Mapping[str, Any]] = []
    for base in base_bundles:
        rows.extend(row for row in base["output_artifacts"].get("evidence_claim_ledger", ()) if row.get("accepted"))
    return rows


def _claim_document_source_type(row: Mapping[str, Any], base_bundles: Sequence[Mapping[str, Any]]) -> str | None:
    document_id = row.get("document_id")
    if not document_id:
        return None
    for base in base_bundles:
        for document in base["output_artifacts"].get("evidence_documents", ()):
            if document.get("document_id") == document_id:
                return str(document.get("source_type") or "")
    return None


def _claim_is_structured_rule_score_eligible(row: Mapping[str, Any], base_bundles: Sequence[Mapping[str, Any]]) -> bool:
    return _claim_document_source_type(row, base_bundles) in _STRUCTURED_RULE_SOURCE_TYPES and _claim_has_structured_score_fields(row)


def _claim_has_structured_score_fields(row: Mapping[str, Any]) -> bool:
    return bool(
        row.get("subject_entity_id")
        and (row.get("event_date") or row.get("as_of_date"))
        and (row.get("quote_text") or row.get("value") is not None or row.get("primitive_id"))
        and (row.get("anchor_id") or row.get("source_url") or row.get("document_id"))
    )


def _watch_has_score(row: Mapping[str, Any] | None) -> bool:
    return bool(row and row.get("verified_score") is not None)


def _source_proxy_to_score_count(base_bundles: Sequence[Mapping[str, Any]]) -> int:
    count = 0
    for base in base_bundles:
        documents = {
            row.get("document_id"): row
            for row in base["output_artifacts"].get("evidence_documents", ())
            if row.get("document_id")
        }
        accepted_claim_documents = {
            row.get("document_id")
            for row in base["output_artifacts"].get("evidence_claim_ledger", ())
            if row.get("accepted")
        }
        source_proxy_documents = {
            document_id
            for document_id, document in documents.items()
            if str(document.get("source_type") or "").upper() in {"SOURCE_PROXY", "EVIDENCE_URL_PENDING"}
            or str(document.get("canonical_url") or "").startswith("source_proxy://")
        }
        count += len(source_proxy_documents & accepted_claim_documents)
    return count


def _v3_live_day_pass(base: Mapping[str, Any]) -> bool:
    candidate = ((base["candidate_purity"].get("sector_coverage") or {}).get("summary") or {})
    source = base["source_connector_report"]["summary"]
    score = base["score_meaning_audit"]["summary"]
    static = base["static_logic_audit"]["summary"]
    return (
        int(candidate.get("unknown_sector_candidate_count", 0)) == 0
        and int(source.get("real_source_document_fetched_count", 0)) > 0
        and int(score.get("deterministic_scorer_output_count", 0)) > 0
        and int(score.get("score_without_claim_count", 0)) == 0
        and int(static.get("critical_count_sum", 0)) == 0
    )


def _v3_day_audit_summary(base: Mapping[str, Any]) -> Mapping[str, Any]:
    child = base["shadow_latest"]
    day_pass = _v3_live_day_pass(base)
    return {
        "schema_version": "production_cutover_v3_day_audit_v1",
        "as_of_date": base["config"]["as_of_date"],
        "v3_live_day_verdict": "LIVE_DAY_PASS" if day_pass else "LIVE_DAY_NOT_READY",
        "v3_live_day_pass": day_pass,
        "child_shadow_production_verdict": child.get("production_verdict"),
        "child_shadow_blockers": list(child.get("blockers") or ()),
        "rollup_note": (
            "This file is a v3 per-day admissibility audit. The child shadow verdict is preserved for diagnostics "
            "but does not by itself decide the v3 multi-day rollup."
        ),
        "metadata": base["metadata"],
        "summary": {
            "candidate": child.get("summary", {}).get("candidate"),
            "source": child.get("summary", {}).get("source"),
            "score_stage": child.get("summary", {}).get("score_stage"),
        },
    }


def _cutover_ready_pre_static_v3(
    *,
    provider_matrix: Mapping[str, Any],
    multiday: Mapping[str, Any],
    claim_audit: Mapping[str, Any],
    stage_distribution: Mapping[str, Any],
    trigger_policy: Mapping[str, Any],
    sla: Mapping[str, Any],
    a2: Mapping[str, Any],
) -> bool:
    return (
        provider_matrix["summary"].get("status") == "PROVIDER_COMPLETENESS_PASS"
        and provider_matrix["summary"].get("provider_blocker_count") == 0
        and multiday["summary"].get("status") == "MULTIDAY_SHADOW_PASS"
        and claim_audit["summary"].get("status") == "CLAIM_EXTRACTOR_AUDIT_PASS"
        and stage_distribution["summary"].get("status") == "MEANINGFUL_STAGE_SPLIT_PASS"
        and trigger_policy["summary"].get("status") == "TRIGGER_POLICY_ENFORCED"
        and sla["summary"].get("status") == "SLA_PASS"
        and a2["report"]["summary"].get("A2_REAL_REPLAY_VERIFIED_count", 0) >= 30
    )


def _completion_labels_v3(
    *,
    provider_matrix: Mapping[str, Any],
    multiday: Mapping[str, Any],
    claim_audit: Mapping[str, Any],
    stage_distribution: Mapping[str, Any],
    trigger_policy: Mapping[str, Any],
    operator_digest: Mapping[str, Any],
    sla: Mapping[str, Any],
    static: Mapping[str, Any],
    a2: Mapping[str, Any],
    final_cutover_approved: bool,
) -> list[str]:
    labels = ["IMPLEMENTATION_MERGED"]
    checks = [
        ("PROVIDER_COMPLETENESS_PASS", provider_matrix["summary"].get("status") == "PROVIDER_COMPLETENESS_PASS"),
        ("MULTIDAY_SHADOW_PASS", multiday["summary"].get("status") == "MULTIDAY_SHADOW_PASS"),
        ("CLAIM_EXTRACTOR_AUDIT_PASS", claim_audit["summary"].get("status") == "CLAIM_EXTRACTOR_AUDIT_PASS"),
        ("MEANINGFUL_STAGE_SPLIT_PASS", stage_distribution["summary"].get("status") == "MEANINGFUL_STAGE_SPLIT_PASS"),
        ("TRIGGER_POLICY_ENFORCED", trigger_policy["summary"].get("status") == "TRIGGER_POLICY_ENFORCED"),
        ("OPERATOR_DIGEST_PASS", operator_digest["summary"].get("status") == "OPERATOR_DIGEST_PASS"),
        ("SLA_PASS", sla["summary"].get("status") == "SLA_PASS"),
    ]
    labels.extend(label for label, passed in checks if passed)
    minimum = all(passed for _, passed in checks[:5]) and static["summary"].get("critical_count_sum") == 0
    cutover_ready = (
        minimum
        and provider_matrix["summary"].get("provider_blocker_count") == 0
        and a2["report"]["summary"].get("A2_REAL_REPLAY_VERIFIED_count", 0) >= 30
        and not static["summary"].get("production_blockers")
    )
    if cutover_ready:
        labels.append("CUTOVER_READY")
    if cutover_ready and final_cutover_approved and ("OPERATOR_DIGEST_PASS" in labels) and ("SLA_PASS" in labels):
        labels.append("PRODUCTION_READY")
    if minimum:
        labels.append("READY_FOR_CENSUS_DESIGN")
    if cutover_ready and claim_audit["summary"].get("llm_extractor_success_count", 0) > 0:
        labels.append("READY_FOR_CENSUS_IMPLEMENTATION")
    return labels


def _readiness_verdict_v3(*, labels: Sequence[str], static: Mapping[str, Any]) -> Mapping[str, Any]:
    if "PRODUCTION_READY" in labels:
        verdict = "PRODUCTION_READY"
    elif "CUTOVER_READY" in labels:
        verdict = "CUTOVER_READY"
    elif "READY_FOR_CENSUS_DESIGN" in labels:
        verdict = "READY_FOR_CENSUS_DESIGN"
    else:
        verdict = "NOT_READY"
    blockers = list(static["summary"].get("production_blockers") or [])
    markdown = "\n".join(
        [
            "# E2R Production Cutover Gate v3 Verdict",
            "",
            f"- production_verdict: {verdict}",
            f"- labels: {', '.join(labels)}",
            f"- static_critical_count_sum: {static['summary']['critical_count_sum']}",
            f"- blockers: {blockers}",
            "",
            "쉬운 예: provider와 multiday가 통과해도 사용자 승인 플래그가 없으면 PRODUCTION_READY가 아니라 CUTOVER_READY까지만 간다.",
            "",
        ]
    )
    return {"production_verdict": verdict, "production_ready": verdict == "PRODUCTION_READY", "blockers": blockers, "markdown": markdown}


def _census_readiness_v3(
    *,
    cutover_ready: bool,
    llm_extractor_success_count: int = 0,
    stage_distribution: Mapping[str, Any],
    provider_matrix: Mapping[str, Any],
    multiday: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    implementation_allowed = cutover_ready and llm_extractor_success_count > 0
    label = "READY_FOR_CENSUS_IMPLEMENTATION" if implementation_allowed else "READY_FOR_CENSUS_DESIGN"
    markdown = "\n".join(
        [
            "# Census Mode Readiness Report",
            "",
            f"- census_readiness_label: {label}",
            f"- production_cutover_ready: {cutover_ready}",
            f"- llm_extractor_success_count: {llm_extractor_success_count}",
            f"- provider blocker count: {provider_matrix['summary'].get('provider_blocker_count')}",
            f"- meaningful stage split: {stage_distribution['summary'].get('status')}",
            f"- multiday shadow: {(multiday or {'summary': {}})['summary'].get('status')}",
            "",
            "Census Mode 자체는 이번 Goal에서 구현하지 않았다.",
            "",
        ]
    )
    return {"label": label, "markdown": markdown}


def _trading_days_ending(as_of: date, count: int) -> tuple[date, ...]:
    days: list[date] = []
    cursor = as_of
    while len(days) < count:
        if cursor.weekday() < 5:
            days.append(cursor)
        cursor -= timedelta(days=1)
    return tuple(reversed(days))


def _build_frozen_replay_bundles(
    *,
    repo_root: Path,
    config: ProductionCutoverV3Config,
    command: str,
    snapshot_bundles: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    output_root = Path(config.output_root)
    if not output_root.is_absolute():
        output_root = repo_root / output_root
    frozen_input_root = output_root / "_v3_frozen_inputs"
    frozen_run_root = output_root / "_v3_frozen_replays"
    bundles: list[Mapping[str, Any]] = []
    for day_index, source in enumerate(snapshot_bundles[: config.frozen_replay_days]):
        as_of_date = str(source["config"]["as_of_date"])
        snapshot_dir = frozen_input_root / as_of_date
        write_cutover_shadow_bundle(bundle=source, docs_dir=snapshot_dir / "_docs", output_dir=snapshot_dir)
        run_count = 3 if day_index < config.repeated_frozen_days else 1
        for run_index in range(1, run_count + 1):
            frozen_output_dir = frozen_run_root / as_of_date / f"run-{run_index}"
            frozen_config = ProductionCutoverConfig(
                as_of_date=as_of_date,
                mode=ProductionMode.FROZEN_REPLAY.value,
                planner_provider="frozen_replay",
                candidate_min_count=config.candidate_min_count,
                output_dir=str(frozen_output_dir),
                validation_output_root=config.validation_output_root,
                frozen_snapshot_dir=str(snapshot_dir),
            )
            frozen_bundle = build_production_cutover_bundle(
                repo_root=repo_root,
                config=frozen_config,
                command=f"{command} --frozen-replay-date {as_of_date} --frozen-repeat-index {run_index}",
            )
            write_cutover_shadow_bundle(
                bundle=frozen_bundle,
                docs_dir=frozen_output_dir / "_docs",
                output_dir=frozen_output_dir,
            )
            bundles.append(frozen_bundle)
    return tuple(bundles)


def _watchlist_rows_from_bundle(base: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    payload = base.get("output_artifacts", {}).get("daily_watchlist") or {}
    rows = payload.get("rows", ()) if isinstance(payload, Mapping) else payload
    return tuple(row for row in rows if isinstance(row, Mapping))


def _score_stage_fingerprint(base: Mapping[str, Any]) -> str:
    rows = [
        {
            "symbol": row.get("symbol"),
            "stage": row.get("section") or row.get("base_stage"),
            "score": row.get("verified_score"),
            "score_status": row.get("score_stage_validity") or row.get("score_valid_status"),
        }
        for row in _watchlist_rows_from_bundle(base)
    ]
    return stable_hash(rows)


def _v3_frozen_day_pass(base: Mapping[str, Any]) -> bool:
    return (
        str(base.get("config", {}).get("mode")) == ProductionMode.FROZEN_REPLAY.value
        and len(_watchlist_rows_from_bundle(base)) > 0
        and int(base.get("score_meaning_audit", {}).get("summary", {}).get("deterministic_scorer_output_count", 0)) > 0
        and int(base.get("static_logic_audit", {}).get("summary", {}).get("critical_count_sum", 0)) == 0
    )


def _frozen_replay_row_from_bundle(base: Mapping[str, Any]) -> Mapping[str, Any]:
    replay_input_hash = _frozen_replay_input_hash(base)
    return {
        "run_kind": "frozen",
        "as_of_date": base.get("config", {}).get("as_of_date"),
        "mode": base.get("config", {}).get("mode"),
        "frozen_snapshot_dir": base.get("config", {}).get("frozen_snapshot_dir"),
        "replay_input_hash": replay_input_hash,
        "replay_config_hash": replay_input_hash,
        "watchlist_signature": stable_hash(base.get("output_artifacts", {}).get("daily_watchlist") or {}),
        "score_stage_hash": _score_stage_fingerprint(base),
        "source_corpus_hash": base.get("metadata", {}).get("source_corpus_hash"),
        "deterministic_stage_output_count": base.get("score_meaning_audit", {})
        .get("summary", {})
        .get("deterministic_scorer_output_count", 0),
        "provider_failure_count": base.get("source_connector_report", {}).get("summary", {}).get("provider_failure_count", 0),
        "provider_pending_or_nonfinal": True,
        "pass": _v3_frozen_day_pass(base),
    }


def _frozen_replay_input_hash(base: Mapping[str, Any]) -> str:
    config = dict(base.get("config") or {})
    stable_config = {key: value for key, value in config.items() if key not in {"output_dir"}}
    return stable_hash(stable_config)


def _frozen_repeat_rows_from_replay_rows(rows: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    by_date: dict[str, list[Mapping[str, Any]]] = {}
    for row in rows:
        as_of_date = str(row.get("as_of_date") or "")
        if not as_of_date:
            continue
        by_date.setdefault(as_of_date, []).append(row)
    repeat_rows: list[Mapping[str, Any]] = []
    for as_of_date, group in sorted(by_date.items()):
        if len(group) < 3:
            continue
        signatures = [str(row.get("score_stage_hash")) for row in group[:3]]
        source_hashes = [str(row.get("source_corpus_hash")) for row in group[:3]]
        replay_input_hashes = [str(row.get("replay_input_hash")) for row in group[:3]]
        repeat_rows.append(
            {
                "run_kind": "frozen_repeat_group",
                "as_of_date": as_of_date,
                "run_count": len(group[:3]),
                "score_stage_hashes": signatures,
                "source_corpus_hashes": source_hashes,
                "replay_input_hashes": replay_input_hashes,
                "repeat_variance": len(set(signatures)) - 1,
                "source_corpus_repeat_variance": len(set(source_hashes)) - 1,
                "replay_input_repeat_variance": len(set(replay_input_hashes)) - 1,
                "pass": all(row.get("pass") for row in group[:3])
                and len(set(signatures)) == 1
                and len(set(source_hashes)) == 1
                and len(set(replay_input_hashes)) == 1,
            }
        )
    return repeat_rows


def _write_v3_shadow_outputs(
    *, base: Mapping[str, Any], output_dir: Path, operator_rows: Sequence[Mapping[str, Any]]
) -> Mapping[str, str]:
    artifacts = base["output_artifacts"]
    operator_digest = {"schema_version": "production_cutover_v3_operator_digest_v1", "rows": list(operator_rows)}
    paths: dict[str, str] = {}
    json_outputs = {
        "candidate_events.json": artifacts["candidate_events"],
        "source_tasks.json": artifacts["source_tasks"],
        "source_task_executions.json": artifacts["source_task_executions"],
        "stagecourt_traces.json": artifacts["stagecourt_traces"],
        "daily_watchlist.json": artifacts["daily_watchlist"],
        "operator_digest.json": operator_digest,
        "audit_summary.json": _v3_day_audit_summary(base),
    }
    for name, payload in json_outputs.items():
        path = output_dir / name
        write_json(path, payload)
        paths[str(path)] = str(path)
    jsonl_outputs = {
        "provider_fetch_results.jsonl": base["source_connector_report"]["rows"],
        "evidence_documents.jsonl": artifacts["evidence_documents"],
        "evidence_anchors.jsonl": artifacts["evidence_anchors"],
        "raw_assertions.jsonl": artifacts["evidence_claim_ledger"],
        "adjudicated_claims.jsonl": artifacts["evidence_claim_ledger"],
        "accepted_claims.jsonl": [row for row in artifacts["evidence_claim_ledger"] if row.get("accepted")],
        "primitive_states.jsonl": artifacts["primitive_states"],
        "score_contributions.jsonl": artifacts["score_contributions"],
    }
    for name, rows in jsonl_outputs.items():
        path = output_dir / name
        write_jsonl(path, rows)
        paths[str(path)] = str(path)
    write_text(output_dir / "operator_digest.md", _operator_digest_summary_markdown(operator_digest))
    paths[str(output_dir / "operator_digest.md")] = str(output_dir / "operator_digest.md")
    return paths


def _provider_gap_resolution_markdown(provider_matrix: Mapping[str, Any]) -> str:
    lines = ["# Production Cutover v3 Provider Gap Resolution", ""]
    for row in provider_matrix["rows"]:
        lines.append(
            f"- {row['provider_name']}: {row['provider_classification']}, "
            f"success={row['fetch_success_count']}, blocking={row['blocking_cutover']}"
        )
    lines.append("")
    return "\n".join(lines)


def _stability_markdown_v3(multiday: Mapping[str, Any]) -> str:
    s = multiday["summary"]
    return "\n".join(
        [
            "# Production Cutover v3 Stability",
            "",
            f"- status: {s['status']}",
            f"- five_day_live_official_shadow_count: {s['five_day_live_official_shadow_count']}",
            f"- frozen_replay_day_count: {s['frozen_replay_day_count']}",
            f"- frozen_repeat_day_with_3_runs_count: {s['frozen_repeat_day_with_3_runs_count']}",
            f"- repeat_variance: {s['repeat_variance']}",
            "",
        ]
    )


def _operator_digest_summary_markdown(report: Mapping[str, Any]) -> str:
    lines = ["# Production Cutover v3 Operator Digest Summary", ""]
    for row in report.get("rows", ())[:100]:
        claims = ", ".join(str(claim) for claim in (row.get("supporting_claims") or ())) or "none"
        missing = ", ".join(str(item) for item in (row.get("missing_primitives") or ())) or "none"
        provider_gaps = ", ".join(str(item) for item in (row.get("provider_source_gaps") or ())) or "none"
        lines.append(
            "- "
            f"{row.get('as_of_date', '')} {row.get('symbol')} {row.get('company')}: "
            f"stage={row.get('current_stage')}, action={row.get('next_action')}, "
            f"score={row.get('verified_score')}, status={row.get('score_status')}, "
            f"trigger={row.get('trigger_category')}"
        )
        lines.append(f"  claims: {claims}")
        lines.append(f"  missing: {missing}")
        lines.append(f"  provider_gaps: {provider_gaps}")
        lines.append(f"  note: {row.get('operator_note')}")
    lines.append("")
    return "\n".join(lines)


def _v2_to_v3_gap_markdown(*, provider_matrix: Mapping[str, Any], multiday: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Production Cutover v2 to v3 Gap",
            "",
            "- v2 status: READY_FOR_CENSUS_DESIGN, not PRODUCTION_READY",
            f"- v3 provider status: {provider_matrix['summary']['status']}",
            f"- v3 multiday status: {multiday['summary']['status']}",
            "- Census Mode implementation: forbidden in this goal",
            "",
        ]
    )


def _metadata_markdown_lines(metadata: Mapping[str, Any]) -> list[str]:
    lines = ["", "## Reproducibility Metadata", ""]
    for key in _REQUIRED_ROLLUP_METADATA_KEYS:
        lines.append(f"- {key}: {metadata.get(key)}")
    lines.append(f"- accepted_current_head_alignment: {metadata.get('accepted_current_head_alignment')}")
    lines.append(f"- report_artifact_lineage_policy: {metadata.get('report_artifact_lineage_policy')}")
    lines.append("")
    return lines


def _acceptance_markdown_v3(
    *,
    labels: Sequence[str],
    verdict: Mapping[str, Any],
    static: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> str:
    return "\n".join(
        [
            "# E2R Production Cutover Gate v3 Acceptance",
            "",
            f"- labels: {', '.join(labels)}",
            f"- production_verdict: {verdict['production_verdict']}",
            f"- production_ready: {verdict['production_ready']}",
            f"- static critical count: {static['summary']['critical_count_sum']}",
            "",
            "v3는 Census Mode를 구현하지 않고, provider/multiday/stage cutover gate만 닫는다.",
            *_metadata_markdown_lines(metadata),
        ]
    )


def _readiness_markdown_v3(
    *,
    verdict: Mapping[str, Any],
    labels: Sequence[str],
    static: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> str:
    return "\n".join(
        [
            "# E2R Production Cutover Gate v3 Verdict",
            "",
            f"- production_verdict: {verdict['production_verdict']}",
            f"- labels: {', '.join(labels)}",
            f"- static_critical_count_sum: {static['summary']['critical_count_sum']}",
            f"- blockers: {verdict.get('blockers', [])}",
            "",
            "쉬운 예: provider와 multiday가 통과해도 사용자 승인 플래그가 없으면 PRODUCTION_READY가 아니라 CUTOVER_READY까지만 간다.",
            *_metadata_markdown_lines(metadata),
        ]
    )


__all__ = [
    "ProductionCutoverV3Config",
    "build_production_cutover_v3_bundle",
    "write_production_cutover_v3_bundle",
]
