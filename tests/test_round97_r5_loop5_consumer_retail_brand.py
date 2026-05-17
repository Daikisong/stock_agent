import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round97_r5_loop5_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round97_r5_loop5_consumer_retail_brand import (
    ROUND97_CASE_CANDIDATES,
    ROUND97_PRICE_FIELDS,
    ROUND97_SCORE_TARGETS,
    render_round97_green_guardrail_markdown,
    render_round97_price_validation_plan_markdown,
    render_round97_risk_overlay_markdown,
    render_round97_summary_markdown,
    round97_case_candidate_rows,
    round97_case_records,
    round97_price_field_rows,
    round97_score_profile_rows,
    round97_stage_date_rows,
    round97_summary,
    round97_target_for,
    write_round97_r5_loop5_reports,
)


class Round97R5Loop5ConsumerRetailBrandTests(unittest.TestCase):
    def test_round97_targets_cover_consumer_retail_brand_loop5(self):
        labels = {target.target_id for target in ROUND97_SCORE_TARGETS}

        self.assertEqual(len(labels), 23)
        for label in (
            "EXPORT_RECURRING_CONSUMER",
            "K_FOOD_SINGLE_HERO_PRODUCT",
            "K_FOOD_GLOBAL_PORTFOLIO_EXPANSION",
            "K_BEAUTY_EXPORT_DISTRIBUTION",
            "K_BEAUTY_OFFLINE_SELL_THROUGH",
            "K_BEAUTY_RETAIL_PLATFORM",
            "BEAUTY_DEVICE_EXPORT",
            "BEAUTY_DEVICE_AFFILIATE_COMMERCE",
            "BEAUTY_OEM_ODM_SUPPLYCHAIN",
            "RETAIL_CONVENIENCE_OFFLINE",
            "RETAIL_ECOMMERCE_LOGISTICS",
            "ECOMMERCE_FRESH_LOGISTICS",
            "APPAREL_FAST_FASHION_BRAND_OEM",
            "ULTRA_LOW_COST_CROSSBORDER_PLATFORM",
            "HOME_LIVING_APPLIANCE_RENTAL",
            "HOME_APPLIANCE_HARDWARE_CYCLE",
            "HOME_CHILD_EDUCATION",
            "CONSUMER_REGULATED_PRODUCT",
            "FOOD_SAFETY_RECALL_OVERLAY",
            "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY",
            "CHANNEL_STUFFING_INVENTORY_OVERLAY",
            "TARIFF_IMPORT_REGULATION_OVERLAY",
            "DISCOUNT_PROMOTION_MARGIN_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND97_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.CONSUMER_RETAIL_BRAND)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop5_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.K_FOOD_GLOBAL_PORTFOLIO_EXPANSION,
            E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH,
            E2RArchetype.K_BEAUTY_RETAIL_PLATFORM,
            E2RArchetype.BEAUTY_DEVICE_AFFILIATE_COMMERCE,
            E2RArchetype.ULTRA_LOW_COST_CROSSBORDER_PLATFORM,
            E2RArchetype.HOME_APPLIANCE_HARDWARE_CYCLE,
            E2RArchetype.DISCOUNT_PROMOTION_MARGIN_OVERLAY,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_green_possible_watch_and_redteam_targets_are_separated(self):
        green_targets = (
            "EXPORT_RECURRING_CONSUMER",
            "K_FOOD_SINGLE_HERO_PRODUCT",
            "K_BEAUTY_EXPORT_DISTRIBUTION",
            "BEAUTY_DEVICE_EXPORT",
            "BEAUTY_OEM_ODM_SUPPLYCHAIN",
        )
        watch_targets = (
            "K_FOOD_GLOBAL_PORTFOLIO_EXPANSION",
            "K_BEAUTY_OFFLINE_SELL_THROUGH",
            "K_BEAUTY_RETAIL_PLATFORM",
            "BEAUTY_DEVICE_AFFILIATE_COMMERCE",
            "HOME_LIVING_APPLIANCE_RENTAL",
        )
        gate_targets = (
            "FOOD_SAFETY_RECALL_OVERLAY",
            "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY",
            "CHANNEL_STUFFING_INVENTORY_OVERLAY",
            "TARIFF_IMPORT_REGULATION_OVERLAY",
            "DISCOUNT_PROMOTION_MARGIN_OVERLAY",
        )

        for target_id in green_targets:
            target = round97_target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
            self.assertGreater(len(target.green_conditions), 0)
        for target_id in watch_targets:
            target = round97_target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        for target_id in gate_targets:
            target = round97_target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertTrue(target.gate_only)
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertEqual(target.score_weight.eps_fcf, "gate")

    def test_required_round97_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round97_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND97_CASE_CANDIDATES))
        self.assertEqual(rows["samyang_buldak_export_rerating_case"]["target_id"], "EXPORT_RECURRING_CONSUMER")
        self.assertEqual(rows["samyang_buldak_export_rerating_case"]["stage2_date"], "2024-06-14")
        self.assertEqual(rows["samyang_buldak_export_rerating_case"]["stage4b_date"], "2024-06-14")
        self.assertEqual(rows["samyang_buldak_denmark_recall_case"]["stage4c_date"], "2024-06-12")
        self.assertEqual(rows["samyang_buldak_denmark_partial_reversal_case"]["stage2_date"], "2024-08-08")
        self.assertEqual(rows["kbeauty_us_export_overtake_france_case"]["stage2_date"], "2025-06-05")
        self.assertEqual(rows["olive_young_us_retail_platform_case"]["target_id"], "K_BEAUTY_RETAIL_PLATFORM")
        self.assertEqual(rows["olive_young_us_retail_platform_case"]["stage2_date"], "")
        self.assertEqual(rows["kbeauty_us_tariff_risk_case"]["stage4c_date"], "")
        self.assertEqual(rows["kbeauty_france_us_tariff_competition_case"]["target_id"], "TARIFF_IMPORT_REGULATION_OVERLAY")
        self.assertEqual(rows["apr_medicube_beauty_device_case"]["stage4b_date"], "2025-10-20")
        self.assertEqual(rows["medicube_ulta_tiktok_omnichannel_case"]["target_id"], "BEAUTY_DEVICE_AFFILIATE_COMMERCE")
        self.assertEqual(rows["medicube_ulta_tiktok_omnichannel_case"]["stage2_date"], "2026-02-13")
        self.assertEqual(rows["kbeauty_oem_odm_fast_beauty_case"]["target_id"], "BEAUTY_OEM_ODM_SUPPLYCHAIN")
        self.assertEqual(rows["kbeauty_oem_odm_fast_beauty_case"]["stage2_date"], "2025-06-05")
        self.assertEqual(rows["coupang_data_breach_case"]["stage4c_date"], "2025-11-29")
        self.assertEqual(rows["coupang_supplier_payment_regulation_case"]["stage4c_date"], "2026-02-26")
        self.assertEqual(rows["whirlpool_dividend_suspension_case"]["target_id"], "HOME_APPLIANCE_HARDWARE_CYCLE")
        self.assertEqual(rows["shein_temu_ip_litigation_case"]["target_id"], "ULTRA_LOW_COST_CROSSBORDER_PLATFORM")
        self.assertEqual(rows["shein_temu_ip_litigation_case"]["stage4c_date"], "2026-05-11")

    def test_case_records_validate_and_keep_consumer_guardrails(self):
        records = round97_case_records()

        self.assertEqual(len(records), len(ROUND97_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "CONSUMER_RETAIL_BRAND")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("shipment_is_not_sell_through", record.green_guardrails)
            self.assertIn("discount_promotion_sales_are_not_green_without_margin_quality", record.green_guardrails)
            self.assertIn("consumer_sales_growth_is_not_structural_evidence_alone", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["samyang_buldak_export_rerating_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["samyang_buldak_denmark_partial_reversal_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["kbeauty_france_us_tariff_competition_case"].rerating_result, "event_premium")
        self.assertIn(
            E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH,
            by_id["olive_young_us_retail_platform_case"].secondary_archetypes,
        )
        self.assertEqual(by_id["apr_medicube_beauty_device_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["coupang_data_breach_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["shein_temu_ip_litigation_case"].score_price_alignment, "false_positive_score")
        self.assertIn(
            E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT,
            by_id["samyang_buldak_export_rerating_case"].secondary_archetypes,
        )

    def test_score_profile_rows_match_round97_weight_table(self):
        rows = {row["target_id"]: row for row in round97_score_profile_rows()}

        self.assertEqual(rows["EXPORT_RECURRING_CONSUMER"]["eps_fcf"], "22")
        self.assertEqual(rows["K_FOOD_SINGLE_HERO_PRODUCT"]["valuation"], "10")
        self.assertEqual(rows["K_FOOD_GLOBAL_PORTFOLIO_EXPANSION"]["structural_visibility"], "22")
        self.assertEqual(rows["K_BEAUTY_EXPORT_DISTRIBUTION"]["valuation"], "12")
        self.assertEqual(rows["K_BEAUTY_OFFLINE_SELL_THROUGH"]["market_mispricing"], "16")
        self.assertEqual(rows["K_BEAUTY_RETAIL_PLATFORM"]["structural_visibility"], "21")
        self.assertEqual(rows["BEAUTY_DEVICE_EXPORT"]["valuation"], "9")
        self.assertEqual(rows["BEAUTY_DEVICE_AFFILIATE_COMMERCE"]["structural_visibility"], "19")
        self.assertEqual(rows["BEAUTY_OEM_ODM_SUPPLYCHAIN"]["eps_fcf"], "22")
        self.assertEqual(rows["RETAIL_ECOMMERCE_LOGISTICS"]["structural_visibility"], "12")
        self.assertEqual(rows["ULTRA_LOW_COST_CROSSBORDER_PLATFORM"]["posture"], "REDTEAM_FIRST")
        self.assertEqual(rows["HOME_APPLIANCE_HARDWARE_CYCLE"]["eps_fcf"], "14")
        self.assertEqual(rows["FOOD_SAFETY_RECALL_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["DISCOUNT_PROMOTION_MARGIN_OVERLAY"]["eps_fcf"], "gate")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round97_stage_date_rows()}
        fields = {row["field"] for row in round97_price_field_rows()}

        self.assertIn("channel_sell_through", rows["EXPORT_RECURRING_CONSUMER"]["stage3"])
        self.assertIn("sku_expansion_failure", rows["K_FOOD_GLOBAL_PORTFOLIO_EXPANSION"]["stage4c"])
        self.assertIn("reorder_absent", rows["K_BEAUTY_OFFLINE_SELL_THROUGH"]["stage4c"])
        self.assertIn("store_level_sell_through", rows["K_BEAUTY_RETAIL_PLATFORM"]["stage3"])
        self.assertIn("affiliate_cac_stable", rows["BEAUTY_DEVICE_AFFILIATE_COMMERCE"]["stage3"])
        self.assertIn("data_breach", rows["RETAIL_ECOMMERCE_LOGISTICS"]["stage4c"])
        self.assertIn("unsafe_item_removal", rows["ULTRA_LOW_COST_CROSSBORDER_PLATFORM"]["stage4c"])
        self.assertIn("dividend_suspension", rows["HOME_APPLIANCE_HARDWARE_CYCLE"]["stage4c"])
        self.assertIn("discount_rate_increase", rows["DISCOUNT_PROMOTION_MARGIN_OVERLAY"]["stage4c"])
        for field in (
            "single_product_revenue_ratio",
            "country_sales_ban_reversal_flag",
            "tariff_rate",
            "store_level_sales",
            "store_level_margin",
            "price_increase_flag",
            "beauty_device_asp",
            "affiliate_creator_count",
            "creator_commission_rate",
            "affiliate_cac",
            "roas",
            "affected_customer_count",
            "post_incident_disclosure_risk_flag",
            "gross_margin_quality_risk_flag",
            "unsafe_item_removal_count",
            "platform_regulatory_investigation_flag",
            "opendart_rcept_no",
            "disclosure_confidence_score",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND97_PRICE_FIELDS))

    def test_summary_and_markdown_explain_round97_guardrails(self):
        summary = round97_summary()
        summary_md = render_round97_summary_markdown()
        guardrails = render_round97_green_guardrail_markdown()
        overlays = render_round97_risk_overlay_markdown()
        price_plan = render_round97_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 23)
        self.assertEqual(summary["case_candidate_count"], 16)
        self.assertEqual(summary["structural_success_count"], 0)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 10)
        self.assertEqual(summary["redteam_first_count"], 8)
        self.assertEqual(summary["gate_only_target_count"], 5)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R5 Loop 5", summary_md)
        self.assertIn("Do not apply R5 Loop-5 v5.0 weights", guardrails)
        self.assertIn("RETAIL_PLATFORM_STAGE2_NOT_STAGE3", overlays)
        self.assertIn("AFFILIATE_COMMERCE_MARGIN_WATCH", overlays)
        self.assertIn("DISCOUNT_PROMOTION_MARGIN_OVERLAY", guardrails)
        self.assertIn("olive_young_us_retail_platform_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round97_r5_loop5_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r5_loop5_round97.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round97_r5_loop5_v5.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND97_CASE_CANDIDATES))

    def test_cli_argument_parser_supports_paths(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--score-profiles",
                "scores.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.score_profiles, "scores.csv")

    def test_production_scoring_modules_do_not_import_round97_pack(self):
        root = Path(__file__).resolve().parents[1]
        for relative in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = (root / relative).read_text(encoding="utf-8")
            self.assertNotIn("round97_r5_loop5_consumer_retail_brand", text)


if __name__ == "__main__":
    unittest.main()
