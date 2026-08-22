from __future__ import annotations

from datetime import date, datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.dossier.validator import CANONICAL_COMPONENT_IDS
from e2r.pro_first.ids import canonical_hash, canonical_json
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.state_machine import TransitionContext
from e2r.pro_first.state_machine import NoProgressDetected
from e2r.pro_first.verification import ProSourceVerificationService
from e2r.pro_first.verification.mechanism_scope_mapper import (
    MechanismScopeMappingRun,
)
from e2r.pro_first.verification.quote_verifier import ExactQuoteVerifier
from e2r.pro_first.verification.source_verifier import ProSourceVerifier
from e2r.research.page_fetcher import FetchResult, PageFetcher


class _CountingFetcher:
    def __init__(self, results: dict[str, FetchResult]) -> None:
        self.results = results
        self.calls: list[tuple[str, str]] = []

    def fetch(self, url: str, *, as_of_date: date) -> FetchResult:
        self.calls.append((url, as_of_date.isoformat()))
        return self.results[url]


class _ChangedSemanticsVerifier(ProSourceVerifier):
    @property
    def semantics_version(self) -> str:
        return "e2r_pro_source_verification_test_v3"


class ProFirstSourceVerificationTest(unittest.TestCase):
    target_id = "123456"
    company_name = "검증기업"
    as_of_date = "2026-08-22"
    url = "https://example.com/hbm-capacity"
    excerpt = "검증기업은 MEMORY 사업의 HBM capacity가 전량 배정됐다고 밝혔다."

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name) / "job-root"
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "pro-first.sqlite3",
            now=lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc),
        )
        candidate = self.store.create_candidate(
            symbol=self.target_id,
            company_name=self.company_name,
            as_of_date=self.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="source-verification-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        self.job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
        )

    def _fact(self, **updates: object) -> dict:
        fact = {
            "dossier_fact_id": "PROFACT-001",
            "statement": "HBM capacity가 전량 배정됐다.",
            "direction": "POSITIVE",
            "subject": self.company_name,
            "target_id": self.target_id,
            "issuer_scoped": True,
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": "CAPACITY_SCARCITY",
            "predicate": "HBM_CAPACITY_ALLOCATED",
            "value": 100,
            "unit": "%",
            "period": "2026",
            "event_date": "2026-08-01",
            "current_status": "CURRENT",
            "candidate_components": ["bottleneck_pricing"],
            "source_url": self.url,
            "source_title": "2026 HBM capacity update",
            "source_publisher": self.company_name,
            "published_at": "2026-08-01",
            "supporting_excerpt": self.excerpt,
            "confidence": 0.93,
            "scope_business_segment": "MEMORY",
            "scope_product_family": "HBM",
            "scope_technology_family": "HBM",
            "scope_transaction_type": "CAPACITY_INVESTMENT",
            "scope_economic_mechanism": "CAPACITY_SCARCITY",
            "scope_confidence": 1.0,
        }
        fact.update(updates)
        return fact

    def _dossier(self, *facts: dict) -> dict:
        return {
            "schema_version": "e2r_pro_research_dossier_v1",
            "job_id": self.job.job_id,
            "run_id": "PRORUN-source-verification",
            "target": {
                "target_id": self.target_id,
                "company_name": self.company_name,
                "aliases": ["검증 기업"],
            },
            "as_of_date": self.as_of_date,
            "research_status": "COMPLETE",
            "business_model": {"summary": "HBM 검증 fixture"},
            "candidate_archetypes": ["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            "material_facts": list(facts),
            "counterfacts": [],
            "component_research": {
                component_id: {"positive_fact_ids": [], "counterfact_ids": []}
                for component_id in CANONICAL_COMPONENT_IDS
            },
            "structured_metrics": {},
            "unresolved_gaps": [],
            "sources": [
                {
                    "source_id": "SOURCE-001",
                    "source_url": self.url,
                    "source_title": "2026 HBM capacity update",
                    "source_publisher": self.company_name,
                    "published_at": "2026-08-01",
                }
            ],
            "research_saturation": {"status": "SATURATED"},
            "proposed_score_ranges": {},
            "score_authority": False,
            "stage_authority": False,
        }

    def _document(
        self,
        *,
        excerpt: str | None = None,
        include_company: bool = True,
        include_segment: bool = True,
        include_product: bool = True,
    ) -> str:
        tokens = [
            "2026년 8월 1일 공식 사업 보고서.",
            self.company_name if include_company else "비교기업",
            "MEMORY" if include_segment else "반도체 사업",
            "HBM" if include_product else "고성능 제품",
            excerpt if excerpt is not None else self.excerpt,
            "이 문서는 경영진 설명, 생산 계획, 고객 배정 현황과 사업 위험을 포함한 전체 보고서 본문이다.",
            "검증 fixture는 검색 결과의 짧은 요약문이 아니라 원문 전체를 모사하기 위해 충분한 길이를 유지한다.",
        ]
        return " ".join(value for value in tokens if value)

    def _verify(
        self,
        fact: dict,
        *,
        document: str | None = None,
        fetch_result: FetchResult | None = None,
    ):
        if fetch_result is None:
            fetcher = PageFetcher(
                fixture_text_by_url={self.url: document or self._document()},
                live_enabled=False,
                max_text_chars=None,
            )
        else:
            fetcher = _CountingFetcher({self.url: fetch_result})
        verifier = ProSourceVerifier(page_fetcher=fetcher)
        return verifier.verify(
            dossier=self._dossier(fact),
            job=self.job,
            job_root=self.root,
        )

    def test_full_document_required(self) -> None:
        result = self._verify(self._fact())
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertTrue(result.verifications[0].full_document)
        self.assertEqual(result.full_document_fetch_count, 1)
        self.assertEqual(len(result.fact_compilation.facts), 1)
        evidence = result.fact_compilation.facts[0]
        self.assertEqual(evidence.source_ids, (result.verifications[0].source_id,))
        self.assertEqual(evidence.allowed_component_ids, ("bottleneck_pricing",))
        self.assertEqual(len(evidence.claim_ids), 1)
        self.assertEqual(len(evidence.quote_ids), 1)

    def test_open_ended_pro_scope_is_structured_before_existing_validator(self) -> None:
        fact = self._fact(
            predicate="novel_open_ended_capacity_predicate",
        )
        for field in (
            "scope_business_segment",
            "scope_product_family",
            "scope_technology_family",
            "scope_transaction_type",
            "scope_economic_mechanism",
            "scope_confidence",
        ):
            fact.pop(field)

        class ScopeMapper:
            provider_name = "UNIT_SCOPE_MAPPER"

            def map_facts(inner_self, *, facts, contracts):
                self.assertEqual(len(facts), 1)
                self.assertTrue(contracts)
                return MechanismScopeMappingRun(
                    mappings_by_fact_id={
                        "PROFACT-001": {
                            "scope_business_segment": "MEMORY",
                            "scope_product_family": "HBM",
                            "scope_technology_family": "HBM",
                            "scope_transaction_type": "CAPACITY_INVESTMENT",
                            "scope_economic_mechanism": "CAPACITY_SCARCITY",
                            "scope_confidence": 0.97,
                        }
                    },
                    provider_name=inner_self.provider_name,
                    prompt_hash="prompt-hash",
                    response_hash="response-hash",
                )

        fetcher = PageFetcher(
            fixture_text_by_url={self.url: self._document()},
            live_enabled=False,
            max_text_chars=None,
        )
        result = ProSourceVerifier(
            page_fetcher=fetcher,
            mechanism_scope_mapper=ScopeMapper(),
        ).verify(
            dossier=self._dossier(fact),
            job=self.job,
            job_root=self.root,
        )
        self.assertEqual(
            result.verifications[0].allowed_component_ids,
            ("bottleneck_pricing",),
        )
        self.assertEqual(result.receipt_payload["mechanism_scope_mapping_count"], 1)
        self.assertEqual(
            result.receipt_payload["mechanism_scope_provider_name"],
            "UNIT_SCOPE_MAPPER",
        )

    def test_snippet_only_rejected(self) -> None:
        result = self._verify(
            self._fact(),
            fetch_result=FetchResult(
                url=self.url,
                ok=True,
                text=self._document(),
                text_complete=False,
                reason="upstream text was truncated",
            ),
        )
        self.assertEqual(result.verifications[0].status, "REJECTED_SNIPPET_ONLY")
        self.assertEqual(len(result.fact_compilation.facts), 0)

    def test_future_source_rejected(self) -> None:
        result = self._verify(self._fact(published_at="2026-08-23"))
        self.assertEqual(result.verifications[0].status, "REJECTED_FUTURE")
        self.assertEqual(len(result.fact_compilation.facts), 0)

    def test_quote_mismatch_rejected(self) -> None:
        result = self._verify(
            self._fact(supporting_excerpt="원문에는 존재하지 않는 HBM 계약 해지 문장이다.")
        )
        self.assertEqual(result.verifications[0].status, "REJECTED_QUOTE_MISMATCH")
        self.assertEqual(len(result.fact_compilation.facts), 0)

    def test_wrong_subject_rejected(self) -> None:
        quote = "비교기업은 MEMORY 사업의 HBM capacity가 전량 배정됐다고 밝혔다."
        result = self._verify(
            self._fact(supporting_excerpt=quote),
            document=self._document(excerpt=quote, include_company=False),
        )
        self.assertEqual(result.verifications[0].status, "REJECTED_WRONG_SUBJECT")

    def test_wrong_segment_rejected(self) -> None:
        quote = "검증기업은 HBM capacity가 전량 배정됐다고 밝혔다."
        result = self._verify(
            self._fact(supporting_excerpt=quote),
            document=self._document(
                excerpt=quote,
                include_segment=False,
            ),
        )
        self.assertEqual(result.verifications[0].status, "REJECTED_WRONG_SEGMENT")

    def test_wrong_product_rejected(self) -> None:
        quote = "검증기업은 MEMORY capacity가 전량 배정됐다고 밝혔다."
        result = self._verify(
            self._fact(supporting_excerpt=quote),
            document=self._document(
                excerpt=quote,
                include_product=False,
            ),
        )
        self.assertEqual(result.verifications[0].status, "REJECTED_WRONG_PRODUCT")

    def test_resolved_fact_not_open_risk(self) -> None:
        result = self._verify(
            self._fact(
                current_status="RESOLVED",
                direction="COUNTER",
                resolves_fact_ids=["EFACT-prior-risk"],
            )
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_RESOLUTION")
        evidence = result.fact_compilation.facts[0]
        self.assertEqual(evidence.direction, "RESOLUTION")
        self.assertEqual(evidence.current_lifecycle, "RESOLVED")
        self.assertNotEqual(evidence.current_lifecycle, "OPEN")

    def test_same_url_content_cache_reused(self) -> None:
        second = self._fact(
            dossier_fact_id="PROFACT-002",
            predicate="HBM_CAPACITY_LOCKED",
            value=95,
        )
        fetcher = _CountingFetcher(
            {
                self.url: FetchResult(
                    url=self.url,
                    ok=True,
                    text=self._document(),
                    text_complete=True,
                )
            }
        )
        result = ProSourceVerifier(page_fetcher=fetcher).verify(
            dossier=self._dossier(self._fact(), second),
            job=self.job,
            job_root=self.root,
        )
        self.assertEqual(len(fetcher.calls), 1)
        self.assertEqual(result.full_document_fetch_count, 1)
        self.assertEqual(result.document_cache_reuse_count, 1)
        self.assertFalse(result.verifications[0].cache_reused)
        self.assertTrue(result.verifications[1].cache_reused)
        self.assertEqual(len(result.fact_compilation.facts), 2)

    def test_hash_verified_durable_document_cache_avoids_refetch(self) -> None:
        first = self._verify(self._fact())
        verification_root = self.root / "verification"
        (verification_root / "source_verifications.jsonl").write_text(
            "".join(
                canonical_json(row.to_dict()) + "\n"
                for row in first.verifications
            ),
            encoding="utf-8",
        )
        no_network = _CountingFetcher({})
        second = ProSourceVerifier(page_fetcher=no_network).verify(
            dossier=self._dossier(self._fact()),
            job=self.job,
            job_root=self.root,
        )
        self.assertEqual(no_network.calls, [])
        self.assertEqual(second.full_document_fetch_count, 0)
        self.assertEqual(second.document_cache_reuse_count, 1)
        self.assertEqual(second.verifications[0].status, "ACCEPTED_CURRENT")

    def test_unicode_punctuation_normalized_quote_is_literal_enough(self) -> None:
        quoted = "검증기업 MEMORY HBM capacity—전량 배정"
        source = "검증기업 MEMORY HBM capacity - 전량 배정"
        result = self._verify(
            self._fact(supporting_excerpt=quoted),
            document=self._document(excerpt=source),
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertEqual(
            result.verifications[0].quote_match_mode,
            "UNICODE_PUNCTUATION_WHITESPACE_NORMALIZED",
        )

    def test_ordered_ellipsis_quote_is_deletion_only_literal_match(self) -> None:
        quoted = "검증기업 MEMORY ... HBM capacity 전량 배정"
        source = (
            "검증기업 MEMORY 사업에서 여러 고객 검증을 마쳤으며 "
            "HBM capacity 전량 배정 상태라고 밝혔다."
        )
        result = self._verify(
            self._fact(supporting_excerpt=quoted),
            document=self._document(excerpt=source),
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertEqual(
            result.verifications[0].quote_match_mode,
            "EXACT_ORDERED_FRAGMENT_LIST",
        )

    def test_semicolon_separated_table_cells_are_ordered_literal_anchors(self) -> None:
        quoted = "Revenue ... 131,895,033; Operating Profit ... 98,152,891"
        source = (
            "Revenue for the period was 131,895,033 in the filed table. "
            "Operating Profit for the same period was 98,152,891."
        )
        result = self._verify(
            self._fact(supporting_excerpt=quoted),
            document=self._document(excerpt=source),
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertEqual(
            result.verifications[0].quote_match_mode,
            "EXACT_ORDERED_FRAGMENT_LIST",
        )

    def test_ordered_fragments_try_later_repeated_anchor(self) -> None:
        quote = "Revenue ... 131,895,033; Operating Profit ... 98,152,891"
        document = self._document(
            excerpt=(
                "Revenue appeared in an earlier narrative section. "
                + ("unrelated disclosure text " * 120)
                + "Revenue current period 131,895,033 "
                + "Operating Profit current period 98,152,891"
            )
        )
        result = self._verify(
            self._fact(supporting_excerpt=quote),
            document=document,
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertEqual(
            result.verifications[0].quote_match_mode,
            "EXACT_ORDERED_FRAGMENT_LIST",
        )

    def test_ordered_fragment_keeps_exact_short_numeric_cell(self) -> None:
        quote = "Average utilization ratio ... 100%"
        document = self._document(
            excerpt=(
                "Average utilization ratio Semiconductor "
                "136,255,098 136,255,098 100 %"
            )
        )
        result = self._verify(
            self._fact(supporting_excerpt=quote),
            document=document,
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")
        self.assertEqual(
            result.verifications[0].quote_match_mode,
            "EXACT_ORDERED_FRAGMENT_LIST",
        )

    def test_ellipsis_fragments_wrong_order_or_unbounded_gap_are_rejected(self) -> None:
        result = ExactQuoteVerifier().verify(
            "검증기업 MEMORY ... HBM capacity 전량 배정",
            "HBM capacity 전량 배정 이후 검증기업 MEMORY 사업을 설명했다.",
        )
        self.assertFalse(result.matched)

    def test_semantic_scope_descriptor_uses_general_literal_anchors(self) -> None:
        result = self._verify(
            self._fact(
                business_segment="Consolidated MEMORY business",
                product_family="Strategic HBM product portfolio",
            )
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")

    def test_issuer_english_alias_and_joint_party_are_supported(self) -> None:
        excerpt = "SK hynix and NVIDIA announced an HBM partnership."
        fact = self._fact(
            subject="SK hynix Inc. and NVIDIA",
            supporting_excerpt=excerpt,
            business_segment="MEMORY",
            product_family="HBM",
        )
        dossier = self._dossier(fact)
        dossier["target"]["english_name"] = "SK hynix Inc."
        fetcher = PageFetcher(
            fixture_text_by_url={
                self.url: self._document(excerpt=excerpt)
                .replace(self.company_name, "SK hynix Inc. and NVIDIA")
            },
            live_enabled=False,
            max_text_chars=None,
        )
        result = ProSourceVerifier(page_fetcher=fetcher).verify(
            dossier=dossier,
            job=self.job,
            job_root=self.root,
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")

    def test_nonissuer_peer_fact_does_not_require_target_name_in_peer_source(self) -> None:
        excerpt = "Micron Technology, Inc. began HBM volume shipments."
        result = self._verify(
            self._fact(
                subject="Micron Technology, Inc.",
                issuer_scoped=False,
                supporting_excerpt=excerpt,
            ),
            document=self._document(excerpt=excerpt, include_company=False),
        )
        self.assertEqual(result.verifications[0].status, "ACCEPTED_CURRENT")

    def test_source_unavailable_rejected_without_search(self) -> None:
        result = self._verify(
            self._fact(),
            fetch_result=FetchResult(
                url=self.url,
                ok=False,
                reason="fixture unavailable",
            ),
        )
        self.assertEqual(
            result.verifications[0].status,
            "REJECTED_SOURCE_UNAVAILABLE",
        )
        self.assertEqual(result.receipt_payload["query_count"], 0)
        self.assertEqual(result.receipt_payload["search_count"], 0)

    def test_durable_service_is_idempotent_and_writes_lineage(self) -> None:
        dossier = self._dossier(self._fact())
        self.job = self._advance_to_importing(self.job)
        dossier["job_id"] = self.job.job_id
        normalized_hash = canonical_hash(dossier)
        import_root = self.root / "import"
        import_root.mkdir(parents=True, exist_ok=True)
        (import_root / "research_dossier.normalized.json").write_text(
            canonical_json(dossier) + "\n",
            encoding="utf-8",
        )
        dossier_id = "PRODOSSIER-source-verification"
        self.job = self.store.record_dossier_import(
            self.job.job_id,
            expected_version=self.job.state_version,
            dossier_id=dossier_id,
            dossier_hash=normalized_hash,
            import_receipt={
                "schema_version": "e2r_pro_dossier_import_receipt_v1",
                "job_id": self.job.job_id,
                "normalized_dossier_hash": normalized_hash,
                "validation_status": "PASS",
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
                "component_ids": list(CANONICAL_COMPONENT_IDS),
            },
            actor="test",
            idempotency_key="dossier-imported",
        )
        verifier = ProSourceVerifier(
            page_fetcher=PageFetcher(
                fixture_text_by_url={self.url: self._document()},
                live_enabled=False,
                max_text_chars=None,
            )
        )
        service = ProSourceVerificationService(self.store, verifier=verifier)
        first = service.verify_job(self.job.job_id, job_root=self.root)
        second = service.verify_job(self.job.job_id, job_root=self.root)

        self.assertEqual(first.job.status, JobStatus.GAP_ADJUDICATION.value)
        self.assertIsNotNone(first.result)
        self.assertIsNone(second.result)
        self.assertEqual(first.receipt, second.receipt)
        self.assertEqual(first.receipt["query_count"], 0)
        self.assertEqual(first.receipt["search_count"], 0)
        self.assertFalse(first.receipt["pro_score_authority"])
        self.assertFalse(first.receipt["pro_stage_authority"])
        verification_root = self.root / "verification"
        for filename in (
            "source_verifications.jsonl",
            "evidence_facts.jsonl",
            "claim_fact_links.jsonl",
            "fact_compilation_rejections.jsonl",
            "fact_compilation_receipt.json",
            "source_verification_receipt.json",
        ):
            self.assertTrue((verification_root / filename).is_file(), filename)
        evidence_rows = self._jsonl(verification_root / "evidence_facts.jsonl")
        self.assertEqual(len(evidence_rows), 1)
        self.assertEqual(evidence_rows[0]["target_id"], self.target_id)
        self.assertTrue(evidence_rows[0]["claim_ids"])
        self.assertTrue(evidence_rows[0]["quote_ids"])
        matching_events = [
            event
            for event in self.store.list_events(self.job.job_id)
            if event.to_status == JobStatus.GAP_ADJUDICATION.value
        ]
        self.assertEqual(len(matching_events), 1)

    def test_changed_semantics_allows_one_bounded_durable_reverification(self) -> None:
        dossier = self._dossier(self._fact())
        self.job = self._advance_to_importing(self.job)
        dossier["job_id"] = self.job.job_id
        normalized_hash = canonical_hash(dossier)
        import_root = self.root / "import"
        import_root.mkdir(parents=True, exist_ok=True)
        (import_root / "research_dossier.normalized.json").write_text(
            canonical_json(dossier) + "\n", encoding="utf-8"
        )
        self.job = self.store.record_dossier_import(
            self.job.job_id,
            expected_version=self.job.state_version,
            dossier_id="PRODOSSIER-reverification",
            dossier_hash=normalized_hash,
            import_receipt={
                "schema_version": "e2r_pro_dossier_import_receipt_v1",
                "job_id": self.job.job_id,
                "normalized_dossier_hash": normalized_hash,
                "validation_status": "PASS",
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
                "component_ids": list(CANONICAL_COMPONENT_IDS),
            },
            actor="test",
            idempotency_key="dossier-imported-reverification",
        )
        fetcher = PageFetcher(
            fixture_text_by_url={self.url: self._document()},
            live_enabled=False,
            max_text_chars=None,
        )
        first_service = ProSourceVerificationService(
            self.store, verifier=ProSourceVerifier(page_fetcher=fetcher)
        )
        first = first_service.verify_job(self.job.job_id, job_root=self.root)
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=first.job.state_version,
            to_status=JobStatus.SUPPLEMENTAL_RESEARCH,
            actor="test",
            idempotency_key="test-material-gap",
        )
        changed_service = ProSourceVerificationService(
            self.store, verifier=_ChangedSemanticsVerifier(page_fetcher=fetcher)
        )
        reopened = changed_service.request_reverification(
            self.job.job_id, reason="scope verifier semantics corrected"
        )
        self.assertEqual(reopened.status, JobStatus.VERIFYING_SOURCES.value)
        second = changed_service.verify_job(self.job.job_id, job_root=self.root)
        self.assertEqual(second.job.status, JobStatus.GAP_ADJUDICATION.value)
        self.assertEqual(self.store.source_verification_attempt_count(self.job.job_id), 2)
        self.assertEqual(
            self.store.get_source_verification_receipt(self.job.job_id)[
                "verification_semantics_version"
            ],
            "e2r_pro_source_verification_test_v3",
        )
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=second.job.state_version,
            to_status=JobStatus.SUPPLEMENTAL_RESEARCH,
            actor="test",
            idempotency_key="test-material-gap-again",
        )
        with self.assertRaisesRegex(NoProgressDetected, "unchanged"):
            changed_service.request_reverification(
                self.job.job_id, reason="same semantics must not repeat"
            )

    def _advance_to_importing(self, job):
        contexts = {
            JobStatus.SUBMITTING: TransitionContext(approval_nonce_consumed=True),
            JobStatus.IMPORTING: TransitionContext(capture_receipt_verified=True),
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
                idempotency_key=f"advance-{index}-{target.value}",
                context=contexts.get(target),
            )
        return job

    @staticmethod
    def _jsonl(path: Path) -> list[dict]:
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]


if __name__ == "__main__":
    unittest.main()
