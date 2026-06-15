from dataclasses import replace
from datetime import date, datetime
from pathlib import Path
import unittest

from e2r.connectors import CSVJSONDataConnector
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, engineer_score_from_connector
from e2r.models import ConsensusRevision, ConsensusSnapshot, FinancialActual, NewsItem, PriceBar, ResearchReport, ShortageType, Stage
from e2r.red_team import RedTeamEngine
from e2r.staging import StageClassificationInput, StageClassifier


def make_bar(day, low, high, close):
    bar_date = date(2024, 1, day)
    return PriceBar(
        symbol="CASE",
        date=bar_date,
        open=close,
        high=high,
        low=low,
        close=close,
        adj_close=close,
        volume=1000,
        trading_value=close * 1000,
        market_cap=1000000000.0,
        source="feature-test",
        as_of_date=bar_date,
    )


def base_input(parsed_fields):
    as_of_date = date(2024, 1, 6)
    return FeatureEngineeringInput(
        symbol="CASE",
        as_of_date=as_of_date,
        price_bars=(
            make_bar(1, 50, 60, 55),
            make_bar(6, 95, 120, 110),
        ),
        financial_actuals=(
            FinancialActual(
                symbol="CASE",
                fiscal_year=2023,
                fiscal_quarter=None,
                period_end=date(2023, 12, 31),
                reported_at=datetime(2024, 1, 3, 8, 0),
                as_of_date=as_of_date,
                source="test",
                sales=1000,
                operating_profit=100,
                net_income=80,
                eps=100,
                cashflow_from_operations=90,
                fcf=80,
            ),
        ),
        consensus=(
            ConsensusSnapshot(
                symbol="CASE",
                date=as_of_date,
                fiscal_year=2024,
                as_of_date=as_of_date,
                source="test",
                sales_e=1800,
                op_e=500,
                net_income_e=400,
                eps_e=500,
                per_e=12,
                pbr_e=1.5,
                analyst_count=4,
            ),
        ),
        consensus_revisions=(
            ConsensusRevision(
                symbol="CASE",
                date=as_of_date,
                fiscal_year=2024,
                as_of_date=as_of_date,
                eps_revision_1m=35,
                op_revision_1m=40,
                fcf_revision_1m=25,
                target_price_revision_1m=30,
            ),
        ),
        research_reports=(
            ResearchReport(
                symbol="CASE",
                publish_date=as_of_date,
                broker="TestBroker",
                title="feature test report",
                as_of_date=as_of_date,
                target_revision_pct=30,
                target_multiple_before=10,
                target_multiple_after=14,
                est_per=12,
                parsed_fields=parsed_fields,
            ),
        ),
    )


