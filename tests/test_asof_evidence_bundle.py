from datetime import date, datetime
from pathlib import Path
import tempfile
import unittest

from e2r.backtest.asof_evidence_bundle import build_asof_evidence_bundle, score_asof_evidence_bundle
from e2r.backtest.historical_official_store import HistoricalOfficialStore
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.llm import FakeThemeRouteProvider, ThemeRouteOutput
from e2r.models import Market, Stage
from e2r.research.asof_web_research import AsOfWebResearchConfig, AsOfWebResearchRunner
from e2r.research.search_provider import SearchResult


class _Provider:
    def __init__(self, result):
        self.result = result

    def search(self, query, as_of_date, max_results=10):
        return (self.result,)


class AsOfEvidenceBundleTests(unittest.TestCase):
    def test_merges_official_and_web_sources_and_lifts_confidence(self):
        with tempfile.TemporaryDirectory() as root:
            official_root = Path(root) / "official"
            _write_official(official_root)
            report_path = Path(root) / "report.txt"
            report_path.write_text(_report_text(), encoding="utf-8")
            candidate = _candidate()
            web_result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    SearchResult(
                        title="테스트 수주잔고 OPM Review PDF",
                        url="https://example.com/report.pdf",
                        published_at=datetime(2023, 7, 27, 8, 0),
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    )
                ),
                fixture_text_by_url={"https://example.com/report.pdf": report_path},
                config=AsOfWebResearchConfig(as_of_date=date(2023, 8, 1)),
            )
            web_only = web_result.pipeline_result.score.information_confidence_score

            bundle = build_asof_evidence_bundle(candidate=candidate, store=HistoricalOfficialStore(official_root), web_result=web_result)
            scored = score_asof_evidence_bundle(bundle, candidate=candidate, web_result=web_result)

        self.assertGreater(len(bundle.price_bars), 0)
        self.assertGreater(len(bundle.financial_actuals), 0)
        self.assertGreater(len(bundle.official_disclosures), 0)
        self.assertGreater(len(bundle.research_reports), 0)
        self.assertGreater(len(bundle.consensus), 0)
        self.assertGreater(len(bundle.consensus_revisions), 0)
        self.assertGreater(scored.score.information_confidence_score, web_only)
        self.assertIn("price", bundle.source_types)
        self.assertIn("consensus_revision", bundle.source_types)

    def test_invalid_web_score_blocks_merged_asof_score(self):
        with tempfile.TemporaryDirectory() as root:
            official_root = Path(root) / "official"
            _write_official(official_root)
            report_path = Path(root) / "report.txt"
            report_path.write_text(_strong_report_text(), encoding="utf-8")
            candidate = _candidate()
            web_result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    SearchResult(
                        title="테스트 수주잔고 OPM Review PDF",
                        url="https://example.com/report.pdf",
                        published_at=datetime(2023, 7, 27, 8, 0),
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    )
                ),
                fixture_text_by_url={"https://example.com/report.pdf": report_path},
                config=AsOfWebResearchConfig(
                    as_of_date=date(2023, 8, 1),
                    theme_rebalance_enabled=True,
                    theme_route_provider=FakeThemeRouteProvider(
                        output=ThemeRouteOutput(status="provider_error", blocked_reason="codex_cli_timeout")
                    ),
                    theme_evidence_review_enabled=False,
                ),
            )
            bundle = build_asof_evidence_bundle(candidate=candidate, store=HistoricalOfficialStore(official_root), web_result=web_result)
            scored = score_asof_evidence_bundle(bundle, candidate=candidate, web_result=web_result)

        self.assertEqual(web_result.pipeline_result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(scored.stage.stage, Stage.STAGE_0)
        self.assertEqual(scored.score.total_score, 0.0)
        self.assertEqual(scored.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(scored.score.diagnostic_scores["score_blocked_by_asof_web"], 100.0)
        self.assertIn("raw_score_total_before_asof_web_block", scored.score.diagnostic_scores)

    def test_date_unverified_report_cannot_create_green_alone(self):
        with tempfile.TemporaryDirectory() as root:
            official_root = Path(root) / "official"
            _write_official(official_root)
            report_path = Path(root) / "report.txt"
            report_path.write_text(_strong_report_text(), encoding="utf-8")
            candidate = _candidate()
            web_result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    SearchResult(
                        title="테스트 수주잔고 OPM Review PDF",
                        url="https://example.com/report.pdf",
                        published_at=None,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    )
                ),
                fixture_text_by_url={"https://example.com/report.pdf": report_path},
                config=AsOfWebResearchConfig(as_of_date=date(2023, 8, 1)),
            )
            bundle = build_asof_evidence_bundle(candidate=candidate, store=HistoricalOfficialStore(official_root), web_result=web_result)
            scored = score_asof_evidence_bundle(bundle, candidate=candidate, web_result=web_result)

        self.assertNotEqual(scored.stage.stage, Stage.STAGE_3_GREEN)


def _candidate():
    return CheapScanCandidate(
        symbol="111111",
        company_name="테스트",
        market=Market.KR,
        as_of_date=date(2023, 8, 1),
        reason_codes=("DISC_SUPPLY_CONTRACT",),
        disclosure_event_score=70,
        cheap_scan_total_score=40,
        recommended_next_layer=RecommendedNextLayer.DEEP_RESEARCH,
    )


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


def _report_text() -> str:
    return """
2023.07.27
현재주가: 10000
목표주가: 15000
목표주가 상향: 25%
FY1 매출액: 1000
FY1 영업이익: 200
FY1 EPS: 1200
FY2 매출액: 1600
FY2 영업이익: 420
FY2 EPS: 2600
PER: 7
PBR: 1.2
수주잔고/매출: 180%
계약금액/매출: 30%
계약기간: 48개월
ASP 상승 리드타임 장기화 구조적 공급부족
"""


def _strong_report_text() -> str:
    return _report_text() + "\nOPM: 30%\nROE: 35%\nCAPA 증가율: 80%\n"


if __name__ == "__main__":
    unittest.main()
