# Round-29 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| DEFENSE_GOVERNMENT_BACKLOG | GREEN_POSSIBLE | government_customer, multi_year_contract, order_backlog_to_sales, delivery_schedule, opm_improvement, dilution_risk_low | delivery_delay, cost_overrun, political_or_export_permit, dilution, theme_only |
| SHIPBUILDING_OFFSHORE_BACKLOG | GREEN_POSSIBLE | newbuilding_price_up, low_margin_backlog_rolloff, high_margin_delivery_start, op_eps_revision, contract_cancellation_risk_low | low_margin_backlog, steel_plate_cost, labor_cost, contract_cancellation, order_slowdown |
| EXPORT_RECURRING_CONSUMER | GREEN_POSSIBLE | repeat_consumer_demand, overseas_channel_expansion, opm_expansion, fy1_fy2_eps_revision, inventory_risk_low | single_product, inventory, recall_or_regulation, asp_drop, channel_stuffing |
| RAIL_INFRASTRUCTURE | GREEN_POSSIBLE | actual_contract, contract_amount_to_sales, delivery_schedule, margin_visible, financing_risk_low | policy_theme_only, mou_only, project_delay, margin_uncertainty, financing |
| CHEMICAL_SPREAD | WATCH_YELLOW_FIRST | spread_sustained, supply_glut_eases, op_fcf_improvement, inventory_risk_low | china_middle_east_overcapacity, spread_reversal, inventory, demand_slowdown |
| DIGITAL_ASSET_TOKENIZATION | WATCH_YELLOW_FIRST | regulatory_approval, transaction_volume, fee_model, payment_network_adoption, security_risk_low | regulation, security, adoption, liquidity, no_revenue, coin_theme_only |
| SECURITY_IDENTITY_DEEPFAKE | GREEN_POSSIBLE | recurring_subscription_revenue, low_churn, customer_diversification, opm_improvement, operational_trust_intact | operational_trust, outage, legal, customer_retention, theme_only |
| RETAIL_ECOMMERCE_LOGISTICS | WATCH_YELLOW_FIRST | opm_improvement, fcf_conversion, repeat_customer, inventory_normalizes, data_security_risk_low | logistics_cost, inventory, supplier_regulation, data_security, competition, revenue_only_growth |
| BATTERY_MATERIALS_ESS | WATCH_YELLOW_FIRST | customer_contract, demand_visibility, margin_stable, recycling_volume, fcf_safe_capex | ev_demand, mineral_price, capex_overbuild, policy, recycling_volume_missing |
| INSURANCE_UNDERWRITING | GREEN_POSSIBLE | roe_improvement, csm_or_underwriting_quality, capital_ratio_stable, actual_return_policy, credit_cost_low | underwriting, capital_ratio, cyber_operational, credit_cost, low_roe |
| SECURITIES_BROKERAGE | WATCH_YELLOW_FIRST | market_turnover_sustained, ib_recovery, shareholder_return, pf_risk_low | market_turnover, pf, proprietary_loss, ipo_cycle, cycle_only |
| VALUE_UP_SHAREHOLDER | GREEN_POSSIBLE | roe_improvement, actual_cancellation, repeat_shareholder_return, dividend_sustainability, fcf_support | governance, execution, low_roe, no_cancellation, index_inclusion_only |

## What Not To Change
- Do not apply v1.4 weights to production scoring yet.
- Do not use case IDs or theme labels as candidate-generation input.
- Do not invent stage dates, prices, contract size, contract duration, OP YoY, ASP, OPM, CSM, ROE, or transaction volume.
- Do not lower Stage 3-Green thresholds to improve recall.
