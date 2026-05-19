# Round-202 R11 Loop-7 Green Gate Review

## Green Required Evidence

- `company_level_contract_confirmed`
- `budget_or_contract_amount_confirmed`
- `financing_secured`
- `actual_order_or_procurement_award_confirmed`
- `revenue_conversion_confirmed`
- `margin_or_eps_fcf_revision_confirmed`
- `repeat_demand_not_event_fade_confirmed`
- `price_path_after_contract_evidence`

## Green Forbidden Patterns

- `policy_news_only`
- `mou_only`
- `geopolitical_headline_only`
- `resource_estimate_without_drilling`
- `preprint_or_science_claim_only`
- `disease_import_ban_only`
- `tourist_or_reconstruction_policy_only`
- `market_structure_reform_without_earnings`
- `price_rally_before_contract`
- `event_fade_risk`
- `unfunded_budget`
- `policy_reversal`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `funded_budget` | raise | 5 | R11 이벤트는 예산이 붙어야 회사 단위 증거가 된다. |
| `actual_contract` | raise | 5 | 정책·MOU는 실제 계약으로 승격될 때만 강해진다. |
| `revenue_conversion` | raise | 5 | 계약이 매출 인식으로 내려와야 Stage 3 후보가 된다. |
| `financing_secured` | raise | 4 | 재건·인프라·원전 이벤트는 financing 확인이 필요하다. |
| `government_stockpile_order` | raise | 4 | 정부 비축/조달은 실제 order와 guidance가 있어야 한다. |
| `procurement_award` | raise | 4 | 발주·조달계약은 단순 headline보다 강한 Stage 2 증거다. |
| `commerciality_confirmed` | raise | 4 | 자원 발견은 상업성이 확인되어야 현금흐름 후보가 된다. |
| `independent_replication_or_validation` | raise | 4 | 과학/신소재 claim은 독립 검증 전까지 Stage 1이다. |
| `event_to_contract_escalation` | raise | 4 | 이벤트가 계약으로 승격되는 순간을 따로 보상한다. |
| `policy_durability` | raise | 3 | 정책 지속성과 예산 집행 가능성이 있어야 event fade를 줄인다. |
| `policy_news_only` | lower | -5 | 정책 뉴스만으로 Stage 3-Green을 만들지 않는다. |
| `mou_only` | lower | -5 | MOU는 계약이 아니며 revenue conversion 전까지 Watch다. |
| `geopolitical_headline_only` | lower | -5 | 지정학 headline은 회사 단위 계약 전까지 event premium이다. |
| `resource_estimate_without_drilling` | lower | -5 | 매장 가능성은 시추·상업성 전까지 Green 금지다. |
| `preprint_or_science_claim_only` | lower | -5 | preprint와 과학 claim은 독립 재현 전까지 Green 금지다. |
| `disease_import_ban_only` | lower | -4 | 질병·수입금지는 마진 확인 전까지 one-off event다. |
| `tourist_or_reconstruction_policy_only` | lower | -4 | 관광·재건 정책은 funded order 전까지 제한한다. |
| `market_structure_reform_without_earnings` | lower | -3 | 시장구조 개선은 기업 EPS 전까지 개별 Green이 아니다. |
| `price_rally_before_contract` | lower | -5 | 계약 전 가격 급등은 4B-watch 우선이다. |
| `event_fade_risk` | lower | -4 | 후속 evidence 없는 이벤트는 drawdown 위험을 크게 본다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round202 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent contract, budget, financing, order, revenue, EPS/FCF, stage prices, or MFE/MAE.
- Do not treat policy news, MOU, resource discovery, disease event, science preprint, or market-structure reform as Green evidence alone.
