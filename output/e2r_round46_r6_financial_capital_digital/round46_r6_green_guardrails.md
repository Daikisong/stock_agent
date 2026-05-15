# Round-46 R6 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `FINANCIAL_SPREAD_BALANCE_SHEET` | GREEN_POSSIBLE | roe, cet1_ratio, credit_cost, pf_exposure_controlled, shareholder_return_execution | credit_cost, pf_exposure, cet1_deterioration, return_policy_retreat |
| `INSURANCE_UNDERWRITING_CYCLE` | GREEN_POSSIBLE | roe, k_ics_ratio, csm_growth, loss_ratio, shareholder_return_execution | loss_ratio, k_ics_deterioration, operational_risk, investment_loss |
| `SECURITIES_BROKERAGE_CYCLE` | WATCH_YELLOW_FIRST | trading_value, ib_fee_revenue, pf_risk_low, roe_improvement | tax_policy_shock, trading_value_drop, pf_loss, proprietary_loss |
| `VALUE_UP_SHAREHOLDER_RETURN` | WATCH_YELLOW_FIRST | buyback_cancelled, dividend_growth, roe_improvement, minority_shareholder_protection | no_cancellation, execution_failure, low_roe, controlling_shareholder_risk |
| `HOLDING_RESTRUCTURING_GOVERNANCE` | WATCH_YELLOW_FIRST | nav_discount, actual_cancellation, governance_improvement, capital_structure_stable | governance_battle, event_premium, debt_ratio_jump, minority_conflict |
| `PAYMENT_FINTECH_INFRA` | WATCH_YELLOW_FIRST | payment_volume, take_rate, attach_rate, profit_fcf, regulation_security_clean | take_rate_pressure, security_incident, credit_loss, regulatory_sanction |
| `DIGITAL_ASSET_TOKENIZATION` | WATCH_YELLOW_FIRST | regulatory_approval, reserve_transparency, redemption_capacity, transaction_volume, fee_model | depeg, reserve_opacity, convertibility_risk, fraud, regulatory_rejection |
| `CREDIT_DATA_INFRA` | WATCH_YELLOW_FIRST | recurring_contracts, data_revenue, regulatory_clean, customer_diversification | privacy_breach, regulation, customer_concentration |
| `VC_EXIT_MARKET_CYCLE` | REDTEAM_FIRST | exit_volume, realized_gain, cash_return | ipo_slowdown, valuation_loss, funding_freeze |
| `DIGITAL_ASSET_THEME_OVERHEAT` | REDTEAM_FIRST | regulated_revenue, reserve_transparency, cash_flow | depeg, reserve_failure, fraud, theme_only, no_revenue |

## What Not To Change

- Do not apply these R6 v1.0 weights to production scoring yet.
- Do not treat low PBR, high dividend yield, value-up index inclusion, buyback headline, user count, stablecoin/STO headline, or IPO valuation as score evidence by themselves.
- Do not invent ROE, CET1, K-ICS, credit cost, PF exposure, buyback cancellation, payment volume, take rate, reserve ratio, transaction volume, or price-path fields.
- Do not lower Stage 3-Green for value-up or fintech stories. Green requires executed capital return, quality balance sheet, recurring revenue, or regulated financial infrastructure evidence.
- Treat activist rejection, buyback without cancellation, governance battle, debt jump, tax shock, de-peg, convertibility risk, fraud, and reserve failure as RedTeam evidence.
