from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round242_r12_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round242_r12_loop10_agri_life_service_misc_price_validation import (
    ROUND242_CASE_CANDIDATES,
    ROUND242_DEFAULT_STAGE3_BIAS,
    ROUND242_GREEN_FORBIDDEN_PATTERNS,
    ROUND242_GREEN_REQUIRED_FIELDS,
    ROUND242_HARD_4C_GATES,
    ROUND242_PRICE_VALIDATION_FIELDS,
    ROUND242_REQUIRED_TARGET_ALIASES,
    ROUND242_SCORE_ADJUSTMENTS,
    ROUND242_SHADOW_WEIGHT_ROWS,
    ROUND242_STAGE4B_WATCH_TRIGGERS,
    render_round242_green_gate_review_markdown,
    render_round242_stage4b_4c_review_markdown,
    round242_audit_payload,
    round242_case_records,
    round242_case_rows,
    round242_deep_sub_archetype_rows,
    round242_shadow_weight_rows,
    round242_summary,
    write_round242_r12_loop10_reports,
)


class Round242R12Loop10AgriLifeServiceMiscPriceValidationTests(unittest.TestCase):
    def test_round242_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND242_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND242_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND242_REQUIRED_TARGET_ALIASES["HOME_LIVING_RENTAL_RECURRING"],
            E2RArchetype.HOME_LIVING_RENTAL_RECURRING.value,
        )
        self.assertEqual(
            ROUND242_REQUIRED_TARGET_ALIASES["EDUCATION_POLICY_MEDICAL_QUOTA"],
            E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA.value,
        )
        self.assertEqual(
            ROUND242_REQUIRED_TARGET_ALIASES["FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM"],
            E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM.value,
        )

    def test_case_records_validate_and_keep_non_production_guardrails(self) -> None:
        records = round242_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.EDUCATION_LIFE_AGRI_MISC.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("r12_default_stage3_bias_conservative_except_verified_recurring_service", record.green_guardrails)

        summary = round242_summary()
        self.assertEqual(summary["analyst_round_id"], "round_170")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 3)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["r12_default_stage3_bias"], ROUND242_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_round242_archetype_definitions_are_available(self) -> None:
        rental = archetype_definition(E2RArchetype.HOME_LIVING_RENTAL_RECURRING)
        quota = archetype_definition(E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA)
        edtech = archetype_definition(E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL)
        celebrity = archetype_definition(E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM)

        self.assertIn(
            "recurring revenue, churn stability, ARPU, overseas growth, and FCF conversion all verified",
            rental.stage3_high_conviction_signals,
        )
        self.assertIn("medical quota headline treated as company revenue", quota.false_positive_patterns)
        self.assertIn("official textbook status removed", edtech.stage4c_thesis_break_signals)
        self.assertIn("stock jumps 20-30% before revenue evidence", celebrity.stage4b_graduation_overheat_signals)

    def test_coway_is_recurring_candidate_but_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND242_CASE_CANDIDATES}
        coway = by_id["r12_loop10_coway_recurring_rental_watch"]

        self.assertEqual(coway.primary_archetype, E2RArchetype.HOME_LIVING_RENTAL_RECURRING)
        self.assertIsNone(coway.stage3_date)
        self.assertEqual(coway.round_score_price_alignment, "success_candidate")
        self.assertIn("Malaysia", coway.extra_price_metrics["overseas_subsidiaries"])
        self.assertIn("churn_unverified", coway.red_flag_fields)
        self.assertIn("fcf_unverified", coway.red_flag_fields)

    def test_education_and_edtech_policy_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND242_CASE_CANDIDATES}
        quota = by_id["r12_loop10_medical_quota_private_education_watch"]
        edtech = by_id["r12_loop10_edtech_ai_textbook_rollback_phone_ban"]

        self.assertEqual(quota.primary_archetype, E2RArchetype.EDUCATION_POLICY_MEDICAL_QUOTA)
        self.assertEqual(quota.stage2_date.isoformat(), "2026-02-10")
        self.assertEqual(quota.extra_price_metrics["quota_2027"], 3548.0)
        self.assertEqual(quota.extra_price_metrics["quota_increase_2027_pct"], 16.0)
        self.assertEqual(quota.extra_price_metrics["quota_2030"], 3871.0)
        self.assertEqual(quota.extra_price_metrics["quota_increase_2030_pct"], 26.6)
        self.assertIn("education_quota_only", quota.red_flag_fields)

        self.assertEqual(edtech.primary_archetype, E2RArchetype.EDTECH_AI_TEXTBOOK_POLICY_REVERSAL)
        self.assertEqual(edtech.stage4c_date.isoformat(), "2025-08-01")
        self.assertEqual(edtech.extra_price_metrics["phone_device_ban_effective"], "2026-03")
        self.assertEqual(edtech.extra_price_metrics["students_social_media_affects_daily_life_pct"], 37.0)
        self.assertEqual(edtech.extra_price_metrics["students_anxious_without_social_media_pct"], 22.0)
        self.assertIn("ai_textbook_theme_only", edtech.red_flag_fields)

    def test_childcare_pet_and_input_cost_cases_are_policy_or_4c_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND242_CASE_CANDIDATES}
        childcare = by_id["r12_loop10_childcare_fertility_policy_watch"]
        kimchi = by_id["r12_loop10_kimchi_cabbage_input_cost_watch"]
        feed = by_id["r12_loop10_feed_wheat_livestock_input_cost_watch"]
        dog = by_id["r12_loop10_dog_meat_ban_pet_welfare_transition"]

        self.assertEqual(childcare.primary_archetype, E2RArchetype.CHILDCARE_DEMOGRAPHIC_POLICY_EVENT)
        self.assertEqual(childcare.extra_price_metrics["fertility_rate_2023"], 0.72)
        self.assertEqual(childcare.extra_price_metrics["fertility_rate_2025"], 0.80)
        self.assertEqual(childcare.extra_price_metrics["marriages_2025_growth_pct"], 8.1)
        self.assertEqual(childcare.extra_price_metrics["births_2025_growth_pct"], 6.8)
        self.assertEqual(childcare.extra_price_metrics["foreign_housekeeper_pilot_workers"], 100.0)
        self.assertEqual(childcare.extra_price_metrics["possible_expansion_workers"], 1200.0)
        self.assertIn("birthrate_headline_only", childcare.red_flag_fields)

        self.assertEqual(kimchi.primary_archetype, E2RArchetype.AGRI_FOOD_INPUT_COST_SHOCK)
        self.assertEqual(kimchi.extra_price_metrics["government_cabbage_release_tonnes"], 24000.0)
        self.assertEqual(kimchi.extra_price_metrics["cabbage_price_jump_pct"], 217.9)
        self.assertEqual(kimchi.extra_price_metrics["area_decline_pct"], -54.6)
        self.assertIn("input_price_spike_without_pass_through", kimchi.red_flag_fields)

        self.assertEqual(feed.primary_archetype, E2RArchetype.FEED_GRAIN_INPUT_COST_4C)
        self.assertEqual(feed.extra_price_metrics["tender_volume_tonnes"], 65000.0)
        self.assertEqual(feed.extra_price_metrics["effective_lowest_offer_usd_per_t"], 300.5)
        self.assertEqual(feed.extra_price_metrics["effective_offer_for_65000t_usd_mn"], 19.53)
        self.assertIn("feed_cost_spike_without_pass_through", feed.red_flag_fields)

        self.assertEqual(dog.primary_archetype, E2RArchetype.PET_WELFARE_POLICY_TRANSITION)
        self.assertEqual(dog.stage2_date.isoformat(), "2027-02-01")
        self.assertEqual(dog.extra_price_metrics["government_support_krw_bn"], 100.0)
        self.assertEqual(dog.extra_price_metrics["dogs_to_rehome"], 500000.0)
        self.assertEqual(dog.extra_price_metrics["farmer_subsidy_per_dog_krw"], 600000.0)
        self.assertIn("pet_welfare_policy_only", dog.red_flag_fields)

    def test_celebrity_food_event_is_price_moved_without_evidence(self) -> None:
        by_id = {case.case_id: case for case in ROUND242_CASE_CANDIDATES}
        chicken = by_id["r12_loop10_kyochon_cherrybro_neuromeka_jensen_event"]

        self.assertEqual(chicken.primary_archetype, E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM)
        self.assertEqual(chicken.stage4b_date.isoformat(), "2025-10-31")
        self.assertEqual(chicken.mfe_1d, 30.0)
        self.assertEqual(chicken.extra_price_metrics["kyochon_event_mfe_pct"], 20.0)
        self.assertEqual(chicken.extra_price_metrics["cherrybro_event_mfe_pct"], 30.0)
        self.assertEqual(chicken.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("celebrity_food_event_only", chicken.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND242_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND242_GREEN_FORBIDDEN_PATTERNS)
        review = render_round242_green_gate_review_markdown()
        stage_review = render_round242_stage4b_4c_review_markdown()
        fields = set(ROUND242_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND242_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round242_shadow_weight_rows()}
        deep_rows = round242_deep_sub_archetype_rows()

        self.assertIn("recurring_revenue_or_repeat_purchase_confirmed", required)
        self.assertIn("paid_enrollment_or_utilization_confirmed", required)
        self.assertIn("input_cost_pass_through_confirmed", required)
        self.assertIn("education_quota_only", forbidden)
        self.assertIn("celebrity_food_event_only", forbidden)
        self.assertIn("agri_input_price_spike_only", forbidden)
        self.assertIn("recurring_revenue", axes)
        self.assertIn("celebrity_food_event_only", axes)
        self.assertIn("reported_return_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("celebrity_food_event_plus_20_to_30pct_without_sales", ROUND242_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("feed_cost_shock", ROUND242_HARD_4C_GATES)
        self.assertIn("celebrity_event_fade", ROUND242_HARD_4C_GATES)
        self.assertEqual(len(ROUND242_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["HOME_LIVING_RENTAL_RECURRING"]["recurring_revenue"], "+5")
        self.assertEqual(shadow_rows["FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertTrue(any("Coway" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Jensen Huang chicken event" in row["terms"] for row in deep_rows))
        self.assertIn("r12_loop10_kyochon_cherrybro_neuromeka_jensen_event", stage_review)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round242_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_242.md")
        self.assertEqual(audit["analyst_round_id"], "round_170")
        self.assertEqual(audit["raw_large_sector_label"], "AGRI_LIFE_SERVICE_MISC")
        self.assertEqual(audit["large_sector"], Round10LargeSector.EDUCATION_LIFE_AGRI_MISC.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertEqual(audit["summary"]["r12_default_stage3_bias"], "conservative_except_verified_recurring_service")
        self.assertIn("do_not_use_round242_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round242_r12_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round242_case_rows()
            self.assertEqual(len(records), len(ROUND242_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND242_CASE_CANDIDATES))
            self.assertIn("Coway", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("recurring_revenue", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("HOME_LIVING_RENTAL_RECURRING", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Jensen Huang chicken event", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[-1]["extra_price_metrics"])["cherrybro_event_mfe_pct"], 30.0)


if __name__ == "__main__":
    unittest.main()
