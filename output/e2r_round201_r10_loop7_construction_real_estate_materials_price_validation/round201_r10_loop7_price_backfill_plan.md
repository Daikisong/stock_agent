# Round-201 R10 Loop-7 Price Backfill Plan

## Required Fields

- `stage1_date`
- `stage2_date`
- `stage3_date`
- `stage4b_date`
- `stage4c_date`
- `stage1_price`
- `stage2_price`
- `stage3_price`
- `stage4b_price`
- `stage4c_price`
- `peak_date`
- `peak_price`
- `MFE_5D`
- `MFE_20D`
- `MFE_30D`
- `MFE_60D`
- `MFE_90D`
- `MFE_180D`
- `MFE_1Y`
- `MFE_2Y`
- `MAE_5D`
- `MAE_20D`
- `MAE_30D`
- `MAE_60D`
- `MAE_90D`
- `MAE_180D`
- `MAE_1Y`
- `MAE_2Y`
- `drawdown_after_peak`
- `relative_strength_vs_kospi`
- `relative_strength_vs_construction_basket`
- `relative_strength_vs_reit_basket`
- `relative_strength_vs_building_materials_basket`
- `relative_strength_vs_data_center_real_asset_basket`
- `contract_size`
- `epc_margin_visibility`
- `project_cost_control`
- `progress_revenue`
- `cash_collection`
- `working_capital`
- `pf_exposure`
- `pf_delinquency`
- `funding_cost`
- `unsold_inventory`
- `construction_cost_ratio`
- `tenant_contract_quality`
- `occupancy`
- `noi_affo`
- `capex_per_share`
- `power_water_permitting`
- `safety_quality_incident_flag`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `samsung_ea_fadhili_epc_backlog_stage2_watch` | 2024-04-03 | needs_ohlc_backfill | `watch` | false |
| `hyundai_ec_jafurah_gas_infra_stage2_watch` | 2024-06-30 | needs_ohlc_backfill | `watch` | false |
| `daewoo_ec_grand_faw_handover_stage2_watch` | 2024-11-12 | needs_ohlc_backfill | `watch` | false |
| `taeyoung_pf_workout_credit_hard_4c` | 2023-12-01 | needs_ohlc_backfill | `none` | true |
| `hdc_hyundai_development_apartment_collapse_hard_4c` | 2022-01-11 | needs_ohlc_backfill | `none` | true |
| `posco_ec_dl_construction_workplace_safety_4c_watch` | 2025-09-15 | needs_ohlc_backfill | `watch` | false |
| `sk_aws_ulsan_ai_data_center_real_asset_insufficient_evidence` | 2026-02-11 | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split EPC award, handover, PF workout, safety accident, data-center announcement, and permitting dates.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
