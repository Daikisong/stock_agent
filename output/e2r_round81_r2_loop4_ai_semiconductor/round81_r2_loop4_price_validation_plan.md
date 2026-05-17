# Round-81 R2 Loop-4 Price Validation Plan

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
| `samsung_hbm4_shipping_case` | `HBM_CATCHUP_EXECUTION` | 2026-02-12 | needs_price_backfill |
| `samsung_amd_hbm4_mou_case` | `HBM_CATCHUP_EXECUTION` | 2026-03-18 | needs_price_backfill |
| `samsung_labor_strike_execution_case` | `HBM_CATCHUP_EXECUTION` | 2026-05-15 | needs_price_backfill |
| `kioxia_ai_nand_profit_case` | `AI_STORAGE_NAND_SHORTAGE` | 2026-05-15 | needs_price_backfill |
| `applied_materials_ai_packaging_growth_case` | `SEMI_EQUIPMENT_AI_CAPEX` | 2026-05-14 | needs_price_backfill |
| `nvidia_cowos_l_transition_case` | `ADVANCED_PACKAGING_COWOS_EMIB` | 2025-01-16 | needs_price_backfill |
| `broadcom_optical_pcb_leadtime_case` | `OPTICAL_NETWORKING_AI_DATACENTER` | 2026-03-24 | needs_price_backfill |
| `foxconn_ai_server_rack_growth_case` | `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | 2026-05-14 | needs_price_backfill |
| `ecolab_coolit_liquid_cooling_case` | `AI_DATA_CENTER_COOLING` | 2026-03-20 | needs_price_backfill |
| `coreweave_openai_contract_case` | `NEOCLOUD_GPU_RENTAL` | 2025-03-10 | needs_price_backfill |
| `coreweave_expanded_openai_contract_case` | `NEOCLOUD_GPU_RENTAL` | 2025-09-25 | needs_price_backfill |
| `coreweave_downsized_ipo_debt_case` | `NEOCLOUD_GPU_RENTAL` | 2025-03-28 | needs_price_backfill |
| `cerebras_ai_accelerator_ipo_case` | `AI_ACCELERATOR_CHIP_PUREPLAY` | 2026-05-14 | needs_price_backfill |
| `supermicro_ey_resignation_case` | `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | 2024-10-30 | needs_price_backfill |
| `cxl_glass_substrate_theme_case` | `AI_CHIP_FABRIC_INFRA` | undated | missing_price_data |
| `furiosa_ai_related_stock_case` | `AI_ACCELERATOR_CHIP_PUREPLAY` | undated | missing_price_data |
| `ai_capex_crowding_overlay_case` | `AI_CAPEX_CROWDING_OVERLAY` | undated | missing_price_data |

## Alignment Labels

- `hbm_structural_success_but_4b`: HBM evidence and price path align, but rerating may already be crowded.
- `ai_revenue_but_margin_watch`: AI server revenue grows but margin and working capital remain unproven.
- `contract_visibility_but_leverage_risk`: contract visibility exists but leverage and FCF block Green.
- `theme_without_revenue`: technical theme has no customer validation, yield, production, or revenue.
- `accounting_trust_break_4c`: trust evidence breaks the Stage 3 thesis.
