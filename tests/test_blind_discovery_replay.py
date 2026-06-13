from datetime import date
from pathlib import Path
import csv
import json
import tempfile
import unittest

from e2r.backtest.blind_discovery_replay import BlindDiscoveryConfig, BlindDiscoveryReplay, DiscoveredCandidate, _discovered_candidates, _write_candidates
from e2r.backtest.e2r_standard_replay import (
    E2RStandardReplayCandidate,
    E2RStandardReplayConfig,
    E2RStandardReplayResult,
    E2RStandardReplaySnapshot,
)
from e2r.backtest.historical_source_adapter import HistoricalSourceCoverage
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
        self.assertTrue(result.replay_result.candidates)
        self.assertIsNotNone(result.replay_result.candidates[0].score_valid)
        self.assertIsInstance(result.replay_result.candidates[0].score_fingerprint, str)
        self.assertIsInstance(result.replay_result.candidates[0].score_variability_drivers, tuple)
        self.assertIsNotNone(result.discovered_candidates[0].score_valid)
        self.assertIsInstance(result.discovered_candidates[0].score_fingerprint, str)
        self.assertIsInstance(result.discovered_candidates[0].score_variability_drivers, tuple)
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
        self.assertTrue(result.replay_result.candidates)
        self.assertIsNotNone(result.replay_result.candidates[0].score_valid)
        self.assertIsInstance(result.replay_result.candidates[0].score_fingerprint, str)
        self.assertIsInstance(result.replay_result.candidates[0].score_variability_drivers, tuple)

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

    def test_invalid_score_candidate_is_sorted_last_and_written_blank(self):
        coverage = HistoricalSourceCoverage(
            universe_available=True,
            price_available=True,
            disclosure_available=True,
            financial_available=True,
            search_snapshot_available=True,
            report_snapshot_available=True,
        )
        replay_result = E2RStandardReplayResult(
            config=E2RStandardReplayConfig(start_date=date(2026, 6, 1), end_date=date(2026, 6, 1)),
            snapshots=(
                E2RStandardReplaySnapshot(
                    as_of_date=date(2026, 6, 1),
                    source_coverage=coverage,
                    candidates=(
                        E2RStandardReplayCandidate(
                            symbol="000001",
                            company_name="유효점수",
                            as_of_date=date(2026, 6, 1),
                            layer="deep_research",
                            stage=Stage.STAGE_2,
                            rank=1,
                            score=72.0,
                            evidence_types_seen=("research_report",),
                            reason_codes=("ok",),
                            candidate_source_path="fixture",
                            score_valid=True,
                            score_fingerprint="valid-fingerprint",
                            research_input_fingerprint="valid-input-fingerprint",
                            score_variability_drivers=(),
                        ),
                        E2RStandardReplayCandidate(
                            symbol="000002",
                            company_name="보류점수",
                            as_of_date=date(2026, 6, 1),
                            layer="deep_research",
                            stage=Stage.STAGE_0,
                            rank=2,
                            score=None,
                            evidence_types_seen=("research_report",),
                            reason_codes=("score_pending",),
                            candidate_source_path="fixture",
                            score_valid=False,
                            score_blocked_reason="score_gap_unresolved",
                            score_fingerprint="blocked-fingerprint",
                            research_input_fingerprint="blocked-input-fingerprint",
                            score_variability_drivers=(
                                "score_invalid:score_gap_unresolved",
                                "raw_score_before_block:83",
                                "research_input_fingerprint:blocked-input-fingerprint",
                            ),
                        ),
                    ),
                ),
            ),
            candidates=(),
            source_coverage_summary={},
        )

        rows = _discovered_candidates(replay_result)

        self.assertEqual([item.symbol for item in rows], ["000001", "000002"])
        self.assertIsNone(rows[1].score)
        self.assertFalse(rows[1].score_valid)
        self.assertEqual(rows[1].score_blocked_reason, "score_gap_unresolved")
        self.assertEqual(rows[1].research_input_fingerprint, "blocked-input-fingerprint")
        self.assertIn("score_invalid:score_gap_unresolved", rows[1].score_variability_drivers)
        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "candidates.csv"
            json_path = Path(directory) / "candidates.json"
            _write_candidates(csv_path, json_path, rows)
            with csv_path.open(encoding="utf-8") as handle:
                csv_rows = list(csv.DictReader(handle))
            json_rows = json.loads(json_path.read_text(encoding="utf-8"))

        self.assertEqual(csv_rows[1]["score"], "")
        self.assertEqual(csv_rows[1]["visible_score"], "")
        self.assertEqual(csv_rows[1]["score_valid"], "False")
        self.assertEqual(csv_rows[1]["score_blocked_reason"], "score_gap_unresolved")
        self.assertEqual(csv_rows[1]["research_input_fingerprint"], "blocked-input-fingerprint")
        self.assertIn("score_invalid:score_gap_unresolved", csv_rows[1]["score_variability_drivers"])
        self.assertEqual(json_rows[1]["research_input_fingerprint"], "blocked-input-fingerprint")
        self.assertIn("visible_score", json_rows[1])
        self.assertIsNone(json_rows[1]["visible_score"])
        self.assertFalse(json_rows[1]["score_valid"])
        self.assertEqual(json_rows[1]["score_fingerprint"], "blocked-fingerprint")

    def test_blind_discovery_writer_normalizes_invalid_non_null_score(self):
        rows = (
            DiscoveredCandidate(
                symbol="000003",
                company_name="잘못된보류점수",
                as_of_date=date(2026, 6, 1),
                layer="deep_research",
                stage=Stage.STAGE_0,
                rank=1,
                score=83.0,
                evidence_types_seen=("research_report",),
                reason_codes=("score_pending",),
                score_valid=False,
                score_blocked_reason="score_gap_unresolved",
                score_fingerprint="blocked-fingerprint",
                research_input_fingerprint="blocked-input-fingerprint",
                score_variability_drivers=("score_invalid:score_gap_unresolved", "raw_score_before_block:83"),
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "candidates.csv"
            json_path = Path(directory) / "candidates.json"
            _write_candidates(csv_path, json_path, rows)
            with csv_path.open(encoding="utf-8") as handle:
                csv_rows = list(csv.DictReader(handle))
            json_rows = json.loads(json_path.read_text(encoding="utf-8"))

        self.assertEqual(csv_rows[0]["score"], "")
        self.assertEqual(csv_rows[0]["visible_score"], "")
        self.assertIsNone(json_rows[0]["score"])
        self.assertIsNone(json_rows[0]["visible_score"])

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
