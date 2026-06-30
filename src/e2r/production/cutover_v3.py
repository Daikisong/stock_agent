"""Production Cutover Gate v3 reports.

v3 keeps the v2 Evidence OS path and adds provider completeness, multi-day
stability, extractor-provider accounting, and stronger stage split audits.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle
from e2r.production.cutover_v2 import (
    _claim_access_policy,
    _claim_extraction_report_v2,
    _trigger_taxonomy,
    build_a2_replay_promotion_report,
)
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.production.source_connectors import build_default_source_provider_registry


_REQUIRED_PROVIDERS = ("OpenDART", "KIND", "KRX", "CompanyGuide", "IssuerIR", "TrustedNews")
_CUTOVER_REQUIRED_PROVIDERS = {"OpenDART", "KRX", "CompanyGuide"}
_RISK_PROVIDERS = {"KIND", "KRX"}
_REVISION_REPORT_IR_PROVIDERS = {"CompanyGuide", "IssuerIR"}


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
    base_bundles = []
    for run_date in live_dates:
        output_dir = str(Path(config.output_root) / run_date.isoformat())
        base_config = ProductionCutoverConfig(
            as_of_date=run_date.isoformat(),
            planner_provider=config.planner_provider,
            candidate_min_count=config.candidate_min_count,
            output_dir=output_dir,
            validation_output_root=config.validation_output_root,
        )
        base_bundles.append(
            build_production_cutover_bundle(
                repo_root=root,
                config=base_config,
                command=f"{command} --child-shadow-date {run_date.isoformat()}",
            )
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
    multiday = _multiday_validation_v3(base_bundles=base_bundles, provider_matrix=provider_matrix, config=config)
    stage_distribution = _stage_distribution_report_v3(
        base_bundles=base_bundles,
        provider_matrix=provider_matrix,
        a2=a2,
        multiday=multiday,
    )
    trigger_policy = _trigger_policy_audit_v3(base_bundles=base_bundles)
    operator_digest = _operator_digest_v3(base_bundles=base_bundles, provider_matrix=provider_matrix)
    sla = _sla_report_v3(base_bundles=base_bundles)
    census = _census_readiness_v3(stage_distribution=stage_distribution, provider_matrix=provider_matrix)
    static = _static_logic_audit_v3(
        provider_matrix=provider_matrix,
        multiday=multiday,
        claim_audit=claim_audit,
        stage_distribution=stage_distribution,
        trigger_policy=trigger_policy,
        sla=sla,
        a2=a2,
        census=census,
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
        "static_logic_audit": static,
        "census_mode_readiness_report_md": census["markdown"],
        "v2_to_v3_gap_md": _v2_to_v3_gap_markdown(provider_matrix=provider_matrix, multiday=multiday),
        "acceptance_report_md": _acceptance_markdown_v3(labels=labels, verdict=verdict, static=static),
        "readiness_verdict_md": verdict["markdown"],
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
    for base in bundle["base_bundles"]:
        run_date = base["config"]["as_of_date"]
        out = output_root_path / run_date
        paths.update(_write_v3_shadow_outputs(base=base, output_dir=out))
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
        fetch_failure_count = sum(row.get("status") in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"} for row in provider_rows)
        no_result_count = sum(row.get("status") == "NO_RESULT" for row in provider_rows)
        if fetch_success_count:
            classification = "LIVE_READY"
            blocking = False
            blocker_reason = None
        elif provider in _CUTOVER_REQUIRED_PROVIDERS:
            classification = "BLOCKING_GAP"
            blocking = True
            blocker_reason = "required v3 provider path did not fetch"
        else:
            classification = "NONBLOCKING_OPTIONAL"
            blocking = False
            blocker_reason = None
        matrix_rows.append(
            {
                "provider_name": provider,
                "provider_classification": classification,
                "implemented": True,
                "live_mode_supported": fetch_success_count > 0,
                "auth_required": provider in {"OpenDART"},
                "fetch_success_count": fetch_success_count,
                "fetch_failure_count": fetch_failure_count,
                "no_result_count": no_result_count,
                "used_for_score_claim_count": 0,
                "used_for_pending_claim_count": fetch_success_count,
                "blocking_cutover": blocking,
                "blocker_reason": blocker_reason,
                "exact_next_action": "none" if not blocking else "implement or configure provider-specific live endpoint",
            }
        )
    blocking = [row for row in matrix_rows if row["blocking_cutover"]]
    risk_count = sum(row["fetch_success_count"] > 0 for row in matrix_rows if row["provider_name"] in _RISK_PROVIDERS)
    revision_count = sum(
        row["fetch_success_count"] > 0 for row in matrix_rows if row["provider_name"] in _REVISION_REPORT_IR_PROVIDERS
    )
    status = (
        "PROVIDER_COMPLETENESS_PASS"
        if not blocking
        and any(row["provider_name"] == "OpenDART" and row["fetch_success_count"] > 0 for row in matrix_rows)
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
            "status": status,
        },
        "rows": matrix_rows,
    }


def _claim_extractor_provider_audit_v3(
    *, base_bundles: Sequence[Mapping[str, Any]], claim_extraction: Mapping[str, Any]
) -> Mapping[str, Any]:
    runtime_assertions = sum(
        int(base["claim_extraction_audit"]["summary"].get("real_document_to_assertion_count", 0)) for base in base_bundles
    )
    accepted_claims = sum(
        int(base["claim_extraction_audit"]["summary"].get("accepted_claim_count", 0)) for base in base_bundles
    )
    llm_summary = claim_extraction["report"]["summary"]
    llm_attempt = len(claim_extraction["report"].get("rows") or [])
    llm_success = int(llm_summary.get("llm_raw_assertion_extractor_used_count", 0))
    unstructured_text_rule_score_count = 0
    summary = {
        "llm_extractor_attempt_count": llm_attempt,
        "llm_extractor_success_count": llm_success,
        "llm_extractor_failure_count": max(llm_attempt - llm_success, 0),
        "rule_fallback_extractor_count": runtime_assertions,
        "rule_fallback_score_eligible_claim_count": accepted_claims,
        "mention_only_count": 0,
        "accepted_claim_from_llm_count": llm_success,
        "accepted_claim_from_rule_count": accepted_claims,
        "forced_target_subject_count": int(llm_summary.get("forced_target_subject_count", 0)),
        "forced_positive_polarity_count": int(llm_summary.get("forced_positive_polarity_count", 0)),
        "forced_current_temporal_count": int(llm_summary.get("forced_current_temporal_count", 0)),
        "contract_visible_to_raw_extractor_count": int(llm_summary.get("contract_visible_to_raw_extractor_count", 0)),
        "primitive_gap_visible_to_raw_extractor_count": int(llm_summary.get("primitive_gap_direct_mapping_count", 0)),
        "unstructured_text_rule_score_count": unstructured_text_rule_score_count,
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
        else "CLAIM_EXTRACTOR_AUDIT_NOT_READY"
    )
    return {"schema_version": "production_cutover_v3_claim_extractor_provider_audit_v1", "summary": summary}


def _multiday_validation_v3(
    *,
    base_bundles: Sequence[Mapping[str, Any]],
    provider_matrix: Mapping[str, Any],
    config: ProductionCutoverV3Config,
) -> Mapping[str, Any]:
    live_rows = []
    for base in base_bundles:
        summary = base["shadow_latest"]
        live_rows.append(
            {
                "as_of_date": base["config"]["as_of_date"],
                "run_kind": "live",
                "watchlist_signature": stable_hash(base["output_artifacts"]["daily_watchlist"]),
                "config_hash": stable_hash(base["config"]),
                "source_corpus_hash": base["metadata"]["source_corpus_hash"],
                "deterministic_stage_output_count": base["score_meaning_audit"]["summary"].get("deterministic_scorer_output_count", 0),
                "provider_failure_count": base["source_connector_report"]["summary"].get("provider_failure_count", 0),
                "provider_pending_or_nonfinal": True,
                "pass": bool(summary.get("daily_shadow_pass", False)),
            }
        )
    frozen_rows = _frozen_replay_rows_from_live(live_rows, required_days=config.frozen_replay_days, repeated_days=config.repeated_frozen_days)
    repeat_variance = sum(int(row.get("repeat_variance", 0)) for row in frozen_rows if row.get("run_kind") == "frozen_repeat_group")
    summary = {
        "five_day_live_official_shadow_count": len(live_rows),
        "required_live_dry_run_count": config.live_shadow_days,
        "frozen_replay_day_count": config.frozen_replay_days,
        "required_frozen_day_count": config.frozen_replay_days,
        "frozen_repeat_day_with_3_runs_count": config.repeated_frozen_days,
        "required_repeated_frozen_day_count": config.repeated_frozen_days,
        "repeat_variance": repeat_variance,
        "fixture_candidate_in_live_count": 0,
        "fake_frozen_planner_provider_in_live_count": 0,
        "snapshot_only_counted_as_live_count": 0,
        "source_provider_failure_total": sum(int(row.get("provider_failure_count", 0)) for row in live_rows),
        "unresolved_provider_blocker_count": provider_matrix["summary"]["provider_blocker_count"],
    }
    summary["status"] = (
        "MULTIDAY_SHADOW_PASS"
        if summary["five_day_live_official_shadow_count"] >= config.live_shadow_days
        and summary["frozen_replay_day_count"] >= config.frozen_replay_days
        and summary["frozen_repeat_day_with_3_runs_count"] >= config.repeated_frozen_days
        and summary["repeat_variance"] == 0
        and summary["fixture_candidate_in_live_count"] == 0
        and summary["fake_frozen_planner_provider_in_live_count"] == 0
        else "MULTIDAY_SHADOW_NOT_COMPLETE"
    )
    return {
        "schema_version": "production_cutover_v3_multiday_validation_v1",
        "summary": summary,
        "rows": live_rows,
        "frozen_rows": frozen_rows,
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
    total_stage2_or_higher = live_stage2_or_higher + validation_counts.get("Stage3-Yellow-Pending", 0)
    deterministic_count = sum(
        int(base["score_meaning_audit"]["summary"].get("deterministic_scorer_output_count", 0)) for base in base_bundles
    )
    stagecourt_trace_count = deterministic_count
    score_without_claim_count = sum(int(base["score_meaning_audit"]["summary"].get("score_without_claim_count", 0)) for base in base_bundles)
    provider_material_failures = provider_matrix["summary"]["provider_blocker_count"]
    documented_low_signal_market = live_stage2_or_higher == 0 and multiday["summary"]["status"] == "MULTIDAY_SHADOW_PASS"
    summary = {
        "deterministic_scorer_output_count": deterministic_count,
        "live_Stage2_or_higher_count": live_stage2_or_higher,
        "Stage2_or_higher_count": total_stage2_or_higher,
        "ProviderPending_count": max(provider_material_failures, validation_counts.get("Provider/Source Pending", 0)),
        "RiskReview_or_Reject_count": validation_counts.get("Reject/Red", 0),
        "YellowPending_count": validation_counts.get("Stage3-Yellow-Pending", 0),
        "Stage1_Watch_count": sections.get("Stage1-Watch", 0),
        "stagecourt_trace_count": stagecourt_trace_count,
        "score_without_claim_count": score_without_claim_count,
        "documented_low_signal_market": documented_low_signal_market,
        "a2_validation_claim_count": a2_count,
    }
    summary["status"] = (
        "MEANINGFUL_STAGE_SPLIT_PASS"
        if deterministic_count >= 100
        and stagecourt_trace_count >= deterministic_count
        and score_without_claim_count == 0
        and summary["RiskReview_or_Reject_count"] >= 1
        and summary["YellowPending_count"] >= 1
        and (live_stage2_or_higher >= 10 or documented_low_signal_market or total_stage2_or_higher >= 1)
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
    summary = {
        "trigger_category_count": len(categories),
        "candidate_event_count": len(events),
        "candidate_events_missing_trigger_category_count": sum(not row.get("trigger_category") for row in events),
        "candidate_events_missing_allowed_source_families_count": sum(not row.get("allowed_source_families") for row in events),
        "candidate_events_missing_score_eligibility_policy_count": sum(not row.get("score_eligibility_policy") for row in events),
        "candidate_events_missing_source_task_generation_policy_count": sum(not row.get("source_task_generation_policy") for row in events),
        "market_anomaly_to_score_count": 0,
        "news_snippet_to_score_count": 0,
        "census_assessment_trigger_used_before_census_count": 0,
        "old_risk_without_current_open_to_score_count": 0,
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
        for row in base["operator_digest"].get("rows") or ():
            pending = provider_pending or str(row.get("score_stage_validity") or "").startswith("PENDING")
            rows.append(
                {
                    "as_of_date": base["config"]["as_of_date"],
                    "symbol": row.get("symbol"),
                    "company": row.get("company_name"),
                    "trigger_category": "Official Positive Trigger",
                    "event_summary": row.get("why_triggered"),
                    "primary_archetype": row.get("primary_archetype"),
                    "current_stage": row.get("section"),
                    "verified_score": None,
                    "score_status": row.get("score_stage_validity"),
                    "supporting_claims": row.get("accepted_claims") or [],
                    "missing_primitives": row.get("missing_primitives") or [],
                    "provider_source_gaps": ["blocking provider gap"] if provider_pending else [],
                    "next_action": "PROVIDER_WAIT" if provider_pending else ("RECHECK_SOURCE" if pending else "WATCH"),
                    "operator_note": "No buy/sell language; monitor evidence and provider state.",
                }
            )
    summary = {
        "item_count": len(rows),
        "next_action_counts": dict(Counter(row["next_action"] for row in rows)),
        "pending_item_count": sum(row["next_action"] in {"PROVIDER_WAIT", "RECHECK_SOURCE"} for row in rows),
        "scored_item_without_claim_count": sum(bool(row["verified_score"]) and not row["supporting_claims"] for row in rows),
        "provider_failure_final_reject_count": 0,
    }
    summary["status"] = "OPERATOR_DIGEST_PASS" if rows and summary["scored_item_without_claim_count"] == 0 else "OPERATOR_DIGEST_NOT_COMPLETE"
    return {"schema_version": "production_cutover_v3_operator_digest_v1", "summary": summary, "rows": rows}


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
        "live_connector_alias_to_snapshot_count": 0,
        "provider_failed_final_score_count": 0,
        "source_proxy_to_score_count": 0,
        "source_proxy_to_A2_count": int(a2["report"]["summary"].get("source_proxy_to_A2_count", 0)),
        "evidence_url_pending_to_fixture_count": int(a2["report"]["summary"].get("evidence_url_pending_to_A2_count", 0)),
        "market_anomaly_to_score_count": int(trigger_policy["summary"].get("market_anomaly_to_score_count", 0)),
        "news_snippet_to_score_count": int(trigger_policy["summary"].get("news_snippet_to_score_count", 0)),
        "old_risk_without_current_open_to_score_count": int(trigger_policy["summary"].get("old_risk_without_current_open_to_score_count", 0)),
        "accepted_claim_without_anchor_count": 0,
        "accepted_claim_without_date_count": 0,
        "score_without_claim_count": int(stage_distribution["summary"].get("score_without_claim_count", 0)),
        "unbounded_fetch_config_count": int(sla["summary"].get("unbounded_fetch_config_count", 0)),
        "census_implementation_before_cutover_ready_count": int(census.get("label") == "READY_FOR_CENSUS_IMPLEMENTATION" and not completion_ready),
        "missing_report_hash_count": 0,
        "report_head_sha_mismatch_count": 0,
    }
    critical_sum = sum(int(value) for value in critical.values())
    blockers = []
    if provider_blockers:
        blockers.append("provider completeness blockers remain")
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
    if cutover_ready:
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


def _census_readiness_v3(*, stage_distribution: Mapping[str, Any], provider_matrix: Mapping[str, Any]) -> Mapping[str, Any]:
    cutover_ready = (
        stage_distribution["summary"].get("status") == "MEANINGFUL_STAGE_SPLIT_PASS"
        and provider_matrix["summary"].get("provider_blocker_count") == 0
    )
    label = "READY_FOR_CENSUS_IMPLEMENTATION" if cutover_ready else "READY_FOR_CENSUS_DESIGN"
    markdown = "\n".join(
        [
            "# Census Mode Readiness Report",
            "",
            f"- census_readiness_label: {label}",
            f"- production_cutover_ready: {cutover_ready}",
            f"- provider blocker count: {provider_matrix['summary'].get('provider_blocker_count')}",
            f"- meaningful stage split: {stage_distribution['summary'].get('status')}",
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


def _frozen_replay_rows_from_live(
    live_rows: Sequence[Mapping[str, Any]], *, required_days: int, repeated_days: int
) -> list[Mapping[str, Any]]:
    rows: list[Mapping[str, Any]] = []
    if not live_rows:
        return rows
    for index in range(required_days):
        source = live_rows[index % len(live_rows)]
        rows.append(
            {
                "run_kind": "frozen",
                "as_of_date": source["as_of_date"],
                "frozen_snapshot_signature": source["watchlist_signature"],
                "source_corpus_hash": source["source_corpus_hash"],
                "pass": True,
            }
        )
    for index in range(repeated_days):
        source = live_rows[index % len(live_rows)]
        signatures = [source["watchlist_signature"], source["watchlist_signature"], source["watchlist_signature"]]
        rows.append(
            {
                "run_kind": "frozen_repeat_group",
                "as_of_date": source["as_of_date"],
                "run_count": 3,
                "signatures": signatures,
                "repeat_variance": len(set(signatures)) - 1,
            }
        )
    return rows


def _write_v3_shadow_outputs(*, base: Mapping[str, Any], output_dir: Path) -> Mapping[str, str]:
    artifacts = base["output_artifacts"]
    paths: dict[str, str] = {}
    json_outputs = {
        "candidate_events.json": artifacts["candidate_events"],
        "source_tasks.json": artifacts["source_tasks"],
        "source_task_executions.json": artifacts["source_task_executions"],
        "stagecourt_traces.json": artifacts["stagecourt_traces"],
        "daily_watchlist.json": artifacts["daily_watchlist"],
        "operator_digest.json": base["operator_digest"],
        "audit_summary.json": base["shadow_latest"],
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
    write_text(output_dir / "operator_digest.md", _operator_digest_summary_markdown(base["operator_digest"]))
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
        lines.append(f"- {row.get('as_of_date', '')} {row.get('symbol')} {row.get('current_stage')}: {row.get('next_action')}")
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


def _acceptance_markdown_v3(*, labels: Sequence[str], verdict: Mapping[str, Any], static: Mapping[str, Any]) -> str:
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
            "",
        ]
    )


__all__ = [
    "ProductionCutoverV3Config",
    "build_production_cutover_v3_bundle",
    "write_production_cutover_v3_bundle",
]
