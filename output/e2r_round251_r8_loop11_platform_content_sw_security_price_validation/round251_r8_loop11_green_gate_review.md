# Round 251 R8 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- recurring_revenue_or_bookings
- arpu_paid_usage_or_arr_proxy
- opm_or_gross_margin_improvement
- fcf_conversion
- customer_retention_or_churn_stability
- ip_monetization_beyond_single_launch
- ai_feature_to_paid_revenue_or_cost_savings
- privacy_security_governance_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- ai_partnership_headline_only
- ai_infra_capital_plan_only
- mau_without_arpu
- ipo_or_debut_premium_only
- mna_without_integration
- download_count_without_bookings
- single_ip_dependence_without_retention
- founder_legal_risk
- security_privacy_incident
- data_breach_revenue_cut

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| recurring_revenue | raise | 5 | SaaS·SW·플랫폼은 일회성 이벤트보다 반복매출이 Stage 3 visibility다. |
| arr_proxy | raise | 5 | ARR proxy는 B2B SaaS와 cloud/AI 매출 지속성을 보는 핵심 축이다. |
| paid_usage_conversion | raise | 5 | MAU나 partnership보다 paid usage와 ARPU가 중요하다. |
| bookings_repeatability | raise | 4 | 게임·콘텐츠는 다운로드보다 반복 bookings가 중요하다. |
| enterprise_contract_quality | raise | 4 | B2B 계약은 고객 lock-in, 기간, 갱신성이 확인돼야 한다. |
| opm_improvement | raise | 5 | 플랫폼 매출 성장이 OPM 개선으로 이어져야 체급 변화다. |
| fcf_conversion | raise | 5 | AI capex와 콘텐츠 투자가 FCF를 훼손하면 Green을 제한한다. |
| customer_retention_or_churn | raise | 4 | retention/churn은 반복매출 품질을 확인하는 지표다. |
| ip_monetization_beyond_launch | raise | 4 | 웹툰·게임·K-pop은 launch/comeback 이후 반복 monetization이 필요하다. |
| operational_trust | raise | 5 | 플랫폼은 운영 신뢰가 깨지면 반복매출 질도 깨진다. |
| security_privacy_trust | raise | 5 | 보안·개인정보 신뢰는 R8의 hard gate다. |
| data_governance | raise | 5 | AI·플랫폼은 데이터 governance가 없으면 RedTeam 리스크가 커진다. |
| ai_feature_only | lower | -5 | AI 기능명만으로 paid revenue를 인정하지 않는다. |
| partnership_headline_only | lower | -5 | AI partnership headline은 monetization 전 event premium이다. |
| mau_without_arpu | lower | -4 | MAU만 있고 ARPU/paid usage가 없으면 Green 금지다. |
| ipo_debut_premium | lower | -5 | IPO/debut premium은 반복 monetization 전 4B-watch다. |
| mna_without_integration | lower | -4 | M&A 발표만 있고 통합·매출 전환이 없으면 제한한다. |
| ai_capex_without_revenue | lower | -5 | AI capex는 유료 매출이나 비용절감으로 닫혀야 한다. |
| game_downloads_without_bookings | lower | -4 | 다운로드 수만으로 bookings와 retention을 대체하지 않는다. |
| single_ip_dependence | lower | -4 | 단일 IP 의존은 4B/4C 감시를 높인다. |
| founder_legal_risk | lower | -5 | 창업자 법적 리스크는 IP monetization보다 먼저 봐야 한다. |
| privacy_security_trust_break | lower | -5 | 보안·개인정보 사고는 플랫폼 논리 훼손이다. |
| data_breach_revenue_cut | lower | -5 | 매출전망 하향·보상비·벌금이 동반된 유출은 hard 4C다. |

## Easy Examples
- `AI partnership` is not Green until paid usage, ARPU, margin and FCF appear.
- `Webtoon MAU` is not enough without paid content, IP licensing and operating leverage.
- `BGMI downloads` are useful context, but bookings and retention decide game/IP quality.
- `Data breach with revenue cut and fine` is hard 4C because operational trust is broken.
