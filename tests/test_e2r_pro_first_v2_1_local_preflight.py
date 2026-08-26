from __future__ import annotations

from copy import deepcopy
from datetime import date, datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.ids import canonical_hash, canonical_json
from e2r.pro_first.dossier import (
    CANONICAL_COMPONENT_IDS,
    bind_dossier_transport_identity,
)
from e2r.pro_first.dossier.validator import (
    DossierValidationContext,
    DossierValidationError,
    ResearchDossierValidator,
)
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.state_machine import TransitionContext
from e2r.pro_first.preflight import (
    CanonicalURLResolver,
    DatePrecedenceResolver,
    IssuerAliasResolver,
    LocalEvidencePreflightService,
    PreSchemaV3Normalizer,
    RejectionClassifier,
    RejectionRootCauseClass,
    TextQuoteNormalizer,
    split_compound_fact,
)
from e2r.pro_first.verification import (
    AsOfDateVerifier,
    ExactQuoteVerifier,
    ProSourceVerificationService,
    ProSourceVerifier,
    SubjectScopeVerifier,
)
from e2r.research.page_fetcher import FetchResult


class _CountingFetcher:
    def __init__(self, results: dict[str, FetchResult]) -> None:
        self.results = results
        self.calls: list[tuple[str, str]] = []

    def fetch(self, url: str, *, as_of_date: date) -> FetchResult:
        self.calls.append((url, as_of_date.isoformat()))
        return self.results.get(
            url,
            FetchResult(url=url, ok=False, reason="fixture URL unavailable"),
        )


