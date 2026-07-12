"""Phase 79 independent Reviewer A~H leaf-level semantic scoring gate."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import (
    load_scoring_contract_catalog,
)


SCHEMA_VERSION = "e2r_semantic_scoring_reviewer_gate_v1"
PASS_STATUS = "SEMANTIC_SCORING_REVIEWER_GATE_PASS"
FAIL_STATUS = "SEMANTIC_SCORING_REVIEWER_GATE_FAIL"
TARGETS = ("005930", "000660")
CANONICAL_STAGES = {
    "0",
    "1",
    "2",
    "3-Green",
    "3-Yellow",
    "3-Red",
    "4A",
    "4B",
    "4C",
    "5",
}
COMPONENTS = {
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
}
REVIEWER_SCOPES = {
    "A": "Scoring Schema Totality",
    "B": "Mechanism Scope & Eligibility",
    "C": "Research Acquisition",
    "D": "Claim Impact Semantics",
    "E": "Question/Component Reconciliation",
    "F": "Score & Stage",
    "G": "Samsung/Hynix C06",
    "H": "Generalization",
}


def compile_semantic_scoring_reviewer_gate(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    builders: tuple[
        tuple[str, Callable[[Path], Mapping[str, Any]]], ...
    ] = (
        ("A", _reviewer_a),
        ("B", _reviewer_b),
        ("C", _reviewer_c),
        ("D", _reviewer_d),
        ("E", _reviewer_e),
        ("F", _reviewer_f),
        ("G", _reviewer_g),
        ("H", _reviewer_h),
    )
    reviewers = {reviewer_id: builder(root) for reviewer_id, builder in builders}
    return evaluate_semantic_scoring_reviewer_gate(reviewers)


def evaluate_semantic_scoring_reviewer_gate(
    reviewers: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    recomputed_reviewers = {}
    for reviewer_id, row in reviewers.items():
        critical_counts = {
            str(key): int(value)
            for key, value in (row.get("critical_counts") or {}).items()
        }
        critical_sum = sum(critical_counts.values())
        recomputed_reviewers[reviewer_id] = {
            **dict(row),
            "status": (
                f"REVIEWER_{reviewer_id}_PASS"
                if critical_sum == 0
                else f"REVIEWER_{reviewer_id}_FAIL"
            ),
            "critical_counts": critical_counts,
            "critical_count_sum": critical_sum,
        }
    namespaces = [
        str(row.get("counter_namespace") or "")
        for row in recomputed_reviewers.values()
    ]
    critical = {
        "reviewer_roster_mismatch_count": len(
            set(REVIEWER_SCOPES) ^ set(recomputed_reviewers)
        ),
        "duplicate_counter_namespace_count": len(namespaces)
        - len(set(namespaces)),
        "reviewer_without_direct_leaf_count": sum(
            not row.get("direct_leaf_paths")
            or row.get("direct_leaf_reread") is not True
            for row in recomputed_reviewers.values()
        ),
        "report_generator_counter_reuse_count": sum(
            bool(row.get("report_generator_counter_ids"))
            for row in recomputed_reviewers.values()
        ),
        **{
            f"reviewer_{reviewer_id.lower()}_critical_count": int(
                row["critical_count_sum"]
            )
            for reviewer_id, row in recomputed_reviewers.items()
        },
    }
    total = sum(critical.values())
    return {
        "schema_version": SCHEMA_VERSION,
        "status": PASS_STATUS if total == 0 else FAIL_STATUS,
        "reviewer_count": len(recomputed_reviewers),
        "reviewers": recomputed_reviewers,
        "counter_independence": {
            "counter_namespaces": namespaces,
            "unique_counter_namespace_count": len(set(namespaces)),
            "shared_report_generator_counter_count": critical[
                "report_generator_counter_reuse_count"
            ],
            "rule": "Each reviewer rereads detailed leaves and computes a private counter namespace.",
        },
        "critical_counts": critical,
        "critical_count_sum": total,
    }


def _reviewer_a(root: Path) -> Mapping[str, Any]:
    policy_path = root / "configs/e2r_scoring_policy_v2.json"
    weight_path = root / "configs/e2r_archetype_weight_profile_v2_2.json"
    evidence_path = root / "configs/e2r_archetype_evidence_contracts_v12.json"
    edge_path = root / "configs/e2r_archetype_scoring_contract_edges_v1.json"
    stage_path = root / "configs/e2r_scoring_profile_v2_2.yaml"
    policy = _json(policy_path)
    enums = policy.get("enum_registry") or {}
    policy_pairs = {
        "strength_bands": "strength_bands",
        "completeness_bands": "completeness_bands",
        "causal_distances": "causal_distance_caps",
        "source_families": "source_family_caps",
        "temporal_scopes": "temporal_scope_caps",
        "directions": "direction_policy_fields",
        "support_types": "support_type_policies",
    }
    enum_policy_mismatch = sum(
        len(set(enums.get(enum_name) or ()) ^ set(policy.get(policy_name) or {}))
        for enum_name, policy_name in policy_pairs.items()
    )
    support_policies = policy.get("support_type_policies") or {}
    required_support_fields = {
        "support_credit_cap",
        "counter_effect_cap",
        "resolution_effect",
        "counter_effect_mode",
        "research_case_refs",
        "rationale",
        "replay_result",
    }
    support_field_missing = sum(
        len(required_support_fields - set(row))
        for row in support_policies.values()
    )
    catalog = load_scoring_contract_catalog(
        weight_profile_path=weight_path,
        evidence_contract_path=evidence_path,
        edge_catalog_path=edge_path,
        stage_config_path=stage_path,
    )
    component_roster_mismatch = 0
    weight_total_mismatch = 0
    cap_roster_mismatch = 0
    source_cap_mismatch = 0
    temporal_cap_mismatch = 0
    missing_edge_contract = 0
    for contract in catalog.contracts.values():
        component_roster_mismatch += len(
            COMPONENTS ^ set(contract.component_weights)
        )
        weight_total_mismatch += int(
            abs(sum(contract.component_weights.values()) - 100.0) > 1e-9
        )
        cap_roster_mismatch += len(
            set(contract.component_weights) ^ set(contract.component_caps)
        )
        source_cap_mismatch += len(
            set(enums.get("source_families") or ())
            ^ set(contract.source_tier_caps)
        )
        temporal_cap_mismatch += len(
            set(enums.get("temporal_scopes") or ())
            ^ set(contract.freshness_caps)
        )
        missing_edge_contract += int(
            contract.edge_catalog_status not in {"EXPLICIT", "EXPLICIT_PENDING"}
        )
    critical = {
        "schema_enum_policy_roster_mismatch_count": enum_policy_mismatch,
        "schema_support_policy_field_missing_count": support_field_missing,
        "schema_archetype_count_mismatch": abs(len(catalog.contracts) - 36),
        "schema_component_roster_mismatch_count": component_roster_mismatch,
        "schema_weight_total_mismatch_count": weight_total_mismatch,
        "schema_component_cap_roster_mismatch_count": cap_roster_mismatch,
        "schema_source_cap_roster_mismatch_count": source_cap_mismatch,
        "schema_temporal_cap_roster_mismatch_count": temporal_cap_mismatch,
        "schema_missing_explicit_edge_contract_count": missing_edge_contract,
        "schema_partial_bridge_silent_zero_count": int(
            float(
                (support_policies.get("PARTIAL_BRIDGE") or {}).get(
                    "support_credit_cap", 0
                )
            )
            <= 0
        ),
        "schema_risk_open_counter_silent_zero_count": int(
            float(
                (support_policies.get("RISK_OPEN") or {}).get(
                    "counter_effect_cap", 0
                )
            )
            <= 0
        ),
        "schema_risk_resolved_release_silent_zero_count": int(
            float(
                (support_policies.get("RISK_RESOLVED") or {}).get(
                    "resolution_effect", 0
                )
            )
            <= 0
        ),
    }
    return _review(
        root,
        "A",
        critical,
        (policy_path, weight_path, evidence_path, edge_path, stage_path),
        {
            "archetype_count": len(catalog.contracts),
            "support_type_count": len(support_policies),
            "component_count": len(COMPONENTS),
            "enum_policy_pairs_checked": len(policy_pairs),
        },
    )


def _reviewer_b(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    critical: Counter[str] = Counter()
    observations: dict[str, Any] = {}
    for target in TARGETS:
        dossier = _dossier(root, target)
        claim_path = dossier / "accepted_current_claims.jsonl"
        decision_path = dossier / "claim_eligibility_decisions.jsonl"
        impact_path = dossier / "claim_impacts_validated.jsonl"
        leafs.extend((claim_path, decision_path, impact_path))
        claims = _jsonl(claim_path)
        decisions = _jsonl(decision_path)
        impacts = _jsonl(impact_path)
        claim_ids = {str(row.get("claim_id") or "") for row in claims}
        decision_claim_ids = {
            str(row.get("claim_id") or "") for row in decisions
        }
        decision_ids = [
            str(row.get("eligibility_decision_id") or "") for row in decisions
        ]
        decisions_by_id = {
            str(row.get("eligibility_decision_id") or ""): row
            for row in decisions
        }
        critical["mechanism_eligibility_claim_roster_mismatch_count"] += len(
            claim_ids ^ decision_claim_ids
        )
        critical["mechanism_duplicate_eligibility_decision_id_count"] += len(
            decision_ids
        ) - len(set(decision_ids))
        critical["mechanism_implicit_stage_event_eligibility_count"] += sum(
            row.get("stage_event_eligibility") is True for row in decisions
        )
        critical["mechanism_ledger_acceptance_contradiction_count"] += sum(
            row.get("ledger_acceptance") is not True for row in decisions
        )
        for impact in impacts:
            decision = decisions_by_id.get(
                str(impact.get("eligibility_decision_id") or "")
            )
            critical["mechanism_score_without_eligibility_count"] += int(
                decision is None
            )
            critical["mechanism_ineligible_impact_credited_count"] += int(
                decision is not None
                and decision.get("component_scoring_eligibility") is not True
            )
            validation = impact.get("scope_validation") or {}
            scope = validation.get("scope") or {}
            critical["mechanism_scope_match_failure_count"] += int(
                validation.get("scope_match") is not True
            )
            critical["mechanism_scope_field_missing_count"] += sum(
                not str(scope.get(field) or "")
                for field in (
                    "issuer_id",
                    "business_segment",
                    "product_family",
                    "economic_mechanism",
                )
            )
            critical["mechanism_scope_target_mismatch_count"] += int(
                str(scope.get("issuer_id") or "") != target
            )
            scope_text = " ".join(str(value) for value in scope.values()).casefold()
            critical["mechanism_foundry_credit_in_c06_count"] += int(
                ("foundry" in scope_text or "logic_foundry" in scope_text)
                and float(impact.get("validated_credit_fraction") or 0) > 0
            )
            critical["mechanism_adjacent_substrate_economic_credit_count"] += int(
                impact.get("primitive_id") == "package_substrate_sympathy"
                and (
                    impact.get("component_id") != "information_confidence"
                    or float(impact.get("validated_credit_fraction") or 0) > 0
                )
            )
        observations[target] = {
            "claim_count": len(claims),
            "eligibility_decision_count": len(decisions),
            "validated_impact_count": len(impacts),
            "wrong_mechanism_decision_count": sum(
                row.get("eligibility_status")
                == "INELIGIBLE_WRONG_MECHANISM"
                for row in decisions
            ),
        }
    return _review(root, "B", dict(critical), leafs, observations)


def _reviewer_c(root: Path) -> Mapping[str, Any]:
    blind = root / "output/evidence_to_score_v2/blind_2026-07-11"
    gold_path = blind / "gold/gold_material_facts.jsonl"
    source_map_path = blind / "gold/gold_source_map.jsonl"
    input_path = blind / "production/production_input_manifest.jsonl"
    lane_path = blind / "production/production_lane_manifest.json"
    production_fact_path = blind / "production/production_material_facts.jsonl"
    leafs: list[Path] = [
        gold_path,
        source_map_path,
        input_path,
        lane_path,
        production_fact_path,
    ]
    gold = _jsonl(gold_path)
    source_map = _jsonl(source_map_path)
    production_inputs = _jsonl(input_path)
    production_facts = _jsonl(production_fact_path)
    comparisons = []
    adequacy_rows = []
    evidence_documents = []
    for target in TARGETS:
        dossier = _dossier(root, target)
        comparison_path = dossier / "material_fact_comparison.jsonl"
        adequacy_path = dossier / "evidence_search_adequacy.jsonl"
        document_path = dossier / "evidence_documents.jsonl"
        task_path = dossier / "question_source_tasks.jsonl"
        leafs.extend(
            (comparison_path, adequacy_path, document_path, task_path)
        )
        comparisons.extend(_jsonl(comparison_path))
        adequacy_rows.extend(_jsonl(adequacy_path))
        evidence_documents.extend(_jsonl(document_path))
    comparison_by_gold = {
        str(row.get("gold_fact_id") or ""): row for row in comparisons
    }
    gold_ids = {str(row.get("fact_id") or "") for row in gold}
    qualified = lambda row: all(  # noqa: E731
        row.get(key) is True
        for key in (
            "semantic_match",
            "mechanism_scope_match",
            "currentness_match",
            "source_quality_match",
        )
    )
    critical_gold = [row for row in gold if row.get("materiality") == "CRITICAL"]
    noncritical_gold = [
        row for row in gold if row.get("materiality") != "CRITICAL"
    ]
    critical_miss = sum(
        not qualified(comparison_by_gold.get(str(row.get("fact_id")), {}))
        for row in critical_gold
    )
    noncritical_match = sum(
        qualified(comparison_by_gold.get(str(row.get("fact_id")), {}))
        for row in noncritical_gold
    )
    noncritical_recall = (
        noncritical_match / len(noncritical_gold) if noncritical_gold else 1.0
    )
    required_routes = {
        "official_filing",
        "issuer_ir_earnings",
        "issuer_newsroom",
        "customer_official",
        "trusted_independent",
        "financial_revision",
        "counter_supersession",
    }
    observed_routes = {
        str(row.get("research_route") or "") for row in source_map
    }
    counter_gold_ids = {
        str(row.get("fact_id") or "")
        for row in gold
        if row.get("fact_role") == "COUNTER"
    }
    critical = {
        "acquisition_gold_roster_mismatch_count": len(
            gold_ids ^ set(comparison_by_gold)
        ),
        "acquisition_critical_gold_miss_count": critical_miss,
        "acquisition_noncritical_recall_below_90_count": int(
            noncritical_recall < 0.9
        ),
        "acquisition_source_route_roster_mismatch_count": len(
            required_routes ^ observed_routes
        ),
        "acquisition_unavailable_route_reason_missing_count": sum(
            row.get("availability_status") == "UNAVAILABLE"
            and not row.get("unavailable_reason")
            for row in source_map
        ),
        "acquisition_counter_fact_missing_or_unmatched_count": sum(
            not qualified(comparison_by_gold.get(gold_id, {}))
            for gold_id in counter_gold_ids
        )
        + int(not counter_gold_ids),
        "acquisition_supersession_route_missing_count": int(
            "counter_supersession" not in observed_routes
        ),
        "acquisition_required_counter_route_not_attempted_count": sum(
            row.get("saturation_status") == "ADEQUATE_ABSENCE"
            and "COUNTER" in set(row.get("required_route_categories") or ())
            and row.get("counter_route_attempted") is not True
            and "COUNTER"
            not in set(row.get("unavailable_route_categories") or ())
            for row in adequacy_rows
        ),
        "acquisition_required_supersession_route_not_attempted_count": sum(
            row.get("saturation_status") == "ADEQUATE_ABSENCE"
            and "SUPERSESSION"
            in set(row.get("required_route_categories") or ())
            and row.get("supersession_route_attempted") is not True
            and "SUPERSESSION"
            not in set(row.get("unavailable_route_categories") or ())
            for row in adequacy_rows
        ),
        "acquisition_inadequate_absence_count": sum(
            row.get("saturation_status") == "ADEQUATE_ABSENCE"
            and bool(
                row.get("provider_failures")
                or row.get("budget_exhausted") is True
                or row.get("missing_route_categories")
                or row.get("adequate_absence_allowed") is not True
            )
            for row in adequacy_rows
        ),
        "acquisition_gold_input_class_leak_count": sum(
            str(row.get("origin") or "").startswith("GOLD")
            or str(row.get("input_type") or "").startswith("GOLD")
            for row in production_inputs
        ),
        "acquisition_production_fact_zero_count": int(not production_facts),
        "acquisition_full_document_zero_count": int(not evidence_documents),
    }
    return _review(
        root,
        "C",
        critical,
        leafs,
        {
            "gold_fact_count": len(gold),
            "critical_gold_fact_count": len(critical_gold),
            "critical_gold_match_count": len(critical_gold) - critical_miss,
            "noncritical_recall": noncritical_recall,
            "source_routes": sorted(observed_routes),
            "production_fact_count": len(production_facts),
            "evidence_document_count": len(evidence_documents),
            "adequacy_question_count": len(adequacy_rows),
        },
    )


def _reviewer_d(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    critical: Counter[str] = Counter()
    observations: dict[str, Any] = {}
    total_support = total_counter = total_multi_claim = 0
    for target in TARGETS:
        dossier = _dossier(root, target)
        impact_path = dossier / "claim_impacts_validated.jsonl"
        fact_path = dossier / "economic_fact_clusters.jsonl"
        document_path = dossier / "document_clusters.jsonl"
        leafs.extend((impact_path, fact_path, document_path))
        impacts = _jsonl(impact_path)
        facts = _jsonl(fact_path)
        documents = _jsonl(document_path)
        impacts_by_id = {
            str(row.get("impact_id") or ""): row for row in impacts
        }
        facts_by_id = {
            str(row.get("fact_cluster_id") or ""): row for row in facts
        }
        documents_by_id = {
            str(row.get("document_cluster_id") or ""): row
            for row in documents
        }
        by_claim = Counter(str(row.get("claim_id") or "") for row in impacts)
        multi_claim = sum(count > 1 for count in by_claim.values())
        total_multi_claim += multi_claim
        support_count = sum(
            row.get("direction") in {"SUPPORT", "NEUTRAL"}
            and float(row.get("support_credit_fraction") or 0) > 0
            for row in impacts
        )
        counter_count = sum(
            row.get("direction") == "COUNTER"
            and float(row.get("counter_effect_fraction") or 0) > 0
            for row in impacts
        )
        total_support += support_count
        total_counter += counter_count
        fact_groups: defaultdict[tuple[str, str, str], list[Mapping[str, Any]]] = defaultdict(list)
        document_groups: defaultdict[
            tuple[str, str, str], list[Mapping[str, Any]]
        ] = defaultdict(list)
        for impact in impacts:
            fact_groups[
                (
                    str(impact.get("fact_cluster_id") or ""),
                    str(impact.get("component_id") or ""),
                    str(impact.get("direction") or ""),
                )
            ].append(impact)
            if impact.get("component_id") == "information_confidence":
                document_groups[
                    (
                        str(impact.get("document_cluster_id") or ""),
                        str(impact.get("component_id") or ""),
                        str(impact.get("direction") or ""),
                    )
                ].append(impact)
            fact = facts_by_id.get(str(impact.get("fact_cluster_id") or ""))
            document = documents_by_id.get(
                str(impact.get("document_cluster_id") or "")
            )
            critical["impact_fact_cluster_lineage_missing_count"] += int(
                fact is None
                or impact.get("impact_id") not in (fact or {}).get("impact_ids", [])
                or impact.get("claim_id") not in (fact or {}).get("claim_ids", [])
            )
            critical["impact_document_cluster_lineage_missing_count"] += int(
                document is None
                or impact.get("impact_id")
                not in (document or {}).get("impact_ids", [])
                or impact.get("claim_id")
                not in (document or {}).get("claim_ids", [])
            )
            critical["impact_invalid_validation_status_count"] += int(
                impact.get("validation_status") != "CREDIT_VALIDATED_V2"
            )
            critical["impact_corroboration_only_has_credit_count"] += int(
                impact.get("corroboration_only") is True
                and float(impact.get("validated_credit_fraction") or 0) > 0
            )
            critical["impact_counter_zero_effect_count"] += int(
                impact.get("direction") == "COUNTER"
                and float(impact.get("counter_effect_fraction") or 0) <= 0
            )
        critical["impact_same_fact_duplicate_credit_count"] += sum(
            max(
                0,
                sum(
                    float(row.get("validated_credit_fraction") or 0) > 0
                    for row in rows
                )
                - 1,
            )
            for rows in fact_groups.values()
        )
        critical["impact_same_document_information_duplicate_credit_count"] += sum(
            max(
                0,
                sum(
                    float(row.get("validated_credit_fraction") or 0) > 0
                    for row in rows
                )
                - 1,
            )
            for rows in document_groups.values()
        )
        critical["impact_fact_primary_missing_count"] += sum(
            row.get("primary_impact_id") not in impacts_by_id for row in facts
        )
        observations[target] = {
            "impact_count": len(impacts),
            "multi_impact_claim_count": multi_claim,
            "support_effect_count": support_count,
            "counter_effect_count": counter_count,
            "fact_cluster_count": len(facts),
            "document_cluster_count": len(documents),
        }
    critical["impact_many_to_many_missing_count"] += int(total_multi_claim == 0)
    critical["impact_support_plane_empty_count"] += int(total_support == 0)
    critical["impact_counter_plane_empty_count"] += int(total_counter == 0)
    return _review(root, "D", dict(critical), leafs, observations)


def _reviewer_e(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    critical: Counter[str] = Counter()
    observations: dict[str, Any] = {}
    for target in TARGETS:
        dossier = _dossier(root, target)
        task_path = dossier / "question_source_tasks.jsonl"
        closure_path = dossier / "question_closure.jsonl"
        trace_path = dossier / "semantic_closure_trace.jsonl"
        adequacy_path = dossier / "evidence_search_adequacy.jsonl"
        assessment_path = dossier / "component_assessments.jsonl"
        leafs.extend(
            (task_path, closure_path, trace_path, adequacy_path, assessment_path)
        )
        tasks = _jsonl(task_path)
        closures = _jsonl(closure_path)
        traces = _jsonl(trace_path)
        adequacy = _jsonl(adequacy_path)
        assessments = _jsonl(assessment_path)
        rosters = [
            {str(row.get("question_family_id") or "") for row in rows}
            for rows in (tasks, closures, traces, adequacy)
        ]
        critical["reconciliation_question_roster_mismatch_count"] += sum(
            len(rosters[0] ^ roster) for roster in rosters[1:]
        )
        critical["reconciliation_component_roster_mismatch_count"] += len(
            COMPONENTS
            ^ {str(row.get("component_id") or "") for row in assessments}
        )
        for row in traces:
            input_status = str(row.get("input_closure_status") or "")
            links = row.get("component_links") or []
            linked_claim_ids = {
                str(link.get("claim_id") or "") for link in links
            }
            positive_claim_ids = {
                str(value) for value in row.get("positive_scoring_claim_ids") or ()
            }
            has_support = any(
                float(link.get("support_credit_fraction") or 0) > 0
                or link.get("credit_link_type")
                == "SHARED_FACT_OR_DOCUMENT_CREDIT"
                for link in links
            )
            has_bounded_support = any(
                0 < float(link.get("support_credit_fraction") or 0) < 1
                or link.get("credit_link_type")
                == "SHARED_FACT_OR_DOCUMENT_CREDIT"
                for link in links
            )
            critical["reconciliation_error_code_count"] += len(
                row.get("error_codes") or ()
            )
            critical["reconciliation_supported_zero_credit_count"] += int(
                input_status == "SUPPORTED_SCORING" and not has_support
            )
            critical[
                "reconciliation_partially_supported_zero_credit_count"
            ] += int(
                input_status == "PARTIALLY_SUPPORTED_SCORING"
                and not has_bounded_support
            )
            critical["reconciliation_supported_absent_component_count"] += int(
                input_status
                in {"SUPPORTED_SCORING", "PARTIALLY_SUPPORTED_SCORING"}
                and (
                    not links
                    or any(
                        link.get("component_state")
                        == "VERIFIED_ABSENT_AFTER_SEARCH"
                        for link in links
                    )
                )
            )
            critical["reconciliation_positive_claim_absent_component_count"] += len(
                positive_claim_ids - linked_claim_ids
            )
            critical["reconciliation_inadequate_absence_count"] += int(
                input_status == "EVALUATED_ABSENT"
                and row.get("search_adequate") is not True
            )
            critical["reconciliation_provider_failure_finalized_count"] += int(
                row.get("provider_failure") is True
                and row.get("reconciled_closure_status")
                not in {"PROVIDER_PENDING", "SOURCE_PENDING"}
            )
        for row in adequacy:
            critical["reconciliation_false_adequate_absence_count"] += int(
                row.get("saturation_status") == "ADEQUATE_ABSENCE"
                and bool(
                    row.get("provider_failures")
                    or row.get("budget_exhausted") is True
                    or row.get("missing_route_categories")
                    or row.get("positive_claim_ids")
                    or row.get("adequate_absence_allowed") is not True
                )
            )
        observations[target] = {
            "question_count": len(traces),
            "component_count": len(assessments),
            "scoring_question_count": sum(
                row.get("input_closure_status")
                in {"SUPPORTED_SCORING", "PARTIALLY_SUPPORTED_SCORING"}
                for row in traces
            ),
            "evaluated_absent_count": sum(
                row.get("input_closure_status") == "EVALUATED_ABSENT"
                for row in traces
            ),
        }
    return _review(root, "E", dict(critical), leafs, observations)


def _reviewer_f(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    critical: Counter[str] = Counter()
    observations: dict[str, Any] = {}
    for target in TARGETS:
        dossier = _dossier(root, target)
        subcriterion_path = dossier / "component_subcriteria.jsonl"
        assessment_path = dossier / "component_assessments.jsonl"
        vector_path = dossier / "component_score_vector.json"
        impact_path = dossier / "claim_impacts_validated.jsonl"
        claim_path = dossier / "accepted_current_claims.jsonl"
        decision_path = dossier / "atomic_stage_decision.json"
        trace_path = dossier / "stagecourt_trace.json"
        leafs.extend(
            (
                subcriterion_path,
                assessment_path,
                vector_path,
                impact_path,
                claim_path,
                decision_path,
                trace_path,
            )
        )
        subcriteria = _jsonl(subcriterion_path)
        assessments = _jsonl(assessment_path)
        vector = _json(vector_path)
        impacts = _jsonl(impact_path)
        claims = _jsonl(claim_path)
        decision = _json(decision_path)
        trace = _json(trace_path)
        subcriteria_by_id = {
            str(row.get("score_id") or ""): row for row in subcriteria
        }
        assessment_by_component = {
            str(row.get("component_id") or ""): row for row in assessments
        }
        vector_values = vector.get("component_score_vector") or {}
        critical["score_component_vector_roster_mismatch_count"] += len(
            COMPONENTS ^ set(vector_values)
        )
        critical["score_assessment_roster_mismatch_count"] += len(
            COMPONENTS ^ set(assessment_by_component)
        )
        for component_id, assessment in assessment_by_component.items():
            critical["score_assessment_vector_value_mismatch_count"] += int(
                not _close(
                    assessment.get("verified_points"),
                    vector_values.get(component_id),
                )
            )
            score_ids = set(assessment.get("subcriterion_score_ids") or ())
            critical["score_subcriterion_lineage_mismatch_count"] += len(
                score_ids
                ^ {
                    score_id
                    for score_id, row in subcriteria_by_id.items()
                    if row.get("component_id") == component_id
                }
            )
            for score_id in score_ids:
                subcriterion = subcriteria_by_id.get(score_id) or {}
                subcriterion_id = str(
                    subcriterion.get("subcriterion_id") or ""
                )
                critical["score_subcriterion_point_mismatch_count"] += int(
                    not _close(
                        subcriterion.get("points"),
                        (assessment.get("subcriterion_points") or {}).get(
                            subcriterion_id
                        ),
                    )
                )
        vector_sum = round(
            sum(float(value) for value in vector_values.values()), 6
        )
        critical["score_component_sum_total_mismatch_count"] += int(
            not _close(vector_sum, vector.get("full_e2r_score"))
        )
        critical["score_full_validity_failure_count"] += int(
            bool(
                vector.get("full_score_valid") is not True
                or vector.get("score_type") != "FULL_E2R_100"
                or vector.get("material_nonterminal_components")
            )
        )
        critical["score_stage_not_final_count"] += int(
            decision.get("decision_status") != "FINAL"
        )
        critical["score_invalid_canonical_stage_count"] += int(
            decision.get("canonical_stage") not in CANONICAL_STAGES
        )
        critical["score_decision_value_mismatch_count"] += int(
            not _close(
                decision.get("full_e2r_score"), vector.get("full_e2r_score")
            )
        )
        for key in (
            "decision_id",
            "trace_id",
            "target_id",
            "as_of_date",
            "canonical_stage",
            "full_thesis_stage",
        ):
            critical["score_stage_trace_identity_mismatch_count"] += int(
                decision.get(key) != trace.get(key)
            )
        critical["score_claim_trace_roster_mismatch_count"] += len(
            {str(row.get("claim_id") or "") for row in claims}
            ^ set(decision.get("accepted_claim_ids") or ())
        )
        critical["score_impact_trace_roster_mismatch_count"] += len(
            {str(row.get("impact_id") or "") for row in impacts}
            ^ set(decision.get("claim_impact_ids") or ())
        )
        critical["score_component_trace_roster_mismatch_count"] += len(
            {str(row.get("assessment_id") or "") for row in assessments}
            ^ set(decision.get("component_assessment_ids") or ())
        )
        event_overlay = decision.get("event_overlay") or {}
        critical["score_event_overlay_stage_injection_count"] += int(
            event_overlay.get("canonical_stage_effect") != "NONE"
            or decision.get("full_thesis_stage")
            != decision.get("canonical_stage")
        )
        risk_overlay = decision.get("risk_overlay") or {}
        critical["score_hard_break_without_current_open_counter_count"] += len(
            set(risk_overlay.get("hard_break_claim_ids") or ())
            - set(
                risk_overlay.get("current_direct_open_counter_claim_ids") or ()
            )
        )
        observations[target] = {
            "subcriterion_count": len(subcriteria),
            "component_vector": dict(vector_values),
            "full_e2r_score": vector.get("full_e2r_score"),
            "score_type": vector.get("score_type"),
            "canonical_stage": decision.get("canonical_stage"),
            "decision_status": decision.get("decision_status"),
            "event_overlay_status": event_overlay.get("status"),
        }
    return _review(root, "F", dict(critical), leafs, observations)


def _reviewer_g(root: Path) -> Mapping[str, Any]:
    leafs: list[Path] = []
    live_impacts = {}
    live_claims = {}
    live_subcriteria = {}
    for target in TARGETS:
        dossier = _dossier(root, target)
        claim_path = dossier / "accepted_current_claims.jsonl"
        impact_path = dossier / "claim_impacts_validated.jsonl"
        subcriterion_path = dossier / "component_subcriteria.jsonl"
        leafs.extend((claim_path, impact_path, subcriterion_path))
        live_claims[target] = _jsonl(claim_path)
        live_impacts[target] = _jsonl(impact_path)
        live_subcriteria[target] = _jsonl(subcriterion_path)
    frozen = root / "output/evidence_to_score_v2/frozen_52f09f3/005930"
    frozen_claim_path = frozen / "accepted_current_claims.jsonl"
    frozen_eligibility_path = frozen / "claim_eligibility_decisions.jsonl"
    frozen_impact_path = frozen / "claim_impacts_validated.jsonl"
    frozen_disposition_path = frozen / "impact_mapping_dispositions.jsonl"
    replay_path = root / "docs/operational/e2r_c06_historical_component_replay.json"
    leafs.extend(
        (
            frozen_claim_path,
            frozen_eligibility_path,
            frozen_impact_path,
            frozen_disposition_path,
            replay_path,
        )
    )
    frozen_claims = _jsonl(frozen_claim_path)
    frozen_eligibility = _jsonl(frozen_eligibility_path)
    frozen_impacts = _jsonl(frozen_impact_path)
    frozen_dispositions = _jsonl(frozen_disposition_path)
    replay = _json(replay_path)
    replay_cases = {
        str(row.get("case_id") or ""): row for row in replay.get("cases") or ()
    }
    samsung = live_impacts["005930"]
    hynix = live_impacts["000660"]
    tesla_claim_ids = {
        str(row.get("claim_id") or "")
        for row in frozen_claims
        if "tesla" in _compact_text(row).casefold()
        and "foundry" in _compact_text(row).casefold()
    }
    frozen_eligibility_by_claim = {
        str(row.get("claim_id") or ""): row for row in frozen_eligibility
    }
    qualification = replay_cases.get(
        "C06-SAMSUNG-20240524-QUALIFICATION-LAG", {}
    )
    sold_out = replay_cases.get("C06-SKHYNIX-20240502-SOLDOUT", {})
    revenue_mix = replay_cases.get(
        "C06-SKHYNIX-20250123-REVENUE-MIX", {}
    )
    reopen = replay_cases.get("C06-SAMSUNG-20250131-REOPEN-CAP", {})
    package_guard = replay_cases.get("C06-SAMSUNG-PACKAGE-PROFILE-GUARD", {})
    critical = {
        "c06_samsung_hbm_shipment_nonzero_missing_count": int(
            not _has_positive_effect(
                samsung,
                primitive_ids={"shipment_or_revenue_mix"},
                component_ids={"earnings_visibility", "eps_fcf_explosion"},
            )
        ),
        "c06_samsung_capacity_nonzero_missing_count": int(
            not _has_positive_effect(
                samsung,
                primitive_ids={"hbm_capacity_constraint"},
                component_ids={"earnings_visibility", "bottleneck_pricing"},
            )
        ),
        "c06_hynix_capacity_nonzero_missing_count": int(
            not _has_positive_effect(
                hynix,
                primitive_ids={"hbm_capacity_constraint"},
                component_ids={"earnings_visibility", "bottleneck_pricing"},
            )
        ),
        "c06_hynix_revenue_nonzero_missing_count": int(
            not _has_positive_effect(
                hynix,
                primitive_ids={"actual_earnings_conversion"},
                component_ids={"earnings_visibility", "eps_fcf_explosion"},
            )
        ),
        "c06_hynix_margin_nonzero_missing_count": int(
            not any(
                row.get("subcriterion_id") == "C06_EPS_MARGIN_CONVERSION"
                and float(row.get("points") or 0) > 0
                for row in live_subcriteria["000660"]
            )
        ),
        "c06_capacity_counter_nonzero_missing_count": int(
            not any(
                row.get("primitive_id") == "capacity_supply_response"
                and row.get("direction") == "COUNTER"
                and float(row.get("counter_effect_fraction") or 0) > 0
                for row in samsung
            )
        ),
        "c06_foundry_tesla_fixture_missing_count": int(not tesla_claim_ids),
        "c06_foundry_tesla_credited_count": sum(
            row.get("claim_id") in tesla_claim_ids
            and float(row.get("validated_credit_fraction") or 0) > 0
            for row in frozen_impacts
        ),
        "c06_foundry_tesla_eligibility_failure_count": sum(
            frozen_eligibility_by_claim.get(claim_id, {}).get(
                "eligibility_status"
            )
            != "INELIGIBLE_WRONG_MECHANISM"
            for claim_id in tesla_claim_ids
        ),
        "c06_foundry_tesla_rejection_missing_count": sum(
            not any(
                row.get("claim_id") == claim_id
                and row.get("status") == "IMPACT_MAPPING_REJECTED"
                for row in frozen_dispositions
            )
            for claim_id in tesla_claim_ids
        ),
        "c06_substrate_economic_credit_count": sum(
            row.get("primitive_id") == "package_substrate_sympathy"
            and float(row.get("validated_credit_fraction") or 0) > 0
            for row in hynix
        ),
        "c06_qualification_counter_failure_count": int(
            not any(
                row.get("direction") == "COUNTER"
                for row in qualification.get("proposal_rows") or ()
            )
            or qualification.get("hard_break_emitted") is True
            or int(qualification.get("direction_error_count") or 0) != 0
        ),
        "c06_historical_soldout_effect_failure_count": int(
            not {"earnings_visibility", "bottleneck_pricing"}
            <= set(sold_out.get("predicted_component_ids") or ())
            or int(sold_out.get("required_component_missing_count") or 0) != 0
            or int(sold_out.get("forbidden_component_count") or 0) != 0
        ),
        "c06_historical_revenue_mix_effect_failure_count": int(
            not {"earnings_visibility", "eps_fcf_explosion"}
            <= set(revenue_mix.get("predicted_component_ids") or ())
            or int(revenue_mix.get("required_component_missing_count") or 0)
            != 0
            or int(revenue_mix.get("forbidden_component_count") or 0) != 0
        ),
        "c06_reopen_customer_dependency_overcredit_count": sum(
            key in set(reopen.get("predicted_component_ids") or ())
            for key in ("earnings_visibility", "bottleneck_pricing")
        ),
        "c06_package_profile_economic_credit_count": sum(
            key in set(package_guard.get("predicted_component_ids") or ())
            for key in COMPONENTS - {"information_confidence"}
        ),
    }
    return _review(
        root,
        "G",
        critical,
        leafs,
        {
            "live_claim_counts": {
                target: len(rows) for target, rows in live_claims.items()
            },
            "live_impact_counts": {
                target: len(rows) for target, rows in live_impacts.items()
            },
            "tesla_foundry_claim_ids": sorted(tesla_claim_ids),
            "historical_case_count": len(replay_cases),
            "samsung_counter_effect_count": sum(
                row.get("direction") == "COUNTER"
                and float(row.get("counter_effect_fraction") or 0) > 0
                for row in samsung
            ),
        },
    )


def _reviewer_h(root: Path) -> Mapping[str, Any]:
    artifact_path = (
        root / "docs/operational/e2r_evidence_to_score_generalization_audit.json"
    )
    policy_path = root / "configs/e2r_scoring_policy_v2.json"
    weight_path = root / "configs/e2r_archetype_weight_profile_v2_2.json"
    artifact = _json(artifact_path)
    cases = artifact.get("cases") or {}
    c08_positive = cases.get("c08_direct_customer_order_positive") or {}
    c08_profile = cases.get("c08_product_profile_only_guard") or {}
    c15_positive = cases.get("c15_issuer_pass_through_positive") or {}
    c15_headline = cases.get("c15_raw_commodity_headline_guard") or {}
    wrong_subject = cases.get("wrong_subject_accounting_guard") or {}
    wrong_segment = cases.get("same_issuer_wrong_segment_guard") or {}
    old_risk = cases.get("old_risk_resolved_guard") or {}
    support_counter = cases.get("support_counter_same_component") or {}
    weights = _json(weight_path)
    critical = {
        "generalization_case_count_mismatch": abs(len(cases) - 13),
        "generalization_all_archetype_totality_count_mismatch": abs(
            len(weights.get("archetype_weights") or {}) - 36
        )
        + abs(int(artifact.get("all_archetype_rubric_count") or 0) - 36),
        "generalization_c08_positive_failure_count": int(
            float(
                (c08_positive.get("component_score_vector") or {}).get(
                    "earnings_visibility", 0
                )
            )
            <= 0
            or int(c08_positive.get("support_impact_count") or 0) <= 0
        ),
        "generalization_c08_profile_overcredit_count": sum(
            float((c08_profile.get("component_score_vector") or {}).get(key, 0))
            > 0
            for key in COMPONENTS - {"information_confidence"}
        ),
        "generalization_c15_positive_failure_count": int(
            float(
                (c15_positive.get("component_score_vector") or {}).get(
                    "bottleneck_pricing", 0
                )
            )
            <= 0
            or float(
                (c15_positive.get("component_score_vector") or {}).get(
                    "eps_fcf_explosion", 0
                )
            )
            <= 0
        ),
        "generalization_c15_headline_overcredit_count": sum(
            float(value) > 0
            for value in (c15_headline.get("component_score_vector") or {}).values()
        ),
        "generalization_wrong_subject_acceptance_count": int(
            wrong_subject.get("rejection_reason") != "TARGET_MISMATCH"
            or int(wrong_subject.get("rejected_impact_count") or 0) <= 0
        ),
        "generalization_wrong_segment_acceptance_count": int(
            wrong_segment.get("rejection_reason")
            != "REROUTED_TO_OTHER_MECHANISM"
            or wrong_segment.get("original_gap_open") is not True
        ),
        "generalization_old_risk_penalty_retained_count": int(
            int(old_risk.get("open_counter_impact_count") or 0) != 0
            or int(old_risk.get("resolution_impact_count") or 0) <= 0
            or float(old_risk.get("counter_effect_fraction") or 0) != 0
        ),
        "generalization_support_counter_plane_loss_count": int(
            float(support_counter.get("support_effect_fraction") or 0) <= 0
            or float(support_counter.get("counter_effect_fraction") or 0) <= 0
            or (support_counter.get("component_statuses") or {}).get(
                "bottleneck_pricing"
            )
            != "CONTRADICTED_OPEN"
        ),
        "generalization_case_future_leakage_count": sum(
            int(row.get("future_leakage_count") or 0)
            for row in cases.values()
            if isinstance(row, Mapping)
        ),
        "generalization_source_proxy_score_count": int(
            artifact.get("source_proxy_score_count") or 0
        ),
    }
    return _review(
        root,
        "H",
        critical,
        (artifact_path, policy_path, weight_path),
        {
            "case_count": len(cases),
            "all_archetype_rubric_count": artifact.get(
                "all_archetype_rubric_count"
            ),
            "c08_positive_score": c08_positive.get("verified_supported_score"),
            "c08_profile_score": c08_profile.get("verified_supported_score"),
            "c15_positive_score": c15_positive.get("verified_supported_score"),
            "c15_headline_score": c15_headline.get("verified_supported_score"),
        },
    )


def _review(
    root: Path,
    reviewer_id: str,
    critical_counts: Mapping[str, int],
    leaf_paths: Sequence[Path],
    observations: Mapping[str, Any],
) -> Mapping[str, Any]:
    unique_paths = tuple(dict.fromkeys(Path(path) for path in leaf_paths))
    missing_leaf_count = sum(not path.is_file() for path in unique_paths)
    normalized = {
        str(key): int(value) for key, value in critical_counts.items()
    }
    normalized[f"reviewer_{reviewer_id.lower()}_missing_leaf_count"] = (
        missing_leaf_count
    )
    critical_sum = sum(normalized.values())
    existing_paths = tuple(path for path in unique_paths if path.is_file())
    return {
        "reviewer_id": reviewer_id,
        "scope": REVIEWER_SCOPES[reviewer_id],
        "counter_namespace": f"semantic_reviewer_{reviewer_id.lower()}",
        "counter_derivation": "DIRECT_DETAILED_LEAF_RECOMPUTE",
        "report_generator_counter_ids": [],
        "status": (
            f"REVIEWER_{reviewer_id}_PASS"
            if critical_sum == 0
            else f"REVIEWER_{reviewer_id}_FAIL"
        ),
        "direct_leaf_reread": bool(existing_paths),
        "direct_leaf_paths": [
            str(path.relative_to(root)) for path in existing_paths
        ],
        "direct_leaf_sha256": {
            str(path.relative_to(root)): _sha256(path) for path in existing_paths
        },
        "observations": dict(observations),
        "critical_counts": normalized,
        "critical_count_sum": critical_sum,
    }


def _dossier(root: Path, target: str) -> Path:
    return root / "output/evidence_to_score_v2/live_2026-07-11" / target


def _json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[Mapping[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _close(first: Any, second: Any, tolerance: float = 1e-6) -> bool:
    if first is None or second is None:
        return False
    return abs(float(first) - float(second)) <= tolerance


def _compact_text(row: Mapping[str, Any]) -> str:
    return json.dumps(row, ensure_ascii=False, sort_keys=True)


def _has_positive_effect(
    impacts: Sequence[Mapping[str, Any]],
    *,
    primitive_ids: set[str],
    component_ids: set[str],
) -> bool:
    return any(
        row.get("primitive_id") in primitive_ids
        and row.get("component_id") in component_ids
        and float(row.get("support_credit_fraction") or 0) > 0
        for row in impacts
    )


__all__ = [
    "FAIL_STATUS",
    "PASS_STATUS",
    "REVIEWER_SCOPES",
    "SCHEMA_VERSION",
    "compile_semantic_scoring_reviewer_gate",
    "evaluate_semantic_scoring_reviewer_gate",
]
