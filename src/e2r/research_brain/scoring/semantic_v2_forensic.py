"""52f09f3 frozen dossier의 semantic-scoring v2 결함 기준선 감사."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_text
from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    compile_evidence_impact_rubrics,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .claim_impact_ledger import SUPPORT_TYPES


SCHEMA_VERSION = "e2r_semantic_scoring_v2_forensic_baseline_v1"
ARCHETYPE_ID = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
TARGETS = ("005930", "000660")

QUESTION_COMPONENTS = {
    "current_customer_allocation_commitment": (
        "earnings_visibility",
        "bottleneck_pricing",
    ),
    "capacity_constraint_presold_status": (
        "earnings_visibility",
        "bottleneck_pricing",
    ),
    "qualification_pass_lag_reopen": (
        "earnings_visibility",
        "information_confidence",
    ),
    "shipment_mass_production_generation": (
        "earnings_visibility",
        "information_confidence",
    ),
    "hbm_ai_memory_revenue_mix": (
        "earnings_visibility",
        "eps_fcf_explosion",
    ),
    "asp_pricing_actual": ("bottleneck_pricing", "eps_fcf_explosion"),
    "revenue_operating_profit_conversion": (
        "eps_fcf_explosion",
        "information_confidence",
    ),
    "margin_fcf_conversion": ("eps_fcf_explosion",),
    "medium_term_revision_consensus": (
        "earnings_visibility",
        "market_mispricing",
    ),
    "conventional_memory_drag": (
        "eps_fcf_explosion",
        "earnings_visibility",
    ),
    "capex_supply_oversupply": (
        "capital_allocation",
        "bottleneck_pricing",
    ),
    "customer_concentration_dependency": (
        "earnings_visibility",
        "information_confidence",
    ),
}


def compile_semantic_scoring_v2_forensic_baseline(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    contract = load_archetype_scoring_contract(ARCHETYPE_ID)
    rubric_catalog = compile_evidence_impact_rubrics(ARCHETYPE_ID)
    cap_support_types = set(
        next(iter(rubric_catalog.rubrics)).actual_vs_forward_rules
        if rubric_catalog.rubrics
        else ()
    )
    declared_support_types = set(SUPPORT_TYPES)

    positive_zero_rows: list[Mapping[str, Any]] = []
    counter_zero_rows: list[Mapping[str, Any]] = []
    question_absence_rows: list[Mapping[str, Any]] = []
    mechanism_failure_rows: list[Mapping[str, Any]] = []
    document_duplicate_groups: list[Mapping[str, Any]] = []
    fact_duplicate_groups: list[Mapping[str, Any]] = []
    counter_failure_rows: list[Mapping[str, Any]] = []
    event_injection_rows: list[Mapping[str, Any]] = []
    eligibility_contradiction_rows: list[Mapping[str, Any]] = []
    observed_source_families: set[str] = set()
    observed_temporal_scopes: set[str] = set()
    leaf_paths: list[Path] = []

    for target_id in TARGETS:
        dossier = (
            root
            / "output/evidence_to_score/c06/2026-07-11"
            / target_id
        )
        paths = {
            name: dossier / name
            for name in (
                "accepted_current_claims.jsonl",
                "claim_provenance.jsonl",
                "claim_impact_ledger.jsonl",
                "claim_impacts_validated.jsonl",
                "component_assessments.jsonl",
                "question_closure.jsonl",
                "atomic_stage_decision.json",
            )
        }
        leaf_paths.extend(paths.values())
        claims = _jsonl(paths["accepted_current_claims.jsonl"])
        claim_by_id = {str(row["claim_id"]): row for row in claims}
        provenance = {
            str(row["claim_id"]): row
            for row in _jsonl(paths["claim_provenance.jsonl"])
        }
        ledger = _jsonl(paths["claim_impact_ledger.jsonl"])
        impacts = _jsonl(paths["claim_impacts_validated.jsonl"])
        assessments = {
            str(row["component_id"]): row
            for row in _jsonl(paths["component_assessments.jsonl"])
        }
        questions = _jsonl(paths["question_closure.jsonl"])
        decision = _json(paths["atomic_stage_decision.json"])

        for row in ledger:
            observed_source_families.add(str(row.get("source_family") or ""))
            observed_temporal_scopes.add(str(row.get("temporal_scope") or ""))

        for row in impacts:
            if (
                float(row.get("validated_credit_fraction") or 0.0) == 0.0
                and float(row.get("support_type_cap") or 0.0) == 0.0
                and str(row.get("support_type") or _ledger_support_type(ledger, row))
                not in cap_support_types
            ):
                target = (
                    counter_zero_rows
                    if row.get("direction") == "COUNTER"
                    else positive_zero_rows
                )
                target.append(
                    {
                        "target_id": target_id,
                        "impact_id": row["impact_id"],
                        "claim_id": row["claim_id"],
                        "primitive_id": row["primitive_id"],
                        "component_id": row["component_id"],
                        "direction": row["direction"],
                        "support_type": _ledger_support_type(ledger, row),
                        "support_type_cap": row["support_type_cap"],
                    }
                )

        for row in questions:
            status = str(row.get("status") or "")
            if status not in {"SUPPORTED", "PARTIALLY_SUPPORTED"}:
                continue
            for component_id in QUESTION_COMPONENTS.get(
                str(row.get("question_family_id") or ""), ()
            ):
                assessment = assessments.get(component_id, {})
                if assessment.get("status") != "VERIFIED_ABSENT_AFTER_SEARCH":
                    continue
                question_absence_rows.append(
                    {
                        "target_id": target_id,
                        "question_family_id": row["question_family_id"],
                        "question_status": status,
                        "component_id": component_id,
                        "component_status": assessment.get("status"),
                        "supporting_claim_ids": list(
                            row.get("supporting_claim_ids") or ()
                        ),
                    }
                )
            for claim_id in row.get("supporting_claim_ids") or ():
                claim = claim_by_id.get(str(claim_id))
                if claim is None:
                    continue
                reason = _c06_question_scope_failure(
                    str(row.get("question_family_id") or ""), claim
                )
                if reason:
                    mechanism_failure_rows.append(
                        {
                            "target_id": target_id,
                            "question_family_id": row["question_family_id"],
                            "question_status": status,
                            "claim_id": claim_id,
                            "failure_reason": reason,
                            "predicate": str(
                                (claim.get("raw_assertion") or {}).get("predicate")
                                or ""
                            ),
                            "exact_quote": str(claim.get("exact_quote") or ""),
                        }
                    )

        credited = [
            row
            for row in impacts
            if float(row.get("validated_credit_fraction") or 0.0) > 0.0
        ]
        by_document: dict[tuple[str, str, str], list[Mapping[str, Any]]] = (
            defaultdict(list)
        )
        by_fact: dict[tuple[str, str, str], list[Mapping[str, Any]]] = defaultdict(
            list
        )
        for row in credited:
            claim_id = str(row["claim_id"])
            prov = provenance[claim_id]
            by_document[
                (
                    str(prov["document_id"]),
                    str(row["component_id"]),
                    str(row["direction"]),
                )
            ].append(row)
            fact_key = _fact_key(claim_by_id[claim_id])
            by_fact[(fact_key, str(row["component_id"]), str(row["direction"]))].append(
                row
            )
        for (document_id, component_id, direction), rows in by_document.items():
            claim_ids = sorted({str(row["claim_id"]) for row in rows})
            if len(claim_ids) <= 1:
                continue
            document_duplicate_groups.append(
                {
                    "target_id": target_id,
                    "document_id": document_id,
                    "component_id": component_id,
                    "direction": direction,
                    "claim_ids": claim_ids,
                    "duplicate_credit_excess": len(claim_ids) - 1,
                }
            )
        for (fact_key, component_id, direction), rows in by_fact.items():
            claim_ids = sorted({str(row["claim_id"]) for row in rows})
            if len(claim_ids) <= 1:
                continue
            fact_duplicate_groups.append(
                {
                    "target_id": target_id,
                    "fact_key": fact_key,
                    "component_id": component_id,
                    "direction": direction,
                    "claim_ids": claim_ids,
                    "duplicate_credit_excess": len(claim_ids) - 1,
                }
            )

        zeroed_counter_ids = {
            str(row["impact_id"])
            for row in counter_zero_rows
            if row["target_id"] == target_id
        }
        for assessment in assessments.values():
            ledger_counter_ids = {
                str(row["impact_id"])
                for row in ledger
                if row.get("component_id") == assessment["component_id"]
                and row.get("direction") == "COUNTER"
            }
            ignored = sorted(ledger_counter_ids & zeroed_counter_ids)
            if ignored:
                counter_failure_rows.append(
                    {
                        "target_id": target_id,
                        "component_id": assessment["component_id"],
                        "counter_impact_ids": ignored,
                        "component_counter_impact_ids": list(
                            assessment.get("counter_impact_ids") or ()
                        ),
                        "counter_effect": 0.0,
                        "component_status": assessment.get("status"),
                    }
                )

        if (
            decision.get("full_score_valid") is True
            and decision.get("accepted_claim_ids")
        ):
            event_injection_rows.append(
                {
                    "target_id": target_id,
                    "accepted_claim_count": len(decision["accepted_claim_ids"]),
                    "injected_company_event_score": 60.0,
                    "injected_high_quality_company_event": True,
                    "canonical_stage": decision.get("canonical_stage"),
                }
            )
        for claim in claims:
            if (
                claim.get("current_score_eligible") is False
                and claim.get("scoring_readiness_eligible") is True
            ):
                eligibility_contradiction_rows.append(
                    {
                        "target_id": target_id,
                        "claim_id": claim["claim_id"],
                        "current_score_eligible": False,
                        "scoring_readiness_eligible": True,
                    }
                )

    missing_support_types = sorted(declared_support_types - cap_support_types)
    missing_source_families = sorted(
        observed_source_families - set(contract.source_tier_caps)
    )
    missing_temporal_scopes = sorted(
        observed_temporal_scopes - set(contract.freshness_caps)
    )
    supported_absent = [
        row for row in question_absence_rows if row["question_status"] == "SUPPORTED"
    ]
    partial_absent = [
        row
        for row in question_absence_rows
        if row["question_status"] == "PARTIALLY_SUPPORTED"
    ]
    metrics = {
        "declared_support_type_count": len(declared_support_types),
        "cap_table_support_type_count": len(cap_support_types),
        "missing_support_type_count": len(missing_support_types),
        "source_cap_missing_count": len(missing_source_families),
        "temporal_cap_missing_count": len(missing_temporal_scopes),
        "positive_proposal_zeroed_by_missing_cap_count": len(positive_zero_rows),
        "counter_proposal_zeroed_by_missing_cap_count": len(counter_zero_rows),
        "supported_question_absent_component_count": len(supported_absent),
        "partially_supported_question_absent_component_count": len(partial_absent),
        "cross_business_question_closure_count": len(mechanism_failure_rows),
        "same_document_duplicate_credit_group_count": len(
            document_duplicate_groups
        ),
        "same_document_duplicate_credit_count": sum(
            int(row["duplicate_credit_excess"])
            for row in document_duplicate_groups
        ),
        "same_fact_duplicate_credit_group_count": len(fact_duplicate_groups),
        "same_fact_duplicate_credit_count": sum(
            int(row["duplicate_credit_excess"]) for row in fact_duplicate_groups
        ),
        "support_counter_component_counter_effect_zero_count": len(
            counter_failure_rows
        ),
        "accepted_claim_event_score_injection_count": len(event_injection_rows),
        "eligibility_field_contradiction_count": len(
            eligibility_contradiction_rows
        ),
    }
    leaf_hashes = {
        str(path.relative_to(root)): _sha256(path) for path in leaf_paths
    }
    result = {
        "schema_version": SCHEMA_VERSION,
        "status": "SEMANTIC_SCORING_V2_FORENSIC_BASELINE_CAPTURED",
        "frozen_head": "52f09f3",
        "archetype_id": ARCHETYPE_ID,
        "target_ids": list(TARGETS),
        "metrics": metrics,
        "missing_support_types": missing_support_types,
        "missing_source_families": missing_source_families,
        "missing_temporal_scopes": missing_temporal_scopes,
        "positive_zero_rows": positive_zero_rows,
        "counter_zero_rows": counter_zero_rows,
        "question_absence_rows": question_absence_rows,
        "mechanism_failure_rows": mechanism_failure_rows,
        "document_duplicate_groups": document_duplicate_groups,
        "fact_duplicate_groups": fact_duplicate_groups,
        "counter_failure_rows": counter_failure_rows,
        "event_injection_rows": event_injection_rows,
        "eligibility_contradiction_rows": eligibility_contradiction_rows,
        "leaf_sha256": leaf_hashes,
        "baseline_hash": stable_hash(
            {
                "metrics": metrics,
                "leaf_sha256": leaf_hashes,
                "rows": {
                    "positive_zero": positive_zero_rows,
                    "counter_zero": counter_zero_rows,
                    "question_absence": question_absence_rows,
                    "mechanism": mechanism_failure_rows,
                },
            }
        ),
        "production_ready": False,
    }
    return result


def write_semantic_scoring_v2_forensic_baseline(
    audit: Mapping[str, Any], *, docs_root: str | Path
) -> Mapping[str, Path]:
    docs = Path(docs_root)
    paths = {
        "baseline": docs / "e2r_semantic_scoring_v2_forensic_baseline.md",
        "cap_matrix": docs / "e2r_support_type_cap_matrix_before.json",
        "question_consistency": docs
        / "e2r_question_component_consistency_before.json",
        "mechanism": docs
        / "e2r_business_mechanism_scope_failures_before.json",
        "counter": docs / "e2r_counter_credit_failures_before.json",
        "duplication": docs / "e2r_fact_duplication_before.json",
        "stage": docs / "e2r_stage_event_injection_before.json",
    }
    write_json(
        paths["cap_matrix"],
        {
            "schema_version": "e2r_support_type_cap_matrix_before_v1",
            "declared_support_types": sorted(SUPPORT_TYPES),
            "configured_support_types": sorted(
                set(SUPPORT_TYPES) - set(audit["missing_support_types"])
            ),
            "missing_support_types": audit["missing_support_types"],
            "positive_zero_rows": audit["positive_zero_rows"],
            "counter_zero_rows": audit["counter_zero_rows"],
            "metrics": {
                key: audit["metrics"][key]
                for key in (
                    "declared_support_type_count",
                    "cap_table_support_type_count",
                    "missing_support_type_count",
                    "source_cap_missing_count",
                    "temporal_cap_missing_count",
                    "positive_proposal_zeroed_by_missing_cap_count",
                    "counter_proposal_zeroed_by_missing_cap_count",
                )
            },
        },
    )
    write_json(
        paths["question_consistency"],
        {
            "schema_version": "e2r_question_component_consistency_before_v1",
            "rows": audit["question_absence_rows"],
            "supported_question_absent_component_count": audit["metrics"][
                "supported_question_absent_component_count"
            ],
            "partially_supported_question_absent_component_count": audit[
                "metrics"
            ]["partially_supported_question_absent_component_count"],
        },
    )
    write_json(
        paths["mechanism"],
        {
            "schema_version": "e2r_business_mechanism_scope_failures_before_v1",
            "cross_business_question_closure_count": audit["metrics"][
                "cross_business_question_closure_count"
            ],
            "rows": audit["mechanism_failure_rows"],
        },
    )
    write_json(
        paths["counter"],
        {
            "schema_version": "e2r_counter_credit_failures_before_v1",
            "counter_proposal_zeroed_by_missing_cap_count": audit["metrics"][
                "counter_proposal_zeroed_by_missing_cap_count"
            ],
            "support_counter_component_counter_effect_zero_count": audit["metrics"][
                "support_counter_component_counter_effect_zero_count"
            ],
            "zero_rows": audit["counter_zero_rows"],
            "component_rows": audit["counter_failure_rows"],
        },
    )
    write_json(
        paths["duplication"],
        {
            "schema_version": "e2r_fact_duplication_before_v1",
            "same_document_duplicate_credit_group_count": audit["metrics"][
                "same_document_duplicate_credit_group_count"
            ],
            "same_document_duplicate_credit_count": audit["metrics"][
                "same_document_duplicate_credit_count"
            ],
            "same_fact_duplicate_credit_group_count": audit["metrics"][
                "same_fact_duplicate_credit_group_count"
            ],
            "same_fact_duplicate_credit_count": audit["metrics"][
                "same_fact_duplicate_credit_count"
            ],
            "document_groups": audit["document_duplicate_groups"],
            "fact_groups": audit["fact_duplicate_groups"],
        },
    )
    write_json(
        paths["stage"],
        {
            "schema_version": "e2r_stage_event_injection_before_v1",
            "accepted_claim_event_score_injection_count": audit["metrics"][
                "accepted_claim_event_score_injection_count"
            ],
            "eligibility_field_contradiction_count": audit["metrics"][
                "eligibility_field_contradiction_count"
            ],
            "event_injection_rows": audit["event_injection_rows"],
            "eligibility_contradiction_rows": audit[
                "eligibility_contradiction_rows"
            ],
        },
    )
    write_text(paths["baseline"], _render_baseline(audit))
    return paths


def _render_baseline(audit: Mapping[str, Any]) -> str:
    metrics = audit["metrics"]
    lines = [
        "# E2R Semantic Scoring v2 Forensic Baseline",
        "",
        "- status: SEMANTIC_SCORING_V2_FORENSIC_BASELINE_CAPTURED",
        "- frozen input: 52f09f3 Samsung/Hynix dossier leaves",
        f"- baseline hash: {audit['baseline_hash']}",
        "- production ready: false",
        "",
        "## Measured defects",
        "",
    ]
    for key, value in metrics.items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        (
            "",
            "## 쉬운 예",
            "",
            "`PARTIAL_BRIDGE` impact는 proposal과 ledger에 존재하지만 cap table에 key가 없어 0점이 됐다. 이는 근거가 약해서 0점인 것이 아니라 lookup 계약이 빠진 내부 오류다.",
            "",
            "삼성 Tesla Foundry 위탁생산 계약은 삼성전자 claim 장부에는 남길 수 있지만, HBM 고객 배정 질문을 닫아서는 안 된다.",
            "",
            "## Exact baseline rows",
            "",
            f"- positive impacts silently zeroed: {len(audit['positive_zero_rows'])}",
            f"- counter impacts silently zeroed: {len(audit['counter_zero_rows'])}",
            f"- question/component contradictions: {len(audit['question_absence_rows'])}",
            f"- mechanism-scope failures: {len(audit['mechanism_failure_rows'])}",
            f"- same-document duplicate-credit groups: {len(audit['document_duplicate_groups'])}",
            f"- accepted-claim event injections: {len(audit['event_injection_rows'])}",
            f"- eligibility contradictions: {len(audit['eligibility_contradiction_rows'])}",
            "",
            "이 문서는 결함이 해결됐다는 PASS가 아니라, Phase 59+ 수리 전 결함을 같은 frozen corpus에서 재현한 기준선이다.",
            "",
        )
    )
    return "\n".join(lines)


def _ledger_support_type(
    ledger: Sequence[Mapping[str, Any]], impact: Mapping[str, Any]
) -> str:
    return next(
        (
            str(row.get("support_type") or "")
            for row in ledger
            if row.get("impact_id") == impact.get("impact_id")
        ),
        "",
    )


def _c06_question_scope_failure(
    question_family_id: str, claim: Mapping[str, Any]
) -> str:
    raw = claim.get("raw_assertion") or {}
    text = " ".join(
        str(value or "")
        for value in (
            raw.get("predicate"),
            raw.get("object_text"),
            claim.get("exact_quote"),
            claim.get("adjudication_rationale"),
        )
    ).lower()
    if any(token in text for token in ("foundry", "위탁생산")):
        return "WRONG_BUSINESS_SEGMENT_FOUNDRY"
    hbm = any(token in text for token in ("hbm", "ai memory", "ai메모리"))
    memory = hbm or any(
        token in text for token in ("memory", "dram", "메모리", "d램")
    )
    non_hbm_product = next(
        (
            token
            for token in ("nand", "socamm", "lpddr")
            if token in text and not hbm
        ),
        "",
    )
    if question_family_id in {
        "shipment_mass_production_generation",
        "hbm_ai_memory_revenue_mix",
    }:
        if non_hbm_product:
            return f"WRONG_PRODUCT_FAMILY_{non_hbm_product.upper()}"
        if not hbm:
            return "HBM_PRODUCT_SCOPE_MISSING"
    if question_family_id == "current_customer_allocation_commitment":
        if not memory:
            return "MEMORY_HBM_MECHANISM_MISSING"
        if not any(
            token in text
            for token in (
                "allocation",
                "commit",
                "booking",
                "preorder",
                "배정",
                "예약",
                "공급계약",
            )
        ):
            return "CUSTOMER_COMMITMENT_MECHANISM_MISSING"
    if question_family_id in {
        "capacity_constraint_presold_status",
        "revenue_operating_profit_conversion",
        "margin_fcf_conversion",
        "customer_concentration_dependency",
    } and not memory:
        return "C06_ECONOMIC_ATTRIBUTION_MISSING"
    if question_family_id == "capex_supply_oversupply" and not memory:
        return "MEMORY_CAPEX_ATTRIBUTION_MISSING"
    return ""


def _fact_key(claim: Mapping[str, Any]) -> str:
    raw = claim.get("raw_assertion") or {}
    text = "|".join(
        str(value or "")
        for value in (
            raw.get("subject_entity_id") or claim.get("subject_entity_id"),
            raw.get("predicate"),
            raw.get("object_text"),
            raw.get("event_date") or claim.get("event_date"),
            claim.get("effective_start"),
            claim.get("effective_end"),
        )
    ).casefold()
    return re.sub(r"[^0-9a-z가-힣|]+", " ", text).strip()


def _json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[Mapping[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _sha256(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


__all__ = [
    "SCHEMA_VERSION",
    "compile_semantic_scoring_v2_forensic_baseline",
    "write_semantic_scoring_v2_forensic_baseline",
]
