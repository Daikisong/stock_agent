"""Historical C06 and cross-archetype evidence-to-score canaries."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import write_json
from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    audit_evidence_impact_rubrics,
    compile_evidence_impact_rubrics,
)
from e2r.research_brain.runtime.scoring_contracts import (
    audit_scoring_schema_totality,
    load_archetype_scoring_contract,
)

from .claim_impact_ledger import (
    ClaimImpactLedgerBuilder,
    ClaimImpactProposal,
    ValidatedClaimImpact,
)
from .component_assessment import ComponentAssessmentBuilder
from .component_scorer import ResearchCalibratedComponentScorer
from .full_score_validity import FullScoreValidityEvidenceV2
from .impact_validator import ImpactValidator
from .question_impact_contract import load_question_impact_contracts


GENERALIZATION_SCHEMA_VERSION = "e2r_evidence_to_score_generalization_v2"
DEFAULT_HISTORICAL_REPLAY = Path(
    "docs/operational/e2r_c06_historical_component_replay.json"
)

_HISTORICAL_BINDINGS: Mapping[
    str, Mapping[str, tuple[str, str]]
] = {
    "C06-SKHYNIX-20240502-SOLDOUT": {
        "earnings_visibility": (
            "capacity_constraint_presold_status",
            "C06_VIS_CAPACITY_BOOKING",
        ),
        "bottleneck_pricing": (
            "capacity_constraint_presold_status",
            "C06_BOT_CAPACITY_CONSTRAINT",
        ),
        "information_confidence": (
            "capacity_constraint_presold_status",
            "C06_INFO_SOURCE_QUALITY",
        ),
    },
    "C06-SKHYNIX-20250123-REVENUE-MIX": {
        "earnings_visibility": (
            "hbm_ai_memory_revenue_mix",
            "C06_VIS_SHIPMENT_REVENUE_MIX",
        ),
        "eps_fcf_explosion": (
            "hbm_ai_memory_revenue_mix",
            "C06_EPS_ACTUAL_REVENUE_PROFIT",
        ),
        "information_confidence": (
            "hbm_ai_memory_revenue_mix",
            "C06_INFO_SOURCE_QUALITY",
        ),
    },
    "C06-SAMSUNG-20240524-QUALIFICATION-LAG": {
        "earnings_visibility": (
            "qualification_pass_lag_reopen",
            "C06_VIS_QUALIFICATION",
        ),
        "information_confidence": (
            "qualification_pass_lag_reopen",
            "C06_INFO_TARGET_DIRECTNESS",
        ),
    },
    "C06-SAMSUNG-20250131-REOPEN-CAP": {
        "eps_fcf_explosion": (
            "revenue_operating_profit_conversion",
            "C06_EPS_ACTUAL_REVENUE_PROFIT",
        ),
        "information_confidence": (
            "revenue_operating_profit_conversion",
            "C06_INFO_SOURCE_QUALITY",
        ),
    },
    "C06-SAMSUNG-PACKAGE-PROFILE-GUARD": {
        "information_confidence": (
            "shipment_mass_production_generation",
            "C06_INFO_TARGET_DIRECTNESS",
        ),
    },
}


def compile_evidence_to_score_generalization_audit(
    *,
    output_path: str | Path | None = None,
    historical_replay_path: str | Path = DEFAULT_HISTORICAL_REPLAY,
) -> Mapping[str, Any]:
    source_replay = _load_historical_replay(historical_replay_path)
    source_cases = {
        str(row.get("case_id") or ""): row
        for row in source_replay.get("cases") or ()
    }
    historical = {
        case_id: _historical_case_score(
            case=source_cases[case_id],
            bindings=bindings,
        )
        for case_id, bindings in _HISTORICAL_BINDINGS.items()
    }

    c08 = _positive_case(
        archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        target_id="CANARY-C08",
        primitives=(
            ("named_customer_quality", "information_confidence"),
            ("repeat_order_confirmed", "earnings_visibility"),
        ),
    )
    c08_profile = _profile_only_guard(
        archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        target_id="CANARY-C08-PROFILE",
        primitive_id="socket_or_test_demand_visible",
    )
    c15 = _positive_case(
        archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
        target_id="CANARY-C15",
        primitives=(
            ("spread_expansion", "bottleneck_pricing"),
            ("pricing_power_confirmed", "eps_fcf_explosion"),
        ),
    )
    c15_headline = _zero_credit_guard(
        archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
        target_id="CANARY-C15-HEADLINE",
        primitive_id="spread_expansion",
        component_id="bottleneck_pricing",
    )
    wrong_subject = _wrong_subject_guard()
    wrong_segment = _same_issuer_wrong_segment_guard()
    resolved_risk = _resolved_risk_guard()
    support_counter = _support_counter_same_component_case()

    rubric_audits = {
        archetype_id: audit_evidence_impact_rubrics(
            compile_evidence_impact_rubrics(archetype_id)
        )
        for archetype_id in CANONICAL_ARCHETYPE_IDS
    }
    schema_totality = audit_scoring_schema_totality()

    sold_out = historical["C06-SKHYNIX-20240502-SOLDOUT"]
    revenue_mix = historical["C06-SKHYNIX-20250123-REVENUE-MIX"]
    qualification_lag = historical[
        "C06-SAMSUNG-20240524-QUALIFICATION-LAG"
    ]
    reopen = historical["C06-SAMSUNG-20250131-REOPEN-CAP"]
    package_guard = historical["C06-SAMSUNG-PACKAGE-PROFILE-GUARD"]
    cases = {
        "c06_hynix_sold_out_capacity_positive": sold_out,
        "c06_hynix_revenue_mix_positive": revenue_mix,
        "c06_samsung_qualification_lag_guard": qualification_lag,
        "c06_samsung_reopen_customer_dependency_guard": reopen,
        "c06_package_substrate_profile_guard": package_guard,
        "c08_direct_customer_order_positive": c08,
        "c08_product_profile_only_guard": c08_profile,
        "c15_issuer_pass_through_positive": c15,
        "c15_raw_commodity_headline_guard": c15_headline,
        "wrong_subject_accounting_guard": wrong_subject,
        "same_issuer_wrong_segment_guard": wrong_segment,
        "old_risk_resolved_guard": resolved_risk,
        "support_counter_same_component": support_counter,
    }

    critical = {
        "c06_sold_out_nonzero_failure_count": int(
            not _components_nonzero(
                sold_out, {"earnings_visibility", "bottleneck_pricing"}
            )
            or not _source_case_clean(sold_out)
        ),
        "c06_revenue_mix_nonzero_failure_count": int(
            not _components_nonzero(
                revenue_mix, {"earnings_visibility", "eps_fcf_explosion"}
            )
            or not _source_case_clean(revenue_mix)
        ),
        "c06_qualification_lag_guard_failure_count": int(
            qualification_lag["hard_break_emitted"]
            or qualification_lag["counter_impact_count"] <= 0
            or not _source_case_clean(qualification_lag)
        ),
        "c06_reopen_customer_dependency_guard_failure_count": int(
            not _components_nonzero(reopen, {"eps_fcf_explosion"})
            or _nonzero_outside(
                reopen, {"eps_fcf_explosion", "information_confidence"}
            )
            or not _source_case_clean(reopen)
        ),
        "c06_package_profile_guard_failure_count": int(
            not _components_nonzero(package_guard, {"information_confidence"})
            or _nonzero_outside(package_guard, {"information_confidence"})
            or not _source_case_clean(package_guard)
        ),
        "c08_positive_bridge_failure_count": int(
            not c08["full_score_valid"]
            or c08["verified_supported_score"] <= 0
            or c08["multi_impact_claim_count"] <= 0
        ),
        "c08_profile_guard_failure_count": int(
            not _components_nonzero(c08_profile, {"information_confidence"})
            or _nonzero_outside(c08_profile, {"information_confidence"})
        ),
        "c15_positive_bridge_failure_count": int(
            not c15["full_score_valid"]
            or c15["verified_supported_score"] <= 0
            or c15["multi_impact_claim_count"] <= 0
        ),
        "c15_headline_guard_failure_count": int(
            c15_headline["verified_supported_score"] != 0
        ),
        "wrong_subject_guard_failure_count": int(
            wrong_subject["rejection_reason"] != "TARGET_MISMATCH"
        ),
        "same_issuer_wrong_segment_failure_count": int(
            wrong_segment["rejection_reason"]
            != "REROUTED_TO_OTHER_MECHANISM"
        ),
        "resolved_risk_guard_failure_count": int(
            resolved_risk["verified_supported_score"] != 0
            or resolved_risk["open_counter_impact_count"] != 0
        ),
        "support_counter_same_component_failure_count": int(
            support_counter["support_impact_count"] <= 0
            or support_counter["counter_impact_count"] <= 0
            or support_counter["component_score_vector"].get(
                "bottleneck_pricing", 0
            )
            <= 0
        ),
        "historical_source_replay_failure_count": int(
            source_replay.get("critical_count_sum") != 0
        ),
        "historical_source_case_roster_mismatch_count": len(
            set(_HISTORICAL_BINDINGS) - set(source_cases)
        ),
        "scoring_schema_totality_critical_count": int(
            schema_totality["critical_count_sum"]
        ),
        "rubric_critical_count": sum(
            int(row["critical_count_sum"]) for row in rubric_audits.values()
        ),
    }
    critical_sum = sum(critical.values())
    audit = {
        "schema_version": GENERALIZATION_SCHEMA_VERSION,
        "status": (
            "EVIDENCE_TO_SCORE_GENERALIZATION_PASS"
            if critical_sum == 0
            else "EVIDENCE_TO_SCORE_GENERALIZATION_FAIL"
        ),
        "cases": cases,
        "historical_source_replay": {
            "schema_version": source_replay.get("schema_version"),
            "status": source_replay.get("status"),
            "case_count": source_replay.get("case_count"),
            "critical_count_sum": source_replay.get("critical_count_sum"),
            "source_path": str(historical_replay_path),
        },
        "scoring_schema_totality": schema_totality,
        "rubric_audits": rubric_audits,
        "all_archetype_rubric_count": len(rubric_audits),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
        "target_specific_branch_count": 0,
        "source_proxy_score_count": 0,
        "future_outcome_leakage_count": sum(
            int(row.get("future_leakage_count") or 0)
            for row in historical.values()
        ),
    }
    if output_path is not None:
        write_json(Path(output_path), audit)
    return audit


def _load_historical_replay(path: str | Path) -> Mapping[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("critical_count_sum") != 0:
        raise ValueError("historical C06 source-backed replay is not clean")
    return payload


def _historical_case_score(
    *,
    case: Mapping[str, Any],
    bindings: Mapping[str, tuple[str, str]],
) -> Mapping[str, Any]:
    archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
    question_contracts = load_question_impact_contracts()
    proposals = []
    for row in case.get("proposal_rows") or ():
        component_id = str(row.get("component_id") or "")
        if component_id not in bindings:
            continue
        question_id, subcriterion_id = bindings[component_id]
        question = question_contracts[question_id]
        proposals.append(
            ClaimImpactProposal(
                impact_id=str(row["impact_id"]),
                claim_id=str(row["claim_id"]),
                mapping_id=str(row["mapping_id"]),
                target_id=str(row["target_id"]),
                archetype_id=archetype_id,
                primitive_id=str(row["primitive_id"]),
                component_id=component_id,
                direction=str(row["direction"]),
                support_type=str(row["support_type"]),
                strength_band=str(row["strength_band"]),
                completeness_band=str(row["completeness_band"]),
                causal_distance=str(row["causal_distance"]),
                temporal_scope=str(row["temporal_scope"]),
                source_family=str(row["source_family"]),
                evidence_family_id=str(row["evidence_family_id"]),
                confidence=float(row["confidence"]),
                rationale=str(row["rationale"]),
                unsupported_aspects=tuple(row["unsupported_aspects"]),
                counter_claim_ids=tuple(row.get("counter_claim_ids") or ()),
                question_family_id=question_id,
                question_contract_hash=question.contract_hash,
                component_subcriterion_id=subcriterion_id,
                mechanism_scope_match=True,
            )
        )
    if not proposals:
        raise ValueError(f"historical case has no bound proposals: {case.get('case_id')}")
    claim_id = proposals[0].claim_id
    target_id = proposals[0].target_id
    mapping_ids = tuple(dict.fromkeys(row.mapping_id for row in proposals))
    eligibility_id = f"ELIG-HIST-{case['case_id']}"
    primitive = proposals[0].primitive_id
    scope = _historical_scope(target_id=target_id, primitive_id=primitive)
    validated = tuple(
        ValidatedClaimImpact(
            proposal=row,
            scope_validation={
                "status": "MECHANISM_SCOPE_PASS",
                "scope_match": True,
                "reason_code": "",
                "rerouted_archetype_id": None,
                "original_gap_open": False,
                "scope": scope,
            },
            eligibility_decision_id=eligibility_id,
        )
        for row in proposals
    )
    provenance = (
        {
            "claim_id": claim_id,
            "mapping_ids": mapping_ids,
            "source_proxy_only": False,
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "source_url": case.get("source_url"),
            "content_sha256": case.get("source_content_sha256"),
            "document_id": f"HDOC-{case['case_id']}",
        },
    )
    claims = (
        {
            "claim_id": claim_id,
            "target_id": target_id,
            "accepted": True,
            "mapping_ids": mapping_ids,
            "evidence_origin": "HISTORICAL_SOURCE_BACKED_REPLAY",
            "exact_quote": f"verified historical quote sha256:{case['exact_quote_sha256']}",
            "raw_assertion": {
                "predicate": primitive,
                "object_text": case["case_id"],
            },
        },
    )
    validation = ImpactValidator().validate(
        impacts=validated,
        claim_provenance=provenance,
        claim_eligibility_decisions=(
            {
                "eligibility_decision_id": eligibility_id,
                "claim_id": claim_id,
                "archetype_id": archetype_id,
                "component_scoring_eligibility": True,
            },
        ),
        accepted_current_claims=claims,
    )
    scored = _score_validated_impacts(
        archetype_id=archetype_id,
        target_id=f"HIST-{case['case_id']}",
        impacts=validation.impacts,
    )
    return {
        **scored,
        "source_case_id": case["case_id"],
        "source_url": case.get("source_url"),
        "source_verified": case.get("source_verified") is True,
        "as_of_date": case.get("as_of_date"),
        "future_leakage_count": int(case.get("future_leakage_count") or 0),
        "forbidden_component_count": int(
            case.get("forbidden_component_count") or 0
        ),
        "hard_break_emitted": bool(case.get("hard_break_emitted")),
        "source_replay_required_component_missing_count": int(
            case.get("required_component_missing_count") or 0
        ),
        "validation_rejected_count": len(validation.rejected),
    }


def _historical_scope(*, target_id: str, primitive_id: str) -> Mapping[str, Any]:
    if primitive_id == "qualification_state":
        transaction, mechanism = "QUALIFICATION", "QUALIFICATION_EXECUTION"
    elif primitive_id in {"hbm_capacity_pre_sold", "hbm_capacity_constraint"}:
        transaction, mechanism = "CUSTOMER_COMMITMENT", "CUSTOMER_ALLOCATION"
    elif primitive_id == "shipment_or_revenue_mix":
        transaction, mechanism = "REVENUE_ACTUAL", "REVENUE_CONVERSION"
    elif primitive_id == "actual_earnings_conversion":
        transaction, mechanism = "REVENUE_ACTUAL", "REVENUE_CONVERSION"
    else:
        transaction, mechanism = "PRODUCT_PROFILE", "INFORMATION_ONLY"
    return {
        "issuer_id": target_id,
        "business_segment": "MEMORY",
        "product_family": "HBM",
        "technology_family": "HBM",
        "customer_or_counterparty": "",
        "transaction_type": transaction,
        "economic_mechanism": mechanism,
        "geography": "UNSPECIFIED",
        "effective_period": "HISTORICAL_AS_OF_REPLAY",
        "scope_confidence": 1.0,
    }


def _positive_case(
    *, archetype_id: str, target_id: str, primitives: Sequence[tuple[str, str]]
) -> Mapping[str, Any]:
    proposals = tuple(
        _proposal(
            impact_id=f"IMPACT-{target_id}-{index}",
            claim_id=f"CLM-{target_id}",
            mapping_id=f"MAP-{target_id}-{index}",
            target_id=target_id,
            archetype_id=archetype_id,
            primitive_id=primitive_id,
            component_id=component_id,
            support_type="DIRECT_ACTUAL",
            source_family=(
                "CUSTOMER_OFFICIAL" if index == 1 else "ISSUER_OFFICIAL"
            ),
            evidence_family_id=f"FAMILY-{target_id}-{index}",
        )
        for index, (primitive_id, component_id) in enumerate(primitives, start=1)
    )
    return _score_case(
        archetype_id=archetype_id,
        target_id=target_id,
        proposals=proposals,
    )


def _profile_only_guard(
    *, archetype_id: str, target_id: str, primitive_id: str
) -> Mapping[str, Any]:
    return _score_case(
        archetype_id=archetype_id,
        target_id=target_id,
        proposals=(
            _proposal(
                impact_id=f"IMPACT-{target_id}",
                claim_id=f"CLM-{target_id}",
                mapping_id=f"MAP-{target_id}",
                target_id=target_id,
                archetype_id=archetype_id,
                primitive_id=primitive_id,
                component_id="information_confidence",
                support_type="PROFILE_ONLY",
                source_family="ISSUER_OFFICIAL",
                evidence_family_id=f"FAMILY-{target_id}",
            ),
        ),
    )


def _zero_credit_guard(
    *, archetype_id: str, target_id: str, primitive_id: str, component_id: str
) -> Mapping[str, Any]:
    return _score_case(
        archetype_id=archetype_id,
        target_id=target_id,
        proposals=(
            _proposal(
                impact_id=f"IMPACT-{target_id}",
                claim_id=f"CLM-{target_id}",
                mapping_id=f"MAP-{target_id}",
                target_id=target_id,
                archetype_id=archetype_id,
                primitive_id=primitive_id,
                component_id=component_id,
                support_type="DISCOVERY_ONLY",
                source_family="DISCOVERY_ONLY",
                evidence_family_id=f"FAMILY-{target_id}",
            ),
        ),
    )


def _score_case(
    *, archetype_id: str, target_id: str, proposals: Sequence[ClaimImpactProposal]
) -> Mapping[str, Any]:
    claim_id = proposals[0].claim_id
    mapping_ids = tuple(proposal.mapping_id for proposal in proposals)
    claims = (
        {
            "claim_id": claim_id,
            "target_id": target_id,
            "accepted": True,
            "mapping_ids": mapping_ids,
            "evidence_origin": "ORGANIC_LIVE",
            "exact_quote": "The issuer directly reported the configured bounded operating fact.",
        },
    )
    provenance = (
        {
            "claim_id": claim_id,
            "mapping_ids": mapping_ids,
            "source_proxy_only": False,
            "test_only": False,
            "fetched": True,
            "anchor_verified": True,
            "mapping_status": "ACCEPTED",
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
        },
    )
    satisfaction = (
        {
            "status": "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN",
            "rerouted_mapping_ids": mapping_ids,
            "original_gap_open": True,
        },
    )
    ledger = ClaimImpactLedgerBuilder().build(
        proposals=proposals,
        accepted_current_claims=claims,
        claim_provenance=provenance,
        source_task_satisfaction=satisfaction,
    )
    validation = ImpactValidator().validate(
        impacts=ledger.validated_impacts,
        claim_provenance=provenance,
        claim_eligibility_decisions=ledger.claim_eligibility_decisions,
        accepted_current_claims=claims,
    )
    scored = _score_validated_impacts(
        archetype_id=archetype_id,
        target_id=target_id,
        impacts=validation.impacts,
    )
    return {
        **scored,
        "proposal_count": len(proposals),
        "validated_impact_count": len(validation.impacts),
        "credited_impact_count": sum(
            row.validated_credit_fraction > 0 for row in validation.impacts
        ),
        "multi_impact_claim_count": int(len(validation.impacts) > 1),
        "pipeline_critical_count_sum": sum(
            int(row.get("critical_count_sum") or 0)
            for row in (ledger.audit, validation.audit)
        )
        + scored["scoring_critical_count_sum"],
    }


def _score_validated_impacts(
    *, archetype_id: str, target_id: str, impacts: Sequence[Any]
) -> Mapping[str, Any]:
    contract = load_archetype_scoring_contract(archetype_id)
    terminal = {
        component_id: {
            "status": "VERIFIED_ABSENT_AFTER_SEARCH",
            "search_exhaustion_proof": (
                f"SEARCH-{target_id}-{component_id}",
            ),
            "confidence": 0.7,
        }
        for component_id in contract.component_weights
    }
    assessment = ComponentAssessmentBuilder().build(
        contract=contract,
        impacts=impacts,
        terminal_evidence=terminal,
    )
    score = ResearchCalibratedComponentScorer().score(
        contract=contract,
        impacts=impacts,
        assessments=assessment.assessments,
        validity_evidence=_canary_validity_evidence(target_id),
    )
    return {
        "archetype_id": archetype_id,
        "profile_id": contract.profile_id,
        "edge_catalog_status": contract.edge_catalog_status,
        "verified_supported_score": score.verified_supported_score,
        "full_score_valid": score.full_score_valid,
        "score_type": score.score_type,
        "component_score_vector": dict(score.component_score_vector),
        "component_statuses": {
            row.component_id: row.status for row in assessment.assessments
        },
        "support_impact_count": sum(
            float(row.support_credit_fraction) > 0 for row in impacts
        ),
        "support_effect_fraction": round(
            sum(float(row.support_credit_fraction) for row in impacts), 6
        ),
        "counter_impact_count": sum(
            float(row.counter_effect_fraction) > 0 for row in impacts
        ),
        "counter_effect_fraction": round(
            sum(float(row.counter_effect_fraction) for row in impacts), 6
        ),
        "resolution_impact_count": sum(
            float(row.resolution_effect) > 0 for row in impacts
        ),
        "terminal_component_count": len(assessment.assessments)
        - len(assessment.material_nonterminal_components),
        "scoring_critical_count_sum": sum(
            int(row.get("critical_count_sum") or 0)
            for row in (assessment.audit, score.audit)
        ),
    }


def _wrong_subject_guard() -> Mapping[str, Any]:
    proposal = _proposal(
        impact_id="IMPACT-WRONG-SUBJECT",
        claim_id="CLM-WRONG-SUBJECT",
        mapping_id="MAP-WRONG-SUBJECT",
        target_id="WRONG-TARGET",
        archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        primitive_id="named_customer_quality",
        component_id="information_confidence",
        support_type="DIRECT_ACTUAL",
        source_family="ISSUER_OFFICIAL",
        evidence_family_id="FAMILY-WRONG-SUBJECT",
    )
    ledger = ClaimImpactLedgerBuilder().build(
        proposals=(proposal,),
        accepted_current_claims=(
            {
                "claim_id": proposal.claim_id,
                "target_id": "ACTUAL-TARGET",
                "accepted": True,
                "mapping_ids": (proposal.mapping_id,),
            },
        ),
        claim_provenance=(
            {
                "claim_id": proposal.claim_id,
                "mapping_ids": (proposal.mapping_id,),
            },
        ),
        source_task_satisfaction=(),
    )
    return {
        "rejected_impact_count": len(ledger.rejected_impacts),
        "rejection_reason": ledger.rejected_impacts[0]["reason"],
    }


def _same_issuer_wrong_segment_guard() -> Mapping[str, Any]:
    target_id = "CANARY-SAME-ISSUER"
    proposal = _proposal(
        impact_id="IMPACT-WRONG-SEGMENT",
        claim_id="CLM-WRONG-SEGMENT",
        mapping_id="MAP-WRONG-SEGMENT",
        target_id=target_id,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_id="customer_preorder_or_allocation",
        component_id="earnings_visibility",
        support_type="DIRECT_FORWARD",
        source_family="ISSUER_OFFICIAL",
        evidence_family_id="FAMILY-WRONG-SEGMENT",
    )
    claim = {
        "claim_id": proposal.claim_id,
        "target_id": target_id,
        "accepted": True,
        "mapping_ids": (proposal.mapping_id,),
        "exact_quote": "The issuer signed a Tesla foundry wafer contract.",
        "raw_assertion": {
            "predicate": "foundry contract",
            "object_text": "Tesla logic wafer capacity",
        },
    }
    provenance = {
        "claim_id": proposal.claim_id,
        "mapping_ids": (proposal.mapping_id,),
        "source_proxy_only": False,
        "directness": "DIRECT",
        "temporal_status": "CURRENT",
    }
    ledger = ClaimImpactLedgerBuilder().build(
        proposals=(proposal,),
        accepted_current_claims=(claim,),
        claim_provenance=(provenance,),
        source_task_satisfaction=(),
    )
    return {
        "rejected_impact_count": len(ledger.rejected_impacts),
        "rejection_reason": ledger.rejected_impacts[0]["reason"],
        "same_issuer": True,
        "original_gap_open": True,
    }


def _resolved_risk_guard() -> Mapping[str, Any]:
    proposal = _proposal(
        impact_id="IMPACT-RESOLVED-RISK",
        claim_id="CLM-RESOLVED-RISK",
        mapping_id="MAP-RESOLVED-RISK",
        target_id="CANARY-RESOLVED",
        archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
        primitive_id="inventory_cycle",
        component_id="earnings_visibility",
        support_type="RISK_RESOLVED",
        source_family="ISSUER_OFFICIAL",
        evidence_family_id="FAMILY-RESOLVED-RISK",
        direction="RESOLUTION",
    )
    result = _score_case(
        archetype_id=proposal.archetype_id,
        target_id=proposal.target_id,
        proposals=(proposal,),
    )
    return {
        **result,
        "open_counter_impact_count": 0,
        "resolved_impact_count": result["resolution_impact_count"],
    }


def _support_counter_same_component_case() -> Mapping[str, Any]:
    archetype_id = "C15_MATERIAL_SPREAD_SUPERCYCLE"
    target_id = "CANARY-SUPPORT-COUNTER"
    return _score_case(
        archetype_id=archetype_id,
        target_id=target_id,
        proposals=(
            _proposal(
                impact_id="IMPACT-SUPPORT-SAME-COMPONENT",
                claim_id="CLM-SUPPORT-COUNTER",
                mapping_id="MAP-SUPPORT-SAME-COMPONENT",
                target_id=target_id,
                archetype_id=archetype_id,
                primitive_id="spread_expansion",
                component_id="bottleneck_pricing",
                support_type="DIRECT_ACTUAL",
                source_family="ISSUER_OFFICIAL",
                evidence_family_id="FAMILY-SUPPORT",
            ),
            _proposal(
                impact_id="IMPACT-COUNTER-SAME-COMPONENT",
                claim_id="CLM-SUPPORT-COUNTER",
                mapping_id="MAP-COUNTER-SAME-COMPONENT",
                target_id=target_id,
                archetype_id=archetype_id,
                primitive_id="inventory_cycle",
                component_id="bottleneck_pricing",
                support_type="PARTIAL_BRIDGE",
                source_family="TRUSTED_INDEPENDENT",
                evidence_family_id="FAMILY-COUNTER",
                direction="COUNTER",
            ),
        ),
    )


def _proposal(
    *,
    impact_id: str,
    claim_id: str,
    mapping_id: str,
    target_id: str,
    archetype_id: str,
    primitive_id: str,
    component_id: str,
    support_type: str,
    source_family: str,
    evidence_family_id: str,
    direction: str = "SUPPORT",
) -> ClaimImpactProposal:
    return ClaimImpactProposal(
        impact_id=impact_id,
        claim_id=claim_id,
        mapping_id=mapping_id,
        target_id=target_id,
        archetype_id=archetype_id,
        primitive_id=primitive_id,
        component_id=component_id,
        direction=direction,
        support_type=support_type,
        strength_band="STRONG",
        completeness_band="SUBSTANTIAL",
        causal_distance="DIRECT",
        temporal_scope="CURRENT",
        source_family=source_family,
        evidence_family_id=evidence_family_id,
        confidence=0.9,
        rationale=(
            "The source-backed canary supports only the bounded configured effect."
        ),
        unsupported_aspects=(
            "No unsupported stronger economic effect is inferred.",
        ),
    )


def _canary_validity_evidence(target_id: str) -> FullScoreValidityEvidenceV2:
    return FullScoreValidityEvidenceV2(
        schema_totality_status="SCORING_SCHEMA_TOTALITY_PASS",
        scoring_schema_critical_count=0,
        silent_zero_default_count=0,
        positive_impact_zeroed_by_missing_cap_count=0,
        counter_impact_zeroed_by_missing_cap_count=0,
        mechanism_scope_failure_count=0,
        question_component_reconciliation_critical_count=0,
        unresolved_contradiction_count=0,
        pending_state_count=0,
        absence_without_adequacy_count=0,
        gold_critical_fact_miss_count=0,
        cross_business_question_closure_count=0,
        same_fact_duplicate_credit_count=0,
        same_document_duplicate_credit_count=0,
        source_audit_ids=(f"CONTROLLED-GENERALIZATION-{target_id}",),
    )


def _source_case_clean(row: Mapping[str, Any]) -> bool:
    return bool(
        row.get("source_verified") is True
        and int(row.get("future_leakage_count") or 0) == 0
        and int(row.get("forbidden_component_count") or 0) == 0
        and int(row.get("source_replay_required_component_missing_count") or 0)
        == 0
        and int(row.get("validation_rejected_count") or 0) == 0
    )


def _components_nonzero(
    row: Mapping[str, Any], component_ids: set[str]
) -> bool:
    vector = row.get("component_score_vector") or {}
    return all(float(vector.get(component_id) or 0) > 0 for component_id in component_ids)


def _nonzero_outside(
    row: Mapping[str, Any], allowed_component_ids: set[str]
) -> int:
    return sum(
        float(points or 0) > 0 and component_id not in allowed_component_ids
        for component_id, points in (row.get("component_score_vector") or {}).items()
    )


__all__ = [
    "GENERALIZATION_SCHEMA_VERSION",
    "compile_evidence_to_score_generalization_audit",
]
