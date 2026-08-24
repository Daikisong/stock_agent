from __future__ import annotations

from copy import deepcopy
import unittest

from e2r.pro_first.dossier import (
    DossierDialectError,
    DossierValidationContext,
    DossierValidationError,
    ResearchDossierDialectAdapter,
    ResearchDossierNormalizer,
    ResearchDossierValidator,
)
from e2r.pro_first.dossier.dialect_adapter import (
    _scoped_verifier_repair_proposals,
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

    def test_only_current_verifier_repair_packet_proposals_are_preserved(self) -> None:
        rows = [
            {
                "candidate_id": "PROFACT-MF015",
                "question_family_id": "R13_EXECUTION_CROSS_GUARD_Q04",
                "rejection_category": "QUOTE_MISMATCH",
                "status": "NARROWED",
                "dossier_fact_id": "PROFACT-MF051",
            },
            {
                "repair_id": "PRO-SELF-REPAIR-1",
                "status": "CLAIMED_COMPLETE",
            },
        ]
        passes = [
            {
                "pass_id": "PASS-REPAIR-1",
                "pass_name": "VERIFIER_REPAIR",
            }
        ]

        preserved = _scoped_verifier_repair_proposals(
            rows,
            research_pass_id="PASS-REPAIR-1",
            research_passes=passes,
        )

        self.assertEqual(preserved, [rows[0]])
        self.assertEqual(
            _scoped_verifier_repair_proposals(
                rows,
                research_pass_id="PASS-INITIAL-1",
                research_passes=[
                    {
                        "pass_id": "PASS-INITIAL-1",
                        "pass_name": "INITIAL_FULL_RESEARCH",
                    }
                ],
            ),
            [],
        )

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

    def test_compact_visible_pro_dialect_preserves_evidence_and_relationships(self) -> None:
        payload = _base_v2(complete=True)
        question = payload["question_family_results"][0]
        question_id = question["question_family_id"]
        question.update(
            {
                "status": "SUPPORTED_SCORING",
                "support_fact_ids": ["MF-000660-001"],
                "counter_fact_ids": ["CF-000660-001"],
                "resolution_fact_ids": ["RF-000660-001"],
                "attempted_source_role_ids": ["ISSUER_OFFICIAL"],
                "search_route_receipt_ids": ["ROUTE-001"],
                "required_source_roles_satisfied": ["ISSUER_OFFICIAL"],
                "required_source_roles_missing": [],
                "availability_class": "PUBLIC_SEARCHABLE",
                "affected_component_ids": ["eps_fcf_explosion"],
                "adequate_search_proven": True,
            }
        )
        payload["candidate_archetypes"] = [
            {"archetype_id": ARCHETYPE, "reason": "primary candidate"}
        ]
        payload["selected_archetypes"] = [
            {"archetype_id": ARCHETYPE, "role": "PRIMARY"},
            {"archetype_id": "R13_EXECUTION_CROSS_GUARD", "role": "CROSS_GUARD"},
        ]
        payload["material_facts"] = [
            {
                "fact_id": "MF-000660-001",
                "fact_type": "ISSUER_ACTUAL",
                "url": "https://example.com/issuer",
                "publisher": "검증대상",
                "publication_date": "2026-08-01",
                "availability_date": "2026-08-01",
                "subject": "검증대상",
                "target": "000660 검증대상",
                "business_segment": "메모리",
                "product_family": "HBM",
                "current_status": "CURRENT",
                "source_role_ids": ["ISSUER_OFFICIAL"],
                "source_lineage_id": "LINEAGE-001",
                "summary": "HBM 매출이 증가했다.",
                "exact_short_excerpt": "HBM 매출이 증가했다.",
            }
        ]
        payload["counterfacts"] = [
            {
                "counterfact_id": "CF-000660-001",
                "fact_ids": ["MF-000660-001"],
                "summary": "증가 속도에는 변동성이 있다.",
                "status": "OPEN",
                "current_status": "OPEN",
                "affected_question_ids": [question_id],
                "resolution_or_supersession": "RF-000660-001",
            }
        ]
        payload["resolution_facts"] = [
            {
                "resolution_fact_id": "RF-000660-001",
                "support_fact_ids": ["MF-000660-001"],
                "resolved_or_superseded_fact_ids": ["CF-000660-001"],
                "summary": "공식 실적으로 변동성 우려 일부가 해소됐다.",
                "status": "RESOLVED",
                "current_status": "RESOLVED",
                "affected_question_ids": [question_id],
            }
        ]
        component_ids = (
            "eps_fcf_explosion",
            "earnings_visibility",
            "bottleneck_pricing",
            "market_mispricing",
            "valuation_rerating",
            "capital_allocation",
            "information_confidence",
        )
        payload["component_research"] = [
            {
                "component_id": component_id,
                "positive_fact_ids": (
                    ["MF-000660-001"] if component_id == "eps_fcf_explosion" else []
                ),
                "counter_fact_ids": (
                    ["CF-000660-001"] if component_id == "eps_fcf_explosion" else []
                ),
                "resolution_fact_ids": (
                    ["RF-000660-001"] if component_id == "eps_fcf_explosion" else []
                ),
            }
            for component_id in component_ids
        ]
        payload["source_lineages"] = [
            {
                "source_lineage_id": "LINEAGE-001",
                "canonical_source_urls": ["https://example.com/issuer"],
                "fact_ids": ["MF-000660-001"],
                "lineage_status": "ACCEPTED",
            }
        ]
        payload["search_route_receipts"] = [
            {
                "route_receipt_id": "ROUTE-001",
                "pass_id": "PASS-1",
                "archetype_id": ARCHETYPE,
                "question_family_id": question_id,
                "source_role_id": "ISSUER_OFFICIAL",
                "navigation_objective": "공식 실적 원문 확인",
                "query": "검증대상 공식 실적",
                "result_roster": ["https://example.com/issuer"],
                "opened_url_roster": ["https://example.com/issuer"],
                "accepted_fact_roster": ["MF-000660-001"],
                "rejection_roster": [],
                "provider_status": "NORMAL_AFTER_VERIFIER_REPAIR",
                "performed_at": "2026-08-01T00:00:00Z",
            }
        ]
        payload["research_passes"] = [
            {
                "research_pass_id": "PASS-1",
                "parent_pass_id": "NONE",
                "pass_name": "INITIAL_FULL_RESEARCH",
                "status": "COMPLETE",
                "prompt_hash": "prompt-hash",
                "response_hash": "response-hash",
            }
        ]
        payload["verification_repair_register"] = [
            {"repair_id": "PRO-SELF-REPAIR-1", "status": "CLAIMED_COMPLETE"}
        ]

        adapted = ResearchDossierDialectAdapter().adapt(payload)
        normalized = ResearchDossierNormalizer().normalize(adapted.payload)
        receipt = self.validator.validate(normalized.payload, _context())

        self.assertEqual(len(receipt.fact_ids), 3)
        self.assertEqual(adapted.id_map["MF-000660-001"], "PROFACT-MF-000660-001")
        self.assertEqual(
            normalized.payload["material_facts"][0]["source_url"],
            "https://example.com/issuer",
        )
        self.assertEqual(
            normalized.payload["material_facts"][0]["supporting_excerpt"],
            "HBM 매출이 증가했다.",
        )
        self.assertEqual(normalized.payload["selected_archetypes"], [ARCHETYPE])
        self.assertEqual(normalized.payload["research_passes"][0]["parent_pass_id"], None)
        self.assertEqual(
            normalized.payload["search_route_receipts"][0]["provider_status"],
            "SUCCESS",
        )
        saturation = normalized.payload["research_saturation"]
        self.assertEqual(len(saturation["pro_applied_cross_guards"]), 1)
        self.assertEqual(len(saturation["pro_self_reported_verification_repairs"]), 1)
        self.assertEqual(normalized.payload["verification_repair_register"], [])

    def test_compact_followup_can_anchor_relationship_to_exact_prior_fact(self) -> None:
        prior = _base_v2(complete=True)
        prior["research_pass_id"] = "PASS-PRIOR"
        prior["material_facts"] = [
            {
                "dossier_fact_id": "PROFACT-MF-PRIOR-001",
                "research_pass_id": "PASS-PRIOR",
                "question_family_ids": [],
                "statement": "이전 패스에서 확인한 영업현금흐름이다.",
                "direction": "POSITIVE",
                "target_id": "000660",
                "issuer_scoped": True,
                "economic_mechanism": "OPERATING_CASH_FLOW",
                "predicate": "OPERATING_CASH_FLOW",
                "value": None,
                "unit": None,
                "period": "AS_OF:2026-08-01",
                "event_date": "2026-08-01",
                "current_status": "CURRENT",
                "candidate_components": ["eps_fcf_explosion"],
                "source_url": "https://example.com/prior-filing",
                "source_title": "이전 공시",
                "source_publisher": "검증대상",
                "published_at": "2026-08-01",
                "supporting_excerpt": "영업활동현금흐름 100",
                "source_lineage_id": "LINEAGE-PRIOR",
            }
        ]

        delta = _base_v2(complete=True)
        delta["research_pass_id"] = "PASS-NEXT"
        delta["parent_pass_id"] = "PASS-PRIOR"
        delta["candidate_archetypes"] = []
        delta["selected_archetypes"] = []
        delta["material_facts"] = []
        delta["counterfacts"] = []
        delta["resolution_facts"] = [
            {
                "resolution_fact_id": "RF-NEXT-001",
                "prior_counterfact_ids": ["CF-PRIOR-001"],
                "support_fact_ids": ["MF-PRIOR-001"],
                "resolved_or_superseded_fact_ids": ["CF-PRIOR-001"],
                "current_state_summary": "이전 현금흐름 근거로 우려를 해소했다.",
                "status": "RESOLVED",
                "current_status": "RESOLVED",
                "affected_question_ids": [],
            }
        ]

        with self.assertRaisesRegex(
            DossierDialectError,
            "lacks a source-fact anchor",
        ):
            ResearchDossierDialectAdapter().adapt(delta)

        adapted = ResearchDossierDialectAdapter().adapt(
            delta,
            prior_dossier=prior,
        )
        relationship = adapted.payload["resolution_facts"][0]
        self.assertEqual(
            relationship["source_url"],
            "https://example.com/prior-filing",
        )
        self.assertEqual(
            relationship["supporting_excerpt"],
            "영업활동현금흐름 100",
        )
        self.assertEqual(
            relationship["statement"],
            "이전 현금흐름 근거로 우려를 해소했다.",
        )
        self.assertEqual(
            relationship["source_anchor_fact_ids"],
            ["PROFACT-MF-PRIOR-001"],
        )
        self.assertEqual(
            relationship["prior_counterfact_ids"],
            ["PROFACT-CF-PRIOR-001"],
        )

    def test_compact_followup_rejects_prior_dossier_from_other_scope(self) -> None:
        prior = _base_v2(complete=True)
        prior["research_pass_id"] = "PASS-PRIOR"
        delta = _base_v2(complete=True)
        delta["research_pass_id"] = "PASS-NEXT"
        delta["parent_pass_id"] = "PASS-PRIOR"
        delta["conversation_id"] = "OTHER-CONVERSATION"
        delta["material_facts"] = []
        delta["counterfacts"] = []
        delta["resolution_facts"] = []

        with self.assertRaisesRegex(
            DossierDialectError,
            "scope: conversation_id",
        ):
            ResearchDossierDialectAdapter().adapt(
                delta,
                prior_dossier=prior,
            )

    def test_compact_question_keeps_only_route_owned_by_that_question(self) -> None:
        payload = _base_v2(complete=True)
        first = payload["question_family_results"][0]
        second = payload["question_family_results"][1]
        first["search_route_receipt_ids"] = ["ROUTE-FIRST", "ROUTE-SECOND"]
        payload["search_route_receipts"] = [
            {
                "route_receipt_id": "ROUTE-FIRST",
                "pass_id": "PASS-1",
                "archetype_id": first["archetype_id"],
                "question_family_id": first["question_family_id"],
                "source_role_id": "ISSUER_OFFICIAL",
                "navigation_objective": "첫 질문 경로",
                "result_roster": [],
                "opened_url_roster": [],
                "accepted_fact_roster": [],
                "rejection_roster": [],
                "provider_status": "NORMAL",
                "no_new_route_reason": "추가 결과 없음",
                "performed_at": "2026-08-01T00:00:00Z",
            },
            {
                "route_receipt_id": "ROUTE-SECOND",
                "pass_id": "PASS-1",
                "archetype_id": second["archetype_id"],
                "question_family_id": second["question_family_id"],
                "source_role_id": "ISSUER_OFFICIAL",
                "navigation_objective": "둘째 질문 경로",
                "result_roster": [],
                "opened_url_roster": [],
                "accepted_fact_roster": [],
                "rejection_roster": [],
                "provider_status": "NORMAL",
                "no_new_route_reason": "추가 결과 없음",
                "performed_at": "2026-08-01T00:00:00Z",
            },
        ]

        adapted = ResearchDossierDialectAdapter().adapt(payload)
        canonical = adapted.payload["question_family_results"][0]
        self.assertEqual(
            canonical["search_route_receipt_ids"],
            ["ROUTE-FIRST"],
        )
        self.assertEqual(
            adapted.payload["research_saturation"][
                "pro_cross_question_route_references"
            ],
            [
                {
                    "question_family_id": first["question_family_id"],
                    "route_receipt_ids": ["ROUTE-SECOND"],
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
