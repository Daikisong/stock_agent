"""Leaf-backed readiness gate for meaningful E2R scoring."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from .component_assessment import TERMINAL_FULL_SCORE_STATUSES
from .evidence_origin import partition_scoring_evidence


SCORING_READINESS_SCHEMA_VERSION_V2 = "e2r_meaningful_scoring_readiness_v2"
SCORING_READINESS_SCHEMA_VERSION = "e2r_meaningful_scoring_readiness_v3"
READY = "ORGANIC_EVIDENCE_TO_SCORE_PIPELINE_PARTIAL_PASS"
MEANINGFUL_READY_V2 = "MEANINGFUL_E2R_SCORING_READY_V2"
NOT_READY = "MEANINGFUL_E2R_SCORING_NOT_READY"
SEMANTIC_NOT_READY = "SEMANTIC_SCORING_CLOSURE_NOT_READY"
RESEARCH_NOT_VERIFIED = "RESEARCH_GRADE_EVIDENCE_ACQUISITION_NOT_VERIFIED"

REQUIRED_DOSSIER_LEAVES = (
    "accepted_current_claims.jsonl",
    "claim_impacts_validated.jsonl",
    "component_assessments.jsonl",
    "component_score_vector.json",
    "atomic_stage_decision.json",
    "stagecourt_trace.json",
)

REQUIRED_DOSSIER_LEAVES_V3 = (
    *REQUIRED_DOSSIER_LEAVES,
    "claim_eligibility_decisions.jsonl",
    "question_component_reconciliation.jsonl",
    "evidence_search_adequacy.jsonl",
    "economic_fact_clusters.jsonl",
    "document_clusters.jsonl",
    "impact_validation_audit.json",
    "component_assessment_audit.json",
    "question_component_reconciliation_audit.json",
    "scoring_schema_totality_audit.json",
    "full_score_validity_v2.json",
)

V3_REQUIRED_CRITICAL_SOURCES = {
    "missing_scoring_policy_count": (
        "scoring_schema_totality",
        "missing_scoring_key_count",
    ),
    "silent_zero_default_count": (
        "scoring_schema_totality",
        "silent_zero_default_count",
    ),
    "positive_impact_zeroed_by_missing_cap_count": (
        "impact_validator_v2",
        "positive_impact_zeroed_by_missing_cap_count",
    ),
    "counter_impact_zeroed_by_missing_cap_count": (
        "impact_validator_v2",
        "counter_impact_zeroed_by_missing_cap_count",
    ),
    "cross_business_question_closure_count": (
        "business_mechanism_scope",
        "cross_business_question_closure_count",
    ),
    "supported_question_absent_component_count": (
        "question_component_reconciliation",
        "supported_question_absent_component_count",
    ),
    "positive_claim_absent_component_count": (
        "question_component_reconciliation",
        "positive_claim_absent_component_count",
    ),
    "absence_with_inadequate_search_count": (
        "question_component_reconciliation",
        "absence_with_inadequate_search_count",
    ),
    "counter_impact_ignored_count": (
        "counter_component",
        "counter_impact_ignored_count",
    ),
    "same_fact_duplicate_credit_count": (
        "fact_document_dedupe",
        "same_fact_duplicate_credit_count",
    ),
    "same_document_duplicate_credit_count": (
        "fact_document_dedupe",
        "same_document_duplicate_credit_count",
    ),
    "claim_count_event_boost_count": (
        "full_thesis_event_separation",
        "claim_count_event_boost_count",
    ),
    "eligibility_contradiction_count": (
        "claim_eligibility",
        "eligibility_boolean_contradiction_count",
    ),
    "critical_material_fact_miss_count": (
        "research_quality_gold",
        "critical_material_fact_miss_count",
    ),
}


def compile_meaningful_scoring_readiness(
    *, config_path: str | Path, verify_repository: bool = False
) -> Mapping[str, Any]:
    config_file = Path(config_path)
    config = _read_json(config_file)
    schema_version = str(config.get("schema_version") or "")
    if schema_version == SCORING_READINESS_SCHEMA_VERSION:
        return _compile_meaningful_scoring_readiness_v3(
            config_file=config_file,
            config=config,
            verify_repository=verify_repository,
        )
    if schema_version != SCORING_READINESS_SCHEMA_VERSION_V2:
        raise ValueError("meaningful scoring readiness config schema mismatch")

    target_results = tuple(
        _read_and_evaluate_target(
            target={**dict(row), "as_of_date": config["as_of_date"]},
            base_dir=config_file.resolve().parent.parent,
            required_components=tuple(config["required_component_ids"]),
        )
        for row in config.get("mandatory_targets") or ()
    )
    global_audits = tuple(
        _read_global_audit(
            row=dict(row), base_dir=config_file.resolve().parent.parent
        )
        for row in config.get("required_global_audits") or ()
    )
    repository = _repository_verification() if verify_repository else {
        "status": "NOT_VERIFIED_IN_THIS_RUN",
        "critical_count_sum": 0,
        "repo_dirty": None,
        "head_origin_same_commit": None,
    }
    target_critical = sum(int(row["critical_count_sum"]) for row in target_results)
    audit_critical = sum(int(row["critical_count_sum"]) for row in global_audits)
    repository_critical = int(repository["critical_count_sum"])
    mandatory_ids = {
        str(row.get("target_id") or "") for row in config.get("mandatory_targets") or ()
    }
    observed_ids = {str(row.get("target_id") or "") for row in target_results}
    target_roster_mismatch = len(mandatory_ids ^ observed_ids)
    live_materialization_missing = int(
        not any(
            row["audit_id"] == "live_materialization"
            and row["critical_count_sum"] == 0
            for row in global_audits
        )
    )
    critical = (
        target_critical
        + audit_critical
        + repository_critical
        + target_roster_mismatch
        + live_materialization_missing
    )

    organic_claim_count = sum(int(row["counts"]["organic_accepted_claim_count"]) for row in target_results)
    validated_impact_count = sum(int(row["counts"]["organic_validated_impact_count"]) for row in target_results)
    verified_points = round(
        sum(
            float(row["counts"]["organic_verified_component_points"])
            for row in target_results
        ),
        6,
    )
    calibrated_profile_count = sum(int(row["counts"]["calibrated_profile_used_count"]) for row in target_results)
    full_score_valid_canary_count = sum(bool(row["facts"].get("full_score_valid")) for row in target_results)

    intermediate_labels = _intermediate_labels(
        target_results,
        global_audits=global_audits,
        configured_targets=tuple(config.get("mandatory_targets") or ()),
    )
    blockers = [
        f"{row['target_id']}:{name}"
        for row in target_results
        for name, value in row["critical_counts"].items()
        if value
    ]
    blockers.extend(
        f"global:{row['audit_id']}:{name}"
        for row in global_audits
        for name, value in row["critical_counts"].items()
        if value
    )
    if target_roster_mismatch:
        blockers.append("mandatory_target_roster_mismatch")
    if live_materialization_missing:
        blockers.append("live_materialization_pass_missing")
    if repository_critical:
        blockers.append("repository_verification_failed")

    return {
        "schema_version": SCORING_READINESS_SCHEMA_VERSION_V2,
        "status": READY if critical == 0 else NOT_READY,
        "exact_final_verdict": SEMANTIC_NOT_READY if critical == 0 else NOT_READY,
        "research_grade_acquisition_status": RESEARCH_NOT_VERIFIED,
        "legacy_ready_alias_active": False,
        "readiness_v3_required": True,
        "v2_deprecated": True,
        "as_of_date": config["as_of_date"],
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "intermediate_labels": intermediate_labels,
        "mandatory_target_count": len(mandatory_ids),
        "target_results": target_results,
        "global_audits": global_audits,
        "repository_verification": repository,
        "counts": {
            "organic_accepted_claim_count": organic_claim_count,
            "organic_validated_impact_count": validated_impact_count,
            "organic_verified_component_points": verified_points,
            "calibrated_profile_used_count": calibrated_profile_count,
            "full_score_valid_canary_count": full_score_valid_canary_count,
            "full_e2r_100_canary_count": sum(
                row["facts"].get("score_type") == "FULL_E2R_100"
                for row in target_results
            ),
            "no_score_only_target_count": sum(
                row["facts"].get("score_type") in {None, "NO_SCORE"}
                for row in target_results
            ),
            "probe_claim_counted_organic_count": sum(
                int(row["counts"]["probe_claim_counted_organic_count"])
                for row in target_results
            ),
        },
        "blockers": blockers,
        "critical_count_sum": critical,
        "hard_acceptance_pass": critical == 0,
        "investment_recommendation_emitted": False,
    }


def _compile_meaningful_scoring_readiness_v3(
    *,
    config_file: Path,
    config: Mapping[str, Any],
    verify_repository: bool,
) -> Mapping[str, Any]:
    base_dir = config_file.resolve().parent.parent
    target_results = tuple(
        _read_and_evaluate_target_v3(
            target={**dict(row), "as_of_date": config["as_of_date"]},
            base_dir=base_dir,
            required_components=tuple(config["required_component_ids"]),
        )
        for row in config.get("mandatory_targets") or ()
    )
    global_audits = tuple(
        _read_global_audit(row=dict(row), base_dir=base_dir)
        for row in config.get("required_global_audits") or ()
    )
    repository = (
        _repository_verification()
        if verify_repository
        else {
            "status": "NOT_VERIFIED_IN_THIS_RUN",
            "critical_count_sum": 0,
            "repo_dirty": None,
            "head_origin_same_commit": None,
        }
    )
    mandatory_ids = {
        str(row.get("target_id") or "")
        for row in config.get("mandatory_targets") or ()
    }
    observed_ids = {
        str(row.get("target_id") or "") for row in target_results
    }
    target_roster_mismatch = len(mandatory_ids ^ observed_ids)
    mandatory_target_missing = int(not mandatory_ids)
    live_materialization_missing = int(
        not any(
            row["audit_id"] == "live_materialization"
            and row["critical_count_sum"] == 0
            for row in global_audits
        )
    )
    global_semantic = _v3_global_semantic_critical_counts(global_audits)
    target_semantic = {
        name: sum(
            int(row.get("semantic_critical_counts", {}).get(name) or 0)
            for row in target_results
        )
        for name in V3_REQUIRED_CRITICAL_SOURCES
    }
    semantic_critical = {
        name: global_semantic[name] + target_semantic[name]
        for name in V3_REQUIRED_CRITICAL_SOURCES
    }
    target_critical = sum(
        int(row["critical_count_sum"]) for row in target_results
    )
    audit_critical = sum(
        int(row["critical_count_sum"]) for row in global_audits
    )
    repository_critical = int(repository["critical_count_sum"])
    # Target semantic counts are already included in each target critical sum.
    global_semantic_critical = sum(global_semantic.values())
    critical = (
        target_critical
        + audit_critical
        + repository_critical
        + target_roster_mismatch
        + mandatory_target_missing
        + live_materialization_missing
        + global_semantic_critical
    )
    ready = critical == 0
    organic_claim_count = sum(
        int(row["counts"]["organic_accepted_claim_count"])
        for row in target_results
    )
    validated_impact_count = sum(
        int(row["counts"]["organic_validated_impact_count"])
        for row in target_results
    )
    verified_points = round(
        sum(
            float(row["counts"]["organic_verified_component_points"])
            for row in target_results
        ),
        6,
    )
    blockers = [
        f"{row['target_id']}:{name}"
        for row in target_results
        for name, value in row["critical_counts"].items()
        if value
    ]
    blockers.extend(
        f"global:{row['audit_id']}:{name}"
        for row in global_audits
        for name, value in row["critical_counts"].items()
        if value
    )
    blockers.extend(
        f"semantic:{name}"
        for name, value in global_semantic.items()
        if value
    )
    if target_roster_mismatch:
        blockers.append("mandatory_target_roster_mismatch")
    if mandatory_target_missing:
        blockers.append("mandatory_target_missing")
    if live_materialization_missing:
        blockers.append("live_materialization_pass_missing")
    if repository_critical:
        blockers.append("repository_verification_failed")
    research_grade_pass = any(
        row["audit_id"] == "research_quality_gold"
        and row["critical_count_sum"] == 0
        for row in global_audits
    )
    return {
        "schema_version": SCORING_READINESS_SCHEMA_VERSION,
        "status": MEANINGFUL_READY_V2 if ready else NOT_READY,
        "exact_final_verdict": MEANINGFUL_READY_V2 if ready else NOT_READY,
        "pass_only_final_label": MEANINGFUL_READY_V2,
        "research_grade_acquisition_status": (
            "RESEARCH_GRADE_EVIDENCE_ACQUISITION_PASS"
            if research_grade_pass
            else RESEARCH_NOT_VERIFIED
        ),
        "legacy_ready_alias_active": False,
        "legacy_ready_alias_allowed": ready,
        "readiness_v3_required": False,
        "v2_deprecated": True,
        "as_of_date": config["as_of_date"],
        "generated_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        ),
        "intermediate_labels": _intermediate_labels(
            target_results,
            global_audits=global_audits,
            configured_targets=tuple(config.get("mandatory_targets") or ()),
        ),
        "mandatory_target_count": len(mandatory_ids),
        "target_results": target_results,
        "global_audits": global_audits,
        "repository_verification": repository,
        "semantic_critical_counts": semantic_critical,
        "semantic_critical_count_sum": sum(semantic_critical.values()),
        "counts": {
            "organic_accepted_claim_count": organic_claim_count,
            "organic_validated_impact_count": validated_impact_count,
            "organic_verified_component_points": verified_points,
            "calibrated_profile_used_count": sum(
                int(row["counts"]["calibrated_profile_used_count"])
                for row in target_results
            ),
            "full_score_valid_canary_count": sum(
                row["facts"].get("full_score_valid") is True
                for row in target_results
            ),
            "full_e2r_100_canary_count": sum(
                row["facts"].get("score_type") == "FULL_E2R_100"
                for row in target_results
            ),
            "no_score_only_target_count": sum(
                row["facts"].get("score_type") in {None, "NO_SCORE"}
                for row in target_results
            ),
            "probe_claim_counted_organic_count": sum(
                int(row["counts"]["probe_claim_counted_organic_count"])
                for row in target_results
            ),
        },
        "blockers": list(dict.fromkeys(blockers)),
        "critical_count_sum": critical,
        "hard_acceptance_pass": ready,
        "investment_recommendation_emitted": False,
    }


def write_meaningful_scoring_readiness(
    verdict: Mapping[str, Any], *, output_path: str | Path
) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# E2R Meaningful Scoring Readiness Verdict",
        "",
        f"- final status: {verdict['status']}",
        *(
            [f"- pass-only final label: {verdict['pass_only_final_label']}"]
            if verdict.get("pass_only_final_label")
            else []
        ),
        f"- as_of_date: {verdict['as_of_date']}",
        f"- mandatory targets: {verdict['mandatory_target_count']}",
        f"- organic accepted claims: {verdict['counts']['organic_accepted_claim_count']}",
        f"- organic validated impacts: {verdict['counts']['organic_validated_impact_count']}",
        f"- organic verified component points: {verdict['counts']['organic_verified_component_points']}",
        f"- full score valid canaries: {verdict['counts']['full_score_valid_canary_count']}",
        f"- critical_count_sum: {verdict['critical_count_sum']}",
        f"- blockers: {verdict['blockers']}",
        f"- research-grade acquisition: {verdict['research_grade_acquisition_status']}",
        f"- legacy READY alias active: {str(verdict['legacy_ready_alias_active']).lower()}",
        f"- readiness v3 required: {str(verdict['readiness_v3_required']).lower()}",
        f"- v2 deprecated: {str(verdict.get('v2_deprecated', False)).lower()}",
        "- investment recommendation emitted: false",
        "",
        "## Mandatory Target Gates",
        "",
    ]
    for row in verdict["target_results"]:
        lines.append(
            f"- {row['target_id']} ({row['company_name']}): {row['status']}; "
            f"claims={row['counts']['organic_accepted_claim_count']}, "
            f"impacts={row['counts']['organic_validated_impact_count']}, "
            f"points={row['counts']['organic_verified_component_points']}, "
            f"score_type={row['facts'].get('score_type')}"
        )
    lines.extend(("", "## Required Global Audits", ""))
    for row in verdict["global_audits"]:
        lines.append(
            f"- {row['audit_id']}: {row['observed_status']}; "
            f"critical={row['critical_count_sum']}"
        )
    if "semantic_critical_counts" in verdict:
        lines.extend(("", "## Semantic Critical Counts", ""))
        for name, value in verdict["semantic_critical_counts"].items():
            lines.append(f"- {name}: {value}")
    repository = verdict["repository_verification"]
    lines.extend(
        (
            "",
            "## Repository Verification",
            "",
            f"- status: {repository['status']}",
            f"- repo_dirty: {repository['repo_dirty']}",
            f"- head_origin_same_commit: {repository['head_origin_same_commit']}",
        )
    )
    lines.extend(("", "## Exact Final Verdict", "", str(verdict["exact_final_verdict"]), ""))
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _read_and_evaluate_target(
    *, target: Mapping[str, Any], base_dir: Path, required_components: Sequence[str]
) -> Mapping[str, Any]:
    root = _resolve_path(base_dir, str(target["dossier_root"]))
    missing = tuple(name for name in REQUIRED_DOSSIER_LEAVES if not (root / name).is_file())
    if missing:
        return _evaluate_target(
            target=target,
            required_components=required_components,
            claims=(),
            impacts=(),
            assessments=(),
            score={},
            decision={},
            trace={},
            missing_leaves=missing,
        )
    return _evaluate_target(
        target=target,
        required_components=required_components,
        claims=_read_jsonl(root / "accepted_current_claims.jsonl"),
        impacts=_read_jsonl(root / "claim_impacts_validated.jsonl"),
        assessments=_read_jsonl(root / "component_assessments.jsonl"),
        score=_read_json(root / "component_score_vector.json"),
        decision=_read_json(root / "atomic_stage_decision.json"),
        trace=_read_json(root / "stagecourt_trace.json"),
        missing_leaves=(),
    )


def _read_and_evaluate_target_v3(
    *,
    target: Mapping[str, Any],
    base_dir: Path,
    required_components: Sequence[str],
) -> Mapping[str, Any]:
    root = _resolve_path(base_dir, str(target["dossier_root"]))
    missing = tuple(
        name
        for name in REQUIRED_DOSSIER_LEAVES_V3
        if not (root / name).is_file()
    )
    if missing:
        base = _evaluate_target(
            target=target,
            required_components=required_components,
            claims=(),
            impacts=(),
            assessments=(),
            score={},
            decision={},
            trace={},
            missing_leaves=missing,
        )
        return _merge_v3_target_semantics(
            base=base,
            semantic_counts={name: 1 for name in V3_REQUIRED_CRITICAL_SOURCES},
            additional_critical={
                "v3_semantic_leaf_missing_count": len(missing),
                "full_score_validity_v2_failure_count": 1,
            },
        )
    claims = _read_jsonl(root / "accepted_current_claims.jsonl")
    impacts = _read_jsonl(root / "claim_impacts_validated.jsonl")
    assessments = _read_jsonl(root / "component_assessments.jsonl")
    score = _read_json(root / "component_score_vector.json")
    decision = _read_json(root / "atomic_stage_decision.json")
    trace = _read_json(root / "stagecourt_trace.json")
    base = _evaluate_target(
        target=target,
        required_components=required_components,
        claims=claims,
        impacts=impacts,
        assessments=assessments,
        score=score,
        decision=decision,
        trace=trace,
        missing_leaves=(),
    )
    eligibility = _read_jsonl(root / "claim_eligibility_decisions.jsonl")
    reconciliations = _read_jsonl(
        root / "question_component_reconciliation.jsonl"
    )
    adequacy = _read_jsonl(root / "evidence_search_adequacy.jsonl")
    impact_audit = _read_json(root / "impact_validation_audit.json")
    component_audit = _read_json(root / "component_assessment_audit.json")
    reconciliation_audit = _read_json(
        root / "question_component_reconciliation_audit.json"
    )
    schema_audit = _read_json(root / "scoring_schema_totality_audit.json")
    validity = _read_json(root / "full_score_validity_v2.json")
    semantic = _target_semantic_critical_counts(
        impacts=impacts,
        eligibility=eligibility,
        reconciliations=reconciliations,
        adequacy=adequacy,
        impact_audit=impact_audit,
        component_audit=component_audit,
        reconciliation_audit=reconciliation_audit,
        schema_audit=schema_audit,
        decision=decision,
    )
    score_validity = (score.get("audit") or {}).get(
        "full_score_validity", {}
    )
    additional = {
        "v3_semantic_leaf_missing_count": 0,
        "unresolved_contradiction_count": sum(
            row.get("status") == "CONTRADICTED_OPEN"
            or row.get("contradiction_status") == "CONTRADICTED_OPEN"
            for row in assessments
        ),
        "semantic_pending_state_count": sum(
            row.get("status")
            in {
                "UNKNOWN_UNINVESTIGATED",
                "SOURCE_PENDING",
                "PROVIDER_PENDING",
                "BUDGET_PENDING",
                "HISTORICAL_ONLY",
            }
            for row in assessments
        ),
        "full_score_validity_v2_failure_count": int(
            validity.get("status") != "FULL_SCORE_VALIDITY_V2_PASS"
            or int(validity.get("critical_count_sum") or 0) != 0
            or validity.get("full_score_valid") is not True
            or score_validity.get("validity_id") != validity.get("validity_id")
        ),
    }
    return _merge_v3_target_semantics(
        base=base,
        semantic_counts=semantic,
        additional_critical=additional,
    )


def _merge_v3_target_semantics(
    *,
    base: Mapping[str, Any],
    semantic_counts: Mapping[str, int],
    additional_critical: Mapping[str, int],
) -> Mapping[str, Any]:
    critical = {
        **dict(base["critical_counts"]),
        **{name: int(value) for name, value in semantic_counts.items()},
        **{name: int(value) for name, value in additional_critical.items()},
    }
    return {
        **dict(base),
        "status": (
            "CANONICAL_FULL_THESIS_PASS"
            if sum(critical.values()) == 0
            else "CANONICAL_FULL_THESIS_NOT_READY"
        ),
        "semantic_critical_counts": dict(semantic_counts),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def _target_semantic_critical_counts(
    *,
    impacts: Sequence[Mapping[str, Any]],
    eligibility: Sequence[Mapping[str, Any]],
    reconciliations: Sequence[Mapping[str, Any]],
    adequacy: Sequence[Mapping[str, Any]],
    impact_audit: Mapping[str, Any],
    component_audit: Mapping[str, Any],
    reconciliation_audit: Mapping[str, Any],
    schema_audit: Mapping[str, Any],
    decision: Mapping[str, Any],
) -> Mapping[str, int]:
    schema_counts = schema_audit.get("critical_counts") or {}
    impact_counts = impact_audit.get("critical_counts") or {}
    component_counts = component_audit.get("critical_counts") or {}
    reconciliation_counts = reconciliation_audit.get("critical_counts") or {}
    credited = tuple(
        row
        for row in impacts
        if float(row.get("validated_credit_fraction") or 0.0) > 0
        and row.get("corroboration_only") is not True
    )
    decision_by_id = {
        str(row.get("eligibility_decision_id") or ""): row
        for row in eligibility
        if str(row.get("eligibility_decision_id") or "")
    }
    eligibility_contradictions = sum(
        not str(row.get("eligibility_decision_id") or "")
        or decision_by_id.get(
            str(row.get("eligibility_decision_id") or ""), {}
        ).get("component_scoring_eligibility")
        is not True
        for row in credited
    )
    supported_absent = sum(
        str(row.get("input_closure_status") or "")
        in {"SUPPORTED_SCORING", "PARTIALLY_SUPPORTED_SCORING"}
        and not row.get("component_links")
        for row in reconciliations
    )
    positive_claim_absent = sum(
        len(
            {
                str(value)
                for value in row.get("positive_scoring_claim_ids") or ()
            }
            - {
                str(link.get("claim_id") or "")
                for link in row.get("component_links") or ()
            }
        )
        for row in reconciliations
        if row.get("provider_failure") is not True
    )
    adequacy_by_question = {
        str(row.get("question_family_id") or ""): row for row in adequacy
    }
    inadequate_absence = sum(
        str(row.get("input_closure_status") or "") == "EVALUATED_ABSENT"
        and not _readiness_adequate_absence(
            adequacy_by_question.get(
                str(row.get("question_family_id") or "")
            )
        )
        for row in reconciliations
    )
    same_fact_duplicate = _duplicate_credit_count(
        credited,
        fields=("fact_cluster_id", "component_id", "direction"),
    )
    same_document_duplicate = _duplicate_credit_count(
        tuple(
            row
            for row in credited
            if row.get("component_id") == "information_confidence"
        ),
        fields=("document_cluster_id", "component_id", "direction"),
    )
    event_overlay = decision.get("event_overlay") or {}
    event_stage_injection = int(
        event_overlay.get("canonical_stage_effect") not in {None, "NONE"}
        or (
            decision.get("full_thesis_stage") is not None
            and decision.get("canonical_stage")
            != decision.get("full_thesis_stage")
        )
        or any(
            "company-level event" in str(reason).casefold()
            for reason in decision.get("stage_reason") or ()
        )
    )
    return {
        "missing_scoring_policy_count": int(
            _required_nonnegative_counter(
                schema_counts, "missing_scoring_key_count"
            )
        ),
        "silent_zero_default_count": int(
            _required_nonnegative_counter(
                schema_counts, "silent_zero_default_count"
            )
        ),
        "positive_impact_zeroed_by_missing_cap_count": int(
            _required_nonnegative_counter(
                impact_counts,
                "positive_impact_zeroed_by_missing_cap_count",
            )
        ),
        "counter_impact_zeroed_by_missing_cap_count": int(
            _required_nonnegative_counter(
                impact_counts,
                "counter_impact_zeroed_by_missing_cap_count",
            )
        ),
        "cross_business_question_closure_count": sum(
            (row.get("scope_validation") or {}).get("scope_match") is not True
            for row in credited
        ),
        "supported_question_absent_component_count": max(
            supported_absent,
            _required_nonnegative_counter(
                reconciliation_counts,
                "supported_question_absent_component_count",
            ),
        ),
        "positive_claim_absent_component_count": max(
            positive_claim_absent,
            _required_nonnegative_counter(
                reconciliation_counts,
                "positive_claim_absent_component_count",
            ),
        ),
        "absence_with_inadequate_search_count": max(
            inadequate_absence,
            _required_nonnegative_counter(
                reconciliation_counts,
                "absence_with_inadequate_search_count",
            ),
        ),
        "counter_impact_ignored_count": _required_nonnegative_counter(
            component_counts, "counter_impact_ignored_count"
        ),
        "same_fact_duplicate_credit_count": max(
            same_fact_duplicate,
            _required_nonnegative_counter(
                impact_counts, "same_fact_duplicate_credit_count"
            ),
        ),
        "same_document_duplicate_credit_count": max(
            same_document_duplicate,
            _required_nonnegative_counter(
                impact_counts, "same_document_duplicate_credit_count"
            ),
        ),
        "claim_count_event_boost_count": event_stage_injection,
        "eligibility_contradiction_count": eligibility_contradictions,
        "critical_material_fact_miss_count": sum(
            int(row.get("gold_material_fact_miss_count") or 0)
            for row in adequacy
        ),
    }


def _v3_global_semantic_critical_counts(
    global_audits: Sequence[Mapping[str, Any]],
) -> Mapping[str, int]:
    by_id = {str(row.get("audit_id") or ""): row for row in global_audits}
    result = {}
    for output_name, (audit_id, source_name) in (
        V3_REQUIRED_CRITICAL_SOURCES.items()
    ):
        audit = by_id.get(audit_id)
        source_counts = (audit or {}).get("source_critical_counts") or {}
        result[output_name] = _required_nonnegative_counter(
            source_counts, source_name
        )
    return result


def _duplicate_credit_count(
    rows: Sequence[Mapping[str, Any]], *, fields: Sequence[str]
) -> int:
    keys = [tuple(str(row.get(field) or "") for field in fields) for row in rows]
    nonempty = [key for key in keys if all(key)]
    return len(nonempty) - len(set(nonempty))


def _required_nonnegative_counter(
    counts: Mapping[str, Any], name: str
) -> int:
    if name not in counts:
        return 1
    try:
        value = int(counts[name])
    except (TypeError, ValueError):
        return 1
    return value if value >= 0 else 1


def _readiness_adequate_absence(row: Mapping[str, Any] | None) -> bool:
    return bool(
        row
        and row.get("adequate_absence_allowed") is True
        and row.get("saturation_status") == "ADEQUATE_ABSENCE"
        and int(row.get("provider_failures") or 0) == 0
        and row.get("budget_exhausted") is not True
        and not row.get("missing_route_categories")
    )


def _evaluate_target(
    *,
    target: Mapping[str, Any],
    required_components: Sequence[str],
    claims: Sequence[Mapping[str, Any]],
    impacts: Sequence[Mapping[str, Any]],
    assessments: Sequence[Mapping[str, Any]],
    score: Mapping[str, Any],
    decision: Mapping[str, Any],
    trace: Mapping[str, Any],
    missing_leaves: Sequence[str],
) -> Mapping[str, Any]:
    evidence_partition = partition_scoring_evidence(claims)
    organic_claims = evidence_partition.organic_rows
    organic_claim_ids = {str(row.get("claim_id") or "") for row in organic_claims}
    probe_claims = tuple(
        row
        for row in claims
        if row.get("evidence_origin") == "CONTROLLED_CLAIM_PROBE"
    )
    valid_impacts = tuple(
        row
        for row in impacts
        if str(row.get("claim_id") or "") in organic_claim_ids
    )
    credited_impacts = tuple(
        row
        for row in valid_impacts
        if float(row.get("validated_credit_fraction") or 0.0) > 0.0
    )
    impact_ids = {str(row.get("impact_id") or "") for row in valid_impacts}
    assessment_ids = {str(row.get("assessment_id") or "") for row in assessments}
    assessment_components = {str(row.get("component_id") or "") for row in assessments}
    nonterminal = tuple(
        row
        for row in assessments
        if row.get("status") not in TERMINAL_FULL_SCORE_STATUSES
    )
    vector = dict(score.get("component_score_vector") or {})
    verified_points = float(score.get("verified_supported_score") or 0.0)
    full_score = score.get("full_e2r_score")
    decision_claim_ids = set(str(v) for v in decision.get("accepted_claim_ids") or ())
    decision_impact_ids = set(str(v) for v in decision.get("claim_impact_ids") or ())
    decision_assessment_ids = set(
        str(v) for v in decision.get("component_assessment_ids") or ()
    )
    score_type = str(score.get("score_type") or decision.get("score_type") or "") or None
    full_score_valid = score.get("full_score_valid") is True and decision.get("full_score_valid") is True
    trace_id = str(decision.get("trace_id") or "")
    trace_decision_id = str(trace.get("decision_id") or "")
    critical = {
        "required_dossier_leaf_missing_count": len(missing_leaves),
        "organic_accepted_claim_missing": int(not organic_claims),
        "organic_validated_impact_missing": int(not valid_impacts),
        "organic_verified_component_points_missing": int(verified_points <= 0),
        "calibrated_profile_missing": int(
            not score.get("profile_id") or not score.get("contract_hash")
        ),
        "calibrated_profile_mismatch": int(
            bool(target.get("expected_profile_id"))
            and score.get("profile_id") != target.get("expected_profile_id")
        ),
        "probe_claim_counted_organic_count": sum(
            str(row.get("claim_id") or "") in organic_claim_ids for row in probe_claims
        ),
        "no_score_only_decision": int(score_type in {None, "NO_SCORE"}),
        "component_coverage_mismatch": len(
            set(required_components) ^ assessment_components
        ),
        "component_vector_coverage_mismatch": len(
            set(required_components) ^ set(vector)
        ),
        "material_nonterminal_component_count": len(nonterminal),
        "full_score_invalid": int(not full_score_valid),
        "score_type_not_full_e2r_100": int(score_type != "FULL_E2R_100"),
        "component_sum_total_mismatch": int(
            full_score is None
            or abs(sum(float(v) for v in vector.values()) - float(full_score or 0.0))
            > 1e-6
        ),
        "component_sum_verified_mismatch": int(
            abs(sum(float(v) for v in vector.values()) - verified_points) > 1e-6
        ),
        "decision_claim_lineage_mismatch": len(organic_claim_ids ^ decision_claim_ids),
        "decision_impact_lineage_mismatch": len(impact_ids ^ decision_impact_ids),
        "decision_component_lineage_mismatch": len(
            assessment_ids ^ decision_assessment_ids
        ),
        "stagecourt_trace_missing": int(
            not trace_id
            or trace.get("trace_id") != trace_id
            or not trace_decision_id
            or trace_decision_id != str(decision.get("decision_id") or "")
        ),
        "forced_expected_stage_present": int(
            "expected_stage" in decision or "forced_stage" in decision
        ),
        "decision_target_mismatch": int(
            str(decision.get("target_id") or "")
            != str(target.get("target_id") or "")
        ),
        "decision_as_of_date_mismatch": int(
            str(decision.get("as_of_date") or "")
            != str(target.get("as_of_date") or "")
        ),
        "score_archetype_mismatch": int(
            str(score.get("archetype_id") or "")
            != str(target.get("archetype_id") or "")
        ),
        "future_organic_claim_count": sum(
            bool(row.get("published_date"))
            and str(row.get("published_date")) > str(target.get("as_of_date") or "")
            for row in organic_claims
        ),
    }
    return {
        "target_id": str(target.get("target_id") or ""),
        "company_name": str(target.get("company_name") or ""),
        "archetype_id": str(target.get("archetype_id") or ""),
        "status": "CANONICAL_FULL_THESIS_PASS" if sum(critical.values()) == 0 else "CANONICAL_FULL_THESIS_NOT_READY",
        "missing_leaves": tuple(missing_leaves),
        "counts": {
            "organic_accepted_claim_count": len(organic_claims),
            "organic_validated_impact_count": len(valid_impacts),
            "organic_credited_impact_count": len(credited_impacts),
            "organic_verified_component_points": round(verified_points, 6),
            "calibrated_profile_used_count": int(
                bool(score.get("profile_id") and score.get("contract_hash"))
            ),
            "probe_claim_counted_organic_count": critical[
                "probe_claim_counted_organic_count"
            ],
            "component_assessment_count": len(assessments),
        },
        "facts": {
            "profile_id": score.get("profile_id"),
            "contract_hash": score.get("contract_hash"),
            "verified_supported_score": verified_points,
            "full_e2r_score": full_score,
            "full_score_valid": full_score_valid,
            "score_type": score_type,
            "canonical_stage": decision.get("canonical_stage"),
            "decision_status": decision.get("decision_status"),
            "trace_id": trace_id or None,
        },
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def _read_global_audit(*, row: Mapping[str, Any], base_dir: Path) -> Mapping[str, Any]:
    path = _resolve_path(base_dir, str(row["path"]))
    accepted = set(str(value) for value in row.get("accepted_statuses") or ("PASS",))
    if not path.is_file():
        critical = {"audit_leaf_missing": 1, "audit_status_failed": 0, "audit_critical_nonzero": 0}
        status = None
        source_critical_counts: Mapping[str, Any] = {}
        source_schema_version = None
    else:
        payload = _read_json(path)
        status = str(payload.get("status") or "")
        raw_source_counts = payload.get("critical_counts")
        source_critical_counts = (
            dict(raw_source_counts)
            if isinstance(raw_source_counts, Mapping)
            else {}
        )
        source_schema_version = payload.get("schema_version")
        recomputed_source_critical = sum(
            _required_nonnegative_counter(source_critical_counts, name)
            for name in source_critical_counts
        )
        critical = {
            "audit_leaf_missing": 0,
            "audit_status_failed": int(status not in accepted),
            "audit_critical_nonzero": int(
                payload.get("critical_count_sum", 0) != 0
                or recomputed_source_critical != 0
            ),
        }
    return {
        "audit_id": str(row.get("audit_id") or path.stem),
        "path": str(path),
        "observed_status": status,
        "source_schema_version": source_schema_version,
        "source_critical_counts": source_critical_counts,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def _intermediate_labels(
    targets: Sequence[Mapping[str, Any]],
    *,
    global_audits: Sequence[Mapping[str, Any]],
    configured_targets: Sequence[Mapping[str, Any]],
) -> Mapping[str, bool]:
    target_by_id = {str(row["target_id"]): row for row in targets}
    all_claims = bool(targets) and all(row["counts"]["organic_accepted_claim_count"] > 0 for row in targets)
    all_scores = bool(targets) and all(
        row["counts"]["organic_verified_component_points"] > 0
        and row["facts"].get("full_score_valid") is True
        for row in targets
    )
    labels = {
        "LIVE_MATERIALIZATION_PASS": any(
            row["audit_id"] == "live_materialization"
            and row["critical_count_sum"] == 0
            for row in global_audits
        ),
        "ORGANIC_CLAIM_COMPILATION_PASS": all_claims,
        "RESEARCH_CALIBRATED_COMPONENT_SCORING_PASS": all_scores,
        "C06_CANONICAL_LIVE_CUTOVER_PASS": bool(targets)
        and all(row["status"] == "CANONICAL_FULL_THESIS_PASS" for row in targets),
    }
    for configured in configured_targets:
        label = str(configured.get("success_label") or "")
        if label:
            result = target_by_id.get(str(configured.get("target_id") or ""))
            labels[label] = bool(
                result and result["status"] == "CANONICAL_FULL_THESIS_PASS"
            )
    return labels


def _repository_verification() -> Mapping[str, Any]:
    status = subprocess.run(
        ("git", "status", "--porcelain", "--untracked-files=all"),
        text=True,
        capture_output=True,
        check=True,
    ).stdout.splitlines()
    head = subprocess.run(
        ("git", "rev-parse", "HEAD"), text=True, capture_output=True, check=True
    ).stdout.strip()
    origin = subprocess.run(
        ("git", "rev-parse", "origin/main"), text=True, capture_output=True, check=False
    )
    origin_sha = origin.stdout.strip() if origin.returncode == 0 else ""
    critical = {
        "repo_dirty": len(status),
        "origin_main_missing": int(not origin_sha),
        "head_not_pushed_to_origin_main": int(bool(origin_sha) and origin_sha != head),
    }
    return {
        "status": "CLEAN_PUSHED_SAME_COMMIT_PASS" if sum(critical.values()) == 0 else "CLEAN_PUSHED_SAME_COMMIT_FAIL",
        "repo_dirty": bool(status),
        "head_origin_same_commit": bool(origin_sha) and origin_sha == head,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def _object_rows(payload: Mapping[str, Any], key: str) -> tuple[Mapping[str, Any], ...]:
    value = payload.get(key)
    if not isinstance(value, list):
        return ()
    return tuple(row for row in value if isinstance(row, Mapping))


def _resolve_path(base_dir: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base_dir / path


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = [
    "NOT_READY",
    "READY",
    "MEANINGFUL_READY_V2",
    "RESEARCH_NOT_VERIFIED",
    "SEMANTIC_NOT_READY",
    "REQUIRED_DOSSIER_LEAVES",
    "SCORING_READINESS_SCHEMA_VERSION",
    "SCORING_READINESS_SCHEMA_VERSION_V2",
    "V3_REQUIRED_CRITICAL_SOURCES",
    "compile_meaningful_scoring_readiness",
    "write_meaningful_scoring_readiness",
]
