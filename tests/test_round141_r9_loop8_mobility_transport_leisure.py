import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round141_r9_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round141_r9_loop8_mobility_transport_leisure import (
    ROUND141_CASE_CANDIDATES,
    ROUND141_PRICE_FIELDS,
    ROUND141_SCORE_TARGETS,
    render_round141_green_guardrail_markdown,
    render_round141_price_validation_plan_markdown,
    render_round141_risk_overlay_markdown,
    render_round141_summary_markdown,
    round141_base_score_axis_rows,
    round141_case_candidate_rows,
    round141_case_records,
    round141_price_field_rows,
    round141_score_profile_rows,
    round141_stage_date_rows,
    round141_summary,
    target_for,
    write_round141_r9_loop8_reports,
)


class Round141R9Loop8MobilityTransportLeisureTests(unittest.TestCase):
    def test_round141_targets_cover_r9_loop8_archetypes(self):
        labels = {target.target_id for target in ROUND141_SCORE_TARGETS}

        self.assertEqual(len(labels), 33)
        for label in (
            "AUTO_MOBILITY_COMPLETED_VEHICLE",
            "AUTO_HYBRID_VALUEUP",
            "AUTO_TARIFF_LOCALIZATION",
            "AUTO_US_LOCALIZATION_LABOR_VISA_RISK",
            "AUTO_MOBILITY_COMPONENTS",
            "HYBRID_COMPONENT_BOTTLENECK",
            "AUTO_COMPONENTS_EV_ADAS",
            "AUTONOMOUS_ROBOTAXI_DEPLOYMENT",
            "ROBOTAXI_OPERATIONAL_REALITY_CHECK",
            "ROBOTAXI_SAFETY_REGULATORY_OVERLAY",
            "AV_CRASH_DISCLOSURE_PROBE_OVERLAY",
            "AUTONOMOUS_TRUCKING_COMMERCIAL_LAUNCH",
            "AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE",
            "AUTONOMOUS_TRUCKING_UNIT_ECONOMICS",
            "TIRE_AUTO_COMPONENT_SPREAD",
            "AIRLINE_TRAVEL_CYCLE",
            "AIRLINE_INTEGRATION_SCALE",
            "TRAVEL_LEISURE_REOPENING",
            "CASINO_DUTYFREE_TOURISM",
            "TOURISM_POLICY_EVENT",
            "SHIPPING_FREIGHT_CYCLE",
            "LOGISTICS_PARCEL_FREIGHT",
            "RENTAL_USED_CAR_MOBILITY",
            "EV_RENTAL_UNIT_ECONOMICS",
            "MOBILITY_RENTAL_MICROMOBILITY",
            "URBAN_AIR_DRONE",
            "EVTOL_CERTIFICATION_CASH_BURN",
            "PART135_NOT_TYPE_CERTIFICATION",
            "SPACE_SUPPLYCHAIN",
            "SATELLITE_CONNECTIVITY_INFRA",
            "TRANSPORT_SAFETY_REGULATORY_OVERLAY",
            "FLEET_UNIT_ECONOMICS_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND141_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.MOBILITY_TRANSPORT_LEISURE)
            self.assertFalse(target.production_scoring_changed)

    def test_auto_hybrid_and_satellite_are_green_possible_but_guardrailed(self):
        hybrid = target_for("AUTO_HYBRID_VALUEUP")
        tariff = target_for("AUTO_TARIFF_LOCALIZATION")
        localization_labor = target_for("AUTO_US_LOCALIZATION_LABOR_VISA_RISK")
        satellite = target_for("SATELLITE_CONNECTIVITY_INFRA")

        assert hybrid is not None
        assert tariff is not None
        assert localization_labor is not None
        assert satellite is not None
        self.assertEqual(hybrid.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(hybrid.score_weight.capital_allocation, 10)
        self.assertIn("shareholder_return_ratio", hybrid.green_conditions)
        self.assertIn("tariff", hybrid.red_flags)
        self.assertEqual(tariff.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("op_margin_cut", tariff.red_flags)
        self.assertIn("tariff_cost_absorbed", tariff.green_conditions)
        self.assertEqual(localization_labor.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(localization_labor.gate_only)
        self.assertIn("visa_delay", localization_labor.stage4c_conditions)
        self.assertIn("plant_ramp", localization_labor.red_flags)
        self.assertEqual(satellite.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("satellite_backlog", satellite.green_conditions)
        self.assertIn("capex_debt", satellite.red_flags)

    def test_robotaxi_shipping_evtol_and_overlays_are_redteam_or_watch_first(self):
        robotaxi = target_for("AUTONOMOUS_ROBOTAXI_DEPLOYMENT")
        robotaxi_ops = target_for("ROBOTAXI_OPERATIONAL_REALITY_CHECK")
        robotaxi_safety = target_for("ROBOTAXI_SAFETY_REGULATORY_OVERLAY")
        av_probe = target_for("AV_CRASH_DISCLOSURE_PROBE_OVERLAY")
        shipping = target_for("SHIPPING_FREIGHT_CYCLE")
        evtol = target_for("URBAN_AIR_DRONE")
        evtol_gate = target_for("EVTOL_CERTIFICATION_CASH_BURN")
        part135_gate = target_for("PART135_NOT_TYPE_CERTIFICATION")
        ev_rental = target_for("EV_RENTAL_UNIT_ECONOMICS")
        trucking = target_for("AUTONOMOUS_TRUCKING_COMMERCIAL_LAUNCH")
        paid_freight = target_for("AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE")
        trucking_gate = target_for("AUTONOMOUS_TRUCKING_UNIT_ECONOMICS")
        tourism_policy = target_for("TOURISM_POLICY_EVENT")
        safety = target_for("TRANSPORT_SAFETY_REGULATORY_OVERLAY")
        fleet = target_for("FLEET_UNIT_ECONOMICS_OVERLAY")
        disclosure = target_for("DISCLOSURE_CONFIDENCE_CAP")

        assert robotaxi is not None
        assert robotaxi_ops is not None
        assert robotaxi_safety is not None
        assert av_probe is not None
        assert shipping is not None
        assert evtol is not None
        assert evtol_gate is not None
        assert part135_gate is not None
        assert ev_rental is not None
        assert trucking is not None
        assert paid_freight is not None
        assert trucking_gate is not None
        assert tourism_policy is not None
        assert safety is not None
        assert fleet is not None
        assert disclosure is not None
        self.assertEqual(robotaxi.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(robotaxi_ops.gate_only)
        self.assertTrue(robotaxi_safety.gate_only)
        self.assertTrue(av_probe.gate_only)
        self.assertEqual(shipping.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertEqual(evtol.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(evtol_gate.gate_only)
        self.assertTrue(part135_gate.gate_only)
        self.assertTrue(ev_rental.gate_only)
        self.assertEqual(trucking.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(paid_freight.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(trucking_gate.gate_only)
        self.assertEqual(tourism_policy.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(safety.gate_only)
        self.assertTrue(fleet.gate_only)
        self.assertFalse(disclosure.gate_only)
        self.assertIn("long_wait_time", robotaxi_ops.stage4c_conditions)
        self.assertIn("weather_handling_failure", robotaxi_safety.stage4c_conditions)
        self.assertIn("nhtsa_probe_flag", av_probe.stage4c_conditions)
        self.assertIn("spot_rate_below_breakeven", shipping.stage4c_conditions)
        self.assertIn("type_certification_flag", evtol.green_conditions)
        self.assertIn("type_certification_missing", evtol_gate.stage4c_conditions)
        self.assertIn("type_certification_missing", part135_gate.stage4c_conditions)
        self.assertIn("residual_value_drop", ev_rental.stage4c_conditions)
        self.assertIn("driverless_miles", trucking.stage2_signals)
        self.assertIn("paid_freight_flag", paid_freight.stage2_signals)
        self.assertIn("remote_support_cost_unknown", trucking_gate.stage4c_conditions)
        self.assertIn("visa_policy_rally_without_spend", tourism_policy.stage4c_conditions)
        self.assertIn("nhtsa_scrutiny", safety.red_flags)
        self.assertIn("repair_cost", fleet.red_flags)
        self.assertIn("unit_economics_missing", disclosure.stage4c_conditions)

    def test_required_round141_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round141_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND141_CASE_CANDIDATES))
        self.assertEqual(rows["hyundai_hybrid_valueup_case"]["target_id"], "AUTO_HYBRID_VALUEUP")
        self.assertEqual(rows["hyundai_hybrid_valueup_case"]["stage2_date"], "2024-08-28")
        self.assertEqual(rows["hyundai_tariff_margin_cut_case"]["target_id"], "AUTO_TARIFF_LOCALIZATION")
        self.assertEqual(rows["hyundai_tariff_margin_cut_case"]["stage4b_date"], "2025-09-18")
        self.assertEqual(rows["toyota_hybrid_parts_bottleneck_case"]["target_id"], "HYBRID_COMPONENT_BOTTLENECK")
        self.assertEqual(rows["toyota_hybrid_parts_bottleneck_case"]["stage2_date"], "2025-03-31")
        self.assertEqual(rows["avride_hyundai_ioniq5_robotaxi_case"]["stage2_date"], "2025-03-05")
        self.assertEqual(rows["tesla_texas_robotaxi_wait_time_case"]["target_id"], "ROBOTAXI_OPERATIONAL_REALITY_CHECK")
        self.assertEqual(rows["tesla_texas_robotaxi_wait_time_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["waymo_flood_recall_robotaxi_case"]["target_id"], "ROBOTAXI_SAFETY_REGULATORY_OVERLAY")
        self.assertEqual(rows["waymo_flood_recall_robotaxi_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["avride_nhtsa_probe_case"]["target_id"], "AV_CRASH_DISCLOSURE_PROBE_OVERLAY")
        self.assertEqual(rows["avride_nhtsa_probe_case"]["stage4b_date"], "2026-05-12")
        self.assertEqual(rows["uber_avride_dallas_robotaxi_case"]["stage2_date"], "2025-12-03")
        self.assertNotIn("waymo_houston_expansion_case", rows)
        self.assertEqual(rows["aurora_driverless_trucking_texas_case"]["target_id"], "AUTONOMOUS_TRUCKING_COMMERCIAL_LAUNCH")
        self.assertEqual(rows["aurora_driverless_trucking_texas_case"]["stage2_date"], "2025-05-01")
        self.assertEqual(rows["bot_auto_paid_driverless_freight_case"]["target_id"], "AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE")
        self.assertEqual(rows["bot_auto_paid_driverless_freight_case"]["stage2_date"], "2026-04-30")
        self.assertEqual(rows["gm_aurora_sterling_anderson_product_case"]["target_id"], "AUTO_COMPONENTS_EV_ADAS")
        self.assertEqual(rows["gm_aurora_sterling_anderson_product_case"]["stage2_date"], "2025-05-12")
        self.assertEqual(rows["korean_air_asiana_integration_case"]["target_id"], "AIRLINE_INTEGRATION_SCALE")
        self.assertEqual(rows["korean_air_asiana_integration_case"]["stage2_date"], "2025-02-07")
        self.assertEqual(rows["china_group_visa_tourism_case"]["target_id"], "TOURISM_POLICY_EVENT")
        self.assertEqual(rows["china_group_visa_tourism_case"]["case_type"], "event_premium")
        self.assertEqual(rows["ses_airline_connectivity_case"]["stage2_date"], "2026-05-12")
        self.assertEqual(rows["container_rate_collapse_case"]["stage4c_date"], "2025-10-03")
        self.assertNotIn("maersk_suez_overcapacity_loss_case", rows)
        self.assertEqual(rows["hertz_ev_rental_failure_case"]["target_id"], "EV_RENTAL_UNIT_ECONOMICS")
        self.assertEqual(rows["hertz_ev_rental_failure_case"]["stage4c_date"], "2024-01-11")
        self.assertEqual(rows["michelin_tire_demand_cut_case"]["stage4c_date"], "2025-10-13")
        self.assertNotIn("lime_ipo_micromobility_case", rows)
        self.assertEqual(rows["joby_discounted_offering_case"]["target_id"], "EVTOL_CERTIFICATION_CASH_BURN")
        self.assertEqual(rows["joby_discounted_offering_case"]["stage4c_date"], "2025-10-08")
        self.assertEqual(rows["lilium_evtol_cash_crunch_case"]["target_id"], "EVTOL_CERTIFICATION_CASH_BURN")
        self.assertEqual(rows["lilium_evtol_cash_crunch_case"]["stage4c_date"], "2024-11-25")
        self.assertEqual(rows["archer_part135_no_type_cert_case"]["target_id"], "PART135_NOT_TYPE_CERTIFICATION")
        self.assertEqual(rows["archer_part135_no_type_cert_case"]["case_type"], "event_premium")
        self.assertNotIn("archer_nyc_network_case", rows)

    def test_case_records_validate_and_keep_round141_guardrails(self):
        records = round141_case_records()

        self.assertEqual(len(records), len(ROUND141_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("demand_recovery_or_policy_headline_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("hybrid_label_is_not_margin_or_fcf", record.green_guardrails)
            self.assertIn("robotaxi_deployment_is_not_unit_economics", record.green_guardrails)
            self.assertIn("autonomous_trucking_miles_are_not_unit_economics", record.green_guardrails)
            self.assertIn("freight_spike_is_not_structural_green", record.green_guardrails)
            self.assertIn("part135_is_not_type_certification_or_revenue", record.green_guardrails)
            self.assertIn("disclosure_confidence_cap_blocks_stage3_until_fleet_freight_contract_or_unit_economics_details_are_verified", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["hyundai_tariff_margin_cut_case"].secondary_archetypes, (E2RArchetype.AUTO_US_LOCALIZATION_LABOR_VISA_RISK,))
        self.assertEqual(by_id["avride_nhtsa_probe_case"].primary_archetype, E2RArchetype.AV_CRASH_DISCLOSURE_PROBE_OVERLAY)
        self.assertEqual(by_id["bot_auto_paid_driverless_freight_case"].primary_archetype, E2RArchetype.AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE)
        self.assertEqual(by_id["china_group_visa_tourism_case"].primary_archetype, E2RArchetype.TOURISM_POLICY_EVENT)
        self.assertEqual(by_id["archer_part135_no_type_cert_case"].primary_archetype, E2RArchetype.PART135_NOT_TYPE_CERTIFICATION)
        self.assertEqual(by_id["korean_air_asiana_integration_case"].rerating_result, "cyclical_rerating")
        self.assertEqual(by_id["china_group_visa_tourism_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(by_id["hertz_ev_rental_failure_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["archer_part135_no_type_cert_case"].rerating_result, "event_premium")

    def test_score_profile_rows_match_round141_weight_table(self):
        rows = {row["target_id"]: row for row in round141_score_profile_rows()}

        self.assertEqual(rows["AUTO_MOBILITY_COMPLETED_VEHICLE"]["capital_allocation"], "10")
        self.assertEqual(rows["AUTO_HYBRID_VALUEUP"]["eps_fcf"], "21")
        self.assertEqual(rows["AUTO_TARIFF_LOCALIZATION"]["capital_allocation"], "5")
        self.assertEqual(rows["AUTO_US_LOCALIZATION_LABOR_VISA_RISK"]["gate_only"], "true")
        self.assertEqual(rows["HYBRID_COMPONENT_BOTTLENECK"]["bottleneck_pricing"], "14")
        self.assertEqual(rows["AUTONOMOUS_ROBOTAXI_DEPLOYMENT"]["information_confidence"], "6")
        self.assertEqual(rows["ROBOTAXI_OPERATIONAL_REALITY_CHECK"]["gate_only"], "true")
        self.assertEqual(rows["ROBOTAXI_SAFETY_REGULATORY_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["AV_CRASH_DISCLOSURE_PROBE_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["AUTONOMOUS_TRUCKING_COMMERCIAL_LAUNCH"]["eps_fcf"], "16")
        self.assertEqual(rows["AUTONOMOUS_TRUCKING_COMMERCIAL_LAUNCH"]["information_confidence"], "6")
        self.assertEqual(rows["AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE"]["eps_fcf"], "17")
        self.assertEqual(rows["AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE"]["information_confidence"], "6")
        self.assertEqual(rows["AUTONOMOUS_TRUCKING_UNIT_ECONOMICS"]["gate_only"], "true")
        self.assertEqual(rows["AIRLINE_INTEGRATION_SCALE"]["structural_visibility"], "16")
        self.assertEqual(rows["TOURISM_POLICY_EVENT"]["eps_fcf"], "8")
        self.assertEqual(rows["SHIPPING_FREIGHT_CYCLE"]["structural_visibility"], "7")
        self.assertEqual(rows["EV_RENTAL_UNIT_ECONOMICS"]["gate_only"], "true")
        self.assertEqual(rows["URBAN_AIR_DRONE"]["eps_fcf"], "8")
        self.assertEqual(rows["EVTOL_CERTIFICATION_CASH_BURN"]["gate_only"], "true")
        self.assertEqual(rows["PART135_NOT_TYPE_CERTIFICATION"]["gate_only"], "true")
        self.assertEqual(rows["SATELLITE_CONNECTIVITY_INFRA"]["structural_visibility"], "21")
        self.assertEqual(rows["TRANSPORT_SAFETY_REGULATORY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["FLEET_UNIT_ECONOMICS_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["information_confidence"], "+")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["gate_only"], "false")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_base_score_axes_match_round141_v8_table(self):
        rows = {row["axis_id"]: row for row in round141_base_score_axis_rows()}

        self.assertEqual(len(rows), 7)
        self.assertEqual(rows["eps_fcf_opm_conversion"]["weight"], "22")
        self.assertIn("op_margin_target", rows["eps_fcf_opm_conversion"]["stage2_evidence"])
        self.assertIn("op_margin_cut", rows["eps_fcf_opm_conversion"]["hard_redteam"])
        self.assertEqual(rows["contract_backlog_operating_visibility"]["weight"], "20")
        self.assertIn("paid_freight_flag", rows["contract_backlog_operating_visibility"]["stage2_evidence"])
        self.assertIn("service_area_only", rows["contract_backlog_operating_visibility"]["hard_redteam"])
        self.assertEqual(rows["unit_fleet_economics"]["weight"], "18")
        self.assertIn("cost_per_mile", rows["unit_fleet_economics"]["stage2_evidence"])
        self.assertIn("repair_cost_spike", rows["unit_fleet_economics"]["hard_redteam"])
        self.assertEqual(rows["recurrence_demand_duration"]["weight"], "12")
        self.assertIn("policy_event_only", rows["recurrence_demand_duration"]["hard_redteam"])
        self.assertEqual(rows["safety_regulatory_certification_disclosure"]["weight"], "12")
        self.assertIn("part135_without_type_certification", rows["safety_regulatory_certification_disclosure"]["hard_redteam"])
        self.assertEqual(rows["market_mispricing_rerating_gap"]["weight"], "8")
        self.assertEqual(rows["valuation_room_4b_margin"]["weight"], "8")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round141_stage_date_rows()}
        fields = {row["field"] for row in round141_price_field_rows()}

        self.assertIn("op_margin_target", rows["AUTO_HYBRID_VALUEUP"]["stage2"])
        self.assertIn("plant_ramp_delay", rows["AUTO_US_LOCALIZATION_LABOR_VISA_RISK"]["stage4c"])
        self.assertIn("hybrid_component_order", rows["HYBRID_COMPONENT_BOTTLENECK"]["stage2"])
        self.assertIn("paid_ride_volume", rows["AUTONOMOUS_ROBOTAXI_DEPLOYMENT"]["stage2"])
        self.assertIn("long_wait_time", rows["ROBOTAXI_OPERATIONAL_REALITY_CHECK"]["stage4c"])
        self.assertIn("weather_handling_failure", rows["ROBOTAXI_SAFETY_REGULATORY_OVERLAY"]["stage4c"])
        self.assertIn("nhtsa_probe_flag", rows["AV_CRASH_DISCLOSURE_PROBE_OVERLAY"]["stage4c"])
        self.assertIn("driverless_miles", rows["AUTONOMOUS_TRUCKING_COMMERCIAL_LAUNCH"]["stage2"])
        self.assertIn("paid_freight_flag", rows["AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE"]["stage2"])
        self.assertIn("remote_support_cost_unknown", rows["AUTONOMOUS_TRUCKING_UNIT_ECONOMICS"]["stage4c"])
        self.assertIn("integration_synergy", rows["AIRLINE_INTEGRATION_SCALE"]["stage2"])
        self.assertIn("spot_rate_below_breakeven", rows["SHIPPING_FREIGHT_CYCLE"]["stage4c"])
        self.assertIn("residual_value_drop", rows["EV_RENTAL_UNIT_ECONOMICS"]["stage4c"])
        self.assertIn("tourist_spend", rows["CASINO_DUTYFREE_TOURISM"]["stage2"])
        self.assertIn("visa_policy_rally_without_spend", rows["TOURISM_POLICY_EVENT"]["stage4c"])
        self.assertIn("type_certification", rows["URBAN_AIR_DRONE"]["stage2"])
        self.assertIn("type_certification_missing", rows["EVTOL_CERTIFICATION_CASH_BURN"]["stage4c"])
        self.assertIn("type_certification_missing", rows["PART135_NOT_TYPE_CERTIFICATION"]["stage4c"])
        self.assertIn("nhtsa_scrutiny", rows["TRANSPORT_SAFETY_REGULATORY_OVERLAY"]["stage4c"])
        self.assertIn("unit_economics_missing", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "vehicle_sales_growth",
            "hybrid_sales_growth",
            "op_margin_target",
            "shareholder_return_ratio",
            "tariff_event_flag",
            "local_production_capacity",
            "us_localization_labor_risk_flag",
            "visa_delay_flag",
            "plant_ramp_delay_flag",
            "hybrid_component_revenue",
            "capacity_normalization_flag",
            "hybrid_wait_time_months",
            "adas_component_revenue",
            "robotaxi_service_area",
            "paid_ride_volume",
            "wait_time_minutes",
            "ride_completion_rate",
            "misrouting_flag",
            "dropoff_distance_issue_flag",
            "safety_monitor_flag",
            "safety_recall_flag",
            "nhtsa_scrutiny_flag",
            "av_crash_report_count",
            "flooded_road_recall_flag",
            "weather_handling_failure_flag",
            "insurance_liability_cost",
            "autonomous_trucking_route",
            "paid_freight_flag",
            "driverless_miles",
            "truck_cost_per_mile",
            "remote_support_cost",
            "insurance_cost_per_truck",
            "driver_as_a_service_flag",
            "passenger_revenue_growth",
            "synergy_amount",
            "route_divestment_flag",
            "cargo_business_divestment_flag",
            "brand_integration_timeline",
            "casino_drop_amount",
            "alipay_wechatpay_integration_flag",
            "freight_rate_index",
            "used_car_residual_value",
            "repair_cost_per_vehicle",
            "tire_replacement_demand",
            "oe_tire_demand",
            "north_america_volume_change",
            "raw_material_spread",
            "tire_guidance_cut_flag",
            "tariff_impact_on_tire_demand",
            "micromobility_fcf",
            "debt_maturity_amount",
            "type_certification_flag",
            "evtol_cash_burn",
            "part135_flag",
            "vertiport_contract_flag",
            "satellite_backlog",
            "gross_backlog",
            "capex_debt_ratio",
            "opendart_rcept_no",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND141_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r9_loop8_guardrails(self):
        summary = round141_summary()
        summary_md = render_round141_summary_markdown()
        guardrails = render_round141_green_guardrail_markdown()
        overlays = render_round141_risk_overlay_markdown()
        price_plan = render_round141_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 33)
        self.assertEqual(summary["base_score_axis_count"], 7)
        self.assertEqual(summary["case_candidate_count"], 20)
        self.assertEqual(summary["success_candidate_count"], 8)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 10)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 2)
        self.assertEqual(summary["watch_yellow_first_count"], 17)
        self.assertEqual(summary["redteam_first_count"], 14)
        self.assertEqual(summary["gate_only_target_count"], 10)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round 141", summary_md)
        self.assertIn("Do not apply R9 Loop-8 v8.0 weights", guardrails)
        self.assertIn("R9 v8 Base Score Axes", summary_md)
        self.assertIn("unit_fleet_economics", summary_md)
        self.assertIn("US localization", guardrails)
        self.assertIn("Paid driverless freight", guardrails)
        self.assertIn("ROBOTAXI_SAFETY_4C", overlays)
        self.assertIn("AV_CRASH_DISCLOSURE_PROBE_WATCH", overlays)
        self.assertIn("AUTONOMOUS_TRUCKING_PAID_FREIGHT_MILESTONE", overlays)
        self.assertIn("AUTONOMOUS_TRUCKING_UNIT_ECONOMICS_UNPROVEN", overlays)
        self.assertIn("TOURISM_POLICY_EVENT", overlays)
        self.assertIn("PART135_NOT_TYPE_CERTIFICATION", overlays)
        self.assertIn("DISCLOSURE_CONFIDENCE_CAP", overlays)
        self.assertIn("hyundai_tariff_margin_cut_case", price_plan)
        self.assertIn("avride_nhtsa_probe_case", price_plan)
        self.assertIn("bot_auto_paid_driverless_freight_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round141_r9_loop8_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r9_loop8_round141.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round141_r9_loop8_v8.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["base_score_axes"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND141_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round141_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round141_r9_loop8_mobility_transport_leisure", text)


if __name__ == "__main__":
    unittest.main()
