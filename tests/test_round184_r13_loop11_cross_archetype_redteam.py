import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round184_r13_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round184_r13_loop11_cross_archetype_redteam import (
    ROUND184_CASE_CANDIDATES,
    ROUND184_LARGE_SECTOR,
    ROUND184_OVERLAY_AXES,
    ROUND184_OVERLAY_TARGETS,
    ROUND184_PRICE_FIELDS,
    ROUND184_SOURCE_CANONICAL_TARGET_COUNT,
    ROUND184_SOURCE_CANONICAL_TARGET_IDS,
    ROUND184_STAGE_CAPS,
    render_round184_price_validation_plan_markdown,
    render_round184_redteam_gate_plan_markdown,
    render_round184_score_stage_price_alignment_markdown,
    render_round184_summary_markdown,
    round184_case_candidate_rows,
    round184_case_records,
    round184_overlay_axis_rows,
    round184_price_field_rows,
    round184_score_profile_rows,
    round184_score_stage_price_alignment_rows,
    round184_stage_cap_rows,
    round184_stage_date_rows,
    round184_summary,
    round184_target_for,
    write_round184_r13_loop11_reports,
)


class Round184R13Loop11CrossArchetypeRedTeamTests(unittest.TestCase):
    def test_round184_targets_cover_loop11_common_buckets(self):
        labels = {target.target_id for target in ROUND184_OVERLAY_TARGETS}

        self.assertEqual(len(labels), 10)
        self.assertEqual(ROUND184_SOURCE_CANONICAL_TARGET_COUNT, 10)
        self.assertEqual(set(ROUND184_SOURCE_CANONICAL_TARGET_IDS), labels)
        for label in (
            "STRUCTURAL_STAGE3_EARLY_CAPTURE",
            "STAGE2_STRONG_NOT_GREEN",
            "EVENT_PRICE_RALLY_NOT_STAGE3",
            "STRUCTURAL_SUCCESS_BUT_4B_WATCH",
            "CYCLE_SUCCESS_NOT_STRUCTURAL",
            "DISCLOSURE_CONFIDENCE_CAP",
            "PRIVATE_OR_HOLDCO_LINK_CAP",
            "OPERATIONAL_TRUST_HARD_4C",
            "LEGAL_GOVERNANCE_4C_WATCH",
            "POLICY_MARKET_SHOCK_OVERLAY",
        ):
            self.assertIn(label, labels)

    def test_round184_new_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.STRUCTURAL_STAGE3_EARLY_CAPTURE,
            E2RArchetype.STAGE2_STRONG_NOT_GREEN,
            E2RArchetype.CYCLE_SUCCESS_NOT_STRUCTURAL,
            E2RArchetype.PRIVATE_OR_HOLDCO_LINK_CAP,
            E2RArchetype.OPERATIONAL_TRUST_HARD_4C,
            E2RArchetype.LEGAL_GOVERNANCE_4C_WATCH,
            E2RArchetype.POLICY_MARKET_SHOCK_OVERLAY,
            E2RArchetype.EVENT_PRICE_RALLY_NOT_STAGE3,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_overlay_axes_and_stage_caps_match_round184_note(self):
        axis_weights = {axis.axis_id: axis.points for axis in ROUND184_OVERLAY_AXES}
        self.assertEqual(
            axis_weights,
            {
                "eps_fcf_roe_affo_opm_bodyweight_change": 24,
                "cross_evidence_visibility": 20,
                "price_path_early_validation": 14,
                "repeatability_durability": 14,
                "redteam_hard_4c_risk": 14,
                "disclosure_confidence": 8,
                "valuation_room_4b_margin": 6,
            },
        )
        self.assertEqual(len(round184_overlay_axis_rows()), 7)
        self.assertEqual(len(ROUND184_STAGE_CAPS), 4)
        stage_rows = {row["stage_band"]: row for row in round184_stage_cap_rows()}
        self.assertEqual(stage_rows["Stage 3"]["max_score"], "requires_6_of_9")
        self.assertIn("op_eps_fcf_or_roe_affo_opm_improvement", stage_rows["Stage 3"]["required_evidence"])
        self.assertEqual(stage_rows["Stage 2 strong"]["max_score"], "70")
        self.assertEqual(stage_rows["Stage 4B"]["max_score"], "requires_4_of_7")
        self.assertEqual(stage_rows["Stage 4C"]["max_score"], "hard_gate")
        self.assertIn("fatal_accident_or_safety_inspection", stage_rows["Stage 4C"]["required_evidence"])
        for row in round184_overlay_axis_rows():
            self.assertEqual(row["production_scoring_changed"], "false")
        for row in stage_rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_green_allowed_and_hard_gate_rules_are_explicit(self):
        structural = round184_target_for("STRUCTURAL_STAGE3_EARLY_CAPTURE")
        stage2 = round184_target_for("STAGE2_STRONG_NOT_GREEN")
        event = round184_target_for("EVENT_PRICE_RALLY_NOT_STAGE3")
        disclosure = round184_target_for("DISCLOSURE_CONFIDENCE_CAP")
        holdco = round184_target_for("PRIVATE_OR_HOLDCO_LINK_CAP")
        operational = round184_target_for("OPERATIONAL_TRUST_HARD_4C")
        legal = round184_target_for("LEGAL_GOVERNANCE_4C_WATCH")
        policy = round184_target_for("POLICY_MARKET_SHOCK_OVERLAY")

        self.assertTrue(structural and structural.stage3_green_allowed)
        self.assertTrue(stage2 and not stage2.stage3_green_allowed)
        self.assertTrue(event and event.hard_gate)
        self.assertIn("price_only", event.red_flags)
        self.assertTrue(disclosure and not disclosure.stage3_green_allowed)
        self.assertIn("media_only", disclosure.red_flags)
        self.assertTrue(holdco and not holdco.stage3_green_allowed)
        self.assertIn("holdco_link_missing", holdco.red_flags)
        self.assertTrue(operational and operational.hard_gate)
        self.assertIn("fatal_accident", operational.red_flags)
        self.assertTrue(legal and legal.hard_gate)
        self.assertIn("founder_legal", legal.red_flags)
        self.assertTrue(policy and policy.hard_gate)
        self.assertIn("policy_market_shock", policy.red_flags)

    def test_required_round184_cases_are_present(self):
        rows = {row["case_id"]: row for row in round184_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND184_CASE_CANDIDATES))
        self.assertEqual(rows["hanmi_hbm_equipment_stage3_early_capture_case"]["target_id"], "STRUCTURAL_STAGE3_EARLY_CAPTURE")
        self.assertIn("unconfirmed_customer_report", rows["hanmi_hbm_equipment_stage3_early_capture_case"]["red_flag_fields"])
        self.assertEqual(rows["samsung_sds_kkr_cb_stage2_not_green_case"]["stage4b_date"], "2026-04-15")
        self.assertEqual(rows["kogas_daesung_gas_event_4b_case"]["target_id"], "EVENT_PRICE_RALLY_NOT_STAGE3")
        self.assertEqual(rows["kogas_daesung_gas_event_4b_case"]["stage4b_date"], "2024-06-03")
        self.assertEqual(rows["jeju_air_fatal_accident_hard_4c_case"]["target_id"], "OPERATIONAL_TRUST_HARD_4C")
        self.assertEqual(rows["jeju_air_fatal_accident_hard_4c_case"]["stage4c_date"], "2024-12-30")
        self.assertEqual(rows["naver_dunamu_holdco_link_stage2_case"]["target_id"], "PRIVATE_OR_HOLDCO_LINK_CAP")
        self.assertEqual(rows["oci_spacex_mipo_loi_lgchem_nonbinding_cap_case"]["target_id"], "DISCLOSURE_CONFIDENCE_CAP")
        self.assertEqual(rows["policy_market_shock_overlay_korea_case"]["target_id"], "POLICY_MARKET_SHOCK_OVERLAY")

    def test_case_records_validate_and_keep_guardrails(self):
        records = round184_case_records()

        self.assertEqual(len(records), len(ROUND184_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND184_LARGE_SECTOR)
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("stage3_green_requires_6_of_9_loop11_checks", record.green_guardrails)
            self.assertIn("hard_4c_blocks_green", record.green_guardrails)
            self.assertIn("event_price_path_is_not_stage3_evidence_alone", record.green_guardrails)

    def test_score_profile_rows_are_overlay_not_production_scoring(self):
        rows = round184_score_profile_rows()
        by_target = {row["target_id"]: row for row in rows}

        self.assertEqual(len(rows), len(ROUND184_OVERLAY_TARGETS))
        self.assertEqual(by_target["STRUCTURAL_STAGE3_EARLY_CAPTURE"]["stage3_green_allowed"], "true")
        self.assertEqual(by_target["STAGE2_STRONG_NOT_GREEN"]["stage3_green_allowed"], "false")
        self.assertEqual(by_target["EVENT_PRICE_RALLY_NOT_STAGE3"]["hard_gate"], "true")
        self.assertEqual(by_target["DISCLOSURE_CONFIDENCE_CAP"]["hard_gate"], "false")
        self.assertEqual(by_target["OPERATIONAL_TRUST_HARD_4C"]["hard_gate"], "true")
        self.assertEqual(by_target["POLICY_MARKET_SHOCK_OVERLAY"]["hard_gate"], "true")
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_price_and_alignment_rows_cover_loop11_needs(self):
        stage_rows = {row["target_id"]: row for row in round184_stage_date_rows()}
        price_fields = {row["field"] for row in round184_price_field_rows()}
        alignment_rows = {row["case_id"]: row for row in round184_score_stage_price_alignment_rows()}

        self.assertIn("blocked_without_eps_fcf_contract_repeat_revenue", stage_rows["EVENT_PRICE_RALLY_NOT_STAGE3"]["stage3"])
        self.assertIn("fatal_accident", stage_rows["OPERATIONAL_TRUST_HARD_4C"]["stage4c"])
        self.assertIn("media_report", stage_rows["DISCLOSURE_CONFIDENCE_CAP"]["stage1"])
        for field in (
            "return_60d_after_stage2",
            "mfe_120d_after_stage2",
            "relative_strength_vs_sector_basket",
            "op_revision_before_stage3",
            "contract_counterparty",
            "royalty_revenue",
            "arr_or_bookings",
            "opendart_detail_flag",
            "media_report_only_flag",
            "event_price_only_flag",
            "stage3_green_allowed",
            "stage4c_hard_flag",
            "valuation_at_stage4b",
        ):
            self.assertIn(field, price_fields)
        self.assertEqual(alignment_rows["jeju_air_fatal_accident_hard_4c_case"]["verdict"], "operational_trust_hard_4c")
        self.assertEqual(alignment_rows["kogas_daesung_gas_event_4b_case"]["verdict"], "event_price_rally_not_stage3")

    def test_summary_and_markdown_explain_common_checkpoint(self):
        summary = round184_summary()
        summary_md = render_round184_summary_markdown()
        gate_plan = render_round184_redteam_gate_plan_markdown()
        price_plan = render_round184_price_validation_plan_markdown()
        alignment_md = render_round184_score_stage_price_alignment_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["source_canonical_target_count"], 10)
        self.assertEqual(summary["overlay_axis_count"], 7)
        self.assertEqual(summary["stage_cap_count"], 4)
        self.assertEqual(summary["case_candidate_count"], 15)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 4)
        self.assertEqual(summary["hard_gate_target_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("common validation overlay", summary_md)
        self.assertIn("source_canonical_target_count: 10", summary_md)
        self.assertIn("Do not apply Round184 overlay weights", gate_plan)
        self.assertIn("Hard 4C gates", gate_plan)
        self.assertIn("Required Fields", price_plan)
        self.assertIn("Samsung SDS shows Stage 2 strong", alignment_md)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round184_r13_loop11_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r13_loop11_round184.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round184_r13_loop11_v11.csv",
            )

            for key in (
                "cases",
                "score_profiles",
                "summary",
                "case_matrix",
                "stage_date_plan",
                "redteam_gate_plan",
                "price_validation_plan",
                "price_fields",
                "overlay_axes",
                "stage_caps",
                "score_stage_price_alignment",
                "score_stage_price_alignment_md",
            ):
                self.assertTrue(paths[key].exists(), key)
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND184_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round184_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round184_r13_loop11_cross_archetype_redteam", text)


if __name__ == "__main__":
    unittest.main()
