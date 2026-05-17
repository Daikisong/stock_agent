import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round52_r12_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round52_r12_agri_life_misc import (
    ROUND52_CASE_CANDIDATES,
    ROUND52_SCORE_TARGETS,
    render_round52_green_guardrail_markdown,
    render_round52_price_validation_plan_markdown,
    render_round52_summary_markdown,
    render_round52_unit_economics_cap_markdown,
    round52_case_candidate_rows,
    round52_case_records,
    round52_price_field_rows,
    round52_score_profile_rows,
    round52_stage_date_rows,
    round52_summary,
    target_for,
    write_round52_r12_reports,
)


class Round52R12AgriLifeMiscTests(unittest.TestCase):
    def test_round52_targets_cover_r12_archetypes(self):
        labels = {target.target_id for target in ROUND52_SCORE_TARGETS}

        self.assertEqual(len(labels), 11)
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
        ):
            self.assertIn(label, labels)

    def test_new_r12_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.SMART_FARM_AGRI_TECH,
            E2RArchetype.AGRI_MACHINERY_PRECISION_CYCLE,
            E2RArchetype.AGRI_LIVESTOCK_FOOD_COMMODITY,
            E2RArchetype.FOOD_INPUT_REGULATED_CYCLE,
            E2RArchetype.POLICY_LOCAL_SERVICE_THEME,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_agri_livestock_and_policy_are_redteam_first(self):
        livestock = target_for("AGRI_LIVESTOCK_FOOD_COMMODITY")
        policy = target_for("POLICY_LOCAL_SERVICE_THEME")
        smart_farm = target_for("SMART_FARM_AGRI_TECH")
        rental = target_for("HOME_LIVING_APPLIANCE_RENTAL")

        self.assertIsNotNone(livestock)
        self.assertIsNotNone(policy)
        self.assertIsNotNone(smart_farm)
        self.assertIsNotNone(rental)
        assert livestock is not None
        assert policy is not None
        assert smart_farm is not None
        assert rental is not None
        self.assertEqual(livestock.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("price_normalization", livestock.red_flags)
        self.assertEqual(policy.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertEqual(smart_farm.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("unit_economics_positive", smart_farm.green_conditions)
        self.assertIn("rental_churn_stable", rental.green_conditions)

    def test_required_round52_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round52_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND52_CASE_CANDIDATES))
        self.assertEqual(rows["john_deere_autonomous_agri_stage1_case"]["stage1_date"], "2025-01-07")
        self.assertEqual(rows["deere_farm_equipment_demand_slowdown_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["zoetis_bird_flu_vaccine_conditional_case"]["stage2_date"], "2025-02-14")
        self.assertEqual(rows["calmaine_egg_price_profit_case"]["case_type"], "cyclical_success")
        self.assertEqual(rows["duolingo_ai_strategy_bookings_miss_case"]["stage4c_date"], "2026-02-26")
        self.assertEqual(rows["juul_fda_approval_case"]["stage2_date"], "2025-07-17")
        self.assertEqual(rows["cannabis_schedule3_limited_case"]["stage4b_date"], "2026-05-12")

    def test_case_records_validate_and_keep_unit_economics_guardrails(self):
        records = round52_case_records()

        self.assertEqual(len(records), len(ROUND52_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("life_essential_label_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("repeat_contract_repeat_revenue_unit_economics_or_regulatory_approval_required", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        rows = round52_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND52_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["SMART_FARM_AGRI_TECH"]["posture"], "WATCH_YELLOW_FIRST")
        self.assertEqual(by_target["AGRI_LIVESTOCK_FOOD_COMMODITY"]["posture"], "REDTEAM_FIRST")
        self.assertEqual(by_target["POLICY_LOCAL_SERVICE_THEME"]["information_confidence"], "3")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        stage_rows = {row["target_id"]: row for row in round52_stage_date_rows()}
        price_fields = {row["field"] for row in round52_price_field_rows()}

        self.assertIn("chapter11", stage_rows["SMART_FARM_AGRI_TECH"]["stage4c"])
        self.assertIn("bookings_miss", "|".join(round52_case_candidate_rows()[5]["red_flag_fields"].split("|")))
        self.assertIn("government_purchase_contract", stage_rows["ANIMAL_HEALTH_BIOSECURITY"]["stage2"])
        self.assertIn("farm_income_indicator", price_fields)
        self.assertIn("unit_economics_margin", price_fields)
        self.assertIn("completion_rate", price_fields)
        self.assertIn("retailer_retreat_flag", price_fields)
        self.assertIn("fda_approval_flag", price_fields)

    def test_summary_and_markdown_explain_r12_guardrails(self):
        summary = round52_summary()
        summary_md = render_round52_summary_markdown()
        guardrails = render_round52_green_guardrail_markdown()
        caps = render_round52_unit_economics_cap_markdown()
        price_plan = render_round52_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 11)
        self.assertEqual(summary["case_candidate_count"], 15)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("Do not apply these R12 v1.0 weights", guardrails)
        self.assertIn("unit economics", caps)
        self.assertIn("cyclical_success", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round52_r12_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r12_round52.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round52_r12_v1.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND52_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round52_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round52_r12_agri_life_misc", text)


if __name__ == "__main__":
    unittest.main()
