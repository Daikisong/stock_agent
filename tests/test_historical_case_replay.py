from datetime import date
from pathlib import Path
import json
import tempfile
from types import SimpleNamespace
import unittest

from e2r.backtest.historical_case_replay import HistoricalCaseReplayRunner, _score_state_text, render_historical_case_replay_summary
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class HistoricalCaseReplayTests(unittest.TestCase):
    def test_replay_writes_json_and_markdown_outputs(self):
        with tempfile.TemporaryDirectory() as output_dir:
            summary = HistoricalCaseReplayRunner().run(
                as_of_date=date(2026, 5, 14),
                case_root=CASE_ROOT,
                output_directory=output_dir,
            )

            self.assertTrue(summary.output_json_path.exists())
            self.assertTrue(summary.output_md_path.exists())
            payload = json.loads(summary.output_json_path.read_text(encoding="utf-8"))
            rendered = summary.output_md_path.read_text(encoding="utf-8")

        self.assertEqual(payload["total_cases"], summary.total_cases)
        self.assertIn("stage_distribution", payload)
        self.assertIn("results", payload)
        self.assertIn("score_valid", payload["results"][0])
        self.assertIn("visible_score", payload["results"][0])
        self.assertIn("score_fingerprint", payload["results"][0])
        self.assertIn("research_input_fingerprint", payload["results"][0])
        self.assertIn("score_variability_drivers", payload["results"][0])
        self.assertIn("visible_score", rendered)
        self.assertIn("score state", rendered)

    def test_replay_records_stage_backtest_and_layer1_for_each_case(self):
        summary = HistoricalCaseReplayRunner().run(
            as_of_date=date(2026, 5, 14),
            case_root=CASE_ROOT,
            write_outputs=False,
        )

        self.assertGreaterEqual(summary.total_cases, 10)
        self.assertTrue(all(item.layer1_result.actual_layer1_result for item in summary.results))
        self.assertTrue(all(item.backtest.mfe_1y is not None for item in summary.results))
        self.assertTrue(all(item.backtest.mae_1y is not None for item in summary.results))
        self.assertTrue(all(item.score_valid is not None for item in summary.results))
        self.assertTrue(all(isinstance(item.score_fingerprint, str) for item in summary.results))
        self.assertTrue(all(isinstance(item.research_input_fingerprint, str) for item in summary.results))
        self.assertTrue(all(isinstance(item.score_variability_drivers, tuple) for item in summary.results))

    def test_expected_warning_cases_do_not_become_green_and_smci_order_is_preserved(self):
        summary = HistoricalCaseReplayRunner().run(
            as_of_date=date(2026, 5, 14),
            case_root=CASE_ROOT,
            write_outputs=False,
        )
        by_case = {item.case_id: item for item in summary.results}

        self.assertNotEqual(by_case["zoom_2020_red"].final_stage, Stage.STAGE_3_GREEN)
        self.assertNotEqual(by_case["seegene_2020_red"].final_stage, Stage.STAGE_3_GREEN)
        self.assertNotEqual(by_case["daehan_cable_like_2026_red"].final_stage, Stage.STAGE_3_GREEN)
        self.assertTrue(summary.smci_4b_before_4c)
        self.assertLess(by_case["smci_2024_4b_4c"].backtest.time_to_4b, by_case["smci_2024_4b_4c"].backtest.time_to_4c)

    def test_structural_miss_is_reported_instead_of_hidden(self):
        summary = HistoricalCaseReplayRunner().run(
            as_of_date=date(2026, 5, 14),
            case_root=CASE_ROOT,
            write_outputs=False,
        )

        self.assertIn("samyang_foods_2024", summary.structural_misses)
        rendered = render_historical_case_replay_summary(summary)
        self.assertIn("samyang_foods_2024", rendered)
        self.assertIn("structural_case_below_stage2", rendered)

    def test_markdown_score_state_does_not_show_valid_true_without_visible_score(self):
        text = _score_state_text(
            SimpleNamespace(
                total_score=None,
                score_valid=True,
                score_blocked_reason=None,
                score_fingerprint="scorefp",
            )
        )

        self.assertIn("valid=False", text)
        self.assertIn("reason=visible_score_missing", text)


if __name__ == "__main__":
    unittest.main()
