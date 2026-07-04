import unittest
import json
import subprocess
from datetime import date
from pathlib import Path
from unittest.mock import patch

from e2r.production.claim_extraction import (
    ContractBlindRawAssertionExtractor,
    ExtractionInput,
    adjudicate_entity_temporal_scope,
    map_claim_to_primitive,
)
from e2r.production.claim_extraction.extractor_provider import (
    ALLOWED_PREDICATES,
    CodexCLIExtractorProvider,
    EXTRACTOR_OUTPUT_SCHEMA,
    _codex_command,
    _prompt_payload,
    _records_from_payload,
)
from e2r.production.official_live_shadow import _claim_satisfies_source_task


class CutoverContractBlindExtractionTests(unittest.TestCase):
    def test_extractor_rejects_primitive_gap_context(self):
        extractor = ContractBlindRawAssertionExtractor()
        with self.assertRaises(ValueError):
            extractor.extract(
                ExtractionInput(
                    target_entity_id="TICKER:005930",
                    target_aliases=("삼성전자", "005930"),
                    as_of_date="2026-06-30",
                    document_id="DOC1",
                    anchor_id="ANCHOR1",
                    source_text="삼성전자는 목표주가가 상향됐다.",
                    extra_context={"primitive_gap": "medium_term_revision_visibility"},
                )
            )

    def test_extractor_rejects_score_stage_and_eligibility_context(self):
        extractor = ContractBlindRawAssertionExtractor()
        forbidden_keys = [
            "current_score_eligible",
            "hard_break",
            "verified",
            "green_gate",
            "score_gap_context",
        ]
        for key in forbidden_keys:
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError, key):
                    extractor.extract(
                        ExtractionInput(
                            target_entity_id="TICKER:005930",
                            target_aliases=("삼성전자", "005930"),
                            as_of_date="2026-06-30",
                            document_id="DOC1",
                            anchor_id="ANCHOR1",
                            source_text="삼성전자는 목표주가가 상향됐다.",
                            extra_context={key: True},
                        )
                    )

    def test_normal_audit_opinion_is_normal_not_positive_score_hint(self):
        extractor = ContractBlindRawAssertionExtractor()
        assertions = extractor.extract(
            ExtractionInput(
                target_entity_id="TICKER:005930",
                target_aliases=("삼성전자", "005930"),
                as_of_date="2026-06-30",
                document_id="DOC1",
                anchor_id="ANCHOR1",
                source_text="삼성전자의 감사의견은 적정이다.",
                extra_context={},
            )
        )
        self.assertEqual(len(assertions), 1)
        self.assertEqual(assertions[0].predicate, "audit_or_accounting_claim")
        self.assertEqual(assertions[0].polarity_proposal, "NORMAL")

    def test_official_document_fact_maps_only_to_information_confidence(self):
        extractor = ContractBlindRawAssertionExtractor()
        assertions = extractor.extract(
            ExtractionInput(
                target_entity_id="TICKER:005930",
                target_aliases=("삼성전자", "005930"),
                as_of_date="2026-06-30",
                document_id="DOC1",
                anchor_id="ANCHOR1",
                source_text="삼성전자(005930) OpenDART disclosure 접수번호 20260630000001 접수일 2026-06-30",
                extra_context={},
            )
        )
        self.assertEqual(len(assertions), 1)
        self.assertEqual(assertions[0].predicate, "official_document_fact")
        adjudication = adjudicate_entity_temporal_scope(
            assertions[0],
            target_aliases=("삼성전자", "005930"),
            as_of_date=date(2026, 6, 30),
            source_published_at=date(2026, 6, 30),
        )
        mapping = map_claim_to_primitive(
            assertions[0],
            adjudication,
            allowed_primitives=("information_confidence", "contract_quality"),
        )
        self.assertEqual(mapping.mapping_status, "ACCEPTED")
        self.assertEqual(mapping.primitive_id, "information_confidence")

    def test_structured_dart_contract_title_maps_to_contract_before_generic_fact(self):
        extractor = ContractBlindRawAssertionExtractor()
        assertions = extractor.extract(
            ExtractionInput(
                target_entity_id="TICKER:005930",
                target_aliases=("삼성전자", "005930"),
                as_of_date="2026-06-30",
                document_id="DOC1",
                anchor_id="ANCHOR1",
                source_text="삼성전자(005930) [기재정정]단일판매ㆍ공급계약체결 OpenDART 접수번호 20260630000001 접수일 2026-06-30",
                extra_context={},
            )
        )
        self.assertEqual(len(assertions), 1)
        self.assertEqual(assertions[0].predicate, "contract_or_order_claim")
        adjudication = adjudicate_entity_temporal_scope(
            assertions[0],
            target_aliases=("삼성전자", "005930"),
            as_of_date=date(2026, 6, 30),
            source_published_at=date(2026, 6, 30),
        )
        mapping = map_claim_to_primitive(
            assertions[0],
            adjudication,
            allowed_primitives=("information_confidence", "contract_quality"),
        )
        self.assertEqual(mapping.mapping_status, "ACCEPTED")
        self.assertEqual(mapping.primitive_id, "contract_quality")

    def test_baseline_information_claim_does_not_complete_unrelated_source_task(self):
        self.assertFalse(
            _claim_satisfies_source_task(
                "information_confidence",
                {"primitive_gap": "capital_allocation_event"},
            )
        )
        self.assertTrue(
            _claim_satisfies_source_task(
                "information_confidence",
                {"primitive_gap": "information_confidence"},
            )
        )

    def test_facility_investment_correction_does_not_map_to_positive_capacity_score(self):
        extractor = ContractBlindRawAssertionExtractor()
        assertions = extractor.extract(
            ExtractionInput(
                target_entity_id="TICKER:003090",
                target_aliases=("대웅", "003090"),
                as_of_date="2026-07-01",
                document_id="DOC1",
                anchor_id="ANCHOR1",
                source_text="대웅(003090) [기재정정]신규시설투자등 정정사유 종료일 연장 정정전 2026-06-30 정정후 2027-05-31 OpenDART 접수번호 20260630801612",
                extra_context={},
            )
        )
        self.assertEqual(len(assertions), 1)
        self.assertEqual(assertions[0].predicate, "capacity_investment_claim")
        adjudication = adjudicate_entity_temporal_scope(
            assertions[0],
            target_aliases=("대웅", "003090"),
            as_of_date=date(2026, 7, 1),
            source_published_at=date(2026, 6, 30),
        )
        mapping = map_claim_to_primitive(
            assertions[0],
            adjudication,
            allowed_primitives=("capacity_expansion", "capacity_precommitted", "information_confidence"),
        )
        self.assertEqual(mapping.mapping_status, "REJECTED")
        self.assertEqual(mapping.support_direction, "NEUTRAL")
        self.assertEqual(mapping.rationale, "facility_investment_correction_requires_followup_not_positive_capacity")

    def test_codex_payload_decoder_accepts_quote_alias_and_dedupes_empty_rows(self):
        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-06-30",
            document_id="DOC1",
            anchor_id="ANCHOR1",
            source_text="삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.",
            extra_context={},
        )

        records = _records_from_payload(
            request,
            [
                {
                    "subject_text": "삼성전자",
                    "predicate": "customer_allocation_or_qualification_claim",
                    "quote_text": "삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.",
                    "polarity": "POSITIVE",
                },
                {
                    "subject_text": "삼성전자",
                    "predicate": "customer_allocation_or_qualification_claim",
                    "quote_text": "삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.",
                    "polarity": "POSITIVE",
                },
                {
                    "subject_text": "삼성전자",
                    "predicate": "customer_allocation_or_qualification_claim",
                    "quote_text": "",
                    "polarity": "POSITIVE",
                },
            ],
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].subject, "삼성전자")
        self.assertEqual(records[0].exact_quote, "삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.")
        self.assertEqual(records[0].polarity_proposal, "POSITIVE")

    def test_codex_extractor_prompt_and_schema_force_predicate_taxonomy_without_score_context(self):
        request = ExtractionInput(
            target_entity_id="TICKER:003090",
            target_aliases=("대웅", "003090"),
            as_of_date="2026-07-01",
            document_id="DOC1",
            anchor_id="ANCHOR1",
            source_text="대웅은 자회사 신규시설투자의 종료일을 연장한다고 공시했다.",
            extra_context={},
        )

        payload = _prompt_payload(request)
        schema_predicates = (
            EXTRACTOR_OUTPUT_SCHEMA["properties"]["raw_assertions"]["items"]["properties"]["predicate"]["enum"]
        )

        self.assertIn("capacity_investment_claim", payload["allowed_predicates"])
        self.assertIn("capacity_investment_claim", schema_predicates)
        self.assertIn("mention_only", schema_predicates)
        item_schema = EXTRACTOR_OUTPUT_SCHEMA["properties"]["raw_assertions"]["items"]
        self.assertEqual(set(item_schema["required"]), set(item_schema["properties"]))
        self.assertEqual(item_schema["properties"]["event_date"]["type"], "string")
        self.assertEqual(item_schema["properties"]["uncertainty_reason"]["type"], "string")
        self.assertEqual(tuple(payload["allowed_predicates"]), ALLOWED_PREDICATES)
        self.assertNotIn("primitive_gap", payload)
        self.assertNotIn("score_gap_context", payload)
        self.assertTrue(
            any("do not use mention_only" in rule.lower() for rule in payload["rules"]),
            payload["rules"],
        )

    def test_codex_extractor_prompt_compacts_long_document_without_score_context(self):
        target_sentence = "삼성전자는 HBM 고객 물량 배정과 capacity sold out에 따른 공급 제약을 설명했다."
        tail_sentence = "회사는 다음 분기 출하와 현금흐름 전환을 추가로 설명할 예정이다."
        long_text = (
            "반복 배경 문장입니다. " * 500
            + target_sentence
            + "\n"
            + "목표주가 관련 일반 코멘트입니다. " * 200
            + tail_sentence
        )
        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC-LONG",
            anchor_id="ANCHOR-LONG",
            source_text=long_text,
            extra_context={},
        )

        payload = _prompt_payload(request, text_limit=3600)

        self.assertTrue(payload["document_text_compacted"])
        self.assertEqual(payload["document_text_chars"], len(long_text))
        self.assertLess(len(payload["document_text"]), len(long_text))
        self.assertIn(target_sentence, payload["document_text"])
        self.assertIn(tail_sentence, payload["document_text"])
        self.assertIn("[[high_signal_sentences]]", payload["document_text"])
        self.assertNotIn("primitive_gap", payload)
        self.assertNotIn("score_gap_context", payload)
        self.assertEqual(payload["document_text_selection_policy"], "contract_blind_head_signal_tail_v1")

    def test_codex_extractor_timeout_retries_once_with_smaller_contract_blind_prompt(self):
        calls: list[str] = []
        quote = "삼성전자는 HBM 고객 물량 배정과 capacity sold out에 따른 공급 제약을 설명했다."
        signal_block = "\n".join(
            (
                f"삼성전자는 {index}번째 HBM 고객 물량 배정과 capacity sold out에 따른 공급 제약을 설명했고 "
                "출하 일정, 고객사 qualification, ASP, 현금흐름 전환, 장기 공급 가능성, 생산능력 제약, "
                "분기별 매출 인식 조건을 함께 언급했다."
            )
            for index in range(30)
        )
        long_text = "반복 배경 문장입니다. " * 500 + signal_block + " 후행 설명입니다. " * 500

        def fake_run(command, *, prompt, timeout):
            calls.append(prompt)
            if len(calls) == 1:
                raise subprocess.TimeoutExpired(cmd=command, timeout=timeout)
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(
                json.dumps(
                    {
                        "raw_assertions": [
                            {
                                "subject": "삼성전자",
                                "predicate": "capacity_allocation_claim",
                                "object_text": quote,
                                "polarity_proposal": "POSITIVE",
                                "modality": "STATED",
                                "event_date": "",
                                "exact_quote": quote,
                                "related_entities": ["삼성전자"],
                                "uncertainty_reason": "",
                            }
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            return subprocess.CompletedProcess(command, 0, "", "")

        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC-LONG",
            anchor_id="ANCHOR-LONG",
            source_text=long_text,
            extra_context={},
        )

        with patch("e2r.production.claim_extraction.extractor_provider._run_codex_command", side_effect=fake_run):
            result = CodexCLIExtractorProvider(repo_root=".", timeout_seconds=1).extract(request)

        self.assertIsNone(result.provider_error)
        self.assertEqual(result.attempt_count, 2)
        self.assertTrue(result.timeout_retry_attempted)
        self.assertEqual(len(result.raw_assertions), 1)
        self.assertEqual(result.raw_assertions[0].predicate, "capacity_allocation_claim")
        self.assertEqual(len(calls), 2)
        self.assertLess(len(calls[1]), len(calls[0]))
        self.assertNotEqual(result.initial_prompt_hash, result.retry_prompt_hash)
        self.assertEqual(result.retry_prompt_hash, result.prompt_hash)
        self.assertNotIn("score_gap_context", calls[1])
        self.assertNotIn("primitive_gap", calls[1])

    def test_codex_extractor_runtime_budget_caps_subprocess_timeout(self):
        observed_timeouts: list[float] = []

        def fake_run(command, *, prompt, timeout):
            observed_timeouts.append(timeout)
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps({"raw_assertions": []}), encoding="utf-8")
            return subprocess.CompletedProcess(command, 0, "", "")

        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC-BUDGET",
            anchor_id="ANCHOR-BUDGET",
            source_text="삼성전자는 HBM 고객 물량 배정을 설명했다.",
            extra_context={},
        )

        provider = CodexCLIExtractorProvider(
            repo_root=".",
            timeout_seconds=30,
            remaining_budget_seconds=lambda: 7.0,
        )
        with patch("e2r.production.claim_extraction.extractor_provider._run_codex_command", side_effect=fake_run):
            result = provider.extract(request)

        self.assertIsNone(result.provider_error)
        self.assertEqual(observed_timeouts, [5.0])
        self.assertEqual(result.timeout_seconds, 5.0)

    def test_codex_extractor_runtime_budget_insufficient_skips_subprocess(self):
        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC-BUDGET-SKIP",
            anchor_id="ANCHOR-BUDGET-SKIP",
            source_text="삼성전자는 HBM 고객 물량 배정을 설명했다.",
            extra_context={},
        )

        provider = CodexCLIExtractorProvider(
            repo_root=".",
            timeout_seconds=30,
            remaining_budget_seconds=lambda: 4.0,
        )
        with patch("e2r.production.claim_extraction.extractor_provider._run_codex_command") as run_mock:
            result = provider.extract(request)

        run_mock.assert_not_called()
        self.assertEqual(result.provider_error, "codex_cli_runtime_budget_insufficient_before_initial_call")
        self.assertEqual(result.attempt_count, 0)
        self.assertEqual(result.timeout_seconds, 0.0)
        self.assertTrue(result.raw_prompt_payload)

    def test_codex_extractor_timeout_retry_non_json_becomes_provider_error(self):
        calls: list[str] = []

        def fake_run(command, *, prompt, timeout):
            calls.append(prompt)
            if len(calls) == 1:
                raise subprocess.TimeoutExpired(cmd=command, timeout=timeout)
            return subprocess.CompletedProcess(command, 0, "not-json", "")

        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC-LONG",
            anchor_id="ANCHOR-LONG",
            source_text="삼성전자는 HBM 고객 물량 배정을 설명했다.",
            extra_context={},
        )

        with patch("e2r.production.claim_extraction.extractor_provider._run_codex_command", side_effect=fake_run):
            result = CodexCLIExtractorProvider(repo_root=".", timeout_seconds=1).extract(request)

        self.assertEqual(result.attempt_count, 2)
        self.assertTrue(result.timeout_retry_attempted)
        self.assertTrue(result.provider_error)
        self.assertIn("codex_cli_timeout_initial_then_retry_RuntimeError", result.provider_error)
        self.assertFalse(result.raw_assertions)

    def test_codex_extractor_nonzero_exit_with_json_is_provider_error(self):
        def fake_run(command, *, prompt, timeout):
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps({"raw_assertions": []}), encoding="utf-8")
            return subprocess.CompletedProcess(command, 1, "", "unit cli failed")

        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC1",
            anchor_id="ANCHOR1",
            source_text="삼성전자는 HBM 고객 물량 배정을 설명했다.",
            extra_context={},
        )

        with patch("e2r.production.claim_extraction.extractor_provider._run_codex_command", side_effect=fake_run):
            result = CodexCLIExtractorProvider(repo_root=".", timeout_seconds=1).extract(request)

        self.assertEqual(result.attempt_count, 1)
        self.assertTrue(result.provider_error)
        self.assertIn("RuntimeError", result.provider_error)
        self.assertFalse(result.raw_assertions)

    def test_codex_extractor_source_metadata_drops_forbidden_context_keys(self):
        request = ExtractionInput(
            target_entity_id="TICKER:005930",
            target_aliases=("삼성전자", "005930"),
            as_of_date="2026-07-01",
            document_id="DOC1",
            anchor_id="ANCHOR1",
            source_text="삼성전자는 HBM 고객 물량 배정을 설명했다.",
            source_metadata={
                "canonical_url": "https://example.com/report",
                "primitive_gap": "customer_preorder_or_allocation",
                "nested": {"score": 90, "safe": "kept"},
                "items": [{"stage": "3-Green", "source_name": "kept"}],
            },
            extra_context={},
        )

        payload = _prompt_payload(request)

        self.assertEqual(payload["source_metadata_removed_forbidden_key_count"], 3)
        self.assertEqual(payload["source_metadata"]["canonical_url"], "https://example.com/report")
        self.assertEqual(payload["source_metadata"]["nested"], {"safe": "kept"})
        self.assertEqual(payload["source_metadata"]["items"], [{"source_name": "kept"}])
        self.assertNotIn("primitive_gap", json.dumps(payload["source_metadata"], ensure_ascii=False))
        self.assertNotIn("3-Green", json.dumps(payload["source_metadata"], ensure_ascii=False))

    def test_codex_command_uses_output_schema_for_contract_blind_extractor(self):
        command = _codex_command(
            repo_root=".",
            model="codex-cli-default",
            output_path="extractor_output.json",
            output_schema_path="extractor_schema.json",
        )

        self.assertIn("--output-schema", command)
        self.assertEqual(command[command.index("--output-schema") + 1], "extractor_schema.json")

    def test_codex_payload_decoder_downgrades_unknown_predicate_to_mention_only(self):
        request = ExtractionInput(
            target_entity_id="TICKER:003090",
            target_aliases=("대웅", "003090"),
            as_of_date="2026-07-01",
            document_id="DOC1",
            anchor_id="ANCHOR1",
            source_text="대웅은 자회사 신규시설투자의 종료일을 연장한다고 공시했다.",
            extra_context={},
        )

        records = _records_from_payload(
            request,
            [
                {
                    "subject": "대웅",
                    "predicate": "facility delay",
                    "object_text": "대웅은 자회사 신규시설투자의 종료일을 연장한다고 공시했다.",
                    "polarity_proposal": "NEGATIVE",
                    "modality": "STATED",
                    "event_date": "2026-06-30",
                    "exact_quote": "대웅은 자회사 신규시설투자의 종료일을 연장한다고 공시했다.",
                    "related_entities": ["대웅"],
                }
            ],
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].predicate, "mention_only")


if __name__ == "__main__":
    unittest.main()
