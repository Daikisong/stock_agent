from datetime import date
from pathlib import Path
import tempfile
import unittest

from e2r.backtest.historical_universe_replay import (
    HistoricalReplayConfig,
    HistoricalReplayMode,
    HistoricalUniverseReplay,
    ReplayFrequency,
)
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class HistoricalUniverseReplayTests(unittest.TestCase):
    def test_case_fixture_mode_detects_known_structural_winners(self):
        result = HistoricalUniverseReplay().run(
            HistoricalReplayConfig(
                start_date=date(2023, 7, 27),
                end_date=date(2023, 11, 27),
                replay_frequency=ReplayFrequency.MONTHLY,
                mode=HistoricalReplayMode.CASE_FIXTURE,
                case_root=CASE_ROOT,
            ),
            write_outputs=False,
        )
        by_case = {item.case_id: item for item in result.known_case_validations}

        self.assertEqual(by_case["hd_hyundai_electric_2023"].status, "detected")
        self.assertEqual(by_case["hyosung_heavy_2023"].status, "detected")
        self.assertEqual(by_case["iljin_electric_2023_2024"].status, "detected")
        self.assertEqual(by_case["hd_hyundai_electric_2023"].final_stage, Stage.STAGE_3_GREEN)

    def test_replay_never_uses_report_evidence_after_as_of_date(self):
        result = HistoricalUniverseReplay().run(
            HistoricalReplayConfig(
                start_date=date(2023, 7, 27),
                end_date=date(2023, 7, 27),
                replay_frequency=ReplayFrequency.DAILY,
                mode=HistoricalReplayMode.CASE_FIXTURE,
                case_root=CASE_ROOT,
            ),
            write_outputs=False,
        )
        snapshot = result.snapshots[0]
        hyosung = next((item for item in snapshot.candidates if item.case_id == "hyosung_heavy_2023"), None)

        if hyosung is not None:
            self.assertNotIn("research_report", hyosung.evidence_types_seen)
        self.assertTrue(all(item.as_of_date == snapshot.as_of_date for item in snapshot.stage_snapshots))

    def test_official_only_mode_marks_missing_report_evidence(self):
        result = HistoricalUniverseReplay().run(
            HistoricalReplayConfig(
                start_date=date(2023, 7, 27),
                end_date=date(2023, 7, 27),
                replay_frequency=ReplayFrequency.DAILY,
                mode=HistoricalReplayMode.OFFICIAL_ONLY,
                case_root=CASE_ROOT,
            ),
            write_outputs=False,
        )
        joined = "\n".join(result.snapshots[0].missing_evidence_warnings)

        self.assertIn("evidence_missing:research_report_excluded_in_official_only", joined)
        self.assertTrue(result.snapshots[0].source_coverage_summary["official_only_report_news_excluded"])

    def test_one_off_case_does_not_become_stage_3_green(self):
        result = HistoricalUniverseReplay().run(
            HistoricalReplayConfig(
                start_date=date(2020, 8, 24),
                end_date=date(2020, 8, 24),
                replay_frequency=ReplayFrequency.DAILY,
                mode=HistoricalReplayMode.CASE_FIXTURE,
                case_root=CASE_ROOT,
            ),
            write_outputs=False,
        )
        seegene = next(item for item in result.known_case_validations if item.case_id == "seegene_2020_red")

        self.assertNotEqual(seegene.final_stage, Stage.STAGE_3_GREEN)
        self.assertEqual(seegene.status, "detected_but_yellow_red")

    def test_output_reports_are_written(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = HistoricalUniverseReplay().run(
                HistoricalReplayConfig(
                    start_date=date(2023, 7, 27),
                    end_date=date(2023, 7, 27),
                    replay_frequency=ReplayFrequency.DAILY,
                    mode=HistoricalReplayMode.CASE_FIXTURE,
                    case_root=CASE_ROOT,
                    output_directory=output_dir,
                )
            )

            self.assertTrue(result.summary_json_path.exists())
            self.assertTrue(result.summary_md_path.exists())
            self.assertTrue(result.lifecycle_json_path.exists())
            self.assertTrue(result.lifecycle_csv_path.exists())
            self.assertTrue(result.top_stage3_path.exists())
            self.assertTrue(result.false_positive_path.exists())
            self.assertTrue(result.missed_winner_path.exists())

    def test_missed_or_skipped_winner_report_includes_failure_reason(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = HistoricalUniverseReplay().run(
                HistoricalReplayConfig(
                    start_date=date(2023, 7, 27),
                    end_date=date(2023, 7, 27),
                    replay_frequency=ReplayFrequency.DAILY,
                    mode=HistoricalReplayMode.OFFICIAL_ONLY,
                    case_root=CASE_ROOT,
                    output_directory=output_dir,
                )
            )
            text = result.missed_winner_path.read_text(encoding="utf-8")

        self.assertIn("skipped_missing_historical_report_news_data", text)
        self.assertIn("evidence_missing", text)


if __name__ == "__main__":
    unittest.main()
