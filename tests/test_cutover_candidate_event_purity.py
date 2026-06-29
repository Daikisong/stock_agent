import unittest

from e2r.production.candidate_event_purity import (
    ProductionMode,
    build_candidate_purity_report,
    evaluate_candidate_event_production_eligibility,
    load_instrument_registry,
)


class CutoverCandidateEventPurityTests(unittest.TestCase):
    def test_fixture_like_symbol_is_not_production_eligible(self):
        event = {
            "candidate_event_id": "fixture",
            "symbol": "111111",
            "company_name": "테스트기업",
            "event_date": "2026-06-30",
            "detected_at": "2026-06-30",
            "source_family": "DART",
            "source_id": "data/raw/korea_cheap_scan/opendart/disclosures/fixture.csv",
        }
        result = evaluate_candidate_event_production_eligibility(
            event,
            mode=ProductionMode.PRODUCTION_SHADOW_LIVE,
            registry=load_instrument_registry("."),
            as_of_date="2026-06-30",
        )
        self.assertFalse(result.eligible)
        self.assertIn("fixture_like_symbol", result.reasons)
        self.assertIn("cached_or_fixture_path_forbidden_in_production", result.reasons)

    def test_report_separates_fixture_from_production_count(self):
        report = build_candidate_purity_report(
            [
                {
                    "candidate_event_id": "fixture",
                    "symbol": "111111",
                    "company_name": "테스트기업",
                    "event_date": "2026-06-30",
                    "detected_at": "2026-06-30",
                    "source_family": "DART",
                    "source_id": "fixtures/historical/disclosures.csv",
                },
                {
                    "candidate_event_id": "real",
                    "symbol": "005930",
                    "company_name": "삼성전자",
                    "event_date": "2026-06-30",
                    "detected_at": "2026-06-30",
                    "source_family": "DART",
                    "source_id": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=1",
                },
            ],
            mode=ProductionMode.PRODUCTION_SHADOW_LIVE,
            as_of_date="2026-06-30",
        )
        self.assertEqual(report["summary"]["fixture_candidate_event_count"], 1)
        self.assertEqual(report["summary"]["production_candidate_event_count"], 1)

    def test_sector_coverage_counts_active_large_sectors(self):
        registry = load_instrument_registry(".")
        events = []
        for index, sector in enumerate(
            [
                "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "L4_MATERIALS_SPREAD_RESOURCE",
                "L5_CONSUMER_BRAND_DISTRIBUTION",
                "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                "L8_PLATFORM_CONTENT_SW_SECURITY",
            ],
            start=1,
        ):
            events.append(
                {
                    "candidate_event_id": f"sector-{index}",
                    "symbol": "005930",
                    "company_name": "삼성전자",
                    "event_date": "2026-06-30",
                    "detected_at": "2026-06-30",
                    "source_family": "DART",
                    "source_id": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={index}",
                    "large_sector_id": sector,
                    "sector_classification_source": "unit-test",
                }
            )
        report = build_candidate_purity_report(
            events,
            mode=ProductionMode.PRODUCTION_SHADOW_LIVE,
            registry=registry,
            as_of_date="2026-06-30",
        )
        coverage = report["summary"]["sector_coverage"]["summary"]
        self.assertGreaterEqual(coverage["active_large_sector_count"], 6)
        self.assertEqual(coverage["unknown_sector_candidate_count"], 0)


if __name__ == "__main__":
    unittest.main()
