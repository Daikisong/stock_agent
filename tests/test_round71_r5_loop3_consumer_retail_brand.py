import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round71_r5_loop3_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round71_r5_loop3_consumer_retail_brand import (
    ROUND71_CASE_CANDIDATES,
    ROUND71_PRICE_FIELDS,
    ROUND71_SCORE_TARGETS,
    render_round71_green_guardrail_markdown,
    render_round71_price_validation_plan_markdown,
    render_round71_risk_overlay_markdown,
    render_round71_summary_markdown,
    round71_case_candidate_rows,
    round71_case_records,
    round71_price_field_rows,
    round71_score_profile_rows,
    round71_stage_date_rows,
    round71_summary,
    round71_target_for,
    write_round71_r5_loop3_reports,
)


class Round71R5Loop3ConsumerRetailBrandTests(unittest.TestCase):
    def test_round71_targets_cover_consumer_retail_brand_loop3(self):
        labels = {target.target_id for target in ROUND71_SCORE_TARGETS}

        self.assertEqual(len(labels), 16)
        for label in (
            "EXPORT_RECURRING_CONSUMER",
            "K_FOOD_SINGLE_HERO_PRODUCT",
            "K_BEAUTY_EXPORT_DISTRIBUTION",
            "BEAUTY_DEVICE_EXPORT",
            "BEAUTY_OEM_ODM_SUPPLYCHAIN",
            "RETAIL_CONVENIENCE_OFFLINE",
            "RETAIL_ECOMMERCE_LOGISTICS",
            "ECOMMERCE_FRESH_LOGISTICS",
            "APPAREL_FAST_FASHION_BRAND_OEM",
            "HOME_LIVING_APPLIANCE_RENTAL",
            "HOME_CHILD_EDUCATION",
            "CONSUMER_REGULATED_PRODUCT",
            "FOOD_SAFETY_RECALL_OVERLAY",
            "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY",
            "CHANNEL_STUFFING_INVENTORY_OVERLAY",
            "TARIFF_IMPORT_REGULATION_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND71_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.CONSUMER_RETAIL_BRAND)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop3_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
            E2RArchetype.TARIFF_IMPORT_REGULATION_OVERLAY,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_green_possible_targets_and_redteam_overlays_are_separated(self):
        k_food = round71_target_for("K_FOOD_SINGLE_HERO_PRODUCT")
        k_beauty = round71_target_for("K_BEAUTY_EXPORT_DISTRIBUTION")
        device = round71_target_for("BEAUTY_DEVICE_EXPORT")
        odm = round71_target_for("BEAUTY_OEM_ODM_SUPPLYCHAIN")
        recall = round71_target_for("FOOD_SAFETY_RECALL_OVERLAY")
        stuffing = round71_target_for("CHANNEL_STUFFING_INVENTORY_OVERLAY")
        tariff = round71_target_for("TARIFF_IMPORT_REGULATION_OVERLAY")

        for target in (k_food, k_beauty, device, odm, recall, stuffing, tariff):
            self.assertIsNotNone(target)
        assert k_food is not None
        assert k_beauty is not None
        assert device is not None
        assert odm is not None
        assert recall is not None
        assert stuffing is not None
        assert tariff is not None
        for target in (k_food, k_beauty, device, odm):
            self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
            self.assertGreater(len(target.green_conditions), 0)
            self.assertGreater(len(target.red_flags), 0)
        for target in (recall, stuffing, tariff):
            self.assertTrue(target.gate_only)
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertEqual(target.score_weight.eps_fcf, "gate")

    def test_required_round71_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round71_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND71_CASE_CANDIDATES))
        self.assertEqual(rows["samyang_buldak_export_rerating_case"]["target_id"], "EXPORT_RECURRING_CONSUMER")
        self.assertEqual(rows["samyang_buldak_export_rerating_case"]["stage2_date"], "2024-06-14")
        self.assertEqual(rows["samyang_buldak_export_rerating_case"]["stage4b_date"], "2024-06-14")
        self.assertEqual(rows["samyang_buldak_denmark_recall_case"]["stage4c_date"], "2024-06-12")
        self.assertEqual(rows["kbeauty_us_export_overtake_france_case"]["stage2_date"], "2025-06-05")
        self.assertEqual(rows["kbeauty_us_export_overtake_france_case"]["stage4b_date"], "2025-06-05")
        self.assertEqual(rows["kbeauty_us_tariff_risk_case"]["stage4c_date"], "")
        self.assertEqual(rows["apr_medicube_beauty_device_case"]["target_id"], "BEAUTY_DEVICE_EXPORT")
        self.assertEqual(rows["apr_medicube_beauty_device_case"]["stage2_date"], "2025-10-20")
        self.assertEqual(rows["apr_medicube_beauty_device_case"]["stage4b_date"], "2025-10-20")
        self.assertEqual(rows["medicube_ulta_tiktok_omnichannel_case"]["stage2_date"], "2026-02-13")
        self.assertEqual(rows["coupang_data_breach_case"]["stage4c_date"], "")
        self.assertEqual(rows["coupang_supplier_payment_regulation_case"]["stage4c_date"], "2026-02-26")
        self.assertEqual(rows["coway_rental_recurring_case"]["stage2_date"], "")
        self.assertEqual(rows["whirlpool_dividend_suspension_case"]["stage4c_date"], "")
        self.assertEqual(rows["shein_temu_ip_litigation_case"]["stage4c_date"], "2026-05-11")
        self.assertEqual(rows["shein_temu_eu_product_safety_case"]["stage4c_date"], "")

    def test_case_records_validate_and_keep_consumer_guardrails(self):
        records = round71_case_records()

        self.assertEqual(len(records), len(ROUND71_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "CONSUMER_RETAIL_BRAND")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("shipment_is_not_sell_through", record.green_guardrails)
            self.assertIn("consumer_sales_growth_is_not_structural_evidence_alone", record.green_guardrails)
            self.assertIn(
                "do_not_invent_export_sell_through_reorder_inventory_receivables_churn_or_stage_prices",
                record.green_guardrails,
            )
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["samyang_buldak_export_rerating_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["apr_medicube_beauty_device_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["coupang_data_breach_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["shein_temu_ip_litigation_case"].score_price_alignment, "false_positive_score")
        self.assertIn(
            E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT,
            by_id["samyang_buldak_export_rerating_case"].secondary_archetypes,
        )

    def test_score_profile_rows_match_round71_weight_table(self):
        rows = {row["target_id"]: row for row in round71_score_profile_rows()}

        self.assertEqual(rows["EXPORT_RECURRING_CONSUMER"]["eps_fcf"], "22")
        self.assertEqual(rows["K_FOOD_SINGLE_HERO_PRODUCT"]["eps_fcf"], "23")
        self.assertEqual(rows["K_BEAUTY_EXPORT_DISTRIBUTION"]["structural_visibility"], "23")
        self.assertEqual(rows["BEAUTY_DEVICE_EXPORT"]["bottleneck_pricing"], "14")
        self.assertEqual(rows["RETAIL_ECOMMERCE_LOGISTICS"]["eps_fcf"], "16")
        self.assertEqual(rows["ECOMMERCE_FRESH_LOGISTICS"]["valuation"], "9")
        self.assertEqual(rows["APPAREL_FAST_FASHION_BRAND_OEM"]["eps_fcf"], "16")
        self.assertEqual(rows["FOOD_SAFETY_RECALL_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["FOOD_SAFETY_RECALL_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["CHANNEL_STUFFING_INVENTORY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["TARIFF_IMPORT_REGULATION_OVERLAY"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round71_stage_date_rows()}
        fields = {row["field"] for row in round71_price_field_rows()}

        self.assertIn("channel_sell_through", rows["EXPORT_RECURRING_CONSUMER"]["stage3"])
        self.assertIn("country_recall", rows["K_FOOD_SINGLE_HERO_PRODUCT"]["stage4c"])
        self.assertIn("tariff_flag", rows["K_BEAUTY_EXPORT_DISTRIBUTION"]["stage4c"])
        self.assertIn("beauty_device_narrative_overheated", rows["BEAUTY_DEVICE_EXPORT"]["stage4b"])
        self.assertIn("data_breach", rows["RETAIL_ECOMMERCE_LOGISTICS"]["stage4c"])
        self.assertIn("channel_stuffing", rows["CHANNEL_STUFFING_INVENTORY_OVERLAY"]["stage4c"])
        self.assertIn("fda_import_review", rows["TARIFF_IMPORT_REGULATION_OVERLAY"]["stage4c"])
        for field in (
            "single_product_revenue_ratio",
            "capsaicin_or_additive_risk_flag",
            "tariff_rate",
            "de_minimis_change_flag",
            "fda_import_review_flag",
            "beauty_device_asp",
            "affected_customer_count",
            "gross_margin_quality_risk_flag",
            "unsafe_item_removal_count",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND71_PRICE_FIELDS))

    def test_summary_and_markdown_explain_round71_guardrails(self):
        summary = round71_summary()
        summary_md = render_round71_summary_markdown()
        guardrails = render_round71_green_guardrail_markdown()
        overlays = render_round71_risk_overlay_markdown()
        price_plan = render_round71_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 16)
        self.assertEqual(summary["case_candidate_count"], 12)
        self.assertEqual(summary["structural_success_count"], 0)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["cyclical_success_count"], 0)
        self.assertEqual(summary["event_premium_count"], 0)
        self.assertEqual(summary["overheat_count"], 0)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 6)
        self.assertEqual(summary["redteam_first_count"], 5)
        self.assertEqual(summary["gate_only_target_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R5 Loop 3", summary_md)
        self.assertIn("Do not apply R5 Loop-3 v3.0 weights", guardrails)
        self.assertIn("CHANNEL_ENTRY_BUT_UNKNOWN_REORDER", overlays)
        self.assertIn("samyang_buldak_export_rerating_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round71_r5_loop3_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r5_loop3_round71.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round71_r5_loop3_v3.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND71_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round71_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round71_r5_loop3_consumer_retail_brand", text)


if __name__ == "__main__":
    unittest.main()
