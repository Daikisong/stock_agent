# Round-67 R1 Loop-3 Green Guardrails

| target | posture | Green unlock evidence | Loop-3 penalties |
| --- | --- | --- | --- |
| `GRID_TRANSFORMER_SHORTAGE` | GREEN_POSSIBLE | contract_value, contract_duration, delivery_schedule, backlog_growth, margin_improvement, op_eps_revision | capa_normalization, data_center_delay, low_margin_long_term_contract, project_delay |
| `AI_DATA_CENTER_POWER_EQUIPMENT` | GREEN_POSSIBLE | orders, backlog, revenue_guidance, op_eps_revision, margin_visible | project_delay, valuation_crowding, orders_slowdown |
| `CONTRACT_BACKLOG_INDUSTRIAL` | GREEN_POSSIBLE | contract_value, contract_duration, counterparty, delivery_schedule, margin_visible, op_eps_revision | contract_quality_unclear, delivery_delay, margin_uncertainty |
| `DEFENSE_GOVERNMENT_BACKLOG` | GREEN_POSSIBLE | government_customer, multi_year_contract, delivery_schedule, backlog_growth, opm_improvement | capital_allocation_shock, dilution, delivery_delay, export_permit_issue |
| `DEFENSE_TECH_AUTONOMOUS_SYSTEMS` | WATCH_YELLOW_FIRST | funded_procurement, production_capacity, customer_budget, eps_conversion | prototype, production_delay, valuation_overheat |
| `DEFENSE_DRONE_COUNTER_UAS` | WATCH_YELLOW_FIRST | actual_order, delivery_schedule, production_capacity, repeat_procurement | prototype, export_control, mna_dilution |
| `DEFENSE_AI_SOFTWARE_INTELLIGENCE` | WATCH_YELLOW_FIRST | government_customer, deployment_schedule, recurring_license, gross_margin_visible | prototype, no_repeat_software_revenue, budget_cycle |
| `SHIPBUILDING_OFFSHORE_BACKLOG` | GREEN_POSSIBLE | newbuilding_price_up, low_margin_backlog_rolloff, high_margin_delivery_start, op_eps_revision | low_margin_backlog, steel_plate_cost, labor_cost, delivery_delay |
| `SHIPBUILDING_NAVAL_MRO` | WATCH_YELLOW_FIRST | repeat_mro, margin_visible, newbuild_order_or_license, revenue_conversion | mro_option_only, low_margin_mro, legal_restriction |
| `RAIL_INFRASTRUCTURE` | WATCH_YELLOW_FIRST | official_contract, contract_amount_to_sales, delivery_schedule, margin_visible, financing_secured | project_delay, financing, warranty_cost, margin_uncertainty |
| `NUCLEAR_EXISTING_PPA` | WATCH_YELLOW_FIRST | signed_ppa, duration, plant_capacity, fcf_visibility | relicense, plant_outage, ppa_economics |
| `NUCLEAR_SMR_GRID_POLICY` | REDTEAM_FIRST | ppa, customer_subscription, cost_confirmed, permit, financing, revenue_visibility | cost_overrun, customer_subscription_failure, financing_failure, project_cancelled |
| `GEOPOLITICAL_RECONSTRUCTION` | WATCH_YELLOW_FIRST | binding_contract, revenue_schedule, financing_visible, margin_visible | policy_to_contract_failed, financing_failure, mou_only |
| `SMART_FACTORY_AUTOMATION` | WATCH_YELLOW_FIRST | actual_order, installed_base, recurring_revenue, opm_improvement | mou_only, poc_only, customer_capex_delay |
| `PROJECT_DELAY_CAPEX_OVERLAY` | REDTEAM_FIRST |  | project_delay, permitting_delay, capex_burden |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` | REDTEAM_FIRST |  | capital_allocation_shock, dilution, capex_burden |

## What Not To Change

- Do not apply R1 Loop-3 v3.0 weights to production scoring yet.
- Do not lower Stage 3-Green thresholds because R1 is Green-capable.
- Do not treat MOU, policy expectation, prototype, or project headline as Green evidence.
- Do not invent contract values, contract dates, counterparties, delivery schedules, margins, or stage prices.
- Treat project delay, capital-allocation shock, low-margin backlog, MRO option-only, and SMR policy false Green as strong penalties.
