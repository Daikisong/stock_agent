import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round92_r13_loop4_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round92_r13_loop4_cross_archetype_redteam import (
    ROUND92_CASE_CANDIDATES,
    ROUND92_LARGE_SECTOR,
    ROUND92_OVERLAY_TARGETS,
    render_round92_price_validation_plan_markdown,
    render_round92_redteam_gate_plan_markdown,
    render_round92_summary_markdown,
    round92_case_candidate_rows,
    round92_case_records,
    round92_price_field_rows,
    round92_score_profile_rows,
    round92_stage_date_rows,
    round92_summary,
    round92_target_for,
    write_round92_r13_loop4_reports,
)


class Round92R13Loop4CrossArchetypeRedTeamTests(unittest.TestCase):
    def test_round92_targets_cover_loop4_overlays(self):
        labels = {target.target_id for target in ROUND92_OVERLAY_TARGETS}

        self.assertEqual(len(labels), 19)
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
            "CAPEX_AFFO_DILUTION_RISK",
            "STABLECOIN_CONVERTIBILITY_RISK",
            "POLICY_MARKET_SHOCK_EVENT",
            "DISCLOSURE_CONFIDENCE_CAP",
            "UNKNOWN_INSUFFICIENT_EVIDENCE",
        ):
            self.assertIn(label, labels)

    def test_round92_new_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.EVENT_TO_CONTRACT_ESCALATION,
            E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH,
            E2RArchetype.COMMERCIALIZATION_FAILURE,
            E2RArchetype.AFFO_CASHFLOW_INTEGRITY_RISK,
            E2RArchetype.CAPEX_AFFO_DILUTION_RISK,
            E2RArchetype.STABLECOIN_CONVERTIBILITY_RISK,
            E2RArchetype.POLICY_MARKET_SHOCK_EVENT,
            E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_round92_green_and_hard_gate_rules_are_explicit(self):
        structural = round92_target_for("STRUCTURAL_SUCCESS_ALIGNED")
        sector_4b = round92_target_for("SECTOR_SUCCESS_BUT_4B_WATCH")
        accounting = round92_target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")
        stablecoin = round92_target_for("STABLECOIN_CONVERTIBILITY_RISK")
        policy_shock = round92_target_for("POLICY_MARKET_SHOCK_EVENT")
        event_contract = round92_target_for("EVENT_TO_CONTRACT_ESCALATION")
        capex_affo = round92_target_for("CAPEX_AFFO_DILUTION_RISK")
        disclosure_cap = round92_target_for("DISCLOSURE_CONFIDENCE_CAP")

        self.assertIsNotNone(structural)
        self.assertIsNotNone(sector_4b)
        self.assertIsNotNone(accounting)
        self.assertIsNotNone(stablecoin)
        self.assertIsNotNone(policy_shock)
        self.assertIsNotNone(event_contract)
        self.assertIsNotNone(capex_affo)
        self.assertIsNotNone(disclosure_cap)
        assert structural is not None
        assert sector_4b is not None
        assert accounting is not None
        assert stablecoin is not None
        assert policy_shock is not None
        assert event_contract is not None
        assert capex_affo is not None
        assert disclosure_cap is not None
        self.assertEqual(structural.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertTrue(structural.stage3_green_allowed)
        self.assertFalse(sector_4b.stage3_green_allowed)
        self.assertIn("valuation_saturation", sector_4b.red_flags)
        self.assertTrue(accounting.hard_gate)
        self.assertIn("auditor_resignation", accounting.red_flags)
        self.assertTrue(stablecoin.hard_gate)
        self.assertIn("depeg_event", stablecoin.red_flags)
        self.assertTrue(policy_shock.hard_gate)
        self.assertIn("policy_market_shock", policy_shock.red_flags)
        self.assertIn("crowded_trade_unwind", policy_shock.stage4b_conditions)
        self.assertFalse(event_contract.hard_gate)
        self.assertIn("binding_contract", event_contract.stage2_signals)
        self.assertTrue(capex_affo.hard_gate)
        self.assertIn("capex_growth_above_affo_growth", capex_affo.stage4c_conditions)
        self.assertFalse(disclosure_cap.hard_gate)
        self.assertFalse(disclosure_cap.stage3_green_allowed)
        self.assertEqual(disclosure_cap.score_weight.redteam_gate, "stage3_confidence_cap")
        self.assertIn("detail_missing", disclosure_cap.red_flags)

    def test_required_round92_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round92_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND92_CASE_CANDIDATES))
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
        self.assertEqual(rows["circle_regulated_stablecoin_infra_4b_watch_case"]["target_id"], "SECTOR_SUCCESS_BUT_4B_WATCH")
        self.assertEqual(rows["circle_regulated_stablecoin_infra_4b_watch_case"]["stage4b_date"], "2026-05-11")
        self.assertEqual(rows["event_to_contract_escalation_reference_case"]["case_type"], "success_candidate")
        self.assertEqual(rows["korea_ai_tax_policy_market_shock_case"]["target_id"], "POLICY_MARKET_SHOCK_EVENT")
        self.assertEqual(rows["korea_ai_tax_policy_market_shock_case"]["stage4b_date"], "2026-05-12")
        self.assertEqual(rows["equinix_affo_cashflow_integrity_case"]["target_id"], "AFFO_CASHFLOW_INTEGRITY_RISK")
        self.assertEqual(rows["equinix_capex_affo_dilution_case"]["target_id"], "CAPEX_AFFO_DILUTION_RISK")
        self.assertEqual(rows["equinix_capex_affo_dilution_case"]["stage4c_date"], "2026-05-08")
        self.assertEqual(rows["opendart_disclosure_confidence_cap_reference_case"]["target_id"], "DISCLOSURE_CONFIDENCE_CAP")

    def test_case_records_validate_and_keep_green_guardrails(self):
        records = round92_case_records()

        self.assertEqual(len(records), len(ROUND92_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND92_LARGE_SECTOR)
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
        rows = round92_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND92_OVERLAY_TARGETS))
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["redteam_gate"], "hard_block")
        self.assertEqual(by_target["AFFO_CASHFLOW_INTEGRITY_RISK"]["redteam_gate"], "reit_hard_review")
        self.assertEqual(by_target["CAPEX_AFFO_DILUTION_RISK"]["redteam_gate"], "reit_infra_hard_review")
        self.assertEqual(by_target["CAPEX_AFFO_DILUTION_RISK"]["hard_gate"], "true")
        self.assertEqual(by_target["STABLECOIN_CONVERTIBILITY_RISK"]["hard_gate"], "true")
        self.assertEqual(by_target["POLICY_MARKET_SHOCK_EVENT"]["redteam_gate"], "policy_price_path_shock")
        self.assertEqual(by_target["POLICY_MARKET_SHOCK_EVENT"]["hard_gate"], "true")
        self.assertEqual(by_target["DISCLOSURE_CONFIDENCE_CAP"]["redteam_gate"], "stage3_confidence_cap")
        self.assertEqual(by_target["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        self.assertEqual(by_target["PRICE_ONLY_RALLY"]["stage3_green_allowed"], "false")
        self.assertEqual(by_target["STRUCTURAL_SUCCESS_ALIGNED"]["stage3_green_allowed"], "true")

    def test_stage_date_and_price_fields_cover_loop4_needs(self):
        stage_rows = {row["target_id"]: row for row in round92_stage_date_rows()}
        price_fields = {row["field"] for row in round92_price_field_rows()}

        self.assertIn("auditor_resignation", stage_rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("4b_watch", stage_rows["SECTOR_SUCCESS_BUT_4B_WATCH"]["stage4b"])
        self.assertIn("government_order", stage_rows["EVENT_TO_CONTRACT_ESCALATION"]["stage2"])
        self.assertIn("depeg", stage_rows["STABLECOIN_CONVERTIBILITY_RISK"]["stage4c"])
        self.assertIn("market_wide_policy_shock", stage_rows["POLICY_MARKET_SHOCK_EVENT"]["stage4c"])
        self.assertIn("capex_growth_above_affo_growth", stage_rows["CAPEX_AFFO_DILUTION_RISK"]["stage4c"])
        self.assertIn("detail_missing", stage_rows["DISCLOSURE_CONFIDENCE_CAP"]["stage4c"])
        self.assertIn("MFE_5D", price_fields)
        self.assertIn("MFE_2Y", price_fields)
        self.assertIn("MAE_1Y", price_fields)
        self.assertIn("opendart_detail_fetched_flag", price_fields)
        self.assertIn("contract_amount_disclosed_flag", price_fields)
        self.assertIn("customer_name_disclosed_flag", price_fields)
        self.assertIn("auditor_resignation_flag", price_fields)
        self.assertIn("operational_trust_break_flag", price_fields)
        self.assertIn("affo_integrity_risk_flag", price_fields)
        self.assertIn("capex_to_affo_ratio", price_fields)
        self.assertIn("capex_affo_dilution_risk_flag", price_fields)
        self.assertIn("capex_growth_above_affo_growth_flag", price_fields)
        self.assertIn("power_water_permitting_flag", price_fields)
        self.assertIn("stablecoin_type", price_fields)
        self.assertIn("stablecoin_circulation", price_fields)
        self.assertIn("reserve_income", price_fields)
        self.assertIn("redemption_at_par_flag", price_fields)
        self.assertIn("algorithmic_stablecoin_flag", price_fields)
        self.assertIn("policy_market_shock_flag", price_fields)
        self.assertIn("disclosure_confidence_capped_flag", price_fields)
        self.assertIn("stage_confidence_cap_reason", price_fields)
        self.assertIn("stage_after_redteam", price_fields)

    def test_summary_and_markdown_explain_loop4_validation_layer(self):
        summary = round92_summary()
        summary_md = render_round92_summary_markdown()
        gate_plan = render_round92_redteam_gate_plan_markdown()
        price_plan = render_round92_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 19)
        self.assertEqual(summary["case_candidate_count"], 22)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 5)
        self.assertEqual(summary["stage4b_case_count"], 4)
        self.assertEqual(summary["stage4c_case_count"], 8)
        self.assertEqual(summary["hard_gate_target_count"], 9)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("common validation overlay", summary_md)
        self.assertIn("Do not apply Round92 overlay symbols", gate_plan)
        self.assertIn("capex/AFFO dilution", gate_plan)
        self.assertIn("score-before-RedTeam", price_plan)
        self.assertIn("disclosure_confidence_capped", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round92_r13_loop4_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r13_loop4_round92.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round92_r13_loop4_v4.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND92_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round92_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round92_r13_loop4_cross_archetype_redteam", text)


if __name__ == "__main__":
    unittest.main()
