from __future__ import annotations

from copy import deepcopy
import unittest

from e2r.pro_first.dossier import (
    DOSSIER_V3_SCHEMA_VERSION,
    DossierValidationContext,
    DossierValidationError,
    ResearchDossierNormalizer,
    ResearchDossierValidator,
    bind_dossier_transport_identity,
)


class ProFirstV3DossierTest(unittest.TestCase):
    target_id = "000660"
    archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
    question_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
    pass_id = "PROPASS-v3-initial"

    def _preflight(self):
        return {
            "source_opened": True,
            "canonical_url_used": True,
            "exact_excerpt_copied_from_source": True,
            "statement_not_broader_than_excerpt": True,
            "single_atomic_predicate": True,
            "target_subject_scope_confirmed": True,
            "publication_date_confirmed": True,
            "as_of_cutoff_pass": True,
            "lineage_duplicate_checked": True,
            "derived_calculation_mixed_into_fact": False,
        }

    def _source(self, source_id="SRC-001", url="https://example.com/filing"):
        return {
            "source_document_id": source_id,
            "canonical_url": url,
            "opened_url": url,
            "source_title": "Official filing",
            "source_publisher": "Issuer",
            "publication_date": "2026-08-20",
            "availability_date": "2026-08-20",
            "source_role_ids": ["OFFICIAL_FILING"],
            "document_type": "FILING",
            "target_scope": {
                "target_id": self.target_id,
                "issuer_scoped": True,
                "subject": "Issuer",
                "business_segment": "CORPORATE_GENERIC",
                "product_family": "CORPORATE_GENERIC",
            },
            "locator_type": "FILING_SECTION",
            "locator_value": "Operating results",
            "lineage_id": "SL-001",
            "opened_and_read": True,
            "as_of_cutoff_pass": True,
        }

    def _fact(
        self,
        fact_id="FACT-001",
        *,
        kind="MATERIAL",
        source_id="SRC-001",
        predicate="REVENUE_GROWTH",
        excerpt="Revenue increased by twenty percent year over year.",
    ):
        return {
            "dossier_fact_id": fact_id,
            "research_pass_id": self.pass_id,
            "fact_kind": kind,
            "statement": excerpt,
            "predicate_id": predicate,
            "direction": "POSITIVE" if kind == "MATERIAL" else "NEGATIVE",
            "target_id": self.target_id,
            "subject": "Revenue",
            "issuer_scoped": True,
            "business_segment": "CORPORATE_GENERIC",
            "product_family": "CORPORATE_GENERIC",
            "economic_mechanism_id": "EARNINGS_CONVERSION",
            "value": 20,
            "unit": "PERCENT",
            "period": "2026-Q2",
            "event_date": "2026-06-30",
            "current_status": "CURRENT",
            "question_family_ids": [self.question_id],
            "candidate_component_ids": ["eps_fcf_explosion"],
            "source_document_id": source_id,
            "supporting_excerpt": excerpt,
            "source_locator": "Operating results / paragraph 2",
            "confidence": 0.0,
            "verifier_preflight": self._preflight(),
        }

    def _dossier(self):
        fact = self._fact()
        return {
            "schema_version": DOSSIER_V3_SCHEMA_VERSION,
            "job_id": "PROJOB-v3",
            "run_id": "PRORUN-v3",
            "conversation_id": "conversation-v3",
            "research_pass_id": self.pass_id,
            "parent_pass_id": None,
            "target": {
                "target_id": self.target_id,
                "symbol": self.target_id,
                "company_name": "Fixture Issuer",
                "aliases": ["Fixture"],
            },
            "as_of_date": "2026-08-23",
            "candidate_archetypes": [self.archetype_id],
            "selected_archetypes": [self.archetype_id],
            "research_status": "NEEDS_PUBLIC_GAP_CLOSURE",
            "business_model": {},
            "source_documents": [self._source()],
            "material_facts": [fact],
            "counterfacts": [],
            "resolution_facts": [],
            "derived_metrics": [],
            "question_family_results": [],
            "component_research": {},
            "structured_metrics": {},
            "unresolved_gaps": [],
            "source_lineages": [
                {
                    "lineage_id": "SL-001",
                    "source_document_ids": ["SRC-001"],
                    "fact_ids": ["FACT-001"],
                    "independence_group_id": "ISSUER-FILING",
                    "status": "ACTIVE",
                }
            ],
            "search_route_receipts": [],
            "research_passes": [
                {
                    "pass_id": self.pass_id,
                    "parent_pass_id": None,
                    "pass_name": "INITIAL_FULL_RESEARCH",
                    "status": "COMPLETE",
                    "prompt_hash": "a" * 64,
                    "response_hash": "b" * 64,
                }
            ],
            "research_saturation": {},
            "score_authority": False,
            "stage_authority": False,
        }

    def _question_result(self, *, question_id=None, support_fact_ids=None):
        return {
            "archetype_id": self.archetype_id,
            "question_family_id": question_id or self.question_id,
            "status": "PARTIALLY_SUPPORTED_SCORING",
            "support_fact_ids": support_fact_ids or ["FACT-001"],
            "counter_fact_ids": [],
            "resolution_fact_ids": [],
            "attempted_source_role_ids": ["OFFICIAL_FILING"],
            "search_route_receipt_ids": [],
            "required_source_roles_satisfied": ["OFFICIAL_FILING"],
            "required_source_roles_missing": [],
            "availability_class": "PUBLIC_SEARCHABLE",
            "affected_component_ids": ["eps_fcf_explosion"],
            "could_change_score": True,
            "could_change_stage": False,
            "could_change_hard_break": False,
            "closure_reason": "One atomic filing fact is available.",
            "adequate_search_proven": False,
        }

    def _context(self, *, conversation_id="conversation-v3"):
        return DossierValidationContext(
            job_id="PROJOB-v3",
            run_id="PRORUN-v3",
            target_id=self.target_id,
            as_of_date="2026-08-23",
            conversation_id=conversation_id,
            candidate_archetype_ids=(self.archetype_id,),
            research_pass_id=self.pass_id,
            parent_pass_id=None,
            enforce_parent_pass_id=True,
        )

    def test_v3_validates_one_document_and_one_atomic_fact(self) -> None:
        receipt = ResearchDossierValidator().validate(
            self._dossier(), self._context()
        )
        self.assertEqual(receipt.schema_version, DOSSIER_V3_SCHEMA_VERSION)
        self.assertEqual(receipt.fact_ids, ("FACT-001",))
        self.assertEqual(receipt.source_document_ids, ("SRC-001",))
        self.assertEqual(receipt.derived_metric_ids, ())
        self.assertEqual(receipt.source_urls, ("https://example.com/filing",))
        self.assertFalse(receipt.score_authority)
        self.assertFalse(receipt.stage_authority)

    def test_same_document_supports_separate_facts_and_derived_metric(self) -> None:
        payload = self._dossier()
        second = self._fact(
            "FACT-002",
            predicate="CASH_CAPEX",
            excerpt="Cash capital expenditure was ten currency units.",
        )
        payload["material_facts"].append(second)
        payload["source_lineages"][0]["fact_ids"].append("FACT-002")
        payload["derived_metrics"] = [
            {
                "derived_metric_id": "DERIVED-FCF",
                "metric_name": "simple_fcf_proxy",
                "formula": "FACT-001 - FACT-002",
                "input_fact_ids": ["FACT-001", "FACT-002"],
                "result_value": 10,
                "unit": "KRW",
                "period": "2026-Q2",
                "researcher_defined": True,
                "issuer_reported_metric": False,
                "score_authority": False,
            }
        ]
        receipt = ResearchDossierValidator().validate(payload, self._context())
        self.assertEqual(receipt.fact_ids, ("FACT-001", "FACT-002"))
        self.assertEqual(len(receipt.source_urls), 1)
        self.assertNotIn("source_url", payload["material_facts"][0])

    def test_future_source_and_duplicate_atomic_identity_are_rejected(self) -> None:
        payload = self._dossier()
        payload["source_documents"][0]["publication_date"] = "2026-08-24"
        with self.assertRaisesRegex(DossierValidationError, "exceeds as_of_date"):
            ResearchDossierValidator().validate(payload, self._context())

        payload = self._dossier()
        duplicate = deepcopy(payload["material_facts"][0])
        duplicate["dossier_fact_id"] = "FACT-002"
        payload["material_facts"].append(duplicate)
        payload["source_lineages"][0]["fact_ids"].append("FACT-002")
        with self.assertRaisesRegex(DossierValidationError, "duplicate atomic"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_source_date_order_and_issuer_scope_must_match(self) -> None:
        payload = self._dossier()
        payload["source_documents"][0]["availability_date"] = "2026-08-19"
        with self.assertRaisesRegex(DossierValidationError, "precedes publication"):
            ResearchDossierValidator().validate(payload, self._context())

        payload = self._dossier()
        payload["material_facts"][0]["issuer_scoped"] = False
        with self.assertRaisesRegex(DossierValidationError, "issuer scope differs"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_question_reference_must_match_fact_question_binding(self) -> None:
        payload = self._dossier()
        payload["material_facts"][0]["question_family_ids"] = [
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02"
        ]
        payload["question_family_results"] = [self._question_result()]
        with self.assertRaisesRegex(DossierValidationError, "another question"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_fact_cannot_repeat_source_url_or_mix_derived_metric(self) -> None:
        for forbidden_key, value in (
            ("source_url", "https://example.com/filing"),
            ("derived_metric_id", "DERIVED-FCF"),
        ):
            with self.subTest(forbidden_key=forbidden_key):
                payload = self._dossier()
                payload["material_facts"][0][forbidden_key] = value
                with self.assertRaisesRegex(
                    DossierValidationError, "schema validation failed"
                ):
                    ResearchDossierValidator().validate(payload, self._context())

    def test_short_nonempty_excerpt_is_preserved_for_downstream_verification(self) -> None:
        payload = self._dossier()
        payload["material_facts"][0]["supporting_excerpt"] = "정기보수 영향"

        receipt = ResearchDossierValidator().validate(payload, self._context())

        self.assertEqual(receipt.fact_ids, ("FACT-001",))

        payload["material_facts"][0]["supporting_excerpt"] = ""
        with self.assertRaisesRegex(DossierValidationError, "schema validation failed"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_unknown_lifecycle_and_failed_preflight_are_rejected(self) -> None:
        payload = self._dossier()
        payload["material_facts"][0]["current_status"] = "UNKNOWN"
        with self.assertRaisesRegex(DossierValidationError, "schema validation failed"):
            ResearchDossierValidator().validate(payload, self._context())

        payload = self._dossier()
        payload["material_facts"][0]["verifier_preflight"][
            "single_atomic_predicate"
        ] = False
        with self.assertRaisesRegex(DossierValidationError, "schema validation failed"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_tracking_url_and_duplicate_document_identity_are_rejected(self) -> None:
        payload = self._dossier()
        payload["source_documents"][0]["canonical_url"] += "?utm_source=x"
        with self.assertRaisesRegex(DossierValidationError, "tracking"):
            ResearchDossierValidator().validate(payload, self._context())

        payload = self._dossier()
        duplicate = self._source("SRC-002")
        payload["source_documents"].append(duplicate)
        payload["source_lineages"][0]["source_document_ids"].append("SRC-002")
        with self.assertRaisesRegex(DossierValidationError, "canonical source URL"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_fact_kind_and_derived_input_graph_are_strict(self) -> None:
        payload = self._dossier()
        payload["material_facts"][0]["fact_kind"] = "COUNTER"
        with self.assertRaisesRegex(DossierValidationError, "fact_kind"):
            ResearchDossierValidator().validate(payload, self._context())

        payload = self._dossier()
        payload["derived_metrics"] = [
            {
                "derived_metric_id": "DERIVED-FCF",
                "metric_name": "fcf",
                "formula": "missing input",
                "input_fact_ids": ["FACT-MISSING"],
                "result_value": None,
                "unit": "KRW",
                "period": None,
                "researcher_defined": True,
                "issuer_reported_metric": False,
                "score_authority": False,
            }
        ]
        with self.assertRaisesRegex(DossierValidationError, "missing atomic input"):
            ResearchDossierValidator().validate(payload, self._context())

    def test_provider_pending_can_preserve_an_empty_evidence_graph(self) -> None:
        payload = self._dossier()
        payload["research_status"] = "PROVIDER_PENDING"
        payload["source_documents"] = []
        payload["material_facts"] = []
        payload["source_lineages"] = []
        receipt = ResearchDossierValidator().validate(payload, self._context())
        self.assertEqual(receipt.fact_ids, ())
        self.assertEqual(receipt.source_urls, ())

    def test_normalizer_sorts_v3_registries_without_rewriting_urls(self) -> None:
        payload = self._dossier()
        second_source = self._source("SRC-000", "https://example.com/earlier")
        second_source["lineage_id"] = "SL-000"
        payload["source_documents"].append(second_source)
        payload["source_lineages"].append(
            {
                "lineage_id": "SL-000",
                "source_document_ids": ["SRC-000"],
                "fact_ids": [],
                "independence_group_id": "SECOND",
                "status": "ACTIVE",
            }
        )
        normalized = ResearchDossierNormalizer().normalize(payload)
        self.assertEqual(
            [row["source_document_id"] for row in normalized.payload["source_documents"]],
            ["SRC-000", "SRC-001"],
        )
        self.assertIn("SORT_SOURCE_DOCUMENT_REGISTRY", normalized.operations)
        self.assertEqual(
            {row["canonical_url"] for row in normalized.payload["source_documents"]},
            {"https://example.com/earlier", "https://example.com/filing"},
        )

    def test_initial_transport_identity_binding_supports_v3(self) -> None:
        payload = self._dossier()
        payload["conversation_id"] = "PENDING_INITIAL_CONVERSATION"
        bound = bind_dossier_transport_identity(
            payload,
            conversation_id="captured-conversation",
            research_pass_id=self.pass_id,
            parent_pass_id=None,
            allow_initial_conversation_placeholder=True,
            pass_name="INITIAL_FULL_RESEARCH",
            prompt_hash="c" * 64,
            response_hash="d" * 64,
        )
        self.assertEqual(bound.payload["conversation_id"], "captured-conversation")
        self.assertEqual(
            bound.payload["material_facts"], payload["material_facts"]
        )
        self.assertEqual(
            bound.payload["research_passes"][0]["prompt_hash"], "c" * 64
        )

    def test_validator_keeps_v1_v2_and_v3_schema_compatibility(self) -> None:
        validator = ResearchDossierValidator()
        self.assertEqual(
            set(validator.validators),
            {
                "e2r_pro_research_dossier_v1",
                "e2r_pro_research_dossier_v2",
                "e2r_pro_research_dossier_v3",
            },
        )


if __name__ == "__main__":
    unittest.main()
