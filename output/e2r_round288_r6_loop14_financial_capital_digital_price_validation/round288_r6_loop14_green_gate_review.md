# Round 288 R6 Green Gate Review

Do not apply these weights to production scoring yet.

R6 Stage 3-Green is not `Value-Up`, `buyback`, `IPO`, `crypto`, `stablecoin`, or `PE investment` as a headline. It requires CET1, actual payout/cancellation, credit-cost control, discount compression, aftermarket demand, custody/internal control, AML/KYC, capital treatment, dilution-adjusted ROIC, and price-path evidence.

## Required Fields

- cet1_capital_buffer_confirmed
- actual_payout_execution_confirmed
- treasury_share_cancellation_confirmed
- credit_cost_control_confirmed
- holdco_discount_compression_confirmed
- ipo_aftermarket_demand_confirmed
- digital_asset_custody_control_confirmed
- aml_kyc_regulatory_clearance_confirmed
- cb_dilution_adjusted_roic_confirmed
- minority_shareholder_alignment_confirmed
- price_path_after_evidence

## Forbidden Patterns

- Value_Up_headline_only
- shareholder_return_proposal_only
- announced_buyback_without_cancellation
- IPO_size_or_customer_count_only
- crypto_exchange_market_share_only
- M&A_synergy_without_custody_control
- CB_or_PE_investment_headline_only
- stablecoin_keyword_without_revenue
- founder_legal_risk_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| CET1_capital_buffer | raise | 5 | 금융지주 Green은 자본비율이 배당·소각을 버틸 때만 가능하다. |
| actual_payout_execution | raise | 5 | 배당·자사주는 발표가 아니라 실제 집행이 증거다. |
| treasury_share_cancellation | raise | 5 | 자사주 매입은 소각되어야 minority alignment로 연결된다. |
| credit_cost_control | raise | 5 | 은행/금융지주 EPS는 대손비용이 흔들리면 바로 약해진다. |
| holdco_discount_compression | raise | 4 | 지주 할인은 실제 discount compression이 확인되어야 한다. |
| IPO_aftermarket_demand | raise | 5 | IPO 규모와 고객수보다 상장 후 수요와 가격 검증이 중요하다. |
| digital_asset_custody_control | raise | 5 | 디지털자산은 거래량보다 custody/internal control이 먼저다. |
| AML_KYC_regulatory_clearance | raise | 5 | 가상자산/핀테크 수익화는 AML/KYC와 규제 승인 전엔 Stage 2다. |
| CB_dilution_adjusted_ROIC | raise | 5 | CB/PE 투자는 희석 조정 ROIC와 자금사용 성과로 닫혀야 한다. |
| minority_shareholder_alignment | raise | 5 | Value-Up은 소액주주 정렬이 실제로 개선될 때만 점수를 준다. |
| Value_Up_headline_only | lower | -5 | 정책 headline은 Stage 2 신호이지 은행 Green 증거가 아니다. |
| shareholder_return_proposal_only | lower | -5 | 주주제안은 통과·집행 전에는 자본환원이 아니다. |
| announced_buyback_without_cancellation | lower | -5 | 소각 없는 매입 발표는 반복 환원으로 보지 않는다. |
| IPO_size_or_customer_count_only | lower | -5 | 인터넷은행 고객수/IPO 규모만으로 bank-quality Green 금지다. |
| crypto_exchange_market_share_only | lower | -5 | 거래소 점유율은 custody와 regulatory gate 전에는 수익가시성이 아니다. |
| M&A_synergy_without_custody_control | lower | -5 | 디지털자산 M&A 시너지는 custody/internal control 전에는 event premium이다. |
| CB_or_PE_investment_headline_only | lower | -5 | PE/CB headline만 있고 ROIC·희석 조건이 없으면 4B-watch다. |
| stablecoin_keyword_without_revenue | lower | -5 | stablecoin 단어는 실제 수익모델 전에는 Green 증거가 아니다. |
| founder_legal_risk_unresolved | lower | -5 | 은행 ownership에 영향을 주는 창업자 법적 리스크는 RedTeam gate다. |

## Easy Examples
- `Value-Up law` is like a door opening. The company still has to walk through it with CET1, payout execution and credit-cost control.
- `K Bank customers` are useful, but Green needs listed aftermarket demand, NIM, funding cost and credit quality.
- `Naver/Dunamu M&A` can move price, but an Upbit abnormal withdrawal makes custody/internal-control a blocking gate.
- `Samsung SDS/KKR CB` is a credible catalyst, but dilution-adjusted ROIC and real AI/stablecoin revenue decide durability.
