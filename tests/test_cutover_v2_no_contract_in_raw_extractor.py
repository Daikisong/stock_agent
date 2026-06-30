import unittest

from e2r.production.claim_extraction.extraction_validator import count_forbidden_extractor_output_keys


class CutoverV2NoContractInRawExtractorTests(unittest.TestCase):
    def test_forbidden_output_keys_are_detected(self):
        payload = {"raw_assertions": [{"subject": "A", "primitive_id": "contract_quality", "score": 10}]}
        self.assertEqual(count_forbidden_extractor_output_keys(payload), 2)


if __name__ == "__main__":
    unittest.main()
