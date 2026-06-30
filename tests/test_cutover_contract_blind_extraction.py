import unittest
from datetime import date

from e2r.production.claim_extraction import (
    ContractBlindRawAssertionExtractor,
    ExtractionInput,
    adjudicate_entity_temporal_scope,
    map_claim_to_primitive,
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


if __name__ == "__main__":
    unittest.main()
