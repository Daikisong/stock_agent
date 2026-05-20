# Round 236 R6 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- roe_improvement_or_sustainability
- cet1_kics_or_capital_buffer
- actual_buyback_cancellation_or_repeated_dividend_execution
- credit_cost_pf_risk_passed
- pbr_roe_gap_rerating_runway
- capital_release_or_nav_monetization_quality
- regulated_digital_revenue_or_equity_method_income
- privacy_exchange_trust_governance_passed
- price_path_after_evidence

## Forbidden Patterns

- low_pbr_only
- policy_valueup_only
- treasury_buyback_without_cancellation
- stablecoin_policy_theme_only
- digital_asset_equity_option_without_revenue
- fintech_user_growth_without_profit
- internet_bank_ipo_without_listed_price_path
- major_shareholder_legal_risk
- exchange_trust_break
- capital_ratio_weakening_after_mna
- event_rally_before_regulated_revenue

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| roe_sustainability | raise | 5 | 저PBR보다 ROE가 유지되거나 개선되는지가 PBR 프레임 변화의 핵심이다. |
| cet1_or_capital_buffer | raise | 5 | 은행 CET1과 보험 K-ICS/CSM buffer가 있어야 환원과 인수가 지속된다. |
| real_buyback_cancellation | raise | 5 | 자사주 매입보다 실제 소각이 자본배분 실행 증거다. |
| dividend_payout_visibility | raise | 4 | 배당과 소각이 반복 policy로 고정될 때 신뢰도가 올라간다. |
| credit_cost_control | raise | 5 | PF와 credit cost가 안정돼야 금융주 rerating이 지속된다. |
| pbr_roe_gap | raise | 4 | ROE 대비 PBR discount가 줄어들 여지가 있어야 한다. |
| capital_release_quality | raise | 4 | 보험/지주 NAV는 매각대금 활용과 capital release가 확인될 때 강해진다. |
| regulated_revenue_visibility | raise | 4 | 디지털자산/결제는 실제 수수료, 지분법, reserve income이 필요하다. |
| nav_discount_with_monetization | raise | 4 | NAV discount는 소각/배당/자산화로 이어질 때만 강하다. |
| digital_asset_equity_value_with_regulation | raise | 3 | 디지털자산 지분 옵션은 규제 승인과 수익화 구조가 붙어야 한다. |
| low_pbr_only | lower | -5 | 저PBR만으로는 Stage 3-Green을 만들 수 없다. |
| policy_valueup_only | lower | -4 | 밸류업 정책 기대만 있고 실행이 없으면 Stage 1 attention이다. |
| treasury_buyback_without_cancellation | lower | -4 | 자사주 매입만 있고 소각이 없으면 자본배분 품질을 제한한다. |
| stablecoin_policy_theme_only | lower | -5 | 스테이블코인 정책 테마만으로는 규제수익을 증명하지 못한다. |
| digital_asset_equity_option_without_revenue | lower | -3 | 지분 옵션만 있고 지분법/수수료/거래량 지속성이 없으면 Green 금지다. |
| fintech_user_growth_without_profit | lower | -3 | 사용자 수 성장만 있고 take-rate/이익이 없으면 제한한다. |
| privacy_or_exchange_trust_break | lower | -5 | 개인정보·거래소 신뢰 훼손은 핀테크 hard gate다. |
| major_shareholder_legal_risk | lower | -5 | 인터넷은행은 대주주 적격성 리스크가 성장성보다 먼저다. |
| capital_ratio_weakening | lower | -4 | 대형 인수나 비은행 확장이 자본비율을 훼손하면 제한한다. |
| mna_expansion_without_capital_buffer | lower | -3 | M&A 확장은 자본 buffer와 수익성을 확인하기 전 Stage 2 watch다. |
| event_rally_before_regulated_revenue | lower | -5 | 규제수익 전 가격 급등은 4B/event premium이다. |

## Easy Examples
- `저PBR + 밸류업`은 Stage 1/2 관심이다. ROE, CET1, 반복 소각, credit cost 통과 전 Green이 아니다.
- `증권주 +13.5%`는 거래대금 사이클 4B-watch다. 개별 증권사 ROE/IB 수익 확인 전 Green이 아니다.
- `스테이블코인 관련주 2~3배`는 수익모델 전 가격 선반영이다. 발행권, reserve income, fee revenue 없으면 event premium이다.
- `Dunamu 지분투자`는 Stage 2 후보지만 지분법 이익과 규제 승인 전에는 Green이 아니다.
