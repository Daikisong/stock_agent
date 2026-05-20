# Round 246 R3 Green Gate Review

Do not apply these weights to production scoring yet.

R3 Stage 3-Green is not `ESS/LFP/lithium/solar localization is good`. It requires contracts to close into GWh, delivery, utilization, OPM, FCF, and cleared execution risks.

## Required Fields

- binding_contract
- customer_gwh_supply_period_confirmed
- actual_delivery_or_revenue_recognition_started
- utilization_improvement
- opm_or_gross_margin_confirmed
- fcf_after_capex
- subsidy_excluded_profit_quality
- customer_ev_strategy_or_ess_demand_risk_passed
- supply_chain_customs_labor_execution_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- ev_capacity_announcement_only
- ess_lfp_theme_only
- customer_name_only
- unofficial_customer_source_only
- factory_construction_only
- lithium_resource_headline_only
- solar_localization_headline_only
- subsidy_excluded_losses
- contract_value_without_utilization

## Easy Example
- `Samsung SDI +6.1% on an ESS contract` is useful Stage 2 evidence, but not Green until delivery, utilization, OPM and FCF confirm.
- `Tesla according to source` is helpful context, but unofficial customer evidence cannot create Green alone.
- `DOE loan guarantee for a solar plant` is Stage 2 at best if component flow and labor execution are not stable.
