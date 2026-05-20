from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round274_r5_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round274_r5_loop13_consumer_retail_brand_price_validation import (
    ROUND274_CASE_CANDIDATES,
    ROUND274_GREEN_FORBIDDEN_PATTERNS,
    ROUND274_GREEN_REQUIRED_FIELDS,
    ROUND274_HARD_4C_GATES,
    ROUND274_LARGE_SECTOR,
    ROUND274_PRICE_VALIDATION_FIELDS,
    ROUND274_REQUIRED_TARGET_ALIASES,
    ROUND274_SCORE_ADJUSTMENTS,
    ROUND274_SHADOW_WEIGHT_ROWS,
    ROUND274_STAGE4B_WATCH_TRIGGERS,
    render_round274_green_gate_review_markdown,
    render_round274_stage4b_4c_review_markdown,
    round274_audit_payload,
    round274_case_records,
    round274_case_rows,
    round274_deep_sub_archetype_rows,
    round274_shadow_weight_rows,
    round274_summary,
    write_round274_r5_loop13_reports,
)


class Round274R5Loop13ConsumerRetailBrandPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND274_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND274_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND274_REQUIRED_TARGET_ALIASES["K_BEAUTY_DEVICE_GLOBAL_BRAND_4B"],
            E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B.value,
        )
        self.assertEqual(
            ROUND274_REQUIRED_TARGET_ALIASES["INDIE_K_BEAUTY_US_RETAIL_CHANNEL"],
            E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL.value,
        )
        self.assertEqual(
            ROUND274_REQUIRED_TARGET_ALIASES["CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM"],
            E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM.value,
        )

    def test_archetype_definitions_encode_r5_loop13_gates(self) -> None:
        apr = archetype_definition(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B)
        indie = archetype_definition(E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL)
        hb = archetype_definition(E2RArchetype.H_AND_B_PLATFORM_GLOBALIZATION)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT)
        ecommerce = archetype_definition(E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE)
        grocery = archetype_definition(E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE)
        celebrity = archetype_definition(E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM)

        self.assertIn("repeat purchase or device replacement cycle", apr.stage3_high_conviction_signals)
        self.assertIn("channel talks without sell-through", indie.false_positive_patterns)
        self.assertIn("parent value bridge", hb.stage3_high_conviction_signals)
        self.assertIn("duty-free spend", tourism.stage3_high_conviction_signals)
        self.assertIn("data-governance clearance", ecommerce.stage3_high_conviction_signals)
        self.assertIn("liquidation value exceeds going-concern value", grocery.stage4c_thesis_break_signals)
        self.assertIn("famous-person restaurant visit treated as listed-company demand", celebrity.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round274_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND274_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round274_summary()
        self.assertEqual(summary["round_id"], "round_202")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_candidate_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["overheat_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["direct_listed_hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertFalse(summary["direct_listed_hard_4c_confirmed"])

    def test_apr_dalba_oliveyoung_and_samyang_capture_price_anchors(self) -> None:
        by_id = {case.case_id: case for case in ROUND274_CASE_CANDIDATES}
        apr = by_id["r5_loop13_apr_medicube_kbeauty_device_4b"]
        dalba = by_id["r5_loop13_dalba_indie_kbeauty_us_channel"]
        olive = by_id["r5_loop13_cj_olive_young_global_hb_platform"]
        samyang = by_id["r5_loop13_samyang_buldak_export_asp_capacity"]

        self.assertEqual(apr.primary_archetype, E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B)
        self.assertEqual(apr.extra_price_metrics["reported_stock_return_since_jan_2025_pct"], 300.0)
        self.assertEqual(apr.extra_price_metrics["market_value_usd_bn"], 6.0)
        self.assertEqual(apr.round_alignment_label, "aligned_partial_but_4B_watch")

        self.assertEqual(dalba.primary_archetype, E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL)
        self.assertEqual(dalba.extra_price_metrics["d_alba_post_debut_return_min_pct"], 100.0)
        self.assertEqual(dalba.extra_price_metrics["korean_vs_overall_growth_spread_pp"], 50.0)
        self.assertFalse(dalba.extra_price_metrics["actual_physical_store_sellthrough_confirmed"])

        self.assertEqual(olive.primary_archetype, E2RArchetype.H_AND_B_PLATFORM_GLOBALIZATION)
        self.assertEqual(olive.extra_price_metrics["olive_young_korea_store_count"], 1300)
        self.assertFalse(olive.extra_price_metrics["parent_value_bridge_confirmed"])

        self.assertEqual(samyang.primary_archetype, E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY)
        self.assertEqual(samyang.stage3_price_anchor, 647000.0)
        self.assertEqual(samyang.extra_price_metrics["target_upside_from_stage3_pct"], 28.3)
        self.assertEqual(samyang.extra_price_metrics["op_growth_estimate_pct"], 84.0)
        self.assertIn("denmark_recall_three_spicy_products", samyang.red_flag_fields)

    def test_tourism_ecommerce_homeplus_and_jensen_cases_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND274_CASE_CANDIDATES}
        tourism = by_id["r5_loop13_china_tourism_dutyfree_retail_event"]
        jv = by_id["r5_loop13_shinsegae_aliexpress_gmarket_data_gate"]
        homeplus = by_id["r5_loop13_homeplus_retail_credit_hard_reference"]
        jensen = by_id["r5_loop13_kyochon_cherrybro_neuromeka_jensen_event"]

        self.assertEqual(tourism.primary_archetype, E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT)
        self.assertEqual(tourism.extra_price_metrics["hyundai_department_store_mfe_pct"], 7.1)
        self.assertIn("tourist_arrival_headline_only", tourism.red_flag_fields)
        self.assertEqual(tourism.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(jv.primary_archetype, E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE)
        self.assertEqual(jv.extra_price_metrics["combined_market_share_overseas_online_shopping_pct"], 41.0)
        self.assertEqual(jv.extra_price_metrics["data_sharing_ban_years"], 3)
        self.assertIn("data_sharing_ban_three_years", jv.red_flag_fields)

        self.assertEqual(homeplus.primary_archetype, E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE)
        self.assertTrue(homeplus.hard_4c_confirmed)
        self.assertFalse(homeplus.direct_listed_hard_4c_confirmed)
        self.assertEqual(homeplus.extra_price_metrics["liquidation_value_krw_trn"], 3.7)
        self.assertEqual(homeplus.rerating_result, "thesis_break")

        self.assertEqual(jensen.primary_archetype, E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM)
        self.assertEqual(jensen.extra_price_metrics["kyochon_event_mfe_pct"], 20.0)
        self.assertEqual(jensen.extra_price_metrics["cherrybro_event_mfe_pct"], 30.0)
        self.assertFalse(jensen.extra_price_metrics["actual_restaurant_listed"])
        self.assertEqual(jensen.score_price_alignment, "price_moved_without_evidence")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND274_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND274_GREEN_FORBIDDEN_PATTERNS)
        review = render_round274_green_gate_review_markdown()
        stage_review = render_round274_stage4b_4c_review_markdown()
        fields = set(ROUND274_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND274_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round274_shadow_weight_rows()}
        deep_rows = round274_deep_sub_archetype_rows()

        self.assertIn("repeat_purchase_confirmed", required)
        self.assertIn("same_store_sales_confirmed", required)
        self.assertIn("data_governance_passed", required)
        self.assertIn("celebrity_event_only", forbidden)
        self.assertIn("tourist_arrival_headline_only", forbidden)
        self.assertIn("unlisted_subsidiary_readthrough_only", forbidden)
        self.assertIn("repeat_purchase", axes)
        self.assertIn("offline_retail_credit_stress", axes)
        self.assertIn("sellthrough_or_reorder_anchor", fields)
        self.assertIn("celebrity_food_service_event_plus_20_to_30pct", ROUND274_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("retail_credit_restructuring", ROUND274_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C", stage_review)
        self.assertEqual(len(ROUND274_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["INDIE_K_BEAUTY_US_RETAIL_CHANNEL"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CROSS_BORDER_ECOMMERCE_DATA_GATE"]["data_governance"], "+5")
        self.assertEqual(shadow_rows["CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertTrue(any("APR" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Homeplus" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Kyochon" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round274_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_274.md")
        self.assertEqual(audit["round_id"], "round_202")
        self.assertEqual(audit["large_sector"], ROUND274_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertFalse(audit["summary"]["direct_listed_hard_4c_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round274_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round274_r5_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            loaded = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(loaded), 8)
            self.assertTrue((root / "out" / "round274_r5_loop13_green_gate_review.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
