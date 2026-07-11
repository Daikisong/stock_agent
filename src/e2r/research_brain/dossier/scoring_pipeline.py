"""Compile an organic dossier through impact, component score, and StageCourt."""

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl, write_text
from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    compile_evidence_impact_rubrics,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.scoring import (
    AtomicStageCourtV2,
    ClaimImpactLedgerBuilder,
    ComponentAssessmentBuilder,
    EvidenceImpactAdjudicator,
    ImpactValidator,
    ResearchCalibratedComponentScorer,
    SemanticClosureReconciler,
    compile_claim_eligibility_decisions,
    compile_question_component_subcriteria,
    compile_question_closures_v2,
    load_question_impact_contracts,
)
from e2r.research_brain.scoring.claim_impact_ledger import ClaimImpactProposal
from e2r.research_brain.scoring.business_mechanism_scope import (
    infer_business_mechanism_scope,
)


COMPONENT_QUESTION_FAMILIES = {
    "eps_fcf_explosion": (
        "revenue_operating_profit_conversion",
        "margin_fcf_conversion",
        "hbm_ai_memory_revenue_mix",
    ),
    "earnings_visibility": (
        "current_customer_allocation_commitment",
        "capacity_constraint_presold_status",
        "medium_term_revision_consensus",
    ),
    "bottleneck_pricing": (
        "capacity_constraint_presold_status",
        "asp_pricing_actual",
        "capex_supply_oversupply",
    ),
    "market_mispricing": ("medium_term_revision_consensus",),
    "valuation_rerating": ("medium_term_revision_consensus",),
    "capital_allocation": ("margin_fcf_conversion", "capex_supply_oversupply"),
    "information_confidence": (
        "shipment_mass_production_generation",
        "qualification_pass_lag_reopen",
        "customer_concentration_dependency",
    ),
}


