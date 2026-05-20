from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round287_r5_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round287_r5_loop14_consumer_retail_brand_price_validation import (
    ROUND287_CASE_CANDIDATES,
    ROUND287_GREEN_FORBIDDEN_PATTERNS,
    ROUND287_GREEN_REQUIRED_FIELDS,
    ROUND287_HARD_4C_GATES,
    ROUND287_LARGE_SECTOR,
    ROUND287_PRICE_VALIDATION_FIELDS,
    ROUND287_REQUIRED_TARGET_ALIASES,
    ROUND287_SCORE_ADJUSTMENTS,
    ROUND287_SHADOW_WEIGHT_ROWS,
    ROUND287_STAGE4B_WATCH_TRIGGERS,
    render_round287_green_gate_review_markdown,
    render_round287_stage4b_4c_review_markdown,
    round287_audit_payload,
    round287_case_records,
    round287_deep_sub_archetype_rows,
    round287_shadow_weight_rows,
    round287_summary,
    write_round287_r5_loop14_reports,
)


class Round287R5Loop14ConsumerRetailBrandPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND287_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND287_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND287_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE"],
            E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE.value,
        )
        self.assertEqual(
            ROUND287_REQUIRED_TARGET_ALIASES["ECOMMERCE_TRUST_BREAK_HARD_REFERENCE"],
            E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_REFERENCE.value,
        )

    def test_archetype_definitions_encode_round287_gates(self) -> None:
        kfood = archetype_definition(E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE)
        food_reg = archetype_definition(E2RArchetype.K_FOOD_EXPORT_REGULATORY_4C_WATCH)
        apr = archetype_definition(E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B)
        kbeauty = archetype_definition(E2RArchetype.K_BEAUTY_US_EXPANSION_STAGE2)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_RETAIL_EVENT_PREMIUM)
        jv = archetype_definition(E2RArchetype.ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE)
        trust = archetype_definition(E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_REFERENCE)
        fulfillment = archetype_definition(E2RArchetype.RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2)
        domestic = archetype_definition(E2RArchetype.DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH)

        self.assertIn("export sell-through", kfood.stage3_high_conviction_signals)
        self.assertIn("spiciness or capsaicin health restriction", food_reg.stage4c_thesis_break_signals)
        self.assertIn("repeat purchase or device replacement cycle", apr.stage3_high_conviction_signals)
        self.assertIn("physical-store sell-through", kbeauty.stage3_high_conviction_signals)
        self.assertIn("tourist spend per head", tourism.stage3_high_conviction_signals)
        self.assertIn("data compliance", jv.stage3_high_conviction_signals)
        self.assertIn("data breach", trust.stage4c_thesis_break_signals)
        self.assertIn("fulfillment unit economics", fulfillment.stage3_high_conviction_signals)
        self.assertIn("domestic retail sales contraction", domestic.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round287_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND287_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round287_summary()
        self.assertEqual(summary["round_id"], "round_215")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["service_trust_hard_reference_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertTrue(summary["service_trust_hard_reference_confirmed"])

    def test_food_beauty_tourism_and_ecommerce_cases_capture_round_anchors(self) -> None:
        by_id = {case.case_id: case for case in ROUND287_CASE_CANDIDATES}
        samyang = by_id["r5_loop14_samyang_buldak_export_stage3_candidate"]
        nongshim = by_id["r5_loop14_nongshim_shin_ramyun_global_expansion"]
        apr = by_id["r5_loop14_apr_medicube_beauty_device_brand_4b"]
        kbeauty = by_id["r5_loop14_kbeauty_us_expansion_basket"]
        tourism = by_id["r5_loop14_china_tourism_retail_event_premium"]
        jv = by_id["r5_loop14_shinsegae_emart_alibaba_gmarket_jv_data_gate"]

        self.assertEqual(samyang.primary_archetype, E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE)
        self.assertEqual(samyang.stage3_price_anchor, 647000.0)
        self.assertEqual(samyang.extra_price_metrics["q2_op_estimate_krw_bn"], 81.2)
        self.assertEqual(samyang.extra_price_metrics["target_upside_from_stage3_price_pct"], 28.3)
        self.assertEqual(samyang.extra_price_metrics["denmark_recall_products_count"], 3)

        self.assertEqual(nongshim.extra_price_metrics["overseas_sales_share_pct"], 60)
        self.assertEqual(nongshim.extra_price_metrics["shin_ramyun_2023_sales_krw_trn"], 1.2)
        self.assertEqual(nongshim.extra_price_metrics["us_sales_target_2030_usd_bn"], 1.5)

        self.assertEqual(apr.extra_price_metrics["market_cap_october_usd_bn"], 6.0)
        self.assertEqual(apr.extra_price_metrics["stock_gain_since_january_multiple"], 4.0)
        self.assertEqual(apr.extra_price_metrics["overseas_revenue_share_q2_2025_pct"], 80)
        self.assertFalse(apr.extra_price_metrics["repeat_purchase_confirmed"])

        self.assertEqual(kbeauty.extra_price_metrics["top5_korean_us_ecommerce_growth_2y_pct"], 71)
        self.assertEqual(kbeauty.extra_price_metrics["tariff_risk_pct"], 25)
        self.assertFalse(kbeauty.extra_price_metrics["physical_sellthrough_confirmed"])

        self.assertEqual(tourism.extra_price_metrics["hyundai_department_event_mfe_pct"], 7.1)
        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_event_mfe_pct"], 9.9)
        self.assertFalse(tourism.extra_price_metrics["spend_conversion_margin_confirmed"])

        self.assertEqual(jv.extra_price_metrics["customer_database_mn"], 50)
        self.assertEqual(jv.extra_price_metrics["expected_cross_border_market_share_pct"], 41)
        self.assertEqual(jv.extra_price_metrics["data_sharing_restriction_years"], 3)
        self.assertFalse(jv.extra_price_metrics["take_rate_confirmed"])

    def test_trust_fulfillment_and_domestic_cases_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND287_CASE_CANDIDATES}
        coupang = by_id["r5_loop14_coupang_data_breach_retail_trust_hard_reference"]
        cj = by_id["r5_loop14_cj_logistics_shinsegae_fulfillment_unit_economics"]
        domestic = by_id["r5_loop14_domestic_retail_sales_shock_4c_watch"]

        self.assertTrue(coupang.hard_4c_confirmed)
        self.assertTrue(coupang.service_trust_hard_reference_confirmed)
        self.assertEqual(coupang.extra_price_metrics["affected_users_mn"], 34)
        self.assertEqual(coupang.extra_price_metrics["CPNG_share_decline_pct"], -34)
        self.assertEqual(coupang.extra_price_metrics["naver_user_gain_pct"], 23)
        self.assertEqual(coupang.extra_price_metrics["cj_logistics_volume_gain_pct"], 120)
        self.assertFalse(coupang.extra_price_metrics["competitor_stage3_allowed"])

        self.assertEqual(cj.extra_price_metrics["annual_revenue_uplift_krw_bn"], 300)
        self.assertEqual(cj.stage2_price_anchor, 99100.0)
        self.assertEqual(cj.extra_price_metrics["target_price_krw"], 116000)
        self.assertEqual(cj.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(domestic.extra_price_metrics["dec_retail_sales_mom_pct"], -0.6)
        self.assertEqual(domestic.extra_price_metrics["cars_home_appliances_pct"], -4.1)
        self.assertEqual(domestic.extra_price_metrics["q4_gdp_pct"], 0.1)
        self.assertEqual(domestic.stage_failure_type, "should_have_been_red")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND287_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND287_GREEN_FORBIDDEN_PATTERNS)
        review = render_round287_green_gate_review_markdown()
        stage_review = render_round287_stage4b_4c_review_markdown()
        fields = set(ROUND287_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND287_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round287_shadow_weight_rows()}
        deep_rows = round287_deep_sub_archetype_rows()

        self.assertIn("export_sellthrough_confirmed", required)
        self.assertIn("ecommerce_take_rate_confirmed", required)
        self.assertIn("data_trust_internal_control_confirmed", required)
        self.assertIn("visitor_count_only", forbidden)
        self.assertIn("JV_scale_without_take_rate", forbidden)
        self.assertIn("data_breach_or_customer_trust_failure", forbidden)
        self.assertIn("export_sellthrough", axes)
        self.assertIn("data_breach_or_customer_trust_failure", axes)
        self.assertIn("data_trust_anchor", fields)
        self.assertIn("tourism_visa_headline_basket_rally", ROUND287_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("data_breach_customer_trust_break", ROUND287_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C", stage_review)
        self.assertEqual(len(ROUND287_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE"]["ecommerce_take_rate"], "+5")
        self.assertEqual(shadow_rows["K_BEAUTY_US_EXPANSION_STAGE2"]["tariff_absorption"], "+5")
        self.assertEqual(shadow_rows["ECOMMERCE_TRUST_BREAK_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Samyang" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Coupang" in row["terms"] for row in deep_rows))
        self.assertTrue(any("spend per head" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round287_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_287.md")
        self.assertEqual(audit["round_id"], "round_215")
        self.assertEqual(audit["large_sector"], ROUND287_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["service_trust_hard_reference_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 9)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 9)
        self.assertIn("do_not_use_round287_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round287_r5_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            loaded = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(loaded), 9)
            self.assertIn(
                "Samyang/Buldak",
                (root / "out" / "round287_r5_loop14_price_validation_summary.md").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
