import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round66_r13_loop2_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round66_r13_loop2_cross_archetype_redteam import (
    ROUND66_CASE_CANDIDATES,
    ROUND66_LARGE_SECTOR,
    ROUND66_OVERLAY_TARGETS,
    render_round66_price_validation_plan_markdown,
    render_round66_redteam_gate_plan_markdown,
    render_round66_summary_markdown,
    round66_case_candidate_rows,
    round66_case_records,
    round66_price_field_rows,
    round66_score_profile_rows,
    round66_stage_date_rows,
    round66_summary,
    round66_target_for,
    write_round66_r13_loop2_reports,
)


class Round66R13Loop2CrossArchetypeRedTeamTests(unittest.TestCase):
    def test_round66_targets_cover_loop2_overlays(self):
        labels = {target.target_id for target in ROUND66_OVERLAY_TARGETS}

        self.assertEqual(len(labels), 16)
        for label in (
            "STRUCTURAL_SUCCESS_ALIGNED",
            "SECTOR_SUCCESS_BUT_4B_WATCH",
            "PRICE_ONLY_RALLY",
            "EVENT_PREMIUM",
            "EVENT_TO_CONTRACT_ESCALATION",
            "CYCLICAL_SUCCESS",
            "FALSE_POSITIVE_SCORE",
            "EVIDENCE_GOOD_BUT_PRICE_FAILED",
            "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
            "OPERATIONAL_TRUST_BREAK",
            "LEGAL_REGULATORY_REDTEAM",
            "LEVERAGE_FCF_BREAKDOWN",
            "COMMERCIALIZATION_FAILURE",
            "AFFO_CASHFLOW_INTEGRITY_RISK",
            "STABLECOIN_CONVERTIBILITY_RISK",
            "UNKNOWN_INSUFFICIENT_EVIDENCE",
        ):
            self.assertIn(label, labels)

    def test_round66_new_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.EVENT_TO_CONTRACT_ESCALATION,
            E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH,
            E2RArchetype.COMMERCIALIZATION_FAILURE,
            E2RArchetype.AFFO_CASHFLOW_INTEGRITY_RISK,
            E2RArchetype.STABLECOIN_CONVERTIBILITY_RISK,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_round66_green_and_hard_gate_rules_are_explicit(self):
        structural = round66_target_for("STRUCTURAL_SUCCESS_ALIGNED")
        sector_4b = round66_target_for("SECTOR_SUCCESS_BUT_4B_WATCH")
        accounting = round66_target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")
        stablecoin = round66_target_for("STABLECOIN_CONVERTIBILITY_RISK")
        event_contract = round66_target_for("EVENT_TO_CONTRACT_ESCALATION")

        self.assertIsNotNone(structural)
        self.assertIsNotNone(sector_4b)
        self.assertIsNotNone(accounting)
        self.assertIsNotNone(stablecoin)
        self.assertIsNotNone(event_contract)
        assert structural is not None
        assert sector_4b is not None
        assert accounting is not None
        assert stablecoin is not None
        assert event_contract is not None
        self.assertEqual(structural.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertTrue(structural.stage3_green_allowed)
        self.assertFalse(sector_4b.stage3_green_allowed)
        self.assertIn("valuation_saturation", sector_4b.red_flags)
        self.assertTrue(accounting.hard_gate)
        self.assertIn("auditor_resignation", accounting.red_flags)
        self.assertTrue(stablecoin.hard_gate)
        self.assertIn("depeg_event", stablecoin.red_flags)
        self.assertFalse(event_contract.hard_gate)
        self.assertIn("binding_contract", event_contract.stage2_signals)

    def test_required_round66_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round66_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND66_CASE_CANDIDATES))
        self.assertEqual(rows["sk_hynix_hbm_memory_structural_4b_watch_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["supermicro_accounting_trust_4c_case"]["stage4c_date"], "2024-10-30")
        self.assertEqual(rows["crowdstrike_operational_trust_break_case"]["stage4c_date"], "2024-07-31")
        self.assertEqual(rows["terrausd_luna_algorithmic_stablecoin_break_case"]["target_id"], "STABLECOIN_CONVERTIBILITY_RISK")
        self.assertEqual(rows["terrausd_luna_algorithmic_stablecoin_break_case"]["stage4c_date"], "2022-05-12")
        self.assertEqual(rows["bluebird_bio_commercialization_failure_case"]["target_id"], "COMMERCIALIZATION_FAILURE")
        self.assertEqual(rows["bluebird_bio_commercialization_failure_case"]["stage4c_date"], "2025-02-21")
        self.assertEqual(rows["novo_nordisk_glp1_4b_to_4c_case"]["stage4b_date"], "2025-07-29")
        self.assertEqual(rows["novo_nordisk_glp1_4b_to_4c_case"]["stage4c_date"], "2026-02-04")
        self.assertEqual(rows["korea_buyback_cancellation_policy_to_execution_case"]["target_id"], "EVENT_TO_CONTRACT_ESCALATION")
        self.assertEqual(rows["event_to_contract_escalation_reference_case"]["case_type"], "success_candidate")
        self.assertEqual(rows["equinix_affo_cashflow_integrity_case"]["target_id"], "AFFO_CASHFLOW_INTEGRITY_RISK")

    def test_case_records_validate_and_keep_green_guardrails(self):
        records = round66_case_records()

        self.assertEqual(len(records), len(ROUND66_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND66_LARGE_SECTOR)
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn(
                "stage3_green_requires_cross_evidence_eps_fcf_price_alignment_no_hard_redteam_no_saturated_4b",
                record.green_guardrails,
            )
            self.assertIn("hard_redteam_blocks_green", record.green_guardrails)

    def test_score_profile_rows_are_overlay_not_production_scoring(self):
        rows = round66_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND66_OVERLAY_TARGETS))
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["redteam_gate"], "hard_block")
        self.assertEqual(by_target["AFFO_CASHFLOW_INTEGRITY_RISK"]["redteam_gate"], "reit_hard_review")
        self.assertEqual(by_target["STABLECOIN_CONVERTIBILITY_RISK"]["hard_gate"], "true")
        self.assertEqual(by_target["PRICE_ONLY_RALLY"]["stage3_green_allowed"], "false")
        self.assertEqual(by_target["STRUCTURAL_SUCCESS_ALIGNED"]["stage3_green_allowed"], "true")

    def test_stage_date_and_price_fields_cover_loop2_needs(self):
        stage_rows = {row["target_id"]: row for row in round66_stage_date_rows()}
        price_fields = {row["field"] for row in round66_price_field_rows()}

        self.assertIn("auditor_resignation", stage_rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("4b_watch", stage_rows["SECTOR_SUCCESS_BUT_4B_WATCH"]["stage4b"])
        self.assertIn("government_order", stage_rows["EVENT_TO_CONTRACT_ESCALATION"]["stage2"])
        self.assertIn("depeg", stage_rows["STABLECOIN_CONVERTIBILITY_RISK"]["stage4c"])
        self.assertIn("MFE_5D", price_fields)
        self.assertIn("MFE_2Y", price_fields)
        self.assertIn("MAE_1Y", price_fields)
        self.assertIn("auditor_resignation_flag", price_fields)
        self.assertIn("operational_trust_break_flag", price_fields)
        self.assertIn("affo_integrity_risk_flag", price_fields)
        self.assertIn("algorithmic_stablecoin_flag", price_fields)
        self.assertIn("stage_after_redteam", price_fields)

    def test_summary_and_markdown_explain_loop2_validation_layer(self):
        summary = round66_summary()
        summary_md = render_round66_summary_markdown()
        gate_plan = render_round66_redteam_gate_plan_markdown()
        price_plan = render_round66_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 16)
        self.assertEqual(summary["case_candidate_count"], 18)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 4)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["hard_gate_target_count"], 7)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("common validation overlay", summary_md)
        self.assertIn("Do not apply Round66 overlay symbols", gate_plan)
        self.assertIn("score-before-RedTeam", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round66_r13_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r13_loop2_round66.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round66_r13_loop2_v2.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["target_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["redteam_gate_plan"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND66_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round66_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round66_r13_loop2_cross_archetype_redteam", text)


if __name__ == "__main__":
    unittest.main()
