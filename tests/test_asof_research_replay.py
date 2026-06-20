from collections import Counter
from datetime import date, datetime
from pathlib import Path
import csv
import json
import tempfile
import unittest
from unittest.mock import patch

from e2r.backtest.asof_research_replay import (
    AsOfReplayCandidate,
    AsOfResearchReplay,
    AsOfResearchReplayConfig,
    _scheduled_replay_dates,
    _theme_route_provider_for_config,
    _write_candidates,
)
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.cli.run_asof_research_replay import build_parser, config_from_args, load_extra_replay_dates_file
from e2r.models import Stage
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchResult
from e2r.research.search_snapshot_store import SearchSnapshotStore, snapshot_from_search_result


class AsOfResearchReplayTests(unittest.TestCase):
    def test_cli_defaults_to_fixture_search_and_official_universe(self):
        args = build_parser().parse_args(["--start-date", "2023-07-01", "--end-date", "2023-08-01"])
        config = config_from_args(args)

        self.assertTrue(config.fixture_search)
        self.assertFalse(config.allow_snapshot_derived_universe)
        self.assertEqual(str(config.official_root), "data/historical_official")
        self.assertEqual(config.extra_replay_dates, ())
        self.assertIsNone(config.max_queries_per_candidate)
        self.assertIsNone(config.max_candidates_per_date)
        self.assertIsNone(config.max_web_research_candidates_per_date)
        self.assertIsNone(config.theme_rebalance_enabled)

    def test_cli_can_enable_asof_theme_rebalance_without_query_cap(self):
        args = build_parser().parse_args(
            [
                "--start-date",
                "2023-07-01",
                "--end-date",
                "2023-08-01",
                "--theme-rebalance",
            ]
        )
        config = config_from_args(args)

        self.assertTrue(config.theme_rebalance_enabled)
        self.assertIsNone(config.max_queries_per_candidate)
        self.assertIsNone(config.max_candidates_per_date)
        self.assertIsNone(config.max_web_research_candidates_per_date)

    def test_cli_accepts_extra_replay_dates_for_exact_fixture_runs(self):
        args = build_parser().parse_args(
            [
                "--start-date",
                "2023-07-01",
                "--end-date",
                "2023-08-01",
                "--extra-replay-date",
                "2023-07-27",
            ]
        )
        config = config_from_args(args)

        self.assertEqual(config.extra_replay_dates, (date(2023, 7, 27),))

    def test_cli_loads_extra_replay_dates_from_v12_fixture_spec_file(self):
        with tempfile.TemporaryDirectory() as directory:
            spec_path = Path(directory) / "fixture_spec.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "rows": [
                            {"candidate": {"as_of_date": "2024-04-25", "symbol": "000660"}},
                            {"candidate": {"trigger_date": "2024-05-14", "symbol": "006340"}},
                            {"candidate": {"as_of_date": "2026-01-01", "symbol": "OUT_OF_RANGE"}},
                        ]
                    }
                ),
                encoding="utf-8",
            )

            args = build_parser().parse_args(
                [
                    "--start-date",
                    "2024-04-01",
                    "--end-date",
                    "2024-05-31",
                    "--extra-replay-date",
                    "2024-04-01",
                    "--extra-replay-dates-file",
                    str(spec_path),
                ]
            )
            config = config_from_args(args)

        self.assertEqual(
            config.extra_replay_dates,
            (date(2024, 4, 1), date(2024, 4, 25), date(2024, 5, 14)),
        )

    def test_extra_replay_dates_file_supports_jsonl_and_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            jsonl_path = Path(directory) / "dates.jsonl"
            csv_path = Path(directory) / "dates.csv"
            jsonl_path.write_text(
                '{"candidate":{"as_of_date":"2024-04-25"}}\n{"trigger_date":"2024-05-14"}\n',
                encoding="utf-8",
            )
            csv_path.write_text("symbol,as_of_date\n000660,2024-04-25\n267260,2024-02-16\n", encoding="utf-8")

            jsonl_dates = load_extra_replay_dates_file(jsonl_path)
            csv_dates = load_extra_replay_dates_file(csv_path)

        self.assertEqual(jsonl_dates, (date(2024, 4, 25), date(2024, 5, 14)))
        self.assertEqual(csv_dates, (date(2024, 2, 16), date(2024, 4, 25)))

    def test_extra_replay_dates_are_sorted_and_deduped_with_base_schedule(self):
        replay_dates = _scheduled_replay_dates(
            date(2023, 7, 1),
            date(2023, 9, 1),
            ReplayFrequency.MONTHLY,
            (date(2023, 7, 27), "2023-08-01"),
        )

        self.assertEqual(
            replay_dates,
            (date(2023, 7, 1), date(2023, 7, 27), date(2023, 8, 1), date(2023, 9, 1)),
        )

    def test_asof_theme_rebalance_flag_defaults_to_codex_provider_without_env(self):
        with patch.dict("os.environ", {}, clear=True):
            provider = _theme_route_provider_for_config(
                AsOfResearchReplayConfig(
                    start_date=date(2023, 7, 1),
                    end_date=date(2023, 8, 1),
                    theme_rebalance_enabled=True,
                )
            )

        self.assertIsNotNone(provider)

    def test_universe_is_not_derived_from_search_snapshots(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111",))
            _write_labels(paths["labels"], symbol="999999")
            SearchSnapshotStore(paths["search"]).save_snapshot(
                snapshot_from_search_result(
                    SearchResult(title="스냅샷전용 수주잔고", url="https://example.com/999.pdf", published_at=datetime(2023, 7, 1, 8, 0)),
                    query="스냅샷전용 수주잔고",
                    search_date=date(2026, 5, 14),
                    symbol="999999",
                    company_name="스냅샷전용",
                )
            )

            result = AsOfResearchReplay().run(_config(paths), write_outputs=False)

        self.assertTrue(all(item.symbol != "999999" for item in result.discovered_candidates))
        self.assertEqual(result.benchmark_recall[0].failure_stage, "not_in_universe")

    def test_snapshot_derived_universe_adds_report_radar_candidate_when_enabled(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_labels(paths["labels"], symbol="333333")
            SearchSnapshotStore(paths["search"]).save_snapshot(
                snapshot_from_search_result(
                    SearchResult(
                        title="스냅샷후보 수주잔고 OPM Review PDF",
                        url="https://example.com/snapshot.pdf",
                        published_at=datetime(2023, 8, 1, 8, 0),
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                    query="스냅샷후보 수주잔고 OPM 수출 비중 PDF",
                    search_date=date(2026, 5, 14),
                    symbol="333333",
                    company_name="스냅샷후보",
                )
            )

            result = AsOfResearchReplay().run(
                AsOfResearchReplayConfig(
                    start_date=date(2023, 8, 1),
                    end_date=date(2023, 8, 1),
                    official_root=paths["official"],
                    benchmark_label_path=paths["labels"],
                    search_snapshot_root=paths["search"],
                    report_snapshot_root=paths["reports"],
                    output_directory=paths["output"],
                    allow_snapshot_derived_universe=True,
                    max_web_research_candidates_per_date=0,
                    max_queries_per_candidate=4,
                    max_results_per_query=5,
                ),
                write_outputs=False,
            )

        by_symbol = {item.symbol: item for item in result.discovered_candidates}
        self.assertIn("333333", by_symbol)
        self.assertEqual(by_symbol["333333"].candidate_source_path, "report_radar")
        self.assertTrue(result.benchmark_recall[0].appeared_in_candidates)
        self.assertIn("snapshot_derived_universe", result.snapshots[0].limitations)
        trace = result.snapshots[0].flow_traces[0]
        self.assertFalse(trace.reached("passed_official_cheap_scan"))
        self.assertTrue(trace.reached("report_radar_candidate"))

    def test_snapshot_derived_universe_rejects_future_published_snapshot(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_labels(paths["labels"], symbol="333333")
            SearchSnapshotStore(paths["search"]).save_snapshot(
                snapshot_from_search_result(
                    SearchResult(
                        title="스냅샷후보 수주잔고 OPM Review PDF",
                        url="https://example.com/future.pdf",
                        published_at=datetime(2023, 8, 2, 8, 0),
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                    query="스냅샷후보 수주잔고 OPM 수출 비중 PDF",
                    search_date=date(2026, 5, 14),
                    symbol="333333",
                    company_name="스냅샷후보",
                )
            )

            result = AsOfResearchReplay().run(
                AsOfResearchReplayConfig(
                    start_date=date(2023, 8, 1),
                    end_date=date(2023, 8, 1),
                    official_root=paths["official"],
                    benchmark_label_path=paths["labels"],
                    search_snapshot_root=paths["search"],
                    report_snapshot_root=paths["reports"],
                    output_directory=paths["output"],
                    allow_snapshot_derived_universe=True,
                    max_web_research_candidates_per_date=0,
                    max_queries_per_candidate=4,
                    max_results_per_query=5,
                ),
                write_outputs=False,
            )

        self.assertFalse(result.discovered_candidates)
        self.assertFalse(result.benchmark_recall[0].appeared_in_candidates)

    def test_snapshot_report_radar_does_not_cross_match_unrelated_official_symbol(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111",))
            _write_labels(paths["labels"], symbol="333333")
            SearchSnapshotStore(paths["search"]).save_snapshot(
                snapshot_from_search_result(
                    SearchResult(
                        title="스냅샷후보 수주잔고 OPM Review PDF",
                        url="https://example.com/snapshot.pdf",
                        published_at=datetime(2023, 8, 1, 8, 0),
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                    query="스냅샷후보 수주잔고 OPM 수출 비중 PDF",
                    search_date=date(2026, 5, 14),
                    symbol="333333",
                    company_name="스냅샷후보",
                )
            )

            result = AsOfResearchReplay().run(
                AsOfResearchReplayConfig(
                    start_date=date(2023, 8, 1),
                    end_date=date(2023, 8, 1),
                    official_root=paths["official"],
                    benchmark_label_path=paths["labels"],
                    search_snapshot_root=paths["search"],
                    report_snapshot_root=paths["reports"],
                    output_directory=paths["output"],
                    allow_snapshot_derived_universe=True,
                    max_web_research_candidates_per_date=0,
                    max_queries_per_candidate=4,
                    max_results_per_query=5,
                ),
                write_outputs=False,
            )

        self.assertFalse(
            any(item.symbol == "111111" and item.candidate_source_path == "report_radar" for item in result.discovered_candidates)
        )
        self.assertTrue(any(item.symbol == "333333" and item.candidate_source_path == "report_radar" for item in result.discovered_candidates))

    def test_missing_official_universe_reports_insufficient_data(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_labels(paths["labels"], symbol="111111")

            result = AsOfResearchReplay().run(_config(paths), write_outputs=False)

        self.assertIn("insufficient official historical data: universe missing", result.snapshots[0].limitations)
        self.assertFalse(result.discovered_candidates)

    def test_official_cheap_scan_runs_before_web_research_and_outputs_candidate(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111", "222222"))
            _write_labels(paths["labels"], symbol="111111")
            _write_search_and_report(paths["search"], paths["reports"], symbol="111111", company="공식테스트")

            result = AsOfResearchReplay().run(_config(paths), write_outputs=False)

        by_symbol = {item.symbol: item for item in result.discovered_candidates}
        self.assertIn("111111", by_symbol)
        self.assertNotIn("222222", by_symbol)
        trace = result.snapshots[0].flow_traces[0]
        self.assertEqual([step.name for step in trace.steps[:2]], ["entered_universe", "passed_official_cheap_scan"])
        self.assertTrue(trace.reached("free_web_research_executed"))
        self.assertTrue(trace.reached("documents_date_verified"))

    def test_extra_replay_date_enters_same_candidate_pipeline(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111", "222222"))
            _write_labels(paths["labels"], symbol="111111")
            result = AsOfResearchReplay().run(
                AsOfResearchReplayConfig(
                    start_date=date(2023, 7, 1),
                    end_date=date(2023, 8, 1),
                    frequency=ReplayFrequency.MONTHLY,
                    extra_replay_dates=(date(2023, 7, 27),),
                    official_root=paths["official"],
                    benchmark_label_path=paths["labels"],
                    search_snapshot_root=paths["search"],
                    report_snapshot_root=paths["reports"],
                    output_directory=paths["output"],
                    max_web_research_candidates_per_date=0,
                ),
                write_outputs=False,
            )

        snapshot_dates = tuple(snapshot.as_of_date for snapshot in result.snapshots)
        self.assertEqual(snapshot_dates, (date(2023, 7, 1), date(2023, 7, 27), date(2023, 8, 1)))
        self.assertTrue(
            any(item.symbol == "111111" and item.as_of_date == date(2023, 7, 27) for item in result.discovered_candidates)
        )

    def test_runtime_fixture_spec_adds_source_backed_candidate_without_official_universe(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_labels(paths["labels"], symbol="267260", expected_safe_stage="Green")
            source_path = Path(root) / "fixture_research.md"
            trigger = {
                "row_type": "trigger",
                "trigger_id": "fixture-green",
                "case_id": "fixture-case",
                "symbol": "267260",
                "company_name": "HD현대일렉트릭",
                "trigger_type": "Stage3-Green",
                "entry_date": "2024-02-16",
                "stage2_evidence_fields": ["power-grid/datacenter demand", "customer/capex route"],
                "stage3_evidence_fields": ["named backlog/order evidence", "delivery/revenue/margin bridge"],
                "evidence_available_at_that_date": "source-backed backlog, global customers, delivery and margin bridge",
            }
            source_path.write_text(json.dumps(trigger, ensure_ascii=False) + "\n", encoding="utf-8")
            spec_path = Path(root) / "runtime_fixture_spec.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "rows": [
                            {
                                "role": "green",
                                "fixture_status": "ready_for_runtime_replay_fixture",
                                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                                "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                                "expected_runtime_primitives": [
                                    "datacenter_customer",
                                    "order_backlog_to_sales",
                                "lead_time_extended",
                                "capacity_constraint",
                                "pricing_power_confirmed",
                                "delivery_schedule",
                                "order_to_revenue_bridge",
                                "customer_contract_visible",
                                "contract_amount_to_prior_sales",
                                "contract_duration_months",
                            ],
                            "candidate": {
                                    "symbol": "267260",
                                    "as_of_date": "2024-02-16",
                                    "trigger_id": "fixture-green",
                                    "case_id": "fixture-case",
                                "trigger_type": "Stage3-Green",
                                "evidence_source": "https://example.com/source-backed-report.pdf",
                                "source_file": str(source_path),
                                    "source_proxy_only": False,
                                    "evidence_url_pending": False,
                                },
                            }
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            result = AsOfResearchReplay().run(
                AsOfResearchReplayConfig(
                    start_date=date(2024, 2, 16),
                    end_date=date(2024, 2, 16),
                    official_root=paths["official"],
                    benchmark_label_path=paths["labels"],
                    search_snapshot_root=paths["search"],
                    report_snapshot_root=paths["reports"],
                    output_directory=paths["output"],
                    runtime_fixture_spec_paths=(spec_path,),
                    max_web_research_candidates_per_date=0,
                ),
                write_outputs=False,
            )

        row = result.discovered_candidates[0]
        self.assertEqual(row.symbol, "267260")
        self.assertEqual(row.candidate_source_path, "runtime_fixture_spec")
        self.assertIn("research_report", row.evidence_types_seen)
        self.assertTrue(row.score_valid)
        self.assertEqual(row.stage, Stage.STAGE_3_GREEN)

    def test_v12_runtime_fixture_spec_acceptance_covers_green_and_guard_rows(self):
        spec_path = Path("docs/0619/v12_runtime_replay_fixture_spec_2026-06-19.json")
        spec_payload = json.loads(spec_path.read_text(encoding="utf-8"))
        spec_rows = spec_payload["rows"]
        expected_roles = Counter(row["role"] for row in spec_rows)

        with tempfile.TemporaryDirectory() as root:
            result = AsOfResearchReplay().run(
                AsOfResearchReplayConfig(
                    start_date=date(2020, 1, 1),
                    end_date=date(2026, 5, 14),
                    frequency=ReplayFrequency.MONTHLY,
                    extra_replay_dates=load_extra_replay_dates_file(spec_path),
                    official_root=Path("data/historical_official"),
                    benchmark_label_path=Path("data/benchmark_labels/e2r_known_winners.json"),
                    search_snapshot_root=Path("data/search_snapshots"),
                    report_snapshot_root=Path("data/report_snapshots"),
                    output_directory=Path(root) / "output",
                    max_web_research_candidates_per_date=0,
                    runtime_fixture_spec_paths=(spec_path,),
                ),
                write_outputs=False,
            )

        fixture_rows = [item for item in result.discovered_candidates if item.candidate_source_path == "runtime_fixture_spec"]
        stage_counts = Counter((_fixture_candidate_role(item), item.stage) for item in fixture_rows)

        self.assertEqual(len(fixture_rows), len(spec_rows))
        self.assertEqual(stage_counts[("green", Stage.STAGE_3_GREEN)], expected_roles["green"])
        self.assertEqual(
            sum(count for (role, stage), count in stage_counts.items() if role == "green" and stage != Stage.STAGE_3_GREEN),
            0,
        )
        self.assertEqual(
            sum(count for (role, stage), count in stage_counts.items() if role == "guard" and stage == Stage.STAGE_3_GREEN),
            0,
        )
        self.assertEqual(sum(count for (role, _stage), count in stage_counts.items() if role == "guard"), expected_roles["guard"])

    def test_fake_benchmark_label_without_evidence_does_not_create_candidate(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111",))
            _write_labels(paths["labels"], symbol="333333", expected_safe_stage="Green")

            result = AsOfResearchReplay().run(_config(paths), write_outputs=False)

        self.assertTrue(all(item.symbol != "333333" for item in result.discovered_candidates))
        self.assertFalse(result.benchmark_recall[0].appeared_in_candidates)

    def test_outputs_are_written_with_failure_stage_report(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111",))
            _write_labels(paths["labels"], symbol="111111")
            result = AsOfResearchReplay().run(_config(paths, output=paths["output"]))
            summary_exists = (result.output_root / "asof_replay_summary.md").exists()
            failure_exists = (result.output_root / "failure_stage_report.md").exists()
            candidates_exists = (result.output_root / "discovered_candidates.csv").exists()
            candidates_json = json.loads((result.output_root / "discovered_candidates.json").read_text(encoding="utf-8"))
            candidates_csv = (result.output_root / "discovered_candidates.csv").read_text(encoding="utf-8")

        self.assertTrue(summary_exists)
        self.assertTrue(failure_exists)
        self.assertTrue(candidates_exists)
        self.assertIn("score_valid", candidates_json[0])
        self.assertIn("visible_score", candidates_json[0])
        self.assertIn("score_fingerprint", candidates_json[0])
        self.assertIn("research_input_fingerprint", candidates_json[0])
        self.assertIn("score_variability_drivers", candidates_json[0])
        self.assertIn("web_only_research_input_fingerprint", candidates_json[0])
        self.assertIn("web_only_score_variability_drivers", candidates_json[0])
        self.assertIn("visible_score", candidates_csv)
        self.assertIn("research_input_fingerprint", candidates_csv)
        self.assertIn("score_variability_drivers", candidates_csv)

    def test_asof_writer_normalizes_invalid_non_null_score(self):
        rows = (
            AsOfReplayCandidate(
                symbol="000003",
                company_name="잘못된보류점수",
                as_of_date=date(2026, 6, 1),
                layer="deep_research",
                stage=Stage.STAGE_0,
                rank=1,
                score=83.0,
                evidence_types_seen=("research_report",),
                reason_codes=("score_pending",),
                candidate_source_path="fixture",
                web_only_score=77.0,
                merged_score=83.0,
                score_valid=False,
                score_blocked_reason="score_gap_unresolved",
                score_fingerprint="blocked-fingerprint",
                research_input_fingerprint="blocked-input-fingerprint",
                score_variability_drivers=("score_invalid:score_gap_unresolved", "raw_score_before_block:83"),
                web_only_score_valid=None,
                web_only_score_blocked_reason=None,
                web_only_score_fingerprint="blocked-web-only-fingerprint",
                web_only_research_input_fingerprint="blocked-web-only-input-fingerprint",
                web_only_score_variability_drivers=("score_invalid:theme_route_unresolved", "raw_score_before_block:77"),
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
        self.assertEqual(csv_rows[0]["merged_score"], "")
        self.assertEqual(csv_rows[0]["web_only_score"], "")
        self.assertIsNone(json_rows[0]["score"])
        self.assertIsNone(json_rows[0]["visible_score"])
        self.assertIsNone(json_rows[0]["merged_score"])
        self.assertIsNone(json_rows[0]["web_only_score"])

    def test_one_off_label_is_not_forced_green(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _fixture_paths(root)
            _write_official(paths["official"], symbols=("111111",))
            _write_labels(paths["labels"], symbol="111111", group="one_off", expected_safe_stage="Red")
            result = AsOfResearchReplay().run(_config(paths), write_outputs=False)

        for item in result.benchmark_recall:
            if item.appeared_in_candidates:
                self.assertNotEqual(item.first_stage, Stage.STAGE_3_GREEN)


def _fixture_paths(root: str):
    base = Path(root)
    return {
        "official": base / "official",
        "search": base / "search",
        "reports": base / "reports",
        "labels": base / "labels.json",
        "output": base / "output",
    }


def _config(paths, *, output=None):
    return AsOfResearchReplayConfig(
        start_date=date(2023, 8, 1),
        end_date=date(2023, 8, 1),
        official_root=paths["official"],
        benchmark_label_path=paths["labels"],
        search_snapshot_root=paths["search"],
        report_snapshot_root=paths["reports"],
        output_directory=output or paths["output"],
        max_web_research_candidates_per_date=5,
        max_queries_per_candidate=4,
        max_results_per_query=2,
    )


def _fixture_candidate_role(candidate: AsOfReplayCandidate) -> str:
    for code in candidate.reason_codes:
        if code.startswith("fixture_role:"):
            return code.split(":", 1)[1]
    return ""


def _write_labels(path: Path, *, symbol: str, group: str = "structural", expected_safe_stage: str = "Yellow") -> None:
    rows = [
        {
            "label_id": f"label-{symbol}",
            "symbol": symbol,
            "company_name": "벤치마크",
            "market": "KR",
            "expected_window_start": "2023-07-01",
            "expected_window_end": "2023-09-30",
            "expected_group": group,
            "expected_min_layer": "event_search",
            "expected_safe_stage": expected_safe_stage,
            "notes": "test only",
            "evaluation_only": True,
        }
    ]
    path.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")


def _write_official(root: Path, *, symbols: tuple[str, ...]) -> None:
    for name in ("universe", "prices", "disclosures", "financials", "risks"):
        (root / name).mkdir(parents=True, exist_ok=True)
    universe = "symbol,name,market,exchange,listed_date\n"
    for symbol in symbols:
        name = "공식테스트" if symbol == "111111" else "비후보"
        universe += f"{symbol},{name},KR,KRX,2020-01-01\n"
    (root / "universe" / "universe.csv").write_text(universe, encoding="utf-8")
    (root / "prices" / "prices.csv").write_text(
        "symbol,date,open,high,low,close,adj_close,volume,trading_value,market_cap,source,as_of_date\n"
        "111111,2023-07-01,1000,1000,1000,1000,1000,100,100000,100000000,historical,2023-07-01\n"
        "111111,2023-07-27,1300,1400,1200,1350,1350,1000,1350000,135000000,historical,2023-07-27\n"
        "222222,2023-07-27,1000,1000,1000,1000,1000,100,100000,100000000,historical,2023-07-27\n",
        encoding="utf-8",
    )
    (root / "disclosures" / "disclosures.csv").write_text(
        "symbol,source,report_type,title,published_at,observed_at,available_at,as_of_date,rcept_no,raw_text\n"
        '111111,OpenDART,단일판매·공급계약체결,단일판매·공급계약체결,2023-07-27T08:00:00,'
        '2023-07-27T08:00:00,2023-07-27T08:00:00,2023-07-27,r1,'
        '"계약금액 100억원 매출액 대비 20% 계약기간 2023-07-27 ~ 2026-07-26"\n',
        encoding="utf-8",
    )
    (root / "financials" / "financials.csv").write_text(
        "symbol,fiscal_year,fiscal_quarter,period_end,reported_at,as_of_date,source\n",
        encoding="utf-8",
    )
    (root / "risks" / "risks.csv").write_text(
        "symbol,as_of_date,source,managed_issue,trading_halt,investment_warning,investor_caution,unfaithful_disclosure,delisting_risk,raw_text\n",
        encoding="utf-8",
    )


def _write_search_and_report(search_root: Path, report_root: Path, *, symbol: str, company: str) -> None:
    SearchSnapshotStore(search_root).save_snapshot(
        snapshot_from_search_result(
            SearchResult(
                title=f"{company} 수주잔고 OPM Review PDF",
                url="https://example.com/report.pdf",
                published_at=datetime(2023, 7, 27, 8, 0),
                is_pdf=True,
                is_report_domain=True,
                confidence=0.9,
            ),
            query=f"{company} 수주잔고 OPM 수출 비중 PDF",
            search_date=date(2026, 5, 14),
            symbol=symbol,
            company_name=company,
        )
    )
    ReportSnapshotStore(report_root).save_text_snapshot(
        url="https://example.com/report.pdf",
        title=f"{company} 수주잔고 OPM Review PDF",
        text="2023.07.27\n현재주가: 10000\n목표주가: 15000\n목표주가 상향: 25%\nFY1 EPS: 1000\nFY2 EPS: 1800\n수주잔고/매출: 150%\nOPM: 15%\nASP 상승 리드타임 장기화 구조적 공급부족",
        fetched_at=datetime(2026, 5, 14, 9, 0),
        as_of_date=date(2023, 7, 27),
        symbol=symbol,
        company_name=company,
        source_type="broker_report",
    )


if __name__ == "__main__":
    unittest.main()
