from datetime import date
from pathlib import Path
import tempfile
import unittest

from e2r.backtest.blind_discovery_replay import BlindDiscoveryConfig, BlindDiscoveryReplay
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.cli.run_blind_discovery_replay import build_parser, config_from_args
from e2r.models import Market, Stage
from e2r.pipeline.e2r_standard_flow import E2R_STANDARD


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "data/historical_cases"
LABELS = ROOT / "data/benchmark_labels/e2r_known_winners.json"


class BlindDiscoveryReplayTests(unittest.TestCase):
    def test_cli_parses_e2r_standard_flow(self):
        args = build_parser().parse_args(
            [
                "--start-date",
                "2023-01-01",
                "--end-date",
                "2026-05-14",
                "--frequency",
                "monthly",
                "--market",
                "KR",
                "--flow",
                "E2R_STANDARD",
            ]
        )
        config = config_from_args(args)

        self.assertEqual(config.flow, E2R_STANDARD)
        self.assertEqual(config.market, Market.KR)
        self.assertEqual(config.frequency, ReplayFrequency.MONTHLY)
        self.assertFalse(config.allow_fixture_source_proxy)
        self.assertTrue(config.use_search_snapshots)
        self.assertTrue(config.use_report_snapshots)

    def test_blind_discovery_runs_and_applies_labels_after_outputs(self):
        result = BlindDiscoveryReplay().run(
            BlindDiscoveryConfig(
                start_date=date(2023, 7, 1),
                end_date=date(2023, 12, 31),
                case_root=CASE_ROOT,
                benchmark_label_path=LABELS,
            ),
            write_outputs=False,
        )
        by_label = {item.label_id: item for item in result.benchmark_recall}

        self.assertTrue(result.discovered_candidates)
        self.assertTrue(result.replay_result.true_standard_flow_used)
        self.assertFalse(result.replay_result.fixture_proxy_used)
        self.assertTrue(by_label["hd_hyundai_electric_2023"].appeared_in_candidates)
        self.assertIn(by_label["hd_hyundai_electric_2023"].first_layer, {"event_search", "deep_research"})
        self.assertFalse(by_label["silicontwo_2024"].appeared_in_candidates)

    def test_fixture_proxy_is_explicit_and_labeled_diagnostic(self):
        result = BlindDiscoveryReplay().run(
            BlindDiscoveryConfig(
                start_date=date(2023, 7, 1),
                end_date=date(2023, 12, 31),
                case_root=CASE_ROOT,
                benchmark_label_path=LABELS,
                allow_fixture_source_proxy=True,
            ),
            write_outputs=False,
        )

        self.assertTrue(result.replay_result.fixture_proxy_used)
        self.assertFalse(result.replay_result.true_standard_flow_used)
        self.assertIn("fixture proxy mode; not proof of live discovery", result.replay_result.limitations)

    def test_one_off_or_boom_bust_labels_do_not_become_green(self):
        result = BlindDiscoveryReplay().run(
            BlindDiscoveryConfig(
                start_date=date(2020, 1, 1),
                end_date=date(2026, 5, 14),
                case_root=CASE_ROOT,
                benchmark_label_path=LABELS,
            ),
            write_outputs=False,
        )

        for item in result.benchmark_recall:
            if item.expected_group in {"one_off", "boom_bust", "valuation_overheat"} and item.appeared_in_candidates:
                self.assertNotEqual(item.first_stage, Stage.STAGE_3_GREEN)

    def test_blind_discovery_writes_required_reports(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = BlindDiscoveryReplay().run(
                BlindDiscoveryConfig(
                    start_date=date(2023, 7, 1),
                    end_date=date(2023, 12, 31),
                    output_directory=output_dir,
                    case_root=CASE_ROOT,
                    benchmark_label_path=LABELS,
                )
            )

            for filename in (
                "blind_discovery_summary.md",
                "blind_discovery_summary.json",
                "discovered_candidates.csv",
                "discovered_candidates.json",
                "benchmark_recall_report.md",
                "benchmark_recall_report.json",
                "missed_benchmark_labels.md",
                "false_positive_report.md",
                "stage_lifecycle_report.md",
                "evidence_coverage_report.md",
                "limitations.md",
                "source_coverage_report.md",
                "benchmark_leakage_audit.md",
                "llm_review.json",
                "llm_review.md",
            ):
                self.assertTrue((result.output_root / filename).exists(), filename)


if __name__ == "__main__":
    unittest.main()
