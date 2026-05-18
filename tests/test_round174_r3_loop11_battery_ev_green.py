import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round174_r3_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round174_r3_loop11_battery_ev_green import (
    ROUND174_BASE_SCORE_WEIGHTS,
    ROUND174_CASE_CANDIDATES,
    ROUND174_PRICE_FIELDS,
    ROUND174_SCORE_STAGE_PRICE_ALIGNMENT,
    ROUND174_SCORE_TARGETS,
    ROUND174_SOURCE_CANONICAL_TARGET_COUNT,
    ROUND174_SOURCE_CANONICAL_TARGET_IDS,
    ROUND174_STAGE_CAPS,
    render_round174_green_guardrail_markdown,
    render_round174_loop11_risk_overlay_markdown,
    render_round174_price_validation_plan_markdown,
    render_round174_score_stage_price_alignment_markdown,
    render_round174_summary_markdown,
    round174_base_score_weight_rows,
    round174_case_candidate_rows,
    round174_case_records,
    round174_price_field_rows,
    round174_score_profile_rows,
    round174_score_stage_price_alignment_rows,
    round174_stage_cap_rows,
    round174_stage_date_rows,
    round174_summary,
    round174_target_for,
    write_round174_r3_loop11_reports,
)


class Round174R3Loop11BatteryEVGreenTests(unittest.TestCase):
    def test_round174_targets_cover_source_archetypes(self):
        labels = {target.target_id for target in ROUND174_SCORE_TARGETS}

        self.assertEqual(ROUND174_SOURCE_CANONICAL_TARGET_COUNT, 12)
        self.assertEqual(len(labels), 12)
        self.assertEqual(set(ROUND174_SOURCE_CANONICAL_TARGET_IDS), labels)
        for target in ROUND174_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.BATTERY_EV_GREEN)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r3_loop11_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.ESS_LFP_GRID_STORAGE_KOREA,
            E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA,
            E2RArchetype.ANODE_GRAPHITE_SUPPLYCHAIN_KOREA,
            E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY,
            E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA,
            E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA,
            E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE,
            E2RArchetype.ELECTROLYTE_CAPA_SUPPLYCHAIN,
            E2RArchetype.SILICON_ANODE_COMMERCIALIZATION,
            E2RArchetype.EVENT_LITHIUM_PRICE_RALLY,
            E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK,
            E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_loop11_base_score_weights_and_stage_caps_match_round_note(self):
        weights = {row["component"]: row for row in round174_base_score_weight_rows()}
        caps = {row["stage_band"]: row for row in round174_stage_cap_rows()}

        self.assertEqual(len(ROUND174_BASE_SCORE_WEIGHTS), 7)
        self.assertEqual(weights["eps_fcf_opm_conversion"]["points"], "24")
        self.assertEqual(weights["contract_visibility"]["points"], "22")
        self.assertEqual(weights["capa_utilization_line_conversion"]["points"], "14")
        self.assertEqual(weights["structural_demand_shift"]["points"], "12")
        self.assertEqual(weights["early_price_path_validation"]["points"], "10")
        self.assertEqual(weights["safety_regulatory_disclosure_confidence"]["points"], "8")
        self.assertEqual(weights["valuation_room_4b_runway"]["points"], "10")
        self.assertEqual(len(ROUND174_STAGE_CAPS), 6)
        self.assertEqual(caps["Stage 1"]["max_score"], "45")
        self.assertEqual(caps["Stage 2"]["max_score"], "70")
        self.assertEqual(caps["Stage 2 strong"]["max_score"], "watch")
        self.assertIn("requires_4_of_7", caps["Stage 3"]["max_score"])
        self.assertIn("one_day_event_rally_10_20pct", caps["Stage 4B"]["required_evidence"])
        self.assertIn("customer_contract_cancelled", caps["Stage 4C"]["required_evidence"])

    def test_loop11_target_rules_separate_contracts_events_and_hard_gates(self):
        ess = round174_target_for("ESS_LFP_GRID_STORAGE_KOREA")
        redeploy = round174_target_for("EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA")
        graphite = round174_target_for("ANODE_GRAPHITE_SUPPLYCHAIN_KOREA")
        lithium = round174_target_for("LITHIUM_RESOURCE_SECURITY_KOREA")
        materials = round174_target_for("BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA")
        separator = round174_target_for("SEPARATOR_EV_DEMAND_CYCLE")
        event = round174_target_for("EVENT_LITHIUM_PRICE_RALLY")
        cancellation = round174_target_for("CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK")
        disclosure = round174_target_for("DISCLOSURE_CONFIDENCE_CAP")

        for target in (ess, redeploy, graphite, lithium, materials, separator, event, cancellation, disclosure):
            self.assertIsNotNone(target)
        assert ess is not None
        assert redeploy is not None
        assert graphite is not None
        assert lithium is not None
        assert materials is not None
        assert separator is not None
        assert event is not None
        assert cancellation is not None
        assert disclosure is not None
        self.assertEqual(ess.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("ess_contract_value", ess.stage2_signals)
        self.assertIn("customer_undisclosed", ess.red_flags)
        self.assertEqual(redeploy.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("converted_line_utilization", redeploy.stage3_conditions)
        self.assertEqual(graphite.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("tariff_event_rally_20pct", graphite.stage4b_conditions)
        self.assertIn("lithium_cycle", lithium.red_flags)
        self.assertEqual(materials.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("operating_loss", materials.red_flags)
        self.assertIn("sale_review", separator.stage4c_conditions)
        self.assertTrue(event.hard_gate)
        self.assertIn("event_rally_only", event.red_flags)
        self.assertTrue(cancellation.hard_gate)
        self.assertIn("customer_strategy_stable", cancellation.green_conditions)
        self.assertIn("customer_strategy_risk", cancellation.red_flags)
        self.assertEqual(disclosure.score_weight.eps_fcf_opm, "cap")

    def test_required_round174_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round174_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND174_CASE_CANDIDATES))
        self.assertEqual(rows["samsung_sdi_ess_lfp_stage2_case"]["stage2_date"], "2025-12-09")
        self.assertEqual(rows["samsung_sdi_ess_lfp_stage2_case"]["target_id"], "ESS_LFP_GRID_STORAGE_KOREA")
        self.assertIn("line_conversion", rows["samsung_sdi_ess_lfp_stage2_case"]["evidence_fields"])
        self.assertEqual(rows["posco_future_m_graphite_tariff_4b_case"]["case_type"], "4b_watch")
        self.assertIn("price_reaction_20pct", rows["posco_future_m_graphite_tariff_4b_case"]["evidence_fields"])
        self.assertEqual(rows["posco_holdings_lithium_resource_stage2_case"]["stage2_date"], "2025-11-11")
        self.assertEqual(rows["lg_chem_cathode_toyota_stage2_case"]["stage2_date"], "2025-09-08")
        self.assertEqual(rows["lg_chem_exxon_non_binding_lithium_case"]["case_type"], "event_premium")
        self.assertEqual(rows["lnf_lithium_event_rally_case"]["target_id"], "EVENT_LITHIUM_PRICE_RALLY")
        self.assertEqual(rows["skiet_separator_sale_review_4c_case"]["stage4c_date"], "2024-05-15")
        self.assertEqual(rows["ecopro_materials_ev_slowdown_4c_case"]["target_id"], "BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA")
        self.assertEqual(rows["wcp_separator_watch_red_case"]["target_id"], "SEPARATOR_EV_DEMAND_CYCLE")
        self.assertEqual(rows["enchem_electrolyte_capa_watch_case"]["target_id"], "ELECTROLYTE_CAPA_SUPPLYCHAIN")
        self.assertEqual(rows["daejoo_silicon_anode_commercialization_case"]["target_id"], "SILICON_ANODE_COMMERCIALIZATION")

    def test_case_records_validate_and_keep_loop11_guardrails(self):
        records = round174_case_records()

        self.assertEqual(len(records), len(ROUND174_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "BATTERY_EV_GREEN")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("stage3_early_catch_requires_4_of_7_loop11_conditions", record.green_guardrails)
            self.assertIn("policy_tariff_lithium_event_non_binding_deal_and_capa_narrative_do_not_create_green", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["samsung_sdi_ess_lfp_stage2_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["posco_future_m_graphite_tariff_4b_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["lg_chem_exxon_non_binding_lithium_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["skiet_separator_sale_review_4c_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["ecopro_materials_ev_slowdown_4c_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["wcp_separator_watch_red_case"].rerating_result, "no_rerating")

    def test_score_profile_rows_mark_no_production_change(self):
        rows = round174_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND174_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["large_sector"], "BATTERY_EV_GREEN")
            self.assertEqual(row["production_scoring_changed"], "false")
            self.assertIn("loop11_penalty_axes", row)
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["ESS_LFP_GRID_STORAGE_KOREA"]["eps_fcf_opm"], "24")
        self.assertEqual(by_target["ESS_LFP_GRID_STORAGE_KOREA"]["contract_visibility"], "22")
        self.assertEqual(by_target["EVENT_LITHIUM_PRICE_RALLY"]["hard_gate"], "true")
        self.assertEqual(by_target["EVENT_LITHIUM_PRICE_RALLY"]["eps_fcf_opm"], "event")
        self.assertEqual(by_target["CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK"]["hard_gate"], "true")
        self.assertEqual(by_target["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf_opm"], "cap")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round174_stage_date_rows()}
        fields = {row["field"] for row in round174_price_field_rows()}

        self.assertIn("ess_opm", rows["ESS_LFP_GRID_STORAGE_KOREA"]["stage3"])
        self.assertIn("line_conversion_plan", rows["EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA"]["stage2"])
        self.assertIn("tariff_event_rally_20pct", rows["ANODE_GRAPHITE_SUPPLYCHAIN_KOREA"]["stage4b"])
        self.assertIn("operating_loss", rows["BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA"]["stage4c"])
        self.assertIn("sale_review", rows["SEPARATOR_EV_DEMAND_CYCLE"]["stage4c"])
        self.assertIn("one_day_10_20pct_event_rally", rows["EVENT_LITHIUM_PRICE_RALLY"]["stage4b"])
        self.assertIn("customer_contract_cancelled", rows["CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK"]["stage4c"])
        for field in (
            "price_at_stage2",
            "return_60d_after_stage2",
            "return_120d_after_stage2",
            "mfe_120d_after_stage2",
            "relative_strength_vs_battery_basket",
            "contract_amount",
            "contract_counterparty",
            "contract_period",
            "gwh_or_tonnage",
            "production_start_date",
            "line_conversion_flag",
            "converted_line_utilization",
            "ess_opm",
            "raw_material_price_exposure",
            "lithium_price_exposure",
            "graphite_tariff_flag",
            "quarterly_price_negotiation_flag",
            "non_binding_offtake_flag",
            "inventory_loss_flag",
            "customer_strategy_risk",
            "sale_review_flag",
            "factory_idle_flag",
            "operating_loss_flag",
            "customer_undisclosed_flag",
            "disclosure_confidence",
            "valuation_at_stage4b",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)

    def test_score_stage_price_alignment_rows_and_markdown(self):
        rows = {row["case_id"]: row for row in round174_score_stage_price_alignment_rows()}
        markdown = render_round174_score_stage_price_alignment_markdown()

        self.assertEqual(len(rows), len(ROUND174_SCORE_STAGE_PRICE_ALIGNMENT))
        self.assertEqual(rows["samsung_sdi_ess_lfp_stage2_case"]["verdict"], "stage2_strong_not_green_yet")
        self.assertEqual(rows["posco_future_m_graphite_tariff_4b_case"]["verdict"], "supply_chain_event_not_green")
        self.assertEqual(rows["skiet_separator_sale_review_4c_case"]["verdict"], "hard_redteam_alignment")
        self.assertIn("Samsung SDI", markdown)
        self.assertIn("POSCO Future M", markdown)
        self.assertIn("4B", markdown)

    def test_summary_and_markdown_explain_r3_loop11_guardrails(self):
        summary = round174_summary()
        summary_md = render_round174_summary_markdown()
        guardrails = render_round174_green_guardrail_markdown()
        overlays = render_round174_loop11_risk_overlay_markdown()
        price_plan = render_round174_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 12)
        self.assertEqual(summary["source_canonical_target_count"], 12)
        self.assertEqual(summary["case_candidate_count"], len(ROUND174_CASE_CANDIDATES))
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R3 Loop 11", summary_md)
        self.assertIn("EPS/FCF/OPM 24", summary_md)
        self.assertIn("Do not apply R3 Loop-11", guardrails)
        self.assertIn("SEPARATOR_DEMAND_4C", overlays)
        self.assertIn("samsung_sdi_ess_lfp_stage2_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            paths = write_round174_r3_loop11_reports(
                output_directory=tmp_path / "out",
                cases_path=tmp_path / "cases.jsonl",
                score_profile_path=tmp_path / "profiles.csv",
            )

            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND174_CASE_CANDIDATES))
            summary = paths["summary"].read_text(encoding="utf-8")
            self.assertIn("Round-174 R3 Loop-11", summary)
            self.assertIn("production_scoring_changed: false", summary)

    def test_cli_argument_parser_supports_paths(self):
        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--score-profiles",
                "profiles.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.score_profiles, "profiles.csv")

    def test_production_scoring_modules_do_not_import_round174_pack(self):
        root = Path(__file__).resolve().parents[1]
        forbidden = "round174_r3_loop11_battery_ev_green"
        for relative in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/scoring.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = (root / relative).read_text(encoding="utf-8")
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
