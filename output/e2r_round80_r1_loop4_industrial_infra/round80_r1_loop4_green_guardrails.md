# Round-80 R1 Loop-4 Green Guardrails

| target | posture | Green unlock evidence | Loop-4 penalties |
| --- | --- | --- | --- |
| `GRID_TRANSFORMER_SHORTAGE` | GREEN_POSSIBLE | contract_value, contract_duration, delivery_schedule, backlog_growth, margin_improvement, op_eps_revision | capa_normalization, data_center_delay, low_margin_long_term_contract, project_delay |
| `GRID_MEDIUM_VOLTAGE_EXPANSION` | WATCH_YELLOW_FIRST | medium_voltage_order, switchgear_order, utility_customer, op_eps_revision, margin_visible | capa_normalization, product_mix_unclear, price_normalization |
| `AI_DATA_CENTER_POWER_EQUIPMENT` | GREEN_POSSIBLE | orders, backlog, revenue_guidance, op_eps_revision, margin_visible | project_delay, valuation_crowding, orders_slowdown, grid_interconnection_delay |
| `CONTRACT_BACKLOG_INDUSTRIAL` | GREEN_POSSIBLE | contract_value, contract_duration, counterparty, delivery_schedule, margin_visible, op_eps_revision | contract_quality_unclear, delivery_delay, margin_uncertainty |
| `DEFENSE_GOVERNMENT_BACKLOG` | GREEN_POSSIBLE | government_customer, multi_year_contract, delivery_schedule, backlog_growth, opm_improvement | capital_allocation_shock, dilution, delivery_delay, export_permit_issue |
| `DEFENSE_LOCAL_PRODUCTION_PLATFORM` | WATCH_YELLOW_FIRST | local_production_contract, repeat_customer_demand, delivery_batch, opm_improvement | local_factory_capex, margin_dilution, political_risk, dilution |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK` | REDTEAM_FIRST |  | capital_allocation_shock, dilution, use_of_proceeds_unclear, regulator_revision_request |
| `DEFENSE_UNMANNED_NAVAL_SYSTEMS` | WATCH_YELLOW_FIRST | production_contract, delivery_schedule, military_customer, margin_visible | prototype_only, production_contract_absent, technical_validation_risk |
| `SHIPBUILDING_OFFSHORE_BACKLOG` | GREEN_POSSIBLE | newbuilding_price_up, low_margin_backlog_rolloff, high_margin_delivery_start, op_eps_revision | low_margin_backlog, steel_plate_cost, labor_cost, delivery_delay |
| `SHIPBUILDING_NAVAL_MRO` | WATCH_YELLOW_FIRST | repeat_mro, margin_visible, newbuild_order_or_license, revenue_conversion | mro_option_only, low_margin_mro, legal_restriction |
| `RAIL_INFRASTRUCTURE` | WATCH_YELLOW_FIRST | official_contract, contract_amount_to_sales, delivery_schedule, margin_visible, financing_secured | project_delay, financing, warranty_cost, margin_uncertainty |
| `NUCLEAR_EXISTING_PPA_RESTART` | WATCH_YELLOW_FIRST | signed_ppa, duration, plant_capacity, fcf_visibility, grid_injection_rights | relicense, plant_outage, ppa_economics, restart_capex |
| `NUCLEAR_SMR_GRID_POLICY` | REDTEAM_FIRST | ppa, customer_subscription, cost_confirmed, permit, financing, revenue_visibility | cost_overrun, customer_subscription_failure, financing_failure, project_cancelled |
| `GEOPOLITICAL_RECONSTRUCTION` | WATCH_YELLOW_FIRST | binding_contract, revenue_schedule, financing_visible, margin_visible | policy_to_contract_failed, financing_failure, mou_only |
| `DATA_CENTER_GRID_PERMITTING_OVERLAY` | REDTEAM_FIRST |  | project_delay, permitting_delay, grid_interconnection_delay, moratorium |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` | REDTEAM_FIRST |  | capital_allocation_shock, dilution, capex_burden |

## What Not To Change

- Do not apply R1 Loop-4 v4.0 weights to production scoring yet.
- Do not lower Stage 3-Green thresholds because R1 is Green-capable.
- Do not treat MOU, policy expectation, prototype, or project headline as Green evidence.
- Do not invent contract values, contract dates, counterparties, delivery schedules, margins, or stage prices.
- Treat project delay, capital-allocation shock, low-margin backlog, MRO option-only, and SMR policy false Green as strong penalties.
