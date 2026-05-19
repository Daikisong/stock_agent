# Round-199 R8 Loop-7 Price Backfill Plan

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
- `relative_strength_vs_platform_sw_basket`
- `relative_strength_vs_game_ip_basket`
- `relative_strength_vs_kpop_content_basket`
- `arr_proxy`
- `billings`
- `bookings`
- `paid_usage`
- `arpu`
- `mau`
- `retention_rate`
- `churn_rate`
- `opm`
- `gross_margin`
- `fcf_conversion`
- `enterprise_contract_value`
- `ip_repeat_monetization`
- `ai_revenue_conversion`
- `ai_capex`
- `mna_integration_status`
- `founder_legal_risk_flag`
- `privacy_security_incident_flag`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `douzone_bizon_eqt_cloud_erp_stage2_watch` | 2025-11-07 | needs_ohlc_backfill | `watch` | false |
| `samsung_sds_kkr_ai_cloud_cb_4b_watch` | 2026-04-15 | needs_ohlc_backfill | `watch` | false |
| `naver_webtoon_hyperclova_platform_ai_ip_stage2_watch` | 2024-06-17 | needs_ohlc_backfill | `watch` | false |
| `kakao_openai_partnership_governance_legal_event_watch` | 2025-02-04 | needs_ohlc_backfill | `watch` | false |
| `krafton_inzoi_adk_ai_first_game_ip_stage2_watch` | 2025-04-01 | needs_ohlc_backfill | `watch` | false |
| `shiftup_stellar_blade_ipo_single_ip_overheat_watch` | 2024-07-11 | needs_ohlc_backfill | `watch` | false |
| `hybe_newjeans_bang_legal_governance_4c_watch` | 2025-03-21 | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split AI partnership, model release, IPO, game launch, M&A, legal-risk, and repeat-revenue dates.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
