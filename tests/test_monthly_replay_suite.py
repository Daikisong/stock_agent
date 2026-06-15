from datetime import date
from pathlib import Path
import json
import tempfile
import unittest

from e2r.backtest.historical_universe_replay import (
    HistoricalReplayCandidate,
    HistoricalReplayConfig,
    HistoricalReplayMode,
    HistoricalReplaySnapshot,
    HistoricalUniverseReplayResult,
    ReplayFrequency,
)
from e2r.backtest.monthly_replay_suite import (
    MonthlyReplaySuiteConfig,
    MonthlyReplaySuiteResult,
    MonthlyReplaySuiteRunner,
    _candidate_score_state,
    render_top_stage3_candidate_cards,
)
from e2r.cli.run_monthly_replay_suite import build_parser, config_from_args
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"


class MonthlyReplaySuiteTests(unittest.TestCase):
    def test_suite_cli_parses_args(self):
        args = build_parser().parse_args(
            [
                "--start-date",
                "2023-01-01",
                "--end-date",
                "2026-05-14",
                "--modes",
                "case_fixture,official_only,hybrid",
                "--skip-hybrid",
                "--frequency",
                "monthly",
                "--universe-limit",
                "3",
            ]
        )
        config = config_from_args(args)

        self.assertEqual(config.start_date, date(2023, 1, 1))
        self.assertEqual(config.end_date, date(2026, 5, 14))
        self.assertEqual(config.frequency, ReplayFrequency.MONTHLY)
        self.assertIn(HistoricalReplayMode.CASE_FIXTURE, config.modes)
        self.assertIn(HistoricalReplayMode.OFFICIAL_ONLY, config.modes)
        self.assertNotIn(HistoricalReplayMode.HYBRID, config.modes)
        self.assertEqual(config.universe_limit, 3)

    def test_suite_runs_all_modes_and_writes_operator_reports(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = MonthlyReplaySuiteRunner().run(
                MonthlyReplaySuiteConfig(
                    start_date=date(2023, 7, 27),
                    end_date=date(2023, 11, 27),
                    output_directory=output_dir,
                    modes=(
                        HistoricalReplayMode.CASE_FIXTURE,
                        HistoricalReplayMode.OFFICIAL_ONLY,
                        HistoricalReplayMode.HYBRID,
                    ),
                    frequency=ReplayFrequency.MONTHLY,
                    case_root=CASE_ROOT,
                )
            )

            expected_files = (
                "suite_summary.md",
                "suite_summary.json",
                "mode_comparison.md",
                "mode_comparison.json",
                "stage3_lifecycle_summary.md",
                "stage3_lifecycle_results.csv",
                "stage3_lifecycle_results.json",
                "known_case_validation.md",
                "missed_winners.md",
                "false_positives.md",
                "stage4b_4c_review.md",
                "evidence_coverage.md",
                "next_backtest_readiness.md",
                "top_stage3_candidate_cards.md",
            )
            for filename in expected_files:
                self.assertTrue((result.output_root / filename).exists(), filename)
            for mode in ("case_fixture", "official_only", "hybrid"):
                self.assertTrue((result.output_root / mode).is_dir(), mode)

            suite_text = (result.output_root / "suite_summary.md").read_text(encoding="utf-8")
            known_text = (result.output_root / "known_case_validation.md").read_text(encoding="utf-8")
            coverage_text = (result.output_root / "evidence_coverage.md").read_text(encoding="utf-8")

            self.assertIn("Stage 3-Green count", suite_text)
            self.assertIn("HD현대일렉트릭", known_text)
            self.assertIn("씨젠", known_text)
            self.assertIn("missing_report_news_snapshot_count", coverage_text)

    def test_suite_summary_json_has_required_schema_keys(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = MonthlyReplaySuiteRunner().run(
                MonthlyReplaySuiteConfig(
                    start_date=date(2023, 7, 27),
                    end_date=date(2023, 7, 27),
                    output_directory=output_dir,
                    modes=(HistoricalReplayMode.CASE_FIXTURE,),
                    case_root=CASE_ROOT,
                )
            )
            payload = json.loads((result.output_root / "suite_summary.json").read_text(encoding="utf-8"))

        for key in (
            "config",
            "modes",
            "aggregate_counts",
            "stage_distribution",
            "lifecycle_aggregates",
            "known_case_validation",
            "missed_winners",
            "false_positives",
            "evidence_coverage",
            "readiness_assessment",
            "limitations",
        ):
            self.assertIn(key, payload)

    def test_one_off_cases_are_not_forced_to_stage_3_green(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = MonthlyReplaySuiteRunner().run(
                MonthlyReplaySuiteConfig(
                    start_date=date(2020, 8, 24),
                    end_date=date(2020, 9, 1),
                    output_directory=output_dir,
                    modes=(HistoricalReplayMode.CASE_FIXTURE, HistoricalReplayMode.HYBRID),
                    frequency=ReplayFrequency.MONTHLY,
                    case_root=CASE_ROOT,
                )
            )

            one_off_rows = [row for row in result.known_case_validation if row["expected_group"] == "one_off"]
            self.assertTrue(one_off_rows)
            for row in one_off_rows:
                self.assertNotIn("3-Green", set(row["actual_stage_by_mode"].values()))

    def test_stage4b_unknown_is_reported_when_evidence_is_insufficient(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = MonthlyReplaySuiteRunner().run(
                MonthlyReplaySuiteConfig(
                    start_date=date(2023, 7, 27),
                    end_date=date(2023, 7, 27),
                    output_directory=output_dir,
                    modes=(HistoricalReplayMode.OFFICIAL_ONLY,),
                    case_root=CASE_ROOT,
                )
            )
            text = (result.output_root / "stage4b_4c_review.md").read_text(encoding="utf-8")

        self.assertIn("unknown_insufficient_evidence", text)

    def test_suite_outputs_do_not_contain_api_key_literals(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = MonthlyReplaySuiteRunner().run(
                MonthlyReplaySuiteConfig(
                    start_date=date(2023, 7, 27),
                    end_date=date(2023, 7, 27),
                    output_directory=output_dir,
                    modes=(HistoricalReplayMode.CASE_FIXTURE,),
                    case_root=CASE_ROOT,
                )
            )
            joined = "\n".join(path.read_text(encoding="utf-8") for path in result.output_root.glob("*.md"))

        self.assertNotIn("OPENDART_API_KEY", joined)
        self.assertNotIn("NAVER_CLIENT_SECRET", joined)
        self.assertNotIn("DATA_GO_KR_SERVICE_KEY", joined)

    def test_top_stage3_cards_do_not_fallback_to_diagnostics_when_score_pending(self):
        candidate = HistoricalReplayCandidate(
            case_id="case-1",
            symbol="111111",
            company_name="테스트",
            as_of_date=date(2023, 8, 1),
            stage=Stage.STAGE_3_YELLOW,
            total_score=None,
            layer1_result="deep_research",
            layer1_score=80.0,
            candidate_source_path="fixture",
            reason_codes=("TEST",),
            evidence_types_seen=("research_report",),
            score_components={},
            diagnostic_scores={"eps_fcf_explosion": 17.0, "contract_quality": 80.0},
            score_valid=False,
            score_blocked_reason="score_gap_unresolved",
            score_fingerprint="blocked-fingerprint",
            score_variability_drivers=("score_invalid:score_gap_unresolved", "raw_score_before_block:83"),
        )
        snapshot = HistoricalReplaySnapshot(
            as_of_date=date(2023, 8, 1),
            instruments_scanned=1,
            candidates=(candidate,),
            dropped_candidates=(),
            stage_snapshots=(),
            evidence_counts={},
            reason_code_distribution={},
            missing_evidence_warnings=(),
            source_coverage_summary={},
        )
        mode_result = HistoricalUniverseReplayResult(
            config=HistoricalReplayConfig(start_date=date(2023, 8, 1), end_date=date(2023, 8, 1)),
            snapshots=(snapshot,),
            lifecycle_results=(),
            known_case_validations=(),
        )
        suite = MonthlyReplaySuiteResult(
            config=MonthlyReplaySuiteConfig(start_date=date(2023, 8, 1), end_date=date(2023, 8, 1)),
            output_root=Path("."),
            mode_results={"case_fixture": mode_result},
            suite_summary={},
            mode_comparison={},
            lifecycle_aggregates={},
            known_case_validation=(),
            missed_winners=(),
            false_positives=(),
            evidence_coverage={},
            readiness_assessment={},
            limitations=(),
            report_paths={},
        )

        text = render_top_stage3_candidate_cards(suite)

        self.assertIn("| eps_fcf_explosion | n/a |", text)
        self.assertNotIn("17.0", text)
        self.assertIn("score_state: total=n/a; valid=False; reason=score_gap_unresolved", text)
        self.assertIn("score_invalid:score_gap_unresolved", text)

    def test_top_stage3_card_score_state_does_not_show_valid_true_without_visible_score(self):
        candidate = HistoricalReplayCandidate(
            case_id="case-1",
            symbol="111111",
            company_name="테스트",
            as_of_date=date(2023, 8, 1),
            stage=Stage.STAGE_3_YELLOW,
            total_score=None,
            layer1_result="deep_research",
            layer1_score=80.0,
            candidate_source_path="fixture",
            reason_codes=("TEST",),
            evidence_types_seen=("research_report",),
            score_valid=True,
            score_blocked_reason=None,
            score_fingerprint="scorefp",
        )

        text = _candidate_score_state(candidate)

        self.assertIn("total=n/a", text)
        self.assertIn("valid=False", text)
        self.assertIn("reason=visible_score_missing", text)


if __name__ == "__main__":
    unittest.main()
