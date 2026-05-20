# Round 290 R8 Green Gate Review

Do not apply these weights to production scoring yet.

R8 Stage 3-Green is not `MAU`, `IPO`, `K-pop fandom`, `game IP`, `AI/cloud`, `PE control premium`, or `buyback`. It requires paid conversion, retention, IP revenue stability, contract/governance clearance, ARR, margin, trust, OP/FCF, and price path after evidence.

## Required Fields

- paid_conversion_arpu_confirmed
- retention_and_repeat_usage_confirmed
- ip_revenue_stability_confirmed
- artist_contract_continuity_confirmed
- game_live_service_retention_confirmed
- new_title_pipeline_execution_confirmed
- cloud_ai_recurring_revenue_confirmed
- arr_retention_enterprise_sw_confirmed
- data_trust_internal_control_confirmed
- regulatory_governance_clearance_confirmed
- price_path_after_evidence

## Forbidden Patterns

- MAU_headline_only
- IPO_pop_only
- AI_cloud_keyword_only
- creator_IP_optional_value_only
- artist_fandom_without_contract_stability
- buyback_without_new_title_retention
- PE_control_premium_without_ARR
- cybersecurity_theme_readthrough_without_contract
- governance_legal_risk_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| paid_conversion_ARPU | raise | 5 | 플랫폼 MAU는 결제전환과 ARPU로 닫혀야 한다. |
| retention_and_repeat_usage | raise | 5 | 콘텐츠와 게임은 반복 사용/retention이 핵심이다. |
| IP_revenue_stability | raise | 5 | IP optionality는 안정 매출로 확인되어야 한다. |
| artist_contract_continuity | raise | 5 | K-pop IP는 artist contract와 label governance가 뿌리다. |
| game_live_service_retention | raise | 5 | 게임 hit title은 live-service retention으로 검증한다. |
| new_title_pipeline_execution | raise | 5 | 레거시 게임 턴어라운드는 신작 실행력이 필요하다. |
| cloud_AI_recurring_revenue | raise | 5 | AI/cloud 매출비중보다 반복매출과 margin이 중요하다. |
| ARR_retention_enterprise_SW | raise | 5 | enterprise SW는 ARR, churn, retention이 Green의 핵심이다. |
| data_trust_internal_control | raise | 5 | 보안 신뢰는 매출전망, 과징금, 보상비용으로 연결된다. |
| regulatory_governance_clearance | raise | 5 | 창업자/규제 overhang이 있으면 플랫폼 premium을 유예한다. |
| MAU_headline_only | lower | -5 | MAU headline만으로 Stage 3-Green을 만들지 않는다. |
| IPO_pop_only | lower | -5 | IPO pop은 unit economics 전에는 event premium이다. |
| AI_cloud_keyword_only | lower | -5 | AI/cloud 키워드는 recurring revenue 전에는 부족하다. |
| creator_IP_optional_value_only | lower | -5 | creator/IP optional value만으로 OP/FCF를 만들지 않는다. |
| artist_fandom_without_contract_stability | lower | -5 | fandom은 contract stability 없이는 Green이 아니다. |
| buyback_without_new_title_retention | lower | -5 | buyback은 신작 retention 없이는 event premium이다. |
| PE_control_premium_without_ARR | lower | -5 | PE control premium은 ARR/margin 전에는 Stage 2다. |
| cybersecurity_theme_readthrough_without_contract | lower | -5 | 보안사고 수혜 테마는 실제 계약/ARR 전에는 Green이 아니다. |
| governance_legal_risk_unresolved | lower | -5 | 거버넌스·법률 리스크 미해소는 Green을 막는다. |

## Easy Examples
- `Webtoon 170M MAU` is Stage 2; Green needs paid conversion and parent value capture.
- `LG CNS cloud/AI 54% sales` is useful, but IPO price failure means recurring margin is not proven.
- `SK Telecom data breach` is hard 4C because revenue guidance, fine, compensation, and trust costs followed.
