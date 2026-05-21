from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round326_r5_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round326_r5_loop17_consumer_retail_brand_trigger_validation import (
    ROUND326_CASE_CANDIDATES,
    ROUND326_GREEN_BLOCKERS,
    ROUND326_HARD_4C_GATES,
    ROUND326_LARGE_SECTOR,
    ROUND326_REQUIRED_TARGET_ALIASES,
    ROUND326_ROW_SEPARATION_RULES,
    ROUND326_SCORE_DOWN_AXES,
    ROUND326_SCORE_UP_AXES,
    ROUND326_SHADOW_WEIGHT_ROWS,
    ROUND326_STAGE2_ACTIONABLE_RULES,
    ROUND326_STAGE3_GREEN_RULES,
    ROUND326_STAGE3_YELLOW_RULES,
    ROUND326_STAGE4B_WATCH_TRIGGERS,
    ROUND326_TRIGGER_RECORDS,
    render_round326_stage4b_4c_review_markdown,
    render_round326_stage_rules_markdown,
    render_round326_trigger_grid_markdown,
    round326_audit_payload,
    round326_case_records,
    round326_case_rows,
    round326_shadow_weight_rows,
    round326_summary,
    round326_trigger_rows,
    write_round326_r5_loop17_reports,
)


class Round326R5Loop17ConsumerRetailBrandTests(unittest.TestCase):
    def test_round326_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND326_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND326_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND326_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE"],
            E2RArchetype.K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND326_REQUIRED_TARGET_ALIASES["ECOMMERCE_TRUST_BREAK_HARD_4C"],
            E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_4C.value,
        )
        self.assertEqual(
            ROUND326_REQUIRED_TARGET_ALIASES["K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE"],
            E2RArchetype.K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE.value,
        )

    def test_archetype_definitions_capture_r5_loop17_rules(self) -> None:
        kfood = archetype_definition(E2RArchetype.K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE)
        device = archetype_definition(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW)
        indie = archetype_definition(E2RArchetype.K_BEAUTY_INDIE_US_RETAIL_STAGE2)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE)
        trust = archetype_definition(E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_4C)
        ma = archetype_definition(E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B)
        china = archetype_definition(E2RArchetype.CHINA_PRESTIGE_BEAUTY_FAILED_RERATING)
        reference = archetype_definition(E2RArchetype.K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE)

        self.assertIn("ASP", " ".join(kfood.stage2_candidate_signals))
        self.assertIn("repeat device purchase", " ".join(device.stage3_high_conviction_signals))
        self.assertIn("physical-store sell-through", " ".join(indie.stage3_high_conviction_signals))
        self.assertIn("basket size", " ".join(tourism.stage3_high_conviction_signals))
        self.assertIn("MAU or spending decline", " ".join(trust.stage4c_thesis_break_signals))
        self.assertIn("final SPA", " ".join(ma.stage3_high_conviction_signals))
        self.assertIn("weak China demand", " ".join(china.stage4c_thesis_break_signals))
        self.assertIn("not Green", " ".join(reference.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round326_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND326_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round326_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round326_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_326.md")
        self.assertEqual(summary["round_id"], "round_254")
        self.assertEqual(summary["large_sector"], ROUND326_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_consumer_retail_brand_round(self) -> None:
        by_id = {case.case_id: case for case in ROUND326_CASE_CANDIDATES}
        samyang = by_id["r5_loop17_samyang_buldak_export"]
        apr = by_id["r5_loop17_apr_medicube_beauty_device"]
        kbeauty = by_id["r5_loop17_kbeauty_indie_us_retail"]
        tourism = by_id["r5_loop17_china_visa_free_tourism_retail"]
        coupang = by_id["r5_loop17_coupang_trust_break_retail_shift"]
        baemin = by_id["r5_loop17_baemin_uber_naver_ma"]
        amore = by_id["r5_loop17_amorepacific_china_prestige_failed_rerating"]
        drg = by_id["r5_loop17_dr_g_loreal_kbeauty_ma"]

        self.assertEqual(samyang.extra_price_metrics["op_estimate_yoy_pct"], 84)
        self.assertEqual(samyang.extra_price_metrics["entry_price_krw"], 647000)
        self.assertEqual(samyang.stage_candidate, "Stage2-Actionable")

        self.assertEqual(apr.extra_price_metrics["market_value_context_usd_bn"], 6)
        self.assertEqual(apr.stage_candidate, "Stage3-Yellow_candidate")
        self.assertIn("celebrity_virality_overheat_4B", apr.red_flag_fields)

        self.assertEqual(kbeauty.extra_price_metrics["top5_korean_us_ecommerce_sales_growth_2yr_pct"], 71)
        self.assertIn("offline_sellthrough_unknown", kbeauty.red_flag_fields)

        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_event_return_pct"], 9.9)
        self.assertEqual(tourism.stage_candidate, "Stage2-Actionable")

        self.assertTrue(coupang.hard_4c_confirmed)
        self.assertEqual(coupang.extra_price_metrics["coupang_return_since_breach_pct"], -34)
        self.assertEqual(coupang.rerating_result, "thesis_break")

        self.assertEqual(baemin.extra_price_metrics["baemin_bid_value_krw_trn"], 8.0)
        self.assertIn("final_SPA_missing_4B", baemin.red_flag_fields)

        self.assertEqual(amore.rerating_result, "no_rerating")
        self.assertIn("weak_China_demand", amore.evidence_fields)

        self.assertEqual(drg.extra_price_metrics["valuation"], "undisclosed")
        self.assertEqual(drg.stage_candidate, "Stage2 reference")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round326_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round326_shadow_weight_rows()}
        rules_md = render_round326_stage_rules_markdown()
        trigger_md = render_round326_trigger_grid_markdown()
        stage_md = render_round326_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND326_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r5l17_samyang_buldak_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r5l17_coupang_breach_T1"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r5l17_baemin_naver_T0"]["promote_to"], "Stage2+4B")
        self.assertEqual(len(ROUND326_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE"]["export_ASP_shipment_capacity"], "+5")
        self.assertEqual(shadow_rows["K_BEAUTY_INDIE_US_RETAIL_STAGE2"]["US_retail_shelf_in"], "+5")
        self.assertEqual(shadow_rows["ECOMMERCE_TRUST_BREAK_HARD_4C"]["consumer_trust_security"], "+5")
        self.assertIn("event_return_at_least_5pct", ROUND326_STAGE2_ACTIONABLE_RULES)
        self.assertIn("overseas_sellthrough_and_repeat_orders_visible", ROUND326_STAGE3_YELLOW_RULES)
        self.assertIn("brand_demand_converts_into_repeat_revenue_and_margin", ROUND326_STAGE3_GREEN_RULES)
        self.assertIn("viral_brand_without_sellthrough", ROUND326_GREEN_BLOCKERS)
        self.assertIn("export_ASP_shipment_capacity", ROUND326_SCORE_UP_AXES)
        self.assertIn("supplier_regulation_ignored", ROUND326_SCORE_DOWN_AXES)
        self.assertIn("data_breach_and_supplier_regulation", ROUND326_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("consumer_trust_breach_with_MAU_spending_deterioration", ROUND326_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND326_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r5_loop17_samyang_buldak_export", trigger_md)
        self.assertIn("r5_loop17_coupang_trust_break_retail_shift", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round326_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_326.md")
        self.assertEqual(audit["round_id"], "round_254")
        self.assertEqual(audit["large_sector"], ROUND326_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round326_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round326_r5_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND326_CASE_CANDIDATES))
            self.assertEqual(len(round326_case_rows()), len(ROUND326_CASE_CANDIDATES))
            self.assertIn("Stage3-Green confirmed: `0`", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Full adjusted OHLC", paths["price_validation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
