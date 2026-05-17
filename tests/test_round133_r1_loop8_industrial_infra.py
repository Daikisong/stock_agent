import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round133_r1_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round133_r1_loop8_industrial_infra import (
    ROUND133_BASE_SCORE_WEIGHTS,
    ROUND133_CASE_CANDIDATES,
    ROUND133_PRICE_FIELDS,
    ROUND133_SCORE_STAGE_PRICE_ALIGNMENT,
    ROUND133_SCORE_TARGETS,
    ROUND133_STAGE_CAPS,
    render_round133_green_guardrail_markdown,
    render_round133_loop8_risk_overlay_markdown,
    render_round133_price_validation_plan_markdown,
    render_round133_score_stage_price_alignment_markdown,
    render_round133_summary_markdown,
    round133_base_score_weight_rows,
    round133_case_candidate_rows,
    round133_case_records,
    round133_price_field_rows,
    round133_score_profile_rows,
    round133_score_stage_price_alignment_rows,
    round133_stage_cap_rows,
    round133_stage_date_rows,
    round133_summary,
    round133_target_for,
    write_round133_r1_loop8_reports,
)


class Round133R1Loop8IndustrialInfraTests(unittest.TestCase):
    def test_round133_targets_cover_r1_loop8_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND133_SCORE_TARGETS}

        self.assertEqual(len(labels), 24)
        for label in (
            "GRID_TRANSFORMER_SHORTAGE",
            "GRID_EHV_TRANSFORMER_EXPORT",
            "GRID_MEDIUM_VOLTAGE_EXPANSION",
            "GRID_SUPPLY_SLOT_PREBUY",
            "AI_DATA_CENTER_POWER_EQUIPMENT",
            "GAS_TURBINE_POWER_BACKLOG",
            "POWER_EQUIPMENT_BACKLOG_TO_FCF",
            "DATA_CENTER_GRID_FLEXIBILITY_OVERLAY",
            "DATA_CENTER_POWER_WATER_PERMITTING",
            "CONTRACT_BACKLOG_INDUSTRIAL",
            "DEFENSE_GOVERNMENT_BACKLOG",
            "DEFENSE_LOCAL_PRODUCTION_PLATFORM",
            "DEFENSE_CAPITAL_ALLOCATION_SHOCK",
            "DEFENSE_US_SHIPBUILDING_PLATFORM",
            "SHIPBUILDING_OFFSHORE_BACKLOG",
            "SHIPBUILDING_NAVAL_MRO",
            "SHIPBUILDING_PROCUREMENT_LEADTIME",
            "RAIL_INFRASTRUCTURE",
            "NUCLEAR_EXISTING_PPA_RESTART",
            "NUCLEAR_GRID_INJECTION_RIGHTS",
            "NUCLEAR_SMR_GRID_POLICY",
            "GEOPOLITICAL_RECONSTRUCTION",
            "CAPITAL_ALLOCATION_DILUTION_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND133_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.INDUSTRIAL_ORDERS_INFRA)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r1_loop8_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.GRID_EHV_TRANSFORMER_EXPORT,
            E2RArchetype.GRID_MEDIUM_VOLTAGE_EXPANSION,
            E2RArchetype.GRID_SUPPLY_SLOT_PREBUY,
            E2RArchetype.GAS_TURBINE_POWER_BACKLOG,
            E2RArchetype.POWER_EQUIPMENT_BACKLOG_TO_FCF,
            E2RArchetype.DATA_CENTER_GRID_FLEXIBILITY_OVERLAY,
            E2RArchetype.DEFENSE_LOCAL_PRODUCTION_PLATFORM,
            E2RArchetype.DEFENSE_CAPITAL_ALLOCATION_SHOCK,
            E2RArchetype.DEFENSE_US_SHIPBUILDING_PLATFORM,
            E2RArchetype.SHIPBUILDING_NAVAL_MRO,
            E2RArchetype.SHIPBUILDING_PROCUREMENT_LEADTIME,
            E2RArchetype.NUCLEAR_EXISTING_PPA_RESTART,
            E2RArchetype.NUCLEAR_GRID_INJECTION_RIGHTS,
            E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING,
            E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY,
            E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_loop8_weights_and_penalties_are_stricter_than_loop2(self):
        transformer = round133_target_for("GRID_TRANSFORMER_SHORTAGE")
        ehv = round133_target_for("GRID_EHV_TRANSFORMER_EXPORT")
        medium_voltage = round133_target_for("GRID_MEDIUM_VOLTAGE_EXPANSION")
        slot_prebuy = round133_target_for("GRID_SUPPLY_SLOT_PREBUY")
        turbine = round133_target_for("GAS_TURBINE_POWER_BACKLOG")
        capital_return = round133_target_for("POWER_EQUIPMENT_BACKLOG_TO_FCF")
        grid_flex = round133_target_for("DATA_CENTER_GRID_FLEXIBILITY_OVERLAY")
        defense = round133_target_for("DEFENSE_GOVERNMENT_BACKLOG")
        defense_local = round133_target_for("DEFENSE_LOCAL_PRODUCTION_PLATFORM")
        defense_shock = round133_target_for("DEFENSE_CAPITAL_ALLOCATION_SHOCK")
        defense_us_shipbuilding = round133_target_for("DEFENSE_US_SHIPBUILDING_PLATFORM")
        procurement = round133_target_for("SHIPBUILDING_PROCUREMENT_LEADTIME")
        smr = round133_target_for("NUCLEAR_SMR_GRID_POLICY")
        ppa = round133_target_for("NUCLEAR_EXISTING_PPA_RESTART")
        nuclear_grid = round133_target_for("NUCLEAR_GRID_INJECTION_RIGHTS")
        permitting = round133_target_for("DATA_CENTER_POWER_WATER_PERMITTING")
        dilution = round133_target_for("CAPITAL_ALLOCATION_DILUTION_OVERLAY")
        disclosure_cap = round133_target_for("DISCLOSURE_CONFIDENCE_CAP")

        self.assertIsNotNone(transformer)
        self.assertIsNotNone(ehv)
        self.assertIsNotNone(medium_voltage)
        self.assertIsNotNone(slot_prebuy)
        self.assertIsNotNone(turbine)
        self.assertIsNotNone(capital_return)
        self.assertIsNotNone(grid_flex)
        self.assertIsNotNone(defense)
        self.assertIsNotNone(defense_local)
        self.assertIsNotNone(defense_shock)
        self.assertIsNotNone(defense_us_shipbuilding)
        self.assertIsNotNone(procurement)
        self.assertIsNotNone(smr)
        self.assertIsNotNone(ppa)
        self.assertIsNotNone(nuclear_grid)
        self.assertIsNotNone(permitting)
        self.assertIsNotNone(dilution)
        self.assertIsNotNone(disclosure_cap)
        assert transformer is not None
        assert ehv is not None
        assert medium_voltage is not None
        assert slot_prebuy is not None
        assert turbine is not None
        assert capital_return is not None
        assert grid_flex is not None
        assert defense is not None
        assert defense_local is not None
        assert defense_shock is not None
        assert defense_us_shipbuilding is not None
        assert procurement is not None
        assert smr is not None
        assert ppa is not None
        assert nuclear_grid is not None
        assert permitting is not None
        assert dilution is not None
        assert disclosure_cap is not None
        self.assertEqual(transformer.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(transformer.score_weight.eps_fcf, 24)
        self.assertEqual(transformer.score_weight.bottleneck_pricing, 24)
        self.assertIn("low_margin_long_term_contract", transformer.loop8_penalty_axes)
        self.assertEqual(ehv.score_weight.information_confidence, 6)
        self.assertIn("customer_project_delay", ehv.red_flags)
        self.assertEqual(medium_voltage.score_weight.bottleneck_pricing, 20)
        self.assertIn("price_normalization", medium_voltage.red_flags)
        self.assertEqual(slot_prebuy.score_weight.structural_visibility, 24)
        self.assertIn("slot_cancelled", slot_prebuy.red_flags)
        self.assertEqual(turbine.score_weight.eps_fcf, 21)
        self.assertIn("wind_segment_loss", turbine.red_flags)
        self.assertEqual(capital_return.score_weight.capital_allocation, 4)
        self.assertIn("buyback_cut", capital_return.stage4c_conditions)
        self.assertEqual(grid_flex.score_weight.eps_fcf, "gate")
        self.assertFalse(grid_flex.hard_gate)
        self.assertIn("capital_allocation_shock", defense.loop8_penalty_axes)
        self.assertEqual(defense_local.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(defense_shock.hard_gate)
        self.assertIn("use_of_proceeds_unclear", defense_shock.red_flags)
        self.assertIn("moa_only", defense_us_shipbuilding.red_flags)
        self.assertTrue(procurement.hard_gate)
        self.assertIn("pipe_spool_delay", procurement.red_flags)
        self.assertEqual(smr.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("customer_subscription_failure", smr.red_flags)
        self.assertEqual(ppa.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(nuclear_grid.hard_gate)
        self.assertIn("grid_rights_failure", nuclear_grid.red_flags)
        self.assertTrue(permitting.hard_gate)
        self.assertIn("moratorium", permitting.red_flags)
        self.assertTrue(dilution.hard_gate)
        self.assertIn("dilution", dilution.red_flags)
        self.assertFalse(disclosure_cap.hard_gate)
        self.assertEqual(disclosure_cap.score_weight.eps_fcf, "cap")
        self.assertIn("detail_missing", disclosure_cap.red_flags)

    def test_loop8_base_score_weights_and_stage_caps_are_explicit(self):
        weights = {row["component"]: row for row in round133_base_score_weight_rows()}
        caps = {row["stage_band"]: row for row in round133_stage_cap_rows()}

        self.assertEqual(len(ROUND133_BASE_SCORE_WEIGHTS), 7)
        self.assertEqual(weights["eps_fcf_revision"]["points"], "25")
        self.assertEqual(weights["contract_backlog_visibility"]["points"], "22")
        self.assertEqual(weights["bottleneck_pricing_power"]["points"], "18")
        self.assertEqual(weights["market_mispricing_gap"]["points"], "10")
        self.assertEqual(weights["valuation_room_4b_runway"]["points"], "7")
        self.assertEqual(weights["capital_discipline_fcf_conversion"]["points"], "10")
        self.assertEqual(weights["information_confidence_disclosure_detail"]["points"], "8")
        self.assertEqual(len(ROUND133_STAGE_CAPS), 5)
        self.assertEqual(caps["Stage 1"]["max_score"], "45")
        self.assertIn("mou_or_moa", caps["Stage 1"]["required_evidence"])
        self.assertEqual(caps["Stage 2"]["max_score"], "70")
        self.assertIn("ppa_or_slot_reservation_with_gate_status", caps["Stage 2"]["required_evidence"])
        self.assertIn("op_eps_fcf_revision", caps["Stage 3"]["required_evidence"])
        self.assertEqual(caps["Stage 4C"]["max_score"], "hard_gate")
        self.assertIn("profit_miss", caps["Stage 4C"]["required_evidence"])

    def test_score_stage_price_alignment_table_covers_round133_core_examples(self):
        rows = {row["case_id"]: row for row in round133_score_stage_price_alignment_rows()}

        self.assertEqual(len(ROUND133_SCORE_STAGE_PRICE_ALIGNMENT), 9)
        self.assertEqual(rows["ge_vernova_data_center_orders_case"]["verdict"], "score_to_stage_to_price_aligned")
        self.assertIn("4B watch", rows["ge_vernova_data_center_orders_case"]["normalization_adjustment"])
        self.assertEqual(rows["siemens_energy_fcf_buyback_case"]["verdict"], "partially_confirmed")
        self.assertEqual(rows["ls_electric_525kv_us_datacenter_transformer_case"]["detected_stage"], "Stage 2")
        self.assertEqual(rows["hyundai_rotem_morocco_rail_case"]["verdict"], "stage2_not_green_yet")
        self.assertEqual(rows["constellation_tmi_microsoft_restart_case"]["verdict"], "stage2_with_approval_gate")
        self.assertEqual(rows["hanwha_aerospace_dilution_trim_case"]["verdict"], "redteam_alignment_confirmed")
        self.assertEqual(rows["hd_hyundai_huntington_us_navy_aux_case"]["verdict"], "green_block_correct")
        self.assertEqual(rows["siemens_orders_profit_miss_case"]["verdict"], "orders_only_false_positive_contained")
        self.assertEqual(rows["oklo_smr_no_revenue_watch_case"]["verdict"], "pre_revenue_smr_green_block_correct")

    def test_required_round133_cases_are_present_with_dates_and_alignment(self):
        rows = {row["case_id"]: row for row in round133_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND133_CASE_CANDIDATES))
        self.assertEqual(rows["us_transformer_shortage_import_slots_case"]["stage2_date"], "2026-05-11")
        self.assertEqual(rows["ls_electric_525kv_us_datacenter_transformer_case"]["target_id"], "GRID_EHV_TRANSFORMER_EXPORT")
        self.assertEqual(rows["ls_electric_525kv_us_datacenter_transformer_case"]["stage2_date"], "2025-11-01")
        self.assertEqual(rows["abb_medium_voltage_expansion_case"]["target_id"], "GRID_MEDIUM_VOLTAGE_EXPANSION")
        self.assertEqual(rows["siemens_energy_fcf_buyback_case"]["target_id"], "POWER_EQUIPMENT_BACKLOG_TO_FCF")
        self.assertEqual(rows["siemens_energy_fcf_buyback_case"]["stage4b_date"], "2026-05-12")
        self.assertEqual(rows["siemens_energy_record_backlog_case"]["target_id"], "POWER_EQUIPMENT_BACKLOG_TO_FCF")
        self.assertEqual(rows["siemens_orders_profit_miss_case"]["target_id"], "POWER_EQUIPMENT_BACKLOG_TO_FCF")
        self.assertEqual(rows["siemens_orders_profit_miss_case"]["case_type"], "failed_rerating")
        self.assertIn("orders_only_without_profit", rows["siemens_orders_profit_miss_case"]["red_flag_fields"])
        self.assertEqual(rows["ge_vernova_data_center_orders_case"]["stage4b_date"], "2026-04-22")
        self.assertEqual(rows["ge_vernova_power_backlog_turbine_case"]["target_id"], "GAS_TURBINE_POWER_BACKLOG")
        self.assertEqual(rows["ge_vernova_power_backlog_turbine_case"]["stage4b_date"], "2026-04-22")
        self.assertEqual(rows["us_power_demand_record_eia_case"]["target_id"], "AI_DATA_CENTER_POWER_EQUIPMENT")
        self.assertEqual(rows["data_center_grid_flexibility_case"]["target_id"], "DATA_CENTER_GRID_FLEXIBILITY_OVERLAY")
        self.assertEqual(rows["perth_data_center_withdrawal_case"]["target_id"], "DATA_CENTER_POWER_WATER_PERMITTING")
        self.assertEqual(rows["perth_data_center_withdrawal_case"]["stage4c_date"], "2026-05-15")
        self.assertEqual(rows["indianapolis_data_center_moratorium_case"]["target_id"], "DATA_CENTER_POWER_WATER_PERMITTING")
        self.assertEqual(rows["indianapolis_data_center_moratorium_case"]["stage4c_date"], "2026-05-15")
        self.assertEqual(rows["seattle_data_center_moratorium_case"]["stage4c_date"], "2026-05-15")
        self.assertEqual(rows["water_capacity_data_center_case"]["target_id"], "DATA_CENTER_POWER_WATER_PERMITTING")
        self.assertEqual(rows["hanwha_aerospace_romania_k9_case"]["stage2_date"], "2024-07-09")
        self.assertEqual(rows["hanwha_aerospace_romania_k9_case"]["case_type"], "structural_success")
        self.assertEqual(rows["hanwha_aerospace_europe_sales_visibility_case"]["target_id"], "DEFENSE_LOCAL_PRODUCTION_PLATFORM")
        self.assertEqual(rows["hanwha_aerospace_europe_sales_visibility_case"]["stage2_date"], "2024-10-07")
        self.assertEqual(rows["hanwha_aerospace_dilution_trim_case"]["target_id"], "DEFENSE_CAPITAL_ALLOCATION_SHOCK")
        self.assertEqual(rows["hanwha_aerospace_dilution_trim_case"]["stage4b_date"], "2025-04-07")
        self.assertEqual(rows["hd_hyundai_huntington_us_navy_aux_case"]["target_id"], "DEFENSE_US_SHIPBUILDING_PLATFORM")
        self.assertEqual(rows["hanwha_ocean_us_shipbuilding_sanction_case"]["target_id"], "SHIPBUILDING_NAVAL_MRO")
        self.assertEqual(
            rows["hanwha_ocean_us_shipbuilding_sanction_case"]["price_validation_status"],
            "needs_source_date_backfill",
        )
        self.assertEqual(rows["shipbuilding_procurement_leadtime_case"]["target_id"], "SHIPBUILDING_PROCUREMENT_LEADTIME")
        self.assertEqual(rows["shipbuilding_procurement_leadtime_case"]["stage4c_date"], "2026-01-01")
        self.assertEqual(rows["hyundai_rotem_morocco_rail_case"]["stage2_date"], "2025-02-26")
        self.assertEqual(rows["meta_constellation_existing_nuclear_ppa_case"]["target_id"], "NUCLEAR_EXISTING_PPA_RESTART")
        self.assertEqual(rows["constellation_tmi_microsoft_restart_case"]["target_id"], "NUCLEAR_EXISTING_PPA_RESTART")
        self.assertEqual(rows["constellation_tmi_microsoft_restart_case"]["stage2_date"], "2026-05-11")
        self.assertEqual(rows["nuclear_grid_injection_rights_gate_case"]["target_id"], "NUCLEAR_GRID_INJECTION_RIGHTS")
        self.assertEqual(rows["nuscale_uamps_smr_cancel_case"]["stage4c_date"], "2023-11-01")
        self.assertEqual(rows["oklo_smr_no_revenue_watch_case"]["target_id"], "NUCLEAR_SMR_GRID_POLICY")
        self.assertEqual(rows["oklo_smr_no_revenue_watch_case"]["price_validation_status"], "needs_source_date_backfill")
        self.assertIn("pre_revenue_smr", rows["oklo_smr_no_revenue_watch_case"]["red_flag_fields"])
        self.assertEqual(rows["ukraine_reconstruction_policy_case"]["case_type"], "event_premium")
        self.assertEqual(rows["neom_city_policy_case"]["case_type"], "event_premium")

    def test_case_records_validate_and_keep_loop8_guardrails(self):
        records = round133_case_records()

        self.assertEqual(len(records), len(ROUND133_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "INDUSTRIAL_ORDERS_INFRA")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("require_contract_quality_delivery_margin_eps_revision_fcf_for_green", record.green_guardrails)
            self.assertIn("do_not_invent_contract_dates_prices_margins_or_counterparties", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["hanwha_aerospace_dilution_trim_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["nuscale_uamps_smr_cancel_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["siemens_orders_profit_miss_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["oklo_smr_no_revenue_watch_case"].rerating_result, "no_rerating")
        self.assertIn("project_withdrawal", by_id["perth_data_center_withdrawal_case"].red_flag_fields)
        self.assertIn("moratorium", by_id["indianapolis_data_center_moratorium_case"].red_flag_fields)
        self.assertIn("moa_only", by_id["hd_hyundai_huntington_us_navy_aux_case"].red_flag_fields)

    def test_score_profile_rows_mark_no_production_change_and_include_loop8_penalties(self):
        rows = round133_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND133_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["large_sector"], "INDUSTRIAL_ORDERS_INFRA")
            self.assertEqual(row["production_scoring_changed"], "false")
            self.assertIn("loop8_penalty_axes", row)
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["GRID_TRANSFORMER_SHORTAGE"]["eps_fcf"], "24")
        self.assertIn("low_margin_long_term_contract", by_target["GRID_TRANSFORMER_SHORTAGE"]["loop8_penalty_axes"])
        self.assertEqual(by_target["GRID_EHV_TRANSFORMER_EXPORT"]["information_confidence"], "6")
        self.assertIn("customer_project_delay", by_target["GRID_EHV_TRANSFORMER_EXPORT"]["loop8_penalty_axes"])
        self.assertIn("slot_cancelled", by_target["GRID_SUPPLY_SLOT_PREBUY"]["loop8_penalty_axes"])
        self.assertIn("capa_normalization", by_target["GRID_MEDIUM_VOLTAGE_EXPANSION"]["loop8_penalty_axes"])
        self.assertIn("wind_segment_loss", by_target["GAS_TURBINE_POWER_BACKLOG"]["loop8_penalty_axes"])
        self.assertIn("buyback_cut", by_target["POWER_EQUIPMENT_BACKLOG_TO_FCF"]["stage4c_conditions"])
        self.assertEqual(by_target["DATA_CENTER_GRID_FLEXIBILITY_OVERLAY"]["eps_fcf"], "gate")
        self.assertIn("moratorium", by_target["DATA_CENTER_POWER_WATER_PERMITTING"]["loop8_penalty_axes"])
        self.assertEqual(by_target["DEFENSE_CAPITAL_ALLOCATION_SHOCK"]["hard_gate"], "true")
        self.assertIn("moa_only", by_target["DEFENSE_US_SHIPBUILDING_PLATFORM"]["loop8_penalty_axes"])
        self.assertEqual(by_target["SHIPBUILDING_PROCUREMENT_LEADTIME"]["hard_gate"], "true")
        self.assertEqual(by_target["NUCLEAR_GRID_INJECTION_RIGHTS"]["hard_gate"], "true")
        self.assertEqual(by_target["CAPITAL_ALLOCATION_DILUTION_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(by_target["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        self.assertEqual(by_target["NUCLEAR_SMR_GRID_POLICY"]["posture"], "REDTEAM_FIRST")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round133_stage_date_rows()}
        fields = {row["field"] for row in round133_price_field_rows()}

        self.assertIn("fy1_fy2_fy3_revision", rows["GRID_TRANSFORMER_SHORTAGE"]["stage3"])
        self.assertIn("ehv_export_contract", rows["GRID_EHV_TRANSFORMER_EXPORT"]["stage2"])
        self.assertIn("slot_based_long_term_agreement", rows["GRID_SUPPLY_SLOT_PREBUY"]["stage2"])
        self.assertIn("medium_voltage_order", rows["GRID_MEDIUM_VOLTAGE_EXPANSION"]["stage2"])
        self.assertIn("gas_turbine_backlog", rows["GAS_TURBINE_POWER_BACKLOG"]["stage2"])
        self.assertIn("orders_to_fcf", rows["POWER_EQUIPMENT_BACKLOG_TO_FCF"]["stage2"])
        self.assertIn("model_only", rows["DATA_CENTER_GRID_FLEXIBILITY_OVERLAY"]["stage4c"])
        self.assertIn("moratorium", rows["DATA_CENTER_POWER_WATER_PERMITTING"]["stage4c"])
        self.assertIn("pipe_spool_delay", rows["SHIPBUILDING_PROCUREMENT_LEADTIME"]["stage4c"])
        self.assertIn("detail_missing", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage4c"])
        self.assertIn("signed_ppa", rows["NUCLEAR_EXISTING_PPA_RESTART"]["stage2"])
        self.assertIn("ferc_approval", rows["NUCLEAR_GRID_INJECTION_RIGHTS"]["stage2"])
        self.assertIn("project_cancelled", rows["NUCLEAR_SMR_GRID_POLICY"]["stage4c"])
        for field in (
            "contract_value_to_sales",
            "counterparty",
            "delivery_schedule",
            "transformer_lead_time_months",
            "transformer_voltage_kv",
            "ehv_transformer_flag",
            "ehv_transformer_voltage_kv",
            "korea_export_flag",
            "goes_cost_change",
            "copper_cost_change",
            "buyback_amount",
            "medium_voltage_order",
            "medium_voltage_order_flag",
            "switchgear_order",
            "switchgear_order_flag",
            "data_center_orders",
            "data_center_grid_flexibility_flag",
            "ai_power_consumption_twh",
            "grid_investment_savings_pct",
            "gas_turbine_backlog_gw",
            "gas_turbine_backlog",
            "gas_turbine_slot_reservation_gw",
            "power_equipment_backlog",
            "power_equipment_fcf_growth",
            "storage_equipment_order",
            "electrification_profit_growth",
            "wind_segment_loss",
            "tariff_cost_amount",
            "moratorium_flag",
            "water_permitting_delay_flag",
            "water_capacity_needed_mgd",
            "dry_cooling_required_flag",
            "diesel_generator_noise_flag",
            "defense_backlog",
            "local_content_requirement",
            "technology_transfer_flag",
            "dilution_flag",
            "local_factory_capex_flag",
            "us_shipbuilding_moa_flag",
            "naval_auxiliary_ship_option_flag",
            "yard_capex_uncertain_flag",
            "us_workforce_bottleneck_flag",
            "geopolitical_sanction_flag",
            "naval_mro_contract_flag",
            "shipbuilding_procurement_delay_flag",
            "pipe_spool_delay_flag",
            "procurement_lead_time_days",
            "supplier_delay_flag",
            "margin_penalty_flag",
            "orders_only_without_profit_flag",
            "sales_miss_flag",
            "industrial_profit_miss_flag",
            "rail_financing_secured_flag",
            "nuclear_ppa_flag",
            "existing_nuclear_ppa_flag",
            "nuclear_restart_flag",
            "grid_injection_rights_flag",
            "ferc_pjm_gate_flag",
            "smr_cost_overrun_flag",
            "reconstruction_contract_flag",
            "opendart_detail_fetched_flag",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "pre_revenue_smr_flag",
            "loss_widening_flag",
            "commercial_operation_target_year",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND133_PRICE_FIELDS))

    def test_summary_and_markdown_explain_loop8_guardrails(self):
        summary = round133_summary()
        summary_md = render_round133_summary_markdown()
        guardrails = render_round133_green_guardrail_markdown()
        overlays = render_round133_loop8_risk_overlay_markdown()
        price_plan = render_round133_price_validation_plan_markdown()
        alignment = render_round133_score_stage_price_alignment_markdown()

        self.assertEqual(summary["target_count"], 24)
        self.assertEqual(summary["case_candidate_count"], 28)
        self.assertEqual(summary["base_score_component_count"], 7)
        self.assertEqual(summary["stage_cap_count"], 5)
        self.assertEqual(summary["score_stage_price_alignment_count"], 9)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 11)
        self.assertEqual(summary["cyclical_success_count"], 0)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 3)
        self.assertEqual(summary["stage4b_case_count"], 4)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["hard_gate_target_count"], 5)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R1 Loop 8", summary_md)
        self.assertIn("Do not apply R1 Loop-8 v8.0 weights", guardrails)
        self.assertIn("NAVAL_MRO_OPTION_ONLY", overlays)
        self.assertIn("GRID_SLOT_VISIBILITY", overlays)
        self.assertIn("EHV_EXPORT_CONTRACT_ALIGNED", overlays)
        self.assertIn("DATA_CENTER_PERMITTING_4C", overlays)
        self.assertIn("DISCLOSURE_CONFIDENCE_CAPPED", price_plan)
        self.assertIn("SMR_POLICY_FALSE_GREEN", price_plan)
        self.assertIn("EPS/FCF 25, visibility 22, bottleneck/pricing 18", summary_md)
        self.assertIn("Stage 2 contracts are not Stage 3", summary_md)
        self.assertIn("Stage Caps", alignment)
        self.assertIn("GE Vernova", alignment)
        self.assertIn("Hanwha Aerospace", alignment)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round133_r1_loop8_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r1_loop8_round133.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round133_r1_loop8_v8.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["loop8_risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertTrue(paths["base_score_weights"].exists())
            self.assertTrue(paths["stage_caps"].exists())
            self.assertTrue(paths["score_stage_price_alignment"].exists())
            self.assertTrue(paths["score_stage_price_alignment_md"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND133_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round133_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round133_r1_loop8_industrial_infra", text)


if __name__ == "__main__":
    unittest.main()
