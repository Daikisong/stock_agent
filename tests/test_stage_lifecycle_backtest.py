from pathlib import Path
import tempfile
import unittest

from e2r.backtest.stage_lifecycle_backtest import (
    STAGE4B_DETECTED,
    STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE,
    StageLifecycleBacktest,
    StageLifecycleInput,
    write_stage_lifecycle_outputs,
)
from e2r.historical_cases import load_historical_case
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class StageLifecycleBacktestTests(unittest.TestCase):
    def test_stage_lifecycle_metrics_compute_mfe_and_mae(self):
        case = load_historical_case(CASE_ROOT / "hd_hyundai_electric_2023.json")
        result = StageLifecycleBacktest().evaluate(
            StageLifecycleInput(
                symbol=case.symbol,
                company_name=case.company_name,
                stage=Stage.STAGE_3_GREEN,
                stage_date=case.stage3_date,
                stage_price=case.stage3_price,
                price_bars=case.price_bars,
                stage_snapshots=case.stage_snapshots,
            )
        )

        self.assertIsNone(result.failure_reason)
        self.assertIsNotNone(result.mfe_1y)
        self.assertIsNotNone(result.mae_1y)
        self.assertIsNotNone(result.peak_return_from_stage)
        self.assertGreater(result.peak_price, result.stage_price)

    def test_stage4b_unknown_when_evidence_is_missing(self):
        case = load_historical_case(CASE_ROOT / "hd_hyundai_electric_2023.json")
        result = StageLifecycleBacktest().evaluate(
            StageLifecycleInput(
                symbol=case.symbol,
                company_name=case.company_name,
                stage=Stage.STAGE_3_GREEN,
                stage_date=case.stage3_date,
                stage_price=case.stage3_price,
                price_bars=case.price_bars,
                stage_snapshots=(),
                evidence_coverage_insufficient=True,
            )
        )

        self.assertEqual(result.stage4b_status, STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE)
        self.assertIsNone(result.stage4b_date)

    def test_smci_stage4b_is_detected_before_4c(self):
        case = load_historical_case(CASE_ROOT / "smci_2024_4b_4c.json")
        result = StageLifecycleBacktest().evaluate(
            StageLifecycleInput(
                symbol=case.symbol,
                company_name=case.company_name,
                stage=Stage.STAGE_3_RED,
                stage_date=case.stage3_date,
                stage_price=case.stage3_price,
                price_bars=case.price_bars,
                stage_snapshots=case.stage_snapshots,
            )
        )

        self.assertEqual(result.stage4b_status, STAGE4B_DETECTED)
        self.assertIsNotNone(result.stage4b_date)
        self.assertIsNotNone(result.stage4c_date)
        self.assertLess(result.stage4b_date, result.stage4c_date)

    def test_stage_lifecycle_outputs_are_written(self):
        case = load_historical_case(CASE_ROOT / "hd_hyundai_electric_2023.json")
        result = StageLifecycleBacktest().evaluate(
            StageLifecycleInput(
                symbol=case.symbol,
                company_name=case.company_name,
                stage=Stage.STAGE_3_GREEN,
                stage_date=case.stage3_date,
                stage_price=case.stage3_price,
                price_bars=case.price_bars,
            )
        )
        with tempfile.TemporaryDirectory() as output_dir:
            json_path = Path(output_dir) / "stage_lifecycle_results.json"
            csv_path = Path(output_dir) / "stage_lifecycle_results.csv"
            write_stage_lifecycle_outputs((result,), json_path=json_path, csv_path=csv_path)

            self.assertTrue(json_path.exists())
            self.assertTrue(csv_path.exists())
            self.assertIn("stage4b_status", csv_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
