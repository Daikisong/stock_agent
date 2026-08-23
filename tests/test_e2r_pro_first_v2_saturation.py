from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.research_contracts import select_contract_bundle
from e2r.pro_first.saturation import (
    DeterministicQuestionBound,
    NoNewRouteConfirmation,
    ResearchSaturationAdjudicator,
    compile_saturation_audit,
    evaluate_semantic_no_new_route_fixpoint,
)


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"


def _materiality(question: dict) -> str:
    if question["could_change_hard_break"]:
        return "HARD_BREAK"
    if question["could_change_stage"]:
        return "STAGE_BOUNDARY"
    if question["could_change_score"]:
        return "CORE_SCORE"
    return "MONITORING"


def _complete_dossier() -> tuple[dict, set[str]]:
    bundle = select_contract_bundle((ARCHETYPE,))
    facts: list[dict] = []
    lineages: list[dict] = []
    routes: list[dict] = []
    results: list[dict] = []
    verified: set[str] = set()
    for question_index, contract_question in enumerate(
        (
            (contract, question)
            for contract in bundle.contracts
            for question in contract["question_families"]
            if question["mandatory_for_full_thesis"] is True
        ),
        1,
    ):
        contract, question = contract_question
        question_id = question["question_family_id"]
        fact_id = f"PROFACT-Q{question_index:03d}"
        lineage_id = f"LINEAGE-Q{question_index:03d}"
        roles = list(question["required_source_roles"])
        fact = {
            "dossier_fact_id": fact_id,
            "source_lineage_id": lineage_id,
            "question_family_ids": [question_id],
            "source_role_ids": roles,
            "candidate_components": list(question["affected_component_ids"]),
            "predicate": question["support_predicates"][0],
            "economic_mechanism": question["economic_need"],
            "current_status": "CURRENT",
        }
        facts.append(fact)
        verified.add(fact_id)
        lineages.append(
            {
                "source_lineage_id": lineage_id,
                "source_urls": [f"https://issuer.example/q/{question_index}"],
                "fact_ids": [fact_id],
                "independence_group_id": f"GROUP-Q{question_index:03d}",
                "status": "ACTIVE",
            }
        )
        route_ids: list[str] = []
        for role_index, role in enumerate(roles, 1):
            route_id = f"ROUTE-Q{question_index:03d}-{role_index}"
            route_ids.append(route_id)
            routes.append(
                {
                    "route_receipt_id": route_id,
                    "pass_id": "PASS-INITIAL",
                    "archetype_id": contract["archetype_id"],
                    "question_family_id": question_id,
                    "gap_id": None,
                    "source_role_id": role,
                    "query_or_navigation_objective": f"{question_id} {role} 원문 확인",
                    "query_text": f"검증대상 {question_id} {role}",
                    "result_count_seen": 1,
                    "opened_source_urls": [
                        f"https://issuer.example/q/{question_index}/{role_index}"
                    ],
                    "accepted_fact_ids": [fact_id],
                    "rejected_candidate_ids": [],
                    "provider_status": "SUCCESS",
                    "parser_status": "SUCCESS",
                    "no_new_route_reason": None,
                    "performed_at": "2026-08-22T01:00:00Z",
                }
            )
        results.append(
            {
                "archetype_id": contract["archetype_id"],
                "question_family_id": question_id,
                "status": "SUPPORTED_SCORING",
                "support_fact_ids": [fact_id],
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
                "attempted_source_role_ids": roles,
                "search_route_receipt_ids": route_ids,
                "required_source_roles_satisfied": roles,
                "required_source_roles_missing": [],
                "availability_class": "PUBLIC_SEARCHABLE",
                "affected_component_ids": list(question["affected_component_ids"]),
                "could_change_score": question["could_change_score"],
                "could_change_stage": question["could_change_stage"],
                "could_change_hard_break": question["could_change_hard_break"],
                "closure_reason": "검증된 원문 fact와 exact source route가 연결됐다.",
                "adequate_search_proven": True,
            }
        )
    return (
        {
            "schema_version": "e2r_pro_research_dossier_v2",
            "job_id": "JOB-SATURATION",
            "run_id": "RUN-SATURATION",
            "conversation_id": "CONVERSATION-SATURATION",
            "target": {"target_id": "000660", "company_name": "검증대상"},
            "as_of_date": "2026-08-22",
            "candidate_archetypes": [ARCHETYPE],
            "selected_archetypes": [ARCHETYPE],
            "research_status": "COMPLETE",
            "material_facts": facts,
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": results,
            "source_lineages": lineages,
            "search_route_receipts": routes,
        },
        verified,
    )


