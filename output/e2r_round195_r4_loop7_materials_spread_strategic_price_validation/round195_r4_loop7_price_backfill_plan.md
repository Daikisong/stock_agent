# Round-195 R4 Loop-7 Price Backfill Plan

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
- `MFE_90D`
- `MFE_180D`
- `MFE_1Y`
- `MFE_2Y`
- `MAE_5D`
- `MAE_20D`
- `MAE_30D`
- `MAE_90D`
- `MAE_180D`
- `MAE_1Y`
- `MAE_2Y`
- `drawdown_after_peak`
- `relative_strength_vs_kospi`
- `relative_strength_vs_refining_basket`
- `relative_strength_vs_petrochemical_basket`
- `relative_strength_vs_strategic_metals_basket`
- `actual_product_spread`
- `crack_spread`
- `naphtha_ethylene_spread`
- `operating_rate`
- `capacity_shutdown_confirmed`
- `supply_discipline_confirmed`
- `inventory_normalization`
- `working_capital_cashflow`
- `fcf_after_working_capital`
- `price_floor_or_offtake`
- `cost_curve_advantage`
- `capex_commitment`
- `dilution_or_share_issuance_flag`
- `tender_offer_or_governance_premium_flag`
- `unconfirmed_media_report_flag`
- `commodity_price_event_flag`
- `stage4b_status`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `lotte_chemical_petrochemical_loss_restructuring_watch` | 2025-11-26 | needs_ohlc_backfill | `watch` | true |
| `lg_chem_petrochemical_spread_failed_rerating_watch` | 2025-12-19 | needs_ohlc_backfill | `none` | false |
| `sk_innovation_refining_margin_cyclical_success_not_structural` | 2026-05-13 | needs_ohlc_backfill | `watch` | false |
| `korea_zinc_governance_event_vs_critical_minerals_stage2` | 2025-12-15 | needs_ohlc_backfill | `watch` | false |
| `posco_holdings_lithium_resource_security_cycle_watch` | 2025-11-11 | needs_ohlc_backfill | `watch` | false |
| `oci_holdings_spacex_polysilicon_unconfirmed_event_premium` | 2026-04-14 | needs_ohlc_backfill | `watch` | false |
| `poongsan_copper_defense_sale_rumor_event_break` | 2026-04-09 | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split event-premium price paths from structural Stage 2 price paths.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
