from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round268_r12_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round268_r12_loop12_agri_life_service_misc_price_validation import (
    ROUND268_CASE_CANDIDATES,
    ROUND268_DEFAULT_STAGE3_BIAS,
    ROUND268_GREEN_FORBIDDEN_PATTERNS,
    ROUND268_GREEN_REQUIRED_FIELDS,
    ROUND268_HARD_4C_GATES,
    ROUND268_PRICE_VALIDATION_FIELDS,
    ROUND268_REQUIRED_TARGET_ALIASES,
    ROUND268_SCORE_ADJUSTMENTS,
    ROUND268_SHADOW_WEIGHT_ROWS,
    ROUND268_STAGE4B_WATCH_TRIGGERS,
    render_round268_green_gate_review_markdown,
    render_round268_stage4b_4c_review_markdown,
    round268_audit_payload,
    round268_case_records,
    round268_case_rows,
    round268_deep_sub_archetype_rows,
    round268_shadow_weight_rows,
    round268_summary,
    write_round268_r12_loop12_reports,
)


class Round268R12Loop12AgriLifeServiceMiscPriceValidationTests(unittest.TestCase):
    def test_round268_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND268_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND268_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND268_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION"],
            E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION.value,
        )
        self.assertEqual(
            ROUND268_REQUIRED_TARGET_ALIASES["EDUCATION_POLICY_MEDICAL_QUOTA_EVENT"],
            E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT.value,
        )
        self.assertEqual(
            ROUND268_REQUIRED_TARGET_ALIASES["PET_WELFARE_TRANSITION_POLICY_EVENT"],
            E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT.value,
        )
        self.assertEqual(
            ROUND268_REQUIRED_TARGET_ALIASES["FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM"],
            E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round268_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.EDUCATION_LIFE_AGRI_MISC.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)
            self.assertIn(
                "do_not_treat_k_food_education_childcare_pet_or_celebrity_headline_as_green",
                record.green_guardrails,
            )

        summary = round268_summary()
        self.assertEqual(summary["analyst_round_id"], "round_196")
        self.assertEqual(summary["raw_large_sector_label"], "AGRI_LIFE_SERVICE_MISC")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 3)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["r12_default_stage3_bias"], ROUND268_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_round268_archetype_definitions_encode_green_gates(self) -> None:
        k_food = archetype_definition(E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION)
        quota = archetype_definition(E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT)
        edtech = archetype_definition(E2RArchetype.EDTECH_POLICY_ROLLBACK_4C)
        childcare = archetype_definition(E2RArchetype.CHILDCARE_FOREIGN_HELPER_POLICY_EVENT)
        pet = archetype_definition(E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT)
        celebrity = archetype_definition(E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM)

        self.assertIn(
            "overseas sell-through, repeat purchase, ASP, capacity utilization, margin, FCF and price path all verified",
            k_food.stage3_high_conviction_signals,
        )
        self.assertIn("medical quota headline treated as paid enrollment revenue", quota.false_positive_patterns)
        self.assertIn("classroom phone/device ban", edtech.stage4c_thesis_break_signals)
        self.assertIn(
            "paid care demand, utilization, margin, repeat service, subsidy independence, and cash conversion verified",
            childcare.stage3_high_conviction_signals,
        )
        self.assertIn("dog-meat ban policy treated as pet-food revenue", pet.false_positive_patterns)
        self.assertIn("stock jumps 20-30% before revenue evidence", celebrity.stage4b_graduation_overheat_signals)

    def test_nongshim_is_stage2_export_capacity_candidate_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND268_CASE_CANDIDATES}
        nongshim = by_id["r12_loop12_nongshim_shin_export_capacity"]

        self.assertEqual(nongshim.primary_archetype, E2RArchetype.K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION)
        self.assertIsNone(nongshim.stage3_date)
        self.assertEqual(nongshim.stage2_date.isoformat(), "2024-05-27")
        self.assertEqual(nongshim.extra_price_metrics["shin_ramyun_2023_sales_krw_trn"], 1.2)
        self.assertEqual(nongshim.extra_price_metrics["overseas_sales_share_pct"], 60.0)
        self.assertEqual(nongshim.extra_price_metrics["us_market_share_pct"], 25.4)
        self.assertEqual(nongshim.extra_price_metrics["us_target_growth_from_2023_na_sales_pct"], 178.8)
        self.assertIn("margin_fcf_unverified", nongshim.red_flag_fields)

    def test_input_cost_and_policy_rollback_cases_are_4c_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND268_CASE_CANDIDATES}
        kimchi = by_id["r12_loop12_kimchi_cabbage_input_cost_watch"]
        feed = by_id["r12_loop12_feed_wheat_livestock_cost_watch"]
        edtech = by_id["r12_loop12_ai_textbook_edtech_policy_rollback"]

        self.assertEqual(kimchi.primary_archetype, E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK)
        self.assertEqual(kimchi.stage4c_date.isoformat(), "2024-10-23")
        self.assertEqual(kimchi.extra_price_metrics["cabbage_price_jump_pct"], 217.9)
        self.assertEqual(kimchi.extra_price_metrics["late_oct_vs_mid_sept_pct"], -41.2)
        self.assertIn("raw_material_price_spike_without_pass_through", kimchi.red_flag_fields)

        self.assertEqual(feed.primary_archetype, E2RArchetype.FEED_GRAIN_INPUT_COST_4C)
        self.assertEqual(feed.stage4c_date.isoformat(), "2026-05-13")
        self.assertEqual(feed.extra_price_metrics["tender_volume_tonnes"], 65000.0)
        self.assertEqual(feed.extra_price_metrics["effective_lowest_offer_usd_per_t"], 300.5)
        self.assertIn("feed_cost_spike_without_inventory_buffer", feed.red_flag_fields)

        self.assertEqual(edtech.primary_archetype, E2RArchetype.EDTECH_POLICY_ROLLBACK_4C)
        self.assertEqual(edtech.stage4c_date.isoformat(), "2025-08-04")
        self.assertEqual(edtech.extra_price_metrics["teacher_unprepared_share_pct"], 87.4)
        self.assertEqual(edtech.extra_price_metrics["classroom_phone_device_ban_effective"], "2026-03")
        self.assertIn("policy_rollback", edtech.red_flag_fields)

    def test_education_childcare_pet_and_celebrity_events_remain_non_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND268_CASE_CANDIDATES}
        quota = by_id["r12_loop12_medical_quota_private_education_event"]
        childcare = by_id["r12_loop12_childcare_foreign_helper_fertility_policy"]
        dog = by_id["r12_loop12_dog_meat_ban_pet_welfare_transition"]
        chicken = by_id["r12_loop12_kyochon_cherrybro_neuromeka_jensen_event"]

        self.assertEqual(quota.primary_archetype, E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA_EVENT)
        self.assertEqual(quota.extra_price_metrics["quota_increase_2030_pct"], 26.6)
        self.assertEqual(quota.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("paid_enrollment_unverified", quota.red_flag_fields)

        self.assertEqual(childcare.primary_archetype, E2RArchetype.CHILDCARE_FOREIGN_HELPER_POLICY_EVENT)
        self.assertEqual(childcare.extra_price_metrics["pilot_expansion_multiple"], 12.0)
        self.assertEqual(childcare.extra_price_metrics["fertility_rebound_2023_to_2025_pct"], 11.1)
        self.assertIn("paid_household_demand_unverified", childcare.red_flag_fields)

        self.assertEqual(dog.primary_archetype, E2RArchetype.PET_WELFARE_TRANSITION_POLICY_EVENT)
        self.assertEqual(dog.stage2_date.isoformat(), "2027-02-01")
        self.assertEqual(dog.extra_price_metrics["potential_subsidy_liability_if_all_dogs_max_krw_bn"], 300.0)
        self.assertEqual(dog.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("pet_service_revenue_unverified", dog.red_flag_fields)

        self.assertEqual(chicken.primary_archetype, E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM)
        self.assertEqual(chicken.stage4b_date.isoformat(), "2025-10-31")
        self.assertEqual(chicken.extra_price_metrics["kyochon_event_mfe_pct"], 20.0)
        self.assertEqual(chicken.extra_price_metrics["cherrybro_event_mfe_pct"], 30.0)
        self.assertEqual(chicken.score_price_alignment, "price_moved_without_evidence")
        self.assertFalse(chicken.extra_price_metrics["same_store_sales_confirmed"])

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND268_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND268_GREEN_FORBIDDEN_PATTERNS)
        review = render_round268_green_gate_review_markdown()
        stage_review = render_round268_stage4b_4c_review_markdown()
        fields = set(ROUND268_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND268_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round268_shadow_weight_rows()}
        deep_rows = round268_deep_sub_archetype_rows()

        self.assertIn("repeat_purchase_or_repeat_service_usage_confirmed", required)
        self.assertIn("paid_enrollment_or_paid_household_usage_confirmed", required)
        self.assertIn("input_cost_pass_through_confirmed", required)
        self.assertIn("cash_conversion_confirmed", required)
        self.assertIn("medical_quota_only", forbidden)
        self.assertIn("fertility_headline_only", forbidden)
        self.assertIn("celebrity_food_event_only", forbidden)
        self.assertIn("repeat_purchase", axes)
        self.assertIn("policy_headline_only", axes)
        self.assertIn("mfe_event", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("medical quota + education basket rally", review)
        self.assertIn("celebrity_food_event_stock_spike_without_sales", ROUND268_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("policy_rollback", ROUND268_HARD_4C_GATES)
        self.assertIn("celebrity_event_fade", ROUND268_HARD_4C_GATES)
        self.assertEqual(len(ROUND268_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(
            shadow_rows["K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION"]["overseas_sell_through"],
            "+5",
        )
        self.assertEqual(shadow_rows["EDUCATION_POLICY_MEDICAL_QUOTA_EVENT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertTrue(any("Nongshim Shin Ramyun" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Jensen Huang chicken event" in row["terms"] for row in deep_rows))
        self.assertIn("r12_loop12_kyochon_cherrybro_neuromeka_jensen_event", stage_review)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round268_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_268.md")
        self.assertEqual(audit["analyst_round_id"], "round_196")
        self.assertEqual(audit["raw_large_sector_label"], "AGRI_LIFE_SERVICE_MISC")
        self.assertEqual(audit["large_sector"], Round10LargeSector.EDUCATION_LIFE_AGRI_MISC.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertEqual(
            audit["summary"]["r12_default_stage3_bias"],
            "conservative_until_repeat_purchase_paid_conversion_and_cash_conversion",
        )
        self.assertIn("do_not_use_round268_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round268_r12_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round268_case_rows()
            self.assertEqual(len(records), len(ROUND268_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND268_CASE_CANDIDATES))
            self.assertIn("Nongshim", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("repeat_purchase", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Jensen Huang chicken event", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[-1]["extra_price_metrics"])["cherrybro_event_mfe_pct"], 30.0)


if __name__ == "__main__":
    unittest.main()
