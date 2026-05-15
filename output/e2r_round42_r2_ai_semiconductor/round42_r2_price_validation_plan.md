# Round-42 R2 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Calculate peak price, drawdown after peak, and below-stage3 flag.
6. Compare price paths with revenue/OP/EPS revision, margin, inventory, CAPEX, customer concentration, debt, and accounting red flags.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `sk_hynix_hbm_rerating_success_case` | 2026-05-14 | needs_price_backfill |
| `sk_hynix_asml_euv_capex_case` | 2026-03-24 | needs_price_backfill |
| `applied_materials_ai_packaging_growth_case` | 2026-05-14 | needs_price_backfill |
| `nvidia_cowos_l_packaging_bottleneck_case` | 2025-01-16 | needs_price_backfill |
| `broadcom_optical_pcb_leadtime_case` | 2026-03-24 | needs_price_backfill |
| `meta_corning_fiber_contract_case` | 2026-01-27 | needs_price_backfill |
| `tower_semiconductor_ai_light_chip_deal_case` | 2026-05-13 | needs_price_backfill |
| `air_liquide_micron_gas_plant_case` | 2024-06-05 | needs_price_backfill |
| `ecolab_coolit_liquid_cooling_case` | 2026-03-20 | needs_price_backfill |
| `coreweave_neocloud_high_debt_case` | needs_source_date | needs_source_date_and_price_backfill |
| `blackstone_data_center_reit_case` | 2026-05-14 | needs_price_backfill |
| `supermicro_ey_resignation_4c_case` | 2024-10-30 | needs_price_backfill |
| `samsung_commodity_memory_recovery_case` | needs_source_date | needs_source_date_and_price_backfill |
| `advanced_packaging_capacity_normalization_4b_watch` | needs_source_date | missing_price_data |
| `neocloud_debt_fcf_breakdown_4c_watch` | needs_source_date | missing_price_data |

## Alignment Labels

- `aligned`: Stage 2/3 evidence and price rerating persist together.
- `cyclical_success`: price worked, but structural EPS persistence is not yet proven.
- `overheat`: valuation/theme pressure is high enough that Green should be restricted.
- `false_positive_score`: theme or revenue looked strong, but margin/EPS/trust/price validation failed.
- `thesis_break`: accounting, filing, internal-control, order, debt, or FCF failure damages the thesis.
