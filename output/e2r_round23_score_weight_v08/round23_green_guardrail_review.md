# Round-23 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| DIGITAL_HEALTHCARE_AI | WATCH_YELLOW_FIRST | regulatory_clearance, hospital_adoption, reimbursement_or_paid_usage, external_clinical_validation, revenue_or_op_conversion | paper_only, no_reimbursement, overtrust_risk, liability_unclear, subgroup_validation_gap |
| TELECOM_5G_6G_AI_NETWORK | WATCH_YELLOW_FIRST | confirmed_network_or_idc_capex, equipment_order, arpu_or_idc_revenue, security_reliability | generation_upgrade_theme_only, capex_burden, security_breach, no_revenue_conversion |
| MEDIA_AD_CONTENT_CYCLE | WATCH_YELLOW_FIRST | repeat_ip_monetization, global_tour_or_distribution, subscription_or_arpu, opm_improvement | hit_driven, ad_cycle_down, single_artist_contract_risk, broadcast_ad_decline |
| SERVICE_KIOSK_AUTOMATION | WATCH_YELLOW_FIRST | installed_base, maintenance_or_saas_revenue, payment_fee_revenue, customer_cost_saving, opm_improvement | one_off_hardware_sales, minimum_wage_theme_only, margin_competition, no_maintenance_revenue |
| SMART_FARM_AGRI_TECH | WATCH_YELLOW_FIRST | export_order, recurring_service, overseas_sales, opm_improvement | commodity_cycle, subsidy_only, weather_event, feed_cost_pressure, policy_theme_only |
| HOME_LIVING_APPLIANCE | WATCH_YELLOW_FIRST | export_growth, premium_mix, smart_home_subscription, opm_improvement | replacement_cycle_only, birthrate, inventory, single_product_fad, no_recurring_service |
| CONSUMER_REGULATED_PRODUCT | WATCH_YELLOW_FIRST | repeat_consumption, distribution_network, regulatory_stability, brand_margin | regulation_crackdown, legal_uncertainty, social_backlash, license_expectation_only, one_off_demand |
| MEMORY_HBM_CAPACITY | GREEN_POSSIBLE | hbm_demand, dram_nand_price, supply_discipline, long_term_contract_or_prepayment, multi_year_revision | cycle_peak, capex_reversal, crowding, memory_price_down, customer_ai_capex_slowdown |
| AI_DATA_CENTER_INFRASTRUCTURE | GREEN_POSSIBLE | confirmed_order, data_center_capex_link, power_cooling_server_bottleneck, op_eps_revision | ai_capex_expectation_only, project_delay, no_revenue_conversion, customer_capex_cut |

## What Not To Change
- Do not apply v0.8 weights to production scoring yet.
- Do not score papers, policy plans, PoCs, or theme labels without revenue/usage/order evidence.
- Do not invent stage dates, prices, AUC, reimbursement, paid usage, ARR, FCF, or contract values.
