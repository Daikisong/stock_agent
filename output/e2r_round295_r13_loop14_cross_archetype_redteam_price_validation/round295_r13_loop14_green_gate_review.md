# Round 295 R13 Green Gate Review

Do not apply these weights to production scoring yet.

R13 Stage 3-Green is not `headline is good`. It requires the headline to close into cashflow, delivered revenue, margin, internal controls, and post-event price validation.

## Required Fields

- actual_calloff_vs_signed_contract
- actual_calloff_revenue_recognition_confirmed
- dilution_adjusted_EPS
- capital_raise_disclosure_quality
- capex_IRR_and_funding_clarity
- aftermarket_price_validation
- data_trust_internal_control
- contingent_liability_risk
- governance_execution_not_proposal
- control_premium_separation
- resource_economic_viability
- price_path_after_evidence

## Forbidden Patterns

- headline_order_backlog_only
- large_customer_name_only
- policy_or_presidential_announcement_only
- IPO_oversubscription_only
- activist_or_valueup_proposal_only
- control_premium_as_operating_green
- capex_localization_headline_only
- resource_estimate_without_drilling
- data_breach_treated_as_oneoff

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| actual_calloff_vs_signed_contract | raise | 5 | 계약 headline은 매출이 아니다. 실제 call-off와 매출 인식이 필요하다. |
| dilution_adjusted_EPS | raise | 5 | 수주가 좋아도 증자·CB가 EPS를 희석하면 Green이 아니다. |
| capital_raise_disclosure_quality | raise | 5 | 대규모 자금조달은 사용처와 투자자 의사결정 정보가 충분해야 한다. |
| capex_IRR_and_funding_clarity | raise | 5 | 현지화 CAPEX는 IRR, funding, customer demand가 닫혀야 한다. |
| aftermarket_price_validation | raise | 5 | IPO 청약경쟁률보다 상장 후 가격과 첫 실적이 더 강한 검증이다. |
| data_trust_internal_control | raise | 5 | 데이터 신뢰 훼손은 보상, 보안투자, 매출전망, 우발부채로 이어진다. |
| contingent_liability_risk | raise | 5 | 보상·소송·규제 리스크는 일회성 비용으로 단정하면 안 된다. |
| governance_execution_not_proposal | raise | 5 | Value-Up 제안은 실행 전까지 현금흐름 증거가 아니다. |
| control_premium_separation | raise | 4 | 지배권 premium은 영업현금흐름 리레이팅과 분리한다. |
| resource_economic_viability | raise | 5 | 자원 estimate는 시추·경제성·IRR 전까지 Green 증거가 아니다. |
| headline_only_event | lower | -5 | 좋은 headline 하나로 Stage 3-Green을 만들지 않는다. |

## Easy Examples
- `Tesla contract` is not Green until actual call-off and revenue recognition appear.
- `Value-Up proposal` is not Green until the board adopts and executes cash return.
- `data breach` is not one-off if revenue forecast, capex, compensation and liability change.
