from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round312_r4_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round312_r4_loop16_materials_spread_strategic_trigger_validation import (
    ROUND312_4C_WATCH_GATES,
    ROUND312_CASE_CANDIDATES,
    ROUND312_GREEN_BLOCKERS,
    ROUND312_LARGE_SECTOR,
    ROUND312_REQUIRED_TARGET_ALIASES,
    ROUND312_ROW_SEPARATION_RULES,
    ROUND312_SCORE_DOWN_AXES,
    ROUND312_SCORE_UP_AXES,
    ROUND312_SHADOW_WEIGHT_ROWS,
    ROUND312_STAGE2_ACTIONABLE_RULES,
    ROUND312_STAGE3_GREEN_RULES,
    ROUND312_STAGE3_YELLOW_RULES,
    ROUND312_STAGE4B_WATCH_TRIGGERS,
    ROUND312_TRIGGER_RECORDS,
    render_round312_stage4b_4c_review_markdown,
    render_round312_stage_rules_markdown,
    render_round312_trigger_grid_markdown,
    round312_audit_payload,
    round312_case_records,
    round312_case_rows,
    round312_shadow_weight_rows,
    round312_summary,
    round312_trigger_rows,
    write_round312_r4_loop16_reports,
)


class Round312R4Loop16MaterialsSpreadStrategicTests(unittest.TestCase):
    def test_round312_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND312_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND312_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND312_REQUIRED_TARGET_ALIASES["STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF"],
            E2RArchetype.STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF.value,
        )
        self.assertEqual(
            ROUND312_REQUIRED_TARGET_ALIASES["COPPER_TC_RC_SPREAD_4C_WATCH"],
            E2RArchetype.COPPER_TC_RC_SPREAD_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND312_REQUIRED_TARGET_ALIASES["SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2"],
            E2RArchetype.SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2.value,
        )

    def test_archetype_definitions_capture_r4_loop16_rules(self) -> None:
        steel = archetype_definition(E2RArchetype.STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF)
        capex = archetype_definition(E2RArchetype.STEEL_US_LOCALIZATION_CAPEX_4B)
        petro_fail = archetype_definition(E2RArchetype.PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING)
        petro_relief = archetype_definition(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF)
        zinc = archetype_definition(E2RArchetype.CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B)
        lithium_jv = archetype_definition(E2RArchetype.LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2)
        lithium_beta = archetype_definition(E2RArchetype.LITHIUM_PRICE_BETA_CYCLICAL_STAGE2)
        copper = archetype_definition(E2RArchetype.COPPER_TC_RC_SPREAD_4C_WATCH)
        sodium = archetype_definition(E2RArchetype.SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2)

        self.assertIn("anti-dumping", " ".join(steel.stage2_candidate_signals))
        self.assertIn("capex ROI", " ".join(capex.stage3_high_conviction_signals))
        self.assertIn("operating loss", " ".join(petro_fail.stage4c_thesis_break_signals))
        self.assertIn("actual shutdown", " ".join(petro_relief.stage3_high_conviction_signals))
        self.assertIn("dilution", " ".join(zinc.stage4b_graduation_overheat_signals))
        self.assertIn("offtake terms", " ".join(lithium_jv.stage3_high_conviction_signals))
        self.assertIn("cathode ASP", " ".join(lithium_beta.stage3_high_conviction_signals))
        self.assertIn("TC/RC", " ".join(copper.stage4c_thesis_break_signals))
        self.assertIn("customer contract", " ".join(sodium.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round312_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND312_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round312_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_commodity_price_strategic_resource_capex_or_restructuring_headline_as_green_without_spread_margin_offtake_or_FCF", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round312_summary()
        self.assertEqual(summary["round_id"], "round_240")
        self.assertEqual(summary["large_sector"], ROUND312_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 11)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage2_event_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_spread_capex_lithium_copper_and_optionality(self) -> None:
        by_id = {case.case_id: case for case in ROUND312_CASE_CANDIDATES}
        steel = by_id["r4_loop16_hyundai_steel_posco_tariff_antidumping"]
        capex = by_id["r4_loop16_hyundai_steel_louisiana_capex"]
        oversupply = by_id["r4_loop16_lgchem_lotte_petrochemical_oversupply"]
        restructuring = by_id["r4_loop16_lotte_hdhyundai_petrochemical_restructuring"]
        zinc = by_id["r4_loop16_korea_zinc_tennessee_critical_minerals"]
        posco = by_id["r4_loop16_posco_minres_lithium_jv"]
        lithium = by_id["r4_loop16_catl_yichun_korea_lithium_beta"]
        copper = by_id["r4_loop16_copper_tcrc_spread_watch"]
        sodium = by_id["r4_loop16_lgchem_sinopec_sodium_ion_materials"]

        self.assertEqual(steel.extra_price_metrics["posco_tariff_event_price_krw"], 230500)
        self.assertEqual(steel.extra_price_metrics["hyundai_steel_antidumping_event_return_pct"], 5.8)
        self.assertIn("domestic_ASP_recovery_missing", steel.red_flag_fields)

        self.assertEqual(capex.extra_price_metrics["plant_investment_usd_bn"], 5.8)
        self.assertEqual(capex.extra_price_metrics["annual_capacity_mn_tons"], 2.7)
        self.assertEqual(capex.extra_price_metrics["late_session_event_return_pct"], -4.4)
        self.assertEqual(capex.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(oversupply.extra_price_metrics["lotte_chemical_2024_op_loss_krw_bn"], 895)
        self.assertEqual(oversupply.extra_price_metrics["lg_chem_op_yoy_pct"], -63.75)
        self.assertEqual(oversupply.rerating_result, "thesis_break")

        self.assertEqual(restructuring.extra_price_metrics["government_capacity_cut_target_pct"], 25)
        self.assertEqual(restructuring.extra_price_metrics["national_capacity_cut_target_mn_tons_per_year"], 3.7)

        self.assertEqual(zinc.extra_price_metrics["refinery_project_value_usd_bn"], 7.4)
        self.assertEqual(zinc.extra_price_metrics["new_share_sale_value_usd_bn"], 1.9)
        self.assertEqual(zinc.extra_price_metrics["injunction_news_event_return_pct"], -13)

        self.assertEqual(posco.extra_price_metrics["transaction_value_usd_mn"], 765)
        self.assertEqual(posco.extra_price_metrics["indirect_stake_wodgina_pct"], 15)
        self.assertEqual(posco.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(lithium.extra_price_metrics["lithium_futures_event_return_pct"], 8)
        self.assertEqual(lithium.extra_price_metrics["posco_future_m_event_return_pct"], 8.3)
        self.assertEqual(lithium.extra_price_metrics["l_and_f_event_return_pct"], 10)
        self.assertEqual(lithium.rerating_result, "cyclical_rerating")

        self.assertEqual(copper.extra_price_metrics["issue"], "copper_treatment_refining_charges_unsustainable")
        self.assertIn("copper_bull_without_TC_RC", copper.red_flag_fields)

        self.assertEqual(sodium.extra_price_metrics["china_sodium_ion_market_2025_gwh"], 10)
        self.assertEqual(sodium.extra_price_metrics["china_sodium_ion_market_2034_gwh"], 292)
        self.assertIn("customer_contract_missing", sodium.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round312_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round312_shadow_weight_rows()}
        rules_md = render_round312_stage_rules_markdown()
        trigger_md = render_round312_trigger_grid_markdown()
        stage_md = render_round312_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND312_TRIGGER_RECORDS), 11)
        self.assertEqual(trigger_rows["r4l16_steel_us_tariff_T0"]["promote_to"], "4C-watch")
        self.assertEqual(trigger_rows["r4l16_steel_antidumping_T1"]["promote_to"], "Stage2_relief")
        self.assertEqual(trigger_rows["r4l16_koreazinc_refinery_T0"]["promote_to"], "Stage2+4B")
        self.assertEqual(trigger_rows["r4l16_copper_tcrc_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND312_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF"]["domestic_spread_recovery"], "+5")
        self.assertEqual(shadow_rows["PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF"]["restructuring_plan_without_shutdown_penalty"], "-5")
        self.assertEqual(shadow_rows["COPPER_TC_RC_SPREAD_4C_WATCH"]["smelter_TC_RC_margin"], "+5")
        self.assertIn("commodity_price_or_policy_change_links_to_company_ASP_or_margin", ROUND312_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_spread_margin_offtake_capacity_cut_dilution_or_commercialization_gate_remains_open", ROUND312_STAGE3_YELLOW_RULES)
        self.assertIn("strategic_resource_investment_has_clear_offtake_or_customer_demand", ROUND312_STAGE3_GREEN_RULES)
        self.assertIn("copper_bull_without_TC_RC", ROUND312_GREEN_BLOCKERS)
        self.assertIn("smelter_TC_RC_margin", ROUND312_SCORE_UP_AXES)
        self.assertIn("strategic_resource_capex_without_offtake", ROUND312_SCORE_DOWN_AXES)
        self.assertIn("plant_localization_capex_reverses_price_intraday", ROUND312_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("smelter_TC_RC_negative_economics", ROUND312_4C_WATCH_GATES)
        self.assertIn("do_not_treat_commodity_price_capex_restructuring_or_strategic_resource_headline_as_margin_offtake_or_FCF", ROUND312_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r4_loop16_korea_zinc_tennessee_critical_minerals", trigger_md)
        self.assertIn("r4_loop16_copper_tcrc_spread_watch", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round312_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_312.md")
        self.assertEqual(audit["round_id"], "round_240")
        self.assertEqual(audit["large_sector"], ROUND312_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_commodity_price_strategic_resource_capex_or_restructuring_headline_as_green_without_spread_margin_offtake_or_FCF", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--triggers",
                "triggers.jsonl",
                "--audit",
                "audit.json",
                "--weight-profile",
                "weights.csv",
            ]
        )
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")
        self.assertEqual(args.weight_profile, "weights.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round312_r4_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round312_case_rows()
            self.assertEqual(len(records), len(ROUND312_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND312_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND312_TRIGGER_RECORDS))
            self.assertIn("Korea Zinc", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r4l16_steel_antidumping_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("COPPER_TC_RC_SPREAD_4C_WATCH", paths["weight_profiles"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
