# Round-107 R2 Loop-6 Green Guardrails

| target | posture | Green unlock evidence | Loop-6 penalties |
| --- | --- | --- | --- |
| `MEMORY_HBM_CAPACITY` | GREEN_POSSIBLE | hbm_customer_visibility, capacity_constraint, multi_year_eps_revision, price_band_or_prepayment | 4b_crowding, capacity_normalization, customer_price_resistance |
| `MEMORY_HBM_LTA_PREPAYMENT` | GREEN_POSSIBLE | hbm_lta_flag, hbm_price_band_flag, prepayment_flag, capacity_reservation_flag, multi_year_eps_revision | contract_binding_quality, prepayment_quality, capacity_reservation, customer_concentration |
| `HBM_CATCHUP_EXECUTION` | WATCH_YELLOW_FIRST | customer_qualification, volume_shipment, yield_stable, eps_revision | qualification, yield, labor, foundry_execution |
| `MEMORY_SUPPLY_REALLOCATION` | WATCH_YELLOW_FIRST | strategic_customer_allocation_flag, capacity_reallocation_flag, op_eps_revision, mix_improvement | consumer_demand_destruction, ai_capex_slowdown, supply_normalization |
| `AI_STORAGE_NAND_SHORTAGE` | WATCH_YELLOW_FIRST | enterprise_ssd_revenue, nand_profit_growth, op_eps_revision, supply_discipline | nand_cycle_reversal, supply_rebound, 4b_crowding |
| `COMMODITY_MEMORY_GENERAL_SEMI` | WATCH_YELLOW_FIRST | op_eps_revision, supply_discipline, ai_storage_demand | nand_dram_cycle_reversal, supply_rebound |
| `SEMI_EQUIPMENT_AI_CAPEX` | WATCH_YELLOW_FIRST | orders, revenue_conversion, op_eps_revision, customer_capex | customer_capex_peak, order_delay, export_control |
| `SEMI_MATERIALS_PROCESS` | WATCH_YELLOW_FIRST | qualification, volume_ramp, margin_visibility | qualification_delay, customer_concentration, price_pressure |
| `CUSTOM_AI_ASIC_HYPERSCALER` | GREEN_POSSIBLE | named_hyperscaler_customer, custom_ai_asic_revenue, capacity_secured, margin_visible | customer_concentration, margin, startup_credit, capacity |
| `CUSTOM_AI_ASIC_MARGIN_CONCENTRATION` | REDTEAM_FIRST | not_applicable | customer_concentration, margin, startup_credit, project_delay |
| `ADVANCED_PACKAGING_COWOS_EMIB` | GREEN_POSSIBLE | packaging_bottleneck, revenue_growth, op_eps_revision, customer_visibility | capacity_normalization, yield, capex_cycle |
| `ADVANCED_PACKAGING_PCB` | WATCH_YELLOW_FIRST | order_visibility, capacity_constraint, op_eps_revision, pricing_power | lead_time_normalization, customer_concentration, inventory |
| `OPTICAL_NETWORKING_AI_DATACENTER` | GREEN_POSSIBLE | hyperscaler_contract, lead_time_extended, op_eps_revision, capacity_constraint | lead_time_normalization, customer_concentration, valuation_crowding |
| `AI_NETWORKING_SWITCHING_INFRA` | WATCH_YELLOW_FIRST | ai_networking_orders, guidance_raise, opm_conversion, fcf_conversion | hyperscaler_concentration, legacy_mix, restructuring, order_delay |
| `PHOTONICS_AI_DATACENTER_CHIPS` | WATCH_YELLOW_FIRST | contract_value, delivery_schedule, revenue_recognition, margin_visible | customer_concentration, delivery_delay, yield, margin_unverified |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | WATCH_YELLOW_FIRST | ai_server_revenue_mix, op_eps_revision, margin_stability, inventory_quality | low_margin, consignment, inventory, accounting, customer_concentration |
| `NEOCLOUD_GPU_RENTAL` | WATCH_YELLOW_FIRST | take_or_pay_backlog, fcf_conversion, debt_stabilization, customer_diversification | high_debt, gpu_depreciation, fcf_negative, refinancing, customer_concentration |
| `AI_DATA_CENTER_COOLING` | GREEN_POSSIBLE | data_center_customer, thermal_bottleneck, orders, op_eps_revision | mna_overpay, debt, ai_capex_delay |
| `AI_CHIP_FABRIC_INFRA` | WATCH_YELLOW_FIRST | customer_validation, mass_production, revenue_conversion | customer_validation_missing, yield, no_revenue |
| `AI_ACCELERATOR_CHIP_PUREPLAY` | WATCH_YELLOW_FIRST | named_customer, commercial_revenue, gross_margin_visible | nvidia_competition, valuation_overheat, rd_burn |
| `DISPLAY_OLED_SUPPLYCHAIN` | WATCH_YELLOW_FIRST | panel_capex_order, volume_ramp, margin_visible | capex_cycle, price_competition, customer_concentration |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR` | WATCH_YELLOW_FIRST | content_growth, customer_diversification, margin_improvement | inventory, customer_concentration, china_supply_chain |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | REDTEAM_FIRST | not_applicable | auditor_resignation, filing_delay, internal_control_weakness |
| `AI_CAPEX_CROWDING_OVERLAY` | REDTEAM_FIRST | not_applicable | crowding, capex_peak, capacity_normalization, revision_slowdown |
| `CIRCULAR_AI_FINANCING_OVERLAY` | REDTEAM_FIRST | not_applicable | circular_financing, capacity_guarantee, refinancing, customer_supplier_overlap |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST | not_applicable | detail_missing, amount_missing, counterparty_missing, duration_missing, margin_missing |

## What Not To Change

- Do not apply R2 Loop-6 v6.0 weights to production scoring yet.
- Do not treat all AI beneficiaries as one archetype.
- Do not treat HBM LTA, custom ASIC, AI server ODM, neocloud, and theme-only AI chips as the same evidence type.
- Do not make CXL, glass substrate, neuromorphic, or AI chip related-stock keywords Green evidence without revenue.
- Do not invent contract value, customer name, duration, prepayment, HBM yield, custom ASIC margin, stage price, or FCF.
- Treat accounting trust break as hard 4C; treat AI CAPEX crowding as a 4B overlay, not a positive score.
