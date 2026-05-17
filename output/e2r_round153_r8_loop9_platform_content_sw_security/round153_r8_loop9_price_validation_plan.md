# Round 153 R8 Loop-9 Price Validation Plan

For every case, backfill stage prices and forward MFE/MAE before applying score-weight changes.

## Priority Cases
- douzone_bizon_eqt_cloud_erp_case: 2025-11-07 / b2b_saas_success_candidate_price_backfill_needed
- palantir_q4_2025_ai_revenue_case: 2026-02-03 / government_and_commercial_ai_contract_success
- palantir_q1_2026_fastest_growth_case: 2026-05-04 / ai_software_4b_valuation
- akamai_frontier_model_ai_cloud_deal_case: 2026-05-08 / edge_ai_cloud_contract_aligned_4b_watch
- akamai_ai_cloud_revenue_contribution_case: 2026-05-13 / edge_ai_cloud_revenue_contribution_watch
- datadog_q1_2026_ai_observability_case: 2026-05-07 / observability_ai_aligned
- dynatrace_q4_2026_arr_guidance_case: 2026-05-13 / observability_guidance_failed
- fortinet_q1_2026_security_billings_case: 2026-05-07 / security_billings_aligned_candidate
- cisco_ai_infrastructure_orders_case: 2026-05-13 / ai_networking_software_infra_crossover_stage2_restructuring_watch
- netflix_ad_tier_250m_case: 2026-05-13 / streaming_ad_platform_aligned_privacy_watch
- trade_desk_revenue_miss_case: 2025-02-13 / adtech_premium_miss
- crowdstrike_outage_shareholder_case: 2024-07-31 / security_trust_break_hard_4c
- kakao_founder_legal_overhang_case: 2024-07-01 / legal_overhang_watch_resolved_by_acquittal
- roblox_safety_forecast_cut_case: 2026-05-01 / ugc_platform_safety_4c
- take_two_gta_preorder_rumor_case: 2026-05-14 / single_ip_event_premium
- wpp_ad_forecast_cut_case: 2025-06-09 / traditional_ad_agency_4c_watch
- netflix_texas_privacy_lawsuit_case: 2026-05-11 / platform_legal_overhang_privacy_4c_watch
- meta_scam_ads_lawsuit_case: 2026-05-11 / platform_ad_trust_4c_watch
- meta_youth_safety_trial_case: 2026-05-13 / youth_safety_platform_risk
- legacy_saas_ai_disruption_case: 2026-05-14 / legacy_saas_ai_disruption
- salesforce_agentforce_arr_case: 2026-05-14 / legacy_saas_ai_reinforcement_watch

## Required Validation Fields

case_id, symbol, company_name, primary_archetype, secondary_archetypes, stage1_date, stage2_date, stage3_date, stage4b_date, stage4c_date, stage1_price, stage2_price, stage3_price, stage4b_price, stage4c_price, peak_price, peak_date, MFE_30D, MFE_90D, MFE_180D, MFE_1Y, MFE_2Y, MAE_30D, MAE_90D, MAE_180D, MAE_1Y, drawdown_after_peak, below_stage2_price_flag, below_stage3_price_flag, arr_growth, subscription_revenue_growth, recurring_revenue_ratio, churn_rate, net_retention_rate, customer_count, large_customer_concentration, op_margin_change, fcf_margin, ai_revenue_contribution, ai_arr, ai_attach_rate, ai_contract_value, total_contract_value, rule_of_40, compute_cost_ratio, model_dependency_flag, ai_workflow_integration_flag, ontology_workflow_flag, auditability_flag, program_of_record_flag, government_program_budget_flag, maven_or_defense_ai_flag, revenue_per_employee, government_revenue_growth, commercial_revenue_growth, seat_churn_flag, license_downsell_flag, gross_margin_impact_from_ai, agent_cost_overrun_flag, workflow_lockin_failure_flag, ai_arr_too_small_flag, edge_cloud_contract_value, edge_cloud_contract_duration_years, frontier_model_customer_flag, customer_disclosed_flag, cloud_infrastructure_services_revenue, cdn_legacy_revenue_change, edge_inference_revenue_flag, cloud_capex_amount, ai_customer_concentration, observability_revenue, observability_arr, ai_workload_customer_count, sre_agent_revenue_flag, security_analyst_agent_flag, cloud_optimization_risk_flag, arr_miss_flag, guidance_miss_flag, net_new_arr_change, ai_infrastructure_orders, hyperscaler_ai_orders, data_center_switching_orders, software_security_mix, silicon_optics_revenue_mix, order_to_revenue_conversion, margin_conversion_flag, restructuring_cost, workforce_reduction, legacy_networking_mix, bookings_growth, daily_active_users, monthly_active_users, communication_engagement_change, single_ip_revenue_ratio, game_delay_flag, preorder_event_flag, platform_safety_flag, age_verification_flag, content_monitoring_flag, regulatory_ban_flag, ad_revenue_growth, ad_arpu, ad_tier_users, ad_supported_signup_mix, own_adtech_flag, client_budget_cut_flag, ad_growth_forecast_cut, ai_production_disruption_flag, privacy_lawsuit_flag, scam_ad_lawsuit_flag, ad_quality_risk_flag, high_risk_ad_revenue_estimate, child_data_collection_flag, dark_pattern_allegation_flag, autoplay_restriction_flag, security_billings_growth, security_arr_growth, ai_threat_demand_flag, sase_revenue_growth, firewall_revenue_growth, security_outage_flag, affected_device_count, customer_lawsuit_flag, shareholder_lawsuit_flag, renewal_rate, incident_recovery_days, trust_damage_flag, founder_legal_case_flag, governance_overhang_flag, mna_legal_dispute_flag, regulatory_investigation_flag, youth_safety_lawsuit_flag, age_verification_order_flag, algorithm_modification_order_flag, addictive_design_claim_flag, infinite_scroll_restriction_flag, antitrust_lawsuit_flag, copyright_lawsuit_flag, training_data_risk_flag, license_risk_flag, generative_ai_ip_risk_flag, opendart_rcept_no, opendart_detail_fetched_flag, disclosure_confidence_score, detail_parser_confidence, disclosure_signal_class, routine_disclosure_flag, risk_disclosure_flag, high_signal_disclosure_flag, score_price_alignment, price_validation_status, review_notes
