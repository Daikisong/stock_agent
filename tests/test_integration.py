from datetime import date
import unittest

from e2r.briefing import ScheduledEvent, generate_morning_briefing
from e2r.connectors import MockDataConnector
from e2r.fixtures import FIXTURE_CASES, FixtureCategory, fixture_cases_by_category
from e2r.models import Market, SectorRegime, StageSnapshot


class E2RIntegrationTests(unittest.TestCase):
    def test_fixture_connector_pipeline_generates_briefing(self):
        connector = MockDataConnector.from_fixture_cases()
        cases = (
            fixture_cases_by_category(FixtureCategory.POWER_EQUIPMENT_SUCCESS)[0],
            fixture_cases_by_category(FixtureCategory.US_BOOM_BUST)[0],
            fixture_cases_by_category(FixtureCategory.PEAK_OUT_AFTER_SUCCESS)[0],
        )
        as_of_date = date(2024, 1, 11)
        instruments = connector.list_instruments(Market.KR, as_of_date) + connector.list_instruments(Market.US, as_of_date)
        scores = tuple(case.score() for case in cases)
        stages = tuple(self._force_changed(case.classify()) for case in cases)
        findings = tuple(finding for case in cases for finding in case.red_team_assessment().findings)
        backtests = tuple(case.backtest() for case in cases)
        evidence = tuple(evidence for case in cases for evidence in case.evidence)

        brief = generate_morning_briefing(
            as_of_date=as_of_date,
            instruments=instruments,
            scores=scores,
            stages=stages,
            red_team_findings=findings,
            backtests=backtests,
            evidence=evidence,
            sector_regimes=(
                SectorRegime(
                    sector="fixture_industrials",
                    date=as_of_date,
                    as_of_date=as_of_date,
                    theme_regime_score=81,
                    official_data_confirmation=76,
                    sector_relative_strength=67,
                ),
            ),
            scheduled_events=(
                ScheduledEvent(
                    event_date=as_of_date,
                    title="fixture disclosure review",
                    event_type="disclosure",
                    as_of_date=as_of_date,
                    source="fixture",
                ),
            ),
        )

        self.assertIn("[E2R Morning Brief / 2024-01-11]", brief.text)
        for case in cases:
            self.assertIn(case.scoring_payload.symbol, brief.text)
        self.assertIn("PreRunUp252D", brief.text)
        self.assertIn("Red Team thesis-break 감시", brief.text)
        self.assertIn("fixture disclosure review", brief.text)

    def test_connector_hides_future_price_bars_for_classification_date(self):
        case = fixture_cases_by_category(FixtureCategory.US_BOOM_BUST)[0]
        connector = MockDataConnector.from_fixture_cases((case,))
        future_end = date(2024, 1, 12)

        classification_bars = connector.get_price_bars(
            case.scoring_payload.symbol,
            date(2024, 1, 1),
            future_end,
            case.stage3_date,
        )
        outcome_bars = connector.get_price_bars(
            case.scoring_payload.symbol,
            date(2024, 1, 1),
            future_end,
            future_end,
        )

        self.assertTrue(classification_bars)
        self.assertTrue(outcome_bars)
        self.assertLess(len(classification_bars), len(outcome_bars))
        self.assertLessEqual(max(bar.as_of_date for bar in classification_bars), case.stage3_date)
        self.assertGreater(max(bar.high for bar in outcome_bars), max(bar.high for bar in classification_bars))

    def test_all_fixture_cases_complete_score_stage_and_backtest_path(self):
        for case in FIXTURE_CASES:
            with self.subTest(case=case.case_id):
                score = case.score()
                stage = case.classify()
                backtest = case.backtest()

                self.assertEqual(score.symbol, case.scoring_payload.symbol)
                self.assertEqual(stage.stage, case.expected_stage)
                self.assertEqual(backtest.symbol, case.scoring_payload.symbol)
                self.assertIsNotNone(backtest.peak_return_from_stage3)
                self.assertLessEqual(case.red_team_signals.as_of_date, case.scoring_payload.as_of_date)

    @staticmethod
    def _force_changed(stage: StageSnapshot) -> StageSnapshot:
        return StageSnapshot(
            symbol=stage.symbol,
            as_of_date=stage.as_of_date,
            stage=stage.stage,
            previous_stage=stage.previous_stage,
            stage_changed=True,
            grade=stage.grade,
            stage_reason=stage.stage_reason,
            red_team_status=stage.red_team_status,
            evidence_ids=stage.evidence_ids,
            classifier_version=stage.classifier_version,
        )


if __name__ == "__main__":
    unittest.main()