def run_dossier_scoring_pipeline(
    *,
    dossier_root: str | Path,
    target_id: str,
    company_name: str,
    as_of_date: str,
    archetype_id: str,
    impact_provider: Any,
    max_claims: int | None = None,
    reuse_proposals: bool = False,
    retry_failed_only: bool = False,
    retry_claim_ids: Sequence[str] = (),
) -> Mapping[str, Any]:
    root = Path(dossier_root)
    claims = _read_jsonl(root / "accepted_current_claims.jsonl")
    provenance = _read_jsonl(root / "claim_provenance.jsonl")
    mappings = _read_jsonl(root / "primitive_mappings.jsonl")
    closures = _read_jsonl(root / "question_closure.jsonl")
    search_adequacy = _read_jsonl(root / "evidence_search_adequacy.jsonl")
    documents = _read_jsonl(root / "evidence_documents.jsonl")
    if not claims or not provenance or not mappings:
        raise ValueError("dossier scoring requires organic claim, provenance, and mapping leaves")
    if any(row.get("evidence_origin") != "ORGANIC_LIVE" for row in claims):
        raise ValueError("dossier scoring refuses non-organic accepted claims")
    if max_claims is not None and max_claims <= 0:
        raise ValueError("max_claims must be positive when configured")
    selected_claims = tuple(claims[:max_claims] if max_claims else claims)
    provenance_by_claim = {
        str(row.get("claim_id") or ""): row for row in provenance
    }
    document_by_id = {
        str(row.get("document_id") or ""): row for row in documents
    }
    mappings_by_claim: dict[str, list[Mapping[str, Any]]] = {}
    for row in mappings:
        if row.get("accepted_by_evidence_os") is True:
            mappings_by_claim.setdefault(str(row.get("claim_id") or ""), []).append(row)
    contract = load_archetype_scoring_contract(archetype_id)
    rubrics = compile_evidence_impact_rubrics(archetype_id)
    eligibility_decisions = tuple(
        decision.to_dict()
        for decision in compile_claim_eligibility_decisions(
            claims=selected_claims,
            claim_provenance=tuple(
                provenance_by_claim[str(row.get("claim_id") or "")]
                for row in selected_claims
            ),
            archetype_id=archetype_id,
        )
    )
    question_contracts = {
        question_id: question_contract
        for question_id, question_contract in load_question_impact_contracts().items()
        if question_contract.archetype_id == archetype_id
    }
    eligibility_by_claim = {
        str(row.get("claim_id") or ""): row
        for row in eligibility_decisions
    }
    adjudication_rows: list[Mapping[str, Any]] = []
    proposals: list[ClaimImpactProposal] = []
    invalid_proposal_count = 0
    retry_ids = {str(value) for value in retry_claim_ids if str(value).strip()}
    if sum((bool(reuse_proposals), bool(retry_failed_only), bool(retry_ids))) > 1:
        raise ValueError("proposal reuse and retry modes are mutually exclusive")
    claims_to_adjudicate: Sequence[Mapping[str, Any]] = selected_claims
    if retry_failed_only or retry_ids:
        prior_adjudications = _read_jsonl(root / "impact_adjudications.jsonl")
        prior_proposal_rows = _read_jsonl(root / "claim_impacts_proposed.jsonl")
        if not prior_adjudications:
            raise ValueError("claim retry requires prior impact adjudications")
        failed_claim_ids = retry_ids or {
                str(row.get("claim_id") or "")
                for row in prior_adjudications
                if row.get("status") != "IMPACT_ADJUDICATION_PASS"
            }
        known_claim_ids = {str(row.get("claim_id") or "") for row in selected_claims}
        unknown_retry_ids = failed_claim_ids - known_claim_ids
        if unknown_retry_ids:
            raise ValueError(f"retry claim ids are unknown: {sorted(unknown_retry_ids)}")
        adjudication_rows = [
            row
            for row in prior_adjudications
            if str(row.get("claim_id") or "") not in failed_claim_ids
        ]
        proposals = [
            _proposal_from_row(row)
            for row in prior_proposal_rows
            if str(row.get("claim_id") or "") not in failed_claim_ids
        ]
        claims_to_adjudicate = tuple(
            row
            for row in selected_claims
            if str(row.get("claim_id") or "") in failed_claim_ids
        )
        if not claims_to_adjudicate:
            raise ValueError("claim retry found no matching adjudications")
    if reuse_proposals:
        proposals = [
            _proposal_from_row(row)
            for row in _read_jsonl(root / "claim_impacts_proposed.jsonl")
        ]
        adjudication_rows = list(_read_jsonl(root / "impact_adjudications.jsonl"))
    prior_by_claim = {
        str(row.get("claim_id") or ""): row
        for row in _read_jsonl(root / "impact_adjudications.jsonl")
    }
    for claim in (() if reuse_proposals else claims_to_adjudicate):
        claim_id = str(claim.get("claim_id") or "")
        claim_mappings = tuple(mappings_by_claim.get(claim_id, ()))
        claim_provenance = provenance_by_claim.get(claim_id)
        if not claim_mappings or claim_provenance is None:
            raise ValueError("selected organic claim lacks accepted mapping or provenance")
        claim_primitive_ids = {
            str(row.get("primitive_id") or "") for row in claim_mappings
        }
        applicable_question_contracts = tuple(
            question_contract
            for question_contract in question_contracts.values()
            if claim_primitive_ids.intersection(
                question_contract.allowed_primitive_ids
            )
        )
        if not applicable_question_contracts:
            adjudication_rows.append(
                {
                    "claim_id": claim_id,
                    "status": "IMPACT_MAPPING_REJECTED",
                    "accepted_mapping_ids": [
                        row.get("mapping_id") for row in claim_mappings
                    ],
                    "valid_proposal_ids": [],
                    "invalid_proposal_count": 0,
                    "unsupported_aspects": [
                        "No QuestionImpactContract permits the mapped primitive."
                    ],
                    "counter_thesis": [],
                    "review_issues": ["NO_APPLICABLE_QUESTION_CONTRACT"],
                    "prompt_hashes": [],
                    "response_hashes": [],
                    "audit": {
                        "provider_call_count": 0,
                        "critical_count_sum": 0,
                    },
                }
            )
            continue
        enriched_claim = {
            **dict(claim),
            "accepted_mappings": [
                {
                    "mapping_id": row.get("mapping_id"),
                    "primitive_id": row.get("primitive_id"),
                    "support_direction": row.get("support_direction"),
                }
                for row in claim_mappings
            ],
        }
        if retry_failed_only or retry_ids:
            prior = prior_by_claim.get(claim_id) or {}
            enriched_claim["adjudication_retry_context"] = {
                "prior_status": prior.get("status"),
                "prior_review_issues": list(prior.get("review_issues") or ()),
                "prior_unsupported_aspects": list(
                    prior.get("unsupported_aspects") or ()
                ),
                "instruction": (
                    "Re-evaluate the exact accepted mapping against the supplied rubric. "
                    "Preserve a bounded PARTIAL impact when its partial predicate is "
                    "directly supported; do not promote unsupported stronger effects."
                ),
            }
        document = document_by_id.get(str(claim_provenance.get("document_id") or ""), {})
        result = EvidenceImpactAdjudicator(impact_provider).adjudicate(
            target_identity={"target_id": target_id, "company_name": company_name},
            as_of_date=as_of_date,
            archetype_id=archetype_id,
            accepted_claim=enriched_claim,
            exact_quote=str(claim_provenance.get("exact_quote") or ""),
            document_metadata={
                "document_id": claim_provenance.get("document_id"),
                "source_url": claim_provenance.get("source_url"),
                "published_date": claim_provenance.get("published_date"),
                "source_family": _source_family(document),
                "evidence_origin": "ORGANIC_LIVE",
            },
            current_claim_ledger=selected_claims,
            counter_claims=tuple(
                row
                for row in selected_claims
                if str(row.get("claim_id") or "") != claim_id
                and str(row.get("polarity") or "").upper()
                in {"NEGATIVE", "CONDITIONAL", "COUNTER"}
            ),
            rubrics=rubrics.rubrics,
            allowed_component_ids=tuple(contract.component_weights),
            business_mechanism_scope=infer_business_mechanism_scope(
                claim,
                primitive_id=sorted(claim_primitive_ids)[0],
                archetype_id=archetype_id,
            ),
            question_impact_contracts=applicable_question_contracts,
            claim_eligibility_decision=eligibility_by_claim[claim_id],
            component_subcriteria=compile_question_component_subcriteria(
                applicable_question_contracts,
                allowed_component_ids=tuple(contract.component_weights),
            ),
        )
        mapping_pairs = {
            (str(row.get("mapping_id") or ""), str(row.get("primitive_id") or ""))
            for row in claim_mappings
        }
        valid = tuple(
            proposal
            for proposal in result.proposals
            if (proposal.mapping_id, proposal.primitive_id) in mapping_pairs
        )
        invalid = len(result.proposals) - len(valid)
        invalid_proposal_count += invalid
        proposals.extend(valid)
        adjudication_rows.append(
            {
                "claim_id": claim_id,
                "status": result.status,
                "accepted_mapping_ids": [row.get("mapping_id") for row in claim_mappings],
                "valid_proposal_ids": [row.impact_id for row in valid],
                "invalid_proposal_count": invalid,
                "unsupported_aspects": list(result.unsupported_aspects),
                "counter_thesis": list(result.counter_thesis),
                "review_issues": list(result.review_issues),
                "prompt_hashes": list(result.prompt_hashes),
                "response_hashes": list(result.response_hashes),
                "audit": dict(result.audit),
            }
        )
    proposals, suppressed_duplicates = _dedupe_economic_proposals(proposals)
    satisfaction = _impact_satisfaction_rows(
        selected_claims=selected_claims,
        mappings_by_claim=mappings_by_claim,
        proposals=proposals,
    )
    ledger = ClaimImpactLedgerBuilder().build(
        proposals=proposals,
        accepted_current_claims=selected_claims,
        claim_provenance=tuple(
            provenance_by_claim[str(row.get("claim_id") or "")]
            for row in selected_claims
        ),
        source_task_satisfaction=satisfaction,
        claim_eligibility_decisions=eligibility_decisions,
    )
    validation = ImpactValidator().validate(
        impacts=ledger.validated_impacts,
        claim_provenance=tuple(
            provenance_by_claim[str(row.get("claim_id") or "")]
            for row in selected_claims
        ),
        claim_eligibility_decisions=ledger.claim_eligibility_decisions,
        accepted_current_claims=selected_claims,
    )
    closures_v2 = (
        compile_question_closures_v2(
            contracts=question_contracts,
            claims=selected_claims,
            primitive_mappings=mappings,
            eligibility_decisions=ledger.claim_eligibility_decisions,
            prior_closures=closures,
            validated_impacts=validation.impacts,
        )
        if question_contracts
        else tuple(closures)
    )
    rejected_impacts = tuple(
        (*ledger.rejected_impacts, *validation.rejected)
    )
    preliminary_reconciliation = SemanticClosureReconciler().reconcile(
        contracts=question_contracts,
        question_closures=closures_v2,
        claims=selected_claims,
        primitive_mappings=mappings,
        eligibility_decisions=ledger.claim_eligibility_decisions,
        proposed_impacts=proposals,
        validated_impacts=validation.impacts,
        rejected_impacts=rejected_impacts,
        adjudications=adjudication_rows,
        search_adequacy=search_adequacy,
    )
    terminal_evidence = _terminal_component_evidence(
        contract_components=tuple(contract.component_weights),
        impacts=validation.impacts,
        question_closures=preliminary_reconciliation.question_closures,
    )
    assessment = ComponentAssessmentBuilder().build(
        contract=contract,
        impacts=validation.impacts,
        terminal_evidence=terminal_evidence,
    )
    reconciliation = SemanticClosureReconciler().reconcile(
        contracts=question_contracts,
        question_closures=closures_v2,
        claims=selected_claims,
        primitive_mappings=mappings,
        eligibility_decisions=ledger.claim_eligibility_decisions,
        proposed_impacts=proposals,
        validated_impacts=validation.impacts,
        component_assessments=assessment.assessments,
        rejected_impacts=rejected_impacts,
        adjudications=adjudication_rows,
        search_adequacy=search_adequacy,
    )
    score = ResearchCalibratedComponentScorer().score(
        contract=contract,
        impacts=validation.impacts,
        assessments=assessment.assessments,
    )
    decision = AtomicStageCourtV2().decide(
        target_id=target_id,
        as_of_date=as_of_date,
        contract=contract,
        score=score,
        assessments=assessment.assessments,
        impacts=validation.impacts,
        accepted_claim_ids=tuple(
            str(row.get("claim_id") or "") for row in selected_claims
        ),
        claim_eligibility_decisions=ledger.claim_eligibility_decisions,
    )
    adjudication_failure_count = sum(
        row["status"]
        not in {"IMPACT_ADJUDICATION_PASS", "IMPACT_MAPPING_REJECTED"}
        for row in adjudication_rows
    )
    proposal_mapping_ids = {
        mapping_id
        for proposal in proposals
        for mapping_id in (proposal.mapping_id, *proposal.lineage_mapping_ids)
    }
    explicitly_rejected_mapping_ids = {
        str(mapping_id)
        for row in adjudication_rows
        if row.get("status") == "IMPACT_MAPPING_REJECTED"
        for mapping_id in row.get("accepted_mapping_ids") or ()
    }
    implicitly_rejected_mapping_ids = {
        str(mapping_id)
        for row in adjudication_rows
        if row.get("status") == "IMPACT_ADJUDICATION_PASS"
        for mapping_id in row.get("accepted_mapping_ids") or ()
        if str(mapping_id) not in proposal_mapping_ids
    }
    rejected_mapping_ids = (
        explicitly_rejected_mapping_ids | implicitly_rejected_mapping_ids
    )
    accepted_mapping_ids = {
        str(row.get("mapping_id") or "")
        for claim_id in {
            str(row.get("claim_id") or "") for row in selected_claims
        }
        for row in mappings_by_claim.get(claim_id, ())
    }
    effective_mapping_ids = accepted_mapping_ids - rejected_mapping_ids
    impact_mapping_ids = {
        mapping_id
        for impact in validation.impacts
        for mapping_id in (impact.mapping_id, *impact.lineage_mapping_ids)
    }
    critical = {
        "impact_adjudication_failure_count": adjudication_failure_count,
        "invalid_provider_proposal_count": invalid_proposal_count,
        "semantic_proposal_contract_missing_count": sum(
            not proposal.question_family_id
            or not proposal.question_contract_hash
            or not proposal.component_subcriterion_id
            or proposal.mechanism_scope_match is None
            for proposal in proposals
        ),
        "accepted_mapping_without_validated_impact_count": len(
            effective_mapping_ids - impact_mapping_ids
        ),
        "claim_impact_ledger_critical_count": int(
            ledger.audit.get("critical_count_sum") or 0
        ),
        "impact_validation_critical_count": int(
            validation.audit.get("critical_count_sum") or 0
        ),
        "component_assessment_critical_count": int(
            assessment.audit.get("critical_count_sum") or 0
        ),
        "question_component_reconciliation_critical_count": int(
            reconciliation.audit.get("critical_count_sum") or 0
        ),
        "score_audit_critical_count": int(score.audit.get("critical_count_sum") or 0),
        "probe_contamination_count": sum(
            row.get("evidence_origin") == "CONTROLLED_CLAIM_PROBE"
            for row in selected_claims
        ),
    }
    audit = {
        "schema_version": "e2r_organic_dossier_scoring_pipeline_v2",
        "status": (
            "ORGANIC_DOSSIER_FULL_SCORE_PASS"
            if sum(critical.values()) == 0 and score.full_score_valid
            else "ORGANIC_DOSSIER_SCORING_PENDING"
        ),
        "target_id": target_id,
        "as_of_date": as_of_date,
        "archetype_id": archetype_id,
        "organic_accepted_claim_count": len(selected_claims),
        "accepted_mapping_count": len(accepted_mapping_ids),
        "impact_rejected_mapping_count": len(rejected_mapping_ids),
        "effective_accepted_mapping_count": len(effective_mapping_ids),
        "impact_proposal_count": len(proposals),
        "suppressed_duplicate_economic_proposal_count": suppressed_duplicates,
        "validated_impact_count": len(validation.impacts),
        "supported_component_count": sum(
            bool(row.support_impact_ids) for row in assessment.assessments
        ),
        "terminal_component_count": len(assessment.assessments)
        - len(assessment.material_nonterminal_components),
        "verified_supported_score": score.verified_supported_score,
        "full_score_valid": score.full_score_valid,
        "score_type": score.score_type,
        "canonical_stage": decision.canonical_stage,
        "decision_status": decision.decision_status,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }
    _write_pipeline_leaves(
        root=root,
        adjudications=adjudication_rows,
        proposals=proposals,
        ledger=ledger,
        validation=validation,
        assessment=assessment,
        score=score,
        decision=decision,
        audit=audit,
        question_closures_v2=closures_v2,
        reconciliation=reconciliation,
    )
    return audit


