# Round-199 R8 Loop-7 Green Gate Review

## Green Required Evidence

- `recurring_revenue_or_bookings_confirmed`
- `arr_arpu_paid_usage_or_billings_confirmed`
- `opm_or_gross_margin_improving`
- `fcf_conversion_visible`
- `retention_or_churn_stable`
- `ip_monetization_beyond_single_launch`
- `ai_feature_converts_to_paid_revenue_or_cost_savings`
- `privacy_security_governance_trust_passed`
- `price_path_after_repeat_economics`

## Green Forbidden Patterns

- `ai_feature_only`
- `partnership_headline_only`
- `model_release_or_paper_only`
- `mau_without_arpu`
- `game_launch_first_week_only`
- `ipo_first_month_rally`
- `mna_announcement_only`
- `single_ip_dependence_without_repeat_monetization`
- `ai_capex_without_revenue`
- `founder_legal_risk`
- `privacy_or_security_trust_break`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `recurring_revenue` | raise | 5 | R8 Green은 반복매출과 고객 lock-in에서 시작한다. |
| `arr_proxy` | raise | 5 | ARR, billings, bookings proxy가 확인되면 SaaS/플랫폼 visibility가 올라간다. |
| `bookings_repeatability` | raise | 4 | 게임/IP는 첫 주 판매보다 반복 bookings와 retention이 중요하다. |
| `paid_usage_conversion` | raise | 4 | AI 기능은 유료 사용 전환이 보여야 강한 증거다. |
| `enterprise_contract_quality` | raise | 4 | AI cloud/SW는 기업계약과 매출 전환이 확인될 때 강하다. |
| `opm_improvement` | raise | 4 | OPM 개선은 테마가 이익 체급 변화로 내려왔다는 증거다. |
| `fcf_conversion` | raise | 4 | AI capex와 콘텐츠 투자가 FCF를 훼손하지 않아야 한다. |
| `customer_retention_or_churn` | raise | 4 | retention 안정과 churn 하락은 반복매출의 질을 보여준다. |
| `ip_monetization_beyond_launch` | raise | 3 | 콘텐츠/IP는 출시 이후 반복 monetization이 필요하다. |
| `cloud_ai_revenue_conversion` | raise | 4 | AI infra 투자는 실제 AI 매출로 전환될 때 점수를 준다. |
| `operational_trust` | raise | 4 | 플랫폼/보안/콘텐츠는 법적·개인정보·운영 신뢰가 핵심 gate다. |
| `ai_feature_only` | lower | -5 | AI 기능 출시만으로 Stage 3-Green을 만들지 않는다. |
| `partnership_headline_only` | lower | -4 | OpenAI/KKR/파트너십 headline은 매출 전까지 Stage 1~2다. |
| `mau_without_arpu` | lower | -4 | MAU는 ARPU와 paid usage 없이 이익 체급 변화가 아니다. |
| `game_launch_first_week_only` | lower | -4 | 첫 주 판매는 Stage 2 재료지만 반복 bookings 전 Green 금지다. |
| `ipo_first_month_rally` | lower | -4 | IPO 직후 가격반응은 single-IP/valuation overheat로 분리한다. |
| `single_ip_dependence` | lower | -4 | 단일 IP 의존은 repeat portfolio 전까지 RedTeam이다. |
| `mna_event_without_integration` | lower | -3 | M&A 발표는 integration, 계약, margin 전까지 event premium이다. |
| `ai_capex_without_revenue` | lower | -4 | AI capex가 매출로 전환되지 않으면 FCF를 훼손할 수 있다. |
| `media_report_or_model_release_only` | lower | -3 | 모델 공개나 언론 보도만으로 유료화 근거를 발명하지 않는다. |
| `founder_legal_risk` | lower | -5 | 창업자/대주주 법적 리스크는 플랫폼 Green을 막을 수 있다. |
| `privacy_or_security_trust_break` | lower | -5 | 개인정보·보안 신뢰 훼손은 hard RedTeam이다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round199 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent ARR, bookings, paid usage, ARPU, retention, churn, OPM, FCF, stage prices, or MFE/MAE.
- Do not treat AI feature launch, partnership, model release, game launch, IPO, or M&A headline as Green evidence.
