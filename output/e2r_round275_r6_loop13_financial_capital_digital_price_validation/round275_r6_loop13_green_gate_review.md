# Round 275 R6 Green Gate Review

Do not apply these weights to production scoring yet.

R6 Stage 3-Green is not `value-up`, `buyback`, `financial holding`, `Dunamu stake`, `internet-bank IPO`, `stablecoin policy`, or `trading volume`. It requires actual payout execution, capital buffer, bank-quality earnings, regulatory clearance, trust, internal controls, and price path after evidence.

## Required Fields

- actual_buyback_cancellation_confirmed
- sustainable_dividend_payout_confirmed
- cet1_rbc_capital_buffer_stable
- credit_cost_control_confirmed
- nim_fee_income_stability_confirmed
- roe_improvement_confirmed
- regulatory_approval_clearance_confirmed
- digital_asset_trust_confirmed
- exchange_internal_control_confirmed
- fee_revenue_bridge_confirmed
- price_path_after_evidence

## Forbidden Patterns

- policy_valueup_headline_only
- sector_rally_without_bank_metrics
- IPO_valuation_without_credit_quality
- digital_asset_equity_stake_only
- stablecoin_theme_only
- exchange_trust_incident
- regulatory_capital_uncertainty
- data_or_internal_control_failure
- trading_volume_event_only

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| actual_buyback_cancellation | raise | 5 | Value-up은 취득보다 실제 소각과 반복성이 중요하다. |
| sustainable_dividend_payout | raise | 4 | 배당은 CET1/RBC와 credit cost가 받쳐야 한다. |
| CET1_RBC_capital_buffer | raise | 5 | 은행·보험 Green은 자본비율이 먼저다. |
| NIM_fee_income_stability | raise | 5 | 금융 EPS는 NIM·수수료·credit cost로 닫혀야 한다. |
| ROE_RWA_control | raise | 5 | 저PBR이 아니라 ROE와 RWA control이 rerating 근거다. |
| regulatory_approval_clearance | raise | 5 | 지분투자와 M&A는 규제 승인 전에는 Stage 2다. |
| digital_asset_trust | raise | 5 | Upbit/Dunamu optionality는 exchange trust가 있어야 한다. |
| exchange_internal_control | raise | 5 | 이상출금·오배분은 hard 4C reference다. |
| policy_valueup_headline_only | lower | -5 | 정책 headline만으로 은행 Green 금지다. |
| sector_rally_without_bank_metrics | lower | -5 | 섹터 랠리는 ROE/CET1/NIM 확인 전엔 4B-watch다. |
| IPO_valuation_without_credit_quality | lower | -5 | 인터넷은행 IPO는 credit/NIM/예금집중 확인 전엔 event premium이다. |
| digital_asset_equity_stake_only | lower | -5 | Dunamu 지분만으로 은행 EPS를 만들지 않는다. |
| stablecoin_theme_only | lower | -5 | 스테이블코인 정책 테마는 발행·준비금·수수료 전에는 과열이다. |
| exchange_trust_incident | lower | -5 | 거래소 신뢰 사고는 Green을 막는 RedTeam gate다. |
| trading_volume_event_only | lower | -4 | 증권주는 거래대금 이벤트만으로 구조적 Green 금지다. |

## Easy Examples
- `KB value-up headline` is Stage 2 attention; Green needs CET1, ROE, NIM and credit cost.
- `Hana buys Dunamu stake` is an option; Green needs equity-method income, capital impact and exchange trust.
- `stablecoin basket doubles` is 4B-watch until issuer economics and FX stability are visible.
