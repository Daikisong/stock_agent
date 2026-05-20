from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round248_r5_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round248_r5_loop11_consumer_retail_brand_price_validation import (
    ROUND248_CASE_CANDIDATES,
    ROUND248_GREEN_FORBIDDEN_PATTERNS,
    ROUND248_GREEN_REQUIRED_FIELDS,
    ROUND248_HARD_4C_GATES,
    ROUND248_LARGE_SECTOR,
    ROUND248_PRICE_VALIDATION_FIELDS,
    ROUND248_REQUIRED_TARGET_ALIASES,
    ROUND248_SCORE_ADJUSTMENTS,
    ROUND248_SHADOW_WEIGHT_ROWS,
    ROUND248_STAGE4B_WATCH_TRIGGERS,
    render_round248_green_gate_review_markdown,
    render_round248_stage4b_4c_review_markdown,
    round248_audit_payload,
    round248_case_records,
    round248_case_rows,
    round248_deep_sub_archetype_rows,
    round248_shadow_weight_rows,
    round248_summary,
    write_round248_r5_loop11_reports,
)


class Round248R5Loop11ConsumerRetailBrandPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND248_REQUIRED_TARGET_ALIASES), 12)
        self.assertTrue(set(ROUND248_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND248_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_RECURRING"],
            E2RArchetype.K_FOOD_EXPORT_RECURRING.value,
        )
        self.assertEqual(
            ROUND248_REQUIRED_TARGET_ALIASES["ECOMMERCE_TRUST_BREACH_HARD_4C"],
            E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C.value,
        )
        self.assertEqual(
            ROUND248_REQUIRED_TARGET_ALIASES["TOURISM_RETAIL_DUTYFREE_EVENT"],
            E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT.value,
        )

    def test_archetype_definitions_capture_round248_gates(self) -> None:
        food = archetype_definition(E2RArchetype.K_FOOD_EXPORT_RECURRING)
        staple = archetype_definition(E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND)
        device = archetype_definition(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND)
        ecommerce = archetype_definition(E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C)
        tourism = archetype_definition(E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT)

        self.assertIn("repeat demand", food.stage3_high_conviction_signals)
        self.assertIn("packaging/input shortage", food.stage4c_thesis_break_signals)
        self.assertIn("reorder repeat consumption", staple.stage3_high_conviction_signals)
        self.assertIn("revenue conversion", device.stage3_high_conviction_signals)
        self.assertIn("customer data breach", ecommerce.stage4c_thesis_break_signals)
        self.assertIn("tourist count without spend", tourism.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round248_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND248_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_brand_heat_tourism_policy_jv_or_viral_media_as_green", record.green_guardrails)

        summary = round248_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["hard_4c_krx_confirmed"])
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["watch_4c_count"], 3)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_food_and_kbeauty_cases_capture_price_anchors_without_inventing_ohlc(self) -> None:
        by_id = {case.case_id: case for case in ROUND248_CASE_CANDIDATES}
        samyang = by_id["r5_loop11_samyang_buldak_export_packaging_watch"]
        nongshim = by_id["r5_loop11_nongshim_shin_global_staple"]
        apr = by_id["r5_loop11_apr_medicube_structural_4b"]
        indie = by_id["r5_loop11_indie_kbeauty_odm_distribution_watch"]
        legacy = by_id["r5_loop11_amore_lghh_legacy_china_exposure"]

        self.assertEqual(samyang.primary_archetype, E2RArchetype.K_FOOD_EXPORT_RECURRING)
        self.assertEqual(samyang.stage3_date.isoformat(), "2024-06-14")
        self.assertEqual(samyang.stage3_price_anchor, 647000.0)
        self.assertEqual(samyang.extra_price_metrics["op_growth_estimate_pct"], 84.0)
        self.assertEqual(samyang.extra_price_metrics["target_upside_pct"], 28.3)
        self.assertIn("packaging_shortage_context", samyang.red_flag_fields)

        self.assertEqual(nongshim.primary_archetype, E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND)
        self.assertEqual(nongshim.extra_price_metrics["overseas_sales_share_pct"], 60.0)
        self.assertEqual(nongshim.stage_failure_type, "stage2_watch_success")

        self.assertEqual(apr.primary_archetype, E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND)
        self.assertEqual(apr.stage4b_date.isoformat(), "2025-07-08")
        self.assertGreater(apr.extra_price_metrics["q4_2025_overseas_growth_pct"], 200.0)
        self.assertIn("single_brand_device_concentration", apr.red_flag_fields)

        self.assertEqual(indie.primary_archetype, E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL)
        self.assertIn(E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE, indie.secondary_archetypes)
        self.assertEqual(indie.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("physical_store_sellthrough_missing", indie.red_flag_fields)

        self.assertEqual(legacy.primary_archetype, E2RArchetype.LEGACY_BEAUTY_CHINA_EXPOSURE_4C)
        self.assertEqual(legacy.rerating_result, "thesis_break")
        self.assertIn("china_demand_weakness", legacy.red_flag_fields)

    def test_ecommerce_trust_and_tourism_cases_keep_green_blocked(self) -> None:
        by_id = {case.case_id: case for case in ROUND248_CASE_CANDIDATES}
        jv = by_id["r5_loop11_emart_shinsegae_alibaba_jv_data_gate"]
        breach = by_id["r5_loop11_coupang_breach_ecommerce_trust_reference"]
        tourism = by_id["r5_loop11_tourism_retail_china_visa_event"]

        self.assertEqual(jv.primary_archetype, E2RArchetype.ECOMMERCE_JV_SCALE_AND_DATA_GATE)
        self.assertEqual(jv.extra_price_metrics["jv_structure"], "50:50 joint venture")
        self.assertEqual(jv.extra_price_metrics["growth_pct"], 32.0)
        self.assertIn("data_sharing_restriction_three_years", jv.red_flag_fields)

        self.assertEqual(breach.primary_archetype, E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C)
        self.assertTrue(breach.hard_4c_confirmed)
        self.assertFalse(breach.hard_4c_krx_direct)
        self.assertEqual(breach.stage4c_date.isoformat(), "2026-02-25")
        self.assertEqual(breach.extra_price_metrics["coupang_users_affected_mn"], 34.0)
        self.assertEqual(breach.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(tourism.primary_archetype, E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT)
        self.assertEqual(tourism.case_type, "event_premium")
        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_event_mfe_1d_pct"], 9.9)
        self.assertIn("tourist_spend_unconfirmed", tourism.red_flag_fields)

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND248_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND248_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND248_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND248_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round248_shadow_weight_rows()}
        deep_rows = round248_deep_sub_archetype_rows()
        green_markdown = render_round248_green_gate_review_markdown()
        stage_markdown = render_round248_stage4b_4c_review_markdown()

        self.assertIn("repeat_demand_confirmed", required)
        self.assertIn("channel_sellthrough_confirmed", required)
        self.assertIn("data_breach_or_trust_break", forbidden)
        self.assertIn("tourism_policy_only", forbidden)
        self.assertIn("ipo_or_debut_doubles_within_one_month", ROUND248_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("customer_data_breach", ROUND248_HARD_4C_GATES)
        self.assertIn("reported_price_anchor", fields)
        self.assertIn("channel_sellthrough", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("tourism visa-free policy", green_markdown)
        self.assertIn("r5_loop11_coupang_breach_ecommerce_trust_reference", stage_markdown)
        self.assertEqual(len(ROUND248_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["K_FOOD_EXPORT_RECURRING"]["repeat_demand"], "+5")
        self.assertEqual(shadow_rows["ECOMMERCE_TRUST_BREACH_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Buldak" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Coupang" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round248_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_248.md")
        self.assertEqual(audit["round_id"], "round_176")
        self.assertEqual(audit["large_sector"], ROUND248_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round248_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round248_r5_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round248_case_rows()
            self.assertEqual(len(records), len(ROUND248_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND248_CASE_CANDIDATES))
            self.assertIn("Samyang", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("repeat_demand_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("K_BEAUTY_DEVICE_GLOBAL_BRAND", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Coupang", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["op_growth_estimate_pct"], 84.0)


if __name__ == "__main__":
    unittest.main()