def _decision(receipt, question_id: str):
    return next(
        row for row in receipt.question_decisions if row.question_family_id == question_id
    )


class ProFirstV2SaturationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.adjudicator = ResearchSaturationAdjudicator()
        self.dossier, self.verified = _complete_dossier()
        self.bundle = select_contract_bundle((ARCHETYPE,))

    def _adjudicate(self, dossier=None, **kwargs):
        return self.adjudicator.adjudicate(
            dossier=dossier or self.dossier,
            verified_fact_ids=kwargs.pop("verified_fact_ids", self.verified),
            **kwargs,
        )

    def _contract_question(self, question_id: str) -> dict:
        return next(
            question
            for contract in self.bundle.contracts
            for question in contract["question_families"]
            if question["question_family_id"] == question_id
        )

    def _result(self, dossier: dict, question_id: str) -> dict:
        return next(
            row
            for row in dossier["question_family_results"]
            if row["question_family_id"] == question_id
        )

    def test_complete_verified_question_roster_is_full_thesis_ready(self) -> None:
        receipt = self._adjudicate()
        self.assertTrue(receipt.research_saturation_valid)
        self.assertTrue(receipt.component_entry_allowed)
        self.assertEqual(receipt.deterministic_research_status, "COMPLETE")
        self.assertEqual(compile_saturation_audit(receipt)["critical_count_sum"], 0)

    def test_tracked_saturation_audit_matches_current_engine(self) -> None:
        receipt = self._adjudicate()
        expected = dict(compile_saturation_audit(receipt))
        expected.update(
            {
                "phase": "P5",
                "fixture_scope": (
                    "C06 plus four mandatory R13 cross-archetype guards"
                ),
                "legacy_component_fact_count_function_present": False,
                "exact_question_source_role_semantics": True,
                "stale_confirmation_cross_gap_reuse_allowed": False,
                "known_hynix_like_gap_count": 13,
                "known_hynix_like_blocking_gap_count": 13,
                "known_hynix_like_core_blocker_count": 5,
                "known_hynix_like_stage_boundary_gap_count": 1,
                "known_hynix_like_hard_break_gap_count": 7,
                "known_hynix_like_corroboration_cap_count": 0,
                "focused_test_count": 19,
            }
        )
        path = (
            Path(__file__).resolve().parents[1]
            / "docs/operational/e2r_pro_first_v2/saturation_semantics_audit.json"
        )
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), expected)

    def test_research_status_enum_allows_incomplete(self) -> None:
        dossier = deepcopy(self.dossier)
        dossier["research_status"] = "NEEDS_PUBLIC_GAP_CLOSURE"
        dossier["question_family_results"][0]["status"] = "PUBLIC_SEARCHABLE"
        receipt = self._adjudicate(dossier)
        self.assertFalse(receipt.research_saturation_valid)
        self.assertEqual(receipt.deterministic_research_status, "NEEDS_PUBLIC_GAP_CLOSURE")

    def test_public_searchable_is_nonterminal(self) -> None:
        dossier = deepcopy(self.dossier)
        result = dossier["question_family_results"][0]
        result["status"] = "PUBLIC_SEARCHABLE"
        receipt = self._adjudicate(dossier)
        decision = _decision(receipt, result["question_family_id"])
        self.assertFalse(decision.terminal)
        self.assertIn(decision.gap_class, {"CORE_SCORE_BLOCKER", "STAGE_BOUNDARY_GAP", "HARD_BREAK_GAP"})
        self.assertIn(result["question_family_id"], receipt.public_material_gap_question_ids)

    def _likely_nonpublic_fixture(self, *, missing_core: bool = False):
        dossier = deepcopy(self.dossier)
        result = next(
            row
            for row in dossier["question_family_results"]
            if row["archetype_id"] == ARCHETYPE
            and len(self._contract_question(row["question_family_id"])["required_source_roles"])
            >= 2
        )
        question_id = result["question_family_id"]
        question = self._contract_question(question_id)
        fact_id = result["support_fact_ids"][0]
        fact = next(
            row for row in dossier["material_facts"] if row["dossier_fact_id"] == fact_id
        )
        core_roles = [
            role for role in question["required_source_roles"] if not role.startswith(("CUSTOMER_", "PEER_", "PARTNER_"))
        ]
        supporting_roles = [
            role for role in question["required_source_roles"] if role not in core_roles
        ]
        self.assertTrue(core_roles and supporting_roles)
        satisfied = supporting_roles if missing_core else core_roles
        missing = core_roles if missing_core else supporting_roles
        fact["source_role_ids"] = satisfied
        result.update(
            {
                "status": "LIKELY_NONPUBLIC",
                "availability_class": "LIKELY_NONPUBLIC",
                "required_source_roles_satisfied": satisfied,
                "required_source_roles_missing": missing,
                "adequate_search_proven": True,
                "closure_reason": "공시 의무와 반복된 독립 공개경로 검색을 검토했으나 공개되지 않았다.",
            }
        )
        relevant = [
            row
            for row in dossier["search_route_receipts"]
            if row["question_family_id"] == question_id
        ]
        accepted_route = next(
            row for row in relevant if row["source_role_id"] in satisfied
        )
        result["search_route_receipt_ids"] = [accepted_route["route_receipt_id"]]
        no_new_routes = []
        for index in (1, 2):
            route = {
                **deepcopy(accepted_route),
                "route_receipt_id": f"ROUTE-NONE-{question_id}-{index}",
                "pass_id": f"PASS-GAP-{index}",
                "source_role_id": missing[0],
                "query_or_navigation_objective": f"미공개 경계 독립 확인 {index}",
                "query_text": f"검증대상 공개 경로 독립 확인 {index}",
                "opened_source_urls": [f"https://search.example/{question_id}/{index}"],
                "accepted_fact_ids": [],
                "result_count_seen": 0,
                "no_new_route_reason": "공식 공개 범위와 검색 결과에 새 경로가 없다.",
            }
            dossier["search_route_receipts"].append(route)
            result["search_route_receipt_ids"].append(route["route_receipt_id"])
            no_new_routes.append(route)
        result["attempted_source_role_ids"] = list(question["required_source_roles"])
        provisional = self._adjudicate(dossier)
        attempted_hash = canonical_hash(sorted(question["required_source_roles"]))
        confirmations = tuple(
            NoNewRouteConfirmation.from_route_receipt(
                receipt=route,
                stable_gap_key=f"{ARCHETYPE}:{question_id}:{missing[0]}",
                fact_snapshot_hash=provisional.fact_snapshot_hash,
                accepted_lineage_roster_hash=provisional.accepted_lineage_roster_hash,
                attempted_source_roles_hash=attempted_hash,
            )
            for route in no_new_routes
        )
        bound = DeterministicQuestionBound(
            question_family_id=question_id,
            materiality=_materiality(question),
            component_lower_delta={key: 0.0 for key in question["affected_component_ids"]},
            component_upper_delta={key: 1.0 for key in question["affected_component_ids"]},
            deterministic_lower_stage="2",
            deterministic_upper_stage="2",
            hard_break_polarity_resolved=True,
            missing_predicate_is_new_core=False,
        )
        return dossier, question_id, confirmations, bound

    def test_likely_nonpublic_is_terminal_with_cap(self) -> None:
        dossier, question_id, confirmations, bound = self._likely_nonpublic_fixture()
        receipt = self._adjudicate(
            dossier,
            deterministic_bounds={question_id: bound},
            fixpoint_confirmations=confirmations,
        )
        decision = _decision(receipt, question_id)
        self.assertTrue(decision.terminal)
        self.assertEqual(decision.gap_class, "CORROBORATION_CAP")
        self.assertTrue(decision.availability.known_evidence_preserved)
        self.assertTrue(decision.availability.information_confidence_cap_allowed)
        self.assertFalse(decision.availability.component_zeroing_allowed)
        self.assertFalse(decision.availability.whole_score_invalidation_allowed)
        self.assertTrue(receipt.research_saturation_valid)
        self.assertEqual(
            receipt.deterministic_research_status,
            "COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER",
        )

    def test_future_event_only_is_terminal_monitoring(self) -> None:
        dossier = deepcopy(self.dossier)
        result = dossier["question_family_results"][0]
        result["status"] = "FUTURE_EVENT_ONLY"
        result["availability_class"] = "FUTURE_EVENT_ONLY"
        receipt = self._adjudicate(dossier)
        decision = _decision(receipt, result["question_family_id"])
        self.assertTrue(decision.terminal)
        self.assertTrue(decision.availability.monitoring_only)
        self.assertNotIn(result["question_family_id"], receipt.public_material_gap_question_ids)

    def test_absent_requires_adequate_search_receipt(self) -> None:
        dossier = deepcopy(self.dossier)
        result = dossier["question_family_results"][0]
        result.update(
            {
                "status": "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
                "support_fact_ids": [],
                "required_source_roles_satisfied": [],
                "required_source_roles_missing": list(
                    self._contract_question(result["question_family_id"])["required_source_roles"]
                ),
                "adequate_search_proven": True,
            }
        )
        receipt = self._adjudicate(dossier)
        decision = _decision(receipt, result["question_family_id"])
        self.assertFalse(decision.terminal)
        self.assertIn("SEMANTIC_FIXPOINT_NOT_PROVEN", decision.route_adequacy.failure_codes)
        self.assertFalse(receipt.research_saturation_valid)

    def test_adequately_searched_absence_is_terminal(self) -> None:
        dossier = deepcopy(self.dossier)
        verified = set(self.verified)
        result = dossier["question_family_results"][0]
        question_id = result["question_family_id"]
        question = self._contract_question(question_id)
        removed_fact_ids = set(result["support_fact_ids"])
        dossier["material_facts"] = [
            row
            for row in dossier["material_facts"]
            if row["dossier_fact_id"] not in removed_fact_ids
        ]
        verified.difference_update(removed_fact_ids)
        result.update(
            {
                "status": "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
                "support_fact_ids": [],
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
                "required_source_roles_satisfied": [],
                "required_source_roles_missing": list(
                    question["required_source_roles"]
                ),
                "availability_class": "PUBLIC_SEARCHABLE",
                "adequate_search_proven": True,
                "closure_reason": "필수 공식 경로를 독립적으로 확인했지만 대상 사실은 공개 자료에 존재하지 않았다.",
            }
        )
        no_new_routes = []
        for index, role in enumerate(question["required_source_roles"], 1):
            route = {
                "route_receipt_id": f"ROUTE-ABSENT-{index}",
                "pass_id": f"PASS-ABSENT-{index}",
                "archetype_id": ARCHETYPE,
                "question_family_id": question_id,
                "gap_id": f"GAP-ABSENT-{question_id}",
                "source_role_id": role,
                "query_or_navigation_objective": f"{role} 부재 확인 {index}",
                "query_text": f"검증대상 {role} 부재 확인 {index}",
                "result_count_seen": 0,
                "opened_source_urls": [f"https://search.example/absent/{index}"],
                "accepted_fact_ids": [],
                "rejected_candidate_ids": [],
                "provider_status": "SUCCESS",
                "parser_status": "SUCCESS",
                "no_new_route_reason": "공식 공개 경로에 해당 사실이 없다.",
                "performed_at": f"2026-08-22T0{index}:00:00Z",
            }
            dossier["search_route_receipts"].append(route)
            no_new_routes.append(route)
        result["search_route_receipt_ids"] = [
            row["route_receipt_id"] for row in no_new_routes
        ]
        result["attempted_source_role_ids"] = list(
            question["required_source_roles"]
        )
        provisional = self._adjudicate(
            dossier,
            verified_fact_ids=verified,
        )
        attempted_hash = canonical_hash(sorted(question["required_source_roles"]))
        confirmations = tuple(
            NoNewRouteConfirmation.from_route_receipt(
                receipt=route,
                stable_gap_key=f"{ARCHETYPE}:{question_id}:ABSENCE",
                fact_snapshot_hash=provisional.fact_snapshot_hash,
                accepted_lineage_roster_hash=(
                    provisional.accepted_lineage_roster_hash
                ),
                attempted_source_roles_hash=attempted_hash,
            )
            for route in no_new_routes
        )
        receipt = self._adjudicate(
            dossier,
            verified_fact_ids=verified,
            fixpoint_confirmations=confirmations,
        )
        decision = _decision(receipt, question_id)
        self.assertTrue(decision.terminal)
        self.assertTrue(decision.route_adequacy.adequate)
        self.assertEqual(decision.gap_class, "NO_GAP")
        self.assertTrue(receipt.research_saturation_valid)

    def test_not_applicable_with_reason_is_terminal_without_fake_fact(self) -> None:
        dossier = deepcopy(self.dossier)
        verified = set(self.verified)
        result = dossier["question_family_results"][0]
        question_id = result["question_family_id"]
        question = self._contract_question(question_id)
        removed_fact_ids = set(result["support_fact_ids"])
        dossier["material_facts"] = [
            row
            for row in dossier["material_facts"]
            if row["dossier_fact_id"] not in removed_fact_ids
        ]
        verified.difference_update(removed_fact_ids)
        result.update(
            {
                "status": "NOT_APPLICABLE_WITH_REASON",
                "support_fact_ids": [],
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
                "attempted_source_role_ids": [],
                "search_route_receipt_ids": [],
                "required_source_roles_satisfied": [],
                "required_source_roles_missing": list(
                    question["required_source_roles"]
                ),
                "availability_class": "NOT_APPLICABLE",
                "adequate_search_proven": False,
                "closure_reason": "해당 경제 메커니즘은 확인된 사업모델 범위에 적용되지 않는다.",
            }
        )
        receipt = self._adjudicate(
            dossier,
            verified_fact_ids=verified,
        )
        decision = _decision(receipt, question_id)
        self.assertTrue(decision.terminal)
        self.assertEqual(decision.gap_class, "NO_GAP")
        self.assertFalse(decision.verified_linked_fact_ids)
        self.assertTrue(receipt.research_saturation_valid)

    def test_question_missing_blocks_saturation(self) -> None:
        dossier = deepcopy(self.dossier)
        removed = dossier["question_family_results"].pop()["question_family_id"]
        receipt = self._adjudicate(dossier)
        self.assertIn(removed, receipt.missing_mandatory_question_ids)
        self.assertFalse(receipt.component_entry_allowed)

    def test_no_new_route_fixpoint_closes_gap(self) -> None:
        dossier, question_id, confirmations, bound = self._likely_nonpublic_fixture()
        decision = evaluate_semantic_no_new_route_fixpoint(confirmations)
        self.assertTrue(decision.reached)
        self.assertEqual(decision.disposition, "SEMANTIC_NO_NEW_PUBLIC_ROUTE_FIXPOINT")
        receipt = self._adjudicate(
            dossier,
            deterministic_bounds={question_id: bound},
            fixpoint_confirmations=confirmations,
        )
        self.assertTrue(_decision(receipt, question_id).route_adequacy.semantic_fixpoint)

    def test_unrelated_or_stale_confirmations_do_not_close_current_gap(self) -> None:
        dossier, question_id, confirmations, bound = self._likely_nonpublic_fixture()
        stale = tuple(
            NoNewRouteConfirmation(
                **{
                    **row.__dict__,
                    "fact_snapshot_hash": "f" * 64,
                }
            )
            for row in confirmations
        )
        receipt = self._adjudicate(
            dossier,
            deterministic_bounds={question_id: bound},
            fixpoint_confirmations=stale,
        )
        decision = _decision(receipt, question_id)
        self.assertFalse(decision.route_adequacy.semantic_fixpoint)
        self.assertFalse(receipt.research_saturation_valid)

    def test_component_fact_count_is_not_adequacy(self) -> None:
        dossier = deepcopy(self.dossier)
        first = dossier["question_family_results"][0]
        first["status"] = "PUBLIC_SEARCHABLE"
        profile = dossier["material_facts"][0]
        profile["predicate"] = "COMPANY_PROFILE"
        profile["candidate_components"] = list(first["affected_component_ids"])
        first["support_fact_ids"] = []
        receipt = self._adjudicate(dossier)
        decision = _decision(receipt, first["question_family_id"])
        self.assertEqual(decision.gap_class, "CORE_SCORE_BLOCKER")
        self.assertFalse(decision.terminal)

    def test_one_fact_touching_seven_components_not_full_coverage(self) -> None:
        dossier = deepcopy(self.dossier)
        only = dossier["question_family_results"][0]
        dossier["question_family_results"] = [only]
        fact = next(
            row
            for row in dossier["material_facts"]
            if row["dossier_fact_id"] == only["support_fact_ids"][0]
        )
        fact["candidate_components"] = [
            "eps_fcf_explosion",
            "earnings_visibility",
            "bottleneck_pricing",
            "market_mispricing",
            "valuation_rerating",
            "capital_allocation",
            "information_confidence",
        ]
        receipt = self._adjudicate(dossier)
        self.assertGreater(len(receipt.missing_mandatory_question_ids), 20)
        self.assertFalse(receipt.research_saturation_valid)

    def test_core_primary_role_missing_is_not_corroboration(self) -> None:
        dossier, question_id, confirmations, bound = self._likely_nonpublic_fixture(
            missing_core=True
        )
        receipt = self._adjudicate(
            dossier,
            deterministic_bounds={question_id: bound},
            fixpoint_confirmations=confirmations,
        )
        decision = _decision(receipt, question_id)
        self.assertTrue(decision.missing_core_source_roles)
        self.assertEqual(decision.gap_class, "CORE_SCORE_BLOCKER")
        self.assertFalse(receipt.research_saturation_valid)

    def test_public_stage_material_gap_opens_pro_followup(self) -> None:
        dossier = deepcopy(self.dossier)
        result = dossier["question_family_results"][0]
        result["status"] = "PUBLIC_SEARCHABLE"
        question_id = result["question_family_id"]
        question = self._contract_question(question_id)
        bound = DeterministicQuestionBound(
            question_family_id=question_id,
            materiality="STAGE_BOUNDARY",
            component_lower_delta={key: 0.0 for key in question["affected_component_ids"]},
            component_upper_delta={key: 2.0 for key in question["affected_component_ids"]},
            deterministic_lower_stage="2",
            deterministic_upper_stage="3-Green",
        )
        receipt = self._adjudicate(dossier, deterministic_bounds={question_id: bound})
        self.assertEqual(_decision(receipt, question_id).gap_class, "STAGE_BOUNDARY_GAP")
        self.assertEqual(receipt.deterministic_research_status, "NEEDS_PUBLIC_GAP_CLOSURE")

    def test_likely_nonpublic_gap_caps_without_zeroing(self) -> None:
        self.test_likely_nonpublic_is_terminal_with_cap()

    def test_pro_gap_proposal_divergence_receipt(self) -> None:
        dossier = deepcopy(self.dossier)
        result = dossier["question_family_results"][0]
        result.update(
            {
                "status": "PUBLIC_SEARCHABLE",
                "could_change_score": False,
                "could_change_stage": False,
                "could_change_hard_break": False,
            }
        )
        question_id = result["question_family_id"]
        question = self._contract_question(question_id)
        bound = DeterministicQuestionBound(
            question_family_id=question_id,
            materiality="STAGE_BOUNDARY",
            component_lower_delta={key: 0.0 for key in question["affected_component_ids"]},
            component_upper_delta={key: 1.0 for key in question["affected_component_ids"]},
            deterministic_lower_stage="2",
            deterministic_upper_stage="3-Green",
        )
        receipt = self._adjudicate(dossier, deterministic_bounds={question_id: bound})
        decision = _decision(receipt, question_id)
        self.assertTrue(decision.deterministic_materiality_diverged)
        self.assertEqual(decision.gap_class, "STAGE_BOUNDARY_GAP")

    def test_hynix_13_gaps_not_all_silently_downgraded(self) -> None:
        dossier = deepcopy(self.dossier)
        affected = dossier["question_family_results"][:13]
        affected_ids = {row["question_family_id"] for row in affected}
        for row in affected:
            row["status"] = "PUBLIC_SEARCHABLE"
            row["support_fact_ids"] = []
        receipt = self._adjudicate(dossier)
        decisions = [
            row for row in receipt.question_decisions if row.question_family_id in affected_ids
        ]
        self.assertEqual(len(decisions), 13)
        self.assertEqual(
            {label: sum(row.gap_class == label for row in decisions) for label in {
                "CORE_SCORE_BLOCKER",
                "STAGE_BOUNDARY_GAP",
                "HARD_BREAK_GAP",
                "CORROBORATION_CAP",
            }},
            {
                "CORE_SCORE_BLOCKER": 5,
                "STAGE_BOUNDARY_GAP": 1,
                "HARD_BREAK_GAP": 7,
                "CORROBORATION_CAP": 0,
            },
        )
        self.assertFalse(receipt.component_entry_allowed)


if __name__ == "__main__":
    unittest.main()
