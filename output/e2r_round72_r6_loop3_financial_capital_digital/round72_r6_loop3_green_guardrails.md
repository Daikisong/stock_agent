# Round-72 R6 Loop-3 Green Guardrails

| target | posture | Green unlock evidence | Loop-3 penalties |
| --- | --- | --- | --- |
| `FINANCIAL_SPREAD_BALANCE_SHEET` | GREEN_POSSIBLE | roe, cet1_ratio, credit_cost, pf_exposure_controlled, shareholder_return_execution | credit_cost, pf_exposure, cet1, tax_policy |
| `INSURANCE_UNDERWRITING_CYCLE` | GREEN_POSSIBLE | roe, k_ics_ratio, csm_growth, loss_ratio, shareholder_return_execution | loss_ratio, k_ics, investment_loss, csm_quality |
| `SECURITIES_BROKERAGE_CYCLE` | WATCH_YELLOW_FIRST | trading_value, ib_fee_revenue, pf_risk_low, roe_improvement | trading_value, tax_policy, pf_loss, proprietary_loss |
| `VALUE_UP_SHAREHOLDER_RETURN` | WATCH_YELLOW_FIRST | buyback_cancelled, dividend_growth, roe_improvement, minority_shareholder_protection | execution_failure, buyback_only, low_roe, policy_only |
| `HOLDING_RESTRUCTURING_GOVERNANCE` | WATCH_YELLOW_FIRST | nav_discount, actual_cancellation, independent_director, governance_improvement, capital_structure_stable | event_premium, governance_battle, share_issuance, debt_ratio_jump |
| `EVENT_PREMIUM_GOVERNANCE_BATTLE` | REDTEAM_FIRST | not_applicable | event_premium, governance_battle, capital_structure, hostile_takeover |
| `PAYMENT_FINTECH_INFRA` | WATCH_YELLOW_FIRST | payment_volume, take_rate, attach_rate, profit_fcf, regulation_security_clean | take_rate, fcf, security, credit_loss, ipo_valuation |
| `DIGITAL_ASSET_TOKENIZATION` | WATCH_YELLOW_FIRST | regulatory_approval, reserve_transparency, redemption_capacity, transaction_volume, fee_model | reserve, convertibility, regulated_revenue, fee_model |
| `REGULATED_STABLECOIN_INFRA` | WATCH_YELLOW_FIRST | fiat_backed, reserve_transparency, redemption_capacity, issued_amount, transaction_volume, fee_model | reserve, redemption, issuer_margin, regulation |
| `ALGORITHMIC_STABLECOIN_FAILURE` | REDTEAM_FIRST | not_applicable | depeg, reserve_failure, algorithmic, fraud |
| `CREDIT_DATA_INFRA` | WATCH_YELLOW_FIRST | recurring_contracts, data_revenue, regulatory_clean, customer_diversification | privacy, regulation, customer_concentration |
| `VC_EXIT_MARKET_CYCLE` | REDTEAM_FIRST | exit_volume, realized_gain, cash_return | ipo_cycle, valuation_loss, funding_freeze |
| `DIGITAL_ASSET_EXCHANGE_CONSOLIDATION` | WATCH_YELLOW_FIRST | exchange_market_share, fee_revenue, security_clean, regulatory_approval, platform_cross_sell | security, regulation, crypto_cycle, deal_dilution |
| `TAX_POLICY_MARKET_SHOCK_OVERLAY` | REDTEAM_FIRST | not_applicable | tax_policy, trading_value, macro_sentiment |
| `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | REDTEAM_FIRST | not_applicable | governance_execution, minority_protection, capital_structure |
| `STABLECOIN_CONVERTIBILITY_OVERLAY` | REDTEAM_FIRST | not_applicable | reserve, convertibility, depeg, issuer_margin |

## What Not To Change

- Do not apply R6 Loop-3 v3.0 weights to production scoring yet.
- Do not treat low PBR, value-up index inclusion, buyback announcement, user count, exchange market share, or stablecoin law news as Green evidence by themselves.
- Do not equate buyback with cancellation.
- Do not invent ROE, CET1, K-ICS, CSM, cancellation amount, take rate, FCF, reserve ratio, stablecoin volume, exchange security status, or stage prices.
- Treat governance execution failure, tax policy shock, stablecoin convertibility failure, algorithmic stablecoin failure, and exchange security incidents as RedTeam overlays.
