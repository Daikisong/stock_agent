from datetime import date, datetime
import unittest

from e2r.models import Evidence, Market, PriceBar, SourceTier, Stage, StageSnapshot


class EvidenceModelTests(unittest.TestCase):
    def test_evidence_keeps_point_in_time_dates(self):
        evidence = Evidence(
            evidence_id="ev-1",
            source_type="research_report",
            source_name="MockBroker",
            source_tier=SourceTier.TIER_1,
            published_at=datetime(2024, 3, 27, 8, 0),
            observed_at=datetime(2024, 3, 27, 8, 5),
            available_at=datetime(2024, 3, 27, 8, 10),
            as_of_date=date(2024, 3, 27),
            market=Market.KR,
            symbol="103590",
            title="CAPA expansion report",
            parsed_fields={"contract_quality": "high"},
            confidence=0.9,
        )

        self.assertEqual(evidence.as_of_date, date(2024, 3, 27))
        self.assertEqual(evidence.parsed_fields["contract_quality"], "high")

    def test_evidence_rejects_future_availability(self):
        with self.assertRaisesRegex(ValueError, "available_at cannot be after as_of_date"):
            Evidence(
                evidence_id="ev-2",
                source_type="disclosure",
                source_name="MockDART",
                source_tier=SourceTier.TIER_0,
                published_at=datetime(2024, 3, 28, 17, 0),
                observed_at=datetime(2024, 3, 28, 17, 1),
                available_at=datetime(2024, 3, 28, 17, 2),
                as_of_date=date(2024, 3, 27),
                market=Market.KR,
                symbol="103590",
                title="Future disclosure",
            )


class PriceModelTests(unittest.TestCase):
    def test_price_bar_rejects_close_outside_daily_range(self):
        with self.assertRaisesRegex(ValueError, "close must be inside low/high range"):
            PriceBar(
                symbol="005930",
                date=date(2024, 1, 2),
                open=100.0,
                high=110.0,
                low=90.0,
                close=120.0,
                adj_close=120.0,
                volume=1000,
                trading_value=100000.0,
                market_cap=1000000000.0,
                source="mock",
                as_of_date=date(2024, 1, 2),
            )


class StageModelTests(unittest.TestCase):
    def test_stage_snapshot_accepts_canonical_stage_3_color(self):
        snapshot = StageSnapshot(
            symbol="267260",
            as_of_date=date(2023, 7, 27),
            stage=Stage.STAGE_3_GREEN,
            previous_stage=Stage.STAGE_2,
            stage_changed=True,
            stage_reason=("consensus revision and backlog evidence",),
            evidence_ids=("ev-hd-1",),
        )

        self.assertEqual(snapshot.stage.value, "3-Green")
        self.assertTrue(snapshot.stage_changed)


if __name__ == "__main__":
    unittest.main()

