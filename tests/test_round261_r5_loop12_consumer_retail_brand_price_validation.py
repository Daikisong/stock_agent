from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round261_r5_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round261_r5_loop12_consumer_retail_brand_price_validation import (
    ROUND261_CASE_CANDIDATES,
    ROUND261_GREEN_FORBIDDEN_PATTERNS,
    ROUND261_GREEN_REQUIRED_FIELDS,
    ROUND261_HARD_4C_GATES,
    ROUND261_LARGE_SECTOR,
    ROUND261_PRICE_VALIDATION_FIELDS,
    ROUND261_REQUIRED_TARGET_ALIASES,
    ROUND261_SCORE_ADJUSTMENTS,
    ROUND261_SHADOW_WEIGHT_ROWS,
    ROUND261_STAGE4B_WATCH_TRIGGERS,
    render_round261_green_gate_review_markdown,
    render_round261_stage4b_4c_review_markdown,
    round261_audit_payload,
    round261_case_records,
    round261_case_rows,
    round261_deep_sub_archetype_rows,
    round261_shadow_weight_rows,
    round261_summary,
    write_round261_r5_loop12_reports,
)


class Round261R5Loop12ConsumerRetailBrandPriceValidationTests(unittest.TestCase):
    def test_round261_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND261_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND261_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND261_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_ASP_CAPACITY"],
            E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY.value,
        )
        self.assertEqual(
            ROUND261_REQUIRED_TARGET_ALIASES["H_AND_B_RETAIL_GLOBAL_PLATFORM"],
            E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM.value,
        )
        self.assertEqual(
            ROUND261_REQUIRED_TARGET_ALIASES["OFFLINE_GROCERY_DISTRESS_4C"],
            E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C.value,
        )
        self.assertEqual(
            ROUND261_REQUIRED_TARGET_ALIASES["FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM"],
            E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM.value,
        )

    def test_round261_archetype_definitions_capture_green_guards(self) -> None:
        kfood = archetype_definition(E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY)
        hb = archetype_definition(E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM)
        mna = archetype_definition(E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION)
        ecommerce = archetype_definition(E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE)
        grocery = archetype_definition(E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C)

        self.assertIn("export + ASP + OP revision + capacity expansion all visible", kfood.stage3_high_conviction_signals)
        self.assertIn("physical-store sell-through", hb.stage3_high_conviction_signals)
        self.assertIn("M&A validation without listed-stock revenue bridge", mna.false_positive_patterns)
        self.assertIn("data compliance", ecommerce.stage3_high_conviction_signals)
        self.assertIn("liquidation value exceeds going-concern value", grocery.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round261_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND261_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_k_food_k_beauty_mna_store_plan_jv_or_celebrity_event_as_green_alone", record.green_guardrails)

        summary = round261_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["thesis_break_reference_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["direct_krx_hard_4c_confirmed"])
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["reported_price_anchor_count"], 5)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_samyang_and_consumer_success_candidates_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND261_CASE_CANDIDATES}
        samyang = by_id["r5_loop12_samyang_buldak_export_asp_capacity"]
        olive = by_id["r5_loop12_cj_olive_young_hb_global_platform"]
        drg = by_id["r5_loop12_dr_g_loreal_kbeauty_brand_mna_validation"]

        self.assertEqual(samyang.primary_archetype, E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY)
        self.assertEqual(samyang.stage3_date.isoformat(), "2024-06-14")
        self.assertEqual(samyang.stage3_price_anchor, 647000.0)
        self.assertEqual(samyang.extra_price_metrics["target_upside_from_stage3_price_pct"], 28.3)
        self.assertIn("single_sku_concentration", samyang.red_flag_fields)

        self.assertEqual(olive.primary_archetype, E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM)
        self.assertIsNone(olive.stage3_date)
        self.assertIn("parent_earnings_bridge_absent", olive.red_flag_fields)

        self.assertEqual(drg.primary_archetype, E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION)
        self.assertEqual(drg.extra_price_metrics["mibelle_2023_revenue_chf_mn"], 661.0)
        self.assertEqual(drg.rerating_result, "event_premium")

    def test_physical_store_data_gate_distress_and_event_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND261_CASE_CANDIDATES}
        dalba = by_id["r5_loop12_dalba_silicon2_cosmax_kolmar_physical_store_test"]
        emart = by_id["r5_loop12_emart_shinsegae_alibaba_jv_data_gate"]
        homeplus = by_id["r5_loop12_homeplus_mbk_offline_grocery_distress_reference"]
        kyochon = by_id["r5_loop12_kyochon_cherrybro_neuromeka_jensen_event"]

        self.assertEqual(dalba.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(dalba.extra_price_metrics["relative_growth_multiple"], 3.38)
        self.assertIn("physical_store_sell_through_unconfirmed", dalba.red_flag_fields)

        self.assertEqual(emart.primary_archetype, E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE)
        self.assertEqual(emart.extra_price_metrics["expected_cross_border_market_share_pct"], 41.0)
        self.assertIn("customer_data_risk", emart.red_flag_fields)

        self.assertTrue(homeplus.hard_4c_confirmed)
        self.assertFalse(homeplus.direct_krx_hard_4c_confirmed)
        self.assertEqual(homeplus.rerating_result, "thesis_break")
        self.assertEqual(homeplus.extra_price_metrics["liquidation_value_to_assets_pct"], 54.4)

        self.assertEqual(kyochon.primary_archetype, E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM)
        self.assertEqual(kyochon.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(kyochon.extra_price_metrics["cherrybro_event_mfe_pct"], 30.0)
        self.assertIn("same_store_sales_absent", kyochon.red_flag_fields)

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND261_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND261_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND261_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND261_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round261_shadow_weight_rows()}
        deep_rows = round261_deep_sub_archetype_rows()
        green_markdown = render_round261_green_gate_review_markdown()
        stage_markdown = render_round261_stage4b_4c_review_markdown()

        self.assertIn("repeat_purchase_or_repeat_demand_confirmed", required)
        self.assertIn("customer_data_and_platform_trust_risk_passed", required)
        self.assertIn("celebrity_food_event_only", forbidden)
        self.assertIn("offline_asset_value_only", forbidden)
        self.assertIn("celebrity_event_plus_20_30pct", ROUND261_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("offline_grocery_court_led_restructuring", ROUND261_HARD_4C_GATES)
        self.assertIn("data_or_trust_gate", fields)
        self.assertIn("M&A_validation_without_revenue", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("celebrity fried-chicken event", green_markdown)
        self.assertIn("r5_loop12_homeplus_mbk_offline_grocery_distress_reference", stage_markdown)
        self.assertEqual(len(ROUND261_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["ECOMMERCE_JV_SCALE_DATA_GATE"]["data_compliance"], "+5")
        self.assertEqual(shadow_rows["FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertTrue(any("Samyang" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Kkanbu" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round261_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_261.md")
        self.assertEqual(audit["round_id"], "round_189")
        self.assertEqual(audit["large_sector"], ROUND261_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round261_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round261_r5_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round261_case_rows()
            self.assertEqual(len(records), len(ROUND261_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND261_CASE_CANDIDATES))
            self.assertIn("Samyang", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("repeat_purchase_or_repeat_demand_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("ECOMMERCE_JV_SCALE_DATA_GATE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("platform_or_channel_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["target_price_krw"], 830000)


if __name__ == "__main__":
    unittest.main()
