# Round-59 R6 Loop-2 Green Guardrails

| target | posture | Green unlock evidence | Loop-2 penalties |
| --- | --- | --- | --- |
| `FINANCIAL_SPREAD_BALANCE_SHEET` | GREEN_POSSIBLE | roe, cet1_ratio, credit_cost, pf_exposure_controlled, shareholder_return_execution | credit_cost, pf_exposure, cet1, tax_policy |
| `INSURANCE_UNDERWRITING_CYCLE` | GREEN_POSSIBLE | roe, k_ics_ratio, csm_growth, loss_ratio, shareholder_return_execution | loss_ratio, k_ics, investment_loss, operational_risk |
| `SECURITIES_BROKERAGE_CYCLE` | WATCH_YELLOW_FIRST | trading_value, ib_fee_revenue, pf_risk_low, roe_improvement | trading_value, tax_policy, pf_loss, proprietary_loss |
| `VALUE_UP_SHAREHOLDER_RETURN` | WATCH_YELLOW_FIRST | buyback_cancelled, dividend_growth, roe_improvement, minority_shareholder_protection | execution_failure, buyback_only, low_roe, policy_only |
| `HOLDING_RESTRUCTURING_GOVERNANCE` | WATCH_YELLOW_FIRST | nav_discount, actual_cancellation, governance_improvement, capital_structure_stable | event_premium, governance_battle, share_issuance, debt_ratio_jump |
| `PAYMENT_FINTECH_INFRA` | WATCH_YELLOW_FIRST | payment_volume, take_rate, attach_rate, profit_fcf, regulation_security_clean | take_rate, fcf, security, credit_loss, ipo_valuation |
| `DIGITAL_ASSET_TOKENIZATION` | WATCH_YELLOW_FIRST | regulatory_approval, reserve_transparency, redemption_capacity, transaction_volume, fee_model | reserve, convertibility, regulated_revenue, fee_model |
| `CREDIT_DATA_INFRA` | WATCH_YELLOW_FIRST | recurring_contracts, data_revenue, regulatory_clean, customer_diversification | privacy, regulation, customer_concentration |
| `VC_EXIT_MARKET_CYCLE` | REDTEAM_FIRST | exit_volume, realized_gain, cash_return | ipo_cycle, valuation_loss, funding_freeze |
| `DIGITAL_ASSET_THEME_OVERHEAT` | REDTEAM_FIRST | regulated_revenue, reserve_transparency, cash_flow | theme_only, no_revenue, depeg, fraud |
| `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | REDTEAM_FIRST |  | governance_execution, minority_protection, capital_structure |
| `TAX_POLICY_MARKET_SHOCK_OVERLAY` | REDTEAM_FIRST |  | tax_policy, trading_value, macro_sentiment |
| `STABLECOIN_CONVERTIBILITY_OVERLAY` | REDTEAM_FIRST |  | reserve, convertibility, depeg, algorithmic |

## What Not To Change

- Do not apply R6 Loop-2 v2.0 weights to production scoring yet.
- Do not treat low PBR, value-up index inclusion, buyback announcement, user count, or stablecoin law news as Green evidence by themselves.
- Do not equate buyback with cancellation.
- Do not invent ROE, CET1, K-ICS, CSM, cancellation amount, take rate, FCF, reserve ratio, stablecoin volume, or stage prices.
- Treat governance execution failure, tax policy shock, and stablecoin convertibility failure as RedTeam overlays.
