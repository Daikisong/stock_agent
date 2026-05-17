import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round96_r4_loop5_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round96_r4_loop5_materials_spread_strategic import (
    ROUND96_CASE_CANDIDATES,
    ROUND96_PRICE_FIELDS,
    ROUND96_SCORE_TARGETS,
    render_round96_green_guardrail_markdown,
    render_round96_price_validation_plan_markdown,
    render_round96_risk_overlay_markdown,
    render_round96_summary_markdown,
    round96_case_candidate_rows,
    round96_case_records,
    round96_price_field_rows,
    round96_score_profile_rows,
    round96_stage_date_rows,
    round96_summary,
    round96_target_for,
    write_round96_r4_loop5_reports,
)


class Round96R4Loop5MaterialsSpreadStrategicTests(unittest.TestCase):
    def test_round96_targets_cover_r4_loop5_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND96_SCORE_TARGETS}

        self.assertEqual(len(labels), 22)
        for label in (
            "REFINING_OIL_SPREAD",
            "LUBRICANTS_HIGH_MARGIN_MIX",
            "CHEMICAL_SPREAD",
            "STEEL_METAL_SPREAD",
            "IRON_ORE_CHINA_DEMAND_CYCLE",
            "NONFERROUS_STRATEGIC_METALS",
            "COPPER_AI_GRID_STRUCTURAL_DEMAND",
            "COPPER_PROCESSING_INPUT_COST_OVERLAY",
            "RARE_METALS_PRICE_FLOOR_OFFTAKE",
            "RARE_EARTH_MAGNET_SUPPLY_CHAIN",
            "RARE_METALS_EXPORT_CONTROL_EVENT",
            "LITHIUM_ESS_DEMAND_CYCLE",
            "PRECIOUS_METALS_SAFE_HAVEN_MINERS",
            "GOLD_MINER_JURISDICTION_RERATING",
            "GENERAL_TRADING_RESOURCE_INFRA",
            "LNG_ENERGY_TRADING_DISTRIBUTION",
            "PAPER_PACKAGING_CYCLE",
            "ADVANCED_MATERIAL_SPECULATIVE_THEME",
            "SPECULATIVE_SCIENCE_THEME",
            "EVENT_PREMIUM_GOVERNANCE_OVERLAY",
            "COMMODITY_PRICE_4C_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND96_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.MATERIALS_SPREAD_STRATEGIC)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop5_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE,
            E2RArchetype.RARE_EARTH_MAGNET_SUPPLY_CHAIN,
            E2RArchetype.RARE_METALS_EXPORT_CONTROL_EVENT,
            E2RArchetype.LUBRICANTS_HIGH_MARGIN_MIX,
            E2RArchetype.COPPER_AI_GRID_STRUCTURAL_DEMAND,
            E2RArchetype.COPPER_PROCESSING_INPUT_COST_OVERLAY,
            E2RArchetype.GOLD_MINER_JURISDICTION_RERATING,
            E2RArchetype.IRON_ORE_CHINA_DEMAND_CYCLE,
            E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY,
            E2RArchetype.COMMODITY_PRICE_4C_OVERLAY,
            E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
            E2RArchetype.LITHIUM_ESS_DEMAND_CYCLE,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_resource_targets_split_structural_offtake_from_export_control_event(self):
        rare = round96_target_for("RARE_METALS_PRICE_FLOOR_OFFTAKE")
        magnet = round96_target_for("RARE_EARTH_MAGNET_SUPPLY_CHAIN")
        export_control = round96_target_for("RARE_METALS_EXPORT_CONTROL_EVENT")
        copper = round96_target_for("COPPER_AI_GRID_STRUCTURAL_DEMAND")
        copper_cost = round96_target_for("COPPER_PROCESSING_INPUT_COST_OVERLAY")
        gold_jurisdiction = round96_target_for("GOLD_MINER_JURISDICTION_RERATING")
        trading = round96_target_for("GENERAL_TRADING_RESOURCE_INFRA")
        lng = round96_target_for("LNG_ENERGY_TRADING_DISTRIBUTION")
        chemical = round96_target_for("CHEMICAL_SPREAD")
        event = round96_target_for("EVENT_PREMIUM_GOVERNANCE_OVERLAY")
        disclosure = round96_target_for("DISCLOSURE_CONFIDENCE_CAP")

        for target in (rare, magnet, export_control, copper, copper_cost, gold_jurisdiction, trading, lng, chemical, event, disclosure):
            self.assertIsNotNone(target)
        assert rare is not None
        assert magnet is not None
        assert export_control is not None
        assert copper is not None
        assert copper_cost is not None
        assert gold_jurisdiction is not None
        assert trading is not None
        assert lng is not None
        assert chemical is not None
        assert event is not None
        assert disclosure is not None
        self.assertEqual(rare.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("price_floor", rare.green_conditions)
        self.assertIn("offtake_contract", rare.green_conditions)
        self.assertEqual(magnet.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("customer_qualification", magnet.green_conditions)
        self.assertEqual(export_control.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("export_license_delay", export_control.stage1_signals)
        self.assertIn("no_production_capacity", export_control.red_flags)
        self.assertEqual(copper.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("low_cost_production", copper.green_conditions)
        self.assertTrue(copper_cost.gate_only)
        self.assertIn("processing_cost_squeeze", copper_cost.red_flags)
        self.assertEqual(gold_jurisdiction.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("safe_jurisdiction_assets", gold_jurisdiction.green_conditions)
        self.assertEqual(trading.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("capital_return", trading.green_conditions)
        self.assertEqual(lng.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("fid_status", lng.green_conditions)
        self.assertEqual(chemical.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("china_middle_east_capacity_glut", chemical.red_flags)
        self.assertTrue(event.gate_only)
        self.assertEqual(event.score_weight.eps_fcf, "gate")
        self.assertTrue(disclosure.gate_only)
        self.assertEqual(disclosure.score_weight.eps_fcf, "cap")

    def test_required_round96_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round96_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND96_CASE_CANDIDATES))
        self.assertEqual(rows["mp_materials_dod_price_floor_case"]["target_id"], "RARE_METALS_PRICE_FLOOR_OFFTAKE")
        self.assertEqual(rows["mp_materials_dod_price_floor_case"]["stage2_date"], "")
        self.assertEqual(rows["mp_materials_apple_magnet_contract_case"]["target_id"], "RARE_EARTH_MAGNET_SUPPLY_CHAIN")
        self.assertEqual(rows["mp_materials_apple_magnet_contract_case"]["price_validation_status"], "needs_exact_stage_date_backfill")
        self.assertEqual(rows["china_heavy_rare_earth_export_control_case"]["target_id"], "RARE_METALS_EXPORT_CONTROL_EVENT")
        self.assertEqual(rows["china_heavy_rare_earth_export_control_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["china_yttrium_dysprosium_terbium_delay_case"]["stage2_date"], "2026-05-15")
        self.assertEqual(rows["copper_ai_grid_record_high_case"]["stage2_date"], "2026-05-11")
        self.assertEqual(rows["equinox_orla_gold_jurisdiction_case"]["target_id"], "GOLD_MINER_JURISDICTION_RERATING")
        self.assertEqual(rows["equinox_orla_gold_jurisdiction_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["posco_international_alaska_lng_20y_case"]["stage2_date"], "2025-12-04")
        self.assertEqual(rows["barrick_record_gold_buyback_case"]["stage4b_date"], "2026-05-11")
        self.assertEqual(rows["sk_innovation_refining_recovery_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["lg_chem_lotte_chemical_oversupply_case"]["stage4c_date"], "2025-02-07")
        self.assertEqual(rows["lithium_price_86pct_crash_case"]["target_id"], "LITHIUM_ESS_DEMAND_CYCLE")
        self.assertEqual(rows["lithium_price_86pct_crash_case"]["stage4c_date"], "2025-01-13")
        self.assertNotIn("lithium_ess_demand_recovery_case", rows)
        self.assertEqual(rows["bhp_iron_ore_profit_dividend_cut_case"]["target_id"], "IRON_ORE_CHINA_DEMAND_CYCLE")
        self.assertEqual(rows["bhp_iron_ore_profit_dividend_cut_case"]["stage4c_date"], "2025-02-18")
        self.assertEqual(rows["korea_zinc_tender_offer_event_case"]["target_id"], "EVENT_PREMIUM_GOVERNANCE_OVERLAY")
        self.assertEqual(rows["korea_zinc_share_issue_probe_case"]["stage4c_date"], "2024-10-31")
        self.assertEqual(rows["international_paper_ds_smith_divestment_case"]["stage2_date"], "2025-04-14")
        self.assertEqual(rows["graphene_mxene_superconductor_theme_case"]["case_type"], "overheat")

    def test_case_records_validate_and_keep_loop5_guardrails(self):
        records = round96_case_records()

        self.assertEqual(len(records), len(ROUND96_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "MATERIALS_SPREAD_STRATEGIC")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("commodity_price_is_not_structural_evidence", record.green_guardrails)
            self.assertIn("require_price_floor_offtake_production_fcf_for_rare_metals_green", record.green_guardrails)
            self.assertIn("do_not_invent_spread_offtake_price_floor_fcf_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["korea_zinc_tender_offer_event_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["korea_zinc_share_issue_probe_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["lg_chem_lotte_chemical_oversupply_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["graphene_mxene_superconductor_theme_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertIn("price_floor", by_id["mp_materials_dod_price_floor_case"].must_have_fields)
        self.assertIn("customer_qualification", by_id["mp_materials_apple_magnet_contract_case"].must_have_fields)
        self.assertEqual(by_id["equinox_orla_gold_jurisdiction_case"].primary_archetype, E2RArchetype.GOLD_MINER_JURISDICTION_RERATING)

    def test_score_profile_rows_match_round96_weight_table(self):
        rows = {row["target_id"]: row for row in round96_score_profile_rows()}

        self.assertEqual(rows["REFINING_OIL_SPREAD"]["eps_fcf"], "20")
        self.assertEqual(rows["CHEMICAL_SPREAD"]["eps_fcf"], "17")
        self.assertEqual(rows["CHEMICAL_SPREAD"]["structural_visibility"], "6")
        self.assertEqual(rows["RARE_METALS_PRICE_FLOOR_OFFTAKE"]["eps_fcf"], "20")
        self.assertEqual(rows["RARE_METALS_PRICE_FLOOR_OFFTAKE"]["structural_visibility"], "22")
        self.assertEqual(rows["RARE_EARTH_MAGNET_SUPPLY_CHAIN"]["structural_visibility"], "21")
        self.assertEqual(rows["RARE_METALS_EXPORT_CONTROL_EVENT"]["bottleneck_pricing"], "18")
        self.assertEqual(rows["COPPER_AI_GRID_STRUCTURAL_DEMAND"]["bottleneck_pricing"], "17")
        self.assertEqual(rows["COPPER_PROCESSING_INPUT_COST_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["PRECIOUS_METALS_SAFE_HAVEN_MINERS"]["eps_fcf"], "20")
        self.assertEqual(rows["GOLD_MINER_JURISDICTION_RERATING"]["capital_allocation"], "5")
        self.assertEqual(rows["IRON_ORE_CHINA_DEMAND_CYCLE"]["eps_fcf"], "16")
        self.assertEqual(rows["GENERAL_TRADING_RESOURCE_INFRA"]["valuation"], "18")
        self.assertEqual(rows["LNG_ENERGY_TRADING_DISTRIBUTION"]["structural_visibility"], "18")
        self.assertEqual(rows["EVENT_PREMIUM_GOVERNANCE_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["COMMODITY_PRICE_4C_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round96_stage_date_rows()}
        fields = {row["field"] for row in round96_price_field_rows()}

        self.assertIn("inventory_gain_loss_excluded", rows["REFINING_OIL_SPREAD"]["stage2"])
        self.assertIn("china_middle_east_capacity_glut", rows["CHEMICAL_SPREAD"]["stage4c"])
        self.assertIn("tariff_inventory_unwind", rows["COPPER_AI_GRID_STRUCTURAL_DEMAND"]["stage4c"])
        self.assertIn("processing_cost_squeeze", rows["COPPER_PROCESSING_INPUT_COST_OVERLAY"]["stage4c"])
        self.assertIn("price_floor", rows["RARE_METALS_PRICE_FLOOR_OFFTAKE"]["stage2"])
        self.assertIn("apple_prepayment", rows["RARE_EARTH_MAGNET_SUPPLY_CHAIN"]["stage2"])
        self.assertIn("export_license_delay", rows["RARE_METALS_EXPORT_CONTROL_EVENT"]["stage1"])
        self.assertIn("export_control_relief", rows["RARE_METALS_EXPORT_CONTROL_EVENT"]["stage4c"])
        self.assertIn("mna_dilution", rows["GOLD_MINER_JURISDICTION_RERATING"]["stage4c"])
        self.assertIn("dividend_cut", rows["IRON_ORE_CHINA_DEMAND_CYCLE"]["stage4c"])
        self.assertIn("sodium_ion_substitution", rows["LITHIUM_ESS_DEMAND_CYCLE"]["stage4c"])
        self.assertIn("tender_offer", rows["EVENT_PREMIUM_GOVERNANCE_OVERLAY"]["stage1"])
        self.assertIn("contract_value_missing", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage4c"])
        for field in (
            "commodity_price_at_stage",
            "inventory_gain_loss",
            "refining_margin",
            "lubricants_mix_ratio",
            "copper_inventory_distortion_flag",
            "tariff_stockpile_flag",
            "demand_destruction_flag",
            "sulfuric_acid_cost_change",
            "processing_input_cost_risk_flag",
            "offtake_contract_flag",
            "price_floor_flag",
            "government_investment_amount",
            "prepayment_amount",
            "rare_earth_export_control_flag",
            "yttrium_export_delay_flag",
            "dysprosium_shortage_flag",
            "terbium_shortage_flag",
            "gold_realized_price",
            "jurisdiction_quality_score",
            "gold_mna_flag",
            "mna_dilution_flag",
            "integration_risk_flag",
            "lng_contract_volume_mtpa",
            "fid_status",
            "tender_offer_flag",
            "share_issuance_after_tender_flag",
            "regulator_probe_flag",
            "regulator_revision_order_flag",
            "event_premium_flag",
            "speculative_material_theme_flag",
            "magnet_production_flag",
            "magnet_production_start_year",
            "customer_qualification_flag",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND96_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r4_loop5_guardrails(self):
        summary = round96_summary()
        summary_md = render_round96_summary_markdown()
        guardrails = render_round96_green_guardrail_markdown()
        overlays = render_round96_risk_overlay_markdown()
        price_plan = render_round96_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 22)
        self.assertEqual(summary["case_candidate_count"], 16)
        self.assertEqual(summary["structural_success_count"], 0)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 2)
        self.assertEqual(summary["event_premium_count"], 4)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 4)
        self.assertEqual(summary["green_possible_count"], 6)
        self.assertEqual(summary["redteam_first_count"], 8)
        self.assertEqual(summary["gate_only_target_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R4 Loop 5", summary_md)
        self.assertIn("price floor", summary_md)
        self.assertIn("Do not apply R4 Loop-5 v5.0 weights", guardrails)
        self.assertIn("EXPORT_CONTROL_EVENT_ONLY", overlays)
        self.assertIn("RARE_EARTH_MAGNET_SUPPLY_CHAIN_ALIGNED", overlays)
        self.assertIn("COPPER_INPUT_COST_RISK", overlays)
        self.assertIn("GOLD_MINER_JURISDICTION_RERATING", overlays)
        self.assertIn("COMMODITY_PRICE_4C", overlays)
        self.assertIn("mp_materials_dod_price_floor_case", price_plan)
        self.assertIn("mp_materials_apple_magnet_contract_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round96_r4_loop5_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r4_loop5_round96.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round96_r4_loop5_v5.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND96_CASE_CANDIDATES))

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

    def test_production_modules_do_not_import_round96_pack(self):
        root = Path(__file__).resolve().parents[1]
        for relative in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = (root / relative).read_text(encoding="utf-8")
            self.assertNotIn("round96_r4_loop5_materials_spread_strategic", text)


if __name__ == "__main__":
    unittest.main()
