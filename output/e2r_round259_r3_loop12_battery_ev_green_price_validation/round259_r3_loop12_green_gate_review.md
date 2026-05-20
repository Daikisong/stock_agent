# Round 259 R3 Green Gate Review

Do not apply these weights to production scoring yet.

R3 Stage 3-Green requires the contract or plant story to close into actual call-off, GWh, delivery, utilization, OPM, FCF, and cleared customs/visa/labor risks.

## Required Fields

- actual_calloff_or_take_or_pay_confirmed
- gwh_volume_and_supply_period_confirmed
- delivery_or_revenue_recognition_started
- utilization_improvement
- opm_or_gross_margin_confirmed
- fcf_after_capex_confirmed
- subsidy_excluded_unit_economics_confirmed
- customs_visa_labor_supply_chain_flow_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- ev_jv_headline_only
- us_localization_capex_only
- ess_pivot_only
- hydrogen_plant_only
- silicon_anode_optionality_only
- solar_loan_guarantee_only
- share_issuance_for_capex_without_demand_quality
- contract_cancellation_present
- customs_detention_present
- factory_startup_delay_present

## Easy Example
- `LGES Ford/Freudenberg cancellation` is hard 4C because expected revenue disappears.
- `SK On Flatiron ESS 7.2GWh` is Stage 2 until contract value, utilization, OPM and FCF are known.
- `Qcells DOE loan guarantee` is not Green if customs detention cuts production flow.
