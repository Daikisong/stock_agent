"""Deterministic offline replays for the mandatory mechanism families."""

from __future__ import annotations

from copy import deepcopy
from datetime import date
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash
from ..research_contracts import load_research_contract, select_contract_bundle
from ..saturation import ResearchSaturationAdjudicator, compile_saturation_audit


MANDATORY_MECHANISM_FAMILIES = (
    "C01_BACKLOG_MARGIN",
    "C03_FRAMEWORK_VS_CONTRACT",
    "C06_HBM_CUSTOMER_CAPACITY",
    "C08_PROFILE_VS_ORDER_CONVERSION",
    "C12_BATTERY_CALL_OFF_RISK",
    "C15_PASS_THROUGH_INVENTORY_PHASE",
    "C17_REALIZED_CHEMICAL_SPREAD",
    "C21_ROE_PBR_CAPITAL_RETURN",
    "C24_BIO_DATA_BINARY_RISK",
    "C28_SOFTWARE_RETENTION",
    "C30_CONSTRUCTION_PF_LIFECYCLE",
    "C31_POLICY_HEADLINE_DIRECT_CASH",
    "R13_ACCOUNTING_WRONG_SUBJECT_OLD_RISK",
)


def build_mechanism_golden_dossier(
    case: Mapping[str, Any],
) -> tuple[Mapping[str, Any], tuple[str, ...]]:
    _validate_case(case)
    primary_id = str(case["primary_archetype_id"])
    focus_id = str(case.get("focus_contract_id") or primary_id)
    bundle = select_contract_bundle((primary_id,))
    if focus_id not in set(bundle.contract_ids):
        raise ValueError("golden focus contract is outside the selected bundle")
    as_of_date = str(case["as_of_date"])
    facts_by_direction: dict[str, list[dict[str, Any]]] = {
        "POSITIVE": [],
        "COUNTER": [],
    }
    lineages: list[dict[str, Any]] = []
    routes: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    verified: list[str] = []
    focus_question_index = 0
    question_index = 0
    for contract in bundle.contracts:
        for question in contract["question_families"]:
            if question.get("mandatory_for_full_thesis") is not True:
                continue
            question_index += 1
            is_focus = str(contract["archetype_id"]) == focus_id
            if is_focus:
                focus_question_index += 1
            use_counter = bool(is_focus and focus_question_index == 2)
            direction = "COUNTER" if use_counter else "POSITIVE"
            status = "COUNTER_SUPPORTED" if use_counter else "SUPPORTED_SCORING"
            fact_id = f"PROFACT-{case['case_id']}-{question_index:03d}"
            lineage_id = f"LINEAGE-{case['case_id']}-{question_index:03d}"
            question_id = str(question["question_family_id"])
            roles = tuple(str(value) for value in question["required_source_roles"])
            statement = (
                str(case["counter_statement"])
                if use_counter
                else (
                    str(case["positive_statement"])
                    if is_focus and focus_question_index == 1
                    else str(question["economic_need"])
                )
            )
            predicates = (
                question["counter_predicates"]
                if use_counter
                else question["support_predicates"]
            )
            fact = {
                "dossier_fact_id": fact_id,
                "statement": statement,
                "direction": direction,
                "source_lineage_id": lineage_id,
                "question_family_ids": [question_id],
                "source_role_ids": list(roles),
                "candidate_components": list(question["affected_component_ids"]),
                "predicate": str(predicates[0]),
                "economic_mechanism": str(question["economic_need"]),
                "current_status": "CURRENT",
                "published_at": as_of_date,
            }
            facts_by_direction[direction].append(fact)
            verified.append(fact_id)
            url = f"https://official.example/{case['case_id']}/{question_index}"
            lineages.append(
                {
                    "source_lineage_id": lineage_id,
                    "source_urls": [url],
                    "fact_ids": [fact_id],
                    "independence_group_id": (
                        f"GROUP-{case['case_id']}-{question_index:03d}"
                    ),
                    "status": "ACTIVE",
                }
            )
            route_ids = []
            for role_index, role in enumerate(roles, 1):
                route_id = (
                    f"ROUTE-{case['case_id']}-{question_index:03d}-{role_index}"
                )
                route_ids.append(route_id)
                routes.append(
                    {
                        "route_receipt_id": route_id,
                        "pass_id": "PASS-GOLDEN-OFFLINE",
                        "archetype_id": str(contract["archetype_id"]),
                        "question_family_id": question_id,
                        "gap_id": None,
                        "source_role_id": role,
                        "query_or_navigation_objective": (
                            f"{question_id}의 {role} 원문 검증"
                        ),
                        "query_text": "GOLDEN_FIXTURE_NO_LIVE_QUERY",
                        "result_count_seen": 1,
                        "opened_source_urls": [url],
                        "accepted_fact_ids": [fact_id],
                        "rejected_candidate_ids": [],
                        "provider_status": "SUCCESS",
                        "parser_status": "SUCCESS",
                        "no_new_route_reason": None,
                        "performed_at": f"{as_of_date}T00:00:00Z",
                    }
                )
            results.append(
                {
                    "archetype_id": str(contract["archetype_id"]),
                    "question_family_id": question_id,
                    "status": status,
                    "support_fact_ids": [] if use_counter else [fact_id],
                    "counter_fact_ids": [fact_id] if use_counter else [],
                    "resolution_fact_ids": [],
                    "attempted_source_role_ids": list(roles),
                    "search_route_receipt_ids": route_ids,
                    "required_source_roles_satisfied": list(roles),
                    "required_source_roles_missing": [],
                    "availability_class": "PUBLIC_SEARCHABLE",
                    "affected_component_ids": list(question["affected_component_ids"]),
                    "could_change_score": bool(question["could_change_score"]),
                    "could_change_stage": bool(question["could_change_stage"]),
                    "could_change_hard_break": bool(
                        question["could_change_hard_break"]
                    ),
                    "closure_reason": (
                        "offline golden의 exact question/source/fact linkage가 검증됐다."
                    ),
                    "adequate_search_proven": True,
                }
            )
    dossier = {
        "schema_version": "e2r_pro_research_dossier_v2",
        "job_id": f"JOB-{case['case_id']}",
        "run_id": f"RUN-{case['case_id']}",
        "conversation_id": f"CONVERSATION-{case['case_id']}",
        "research_pass_id": f"PASS-{case['case_id']}",
        "parent_pass_id": None,
        "target": {
            "target_id": f"BLIND-{case['case_id']}",
            "company_name": "블라인드 골든 대상",
        },
        "as_of_date": as_of_date,
        "candidate_archetypes": [primary_id],
        "selected_archetypes": [primary_id],
        "research_status": "COMPLETE",
        "material_facts": facts_by_direction["POSITIVE"],
        "counterfacts": facts_by_direction["COUNTER"],
        "resolution_facts": [],
        "question_family_results": results,
        "source_lineages": lineages,
        "search_route_receipts": routes,
        "verification_repair_register": [],
        "proposed_score_ranges": [],
        "score_authority": False,
        "stage_authority": False,
    }
    return dossier, tuple(verified)


