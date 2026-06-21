from dataclasses import replace
from datetime import date, datetime
import math
from pathlib import Path
import unittest

from e2r.agentic import claim_backed_parsed_fields
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


def claim_backed_agent_fields(raw_fields, *, as_of_date, archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY"):
    return claim_backed_parsed_fields(
        evidence_id=f"agent-fixture:CASE:{as_of_date.isoformat()}:{archetype_id}",
        symbol="CASE",
        as_of_date=as_of_date,
        parsed_fields=raw_fields,
        archetype_id=archetype_id,
        subject="CASE",
        quote_text="source-backed agent fixture fields",
        source_tier=2,
        confidence=0.9,
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

    def test_bottleneck_diagnostics_expose_formula_path(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "capa_utilization_pct": 100,
                    "capa_locked_years": 3,
                    "asp_yoy_pct": 30,
                    "pricing_power_confirmed": True,
                    "shortage_type": "structural",
                    "structural_shortage_mentioned": True,
                }
            )
        )
        score = result.score()
        diagnostics = score.diagnostic_scores

        self.assertIn("bottleneck_industrial_raw", diagnostics)
        self.assertIn("bottleneck_sector_raw", diagnostics)
        self.assertIn("bottleneck_selected_raw", diagnostics)
        self.assertIn(
            result.source_fields["bottleneck_selected_path"],
            {"industrial", "sector", "actual_conversion_bridge", "validated_conversion_bridge"},
        )
        self.assertAlmostEqual(
            diagnostics["bottleneck_component_before_one_off_penalty"],
            diagnostics["bottleneck_selected_raw"] / 100.0 * 20.0,
            places=4,
        )
        self.assertEqual(diagnostics["bottleneck_raw_required_for_green"], 75.0)
        self.assertGreaterEqual(diagnostics["bottleneck_raw_deficit_to_green"], 0.0)

    def test_non_finite_parsed_field_numbers_are_ignored(self):
        baseline = DeterministicFeatureEngineer().engineer(base_input({})).score()
        polluted = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "actual_op_yoy_pct": "nan",
                    "actual_eps_yoy_pct": float("nan"),
                    "actual_sales_yoy_pct": float("inf"),
                    "opm_expansion_pctp": "nan",
                    "capa_utilization_pct": "nan",
                    "asp_yoy_pct": float("inf"),
                    "contract_duration_months": "nan",
                    "order_backlog_to_sales": float("nan"),
                    "eps_revision_1m": "nan",
                }
            )
        ).score()

        self.assertEqual(polluted.total_score, baseline.total_score)
        self.assertEqual(polluted.eps_fcf_explosion_score, baseline.eps_fcf_explosion_score)
        self.assertEqual(polluted.bottleneck_pricing_score, baseline.bottleneck_pricing_score)
        self.assertTrue(all(math.isfinite(float(value)) for value in polluted.diagnostic_scores.values()))

    def test_cross_archetype_bridge_diagnostics_are_exposed(self):
        baseline = DeterministicFeatureEngineer().engineer(base_input({})).score()
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "high_margin_mix_improvement": True,
                    "customer_preorder_or_allocation": True,
                    "record_backlog": True,
                    "multi_year_contract": True,
                    "capital_return_execution": True,
                    "treasury_share_cancellation": True,
                    "csm_growth_visible": True,
                    "k_ics_ratio": 245,
                    "regulatory_approval_confirmed": True,
                    "approval_to_revenue_bridge": True,
                    "royalty_route": True,
                    "arr_growth_visible": True,
                    "retention_or_renewal": True,
                    "sell_through_confirmed": True,
                    "repeat_order_confirmed": True,
                    "binary_event_unresolved": True,
                }
            )
        )
        score = result.score()
        diagnostics = score.diagnostic_scores

        self.assertGreaterEqual(diagnostics["research_axis_bridge_present_count_capped"], 8)
        self.assertEqual(diagnostics["research_axis_bridge_margin"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_valuation_repricing"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_capital_return"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_insurance_quality"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_bio_commercialization"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_software_retention"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_consumer_sell_through"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_guard_risk"], 100.0)
        self.assertGreater(score.capital_allocation_score, baseline.capital_allocation_score)
        self.assertGreater(result.industrial_sub_scores.backlog_rpo_visibility, 0)

    def test_cross_archetype_guard_risk_adds_penalty(self):
        baseline = DeterministicFeatureEngineer().engineer(base_input({"market_frame_shift": True})).score()
        guarded = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "market_frame_shift": True,
                    "binary_event_unresolved": True,
                    "approval_not_confirmed": True,
                    "capital_return_unconfirmed": True,
                    "insurance_rate_cycle_beta_only": True,
                    "reserve_quality_unconfirmed": True,
                    "political_theme_risk": True,
                }
            )
        ).score()

        self.assertEqual(guarded.diagnostic_scores["research_axis_bridge_guard_risk"], 100.0)
        self.assertGreater(guarded.diagnostic_scores["research_axis_bridge_guard_risk_penalty_points"], 0)
        self.assertGreater(guarded.risk_penalty, baseline.risk_penalty)
        self.assertLess(guarded.total_score, baseline.total_score)

    def test_generic_contract_backlog_customer_bridge_scores_without_name_or_hbm_bonus(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "customer_contract_visible": True,
                    "supply_agreement_visible": True,
                    "named_customer_quality": True,
                    "customer_preorder_or_allocation": True,
                    "multi_year_contract": True,
                    "prepayment_exists": True,
                    "take_or_pay": True,
                    "minimum_revenue_guarantee": True,
                    "revenue_visibility_contract": True,
                    "delivery_schedule": True,
                    "order_to_revenue_bridge": True,
                    "book_to_bill_visible": True,
                    "capacity_precommitted": True,
                    "booked_out_capacity": True,
                    "order_slot_locked": True,
                    "pricing_power_mentioned": True,
                }
            )
        )
        score = result.score()
        diagnostics = score.diagnostic_scores

        self.assertGreaterEqual(result.industrial_sub_scores.contract_quality, 80)
        self.assertGreaterEqual(result.industrial_sub_scores.backlog_rpo_visibility, 80)
        self.assertGreaterEqual(result.industrial_sub_scores.capa_constraint, 20)
        self.assertEqual(diagnostics["research_axis_bridge_customer"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_backlog"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_contract"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_capacity"], 100.0)
        self.assertGreater(score.earnings_visibility_score, 0)
        self.assertGreater(score.bottleneck_pricing_score, 0)

    def test_customer_preorder_feeds_backlog_and_contract_bridge_without_hbm_name(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "customer_preorder_or_allocation": True,
                    "confirmed_order": True,
                    "revenue_visibility_contract": True,
                    "delivery_schedule": True,
                }
            )
        )
        diagnostics = result.score().diagnostic_scores

        self.assertEqual(diagnostics["research_axis_bridge_customer"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_backlog"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_contract"], 100.0)
        self.assertGreater(result.industrial_sub_scores.contract_quality, 0)
        self.assertGreater(result.industrial_sub_scores.backlog_rpo_visibility, 0)

    def test_customer_allocation_plus_capacity_constraint_scores_without_hbm_name(self):
        baseline = DeterministicFeatureEngineer().engineer(base_input({}))
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "customer_preorder_or_allocation": True,
                    "capacity_constraint": True,
                    "supply_shortage_mentioned": True,
                    "pricing_power_mentioned": True,
                }
            )
        )

        self.assertGreater(result.industrial_sub_scores.contract_quality, baseline.industrial_sub_scores.contract_quality)
        self.assertGreater(result.industrial_sub_scores.backlog_rpo_visibility, baseline.industrial_sub_scores.backlog_rpo_visibility)
        self.assertGreater(result.industrial_sub_scores.capa_constraint, baseline.industrial_sub_scores.capa_constraint)
        self.assertGreater(result.score().bottleneck_pricing_score, baseline.score().bottleneck_pricing_score)

    def test_validated_conversion_bridge_lifts_bottleneck_without_hbm_name(self):
        result = DeterministicFeatureEngineer().engineer(
            replace(
                base_input(
                    {
                        "financial_actuals_present": True,
                        "actual_op_yoy_pct": 180,
                        "actual_eps_yoy_pct": 180,
                        "actual_sales_yoy_pct": 70,
                        "opm_expansion_pctp": 14,
                        "customer_preorder_or_allocation": True,
                        "capacity_constraint": True,
                        "supply_shortage_mentioned": True,
                        "structural_shortage_mentioned": True,
                        "pricing_power_mentioned": True,
                        "recurring_consumer_demand": True,
                        "repeat_order_confirmed": True,
                        "sell_through_confirmed": True,
                        "export_channel_expansion": True,
                        "overseas_channel_expansion": True,
                        "high_margin_mix_improvement": True,
                        "customer_contract_visible": True,
                        "named_customer_quality": True,
                        "record_backlog": True,
                        "delivery_schedule": True,
                        "order_to_revenue_bridge": True,
                        "margin_bridge_visible": True,
                        "operating_leverage_visible": True,
                        "market_frame_shift": True,
                    }
                ),
                canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
            )
        )
        diagnostics = result.score().diagnostic_scores

        self.assertIn(
            result.source_fields["bottleneck_selected_path"],
            {"validated_conversion_bridge", "source_backed_green_bridge"},
        )
        self.assertGreaterEqual(diagnostics["bottleneck_validated_conversion_raw"], 92.0)
        self.assertGreaterEqual(diagnostics["bottleneck_selected_raw"], 92.0)

    def test_validated_conversion_bridge_generalizes_across_non_hbm_archetypes(self):
        cases = {
            "C02_POWER_GRID_DATACENTER_CAPEX": (
                "POWER_EQUIPMENT",
                {
                    "financial_actuals_present": True,
                    "actual_op_yoy_pct": 180,
                    "actual_eps_yoy_pct": 160,
                    "actual_sales_yoy_pct": 80,
                    "opm_expansion_pctp": 12,
                    "customer_contract_visible": True,
                    "multi_year_contract": True,
                    "record_backlog": True,
                    "delivery_schedule": True,
                    "order_to_revenue_bridge": True,
                    "lead_time_extended": True,
                    "supply_shortage_mentioned": True,
                    "structural_shortage_mentioned": True,
                    "capacity_constraint": True,
                    "pricing_power_mentioned": True,
                    "market_frame_shift": True,
                },
            ),
            "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": (
                "FINANCIAL_CAPITAL_RETURN",
                {
                    "financial_actuals_present": True,
                    "actual_op_yoy_pct": 120,
                    "actual_eps_yoy_pct": 120,
                    "actual_sales_yoy_pct": 30,
                    "opm_expansion_pctp": 8,
                    "roe": 12,
                    "pbr_e": 0.8,
                    "capital_return_execution": True,
                    "treasury_share_cancellation": True,
                    "shareholder_return_execution": True,
                    "dividend_visibility": True,
                    "credit_cost_quality": True,
                    "market_frame_shift": True,
                },
            ),
            "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION": (
                "BIO_COMMERCIALIZATION",
                {
                    "financial_actuals_present": True,
                    "actual_op_yoy_pct": 120,
                    "actual_eps_yoy_pct": 120,
                    "actual_sales_yoy_pct": 70,
                    "opm_expansion_pctp": 10,
                    "regulatory_approval_confirmed": True,
                    "approval_to_revenue_bridge": True,
                    "royalty_route": True,
                    "partner_economics_visible": True,
                    "reimbursement_confirmed": True,
                    "market_frame_shift": True,
                },
            ),
            "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": (
                "SOFTWARE_SECURITY",
                {
                    "financial_actuals_present": True,
                    "actual_op_yoy_pct": 120,
                    "actual_eps_yoy_pct": 120,
                    "actual_sales_yoy_pct": 70,
                    "opm_expansion_pctp": 10,
                    "arr_growth_pct": 45,
                    "arr_growth_visible": True,
                    "nrr": 125,
                    "retention_or_renewal": True,
                    "contract_renewal_visible": True,
                    "seat_expansion_visible": True,
                    "recurring_margin_leverage": True,
                    "operating_leverage_visible": True,
                    "market_frame_shift": True,
                },
            ),
        }

        for canonical_archetype_id, (expected_profile, fields) in cases.items():
            with self.subTest(canonical_archetype_id=canonical_archetype_id):
                self.assertNotIn("HBM", canonical_archetype_id)
                self.assertFalse(any("hbm" in key.lower() for key in fields))
                result = DeterministicFeatureEngineer().engineer(
                    replace(base_input(fields), canonical_archetype_id=canonical_archetype_id)
                )
                diagnostics = result.score().diagnostic_scores

                self.assertEqual(result.source_fields["sector_profile"], expected_profile)
                self.assertIn(
                    result.source_fields["bottleneck_selected_path"],
                    {"validated_conversion_bridge", "source_backed_green_bridge"},
                )
                self.assertGreater(diagnostics["bottleneck_validated_conversion_raw"], 0.0)
                self.assertGreater(
                    diagnostics["bottleneck_validated_conversion_raw"],
                    diagnostics["bottleneck_actual_conversion_raw"],
                )
                self.assertEqual(diagnostics["research_axis_bridge_guard_risk"], 0.0)

    def test_guard_risk_blocks_validated_conversion_bridge(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "financial_actuals_present": True,
                    "actual_op_yoy_pct": 180,
                    "actual_eps_yoy_pct": 180,
                    "actual_sales_yoy_pct": 70,
                    "opm_expansion_pctp": 14,
                    "customer_preorder_or_allocation": True,
                    "capacity_constraint": True,
                    "supply_shortage_mentioned": True,
                    "pricing_power_mentioned": True,
                    "record_backlog": True,
                    "delivery_schedule": True,
                    "order_to_revenue_bridge": True,
                    "market_frame_shift": True,
                    "price_only_blowoff": True,
                }
            )
        )
        diagnostics = result.score().diagnostic_scores

        self.assertEqual(diagnostics["bottleneck_validated_conversion_raw"], 0.0)
        self.assertNotEqual(result.source_fields["bottleneck_selected_path"], "validated_conversion_bridge")

    def test_capa_increase_alias_and_absolute_backlog_feed_common_scores(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "backlog": 1800,
                    "fy1_sales": 1000,
                    "capa_increase_pct": 40,
                    "pricing_power_mentioned": True,
                }
            )
        )

        self.assertGreaterEqual(result.industrial_sub_scores.backlog_rpo_visibility, 70)
        self.assertGreater(result.industrial_sub_scores.capa_constraint, 0)
        self.assertGreater(result.score().capital_allocation_score, 0)

    def test_consumer_distribution_bridge_scores_without_brand_name_special_case(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "platform_distribution_scale": True,
                    "brand_channel_expansion": True,
                    "export_channel_expansion": True,
                    "overseas_channel_expansion": True,
                    "export_growth_pct": 70,
                    "repeat_order_confirmed": True,
                    "high_margin_mix_improvement": True,
                }
            )
        )
        diagnostics = result.score().diagnostic_scores

        self.assertEqual(diagnostics["research_axis_bridge_customer"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_consumer_sell_through"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_margin"], 100.0)
        self.assertGreater(diagnostics["export_channel_visibility"], 0)
        self.assertGreater(diagnostics["recurring_demand_visibility"], 0)

    def test_consumer_channel_margin_can_use_actual_conversion_bridge(self):
        result = DeterministicFeatureEngineer().engineer(
            replace(
                base_input(
                    {
                        "export_channel_expansion": True,
                        "repeat_order_confirmed": True,
                        "channel_reorder_confirmed": True,
                        "high_margin_mix_improvement": True,
                        "pricing_power_mentioned": True,
                    }
                ),
                canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
            )
        )
        diagnostics = result.score().diagnostic_scores

        self.assertEqual(result.source_fields["inferred_sector_profile"], "GENERIC")
        self.assertEqual(result.source_fields["sector_profile"], "K_BEAUTY_EXPORT")
        self.assertEqual(result.source_fields["sector_profile_resolution"], "explicit_canonical_profile_override")
        self.assertGreater(diagnostics["actual_profit_conversion_score"], 0)
        self.assertGreater(diagnostics["bottleneck_actual_conversion_raw"], 0)
        self.assertEqual(diagnostics["research_axis_bridge_consumer_sell_through"], 100.0)

    def test_domain_evidence_score_is_not_diluted_when_alias_inventory_expands(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "hbm_demand_mentioned": True,
                    "memory_price_increase_mentioned": True,
                    "customer_preorder_or_allocation": True,
                    "hbm_capacity_constraint": True,
                }
            )
        )

        self.assertEqual(result.score().diagnostic_scores["domain_specific_evidence_score"], 80.0)

    def test_memory_recovery_cycle_feeds_customer_and_backlog_without_contract_axis(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "hbm_demand_mentioned": True,
                    "memory_price_increase_mentioned": True,
                    "pricing_power_mentioned": True,
                    "supply_discipline_mentioned": True,
                    "cycle_demand_visibility": True,
                    "end_market_demand_visibility": True,
                    "supply_demand_tightness": True,
                    "cycle_to_revenue_bridge": True,
                    "advanced_packaging_bottleneck": True,
                }
            )
        )
        diagnostics = result.score().diagnostic_scores

        self.assertEqual(diagnostics["research_axis_bridge_customer"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_backlog"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_capacity"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_contract"], 0.0)
        self.assertGreaterEqual(diagnostics["domain_specific_evidence_score"], 80.0)
        self.assertGreater(result.industrial_sub_scores.backlog_rpo_visibility, 0)
        self.assertEqual(result.industrial_sub_scores.contract_quality, 0.0)

    def test_price_only_theme_hype_is_guard_not_positive_bridge(self):
        baseline = DeterministicFeatureEngineer().engineer(base_input({"market_frame_shift": True})).score()
        guarded = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "market_frame_shift": True,
                    "price_only_blowoff": True,
                    "theme_hype_without_revenue": True,
                    "missing_cashflow_bridge": True,
                    "source_quality_conflict": True,
                }
            )
        ).score()

        self.assertEqual(guarded.diagnostic_scores["research_axis_bridge_guard_risk"], 100.0)
        self.assertEqual(guarded.diagnostic_scores["price_only_blowoff_score"], 100.0)
        self.assertGreater(guarded.diagnostic_scores["research_axis_bridge_guard_risk_penalty_points"], 0)
        self.assertGreater(guarded.risk_penalty, baseline.risk_penalty)
        self.assertLess(guarded.total_score, baseline.total_score)

    def test_operating_and_capex_risk_aliases_feed_guard_penalty(self):
        baseline = DeterministicFeatureEngineer().engineer(base_input({"market_frame_shift": True})).score()
        guarded = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "market_frame_shift": True,
                    "receivables_inventory_spike": True,
                    "customer_capex_decline": True,
                    "contract_cancelled_or_delayed": True,
                    "capex_burden_risk": True,
                }
            )
        ).score()

        self.assertEqual(guarded.diagnostic_scores["research_axis_bridge_guard_risk"], 100.0)
        self.assertGreater(guarded.diagnostic_scores["research_axis_bridge_guard_risk_penalty_points"], 0)
        self.assertGreater(guarded.risk_penalty, baseline.risk_penalty)

    def test_policy_material_software_and_redteam_aliases_feed_common_bridge_axes(self):
        result = DeterministicFeatureEngineer().engineer(
            base_input(
                {
                    "policy_or_regulatory_confirmed": True,
                    "project_award_confirmed": True,
                    "direct_company_cash_route": True,
                    "subsidy_capture_visible": True,
                    "implementation_timeline": True,
                    "spread_expansion": True,
                    "ex_credit_margin": True,
                    "utilization_rate": True,
                    "pf_exposure_reduced": True,
                    "balance_sheet_repair": True,
                    "cash_collection_visible": True,
                    "arpu_growth_pct": 12,
                    "ad_revenue_growth_pct": 18,
                    "take_rate_improvement": True,
                    "ip_monetization_visible": True,
                    "repeat_revenue": True,
                    "user_retention": True,
                    "valuation_overheat": True,
                    "evidence_source_quality": True,
                    "thesis_break_confirmed": True,
                }
            )
        )
        score = result.score()
        diagnostics = score.diagnostic_scores

        self.assertEqual(diagnostics["research_axis_bridge_policy_cash_route"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_margin"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_capacity"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_capital_return"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_software_retention"], 100.0)
        self.assertEqual(diagnostics["research_axis_bridge_guard_risk"], 100.0)
        self.assertEqual(diagnostics["theme_overheat_score"], 100.0)
        self.assertGreater(diagnostics["research_axis_bridge_guard_risk_penalty_points"], 0)

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
                agent_extracted_fields=claim_backed_agent_fields(
                    {
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
                    as_of_date=as_of_date,
                ),
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

    def test_unbacked_agent_extracted_fields_do_not_create_claim_backed_score(self):
        as_of_date = date(2026, 6, 9)
        raw_agent_fields = {
            "contract_duration_months": 48,
            "contract_amount_to_prior_sales": 0.6,
            "order_backlog_to_sales": 1.5,
            "capa_utilization_pct": 96,
            "lead_time_months": 18,
            "asp_yoy_pct": 30,
            "target_multiple_delta": 6,
            "hbm_demand_mentioned": True,
            "memory_price_increase_mentioned": True,
            "customer_preorder_or_allocation": True,
            "hbm_capacity_constraint": True,
            "capacity_precommitted": True,
            "hbm_capacity_pre_sold": True,
            "multi_year_contract": True,
            "pricing_power_mentioned": True,
            "market_frame_shift": True,
        }
        unbacked = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                agent_extracted_fields=raw_agent_fields,
            )
        )
        baseline = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )
        backed = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                agent_extracted_fields=claim_backed_agent_fields(raw_agent_fields, as_of_date=as_of_date),
            )
        )

        unbacked_score = unbacked.score()
        baseline_score = baseline.score()
        backed_score = backed.score()

        self.assertEqual(unbacked_score.total_score, baseline_score.total_score)
        self.assertEqual(unbacked_score.diagnostic_scores["contract_quality"], 0.0)
        self.assertEqual(unbacked_score.diagnostic_scores["capa_constraint"], 0.0)
        self.assertEqual(unbacked_score.diagnostic_scores["asp_pricing_power"], 0.0)
        self.assertEqual(unbacked_score.diagnostic_scores["claim_backed_claim_count_capped"], 0.0)
        self.assertEqual(unbacked_score.diagnostic_scores["evidence_contract_present_primitive_count_capped"], 0.0)
        self.assertEqual(unbacked.payload.score_contribution_claim_ids, {})
        self.assertNotIn("hbm_capacity_pre_sold", unbacked.source_fields["evidence_contract_present_primitives"])
        self.assertGreater(backed_score.diagnostic_scores["claim_backed_claim_count_capped"], 0.0)
        self.assertGreater(backed_score.total_score, unbacked_score.total_score)
        self.assertIn("hbm_capacity_pre_sold", backed.source_fields["evidence_contract_present_primitives"])

    def test_unbacked_agent_extracted_fields_do_not_route_archetype_from_text(self):
        as_of_date = date(2026, 6, 9)
        raw_agent_fields = {
            "hbm_demand_mentioned": True,
            "customer_preorder_or_allocation": True,
            "hbm_capacity_pre_sold": True,
            "market_frame_shift": True,
        }
        baseline = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(symbol="CASE", as_of_date=as_of_date)
        )
        unbacked = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="CASE",
                as_of_date=as_of_date,
                agent_extracted_fields=raw_agent_fields,
            )
        )

        self.assertEqual(unbacked.source_fields["canonical_archetype_id"], baseline.source_fields["canonical_archetype_id"])
        self.assertEqual(unbacked.source_fields["large_sector_id"], baseline.source_fields["large_sector_id"])
        self.assertEqual(unbacked.score().total_score, baseline.score().total_score)

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
            "explicit_canonical_archetype_corrected_large_sector_mismatch",
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
