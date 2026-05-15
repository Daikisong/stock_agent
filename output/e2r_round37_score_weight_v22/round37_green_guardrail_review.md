# Round-37 Green Guardrail Review

| target | posture | validation_group | Green unlock evidence | Red flags |
|---|---|---|---|---|
| DEFENSE_TECH_AUTONOMOUS_SYSTEMS | GREEN_POSSIBLE | backlog_contract | government_framework, procurement_quantity, production_capacity, delivery_schedule, op_eps_revision | program_delay, procurement_uncertainty, valuation_overheat, export_control, prototype_only |
| INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA | GREEN_POSSIBLE | utility_like_infra | long_term_supply_contract, onsite_gas_plant, take_or_pay, advanced_memory_fab, fab_ramp_schedule | fab_delay, customer_concentration, energy_cost, contract_terms, theme_only |
| COLD_CHAIN_REIT_LOGISTICS | WATCH_YELLOW_FIRST | reit_utility_like | occupancy, long_term_tenant_contract, noi_affo_growth, energy_cost_control | energy_cost, occupancy, funding_cost, capex, tenant_concentration, ipo_event_only |
| DATA_CENTER_WATER_REUSE_INFRA | WATCH_YELLOW_FIRST | infra_utility_like | datacenter_customer, water_reuse_contract, water_savings_metric, recurring_service_revenue | permitting, local_opposition, project_economics, policy_dependency, no_customer |
| SATELLITE_CONNECTIVITY_INFRA | WATCH_YELLOW_FIRST | software_recurring | recurring_service_revenue, airline_or_defense_contract, backlog_growth, ebitda_margin | launch_delay, capex_debt, customer_concentration, constellation_competition, spacex_theme_only |
| DEFENSE_AI_SOFTWARE_INTELLIGENCE | GREEN_POSSIBLE | software_recurring | government_software_contract, program_of_record, recurring_license, gross_margin_visible | procurement_delay, ethical_regulation, customer_concentration, budget_cycle, prototype_only |
| AI_DATA_CENTER_POWER_EQUIPMENT | GREEN_POSSIBLE | backlog_contract | bookings_growth, backlog_growth, direct_datacenter_customer, op_margin_improvement | ai_capex_delay, low_margin_project, supply_chain, bookings_slowdown, theme_only |
| DEFENSE_DRONE_COUNTER_UAS | GREEN_POSSIBLE | backlog_contract | military_delivery_contract, idiq_framework, production_capacity, backlog_growth, op_eps_revision | production_capacity, mna_dilution, export_control, program_delay, prototype_only |

## What Not To Change
- Do not apply v2.2 weights to production scoring yet.
- Do not use case IDs, theme labels, private valuations, prototypes, or SpaceX/AI/defense labels as candidate-generation input.
- Do not invent stage dates, prices, contract terms, backlog, AFFO, water savings, recurring revenue, or program renewals.
- Do not lower Stage 3-Green thresholds to improve recall.
