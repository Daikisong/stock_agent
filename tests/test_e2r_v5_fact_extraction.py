from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    EVIDENCE_FACT_EXTRACTION_SCHEMA,
    ResearcherEvidenceFactExtractor,
    production_material_fact_rows,
    write_researcher_fact_extraction_result,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
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
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(
            result.rejections[0].proposed_exact_quote, "quote not found"
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
        self.assertEqual(result.rejections, ())
        self.assertEqual(result.provider_calls[0].provider_attempt_count, 2)
        self.assertTrue(result.provider_calls[0].validation_retry_used)
        self.assertEqual(result.audit["validation_retry_call_count"], 1)

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
