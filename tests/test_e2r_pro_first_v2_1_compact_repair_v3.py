from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import ResearchMode, ScanWindow
from e2r.pro_first.repair import (
    CompactRepairPromptCompilerV3,
    CompactRepairServiceV3,
    RepairDeltaV3ParseError,
    RepairDeltaV3Parser,
    RepairDeltaV3ValidationError,
    RepairDeltaV3Validator,
    apply_repair_delta_v3,
    normalize_repair_delta_v3_transport,
    reconcile_completed_repair_fail_closed,
)
from e2r.pro_first.verification import ProSourceVerifier
from e2r.research.page_fetcher import FetchResult


class _CountingFetcher:
    def __init__(self, text_by_url: dict[str, str]) -> None:
        self.text_by_url = text_by_url
        self.calls: list[tuple[str, str]] = []

    def fetch(self, url: str, *, as_of_date: date) -> FetchResult:
        self.calls.append((url, as_of_date.isoformat()))
        text = self.text_by_url.get(url)
        if text is None:
            return FetchResult(url=url, ok=False, reason="fixture unavailable")
        return FetchResult(url=url, ok=True, text=text, content_type="text/html")


class ProFirstV21CompactRepairV3Test(unittest.TestCase):
    target_id = "123456"
    company_name = "검증기업"
    as_of_date = "2026-08-22"
    url = "https://example.com/hbm-report"
    initial_pass_id = "PROPASS-INITIAL-V3"
    repair_pass_id = "PROPASS-REPAIR-V3"
    accepted_excerpt = "검증기업은 HBM capacity가 전량 배정됐다고 밝혔다."
    replacement_excerpt = "검증기업은 HBM 계약 가격이 20% 상승했다고 밝혔다."

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        root = Path(self.temporary_directory.name)
        self.job_root = root / "job"
        self.store = ProFirstJobStore(
            root / "repair-v3.sqlite3",
            now=lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc),
        )
        candidate = self.store.create_candidate(
            symbol=self.target_id,
            company_name=self.company_name,
            as_of_date=self.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="compact-repair-v3",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        self.job = replace(
            self.store.create_job(
                candidate.candidate_id,
                archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
            ),
            conversation_id="CONVERSATION-REPAIR-V3",
        )
        self.document = " ".join(
            (
                "2026년 8월 1일 공식 MEMORY HBM 사업 보고서.",
                self.accepted_excerpt,
                self.replacement_excerpt,
                "이 문서는 고객 배정, 계약 가격, 생산 capacity와 위험을 설명하는 전체 원문이다.",
                "검색 snippet이 아니라 deterministic verifier가 읽는 충분히 긴 공식 문서 fixture다.",
            )
        )
        document_path = self.job_root / "verification/source_pages/source.txt"
        document_path.parent.mkdir(parents=True, exist_ok=True)
        document_path.write_text(self.document, encoding="utf-8")
        self.document_relative_path = str(document_path.relative_to(self.job_root))
        self.document_hash = hashlib.sha256(document_path.read_bytes()).hexdigest()

    def test_parser_accepts_one_sentinel_json_and_rejects_multiple_blocks(self) -> None:
        delta = self._withdraw_delta()
        text = (
            "설명\nE2R_REPAIR_DELTA_JSON_BEGIN\n```json\n"
            + json.dumps(delta, ensure_ascii=False)
            + "\n```\nE2R_REPAIR_DELTA_JSON_END"
        )
        parsed = RepairDeltaV3Parser().parse_text(text)
        self.assertEqual(parsed.payload, delta)
        self.assertEqual(
            parsed.parser_operations,
            ("EXTRACT_REPAIR_DELTA_SENTINEL_BLOCK", "REMOVE_JSON_CODE_FENCE"),
        )
        with self.assertRaises(RepairDeltaV3ParseError):
            RepairDeltaV3Parser().parse_text(text + "\n" + text)

    def test_parser_removes_only_visible_dom_json_language_label(self) -> None:
        delta = self._withdraw_delta()
        text = (
            "E2R_REPAIR_DELTA_JSON_BEGIN\nJSON\n"
            + json.dumps(delta, ensure_ascii=False)
            + "\nE2R_REPAIR_DELTA_JSON_END"
        )
        parsed = RepairDeltaV3Parser().parse_text(text)
        self.assertEqual(parsed.payload, delta)
        self.assertEqual(
            parsed.parser_operations,
            (
                "EXTRACT_REPAIR_DELTA_SENTINEL_BLOCK",
                "REMOVE_STANDALONE_JSON_LANGUAGE_LABEL",
            ),
        )
        with self.assertRaises(RepairDeltaV3ParseError):
            RepairDeltaV3Parser().parse_text("JSON\n[]")

    def test_prompt_groups_same_source_root_cause_and_question_once(self) -> None:
        dossier = self._dossier()
        second = deepcopy(dossier["material_facts"][1])
        second["dossier_fact_id"] = "FACT-REJECTED-TWO"
        second["statement"] = "HBM 계약 가격 상승폭은 25%다."
        second["predicate_id"] = "HBM_PRICE_PREMIUM_SECOND"
        second["supporting_excerpt"] = "원문에 없는 두 번째 인용"
        dossier["material_facts"].append(second)
        dossier["source_lineages"][0]["fact_ids"].append(
            "FACT-REJECTED-TWO"
        )
        dossier["question_family_results"][0]["support_fact_ids"].append(
            "FACT-REJECTED-TWO"
        )
        dossier["search_route_receipts"][0]["accepted_fact_ids"].append(
            "FACT-REJECTED-TWO"
        )
        classifications = [
            self._classification("FACT-REJECTED"),
            self._classification("FACT-REJECTED-TWO"),
        ]
        verifications = [
            self._verification("FACT-REJECTED"),
            self._verification("FACT-REJECTED-TWO"),
        ]
        compiled = self._compile(
            dossier=dossier,
            classifications=classifications,
            verifications=verifications,
        )
        self.assertEqual(len(compiled.groups), 1)
        self.assertEqual(len(compiled.groups[0].candidates), 2)
        self.assertEqual(compiled.prompt_text.count(self.document), 1)
        self.assertEqual(
            {
                row["fetched_excerpt"]
                for row in compiled.groups[0].candidates
            },
            {self.replacement_excerpt},
        )
        self.assertNotIn('"material_facts"', compiled.prompt_text)
        self.assertEqual(
            compiled.to_receipt()["full_dossier_reoutput_requested_count"],
            0,
        )
        self.assertTrue(compiled.target_size_met)

    def test_local_or_representation_defect_never_routes_to_pro(self) -> None:
        classification = self._classification("FACT-REJECTED")
        classification["cause_class"] = "LOCAL_NORMALIZABLE"
        with self.assertRaisesRegex(ValueError, "cannot route to Pro"):
            self._compile(classifications=[classification])

    def test_nonmaterial_rejection_never_routes_to_pro(self) -> None:
        classification = self._classification("FACT-REJECTED")
        classification["material"] = False
        with self.assertRaisesRegex(ValueError, "nonmaterial"):
            self._compile(classifications=[classification])

    def test_large_source_is_compacted_without_transport_batching(self) -> None:
        huge = "공식 원문 " * 20_000
        path = self.job_root / self.document_relative_path
        path.write_text(huge, encoding="utf-8")
        verification = self._verification("FACT-REJECTED")
        verification["content_hash"] = hashlib.sha256(path.read_bytes()).hexdigest()
        compiled = self._compile(
            verifications=[verification],
            maximum_group_source_text_chars=150_000,
        )
        self.assertLess(compiled.prompt_char_count, 100_000)
        self.assertEqual(compiled.candidate_ids, ("FACT-REJECTED",))
        self.assertEqual(len(compiled.groups), 1)
        self.assertIn('"original_fact_field_order"', compiled.prompt_text)
        self.assertIn('"original_fact_values"', compiled.prompt_text)

    def test_forty_eight_candidates_across_seventeen_groups_fit_one_repair(
        self,
    ) -> None:
        dossier = self._dossier()
        accepted = deepcopy(dossier["material_facts"][0])
        rejected_template = deepcopy(dossier["material_facts"][1])
        dossier["material_facts"] = [accepted]
        dossier["source_documents"] = []
        dossier["source_lineages"][0]["fact_ids"] = ["FACT-ACCEPTED"]
        dossier["question_family_results"][0]["support_fact_ids"] = [
            "FACT-ACCEPTED"
        ]
        dossier["search_route_receipts"][0]["accepted_fact_ids"] = [
            "FACT-ACCEPTED"
        ]
        for source_index in range(17):
            source = deepcopy(self._dossier()["source_documents"][0])
            source["source_document_id"] = f"SRC-GROUP-{source_index:02d}"
            source["canonical_url"] = f"{self.url}/group/{source_index:02d}"
            source["opened_url"] = source["canonical_url"]
            dossier["source_documents"].append(source)
        candidate_ids = []
        for index in range(48):
            candidate_id = f"FACT-REJECTED-{index:02d}"
            candidate_ids.append(candidate_id)
            fact = deepcopy(rejected_template)
            fact.update(
                {
                    "dossier_fact_id": candidate_id,
                    "predicate_id": f"HBM_REPAIR_PREDICATE_{index:02d}",
                    "statement": f"HBM repair candidate {index:02d}는 검증이 필요하다.",
                    "source_document_id": f"SRC-GROUP-{index % 17:02d}",
                }
            )
            dossier["material_facts"].append(fact)
            dossier["source_lineages"][0]["fact_ids"].append(candidate_id)
            dossier["question_family_results"][0]["support_fact_ids"].append(
                candidate_id
            )
            dossier["search_route_receipts"][0]["accepted_fact_ids"].append(
                candidate_id
            )
        compiled = self._compile(
            dossier=dossier,
            classifications=[
                self._classification(candidate_id)
                for candidate_id in candidate_ids
            ],
            verifications=[
                self._verification(candidate_id)
                for candidate_id in candidate_ids
            ],
            maximum_group_source_text_chars=150_000,
        )

        self.assertEqual(len(compiled.groups), 17)
        self.assertEqual(len(compiled.candidate_ids), 48)
        self.assertLess(compiled.prompt_char_count, 100_000)
        self.assertNotIn('"material_facts"', compiled.prompt_text)

    def test_withdraw_preserves_accepted_fact_and_reopens_question(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        application = apply_repair_delta_v3(
            dossier=dossier,
            repair_delta=self._withdraw_delta(),
            compiled_prompt=compiled,
            prior_accepted_candidate_ids=("FACT-ACCEPTED",),
            prompt_hash=compiled.prompt_hash,
            response_hash="c" * 64,
        )
        facts = {
            row["dossier_fact_id"]
            for row in application.effective_dossier["material_facts"]
        }
        self.assertEqual(facts, {"FACT-ACCEPTED"})
        self.assertEqual(
            application.preserved_accepted_candidate_ids,
            ("FACT-ACCEPTED",),
        )
        question = application.effective_dossier["question_family_results"][0]
        self.assertEqual(question["status"], "PUBLIC_SEARCHABLE")
        self.assertIn(
            "FACT-REJECTED",
            application.effective_dossier["search_route_receipts"][0][
                "rejected_candidate_ids"
            ],
        )

    def test_narrow_replacement_requires_exact_scope_and_current_pass_route(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        application = apply_repair_delta_v3(
            dossier=dossier,
            repair_delta=delta,
            compiled_prompt=compiled,
            prior_accepted_candidate_ids=("FACT-ACCEPTED",),
            prompt_hash=compiled.prompt_hash,
            response_hash="d" * 64,
        )
        self.assertEqual(
            application.replacement_candidate_ids,
            ("FACT-REPLACEMENT",),
        )
        question = application.effective_dossier["question_family_results"][0]
        self.assertEqual(question["status"], "VERIFIER_REPAIR_REQUIRED")
        self.assertIn("FACT-REPLACEMENT", question["support_fact_ids"])
        no_route = deepcopy(delta)
        no_route["new_route_receipts"] = []
        with self.assertRaisesRegex(
            RepairDeltaV3ValidationError, "requires a current-pass route"
        ):
            apply_repair_delta_v3(
                dossier=dossier,
                repair_delta=no_route,
                compiled_prompt=compiled,
                prior_accepted_candidate_ids=("FACT-ACCEPTED",),
                prompt_hash=compiled.prompt_hash,
                response_hash="d" * 64,
            )

    def test_replace_adds_one_source_and_deterministic_lineage(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._replace_delta()
        application = apply_repair_delta_v3(
            dossier=dossier,
            repair_delta=delta,
            compiled_prompt=compiled,
            prior_accepted_candidate_ids=("FACT-ACCEPTED",),
            prompt_hash=compiled.prompt_hash,
            response_hash="3" * 64,
        )
        effective = application.effective_dossier
        self.assertIn(
            "SRC-TWO",
            {row["source_document_id"] for row in effective["source_documents"]},
        )
        lineage = next(
            row for row in effective["source_lineages"] if row["lineage_id"] == "SL-TWO"
        )
        self.assertEqual(lineage["source_document_ids"], ["SRC-TWO"])
        self.assertEqual(lineage["fact_ids"], ["FACT-REPLACEMENT"])
        self.assertTrue(lineage["independence_group_id"].startswith("SLGROUP-"))

    def test_transport_normalizer_binds_source_relabels_and_adds_pending_route(
        self,
    ) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._replace_delta()
        action = delta["repair_actions"][0]
        action["action"] = "NARROW"
        action["replacement_source_document"] = None
        action["fetched_excerpt"] = "Pro가 다시 고른 비권위 진단 excerpt"
        delta["new_route_receipts"] = []

        normalized, receipt = normalize_repair_delta_v3_transport(
            repair_delta=delta,
            dossier=dossier,
            compiled_prompt=compiled,
            performed_at="2026-08-22T03:04:05Z",
        )

        normalized_action = normalized["repair_actions"][0]
        self.assertEqual(normalized_action["action"], "REPLACE")
        self.assertEqual(
            normalized_action["replacement_source_document"][
                "source_document_id"
            ],
            "SRC-TWO",
        )
        self.assertEqual(
            normalized_action["replacement_fact"],
            action["replacement_fact"],
        )
        route = normalized["new_route_receipts"][0]
        self.assertEqual(route["provider_status"], "PROVIDER_PENDING")
        self.assertEqual(route["accepted_fact_ids"], ["FACT-REPLACEMENT"])
        self.assertEqual(receipt["replacement_semantic_field_changed_count"], 0)
        RepairDeltaV3Validator().validate(
            normalized,
            dossier=dossier,
            compiled_prompt=compiled,
        )

    def test_transport_normalizer_withdraws_source_scope_mismatch(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._replace_delta()
        delta["repair_actions"][0]["replacement_fact"]["issuer_scoped"] = False
        delta["new_route_receipts"] = []

        normalized, receipt = normalize_repair_delta_v3_transport(
            repair_delta=delta,
            dossier=dossier,
            compiled_prompt=compiled,
            performed_at="2026-08-22T03:04:05Z",
        )

        action = normalized["repair_actions"][0]
        self.assertEqual(action["action"], "WITHDRAW")
        self.assertIsNone(action["replacement_fact"])
        self.assertEqual(normalized["new_source_documents"], [])
        self.assertEqual(normalized["new_route_receipts"], [])
        self.assertEqual(
            receipt["scope_mismatched_replacement_withdrawn_count"],
            1,
        )
        RepairDeltaV3Validator().validate(
            normalized,
            dossier=dossier,
            compiled_prompt=compiled,
        )

    def test_transport_normalizer_restores_equivalent_url_and_new_fact_id(
        self,
    ) -> None:
        encoded_url = (
            "https://example.com/download?contentType=application%2Fpdf"
            "&fileName=4010%2Freport.pdf"
        )
        decoded_url = (
            "https://example.com/download?contentType=application/pdf"
            "&fileName=4010/report.pdf"
        )
        self.url = encoded_url
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        action = delta["repair_actions"][0]
        action["canonical_url"] = decoded_url
        action["replacement_fact"]["dossier_fact_id"] = "FACT-REJECTED"
        delta["new_route_receipts"][0]["opened_source_urls"] = [decoded_url]
        delta["new_route_receipts"][0]["accepted_fact_ids"] = ["FACT-REJECTED"]

        normalized, receipt = normalize_repair_delta_v3_transport(
            repair_delta=delta,
            dossier=dossier,
            compiled_prompt=compiled,
            performed_at="2026-08-22T03:04:05Z",
        )

        normalized_action = normalized["repair_actions"][0]
        replacement_id = normalized_action["replacement_fact"]["dossier_fact_id"]
        self.assertEqual(normalized_action["canonical_url"], encoded_url)
        self.assertNotEqual(replacement_id, "FACT-REJECTED")
        self.assertTrue(replacement_id.startswith("PROFACT-"))
        self.assertEqual(
            normalized["new_route_receipts"][0]["opened_source_urls"],
            [encoded_url],
        )
        self.assertEqual(
            normalized["new_route_receipts"][0]["accepted_fact_ids"],
            [replacement_id],
        )
        self.assertGreaterEqual(
            receipt["equivalent_url_encoding_normalized_count"],
            2,
        )
        self.assertEqual(receipt["replacement_fact_identity_reassigned_count"], 1)
        RepairDeltaV3Validator().validate(
            normalized,
            dossier=dossier,
            compiled_prompt=compiled,
        )

    def test_transport_normalizer_rejects_semantically_different_immutable_url(
        self,
    ) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        delta["repair_actions"][0]["canonical_url"] = (
            "https://other.example.org/unrelated"
        )

        with self.assertRaisesRegex(
            RepairDeltaV3ValidationError,
            "changed immutable scope.*canonical_url",
        ):
            normalize_repair_delta_v3_transport(
                repair_delta=delta,
                dossier=dossier,
                compiled_prompt=compiled,
                performed_at="2026-08-22T03:04:05Z",
            )

    def test_delta_cannot_escape_candidate_or_question_scope(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        delta["repair_actions"][0]["question_family_ids"] = [
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02"
        ]
        with self.assertRaisesRegex(
            RepairDeltaV3ValidationError, "immutable packet field"
        ):
            apply_repair_delta_v3(
                dossier=dossier,
                repair_delta=delta,
                compiled_prompt=compiled,
                prior_accepted_candidate_ids=("FACT-ACCEPTED",),
                prompt_hash=compiled.prompt_hash,
                response_hash="e" * 64,
            )

    def test_replacement_must_keep_initial_v3_preflight_contract(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        delta["repair_actions"][0]["replacement_fact"]["verifier_preflight"][
            "single_atomic_predicate"
        ] = False
        with self.assertRaisesRegex(
            RepairDeltaV3ValidationError, "schema validation failed"
        ):
            apply_repair_delta_v3(
                dossier=dossier,
                repair_delta=delta,
                compiled_prompt=compiled,
                prior_accepted_candidate_ids=("FACT-ACCEPTED",),
                prompt_hash=compiled.prompt_hash,
                response_hash="f" * 64,
            )

    def test_short_nonempty_repair_excerpt_is_preserved_for_reverification(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        delta["repair_actions"][0]["replacement_fact"][
            "supporting_excerpt"
        ] = "정기보수 영향"

        application = apply_repair_delta_v3(
            dossier=dossier,
            repair_delta=delta,
            compiled_prompt=compiled,
            prior_accepted_candidate_ids=("FACT-ACCEPTED",),
            prompt_hash=compiled.prompt_hash,
            response_hash="7" * 64,
        )

        replacement = next(
            row
            for row in application.effective_dossier["material_facts"]
            if row["dossier_fact_id"] == "FACT-REPLACEMENT"
        )
        self.assertEqual(replacement["supporting_excerpt"], "정기보수 영향")

    def test_accepted_fact_cannot_be_targeted_or_deleted(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        with self.assertRaisesRegex(
            RepairDeltaV3ValidationError, "cannot target an accepted fact"
        ):
            apply_repair_delta_v3(
                dossier=dossier,
                repair_delta=self._withdraw_delta(),
                compiled_prompt=compiled,
                prior_accepted_candidate_ids=(
                    "FACT-ACCEPTED",
                    "FACT-REJECTED",
                ),
                prompt_hash=compiled.prompt_hash,
                response_hash="1" * 64,
            )

    def test_later_repair_pass_keeps_deterministic_authority_boundary(self) -> None:
        compiled = self._compile(repair_pass_ordinal=2)

        self.assertEqual(compiled.repair_pass_ordinal, 2)
        self.assertFalse(compiled.to_receipt()["score_authority"])
        self.assertFalse(compiled.to_receipt()["stage_authority"])

    def test_later_repair_pass_reverifies_and_uses_distinct_artifact_root(
        self,
    ) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier, repair_pass_ordinal=2)
        fetcher = _CountingFetcher({self.url: self.document})
        service = CompactRepairServiceV3(
            verifier=ProSourceVerifier(page_fetcher=fetcher)
        )
        artifact_root = self.job_root / "repair_v3/passes/02_PROPASS-REPAIR"

        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.job_root,
            dossier=dossier,
            repair_delta=self._narrow_delta(),
            compiled_prompt=compiled,
            prior_verification_rows=[
                {"dossier_fact_id": "FACT-ACCEPTED", "status": "ACCEPTED_CURRENT"},
                {
                    "dossier_fact_id": "FACT-REJECTED",
                    "status": "REJECTED_QUOTE_MISMATCH",
                },
            ],
            response_hash="8" * 64,
            repair_pass_ordinal=2,
            repair_artifact_root=artifact_root,
        )

        self.assertEqual(run.repair_root, artifact_root.resolve())
        self.assertEqual(run.receipt["repair_pass_ordinal"], 2)
        self.assertTrue(run.receipt["operational_ready_allowed"])
        self.assertFalse(run.receipt["second_repair_pass_blocked"])
        self.assertTrue((artifact_root / "compact_repair_receipt.json").is_file())
        self.assertFalse((self.job_root / "repair_v3/compact_repair_receipt.json").exists())

    def test_one_compact_repair_is_reverified_and_persisted(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        fetcher = _CountingFetcher({self.url: self.document})
        service = CompactRepairServiceV3(
            verifier=ProSourceVerifier(page_fetcher=fetcher)
        )
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.job_root,
            dossier=dossier,
            repair_delta=self._narrow_delta(),
            compiled_prompt=compiled,
            prior_verification_rows=[
                {"dossier_fact_id": "FACT-ACCEPTED", "status": "ACCEPTED_CURRENT"},
                {
                    "dossier_fact_id": "FACT-REJECTED",
                    "status": "REJECTED_QUOTE_MISMATCH",
                },
            ],
            response_hash="2" * 64,
        )
        self.assertTrue(
            run.receipt["operational_ready_allowed"],
            (run.receipt, run.source_verification_rows),
        )
        self.assertEqual(run.receipt["full_dossier_reoutput_count"], 0)
        self.assertEqual(run.receipt["query_count"], 0)
        self.assertEqual(run.receipt["search_count"], 0)
        self.assertEqual(
            run.receipt["unresolved_replacement_candidate_ids"], []
        )
        self.assertEqual(
            run.effective_dossier["question_family_results"][0]["status"],
            "SUPPORTED_SCORING",
        )
        self.assertTrue(
            (run.repair_root / "compact_repair_receipt.json").is_file()
        )
        self.assertEqual(len(fetcher.calls), 1)

    def test_failed_replacement_is_withdrawn_without_second_repair(self) -> None:
        dossier = self._dossier()
        compiled = self._compile(dossier=dossier)
        delta = self._narrow_delta()
        delta["repair_actions"][0]["replacement_fact"][
            "supporting_excerpt"
        ] = "공개 원문에 없는 교체 문구"
        service = CompactRepairServiceV3(
            verifier=ProSourceVerifier(
                page_fetcher=_CountingFetcher({self.url: self.document})
            )
        )

        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.job_root,
            dossier=dossier,
            repair_delta=delta,
            compiled_prompt=compiled,
            prior_verification_rows=[
                {"dossier_fact_id": "FACT-ACCEPTED", "status": "ACCEPTED_CURRENT"},
                {
                    "dossier_fact_id": "FACT-REJECTED",
                    "status": "REJECTED_QUOTE_MISMATCH",
                },
            ],
            response_hash="9" * 64,
        )

        self.assertTrue(run.receipt["operational_ready_allowed"])
        self.assertEqual(
            run.receipt["failed_replacement_withdrawn_candidate_ids"],
            ["FACT-REPLACEMENT"],
        )
        self.assertEqual(
            run.receipt["unresolved_replacement_candidate_ids"],
            [],
        )
        fact_ids = {
            row["dossier_fact_id"]
            for row in run.effective_dossier["material_facts"]
        }
        self.assertEqual(fact_ids, {"FACT-ACCEPTED"})
        self.assertEqual(
            run.effective_dossier["question_family_results"][0]["status"],
            "SUPPORTED_SCORING",
        )

    def test_completed_old_repair_is_reconciled_append_only(self) -> None:
        parent = self._dossier()
        compiled = self._compile(dossier=parent)
        delta = self._narrow_delta()
        delta["new_route_receipts"][0]["route_receipt_id"] = (
            "PROREPAIRROUTE-TEST-COMPLETED"
        )
        application = apply_repair_delta_v3(
            dossier=parent,
            repair_delta=delta,
            compiled_prompt=compiled,
            prior_accepted_candidate_ids=("FACT-ACCEPTED",),
            prompt_hash=compiled.prompt_hash,
            response_hash="8" * 64,
        )
        repaired = deepcopy(dict(application.effective_dossier))
        repair_route = next(
            row
            for row in repaired["search_route_receipts"]
            if row["route_receipt_id"].startswith("PROREPAIRROUTE-")
        )
        repair_route["provider_status"] = "FAILED"
        repair_route["no_new_route_reason"] = (
            "Deterministic local source re-verification did not accept the fact"
        )

        effective, receipt = reconcile_completed_repair_fail_closed(
            repaired_dossier=repaired,
            parent_dossier=parent,
            repair_delta=delta,
            failed_replacement_ids=("FACT-REPLACEMENT",),
        )

        self.assertNotEqual(
            receipt["before_effective_dossier_hash"],
            receipt["after_effective_dossier_hash"],
        )
        self.assertEqual(receipt["new_query_count"], 0)
        self.assertEqual(receipt["new_pro_submit_count"], 0)
        self.assertEqual(
            receipt["failed_replacement_ids"],
            ["FACT-REPLACEMENT"],
        )
        self.assertEqual(
            {
                row["dossier_fact_id"]
                for row in effective["material_facts"]
            },
            {"FACT-ACCEPTED"},
        )
        self.assertEqual(
            effective["question_family_results"][0]["status"],
            "SUPPORTED_SCORING",
        )
        self.assertFalse(
            any(
                row["route_receipt_id"].startswith("PROREPAIRROUTE-")
                for row in effective["search_route_receipts"]
            )
        )

    def _compile(
        self,
        *,
        dossier: dict | None = None,
        classifications: list[dict] | None = None,
        verifications: list[dict] | None = None,
        repair_pass_ordinal: int = 1,
        maximum_group_source_text_chars: int = 12_000,
    ):
        return CompactRepairPromptCompilerV3().compile(
            dossier=dossier or self._dossier(),
            rejection_classifications=(
                classifications
                if classifications is not None
                else [self._classification("FACT-REJECTED")]
            ),
            verification_rows=(
                verifications
                if verifications is not None
                else [self._verification("FACT-REJECTED")]
            ),
            job_root=self.job_root,
            research_pass_id=self.repair_pass_id,
            parent_pass_id=self.initial_pass_id,
            repair_pass_ordinal=repair_pass_ordinal,
            maximum_group_source_text_chars=maximum_group_source_text_chars,
        )

    def _classification(self, candidate_id: str) -> dict:
        return {
            "candidate_id": candidate_id,
            "source_document_id": "SRC-ONE",
            "cause_class": "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
            "cause_code": "LITERAL_QUOTE_MISMATCH_AFTER_LOCAL_ATTEMPTS",
            "detail": "literal quote mismatch",
            "routing": "COMPACT_PRO_REPAIR_ALLOWED",
            "locally_resolved": False,
            "material": True,
            "verifier_status": "REJECTED_QUOTE_MISMATCH",
            "send_to_pro_allowed": True,
        }

    def _verification(self, candidate_id: str) -> dict:
        return {
            "dossier_fact_id": candidate_id,
            "status": "REJECTED_QUOTE_MISMATCH",
            "reason": "supporting excerpt is absent from fetched document",
            "source_url": self.url,
            "source_id": "PROSOURCE-ONE",
            "content_hash": self.document_hash,
            "document_path": self.document_relative_path,
        }

    def _withdraw_delta(self) -> dict:
        return {
            "schema_version": "e2r_pro_repair_delta_v3",
            "job_id": self.job.job_id,
            "run_id": "PRORUN-REPAIR-V3",
            "research_pass_id": self.repair_pass_id,
            "parent_pass_id": self.initial_pass_id,
            "target": self._target(),
            "as_of_date": self.as_of_date,
            "repair_actions": [
                {
                    "candidate_id": "FACT-REJECTED",
                    "question_family_ids": [
                        "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
                    ],
                    "rejection_category": "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
                    "original_statement": "HBM 계약 가격이 25% 상승했다.",
                    "source_document_id": "SRC-ONE",
                    "canonical_url": self.url,
                    "fetched_excerpt": self.replacement_excerpt,
                    "allowed_action": "CORRECT|REPLACE|NARROW|WITHDRAW",
                    "action": "WITHDRAW",
                    "replacement_source_document": None,
                    "replacement_fact": None,
                    "reason": "공개 원문이 25% 수치를 지지하지 않는다.",
                }
            ],
            "new_source_documents": [],
            "new_route_receipts": [],
            "score_authority": False,
            "stage_authority": False,
        }

    def _narrow_delta(self) -> dict:
        payload = self._withdraw_delta()
        action = payload["repair_actions"][0]
        action["action"] = "NARROW"
        action["reason"] = "원문이 직접 지지하는 20% 범위로 축소한다."
        action["replacement_fact"] = self._fact(
            fact_id="FACT-REPLACEMENT",
            pass_id=self.repair_pass_id,
            statement="HBM 계약 가격이 20% 상승했다.",
            predicate="HBM_PRICE_PREMIUM",
            excerpt=self.replacement_excerpt,
        )
        payload["new_route_receipts"] = [
            {
                "route_receipt_id": "ROUTE-REPAIR-ONE",
                "pass_id": self.repair_pass_id,
                "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                "gap_id": "GAP-REPAIR-ONE",
                "source_role_id": "ISSUER_OFFICIAL",
                "query_or_navigation_objective": "기존 공식 source 재검문",
                "query_text": None,
                "result_count_seen": 1,
                "opened_source_urls": [self.url],
                "accepted_fact_ids": ["FACT-REPLACEMENT"],
                "rejected_candidate_ids": [],
                "provider_status": "SUCCESS",
                "no_new_route_reason": None,
                "performed_at": "2026-08-22T03:00:00+00:00",
            }
        ]
        return payload

    def _replace_delta(self) -> dict:
        payload = self._narrow_delta()
        action = payload["repair_actions"][0]
        action["action"] = "REPLACE"
        source = {
            "source_document_id": "SRC-TWO",
            "canonical_url": "https://official.example.org/hbm-update",
            "opened_url": "https://official.example.org/hbm-update",
            "source_title": "HBM 공식 계약 업데이트",
            "source_publisher": "검증기업 IR",
            "publication_date": "2026-08-02",
            "availability_date": "2026-08-02",
            "source_role_ids": ["ISSUER_OFFICIAL"],
            "document_type": "IR",
            "target_scope": {
                "target_id": self.target_id,
                "issuer_scoped": True,
                "subject": self.company_name,
                "business_segment": "MEMORY",
                "product_family": "HBM",
            },
            "locator_type": "HTML_PARAGRAPH",
            "locator_value": "HBM 계약 가격",
            "lineage_id": "SL-TWO",
            "opened_and_read": True,
            "as_of_cutoff_pass": True,
        }
        action["replacement_source_document"] = source
        action["replacement_fact"]["source_document_id"] = "SRC-TWO"
        payload["new_source_documents"] = [source]
        payload["new_route_receipts"][0]["opened_source_urls"] = [
            source["canonical_url"]
        ]
        return payload

    def _target(self) -> dict:
        return {
            "target_id": self.target_id,
            "symbol": self.target_id,
            "company_name": self.company_name,
            "aliases": ["검증 기업"],
        }

    def _fact(
        self,
        *,
        fact_id: str,
        pass_id: str,
        statement: str,
        predicate: str,
        excerpt: str,
    ) -> dict:
        return {
            "dossier_fact_id": fact_id,
            "research_pass_id": pass_id,
            "fact_kind": "MATERIAL",
            "statement": statement,
            "predicate_id": predicate,
            "direction": "POSITIVE",
            "target_id": self.target_id,
            "subject": self.company_name,
            "issuer_scoped": True,
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism_id": "CAPACITY_SCARCITY",
            "value": 20,
            "unit": "%",
            "period": "2026",
            "event_date": "2026-08-01",
            "current_status": "CURRENT",
            "question_family_ids": [
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
            ],
            "candidate_component_ids": ["bottleneck_pricing"],
            "source_document_id": "SRC-ONE",
            "supporting_excerpt": excerpt,
            "source_locator": "HBM 계약 가격",
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

    def _dossier(self) -> dict:
        accepted = self._fact(
            fact_id="FACT-ACCEPTED",
            pass_id=self.initial_pass_id,
            statement="HBM capacity가 전량 배정됐다.",
            predicate="HBM_CAPACITY_ALLOCATED",
            excerpt=self.accepted_excerpt,
        )
        rejected = self._fact(
            fact_id="FACT-REJECTED",
            pass_id=self.initial_pass_id,
            statement="HBM 계약 가격이 25% 상승했다.",
            predicate="HBM_PRICE_PREMIUM",
            excerpt="원문에 없는 인용문이다.",
        )
        return {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": self.job.job_id,
            "run_id": "PRORUN-REPAIR-V3",
            "conversation_id": "CONVERSATION-REPAIR-V3",
            "research_pass_id": self.initial_pass_id,
            "parent_pass_id": None,
            "target": self._target(),
            "as_of_date": self.as_of_date,
            "candidate_archetypes": ["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            "selected_archetypes": ["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            "research_status": "NEEDS_PUBLIC_GAP_CLOSURE",
            "business_model": {},
            "source_documents": [
                {
                    "source_document_id": "SRC-ONE",
                    "canonical_url": self.url,
                    "opened_url": self.url,
                    "source_title": "HBM 공식 보고서",
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
                    "locator_value": "HBM 사업 보고",
                    "lineage_id": "SL-ONE",
                    "opened_and_read": True,
                    "as_of_cutoff_pass": True,
                }
            ],
            "material_facts": [accepted, rejected],
            "counterfacts": [],
            "resolution_facts": [],
            "derived_metrics": [],
            "question_family_results": [
                {
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                    "status": "SUPPORTED_SCORING",
                    "support_fact_ids": ["FACT-ACCEPTED", "FACT-REJECTED"],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                    "attempted_source_role_ids": ["ISSUER_OFFICIAL"],
                    "search_route_receipt_ids": ["ROUTE-INITIAL-ONE"],
                    "required_source_roles_satisfied": ["ISSUER_OFFICIAL"],
                    "required_source_roles_missing": [],
                    "availability_class": "PUBLIC_SEARCHABLE",
                    "affected_component_ids": ["bottleneck_pricing"],
                    "could_change_score": True,
                    "could_change_stage": False,
                    "could_change_hard_break": False,
                    "closure_reason": "공식 원문 fact가 연결됐다.",
                    "adequate_search_proven": False,
                }
            ],
            "component_research": {},
            "structured_metrics": {},
            "unresolved_gaps": [],
            "source_lineages": [
                {
                    "lineage_id": "SL-ONE",
                    "source_document_ids": ["SRC-ONE"],
                    "fact_ids": ["FACT-ACCEPTED", "FACT-REJECTED"],
                    "independence_group_id": "INDEPENDENCE-ONE",
                    "status": "ACTIVE",
                }
            ],
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-INITIAL-ONE",
                    "pass_id": self.initial_pass_id,
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
                    "gap_id": None,
                    "source_role_id": "ISSUER_OFFICIAL",
                    "query_or_navigation_objective": "공식 HBM 자료 확인",
                    "query_text": None,
                    "result_count_seen": 1,
                    "opened_source_urls": [self.url],
                    "accepted_fact_ids": ["FACT-ACCEPTED", "FACT-REJECTED"],
                    "rejected_candidate_ids": [],
                    "provider_status": "SUCCESS",
                    "no_new_route_reason": None,
                    "performed_at": "2026-08-01T00:00:00+00:00",
                }
            ],
            "research_passes": [
                {
                    "pass_id": self.initial_pass_id,
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


if __name__ == "__main__":
    unittest.main()