class ProFirstV21LocalPreflightTest(unittest.TestCase):
    target_id = "123456"
    company_name = "검증기업"
    as_of_date = "2026-08-22"
    raw_url = "HTTPS://EXAMPLE.COM/report/?utm_source=test&b=2&a=1#section"
    canonical_url = "https://example.com/report?a=1&b=2"
    excerpt = "검증기업은 MEMORY 사업의 HBM capacity가 전량 배정됐다고 밝혔다."

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        root = Path(self.temporary_directory.name)
        self.job_root = root / "job"
        self.store = ProFirstJobStore(
            root / "preflight.sqlite3",
            now=lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc),
        )
        candidate = self.store.create_candidate(
            symbol=self.target_id,
            company_name=self.company_name,
            as_of_date=self.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="local-preflight",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        self.job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
        )

    def test_tracking_query_fragment_trailing_slash_and_query_order_fixed_locally(self) -> None:
        resolved = CanonicalURLResolver().resolve(self.raw_url)
        self.assertEqual(resolved.canonical_url, self.canonical_url)
        self.assertEqual(resolved.removed_query_keys, ("utm_source",))
        self.assertTrue(resolved.fragment_removed)
        self.assertTrue(resolved.trailing_slash_removed)

    def test_windows_newline_html_entity_and_unicode_quote_normalized_locally(self) -> None:
        normalizer = TextQuoteNormalizer()
        left = normalizer.normalize_text("A\r\nB &amp; C").normalized_text
        right = normalizer.normalize_text("A\nB & C").normalized_text
        self.assertEqual(left, right)
        self.assertTrue(
            normalizer.match_quote(
                "검증기업은 ‘HBM’을 공급한다.",
                "문서 본문: 검증기업은 \"HBM\"을 공급한다. 후속 설명",
            ).matched
        )

    def test_short_excerpt_survives_schema_but_does_not_bypass_literal_verification(self) -> None:
        dossier = self._dossier()
        dossier["material_facts"][0]["supporting_excerpt"] = "정기보수 영향"
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=True,
                    text=self._document(excerpt="정기보수 영향"),
                )
            }
        )

        preflight = self._run(dossier, fetcher)

        self.assertTrue(
            any(row.cause_code == "QUOTE_TOO_SHORT" for row in preflight.issues)
        )
        self.assertIsNone(
            preflight.resolved_fact_documents["FACT-ONE"].quote_match_mode
        )

    def test_exact_quote_accepts_only_ordered_table_delimiter_representation(self) -> None:
        verifier = ExactQuoteVerifier()
        accepted = verifier.verify(
            "PE | 258,904 | 223,175 | 86.2",
            "생산실적\nPE\n258,904\n223,175\n86.2\n다음 행",
        )
        self.assertTrue(accepted.matched)
        self.assertEqual(
            accepted.match_mode,
            "UNICODE_PUNCTUATION_WHITESPACE_NORMALIZED",
        )
        self.assertFalse(
            verifier.verify(
                "PE | 258,904 | 86.2",
                "PE\n258,904\n다른 제품\n777,000\n86.2",
            ).matched
        )

    def test_body_maturity_table_is_not_inferred_as_publication_date(self) -> None:
        result = AsOfDateVerifier().verify(
            claimed_published_at="2026-08-13",
            event_date="2026-06-30",
            as_of_date="2026-08-23",
            source_url="https://issuer.example/report(2026.08.13).pdf",
            source_title="2026년 반기보고서",
            source_publisher="공시기업",
            document_text=(
                "반기보고서\n"
                "재무제표 작성기준 및 회계정책의 변경\n"
                "회차 발행액 발행일 만기일 평가일 평가기관\n"
                "15-2 1,000 2025.01.31 2028.01.31 2026.04.29 평가사\n"
            ),
            fetch_result=FetchResult(
                url="https://issuer.example/report(2026.08.13).pdf",
                ok=True,
                text="full document",
            ),
        )
        self.assertTrue(result.accepted)
        self.assertEqual(result.effective_published_at, "2026-08-13")

    def test_nonissuer_exact_excerpt_target_anchor_survives_subject_spacing(self) -> None:
        result = SubjectScopeVerifier().verify(
            fact={
                "subject": "롯데케미칼 여수공장",
                "issuer_scoped": False,
                "supporting_excerpt": (
                    "롯데케미칼 여수 공장의 NCC와 PE·PP 사업을 통합"
                ),
                "business_segment": "여수 기초화학",
                "product_family": "NCC·PE·PP",
            },
            document_text=(
                "산업부 승인 내용. 롯데케미칼 여수 공장의 NCC와 PE·PP "
                "사업을 통합한다."
            ),
            target_id="011170",
            company_name="롯데케미칼",
            semantic_scope={
                "scope_business_segment": "여수 기초화학",
                "scope_product_family": "NCC·PE·PP",
                "scope_technology_family": "석유화학",
                "scope_transaction_type": "사업재편",
                "scope_economic_mechanism": "통합",
                "scope_confidence": 0.9,
            },
        )
        self.assertTrue(result.accepted)
        self.assertEqual(result.status, "SUBJECT_SCOPE_ACCEPTED")

    def test_http_last_modified_never_overrides_confirmed_published_date(self) -> None:
        resolution = DatePrecedenceResolver().resolve(
            source_document={
                "publication_date": "2026-08-01",
                "availability_date": "2026-08-01",
            },
            fetch_result=FetchResult(
                url=self.canonical_url,
                ok=True,
                text=self._document(),
                response_last_modified_at=datetime(
                    2026, 8, 24, tzinfo=timezone.utc
                ),
            ),
            as_of_date=self.as_of_date,
        )
        self.assertTrue(resolution.accepted)
        self.assertEqual(resolution.effective_publication_date, "2026-08-01")
        self.assertTrue(resolution.last_modified_ignored)

    def test_field_alias_lineage_alias_and_closed_scope_mapping_are_local(self) -> None:
        dossier = self._dossier()
        fact = dossier["material_facts"][0]
        fact["predicate"] = fact.pop("predicate_id")
        fact["candidate_components"] = fact.pop("candidate_component_ids")
        fact["business_segment"] = "memory"
        fact["product_family"] = "hbm"
        dossier["source_lineage_aliases"] = {"SL-OLD": "SL-ONE"}
        dossier["source_documents"][0]["lineage_id"] = "SL-OLD"
        dossier["source_lineages"][0]["lineage_id"] = "SL-OLD"
        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )
        normalized_fact = normalized.payload["material_facts"][0]
        self.assertEqual(normalized_fact["predicate_id"], "HBM_CAPACITY_ALLOCATED")
        self.assertNotIn("predicate", normalized_fact)
        self.assertEqual(normalized_fact["business_segment"], "MEMORY")
        self.assertEqual(normalized_fact["product_family"], "HBM")
        self.assertEqual(
            normalized.payload["source_documents"][0]["lineage_id"], "SL-ONE"
        )
        self.assertNotIn("source_lineage_aliases", normalized.payload)

    def test_fact_scope_is_only_downgraded_to_bound_nonissuer_source(self) -> None:
        dossier = self._dossier()
        dossier["source_documents"][0]["target_scope"]["issuer_scoped"] = False
        self.assertIs(dossier["material_facts"][0]["issuer_scoped"], True)

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )

        self.assertIs(
            normalized.payload["source_documents"][0]["target_scope"][
                "issuer_scoped"
            ],
            False,
        )
        self.assertIs(
            normalized.payload["material_facts"][0]["issuer_scoped"],
            False,
        )
        self.assertIn(
            "DOWNGRADE_FACT_TO_NONISSUER_SOURCE_SCOPE",
            {row.operation_code for row in normalized.operations},
        )

        stronger_source = self._dossier()
        stronger_source["material_facts"][0]["issuer_scoped"] = False
        unchanged = PreSchemaV3Normalizer().normalize(
            stronger_source,
            archetype_ids=self.job.archetype_ids,
        )
        self.assertIs(
            unchanged.payload["material_facts"][0]["issuer_scoped"],
            False,
        )
        self.assertNotIn(
            "DOWNGRADE_FACT_TO_NONISSUER_SOURCE_SCOPE",
            {row.operation_code for row in unchanged.operations},
        )

    def test_wrong_kind_question_reference_is_dropped_without_promotion(self) -> None:
        dossier = self._dossier()
        counterfact = deepcopy(dossier["material_facts"][0])
        counterfact.update(
            {
                "dossier_fact_id": "FACT-COUNTER",
                "fact_kind": "COUNTER",
                "direction": "NEGATIVE",
            }
        )
        dossier["counterfacts"] = [counterfact]
        dossier["question_family_results"] = [
            {
                "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                "support_fact_ids": [],
                "counter_fact_ids": [
                    "FACT-ONE",
                    "FACT-COUNTER",
                    "FACT-UNKNOWN",
                ],
                "resolution_fact_ids": [],
            }
        ]

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )

        question = normalized.payload["question_family_results"][0]
        self.assertEqual(question["support_fact_ids"], [])
        self.assertEqual(
            question["counter_fact_ids"],
            ["FACT-COUNTER", "FACT-UNKNOWN"],
        )
        self.assertIn(
            "DROP_WRONG_KIND_QUESTION_FACT_REFERENCE",
            {row.operation_code for row in normalized.operations},
        )

    def test_question_reference_without_fact_backlink_is_dropped_conservatively(self) -> None:
        dossier = self._dossier()
        dossier["material_facts"][0]["question_family_ids"] = []
        dossier["question_family_results"] = [
            {
                "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                "support_fact_ids": ["FACT-ONE", "FACT-UNKNOWN"],
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
            }
        ]

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )

        question = normalized.payload["question_family_results"][0]
        self.assertEqual(question["support_fact_ids"], ["FACT-UNKNOWN"])
        self.assertEqual(
            normalized.payload["material_facts"][0]["question_family_ids"],
            [],
        )
        self.assertIn(
            "DROP_UNBOUND_QUESTION_FACT_REFERENCE",
            {row.operation_code for row in normalized.operations},
        )

    def test_unproven_likely_nonpublic_is_reopened_without_fabricated_reason(self) -> None:
        dossier = self._terminal_absence_dossier()
        dossier["research_status"] = "COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER"
        dossier["search_route_receipts"][1]["no_new_route_reason"] = None
        dossier["source_documents"][0]["canonical_url"] = self.canonical_url
        dossier["source_documents"][0]["opened_url"] = self.canonical_url

        with self.assertRaisesRegex(
            DossierValidationError,
            "LIKELY_NONPUBLIC requires no-new-route reasons",
        ):
            ResearchDossierValidator().validate(
                dossier,
                DossierValidationContext(
                    job_id=self.job.job_id,
                    run_id="PRORUN-PREFLIGHT",
                    target_id=self.target_id,
                    as_of_date=self.as_of_date,
                    conversation_id="CONVERSATION-PREFLIGHT",
                    candidate_archetype_ids=self.job.archetype_ids,
                    research_pass_id="PROPASS-PREFLIGHT",
                    parent_pass_id=None,
                    enforce_parent_pass_id=True,
                ),
            )

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )
        question = normalized.payload["question_family_results"][0]
        operation_codes = {row.operation_code for row in normalized.operations}

        self.assertEqual(question["status"], "PUBLIC_SEARCHABLE")
        self.assertEqual(question["availability_class"], "PUBLIC_SEARCHABLE")
        self.assertIs(question["adequate_search_proven"], False)
        self.assertIsNone(
            normalized.payload["search_route_receipts"][1][
                "no_new_route_reason"
            ],
        )
        self.assertEqual(
            normalized.payload["research_status"],
            "NEEDS_PUBLIC_GAP_CLOSURE",
        )
        self.assertIn(
            "DOWNGRADE_UNPROVEN_TERMINAL_ABSENCE_CLAIM",
            operation_codes,
        )
        self.assertIn(
            "RECONCILE_RESEARCH_STATUS_AFTER_TERMINAL_DOWNGRADE",
            operation_codes,
        )
        receipt = ResearchDossierValidator().validate(
            normalized.payload,
            DossierValidationContext(
                job_id=self.job.job_id,
                run_id="PRORUN-PREFLIGHT",
                target_id=self.target_id,
                as_of_date=self.as_of_date,
                conversation_id="CONVERSATION-PREFLIGHT",
                candidate_archetype_ids=self.job.archetype_ids,
                research_pass_id="PROPASS-PREFLIGHT",
                parent_pass_id=None,
                enforce_parent_pass_id=True,
            ),
        )
        self.assertEqual(receipt.schema_version, "e2r_pro_research_dossier_v3")

    def test_proven_likely_nonpublic_is_preserved_exactly(self) -> None:
        dossier = self._terminal_absence_dossier()
        before_reasons = [
            row["no_new_route_reason"]
            for row in dossier["search_route_receipts"]
        ]

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )
        question = normalized.payload["question_family_results"][0]

        self.assertEqual(question["status"], "LIKELY_NONPUBLIC")
        self.assertEqual(question["availability_class"], "LIKELY_NONPUBLIC")
        self.assertIs(question["adequate_search_proven"], True)
        self.assertEqual(
            [
                row["no_new_route_reason"]
                for row in normalized.payload["search_route_receipts"]
            ],
            before_reasons,
        )
        self.assertNotIn(
            "DOWNGRADE_UNPROVEN_TERMINAL_ABSENCE_CLAIM",
            {row.operation_code for row in normalized.operations},
        )

    def test_unproven_evaluated_absence_is_reopened_generically(self) -> None:
        dossier = self._terminal_absence_dossier()
        question = dossier["question_family_results"][0]
        question["status"] = "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH"
        question["availability_class"] = "PUBLIC_SEARCHABLE"
        question["adequate_search_proven"] = False
        question["search_route_receipt_ids"] = question[
            "search_route_receipt_ids"
        ][:1]

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )

        self.assertEqual(
            normalized.payload["question_family_results"][0]["status"],
            "PUBLIC_SEARCHABLE",
        )
        self.assertEqual(
            [row["no_new_route_reason"] for row in dossier["search_route_receipts"]],
            [
                row["no_new_route_reason"]
                for row in normalized.payload["search_route_receipts"]
            ],
        )

    def test_initial_transport_none_and_conversation_aliases_are_local(self) -> None:
        dossier = self._dossier()
        dossier["conversation_id"] = "PENDING_NEW_CONVERSATION"
        dossier["parent_pass_id"] = "NONE"
        dossier["research_passes"][0].update(
            {
                "parent_pass_id": "NONE",
                "status": "TRANSPORT_PENDING",
                "response_hash": None,
            }
        )

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )
        operation_codes = {row.operation_code for row in normalized.operations}

        self.assertIsNone(normalized.payload["parent_pass_id"])
        self.assertIsNone(normalized.payload["research_passes"][0]["parent_pass_id"])
        self.assertEqual(
            normalized.payload["conversation_id"],
            "PENDING_INITIAL_CONVERSATION",
        )
        self.assertIn(
            "NORMALIZE_INITIAL_PARENT_PASS_NULL_ALIAS",
            operation_codes,
        )
        self.assertIn(
            "NORMALIZE_INITIAL_CONVERSATION_PLACEHOLDER_ALIAS",
            operation_codes,
        )
        bound = bind_dossier_transport_identity(
            normalized.payload,
            conversation_id="CAPTURED-CONVERSATION",
            research_pass_id="PROPASS-PREFLIGHT",
            parent_pass_id=None,
            allow_initial_conversation_placeholder=True,
            pass_name="INITIAL_FULL_RESEARCH",
            prompt_hash="c" * 64,
            response_hash="d" * 64,
        )
        self.assertEqual(
            bound.payload["conversation_id"],
            "CAPTURED-CONVERSATION",
        )
        self.assertEqual(
            bound.payload["research_passes"][0]["status"],
            "COMPLETE",
        )

    def test_initial_conversation_alias_accepts_canonical_null_parent(self) -> None:
        dossier = self._dossier()
        dossier["conversation_id"] = "PENDING_NEW_CONVERSATION"
        dossier["parent_pass_id"] = None
        dossier["research_passes"][0].update(
            {
                "parent_pass_id": None,
                "status": "PENDING",
                "response_hash": None,
            }
        )

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )
        operation_codes = {row.operation_code for row in normalized.operations}

        self.assertIsNone(normalized.payload["parent_pass_id"])
        self.assertIsNone(normalized.payload["research_passes"][0]["parent_pass_id"])
        self.assertEqual(
            normalized.payload["conversation_id"],
            "PENDING_INITIAL_CONVERSATION",
        )
        self.assertNotIn(
            "NORMALIZE_INITIAL_PARENT_PASS_NULL_ALIAS",
            operation_codes,
        )
        self.assertIn(
            "NORMALIZE_INITIAL_CONVERSATION_PLACEHOLDER_ALIAS",
            operation_codes,
        )

    def test_missing_initial_parent_field_does_not_enable_identity_rewrite(self) -> None:
        dossier = self._dossier()
        dossier["conversation_id"] = "PENDING_NEW_CONVERSATION"
        dossier.pop("parent_pass_id")

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )

        self.assertEqual(
            normalized.payload["conversation_id"],
            "PENDING_NEW_CONVERSATION",
        )

    def test_followup_none_parent_alias_is_not_normalized(self) -> None:
        dossier = self._dossier()
        dossier["conversation_id"] = "PENDING_NEW_CONVERSATION"
        dossier["parent_pass_id"] = "NONE"
        dossier["research_passes"][0].update(
            {
                "pass_name": "VERIFIER_REPAIR",
                "parent_pass_id": "NONE",
            }
        )

        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )

        self.assertEqual(normalized.payload["parent_pass_id"], "NONE")
        self.assertEqual(
            normalized.payload["conversation_id"],
            "PENDING_NEW_CONVERSATION",
        )

    def test_known_publisher_alias_is_normalized_from_injected_registry(self) -> None:
        dossier = self._dossier()
        dossier["source_documents"][0]["source_publisher"] = "Example Corp."
        alias_resolver = IssuerAliasResolver(
            known_publisher_aliases={"Example Corp.": "Example Corporation"}
        )
        normalized = PreSchemaV3Normalizer(
            issuer_alias_resolver=alias_resolver
        ).normalize(dossier, archetype_ids=self.job.archetype_ids)
        self.assertEqual(
            normalized.payload["source_documents"][0]["source_publisher"],
            "Example Corporation",
        )
        self.assertIn(
            "NORMALIZE_KNOWN_SOURCE_PUBLISHER_ALIAS",
            {row.operation_code for row in normalized.operations},
        )

    def test_pre_schema_normalization_runs_before_strict_v3_graph_validation(self) -> None:
        dossier = self._dossier()
        context = DossierValidationContext(
            job_id=self.job.job_id,
            run_id="PRORUN-PREFLIGHT",
            target_id=self.target_id,
            as_of_date=self.as_of_date,
            conversation_id="CONVERSATION-PREFLIGHT",
            candidate_archetype_ids=self.job.archetype_ids,
            research_pass_id="PROPASS-PREFLIGHT",
            parent_pass_id=None,
            enforce_parent_pass_id=True,
        )
        with self.assertRaises(DossierValidationError):
            ResearchDossierValidator().validate(dossier, context)
        normalized = PreSchemaV3Normalizer().normalize(
            dossier,
            archetype_ids=self.job.archetype_ids,
        )
        receipt = ResearchDossierValidator().validate(normalized.payload, context)
        self.assertEqual(receipt.schema_version, "e2r_pro_research_dossier_v3")
        self.assertEqual(receipt.source_urls, (self.canonical_url,))

    def test_same_lineage_alternate_official_representation_resolves_quote(self) -> None:
        dossier = self._dossier()
        alternate_url = "https://example.com/report.pdf"
        alternate = deepcopy(dossier["source_documents"][0])
        alternate.update(
            {
                "source_document_id": "SRC-ALT",
                "canonical_url": alternate_url,
                "opened_url": alternate_url,
                "document_type": "PDF",
                "locator_type": "PDF_PAGE",
                "locator_value": "page 3",
            }
        )
        dossier["source_documents"].append(alternate)
        dossier["source_lineages"][0]["source_document_ids"].append("SRC-ALT")
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=True,
                    text=self._document(excerpt="다른 요약 문장입니다."),
                ),
                alternate_url: FetchResult(
                    url=alternate_url,
                    ok=True,
                    text=self._document(),
                    content_type="application/pdf",
                ),
            }
        )
        preflight = self._run(dossier, fetcher)
        representation = preflight.resolved_fact_documents["FACT-ONE"]
        self.assertTrue(representation.alternate_representation_used)
        self.assertEqual(representation.resolved_url, alternate_url)
        self.assertTrue(
            any(
                row.cause_class
                is RejectionRootCauseClass.SOURCE_REPRESENTATION_RESOLVABLE
                and row.locally_resolved
                for row in preflight.issues
            )
        )
        self.assertEqual(
            preflight.receipt["source_representation_sent_to_pro_count"], 0
        )

    def test_unavailable_primary_uses_same_lineage_official_representation(self) -> None:
        dossier = self._dossier()
        alternate_url = "https://example.com/report.txt"
        alternate = deepcopy(dossier["source_documents"][0])
        alternate.update(
            {
                "source_document_id": "SRC-ALT",
                "canonical_url": alternate_url,
                "opened_url": alternate_url,
            }
        )
        dossier["source_documents"].append(alternate)
        dossier["source_lineages"][0]["source_document_ids"].append("SRC-ALT")
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=False,
                    reason="primary representation unavailable",
                ),
                alternate_url: FetchResult(
                    url=alternate_url,
                    ok=True,
                    text=self._document(),
                ),
            }
        )
        representation = self._run(
            dossier, fetcher
        ).resolved_fact_documents["FACT-ONE"]
        self.assertTrue(representation.available)
        self.assertTrue(representation.alternate_representation_used)
        self.assertEqual(representation.resolved_url, alternate_url)

    def test_redirect_final_url_is_used_only_in_verifier_projection(self) -> None:
        final_url = "https://example.com/final-report"
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=final_url,
                    ok=True,
                    text=self._document(),
                )
            }
        )
        preflight = self._run(self._dossier(), fetcher)
        self.assertEqual(
            preflight.canonical_dossier["source_documents"][0]["canonical_url"],
            self.canonical_url,
        )
        self.assertEqual(
            preflight.verifier_dossier["material_facts"][0]["source_url"],
            final_url,
        )
        self.assertIn(
            "RESOLVE_REDIRECT_FINAL_URL",
            {row.operation_code for row in preflight.operations},
        )

    def test_nonissuer_subject_alias_is_resolved_without_pro_repair(self) -> None:
        dossier = self._dossier()
        document = dossier["source_documents"][0]
        document["source_publisher"] = "PeerCo"
        document["target_scope"].update(
            {
                "issuer_scoped": False,
                "subject": "PeerCo",
            }
        )
        fact = dossier["material_facts"][0]
        fact.update(
            {
                "issuer_scoped": False,
                "subject": "peer capacity plan",
                "supporting_excerpt": self.excerpt.replace(
                    self.company_name, "PeerCo"
                ),
            }
        )
        peer_text = self._document().replace(self.company_name, "PeerCo")
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=True,
                    text=peer_text,
                )
            }
        )
        preflight = self._run(dossier, fetcher)
        result = ProSourceVerifier(page_fetcher=fetcher).verify(
            dossier=preflight.verifier_dossier,
            job=self.job,
            job_root=self.job_root,
            preflight=preflight,
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertIn(
            "PeerCo",
            preflight.verifier_dossier["material_facts"][0][
                "preflight_subject_aliases"
            ],
        )

    def test_v3_preflight_then_verifier_accepts_without_second_fetch(self) -> None:
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=True,
                    text=self._document(),
                    content_type="text/html",
                )
            }
        )
        preflight = self._run(self._dossier(), fetcher)
        self.assertEqual(len(fetcher.calls), 1)
        verifier = ProSourceVerifier(page_fetcher=fetcher)
        result = verifier.verify(
            dossier=preflight.verifier_dossier,
            job=self.job,
            job_root=self.job_root,
            preflight=preflight,
        )
        self.assertEqual(len(fetcher.calls), 1)
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertEqual(result.full_document_fetch_count, 1)
        self.assertEqual(len(result.fact_compilation.facts), 1)
        evidence = result.fact_compilation.facts[0]
        self.assertEqual(
            evidence.question_family_tags,
            ("C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",),
        )

    def test_durable_source_service_runs_preflight_before_v3_verifier(self) -> None:
        dossier = PreSchemaV3Normalizer().normalize(
            self._dossier(),
            archetype_ids=self.job.archetype_ids,
        ).payload
        self.job = self._advance_to_importing(self.job)
        import_root = self.job_root / "import"
        import_root.mkdir(parents=True, exist_ok=True)
        (import_root / "research_dossier.normalized.json").write_text(
            canonical_json(dossier) + "\n",
            encoding="utf-8",
        )
        dossier_hash = canonical_hash(dossier)
        self.job = self.store.record_dossier_import(
            self.job.job_id,
            expected_version=self.job.state_version,
            dossier_id="PRODOSSIER-PREFLIGHT-V3",
            dossier_hash=dossier_hash,
            import_receipt={
                "schema_version": "e2r_pro_dossier_import_receipt_v1",
                "job_id": self.job.job_id,
                "normalized_dossier_hash": dossier_hash,
                "validation_status": "PASS",
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
                "component_ids": list(CANONICAL_COMPONENT_IDS),
            },
            actor="test",
            idempotency_key="v3-preflight-imported",
        )
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=True,
                    text=self._document(),
                )
            }
        )
        run = ProSourceVerificationService(
            self.store,
            verifier=ProSourceVerifier(page_fetcher=fetcher),
        ).verify_job(self.job.job_id, job_root=self.job_root)
        self.assertEqual(run.job.status, JobStatus.GAP_ADJUDICATION.value)
        self.assertTrue(run.receipt["preflight_applicable"])
        self.assertEqual(run.receipt["unclassified_rejection_count"], 0)
        self.assertEqual(run.receipt["local_normalizable_sent_to_pro_count"], 0)
        self.assertEqual(run.receipt["source_representation_sent_to_pro_count"], 0)
        self.assertEqual(run.receipt["accepted_fact_candidate_count"], 1)
        self.assertTrue(
            (self.job_root / "verification/preflight/preflight_receipt.json").is_file()
        )
        self.assertTrue(
            (self.job_root / "verification/rejection_classifications.jsonl").is_file()
        )

    def test_v3_cannot_bypass_local_preflight(self) -> None:
        with self.assertRaisesRegex(ValueError, "must pass LocalEvidencePreflight"):
            ProSourceVerifier(
                page_fetcher=_CountingFetcher({})
            ).verify(
                dossier=self._dossier(),
                job=self.job,
                job_root=self.job_root,
            )

    def test_failed_initial_preflight_never_becomes_accepted_fact(self) -> None:
        dossier = self._dossier()
        dossier["material_facts"][0]["verifier_preflight"][
            "single_atomic_predicate"
        ] = False
        fetcher = _CountingFetcher(
            {
                self.canonical_url: FetchResult(
                    url=self.canonical_url,
                    ok=True,
                    text=self._document(),
                )
            }
        )
        preflight = self._run(dossier, fetcher)
        result = ProSourceVerifier(page_fetcher=fetcher).verify(
            dossier=preflight.verifier_dossier,
            job=self.job,
            job_root=self.job_root,
            preflight=preflight,
        )
        self.assertEqual(result.verifications[0].status, "UNVERIFIED_PENDING")
        classified = LocalEvidencePreflightService(
            page_fetcher=fetcher
        ).classify_verifications(
            preflight=preflight,
            verification_rows=[row.to_dict() for row in result.verifications],
        )
        self.assertEqual(
            classified.rows[0].cause_class,
            RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT,
        )

    def test_semantic_similarity_without_literal_quote_never_matches(self) -> None:
        match = TextQuoteNormalizer().match_quote(
            "회사는 용량이 모두 배정됐다고 발표했다.",
            "기업은 생산 물량의 예약이 충분하다고 설명했다.",
        )
        self.assertFalse(match.matched)
        self.assertIsNone(match.match_mode)

    def test_compound_split_requires_explicit_atomic_quote_spans(self) -> None:
        fact = self._dossier()["material_facts"][0]
        fact["verifier_preflight"]["single_atomic_predicate"] = False
        rejected = split_compound_fact(fact)
        self.assertFalse(rejected.deterministically_separable)
        fact["supporting_excerpt"] = (
            "HBM capacity sold out. HBM price increased during the quarter."
        )
        fact["atomic_parts"] = [
            {
                "statement": "capacity sold out",
                "predicate_id": "CAPACITY_SOLD_OUT",
                "supporting_excerpt": "HBM capacity sold out.",
            },
            {
                "statement": "price increased",
                "predicate_id": "PRICE_INCREASED",
                "supporting_excerpt": "HBM price increased during the quarter.",
            },
        ]
        split = split_compound_fact(fact)
        self.assertTrue(split.deterministically_separable)
        self.assertEqual(len(split.facts), 2)
        self.assertTrue(
            all(
                row["verifier_preflight"]["single_atomic_predicate"]
                for row in split.facts
            )
        )

    def test_only_genuine_or_initial_material_defect_can_route_to_pro(self) -> None:
        facts = {
            "FACT-ONE": self._dossier()["material_facts"][0],
            "FACT-AUX": {
                **self._dossier()["material_facts"][0],
                "dossier_fact_id": "FACT-AUX",
            },
        }
        classified = RejectionClassifier().classify(
            verifications=(
                {
                    "dossier_fact_id": "FACT-ONE",
                    "status": "REJECTED_QUOTE_MISMATCH",
                    "reason": "literal mismatch",
                },
                {
                    "dossier_fact_id": "FACT-AUX",
                    "status": "REJECTED_SOURCE_UNAVAILABLE",
                    "reason": "unavailable",
                },
            ),
            facts_by_id=facts,
            material_fact_ids=("FACT-ONE",),
        )
        self.assertTrue(classified.rows[0].send_to_pro_allowed)
        self.assertEqual(
            classified.rows[0].cause_class,
            RejectionRootCauseClass.GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
        )
        self.assertFalse(classified.rows[1].send_to_pro_allowed)
        self.assertEqual(
            classified.rows[1].cause_class,
            RejectionRootCauseClass.NONMATERIAL_AUXILIARY_REJECTION,
        )
        self.assertEqual(classified.unclassified_rejection_count, 0)

    def _run(
        self,
        dossier: dict,
        fetcher: _CountingFetcher,
    ):
        return LocalEvidencePreflightService(page_fetcher=fetcher).run(
            dossier=dossier,
            target_id=self.target_id,
            company_name=self.company_name,
            target_aliases=("검증 기업",),
            as_of_date=self.as_of_date,
            archetype_ids=self.job.archetype_ids,
            job_root=self.job_root,
        )

    def _document(self, *, excerpt: str | None = None) -> str:
        return " ".join(
            (
                "2026년 8월 1일 공식 사업 보고서.",
                self.company_name,
                "MEMORY HBM 사업 설명.",
                excerpt or self.excerpt,
                "이 문서는 생산 계획, 고객 배정, 가격, 위험과 현금흐름을 포함한 전체 보고서 본문이다.",
                "검색 결과의 짧은 snippet이 아니라 검증용 원문 전체를 모사하기 위해 충분한 길이를 유지한다.",
            )
        )

    def _terminal_absence_dossier(self) -> dict:
        dossier = self._dossier()
        route_ids = ["ROUTE-ABSENCE-1", "ROUTE-ABSENCE-2"]
        dossier["question_family_results"] = [
            {
                "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                "status": "LIKELY_NONPUBLIC",
                "support_fact_ids": [],
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
                "attempted_source_role_ids": [
                    "ISSUER_OFFICIAL",
                    "CUSTOMER_PARTNER_OFFICIAL",
                ],
                "search_route_receipt_ids": route_ids,
                "required_source_roles_satisfied": [],
                "required_source_roles_missing": [
                    "ISSUER_OFFICIAL",
                    "CUSTOMER_PARTNER_OFFICIAL",
                ],
                "availability_class": "LIKELY_NONPUBLIC",
                "affected_component_ids": [
                    "bottleneck_pricing",
                    "earnings_visibility",
                    "information_confidence",
                    "market_mispricing",
                    "valuation_rerating",
                ],
                "could_change_score": True,
                "could_change_stage": False,
                "could_change_hard_break": False,
                "closure_reason": (
                    "두 개의 독립 공개 경로를 확인했으나 필요한 공개 사실을 "
                    "확인하지 못했다."
                ),
                "adequate_search_proven": True,
            }
        ]
        dossier["search_route_receipts"] = [
            {
                "route_receipt_id": route_id,
                "pass_id": "PROPASS-PREFLIGHT",
                "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                "gap_id": "GAP-ABSENCE-Q01",
                "source_role_id": source_role,
                "query_or_navigation_objective": "독립 공개 경로 확인",
                "query_text": f"검증기업 공개 경로 확인 {index}",
                "result_count_seen": 0,
                "opened_source_urls": [
                    f"https://search.example/absence/{index}"
                ],
                "accepted_fact_ids": [],
                "rejected_candidate_ids": [],
                "provider_status": "SUCCESS",
                "no_new_route_reason": "공식 공개 범위에 새 경로가 없다.",
                "performed_at": "2026-08-22T00:00:00Z",
            }
            for index, (route_id, source_role) in enumerate(
                zip(
                    route_ids,
                    ("ISSUER_OFFICIAL", "CUSTOMER_PARTNER_OFFICIAL"),
                    strict=True,
                ),
                1,
            )
        ]
        return dossier

    def _dossier(self) -> dict:
        return {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": self.job.job_id,
            "run_id": "PRORUN-PREFLIGHT",
            "conversation_id": "CONVERSATION-PREFLIGHT",
            "research_pass_id": "PROPASS-PREFLIGHT",
            "parent_pass_id": None,
            "target": {
                "target_id": self.target_id,
                "symbol": self.target_id,
                "company_name": self.company_name,
                "aliases": ["검증 기업"],
            },
            "as_of_date": self.as_of_date,
            "candidate_archetypes": ["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            "selected_archetypes": ["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            "research_status": "NEEDS_PUBLIC_GAP_CLOSURE",
            "business_model": {},
            "source_documents": [
                {
                    "source_document_id": "SRC-ONE",
                    "canonical_url": self.raw_url,
                    "opened_url": self.raw_url,
                    "source_title": "HBM capacity update",
                    "source_publisher": self.company_name,
                    "publication_date": "2026-08-01",
                    "availability_date": "2026-08-01",
                    "source_role_ids": ["ISSUER_OFFICIAL"],
                    "document_type": "HTML",
                    "target_scope": {
                        "target_id": self.target_id,
                        "issuer_scoped": True,
                        "subject": self.company_name,
                        "business_segment": "MEMORY",
                        "product_family": "HBM",
                    },
                    "locator_type": "HTML_PARAGRAPH",
                    "locator_value": "capacity update",
                    "lineage_id": "SL-ONE",
                    "opened_and_read": True,
                    "as_of_cutoff_pass": True,
                }
            ],
            "material_facts": [
                {
                    "dossier_fact_id": "FACT-ONE",
                    "research_pass_id": "PROPASS-PREFLIGHT",
                    "fact_kind": "MATERIAL",
                    "statement": "HBM capacity가 전량 배정됐다.",
                    "predicate_id": "HBM_CAPACITY_ALLOCATED",
                    "direction": "POSITIVE",
                    "target_id": self.target_id,
                    "subject": self.company_name,
                    "issuer_scoped": True,
                    "business_segment": "MEMORY",
                    "product_family": "HBM",
                    "economic_mechanism_id": "CAPACITY_SCARCITY",
                    "value": 100,
                    "unit": "%",
                    "period": "2026",
                    "event_date": "2026-08-01",
                    "current_status": "CURRENT",
                    "question_family_ids": [
                        "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
                    ],
                    "candidate_component_ids": ["bottleneck_pricing"],
                    "source_document_id": "SRC-ONE",
                    "supporting_excerpt": self.excerpt,
                    "source_locator": "capacity update",
                    "confidence": 0.9,
                    "verifier_preflight": {
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
                    },
                }
            ],
            "counterfacts": [],
            "resolution_facts": [],
            "derived_metrics": [],
            "question_family_results": [],
            "component_research": {},
            "structured_metrics": {},
            "unresolved_gaps": [],
            "source_lineages": [
                {
                    "lineage_id": "SL-ONE",
                    "source_document_ids": ["SRC-ONE"],
                    "fact_ids": ["FACT-ONE"],
                    "independence_group_id": "INDEPENDENCE-ONE",
                    "status": "ACTIVE",
                }
            ],
            "search_route_receipts": [],
            "research_passes": [
                {
                    "pass_id": "PROPASS-PREFLIGHT",
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

    def _advance_to_importing(self, job):
        contexts = {
            JobStatus.SUBMITTING: TransitionContext(
                approval_nonce_consumed=True
            ),
            JobStatus.IMPORTING: TransitionContext(
                capture_receipt_verified=True
            ),
        }
        for index, target in enumerate(
            (
                JobStatus.PACKET_BUILDING,
                JobStatus.PACKET_READY,
                JobStatus.BROWSER_PREPARING,
                JobStatus.AWAITING_USER_APPROVAL,
                JobStatus.APPROVED,
                JobStatus.SUBMITTING,
                JobStatus.RESEARCH_RUNNING,
                JobStatus.RESULT_DETECTED,
                JobStatus.CAPTURING_ARTIFACTS,
                JobStatus.CAPTURE_COMPLETE,
                JobStatus.IMPORTING,
            )
        ):
            job = self.store.transition(
                job.job_id,
                expected_version=job.state_version,
                to_status=target,
                actor="test",
                idempotency_key=f"preflight-advance-{index}-{target.value}",
                context=contexts.get(target),
            )
        return job


if __name__ == "__main__":
    unittest.main()
