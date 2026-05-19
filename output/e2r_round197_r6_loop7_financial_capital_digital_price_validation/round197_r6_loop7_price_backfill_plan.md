# Round-197 R6 Loop-7 Price Backfill Plan

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
- `relative_strength_vs_financial_basket`
- `relative_strength_vs_bank_basket`
- `relative_strength_vs_insurance_basket`
- `roe`
- `cet1_ratio`
- `kics_ratio`
- `csm_growth`
- `credit_cost`
- `pf_exposure`
- `buyback_announced`
- `buyback_cancelled`
- `dividend_payout_ratio`
- `pbr`
- `pbr_roe_gap`
- `nav_discount`
- `equity_method_income`
- `regulated_revenue`
- `stablecoin_policy_theme_flag`
- `digital_asset_revenue_unverified_flag`
- `privacy_data_trust_break_flag`
- `major_shareholder_legal_risk_flag`
- `stage4b_status`
- `hard_4c_confirmed`

## Priority Cases

| case | stage marker | current status | 4B status | hard 4C |
| --- | --- | --- | --- | --- |
| `sk_square_valueup_buyback_nav_discount_stage2_4b_watch` | 2024-11-21 | needs_ohlc_backfill | `watch` | false |
| `hana_financial_dunamu_equity_option_stage2_watch` | 2026-05-14 | needs_ohlc_backfill | `watch` | false |
| `samsung_life_nav_valueup_forced_stake_sale_regulatory_watch` | 2026-03-19 | needs_ohlc_backfill | `watch` | false |
| `kakaobank_internet_bank_governance_ownership_4c_watch` | 2024-07-22 | needs_ohlc_backfill | `watch` | true |
| `kakaopay_aton_krw_stablecoin_policy_theme_overheat` | 2025-06-18 | needs_ohlc_backfill | `watch` | false |
| `kakaopay_privacy_data_transfer_fine_payment_4c_break` | undated | needs_ohlc_backfill | `watch` | true |
| `woori_financial_valueup_nonbank_expansion_capital_buffer_watch` | undated | needs_ohlc_backfill | `watch` | false |

## Backfill Rule

- Use official OHLC data for exact MFE/MAE.
- Keep unknown values null or `needs_ohlc_backfill`.
- Split policy value-up, stablecoin, Dunamu, and NAV event price paths from durable ROE/capital-return evidence.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
