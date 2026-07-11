"""Leaf-backed readiness gate for meaningful E2R scoring."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from .component_assessment import TERMINAL_FULL_SCORE_STATUSES
from .evidence_origin import partition_scoring_evidence


SCORING_READINESS_SCHEMA_VERSION = "e2r_meaningful_scoring_readiness_v2"
READY = "MEANINGFUL_E2R_SCORING_READY"
NOT_READY = "MEANINGFUL_E2R_SCORING_NOT_READY"

REQUIRED_DOSSIER_LEAVES = (
    "accepted_current_claims.jsonl",
    "claim_impacts_validated.jsonl",
    "component_assessments.jsonl",
    "component_score_vector.json",
    "atomic_stage_decision.json",
    "stagecourt_trace.json",
)


def compile_meaningful_scoring_readiness(
    *, config_path: str | Path, verify_repository: bool = False
) -> Mapping[str, Any]:
    config_file = Path(config_path)
    config = _read_json(config_file)
    if config.get("schema_version") != SCORING_READINESS_SCHEMA_VERSION:
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
        "schema_version": SCORING_READINESS_SCHEMA_VERSION,
        "status": READY if critical == 0 else NOT_READY,
        "exact_final_verdict": READY if critical == 0 else NOT_READY,
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


def write_meaningful_scoring_readiness(
    verdict: Mapping[str, Any], *, output_path: str | Path
) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# E2R Meaningful Scoring Readiness Verdict",
        "",
        f"- final status: {verdict['status']}",
        f"- as_of_date: {verdict['as_of_date']}",
        f"- mandatory targets: {verdict['mandatory_target_count']}",
        f"- organic accepted claims: {verdict['counts']['organic_accepted_claim_count']}",
        f"- organic validated impacts: {verdict['counts']['organic_validated_impact_count']}",
        f"- organic verified component points: {verdict['counts']['organic_verified_component_points']}",
        f"- full score valid canaries: {verdict['counts']['full_score_valid_canary_count']}",
        f"- critical_count_sum: {verdict['critical_count_sum']}",
        f"- blockers: {verdict['blockers']}",
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
        and float(row.get("validated_credit_fraction") or 0.0) > 0.0
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
    else:
        payload = _read_json(path)
        status = str(payload.get("status") or "")
        critical = {
            "audit_leaf_missing": 0,
            "audit_status_failed": int(status not in accepted),
            "audit_critical_nonzero": int(payload.get("critical_count_sum", 0) != 0),
        }
    return {
        "audit_id": str(row.get("audit_id") or path.stem),
        "path": str(path),
        "observed_status": status,
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
    "REQUIRED_DOSSIER_LEAVES",
    "SCORING_READINESS_SCHEMA_VERSION",
    "compile_meaningful_scoring_readiness",
    "write_meaningful_scoring_readiness",
]
