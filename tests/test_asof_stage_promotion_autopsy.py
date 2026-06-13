from datetime import date, datetime
from pathlib import Path
import json
from types import SimpleNamespace
import tempfile
import unittest

from e2r.backtest.asof_stage_promotion_autopsy import (
    AsOfStagePromotionAutopsy,
    AsOfStagePromotionAutopsyConfig,
    StagePromotionAutopsyRow,
    _autopsy_row,
    _jsonable,
    _score_state_text,
)
from e2r.cli.analyze_asof_stage_promotion import build_parser, config_from_args
from e2r.models import ScoreSnapshot, Stage
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchResult
from e2r.research.search_snapshot_store import SearchSnapshotStore, snapshot_from_search_result
from e2r.score_validity import score_state_contract_violations


class AsOfStagePromotionAutopsyTests(unittest.TestCase):
    def test_cli_parses_args(self):
        args = build_parser().parse_args(["--asof-output", "output/backtests/asof_research_replay/test"])
        config = config_from_args(args)

        self.assertEqual(str(config.asof_output), "output/backtests/asof_research_replay/test")
        self.assertIsNone(config.top_candidates)
        self.assertIsNone(config.max_queries_per_candidate)

    def test_autopsy_writes_gate_and_coverage_outputs(self):
        with tempfile.TemporaryDirectory() as root:
            paths = _paths(root)
            _write_asof_output(paths["asof"])
            _write_official(paths["official"])
            _write_search_and_report(paths["search"], paths["reports"])

            result = AsOfStagePromotionAutopsy().run(
                AsOfStagePromotionAutopsyConfig(
                    asof_output=paths["asof"],
                    output_directory=paths["output"],
                    official_root=paths["official"],
                    search_snapshot_root=paths["search"],
                    report_snapshot_root=paths["reports"],
                    report_date=date(2026, 5, 14),
                )
            )
            self.assertTrue(result.rows)
            self.assertTrue((paths["output"] / "2026-05-14_autopsy.md").exists())
            self.assertTrue((paths["output"] / "stage_gate_matrix.csv").exists())
            self.assertTrue((paths["output"] / "feature_input_coverage.csv").exists())
            self.assertIn("failed_stage3_bottleneck", (paths["output"] / "stage_gate_matrix.csv").read_text(encoding="utf-8"))
            self.assertIn("score_valid", (paths["output"] / "score_components_by_candidate.csv").read_text(encoding="utf-8"))
            self.assertIn("score_fingerprint", (paths["output"] / "stage_gate_matrix.csv").read_text(encoding="utf-8"))
            self.assertIn("research_input_fingerprint", (paths["output"] / "stage_gate_matrix.csv").read_text(encoding="utf-8"))

    def test_autopsy_row_hides_components_for_invalid_score(self):
        score = ScoreSnapshot(
            symbol="111111",
            as_of_date=date(2023, 8, 1),
            eps_fcf_explosion_score=0,
            earnings_visibility_score=0,
            bottleneck_pricing_score=0,
            market_mispricing_score=0,
            valuation_rerating_score=0,
            capital_allocation_score=0,
            information_confidence_score=0,
            risk_penalty=0,
            total_score=0,
            diagnostic_scores={
                "score_valid": 0.0,
                "score_blocked_by_asof_web": 100.0,
                "raw_eps_fcf_before_asof_web_block": 17.0,
                "raw_score_total_before_asof_web_block": 82.0,
            },
        )
        candidate = SimpleNamespace(
            symbol="111111",
            company_name="테스트",
            as_of_date=date(2023, 8, 1),
            recommended_next_layer=SimpleNamespace(value="deep_research"),
        )
        scored = SimpleNamespace(
            score=score,
            bundle=SimpleNamespace(
                coverage=lambda: {
                    "price_bars_count": 0,
                    "financial_actuals_count": 0,
                    "disclosures_count": 0,
                    "research_reports_count": 0,
                    "news_items_count": 0,
                    "consensus_count": 0,
                    "consensus_revisions_count": 0,
                }
            ),
            audit_findings=(),
            red_team=SimpleNamespace(risk_level=SimpleNamespace(value="low"), has_hard_break=False),
            stage=SimpleNamespace(stage=Stage.STAGE_0),
        )
        diagnostics = SimpleNamespace(
            failed_gate_names=("failed_score_validity",),
            sector_profile="GENERIC",
            stage2_gate_passed=False,
            stage3_green_gate_passed=False,
            cross_evidence_families_present=(),
            missing_evidence_families=(),
        )

        row = _autopsy_row(candidate, scored, diagnostics)

        self.assertIsNone(row.current_score)
        self.assertFalse(row.score_valid)
        self.assertEqual(row.score_blocked_reason, "asof_web_score_unresolved")
        self.assertIsInstance(row.score_fingerprint, str)
        self.assertIsInstance(row.research_input_fingerprint, str)
        self.assertIn("score_invalid:asof_web_score_unresolved", row.score_variability_drivers)
        self.assertIn("raw_score_before_block:82", row.score_variability_drivers)
        self.assertIn(f"research_input_fingerprint:{row.research_input_fingerprint}", row.score_variability_drivers)
        self.assertEqual(row.raw_score_before_block, 82.0)
        self.assertIsNone(row.eps_fcf_explosion)
        self.assertIsNone(row.information_confidence)
        self.assertEqual(row.promotion_band, "Score Pending")
        self.assertEqual(row.explanation, "Score pending: asof_web_score_unresolved.")

    def test_autopsy_jsonable_normalizes_invalid_current_score_alias(self):
        row = StagePromotionAutopsyRow(
            symbol="111111",
            company_name="테스트",
            as_of_date=date(2023, 8, 1),
            layer="deep_research",
            current_stage=Stage.STAGE_0,
            current_score=82.0,
            score_valid=False,
            score_blocked_reason="asof_web_score_unresolved",
            score_fingerprint="blocked-score",
            research_input_fingerprint="input-a",
            score_variability_drivers=("score_invalid:asof_web_score_unresolved", "raw_score_before_block:82"),
            raw_score_before_block=82.0,
            eps_fcf_explosion=None,
            earnings_visibility=None,
            bottleneck_pricing=None,
            market_mispricing=None,
            valuation_rerating=None,
            capital_allocation=None,
            information_confidence=None,
            risk_penalty=None,
            revision_score=None,
            price_stage_score=None,
            contract_quality=None,
            backlog_rpo_visibility=None,
            capa_constraint=None,
            asp_pricing_power=None,
            structural_shortage=None,
            one_off_shortage_risk=None,
            structural_visibility_quality=None,
            sector_visibility_score=None,
            sector_bottleneck_score=None,
            recurring_demand_visibility=None,
            export_channel_visibility=None,
            medium_term_revision_visibility=None,
            domain_specific_evidence_score=None,
            sector_profile="GENERIC",
            promotion_band="Score Pending",
            cross_evidence_families_present="",
            missing_evidence_families="",
            price_bars_count=0,
            financial_actuals_count=0,
            disclosures_count=0,
            research_reports_count=0,
            news_items_count=0,
            consensus_count=0,
            consensus_revisions_count=0,
            failed_stage2_total_score=True,
            failed_stage2_eps_fcf=False,
            failed_stage2_valuation=False,
            failed_stage2_information_confidence=False,
            failed_stage3_total_score=True,
            failed_stage3_eps_fcf=False,
            failed_stage3_visibility=False,
            failed_stage3_bottleneck=False,
            failed_stage3_market_mispricing=False,
            failed_stage3_valuation=False,
            failed_stage3_revision=False,
            failed_stage3_contract_quality=False,
            failed_structural_visibility_quality=False,
            failed_sector_visibility=False,
            failed_sector_bottleneck=False,
            failed_green_cross_evidence=False,
            failed_report_date_confidence=False,
            failed_domain_specific_evidence=False,
            failed_stage3_red_team=False,
            red_team_risk="low",
            hard_audit_count=0,
            explanation="Score pending: asof_web_score_unresolved.",
        )

        payload = _jsonable(row)

        self.assertIsNone(payload["current_score"])
        self.assertIsNone(payload["visible_score"])
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_autopsy_score_state_text_does_not_show_valid_true_without_visible_score(self):
        text = _score_state_text(
            SimpleNamespace(
                current_score=None,
                score_valid=True,
                score_blocked_reason=None,
                score_fingerprint="scorefp",
                raw_score_before_block=None,
            )
        )

        self.assertIn("pending visible_score_missing", text)
        self.assertNotIn("valid / fp", text)


