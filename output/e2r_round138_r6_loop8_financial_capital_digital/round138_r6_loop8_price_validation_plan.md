# Round-138 R6 Loop-8 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare ROE, PBR, CET1, K-ICS, CSM, credit cost, dividends, cancellation, NAV, take rate, FCF, reserve, redemption, equity-method income, collaboration revenue, and exchange security with price path.
6. Mark governance failure, event premium, tax shock, stablecoin convertibility, algorithmic stablecoin failure, and exchange security incidents explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `korea_commercial_act_treasury_cancel_case` | `TREASURY_CANCEL_MANDATE_POLICY` | 2026-02-25 | missing_direct_symbol_mapping |
| `sk_square_buyback_cancel_case` | `HOLDING_RESTRUCTURING_GOVERNANCE` | 2024-11-21 | needs_price_backfill |
| `samsung_electronics_treasury_cancel_case` | `TREASURY_SHARE_CANCEL_EXECUTION` | 2026-03-31 | needs_price_backfill |
| `korea_bank_financial_holding_valueup_candidate` | `BANK_HOLDING_VALUEUP_CAPITAL_RETURN` | undated | needs_named_case_and_price_backfill |
| `korea_insurance_underwriting_valueup_candidate` | `INSURANCE_UNDERWRITING_CYCLE` | undated | needs_named_case_and_price_backfill |
| `samsung_ct_activist_rejection_case` | `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | undated | needs_source_date_and_price_backfill |
| `korea_zinc_tender_offer_event_case` | `EVENT_PREMIUM_GOVERNANCE_BATTLE` | 2024-09-13 | needs_price_backfill |
| `korea_zinc_share_issue_probe_case` | `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | 2024-10-31 | needs_price_backfill |
| `korea_capital_gains_tax_scrap_case` | `TAX_POLICY_MARKET_SHOCK_OVERLAY` | 2025-09-11 | missing_direct_symbol_mapping |
| `ai_citizen_dividend_policy_shock_case` | `AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK` | 2026-05-12 | missing_direct_symbol_mapping |
| `mynt_gcash_ipo_case` | `FINTECH_SUPERAPP_IPO_OPTION` | 2026-05-14 | missing_public_price_data |
| `clear_street_ipo_valuation_cut_case` | `FINTECH_IPO_VALUATION_RISK` | 2026-02-12 | missing_public_price_data |
| `toss_global_stablecoin_case` | `PAYMENT_FINTECH_INFRA` | 2025-09-09 | missing_public_price_data |
| `circle_usdc_stablecoin_earnings_case` | `REGULATED_STABLECOIN_INFRA` | 2026-05-11 | needs_price_backfill |
| `boe_stablecoin_rules_reconsider_case` | `STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION` | 2026-05-14 | missing_direct_symbol_mapping |
| `terrausd_do_kwon_case` | `ALGORITHMIC_STABLECOIN_FAILURE` | undated | needs_source_date_and_price_backfill |
| `hana_bank_dunamu_stake_case` | `BANK_DIGITAL_ASSET_EQUITY_STAKE` | 2026-05-14 | needs_price_backfill |
| `dunamu_naver_financial_merger_option_case` | `DIGITAL_ASSET_EXCHANGE_CONSOLIDATION` | undated | needs_exact_stage_date_backfill |
| `digital_asset_exchange_security_cycle_case` | `DIGITAL_ASSET_EXCHANGE_CONSOLIDATION` | undated | needs_named_case_and_price_backfill |
| `korea_pf_credit_cost_overlay_case` | `BANK_CREDIT_COST_PF_OVERLAY` | 2024-05-13 | missing_direct_symbol_mapping |
| `bybit_exchange_hack_case` | `EXCHANGE_SECURITY_OPERATIONAL_RISK` | 2025-02-27 | missing_public_price_data |

## Alignment Labels

- `VALUEUP_EXECUTION_ALIGNED`: actual cancellation, dividend, ROE, and price path align.
- `TREASURY_CANCEL_POLICY_TAILWIND`: policy is a tailwind; individual execution is still missing.
- `BUYBACK_CANCEL_BUT_BUSINESS_RISK`: cancellation happened, but price/EPS path did not confirm the thesis.
- `HOLDING_NAV_DISCOUNT_REDUCTION`: NAV discount reduction follows capital allocation or governance execution.
- `EVENT_PREMIUM_NOT_VALUEUP`: control premium or tender event is not structural rerating.
- `TAX_POLICY_SHOCK`: tax policy damages value-up or brokerage momentum.
- `AI_CITIZEN_DIVIDEND_POLICY_SHOCK`: policy comments damage crowded AI/value-up price paths.
- `FINTECH_USER_GROWTH_NO_FCF`: user growth exists, economics are still missing.
- `FINTECH_IPO_VALUATION_COMPRESSION`: IPO valuation or size is cut before public proof of economics.
- `KRW_STABLECOIN_OPTION_NOT_REVENUE`: KRW stablecoin option exists, but approval/volume/fees are missing.
- `REGULATED_STABLECOIN_INFRA`: regulated reserve/redemption/volume/fees are proven.
- `STABLECOIN_REGULATION_FLUID_WATCH`: bank-deposit impact, user caps, or reserve rules can compress economics.
- `ALGORITHMIC_STABLECOIN_4C`: algorithmic de-peg or reserve failure is hard 4C.
- `BANK_DIGITAL_ASSET_STAKE_WATCH`: bank exchange stake is strategic, but income/revenue/security is still missing.
- `DIGITAL_ASSET_EXCHANGE_SECURITY_4C`: exchange deal has security/regulatory break risk.
