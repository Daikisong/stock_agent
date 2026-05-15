# Round-34 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| CARBON_CREDIT_CBAM_COMPLIANCE | WATCH_YELLOW_FIRST | pass_through_possible, carbon_monitoring_recurring_revenue, premium_low_carbon_product, fcf_from_compliance_or_cost_saving | policy_change, allowance_price_volatility, greenwashing, pass_through_failure, offset_integrity |
| PAYMENT_FINTECH_INFRA | GREEN_POSSIBLE | transaction_volume_growth, take_rate_stable, merchant_or_user_lock_in, profitable_or_fcf_conversion | regulation, take_rate_pressure, credit_loss, security, competition, user_count_only |
| OPTICAL_NETWORKING_AI_DATACENTER | GREEN_POSSIBLE | hyperscaler_long_contract, direct_ai_datacenter_supply, bottleneck_optical_component, op_eps_revision | hyperscaler_concentration, valuation_crowding, capex_delay, inventory, unclear_ai_dc_exposure |
| TELECOM_5G_6G_CAPEX_CYCLE | REDTEAM_FIRST | confirmed_operator_capex, equipment_order, private_network_revenue | telecom_capex_cycle, geopolitics, security_review, operator_delay, policy_no_revenue |
| LITHIUM_BATTERY_RAW_MATERIAL | WATCH_YELLOW_FIRST | low_cost_asset, long_term_offtake, demand_visible, fcf_defense_at_low_price | lithium_price, mine_restart, ev_demand, oversupply, capex, price_rebound_only |
| HOME_LIVING_APPLIANCE_RENTAL | GREEN_POSSIBLE | rental_subscription_revenue, filter_or_care_service, overseas_account_growth, stable_fcf | replacement_cycle, housing_market, consumer_sentiment, inventory, competition, hardware_only |
| AI_ACCELERATOR_CHIP_PUREPLAY | WATCH_YELLOW_FIRST | actual_revenue, customer_mass_production, customer_validation_visible, gross_margin_improvement | customer_validation, nvidia_competition, valuation_overheat, foundry_yield, rd_burn, tapeout_only |
| MOBILITY_RENTAL_MICROMOBILITY | WATCH_YELLOW_FIRST | positive_fcf, stable_city_utilization, maintenance_cost_control, unit_economics_visible | unit_economics, regulation, maintenance_cost, seasonality, competition, revenue_growth_no_profit |

## What Not To Change
- Do not apply v1.9 weights to production scoring yet.
- Do not use case IDs or theme labels as candidate-generation input.
- Do not invent stage dates, prices, CBAM pass-through, fintech take rate, hyperscaler terms, telecom orders, lithium costs, rental churn, AI-chip yield, or mobility unit economics.
- Do not lower Stage 3-Green thresholds to improve recall.
