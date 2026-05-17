# Round-81 R2 Loop-4 Green Guardrails

| target | posture | Green unlock evidence | Loop-4 penalties |
| --- | --- | --- | --- |
| `MEMORY_HBM_CAPACITY` | GREEN_POSSIBLE | hbm_customer_visibility, capacity_constraint, multi_year_eps_revision, price_band_or_prepayment | 4b_crowding, capacity_normalization, customer_price_resistance |
| `HBM_CATCHUP_EXECUTION` | WATCH_YELLOW_FIRST | customer_qualification, volume_shipment, yield_stable, eps_revision | qualification, yield, labor, foundry_execution |
| `AI_STORAGE_NAND_SHORTAGE` | WATCH_YELLOW_FIRST | enterprise_ssd_revenue, nand_profit_growth, op_eps_revision, supply_discipline | nand_cycle_reversal, supply_rebound, 4b_crowding |
| `COMMODITY_MEMORY_GENERAL_SEMI` | WATCH_YELLOW_FIRST | op_eps_revision, supply_discipline, ai_storage_demand | nand_dram_cycle_reversal, supply_rebound |
| `SEMI_EQUIPMENT_AI_CAPEX` | WATCH_YELLOW_FIRST | orders, revenue_conversion, op_eps_revision, customer_capex | customer_capex_peak, order_delay, export_control |
| `SEMI_MATERIALS_PROCESS` | WATCH_YELLOW_FIRST | qualification, volume_ramp, margin_visibility | qualification_delay, customer_concentration, price_pressure |
| `ADVANCED_PACKAGING_COWOS_EMIB` | GREEN_POSSIBLE | packaging_bottleneck, revenue_growth, op_eps_revision, customer_visibility | capacity_normalization, yield, capex_cycle |
| `ADVANCED_PACKAGING_PCB` | WATCH_YELLOW_FIRST | order_visibility, capacity_constraint, op_eps_revision, pricing_power | lead_time_normalization, customer_concentration, inventory |
| `OPTICAL_NETWORKING_AI_DATACENTER` | GREEN_POSSIBLE | hyperscaler_contract, lead_time_extended, op_eps_revision, capacity_constraint | lead_time_normalization, customer_concentration, valuation_crowding |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | WATCH_YELLOW_FIRST | ai_server_revenue_mix, op_eps_revision, margin_stability, inventory_quality | low_margin, consignment, inventory, accounting, customer_concentration |
| `NEOCLOUD_GPU_RENTAL` | WATCH_YELLOW_FIRST | take_or_pay_backlog, fcf_conversion, debt_stabilization, customer_diversification | high_debt, gpu_depreciation, fcf_negative, refinancing, customer_concentration |
| `AI_DATA_CENTER_COOLING` | GREEN_POSSIBLE | data_center_customer, thermal_bottleneck, orders, op_eps_revision | mna_overpay, debt, ai_capex_delay |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` | WATCH_YELLOW_FIRST | long_term_supply, contract_duration, fab_ramp, margin_visible | fab_delay, customer_concentration, energy_cost |
| `AI_CHIP_FABRIC_INFRA` | WATCH_YELLOW_FIRST | customer_validation, mass_production, revenue_conversion | customer_validation_missing, yield, no_revenue |
| `AI_ACCELERATOR_CHIP_PUREPLAY` | WATCH_YELLOW_FIRST | named_customer, commercial_revenue, gross_margin_visible | nvidia_competition, valuation_overheat, rd_burn |
| `DISPLAY_OLED_SUPPLYCHAIN` | WATCH_YELLOW_FIRST | panel_capex_order, volume_ramp, margin_visible | capex_cycle, price_competition, customer_concentration |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR` | WATCH_YELLOW_FIRST | content_growth, customer_diversification, margin_improvement | inventory, customer_concentration, china_supply_chain |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | REDTEAM_FIRST | not_applicable | auditor_resignation, filing_delay, internal_control_weakness |
| `AI_CAPEX_CROWDING_OVERLAY` | REDTEAM_FIRST | not_applicable | crowding, capex_peak, capacity_normalization, revision_slowdown |

## What Not To Change

- Do not apply R2 Loop-4 v4.0 weights to production scoring yet.
- Do not treat all AI beneficiaries as one archetype.
- Do not make CXL, glass substrate, neuromorphic, or AI chip related-stock keywords Green evidence without revenue.
- Do not invent contract value, customer name, duration, prepayment, HBM yield, margin, stage price, or FCF.
- Treat accounting trust break as hard 4C; treat AI CAPEX crowding as a 4B overlay, not a positive score.
