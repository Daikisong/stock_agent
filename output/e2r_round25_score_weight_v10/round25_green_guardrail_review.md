# Round-25 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| AI_DATA_CENTER_COOLING | GREEN_POSSIBLE | customer_datacenter_capex_link, confirmed_order_or_delivery, cooling_bottleneck, repeat_service_revenue, op_eps_revision | liquid_cooling_theme_only, no_customer_order, ai_capex_delay, low_margin_project, customer_concentration |
| SECURITY_IDENTITY_DEEPFAKE | GREEN_POSSIBLE | recurring_subscription, low_churn, customer_diversification, opm_improvement, no_major_outage | operational_trust, outage, legal, customer_retention, contract_absence |
| CRO_CLINICAL_SERVICE | WATCH_YELLOW_FIRST | service_backlog, customer_diversification, repeat_clinical_service_revenue, opm_improvement, funding_cycle_stable | biotech_funding_cycle_down, customer_concentration, trial_delay, low_margin_backlog, customer_budget_cut |
| SOLAR_TARIFF_SUPPLYCHAIN | WATCH_YELLOW_FIRST | utilization_up, component_supply_stable, tariff_risk_low, op_fcf_improvement, long_term_demand | tariff, customs, subsidy, supply_chain, forced_labor_import_detention |
| RETAIL_ECOMMERCE_LOGISTICS | WATCH_YELLOW_FIRST | opm_improvement, inventory_normalization, cost_leverage, fcf_improvement, regulatory_risk_low | logistics_cost, inventory, supplier_regulation, data_security, fresh_ecommerce_loss |
| INSURANCE_UNDERWRITING_CYCLE | GREEN_POSSIBLE | roe_improvement, csm_or_loss_ratio_stability, capital_ratio_stable, shareholder_return_execution, credit_risk_low | underwriting, capital_ratio, cyber_operational, credit_cost, low_pbr_only |
| DIGITAL_HEALTHCARE_AI | WATCH_YELLOW_FIRST | external_clinical_validation, regulatory_clearance, hospital_adoption, reimbursement_or_paid_usage, revenue_or_op_conversion | paper_only, poc_only, no_reimbursement, liability, clinical_validation_gap |
| BATTERY_RECYCLING_ESS_SHIFT | WATCH_YELLOW_FIRST | customer_contract, utilization_up, fcf_disciplined_capex, demand_durable | ev_demand, mineral_price, capex_overbuild, policy, no_commercialization |
| SECURITIES_BROKERAGE_CYCLE | WATCH_YELLOW_FIRST | brokerage_revenue_growth, ib_pipeline, capital_ratio_stable, pf_risk_low, roe_improvement | market_turnover, pf, proprietary_loss, ipo_cycle, vc_exit_market_weakness |
| MEMORY_HBM_CAPACITY | GREEN_POSSIBLE | hbm_demand, supply_discipline, medium_term_revision, capacity_constraint, long_term_contract_or_prepayment | capex_reversal, cycle_peak, crowding, price_only_memory_rally, customer_ai_capex_slowdown |

## What Not To Change
- Do not apply v1.0 weights to production scoring yet.
- Do not score policies, AI features, PoCs, revenue headlines, or theme labels without source-backed economics.
- Do not invent stage dates, prices, margins, retention, FCF, reimbursement, or contract values.
