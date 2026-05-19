# Round-196 R5 Loop-7 Price Backfill Plan

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
- `relative_strength_vs_consumer_basket`
- `relative_strength_vs_kbeauty_basket`
- `relative_strength_vs_kfood_basket`
- `repeat_purchase_evidence`
- `overseas_sales_mix`
- `us_sales_mix`
- `channel_sell_through`
- `repeat_order`
- `opm_improvement`
- `eps_revision`
- `fcf_conversion`
- `inventory_days`
- `receivables_days`
- `asp_or_product_mix`
- `single_sku_dependence`
- `retail_talks_without_sell_through_flag`
- `ipo_first_month_rally_flag`
- `mna_event_premium_flag`
- `holdco_or_private_link_cap_flag`
- `tariff_margin_uncertainty_flag`
- `food_safety_or_recall_flag`
- `stage4b_status`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `nongshim_shin_ramyun_global_staple_stage2_watch` | 2024-05-27 | needs_ohlc_backfill | `none` | false |
| `apr_medicube_beauty_device_structural_success_4b_watch` | 2025-10-20 | needs_ohlc_backfill | `watch` | false |
| `dalba_global_us_retail_talks_ipo_overheat_watch` | 2025-06-05 | needs_ohlc_backfill | `watch` | false |
| `cosmax_kolmar_fast_beauty_odm_supply_chain_stage2_watch` | 2025-06-05 | needs_ohlc_backfill | `none` | false |
| `amorepacific_legacy_kbeauty_china_to_us_transition_watch` | 2025-06-05 | needs_ohlc_backfill | `none` | false |
| `cj_olive_young_private_platform_holdco_cap_stage2_watch` | 2025-06-05 | needs_ohlc_backfill | `watch` | false |
| `fnf_taylormade_mna_event_premium_not_brand_rerating` | 2025-07-21 | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split retail-talks, IPO, M&A, and holdco premium price paths from structural consumer evidence.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
