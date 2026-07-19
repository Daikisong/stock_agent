from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    EVIDENCE_FACT_EXTRACTION_SCHEMA,
    ResearcherEvidenceFactExtractor,
    production_material_fact_rows,
    write_researcher_fact_extraction_result,
)
from e2r.research_brain.researcher_mode.component_researcher import (
    FACT_EXTRACTION_PAGE_FACT_LIMIT,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    _load_fact_checkpoint,
)


TARGET = "CURRENT-TARGET"
TARGET_NAME = "Current Corp"
AS_OF_DATE = "2026-06-29"
ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"


class FactProvider:
    provider_name = "TEST_FACT_PROVIDER"

    def __init__(
        self,
        *,
        bad_quote: bool = False,
        fail: bool = False,
        wrong_scope: bool = False,
    ) -> None:
        self.bad_quote = bad_quote
        self.fail = fail
        self.wrong_scope = wrong_scope
        self.calls: list[Mapping[str, Any]] = []

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if self.fail:
            raise RuntimeError("provider offline")
        self.assert_fact_pass(pass_name)
        documents = payload["full_documents"]
        return {
            "facts": [
                {
                    "document_id": row["document_id"],
                    "question_family_id": "cash_earnings_conversion",
                    "subject_id": "target_core_business",
                    "subject": "Current Corp core business",
                    "business_segment": "CORE",
                    "product_family": "CORE_PRODUCT",
                    "scope_business_segment": "FOUNDRY" if self.wrong_scope else "MEMORY",
                    "scope_product_family": "LOGIC_FOUNDRY" if self.wrong_scope else "HBM",
                    "scope_technology_family": "FOUNDRY" if self.wrong_scope else "HBM",
                    "scope_transaction_type": "CUSTOMER_COMMITMENT" if self.wrong_scope else "REVENUE_ACTUAL",
                    "scope_economic_mechanism": "CUSTOMER_ALLOCATION" if self.wrong_scope else "REVENUE_CONVERSION",
                    "scope_confidence": 0.9,
                    "economic_mechanism": "capacity converts into cash earnings",
                    "mechanism_scope_id": "TARGET_DIRECT_CASH_EARNINGS",
                    "predicate": "reported record operating cash flow",
                    "predicate_family": "operating_cash_flow_actual",
                    "value": "record_high",
                    "normalized_object": "record_operating_cash_flow",
                    "unit": "qualitative",
                    "period": "2026Q1",
                    "direction": "POSITIVE",
                    "current_lifecycle": "CURRENT",
                    "exact_quote": (
                        "quote not found"
                        if self.bad_quote
                        else "Current Corp reported record operating cash flow in 2026Q1."
                    ),
                    "material": True,
                    "materiality": "CRITICAL",
                    "materiality_rationale": "cash conversion is material",
                    "confidence": 0.8,
                    "question_family_tags": ["cash_conversion"],
                    "primitive_tags": [],
                    "structured_evidence_roles": [],
                }
                for row in documents
            ],
            "document_dispositions": [
                {
                    "document_id": row["document_id"],
                    "status": (
                        "WRONG_TARGET_OR_SEGMENT"
                        if self.wrong_scope
                        else "FACTS_EXTRACTED"
                    ),
                    "rationale": "exact quote supports a material current fact",
                }
                for row in documents
            ],
            "unresolved_document_ids": [],
            "unresolved_research_notes": [],
            "extraction_complete": True,
        }

    def assert_fact_pass(self, pass_name: str) -> None:
        if pass_name != "EVIDENCE_FACT_EXTRACTION":
            raise AssertionError(pass_name)


class CorrectingQuoteFactProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        self.bad_quote = "fact_extraction_retry_context" not in payload
        return super().complete(pass_name=pass_name, payload=payload)


class WrappedQuotePercentConfidenceProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        response["facts"] = [dict(row) for row in response["facts"]]
        for fact in response["facts"]:
            fact["exact_quote"] = f'"{fact["exact_quote"]}"'
            fact["confidence"] = 100
            fact["scope_confidence"] = "90"
        return response


class PagedFactProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        template = dict(response["facts"][0])
        continuation = payload.get("fact_extraction_continuation_context")
        start = FACT_EXTRACTION_PAGE_FACT_LIMIT if continuation else 0
        stop = min(start + FACT_EXTRACTION_PAGE_FACT_LIMIT, 13)
        response["facts"] = []
        for index in range(start, stop):
            fact = dict(template)
            fact.update(
                {
                    "question_family_id": f"question_{index}",
                    "subject_id": f"subject_{index}",
                    "subject": f"Current Corp fact {index}",
                    "predicate": f"reported material fact {index}",
                    "predicate_family": f"predicate_{index}",
                    "normalized_object": f"material_fact_{index}",
                    "exact_quote": (
                        f"Current Corp material fact number {index}."
                    ),
                }
            )
            response["facts"].append(fact)
        more = stop < 13
        document_id = payload["full_documents"][0]["document_id"]
        response["document_dispositions"] = [
            {
                "document_id": document_id,
                "status": "FACTS_EXTRACTED",
                "rationale": "페이지별로 모든 고유 사실을 추출했다.",
            }
        ]
        response["unresolved_document_ids"] = [document_id] if more else []
        response["extraction_complete"] = not more
        return response


