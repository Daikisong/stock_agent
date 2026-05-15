import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round32_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round32_score_weight_v17 import (
    ROUND32_CASE_CANDIDATES,
    ROUND32_SCORE_TARGETS,
    render_round32_ai_chip_revenue_gate_markdown,
    render_round32_energy_cycle_markdown,
    render_round32_memory_split_markdown,
    render_round32_summary_markdown,
    round32_case_records,
    round32_score_profile_rows,
    round32_summary,
    target_for,
    write_round32_score_weight_reports,
)


class Round32ScoreWeightV17Tests(unittest.TestCase):
    def test_round32_targets_include_v17_thin_archetype_families(self):
        labels = {target.target_id for target in ROUND32_SCORE_TARGETS}

        self.assertEqual(len(labels), 8)
        self.assertIn("GENERAL_TRADING_RESOURCE_INFRA", labels)
        self.assertIn("LNG_ENERGY_TRADING_DISTRIBUTION", labels)
        self.assertIn("DISPLAY_OLED_SUPPLYCHAIN", labels)
        self.assertIn("ELECTRONIC_COMPONENTS_MLCC_SENSOR", labels)
        self.assertIn("DIGITAL_HEALTHCARE_REMOTE_MEDICINE", labels)
        self.assertIn("COMMODITY_MEMORY_GENERAL_SEMI", labels)
        self.assertIn("ENERGY_UTILITY_LNG_GAS", labels)
        self.assertIn("AI_CHIP_FABRIC_INFRA", labels)

    def test_general_trading_requires_contract_project_fcf_and_capital_return(self):
        target = target_for("GENERAL_TRADING_RESOURCE_INFRA")
        records = {record.case_id: record for record in round32_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.score_weight.capital_allocation, 8)
        self.assertIn("long_term_offtake", target.green_conditions)
        self.assertIn("shareholder_return", target.green_conditions)
        self.assertIn("commodity_price", target.red_flags)
        self.assertEqual(records["posco_international_alaska_lng_20y_contract_candidate"].case_type, "success_candidate")
        self.assertEqual(records["conglomerate_discount_no_capital_return_counterexample"].case_type, "failed_rerating")

    def test_lng_energy_and_utility_are_cycle_or_tariff_capped(self):
        energy = target_for("LNG_ENERGY_TRADING_DISTRIBUTION")
        utility = target_for("ENERGY_UTILITY_LNG_GAS")
        markdown = render_round32_energy_cycle_markdown()
        records = {record.case_id: record for record in round32_case_records()}

        self.assertIsNotNone(energy)
        self.assertIsNotNone(utility)
        assert energy is not None
        assert utility is not None
        self.assertEqual(energy.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(utility.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("inventory_loss", energy.red_flags)
        self.assertIn("receivables", utility.red_flags)
        self.assertEqual(records["sk_innovation_refining_recovery_watch"].case_type, "cyclical_success")
        self.assertEqual(records["tariff_freeze_debt_4c"].case_type, "4c_thesis_break")
        self.assertIn("long-term LNG/offtake evidence", markdown)

    def test_oled_and_components_are_green_possible_but_inventory_and_price_risks_apply(self):
        oled = target_for("DISPLAY_OLED_SUPPLYCHAIN")
        components = target_for("ELECTRONIC_COMPONENTS_MLCC_SENSOR")
        records = {record.case_id: record for record in round32_case_records()}

        self.assertIsNotNone(oled)
        self.assertIsNotNone(components)
        assert oled is not None
        assert components is not None
        self.assertEqual(oled.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(components.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("panel_price_competition", oled.red_flags)
        self.assertIn("inventory_cycle", components.red_flags)
        self.assertEqual(records["apple_all_iphone_oled_transition_candidate"].case_type, "success_candidate")
        self.assertEqual(records["rare_earth_supply_chain_risk_4c"].case_type, "4c_thesis_break")

    def test_digital_healthcare_requires_reimbursement_and_unit_economics(self):
        target = target_for("DIGITAL_HEALTHCARE_REMOTE_MEDICINE")
        records = {record.case_id: record for record in round32_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.score_weight.information_confidence, 6)
        self.assertIn("reimbursement_visible", target.green_conditions)
        self.assertIn("unit_economics", target.red_flags)
        self.assertEqual(records["telemedicine_no_reimbursement_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["remote_care_unit_economics_4c"].case_type, "4c_thesis_break")

    def test_commodity_memory_is_split_from_hbm_visibility(self):
        target = target_for("COMMODITY_MEMORY_GENERAL_SEMI")
        markdown = render_round32_memory_split_markdown()
        records = {record.case_id: record for record in round32_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.score_weight.eps_fcf, 22)
        self.assertEqual(target.score_weight.structural_visibility, 16)
        self.assertIn("spot_rebound_only", target.red_flags)
        self.assertEqual(records["samsung_commodity_memory_price_recovery_candidate"].case_type, "cyclical_success")
        self.assertEqual(records["ai_capex_slowdown_memory_4c"].case_type, "4c_thesis_break")
        self.assertIn("Commodity DRAM/NAND and HBM should not receive the same visibility credit", markdown)

    def test_ai_chip_is_redteam_first_until_contract_validation_and_revenue(self):
        target = target_for("AI_CHIP_FABRIC_INFRA")
        markdown = render_round32_ai_chip_revenue_gate_markdown()
        records = {record.case_id: record for record in round32_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("mass_production_revenue", target.green_conditions)
        self.assertIn("no_revenue", target.red_flags)
        self.assertIn("yield", target.red_flags)
        self.assertEqual(records["ai_chip_related_stock_no_revenue_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["foundry_yield_customer_validation_4c"].case_type, "4c_thesis_break")
        self.assertIn("RedTeam-first", markdown)

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round32_case_records()

        self.assertEqual(len(records), len(ROUND32_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round32_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v17_not_production_scoring(self):
        summary = round32_summary()
        markdown = render_round32_summary_markdown()

        self.assertEqual(summary["target_count"], 8)
        self.assertEqual(summary["case_candidate_count"], 32)
        self.assertEqual(summary["success_candidate_count"], 15)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 2)
        self.assertEqual(summary["redteam_first_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policy labels, CAPEX headlines, and price rallies are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round32_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v14_round32.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round32_v17.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["energy_cycle"].exists())
            self.assertTrue(paths["memory_split"].exists())
            self.assertTrue(paths["ai_chip_revenue_gate"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND32_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round32_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round32_score_weight_v17", text)


if __name__ == "__main__":
    unittest.main()
