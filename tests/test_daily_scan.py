from datetime import date
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.models import Market, ScoreSnapshot, Stage
from e2r.pipeline import ConnectorBundle, DailyScanConfig, DailyScanRunner
from e2r.pipeline.daily_scan import _score_output_row
from e2r.score_validity import score_state_contract_violations


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class DailyScanRunnerTests(unittest.TestCase):
    def test_daily_runner_scans_historical_fixture_universe_and_writes_outputs(self):
        with TemporaryDirectory() as output_dir:
            result = DailyScanRunner().run(
                DailyScanConfig(
                    as_of_date=date(2026, 5, 14),
                    markets=(Market.KR, Market.US),
                    connector_bundle=ConnectorBundle(),
                    output_directory=output_dir,
                    include_historical_cases=True,
                    historical_case_dir=CASE_ROOT,
                )
            )

            self.assertTrue(result.company_results)
            self.assertTrue(result.markdown_path.exists())
            self.assertTrue(result.json_path.exists())
            self.assertTrue(result.stages)
            self.assertTrue(result.evidence)
            self.assertIn("[E2R Morning Brief / 2026-05-14]", result.morning_brief.text)

            payload = json.loads(result.json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["as_of_date"], "2026-05-14")
            self.assertTrue(payload["company_results"])
            self.assertTrue(payload["scores"])
            self.assertIn("score_valid", payload["scores"][0])
            self.assertIn("visible_score", payload["scores"][0])
            self.assertIn("research_input_fingerprint", payload["scores"][0])
            self.assertIn("score_variability_drivers", payload["scores"][0])
            self.assertIn("visible_score", payload["company_results"][0])
            self.assertIn("research_input_fingerprint", payload["company_results"][0])
            self.assertIn("score_variability_drivers", payload["company_results"][0])
            self.assertIn("feature_input_counts", payload["company_results"][0])

    def test_hd_and_zoom_appear_with_expected_stages_in_generated_brief(self):
        with TemporaryDirectory() as output_dir:
            result = DailyScanRunner().run(
                DailyScanConfig(
                    as_of_date=date(2026, 5, 14),
                    markets=(Market.KR, Market.US),
                    connector_bundle=ConnectorBundle(),
                    output_directory=output_dir,
                    include_historical_cases=True,
                    historical_case_dir=CASE_ROOT,
                )
            )

            stage_by_symbol = {item.instrument.symbol: item.stage.stage for item in result.company_results}
            self.assertEqual(stage_by_symbol["267260"], Stage.STAGE_3_GREEN)
            self.assertEqual(stage_by_symbol["ZM"], Stage.STAGE_3_RED)
            self.assertIn("HD현대일렉트릭", result.morning_brief.text)
            self.assertIn("Zoom", result.morning_brief.text)
            self.assertIn("3-Green", result.morning_brief.text)
            self.assertIn("3-Red", result.morning_brief.text)

    def test_daily_runner_does_not_use_future_data_for_feature_scoring(self):
        with TemporaryDirectory() as output_dir:
            result = DailyScanRunner().run(
                DailyScanConfig(
                    as_of_date=date(2026, 5, 14),
                    markets=(Market.KR, Market.US),
                    connector_bundle=ConnectorBundle(),
                    output_directory=output_dir,
                    include_historical_cases=True,
                    historical_case_dir=CASE_ROOT,
                )
            )
            hd_result = next(item for item in result.company_results if item.instrument.symbol == "267260")

            self.assertTrue(hd_result.backtest)
            self.assertGreater(hd_result.backtest.peak_date, hd_result.as_of_date)
            self.assertLessEqual(max(bar.date for bar in hd_result.feature_input.price_bars), hd_result.as_of_date)
            self.assertLessEqual(max(bar.as_of_date for bar in hd_result.feature_input.price_bars), hd_result.as_of_date)
            self.assertLessEqual(max(item.as_of_date for item in hd_result.evidence), hd_result.as_of_date)

    def test_daily_runner_handles_missing_connector_data_gracefully(self):
        with TemporaryDirectory() as output_dir:
            result = DailyScanRunner().run(
                DailyScanConfig(
                    as_of_date=date(2026, 5, 14),
                    markets=(Market.KR,),
                    connector_bundle=ConnectorBundle(),
                    active_watchlist_symbols=("MISSING",),
                    output_directory=output_dir,
                )
            )

            self.assertEqual(len(result.company_results), 1)
            self.assertEqual(result.company_results[0].stage.stage, Stage.STAGE_0)
            self.assertEqual(result.company_results[0].evidence, ())
            self.assertEqual(result.errors, ())
            self.assertIn("해당 없음", result.morning_brief.text)

    def test_stage_3_green_and_stage_3_red_both_appear_in_fixture_output(self):
        with TemporaryDirectory() as output_dir:
            result = DailyScanRunner().run(
                DailyScanConfig(
                    as_of_date=date(2026, 5, 14),
                    markets=(Market.KR, Market.US),
                    connector_bundle=ConnectorBundle(),
                    output_directory=output_dir,
                    include_historical_cases=True,
                    historical_case_dir=CASE_ROOT,
                )
            )

            stages = {item.stage.stage for item in result.company_results}

            self.assertIn(Stage.STAGE_3_GREEN, stages)
            self.assertIn(Stage.STAGE_3_RED, stages)

    def test_score_output_row_hides_invalid_component_scores_and_keeps_raw_reference(self):
        score = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=0,
            earnings_visibility_score=0,
            bottleneck_pricing_score=0,
            market_mispricing_score=0,
            valuation_rerating_score=0,
            capital_allocation_score=0,
            information_confidence_score=0,
            risk_penalty=0,
            total_score=0,
            diagnostic_scores={
                "score_blocked_by_score_gap": 100.0,
                "raw_score_total_before_score_gap_block": 83.0,
            },
        )

        row = _score_output_row(score)

        self.assertFalse(row["score_valid"])
        self.assertEqual(row["score_blocked_reason"], "score_gap_unresolved")
        self.assertIsInstance(row["score_fingerprint"], str)
        self.assertIn("score_invalid:score_gap_unresolved", row["score_variability_drivers"])
        self.assertIn("raw_score_before_block:83", row["score_variability_drivers"])
        self.assertIsNone(row["visible_score"])
        self.assertIsNone(row["total_score"])
        self.assertIsNone(row["research_input_fingerprint"])
        self.assertEqual(row["raw_score_before_block"], 83.0)
        self.assertIsNone(row["component_scores"])
        self.assertEqual(score_state_contract_violations(row), ())

    def test_company_result_output_includes_research_input_fingerprint(self):
        with TemporaryDirectory() as directory:
            config = DailyScanConfig(
                as_of_date=date(2024, 3, 27),
                output_directory=directory,
                universe_limit=1,
            )
            scan = DailyScanRunner().run(config)
            payload = json.loads(scan.json_path.read_text(encoding="utf-8"))

        result = payload["company_results"][0]
        score_row = payload["scores"][0]
        self.assertEqual(result["visible_score"], result["score"])
        self.assertIsInstance(result["research_input_fingerprint"], str)
        self.assertTrue(any(item.startswith("research_input_fingerprint:") for item in result["score_variability_drivers"]))
        self.assertEqual(score_row["research_input_fingerprint"], result["research_input_fingerprint"])
        self.assertEqual(score_row["visible_score"], score_row["total_score"])
        self.assertTrue(any(item.startswith("research_input_fingerprint:") for item in score_row["score_variability_drivers"]))
        self.assertEqual(score_state_contract_violations(result), ())
        self.assertEqual(score_state_contract_violations(score_row), ())


if __name__ == "__main__":
    unittest.main()
