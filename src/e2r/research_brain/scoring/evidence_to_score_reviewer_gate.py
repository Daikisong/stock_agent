"""Reviewer A~G가 담당 leaf를 따로 읽는 evidence-to-score 최종 감사."""

from __future__ import annotations

import ast
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import (
    audit_scoring_contract_catalog,
    load_scoring_contract_catalog,
)

from .component_assessment import TERMINAL_FULL_SCORE_STATUSES
from .generalization_canaries import compile_evidence_to_score_generalization_audit


SCHEMA_VERSION = "e2r_evidence_to_score_reviewer_gate_v1"
PASS_STATUS = "EVIDENCE_TO_SCORE_REVIEWER_GATE_PASS"
FAIL_STATUS = "EVIDENCE_TO_SCORE_REVIEWER_GATE_FAIL"
TARGETS = ("005930", "000660")
STAGES = {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}
REQUIRED_COMPONENTS = {
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
}
REQUIRED_C06_QUESTIONS = {
    "current_customer_allocation_commitment",
    "capacity_constraint_presold_status",
    "qualification_pass_lag_reopen",
    "shipment_mass_production_generation",
    "hbm_ai_memory_revenue_mix",
    "asp_pricing_actual",
    "revenue_operating_profit_conversion",
    "margin_fcf_conversion",
    "medium_term_revision_consensus",
    "conventional_memory_drag",
    "capex_supply_oversupply",
    "customer_concentration_dependency",
}


