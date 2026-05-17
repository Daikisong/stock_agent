# Round-108 R3 Loop-6 Green Guardrails

| target | posture | Green unlock evidence | Loop-6 penalties |
| --- | --- | --- | --- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT` | REDTEAM_FIRST | contract_quality, price_pass_through, fcf_after_capex, demand_visibility | ev_demand_slowdown, capa_overbuild, contract_cancellation, mineral_price |
| `BATTERY_EQUIPMENT_PARTS` | WATCH_YELLOW_FIRST | customer_order, delivery_schedule, margin_visibility, op_eps_revision | customer_capex_cut, delivery_delay, ev_line_idle |
| `BATTERY_RECYCLING_ESS_SHIFT` | WATCH_YELLOW_FIRST | recycling_volume, metal_recovery_revenue, customer_contract, soh_validation, recurring_fcf | recycling_volume, soh_validation, metal_price, contract_value_missing |
| `SECOND_LIFE_BATTERY_GRID_STORAGE` | WATCH_YELLOW_FIRST | soh_validation, grid_storage_customer, safety_validation, repeat_revenue, fcf_conversion | soh, safety, warranty, residual_capacity |
| `ESS_LFP_GRID_STORAGE` | GREEN_POSSIBLE | ess_contract_value, ess_contract_duration, customer, gwh_volume, ess_margin, fcf_conversion | ess_margin, lfp_competition, customer_concentration, subsidy |
| `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN` | WATCH_YELLOW_FIRST | tesla_customer_confirmed, megapack_use_case, contract_value, contract_duration, lansing_ramp_up, ess_opm, fcf_conversion | lansing_ramp, tesla_concentration, ess_margin, lfp_price, feoc_tariff |
| `ESS_AI_DATA_CENTER_STORAGE` | WATCH_YELLOW_FIRST | data_center_customer, deployment_gwh, storage_margin, fcf_conversion, repeat_revenue | customer_contract_missing, datacenter_capex_delay, safety_regulation |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT` | WATCH_YELLOW_FIRST | storage_customer_contract, converted_line_utilization, ess_opm, fcf_conversion | ev_idle_overhang, conversion_cost, contract_absent, margin_unverified |
| `EV_BATTERY_JV_RESTRUCTURING` | WATCH_YELLOW_FIRST | fixed_cost_reduction, ess_customer_contract, opm_improvement, fcf_conversion | jv_dissolution, operating_loss, fixed_cost, ess_pivot_unproven |
| `EV_CAPA_CONTRACT_CANCELLATION` | REDTEAM_FIRST | not_applicable | contract_cancellation, expected_revenue_loss, ev_demand_slowdown, underutilization, write_down |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` | REDTEAM_FIRST | not_applicable | customer_disclosure, use_case_disclosure, contract_value, margin |
| `EV_INFRASTRUCTURE` | WATCH_YELLOW_FIRST | utilization, recurring_revenue, profitability | utilization, fire_regulation, subsidy_dependency |
| `HYDROGEN_FUEL_CELL_INFRA` | WATCH_YELLOW_FIRST | customer_demand, production_capacity, utilization, op_eps_conversion | customer_absent, utilization, subsidy_dependency, infrastructure_gap |
| `SOLAR_TARIFF_SUPPLYCHAIN` | REDTEAM_FIRST | utilization, customer_contract, supply_chain_stable, fcf_margin | customs, tariff, uflpa, feoc, supply_chain_disruption |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS` | REDTEAM_FIRST | permitting, funding, cost_schedule, margin_visibility | rates, cost_overrun, permitting, impairment |
| `WASTE_RECYCLING_ENVIRONMENT` | GREEN_POSSIBLE | permit_asset, treatment_volume, utilization, recurring_fcf | utilization, capex, metal_price, regulatory_cost |
| `CARBON_CREDIT_CBAM_COMPLIANCE` | WATCH_YELLOW_FIRST | recurring_revenue, verification_customer, cost_pass_through | policy_reform, carbon_price, greenwashing |
| `DATA_CENTER_WATER_REUSE_INFRA` | WATCH_YELLOW_FIRST | data_center_customer, contracted_revenue, unit_economics | customer_absent, local_opposition, economics |
| `EV_FIRE_BESS_SAFETY_OVERLAY` | REDTEAM_FIRST | not_applicable | fire, certification, recall, insurance, permitting |
| `BESS_SAFETY_PERMITTING` | REDTEAM_FIRST | not_applicable | bess_fire, permitting, insurance, local_opposition |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY` | REDTEAM_FIRST | not_applicable | soh, second_life_validation, battery_passport, grading_cost |
| `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY` | WATCH_YELLOW_FIRST | graphite_offtake, customer_contract, cost_path, margin_visible, fcf_conversion | us_cost, policy_financing, offtake, china_price_pressure |
| `LITHIUM_ESS_DEMAND_CYCLE` | WATCH_YELLOW_FIRST | low_cost_structure, long_term_offtake, fcf_defense, capex_discipline | price_crash, mine_restart, sodium_ion, ev_demand_slowdown |
| `SODIUM_ION_SUBSTITUTION_OVERLAY` | REDTEAM_FIRST | not_applicable | substitution, price_ceiling, low_cost_ess |
| `SOLID_STATE_COMMERCIALIZATION_LICENSE` | WATCH_YELLOW_FIRST | mass_production, vehicle_series_adoption, royalty_revenue, yield_cost_visible | commercialization, yield, cost, vehicle_adoption |
| `SPECULATIVE_BATTERY_TECH` | REDTEAM_FIRST | scaled_revenue, commercial_customer, verified_margin, fcf_conversion | commercialization, customer_absent, mass_production, cash_burn |

## What Not To Change

- Do not apply R3 Loop-6 v6.0 weights to production scoring yet.
- Do not treat EV growth, ESS, recycling, hydrogen, solar, wind, or lithium labels as Green evidence by themselves.
- Do not invent contract value, customer, duration, GWh, margin, utilization, recovery volume, SOH, graphite cost, offtake, royalty, stage prices, or FCF.
- Treat customer/use-case nondisclosure, JV dissolution, plant idle, contract cancellation, customs detention, wind impairment, lithium supply rebound, sodium-ion substitution, EV/BESS fire, speculative battery tech, and SOH opacity as RedTeam fields.
