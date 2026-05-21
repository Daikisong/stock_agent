from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round320_r12_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round320_r12_loop16_agriculture_life_services_misc_trigger_validation import (
    ROUND320_CASE_CANDIDATES,
    ROUND320_GREEN_BLOCKERS,
    ROUND320_HARD_4C_GATES,
    ROUND320_LARGE_SECTOR,
    ROUND320_REQUIRED_TARGET_ALIASES,
    ROUND320_ROW_SEPARATION_RULES,
    ROUND320_SCORE_DOWN_AXES,
    ROUND320_SCORE_UP_AXES,
    ROUND320_SHADOW_WEIGHT_ROWS,
    ROUND320_STAGE2_ACTIONABLE_RULES,
    ROUND320_STAGE3_GREEN_RULES,
    ROUND320_STAGE3_YELLOW_RULES,
    ROUND320_STAGE4B_WATCH_TRIGGERS,
    ROUND320_TRIGGER_RECORDS,
    render_round320_stage_rules_markdown,
    render_round320_stage4b_4c_review_markdown,
    render_round320_trigger_grid_markdown,
    round320_audit_payload,
    round320_case_records,
    round320_case_rows,
    round320_shadow_weight_rows,
    round320_summary,
    round320_trigger_rows,
    write_round320_r12_loop16_reports,
)


