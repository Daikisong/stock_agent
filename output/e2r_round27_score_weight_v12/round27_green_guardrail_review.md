# Round-27 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| GAME_CONTENT_IP | WATCH_YELLOW_FIRST | repeat_ip_monetization, monetization_confirmed, regional_diversification, op_eps_revision, regulation_risk_low | hit_driven, regulation, data_security, single_ip_dependency, download_only |
| MEDICAL_DEVICE_HEALTHCARE_EXPORT | GREEN_POSSIBLE | export_country_expansion, recurring_consumables_or_procedure, opm_roe_improvement, approval_stable, channel_quality | approval, safety, counterfeit, channel_quality, competition, single_device_no_consumable |
| DIGITAL_HEALTHCARE_AI | WATCH_YELLOW_FIRST | external_clinical_validation, approval_or_clearance, hospital_adoption, reimbursement_or_paid_usage, revenue_conversion | regulation, reimbursement, clinical_validation, subgroup_bias, liability, poc_only |
| RETAIL_ECOMMERCE_LOGISTICS | WATCH_YELLOW_FIRST | opm_improvement, inventory_normalized, logistics_cost_stable, fcf_improvement, regulation_risk_low | logistics_cost, inventory, supplier_regulation, data_security, competition, sales_without_fcf |
| EDUCATION_SPECIALTY_SERVICES | WATCH_YELLOW_FIRST | adult_or_b2b_mix, subscription_or_repeat_enrollment, opm_improvement, policy_risk_low, birthrate_risk_offset | birthrate, regulation, ai_substitution, offline_fixed_cost, entrance_exam_theme_only |
| TELECOM_GRID_AI_NETWORK | WATCH_YELLOW_FIRST | equipment_order, datacenter_or_grid_capex_link, long_term_capex_visibility, op_eps_conversion, regulation_risk_low | capex_burden, regulation, project_delay, low_margin_equipment, policy_keyword_only |
| AI_DATA_CENTER_COOLING | GREEN_POSSIBLE | customer_datacenter_capex_link, confirmed_order_or_delivery, cooling_bottleneck, repeat_service_revenue, op_eps_revision | ai_capex_delay, low_margin_project, customer_concentration, no_customer_order |
| SECURITY_IDENTITY_DEEPFAKE | GREEN_POSSIBLE | recurring_subscription, low_churn, customer_diversification, opm_improvement, no_major_outage | operational_trust, outage, legal, contract_absence, customer_retention |
| CLOUD_AI_SOFTWARE_INFRA | GREEN_POSSIBLE | recurring_revenue, arpu, retention, opm_or_fcf_improvement, ai_cost_control | ai_feature_only, ai_cost_overrun, churn, si_revenue_only, opm_decline |
| INSURANCE_UNDERWRITING_CYCLE | GREEN_POSSIBLE | roe_improvement, csm_or_loss_ratio_stability, capital_ratio_stable, shareholder_return_execution, credit_risk_low | underwriting, capital_ratio, cyber_operational, credit_cost, low_pbr_only |

## What Not To Change
- Do not apply v1.2 weights to production scoring yet.
- Do not score downloads, store counts, papers, policies, PoCs, or traffic without source-backed economics.
- Do not invent stage dates, prices, monetization, reimbursement, OPM, FCF, retention, or approval status.
