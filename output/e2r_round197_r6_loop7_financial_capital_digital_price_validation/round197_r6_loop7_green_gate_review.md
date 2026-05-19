# Round-197 R6 Loop-7 Green Gate Review

## Green Required Evidence

- `roe_structurally_improving_or_sustained`
- `cet1_or_kics_capital_buffer`
- `actual_buyback_cancellation`
- `dividend_or_cancel_policy_durable`
- `credit_cost_pf_risk_passed`
- `pbr_rerating_runway`
- `company_level_capital_allocation_evidence`
- `digital_asset_revenue_model_or_equity_method_income`
- `regulatory_privacy_governance_trust_passed`

## Green Forbidden Patterns

- `low_pbr_only`
- `policy_valueup_only`
- `treasury_buyback_without_cancellation`
- `stablecoin_policy_theme_only`
- `digital_asset_equity_option_without_revenue`
- `fintech_user_growth_without_profit`
- `non_bank_acquisition_with_capital_ratio_weakening`
- `major_shareholder_legal_risk`
- `privacy_or_data_trust_break`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `roe_sustainability` | raise | 4 | 저PBR보다 ROE가 유지되거나 개선되는지가 PBR frame change의 시작이다. |
| `cet1_buffer` | raise | 4 | CET1/K-ICS buffer가 있어야 환원과 인수가 지속된다. |
| `real_buyback_cancellation` | raise | 5 | 자사주 매입보다 실제 소각이 자본배분 실행 증거다. |
| `dividend_payout_visibility` | raise | 3 | 배당/소각 정책이 반복 가능해야 한다. |
| `credit_cost_control` | raise | 4 | PF와 credit cost가 안정돼야 금융주 rerating이 지속된다. |
| `pbr_roe_gap` | raise | 3 | ROE 대비 PBR discount가 줄어들 여지가 있어야 한다. |
| `capital_release_quality` | raise | 3 | 보험/지주 NAV는 매각대금 활용과 자본 release가 확인될 때 강해진다. |
| `regulated_revenue_visibility` | raise | 3 | 디지털자산/결제는 실제 수수료, 지분법, reserve income이 필요하다. |
| `nav_discount_with_monetization` | raise | 3 | NAV discount는 소각/배당/자산화로 이어질 때만 강하다. |
| `non_bank_expansion_with_capital_buffer` | raise | 2 | 비은행 확장은 CET1 buffer를 훼손하지 않을 때만 가점한다. |
| `low_pbr_only` | lower | -5 | 저PBR만으로는 Stage 1 attention이다. |
| `policy_valueup_only` | lower | -4 | 정책 기대만 있고 회사 실행이 없으면 Green 근거가 아니다. |
| `treasury_buyback_without_cancellation` | lower | -4 | 자사주 매입만 있고 소각이 없으면 환원 실행력이 낮다. |
| `stablecoin_policy_theme_only` | lower | -5 | 원화 스테이블코인 정책 테마만으로는 수익모델이 없다. |
| `digital_asset_equity_option_without_revenue` | lower | -3 | 지분투자는 수익화와 자본비율 영향 확인 전 Stage 2 watch다. |
| `fintech_user_growth_without_profit` | lower | -3 | 사용자 수만 있고 take rate/OP가 없으면 제한한다. |
| `privacy_or_data_trust_break` | lower | -5 | 개인정보/데이터 신뢰 훼손은 fintech hard RedTeam이다. |
| `major_shareholder_legal_risk` | lower | -5 | 대주주 적격성 리스크는 은행/핀테크 Green을 막는다. |
| `capital_ratio_weakening` | lower | -4 | 인수나 환원으로 자본비율이 약해지면 Stage 3를 제한한다. |
| `pf_credit_cost_unknown` | lower | -3 | PF/credit cost가 불명확하면 저PBR rerating을 보류한다. |
| `mna_expansion_without_cet1_buffer` | lower | -3 | 비은행 인수는 CET1 buffer 확인 전 가점하지 않는다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round197 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent ROE, CET1, K-ICS, credit cost, cancellation, regulated revenue, stage prices, or MFE/MAE.
