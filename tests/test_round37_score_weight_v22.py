import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round37_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round37_score_weight_v22 import (
    ROUND37_CASE_CANDIDATES,
    ROUND37_SCORE_TARGETS,
    render_round37_defense_tech_markdown,
    render_round37_recurring_platform_markdown,
    render_round37_summary_markdown,
    render_round37_utility_infra_markdown,
    render_round37_validation_plan_markdown,
    round37_case_records,
    round37_score_profile_rows,
    round37_summary,
    target_for,
    write_round37_score_weight_reports,
)


class Round37ScoreWeightV22Tests(unittest.TestCase):
    def test_round37_targets_include_v22_defense_infra_and_connectivity_families(self):
        labels = {target.target_id for target in ROUND37_SCORE_TARGETS}

        self.assertEqual(len(labels), 8)
        self.assertIn("DEFENSE_TECH_AUTONOMOUS_SYSTEMS", labels)
        self.assertIn("INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA", labels)
        self.assertIn("COLD_CHAIN_REIT_LOGISTICS", labels)
        self.assertIn("DATA_CENTER_WATER_REUSE_INFRA", labels)
        self.assertIn("SATELLITE_CONNECTIVITY_INFRA", labels)
        self.assertIn("DEFENSE_AI_SOFTWARE_INTELLIGENCE", labels)
        self.assertIn("AI_DATA_CENTER_POWER_EQUIPMENT", labels)
        self.assertIn("DEFENSE_DRONE_COUNTER_UAS", labels)

    def test_defense_tech_requires_framework_procurement_and_delivery(self):
        autonomous = target_for("DEFENSE_TECH_AUTONOMOUS_SYSTEMS")
        drone = target_for("DEFENSE_DRONE_COUNTER_UAS")
        markdown = render_round37_defense_tech_markdown()
        records = {record.case_id: record for record in round37_case_records()}

        self.assertIsNotNone(autonomous)
        self.assertIsNotNone(drone)
        assert autonomous is not None
        assert drone is not None
        self.assertEqual(autonomous.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(autonomous.validation_group, "backlog_contract")
        self.assertIn("government_framework", autonomous.green_conditions)
        self.assertIn("procurement_quantity", autonomous.green_conditions)
        self.assertIn("prototype_only", autonomous.red_flags)
        self.assertIn("mna_dilution", drone.red_flags)
        self.assertEqual(records["anduril_high_private_valuation_4b_watch"].case_type, "4b_watch")
        self.assertEqual(records["procurement_delay_autonomous_systems_4c"].case_type, "4c_thesis_break")
        self.assertIn("Prototype or private valuation alone is not score evidence", markdown)

    def test_industrial_gases_are_utility_like_only_with_long_term_fab_contracts(self):
        target = target_for("INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA")
        markdown = render_round37_utility_infra_markdown()
        records = {record.case_id: record for record in round37_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.validation_group, "utility_like_infra")
        self.assertIn("onsite_gas_plant", target.green_conditions)
        self.assertIn("take_or_pay", target.green_conditions)
        self.assertIn("fab_delay", target.red_flags)
        self.assertIn("customer_concentration", target.red_flags)
        self.assertIn("capex_payback", target.validation_metrics)
        self.assertEqual(records["air_liquide_micron_ultrapure_gas_plant_candidate"].case_type, "success_candidate")
        self.assertEqual(records["semiconductor_gas_fab_delay_4c"].case_type, "4c_thesis_break")
        self.assertIn("Onsite gas plant", markdown)

    def test_cold_chain_and_water_reuse_are_watch_first_infra(self):
        cold = target_for("COLD_CHAIN_REIT_LOGISTICS")
        water = target_for("DATA_CENTER_WATER_REUSE_INFRA")
        records = {record.case_id: record for record in round37_case_records()}

        self.assertIsNotNone(cold)
        self.assertIsNotNone(water)
        assert cold is not None
        assert water is not None
        self.assertEqual(cold.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(cold.validation_group, "reit_utility_like")
        self.assertEqual(water.validation_group, "infra_utility_like")
        self.assertIn("noi_affo_growth", cold.green_conditions)
        self.assertIn("energy_cost", cold.red_flags)
        self.assertIn("water_reuse_contract", water.green_conditions)
        self.assertIn("local_opposition", water.red_flags)
        self.assertEqual(records["lineage_scale_but_net_loss_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["datacenter_water_opposition_4c"].case_type, "4c_thesis_break")

    def test_satellite_connectivity_separates_recurring_service_from_spacex_theme(self):
        target = target_for("SATELLITE_CONNECTIVITY_INFRA")
        markdown = render_round37_recurring_platform_markdown()
        records = {record.case_id: record for record in round37_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(target.validation_group, "software_recurring")
        self.assertIn("recurring_service_revenue", target.green_conditions)
        self.assertIn("backlog_growth", target.green_conditions)
        self.assertIn("spacex_theme_only", target.red_flags)
        self.assertEqual(records["ses_airline_connectivity_backlog_candidate"].case_type, "success_candidate")
        self.assertEqual(records["spacex_theme_no_revenue_counterexample"].case_type, "failed_rerating")
        self.assertIn("SpaceX-related label", markdown)

    def test_defense_ai_and_ai_power_are_green_possible_but_need_recurring_or_backlog_conversion(self):
        defense_ai = target_for("DEFENSE_AI_SOFTWARE_INTELLIGENCE")
        power = target_for("AI_DATA_CENTER_POWER_EQUIPMENT")
        records = {record.case_id: record for record in round37_case_records()}

        self.assertIsNotNone(defense_ai)
        self.assertIsNotNone(power)
        assert defense_ai is not None
        assert power is not None
        self.assertEqual(defense_ai.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(defense_ai.validation_group, "software_recurring")
        self.assertIn("program_of_record", defense_ai.green_conditions)
        self.assertIn("ethical_regulation", defense_ai.red_flags)
        self.assertEqual(power.validation_group, "backlog_contract")
        self.assertIn("bookings_growth", power.green_conditions)
        self.assertIn("bookings_slowdown", power.red_flags)
        self.assertEqual(records["palantir_maven_contract_candidate"].case_type, "success_candidate")
        self.assertEqual(records["power_equipment_bookings_slowdown_4c"].case_type, "4c_thesis_break")

    def test_validation_plan_renders_backlog_utility_and_software_groups(self):
        plan = render_round37_validation_plan_markdown()
        rows = round37_score_profile_rows()

        self.assertIn("backlog_contract", plan)
        self.assertIn("utility_like_infra", plan)
        self.assertIn("software_recurring", plan)
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")
            self.assertIn("validation_group", row)
            self.assertIn("validation_metrics", row)

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round37_case_records()

        self.assertEqual(len(records), len(ROUND37_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_invent_contracts_backlog_or_prices", record.green_guardrails)

    def test_summary_reports_v22_validation_without_production_scoring(self):
        summary = round37_summary()
        markdown = render_round37_summary_markdown()

        self.assertEqual(summary["target_count"], 8)
        self.assertEqual(summary["case_candidate_count"], 32)
        self.assertEqual(summary["success_candidate_count"], 14)
        self.assertEqual(summary["stage4b_case_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 3)
        self.assertEqual(summary["redteam_first_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("v2.2 validation plans", markdown)

    def test_report_writer_outputs_cases_and_validation_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round37_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v19_round37.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round37_v22.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["validation_plan"].exists())
            self.assertTrue(paths["defense_tech"].exists())
            self.assertTrue(paths["utility_infra"].exists())
            self.assertTrue(paths["recurring_platform"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND37_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round37_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round37_score_weight_v22", text)


if __name__ == "__main__":
    unittest.main()
