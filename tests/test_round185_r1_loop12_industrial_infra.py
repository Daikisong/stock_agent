import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round185_r1_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round185_r1_loop12_industrial_infra import (
    ROUND185_BASE_SCORE_WEIGHTS,
    ROUND185_CASE_CANDIDATES,
    ROUND185_PRICE_FIELDS,
    ROUND185_SCORE_TARGETS,
    ROUND185_SOURCE_CANONICAL_TARGET_COUNT,
    ROUND185_SOURCE_CANONICAL_TARGET_IDS,
    ROUND185_STAGE_CAPS,
    render_round185_green_guardrail_markdown,
    render_round185_price_validation_plan_markdown,
    render_round185_risk_overlay_markdown,
    render_round185_score_stage_price_alignment_markdown,
    render_round185_summary_markdown,
    round185_base_score_weight_rows,
    round185_case_candidate_rows,
    round185_case_records,
    round185_price_field_rows,
    round185_score_profile_rows,
    round185_score_stage_price_alignment_rows,
    round185_stage_cap_rows,
    round185_stage_date_rows,
    round185_summary,
    round185_target_for,
    write_round185_r1_loop12_reports,
)


class Round185R1Loop12IndustrialInfraTests(unittest.TestCase):
    def test_round185_targets_cover_loop12_archetypes(self):
        labels = {target.target_id for target in ROUND185_SCORE_TARGETS}

        self.assertEqual(len(labels), 12)
        self.assertEqual(ROUND185_SOURCE_CANONICAL_TARGET_COUNT, 12)
        self.assertEqual(set(ROUND185_SOURCE_CANONICAL_TARGET_IDS), labels)
        for label in (
            "GRID_TRANSFORMER_MIDCAP_KOREA",
            "POWER_CABLE_GRID_BACKLOG_KOREA",
            "DEFENSE_ELECTRONICS_KF21_RADAR",
            "SPACE_LAUNCH_PROGRAM_OF_RECORD",
            "DEFENSE_CAPITAL_RAISE_DILUTION",
            "CONSTRUCTION_EQUIPMENT_CYCLE_KOREA",
            "CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY",
            "NUCLEAR_DECOMMISSIONING_KOREA",
            "NUCLEAR_POLICY_STAGE1_2_NOT_GREEN",
            "SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA",
            "SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)

    def test_new_loop12_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.GRID_TRANSFORMER_MIDCAP_KOREA,
            E2RArchetype.POWER_CABLE_GRID_BACKLOG_KOREA,
            E2RArchetype.DEFENSE_ELECTRONICS_KF21_RADAR,
            E2RArchetype.SPACE_LAUNCH_PROGRAM_OF_RECORD,
            E2RArchetype.DEFENSE_CAPITAL_RAISE_DILUTION,
            E2RArchetype.CONSTRUCTION_EQUIPMENT_CYCLE_KOREA,
            E2RArchetype.CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY,
            E2RArchetype.NUCLEAR_DECOMMISSIONING_KOREA,
            E2RArchetype.NUCLEAR_POLICY_STAGE1_2_NOT_GREEN,
            E2RArchetype.SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA,
            E2RArchetype.SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK,
            E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_base_weights_and_stage_caps_match_round185_note(self):
        weights = {row["component"]: row for row in round185_base_score_weight_rows()}
        caps = {row["stage_band"]: row for row in round185_stage_cap_rows()}

        self.assertEqual(len(ROUND185_BASE_SCORE_WEIGHTS), 7)
        self.assertEqual(weights["eps_fcf_opm_conversion"]["points"], "24")
        self.assertEqual(weights["contract_backlog_customer_visibility"]["points"], "20")
        self.assertEqual(weights["bottleneck_pricing_power"]["points"], "16")
        self.assertEqual(weights["early_price_path_validation"]["points"], "12")
        self.assertEqual(weights["capital_discipline_governance"]["points"], "10")
        self.assertEqual(weights["disclosure_confidence_hard_redteam"]["points"], "10")
        self.assertEqual(weights["valuation_room_4b_runway"]["points"], "8")
        self.assertEqual(len(ROUND185_STAGE_CAPS), 5)
        self.assertEqual(caps["Stage 3"]["max_score"], "requires_5_of_8")
        self.assertIn("customer_amount_period_confirmed", caps["Stage 3"]["required_evidence"])
        self.assertEqual(caps["Stage 4B"]["max_score"], "requires_4_of_6")
        self.assertIn("basket_rally_without_contract_detail", caps["Stage 4B"]["required_evidence"])
        self.assertEqual(caps["Stage 4C"]["max_score"], "hard_gate")
        self.assertIn("fss_revision_request", caps["Stage 4C"]["required_evidence"])
        for row in weights.values():
            self.assertEqual(row["production_scoring_changed"], "false")
        for row in caps.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_green_possible_stage2_and_hard_gate_targets_are_separated(self):
        grid = round185_target_for("GRID_TRANSFORMER_MIDCAP_KOREA")
        cable = round185_target_for("POWER_CABLE_GRID_BACKLOG_KOREA")
        radar = round185_target_for("DEFENSE_ELECTRONICS_KF21_RADAR")
        ship_equipment = round185_target_for("SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA")
        dilution = round185_target_for("DEFENSE_CAPITAL_RAISE_DILUTION")
        governance = round185_target_for("CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY")
        satellite = round185_target_for("SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK")
        policy = round185_target_for("NUCLEAR_POLICY_STAGE1_2_NOT_GREEN")

        self.assertIsNotNone(grid)
        self.assertIsNotNone(cable)
        self.assertIsNotNone(radar)
        self.assertIsNotNone(ship_equipment)
        self.assertIsNotNone(dilution)
        self.assertIsNotNone(governance)
        self.assertIsNotNone(satellite)
        self.assertIsNotNone(policy)
        assert grid is not None
        assert cable is not None
        assert radar is not None
        assert ship_equipment is not None
        assert dilution is not None
        assert governance is not None
        assert satellite is not None
        assert policy is not None
        self.assertFalse(grid.hard_gate)
        self.assertFalse(cable.hard_gate)
        self.assertFalse(ship_equipment.hard_gate)
        self.assertIn("op_eps_revision", grid.green_conditions)
        self.assertIn("margin_visible", cable.green_conditions)
        self.assertIn("radar_delivery", radar.green_conditions)
        self.assertTrue(dilution.hard_gate)
        self.assertIn("fss_revision_request", dilution.red_flags)
        self.assertTrue(governance.hard_gate)
        self.assertIn("minority_shareholder_risk", governance.red_flags)
        self.assertTrue(satellite.hard_gate)
        self.assertIn("investment_loss", satellite.red_flags)
        self.assertFalse(policy.hard_gate)
        self.assertEqual(policy.score_weight.eps_fcf_opm, "cap")

    def test_required_round185_cases_are_present(self):
        rows = {row["case_id"]: row for row in round185_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND185_CASE_CANDIDATES))
        self.assertEqual(rows["iljin_midcap_transformer_stage3_candidate_case"]["target_id"], "GRID_TRANSFORMER_MIDCAP_KOREA")
        self.assertEqual(rows["daehan_gaon_power_cable_stage3_candidate_case"]["target_id"], "POWER_CABLE_GRID_BACKLOG_KOREA")
        self.assertEqual(rows["power_equipment_midcap_basket_4b_watch_case"]["case_type"], "4b_watch")
        self.assertEqual(rows["hanwha_system_kf21_aesa_radar_stage2_case"]["target_id"], "DEFENSE_ELECTRONICS_KF21_RADAR")
        self.assertEqual(rows["hanwha_aerospace_kslv_program_stage2_case"]["target_id"], "SPACE_LAUNCH_PROGRAM_OF_RECORD")
        self.assertEqual(rows["hanwha_aerospace_capital_raise_dilution_case"]["case_type"], "4c_thesis_break")
        self.assertEqual(rows["doosan_bobcat_governance_cap_case"]["target_id"], "CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY")
        self.assertEqual(rows["nuclear_decommissioning_policy_stage1_2_case"]["target_id"], "NUCLEAR_DECOMMISSIONING_KOREA")
        self.assertEqual(rows["shipbuilding_equipment_backlog_stage3_candidate_case"]["target_id"], "SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA")
        self.assertEqual(rows["hanwha_system_eutelsat_loss_4c_watch_case"]["target_id"], "SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK")

    def test_case_records_validate_and_keep_loop12_guardrails(self):
        records = round185_case_records()

        self.assertEqual(len(records), len(ROUND185_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "INDUSTRIAL_ORDERS_INFRA")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("stage3_early_catch_requires_5_of_8_loop12_conditions", record.green_guardrails)
            self.assertIn("policy_mou_loi_media_only_cannot_create_stage3", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        rows = round185_score_profile_rows()
        by_target = {row["target_id"]: row for row in rows}

        self.assertEqual(len(rows), len(ROUND185_SCORE_TARGETS))
        self.assertEqual(by_target["GRID_TRANSFORMER_MIDCAP_KOREA"]["eps_fcf_opm"], "24")
        self.assertEqual(by_target["POWER_CABLE_GRID_BACKLOG_KOREA"]["contract_customer_visibility"], "21")
        self.assertEqual(by_target["DEFENSE_CAPITAL_RAISE_DILUTION"]["hard_gate"], "true")
        self.assertEqual(by_target["CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(by_target["NUCLEAR_POLICY_STAGE1_2_NOT_GREEN"]["eps_fcf_opm"], "cap")
        self.assertEqual(by_target["SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK"]["hard_gate"], "true")
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_price_and_alignment_rows_are_explicit(self):
        stage_rows = {row["target_id"]: row for row in round185_stage_date_rows()}
        price_fields = {row["field"] for row in round185_price_field_rows()}
        alignment_rows = {row["case_id"]: row for row in round185_score_stage_price_alignment_rows()}

        self.assertIn("op_eps_fcf_revision", stage_rows["GRID_TRANSFORMER_MIDCAP_KOREA"]["stage3"])
        self.assertIn("fss_revision_request", stage_rows["DEFENSE_CAPITAL_RAISE_DILUTION"]["stage4c"])
        self.assertIn("minority_shareholder_damage", stage_rows["CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY"]["stage4c"])
        self.assertIn("policy_only", stage_rows["NUCLEAR_POLICY_STAGE1_2_NOT_GREEN"]["red_flags"])
        for field in (
            "relative_strength_vs_power_equipment_basket",
            "relative_strength_vs_defense_basket",
            "relative_strength_vs_shipbuilding_equipment_basket",
            "contract_amount_to_prior_sales",
            "government_program_flag",
            "program_budget",
            "capital_raise_flag",
            "fss_revision_request_flag",
            "minority_shareholder_risk_flag",
            "disclosure_confidence",
            "valuation_at_stage4b",
        ):
            self.assertIn(field, price_fields)
        self.assertEqual(alignment_rows["hanwha_aerospace_capital_raise_dilution_case"]["verdict"], "capital_redteam_blocks_green")
        self.assertEqual(alignment_rows["nuclear_decommissioning_policy_stage1_2_case"]["verdict"], "policy_to_contract_not_green")

    def test_summary_and_markdown_explain_loop12(self):
        summary = round185_summary()
        summary_md = render_round185_summary_markdown()
        guardrails = render_round185_green_guardrail_markdown()
        overlays = render_round185_risk_overlay_markdown()
        price_plan = render_round185_price_validation_plan_markdown()
        alignment = render_round185_score_stage_price_alignment_markdown()

        self.assertEqual(summary["target_count"], 12)
        self.assertEqual(summary["source_canonical_target_count"], 12)
        self.assertEqual(summary["case_candidate_count"], 13)
        self.assertEqual(summary["base_score_axis_count"], 7)
        self.assertEqual(summary["stage_cap_count"], 5)
        self.assertEqual(summary["score_stage_price_alignment_count"], 6)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 3)
        self.assertEqual(summary["hard_gate_target_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R1 Loop 12", summary_md)
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("at least 5 of 8 checks", guardrails)
        self.assertIn("Hard 4C Examples", overlays)
        self.assertIn("Required Fields", price_plan)
        self.assertIn("Hanwha Aerospace", alignment)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round185_r1_loop12_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r1_loop12_round185.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round185_r1_loop12_v12.csv",
            )

            for key in (
                "cases",
                "score_profiles",
                "summary",
                "case_matrix",
                "stage_date_plan",
                "green_guardrails",
                "risk_overlays",
                "price_validation_plan",
                "price_fields",
                "base_score_weights",
                "stage_caps",
                "score_stage_price_alignment",
                "score_stage_price_alignment_md",
            ):
                self.assertTrue(paths[key].exists(), key)
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND185_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round185_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round185_r1_loop12_industrial_infra", text)


if __name__ == "__main__":
    unittest.main()
