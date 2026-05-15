import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round28_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round28_score_weight_v13 import (
    ROUND28_CASE_CANDIDATES,
    ROUND28_SCORE_TARGETS,
    render_round28_event_theme_boundary_markdown,
    render_round28_summary_markdown,
    round28_case_records,
    round28_score_profile_rows,
    round28_summary,
    target_for,
    write_round28_score_weight_reports,
)


class Round28ScoreWeightV13Tests(unittest.TestCase):
    def test_round28_targets_include_v13_calibration_families(self):
        labels = {target.target_id for target in ROUND28_SCORE_TARGETS}

        self.assertIn("NUCLEAR_SMR_GRID_POLICY", labels)
        self.assertIn("RARE_METALS_STRATEGIC_MATERIALS", labels)
        self.assertIn("DATA_CENTER_REIT_INFRASTRUCTURE", labels)
        self.assertIn("UTILITIES_AI_POWER_PPA", labels)
        self.assertIn("SMART_GRID_FLEXIBLE_DATACENTER", labels)
        self.assertIn("NORTH_KOREA_POLICY_EVENT", labels)
        self.assertIn("METAVERSE_NFT_THEME", labels)
        self.assertIn("ADVANCED_MATERIAL_SPECULATIVE_THEME", labels)
        self.assertIn("VALUE_UP_SHAREHOLDER_RETURN", labels)
        self.assertIn("AI_DATA_CENTER_INFRASTRUCTURE", labels)

    def test_nuclear_smr_is_watch_first_and_requires_ppa_financing_and_license(self):
        target = target_for("NUCLEAR_SMR_GRID_POLICY")
        records = {record.case_id: record for record in round28_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("actual_ppa_or_long_term_contract", target.green_conditions)
        self.assertIn("licensed_or_restarted_asset", target.green_conditions)
        self.assertIn("financing_visible", target.green_conditions)
        self.assertIn("cost_overrun", target.red_flags)
        self.assertEqual(records["nuscale_uamps_cost_cancel_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["smr_policy_no_financing_counterexample"].case_type, "failed_rerating")

    def test_strategic_metals_and_datacenter_reit_can_be_green_with_source_backed_economics(self):
        metals = target_for("RARE_METALS_STRATEGIC_MATERIALS")
        reit = target_for("DATA_CENTER_REIT_INFRASTRUCTURE")
        records = {record.case_id: record for record in round28_case_records()}

        self.assertIsNotNone(metals)
        self.assertIsNotNone(reit)
        assert metals is not None
        assert reit is not None
        self.assertEqual(metals.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(reit.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("price_floor_or_purchase_guarantee", metals.green_conditions)
        self.assertIn("long_term_offtake", metals.green_conditions)
        self.assertIn("ffo_affo_growth", reit.green_conditions)
        self.assertIn("funding_cost_controlled", reit.green_conditions)
        self.assertEqual(records["korea_zinc_tender_event_premium"].case_type, "event_premium")
        self.assertEqual(records["data_center_reit_capex_burden_4c"].case_type, "4c_thesis_break")

    def test_utilities_ppa_and_smart_grid_stay_watch_until_revenue_and_adoption(self):
        utility = target_for("UTILITIES_AI_POWER_PPA")
        grid = target_for("SMART_GRID_FLEXIBLE_DATACENTER")
        records = {record.case_id: record for record in round28_case_records()}

        self.assertIsNotNone(utility)
        self.assertIsNotNone(grid)
        assert utility is not None
        assert grid is not None
        self.assertEqual(utility.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(grid.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("long_term_ppa", utility.green_conditions)
        self.assertIn("tariff", utility.red_flags)
        self.assertIn("repeat_software_or_service_revenue", grid.green_conditions)
        self.assertIn("poc_only", grid.red_flags)
        self.assertEqual(records["tariff_no_pass_through_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["utility_adoption_delay_4c"].case_type, "4c_thesis_break")

    def test_policy_nft_and_speculative_materials_are_redteam_first(self):
        for target_id in (
            "NORTH_KOREA_POLICY_EVENT",
            "METAVERSE_NFT_THEME",
            "ADVANCED_MATERIAL_SPECULATIVE_THEME",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)

        records = {record.case_id: record for record in round28_case_records()}
        markdown = render_round28_event_theme_boundary_markdown()
        self.assertEqual(records["north_korea_policy_rally_event_only"].case_type, "event_premium")
        self.assertEqual(records["nft_price_rally_no_revenue_counterexample"].case_type, "overheat")
        self.assertEqual(records["superconductor_theme_counterexample"].case_type, "overheat")
        self.assertIn("RedTeam-First Targets", markdown)
        self.assertIn("NORTH_KOREA_POLICY_EVENT", markdown)

    def test_valueup_is_green_possible_but_requires_execution_not_index_label(self):
        target = target_for("VALUE_UP_SHAREHOLDER_RETURN")
        records = {record.case_id: record for record in round28_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.score_weight.valuation, 25)
        self.assertEqual(target.score_weight.capital_allocation, 10)
        self.assertIn("actual_cancellation", target.green_conditions)
        self.assertIn("index_inclusion_only", target.red_flags)
        self.assertEqual(records["buyback_no_cancel_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["low_roe_low_pbr_value_trap_counterexample"].case_type, "failed_rerating")

    def test_ai_infrastructure_integrates_axes_but_still_requires_axis_specific_evidence(self):
        target = target_for("AI_DATA_CENTER_INFRASTRUCTURE")
        records = {record.case_id: record for record in round28_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("orders_or_leases", target.green_conditions)
        self.assertIn("power_or_cooling_or_network_bottleneck", target.green_conditions)
        self.assertIn("overbuild", target.red_flags)
        self.assertEqual(records["ai_power_cooling_reit_integrated_success_candidate"].case_type, "success_candidate")
        self.assertEqual(records["ai_capex_overbuild_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["grid_interconnection_delay_4c"].case_type, "4c_thesis_break")

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round28_case_records()

        self.assertEqual(len(records), len(ROUND28_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round28_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v13_not_production_scoring(self):
        summary = round28_summary()
        markdown = render_round28_summary_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["case_candidate_count"], 40)
        self.assertEqual(summary["success_candidate_count"], 10)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 8)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertEqual(summary["watch_yellow_first_count"], 3)
        self.assertEqual(summary["redteam_first_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policies, PoCs, and price rallies are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round28_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v10_round28.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round28_v13.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["event_theme_boundary"].exists())
            self.assertTrue(paths["risk_boundary"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND28_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round28_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round28_score_weight_v13", text)


if __name__ == "__main__":
    unittest.main()