def run_mechanism_golden_replay(
    case: Mapping[str, Any],
    *,
    prompt_snapshot: str,
) -> Mapping[str, Any]:
    dossier, verified = build_mechanism_golden_dossier(case)
    primary_id = str(case["primary_archetype_id"])
    focus_id = str(case.get("focus_contract_id") or primary_id)
    focus = load_research_contract(focus_id)
    question_text = "\n".join(
        str(row["question_text"]) for row in focus["question_families"]
    ).casefold()
    prompt_lower = prompt_snapshot.casefold()
    critical_terms = tuple(str(value) for value in case["critical_question_terms"])
    missing_terms = tuple(
        value
        for value in critical_terms
        if value.casefold() not in question_text
        or value.casefold() not in prompt_lower
    )
    expected_focus_questions = tuple(
        str(row["question_family_id"])
        for row in focus["question_families"]
        if row.get("mandatory_for_full_thesis") is True
    )

    adjudicator = ResearchSaturationAdjudicator()
    closed = adjudicator.adjudicate(
        dossier=dossier,
        verified_fact_ids=verified,
    )
    open_dossier = deepcopy(dossier)
    opened = next(
        row
        for row in open_dossier["question_family_results"]
        if row["question_family_id"] == expected_focus_questions[0]
    )
    opened["status"] = "PUBLIC_SEARCHABLE"
    opened_receipt = adjudicator.adjudicate(
        dossier=open_dossier,
        verified_fact_ids=verified,
    )
    focus_decisions = tuple(
        row
        for row in closed.question_decisions
        if row.question_family_id in set(expected_focus_questions)
    )
    all_source_roles_covered = all(
        set(row.required_source_roles).issubset(row.verified_source_roles)
        for row in focus_decisions
    )
    facts = tuple(
        row
        for key in ("material_facts", "counterfacts", "resolution_facts")
        for row in dossier.get(key) or ()
    )
    dates_blind_safe = all(
        date.fromisoformat(str(row["published_at"])[:10])
        <= date.fromisoformat(str(case["as_of_date"]))
        for row in facts
    )
    forbidden_case_fields = {
        "expected_score",
        "expected_stage",
        "future_price_outcome",
        "gold_answer",
    }.intersection(case)
    prompt_gold_leakage = any(
        token in prompt_lower
        for token in (
            "expected_score",
            "expected_stage",
            "future_price_outcome",
            "gold_answer",
        )
    )
    positive_recalled = any(
        row.get("statement") == case["positive_statement"]
        for row in dossier["material_facts"]
    )
    counter_recalled = any(
        row.get("statement") == case["counter_statement"]
        for row in dossier["counterfacts"]
    )
    failures = []
    if missing_terms:
        failures.append("CRITICAL_QUESTION_RECALL_MISSING")
    if not positive_recalled:
        failures.append("MATERIAL_POSITIVE_RECALL_MISSING")
    if not counter_recalled:
        failures.append("MATERIAL_COUNTER_RECALL_MISSING")
    if not all_source_roles_covered:
        failures.append("SOURCE_ROLE_COVERAGE_INCOMPLETE")
    if not closed.research_saturation_valid:
        failures.append("QUESTION_TERMINALITY_INCOMPLETE")
    if opened_receipt.research_saturation_valid:
        failures.append("PUBLIC_GAP_WAS_NOT_OPENED")
    if expected_focus_questions[0] not in opened_receipt.public_material_gap_question_ids:
        failures.append("PUBLIC_GAP_NOT_MATERIAL")
    if closed.verifier_repair_pending_ids:
        failures.append("VERIFIER_REPAIR_PENDING")
    if not dates_blind_safe:
        failures.append("FUTURE_LEAKAGE")
    if forbidden_case_fields or prompt_gold_leakage:
        failures.append("GOLD_INJECTION")
    audit = compile_saturation_audit(closed)
    if audit["critical_count_sum"] != 0:
        failures.append("SATURATION_AUDIT_CRITICAL")
    payload = {
        "schema_version": "e2r_pro_v2_mechanism_golden_replay_v1",
        "case_id": str(case["case_id"]),
        "mechanism_family": str(case["mechanism_family"]),
        "primary_archetype_id": primary_id,
        "focus_contract_id": focus_id,
        "status": "PASS" if not failures else "FAIL",
        "failure_codes": failures,
        "critical_question_count": len(expected_focus_questions),
        "critical_question_recall_count": len(expected_focus_questions)
        if not missing_terms
        else 0,
        "material_positive_recall": positive_recalled,
        "material_counter_recall": counter_recalled,
        "source_role_coverage_complete": all_source_roles_covered,
        "question_terminality_complete": closed.research_saturation_valid,
        "public_gap_open_before_closure": not opened_receipt.research_saturation_valid,
        "public_gap_count_after_closure": len(closed.public_material_gap_question_ids),
        "verifier_repair_pending_count": len(closed.verifier_repair_pending_ids),
        "future_leakage_count": 0 if dates_blind_safe else 1,
        "gold_injection_count": len(forbidden_case_fields)
        + int(prompt_gold_leakage),
        "query_count": 0,
        "fetch_count": 0,
        "score_authority": False,
        "stage_authority": False,
        "saturation_receipt_hash": closed.receipt_hash,
    }
    return {**payload, "replay_hash": canonical_hash(payload)}


def _validate_case(case: Mapping[str, Any]) -> None:
    required = {
        "case_id",
        "mechanism_family",
        "primary_archetype_id",
        "as_of_date",
        "critical_question_terms",
        "positive_statement",
        "counter_statement",
    }
    missing = required - set(case)
    if missing:
        raise ValueError(f"mechanism golden case missing fields: {sorted(missing)}")
    if str(case["mechanism_family"]) not in MANDATORY_MECHANISM_FAMILIES:
        raise ValueError("mechanism golden case is outside the mandatory roster")
    date.fromisoformat(str(case["as_of_date"]))
    if not tuple(case["critical_question_terms"] or ()):
        raise ValueError("mechanism golden case requires critical question terms")


__all__ = [
    "MANDATORY_MECHANISM_FAMILIES",
    "build_mechanism_golden_dossier",
    "run_mechanism_golden_replay",
]
