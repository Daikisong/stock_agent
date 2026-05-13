from pathlib import Path
import unittest

from e2r.historical_cases import load_historical_case, load_historical_cases, run_historical_case_pipeline
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class HistoricalCaseLoaderTests(unittest.TestCase):
    def test_required_historical_case_files_exist(self):
        expected = {
            "hd_hyundai_electric_2023.json",
            "hyosung_heavy_2023.json",
            "iljin_electric_2023_2024.json",
            "sanil_electric_2025.json",
            "samyang_foods_2024.json",
            "hanwha_aerospace_2024.json",
            "nvidia_2023.json",
            "zoom_2020_red.json",
            "seegene_2020_red.json",
            "smci_2024_4b_4c.json",
        }

        self.assertTrue(expected.issubset({path.name for path in CASE_ROOT.glob("*.json")}))

    def test_hd_hyundai_electric_pipeline_reaches_stage_3_green_from_raw_case_data(self):
        case = load_historical_case(CASE_ROOT / "hd_hyundai_electric_2023.json")
        result = run_historical_case_pipeline(case)

        self.assertTrue(result.case.evidence)
        self.assertGreater(result.score.total_score, 85)
        self.assertEqual(result.feature_result.shortage_type.value, "structural")
        self.assertGreater(result.score.diagnostic_scores["contract_quality"], 45)
        self.assertEqual(result.stage.stage, Stage.STAGE_3_GREEN)
        self.assertEqual(result.backtest.stage3_date, case.stage3_date)

    def test_hyosung_becomes_stage_3_green_after_margin_and_target_revision_evidence(self):
        case = load_historical_case(CASE_ROOT / "hyosung_heavy_2023.json")
        result = run_historical_case_pipeline(case)

        self.assertEqual(result.stage.stage, Stage.STAGE_3_GREEN)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 50)
        self.assertGreater(result.score.diagnostic_scores["contract_quality"], 45)

    def test_daehan_cable_like_case_is_filtered_below_high_confidence(self):
        case = load_historical_case(CASE_ROOT / "daehan_cable_2026_red.json")
        result = run_historical_case_pipeline(case)

        self.assertIn(result.stage.stage, {Stage.STAGE_0, Stage.STAGE_1, Stage.STAGE_2, Stage.STAGE_3_RED})
        self.assertNotIn(result.stage.stage, {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW})
        self.assertLess(result.score.valuation_rerating_score, 7)

    def test_one_off_demand_cases_become_stage_3_red(self):
        for filename in ("zoom_2020_red.json", "seegene_2020_red.json"):
            with self.subTest(filename=filename):
                result = run_historical_case_pipeline(load_historical_case(CASE_ROOT / filename))

                self.assertEqual(result.feature_result.shortage_type.value, "one_off")
                self.assertGreaterEqual(result.score.diagnostic_scores["one_off_shortage_risk"], 80)
                self.assertEqual(result.stage.stage, Stage.STAGE_3_RED)

    def test_smci_like_case_triggers_4b_before_4c_in_backtest(self):
        case = load_historical_case(CASE_ROOT / "smci_2024_4b_4c.json")
        result = run_historical_case_pipeline(case)

        self.assertIsNotNone(result.backtest.time_to_4b)
        self.assertIsNotNone(result.backtest.time_to_4c)
        self.assertLess(result.backtest.time_to_4b, result.backtest.time_to_4c)

    def test_historical_names_are_not_embedded_in_logic_modules(self):
        cases = load_historical_cases(CASE_ROOT)
        logic_files = (
            ROOT / "src/e2r/scoring.py",
            ROOT / "src/e2r/features.py",
            ROOT / "src/e2r/staging.py",
            ROOT / "src/e2r/red_team.py",
        )
        logic_text = "\n".join(path.read_text(encoding="utf-8") for path in logic_files)

        for case in cases:
            with self.subTest(case=case.case_id):
                self.assertNotIn(case.company_name, logic_text)


if __name__ == "__main__":
    unittest.main()
