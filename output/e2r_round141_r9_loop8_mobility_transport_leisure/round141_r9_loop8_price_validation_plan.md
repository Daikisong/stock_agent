# Round 141 R9 Loop-8 Price Validation Plan

For every case, backfill stage prices and forward MFE/MAE before applying score-weight changes.

## Priority Cases
- hyundai_hybrid_valueup_case: 2024-08-28 / auto_valueup_aligned_candidate
- hyundai_tariff_margin_cut_case: 2025-09-18 / auto_tariff_margin_watch
- toyota_hybrid_parts_bottleneck_case: 2025-03-31 / hybrid_component_bottleneck_reference
- avride_hyundai_ioniq5_robotaxi_case: 2025-03-05 / robotaxi_deployment_aligned_stage2_candidate
- uber_avride_dallas_robotaxi_case: 2025-12-03 / uber_integration_small_fleet_watch
- tesla_texas_robotaxi_wait_time_case: 2026-05-12 / robotaxi_operational_reality_check
- waymo_flood_recall_robotaxi_case: 2026-05-12 / robotaxi_safety_4c
- avride_nhtsa_probe_case: 2026-05-12 / robotaxi_deployment_with_av_probe_watch
- aurora_driverless_trucking_texas_case: 2025-05-01 / autonomous_trucking_stage2_candidate
- bot_auto_paid_driverless_freight_case: 2026-04-30 / autonomous_trucking_paid_freight_stage2_candidate
- gm_aurora_sterling_anderson_product_case: 2025-05-12 / adas_super_cruise_strategy_candidate
- korean_air_asiana_integration_case: 2025-02-07 / airline_integration_cycle_watch
- china_group_visa_tourism_case: 2025-09-29 / tourism_policy_event_stage1
- ses_airline_connectivity_case: 2026-05-12 / satellite_connectivity_aligned_candidate
- container_rate_collapse_case: 2025-10-03 / shipping_cyclical_success_or_4c
- hertz_ev_rental_failure_case: 2024-01-11 / rental_ev_unit_economics_4c
- michelin_tire_demand_cut_case: 2025-10-13 / tire_demand_slowdown_4c_watch
- joby_discounted_offering_case: 2025-10-08 / evtOL_execution_candidate_but_dilution_4c_watch
- lilium_evtol_cash_crunch_case: 2024-11-25 / evtol_cash_burn_hard_counterexample
- archer_part135_no_type_cert_case: 2024-06-05 / part135_stage1_not_stage3

## Required Validation Fields

case_id, symbol, company_name, primary_archetype, secondary_archetypes, stage1_date, stage2_date, stage3_date, stage4b_date, stage4c_date, stage1_price, stage2_price, stage3_price, stage4b_price, stage4c_price, peak_price, peak_date, MFE_30D, MFE_90D, MFE_180D, MFE_1Y, MFE_2Y, MAE_30D, MAE_90D, MAE_180D, MAE_1Y, drawdown_after_peak, below_stage2_price_flag, below_stage3_price_flag, vehicle_sales_growth, hybrid_sales_growth, ev_sales_growth, erev_plan_flag, operating_margin, op_margin_target, op_margin_cut_flag, fcf_margin, buyback_amount, dividend_policy_change, shareholder_return_ratio, tariff_event_flag, tariff_cost_amount, local_production_ratio, local_production_capacity, us_localization_labor_risk_flag, visa_delay_flag, plant_ramp_delay_flag, recall_flag, quality_cost_flag, hybrid_component_order, hybrid_component_revenue, inverter_supply_constraint_flag, magnet_supply_constraint_flag, motor_supply_constraint_flag, customer_concentration, raw_material_cost_change, capacity_normalization_flag, hybrid_wait_time_months, adas_component_revenue, camera_lidar_radar_revenue, autonomous_platform_customer, mass_adoption_flag, robotaxi_service_area, robotaxi_fleet_size, paid_ride_volume, rides_per_week, wait_time_minutes, ride_completion_rate, misrouting_flag, dropoff_distance_issue_flag, safety_monitor_flag, cost_per_mile, vehicle_utilization, safety_recall_flag, nhtsa_scrutiny_flag, av_crash_report_count, weather_handling_failure_flag, flooded_road_recall_flag, insurance_liability_cost, remote_assistance_cost, platform_integration_flag, autonomous_trucking_route, autonomous_trucking_customer, paid_freight_flag, driverless_miles, driverless_truck_count, freight_revenue, freight_repeat_customer_flag, driverless_safety_report_flag, restricted_odd_flag, daylight_only_flag, good_weather_only_flag, truck_cost_per_mile, truck_utilization, remote_support_cost, insurance_cost_per_truck, carrier_partner_flag, driver_as_a_service_flag, passenger_revenue_growth, cargo_revenue_growth, load_factor, jet_fuel_price, fx_rate_exposure, integration_cost, synergy_amount, asiana_integration_flag, lcc_integration_flag, route_divestment_flag, cargo_business_divestment_flag, brand_integration_timeline, tourist_arrivals, china_tourist_arrivals, visa_free_policy_flag, casino_drop_amount, vip_mix, duty_free_sales, duty_free_asp, hotel_occupancy, revpar, average_spend_per_visitor, alipay_wechatpay_integration_flag, freight_rate_index, container_rate, spot_rate_below_breakeven_flag, fleet_capacity_growth, red_sea_disruption_flag, suez_route_normalization_flag, overcapacity_flag, ebitda_change, dividend_change, rental_fleet_size, ev_fleet_ratio, used_car_residual_value, repair_cost_per_vehicle, insurance_cost_change, vehicle_depreciation_charge, fleet_write_down, utilization_rate, tire_replacement_demand, oe_tire_demand, north_america_volume_change, raw_material_spread, tire_guidance_cut_flag, tariff_impact_on_tire_demand, micromobility_revenue, micromobility_fcf, net_loss, debt_maturity_amount, going_concern_flag, city_count, seasonality_risk, platform_partner_revenue_ratio, uber_dependency_flag, evtol_cash_burn, cash_runway_months, type_certification_flag, part135_flag, production_certification_flag, discounted_offering_flag, offering_discount_pct, pre_revenue_flag, commercial_launch_date, vertiport_contract_flag, satellite_backlog, connectivity_revenue_growth, airline_contract_count, new_contracts_value, gross_backlog, capex_debt_ratio, launch_delay_flag, secure_comms_revenue_flag, opendart_rcept_no, opendart_detail_fetched_flag, disclosure_confidence_score, detail_parser_confidence, disclosure_signal_class, routine_disclosure_flag, risk_disclosure_flag, high_signal_disclosure_flag, score_price_alignment, price_validation_status, review_notes
