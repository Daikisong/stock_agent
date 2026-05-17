# Round-55 R2 Loop-2 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare EPS revision, revenue guidance, backlog, margin, customer concentration, accounting flags, and price path.
6. Mark accounting trust break, high debt, FCF loss, GPU depreciation, and bottleneck normalization explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `sk_hynix_hbm_rerating_success_case` | `MEMORY_HBM_CAPACITY` | 2026-05-14 | needs_price_backfill |
| `applied_materials_ai_packaging_growth_case` | `SEMI_EQUIPMENT_CAPEX` | 2026-05-14 | needs_price_backfill |
| `nvidia_cowos_l_transition_case` | `ADVANCED_PACKAGING_COWOS_EMIB` | 2025-01-16 | needs_price_backfill |
| `broadcom_optical_pcb_leadtime_case` | `OPTICAL_NETWORKING_AI_DATACENTER` | 2026-03-24 | needs_price_backfill |
| `foxconn_ai_server_rack_growth_case` | `AI_SERVER_ODM_EMS_SUPPLY_CHAIN` | 2026-05-14 | needs_price_backfill |
| `ecolab_coolit_liquid_cooling_case` | `AI_DATA_CENTER_COOLING` | 2026-03-20 | needs_price_backfill |
| `coreweave_openai_contract_ipo_case` | `NEOCLOUD_GPU_RENTAL` | 2025-03-20 | needs_price_backfill |
| `coreweave_downsized_ipo_debt_case` | `NEOCLOUD_GPU_RENTAL` | undated | needs_source_date_and_price_backfill |
| `supermicro_ey_resignation_case` | `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | 2024-10-30 | needs_price_backfill |
| `samsung_ai_boom_labor_execution_case` | `COMMODITY_MEMORY_GENERAL_SEMI` | 2026-05-15 | needs_price_backfill |
| `commodity_memory_price_rebound_case` | `COMMODITY_MEMORY_GENERAL_SEMI` | undated | needs_price_backfill |
| `cxl_glass_substrate_theme_case` | `AI_CHIP_FABRIC_INFRA` | undated | missing_price_data |

## Alignment Labels

- `structural_ai_bottleneck_aligned`: HBM/packaging/optical/cooling bottleneck and EPS/price path align.
- `ai_revenue_but_margin_watch`: AI server revenue grows but margin and working-capital quality are unproven.
- `ai_contract_visibility_but_leverage_risk`: contract visibility exists but leverage and FCF block Green.
- `theme_without_revenue`: technical theme has no customer validation, yield, production, or revenue.
- `hard_4c_accounting_break`: trust evidence breaks the Stage 3 thesis.
