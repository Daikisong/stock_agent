# Round-194 R3 Loop-7 Price Backfill Plan

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
- `MFE_30D`
- `MFE_90D`
- `MFE_180D`
- `MFE_1Y`
- `MFE_2Y`
- `MAE_30D`
- `MAE_90D`
- `MAE_180D`
- `MAE_1Y`
- `MAE_2Y`
- `drawdown_after_peak`
- `relative_strength_vs_kospi`
- `relative_strength_vs_battery_materials_basket`
- `relative_strength_vs_ess_basket`
- `relative_strength_vs_ev_battery_basket`
- `contract_binding_quality`
- `gwh_volume_visibility`
- `customer_order_calloff`
- `take_or_pay_flag`
- `shipment_evidence`
- `utilization_rate`
- `opm_margin_visibility`
- `fcf_after_capex`
- `eps_fcf_revision`
- `ess_revenue_conversion`
- `ev_demand_durability`
- `customer_quality`
- `tax_credit_quality`
- `ampc_dependency`
- `operating_profit_ex_ampc`
- `capa_announcement_flag`
- `contract_value_without_actual_order_flag`
- `unconfirmed_media_report_flag`
- `lithium_price_event_flag`
- `ipo_theme_premium_flag`
- `group_vertical_integration_story_flag`
- `inventory_or_receivables_risk`
- `stage4b_status`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `lg_energy_solution_ess_lfp_stage2_ev_contract_4c_watch` | 2025-07-30 | needs_ohlc_backfill | `watch` | false |
| `lnf_tesla_cathode_contract_value_reduction_hard_4c` | 2025-12-29 | needs_ohlc_backfill | `elevated` | true |
| `sk_innovation_sk_on_ev_thesis_break_ess_pivot_watch` | 2025-09-03 | needs_ohlc_backfill | `none` | false |
| `samsung_sdi_tesla_ess_unconfirmed_stage1_only` | 2025-03-05 | needs_ohlc_backfill | `watch` | false |
| `sk_iet_separator_ev_demand_cycle_4c_watch` | 2024-05-15 | needs_ohlc_backfill | `elevated` | false |
| `posco_future_m_lithium_event_and_ford_shock_false_green_guard` | 2025-12-16 | needs_ohlc_backfill | `watch` | false |
| `ecopro_materials_precursor_ipo_theme_overheat_guard` | 2025-12-16 | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
