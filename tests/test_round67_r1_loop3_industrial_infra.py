import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round67_r1_loop3_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round67_r1_loop3_industrial_infra import (
    ROUND67_CASE_CANDIDATES,
    ROUND67_PRICE_FIELDS,
    ROUND67_SCORE_TARGETS,
    render_round67_green_guardrail_markdown,
    render_round67_loop3_risk_overlay_markdown,
    render_round67_price_validation_plan_markdown,
    render_round67_summary_markdown,
    round67_case_candidate_rows,
    round67_case_records,
    round67_price_field_rows,
    round67_score_profile_rows,
    round67_stage_date_rows,
    round67_summary,
    round67_target_for,
    write_round67_r1_loop3_reports,
)


class Round67R1Loop3IndustrialInfraTests(unittest.TestCase):
    def test_round67_targets_cover_r1_loop3_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND67_SCORE_TARGETS}

        self.assertEqual(len(labels), 16)
        for label in (
            "GRID_TRANSFORMER_SHORTAGE",
            "AI_DATA_CENTER_POWER_EQUIPMENT",
            "CONTRACT_BACKLOG_INDUSTRIAL",
            "DEFENSE_GOVERNMENT_BACKLOG",
            "DEFENSE_TECH_AUTONOMOUS_SYSTEMS",
            "DEFENSE_DRONE_COUNTER_UAS",
            "DEFENSE_AI_SOFTWARE_INTELLIGENCE",
            "SHIPBUILDING_OFFSHORE_BACKLOG",
            "SHIPBUILDING_NAVAL_MRO",
            "RAIL_INFRASTRUCTURE",
            "NUCLEAR_EXISTING_PPA",
            "NUCLEAR_SMR_GRID_POLICY",
            "GEOPOLITICAL_RECONSTRUCTION",
            "SMART_FACTORY_AUTOMATION",
            "PROJECT_DELAY_CAPEX_OVERLAY",
            "CAPITAL_ALLOCATION_DILUTION_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND67_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.INDUSTRIAL_ORDERS_INFRA)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r1_loop3_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.SHIPBUILDING_NAVAL_MRO,
            E2RArchetype.NUCLEAR_EXISTING_PPA,
            E2RArchetype.PROJECT_DELAY_CAPEX_OVERLAY,
            E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_loop3_weights_and_penalties_are_stricter_than_loop2(self):
        transformer = round67_target_for("GRID_TRANSFORMER_SHORTAGE")
        defense = round67_target_for("DEFENSE_GOVERNMENT_BACKLOG")
        smr = round67_target_for("NUCLEAR_SMR_GRID_POLICY")
        ppa = round67_target_for("NUCLEAR_EXISTING_PPA")
        dilution = round67_target_for("CAPITAL_ALLOCATION_DILUTION_OVERLAY")

        self.assertIsNotNone(transformer)
        self.assertIsNotNone(defense)
        self.assertIsNotNone(smr)
        self.assertIsNotNone(ppa)
        self.assertIsNotNone(dilution)
        assert transformer is not None
        assert defense is not None
        assert smr is not None
        assert ppa is not None
        assert dilution is not None
        self.assertEqual(transformer.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(transformer.score_weight.eps_fcf, 24)
        self.assertEqual(transformer.score_weight.bottleneck_pricing, 24)
        self.assertIn("low_margin_long_term_contract", transformer.loop3_penalty_axes)
        self.assertIn("capital_allocation_shock", defense.loop3_penalty_axes)
        self.assertEqual(smr.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("customer_subscription_failure", smr.red_flags)
        self.assertEqual(ppa.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(dilution.hard_gate)
        self.assertIn("dilution", dilution.red_flags)

    def test_required_round67_cases_are_present_with_dates_and_alignment(self):
        rows = {row["case_id"]: row for row in round67_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND67_CASE_CANDIDATES))
        self.assertEqual(rows["us_transformer_shortage_import_slots_case"]["stage2_date"], "2026-05-11")
        self.assertEqual(rows["ge_vernova_data_center_orders_case"]["stage4b_date"], "2026-04-22")
        self.assertEqual(rows["data_center_local_opposition_grid_case"]["target_id"], "PROJECT_DELAY_CAPEX_OVERLAY")
        self.assertEqual(rows["data_center_local_opposition_grid_case"]["stage4c_date"], "2026-05-13")
        self.assertEqual(rows["hanwha_aerospace_romania_k9_case"]["stage2_date"], "2024-07-09")
        self.assertEqual(rows["hanwha_aerospace_romania_k9_case"]["case_type"], "structural_success")
        self.assertEqual(rows["hanwha_aerospace_europe_sales_visibility_case"]["stage2_date"], "2024-10-07")
        self.assertEqual(rows["hanwha_aerospace_dilution_case"]["target_id"], "CAPITAL_ALLOCATION_DILUTION_OVERLAY")
        self.assertEqual(rows["hanwha_aerospace_dilution_case"]["stage4b_date"], "2025-03-27")
        self.assertEqual(rows["hanwha_ocean_us_navy_mro_case"]["target_id"], "SHIPBUILDING_NAVAL_MRO")
        self.assertEqual(rows["hyundai_rotem_morocco_rail_case"]["stage2_date"], "2025-02-26")
        self.assertEqual(rows["meta_constellation_existing_nuclear_ppa_case"]["target_id"], "NUCLEAR_EXISTING_PPA")
        self.assertEqual(rows["nuscale_uamps_smrcancel_case"]["stage4c_date"], "2023-11-01")
        self.assertEqual(rows["ukraine_reconstruction_policy_case"]["case_type"], "event_premium")
        self.assertEqual(rows["neom_city_policy_case"]["case_type"], "event_premium")

    def test_case_records_validate_and_keep_loop3_guardrails(self):
        records = round67_case_records()

        self.assertEqual(len(records), len(ROUND67_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "INDUSTRIAL_ORDERS_INFRA")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("require_contract_quality_delivery_margin_eps_revision_fcf_for_green", record.green_guardrails)
            self.assertIn("do_not_invent_contract_dates_prices_margins_or_counterparties", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["hanwha_aerospace_dilution_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["nuscale_uamps_smrcancel_case"].rerating_result, "thesis_break")
        self.assertIn("water_permitting_delay", by_id["data_center_local_opposition_grid_case"].red_flag_fields)

    def test_score_profile_rows_mark_no_production_change_and_include_loop3_penalties(self):
        rows = round67_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND67_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["large_sector"], "INDUSTRIAL_ORDERS_INFRA")
            self.assertEqual(row["production_scoring_changed"], "false")
            self.assertIn("loop3_penalty_axes", row)
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["GRID_TRANSFORMER_SHORTAGE"]["eps_fcf"], "24")
        self.assertIn("low_margin_long_term_contract", by_target["GRID_TRANSFORMER_SHORTAGE"]["loop3_penalty_axes"])
        self.assertIn("project_delay", by_target["PROJECT_DELAY_CAPEX_OVERLAY"]["loop3_penalty_axes"])
        self.assertEqual(by_target["CAPITAL_ALLOCATION_DILUTION_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(by_target["NUCLEAR_SMR_GRID_POLICY"]["posture"], "REDTEAM_FIRST")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round67_stage_date_rows()}
        fields = {row["field"] for row in round67_price_field_rows()}

        self.assertIn("fy1_fy2_fy3_revision", rows["GRID_TRANSFORMER_SHORTAGE"]["stage3"])
        self.assertIn("project_cancelled", rows["PROJECT_DELAY_CAPEX_OVERLAY"]["stage4c"])
        self.assertIn("signed_ppa", rows["NUCLEAR_EXISTING_PPA"]["stage2"])
        self.assertIn("project_cancelled", rows["NUCLEAR_SMR_GRID_POLICY"]["stage4c"])
        for field in (
            "contract_value_to_sales",
            "counterparty",
            "delivery_schedule",
            "transformer_lead_time_months",
            "data_center_orders",
            "water_permitting_delay_flag",
            "defense_backlog",
            "dilution_flag",
            "naval_mro_contract_flag",
            "rail_financing_secured_flag",
            "nuclear_ppa_flag",
            "smr_cost_overrun_flag",
            "reconstruction_contract_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND67_PRICE_FIELDS))

    def test_summary_and_markdown_explain_loop3_guardrails(self):
        summary = round67_summary()
        summary_md = render_round67_summary_markdown()
        guardrails = render_round67_green_guardrail_markdown()
        overlays = render_round67_loop3_risk_overlay_markdown()
        price_plan = render_round67_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 16)
        self.assertEqual(summary["case_candidate_count"], 13)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 2)
        self.assertEqual(summary["hard_gate_target_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R1 Loop 3", summary_md)
        self.assertIn("Do not apply R1 Loop-3 v3.0 weights", guardrails)
        self.assertIn("NAVAL_MRO_OPTION_ONLY", overlays)
        self.assertIn("SMR_POLICY_FALSE_GREEN", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round67_r1_loop3_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r1_loop3_round67.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round67_r1_loop3_v3.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["loop3_risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND67_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round67_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round67_r1_loop3_industrial_infra", text)


if __name__ == "__main__":
    unittest.main()
