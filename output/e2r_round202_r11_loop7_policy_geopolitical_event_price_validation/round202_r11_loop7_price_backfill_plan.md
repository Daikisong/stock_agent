# Round-202 R11 Loop-7 Price Backfill Plan

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
- `relative_strength_vs_policy_event_basket`
- `relative_strength_vs_resource_discovery_basket`
- `relative_strength_vs_nuclear_smr_basket`
- `relative_strength_vs_poultry_basket`
- `relative_strength_vs_speculative_science_basket`
- `event_volume_spike`
- `event_turnover_spike`
- `contract_amount`
- `funded_budget`
- `financing_secured`
- `actual_order`
- `revenue_conversion`
- `eps_fcf_revision`
- `drilling_result`
- `commerciality_confirmed`
- `replication_result`
- `import_restriction_status`
- `policy_reversal_flag`
- `macro_fx_shock`
- `foreign_outflow`
- `liquidity_support`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `kogas_east_sea_resource_discovery_event_premium` | 2024-06-03 | needs_ohlc_backfill | `watch` | false |
| `doosan_enerbility_nuclear_smr_policy_to_contract_watch` | 2025-08-26 | needs_ohlc_backfill | `watch` | false |
| `hdhyundai_samsungheavy_us_shipbuilding_policy_mou_watch` | 2025-08-26 | needs_ohlc_backfill | `watch` | false |
| `poultry_basket_brazil_bird_flu_import_ban_event_fade` | 2025-05-19 | needs_ohlc_backfill | `watch` | false |
| `lk99_superconductor_speculative_science_thesis_break` | 2023-08-01 | needs_ohlc_backfill | `elevated` | true |
| `korea_martial_law_policy_market_shock_overlay` | 2024-12-04 | needs_ohlc_backfill | `none` | false |
| `short_selling_msci_market_structure_stage2_watch` | 2025-06-20 | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- R11 needs short-window MFE/MAE: 5D, 20D, and 60D matter because event fade can be fast.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split event date, contract date, failure/reversal date, and market-shock date.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
