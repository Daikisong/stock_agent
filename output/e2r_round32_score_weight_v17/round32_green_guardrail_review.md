# Round-32 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| GENERAL_TRADING_RESOURCE_INFRA | GREEN_POSSIBLE | long_term_offtake, project_equity, diversified_fcf, shareholder_return, roe_fcf_improvement | commodity_price, fx, project_execution, conglomerate_discount, low_margin_trading |
| LNG_ENERGY_TRADING_DISTRIBUTION | WATCH_YELLOW_FIRST | long_term_supply_contract, procurement_stability, pass_through_visible, fcf_improvement | energy_price, inventory_loss, tariff, geopolitics, pass_through_failure |
| DISPLAY_OLED_SUPPLYCHAIN | GREEN_POSSIBLE | customer_oled_adoption, oled_order_or_supply, lcd_restructuring, opm_improvement | panel_price_competition, capex_cycle, customer_concentration, china_price_competition |
| ELECTRONIC_COMPONENTS_MLCC_SENSOR | GREEN_POSSIBLE | customer_diversification, high_value_component_demand, capex_to_revenue_conversion, opm_improvement | inventory_cycle, customer_concentration, china_supply_chain, component_price_pressure, rare_earth_dependency |
| DIGITAL_HEALTHCARE_REMOTE_MEDICINE | GREEN_POSSIBLE | hospital_or_insurer_contract, recurring_subscription, reimbursement_visible, unit_economics_visible | regulation, reimbursement, data_security, unit_economics, clinical_liability |
| COMMODITY_MEMORY_GENERAL_SEMI | GREEN_POSSIBLE | memory_price_increase, inventory_decline, op_eps_revision, supply_discipline | cycle, hbm_lag, supply_rebound, ai_capex_slowdown, spot_rebound_only |
| ENERGY_UTILITY_LNG_GAS | WATCH_YELLOW_FIRST | tariff_normalization, receivables_recovery, lng_procurement_stability, fcf_improvement | tariff_regulation, debt, lng_price, receivables, policy_risk |
| AI_CHIP_FABRIC_INFRA | REDTEAM_FIRST | customer_contract, mass_production_revenue, customer_validation, op_eps_conversion | no_revenue, customer_validation, yield, theme_overheat, unclear_equity_exposure |

## What Not To Change
- Do not apply v1.7 weights to production scoring yet.
- Do not use case IDs or theme labels as candidate-generation input.
- Do not invent stage dates, prices, contract amounts, LNG volumes, tariff outcomes, OLED margins, MLCC inventory levels, reimbursement status, HBM approval, or foundry yield.
- Do not lower Stage 3-Green thresholds to improve recall.