def compile_evidence_to_score_reviewer_gate(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    builders: tuple[tuple[str, Callable[[Path], Mapping[str, Any]]], ...] = (
        ("A", _reviewer_a),
        ("B", _reviewer_b),
        ("C", _reviewer_c),
        ("D", _reviewer_d),
        ("E", _reviewer_e),
        ("F", _reviewer_f),
        ("G", _reviewer_g),
    )
    reviewers = {reviewer_id: builder(root) for reviewer_id, builder in builders}
    critical = {
        f"reviewer_{reviewer_id.lower()}_critical_count": int(row["critical_count_sum"])
        for reviewer_id, row in reviewers.items()
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": SCHEMA_VERSION,
        "status": PASS_STATUS if critical_sum == 0 else FAIL_STATUS,
        "reviewer_count": len(reviewers),
        "reviewers": reviewers,
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _reviewer_a(root: Path) -> Mapping[str, Any]:
    catalog = load_scoring_contract_catalog()
    contract_audit = audit_scoring_contract_catalog(catalog)
    c06 = catalog.get("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
    source = root / "src/e2r/research_brain/runtime/live_materialization/current_atomic_decision.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    lockout_path = root / "docs/operational/e2r_legacy_scoring_lockout_audit.json"
    lockout = _json(lockout_path)
    critical = {
        "canonical_contract_failure": int(contract_audit["critical_count_sum"] != 0),
        "c06_profile_missing": int(c06 is None),
        "c06_weight_total_mismatch": int(c06 is None or sum(c06.component_weights.values()) != 100.0),
        "balanced_points_function_present": int("_balanced_points" in functions),
        "controlled_probe_is_not_isolated": int("_controlled_probe_points_test_only" not in functions),
        "legacy_lockout_leaf_failure": int(lockout.get("critical_count_sum") != 0),
    }
    return _review("A", "Scoring Contract", critical, root, (source, lockout_path), {
        "contract_count": len(catalog.contracts),
        "c06_component_weights": dict(c06.component_weights) if c06 else {},
        "balanced_points_function_present": "_balanced_points" in functions,
    })


def _reviewer_b(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    mapping_loss = duplicate_credit = empty_unsupported = 0
    multi_impact_claims = rerouted_retained = rerouted_closed_original = 0
    for target in TARGETS:
        dossier = _dossier(root, target)
        provenance_path = dossier / "claim_provenance.jsonl"
        impacts_path = dossier / "claim_impacts_validated.jsonl"
        ledger_path = dossier / "claim_impact_ledger.jsonl"
        leafs.extend((provenance_path, impacts_path, ledger_path))
        provenance = {row["claim_id"]: row for row in _jsonl(provenance_path)}
        impacts = _jsonl(impacts_path)
        ledger = _jsonl(ledger_path)
        by_claim = Counter(row["claim_id"] for row in impacts)
        multi_impact_claims += sum(count > 1 for count in by_claim.values())
        mapping_loss += sum(
            row["claim_id"] not in provenance
            or row["mapping_id"] not in provenance[row["claim_id"]].get("mapping_ids", [])
            or any(mid not in provenance[row["claim_id"]].get("mapping_ids", []) for mid in row.get("lineage_mapping_ids", []))
            for row in impacts
        )
        keys = [
            (row["claim_id"], row["primitive_id"], row["component_id"], row["direction"], row["evidence_family_id"])
            for row in impacts
        ]
        duplicate_credit += len(keys) - len(set(keys))
        empty_unsupported += sum(not row.get("unsupported_aspects") for row in ledger)
        rerouted = [row for row in ledger if row.get("lineage_mapping_ids")]
        rerouted_retained += len(rerouted)
        rerouted_closed_original += sum(bool(row.get("original_source_task_gap_closed")) for row in rerouted)
    critical = {
        "many_to_many_claim_missing": int(multi_impact_claims == 0),
        "mapping_lineage_loss_count": mapping_loss,
        "duplicate_economic_credit_count": duplicate_credit,
        "unsupported_aspect_missing_count": empty_unsupported,
        "rerouted_valid_impact_missing": int(rerouted_retained == 0),
        "rerouted_original_gap_closed_count": rerouted_closed_original,
    }
    return _review("B", "Claim Impact Semantics", critical, root, leafs, {
        "multi_impact_claim_count": multi_impact_claims,
        "rerouted_retained_impact_count": rerouted_retained,
    })


def _reviewer_c(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    missing = nonterminal = vector_mismatch = support_loss = absent_without_proof = 0
    status_counts: Counter[str] = Counter()
    for target in TARGETS:
        dossier = _dossier(root, target)
        assessments_path = dossier / "component_assessments.jsonl"
        score_path = dossier / "component_score_vector.json"
        leafs.extend((assessments_path, score_path))
        assessments = _jsonl(assessments_path)
        score = _json(score_path)
        by_component = {row["component_id"]: row for row in assessments}
        missing += len(REQUIRED_COMPONENTS ^ set(by_component))
        nonterminal += sum(row.get("status") not in TERMINAL_FULL_SCORE_STATUSES for row in assessments)
        status_counts.update(str(row.get("status")) for row in assessments)
        vector = score.get("component_score_vector", {})
        vector_mismatch += len(REQUIRED_COMPONENTS ^ set(vector))
        for component, assessment in by_component.items():
            if abs(float(assessment.get("verified_points") or 0.0) - float(vector.get(component) or 0.0)) > 1e-6:
                support_loss += 1
            if assessment.get("status") == "VERIFIED_ABSENT_AFTER_SEARCH" and not assessment.get("search_exhaustion_proof"):
                absent_without_proof += 1
    critical = {
        "component_roster_mismatch_count": missing,
        "nonterminal_component_count": nonterminal,
        "component_vector_roster_mismatch_count": vector_mismatch,
        "supported_score_loss_count": support_loss,
        "evaluated_absent_without_search_proof_count": absent_without_proof,
    }
    return _review("C", "Component State", critical, root, leafs, {
        "status_counts": dict(sorted(status_counts.items())),
        "required_component_count_per_target": len(REQUIRED_COMPONENTS),
    })


def _reviewer_d(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    counts: Counter[str] = Counter()
    for target in TARGETS:
        dossier = _dossier(root, target)
        claim_path = dossier / "accepted_current_claims.jsonl"
        provenance_path = dossier / "claim_provenance.jsonl"
        document_path = dossier / "evidence_documents.jsonl"
        anchor_path = dossier / "evidence_anchors.jsonl"
        leafs.extend((claim_path, provenance_path, document_path, anchor_path))
        claims = _jsonl(claim_path)
        provenance = _jsonl(provenance_path)
        documents = {row["document_id"]: row for row in _jsonl(document_path)}
        anchors = {row["anchor_id"]: row for row in _jsonl(anchor_path)}
        counts["organic_claim_count"] += len(claims)
        counts["claim_provenance_roster_mismatch"] += len({row["claim_id"] for row in claims} ^ {row["claim_id"] for row in provenance})
        for row in provenance:
            text = str(row.get("document_text") or "")
            counts["probe_or_fixture_count"] += int(row.get("test_only") is True or row.get("source_proxy_only") is True)
            counts["not_fetched_count"] += int(row.get("fetched") is not True)
            counts["target_mismatch_count"] += int(str(row.get("target_id")) != target)
            counts["future_source_count"] += int(str(row.get("published_date") or "9999-99-99") > "2026-07-11")
            counts["url_missing_count"] += int(not str(row.get("source_url") or "").startswith("http"))
            counts["exact_quote_missing_count"] += int(not row.get("exact_quote") or row["exact_quote"] not in text)
            counts["content_hash_mismatch_count"] += int(hashlib.sha256(text.encode()).hexdigest() != row.get("content_sha256"))
            counts["document_lineage_missing_count"] += int(row.get("document_id") not in documents)
            counts["anchor_lineage_missing_count"] += sum(anchor_id not in anchors for anchor_id in row.get("anchor_ids", []))
    critical = {key: value for key, value in counts.items() if key != "organic_claim_count"}
    critical["organic_claim_zero_target_count"] = sum(
        not _jsonl(_dossier(root, target) / "accepted_current_claims.jsonl") for target in TARGETS
    )
    return _review("D", "Organic Source & Provenance", critical, root, leafs, {
        "organic_claim_count": counts["organic_claim_count"],
        "as_of_date": "2026-07-11",
    })


def _reviewer_e(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    critical: Counter[str] = Counter()
    target_facts: dict[str, Any] = {}
    for target in TARGETS:
        dossier = _dossier(root, target)
        score_path = dossier / "component_score_vector.json"
        decision_path = dossier / "atomic_stage_decision.json"
        trace_path = dossier / "stagecourt_trace.json"
        assessment_path = dossier / "component_assessments.jsonl"
        impact_path = dossier / "claim_impacts_validated.jsonl"
        leafs.extend((score_path, decision_path, trace_path, assessment_path, impact_path))
        score, decision, trace = _json(score_path), _json(decision_path), _json(trace_path)
        assessments, impacts = _jsonl(assessment_path), _jsonl(impact_path)
        vector_sum = round(sum(float(value) for value in score.get("component_score_vector", {}).values()), 6)
        critical["full_score_invalid_count"] += int(score.get("full_score_valid") is not True or score.get("score_type") != "FULL_E2R_100")
        critical["component_sum_mismatch_count"] += int(abs(vector_sum - float(score.get("full_e2r_score") or -1)) > 1e-6)
        critical["decision_score_mismatch_count"] += int(abs(float(decision.get("full_e2r_score") or -1) - float(score.get("full_e2r_score") or -2)) > 1e-6)
        critical["invalid_canonical_stage_count"] += int(decision.get("canonical_stage") not in STAGES)
        critical["nonfinal_decision_count"] += int(decision.get("decision_status") != "FINAL")
        critical["decision_trace_identity_mismatch_count"] += int(any(decision.get(key) != trace.get(key) for key in ("decision_id", "trace_id", "target_id", "as_of_date")))
        critical["claim_trace_mismatch_count"] += len(set(decision.get("accepted_claim_ids", [])) ^ set(trace.get("accepted_claim_ids", [])))
        impact_ids = {row["impact_id"] for row in impacts}
        critical["impact_trace_mismatch_count"] += len(impact_ids ^ set(decision.get("claim_impact_ids", []))) + len(impact_ids ^ set(trace.get("claim_impact_ids", [])))
        assessment_ids = {row["assessment_id"] for row in assessments}
        critical["component_trace_mismatch_count"] += len(assessment_ids ^ set(decision.get("component_assessment_ids", []))) + len(assessment_ids ^ set(trace.get("component_assessment_ids", [])))
        target_facts[target] = {"score": score.get("full_e2r_score"), "stage": decision.get("canonical_stage"), "score_type": score.get("score_type")}
    return _review("E", "Score & Stage", dict(critical), root, leafs, {"targets": target_facts})


def _reviewer_f(root: Path) -> Mapping[str, Any]:
    replay_path = root / "docs/operational/e2r_c06_historical_component_replay.json"
    replay = _json(replay_path)
    leafs: list[Path] = [replay_path]
    missing_questions = nonterminal_questions = 0
    counter_impact_count = 0
    for target in TARGETS:
        dossier = _dossier(root, target)
        question_path = dossier / "question_closure.jsonl"
        impact_path = dossier / "claim_impacts_validated.jsonl"
        leafs.extend((question_path, impact_path))
        questions = _jsonl(question_path)
        missing_questions += len(REQUIRED_C06_QUESTIONS ^ {row["question_family_id"] for row in questions})
        nonterminal_questions += sum(row.get("status") not in {"SUPPORTED", "PARTIALLY_SUPPORTED", "EVALUATED_ABSENT", "COUNTER_EVIDENCE"} for row in questions)
        counter_impact_count += sum(row.get("direction") == "COUNTER" for row in _jsonl(impact_path))
    replay_cases = {row["case_id"]: row for row in replay.get("cases", [])}
    required_replay = {
        "C06-SKHYNIX-20240502-SOLDOUT",
        "C06-SKHYNIX-20250123-REVENUE-MIX",
        "C06-SAMSUNG-20240524-QUALIFICATION-LAG",
        "C06-SAMSUNG-20250131-REOPEN-CAP",
        "C06-SKHYNIX-PRODUCT-SPEC-GUARD",
        "C06-SAMSUNG-PACKAGE-PROFILE-GUARD",
    }
    critical = {
        "c06_question_family_roster_mismatch_count": missing_questions,
        "c06_question_nonterminal_count": nonterminal_questions,
        "counter_thesis_impact_missing": int(counter_impact_count == 0),
        "historical_replay_failure": int(replay.get("critical_count_sum") != 0),
        "historical_replay_case_roster_mismatch": len(required_replay ^ set(replay_cases)),
        "qualification_lag_hard_break_count": int(bool(replay_cases.get("C06-SAMSUNG-20240524-QUALIFICATION-LAG", {}).get("hard_break_emitted"))),
        "semantic_forbidden_component_count": sum(int(row.get("forbidden_component_count") or 0) for row in replay_cases.values()),
    }
    return _review("F", "Samsung/Hynix C06 Semantics", critical, root, leafs, {
        "question_family_count_per_target": len(REQUIRED_C06_QUESTIONS),
        "counter_impact_count": counter_impact_count,
        "historical_case_count": len(replay_cases),
    })


def _reviewer_g(root: Path) -> Mapping[str, Any]:
    artifact_path = root / "docs/operational/e2r_evidence_to_score_generalization_audit.json"
    fresh = compile_evidence_to_score_generalization_audit()
    artifact = _json(artifact_path)
    required = {
        "c08_direct_customer_order_positive",
        "c08_product_profile_only_guard",
        "c15_issuer_pass_through_positive",
        "c15_raw_commodity_headline_guard",
        "wrong_subject_accounting_guard",
        "old_risk_resolved_guard",
    }
    critical = {
        "fresh_generalization_failure": int(fresh.get("critical_count_sum") != 0),
        "committed_generalization_leaf_mismatch": int(fresh != artifact),
        # 필수 canary가 모두 포함됐는지를 본다. Phase가 확장되어 새 canary가
        # 추가되는 것은 실패가 아니며, 필수 canary 누락만 실패다.
        "generalization_case_roster_mismatch": len(
            required - set(fresh.get("cases", {}))
        ),
        "source_proxy_score_count": int(fresh.get("source_proxy_score_count") or 0),
        "future_outcome_leakage_count": int(fresh.get("future_outcome_leakage_count") or 0),
        "target_specific_branch_count": int(fresh.get("target_specific_branch_count") or 0),
    }
    return _review("G", "Generalization", critical, root, (artifact_path,), {
        "case_count": len(fresh.get("cases", {})),
        "fresh_status": fresh.get("status"),
    })


def _review(
    reviewer_id: str,
    scope: str,
    critical_counts: Mapping[str, int],
    root: Path,
    leaf_paths: Sequence[Path],
    observations: Mapping[str, Any],
) -> Mapping[str, Any]:
    normalized = {key: int(value) for key, value in critical_counts.items()}
    critical_sum = sum(normalized.values())
    unique_paths = tuple(dict.fromkeys(Path(path) for path in leaf_paths))
    return {
        "reviewer_id": reviewer_id,
        "scope": scope,
        "status": f"REVIEWER_{reviewer_id}_{'PASS' if critical_sum == 0 else 'FAIL'}",
        "leaf_paths": [str(path.relative_to(root)) for path in unique_paths],
        "leaf_sha256": {str(path.relative_to(root)): _file_sha256(path) for path in unique_paths},
        "observations": dict(observations),
        "critical_counts": normalized,
        "critical_count_sum": critical_sum,
    }


def _dossier(root: Path, target: str) -> Path:
    return root / "output/evidence_to_score/c06/2026-07-11" / target


def _json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[Mapping[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


__all__ = [
    "FAIL_STATUS",
    "PASS_STATUS",
    "SCHEMA_VERSION",
    "compile_evidence_to_score_reviewer_gate",
]
