import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round64_r11_loop2_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round64_r11_loop2_policy_geopolitical_event import (
    ROUND64_CASE_CANDIDATES,
    ROUND64_PRICE_FIELDS,
    ROUND64_SCORE_TARGETS,
    render_round64_event_false_positive_caps_markdown,
    render_round64_green_guardrail_markdown,
    render_round64_price_validation_plan_markdown,
    render_round64_summary_markdown,
    round64_case_candidate_rows,
    round64_case_records,
    round64_price_field_rows,
    round64_score_profile_rows,
    round64_stage_date_rows,
    round64_summary,
    target_for,
    write_round64_r11_loop2_reports,
)


class Round64R11Loop2PolicyGeopoliticalEventTests(unittest.TestCase):
    def test_round64_targets_cover_r11_loop2_archetypes(self):
        labels = {target.target_id for target in ROUND64_SCORE_TARGETS}

        self.assertEqual(len(labels), 12)
        for label in (
            "NORTH_KOREA_POLICY_EVENT",
            "GEOPOLITICAL_RECONSTRUCTION",
            "DISASTER_REBUILD_EVENT",
            "CLIMATE_DISASTER_EVENT",
            "EVENT_DISEASE_PEST_DEMAND",
            "DIAGNOSTICS_INFECTIOUS_EVENT",
            "SPECULATIVE_SCIENCE_THEME",
            "ADVANCED_MATERIAL_SPECULATIVE_THEME",
            "POLICY_LOCAL_THEME",
            "ONE_OFF_EVENT_DEMAND",
            "EVENT_TO_CONTRACT_ESCALATION",
            "THEME_VALUATION_OVERHEAT",
        ):
            self.assertIn(label, labels)
        for target in ROUND64_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.POLICY_GEOPOLITICAL_EVENT)
            self.assertFalse(target.production_scoring_changed)

    def test_event_to_contract_and_overheat_gate_are_explicit(self):
        event_to_contract = target_for("EVENT_TO_CONTRACT_ESCALATION")
        overheat = target_for("THEME_VALUATION_OVERHEAT")
        north_korea = target_for("NORTH_KOREA_POLICY_EVENT")

        assert event_to_contract is not None
        assert overheat is not None
        assert north_korea is not None
        self.assertEqual(event_to_contract.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("actual_contract", event_to_contract.green_conditions)
        self.assertIn("budget_or_financing", event_to_contract.green_conditions)
        self.assertEqual(overheat.score_weight.as_csv_dict()["eps_fcf"], "gate")
        self.assertTrue(overheat.gate_only)
        self.assertEqual(north_korea.score_weight.structural_visibility, 4)
        self.assertIn("facility_dismantle", north_korea.stage4c_conditions)

    def test_required_round64_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round64_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND64_CASE_CANDIDATES))
        self.assertEqual(rows["bavarian_nordic_us_stockpile_contract_case"]["stage2_date"], "2026-05-11")
        self.assertEqual(rows["bavarian_nordic_2024_mpox_order_case"]["case_type"], "event_premium")
        self.assertEqual(rows["bavarian_nordic_2024_mpox_order_case"]["stage4b_date"], "2024-08-16")
        self.assertEqual(rows["ukraine_telecom_ebrd_ifc_case"]["stage2_date"], "2024-10-10")
        self.assertEqual(rows["heatwave_ac_grid_stress_case"]["stage2_date"], "2025-07-18")
        self.assertEqual(rows["nyc_ac_battery_vpp_case"]["stage2_date"], "2026-05-01")
        self.assertEqual(rows["north_korea_kumgang_dismantle_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["lk99_superconductor_no_replication_case"]["stage4c_date"], "2023-08-08")
        self.assertEqual(rows["lk99_cu2s_impurity_case"]["stage4c_date"], "2023-11-01")
        self.assertEqual(rows["abbott_diagnostics_demand_wane_case"]["stage4c_date"], "2025-10-15")

    def test_case_records_validate_and_keep_round64_guardrails(self):
        records = round64_case_records()

        self.assertEqual(len(records), len(ROUND64_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("event_news_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("contract_budget_order_financing_revenue_or_eps_required", record.green_guardrails)
            self.assertIn("do_not_invent_contracts_budgets_orders_financing_stage_prices_or_guidance", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["bavarian_nordic_us_stockpile_contract_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["climate_event_seasonal_watch_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(by_id["lk99_superconductor_no_replication_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["abbott_diagnostics_demand_wane_case"].rerating_result, "thesis_break")

    def test_score_profile_rows_match_round64_weight_table(self):
        rows = {row["target_id"]: row for row in round64_score_profile_rows()}

        self.assertEqual(rows["NORTH_KOREA_POLICY_EVENT"]["structural_visibility"], "4")
        self.assertEqual(rows["GEOPOLITICAL_RECONSTRUCTION"]["structural_visibility"], "11")
        self.assertEqual(rows["CLIMATE_DISASTER_EVENT"]["bottleneck_pricing"], "11")
        self.assertEqual(rows["EVENT_DISEASE_PEST_DEMAND"]["eps_fcf"], "13")
        self.assertEqual(rows["EVENT_TO_CONTRACT_ESCALATION"]["eps_fcf"], "14")
        self.assertEqual(rows["THEME_VALUATION_OVERHEAT"]["eps_fcf"], "gate")
        self.assertEqual(rows["THEME_VALUATION_OVERHEAT"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round64_stage_date_rows()}
        fields = {row["field"] for row in round64_price_field_rows()}

        self.assertIn("sanctions_relief", rows["NORTH_KOREA_POLICY_EVENT"]["stage2"])
        self.assertIn("project_financing", rows["GEOPOLITICAL_RECONSTRUCTION"]["stage2"])
        self.assertIn("vpp_program", rows["CLIMATE_DISASTER_EVENT"]["stage2"])
        self.assertIn("replication_failure", rows["SPECULATIVE_SCIENCE_THEME"]["stage4c"])
        for field in (
            "MFE_5D",
            "MFE_180D",
            "MAE_5D",
            "MAE_180D",
            "actual_contract_flag",
            "stockpile_contract_flag",
            "project_financing_flag",
            "financing_amount",
            "vpp_program_flag",
            "battery_program_capacity",
            "replication_failure_flag",
            "impurity_explanation_flag",
            "diagnostic_sales_change",
            "facility_dismantle_flag",
            "road_rail_destroyed_flag",
            "score_price_alignment",
            "review_notes",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND64_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r11_loop2_guardrails(self):
        summary = round64_summary()
        summary_md = render_round64_summary_markdown()
        guardrails = render_round64_green_guardrail_markdown()
        caps = render_round64_event_false_positive_caps_markdown()
        price_plan = render_round64_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 12)
        self.assertEqual(summary["case_candidate_count"], 12)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 4)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 4)
        self.assertEqual(summary["green_possible_count"], 0)
        self.assertEqual(summary["watch_yellow_first_count"], 4)
        self.assertEqual(summary["redteam_first_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round-64", summary_md)
        self.assertIn("Do not apply these R11 Loop-2 v2 weights", guardrails)
        self.assertIn("EVENT_TO_CONTRACT", caps)
        self.assertIn("bavarian_nordic_us_stockpile_contract_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round64_r11_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r11_loop2_round64.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round64_r11_loop2_v2.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["event_false_positive_caps"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND64_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round64_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round64_r11_loop2_policy_geopolitical_event", text)


if __name__ == "__main__":
    unittest.main()
