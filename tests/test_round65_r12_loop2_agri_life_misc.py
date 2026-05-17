import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round65_r12_loop2_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round65_r12_loop2_agri_life_misc import (
    ROUND65_CASE_CANDIDATES,
    ROUND65_PRICE_FIELDS,
    ROUND65_SCORE_TARGETS,
    render_round65_green_guardrail_markdown,
    render_round65_price_validation_plan_markdown,
    render_round65_summary_markdown,
    render_round65_unit_economics_cap_markdown,
    round65_case_candidate_rows,
    round65_case_records,
    round65_price_field_rows,
    round65_score_profile_rows,
    round65_stage_date_rows,
    round65_summary,
    target_for,
    write_round65_r12_loop2_reports,
)


class Round65R12Loop2AgriLifeMiscTests(unittest.TestCase):
    def test_round65_targets_cover_r12_loop2_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND65_SCORE_TARGETS}

        self.assertEqual(len(labels), 14)
        for label in (
            "SMART_FARM_AGRI_TECH",
            "AGRI_MACHINERY_PRECISION_CYCLE",
            "AGRI_LIVESTOCK_FOOD_COMMODITY",
            "ANIMAL_HEALTH_BIOSECURITY",
            "EDUCATION_SPECIALTY_SERVICES",
            "HOME_CHILD_EDUCATION",
            "HOME_LIVING_APPLIANCE_RENTAL",
            "SERVICE_KIOSK_SELF_CHECKOUT",
            "CONSUMER_REGULATED_PRODUCT",
            "FOOD_INPUT_REGULATED_CYCLE",
            "POLICY_LOCAL_SERVICE_THEME",
            "AGRI_DISEASE_EVENT_OVERLAY",
            "AI_EDUCATION_DISRUPTION_OVERLAY",
            "REGULATED_CONSUMER_APPROVAL_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND65_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.EDUCATION_LIFE_AGRI_MISC)
            self.assertFalse(target.production_scoring_changed)

    def test_new_overlay_archetypes_exist_and_are_gate_only(self):
        for archetype in (
            E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY,
            E2RArchetype.AI_EDUCATION_DISRUPTION_OVERLAY,
            E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY,
        ):
            self.assertIsInstance(archetype.value, str)

        disease = target_for("AGRI_DISEASE_EVENT_OVERLAY")
        ai = target_for("AI_EDUCATION_DISRUPTION_OVERLAY")
        approval = target_for("REGULATED_CONSUMER_APPROVAL_OVERLAY")
        assert disease is not None
        assert ai is not None
        assert approval is not None
        for target in (disease, ai, approval):
            self.assertTrue(target.gate_only)
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertEqual(target.score_weight.as_csv_dict()["eps_fcf"], "gate")

    def test_score_profile_rows_match_round65_weight_table(self):
        rows = {row["target_id"]: row for row in round65_score_profile_rows()}

        self.assertEqual(rows["SMART_FARM_AGRI_TECH"]["eps_fcf"], "17")
        self.assertEqual(rows["SMART_FARM_AGRI_TECH"]["valuation"], "8")
        self.assertEqual(rows["AGRI_LIVESTOCK_FOOD_COMMODITY"]["structural_visibility"], "9")
        self.assertEqual(rows["ANIMAL_HEALTH_BIOSECURITY"]["structural_visibility"], "15")
        self.assertEqual(rows["EDUCATION_SPECIALTY_SERVICES"]["bottleneck_pricing"], "5")
        self.assertEqual(rows["HOME_LIVING_APPLIANCE_RENTAL"]["eps_fcf"], "18")
        self.assertEqual(rows["SERVICE_KIOSK_SELF_CHECKOUT"]["eps_fcf"], "16")
        self.assertEqual(rows["CONSUMER_REGULATED_PRODUCT"]["structural_visibility"], "15")
        self.assertEqual(rows["AGRI_DISEASE_EVENT_OVERLAY"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_required_round65_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round65_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND65_CASE_CANDIDATES))
        self.assertEqual(rows["john_deere_autonomous_agri_ces_case"]["stage1_date"], "2025-01-06")
        self.assertEqual(rows["deere_farm_equipment_demand_slowdown_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["deere_right_to_repair_settlement_case"]["case_type"], "failed_rerating")
        self.assertEqual(rows["zoetis_bird_flu_vaccine_conditional_case"]["stage2_date"], "2025-02-14")
        self.assertEqual(rows["calmaine_egg_price_profit_case"]["case_type"], "cyclical_success")
        self.assertEqual(rows["bowery_vertical_farming_shutdown_case"]["stage4c_date"], "2024-11-05")
        self.assertEqual(rows["appharvest_chapter11_case"]["stage4c_date"], "2023-07-24")
        self.assertEqual(rows["duolingo_ai_strategy_bookings_miss_case"]["stage4c_date"], "2026-02-26")
        self.assertEqual(rows["chegg_ai_disruption_case"]["stage4c_date"], "2023-05-02")
        self.assertEqual(rows["2u_chapter11_case"]["stage4c_date"], "2024-07-25")
        self.assertEqual(rows["whirlpool_dividend_suspension_case"]["stage4c_date"], "2026-05-07")
        self.assertEqual(rows["juul_fda_approval_case"]["stage2_date"], "2025-07-17")
        self.assertEqual(rows["cannabis_schedule3_limited_case"]["stage4b_date"], "2026-05-12")

    def test_case_records_validate_and_keep_round65_guardrails(self):
        records = round65_case_records()

        self.assertEqual(len(records), len(ROUND65_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("life_essential_policy_or_disease_label_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("repeat_contract_repeat_revenue_unit_economics_or_regulatory_scope_required", record.green_guardrails)
            self.assertIn("do_not_invent_unit_economics_orders_cac_churn_regulatory_scope_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["calmaine_egg_price_profit_case"].rerating_result, "cyclical_rerating")
        self.assertEqual(by_id["target_self_checkout_limit_case"].rerating_result, "no_rerating")
        self.assertEqual(by_id["chegg_ai_disruption_case"].rerating_result, "thesis_break")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        stage_rows = {row["target_id"]: row for row in round65_stage_date_rows()}
        price_fields = {row["field"] for row in round65_price_field_rows()}

        self.assertIn("shutdown", stage_rows["SMART_FARM_AGRI_TECH"]["stage4c"])
        self.assertIn("right_to_repair_lawsuit", stage_rows["AGRI_MACHINERY_PRECISION_CYCLE"]["stage4c"])
        self.assertIn("price_fixing_investigation", stage_rows["AGRI_LIVESTOCK_FOOD_COMMODITY"]["stage4c"])
        self.assertIn("bookings_miss", stage_rows["EDUCATION_SPECIALTY_SERVICES"]["stage4c"])
        self.assertIn("sales_authorization", stage_rows["CONSUMER_REGULATED_PRODUCT"]["stage2"])
        for field in (
            "right_to_repair_flag",
            "repair_settlement_amount",
            "premium_pricing_success_flag",
            "shutdown_flag",
            "price_fixing_investigation_flag",
            "bookings_growth",
            "paid_conversion_rate",
            "traffic_decline_flag",
            "self_checkout_limit_flag",
            "employee_workload_flag",
            "compliance_cost",
            "sales_channel_authorized_flag",
            "score_price_alignment",
            "review_notes",
        ):
            self.assertIn(field, price_fields)
        self.assertEqual(len(price_fields), len(ROUND65_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r12_loop2_guardrails(self):
        summary = round65_summary()
        summary_md = render_round65_summary_markdown()
        guardrails = render_round65_green_guardrail_markdown()
        caps = render_round65_unit_economics_cap_markdown()
        price_plan = render_round65_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 14)
        self.assertEqual(summary["case_candidate_count"], 15)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 0)
        self.assertEqual(summary["watch_yellow_first_count"], 8)
        self.assertEqual(summary["redteam_first_count"], 6)
        self.assertEqual(summary["gate_only_target_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round-65", summary_md)
        self.assertIn("Do not apply these R12 Loop-2 v2 weights", guardrails)
        self.assertIn("right-to-repair", caps)
        self.assertIn("regulated_consumer_approval_stage2", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round65_r12_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r12_loop2_round65.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round65_r12_loop2_v2.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["unit_economics_caps"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND65_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round65_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round65_r12_loop2_agri_life_misc", text)


if __name__ == "__main__":
    unittest.main()
