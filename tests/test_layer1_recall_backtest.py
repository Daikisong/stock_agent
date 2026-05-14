from dataclasses import replace
from pathlib import Path
import unittest

from e2r.backtest.layer1_recall import (
    LAYER_DEEP_RESEARCH,
    LAYER_EVENT_SEARCH,
    Layer1RecallCase,
    evaluate_layer1_recall,
    evaluate_layer1_recall_case,
)
from e2r.historical_cases import load_historical_case, load_historical_cases, run_historical_case_pipeline
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class Layer1RecallBacktestTests(unittest.TestCase):
    def test_structural_winners_reach_event_search_or_better(self):
        for filename in (
            "hd_hyundai_electric_2023.json",
            "hyosung_heavy_2023.json",
            "iljin_electric_2023_2024.json",
        ):
            with self.subTest(filename=filename):
                case = load_historical_case(CASE_ROOT / filename)
                result = evaluate_layer1_recall_case(
                    case,
                    Layer1RecallCase(
                        case_id=case.case_id,
                        symbol=case.symbol,
                        company_name=case.company_name,
                        as_of_date=case.stage3_date,
                        expected_trigger_date=case.stage3_date,
                        expected_layer1_min_result=LAYER_EVENT_SEARCH,
                        expected_final_stage=case.expected_stage,
                    ),
                )

                self.assertIn(result.actual_layer1_result, {LAYER_EVENT_SEARCH, LAYER_DEEP_RESEARCH})
                self.assertTrue(result.passed_minimum, result.false_none_reason)
                self.assertFalse(result.future_data_used)

    def test_one_off_cases_do_not_become_stage_3_green(self):
        for filename in ("zoom_2020_red.json", "seegene_2020_red.json"):
            with self.subTest(filename=filename):
                case = load_historical_case(CASE_ROOT / filename)
                result = evaluate_layer1_recall_case(case)

                self.assertNotEqual(result.final_stage, Stage.STAGE_3_GREEN)
                self.assertEqual(run_historical_case_pipeline(case).feature_result.shortage_type.value, "one_off")

    def test_smci_like_case_triggers_4b_before_4c(self):
        case = load_historical_case(CASE_ROOT / "smci_2024_4b_4c.json")
        pipeline = run_historical_case_pipeline(case)

        self.assertIsNotNone(pipeline.backtest.time_to_4b)
        self.assertIsNotNone(pipeline.backtest.time_to_4c)
        self.assertLess(pipeline.backtest.time_to_4b, pipeline.backtest.time_to_4c)

    def test_summary_reports_recall_metrics_and_failures(self):
        summary = evaluate_layer1_recall(load_historical_cases(CASE_ROOT))

        self.assertGreater(summary.recall_top_50, 0.0)
        self.assertGreater(summary.reached_event_search, 0)
        self.assertGreater(summary.reached_deep_research, 0)
        self.assertTrue(all(item.rank is not None for item in summary.results))

    def test_failure_reason_is_explicit_when_structural_fixture_is_not_detected(self):
        case = load_historical_case(CASE_ROOT / "hd_hyundai_electric_2023.json")
        missing = replace(
            case,
            research_reports=(),
            disclosures=(),
            news_items=(),
            financial_actuals=(),
            consensus=(),
            consensus_revisions=(),
            evidence=(),
            price_bars=(),
        )
        result = evaluate_layer1_recall_case(
            missing,
            Layer1RecallCase(
                case_id=missing.case_id,
                symbol=missing.symbol,
                company_name=missing.company_name,
                as_of_date=missing.stage3_date,
                expected_trigger_date=missing.stage3_date,
                expected_layer1_min_result=LAYER_EVENT_SEARCH,
                expected_final_stage=missing.expected_stage,
            ),
        )

        self.assertFalse(result.passed_minimum)
        self.assertEqual(result.false_none_reason, "source_missing")


if __name__ == "__main__":
    unittest.main()
