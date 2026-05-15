# Round-46 R6 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Calculate peak price, drawdown after peak, and below-stage3 flag.
6. Compare price paths with ROE, PBR, CET1, K-ICS, CSM, loss ratio, credit cost, dividends, buybacks, trading value, take rate, and stablecoin volume/reserves.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `korea_commercial_act_treasury_share_cancel_case` | 2026-02-25 | missing_direct_symbol_mapping |
| `korea_dividend_tax_reform_case` | 2025-06-11 | missing_direct_symbol_mapping |
| `sk_square_buyback_cancel_case` | 2024-11-21 | needs_price_backfill |
| `samsung_electronics_buyback_mixed_case` | 2024-11-15 | needs_price_backfill |
| `korean_financial_holdings_valueup_case` | needs_source_date | needs_source_date_and_price_backfill |
| `mynt_gcash_payment_platform_case` | 2026-05-14 | missing_public_price_data |
| `toss_won_stablecoin_case` | 2025-09-09 | missing_public_price_data |
| `samsung_ct_activist_rejection_case` | needs_source_date | needs_source_date_and_price_backfill |
| `korea_zinc_buyback_event_case` | 2024-10-21 | needs_price_backfill |
| `korea_tax_policy_shock_case` | 2025-08-01 | missing_direct_symbol_mapping |
| `terrausd_do_kwon_collapse_case` | needs_source_date | needs_source_date_and_price_backfill |
| `boe_stablecoin_convertibility_warning_case` | 2026-05-08 | missing_direct_symbol_mapping |

## Alignment Labels

- `aligned`: ROE/PBR/shareholder return or transaction economics move with price rerating.
- `policy_rerating`: policy changes rerate the sector, but company execution still needs verification.
- `buyback_only_rebound`: buyback lifts price without business or ROE change.
- `event_premium`: tender, control battle, IPO, or policy event moves price before core economics are proven.
- `false_positive_score`: low PBR or value-up label exists but cancellation, dividend, or ROE improvement is missing.
- `thesis_break`: governance failure, de-peg, stablecoin run, tax shock, or credit-cost spike breaks the thesis.
