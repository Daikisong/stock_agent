from pathlib import Path
import unittest

from e2r.fixtures import FIXTURE_CASES, FixtureCategory, fixture_cases_by_category
from e2r.models import Stage


class FixtureSuiteTests(unittest.TestCase):
    def test_fixture_suite_contains_required_categories(self):
        expected_categories = {
            FixtureCategory.POWER_EQUIPMENT_SUCCESS,
            FixtureCategory.SEMICONDUCTOR_TURNAROUND,
            FixtureCategory.NON_POWER_RERATING,
            FixtureCategory.MOMENTUM_FALSE_POSITIVE,
            FixtureCategory.PEAK_OUT_AFTER_SUCCESS,
            FixtureCategory.STAGE3_OVERHEAT,
            FixtureCategory.US_BOOM_BUST,
        }

        self.assertEqual({case.category for case in FIXTURE_CASES}, expected_categories)

    def test_fixture_category_lookup(self):
        cases = fixture_cases_by_category(FixtureCategory.US_BOOM_BUST)

        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0].case_id, "us_boom_bust_4b_then_4c")

    def test_fixture_expected_stage_classifications(self):
        for case in FIXTURE_CASES:
            with self.subTest(case=case.case_id):
                snapshot = case.classify()

                self.assertEqual(snapshot.stage, case.expected_stage)
                self.assertLessEqual(case.red_team_signals.as_of_date, case.scoring_payload.as_of_date)
                self.assertTrue(snapshot.evidence_ids)

    def test_fixture_backtests_run_for_all_cases(self):
        for case in FIXTURE_CASES:
            with self.subTest(case=case.case_id):
                result = case.backtest()

                self.assertEqual(result.symbol, case.scoring_payload.symbol)
                self.assertEqual(result.stage3_date, case.stage3_date)
                self.assertIsNotNone(result.mfe_30d)
                self.assertIsNotNone(result.mae_30d)
                self.assertIsNotNone(result.pre_runup_252d)
                self.assertIsNotNone(result.below_entry_flag)

    def test_boom_bust_fixture_has_4b_before_4c_metrics(self):
        case = fixture_cases_by_category(FixtureCategory.US_BOOM_BUST)[0]
        result = case.backtest()

        self.assertEqual(case.expected_stage, Stage.STAGE_4B)
        self.assertIsNotNone(result.time_to_4b)
        self.assertIsNotNone(result.time_to_4c)
        self.assertLess(result.time_to_4b, result.time_to_4c)
        self.assertGreater(result.stage4b_return_from_stage3, 0)
        self.assertLess(result.drawdown_after_peak, 0)

    def test_fixture_symbols_are_not_embedded_in_logic_modules(self):
        root = Path(__file__).resolve().parents[1]
        logic_files = (
            root / "src/e2r/scoring.py",
            root / "src/e2r/staging.py",
            root / "src/e2r/red_team.py",
            root / "src/e2r/backtesting.py",
        )
        logic_text = "\n".join(path.read_text(encoding="utf-8") for path in logic_files)

        for case in FIXTURE_CASES:
            with self.subTest(case=case.case_id):
                self.assertNotIn(case.scoring_payload.symbol, logic_text)


if __name__ == "__main__":
    unittest.main()

