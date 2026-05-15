# Round-42 R2 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `MEMORY_HBM_CAPACITY` | GREEN_POSSIBLE | hbm_demand, capacity_constraint, multi_year_eps_revision, supply_discipline, customer_visibility | crowding, capex_reversal, customer_price_resistance, memory_price_decline |
| `COMMODITY_MEMORY_GENERAL_SEMI` | WATCH_YELLOW_FIRST | op_eps_revision, supply_discipline, inventory_normalization | pure_cyclical_bounce, hbm_lag, supply_rebound |
| `SEMI_EQUIPMENT_CAPEX` | WATCH_YELLOW_FIRST | customer_capex, orders, revenue_conversion, op_eps_revision | order_pushout, export_control, customer_concentration |
| `SEMI_MATERIALS_PROCESS` | WATCH_YELLOW_FIRST | qualification, volume_ramp, margin_visibility | qualification_delay, single_customer, price_pressure |
| `ADVANCED_PACKAGING_PCB` | WATCH_YELLOW_FIRST | order_visibility, capacity_constraint, op_eps_revision, pricing_power | capa_normalization, theme_without_order, customer_delay |
| `ADVANCED_PACKAGING_COWOS_EMIB` | GREEN_POSSIBLE | packaging_bottleneck, revenue_growth, op_eps_revision, customer_visibility | capa_expansion, yield_issue, bottleneck_easing |
| `DISPLAY_OLED_SUPPLYCHAIN` | WATCH_YELLOW_FIRST | panel_capex_order, volume_ramp, margin_visible | capex_cycle, single_customer, panel_delay |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR` | WATCH_YELLOW_FIRST | content_growth, customer_diversification, margin_improvement | smartphone_cycle_only, inventory_build, asp_pressure |
| `AI_CHIP_FABRIC_INFRA` | WATCH_YELLOW_FIRST | design_win, mass_production, revenue_conversion | mou_only, no_revenue, yield_issue |
| `AI_ACCELERATOR_CHIP_PUREPLAY` | WATCH_YELLOW_FIRST | named_customer, commercial_revenue, gross_margin_visible | valuation_overheat, no_revenue, funding_need |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | WATCH_YELLOW_FIRST | ai_server_revenue_mix, op_eps_revision, margin_stability | accounting_issue, low_margin, inventory_build, customer_concentration |
| `NEOCLOUD_GPU_RENTAL` | WATCH_YELLOW_FIRST | take_or_pay_backlog, fcf_conversion, debt_stabilization | high_debt, fcf_negative, gpu_obsolescence, customer_concentration |
| `OPTICAL_NETWORKING_AI_DATACENTER` | GREEN_POSSIBLE | hyperscaler_contract, lead_time_extended, op_eps_revision, capacity_constraint | capa_normalization, customer_capex_delay, order_cancellation |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` | WATCH_YELLOW_FIRST | long_term_supply, contract_duration, fab_ramp, margin_visible | fab_delay, capex_cut, low_margin_contract |
| `AI_DATA_CENTER_COOLING` | GREEN_POSSIBLE | data_center_customer, thermal_bottleneck, orders, op_eps_revision | customer_capex_delay, technology_substitution, margin_miss |
| `DATA_CENTER_REIT_INFRASTRUCTURE` | WATCH_YELLOW_FIRST | lease_backlog, funding_cost_visible, cash_yield_growth | funding_cost, power_constraint, flat_ipo |
| `AI_GRID_FLEXIBILITY_SOFTWARE` | WATCH_YELLOW_FIRST | utility_customer, recurring_revenue, deployment_schedule | pilot_only, regulatory_delay, no_recurring_revenue |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | REDTEAM_FIRST | not applicable | auditor_resignation, filing_delay, internal_control_weakness, related_party_transaction |

## What Not To Change

- Do not apply these R2 v1.0 weights to production scoring yet.
- Do not treat AI, HBM, CXL, glass substrate, or neocloud labels as score evidence by themselves.
- Do not invent revenue, EPS, FCF, capacity, order, customer, margin, accounting, or price-path fields.
- Do not loosen Stage 3-Green to catch AI themes. Green still requires cross-evidence and low RedTeam risk.
- Treat auditor resignation, filing delay, internal-control weakness, and related-party trust issues as hard RedTeam evidence.