def _terminal_component_evidence(
    *,
    contract_components: Sequence[str],
    impacts: Sequence[Any],
    question_closures: Sequence[Mapping[str, Any]],
) -> Mapping[str, Mapping[str, Any]]:
    supported = {impact.component_id for impact in impacts if impact.validated_credit_fraction > 0}
    closure_by_family = {
        str(row.get("question_family_id") or ""): row for row in question_closures
    }
    result: dict[str, Mapping[str, Any]] = {}
    for component_id in contract_components:
        if component_id in supported:
            continue
        families = tuple(
            str(row.get("question_family_id") or "")
            for row in question_closures
            if component_id in set(row.get("allowed_component_ids") or ())
        ) or COMPONENT_QUESTION_FAMILIES[component_id]
        rows = tuple(
            closure_by_family[family]
            for family in families
            if family in closure_by_family
        )
        exhaustion = tuple(
            str(proof)
            for row in rows
            for proof in row.get("search_exhaustion_proof") or ()
        )
        investigated_statuses = {
            "COUNTER_SUPPORTED",
            "EVALUATED_ABSENT",
            "SUPPORTED_NON_SCORING",
        }
        investigated_proof = tuple(
            str(claim_id)
            for row in rows
            for claim_id in (
                *(row.get("supporting_claim_ids") or ()),
                *(row.get("counter_claim_ids") or ()),
            )
        )
        component_resolved = all(
            row.get("status") in investigated_statuses
            or (
                row.get("status")
                in {"SUPPORTED_SCORING", "PARTIALLY_SUPPORTED_SCORING"}
                and component_id
                not in set(row.get("reconciled_component_ids") or ())
                and row.get("reconciliation_search_adequate") is True
            )
            for row in rows
        )
        if rows and component_resolved and (exhaustion or investigated_proof):
            result[component_id] = {
                "status": "VERIFIED_ABSENT_AFTER_SEARCH",
                "search_exhaustion_proof": tuple(
                    dict.fromkeys((*exhaustion, *investigated_proof))
                ),
                "confidence": 0.7,
            }
        else:
            pending_statuses = {str(row.get("status") or "") for row in rows}
            status = (
                "PROVIDER_PENDING"
                if "PROVIDER_PENDING" in pending_statuses or not rows
                else "SOURCE_PENDING"
            )
            result[component_id] = {
                "status": status,
                "missing_questions": families,
                "confidence": 0.0,
            }
    return result


