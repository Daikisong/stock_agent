# Round-56 R3 Loop-2 Green Guardrails

| target | posture | Green unlock evidence | Loop-2 penalties |
| --- | --- | --- | --- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT` | REDTEAM_FIRST | contract_quality, price_pass_through, fcf_after_capex, demand_visibility | ev_demand_slowdown, capa_overbuild, contract_cancellation, mineral_price |
| `BATTERY_EQUIPMENT_PARTS` | WATCH_YELLOW_FIRST | customer_order, delivery_schedule, margin_visibility, op_eps_revision | customer_capex_cut, delivery_delay |
| `BATTERY_RECYCLING_ESS_SHIFT` | WATCH_YELLOW_FIRST | ess_contract, capacity_utilization, recycling_volume, metal_recovery_revenue, fcf_margin | ess_margin, recycling_volume, contract_value_missing |
| `EV_INFRASTRUCTURE` | WATCH_YELLOW_FIRST | utilization, recurring_revenue, profitability | utilization, fire_regulation, subsidy_dependency |
| `HYDROGEN_FUEL_CELL_INFRA` | WATCH_YELLOW_FIRST | customer_demand, production_capacity, utilization, op_eps_conversion | customer_absent, utilization, subsidy_dependency |
| `SOLAR_TARIFF_SUPPLYCHAIN` | REDTEAM_FIRST | utilization, customer_contract, supply_chain_stable, fcf_margin | customs, tariff, uflpa, supply_chain_disruption |
| `RENEWABLE_ENERGY_POLICY` | WATCH_YELLOW_FIRST | permitting, funding, cost_schedule, margin_visibility | rates, cost_overrun, permitting, impairment |
| `ENERGY_DISTRIBUTION_FUEL` | WATCH_YELLOW_FIRST | spread_improvement, inventory_status, fcf_margin | energy_price, inventory, policy |
| `WASTE_RECYCLING_ENVIRONMENT` | GREEN_POSSIBLE | permit_asset, treatment_volume, utilization, recurring_fcf | utilization, capex, metal_price |
| `CARBON_CREDIT_CBAM_COMPLIANCE` | WATCH_YELLOW_FIRST | recurring_revenue, verification_customer, cost_pass_through | policy_reform, carbon_price, greenwashing |
| `DATA_CENTER_WATER_REUSE_INFRA` | WATCH_YELLOW_FIRST | data_center_customer, contracted_revenue, unit_economics | customer_absent, local_opposition, economics |
| `EV_FIRE_RISK_OVERLAY` | REDTEAM_FIRST |  | fire, certification, recall, insurance |

## What Not To Change

- Do not apply R3 Loop-2 v2.0 weights to production scoring yet.
- Do not treat EV growth, ESS transition, recycling, hydrogen, solar, or wind labels as Green evidence by themselves.
- Do not invent contract values, margins, utilization, recovery volume, stage prices, or FCF.
- Treat plant idle, contract cancellation, customs detention, wind impairment, lithium crash, and EV fire/certification as RedTeam fields.
