# Round 249 R6 Green Gate Review

Do not apply these weights to production scoring yet.

R6 Stage 3-Green is not `low PBR`, `value-up`, `digital asset`, or `stablecoin`. It requires ROE, capital buffer, actual cancellation/dividend execution, regulated revenue, and platform trust.

## Required Fields

- roe_improving_or_sustained
- cet1_or_kics_capital_buffer
- credit_cost_or_pf_risk_passed
- actual_buyback_cancellation
- repeat_dividend_or_cancellation_policy
- pbr_roe_gap_and_rerating_runway
- capital_release_use_confirmed
- regulated_revenue_or_equity_method_income
- platform_or_exchange_trust_passed
- price_path_after_evidence

## Forbidden Patterns

- low_pbr_only
- policy_valueup_only
- treasury_buyback_without_cancellation
- stablecoin_policy_theme_only
- digital_asset_equity_option_without_revenue
- fintech_user_growth_without_profit
- event_rally_before_regulated_revenue
- major_shareholder_legal_risk
- exchange_trust_break

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| roe_sustainability | raise | 5 | R6 Green은 저PBR보다 ROE 지속성이 먼저다. |
| cet1_or_capital_buffer | raise | 5 | 은행/보험은 자본비율이 주주환원 지속성을 결정한다. |
| real_buyback_cancellation | raise | 5 | 자사주 매입보다 실제 소각이 중요하다. |
| dividend_payout_visibility | raise | 4 | 반복 배당 정책은 PBR 프레임 전환의 증거다. |
| credit_cost_control | raise | 5 | PF와 credit cost를 통과해야 value-up이 Green으로 올라간다. |
| pbr_roe_gap | raise | 4 | PBR-ROE gap은 rerating runway를 판단하는 축이다. |
| capital_release_quality | raise | 4 | 보험/지주 NAV는 현금화와 활용처가 확인될 때 강해진다. |
| regulated_revenue_visibility | raise | 4 | 디지털자산은 규제수익/지분법 이익이 보여야 한다. |
| nav_discount_with_monetization | raise | 4 | NAV discount는 소각/매각/환원으로 연결될 때 Stage 2 품질이 올라간다. |
| digital_asset_equity_value_with_regulation | raise | 3 | 거래소 지분가치는 규제와 신뢰를 통과해야 은행 가치가 된다. |
| platform_trust | raise | 5 | 플랫폼 금융은 신뢰가 깨지면 사용자와 거래가 빠질 수 있다. |
| low_pbr_only | lower | -5 | 저PBR만으로는 구조적 rerating 증거가 아니다. |
| policy_valueup_only | lower | -4 | 정책 기대는 회사별 ROE/환원으로 닫혀야 한다. |
| treasury_buyback_without_cancellation | lower | -4 | 매입만 있고 소각이 없으면 환원 실행력이 약하다. |
| stablecoin_policy_theme_only | lower | -5 | 스테이블코인 정책 테마만으로는 수익모델이 없다. |
| digital_asset_equity_option_without_revenue | lower | -3 | 거래소 지분투자는 지분법/규제수익 전 Stage 2 watch다. |
| fintech_user_growth_without_profit | lower | -3 | 인터넷은행/핀테크 user count는 ROE와 credit quality 전 Green이 아니다. |
| exchange_trust_break | lower | -5 | abnormal withdrawal 같은 거래소 신뢰 훼손은 4C-watch다. |
| major_shareholder_legal_risk | lower | -5 | 인터넷은행 대주주 적격성 리스크는 Green을 막는다. |
| capital_ratio_weakening | lower | -4 | 인수나 주주환원 뒤 자본비율이 훼손되면 thesis break다. |
| event_rally_before_regulated_revenue | lower | -5 | 규제수익 전 이벤트 급등은 4B-watch다. |

## Easy Examples
- `low PBR` is only a cheap label until ROE and credit cost are proven.
- `buyback` is weaker than actual cancellation.
- `stablecoin policy` is a theme until issuer license, reserve income, and fee revenue exist.
