import unittest

from e2r.production.claim_extraction import ContractBlindRawAssertionExtractor, ExtractionInput


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


if __name__ == "__main__":
    unittest.main()
