# Round-121 R2 Loop-7 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare EPS revision, guidance, backlog, margin, customer concentration, accounting flags, and price path.
6. Mark HBM 4B, commodity-memory cycle reversal, neocloud leverage, accounting trust break, and theme-only AI explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `sk_hynix_hbm_trillion_case` | `MEMORY_HBM_CAPACITY` | 2026-05-14 | needs_price_backfill |
| `sk_hynix_record_profit_buyback_case` | `MEMORY_HBM_LTA_PREPAYMENT` | 2026-01-28 | needs_price_backfill |
| `samsung_hbm4_shipping_case` | `HBM_CATCHUP_EXECUTION` | 2026-02-12 | needs_price_backfill |
| `samsung_amd_hbm4_mou_case` | `HBM_CATCHUP_EXECUTION` | 2026-03-18 | needs_price_backfill |
| `samsung_labor_strike_execution_case` | `HBM_CATCHUP_EXECUTION_RISK` | 2026-05-15 | needs_price_backfill |
| `micron_consumer_memory_exit_case` | `MEMORY_SUPPLY_REALLOCATION` | 2025-12-03 | needs_price_backfill |
| `kioxia_ai_nand_profit_case` | `AI_STORAGE_NAND_SHORTAGE` | 2026-05-15 | needs_price_backfill |
| `applied_materials_ai_packaging_growth_case` | `SEMI_EQUIPMENT_AI_CAPEX` | 2026-05-14 | needs_price_backfill |
| `broadcom_custom_ai_asic_100b_case` | `CUSTOM_AI_ASIC_HYPERSCALER` | 2026-03-04 | needs_price_backfill |
| `broadcom_custom_ai_margin_concentration_case` | `CUSTOM_AI_ASIC_MARGIN_CONCENTRATION` | 2026-03-04 | missing_price_data |
| `nvidia_cowos_l_transition_case` | `ADVANCED_PACKAGING_COWOS_EMIB` | 2025-01-16 | needs_price_backfill |
| `broadcom_optical_pcb_leadtime_case` | `OPTICAL_NETWORKING_AI_DATACENTER` | 2026-03-24 | needs_price_backfill |
| `cisco_ai_networking_orders_case` | `AI_NETWORKING_SWITCHING_INFRA` | 2026-05-13 | needs_price_backfill |
| `tower_photonics_ai_datacenter_deal_case` | `PHOTONICS_AI_DATACENTER_CHIPS` | 2026-05-13 | needs_price_backfill |
| `foxconn_ai_server_rack_growth_case` | `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | 2026-05-14 | needs_price_backfill |
| `ecolab_coolit_liquid_cooling_case` | `AI_DATA_CENTER_COOLING` | 2026-03-20 | needs_price_backfill |
| `coreweave_openai_contract_case` | `NEOCLOUD_GPU_RENTAL` | 2025-03-10 | needs_price_backfill |
| `coreweave_expanded_openai_contract_case` | `NEOCLOUD_GPU_RENTAL` | 2025-09-25 | needs_price_backfill |
| `coreweave_nvidia_circular_financing_case` | `CIRCULAR_AI_FINANCING_OVERLAY` | 2026-05-13 | needs_price_backfill |
| `cerebras_ai_accelerator_ipo_case` | `AI_ACCELERATOR_CHIP_PUREPLAY` | 2026-05-14 | needs_price_backfill |
| `supermicro_ey_resignation_case` | `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | 2024-10-30 | needs_price_backfill |
| `cxl_glass_substrate_theme_case` | `AI_CHIP_FABRIC_INFRA` | undated | missing_price_data |
| `furiosa_ai_related_stock_case` | `AI_ACCELERATOR_CHIP_PUREPLAY` | undated | missing_price_data |
| `ai_capex_crowding_overlay_case` | `AI_CAPEX_CROWDING_OVERLAY` | undated | missing_price_data |

## Alignment Labels

- `hbm_structural_success_but_4b`: HBM evidence and price path align, but rerating may already be crowded.
- `hbm_lta_prepayment_confirmed`: long-term agreements, price bands, prepayment, and capacity reservation increase visibility but still need price-path validation.
- `memory_supply_reallocation_aligned`: capacity shift from consumer memory toward AI/HBM/enterprise demand must show mix and EPS improvement.
- `custom_ai_asic_aligned`: hyperscaler custom ASIC demand must show named customer, capacity, margin, and repeat revenue.
- `custom_ai_asic_margin_concentration_watch`: customer concentration or margin pressure is a RedTeam gate, not a positive score.
- `ai_revenue_but_margin_watch`: AI server revenue grows but margin and working capital remain unproven.
- `AI_NETWORKING_ORDER_ALIGNED`: AI networking/switching orders align only after revenue, margin, and repeat customer proof.
- `PHOTONICS_CONTRACT_STAGE2`: AI photonics deal is Stage 2 before revenue recognition and customer diversification.
- `contract_visibility_but_leverage_risk`: contract visibility exists but leverage and FCF block Green.
- `CIRCULAR_AI_FINANCING_WATCH`: circular supplier/customer/investor structures are RedTeam overlays, not clean demand proof.
- `theme_without_revenue`: technical theme has no customer validation, yield, production, or revenue.
- `accounting_trust_break_4c`: trust evidence breaks the Stage 3 thesis.
