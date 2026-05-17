import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round107_r2_loop6_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round107_r2_loop6_ai_semiconductor import (
    ROUND107_CASE_CANDIDATES,
    ROUND107_PRICE_FIELDS,
    ROUND107_SCORE_TARGETS,
    render_round107_green_guardrail_markdown,
    render_round107_loop6_risk_overlay_markdown,
    render_round107_price_validation_plan_markdown,
    render_round107_summary_markdown,
    round107_case_candidate_rows,
    round107_case_records,
    round107_price_field_rows,
    round107_score_profile_rows,
    round107_stage_date_rows,
    round107_summary,
    round107_target_for,
    write_round107_r2_loop6_reports,
)


class Round107R2Loop6AISemiconductorTests(unittest.TestCase):
    def test_round107_targets_cover_loop6_ai_semiconductor_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND107_SCORE_TARGETS}

        self.assertEqual(len(labels), 26)
        for label in (
            "MEMORY_HBM_CAPACITY",
            "MEMORY_HBM_LTA_PREPAYMENT",
            "HBM_CATCHUP_EXECUTION",
            "MEMORY_SUPPLY_REALLOCATION",
            "AI_STORAGE_NAND_SHORTAGE",
            "COMMODITY_MEMORY_GENERAL_SEMI",
            "SEMI_EQUIPMENT_AI_CAPEX",
            "SEMI_MATERIALS_PROCESS",
            "CUSTOM_AI_ASIC_HYPERSCALER",
            "CUSTOM_AI_ASIC_MARGIN_CONCENTRATION",
            "ADVANCED_PACKAGING_COWOS_EMIB",
            "ADVANCED_PACKAGING_PCB",
            "OPTICAL_NETWORKING_AI_DATACENTER",
            "AI_NETWORKING_SWITCHING_INFRA",
            "PHOTONICS_AI_DATACENTER_CHIPS",
            "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
            "NEOCLOUD_GPU_RENTAL",
            "AI_DATA_CENTER_COOLING",
            "AI_CHIP_FABRIC_INFRA",
            "AI_ACCELERATOR_CHIP_PUREPLAY",
            "DISPLAY_OLED_SUPPLYCHAIN",
            "ELECTRONIC_COMPONENTS_MLCC_SENSOR",
            "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
            "AI_CAPEX_CROWDING_OVERLAY",
            "CIRCULAR_AI_FINANCING_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND107_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop6_canonical_archetypes_exist(self):
        self.assertIsInstance(E2RArchetype.MEMORY_HBM_LTA_PREPAYMENT.value, str)
        self.assertIsInstance(E2RArchetype.HBM_CATCHUP_EXECUTION.value, str)
        self.assertIsInstance(E2RArchetype.MEMORY_SUPPLY_REALLOCATION.value, str)
        self.assertIsInstance(E2RArchetype.AI_STORAGE_NAND_SHORTAGE.value, str)
        self.assertIsInstance(E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX.value, str)
        self.assertIsInstance(E2RArchetype.CUSTOM_AI_ASIC_HYPERSCALER.value, str)
        self.assertIsInstance(E2RArchetype.CUSTOM_AI_ASIC_MARGIN_CONCENTRATION.value, str)
        self.assertIsInstance(E2RArchetype.AI_NETWORKING_SWITCHING_INFRA.value, str)
        self.assertIsInstance(E2RArchetype.PHOTONICS_AI_DATACENTER_CHIPS.value, str)
        self.assertIsInstance(E2RArchetype.AI_CAPEX_CROWDING_OVERLAY.value, str)
        self.assertIsInstance(E2RArchetype.CIRCULAR_AI_FINANCING_OVERLAY.value, str)
        self.assertIsInstance(E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value, str)

    def test_loop6_weights_distinguish_hbm_optical_server_and_neocloud(self):
        hbm = round107_target_for("MEMORY_HBM_CAPACITY")
        hbm_lta = round107_target_for("MEMORY_HBM_LTA_PREPAYMENT")
        hbm_catchup = round107_target_for("HBM_CATCHUP_EXECUTION")
        supply_reallocation = round107_target_for("MEMORY_SUPPLY_REALLOCATION")
        ai_storage = round107_target_for("AI_STORAGE_NAND_SHORTAGE")
        equipment = round107_target_for("SEMI_EQUIPMENT_AI_CAPEX")
        custom_asic = round107_target_for("CUSTOM_AI_ASIC_HYPERSCALER")
        custom_margin = round107_target_for("CUSTOM_AI_ASIC_MARGIN_CONCENTRATION")
        optical = round107_target_for("OPTICAL_NETWORKING_AI_DATACENTER")
        networking = round107_target_for("AI_NETWORKING_SWITCHING_INFRA")
        photonics = round107_target_for("PHOTONICS_AI_DATACENTER_CHIPS")
        server = round107_target_for("AI_SERVER_ODM_EMS_SUPPLY_CHAIN")
        neocloud = round107_target_for("NEOCLOUD_GPU_RENTAL")
        capex_overlay = round107_target_for("AI_CAPEX_CROWDING_OVERLAY")
        circular = round107_target_for("CIRCULAR_AI_FINANCING_OVERLAY")
        disclosure_cap = round107_target_for("DISCLOSURE_CONFIDENCE_CAP")

        self.assertIsNotNone(hbm)
        self.assertIsNotNone(hbm_lta)
        self.assertIsNotNone(hbm_catchup)
        self.assertIsNotNone(supply_reallocation)
        self.assertIsNotNone(ai_storage)
        self.assertIsNotNone(equipment)
        self.assertIsNotNone(custom_asic)
        self.assertIsNotNone(custom_margin)
        self.assertIsNotNone(optical)
        self.assertIsNotNone(networking)
        self.assertIsNotNone(photonics)
        self.assertIsNotNone(server)
        self.assertIsNotNone(neocloud)
        self.assertIsNotNone(capex_overlay)
        self.assertIsNotNone(circular)
        self.assertIsNotNone(disclosure_cap)
        assert hbm is not None
        assert hbm_lta is not None
        assert hbm_catchup is not None
        assert supply_reallocation is not None
        assert ai_storage is not None
        assert equipment is not None
        assert custom_asic is not None
        assert custom_margin is not None
        assert optical is not None
        assert networking is not None
        assert photonics is not None
        assert server is not None
        assert neocloud is not None
        assert capex_overlay is not None
        assert circular is not None
        assert disclosure_cap is not None
        self.assertEqual(hbm.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(hbm.score_weight.eps_fcf, 24)
        self.assertEqual(hbm.score_weight.valuation, 7)
        self.assertIn("customer_price_resistance", hbm.loop6_penalty_axes)
        self.assertEqual(hbm_lta.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(hbm_lta.score_weight.structural_visibility, 24)
        self.assertIn("prepayment_absent", hbm_lta.red_flags)
        self.assertEqual(hbm_catchup.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(hbm_catchup.score_weight.valuation, 10)
        self.assertIn("labor_strike", hbm_catchup.red_flags)
        self.assertEqual(supply_reallocation.score_weight.structural_visibility, 19)
        self.assertIn("consumer_demand_destruction", supply_reallocation.red_flags)
        self.assertEqual(ai_storage.score_weight.eps_fcf, 23)
        self.assertEqual(ai_storage.score_weight.valuation, 6)
        self.assertIn("consumer_demand_destruction", ai_storage.red_flags)
        self.assertEqual(equipment.score_weight.valuation, 11)
        self.assertIn("order_pushout", equipment.red_flags)
        self.assertEqual(custom_asic.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(custom_asic.score_weight.information_confidence, 6)
        self.assertIn("custom_chip_margin_pressure", custom_asic.red_flags)
        self.assertEqual(custom_margin.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(custom_margin.hard_gate)
        self.assertIn("customer_project_delay", custom_margin.red_flags)
        self.assertEqual(optical.score_weight.bottleneck_pricing, 21)
        self.assertEqual(optical.score_weight.valuation, 10)
        self.assertIn("lead_time_normalization", optical.red_flags)
        self.assertEqual(networking.score_weight.structural_visibility, 21)
        self.assertIn("restructuring_cost", networking.red_flags)
        self.assertEqual(photonics.score_weight.eps_fcf, 20)
        self.assertIn("delivery_delay", photonics.red_flags)
        self.assertEqual(server.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("consignment_model", server.red_flags)
        self.assertEqual(neocloud.score_weight.valuation, 6)
        self.assertIn("fcf_negative", neocloud.red_flags)
        self.assertEqual(capex_overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(capex_overlay.hard_gate)
        self.assertIn("revision_slowdown", capex_overlay.red_flags)
        self.assertEqual(circular.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(circular.hard_gate)
        self.assertIn("circular_financing", circular.red_flags)
        self.assertEqual(disclosure_cap.score_weight.eps_fcf, "cap")
        self.assertIn("detail_missing", disclosure_cap.red_flags)

    def test_accounting_trust_overlay_is_hard_gate(self):
        overlay = round107_target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")

        self.assertIsNotNone(overlay)
        assert overlay is not None
        self.assertEqual(overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(overlay.hard_gate)
        self.assertEqual(overlay.score_weight.eps_fcf, "gate")
        self.assertIn("auditor_resignation", overlay.red_flags)
        self.assertIn("internal_control_weakness", overlay.red_flags)

    def test_required_round107_cases_are_present_with_loop6_stage_markers(self):
        rows = {row["case_id"]: row for row in round107_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND107_CASE_CANDIDATES))
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage3_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_record_profit_buyback_case"]["target_id"], "MEMORY_HBM_LTA_PREPAYMENT")
        self.assertEqual(rows["sk_hynix_record_profit_buyback_case"]["stage2_date"], "2026-01-28")
        self.assertEqual(rows["sk_hynix_record_profit_buyback_case"]["stage4b_date"], "2026-01-28")
        self.assertEqual(rows["samsung_hbm4_shipping_case"]["target_id"], "HBM_CATCHUP_EXECUTION")
        self.assertEqual(rows["samsung_hbm4_shipping_case"]["stage2_date"], "2026-02-12")
        self.assertEqual(rows["samsung_amd_hbm4_mou_case"]["target_id"], "HBM_CATCHUP_EXECUTION")
        self.assertEqual(rows["samsung_amd_hbm4_mou_case"]["stage2_date"], "2026-03-18")
        self.assertEqual(rows["samsung_labor_strike_execution_case"]["target_id"], "HBM_CATCHUP_EXECUTION")
        self.assertEqual(rows["samsung_labor_strike_execution_case"]["stage2_date"], "2026-05-15")
        self.assertEqual(rows["micron_consumer_memory_exit_case"]["target_id"], "MEMORY_SUPPLY_REALLOCATION")
        self.assertEqual(rows["micron_consumer_memory_exit_case"]["stage2_date"], "2025-12-03")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["target_id"], "AI_STORAGE_NAND_SHORTAGE")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["case_type"], "4b_watch")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["stage4b_date"], "2026-05-15")
        self.assertEqual(rows["applied_materials_ai_packaging_growth_case"]["target_id"], "SEMI_EQUIPMENT_AI_CAPEX")
        self.assertEqual(rows["applied_materials_ai_packaging_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["broadcom_custom_ai_asic_100b_case"]["target_id"], "CUSTOM_AI_ASIC_HYPERSCALER")
        self.assertEqual(rows["broadcom_custom_ai_asic_100b_case"]["stage2_date"], "2026-03-04")
        self.assertEqual(rows["broadcom_custom_ai_margin_concentration_case"]["target_id"], "CUSTOM_AI_ASIC_MARGIN_CONCENTRATION")
        self.assertEqual(rows["broadcom_custom_ai_margin_concentration_case"]["case_type"], "failed_rerating")
        self.assertEqual(rows["nvidia_cowos_l_transition_case"]["stage2_date"], "2025-01-16")
        self.assertEqual(rows["broadcom_optical_pcb_leadtime_case"]["stage2_date"], "2026-03-24")
        self.assertEqual(rows["cisco_ai_networking_orders_case"]["target_id"], "AI_NETWORKING_SWITCHING_INFRA")
        self.assertEqual(rows["cisco_ai_networking_orders_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["tower_photonics_ai_datacenter_deal_case"]["target_id"], "PHOTONICS_AI_DATACENTER_CHIPS")
        self.assertEqual(rows["tower_photonics_ai_datacenter_deal_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["foxconn_ai_server_rack_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["ecolab_coolit_liquid_cooling_case"]["stage2_date"], "2026-03-20")
        self.assertEqual(rows["coreweave_openai_contract_case"]["stage2_date"], "2025-03-10")
        self.assertEqual(rows["coreweave_expanded_openai_contract_case"]["stage2_date"], "2025-09-25")
        self.assertEqual(rows["coreweave_nvidia_circular_financing_case"]["target_id"], "CIRCULAR_AI_FINANCING_OVERLAY")
        self.assertEqual(rows["coreweave_nvidia_circular_financing_case"]["stage4b_date"], "2026-05-13")
        self.assertEqual(rows["cerebras_ai_accelerator_ipo_case"]["case_type"], "event_premium")
        self.assertEqual(rows["cerebras_ai_accelerator_ipo_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["supermicro_ey_resignation_case"]["stage4c_date"], "2024-10-30")
        self.assertEqual(rows["cxl_glass_substrate_theme_case"]["case_type"], "overheat")
        self.assertEqual(rows["ai_capex_crowding_overlay_case"]["target_id"], "AI_CAPEX_CROWDING_OVERLAY")

    def test_case_records_validate_and_keep_loop6_guardrails(self):
        records = round107_case_records()

        self.assertEqual(len(records), len(ROUND107_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "AI_SEMICONDUCTOR_ELECTRONICS")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("ai_beneficiary_is_not_one_archetype", record.green_guardrails)
            self.assertIn("do_not_invent_contract_prices_margins_customers_stage_prices_or_yield", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["sk_hynix_hbm_trillion_case"].rerating_result, "true_rerating")
        self.assertEqual(by_id["sk_hynix_record_profit_buyback_case"].rerating_result, "theme_overheat")
        self.assertIn("prepayment", "|".join(by_id["sk_hynix_record_profit_buyback_case"].must_have_fields))
        self.assertEqual(by_id["micron_consumer_memory_exit_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["broadcom_custom_ai_asic_100b_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["broadcom_custom_ai_margin_concentration_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["coreweave_openai_contract_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["coreweave_nvidia_circular_financing_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["cerebras_ai_accelerator_ipo_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["supermicro_ey_resignation_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["cxl_glass_substrate_theme_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertIn("labor_strike", by_id["samsung_labor_strike_execution_case"].red_flag_fields)

    def test_score_profile_rows_match_round107_weight_table(self):
        rows = {row["target_id"]: row for row in round107_score_profile_rows()}

        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["eps_fcf"], "24")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["structural_visibility"], "22")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["valuation"], "7")
        self.assertEqual(rows["MEMORY_HBM_LTA_PREPAYMENT"]["structural_visibility"], "24")
        self.assertEqual(rows["MEMORY_HBM_LTA_PREPAYMENT"]["information_confidence"], "6")
        self.assertEqual(rows["HBM_CATCHUP_EXECUTION"]["eps_fcf"], "22")
        self.assertEqual(rows["MEMORY_SUPPLY_REALLOCATION"]["structural_visibility"], "19")
        self.assertEqual(rows["AI_STORAGE_NAND_SHORTAGE"]["eps_fcf"], "23")
        self.assertEqual(rows["AI_STORAGE_NAND_SHORTAGE"]["valuation"], "6")
        self.assertEqual(rows["COMMODITY_MEMORY_GENERAL_SEMI"]["eps_fcf"], "22")
        self.assertEqual(rows["SEMI_EQUIPMENT_AI_CAPEX"]["valuation"], "11")
        self.assertEqual(rows["CUSTOM_AI_ASIC_HYPERSCALER"]["information_confidence"], "6")
        self.assertEqual(rows["CUSTOM_AI_ASIC_MARGIN_CONCENTRATION"]["hard_gate"], "true")
        self.assertEqual(rows["OPTICAL_NETWORKING_AI_DATACENTER"]["bottleneck_pricing"], "21")
        self.assertEqual(rows["AI_NETWORKING_SWITCHING_INFRA"]["structural_visibility"], "21")
        self.assertEqual(rows["PHOTONICS_AI_DATACENTER_CHIPS"]["valuation"], "9")
        self.assertEqual(rows["AI_SERVER_ODM_EMS_SUPPLY_CHAIN"]["valuation"], "8")
        self.assertEqual(rows["NEOCLOUD_GPU_RENTAL"]["valuation"], "6")
        self.assertEqual(rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(rows["AI_CAPEX_CROWDING_OVERLAY"]["hard_gate"], "false")
        self.assertEqual(rows["AI_CAPEX_CROWDING_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["CIRCULAR_AI_FINANCING_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["CIRCULAR_AI_FINANCING_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round107_stage_date_rows()}
        fields = {row["field"] for row in round107_price_field_rows()}

        self.assertIn("hbm_capacity_constraint", rows["MEMORY_HBM_CAPACITY"]["stage3"])
        self.assertIn("prepayment_flag", rows["MEMORY_HBM_LTA_PREPAYMENT"]["stage2"])
        self.assertIn("customer_qualification", rows["HBM_CATCHUP_EXECUTION"]["stage2"])
        self.assertIn("consumer_memory_exit_flag", rows["MEMORY_SUPPLY_REALLOCATION"]["stage2"])
        self.assertIn("enterprise_ssd_revenue", rows["AI_STORAGE_NAND_SHORTAGE"]["stage2"])
        self.assertIn("order_pushout", rows["SEMI_EQUIPMENT_AI_CAPEX"]["stage4c"])
        self.assertIn("custom_ai_asic_revenue", rows["CUSTOM_AI_ASIC_HYPERSCALER"]["stage2"])
        self.assertIn("customer_project_delay", rows["CUSTOM_AI_ASIC_MARGIN_CONCENTRATION"]["stage4c"])
        self.assertIn("lead_time_normalization", rows["OPTICAL_NETWORKING_AI_DATACENTER"]["stage4b"])
        self.assertIn("ai_networking_orders", rows["AI_NETWORKING_SWITCHING_INFRA"]["stage2"])
        self.assertIn("photonics_chip_contract_value", rows["PHOTONICS_AI_DATACENTER_CHIPS"]["stage2"])
        self.assertIn("refinancing_pressure", rows["NEOCLOUD_GPU_RENTAL"]["stage4c"])
        self.assertIn("auditor_resignation", rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("customer_capex_cut", rows["AI_CAPEX_CROWDING_OVERLAY"]["stage4c"])
        self.assertIn("capacity_guarantee_break", rows["CIRCULAR_AI_FINANCING_OVERLAY"]["stage4c"])
        self.assertIn("detail_fetch_required", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage2"])
        for field in (
            "hbm4_shipping_flag",
            "hbm_lta_flag",
            "hbm_prepayment_amount",
            "capacity_reservation_flag",
            "hbm_market_share",
            "buyback_cancel_amount",
            "capital_return_flag",
            "hbm4_yield_signal",
            "qualification_status",
            "customer_specific_base_die_flag",
            "nand_profit_growth",
            "enterprise_ssd_revenue",
            "consumer_demand_destruction_flag",
            "consumer_memory_exit_flag",
            "strategic_customer_allocation_flag",
            "capacity_reallocation_flag",
            "customer_forecast_duration_quarters",
            "custom_ai_asic_revenue",
            "custom_ai_asic_customer_count",
            "hyperscaler_customer_name",
            "ai_chip_revenue",
            "custom_chip_margin",
            "startup_customer_risk_flag",
            "tsmc_capacity_secured_flag",
            "emib_revenue_flag",
            "pcb_lead_time_weeks",
            "optical_networking_inventory_flag",
            "photonics_chip_contract_value",
            "photonics_delivery_year",
            "ai_networking_orders",
            "hyperscaler_order_value",
            "ai_infrastructure_order_guidance",
            "networking_restructuring_cost",
            "silicon_photonics_revenue",
            "working_capital_pressure",
            "gpu_depreciation",
            "ipo_downsize_flag",
            "circular_financing_flag",
            "nvidia_capacity_guarantee_flag",
            "openai_equity_stake_flag",
            "delivery_issue_flag",
            "mna_multiple",
            "ai_accelerator_revenue",
            "software_ecosystem_score",
            "government_customer_flag",
            "uae_revenue_concentration",
            "nvidia_competition_flag",
            "ipo_first_day_return",
            "ipo_valuation",
            "cash_burn_flag",
            "auditor_resignation_flag",
            "labor_strike_flag",
            "talent_retention_risk_flag",
            "theme_only_flag",
            "customer_validation_flag",
            "direct_equity_exposure_flag",
            "opendart_rcept_no",
            "opendart_detail_fetched_flag",
            "disclosure_confidence_score",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND107_PRICE_FIELDS))

    def test_summary_and_markdown_explain_loop6_ai_distinctions(self):
        summary = round107_summary()
        summary_md = render_round107_summary_markdown()
        guardrails = render_round107_green_guardrail_markdown()
        overlays = render_round107_loop6_risk_overlay_markdown()
        price_plan = render_round107_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 26)
        self.assertEqual(summary["case_candidate_count"], 24)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 13)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["overheat_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 5)
        self.assertEqual(summary["stage4c_case_count"], 1)
        self.assertEqual(summary["green_possible_count"], 6)
        self.assertEqual(summary["watch_yellow_first_count"], 15)
        self.assertEqual(summary["redteam_first_count"], 5)
        self.assertEqual(summary["hard_gate_target_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R2 Loop 6", summary_md)
        self.assertIn("Do not apply R2 Loop-6 v6.0 weights", guardrails)
        self.assertIn("HBM LTA/prepayment", summary_md)
        self.assertIn("OpenAI contract", overlays)
        self.assertIn("CUSTOM_AI_ASIC_ALIGNED", overlays)
        self.assertIn("CIRCULAR_AI_FINANCING_WATCH", overlays)
        self.assertIn("PHOTONICS_CONTRACT_STAGE2", price_plan)
        self.assertIn("supermicro_ey_resignation_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round107_r2_loop6_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r2_loop6_round107.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round107_r2_loop6_v6.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["loop6_risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND107_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round107_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round107_r2_loop6_ai_semiconductor", text)


if __name__ == "__main__":
    unittest.main()
