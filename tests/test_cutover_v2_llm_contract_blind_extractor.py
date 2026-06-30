import unittest

from e2r.production.claim_extraction import ExtractionInput, LLMContractBlindRawAssertionExtractor, RuleFallbackExtractorProvider


class CutoverV2LLMContractBlindExtractorTests(unittest.TestCase):
    def test_extractor_does_not_accept_score_gap_context(self):
        extractor = LLMContractBlindRawAssertionExtractor(provider=RuleFallbackExtractorProvider())
        with self.assertRaises(ValueError):
            extractor.extract(
                ExtractionInput(
                    target_entity_id="TICKER:005930",
                    target_aliases=("삼성전자", "005930"),
                    as_of_date="2026-06-30",
                    document_id="DOC",
                    anchor_id="ANCH",
                    source_text="삼성전자는 공급계약을 공시했다.",
                    extra_context={"primitive_gap": "contract_quality"},
                )
            )


if __name__ == "__main__":
    unittest.main()
