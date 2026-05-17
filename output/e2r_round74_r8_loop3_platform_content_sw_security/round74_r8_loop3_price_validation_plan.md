# Round 74 R8 Loop-3 Price Validation Plan

For every case, backfill stage prices and forward MFE/MAE before applying score-weight changes.

## Priority Cases
- douzone_bizon_eqt_cloud_erp_case: 2025-11-07 / b2b_saas_success_candidate_price_backfill_needed
- palantir_q4_2025_ai_revenue_case: 2026-02-03 / ai_software_revenue_aligned
- palantir_q1_2026_fastest_growth_case: 2026-05-05 / ai_software_4b_valuation
- datadog_q1_2026_ai_observability_case: 2026-05-07 / observability_ai_aligned
- fortinet_q1_2026_security_billings_case: 2026-05-07 / security_billings_aligned_candidate
- netflix_ad_tier_250m_case: 2026-05-13 / streaming_ad_platform_aligned_privacy_watch
- trade_desk_revenue_miss_case: 2025-02-13 / adtech_premium_miss
- crowdstrike_outage_shareholder_case: 2024-07-31 / security_trust_break_hard_4c
- delta_crowdstrike_lawsuit_case: 2024-10-25 / customer_damage_operational_trust_break
- kakao_founder_legal_overhang_case: 2024-07-01 / legal_overhang_watch_resolved_by_acquittal
- roblox_safety_forecast_cut_case: 2026-05-01 / ugc_platform_safety_4c
- take_two_gta_delay_case: 2025-05-02 / single_ip_delay_and_preorder_event_premium
- take_two_gta_preorder_rumor_case: 2026-05-14 / single_ip_event_premium
- wpp_ad_forecast_cut_case: 2025-06-09 / traditional_ad_agency_4c_watch
- wpp_profit_drop_ai_disruption_case: 2025-08-07 / traditional_ad_agency_ai_disruption_4c
- netflix_texas_privacy_lawsuit_case: 2026-05-11 / platform_legal_overhang_privacy_4c_watch
- meta_scam_ads_lawsuit_case: 2026-05-11 / platform_ad_trust_4c_watch
- meta_youth_safety_trial_case: 2026-05-13 / youth_safety_platform_risk

## Required Validation Fields

case_id, symbol, company_name, primary_archetype, secondary_archetypes, stage1_date, stage2_date, stage3_date, stage4b_date, stage4c_date, stage1_price, stage2_price, stage3_price, stage4b_price, stage4c_price, peak_price, peak_date, MFE_30D, MFE_90D, MFE_180D, MFE_1Y, MFE_2Y, MAE_30D, MAE_90D, MAE_180D, MAE_1Y, drawdown_after_peak, below_stage2_price_flag, below_stage3_price_flag, arr_growth, subscription_revenue_growth, recurring_revenue_ratio, churn_rate, net_retention_rate, customer_count, large_customer_concentration, op_margin_change, fcf_margin, ai_revenue_contribution, ai_contract_value, total_contract_value, rule_of_40, compute_cost_ratio, model_dependency_flag, ai_workflow_integration_flag, auditability_flag, revenue_per_employee, observability_revenue, ai_workload_customer_count, sre_agent_revenue_flag, security_analyst_agent_flag, cloud_optimization_risk_flag, bookings_growth, daily_active_users, monthly_active_users, communication_engagement_change, single_ip_revenue_ratio, game_delay_flag, preorder_event_flag, platform_safety_flag, age_verification_flag, content_monitoring_flag, regulatory_ban_flag, ad_revenue_growth, ad_arpu, ad_tier_users, ad_supported_signup_mix, own_adtech_flag, client_budget_cut_flag, privacy_lawsuit_flag, scam_ad_lawsuit_flag, ad_quality_risk_flag, high_risk_ad_revenue_estimate, child_data_collection_flag, dark_pattern_allegation_flag, security_billings_growth, security_arr_growth, security_outage_flag, affected_device_count, customer_lawsuit_flag, shareholder_lawsuit_flag, renewal_rate, incident_recovery_days, trust_damage_flag, founder_legal_case_flag, governance_overhang_flag, mna_legal_dispute_flag, regulatory_investigation_flag, youth_safety_lawsuit_flag, antitrust_lawsuit_flag, copyright_lawsuit_flag, training_data_risk_flag, license_risk_flag, generative_ai_ip_risk_flag, score_price_alignment, price_validation_status, review_notes