def _impact_satisfaction_rows(
    *,
    selected_claims: Sequence[Mapping[str, Any]],
    mappings_by_claim: Mapping[str, Sequence[Mapping[str, Any]]],
    proposals: Sequence[Any],
) -> tuple[Mapping[str, Any], ...]:
    proposal_mapping_ids = {proposal.mapping_id for proposal in proposals}
    rows = []
    for claim in selected_claims:
        claim_id = str(claim.get("claim_id") or "")
        mapping_ids = tuple(
            str(row.get("mapping_id") or "")
            for row in mappings_by_claim.get(claim_id, ())
        )
        rows.append(
            {
                "status": "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN",
                "claim_id": claim_id,
                "rerouted_mapping_ids": [
                    value for value in mapping_ids if value in proposal_mapping_ids
                ],
                "mapping_ids_without_impact": [
                    value for value in mapping_ids if value not in proposal_mapping_ids
                ],
                "original_gap_open": True,
            }
        )
    return tuple(rows)


def _write_pipeline_leaves(
    *, root: Path, adjudications, proposals, ledger, validation, assessment, score, decision, audit, question_closures_v2, reconciliation
) -> None:
    write_jsonl(root / "impact_adjudications.jsonl", adjudications)
    proposal_mapping_ids = {
        mapping_id
        for proposal in proposals
        for mapping_id in (proposal.mapping_id, *proposal.lineage_mapping_ids)
    }
    write_jsonl(
        root / "impact_mapping_dispositions.jsonl",
        (
            {
                "claim_id": row.get("claim_id"),
                "mapping_id": mapping_id,
                "status": (
                    "IMPACT_MAPPING_REJECTED_NO_BOUNDED_EFFECT"
                    if row.get("status") == "IMPACT_ADJUDICATION_PASS"
                    and str(mapping_id) not in proposal_mapping_ids
                    else row.get("status")
                ),
                "review_issues": list(row.get("review_issues") or ()),
            }
            for row in adjudications
            for mapping_id in row.get("accepted_mapping_ids") or ()
        ),
    )
    write_jsonl(root / "claim_impacts_proposed.jsonl", (row.to_dict() for row in proposals))
    write_jsonl(
        root / "claim_eligibility_decisions.jsonl",
        ledger.claim_eligibility_decisions,
    )
    write_jsonl(
        root / "question_closure_v2_pre_reconciliation.jsonl",
        question_closures_v2,
    )
    write_jsonl(
        root / "question_closure_v2.jsonl",
        reconciliation.question_closures,
    )
    write_jsonl(
        root / "question_component_reconciliation.jsonl",
        (row.to_dict() for row in reconciliation.reconciliations),
    )
    write_jsonl(
        root / "claim_impact_ledger.jsonl",
        (row.to_dict() for row in ledger.validated_impacts),
    )
    write_jsonl(
        root / "claim_impacts_validated.jsonl",
        (row.to_dict() for row in validation.impacts),
    )
    write_jsonl(
        root / "economic_fact_clusters.jsonl",
        (row.to_dict() for row in validation.economic_fact_clusters),
    )
    write_jsonl(
        root / "document_clusters.jsonl",
        (row.to_dict() for row in validation.document_clusters),
    )
    write_jsonl(
        root / "component_assessments.jsonl",
        (row.to_dict() for row in assessment.assessments),
    )
    write_jsonl(
        root / "component_subcriteria.jsonl",
        (row.to_dict() for row in assessment.subcriterion_scores),
    )
    score_payload = {**score.to_dict(), "archetype_id": audit["archetype_id"]}
    write_json(root / "component_score_vector.json", score_payload)
    write_json(
        root / "score_interval.json",
        {
            "target_id": audit["target_id"],
            "verified_supported_score": score.verified_supported_score,
            "provisional_score_lower": score.provisional_score_lower,
            "provisional_score_upper": score.provisional_score_upper,
            "full_e2r_score": score.full_e2r_score,
            "full_score_valid": score.full_score_valid,
        },
    )
    write_json(root / "atomic_stage_decision.json", decision.to_dict())
    write_json(
        root / "stagecourt_trace.json",
        {
            "trace_id": decision.trace_id,
            "decision_id": decision.decision_id,
            "target_id": decision.target_id,
            "as_of_date": decision.as_of_date,
            "accepted_claim_ids": list(decision.accepted_claim_ids),
            "stage_event_claim_ids": list(decision.stage_event_claim_ids),
            "claim_impact_ids": list(decision.claim_impact_ids),
            "component_assessment_ids": list(decision.component_assessment_ids),
        },
    )
    write_json(root / "scoring_audit_summary.json", audit)
    write_json(root / "claim_impact_ledger_audit.json", ledger.audit)
    write_json(root / "impact_validation_audit.json", validation.audit)
    write_json(root / "component_assessment_audit.json", assessment.audit)
    write_json(
        root / "question_component_reconciliation_audit.json",
        reconciliation.audit,
    )
    write_json(root / "component_score_audit.json", score.audit)
    write_text(
        root / "operator_digest.md",
        "\n".join(
            (
                f"# E2R Dossier — {audit['target_id']}",
                "",
                f"- status: {audit['status']}",
                f"- organic claims: {audit['organic_accepted_claim_count']}",
                f"- validated impacts: {audit['validated_impact_count']}",
                f"- verified supported score: {audit['verified_supported_score']}",
                f"- score type: {audit['score_type']}",
                f"- Stage: {audit['canonical_stage']} ({audit['decision_status']})",
                "- investment recommendation emitted: false",
                "",
            )
        ),
    )