class BoundaryCompletePagedFactProvider(PagedFactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        document_id = payload["full_documents"][0]["document_id"]
        if not payload.get("fact_extraction_continuation_context"):
            response["facts"] = response["facts"][:FACT_EXTRACTION_PAGE_FACT_LIMIT]
            response["unresolved_document_ids"] = []
            response["extraction_complete"] = True
        else:
            response["facts"] = []
            response["document_dispositions"] = [
                {
                    "document_id": document_id,
                    "status": "FACTS_EXTRACTED",
                    "rationale": "마지막 빈 페이지로 추가 사실이 없음을 확인했다.",
                }
            ]
            response["unresolved_document_ids"] = []
            response["extraction_complete"] = True
        return response


class WhitespaceVariantPagedFactProvider(PagedFactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        continuation = payload.get("fact_extraction_continuation_context")
        if continuation:
            duplicate = dict(response["facts"][0])
            duplicate.update(
                {
                    "question_family_id": "question_0",
                    "subject_id": "subject_0",
                    "subject": "Current Corp fact 0",
                    "predicate": "reported material fact 0",
                    "predicate_family": "predicate_0",
                    "normalized_object": "material_fact_0",
                    "exact_quote": "CurrentCorpmaterialfactnumber0.",
                }
            )
            response["facts"] = [duplicate]
            response["unresolved_document_ids"] = []
            response["extraction_complete"] = True
        return response


class CorrectingCompletionFactProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        retry = payload.get("fact_extraction_retry_context")
        response["facts"] = []
        response["document_dispositions"] = [
            {
                "document_id": row["document_id"],
                "status": "NO_MATERIAL_FACT",
                "rationale": "이 전송 청크에는 material fact가 없다.",
            }
            for row in payload["full_documents"]
        ]
        response["unresolved_research_notes"] = [
            "다른 원문에서 전체 thesis 근거를 계속 찾아야 한다."
        ]
        corrected = bool(
            retry
            and "local to this supplied batch" in str(retry.get("instruction") or "")
        )
        response["unresolved_document_ids"] = (
            [] if corrected else [payload["full_documents"][0]["document_id"]]
        )
        response["extraction_complete"] = corrected
        return response


class MixedValidInvalidThenDispositionProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        response["facts"] = [dict(row) for row in response["facts"]]
        retry = payload.get("fact_extraction_retry_context")
        if retry is None:
            invalid = dict(response["facts"][0])
            invalid["normalized_object"] = "unsupported_duplicate_claim"
            invalid["exact_quote"] = "quote not found"
            response["facts"].append(invalid)
            return response
        response["facts"] = []
        response["document_dispositions"] = [
            {
                "document_id": row["document_id"],
                "status": (
                    "NO_MATERIAL_FACT"
                    if int(retry["rewrite_attempt"]) == 1
                    else "FACTS_EXTRACTED"
                ),
                "rationale": (
                    "첫 재작성에서 이미 검증된 사실을 잘못 누락했다."
                    if int(retry["rewrite_attempt"]) == 1
                    else "앞선 응답에서 검증된 사실을 보존한다."
                ),
            }
            for row in payload["full_documents"]
        ]
        return response


class RepeatsAcceptedFactOnRetryProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        response["facts"] = [dict(row) for row in response["facts"]]
        if "fact_extraction_retry_context" not in payload:
            invalid = dict(response["facts"][0])
            invalid["normalized_object"] = "unsupported_duplicate_claim"
            invalid["exact_quote"] = "quote not found"
            response["facts"].append(invalid)
        return response


class QuoteFailureThenNoMaterialProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        self.bad_quote = "fact_extraction_retry_context" not in payload
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        if "fact_extraction_retry_context" in payload:
            response["facts"] = []
            response["document_dispositions"] = [
                {
                    "document_id": row["document_id"],
                    "status": "NO_MATERIAL_FACT",
                    "rationale": (
                        "인용 실패를 이유로 material 문서를 무관 자료로 닫는다."
                    ),
                }
                for row in payload["full_documents"]
            ]
        return response


class StructurallyCompleteFalseProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        response["facts"] = []
        response["document_dispositions"] = [
            {
                "document_id": row["document_id"],
                "status": "NO_MATERIAL_FACT",
                "rationale": "현재 전송 청크에는 material fact가 없다.",
            }
            for row in payload["full_documents"]
        ]
        response["unresolved_document_ids"] = []
        response["unresolved_research_notes"] = [
            "부모 문서의 나머지 전송 청크는 별도 배치에서 계속 처리한다."
        ]
        response["extraction_complete"] = False
        return response


class StructurallyIncompleteFalseProvider(StructurallyCompleteFalseProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        response["unresolved_document_ids"] = [
            payload["full_documents"][0]["document_id"]
        ]
        return response


class ChunkAwareFactProvider(FactProvider):
    def __init__(self, *, fail_chunk_index: int | None = None) -> None:
        super().__init__()
        self.fail_chunk_index = fail_chunk_index

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        document = payload["full_documents"][0]
        chunk_index = int(
            (document.get("transport_chunk") or {}).get("chunk_index") or 0
        )
        if self.fail_chunk_index == chunk_index:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            raise StructuredProviderUnavailable("codex_cli_timeout")
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        quote = "Current Corp reported record operating cash flow in 2026Q1."
        if quote not in str(document.get("content_text") or ""):
            response["facts"] = []
            response["document_dispositions"] = [
                {
                    "document_id": document["document_id"],
                    "status": "NO_MATERIAL_FACT",
                    "rationale": "이 전송 청크에는 추가 material fact가 없다.",
                }
            ]
        return response


class E2RV5FactExtractionTests(unittest.TestCase):
    def test_every_full_document_is_processed_and_independent_sources_dedupe_fact(self) -> None:
        provider = FactProvider()
        result = ResearcherEvidenceFactExtractor(
            provider=provider,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(
                _document("DOC-1", "ISSUER_PRESENTATION", "ISSUER:current.example"),
                _document("DOC-2", "REUTERS", "REUTERS:reuters.example"),
            ),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(result.material_claims), 2)
        self.assertEqual(len(result.facts), 1)
        self.assertEqual(
            set(result.facts[0].source_ids),
            {"DOC-1", "DOC-2"},
        )
        self.assertEqual(
            set(result.facts[0].corroborating_independence_groups),
            {"ISSUER:current.example", "REUTERS:reuters.example"},
        )
        production = production_material_fact_rows(result)
        self.assertEqual(production[0]["question_family_id"], "cash_earnings_conversion")
        self.assertEqual(production[0]["temporal_status"], "CURRENT")
        self.assertFalse(production[0]["gold_visibility"])
        with tempfile.TemporaryDirectory() as directory:
            paths = write_researcher_fact_extraction_result(result, directory)
            self.assertTrue(all(path.is_file() for path in paths.values()))

    def test_large_prior_fact_graph_is_compact_while_full_document_is_verbatim(self) -> None:
        provider = FactProvider()
        document = dict(
            _document("DOC-LARGE", "ISSUER_PRESENTATION", "ISSUER:current.example")
        )
        full_text = (
            "Current Corp reported record operating cash flow in 2026Q1. "
            + ("Full source evidence remains verbatim. " * 4_500)
        )
        document["content_text"] = full_text
        document["content_hash"] = hashlib.sha256(
            full_text.encode("utf-8")
        ).hexdigest()
        current_facts = tuple(
            {
                "fact_id": f"FACT-{index:04d}",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "subject": "Current Corp memory business",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "economic_mechanism": f"prior mechanism {index}",
                "predicate": f"PRIOR_PREDICATE_{index}",
                "value": index,
                "unit": "qualitative",
                "period": "2026Q1",
                "direction": "POSITIVE",
                "current_lifecycle": "CURRENT",
                "confidence": 0.8,
                "structured_evidence_roles": ("FORWARD_GUIDANCE",),
                "allowed_component_ids": ("earnings_visibility",),
                "source_ids": (f"SRC-{index:04d}",),
                "claim_ids": (f"CLAIM-{index:04d}",),
                "quote_ids": (f"QUOTE-{index:04d}",),
                "source_independence_group": f"ISSUER:{index % 7}",
            }
            for index in range(1_000)
        )

        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
            current_facts=current_facts,
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        payload = provider.calls[0]["payload"]
        self.assertEqual(payload["full_documents"][0]["content_text"], full_text)
        self.assertNotIn("transport_chunk", payload["full_documents"][0])
        self.assertEqual(result.provider_calls[0].transport_chunk_ids, ())
        context = payload["current_evidence_facts"]
        self.assertEqual(
            context["schema_version"],
            "e2r_v5_fact_extraction_evidence_context_v1",
        )
        self.assertEqual(context["fact_count"], 1_000)
        self.assertTrue(context["every_fact_accounted_by_hash_and_group_count"])
        accounting = result.audit["prompt_transport_accounting"]
        self.assertTrue(accounting["full_document_content_preserved_verbatim"])
        self.assertLess(accounting["current_fact_projection_chars"], 20_000)
        self.assertGreater(
            accounting["maximum_primary_payload_chars"],
            len(full_text),
        )

    def test_long_document_chunks_cover_full_text_and_aggregate_one_disposition(self) -> None:
        provider = ChunkAwareFactProvider()
        document = dict(
            _document("DOC-CHUNKED", "ISSUER_PRESENTATION", "ISSUER:current.example")
        )
        full_text = (
            "Current Corp reported record operating cash flow in 2026Q1.\n"
            + ("complete source body line\n" * 18_000)
        )
        document["content_text"] = full_text
        document["content_hash"] = hashlib.sha256(
            full_text.encode("utf-8")
        ).hexdigest()

        result = ResearcherEvidenceFactExtractor(
            provider=provider,
            max_document_chars_per_call=100_000,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertGreater(len(provider.calls), 1)
        self.assertTrue(
            all(
                len(call["payload"]["full_documents"][0]["content_text"])
                <= 100_000
                for call in provider.calls
            )
        )
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(len(result.document_dispositions), 1)
        disposition = result.document_dispositions[0]
        self.assertTrue(disposition["all_transport_chunks_complete"])
        self.assertEqual(
            disposition["completed_transport_chunk_count"],
            disposition["transport_chunk_count"],
        )
        accounting = result.audit["prompt_transport_accounting"]
        self.assertGreater(accounting["maximum_full_document_chars"], 100_000)
        self.assertLessEqual(accounting["maximum_transport_chunk_chars"], 100_000)
        self.assertTrue(accounting["transport_character_bound_enforced"])
        self.assertTrue(
            all(call.transport_chunk_ids for call in result.provider_calls)
        )
        self.assertTrue(
            all(
                call["payload"]["full_documents"][0]["transport_chunk"][
                    "all_chunks_required_before_document_completion"
                ]
                for call in provider.calls
            )
        )

    def test_one_chunk_timeout_keeps_parent_unaccounted_but_later_chunks_continue(self) -> None:
        provider = ChunkAwareFactProvider(fail_chunk_index=1)
        document = dict(
            _document("DOC-CHUNK-PENDING", "ISSUER_PRESENTATION", "ISSUER:current.example")
        )
        full_text = (
            "Current Corp reported record operating cash flow in 2026Q1.\n"
            + ("complete source body line\n" * 12_000)
        )
        document["content_text"] = full_text
        document["content_hash"] = hashlib.sha256(
            full_text.encode("utf-8")
        ).hexdigest()

        result = ResearcherEvidenceFactExtractor(
            provider=provider,
            max_document_chars_per_call=100_000,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
        )

        observed_indices = [
            int(
                (
                    call["payload"]["full_documents"][0].get(
                        "transport_chunk"
                    )
                    or {}
                ).get("chunk_index")
                or 0
            )
            for call in provider.calls
        ]
        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
        self.assertIn(2, observed_indices)
        self.assertEqual(result.material_claims, ())
        self.assertEqual(result.document_dispositions, ())
        self.assertEqual(
            result.audit["critical_counts"]["unaccounted_document_count"],
            1,
        )
        self.assertFalse(result.audit["provider_circuit_breaker_open"])

    def test_checkpoint_resumes_only_documents_with_parent_disposition(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rows_by_name = {
                "material_fact_claims.jsonl": [
                    {"claim_id": "CLAIM-PARTIAL", "document_id": "DOC-PARTIAL"},
                    {"claim_id": "CLAIM-COMPLETE", "document_id": "DOC-COMPLETE"},
                ],
                "fact_document_dispositions.jsonl": [
                    {"document_id": "DOC-COMPLETE", "status": "FACTS_EXTRACTED"},
                ],
                "fact_extraction_provider_calls.jsonl": [
                    {
                        "status": "COMPLETE",
                        "document_ids": ["DOC-PARTIAL"],
                        "transport_chunk_ids": ["CHUNK-0"],
                    },
                    {
                        "status": "PENDING",
                        "document_ids": ["DOC-PARTIAL"],
                        "transport_chunk_ids": ["CHUNK-1"],
                    },
                    {
                        "status": "COMPLETE",
                        "document_ids": ["DOC-COMPLETE"],
                    },
                ],
                "fact_extraction_rejections.jsonl": [
                    {"document_id": "DOC-PARTIAL", "reason": "RETRY"},
                    {"document_id": "DOC-COMPLETE", "reason": "TERMINAL"},
                ],
            }
            for filename, rows in rows_by_name.items():
                (root / filename).write_text(
                    "".join(
                        json.dumps(row, ensure_ascii=False) + "\n"
                        for row in rows
                    ),
                    encoding="utf-8",
                )
            checkpoint = _load_fact_checkpoint(
                root,
                source_graph=SimpleNamespace(
                    evidence_documents=(
                        {"document_id": "DOC-PARTIAL"},
                        {"document_id": "DOC-COMPLETE"},
                    )
                ),
            )

        self.assertEqual(
            [row["document_id"] for row in checkpoint["prior_material_claims"]],
            ["DOC-COMPLETE"],
        )
        self.assertEqual(
            [row["document_id"] for row in checkpoint["prior_document_dispositions"]],
            ["DOC-COMPLETE"],
        )
        self.assertEqual(len(checkpoint["prior_provider_calls"]), 1)
        self.assertEqual(
            [row["document_id"] for row in checkpoint["prior_rejections"]],
            ["DOC-COMPLETE"],
        )

    def test_large_gap_ledgers_are_projected_without_losing_semantic_questions(self) -> None:
        provider = FactProvider()
        failures = [
            {
                "failure_stage": "FULL_DOCUMENT_FETCH",
                "failure_reason": f"FETCH_FAILURE_{index % 4}",
                "objective_id": f"OBJECTIVE-{index % 7}",
                "query_id": f"QUERY-{index % 31}",
                "candidate_id": f"CANDIDATE-{index}",
                "url": f"https://example.com/failure/{index}",
                "retryable": index % 2 == 0,
            }
            for index in range(3_000)
        ]
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(
                _document("DOC-GAP", "ISSUER_PRESENTATION", "ISSUER"),
            ),
            open_objectives=(),
            score_gap_context={
                "source_graph_pending_reasons": [
                    f"FULL_FETCH_TRANSPORT_BUDGET_CHECKPOINT:{index}"
                    for index in range(2_000)
                ],
                "prior_fact_extraction_feedback": [
                    f"FACT_EXTRACTION_RETRY_CONTEXT:{index}"
                    for index in range(1_000)
                ],
                "prior_supervisor_gap": {
                    "missing_material_facts": ["공식 연간 가이던스"],
                    "unresolved_material_questions": ["현금 전환 귀속은 무엇인가?"],
                    "failure_assessments": failures,
                    "parser_or_extractor_failures": [
                        f"PARSER-{index}" for index in range(1_000)
                    ],
                },
            },
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        context = provider.calls[0]["payload"]["score_gap_context"]
        self.assertEqual(
            context["prior_supervisor_gap"]["missing_material_facts"],
            ["공식 연간 가이던스"],
        )
        self.assertEqual(
            context["prior_supervisor_gap"]["unresolved_material_questions"],
            ["현금 전환 귀속은 무엇인가?"],
        )
        self.assertEqual(
            context["prior_supervisor_gap"]["failure_assessment_projection"][
                "failure_count"
            ],
            3_000,
        )
        self.assertEqual(
            context["source_graph_pending_reasons"]["reason_count"],
            2_000,
        )
        accounting = result.audit["prompt_transport_accounting"]
        self.assertLess(accounting["score_gap_projection_chars"], 100_000)
        self.assertLess(accounting["maximum_primary_payload_chars"], 1_000_000)
        self.assertFalse(
            context["fact_extraction_score_gap_projection_audit"][
                "prompt_projection_is_research_cap"
            ]
        )

    def test_material_proposal_without_exact_quote_is_pending_not_evidence(self) -> None:
        provider = FactProvider(bad_quote=True)
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
        self.assertEqual(result.material_claims, ())
        self.assertEqual(result.facts, ())
        self.assertIn(
            "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT",
            result.pending_reasons[0],
        )
        self.assertTrue(
            any(
                row.startswith("FACT_EXTRACTION_RETRY_CONTEXT:")
                for row in result.research_gap_feedback
            )
        )
        self.assertEqual(len(provider.calls), 3)
        self.assertEqual(
            result.rejections[0].proposed_exact_quote, "quote not found"
        )
        final_retry = provider.calls[-1]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertEqual(final_retry["rewrite_attempt"], 2)
        self.assertTrue(final_retry["must_not_repeat_rejected_proposals"])
        self.assertEqual(
            final_retry["prohibited_exact_quote_reuse"],
            [{"document_id": "DOC-1", "exact_quote": "quote not found"}],
        )

    def test_invalid_exact_quote_is_reprompted_with_the_rejected_proposal(self) -> None:
        provider = CorrectingQuoteFactProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        retry = provider.calls[-1]["payload"]["fact_extraction_retry_context"]
        self.assertIn(
            "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT", retry["validation_errors"][0]
        )
        self.assertEqual(
            retry["rejected_proposals"][0]["proposed_exact_quote"],
            "quote not found",
        )
        self.assertEqual(retry["rewrite_attempt"], 1)
        self.assertTrue(retry["must_not_repeat_rejected_proposals"])
        self.assertEqual(
            retry["prohibited_exact_quote_reuse"],
            [{"document_id": "DOC-1", "exact_quote": "quote not found"}],
        )
        self.assertEqual(result.rejections, ())
        self.assertEqual(result.provider_calls[0].provider_attempt_count, 2)
        self.assertTrue(result.provider_calls[0].validation_retry_used)
        self.assertEqual(result.audit["validation_retry_call_count"], 1)

    def test_literal_quote_wrapper_and_percent_confidence_are_normalized(self) -> None:
        provider = WrappedQuotePercentConfidenceProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 1)
        self.assertEqual(len(result.material_claims), 1)
        claim = result.material_claims[0]
        self.assertEqual(
            claim["exact_quote"],
            "Current Corp reported record operating cash flow in 2026Q1.",
        )
        self.assertEqual(claim["confidence"], 1.0)
        self.assertEqual(claim["scope_confidence"], 0.9)
        self.assertEqual(
            claim["deterministic_field_normalizations"],
            [
                "EXACT_QUOTE_OUTER_WRAPPER_STRIPPED",
                "CONFIDENCE_PERCENT_TO_PROBABILITY",
                "SCOPE_CONFIDENCE_PERCENT_TO_PROBABILITY",
            ],
        )
        self.assertEqual(result.rejections, ())

    def test_fact_pages_continue_without_total_fact_cap(self) -> None:
        provider = PagedFactProvider()
        document = dict(
            _document("DOC-PAGED", "ISSUER_PRESENTATION", "ISSUER")
        )
        text = "\n".join(
            f"Current Corp material fact number {index}."
            for index in range(13)
        )
        document["content_text"] = text
        document["content_hash"] = hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(result.material_claims), 13)
        self.assertEqual(len(result.facts), 13)
        continuation = provider.calls[1]["payload"][
            "fact_extraction_continuation_context"
        ]
        self.assertEqual(continuation["page_number"], 2)
        self.assertEqual(
            len(continuation["previously_accepted_facts"]),
            FACT_EXTRACTION_PAGE_FACT_LIMIT,
        )
        self.assertEqual(
            result.audit["pagination_continuation_call_count"], 1
        )
        self.assertFalse(result.audit["fact_page_limit_is_total_fact_cap"])

    def test_full_page_forces_empty_completion_page_even_if_llm_says_complete(
        self,
    ) -> None:
        provider = BoundaryCompletePagedFactProvider()
        document = dict(
            _document("DOC-PAGED-BOUNDARY", "ISSUER_PRESENTATION", "ISSUER")
        )
        text = "\n".join(
            f"Current Corp material fact number {index}."
            for index in range(FACT_EXTRACTION_PAGE_FACT_LIMIT)
        )
        document["content_text"] = text
        document["content_hash"] = hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(
            len(result.material_claims),
            FACT_EXTRACTION_PAGE_FACT_LIMIT,
        )
        self.assertEqual(result.audit["maximum_pagination_page_count"], 2)

    def test_pagination_rejects_whitespace_only_quote_repetition(self) -> None:
        provider = WhitespaceVariantPagedFactProvider()
        document = dict(
            _document("DOC-PAGED-SPACING", "ISSUER_PRESENTATION", "ISSUER")
        )
        text = "\n".join(
            [
                *(
                    f"Current Corp material fact number {index}."
                    for index in range(FACT_EXTRACTION_PAGE_FACT_LIMIT)
                ),
                "CurrentCorpmaterialfactnumber0.",
            ]
        )
        document["content_text"] = text
        document["content_hash"] = hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(
            len(result.material_claims),
            FACT_EXTRACTION_PAGE_FACT_LIMIT,
        )
        self.assertIn(
            "PREVIOUSLY_ACCEPTED_EXACT_QUOTE_REPEATED",
            {row.reason for row in result.rejections},
        )

    def test_valid_fact_is_preserved_while_invalid_sibling_is_rewritten(self) -> None:
        provider = MixedValidInvalidThenDispositionProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 3)
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(
            result.material_claims[0]["exact_quote"],
            "Current Corp reported record operating cash flow in 2026Q1.",
        )
        first_retry = provider.calls[1]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertEqual(len(first_retry["previously_accepted_facts"]), 1)
        self.assertIn(
            "do not downgrade their document to NO_MATERIAL_FACT",
            first_retry["instruction"],
        )
        second_retry = provider.calls[2]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertIn(
            "ACCEPTED_FACT_DISPOSITION_MISMATCH:DOC-1",
            second_retry["validation_errors"],
        )
        self.assertEqual(len(second_retry["previously_accepted_facts"]), 1)
        self.assertEqual(
            result.document_dispositions[0]["status"],
            "FACTS_EXTRACTED",
        )

    def test_retry_repeating_accepted_quote_is_dropped_without_new_fact(self) -> None:
        provider = RepeatsAcceptedFactOnRetryProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(len(result.facts), 1)
        self.assertEqual(
            [row.reason for row in result.rejections],
            ["PREVIOUSLY_ACCEPTED_EXACT_QUOTE_REPEATED"],
        )
        self.assertEqual(result.pending_reasons, ())
        retry = provider.calls[-1]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertEqual(len(retry["previously_accepted_facts"]), 1)

    def test_quote_failure_cannot_be_relabelled_no_material_on_retry(self) -> None:
        provider = QuoteFailureThenNoMaterialProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
        self.assertEqual(len(provider.calls), 3)
        self.assertIn(
            "NO_MATERIAL_FACT_CANNOT_CLOSE_PRIOR_MATERIAL_"
            "QUOTE_FAILURE:DOC-1",
            result.pending_reasons,
        )
        self.assertEqual(result.material_claims, ())
        self.assertEqual(result.facts, ())
        self.assertEqual(
            [row.reason for row in result.rejections],
            ["EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"],
        )
        final_retry = provider.calls[-1]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertEqual(len(final_retry["prior_material_quote_failures"]), 1)
        self.assertIn("use UNREADABLE", final_retry["instruction"])
        self.assertIn(
            "cannot be closed as NO_MATERIAL_FACT",
            final_retry["instruction"],
        )

    def test_incomplete_flag_retry_distinguishes_batch_from_broader_research(self) -> None:
        provider = CorrectingCompletionFactProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        retry = provider.calls[-1]["payload"]["fact_extraction_retry_context"]
        self.assertEqual(retry["rewrite_attempt"], 1)
        self.assertIn("local to this supplied batch", retry["instruction"])
        self.assertIn("NO_MATERIAL_FACT", retry["instruction"])
        self.assertNotIn(
            "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE", result.pending_reasons
        )
        self.assertTrue(
            any(
                row.startswith("UNRESOLVED_RESEARCH_NOTE:")
                for row in result.research_gap_feedback
            )
        )

    def test_false_completion_flag_is_reconciled_only_after_full_batch_accounting(self) -> None:
        provider = StructurallyCompleteFalseProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 1)
        self.assertEqual(result.audit["completion_flag_reconciled_count"], 1)
        self.assertEqual(
            result.audit["completion_flag_reconciliation_policy"],
            "BATCH_DISPOSITIONS_COMPLETE_AND_NO_UNRESOLVED_DOCUMENT_IDS",
        )
        self.assertNotIn(
            "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE", result.pending_reasons
        )
        self.assertTrue(
            any(
                row.startswith("UNRESOLVED_RESEARCH_NOTE:")
                for row in result.research_gap_feedback
            )
        )

    def test_false_completion_with_unresolved_document_stays_pending(self) -> None:
        provider = StructurallyIncompleteFalseProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
        self.assertEqual(len(provider.calls), 3)
        self.assertEqual(result.audit["completion_flag_reconciled_count"], 0)
        self.assertTrue(
            any(
                row.startswith("UNRESOLVED_DOCUMENT:DOC-1")
                for row in result.pending_reasons
            )
        )
        self.assertIn(
            "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE", result.pending_reasons
        )

    def test_snippet_and_future_document_are_rejected_before_llm(self) -> None:
        provider = FactProvider()
        snippet = dict(_document("DOC-1", "GENERAL_WEB_DISCOVERY", "WEB"))
        snippet["snippet_only"] = True
        with self.assertRaisesRegex(ValueError, "full evidence-eligible"):
            ResearcherEvidenceFactExtractor(provider=provider).extract(
                target_id=TARGET,
                target_name=TARGET_NAME,
                target_aliases=(),
                archetype_id=ARCHETYPE,
                as_of_date=AS_OF_DATE,
                documents=(snippet,),
                open_objectives=(),
            )
        future = dict(_document("DOC-2", "REUTERS", "REUTERS"))
        future["published_at"] = "2026-06-30"
        future["available_at"] = "2026-06-30"
        with self.assertRaisesRegex(ValueError, "future document"):
            ResearcherEvidenceFactExtractor(provider=provider).extract(
                target_id=TARGET,
                target_name=TARGET_NAME,
                target_aliases=(),
                archetype_id=ARCHETYPE,
                as_of_date=AS_OF_DATE,
                documents=(future,),
                open_objectives=(),
            )
        self.assertEqual(provider.calls, [])

    def test_provider_failure_is_pending_without_fact_score_or_stage(self) -> None:
        result = ResearcherEvidenceFactExtractor(
            provider=FactProvider(fail=True)
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )
        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
        self.assertFalse(result.production_score_authority)
        self.assertEqual(result.facts, ())
        self.assertNotIn("score", result.to_dict())
        self.assertNotIn("stage", result.to_dict())

    def test_transport_wide_provider_failure_opens_one_call_circuit_breaker(self) -> None:
        class UnavailableProvider:
            provider_name = "UNAVAILABLE_PROVIDER"

            def __init__(self) -> None:
                self.call_count = 0

            def complete(self, *, pass_name, payload):
                del pass_name, payload
                self.call_count += 1
                raise StructuredProviderUnavailable(
                    "ERROR: You've hit your usage limit. try again later"
                )

        provider = UnavailableProvider()
        result = ResearcherEvidenceFactExtractor(
            provider=provider,
            documents_per_call=1,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=tuple(
                _document(f"DOC-{index}", "ISSUER_PRESENTATION", f"ISSUER:{index}")
                for index in range(3)
            ),
            open_objectives=(),
        )

        self.assertEqual(provider.call_count, 1)
        self.assertTrue(result.audit["provider_circuit_breaker_open"])
        self.assertEqual(
            result.audit["critical_counts"]["unaccounted_document_count"],
            3,
        )
        self.assertEqual(len(result.provider_calls), 1)
        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")

    def test_single_cli_timeout_leaves_only_that_document_pending(self) -> None:
        class TimeoutThenHealthyProvider:
            provider_name = "TIMEOUT_THEN_HEALTHY_PROVIDER"

            def __init__(self) -> None:
                self.call_count = 0
                self.healthy = FactProvider()

            def complete(self, *, pass_name, payload):
                self.call_count += 1
                if self.call_count == 1:
                    raise StructuredProviderUnavailable("codex_cli_timeout")
                return self.healthy.complete(pass_name=pass_name, payload=payload)

        provider = TimeoutThenHealthyProvider()
        result = ResearcherEvidenceFactExtractor(
            provider=provider,
            documents_per_call=1,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(
                _document("DOC-TIMEOUT", "ISSUER_PRESENTATION", "ISSUER:timeout"),
                _document("DOC-HEALTHY", "REUTERS", "REUTERS:healthy"),
            ),
            open_objectives=(),
        )

        self.assertEqual(provider.call_count, 2)
        self.assertFalse(result.audit["provider_circuit_breaker_open"])
        self.assertEqual(
            result.audit["critical_counts"]["unaccounted_document_count"],
            1,
        )
        self.assertEqual(
            [row.status for row in result.provider_calls],
            ["PENDING", "COMPLETE"],
        )
        self.assertEqual(
            [row["document_id"] for row in result.document_dispositions],
            ["DOC-HEALTHY"],
        )
        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")

    def test_wrong_business_segment_is_terminal_and_cannot_enter_fact_graph(self) -> None:
        result = ResearcherEvidenceFactExtractor(
            provider=FactProvider(wrong_scope=True)
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )
        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(result.facts, ())
        self.assertEqual(result.pending_reasons, ())
        self.assertIn("MECHANISM_SCOPE_REJECTED", result.rejections[0].reason)
        self.assertEqual(result.audit["wrong_mechanism_terminal_count"], 1)

    def test_checkpoint_resume_does_not_repeat_completed_document_calls(self) -> None:
        first_provider = FactProvider()
        extractor = ResearcherEvidenceFactExtractor(
            provider=first_provider,
            documents_per_call=1,
        )
        documents = (_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),)
        first = extractor.extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=documents,
            open_objectives=(),
        )
        second_provider = FactProvider(fail=True)
        resumed = ResearcherEvidenceFactExtractor(
            provider=second_provider,
            documents_per_call=1,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=documents,
            open_objectives=(),
            prior_material_claims=first.material_claims,
            prior_document_dispositions=first.document_dispositions,
            prior_provider_calls=first.provider_calls,
            prior_rejections=first.rejections,
        )
        self.assertEqual(resumed.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(second_provider.calls, [])
        self.assertEqual(resumed.fact_compilation.to_dict(), first.fact_compilation.to_dict())

    def test_fact_extraction_schema_uses_supported_json_subset(self) -> None:
        self.assertNotIn("uniqueItems", _recursive_keys(EVIDENCE_FACT_EXTRACTION_SCHEMA))
        self.assertEqual(
            EVIDENCE_FACT_EXTRACTION_SCHEMA["properties"]["facts"][
                "maxItems"
            ],
            FACT_EXTRACTION_PAGE_FACT_LIMIT,
        )


def _document(
    document_id: str,
    source_family: str,
    independence_group: str,
) -> Mapping[str, Any]:
    text = (
        "Current Corp reported record operating cash flow in 2026Q1. "
        "The full report explains the underlying capacity and customer mechanism."
    )
    return {
        "document_id": document_id,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "canonical_url": f"https://example.com/{document_id}",
        "title": f"Current Corp report {document_id}",
        "source_family": source_family,
        "published_at": "2026-04-30",
        "available_at": "2026-04-30",
        "content_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "content_text": text,
        "source_independence_group": independence_group,
        "objective_ids": ["OBJECTIVE-1"],
        "full_fetch_performed": True,
        "snippet_only": False,
        "snippet_used_as_document": False,
        "evidence_eligible": True,
    }


def _recursive_keys(value: Any) -> set[str]:
    if isinstance(value, Mapping):
        return set(value) | {
            nested for item in value.values() for nested in _recursive_keys(item)
        }
    if isinstance(value, (list, tuple)):
        return {nested for item in value for nested in _recursive_keys(item)}
    return set()


if __name__ == "__main__":
    unittest.main()