def _paths(root: str):
    base = Path(root)
    return {
        "asof": base / "asof",
        "official": base / "official",
        "search": base / "search",
        "reports": base / "reports",
        "output": base / "output",
    }


def _write_asof_output(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    candidates = [
        {
            "symbol": "111111",
            "company_name": "테스트",
            "as_of_date": "2023-08-01",
            "layer": "deep_research",
            "stage": "1",
            "rank": 1,
            "score": 30.0,
            "reason_codes": ["DISC_SUPPLY_CONTRACT"],
            "candidate_source_path": "official_cheap_scan",
        }
    ]
    recall = [
        {
            "label_id": "label-111111",
            "symbol": "111111",
            "company_name": "테스트",
            "expected_group": "structural",
            "appeared_in_candidates": True,
            "first_detected_date": "2023-08-01",
            "first_layer": "deep_research",
            "first_stage": "1",
            "detection_lag_days": 31,
            "evidence_types_seen": ["research_report"],
            "failure_stage": None,
        }
    ]
    (root / "discovered_candidates.json").write_text(json.dumps(candidates, ensure_ascii=False), encoding="utf-8")
    (root / "benchmark_recall_report.json").write_text(json.dumps(recall, ensure_ascii=False), encoding="utf-8")


def _write_official(root: Path) -> None:
    for name in ("universe", "prices", "disclosures", "financials", "risks"):
        (root / name).mkdir(parents=True, exist_ok=True)
    (root / "universe" / "universe.csv").write_text(
        "symbol,name,market,exchange,listed_date\n111111,테스트,KR,KRX,2020-01-01\n",
        encoding="utf-8",
    )
    (root / "prices" / "prices.csv").write_text(
        "symbol,date,open,high,low,close,adj_close,volume,trading_value,market_cap,source,as_of_date\n"
        "111111,2023-07-01,1000,1000,900,950,950,100,95000,100000000,historical,2023-07-01\n"
        "111111,2023-07-27,1300,1400,1200,1350,1350,1000,1350000,135000000,historical,2023-07-27\n",
        encoding="utf-8",
    )
    (root / "financials" / "financials.csv").write_text(
        "symbol,fiscal_year,fiscal_quarter,period_end,reported_at,as_of_date,source,sales,operating_profit,net_income,eps,fcf\n"
        "111111,2023,2,2023-06-30,2023-07-27T08:00:00,2023-07-27,historical,800,100,80,500,90\n",
        encoding="utf-8",
    )
    (root / "disclosures" / "disclosures.csv").write_text(
        "symbol,source,report_type,title,published_at,observed_at,available_at,as_of_date,rcept_no,raw_text\n"
        '111111,OpenDART,단일판매·공급계약체결,단일판매·공급계약체결,2023-07-27T08:00:00,2023-07-27T08:00:00,2023-07-27T08:00:00,2023-07-27,r1,'
        '"계약금액 100억원 매출액 대비 30% 계약기간 2023-07-27 ~ 2027-07-26 수주잔고 사상 최대 ASP 상승 리드타임 장기화 공급부족"\n',
        encoding="utf-8",
    )
    (root / "risks" / "risks.csv").write_text(
        "symbol,as_of_date,source,managed_issue,trading_halt,investment_warning,investor_caution,unfaithful_disclosure,delisting_risk,raw_text\n",
        encoding="utf-8",
    )


def _write_search_and_report(search_root: Path, report_root: Path) -> None:
    SearchSnapshotStore(search_root).save_snapshot(
        snapshot_from_search_result(
            SearchResult(
                title="테스트 수주잔고 OPM Review PDF",
                url="https://example.com/report.pdf",
                published_at=datetime(2023, 7, 27, 8, 0),
                is_pdf=True,
                is_report_domain=True,
                confidence=0.9,
            ),
            query="테스트 수주잔고 OPM 수출 비중 PDF",
            search_date=date(2026, 5, 14),
            symbol="111111",
            company_name="테스트",
        )
    )
    ReportSnapshotStore(report_root).save_text_snapshot(
        url="https://example.com/report.pdf",
        title="테스트 수주잔고 OPM Review PDF",
        text="2023.07.27\n현재주가: 10000\n목표주가: 15000\n목표주가 상향: 25%\nFY1 EPS: 1000\nFY2 EPS: 1800\n수주잔고/매출: 160%\nASP 상승 리드타임 장기화 구조적 공급부족",
        fetched_at=datetime(2026, 5, 14, 9, 0),
        as_of_date=date(2023, 8, 1),
        symbol="111111",
        company_name="테스트",
        source_type="broker_report",
    )


if __name__ == "__main__":
    unittest.main()
