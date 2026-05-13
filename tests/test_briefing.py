from datetime import date, datetime
import unittest

from e2r.briefing import MorningBrief, ScheduledEvent, generate_morning_briefing
from e2r.connectors import MockDataConnector
from e2r.fixtures import FIXTURE_CASES, FixtureCategory, fixture_cases_by_category
from e2r.models import Evidence, Instrument, Market, SectorRegime, SourceTier, Stage, StageSnapshot
from e2r.scoring import DeterministicScorer, ScoringPayload


def stage2_payload():
    return ScoringPayload(
        symbol="KR-STAGE2",
        as_of_date=date(2024, 1, 6),
        components={
            "eps_fcf_explosion": 14,
            "earnings_visibility": 13,
            "bottleneck_pricing": 12,
            "market_mispricing": 9,
            "valuation_rerating": 9,
            "capital_allocation": 4,
            "information_confidence": 4,
        },
        diagnostic_scores={"revision_score": 45, "price_stage_score": 60},
        evidence_ids=("KR-STAGE2-numbers",),
    )


def stage2_evidence():
    timestamp = datetime(2024, 1, 6, 8, 0)
    return Evidence(
        evidence_id="KR-STAGE2-numbers",
        source_type="research_report",
        source_name="MockBroker",
        source_tier=SourceTier.TIER_1,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=date(2024, 1, 6),
        market=Market.KR,
        symbol="KR-STAGE2",
        title="Stage 2 fixture evidence",
    )


class MorningBriefingTests(unittest.TestCase):
    def test_korean_morning_briefing_renders_required_sections(self):
        connector = MockDataConnector.from_fixture_cases()
        stage2_score = DeterministicScorer().score(stage2_payload())
        stage2_stage = StageSnapshot(
            symbol="KR-STAGE2",
            as_of_date=date(2024, 1, 6),
            stage=Stage.STAGE_2,
            previous_stage=Stage.STAGE_1,
            stage_changed=True,
            stage_reason=("candidate threshold was met with required score components",),
            red_team_status="low",
            evidence_ids=("KR-STAGE2-numbers",),
        )
        stage2_instrument = Instrument(
            symbol="KR-STAGE2",
            name="Synthetic Stage2",
            market=Market.KR,
            exchange="KRX",
            sector_custom="synthetic",
            listed_date=date(2024, 1, 1),
        )

        green_case = fixture_cases_by_category(FixtureCategory.POWER_EQUIPMENT_SUCCESS)[0]
        boom_case = fixture_cases_by_category(FixtureCategory.US_BOOM_BUST)[0]
        peak_case = fixture_cases_by_category(FixtureCategory.PEAK_OUT_AFTER_SUCCESS)[0]
        cases = (green_case, boom_case, peak_case)
        instruments = list(connector.list_instruments(Market.KR, date(2024, 1, 11)))
        instruments.extend(connector.list_instruments(Market.US, date(2024, 1, 11)))
        instruments.append(stage2_instrument)

        brief = generate_morning_briefing(
            as_of_date=date(2024, 1, 11),
            instruments=tuple(instruments),
            scores=(stage2_score,) + tuple(case.score() for case in cases),
            stages=(stage2_stage,) + tuple(case.classify() for case in cases),
            red_team_findings=tuple(
                finding
                for case in cases
                for finding in case.red_team_assessment().findings
            ),
            backtests=tuple(case.backtest() for case in cases),
            evidence=(stage2_evidence(),) + tuple(evidence for case in cases for evidence in case.evidence),
            sector_regimes=(
                SectorRegime(
                    sector="synthetic_grid",
                    date=date(2024, 1, 11),
                    as_of_date=date(2024, 1, 11),
                    theme_regime_score=82,
                    official_data_confirmation=70,
                    sector_relative_strength=64,
                ),
            ),
            scheduled_events=(
                ScheduledEvent(
                    event_date=date(2024, 1, 11),
                    title="fixture report check",
                    event_type="report",
                    symbol="KR-STAGE2",
                    source="fixture-calendar",
                    as_of_date=date(2024, 1, 11),
                ),
            ),
        )

        self.assertIn("[E2R Morning Brief / 2024-01-11]", brief.text)
        self.assertIn("1. 신규 Stage 2 후보", brief.text)
        self.assertIn("2. Stage 3-Green / Yellow / Red 변화", brief.text)
        self.assertIn("3. Stage 4A / 4B / 4C 변화", brief.text)
        self.assertIn("4. Red Team thesis-break 감시", brief.text)
        self.assertIn("5. 섹터 레짐 변화", brief.text)
        self.assertIn("6. 오늘 확인할 공시, 실적, 리포트 일정", brief.text)
        self.assertIn("Synthetic Stage2 / KR-STAGE2 / KR / synthetic", brief.text)
        self.assertIn("근거:", brief.text)
        self.assertIn("as_of 2024-01-06", brief.text)
        self.assertIn("PreRunUp252D", brief.text)
        self.assertIn("논리 훼손 위험 증가", brief.text)
        self.assertIn("fixture report check", brief.text)

    def test_briefing_output_omits_disallowed_terms(self):
        case = FIXTURE_CASES[0]
        connector = MockDataConnector.from_fixture_cases((case,))

        brief = generate_morning_briefing(
            as_of_date=case.scoring_payload.as_of_date,
            instruments=connector.list_instruments(case.market, case.scoring_payload.as_of_date),
            scores=(case.score(),),
            stages=(case.classify(),),
            evidence=case.evidence,
        )

        for term in ("매" + "수", "매" + "도", "비중 " + "축소", "오늘 " + "사야 함", "b" + "uy", "s" + "ell"):
            self.assertNotIn(term, brief.text.lower())

    def test_briefing_rejects_disallowed_terms(self):
        with self.assertRaisesRegex(ValueError, "disallowed recommendation wording"):
            MorningBrief(as_of_date=date(2024, 1, 1), text="금지 표현: " + "매" + "수")


if __name__ == "__main__":
    unittest.main()

