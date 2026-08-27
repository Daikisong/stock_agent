from __future__ import annotations

from copy import deepcopy
import unittest

from e2r.pro_first.dossier import (
    DOSSIER_V3_SCHEMA_VERSION,
    DossierDeltaMergeError,
    DossierValidationContext,
    DossierValidationError,
    ResearchDossierNormalizer,
    ResearchDossierValidator,
    apply_research_dossier_delta,
    bind_dossier_transport_identity,
)
from e2r.pro_first.dossier.delta_merge import (
    _project_overclaimed_route_closures,
)
from e2r.pro_first.saturation import ResearchSaturationAdjudicator
from e2r.pro_first.saturation.question_closure import (
    compile_question_closure_decision,
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

    def test_v3_document_lineage_and_roles_feed_saturation(self) -> None:
        payload = self._dossier()
        route = {
            "route_receipt_id": "ROUTE-V3-001",
            "pass_id": self.pass_id,
            "archetype_id": self.archetype_id,
            "question_family_id": self.question_id,
            "gap_id": "GAP-V3-001",
            "source_role_id": "OFFICIAL_FILING",
            "query_or_navigation_objective": "Open the official filing",
            "query_text": "issuer official filing",
            "result_count_seen": 1,
            "opened_source_urls": ["https://example.com/filing"],
            "accepted_fact_ids": ["FACT-001"],
            "rejected_candidate_ids": [],
            "provider_status": "SUCCESS",
            "no_new_route_reason": None,
            "performed_at": "2026-08-22T00:00:00Z",
        }
        question = self._question_result()
        question["search_route_receipt_ids"] = ["ROUTE-V3-001"]
        payload["search_route_receipts"] = [route]
        payload["question_family_results"] = [question]

        decision = compile_question_closure_decision(
            question_contract={
                "question_family_id": self.question_id,
                "mandatory_for_full_thesis": True,
                "required_source_roles": ["OFFICIAL_FILING"],
                "question_roles": ["ECONOMIC_BRIDGE"],
                "could_change_score": True,
                "could_change_stage": False,
                "could_change_hard_break": False,
                "affected_component_ids": ["eps_fcf_explosion"],
                "adequate_search_requirements": {
                    "minimum_distinct_source_routes": 1,
                    "official_route_attempt_required": True,
                    "independent_no_new_route_confirmations_for_absence": 2,
                },
            },
            question_result=question,
            dossier_facts=payload["material_facts"],
            source_lineages=payload["source_lineages"],
            source_documents=payload["source_documents"],
            route_receipts=payload["search_route_receipts"],
            verified_fact_ids=frozenset({"FACT-001"}),
        )

        self.assertTrue(decision.question_to_source_linkage_complete)
        self.assertEqual(decision.linked_source_lineage_ids, ("SL-001",))
        self.assertIn("OFFICIAL_FILING", decision.verified_source_roles)
        self.assertNotIn(
            "QUESTION_FACT_MISSING_SOURCE_LINEAGE",
            decision.failure_codes,
        )
        saturation = ResearchSaturationAdjudicator().adjudicate(
            dossier=payload,
            verified_fact_ids=("FACT-001",),
        )
        q01 = next(
            row
            for row in saturation.question_decisions
            if row.question_family_id == self.question_id
        )
        self.assertEqual(q01.linked_source_lineage_ids, ("SL-001",))
        self.assertNotIn(
            "QUESTION_FACT_MISSING_SOURCE_LINEAGE",
            q01.failure_codes,
        )

    def test_v3_followup_delta_extends_existing_lineage_without_v2_fields(self) -> None:
        original = self._dossier()
        original["search_route_receipts"] = [
            {
                "route_receipt_id": "ROUTE-V3-PARSER-PENDING",
                "pass_id": self.pass_id,
                "archetype_id": self.archetype_id,
                "question_family_id": self.question_id,
                "gap_id": "GAP-V3-PARSER",
                "source_role_id": "OFFICIAL_FILING",
                "query_or_navigation_objective": "Read an oversized filing",
                "query_text": "issuer oversized filing",
                "result_count_seen": 1,
                "opened_source_urls": ["https://example.com/filing"],
                "accepted_fact_ids": [],
                "rejected_candidate_ids": [],
                "provider_status": "PARSER_PENDING",
                "no_new_route_reason": "The full text was not parser-readable.",
                "performed_at": "2026-08-21T01:00:00Z",
            }
        ]
        response = self._dossier()
        response["research_pass_id"] = "PROPASS-v3-followup"
        response["parent_pass_id"] = self.pass_id
        response["candidate_archetypes"] = []
        response["selected_archetypes"] = []
        response["source_documents"] = [
            {
                **self._source(
                    "SRC-002",
                    "https://example.com/followup-filing",
                ),
                "lineage_id": "SL-001",
            }
        ]
        followup_fact = self._fact(
            "FACT-002",
            source_id="SRC-002",
            predicate="FREE_CASH_FLOW",
            excerpt="Free cash flow was positive in the current period.",
        )
        followup_fact["research_pass_id"] = "PROPASS-v3-followup"
        response["material_facts"] = [followup_fact]
        response["counterfacts"] = []
        response["resolution_facts"] = []
        response["source_lineages"] = [
            {
                "lineage_id": "SL-001",
                "source_document_ids": ["SRC-002"],
                "fact_ids": ["FACT-002"],
                "independence_group_id": "PRO-RELABELED-ISSUER-FILING",
                "status": "ACTIVE",
            }
        ]
        response["search_route_receipts"] = [
            {
                "route_receipt_id": "ROUTE-V3-002",
                "pass_id": "PROPASS-v3-followup",
                "archetype_id": self.archetype_id,
                "question_family_id": self.question_id,
                "gap_id": "GAP-V3-002",
                "source_role_id": "OFFICIAL_FILING",
                "query_or_navigation_objective": "Open a newer official filing",
                "query_text": "issuer followup official filing",
                "result_count_seen": 1,
                "opened_source_urls": [
                    "https://example.com/followup-filing"
                ],
                "accepted_fact_ids": ["FACT-002"],
                "rejected_candidate_ids": [],
                "provider_status": "SUCCESS",
                "no_new_route_reason": None,
                "performed_at": "2026-08-22T01:00:00Z",
            }
        ]
        response["research_passes"] = [
            {
                "pass_id": "PROPASS-v3-followup",
                "parent_pass_id": self.pass_id,
                "pass_name": "PUBLIC_GAP_CLOSURE",
                "status": "COMPLETE",
                "prompt_hash": "c" * 64,
                "response_hash": "d" * 64,
            }
        ]
        question = self._question_result()
        question.update(
            {
                "status": "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
                "support_fact_ids": [],
                "required_source_roles_satisfied": [],
                "required_source_roles_missing": ["OFFICIAL_FILING"],
                "search_route_receipt_ids": [
                    "ROUTE-V3-PARSER-PENDING",
                    "ROUTE-V3-002",
                ],
                "availability_class": "PUBLIC_SEARCHABLE",
                "adequate_search_proven": True,
                "closure_reason": "The follow-up reported an adequate absence.",
            }
        )
        response["question_family_results"] = [question]
        response["derived_metrics"] = []

        merged = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id="PROPASS-v3-followup",
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )

        self.assertEqual(merged.new_fact_ids, ("FACT-002",))
        self.assertEqual(merged.new_source_lineage_ids, ())
        self.assertEqual(merged.new_route_receipt_ids, ("ROUTE-V3-002",))
        self.assertEqual(
            {row["source_document_id"] for row in merged.effective_dossier["source_documents"]},
            {"SRC-001", "SRC-002"},
        )
        self.assertEqual(
            merged.effective_dossier["source_lineages"],
            [
                {
                    "lineage_id": "SL-001",
                    "source_document_ids": ["SRC-001", "SRC-002"],
                    "fact_ids": ["FACT-001", "FACT-002"],
                    "independence_group_id": "ISSUER-FILING",
                    "status": "ACTIVE",
                }
            ],
        )
        lineage_projection = merged.effective_dossier["research_saturation"][
            "v3_source_lineage_identity_projections"
        ][0]
        self.assertEqual(lineage_projection["lineage_id"], "SL-001")
        self.assertEqual(
            [
                row["field_name"]
                for row in lineage_projection["preserved_fields"]
            ],
            ["independence_group_id"],
        )
        self.assertFalse(lineage_projection["incoming_identity_adopted"])
        self.assertTrue(
            lineage_projection["new_document_and_fact_edges_allowed"]
        )
        self.assertNotIn("proposed_score_ranges", merged.effective_dossier)
        projected_question = merged.effective_dossier["question_family_results"][0]
        self.assertEqual(projected_question["status"], "SOURCE_PENDING")
        self.assertEqual(
            projected_question["availability_class"], "PUBLIC_SEARCHABLE"
        )
        self.assertFalse(projected_question["adequate_search_proven"])
        self.assertEqual(
            merged.effective_dossier["research_status"],
            "NEEDS_PUBLIC_GAP_CLOSURE",
        )
        projection = merged.effective_dossier["research_saturation"][
            "route_truth_question_status_projections"
        ][0]
        self.assertEqual(projection["reported_status"], "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH")
        self.assertEqual(projection["projected_status"], "SOURCE_PENDING")
        self.assertIn("INSUFFICIENT_ROUTE_RECEIPTS", projection["failure_codes"])
        ResearchDossierValidator().validate(
            merged.effective_dossier,
            DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id="PROPASS-v3-followup",
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )

        closed_response = deepcopy(response)
        second_current_route = deepcopy(response["search_route_receipts"][0])
        second_current_route.update(
            {
                "route_receipt_id": "ROUTE-V3-003",
                "query_or_navigation_objective": (
                    "Confirm the current absence through another official route"
                ),
                "query_text": "issuer second official absence check",
                "opened_source_urls": [
                    "https://example.com/second-official-route"
                ],
                "accepted_fact_ids": [],
                "no_new_route_reason": (
                    "The second current official route found no additional fact."
                ),
                "performed_at": "2026-08-22T01:05:00Z",
            }
        )
        closed_response["search_route_receipts"].append(second_current_route)
        closed_response["question_family_results"][0][
            "search_route_receipt_ids"
        ] = [
            "ROUTE-V3-PARSER-PENDING",
            "ROUTE-V3-002",
            "ROUTE-V3-003",
        ]
        closed = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=closed_response,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id="PROPASS-v3-followup",
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )
        closed_question = closed.effective_dossier["question_family_results"][0]
        self.assertEqual(
            closed_question["status"],
            "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
        )
        self.assertEqual(
            closed_question["search_route_receipt_ids"],
            [
                "ROUTE-V3-PARSER-PENDING",
                "ROUTE-V3-002",
                "ROUTE-V3-003",
            ],
        )
        self.assertEqual(
            closed.new_route_receipt_ids,
            ("ROUTE-V3-002", "ROUTE-V3-003"),
        )
        self.assertNotIn(
            "route_truth_question_status_projections",
            closed.effective_dossier.get("research_saturation") or {},
        )

        omitted_lineage = deepcopy(response)
        omitted_lineage["source_lineages"] = []
        graph_projected = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=omitted_lineage,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id="PROPASS-v3-followup",
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )
        self.assertEqual(
            graph_projected.effective_dossier["source_lineages"][0]["fact_ids"],
            ["FACT-001", "FACT-002"],
        )
        extension = graph_projected.effective_dossier["research_saturation"][
            "v3_graph_lineage_roster_extensions"
        ][0]
        self.assertEqual(extension["lineage_id"], "SL-001")
        self.assertEqual(extension["added_fact_ids"], ["FACT-002"])
        self.assertEqual(extension["added_source_document_ids"], ["SRC-002"])

        detached = deepcopy(response)
        detached["source_documents"].append(
            {
                **self._source(
                    "SRC-003",
                    "https://example.com/unattached-filing",
                ),
                "lineage_id": "SL-003",
            }
        )
        with self.assertRaisesRegex(DossierDeltaMergeError, "detached"):
            apply_research_dossier_delta(
                original_dossier=original,
                response_dossier=detached,
                validation_context=DossierValidationContext(
                    job_id="PROJOB-v3",
                    run_id="PRORUN-v3",
                    target_id=self.target_id,
                    as_of_date="2026-08-23",
                    conversation_id="conversation-v3",
                    candidate_archetype_ids=(self.archetype_id,),
                    research_pass_id="PROPASS-v3-followup",
                    parent_pass_id=self.pass_id,
                    enforce_parent_pass_id=True,
                ),
            )

    def test_historical_failed_route_is_audited_but_not_relabelled_as_current(self) -> None:
        question_id = self.question_id
        effective = {
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-HISTORICAL-PARSER-PENDING",
                    "pass_id": "PASS-HISTORICAL",
                    "provider_status": "PARSER_PENDING",
                },
                {
                    "route_receipt_id": "ROUTE-CURRENT-SUCCESS-1",
                    "pass_id": "PASS-CURRENT",
                    "provider_status": "SUCCESS",
                },
                {
                    "route_receipt_id": "ROUTE-CURRENT-SUCCESS-2",
                    "pass_id": "PASS-CURRENT",
                    "provider_status": "SUCCESS",
                },
            ],
            "question_family_results": [
                {
                    "question_family_id": question_id,
                    "status": "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
                    "adequate_search_proven": True,
                    "availability_class": "PUBLIC_SEARCHABLE",
                    "closure_reason": "Current routes found no newer public fact.",
                    "search_route_receipt_ids": [
                        "ROUTE-HISTORICAL-PARSER-PENDING",
                        "ROUTE-CURRENT-SUCCESS-1",
                        "ROUTE-CURRENT-SUCCESS-2",
                    ],
                }
            ],
        }
        current_question = {
            "question_family_id": question_id,
            "status": "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
            "adequate_search_proven": True,
            "search_route_receipt_ids": [
                "ROUTE-CURRENT-SUCCESS-1",
                "ROUTE-CURRENT-SUCCESS-2",
            ],
        }

        _project_overclaimed_route_closures(
            effective,
            current_question_results=(current_question,),
        )

        projected = effective["question_family_results"][0]
        self.assertEqual(
            projected["status"],
            "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
        )
        self.assertEqual(
            projected["search_route_receipt_ids"],
            [
                "ROUTE-HISTORICAL-PARSER-PENDING",
                "ROUTE-CURRENT-SUCCESS-1",
                "ROUTE-CURRENT-SUCCESS-2",
            ],
        )
        self.assertNotIn(
            "route_truth_question_status_projections",
            effective.get("research_saturation") or {},
        )

    def test_followup_coalesces_exact_prior_atomic_fact_without_rewriting_it(self):
        original = self._dossier()
        original["question_family_results"] = [self._question_result()]
        duplicate = deepcopy(original["material_facts"][0])
        duplicate.update(
            {
                "dossier_fact_id": "FACT-REPEATED-BY-FOLLOWUP",
                "research_pass_id": "PROPASS-v3-followup-duplicate",
                "statement": "The same filing atom was restated by the follow-up.",
                "confidence": 0.99,
            }
        )
        question = self._question_result(
            support_fact_ids=["FACT-REPEATED-BY-FOLLOWUP"]
        )
        question["search_route_receipt_ids"] = ["ROUTE-FOLLOWUP-DUPLICATE"]
        response = deepcopy(original)
        response.update(
            {
                "research_pass_id": "PROPASS-v3-followup-duplicate",
                "parent_pass_id": self.pass_id,
                "candidate_archetypes": [],
                "selected_archetypes": [],
                "source_documents": [],
                "material_facts": [duplicate],
                "counterfacts": [],
                "resolution_facts": [],
                "derived_metrics": [],
                "question_family_results": [question],
                "unresolved_gaps": [],
                "source_lineages": [
                    {
                        "lineage_id": "SL-001",
                        "source_document_ids": ["SRC-001"],
                        "fact_ids": ["FACT-REPEATED-BY-FOLLOWUP"],
                        "independence_group_id": "ISSUER-FILING",
                        "status": "ACTIVE",
                    }
                ],
                "search_route_receipts": [
                    {
                        "route_receipt_id": "ROUTE-FOLLOWUP-DUPLICATE",
                        "pass_id": "PROPASS-v3-followup-duplicate",
                        "archetype_id": self.archetype_id,
                        "question_family_id": self.question_id,
                        "gap_id": "GAP-FOLLOWUP-DUPLICATE",
                        "source_role_id": "OFFICIAL_FILING",
                        "query_or_navigation_objective": "Re-open the official filing.",
                        "query_text": None,
                        "result_count_seen": 1,
                        "opened_source_urls": ["https://example.com/filing"],
                        "accepted_fact_ids": ["FACT-REPEATED-BY-FOLLOWUP"],
                        "rejected_candidate_ids": [],
                        "provider_status": "SUCCESS",
                        "no_new_route_reason": None,
                        "performed_at": "2026-08-23T01:00:00Z",
                    }
                ],
                "research_passes": [
                    {
                        "pass_id": "PROPASS-v3-followup-duplicate",
                        "parent_pass_id": self.pass_id,
                        "pass_name": "PUBLIC_GAP_CLOSURE",
                        "status": "COMPLETE",
                        "prompt_hash": "c" * 64,
                        "response_hash": "d" * 64,
                    }
                ],
                "research_saturation": {
                    "new_verified_fact_ids_expected": [
                        "FACT-REPEATED-BY-FOLLOWUP"
                    ]
                },
            }
        )

        merged = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id="PROPASS-v3-followup-duplicate",
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )

        self.assertEqual(merged.new_fact_ids, ())
        self.assertEqual(len(merged.effective_dossier["material_facts"]), 1)
        self.assertEqual(
            merged.effective_dossier["material_facts"][0],
            original["material_facts"][0],
        )
        self.assertEqual(
            merged.effective_dossier["question_family_results"][0][
                "support_fact_ids"
            ],
            ["FACT-001"],
        )
        self.assertEqual(
            merged.effective_dossier["search_route_receipts"][0][
                "accepted_fact_ids"
            ],
            ["FACT-001"],
        )
        self.assertEqual(
            merged.effective_dossier["source_lineages"][0]["fact_ids"],
            ["FACT-001"],
        )
        self.assertEqual(
            merged.effective_dossier["research_saturation"][
                "new_verified_fact_ids_expected"
            ],
            ["FACT-001"],
        )
        projection = merged.effective_dossier["research_saturation"][
            "v3_duplicate_atomic_fact_projections"
        ][0]
        self.assertEqual(
            projection["duplicate_fact_id"],
            "FACT-REPEATED-BY-FOLLOWUP",
        )
        self.assertEqual(projection["canonical_fact_id"], "FACT-001")
        self.assertFalse(projection["incoming_fact_content_adopted"])

    def test_followup_reuses_prior_source_document_for_same_url_and_scope(self):
        original = self._dossier()
        original["question_family_results"] = [self._question_result()]
        pass_id = "PROPASS-v3-followup-source-reuse"
        repeated_source = self._source(
            "SRC-REPEATED-BY-FOLLOWUP",
            "https://example.com/filing",
        )
        new_fact = self._fact(
            "FACT-002",
            source_id="SRC-REPEATED-BY-FOLLOWUP",
            predicate="OPERATING_CASH_FLOW_GROWTH",
            excerpt="Operating cash flow increased during the reported quarter.",
        )
        new_fact["research_pass_id"] = pass_id
        question = self._question_result(support_fact_ids=["FACT-002"])
        question["search_route_receipt_ids"] = ["ROUTE-SOURCE-REUSE"]
        response = deepcopy(original)
        response.update(
            {
                "research_pass_id": pass_id,
                "parent_pass_id": self.pass_id,
                "candidate_archetypes": [],
                "selected_archetypes": [],
                "source_documents": [repeated_source],
                "material_facts": [new_fact],
                "counterfacts": [],
                "resolution_facts": [],
                "derived_metrics": [],
                "question_family_results": [question],
                "unresolved_gaps": [],
                "source_lineages": [
                    {
                        "lineage_id": "SL-001",
                        "source_document_ids": ["SRC-REPEATED-BY-FOLLOWUP"],
                        "fact_ids": ["FACT-002"],
                        "independence_group_id": "ISSUER-FILING",
                        "status": "ACTIVE",
                    }
                ],
                "search_route_receipts": [
                    {
                        "route_receipt_id": "ROUTE-SOURCE-REUSE",
                        "pass_id": pass_id,
                        "archetype_id": self.archetype_id,
                        "question_family_id": self.question_id,
                        "gap_id": "GAP-SOURCE-REUSE",
                        "source_role_id": "OFFICIAL_FILING",
                        "query_or_navigation_objective": (
                            "Re-open the same issuer filing for another atom."
                        ),
                        "query_text": None,
                        "result_count_seen": 1,
                        "opened_source_urls": ["https://example.com/filing"],
                        "accepted_fact_ids": ["FACT-002"],
                        "rejected_candidate_ids": [],
                        "provider_status": "SUCCESS",
                        "no_new_route_reason": None,
                        "performed_at": "2026-08-23T02:00:00Z",
                    }
                ],
                "research_passes": [
                    {
                        "pass_id": pass_id,
                        "parent_pass_id": self.pass_id,
                        "pass_name": "PUBLIC_GAP_CLOSURE",
                        "status": "COMPLETE",
                        "prompt_hash": "e" * 64,
                        "response_hash": "f" * 64,
                    }
                ],
                "research_saturation": {
                    "new_source_document_ids_expected": [
                        "SRC-REPEATED-BY-FOLLOWUP"
                    ],
                    "new_verified_fact_ids_expected": ["FACT-002"],
                },
            }
        )

        merged = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id=pass_id,
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )

        self.assertEqual(merged.new_fact_ids, ("FACT-002",))
        self.assertEqual(
            [
                row["source_document_id"]
                for row in merged.effective_dossier["source_documents"]
            ],
            ["SRC-001"],
        )
        self.assertEqual(
            merged.effective_dossier["material_facts"][1]["source_document_id"],
            "SRC-001",
        )
        self.assertEqual(
            merged.effective_dossier["source_lineages"][0]["source_document_ids"],
            ["SRC-001"],
        )
        projection = merged.effective_dossier["research_saturation"][
            "v3_duplicate_source_document_projections"
        ][0]
        self.assertEqual(projection["action"], "REUSE_PRIOR_CANONICAL_DOCUMENT")
        self.assertTrue(projection["target_scope_compatible"])
        self.assertFalse(projection["incoming_document_content_adopted"])

        same_pass_duplicate = deepcopy(response)
        same_pass_duplicate["source_documents"].append(
            self._source(
                "SRC-SECOND-SAME-PASS-DUPLICATE",
                "https://example.com/filing",
            )
        )
        with self.assertRaisesRegex(DossierDeltaMergeError, "canonical source URL"):
            apply_research_dossier_delta(
                original_dossier=original,
                response_dossier=same_pass_duplicate,
                validation_context=DossierValidationContext(
                    job_id="PROJOB-v3",
                    run_id="PRORUN-v3",
                    target_id=self.target_id,
                    as_of_date="2026-08-23",
                    conversation_id="conversation-v3",
                    candidate_archetype_ids=(self.archetype_id,),
                    research_pass_id=pass_id,
                    parent_pass_id=self.pass_id,
                    enforce_parent_pass_id=True,
                ),
            )

    def test_followup_drops_only_facts_from_same_url_with_conflicting_scope(self):
        original = self._dossier()
        original["question_family_results"] = [self._question_result()]
        pass_id = "PROPASS-v3-followup-source-scope-conflict"
        conflicting_source = self._source(
            "SRC-SUBSIDIARY-SCOPE",
            "https://example.com/filing",
        )
        conflicting_source["target_scope"].update(
            {"issuer_scoped": False, "subject": "Issuer subsidiary"}
        )
        conflicting_fact = self._fact(
            "FACT-SUBSIDIARY-SCOPE",
            kind="RESOLUTION",
            source_id="SRC-SUBSIDIARY-SCOPE",
            predicate="SUBSIDIARY_AUDIT_STATUS",
            excerpt="The cited filing concerns a subsidiary-specific audit status.",
        )
        conflicting_fact.update(
            {
                "research_pass_id": pass_id,
                "issuer_scoped": False,
                "subject": "Issuer subsidiary",
                "direction": "NEUTRAL",
            }
        )
        question = self._question_result()
        question["support_fact_ids"] = []
        question["resolution_fact_ids"] = ["FACT-SUBSIDIARY-SCOPE"]
        question["search_route_receipt_ids"] = ["ROUTE-SCOPE-CONFLICT"]
        response = deepcopy(original)
        response.update(
            {
                "research_pass_id": pass_id,
                "parent_pass_id": self.pass_id,
                "candidate_archetypes": [],
                "selected_archetypes": [],
                "source_documents": [conflicting_source],
                "material_facts": [],
                "counterfacts": [],
                "resolution_facts": [conflicting_fact],
                "derived_metrics": [],
                "question_family_results": [question],
                "unresolved_gaps": [],
                "source_lineages": [
                    {
                        "lineage_id": "SL-SUBSIDIARY-SCOPE",
                        "source_document_ids": ["SRC-SUBSIDIARY-SCOPE"],
                        "fact_ids": ["FACT-SUBSIDIARY-SCOPE"],
                        "independence_group_id": "SUBSIDIARY-FILING",
                        "status": "ACTIVE",
                    }
                ],
                "search_route_receipts": [
                    {
                        "route_receipt_id": "ROUTE-SCOPE-CONFLICT",
                        "pass_id": pass_id,
                        "archetype_id": self.archetype_id,
                        "question_family_id": self.question_id,
                        "gap_id": "GAP-SCOPE-CONFLICT",
                        "source_role_id": "OFFICIAL_FILING",
                        "query_or_navigation_objective": (
                            "Check whether the filing is issuer- or subsidiary-scoped."
                        ),
                        "query_text": None,
                        "result_count_seen": 1,
                        "opened_source_urls": ["https://example.com/filing"],
                        "accepted_fact_ids": ["FACT-SUBSIDIARY-SCOPE"],
                        "rejected_candidate_ids": [],
                        "provider_status": "SUCCESS",
                        "no_new_route_reason": None,
                        "performed_at": "2026-08-23T03:00:00Z",
                    }
                ],
                "research_passes": [
                    {
                        "pass_id": pass_id,
                        "parent_pass_id": self.pass_id,
                        "pass_name": "PUBLIC_GAP_CLOSURE",
                        "status": "COMPLETE",
                        "prompt_hash": "1" * 64,
                        "response_hash": "2" * 64,
                    }
                ],
                "research_saturation": {
                    "new_source_document_ids_expected": ["SRC-SUBSIDIARY-SCOPE"],
                    "new_verified_fact_ids_expected": ["FACT-SUBSIDIARY-SCOPE"],
                },
            }
        )

        merged = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id=pass_id,
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )

        self.assertEqual(merged.new_fact_ids, ())
        self.assertEqual(
            merged.effective_dossier["source_documents"],
            original["source_documents"],
        )
        self.assertEqual(
            merged.effective_dossier["material_facts"],
            original["material_facts"],
        )
        self.assertEqual(merged.effective_dossier["resolution_facts"], [])
        self.assertEqual(
            merged.effective_dossier["search_route_receipts"][0]["accepted_fact_ids"],
            [],
        )
        self.assertEqual(
            merged.effective_dossier["source_lineages"],
            original["source_lineages"],
        )
        projection = merged.effective_dossier["research_saturation"][
            "v3_duplicate_source_document_projections"
        ][0]
        self.assertEqual(
            projection["action"],
            "DROP_SCOPE_CONFLICTING_DUPLICATE_DOCUMENT_AND_FACTS",
        )
        self.assertFalse(projection["target_scope_compatible"])
        self.assertEqual(
            projection["dropped_fact_ids"],
            ["FACT-SUBSIDIARY-SCOPE"],
        )

    def test_followup_drops_prior_fact_reference_without_fact_backlink(self):
        original = self._dossier()
        original["question_family_results"] = [self._question_result()]
        response = deepcopy(original)
        response["research_pass_id"] = "PROPASS-v3-followup-unbound"
        response["parent_pass_id"] = self.pass_id
        response["candidate_archetypes"] = []
        response["selected_archetypes"] = []
        response["source_documents"] = []
        response["material_facts"] = []
        response["counterfacts"] = []
        response["resolution_facts"] = []
        response["derived_metrics"] = []
        response["source_lineages"] = []
        response["search_route_receipts"] = []
        response["unresolved_gaps"] = []
        response["research_passes"] = [
            {
                "pass_id": "PROPASS-v3-followup-unbound",
                "parent_pass_id": self.pass_id,
                "pass_name": "PUBLIC_GAP_CLOSURE",
                "status": "COMPLETE",
                "prompt_hash": "c" * 64,
                "response_hash": "d" * 64,
            }
        ]
        second_question_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02"
        second_question = self._question_result(
            question_id=second_question_id,
            support_fact_ids=["FACT-001"],
        )
        second_question.update(
            {
                "status": "UNKNOWN_ROUTE_NOT_YET_TESTED",
                "required_source_roles_satisfied": [],
                "required_source_roles_missing": ["OFFICIAL_FILING"],
                "closure_reason": "No route has been tested for this question.",
                "adequate_search_proven": False,
            }
        )
        response["question_family_results"] = [second_question]

        merged = apply_research_dossier_delta(
            original_dossier=original,
            response_dossier=response,
            validation_context=DossierValidationContext(
                job_id="PROJOB-v3",
                run_id="PRORUN-v3",
                target_id=self.target_id,
                as_of_date="2026-08-23",
                conversation_id="conversation-v3",
                candidate_archetype_ids=(self.archetype_id,),
                research_pass_id="PROPASS-v3-followup-unbound",
                parent_pass_id=self.pass_id,
                enforce_parent_pass_id=True,
            ),
        )

        projected = next(
            row
            for row in merged.effective_dossier["question_family_results"]
            if row["question_family_id"] == second_question_id
        )
        self.assertEqual(projected["support_fact_ids"], [])
        self.assertEqual(
            merged.effective_dossier["material_facts"][0][
                "question_family_ids"
            ],
            [self.question_id],
        )
        projection = merged.effective_dossier["research_saturation"][
            "v3_question_fact_reference_projections"
        ][0]
        self.assertEqual(projection["question_family_id"], second_question_id)
        self.assertEqual(
            projection["dropped_references"],
            [
                {
                    "fact_id": "FACT-001",
                    "reason": "MISSING_FACT_BACKLINK",
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
