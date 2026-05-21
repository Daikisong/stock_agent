from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round300_r5_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round300_r5_loop15_consumer_retail_brand_trigger_validation import (
    ROUND300_CASE_CANDIDATES,
    ROUND300_GREEN_BLOCKERS,
    ROUND300_HARD_4C_GATES,
    ROUND300_LARGE_SECTOR,
    ROUND300_REQUIRED_TARGET_ALIASES,
    ROUND300_SCORE_DOWN_AXES,
    ROUND300_SCORE_UP_AXES,
    ROUND300_SHADOW_WEIGHT_ROWS,
    ROUND300_STAGE2_ACTIONABLE_RULES,
    ROUND300_STAGE3_GREEN_RULES,
    ROUND300_STAGE3_YELLOW_RULES,
    ROUND300_STAGE4B_WATCH_TRIGGERS,
    ROUND300_TRIGGER_RECORDS,
    render_round300_stage_rules_markdown,
    render_round300_stage4b_4c_review_markdown,
    render_round300_trigger_grid_markdown,
    round300_audit_payload,
    round300_case_records,
    round300_case_rows,
    round300_shadow_weight_rows,
    round300_summary,
    round300_trigger_rows,
    write_round300_r5_loop15_reports,
)


class Round300R5Loop15ConsumerRetailBrandTriggerValidationTests(unittest.TestCase):
    def test_round300_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND300_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND300_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND300_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW"],
            E2RArchetype.K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW.value,
        )
        self.assertEqual(
            ROUND300_REQUIRED_TARGET_ALIASES["FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE"],
            E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE.value,
        )
        self.assertEqual(
            ROUND300_REQUIRED_TARGET_ALIASES["ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B"],
            E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B.value,
        )

    def test_archetype_definitions_capture_r5_loop15_rules(self) -> None:
        k_food = archetype_definition(E2RArchetype.K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW)
        regulatory = archetype_definition(E2RArchetype.K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH)
        beauty = archetype_definition(E2RArchetype.K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE)
        apr = archetype_definition(E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE)
        ecommerce = archetype_definition(E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B)
        brand_ma = archetype_definition(E2RArchetype.BRAND_MA_CONTROL_RIGHTS_STAGE2)
        meme = archetype_definition(E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE)

        self.assertIn("ASP increase", k_food.stage2_candidate_signals)
        self.assertIn("ban reversal ignored after false-break relief", regulatory.false_positive_patterns)
        self.assertIn("physical retail talks", beauty.stage2_candidate_signals)
        self.assertIn("stock rises 3x to 4x before repeat purchase and margin proof", apr.stage4b_graduation_overheat_signals)
        self.assertIn("actual arrivals", tourism.stage3_high_conviction_signals)
        self.assertIn("data sharing restriction blocks monetization", ecommerce.stage4c_thesis_break_signals)
        self.assertIn("funding, control execution", brand_ma.stage3_high_conviction_signals)
        self.assertIn("not applicable without direct listed-company revenue evidence", meme.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round300_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND300_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round300_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_celebrity_policy_jv_or_ma_headline_as_green", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round300_summary()
        self.assertEqual(summary["round_id"], "round_228")
        self.assertEqual(summary["large_sector"], ROUND300_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 2)
        self.assertEqual(summary["stage3_green_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["missed_structural_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_brand_sales_from_headline(self) -> None:
        by_id = {case.case_id: case for case in ROUND300_CASE_CANDIDATES}
        samyang = by_id["r5_loop15_samyang_buldak_export"]
        nongshim = by_id["r5_loop15_nongshim_shinramyun_global"]
        beauty = by_id["r5_loop15_kbeauty_us_export_basket"]
        apr = by_id["r5_loop15_apr_medicube_beauty_device"]
        tourism = by_id["r5_loop15_china_tourist_visa_free_retail_basket"]
        ecommerce = by_id["r5_loop15_emart_shinsegae_alibaba_gmarket_jv"]
        fnf = by_id["r5_loop15_fnf_taylormade_brand_ma"]
        meme = by_id["r5_loop15_kyochon_cherrybro_jensen_meme"]

        self.assertEqual(samyang.primary_archetype, E2RArchetype.K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW)
        self.assertEqual(samyang.extra_price_metrics["q2_2024_op_estimate_yoy_pct"], 84)
        self.assertEqual(samyang.stage_candidate, "Stage3-Yellow")
        self.assertEqual(samyang.score_price_alignment, "missed_due_to_score")

        self.assertEqual(nongshim.primary_archetype, E2RArchetype.RAMEN_GLOBAL_EXPANSION_STAGE2)
        self.assertEqual(nongshim.extra_price_metrics["overseas_sales_share_pct"], 60)
        self.assertEqual(nongshim.stage_candidate, "Stage2")

        self.assertEqual(beauty.primary_archetype, E2RArchetype.K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE)
        self.assertEqual(beauty.extra_price_metrics["top5_korean_us_ecommerce_sales_growth_2y_pct"], 71)
        self.assertIn("physical_store_sellthrough_missing", beauty.red_flag_fields)

        self.assertEqual(apr.primary_archetype, E2RArchetype.BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B)
        self.assertEqual(apr.extra_price_metrics["stock_return_since_january_pct"], 300)
        self.assertEqual(apr.extra_price_metrics["overseas_revenue_share_q2_2025_pct"], 80)

        self.assertEqual(tourism.primary_archetype, E2RArchetype.CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE)
        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_event_return_pct"], 9.9)
        self.assertIn("spending_conversion_missing", tourism.red_flag_fields)

        self.assertEqual(ecommerce.primary_archetype, E2RArchetype.ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B)
        self.assertEqual(ecommerce.extra_price_metrics["data_sharing_restriction_years"], 3)
        self.assertEqual(ecommerce.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(fnf.primary_archetype, E2RArchetype.BRAND_MA_CONTROL_RIGHTS_STAGE2)
        self.assertEqual(fnf.extra_price_metrics["taylormade_possible_sale_value_usd_bn"], 3.5)

        self.assertEqual(meme.primary_archetype, E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE)
        self.assertFalse(meme.extra_price_metrics["direct_revenue_link_confirmed"])
        self.assertEqual(meme.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(meme.stage_failure_type, "false_green")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round300_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round300_shadow_weight_rows()}
        rules_md = render_round300_stage_rules_markdown()
        trigger_md = render_round300_trigger_grid_markdown()
        stage_md = render_round300_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND300_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r5l15_samyang_T1"]["promote_to"], "Stage3-Yellow")
        self.assertEqual(trigger_rows["r5l15_kyochon_T1"]["promote_to"], "N/A")
        self.assertEqual(trigger_rows["r5l15_emart_jv_T2"]["promote_to"], "Stage2")
        self.assertEqual(len(ROUND300_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW"]["export_shipment_growth"], "+5")
        self.assertEqual(shadow_rows["K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE"]["physical_retail_channel_entry"], "+5")
        self.assertEqual(shadow_rows["FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE"]["viral_celebrity_event_only_penalty"], "-5")
        self.assertIn("asp_increase_or_price_pass_through_visible", ROUND300_STAGE2_ACTIONABLE_RULES)
        self.assertIn("two_or_three_operating_numbers_change_eps_op_path", ROUND300_STAGE3_YELLOW_RULES)
        self.assertIn("offline_sellthrough_and_repeat_purchase_confirm", ROUND300_STAGE3_GREEN_RULES)
        self.assertIn("viral_celebrity_event_only", ROUND300_GREEN_BLOCKERS)
        self.assertIn("op_estimate_revision", ROUND300_SCORE_UP_AXES)
        self.assertIn("jv_without_data_rights", ROUND300_SCORE_DOWN_AXES)
        self.assertIn("sns_or_influencer_trigger_rallies_without_direct_sales", ROUND300_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("ecommerce_jv_data_regulation_blocks_monetization", ROUND300_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r5_loop15_samyang_buldak_export", trigger_md)
        self.assertIn("consumer headline", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round300_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_300.md")
        self.assertEqual(audit["round_id"], "round_228")
        self.assertEqual(audit["large_sector"], ROUND300_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_celebrity_meme_policy_jv_or_ma_optional_headline_as_green", audit["what_not_to_change"])

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
            paths = write_round300_r5_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round300_case_rows()
            self.assertEqual(len(records), len(ROUND300_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND300_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND300_TRIGGER_RECORDS))
            self.assertIn("Samyang", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r5l15_kyochon_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["q2_2024_op_estimate_yoy_pct"], 84)


if __name__ == "__main__":
    unittest.main()
