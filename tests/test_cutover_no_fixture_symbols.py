import unittest

from e2r.production.candidate_event_purity import evaluate_candidate_event_production_eligibility


class CutoverNoFixtureSymbolsTests(unittest.TestCase):
    def test_test_and_sample_symbols_are_rejected(self):
        for symbol in ("000000", "222222", "TEST001", "SAMPLEABC"):
            result = evaluate_candidate_event_production_eligibility(
                {
                    "candidate_event_id": symbol,
                    "symbol": symbol,
                    "company_name": "샘플",
                    "event_date": "2026-06-30",
                    "detected_at": "2026-06-30",
                    "source_family": "DART",
                    "source_id": "https://dart.fss.or.kr/doc",
                },
                mode="production_shadow_live",
                as_of_date="2026-06-30",
            )
            self.assertFalse(result.eligible)
            self.assertTrue(result.fixture_like_symbol)


if __name__ == "__main__":
    unittest.main()
