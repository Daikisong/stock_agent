from datetime import date, datetime
from pathlib import Path
import csv
import json
import tempfile
import unittest
from unittest.mock import patch

from e2r.backtest.asof_research_replay import AsOfReplayCandidate, AsOfResearchReplay, AsOfResearchReplayConfig, _theme_route_provider_for_config, _write_candidates
from e2r.cli.run_asof_research_replay import build_parser, config_from_args
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
