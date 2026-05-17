# Round-55 R2 Loop-2 Green Guardrails

| target | posture | Green unlock evidence | Loop-2 penalties |
| --- | --- | --- | --- |
| `MEMORY_HBM_CAPACITY` | GREEN_POSSIBLE | hbm_demand, capacity_constraint, multi_year_eps_revision, supply_discipline, customer_visibility | crowding, capex_reversal, customer_price_resistance |
| `COMMODITY_MEMORY_GENERAL_SEMI` | WATCH_YELLOW_FIRST | op_eps_revision, supply_discipline, inventory_normalization | spot_rebound, supply_rebound, hbm_lag |
| `SEMI_EQUIPMENT_CAPEX` | WATCH_YELLOW_FIRST | customer_capex, orders, revenue_conversion, op_eps_revision | customer_capex_peak, order_delay, export_control |
| `SEMI_MATERIALS_PROCESS` | WATCH_YELLOW_FIRST | qualification, volume_ramp, margin_visibility | customer_concentration, inventory, price_pressure |
| `ADVANCED_PACKAGING_PCB` | WATCH_YELLOW_FIRST | order_visibility, capacity_constraint, op_eps_revision, pricing_power | customer_concentration, capa_normalization, inventory |
| `ADVANCED_PACKAGING_COWOS_EMIB` | GREEN_POSSIBLE | packaging_bottleneck, revenue_growth, op_eps_revision, customer_visibility | capex_cycle, yield, bottleneck_normalization |
| `DISPLAY_OLED_SUPPLYCHAIN` | WATCH_YELLOW_FIRST | panel_capex_order, volume_ramp, margin_visible | capex_cycle, price_competition, customer_concentration |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR` | WATCH_YELLOW_FIRST | content_growth, customer_diversification, margin_improvement | inventory, customer_concentration, china_supply_chain |
| `AI_CHIP_FABRIC_INFRA` | WATCH_YELLOW_FIRST | design_win, mass_production, revenue_conversion | customer_validation, yield, no_revenue |
| `AI_ACCELERATOR_CHIP_PUREPLAY` | WATCH_YELLOW_FIRST | named_customer, commercial_revenue, gross_margin_visible | nvidia_competition, valuation_overheat, rd_burn |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | WATCH_YELLOW_FIRST | ai_server_revenue_mix, op_eps_revision, margin_stability | low_margin, inventory, accounting, customer_concentration |
| `NEOCLOUD_GPU_RENTAL` | WATCH_YELLOW_FIRST | take_or_pay_backlog, fcf_conversion, debt_stabilization, customer_diversification | high_debt, gpu_depreciation, fcf_negative, customer_concentration |
| `OPTICAL_NETWORKING_AI_DATACENTER` | GREEN_POSSIBLE | hyperscaler_contract, lead_time_extended, op_eps_revision, capacity_constraint | customer_concentration, lead_time_normalization, valuation_crowding |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` | WATCH_YELLOW_FIRST | long_term_supply, contract_duration, fab_ramp, margin_visible | fab_delay, customer_concentration, energy_cost |
| `AI_DATA_CENTER_COOLING` | GREEN_POSSIBLE | data_center_customer, thermal_bottleneck, orders, op_eps_revision | mna_overpay, debt, ai_capex_delay |
| `DATA_CENTER_REIT_INFRASTRUCTURE` | WATCH_YELLOW_FIRST | lease_backlog, funding_cost_visible, cash_yield_growth | capex, funding_cost, tenant_concentration |
| `AI_GRID_FLEXIBILITY_SOFTWARE` | WATCH_YELLOW_FIRST | utility_customer, recurring_revenue, deployment_schedule | poc, commercialization_delay |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | REDTEAM_FIRST |  | auditor_resignation, filing_delay, internal_control_weakness |

## What Not To Change

- Do not apply R2 Loop-2 v2.0 weights to production scoring yet.
- Do not score every AI tag equally.
- Do not treat CXL, glass substrate, AI chip, or neuromorphic keywords as Green evidence without revenue.
- Do not invent contract duration, prepayment, price bands, margins, customer names, stage prices, or FCF.
- Treat high debt, FCF losses, accounting trust breaks, customer concentration, and bottleneck normalization as hard RedTeam fields.
