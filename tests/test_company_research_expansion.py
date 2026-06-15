from datetime import date
import unittest
from unittest.mock import patch

from e2r.llm import FakeThemeRouteProvider, ThemeRouteOutput
from e2r.models import Instrument, Market, Stage, StageSnapshot
from e2r.pipeline import CompanyResearchInput, CompanyResearchPipeline, ConnectorBundle
from e2r.pipeline.stage_update import StageUpdateInput
from e2r.sources import ReportSearchResult


class CompanyResearchExpansionTests(unittest.TestCase):
    def test_company_research_score_gap_uses_llm_suggested_query_but_blocks_unresolved_material_gaps(self):
        connector = _ScoreGapReportConnector()
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=("테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )

        pipeline = CompanyResearchPipeline()
        capture_stage = _CaptureStageEngine()
        pipeline._stage_engine = capture_stage

        result = pipeline.run(
            CompanyResearchInput(
                instrument=Instrument(
                    symbol="777777",
                    name="테스트스코어",
                    market=Market.KR,
                    exchange="KRX",
                    sector_custom="semiconductor",
                ),
                as_of_date=date(2026, 6, 8),
                connectors=ConnectorBundle(report_search=connector),
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertGreaterEqual(connector.calls, 2)
        self.assertTrue(any("revision" in item for item in route_provider.calls[1].score_gap_context))
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)
        self.assertTrue(any(item.source_type == "consensus_revision" for item in result.evidence))
        self.assertIsNone(capture_stage.inputs)
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_score_gap"], 100.0)
        self.assertIn("score-gap expansion unresolved", " ".join(result.stage.stage_reason))

    def test_company_research_live_mode_defaults_to_codex_theme_provider(self):
        pipeline = CompanyResearchPipeline()

        with patch.dict("os.environ", {}, clear=True), patch(
            "e2r.llm.codex_theme_provider.CodexCLIThemeRouteProvider.route",
            return_value=ThemeRouteOutput(status="no_transition"),
        ) as route:
            pipeline.run(
                CompanyResearchInput(
                    instrument=Instrument(
                        symbol="888880",
                        name="테스트운영",
                        market=Market.KR,
                        exchange="KRX",
                        sector_custom="industrial",
                    ),
                    as_of_date=date(2026, 6, 8),
                    connectors=ConnectorBundle(),
                    fixture_mode=False,
                    max_theme_expansion_rounds=0,
                )
            )

        self.assertGreater(route.call_count, 0)

    def test_company_research_does_not_reclassify_blocked_theme_route_score(self):
        connector = _ProviderErrorReportConnector()
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="provider_error",
                blocked_reason="codex_cli_timeout",
            )
        )

        pipeline = CompanyResearchPipeline()
        capture_stage = _CaptureStageEngine()
        pipeline._stage_engine = capture_stage

        result = pipeline.run(
            CompanyResearchInput(
                instrument=Instrument(
                    symbol="777778",
                    name="테스트차단",
                    market=Market.KR,
                    exchange="KRX",
                    sector_custom="semiconductor",
                ),
                as_of_date=date(2026, 6, 8),
                connectors=ConnectorBundle(report_search=connector),
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIsNone(capture_stage.inputs)
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.total_score, 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertIn("theme route unresolved", " ".join(result.stage.stage_reason))


class _ScoreGapReportConnector:
    def __init__(self) -> None:
        self.calls = 0

    def search_reports(self, company: str, as_of_date: date):
        self.calls += 1
        if self.calls == 1:
            return ()
        return (
            ReportSearchResult(
                title="테스트스코어 추정치 상향 리포트",
                url="https://finance.example.com/research/test-score-gap-revision",
                source="fixture-research",
                publish_date=as_of_date,
                company=company,
                query="테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",
                snippet="EPS 상향 33%, 영업이익 추정치 상향 36%, FCF 상향 28%",
                is_recognized_report_domain=True,
                parsed_fields={
                    "extracted_text": (
                        "테스트스코어 리포트. EPS 상향 33%, 영업이익 추정치 상향 36%, "
                        "FCF 상향 28%, 목표주가 상향 18%."
                    )
                },
            ),
        )


class _ProviderErrorReportConnector:
    def search_reports(self, company: str, as_of_date: date):
        return (
            ReportSearchResult(
                title="테스트차단 실적 추정치 상향 리포트",
                url="https://finance.example.com/research/provider-error-report",
                source="fixture-research",
                publish_date=as_of_date,
                company=company,
                snippet="EPS 상향, 목표주가 상향, HBM 공급 확대",
                is_recognized_report_domain=True,
                parsed_fields={
                    "extracted_text": (
                        "테스트차단 리포트. EPS 상향 30%, 영업이익 추정치 상향 25%, "
                        "목표주가 상향 20%, HBM 공급 확대."
                    )
                },
            ),
        )


class _CaptureStageEngine:
    def __init__(self) -> None:
        self.inputs: StageUpdateInput | None = None

    def classify(self, inputs: StageUpdateInput) -> StageSnapshot:
        self.inputs = inputs
        return StageSnapshot(
            symbol=inputs.score.symbol,
            as_of_date=inputs.score.as_of_date,
            stage=Stage.STAGE_2,
            evidence_ids=inputs.evidence_ids,
        )


if __name__ == "__main__":
    unittest.main()
