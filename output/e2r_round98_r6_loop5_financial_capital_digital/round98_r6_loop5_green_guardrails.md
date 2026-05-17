# Round-98 R6 Loop-5 Green Guardrails

| target | posture | Green unlock evidence | Loop-5 penalties |
| --- | --- | --- | --- |
| `FINANCIAL_SPREAD_BALANCE_SHEET` | GREEN_POSSIBLE | roe, cet1_ratio, credit_cost, pf_exposure_controlled, shareholder_return_execution | credit_cost, pf_exposure, cet1, tax_policy |
| `BANK_HOLDING_VALUEUP_CAPITAL_RETURN` | GREEN_POSSIBLE | roe, cet1_ratio, credit_cost, pf_exposure_controlled, shareholder_return_execution, pbr_roe_band_change | credit_cost, cet1, nim, pf_exposure, return_execution |
| `INSURANCE_UNDERWRITING_CYCLE` | GREEN_POSSIBLE | roe, k_ics_ratio, csm_growth, loss_ratio, shareholder_return_execution | loss_ratio, k_ics, investment_loss, csm_quality |
| `SECURITIES_BROKERAGE_CYCLE` | WATCH_YELLOW_FIRST | trading_value, ib_fee_revenue, pf_risk_low, roe_improvement | trading_value, tax_policy, pf_loss, proprietary_loss |
| `VALUE_UP_SHAREHOLDER_RETURN` | WATCH_YELLOW_FIRST | buyback_cancelled, dividend_growth, roe_improvement, minority_shareholder_protection | execution_failure, buyback_only, low_roe, policy_only |
| `TREASURY_SHARE_CANCEL_EXECUTION` | WATCH_YELLOW_FIRST | treasury_share_cancellation_completed, roe_improvement, business_eps_fcf_path, repeat_return_policy | buyback_only, business_eps_missing, one_off_cancellation, roe_not_improving |
| `TREASURY_CANCEL_MANDATE_POLICY` | WATCH_YELLOW_FIRST | individual_treasury_cancel_execution, roe_improvement, pbr_roe_band_change, repeat_return_policy | policy_only, execution_missing, buyback_only, low_roe |
| `HOLDING_RESTRUCTURING_GOVERNANCE` | WATCH_YELLOW_FIRST | nav_discount, actual_cancellation, independent_director, governance_improvement, capital_structure_stable | event_premium, governance_battle, share_issuance, debt_ratio_jump |
| `EVENT_PREMIUM_GOVERNANCE_BATTLE` | REDTEAM_FIRST | not_applicable | event_premium, governance_battle, capital_structure, hostile_takeover |
| `PAYMENT_FINTECH_INFRA` | WATCH_YELLOW_FIRST | payment_volume, take_rate, attach_rate, profit_fcf, regulation_security_clean | take_rate, fcf, security, credit_loss, ipo_valuation |
| `FINTECH_SUPERAPP_IPO_OPTION` | WATCH_YELLOW_FIRST | take_rate, attach_rate, profit_fcf, credit_loss_control, security_clean | user_count_only, ipo_valuation, credit_loss, security, regulation |
| `KRW_STABLECOIN_INFRA_OPTION` | WATCH_YELLOW_FIRST | regulatory_approval, reserve_transparency, redemption_capacity, issued_amount, fee_model | regulation, reserve, redemption, bank_deposit_impact, fee_model |
| `DIGITAL_ASSET_TOKENIZATION` | WATCH_YELLOW_FIRST | regulatory_approval, reserve_transparency, redemption_capacity, transaction_volume, fee_model | reserve, convertibility, regulated_revenue, fee_model |
| `REGULATED_STABLECOIN_INFRA` | WATCH_YELLOW_FIRST | fiat_backed, reserve_transparency, redemption_capacity, issued_amount, transaction_volume, fee_model | reserve, redemption, issuer_margin, regulation |
| `STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION` | REDTEAM_FIRST | not_applicable | bank_deposit, user_cap, reserve_requirement, issuer_margin |
| `ALGORITHMIC_STABLECOIN_FAILURE` | REDTEAM_FIRST | not_applicable | depeg, reserve_failure, algorithmic, fraud |
| `CREDIT_DATA_INFRA` | WATCH_YELLOW_FIRST | recurring_contracts, data_revenue, regulatory_clean, customer_diversification | privacy, regulation, customer_concentration |
| `VC_EXIT_MARKET_CYCLE` | REDTEAM_FIRST | exit_volume, realized_gain, cash_return | ipo_cycle, valuation_loss, funding_freeze |
| `FINTECH_IPO_VALUATION_RISK` | REDTEAM_FIRST | not_applicable | ipo_valuation, market_window, crypto_exposure, investor_caution |
| `DIGITAL_ASSET_EXCHANGE_CONSOLIDATION` | WATCH_YELLOW_FIRST | exchange_market_share, fee_revenue, security_clean, regulatory_approval, platform_cross_sell | security, regulation, crypto_cycle, deal_dilution |
| `BANK_DIGITAL_ASSET_EQUITY_STAKE` | WATCH_YELLOW_FIRST | equity_method_income, strategic_collaboration_revenue, regulatory_approval, security_clean | equity_income_unverified, security, regulation, crypto_cycle, stake_valuation |
| `TAX_POLICY_MARKET_SHOCK_OVERLAY` | REDTEAM_FIRST | not_applicable | tax_policy, trading_value, macro_sentiment |
| `AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK` | REDTEAM_FIRST | not_applicable | policy_comment, crowded_trade, market_sentiment |
| `GOVERNANCE_EXECUTION_FAILURE_OVERLAY` | REDTEAM_FIRST | not_applicable | governance_execution, minority_protection, capital_structure |
| `STABLECOIN_CONVERTIBILITY_OVERLAY` | REDTEAM_FIRST | not_applicable | reserve, convertibility, depeg, issuer_margin |

## What Not To Change

- Do not apply R6 Loop-5 v5.0 weights to production scoring yet.
- Do not treat low PBR, value-up index inclusion, buyback announcement, user count, IPO optionality, exchange stake, exchange market share, or stablecoin law news as Green evidence by themselves.
- Do not equate buyback with cancellation.
- Do not invent ROE, CET1, K-ICS, CSM, cancellation amount, cancellation completion, take rate, FCF, reserve ratio, stablecoin volume, equity-method income, collaboration revenue, exchange security status, or stage prices.
- Treat governance execution failure, tax policy shock, stablecoin convertibility failure, algorithmic stablecoin failure, and exchange security incidents as RedTeam overlays.
