from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round313_r5_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round313_r5_loop16_consumer_retail_brand_trigger_validation import (
    ROUND313_4C_WATCH_GATES,
    ROUND313_CASE_CANDIDATES,
    ROUND313_GREEN_BLOCKERS,
    ROUND313_LARGE_SECTOR,
    ROUND313_REQUIRED_TARGET_ALIASES,
    ROUND313_ROW_SEPARATION_RULES,
    ROUND313_SCORE_DOWN_AXES,
    ROUND313_SCORE_UP_AXES,
    ROUND313_SHADOW_WEIGHT_ROWS,
    ROUND313_STAGE2_ACTIONABLE_RULES,
    ROUND313_STAGE3_GREEN_RULES,
    ROUND313_STAGE3_YELLOW_RULES,
    ROUND313_STAGE4B_WATCH_TRIGGERS,
    ROUND313_TRIGGER_RECORDS,
    render_round313_stage4b_4c_review_markdown,
    render_round313_stage_rules_markdown,
    render_round313_trigger_grid_markdown,
    round313_audit_payload,
    round313_case_records,
    round313_case_rows,
    round313_shadow_weight_rows,
    round313_summary,
    round313_trigger_rows,
    write_round313_r5_loop16_reports,
)


class Round313R5Loop16ConsumerRetailBrandTests(unittest.TestCase):
    def test_round313_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND313_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND313_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND313_REQUIRED_TARGET_ALIASES["KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW"],
            E2RArchetype.KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW.value,
        )
        self.assertEqual(
            ROUND313_REQUIRED_TARGET_ALIASES["ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2"],
            E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2.value,
        )
        self.assertEqual(
            ROUND313_REQUIRED_TARGET_ALIASES["OFFLINE_GROCERY_RESTRUCTURING_HARD_4C"],
            E2RArchetype.OFFLINE_GROCERY_RESTRUCTURING_HARD_4C.value,
        )

    def test_archetype_definitions_capture_r5_loop16_rules(self) -> None:
        kfood = archetype_definition(E2RArchetype.KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW)
        kbeauty = archetype_definition(E2RArchetype.KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE)
        device = archetype_definition(E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_DUTYFREE_STAGE2_EVENT)
        ecommerce = archetype_definition(E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2)
        jv = archetype_definition(E2RArchetype.RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B)
        grocery = archetype_definition(E2RArchetype.OFFLINE_GROCERY_RESTRUCTURING_HARD_4C)
        shrink = archetype_definition(E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH)

        self.assertIn("ASP", " ".join(kfood.stage2_candidate_signals))
        self.assertIn("sell-through", " ".join(kbeauty.stage3_high_conviction_signals))
        self.assertIn("recurring revenue", " ".join(device.stage3_high_conviction_signals))
        self.assertIn("per-capita spending", " ".join(tourism.stage3_high_conviction_signals))
        self.assertIn("customer exodus", " ".join(ecommerce.stage4c_thesis_break_signals))
        self.assertIn("take-rate", " ".join(jv.stage3_high_conviction_signals))
        self.assertIn("liquidation value", " ".join(grocery.stage4c_thesis_break_signals))
        self.assertIn("margin compression", " ".join(shrink.stage4c_thesis_break_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round313_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND313_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round313_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_brand_channel_policy_JV_user_shift_or_price_regulation_headline_as_green_without_margin_sellthrough_GMV_or_FCF",
                record.green_guardrails,
            )

        summary = round313_summary()
        self.assertEqual(summary["round_id"], "round_241")
        self.assertEqual(summary["large_sector"], ROUND313_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage2_event_candidate_count"], 3)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_brand_channel_tourism_trust_and_regulation(self) -> None:
        by_id = {case.case_id: case for case in ROUND313_CASE_CANDIDATES}
        samyang = by_id["r5_loop16_samyang_buldak_export"]
        kbeauty = by_id["r5_loop16_kbeauty_us_channel"]
        apr = by_id["r5_loop16_apr_medicube_beauty_device"]
        tourism = by_id["r5_loop16_china_visa_free_tourism_retail"]
        coupang = by_id["r5_loop16_coupang_breach_rival_retail_shift"]
        jv = by_id["r5_loop16_shinsegae_emart_alibaba_gmarket_jv"]
        homeplus = by_id["r5_loop16_homeplus_offline_grocery_restructuring"]
        shrink = by_id["r5_loop16_shrinkflation_price_regulation"]

        self.assertEqual(samyang.extra_price_metrics["op_estimate_yoy_pct"], 84)
        self.assertEqual(samyang.stage2_price_anchor, 647000)
        self.assertEqual(samyang.rerating_result, "true_rerating")

        self.assertEqual(kbeauty.extra_price_metrics["top5_korean_us_ecommerce_growth_2y_pct"], 71)
        self.assertIn("physical_store_sellthrough_missing", kbeauty.red_flag_fields)

        self.assertEqual(apr.extra_price_metrics["market_value_usd_bn"], 6)
        self.assertIn("celebrity_viral_concentration_4B", apr.red_flag_fields)

        self.assertEqual(tourism.extra_price_metrics["hyundai_department_store_event_return_pct"], 7.1)
        self.assertIn("per_capita_spending_missing", tourism.red_flag_fields)

        self.assertEqual(coupang.extra_price_metrics["affected_accounts_mn"], 33.7)
        self.assertEqual(coupang.rerating_result, "thesis_break")
        self.assertTrue(coupang.hard_4c_confirmed)

        self.assertEqual(jv.extra_price_metrics["market_context"], "Korea_ecommerce_world_fourth_largest")
        self.assertEqual(jv.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(homeplus.extra_price_metrics["liquidation_value_krw_trn"], 3.7)
        self.assertTrue(homeplus.hard_4c_confirmed)

        self.assertEqual(shrink.extra_price_metrics["cj_sausage_weight_cut_pct"], 12.5)
        self.assertIn("brand_pricing_power_missing", shrink.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round313_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round313_shadow_weight_rows()}
        rules_md = render_round313_stage_rules_markdown()
        trigger_md = render_round313_trigger_grid_markdown()
        stage_md = render_round313_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND313_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r5l16_samyang_buldak_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r5l16_coupang_breach_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r5l16_shrinkflation_T0"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND313_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW"]["export_ASP_shipment_capacity"], "+5")
        self.assertEqual(shadow_rows["KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE"]["US_physical_channel_sellthrough"], "+5")
        self.assertEqual(shadow_rows["ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2"]["platform_security_trust"], "+5")
        self.assertIn("export_ASP_shipment_capacity_or_offline_channel_metric_is_specific", ROUND313_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_repeat_margin_sellthrough_GMV_conversion_or_recurring_revenue_gate_remains_open", ROUND313_STAGE3_YELLOW_RULES)
        self.assertIn("platform_share_capture_converts_to_GMV_and_delivery_margin", ROUND313_STAGE3_GREEN_RULES)
        self.assertIn("viral_brand_without_margin", ROUND313_GREEN_BLOCKERS)
        self.assertIn("repeat_purchase_or_recurring_revenue", ROUND313_SCORE_UP_AXES)
        self.assertIn("JV_without_integration_economics", ROUND313_SCORE_DOWN_AXES)
        self.assertIn("tourism_policy_moves_stocks_before_visitor_spending", ROUND313_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("ecommerce_data_breach_customer_trust_collapse", ROUND313_4C_WATCH_GATES)
        self.assertIn("do_not_treat_brand_channel_policy_JV_or_user_shift_headline_as_Green_without_margin_sellthrough_GMV_or_FCF", ROUND313_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r5_loop16_samyang_buldak_export", trigger_md)
        self.assertIn("r5_loop16_homeplus_offline_grocery_restructuring", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round313_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_313.md")
        self.assertEqual(audit["round_id"], "round_241")
        self.assertEqual(audit["large_sector"], ROUND313_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_brand_channel_policy_JV_user_shift_or_price_regulation_headline_as_green_without_margin_sellthrough_GMV_or_FCF", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--triggers",
                "triggers.jsonl",
                "--audit",
                "audit.json",
                "--weight-profile",
                "weights.csv",
            ]
        )
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")
        self.assertEqual(args.weight_profile, "weights.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round313_r5_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round313_case_rows()
            self.assertEqual(len(records), len(ROUND313_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND313_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND313_TRIGGER_RECORDS))
            self.assertIn("Samyang", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r5l16_coupang_breach_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("SHRINKFLATION_PRICE_REGULATION_4C_WATCH", paths["weight_profiles"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