class Round320R12Loop16AgricultureLifeServicesTests(unittest.TestCase):
    def test_round320_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND320_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND320_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND320_REQUIRED_TARGET_ALIASES["FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B"],
            E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B.value,
        )
        self.assertEqual(
            ROUND320_REQUIRED_TARGET_ALIASES["EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C"],
            E2RArchetype.EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C.value,
        )
        self.assertEqual(
            ROUND320_REQUIRED_TARGET_ALIASES["MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF"],
            E2RArchetype.MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF.value,
        )

    def test_archetype_definitions_capture_r12_loop16_rules(self) -> None:
        ma = archetype_definition(E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B)
        security = archetype_definition(E2RArchetype.EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C)
        food = archetype_definition(E2RArchetype.FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B)
        feed = archetype_definition(E2RArchetype.FEED_WHEAT_COST_SHOCK_4B)
        pet = archetype_definition(E2RArchetype.PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE)
        education = archetype_definition(E2RArchetype.EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE)
        fertility = archetype_definition(E2RArchetype.FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE)
        medical = archetype_definition(E2RArchetype.MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF)

        self.assertIn("final SPA", " ".join(ma.stage3_high_conviction_signals))
        self.assertIn("GMV", " ".join(ma.stage3_high_conviction_signals))
        self.assertIn("take-rate", " ".join(ma.stage3_high_conviction_signals))
        self.assertIn("approval", " ".join(ma.stage3_high_conviction_signals))
        self.assertIn("data breach", " ".join(security.stage1_radar_signals))
        self.assertIn("GMV", " ".join(security.stage2_candidate_signals))
        self.assertIn("spending", " ".join(security.stage2_candidate_signals))
        self.assertIn("margin", " ".join(security.stage2_candidate_signals))
        self.assertIn("pass-through", " ".join(food.stage3_high_conviction_signals))
        self.assertIn("volume elasticity", " ".join(food.stage2_candidate_signals))
        self.assertIn("gross margin", " ".join(food.stage3_high_conviction_signals))
        self.assertIn("feed wheat", " ".join(feed.stage1_radar_signals))
        self.assertIn("cost shock", " ".join(feed.stage1_radar_signals))
        self.assertIn("pass-through", " ".join(feed.stage3_high_conviction_signals))
        self.assertIn("dog-meat ban", " ".join(pet.stage1_radar_signals))
        self.assertIn("listed pet-food", " ".join(pet.stage2_candidate_signals))
        self.assertIn("vet service", " ".join(pet.stage2_candidate_signals))
        self.assertIn("CSAT", " ".join(education.stage1_radar_signals))
        self.assertIn("ARPU", " ".join(education.stage2_candidate_signals))
        self.assertIn("cohort", " ".join(education.stage1_radar_signals))
        self.assertIn("fertility", " ".join(fertility.stage1_radar_signals))
        self.assertIn("multi-year", " ".join(fertility.stage3_high_conviction_signals))
        self.assertIn("childcare revenue", " ".join(fertility.stage2_candidate_signals))
        self.assertIn("medical student", " ".join(medical.stage1_radar_signals))
        self.assertIn("service normalization", " ".join(medical.stage2_candidate_signals))
        self.assertIn("trainee return", " ".join(medical.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round320_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND320_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round320_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_life_service_agri_education_pet_or_demographic_headline_as_Green_without_final_approval_revenue_margin_ARPU_pass_through_or_service_normalization",
                record.green_guardrails,
            )

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r12_loop16_baemin_naver_uber_food_delivery_ma"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r12_loop16_coupang_everyday_delivery_share_shift"].green_guardrails)

        summary = round320_summary()
        self.assertEqual(summary["round_id"], "round_248")
        self.assertEqual(summary["large_sector"], ROUND320_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 0)
        self.assertEqual(summary["stage2_candidate_count"], 6)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 5)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_life_service_agri_pet_education_and_medical_triggers(self) -> None:
        by_id = {case.case_id: case for case in ROUND320_CASE_CANDIDATES}
        baemin = by_id["r12_loop16_baemin_naver_uber_food_delivery_ma"]
        coupang = by_id["r12_loop16_coupang_everyday_delivery_share_shift"]
        food = by_id["r12_loop16_food_price_inflation_import_quota"]
        feed = by_id["r12_loop16_feed_wheat_cost_shock"]
        dog = by_id["r12_loop16_dog_meat_ban_pet_welfare_transition"]
        csat = by_id["r12_loop16_csat_education_service_demand"]
        birth = by_id["r12_loop16_birthrate_childcare_pipeline"]
        medical = by_id["r12_loop16_medical_education_quota_freeze"]

        self.assertEqual(baemin.primary_archetype, E2RArchetype.FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B)
        self.assertEqual(baemin.extra_price_metrics["bid_value_krw_trn"], 8.0)
        self.assertEqual(baemin.extra_price_metrics["bid_value_usd_bn"], 5.34)
        self.assertEqual(baemin.extra_price_metrics["delivery_hero_event_return_pct"], 5.6)
        self.assertIn("regulatory_approval_missing", baemin.red_flag_fields)

        self.assertTrue(coupang.hard_4c_confirmed)
        self.assertEqual(coupang.extra_price_metrics["coupang_return_since_breach_pct"], -34)
        self.assertEqual(coupang.extra_price_metrics["mobile_MAU_change_pct"], -3.5)
        self.assertEqual(coupang.extra_price_metrics["daily_spending_change_pct"], -6.3)
        self.assertEqual(coupang.extra_price_metrics["naver_online_users_change_pct"], 23)
        self.assertEqual(coupang.extra_price_metrics["cj_logistics_q4_overnight_one_day_volume_pct"], 120)

        self.assertEqual(food.extra_price_metrics["CPI_pct"], 2.4)
        self.assertEqual(food.extra_price_metrics["rice_pct"], 18.6)
        self.assertEqual(food.extra_price_metrics["mandarin_pct"], 26.5)

        self.assertEqual(feed.extra_price_metrics["tender_volume_tons"], 65000)
        self.assertEqual(feed.extra_price_metrics["lowest_offer_usd"], 298.50)
        self.assertEqual(feed.extra_price_metrics["unloading_surcharge_usd"], 2.00)

        self.assertEqual(dog.extra_price_metrics["government_incentives_krw_bn"], 100)
        self.assertEqual(dog.extra_price_metrics["max_per_dog_krw"], 600000)
        self.assertEqual(dog.extra_price_metrics["dogs_to_rehome_context"], "nearly_500000")

        self.assertEqual(csat.extra_price_metrics["registered_applicants"], 554174)
        self.assertEqual(csat.extra_price_metrics["YoY_pct"], 6)
        self.assertEqual(csat.extra_price_metrics["affected_flights"], 140)

        self.assertEqual(birth.extra_price_metrics["fertility_2025"], 0.80)
        self.assertEqual(birth.extra_price_metrics["fertility_2024"], 0.75)
        self.assertEqual(birth.extra_price_metrics["births_change_pct"], 6.8)
        self.assertEqual(birth.extra_price_metrics["marriages_change_pct"], 8.1)

        self.assertEqual(medical.extra_price_metrics["proposed_medical_student_number_annually_context"], 3000)
        self.assertEqual(medical.extra_price_metrics["dispute_duration_months"], 13)
        self.assertEqual(medical.extra_price_metrics["trainee_walkout_context_pct"], 90)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round320_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round320_shadow_weight_rows()}
        rules_md = render_round320_stage_rules_markdown()
        trigger_md = render_round320_trigger_grid_markdown()
        stage_md = render_round320_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND320_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r12l16_baemin_naver_uber_T1"]["promote_to"], "Stage2")
        self.assertEqual(trigger_rows["r12l16_coupang_delivery_shift_T0"]["promote_to"], "4C+Stage2")
        self.assertEqual(trigger_rows["r12l16_food_price_inflation_T0"]["promote_to"], "Stage2+4B")
        self.assertEqual(trigger_rows["r12l16_feed_wheat_T0"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r12l16_dog_meat_pet_T1"]["promote_to"], "Stage2_reference")
        self.assertEqual(trigger_rows["r12l16_medical_quota_relief_T1"]["promote_to"], "relief_reference")
        self.assertEqual(len(ROUND320_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B"]["platform_MA_final_approval"], "+5")
        self.assertEqual(shadow_rows["EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C"]["consumer_trust_security"], "+5")
        self.assertEqual(shadow_rows["FEED_WHEAT_COST_SHOCK_4B"]["commodity_cost_ignored_penalty"], "-5")
        self.assertIn("final_MA_approval_or_financing_confirmed", ROUND320_STAGE2_ACTIONABLE_RULES)
        self.assertIn("approval_revenue_conversion_margin_or_durability_remains_open", ROUND320_STAGE3_YELLOW_RULES)
        self.assertIn("life_service_MA_final_approved_and_GMV_take_rate_margin_connected", ROUND320_STAGE3_GREEN_RULES)
        self.assertIn("food_policy_without_company_margin", ROUND320_GREEN_BLOCKERS)
        self.assertIn("feed_cost_sensitivity", ROUND320_SCORE_UP_AXES)
        self.assertIn("medical_policy_relief_without_service_data", ROUND320_SCORE_DOWN_AXES)
        self.assertIn("medical_quota_relief_before_trainee_return_and_service_normalization", ROUND320_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("major_data_breach_in_everyday_service_platform", ROUND320_HARD_4C_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_policy_deal_price_or_service_disruption_metrics", ROUND320_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r12_loop16_coupang_everyday_delivery_share_shift", trigger_md)
        self.assertIn("r12_loop16_medical_education_quota_freeze", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round320_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_320.md")
        self.assertEqual(audit["round_id"], "round_248")
        self.assertEqual(audit["large_sector"], ROUND320_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_life_service_agri_education_pet_or_demographic_headline_as_Green_without_final_approval_revenue_margin_ARPU_pass_through_or_service_normalization", audit["what_not_to_change"])

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
            paths = write_round320_r12_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round320_case_rows()
            self.assertEqual(len(records), len(ROUND320_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND320_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND320_TRIGGER_RECORDS))


if __name__ == "__main__":
    unittest.main()
