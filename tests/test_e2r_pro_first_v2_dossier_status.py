from __future__ import annotations

from copy import deepcopy
import unittest

from e2r.pro_first.dossier import (
    DossierValidationContext,
    DossierValidationError,
    ResearchDossierValidator,
)
from e2r.pro_first.research_contracts import select_contract_bundle


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"


def _question_result(
    archetype_id: str,
    question_id: str,
    *,
    status: str = "NOT_APPLICABLE_WITH_REASON",
    availability: str = "NOT_APPLICABLE",
    adequate: bool = False,
    receipts: tuple[str, ...] = (),
) -> dict:
    return {
        "archetype_id": archetype_id,
        "question_family_id": question_id,
        "status": status,
        "support_fact_ids": [],
        "counter_fact_ids": [],
        "resolution_fact_ids": [],
        "attempted_source_role_ids": [],
        "search_route_receipt_ids": list(receipts),
        "required_source_roles_satisfied": [],
        "required_source_roles_missing": ["ISSUER_OFFICIAL"],
        "availability_class": availability,
        "affected_component_ids": [],
        "could_change_score": True,
        "could_change_stage": True,
        "could_change_hard_break": False,
        "closure_reason": "테스트에서 명시한 question-level 상태",
        "adequate_search_proven": adequate,
    }


def _base_v2(*, complete: bool = False) -> dict:
    bundle = select_contract_bundle((ARCHETYPE,))
    if complete:
        results = [
            _question_result(
                contract["archetype_id"],
                question["question_family_id"],
            )
            for contract in bundle.contracts
            for question in contract["question_families"]
        ]
        status = "COMPLETE"
    else:
        question = bundle.primary_contracts[0]["question_families"][0]
        results = [
            _question_result(
                ARCHETYPE,
                question["question_family_id"],
                status="PUBLIC_SEARCHABLE",
                availability="PUBLIC_SEARCHABLE",
            )
        ]
        status = "NEEDS_PUBLIC_GAP_CLOSURE"
    return {
        "schema_version": "e2r_pro_research_dossier_v2",
        "job_id": "JOB-V2",
        "run_id": "RUN-V2",
        "conversation_id": "CONVERSATION-V2",
        "research_pass_id": "PASS-1",
        "parent_pass_id": None,
        "target": {"target_id": "000660", "company_name": "검증대상"},
        "as_of_date": "2026-08-22",
        "candidate_archetypes": [ARCHETYPE],
        "selected_archetypes": [ARCHETYPE],
        "research_status": status,
        "business_model": {},
        "material_facts": [],
        "counterfacts": [],
        "resolution_facts": [],
        "question_family_results": results,
        "component_research": {},
        "structured_metrics": {},
        "unresolved_gaps": [],
        "source_lineages": [],
        "search_route_receipts": [],
        "research_passes": [
            {
                "pass_id": "PASS-1",
                "parent_pass_id": None,
                "pass_name": "QUESTION_CLOSURE_AUDIT",
                "status": "COMPLETE",
                "prompt_hash": "prompt-hash",
                "response_hash": "response-hash",
            }
        ],
        "research_saturation": {},
        "verification_repair_register": [],
        "proposed_score_ranges": [],
        "score_authority": False,
        "stage_authority": False,
    }


def _context() -> DossierValidationContext:
    return DossierValidationContext(
        job_id="JOB-V2",
        run_id="RUN-V2",
        target_id="000660",
        as_of_date="2026-08-22",
        conversation_id="CONVERSATION-V2",
        candidate_archetype_ids=(ARCHETYPE,),
    )


class ProFirstV2DossierStatusTest(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = ResearchDossierValidator()

    def test_research_status_not_forced_complete(self) -> None:
        payload = _base_v2()
        receipt = self.validator.validate(payload, _context())
        self.assertEqual(receipt.research_status, "NEEDS_PUBLIC_GAP_CLOSURE")
        self.assertEqual(receipt.schema_version, "e2r_pro_research_dossier_v2")

    def test_question_terminal_status_schema(self) -> None:
        payload = _base_v2(complete=True)
        receipt = self.validator.validate(payload, _context())
        self.assertEqual(receipt.research_status, "COMPLETE")
        self.assertGreater(len(receipt.question_family_ids), 20)

        invalid = deepcopy(payload)
        invalid["question_family_results"][0]["status"] = "PRO_SAYS_DONE"
        with self.assertRaisesRegex(DossierValidationError, "schema validation"):
            self.validator.validate(invalid, _context())

    def test_nonterminal_public_gap_preserved(self) -> None:
        payload = _base_v2()
        payload["research_status"] = "COMPLETE"
        with self.assertRaisesRegex(DossierValidationError, "non-terminal mandatory"):
            self.validator.validate(payload, _context())

    def test_likely_nonpublic_requires_adequacy(self) -> None:
        payload = _base_v2()
        result = payload["question_family_results"][0]
        result["status"] = "LIKELY_NONPUBLIC"
        result["availability_class"] = "LIKELY_NONPUBLIC"
        payload["research_status"] = "COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER"
        with self.assertRaisesRegex(DossierValidationError, "adequate-search proof"):
            self.validator.validate(payload, _context())

    def test_search_route_receipt_bound_to_question(self) -> None:
        payload = _base_v2()
        result = payload["question_family_results"][0]
        result["search_route_receipt_ids"] = ["ROUTE-1"]
        payload["search_route_receipts"] = [
            {
                "route_receipt_id": "ROUTE-1",
                "pass_id": "PASS-1",
                "archetype_id": ARCHETYPE,
                "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q99",
                "gap_id": "GAP-1",
                "source_role_id": "ISSUER_OFFICIAL",
                "query_or_navigation_objective": "공식자료 확인",
                "query_text": "검증대상 공식 자료",
                "result_count_seen": 0,
                "opened_source_urls": [],
                "accepted_fact_ids": [],
                "rejected_candidate_ids": [],
                "provider_status": "SUCCESS",
                "no_new_route_reason": "검색 결과 없음",
                "performed_at": "2026-08-23T00:00:00Z"
            }
        ]
        with self.assertRaisesRegex(DossierValidationError, "another question"):
            self.validator.validate(payload, _context())

    def test_v1_read_only_compatibility(self) -> None:
        components = {
            key: {}
            for key in (
                "eps_fcf_explosion",
                "earnings_visibility",
                "bottleneck_pricing",
                "market_mispricing",
                "valuation_rerating",
                "capital_allocation",
                "information_confidence",
            )
        }
        v1 = {
            "schema_version": "e2r_pro_research_dossier_v1",
            "job_id": "JOB-V1",
            "run_id": "RUN-V1",
            "target": {"target_id": "000660"},
            "as_of_date": "2026-08-22",
            "research_status": "COMPLETE",
            "business_model": {},
            "candidate_archetypes": [ARCHETYPE],
            "material_facts": [],
            "counterfacts": [],
            "component_research": components,
            "structured_metrics": {},
            "unresolved_gaps": [],
            "sources": [],
            "research_saturation": {},
            "proposed_score_ranges": {},
            "score_authority": False,
            "stage_authority": False,
        }
        receipt = self.validator.validate(
            v1,
            DossierValidationContext(
                job_id="JOB-V1",
                run_id="RUN-V1",
                target_id="000660",
                as_of_date="2026-08-22",
            ),
        )
        self.assertEqual(receipt.schema_version, "e2r_pro_research_dossier_v1")
        self.assertEqual(v1["research_status"], "COMPLETE")


if __name__ == "__main__":
    unittest.main()
