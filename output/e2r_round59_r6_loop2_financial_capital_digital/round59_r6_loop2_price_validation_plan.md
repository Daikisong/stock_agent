# Round-59 R6 Loop-2 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare ROE, PBR, CET1, K-ICS, CSM, credit cost, dividends, cancellation, NAV, take rate, FCF, reserve, and redemption with price path.
6. Mark governance failure, event premium, tax shock, stablecoin convertibility, and algorithmic stablecoin failure explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `korea_commercial_act_treasury_cancel_case` | `VALUE_UP_SHAREHOLDER_RETURN` | 2026-02-25 | missing_direct_symbol_mapping |
| `sk_square_buyback_cancel_case` | `HOLDING_RESTRUCTURING_GOVERNANCE` | 2024-11-21 | needs_price_backfill |
| `samsung_electronics_buyback_case` | `VALUE_UP_SHAREHOLDER_RETURN` | 2024-11-15 | needs_price_backfill |
| `samsung_electronics_treasury_cancel_case` | `VALUE_UP_SHAREHOLDER_RETURN` | 2026-03-31 | needs_price_backfill |
| `samsung_ct_activist_rejection_case` | `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | undated | needs_source_date_and_price_backfill |
| `korea_zinc_tender_offer_event_case` | `HOLDING_RESTRUCTURING_GOVERNANCE` | 2024-09-13 | needs_price_backfill |
| `korea_zinc_buyback_court_case` | `HOLDING_RESTRUCTURING_GOVERNANCE` | 2024-10-21 | needs_price_backfill |
| `korea_zinc_share_issue_probe_case` | `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | 2024-10-31 | needs_price_backfill |
| `korea_tax_policy_shock_case` | `TAX_POLICY_MARKET_SHOCK_OVERLAY` | 2025-08-06 | missing_direct_symbol_mapping |
| `ai_windfall_tax_comment_case` | `TAX_POLICY_MARKET_SHOCK_OVERLAY` | 2026-05-12 | missing_direct_symbol_mapping |
| `stripe_payment_infra_profit_case` | `PAYMENT_FINTECH_INFRA` | 2025-02-27 | missing_public_price_data |
| `mynt_gcash_ipo_case` | `PAYMENT_FINTECH_INFRA` | 2026-05-14 | missing_public_price_data |
| `toss_global_stablecoin_case` | `PAYMENT_FINTECH_INFRA` | 2025-09-09 | missing_public_price_data |
| `boe_stablecoin_convertibility_case` | `STABLECOIN_CONVERTIBILITY_OVERLAY` | 2026-05-08 | missing_direct_symbol_mapping |
| `terrausd_do_kwon_case` | `STABLECOIN_CONVERTIBILITY_OVERLAY` | undated | needs_source_date_and_price_backfill |

## Alignment Labels

- `VALUEUP_EXECUTION_ALIGNED`: actual cancellation, dividend, ROE, and price path align.
- `BUYBACK_ONLY_REBOUND`: buyback-driven rebound without business or ROE/FCF confirmation.
- `HOLDING_NAV_DISCOUNT_REDUCTION`: NAV discount reduction follows capital allocation or governance execution.
- `EVENT_PREMIUM_NOT_VALUEUP`: control premium or tender event is not structural rerating.
- `TAX_POLICY_SHOCK`: tax policy damages value-up or brokerage momentum.
- `FINTECH_USER_GROWTH_NO_FCF`: user growth exists, economics are still missing.
- `REGULATED_STABLECOIN_INFRA`: regulated reserve/redemption/volume/fees are proven.
- `ALGORITHMIC_STABLECOIN_4C`: algorithmic de-peg or reserve failure is hard 4C.
