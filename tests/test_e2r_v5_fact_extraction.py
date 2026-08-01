from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    CollaborationCodexResearcherProvider,
    EVIDENCE_FACT_EXTRACTION_SCHEMA,
    EvidenceFactCompiler,
    ResearcherEvidenceFactExtractor,
    import_collaboration_response,
    production_material_fact_rows,
    write_researcher_fact_extraction_result,
)
from e2r.research_brain.researcher_mode.component_researcher import (
    FACT_EXTRACTION_PAGE_FACT_LIMIT,
    _pass_instruction,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    _load_fact_checkpoint,
    write_production_lane,
)
from e2r.research_brain.researcher_mode.evidence_fact_extractor import (
    FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,
    NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED,
    PUNCTUATION_ONLY_VALUE_NORMALIZATION,
    STRUCTURED_JSON_STRING_VALUE_TYPE_RESTORED,
    TRANSPORT_FRAGMENT_VALUE_NORMALIZATION,
    normalize_punctuation_only_fact_value,
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


class CorruptedValueFactProvider(FactProvider):
    def __init__(
        self,
        corrupted_value: Any,
        *,
        unit: str | None = None,
    ) -> None:
        super().__init__()
        self.corrupted_value = corrupted_value
        self.unit = unit

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        response["facts"] = [dict(row) for row in response["facts"]]
        for fact in response["facts"]:
            fact["value"] = self.corrupted_value
            if self.unit is not None:
                fact["unit"] = self.unit
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


class ObjectiveLocalFactProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        response["facts"] = [dict(row) for row in response["facts"]]
        objective_ids_by_document = {
            str(row["document_id"]): list(row["objective_ids"])
            for row in payload["fact_extraction_scope_contract"][
                "document_objective_ids"
            ]
        }
        for fact in response["facts"]:
            fact["objective_ids"] = objective_ids_by_document[
                str(fact["document_id"])
            ]
            fact["objective_relation"] = "ADVANCE"
        return response


class CoverageAuditOmissionProvider(ObjectiveLocalFactProvider):
    def __init__(
        self,
        *,
        omitted_quote: str,
        omitted_predicate_family: str,
        omitted_normalized_object: str,
        direction: str,
    ) -> None:
        super().__init__()
        self.omitted_quote = omitted_quote
        self.omitted_predicate_family = omitted_predicate_family
        self.omitted_normalized_object = omitted_normalized_object
        self.direction = direction

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        if "fact_extraction_coverage_audit_context" not in payload:
            return response
        response["facts"] = [dict(response["facts"][0])]
        response["facts"][0].update(
            {
                "question_family_id": "independent_coverage_review",
                "subject_id": "target_information_quality",
                "subject": "Current Corp source-backed information",
                "predicate": self.omitted_predicate_family,
                "predicate_family": self.omitted_predicate_family,
                "normalized_object": self.omitted_normalized_object,
                "value": self.omitted_normalized_object,
                "direction": self.direction,
                "exact_quote": self.omitted_quote,
                "materiality_rationale": (
                    "The omitted span directly changes objective confidence."
                ),
            }
        )
        return response


class SameQuoteDistinctSemanticCoverageProvider(
    ObjectiveLocalFactProvider
):
    shared_quote = (
        "In this reporting section, there is no material long-term "
        "supply contract requiring separate disclosure."
    )

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        response["facts"] = [dict(response["facts"][0])]
        fact = response["facts"][0]
        fact.update(
            {
                "question_family_id": "contract_existence",
                "predicate": "reported no material contract",
                "predicate_family": "material_contract_existence",
                "normalized_object": "no_material_contract_in_section",
                "value": "none_reported",
                "direction": "COUNTER",
                "exact_quote": self.shared_quote,
            }
        )
        if payload.get("fact_extraction_coverage_audit_context"):
            fact.update(
                {
                    "question_family_id": (
                        "contract_term_information_coverage"
                    ),
                    "predicate": (
                        "bounded section provides no separately "
                        "disclosed material contract terms"
                    ),
                    "predicate_family": (
                        "contract_term_disclosure_limitation"
                    ),
                    "normalized_object": (
                        "section_scoped_contract_term_limitation"
                    ),
                }
            )
        return response


class ObjectiveLocalPagedFactProvider(PagedFactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        response["facts"] = [dict(row) for row in response["facts"]]
        objective_ids_by_document = {
            str(row["document_id"]): list(row["objective_ids"])
            for row in payload["fact_extraction_scope_contract"][
                "document_objective_ids"
            ]
        }
        for fact in response["facts"]:
            fact["objective_ids"] = objective_ids_by_document[
                str(fact["document_id"])
            ]
            fact["objective_relation"] = "ADVANCE"
        if payload.get("fact_extraction_coverage_audit_context"):
            response["facts"] = []
            response["document_dispositions"] = [
                {
                    "document_id": row["document_id"],
                    "status": "FACTS_EXTRACTED",
                    "rationale": (
                        "독립 coverage 재검토에서 누락된 추가 사실이 없다."
                    ),
                }
                for row in payload["full_documents"]
            ]
            response["unresolved_document_ids"] = []
            response["extraction_complete"] = True
        return response


class ObjectiveIrrelevantDocumentProvider(FactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        response["facts"] = []
        response["document_dispositions"] = [
            {
                "document_id": row["document_id"],
                "status": "NO_MATERIAL_FACT",
                "rationale": (
                    "현재 공백에 직접 영향을 주는 사실이 없는 일반 배경이다."
                ),
            }
            for row in payload["full_documents"]
        ]
        response["unresolved_document_ids"] = []
        response["extraction_complete"] = True
        return response


class WrongObjectiveThenCorrectProvider(ObjectiveLocalFactProvider):
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        response["facts"] = [dict(row) for row in response["facts"]]
        if "fact_extraction_retry_context" not in payload:
            for fact in response["facts"]:
                fact["objective_ids"] = ["OBJECTIVE-OUTSIDE-DOCUMENT"]
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


class WrongFinalDispositionThenCorrectProvider(
    BoundaryCompletePagedFactProvider
):
    def __init__(self) -> None:
        super().__init__()
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(
            super().complete(pass_name=pass_name, payload=payload)
        )
        document_id = payload["full_documents"][0]["document_id"]
        if payload.get("fact_extraction_continuation_context"):
            response["facts"] = []
            response["document_dispositions"] = [
                {
                    "document_id": document_id,
                    "status": "NO_MATERIAL_FACT",
                    "rationale": "이전 사실을 잊은 잘못된 최종 처분이다.",
                }
            ]
        elif payload.get("fact_extraction_retry_context"):
            response["facts"] = []
            response["document_dispositions"] = [
                {
                    "document_id": document_id,
                    "status": "FACTS_EXTRACTED",
                    "rationale": "이전에 검증된 사실을 보존한 올바른 처분이다.",
                }
            ]
            response["unresolved_document_ids"] = []
            response["extraction_complete"] = True
        return response


class NonCanonicalScopeThenCorrectProvider(FactProvider):
    def __init__(self) -> None:
        super().__init__()
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        if not payload.get("fact_extraction_retry_context"):
            response["facts"] = [dict(row) for row in response["facts"]]
            response["facts"][0]["scope_business_segment"] = "DS 부문 메모리"
            response["facts"][0]["scope_product_family"] = "HBM3E"
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
    def test_llm_instructions_keep_corroboration_and_uncertainty_distinct(
        self,
    ) -> None:
        query_instruction = _pass_instruction(
            "SOURCE_QUERY_GENERATION"
        )
        extraction_instruction = _pass_instruction(
            "EVIDENCE_FACT_EXTRACTION"
        )
        supervisor_instruction = _pass_instruction(
            "RESEARCH_SUPERVISOR_REVIEW"
        )

        self.assertIn(
            "counterparty's official catalog",
            query_instruction,
        )
        self.assertIn(
            "without proving a purchase obligation",
            query_instruction,
        )
        self.assertIn(
            "figures are preliminary",
            extraction_instruction,
        )
        self.assertIn(
            "official counterparty catalog",
            extraction_instruction,
        )
        self.assertIn(
            "bounded disclosure section",
            extraction_instruction,
        )
        self.assertIn(
            "never generalize it into document-wide",
            extraction_instruction,
        )
        self.assertIn(
            "issuer-affiliated repetitions do not establish independent "
            "corroboration",
            supervisor_instruction,
        )

    def test_punctuation_only_semantic_value_normalizer_is_narrow(self) -> None:
        repaired = normalize_punctuation_only_fact_value(
            {
                "value": ",",
                "normalized_object": "record_operating_cash_flow",
            }
        )
        self.assertEqual(repaired["value"], "record_operating_cash_flow")
        self.assertEqual(
            repaired["deterministic_field_normalizations"],
            [PUNCTUATION_ONLY_VALUE_NORMALIZATION],
        )
        for value in (42, "42.5", "record_high", "매출 증가"):
            with self.subTest(value=value):
                unchanged = normalize_punctuation_only_fact_value(
                    {
                        "value": value,
                        "normalized_object": "replacement_must_not_apply",
                    }
                )
                self.assertEqual(unchanged["value"], value)
                self.assertNotIn(
                    "deterministic_field_normalizations",
                    unchanged,
                )

    def test_transport_fragment_normalizer_never_rewrites_normal_null_text(
        self,
    ) -> None:
        for fragment in (
            ":null},{",
            ":null}],",
            ": null",
            ":true},{",
            ":false},{",
            ":true}],",
        ):
            with self.subTest(fragment=fragment):
                repaired = normalize_punctuation_only_fact_value(
                    {
                        "value": fragment,
                        "normalized_object": "semantic_value",
                    }
                )
                self.assertEqual(repaired["value"], "semantic_value")
                self.assertEqual(
                    repaired["deterministic_field_normalizations"],
                    [TRANSPORT_FRAGMENT_VALUE_NORMALIZATION],
                )
        for literal in ("null", "true", "false"):
            normal_values = (
                literal,
                f"field value is {literal}",
                f"{literal} 값은 정상적인 본문이다",
            )
            for normal_text in normal_values:
                with self.subTest(literal=literal, normal_text=normal_text):
                    unchanged = normalize_punctuation_only_fact_value(
                        {
                            "value": normal_text,
                            "normalized_object": "replacement_must_not_apply",
                        }
                    )
                    self.assertEqual(unchanged["value"], normal_text)
                    self.assertNotIn(
                        "deterministic_field_normalizations",
                        unchanged,
                    )

    def test_structured_json_string_value_restores_native_type_without_scalar_coercion(
        self,
    ) -> None:
        for source, expected in (
            (
                '{"point": "68.1", "unit": "%", "period": "Q1_2026"}',
                {"point": "68.1", "unit": "%", "period": "Q1_2026"},
            ),
            (
                '[{"label": "매출 증가"}, {"point": 68.1}]',
                [{"label": "매출 증가"}, {"point": 68.1}],
            ),
            (
                '{"point": null, "enabled": true, "disabled": false}',
                {"point": None, "enabled": True, "disabled": False},
            ),
            (
                '{"point":"68.1","unit":"%"}',
                {"point": "68.1", "unit": "%"},
            ),
        ):
            with self.subTest(source=source):
                normalized = normalize_punctuation_only_fact_value(
                    {
                        "value": source,
                        "normalized_object": "structured_value",
                    }
                )
                self.assertEqual(normalized["value"], expected)
                self.assertEqual(
                    normalized["deterministic_field_normalizations"],
                    [STRUCTURED_JSON_STRING_VALUE_TYPE_RESTORED],
                )

        actual_mapping = {"point": "68.1", "unit": "%"}
        for preserved in (
            "null",
            "true",
            "68.1",
            '"ordinary JSON scalar string"',
            "ordinary prose",
            actual_mapping,
        ):
            with self.subTest(preserved=preserved):
                normalized = normalize_punctuation_only_fact_value(
                    {
                        "value": preserved,
                        "normalized_object": "replacement_must_not_apply",
                    }
                )
                self.assertEqual(normalized["value"], preserved)
                self.assertNotIn(
                    "deterministic_field_normalizations",
                    normalized,
                )
        self.assertIs(
            normalize_punctuation_only_fact_value(
                {
                    "value": actual_mapping,
                    "normalized_object": "replacement_must_not_apply",
                }
            )["value"],
            actual_mapping,
        )

    def test_numeric_scalar_string_restoration_is_quantitative_and_narrow(
        self,
    ) -> None:
        for source, unit, expected in (
            ("104.1", "조원", 104.1),
            ("39", "%", 39),
            ("-12.5", "KRW trillion", -12.5),
            ("0", "%", 0),
        ):
            with self.subTest(source=source, unit=unit):
                normalized = normalize_punctuation_only_fact_value(
                    {
                        "value": source,
                        "unit": unit,
                        "normalized_object": "quantitative point",
                    }
                )
                self.assertEqual(normalized["value"], expected)
                self.assertIs(type(normalized["value"]), type(expected))
                self.assertEqual(
                    normalized["deterministic_field_normalizations"],
                    [NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED],
                )

        preserved_values = (
            ("2026", "연도"),
            ("2026", "%"),
            ("2026.02", "%"),
            ("31929129041293", None),
            ("000", "count"),
            ("10-20", "%"),
            ("(39)", "%"),
            ("+39", "%"),
            ("1,000", "KRW"),
            ("1234567890123456", "KRW"),
            ("39", None),
            ("39", "qualitative"),
            ("39", "N/A"),
        )
        for source, unit in preserved_values:
            with self.subTest(source=source, unit=unit):
                normalized = normalize_punctuation_only_fact_value(
                    {
                        "value": source,
                        "unit": unit,
                        "normalized_object": "must remain text",
                    }
                )
                self.assertEqual(normalized["value"], source)
                self.assertNotIn(
                    NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED,
                    normalized.get("deterministic_field_normalizations", ()),
                )

    def test_punctuation_only_provider_value_uses_normalized_object(self) -> None:
        result = ResearcherEvidenceFactExtractor(
            provider=CorruptedValueFactProvider(",")
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
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(
            result.material_claims[0]["value"],
            "record_operating_cash_flow",
        )
        self.assertEqual(
            result.material_claims[0]["deterministic_field_normalizations"],
            [PUNCTUATION_ONLY_VALUE_NORMALIZATION],
        )
        self.assertEqual(len(result.facts), 1)
        self.assertEqual(result.facts[0].value, "record_operating_cash_flow")

    def test_fact_provider_payload_ignores_collaboration_wait_request_id(
        self,
    ) -> None:
        def score_gap_context(request_id: str) -> Mapping[str, Any]:
            supervisor_wait = (
                "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                "COLLABORATION_RESPONSE_PENDING:"
                + request_id
            )
            return {
                "source_graph_pending_reasons": [
                    "QUERY_PROVIDER_ERROR:"
                    "COLLABORATION_RESPONSE_PENDING:"
                    + request_id,
                ],
                "prior_fact_extraction_feedback": [
                    "UNRESOLVED_RESEARCH_NOTE:peer band source가 필요하다.",
                    (
                        "FACT_EXTRACTION_RETRY_CONTEXT:"
                        "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        "COLLABORATION_RESPONSE_PENDING:"
                        + request_id
                    ),
                ],
                "prior_supervisor_gap": {
                    "unresolved_material_questions": [supervisor_wait],
                },
                "prior_research_epoch": {
                    "unresolved_material_questions": [supervisor_wait],
                },
            }

        provider_a = FactProvider()
        provider_b = FactProvider()
        common = {
            "target_id": TARGET,
            "target_name": TARGET_NAME,
            "target_aliases": (),
            "archetype_id": ARCHETYPE,
            "as_of_date": AS_OF_DATE,
            "documents": (
                _document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),
            ),
            "open_objectives": (),
        }
        ResearcherEvidenceFactExtractor(provider=provider_a).extract(
            **common,
            score_gap_context=score_gap_context(
                "COLLABREQ-" + "a" * 64
            ),
        )
        ResearcherEvidenceFactExtractor(provider=provider_b).extract(
            **common,
            score_gap_context=score_gap_context(
                "COLLABREQ-" + "b" * 64
            ),
        )

        self.assertEqual(
            provider_a.calls[0]["payload"],
            provider_b.calls[0]["payload"],
        )

    def test_clean_resume_consumes_pending_collaboration_request_after_prior_fact(
        self,
    ) -> None:
        documents = (
            _document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),
            _document("DOC-2", "REGULATORY_FILING", "REGULATOR"),
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            provider = CollaborationCodexResearcherProvider.default()
            provider.configure_response_cache(
                root / "research_provider_response_cache"
            )
            journal = root / "collaboration_codex_subagent_provider"
            extractor = ResearcherEvidenceFactExtractor(provider=provider)
            common = {
                "target_id": TARGET,
                "target_name": TARGET_NAME,
                "target_aliases": (),
                "archetype_id": ARCHETYPE,
                "as_of_date": AS_OF_DATE,
                "open_objectives": (),
            }

            # Materialize DOC-1's deterministic collaboration request first,
            # then import one valid fact so the real two-document invocation
            # can complete DOC-1 and pause exactly at DOC-2.
            extractor.extract(
                **common,
                documents=(documents[0],),
            )
            doc1_request_path = next(
                (journal / "requests").glob("COLLABREQ-*.json")
            )
            doc1_request = json.loads(
                doc1_request_path.read_text(encoding="utf-8")
            )
            doc1_payload = json.loads(
                doc1_request["prompt"].rsplit("\n", 1)[-1]
            )
            import_collaboration_response(
                journal_root=journal,
                request_id=doc1_request["request_id"],
                response_payload=FactProvider().complete(
                    pass_name="EVIDENCE_FACT_EXTRACTION",
                    payload=doc1_payload,
                ),
                agent_id="fact-doc-1",
                canonical_task_name="/root/fact_doc_1",
                agent_model="codex-collaboration",
            )

            first = extractor.extract(
                **common,
                documents=documents,
            )
            self.assertEqual(first.status, "FACT_EXTRACTION_PENDING")
            self.assertEqual(len(first.facts), 1)
            self.assertEqual(
                first.pending_reasons,
                (FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,),
            )
            requests_before_resume = {
                path.name: json.loads(path.read_text(encoding="utf-8"))
                for path in (journal / "requests").glob(
                    "COLLABREQ-*.json"
                )
            }
            self.assertEqual(
                {
                    json.loads(
                        request["prompt"].rsplit("\n", 1)[-1]
                    )["full_documents"][0]["document_id"]
                    for request in requests_before_resume.values()
                },
                {"DOC-1"},
            )

            checkpoint_root = root / "fact_checkpoint"
            write_researcher_fact_extraction_result(
                first,
                checkpoint_root,
            )
            checkpoint = _load_fact_checkpoint(
                checkpoint_root,
                source_graph=SimpleNamespace(
                    evidence_documents=documents
                ),
            )
            refreshed_score_gap = {
                "prior_structured_source_gap": {
                    "status": "SOURCE_PENDING",
                    "missing_roles_by_component": {
                        "market_mispricing": ["PEER_BAND"]
                    },
                }
            }
            waiting = extractor.extract(
                **common,
                documents=documents,
                current_facts=tuple(
                    fact.to_dict() for fact in first.facts
                ),
                score_gap_context=refreshed_score_gap,
                **checkpoint,
            )
            self.assertEqual(waiting.status, "FACT_EXTRACTION_PENDING")
            requests_with_doc2 = {
                path.name: json.loads(path.read_text(encoding="utf-8"))
                for path in (journal / "requests").glob(
                    "COLLABREQ-*.json"
                )
            }
            doc2_request = next(
                request
                for request in requests_with_doc2.values()
                if json.loads(request["prompt"].rsplit("\n", 1)[-1])[
                    "full_documents"
                ][0]["document_id"]
                == "DOC-2"
            )
            doc2_pending_call = next(
                call
                for call in waiting.provider_calls
                if call.document_ids == ("DOC-2",)
            )
            doc2_payload = json.loads(
                doc2_request["prompt"].rsplit("\n", 1)[-1]
            )
            self.assertEqual(
                doc2_payload["score_gap_context"][
                    "prior_structured_source_gap"
                ]["status"],
                "SOURCE_PENDING",
            )
            import_collaboration_response(
                journal_root=journal,
                request_id=doc2_request["request_id"],
                response_payload=FactProvider().complete(
                    pass_name="EVIDENCE_FACT_EXTRACTION",
                    payload=doc2_payload,
                ),
                agent_id="fact-doc-2",
                canonical_task_name="/root/fact_doc_2",
                agent_model="codex-collaboration",
            )

            resumed = extractor.extract(
                **common,
                documents=documents,
                current_facts=tuple(
                    fact.to_dict() for fact in first.facts
                ),
                score_gap_context=refreshed_score_gap,
                **checkpoint,
            )

            self.assertEqual(resumed.status, "FACT_EXTRACTION_COMPLETE")
            self.assertEqual(
                set(requests_with_doc2),
                {
                    path.name
                    for path in (journal / "requests").glob(
                        "COLLABREQ-*.json"
                    )
                },
            )
            doc2_completed_call = next(
                call
                for call in resumed.provider_calls
                if call.document_ids == ("DOC-2",)
            )
            self.assertEqual(doc2_completed_call.status, "COMPLETE")
            self.assertEqual(
                doc2_completed_call.prompt_hash,
                doc2_pending_call.prompt_hash,
            )

    def test_transport_fragment_provider_value_uses_normalized_object(self) -> None:
        result = ResearcherEvidenceFactExtractor(
            provider=CorruptedValueFactProvider(":null},{")
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
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(
            result.material_claims[0]["value"],
            "record_operating_cash_flow",
        )
        self.assertEqual(
            result.material_claims[0]["deterministic_field_normalizations"],
            [TRANSPORT_FRAGMENT_VALUE_NORMALIZATION],
        )
        self.assertEqual(len(result.facts), 1)
        self.assertEqual(result.facts[0].value, "record_operating_cash_flow")

    def test_structured_json_string_provider_value_restores_native_type(
        self,
    ) -> None:
        result = ResearcherEvidenceFactExtractor(
            provider=CorruptedValueFactProvider(
                '{"point": "68.1", "unit": "%", "period": "Q1_2026"}'
            )
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-1", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        expected = {"point": "68.1", "unit": "%", "period": "Q1_2026"}
        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(result.material_claims[0]["value"], expected)
        self.assertEqual(
            result.material_claims[0]["deterministic_field_normalizations"],
            [STRUCTURED_JSON_STRING_VALUE_TYPE_RESTORED],
        )
        self.assertEqual(len(result.facts), 1)
        self.assertEqual(result.facts[0].value, expected)

    def test_native_numeric_provider_value_and_zero_remain_numeric(self) -> None:
        for value in (104.1, 39, 0):
            with self.subTest(value=value):
                provider = CorruptedValueFactProvider(value, unit="%")
                result = ResearcherEvidenceFactExtractor(
                    provider=provider
                ).extract(
                    target_id=TARGET,
                    target_name=TARGET_NAME,
                    target_aliases=(),
                    archetype_id=ARCHETYPE,
                    as_of_date=AS_OF_DATE,
                    documents=(
                        _document(
                            "DOC-1",
                            "ISSUER_PRESENTATION",
                            "ISSUER",
                        ),
                    ),
                    open_objectives=(),
                )

                self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
                self.assertEqual(len(result.material_claims), 1)
                self.assertEqual(result.material_claims[0]["value"], value)
                self.assertIs(
                    type(result.material_claims[0]["value"]),
                    type(value),
                )
                self.assertEqual(result.facts[0].value, value)
                self.assertNotIn(
                    NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED,
                    result.material_claims[0].get(
                        "deterministic_field_normalizations",
                        (),
                    ),
                )
                value_instruction = provider.calls[0]["payload"][
                    "normalization_contract"
                ]["value"]
                self.assertIn("JSON number", value_instruction)
                self.assertIn("ranges", value_instruction)
                self.assertIn("identifiers", value_instruction)
                self.assertIn("dates", value_instruction)

    def test_every_full_document_is_processed_and_independent_sources_dedupe_fact(self) -> None:
        provider = FactProvider()
        extractor = ResearcherEvidenceFactExtractor(
            provider=provider,
        )
        common = {
            "target_id": TARGET,
            "target_name": TARGET_NAME,
            "target_aliases": (),
            "archetype_id": ARCHETYPE,
            "as_of_date": AS_OF_DATE,
            "documents": (
                _document("DOC-1", "ISSUER_PRESENTATION", "ISSUER:current.example"),
                _document("DOC-2", "REUTERS", "REUTERS:reuters.example"),
            ),
            "open_objectives": (),
        }
        first = extractor.extract(**common)
        self.assertEqual(
            first.pending_reasons,
            (FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,),
        )
        result = extractor.extract(
            **common,
            current_facts=tuple(fact.to_dict() for fact in first.facts),
            prior_material_claims=first.material_claims,
            prior_document_dispositions=first.document_dispositions,
            prior_provider_calls=first.provider_calls,
            prior_rejections=first.rejections,
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
        self.assertEqual(
            production[0]["discovery_origin"],
            "CANONICAL_SOURCE_TASK",
        )
        self.assertFalse(production[0]["gold_visibility"])
        with tempfile.TemporaryDirectory() as directory:
            paths = write_researcher_fact_extraction_result(result, directory)
            self.assertTrue(all(path.is_file() for path in paths.values()))
            production_root = Path(directory) / "production"
            lane_paths = write_production_lane(
                config=CurrentResearcherModeConfig(
                    as_of_date=AS_OF_DATE,
                    archetype_id=ARCHETYPE,
                    output_root=production_root,
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                    gold_lane_isolated=True,
                    require_researcher_parity=True,
                ),
                target_runs=(
                    SimpleNamespace(
                        status=(
                            "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                        ),
                        target=SimpleNamespace(target_id=TARGET),
                        fact_extraction=result,
                        component_memo_rows=(),
                        production_input_rows=(),
                    ),
                ),
            )
            lane = json.loads(lane_paths["lane"].read_text(encoding="utf-8"))
            written_facts = [
                json.loads(line)
                for line in lane_paths["facts"].read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip()
            ]
            self.assertEqual(lane["lane_role"], "PRODUCTION")
            self.assertTrue(lane["production_research_complete"])
            self.assertFalse(lane["gold_visibility"])
            self.assertEqual(
                {row["discovery_origin"] for row in written_facts},
                {"CANONICAL_SOURCE_TASK"},
            )

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

    def test_final_split_chunk_yields_before_opening_next_parent(self) -> None:
        provider = ChunkAwareFactProvider()
        chunked = dict(
            _document(
                "DOC-CHUNKED",
                "ISSUER_PRESENTATION",
                "ISSUER:current.example",
            )
        )
        full_text = (
            "Current Corp reported record operating cash flow in 2026Q1.\n"
            + ("complete source body line\n" * 9_000)
        )
        chunked["content_text"] = full_text
        chunked["content_hash"] = hashlib.sha256(
            full_text.encode("utf-8")
        ).hexdigest()
        next_parent = _document(
            "DOC-NEXT",
            "REUTERS",
            "REUTERS:reuters.example",
        )
        extractor = ResearcherEvidenceFactExtractor(
            provider=provider,
            max_document_chars_per_call=100_000,
        )
        common = {
            "target_id": TARGET,
            "target_name": TARGET_NAME,
            "target_aliases": (),
            "archetype_id": ARCHETYPE,
            "as_of_date": AS_OF_DATE,
            "documents": (chunked, next_parent),
            "open_objectives": (),
        }

        first = extractor.extract(**common)

        self.assertEqual(
            first.pending_reasons,
            (FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,),
        )
        self.assertEqual(
            {call["payload"]["full_documents"][0]["document_id"]
             for call in provider.calls},
            {"DOC-CHUNKED"},
        )
        self.assertEqual(len(first.document_dispositions), 1)
        self.assertTrue(
            first.document_dispositions[0]["all_transport_chunks_complete"]
        )

        resumed = extractor.extract(
            **common,
            current_facts=tuple(fact.to_dict() for fact in first.facts),
            prior_material_claims=first.material_claims,
            prior_document_dispositions=first.document_dispositions,
            prior_provider_calls=first.provider_calls,
            prior_rejections=first.rejections,
        )

        self.assertEqual(resumed.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(
            provider.calls[-1]["payload"]["full_documents"][0][
                "document_id"
            ],
            "DOC-NEXT",
        )

    def test_later_split_chunk_does_not_close_parent_with_missing_chunk(
        self,
    ) -> None:
        provider = ChunkAwareFactProvider(fail_chunk_index=1)
        chunked = dict(
            _document(
                "DOC-CHUNK-PENDING",
                "ISSUER_PRESENTATION",
                "ISSUER:current.example",
            )
        )
        full_text = (
            "Current Corp reported record operating cash flow in 2026Q1.\n"
            + ("complete source body line\n" * 12_000)
        )
        chunked["content_text"] = full_text
        chunked["content_hash"] = hashlib.sha256(
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
            documents=(
                chunked,
                _document(
                    "DOC-NEXT",
                    "REUTERS",
                    "REUTERS:reuters.example",
                ),
            ),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_PENDING")
        self.assertNotIn(
            FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED,
            result.pending_reasons,
        )
        self.assertEqual(
            provider.calls[-1]["payload"]["full_documents"][0][
                "document_id"
            ],
            "DOC-NEXT",
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

    def test_source_provenance_migration_rematerializes_claim_without_provider(
        self,
    ) -> None:
        document = _document(
            "DOC-CUSTOMER-NEWSROOM",
            "TRUSTED_BUSINESS_MEDIA",
            "TRUSTED_BUSINESS_MEDIA:news.customer.example.com",
        )
        initial = ResearcherEvidenceFactExtractor(
            provider=FactProvider()
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
        )
        self.assertEqual(
            initial.material_claims[0]["source_tier"],
            "TRUSTED_INDEPENDENT",
        )
        migrated_document = {
            **document,
            "source_family": "CUSTOMER_OFFICIAL",
            "source_independence_group": (
                "CUSTOMER_OFFICIAL:news.customer.example.com"
            ),
            "source_family_provenance_reclassified": True,
            "source_family_provenance_semantics_version": (
                "e2r_v5_customer_official_weak_discovery_override_v1"
            ),
        }

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_researcher_fact_extraction_result(initial, root)
            checkpoint = _load_fact_checkpoint(
                root,
                source_graph=SimpleNamespace(
                    evidence_documents=(migrated_document,)
                ),
            )

        self.assertEqual(len(checkpoint["prior_material_claims"]), 1)
        checkpoint_claim = checkpoint["prior_material_claims"][0]
        self.assertEqual(
            checkpoint_claim["claim_id"],
            initial.material_claims[0]["claim_id"],
        )
        self.assertEqual(
            checkpoint_claim["source_family"],
            "CUSTOMER_OFFICIAL",
        )
        self.assertEqual(
            checkpoint_claim["source_tier"],
            "CUSTOMER_OFFICIAL",
        )
        self.assertEqual(
            checkpoint_claim["source_independence_group"],
            "CUSTOMER_OFFICIAL:news.customer.example.com",
        )
        self.assertEqual(len(checkpoint["prior_document_dispositions"]), 1)
        self.assertEqual(len(checkpoint["prior_provider_calls"]), 1)
        resumed_provider = FactProvider(fail=True)
        resumed = ResearcherEvidenceFactExtractor(
            provider=resumed_provider
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(migrated_document,),
            open_objectives=(),
            **checkpoint,
        )

        self.assertEqual(len(resumed_provider.calls), 0)
        self.assertEqual(len(resumed.material_claims), 1)
        rematerialized = resumed.material_claims[0]
        self.assertEqual(
            rematerialized["claim_id"],
            initial.material_claims[0]["claim_id"],
        )
        self.assertEqual(
            resumed.facts[0].fact_id,
            initial.facts[0].fact_id,
        )
        self.assertEqual(
            rematerialized["source_family"],
            "CUSTOMER_OFFICIAL",
        )
        self.assertEqual(
            rematerialized["source_tier"],
            "CUSTOMER_OFFICIAL",
        )
        self.assertEqual(
            rematerialized["source_independence_group"],
            "CUSTOMER_OFFICIAL:news.customer.example.com",
        )
        self.assertEqual(
            resumed.audit[
                "prior_claim_source_provenance_rematerialized_count"
            ],
            1,
        )

    def test_clean_resume_skips_verified_split_chunks_without_promoting_parent(
        self,
    ) -> None:
        document = dict(
            _document(
                "DOC-CHUNK-RESUME",
                "ISSUER_PRESENTATION",
                "ISSUER:current.example",
            )
        )
        full_text = (
            "Current Corp reported record operating cash flow in 2026Q1.\n"
            + ("complete source body line\n" * 12_000)
        )
        document["content_text"] = full_text
        document["content_hash"] = hashlib.sha256(
            full_text.encode("utf-8")
        ).hexdigest()
        first_provider = ChunkAwareFactProvider(fail_chunk_index=1)
        first = ResearcherEvidenceFactExtractor(
            provider=first_provider,
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

        self.assertEqual(first.status, "FACT_EXTRACTION_PENDING")
        self.assertEqual(first.material_claims, ())
        self.assertEqual(first.facts, ())
        self.assertEqual(first.document_dispositions, ())
        completed_first_chunk_ids = {
            chunk_id
            for call in first.provider_calls
            if call.status == "COMPLETE"
            for chunk_id in call.transport_chunk_ids
        }
        self.assertGreaterEqual(len(completed_first_chunk_ids), 2)
        self.assertTrue(
            all(
                call.accepted_claims is not None
                for call in first.provider_calls
                if call.status == "COMPLETE"
            )
        )

        with tempfile.TemporaryDirectory() as directory:
            write_researcher_fact_extraction_result(first, directory)
            checkpoint = _load_fact_checkpoint(
                Path(directory),
                source_graph=SimpleNamespace(
                    evidence_documents=(document,)
                ),
            )

        self.assertEqual(checkpoint["prior_material_claims"], ())
        self.assertEqual(checkpoint["prior_document_dispositions"], ())
        self.assertEqual(
            {
                chunk_id
                for call in checkpoint["prior_provider_calls"]
                for chunk_id in call["transport_chunk_ids"]
            },
            completed_first_chunk_ids,
        )
        resumed_provider = ChunkAwareFactProvider()
        resumed = ResearcherEvidenceFactExtractor(
            provider=resumed_provider,
            max_document_chars_per_call=100_000,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(),
            **checkpoint,
        )

        resumed_indices = [
            int(
                (
                    call["payload"]["full_documents"][0].get(
                        "transport_chunk"
                    )
                    or {}
                ).get("chunk_index")
                or 0
            )
            for call in resumed_provider.calls
        ]
        self.assertEqual(resumed_indices, [1])
        self.assertEqual(resumed.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(resumed.material_claims), 1)
        self.assertEqual(len(resumed.facts), 1)
        self.assertEqual(len(resumed.document_dispositions), 1)
        self.assertTrue(
            resumed.document_dispositions[0]["all_transport_chunks_complete"]
        )
        self.assertEqual(
            resumed.audit["prompt_transport_accounting"][
                "resumed_transport_chunk_count"
            ],
            len(completed_first_chunk_ids),
        )
        self.assertEqual(
            resumed.audit["prompt_transport_accounting"][
                "provider_transport_chunk_count"
            ],
            1,
        )
        checkpoint_json = json.dumps(checkpoint, ensure_ascii=False)
        for tamper_kind in ("EXACT_QUOTE", "DISPOSITION_COUNT"):
            with self.subTest(tamper_kind=tamper_kind):
                tampered_checkpoint = json.loads(checkpoint_json)
                claim_call = next(
                    call
                    for call in tampered_checkpoint[
                        "prior_provider_calls"
                    ]
                    if call.get("accepted_claims")
                )
                tampered_chunk_index = int(
                    claim_call["document_dispositions"][0][
                        "transport_chunk_index"
                    ]
                )
                if tamper_kind == "EXACT_QUOTE":
                    claim_call["accepted_claims"][0][
                        "exact_quote"
                    ] = "tampered quote absent from source"
                else:
                    claim_call["document_dispositions"][0][
                        "accepted_fact_count"
                    ] += 1
                fail_closed_provider = ChunkAwareFactProvider()
                fail_closed = ResearcherEvidenceFactExtractor(
                    provider=fail_closed_provider,
                    max_document_chars_per_call=100_000,
                ).extract(
                    target_id=TARGET,
                    target_name=TARGET_NAME,
                    target_aliases=(),
                    archetype_id=ARCHETYPE,
                    as_of_date=AS_OF_DATE,
                    documents=(document,),
                    open_objectives=(),
                    **tampered_checkpoint,
                )
                fail_closed_indices = {
                    int(
                        (
                            call["payload"]["full_documents"][0].get(
                                "transport_chunk"
                            )
                            or {}
                        ).get("chunk_index")
                        or 0
                    )
                    for call in fail_closed_provider.calls
                }
                self.assertEqual(
                    fail_closed_indices,
                    {1, tampered_chunk_index},
                )
                self.assertEqual(
                    fail_closed.status,
                    "FACT_EXTRACTION_COMPLETE",
                )
                self.assertEqual(len(fail_closed.material_claims), 1)
                self.assertNotEqual(
                    fail_closed.material_claims[0]["exact_quote"],
                    "tampered quote absent from source",
                )

    def test_checkpoint_resume_migrates_punctuation_only_claim_without_duplication(
        self,
    ) -> None:
        checkpoint_cases = (
            (",", ",", "record_operating_cash_flow", None),
            (
                ":null}],",
                ":null}],",
                "record_operating_cash_flow",
                None,
            ),
            (
                '{"point": "68.1", "unit": "%"}',
                '{"point": "68.1", "unit": "%"}',
                {"point": "68.1", "unit": "%"},
                None,
            ),
            (104.1, "104.1", 104.1, "%"),
        )
        for provider_value, persisted_value, expected_value, unit in checkpoint_cases:
            with self.subTest(persisted_value=persisted_value):
                document = _document("DOC-1", "ISSUER_PRESENTATION", "ISSUER")
                initial = ResearcherEvidenceFactExtractor(
                    provider=CorruptedValueFactProvider(
                        provider_value,
                        unit=unit,
                    )
                ).extract(
                    target_id=TARGET,
                    target_name=TARGET_NAME,
                    target_aliases=(),
                    archetype_id=ARCHETYPE,
                    as_of_date=AS_OF_DATE,
                    documents=(document,),
                    open_objectives=(),
                )
                persisted_claim = dict(initial.material_claims[0])
                persisted_claim["value"] = persisted_value
                persisted_claim["deterministic_field_normalizations"] = []

                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    rows_by_name = {
                        "material_fact_claims.jsonl": [persisted_claim],
                        "fact_document_dispositions.jsonl": list(
                            initial.document_dispositions
                        ),
                        "fact_extraction_provider_calls.jsonl": [
                            row.to_dict() for row in initial.provider_calls
                        ],
                        "fact_extraction_rejections.jsonl": [],
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
                            evidence_documents=(document,)
                        ),
                    )

                migrated_claims = checkpoint["prior_material_claims"]
                self.assertEqual(len(migrated_claims), 1)
                self.assertEqual(
                    migrated_claims[0]["claim_id"],
                    initial.material_claims[0]["claim_id"],
                )
                self.assertEqual(
                    migrated_claims[0]["value"],
                    expected_value,
                )
                resumed_compilation = EvidenceFactCompiler().compile(
                    target_id=TARGET,
                    as_of_date=AS_OF_DATE,
                    accepted_claims=migrated_claims,
                )
                self.assertEqual(
                    len(resumed_compilation.facts),
                    len(initial.facts),
                )
                self.assertEqual(
                    resumed_compilation.facts[0].fact_id,
                    initial.facts[0].fact_id,
                )
                self.assertEqual(
                    resumed_compilation.facts[0].value,
                    initial.facts[0].value,
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

    def test_production_long_background_document_stops_at_current_objective(
        self,
    ) -> None:
        provider = ObjectiveIrrelevantDocumentProvider()
        document = dict(
            _document(
                "DOC-OBJECTIVE-IRRELEVANT",
                "GENERAL_WEB_DISCOVERY",
                "GENERAL",
            )
        )
        text = " ".join(
            f"General adjacent technology history paragraph {index}."
            for index in range(1_000)
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
            open_objectives=(
                {
                    "objective_id": "OBJECTIVE-1",
                    "component_id": "information_confidence",
                    "research_objective": (
                        "Verify final customer allocation and repeat orders."
                    ),
                },
            ),
            score_gap_context={
                "prior_supervisor_gap": {
                    "component_findings": [
                        {
                            "component_id": "information_confidence",
                            "memo_sufficient": False,
                            "missing_fact_needs": [
                                "customer final allocation and repeat orders"
                            ],
                        }
                    ]
                }
            },
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(result.material_claims, ())
        self.assertEqual(
            result.document_dispositions[0]["status"],
            "NO_MATERIAL_FACT",
        )
        scope_contract = provider.calls[0]["payload"][
            "fact_extraction_scope_contract"
        ]
        self.assertEqual(
            scope_contract["mode"],
            "PRODUCTION_OBJECTIVE_LOCAL",
        )
        self.assertTrue(
            result.audit["production_objective_local_completion"]
        )
        self.assertIn(
            "fact_extraction_coverage_audit_context",
            provider.calls[1]["payload"],
        )

    def test_production_coverage_audit_recovers_named_event_session_speaker(
        self,
    ) -> None:
        omitted_quote = (
            "At Open Compute Forum 2026, the Scaling Memory session "
            "featured systems engineer Alex Kim discussing Current Corp HBM4."
        )
        provider = CoverageAuditOmissionProvider(
            omitted_quote=omitted_quote,
            omitted_predicate_family="named_event_session_participation",
            omitted_normalized_object=(
                "named_event_session_speaker_technical_participation"
            ),
            direction="POSITIVE",
        )
        document = dict(
            _document(
                "DOC-COVERAGE-EVENT",
                "COUNTERPARTY_OFFICIAL_EVENT",
                "COUNTERPARTY",
            )
        )
        text = f"{document['content_text']} {omitted_quote}"
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
            open_objectives=(
                {
                    "objective_id": "OBJECTIVE-1",
                    "component_id": "information_confidence",
                    "research_objective": (
                        "Verify independent technical participation and attribution."
                    ),
                },
            ),
            score_gap_context={
                "prior_supervisor_gap": {
                    "component_findings": [
                        {
                            "component_id": "information_confidence",
                            "memo_sufficient": False,
                            "missing_fact_needs": [
                                "independent technical attribution"
                            ],
                        }
                    ]
                }
            },
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(result.material_claims), 2)
        self.assertTrue(
            any(
                row["exact_quote"] == omitted_quote
                and row["predicate_family"]
                == "named_event_session_participation"
                for row in result.material_claims
            )
        )
        coverage_context = provider.calls[1]["payload"][
            "fact_extraction_coverage_audit_context"
        ]
        self.assertEqual(
            len(coverage_context["previously_accepted_facts"]),
            1,
        )
        self.assertEqual(result.audit["coverage_audit_call_count"], 1)
        self.assertEqual(result.audit["coverage_audit_new_fact_count"], 1)
        self.assertEqual(
            result.audit["critical_counts"][
                "production_document_without_coverage_audit_count"
            ],
            0,
        )

    def test_production_coverage_audit_recovers_unaudited_change_risk(
        self,
    ) -> None:
        omitted_quote = (
            "The results are unaudited, remain subject to external review "
            "and may change; forward-looking statements involve known and "
            "unknown risks."
        )
        provider = CoverageAuditOmissionProvider(
            omitted_quote=omitted_quote,
            omitted_predicate_family="reported_information_uncertainty",
            omitted_normalized_object=(
                "unaudited_review_change_and_forward_looking_risk"
            ),
            direction="COUNTER",
        )
        document = dict(
            _document(
                "DOC-COVERAGE-UNCERTAINTY",
                "ISSUER_EARNINGS_RELEASE",
                "ISSUER",
            )
        )
        text = f"{document['content_text']} {omitted_quote}"
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
            open_objectives=(
                {
                    "objective_id": "OBJECTIVE-1",
                    "component_id": "information_confidence",
                    "research_objective": (
                        "Assess the certainty of reported results and forecasts."
                    ),
                },
            ),
            score_gap_context={
                "prior_supervisor_gap": {
                    "component_findings": [
                        {
                            "component_id": "information_confidence",
                            "memo_sufficient": False,
                            "missing_fact_needs": [
                                "reported information uncertainty"
                            ],
                        }
                    ]
                }
            },
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(result.material_claims), 2)
        recovered = [
            row
            for row in result.material_claims
            if row["exact_quote"] == omitted_quote
        ]
        self.assertEqual(len(recovered), 1)
        self.assertEqual(recovered[0]["direction"], "COUNTER")
        self.assertEqual(
            recovered[0]["predicate_family"],
            "reported_information_uncertainty",
        )
        instruction = provider.calls[1]["payload"][
            "fact_extraction_coverage_audit_context"
        ]["instruction"]
        self.assertIn("unaudited", instruction)
        self.assertIn("forward-looking", instruction)

    def test_same_quote_with_distinct_semantic_identity_is_not_dropped(
        self,
    ) -> None:
        provider = SameQuoteDistinctSemanticCoverageProvider()
        document = dict(
            _document(
                "DOC-SCOPED-CONTRACT-LIMIT",
                "ISSUER_FILING",
                "ISSUER",
            )
        )
        text = (
            f"{document['content_text']} "
            f"{provider.shared_quote}"
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
            open_objectives=(
                {
                    "objective_id": "OBJECTIVE-1",
                    "component_id": "information_confidence",
                },
            ),
            score_gap_context={
                "prior_supervisor_gap": {
                    "component_findings": [
                        {
                            "component_id": "information_confidence",
                            "memo_sufficient": False,
                            "missing_fact_needs": [
                                "bounded contract disclosure coverage"
                            ],
                        }
                    ]
                }
            },
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        same_quote_claims = [
            row
            for row in result.material_claims
            if row["exact_quote"] == provider.shared_quote
        ]
        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(same_quote_claims), 2)
        self.assertEqual(
            {
                row["predicate_family"]
                for row in same_quote_claims
            },
            {
                "material_contract_existence",
                "contract_term_disclosure_limitation",
            },
        )
        self.assertFalse(
            any(
                row.reason
                == "PREVIOUSLY_ACCEPTED_EXACT_QUOTE_REPEATED"
                for row in result.rejections
            )
        )

    def test_clean_resume_refreshes_legacy_coverage_without_base_reextract(
        self,
    ) -> None:
        document = _document(
            "DOC-LEGACY-COVERAGE",
            "ISSUER_PRESENTATION",
            "ISSUER",
        )
        objective = {
            "objective_id": "OBJECTIVE-1",
            "component_id": "information_confidence",
        }
        first = ResearcherEvidenceFactExtractor(
            provider=ObjectiveLocalFactProvider()
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(objective,),
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )
        legacy_dispositions = []
        for row in first.document_dispositions:
            legacy = dict(row)
            legacy.pop("extraction_semantics_version", None)
            legacy_dispositions.append(legacy)
        legacy_calls = []
        for row in first.provider_calls:
            legacy = dict(row.to_dict())
            legacy.pop("extraction_semantics_version", None)
            legacy_calls.append(legacy)
        legacy_rejections = []
        for row in first.rejections:
            legacy = dict(row.to_dict())
            legacy.pop("extraction_semantics_version", None)
            legacy_rejections.append(legacy)

        resumed_provider = ObjectiveLocalFactProvider()
        resumed = ResearcherEvidenceFactExtractor(
            provider=resumed_provider
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(document,),
            open_objectives=(objective,),
            prior_material_claims=first.material_claims,
            prior_document_dispositions=legacy_dispositions,
            prior_provider_calls=legacy_calls,
            prior_rejections=legacy_rejections,
            score_gap_context={
                "prior_supervisor_gap": {
                    "component_findings": [
                        {
                            "component_id": "information_confidence",
                            "memo_sufficient": False,
                            "missing_fact_needs": [
                                "independent coverage review"
                            ],
                        }
                    ]
                }
            },
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(resumed.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(resumed_provider.calls), 1)
        self.assertEqual(len(resumed.material_claims), 1)
        self.assertFalse(
            resumed.audit["stale_semantics_checkpoint_reextracted"]
        )
        self.assertTrue(
            resumed.audit[
                "stale_semantics_checkpoint_coverage_refreshed"
            ]
        )
        self.assertEqual(
            resumed.audit["stale_semantics_disposition_count"],
            1,
        )
        self.assertEqual(
            resumed.audit["base_reextraction_document_count"],
            0,
        )
        self.assertEqual(
            resumed.audit["critical_counts"][
                "production_document_without_coverage_audit_count"
            ],
            0,
        )

    def test_gap_lineage_audits_only_relevant_completed_document(
        self,
    ) -> None:
        relevant = dict(
            _document(
                "DOC-GAP-RELEVANT",
                "ISSUER_PRESENTATION",
                "ISSUER",
            )
        )
        unrelated = dict(
            _document(
                "DOC-GAP-UNRELATED",
                "ISSUER_PRESENTATION",
                "ISSUER",
            )
        )
        unrelated["objective_ids"] = ["OBJECTIVE-2"]
        objectives = (
            {
                "objective_id": "OBJECTIVE-1",
                "component_id": "information_confidence",
            },
            {
                "objective_id": "OBJECTIVE-2",
                "component_id": "capital_allocation",
            },
        )
        first = ResearcherEvidenceFactExtractor(
            provider=ObjectiveLocalFactProvider(),
            documents_per_call=2,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(relevant, unrelated),
            open_objectives=objectives,
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )
        first_claim_ids = {
            str(row["claim_id"]) for row in first.material_claims
        }

        resumed_provider = ObjectiveLocalFactProvider()
        resumed = ResearcherEvidenceFactExtractor(
            provider=resumed_provider,
            documents_per_call=2,
        ).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(relevant, unrelated),
            open_objectives=objectives,
            prior_material_claims=first.material_claims,
            prior_document_dispositions=first.document_dispositions,
            prior_provider_calls=first.provider_calls,
            prior_rejections=first.rejections,
            score_gap_context={
                "prior_supervisor_gap": {
                    "component_findings": [
                        {
                            "component_id": "information_confidence",
                            "memo_sufficient": False,
                            "missing_fact_needs": [
                                "independent attribution coverage"
                            ],
                        },
                        {
                            "component_id": "capital_allocation",
                            "memo_sufficient": True,
                            "missing_fact_needs": [],
                        },
                    ]
                }
            },
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(resumed.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(resumed_provider.calls), 1)
        self.assertEqual(
            [
                row["document_id"]
                for row in resumed_provider.calls[0]["payload"][
                    "full_documents"
                ]
            ],
            ["DOC-GAP-RELEVANT"],
        )
        self.assertIn(
            "fact_extraction_coverage_audit_context",
            resumed_provider.calls[0]["payload"],
        )
        self.assertEqual(
            {
                str(row["claim_id"])
                for row in resumed.material_claims
            },
            first_claim_ids,
        )
        self.assertEqual(
            resumed.audit["coverage_refresh_prior_document_count"],
            1,
        )
        self.assertEqual(
            resumed.audit["base_reextraction_document_count"],
            0,
        )

    def test_production_objective_linked_fact_pages_remain_lossless(
        self,
    ) -> None:
        provider = ObjectiveLocalPagedFactProvider()
        document = dict(
            _document(
                "DOC-OBJECTIVE-PAGED",
                "ISSUER_PRESENTATION",
                "ISSUER",
            )
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
            open_objectives=(
                {
                    "objective_id": "OBJECTIVE-1",
                    "component_id": "eps_fcf_explosion",
                },
            ),
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(result.material_claims), 13)
        self.assertEqual(len(provider.calls), 2)
        self.assertTrue(
            all(
                row["objective_ids"] == ["OBJECTIVE-1"]
                and row["objective_relation"] == "ADVANCE"
                for row in result.material_claims
            )
        )
        continuation = provider.calls[1]["payload"][
            "fact_extraction_continuation_context"
        ]
        self.assertTrue(
            all(
                row["objective_ids"] == ["OBJECTIVE-1"]
                for row in continuation["previously_accepted_facts"]
            )
        )

    def test_production_rejects_fact_outside_document_objective_lineage(
        self,
    ) -> None:
        provider = WrongObjectiveThenCorrectProvider()
        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(
                _document(
                    "DOC-OBJECTIVE-RETRY",
                    "ISSUER_PRESENTATION",
                    "ISSUER",
                ),
            ),
            open_objectives=(
                {
                    "objective_id": "OBJECTIVE-1",
                    "component_id": "eps_fcf_explosion",
                },
            ),
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(
            result.material_claims[0]["objective_ids"],
            ["OBJECTIVE-1"],
        )
        retry_context = provider.calls[1]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertTrue(
            any(
                "OBJECTIVE_ID_OUTSIDE_DOCUMENT_LINEAGE" in reason
                for reason in retry_context["validation_errors"]
            )
        )

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

    def test_invalid_final_disposition_is_evicted_before_retry(self) -> None:
        provider = WrongFinalDispositionThenCorrectProvider()
        document = dict(
            _document("DOC-PAGED-EVICT", "ISSUER_PRESENTATION", "ISSUER")
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
        self.assertEqual(
            len(result.material_claims),
            FACT_EXTRACTION_PAGE_FACT_LIMIT,
        )
        self.assertEqual(len(provider.invalidations), 1)
        self.assertIn(
            "ACCEPTED_FACT_DISPOSITION_MISMATCH",
            provider.invalidations[0],
        )
        self.assertEqual(len(provider.calls), 3)

    def test_noncanonical_scope_tokens_are_returned_to_llm_for_rewrite(self) -> None:
        provider = NonCanonicalScopeThenCorrectProvider()

        result = ResearcherEvidenceFactExtractor(provider=provider).extract(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            documents=(_document("DOC-SCOPE-REWRITE", "ISSUER_PRESENTATION", "ISSUER"),),
            open_objectives=(),
        )

        self.assertEqual(result.status, "FACT_EXTRACTION_COMPLETE")
        self.assertEqual(len(result.material_claims), 1)
        self.assertEqual(
            result.material_claims[0]["scope_business_segment"],
            "MEMORY",
        )
        self.assertEqual(result.material_claims[0]["scope_product_family"], "HBM")
        self.assertEqual(len(provider.calls), 2)
        retry_context = provider.calls[1]["payload"][
            "fact_extraction_retry_context"
        ]
        self.assertTrue(
            retry_context["must_not_repeat_invalid_scope_encoding"]
        )
        self.assertEqual(len(retry_context["scope_rejected_proposals"]), 1)
        rejected_scope = retry_context["scope_rejected_proposals"][0]
        self.assertIn("MECHANISM_SCOPE_REJECTED", rejected_scope["reason"])
        self.assertEqual(
            rejected_scope["scope_business_segment"],
            "DS 부문 메모리",
        )
        self.assertEqual(rejected_scope["scope_product_family"], "HBM3E")
        self.assertEqual(len(provider.invalidations), 1)

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
        self.assertIsNone(first.provider_calls[0].accepted_claims)
        self.assertNotIn(
            "accepted_claims",
            first.provider_calls[0].to_dict(),
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
        value_schema = EVIDENCE_FACT_EXTRACTION_SCHEMA["properties"]["facts"][
            "items"
        ]["properties"]["value"]
        self.assertEqual(
            value_schema,
            {
                "anyOf": [
                    {"type": "string", "minLength": 1},
                    {"type": "number"},
                ]
            },
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