def _source_family(document: Mapping[str, Any]) -> str:
    source_class = str(document.get("source_class") or "")
    if source_class in {"DART", "KIND"}:
        return "OFFICIAL_FILING"
    if source_class in {"IssuerIR", "IssuerNewsroom"}:
        return "ISSUER_OFFICIAL"
    if source_class == "CompanyGuide":
        return "TRUSTED_INDEPENDENT"
    return "TRUSTED_INDEPENDENT"


def _proposal_from_row(row: Mapping[str, Any]) -> ClaimImpactProposal:
    payload = dict(row)
    payload["unsupported_aspects"] = tuple(payload.get("unsupported_aspects") or ())
    payload["counter_claim_ids"] = tuple(payload.get("counter_claim_ids") or ())
    payload["lineage_mapping_ids"] = tuple(payload.get("lineage_mapping_ids") or ())
    return ClaimImpactProposal(**payload)


def _dedupe_economic_proposals(
    proposals: Sequence[ClaimImpactProposal],
) -> tuple[list[ClaimImpactProposal], int]:
    seen: dict[tuple[str, str, str, str], int] = {}
    result: list[ClaimImpactProposal] = []
    suppressed = 0
    for proposal in proposals:
        key = (
            proposal.claim_id,
            proposal.component_id,
            proposal.direction,
            proposal.evidence_family_id,
        )
        if key in seen:
            index = seen[key]
            existing = result[index]
            lineage = tuple(
                dict.fromkeys(
                    (
                        *existing.lineage_mapping_ids,
                        proposal.mapping_id,
                        *proposal.lineage_mapping_ids,
                    )
                )
            )
            result[index] = replace(existing, lineage_mapping_ids=lineage)
            suppressed += 1
            continue
        seen[key] = len(result)
        result.append(proposal)
    return result, suppressed


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = ["COMPONENT_QUESTION_FAMILIES", "run_dossier_scoring_pipeline"]
