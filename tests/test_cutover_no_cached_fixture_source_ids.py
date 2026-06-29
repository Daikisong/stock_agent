import unittest

from e2r.production.candidate_event_purity import evaluate_candidate_event_production_eligibility


class CutoverNoCachedFixtureSourceIdsTests(unittest.TestCase):
    def test_cached_source_id_fails_production_purity(self):
        result = evaluate_candidate_event_production_eligibility(
            {
                "candidate_event_id": "cached",
                "symbol": "005930",
                "company_name": "삼성전자",
                "event_date": "2026-06-30",
                "detected_at": "2026-06-30",
                "source_family": "CompanyGuide",
                "source_id": "data/cache/company_guide/2026-06-30/005930_recent_reports.json",
            },
            mode="production_shadow_live",
            as_of_date="2026-06-30",
        )
        self.assertFalse(result.eligible)
        self.assertTrue(result.source_id_cached_or_fixture)


if __name__ == "__main__":
    unittest.main()
