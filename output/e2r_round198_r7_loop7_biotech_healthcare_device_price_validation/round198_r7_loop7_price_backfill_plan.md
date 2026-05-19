# Round-198 R7 Loop-7 Price Backfill Plan

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
- `relative_strength_vs_biotech_basket`
- `relative_strength_vs_cdmo_basket`
- `relative_strength_vs_medical_device_basket`
- `approval_date`
- `commercial_launch_date`
- `prescription_volume`
- `reimbursement_status`
- `commercial_revenue`
- `royalty_recognition`
- `gross_margin`
- `contract_backlog`
- `capacity_utilization`
- `cash_runway_months`
- `dilution_or_cb_flag`
- `manufacturing_inspection_issue_flag`
- `efficacy_safety_crl_flag`
- `external_validation_flag`
- `subgroup_performance_risk_flag`
- `mna_without_utilization_flag`
- `stage4b_status`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `yuhan_lazertinib_fda_approval_royalty_commercialization_watch` | 2024-08-20 | needs_ohlc_backfill | `watch` | false |
| `hugel_letybo_us_launch_botulinum_commercialization_watch` | 2025-03-01 | needs_ohlc_backfill | `watch` | false |
| `celltrion_us_facility_biosimilar_tariff_hedge_stage2_watch` | 2025-09-23 | needs_ohlc_backfill | `watch` | false |
| `sk_bioscience_idt_biologika_cmo_transition_event_watch` | 2024-06-27 | needs_ohlc_backfill | `watch` | false |
| `samsung_biologics_us_gsk_facility_cdmo_4b_benchmark` | 2025-12-22 | needs_ohlc_backfill | `watch` | false |
| `lunit_external_validation_medical_ai_commercialization_gap_watch` | 2025-03-17 | needs_ohlc_backfill | `watch` | false |
| `r7_hard_4c_reliable_source_gap_watch` | undated | needs_ohlc_backfill | `none` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split FDA approval, CRL, paper, M&A, launch, and commercial revenue dates.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
