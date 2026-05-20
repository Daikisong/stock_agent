# Round 233 R3 Green Gate Review

Do not apply these weights to production scoring yet.

R3 Stage 3-Green is not `battery/ESS/green beneficiary`. It requires actual call-off, volume, utilization, margin, FCF, and risk clearance.

## Required Fields

- binding_contract
- actual_calloff
- gwh_or_tonnage_volume
- utilization_improvement
- opm_or_gross_margin_improvement
- fcf_after_capex
- subsidy_excluded_profit_quality
- customer_ev_strategy_risk_passed
- supply_chain_disruption_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- customer_name_only
- factory_groundbreaking_only
- jv_restructuring_only
- ess_lfp_theme_only
- capacity_conversion_only
- lithium_price_event_only
- ampc_or_subsidy_quality_loss
- ev_demand_slowdown_ignored

## Easy Example
- `5GWh ESS contract` is Stage 2 until ESS revenue, utilization, OPM and FCF confirm.
- `lithium futures +8%` can move materials stocks, but without company call-off and margin it stays event premium.
- `factory groundbreaking` is not Green until orders, utilization and FCF are visible.