class FeatureEngineeringTests(unittest.TestCase):
    def test_structural_shortage_beats_one_off_shortage(self):
        common = {
            "contract_duration_months": 48,
            "contract_amount_to_prior_sales": 0.35,
            "prepayment_exists": True,
            "non_cancellable": True,
            "order_backlog_to_sales": 1.4,
            "capa_utilization_pct": 96,
            "lead_time_months": 14,
            "asp_yoy_pct": 18,
            "pricing_power_confirmed": True,
        }

        structural = DeterministicFeatureEngineer().engineer(
            base_input({**common, "shortage_type": "structural", "one_off_shortage_risk": 10})
        )
        one_off = DeterministicFeatureEngineer().engineer(
            base_input({**common, "shortage_type": "one_off", "one_off_shortage_risk": 90})
        )

        self.assertEqual(structural.shortage_type, ShortageType.STRUCTURAL)
        self.assertEqual(one_off.shortage_type, ShortageType.ONE_OFF)
        self.assertGreater(
            structural.industrial_sub_scores.structural_shortage,
            one_off.industrial_sub_scores.structural_shortage,
        )
        self.assertLess(
            structural.industrial_sub_scores.one_off_shortage_risk,
            one_off.industrial_sub_scores.one_off_shortage_risk,
        )

    def test_strong_eps_with_weak_contract_quality_is_not_stage_3_green(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "contract_duration_months": 24,
                    "contract_amount_to_prior_sales": 0.20,
                    "order_backlog_to_sales": 2.0,
                    "rpo_to_sales": 1.7,
                    "backlog_yoy_pct": 80,
                    "record_backlog": True,
                    "capa_utilization_pct": 100,
                    "capa_expansion_pct": 80,
                    "capa_locked_years": 3,
                    "lead_time_months": 18,
                    "asp_yoy_pct": 30,
                    "high_margin_mix_pct": 80,
                    "pricing_power_confirmed": True,
                    "market_frame_shift": True,
                    "capacity_precommitted": True,
                    "shortage_type": "unknown",
                    "one_off_shortage_risk": 20,
                }
            )
        )
        score = result.score()
        stage = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                red_team=RedTeamEngine().assess(result.red_team_signals),
            )
        )

        self.assertGreaterEqual(score.eps_fcf_explosion_score, 17)
        self.assertLess(score.diagnostic_scores["contract_quality"], 25)
        self.assertIn(stage.stage, {Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED})

    def test_minimum_revenue_guarantee_contributes_to_visibility_without_backlog_ratio(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "minimum_revenue_guarantee": True,
                    "revenue_visibility_contract": True,
                    "prepayment_exists": True,
                    "multi_year_contract": True,
                    "hbm_demand_mentioned": True,
                }
            )
        )

        self.assertGreater(result.industrial_sub_scores.backlog_rpo_visibility, 0)
        self.assertGreater(result.score().earnings_visibility_score, 0)

    def test_actual_yoy_financials_contribute_without_consensus_proxy(self):
        as_of_date = date(2024, 5, 1)
        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                price_bars=(
                    PriceBar(
                        symbol="CASE",
                        date=date(2024, 4, 30),
                        open=100,
                        high=110,
                        low=95,
                        close=105,
                        adj_close=105,
                        volume=1000,
                        trading_value=105000,
                        market_cap=3000,
                        source="test",
                        as_of_date=as_of_date,
                    ),
                ),
                financial_actuals=(
                    FinancialActual(
                        symbol="CASE",
                        fiscal_year=2023,
                        fiscal_quarter=1,
                        period_end=date(2023, 3, 31),
                        reported_at=datetime(2023, 4, 30, 8, 0),
                        as_of_date=date(2023, 4, 30),
                        source="test",
                        sales=1000,
                        operating_profit=100,
                        net_income=80,
                        eps=100,
                        opm=10,
                        fcf=70,
                    ),
                    FinancialActual(
                        symbol="CASE",
                        fiscal_year=2024,
                        fiscal_quarter=1,
                        period_end=date(2024, 3, 31),
                        reported_at=datetime(2024, 4, 30, 8, 0),
                        as_of_date=as_of_date,
                        source="test",
                        sales=1600,
                        operating_profit=300,
                        net_income=240,
                        eps=260,
                        opm=18,
                        capex=240,
                        fcf=200,
                    ),
                ),
                agent_extracted_fields={
                    "hbm_demand_mentioned": True,
                    "memory_price_increase_mentioned": True,
                    "pricing_power_mentioned": True,
                },
            )
        )
        score = result.score()

        self.assertGreater(score.eps_fcf_explosion_score, 0)
        self.assertGreater(score.diagnostic_scores["medium_term_revision_visibility"], 0)
        self.assertGreater(score.capital_allocation_score, 0)
        self.assertEqual(score.diagnostic_scores["evidence_family_financial_actual"], 1.0)

    def test_actual_conversion_bridge_lifts_structural_hbm_case_without_consensus(self):
        as_of_date = date(2026, 6, 9)
        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                price_bars=(
                    PriceBar(
                        symbol="CASE",
                        date=date(2026, 6, 8),
                        open=100,
                        high=115,
                        low=95,
                        close=110,
                        adj_close=110,
                        volume=1000,
                        trading_value=110000,
                        market_cap=5000,
                        source="test",
                        as_of_date=as_of_date,
                    ),
                ),
                financial_actuals=(
                    FinancialActual(
                        symbol="CASE",
                        fiscal_year=2025,
                        fiscal_quarter=1,
                        period_end=date(2025, 3, 31),
                        reported_at=datetime(2025, 5, 15, 8, 0),
                        as_of_date=date(2025, 5, 15),
                        source="test",
                        sales=1000,
                        operating_profit=100,
                        net_income=80,
                        eps=100,
                        opm=10,
                        fcf=70,
                        equity=1000,
                    ),
                    FinancialActual(
                        symbol="CASE",
                        fiscal_year=2026,
                        fiscal_quarter=1,
                        period_end=date(2026, 3, 31),
                        reported_at=datetime(2026, 5, 15, 8, 0),
                        as_of_date=as_of_date,
                        source="test",
                        sales=2500,
                        operating_profit=1000,
                        net_income=800,
                        eps=800,
                        opm=40,
                        fcf=600,
                        capex=250,
                        equity=1200,
                    ),
                ),
                agent_extracted_fields={
                    "hbm_demand_mentioned": True,
                    "memory_price_increase_mentioned": True,
                    "customer_preorder_or_allocation": True,
                    "hbm_capacity_constraint": True,
                    "capacity_precommitted": True,
                    "hbm_capacity_pre_sold": True,
                    "multi_year_contract": True,
                    "pricing_power_mentioned": True,
                    "market_frame_shift": True,
                },
            )
        )
        score = result.score()
        stage = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                red_team=RedTeamEngine().assess(result.red_team_signals),
                company_event_score=80,
                high_quality_company_event=True,
            )
        )

        self.assertGreater(score.diagnostic_scores["actual_profit_conversion_score"], 0)
        self.assertGreaterEqual(score.total_score, 65)
        self.assertNotEqual(stage.stage, Stage.STAGE_1)

    def test_actual_equity_feeds_valuation_without_consensus_or_bps(self):
        as_of_date = date(2024, 5, 1)
        price_bars = (
            PriceBar(
                symbol="CASE",
                date=date(2024, 4, 30),
                open=100,
                high=110,
                low=95,
                close=105,
                adj_close=105,
                volume=1000,
                trading_value=105000,
                market_cap=1500,
                source="test",
                as_of_date=as_of_date,
            ),
        )
        base_actual = FinancialActual(
            symbol="CASE",
            fiscal_year=2024,
            fiscal_quarter=1,
            period_end=date(2024, 3, 31),
            reported_at=datetime(2024, 4, 30, 8, 0),
            as_of_date=as_of_date,
            source="test",
            sales=1000,
            operating_profit=None,
            net_income=None,
            equity=None,
        )
        without_equity = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(symbol="CASE", as_of_date=as_of_date, price_bars=price_bars, financial_actuals=(base_actual,))
        )
        with_equity = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                price_bars=price_bars,
                financial_actuals=(replace(base_actual, equity=1000),),
            )
        )

        self.assertGreater(with_equity.score().valuation_rerating_score, without_equity.score().valuation_rerating_score)
        self.assertEqual(with_equity.payload.diagnostic_scores["evidence_family_financial_actual"], 1.0)

    def test_feature_engineering_exposes_fcf_and_valuation_diagnostics_for_gap_expansion(self):
        result = DeterministicFeatureEngineer().engineer(base_input({}))
        score = result.score()

        self.assertIn("fcf_quality_score", score.diagnostic_scores)
        self.assertIn("valuation_score", score.diagnostic_scores)
        self.assertGreater(score.diagnostic_scores["fcf_quality_score"], 0.0)
        self.assertGreater(score.diagnostic_scores["valuation_score"], 0.0)
        self.assertEqual(result.source_fields["fcf_quality_score"], score.diagnostic_scores["fcf_quality_score"])
        self.assertEqual(result.source_fields["valuation_score"], score.diagnostic_scores["valuation_score"])

    def test_quarterly_actual_growth_does_not_compare_against_annual_actual(self):
        actuals = (
            FinancialActual(
                symbol="CASE",
                fiscal_year=2023,
                fiscal_quarter=None,
                period_end=date(2023, 12, 31),
                reported_at=datetime(2024, 3, 31, 8, 0),
                as_of_date=date(2024, 5, 1),
                source="test",
                sales=4000,
                operating_profit=1000,
                fcf=800,
            ),
            FinancialActual(
                symbol="CASE",
                fiscal_year=2024,
                fiscal_quarter=1,
                period_end=date(2024, 3, 31),
                reported_at=datetime(2024, 4, 30, 8, 0),
                as_of_date=date(2024, 5, 1),
                source="test",
                sales=1200,
                operating_profit=400,
                fcf=300,
            ),
        )

        self.assertEqual(DeterministicFeatureEngineer._actual_growths(actuals), {})

    def test_text_financial_fields_and_beat_signal_contribute_to_score(self):
        as_of_date = date(2026, 6, 8)
        result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                price_bars=(
                    PriceBar(
                        symbol="CASE",
                        date=date(2026, 6, 8),
                        open=100,
                        high=110,
                        low=95,
                        close=105,
                        adj_close=105,
                        volume=1000,
                        trading_value=105000,
                        market_cap=3000,
                        source="test",
                        as_of_date=as_of_date,
                    ),
                ),
                news_items=(
                    NewsItem(
                        symbol="CASE",
                        sector="semiconductor",
                        published_at=datetime(2026, 6, 8, 8, 0),
                        source="test-news",
                        title="CASE 2026년 1분기 실적 발표",
                        as_of_date=as_of_date,
                        parsed_fields={
                            "financial_actuals_from_text": True,
                            "financial_actuals_present": True,
                            "actual_sales": 1000,
                            "capex_amount": 120,
                            "actual_op_yoy_pct": 80,
                            "op_yoy_pct": 80,
                            "earnings_beat_mentioned": True,
                            "estimate_upgrade_mentioned": True,
                        },
                    ),
                ),
            )
        )
        score = result.score()

        self.assertGreater(score.eps_fcf_explosion_score, 0)
        self.assertGreater(score.earnings_visibility_score, 0)
        self.assertGreater(score.capital_allocation_score, 0)
        self.assertGreaterEqual(score.diagnostic_scores["revision_score"], 55)

    def test_historical_csv_json_fixture_data_can_produce_score(self):
        root = Path(__file__).resolve().parents[1] / "fixtures" / "historical"
        connector = CSVJSONDataConnector.from_directory(root)

        result = engineer_score_from_connector(
            connector,
            symbol="267260",
            as_of_date=date(2023, 7, 27),
        )
        score = result.score()
        stage = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                red_team=RedTeamEngine().assess(result.red_team_signals),
                theme_regime_score=80,
                company_event_score=80,
            )
        )
        zoom_news = connector.get_news("ZM", date(2020, 1, 1), date(2020, 12, 31), date(2020, 9, 1))

        self.assertGreater(score.total_score, 75)
        self.assertGreater(score.diagnostic_scores["contract_quality"], 0)
        self.assertEqual(result.shortage_type, ShortageType.STRUCTURAL)
        self.assertIn(stage.stage, {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW})
        self.assertTrue(zoom_news)

    def test_unknown_archetype_metadata_is_reclassified_before_scoring(self):
        feature_input = replace(
            base_input(
                {
                    "contract_duration_months": 36,
                    "contract_amount_to_prior_sales": 0.5,
                    "order_backlog_to_sales": 1.4,
                    "lead_time_months": 18,
                    "capa_utilization_pct": 96,
                    "asp_yoy_pct": 15,
                    "pricing_power_confirmed": True,
                    "shortage_type": "structural",
                }
            ),
            sector_context="power_equipment",
            canonical_archetype_id="C00_UNKNOWN",
        )

        result = DeterministicFeatureEngineer().engineer(feature_input)
        score = result.score()

        self.assertEqual(result.source_fields["canonical_archetype_id"], "C02_POWER_GRID_DATACENTER_CAPEX")
        self.assertIn("reclassified_by_agent_context", result.source_fields["archetype_classification_reason"])
        self.assertIn("archetype_weight:C02_POWER_GRID_DATACENTER_CAPEX", score.scoring_version)

    def test_large_sector_mismatch_is_corrected_from_canonical_before_scoring(self):
        feature_input = replace(
            base_input({"export_channel_expansion": True, "recurring_consumer_demand": True}),
            large_sector_id="L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
            canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
        )

        result = DeterministicFeatureEngineer().engineer(feature_input)
        score = result.score()

        self.assertEqual(result.source_fields["large_sector_id"], "L5_CONSUMER_BRAND_DISTRIBUTION")
        self.assertEqual(result.source_fields["canonical_archetype_id"], "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION")
        self.assertEqual(
            result.source_fields["archetype_classification_reason"],
            "explicit_canonical_corrected_large_sector_mismatch",
        )
        self.assertIn("archetype_weight:C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", score.scoring_version)

    def test_feature_input_rejects_future_as_of_financial_actual(self):
        with self.assertRaisesRegex(ValueError, "financial actual cannot be after feature as_of_date"):
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=date(2024, 5, 1),
                financial_actuals=(
                    FinancialActual(
                        symbol="CASE",
                        fiscal_year=2024,
                        fiscal_quarter=1,
                        period_end=date(2024, 3, 31),
                        reported_at=datetime(2024, 4, 30, 8, 0),
                        as_of_date=date(2024, 5, 30),
                        source="future-restatement",
                        sales=999,
                    ),
                ),
            )


if __name__ == "__main__":
    unittest.main()
