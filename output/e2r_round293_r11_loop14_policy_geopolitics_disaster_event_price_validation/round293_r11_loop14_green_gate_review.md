# Round 293 R11 Green Gate Review

Do not apply these weights to production scoring yet.

R11 Stage 3-Green is not `presidential resource headline`, `sanction relief request`, `tax clarification`, `market-access reform`, `disaster recovery theme`, or `defense order headline`. It requires implementation, legal finality, EPS/FCF bridge, production/service continuity, claims/budget/contracts, and price-after-evidence.

## Required Fields

- policy_implementation_certainty_confirmed
- legal_regulatory_finality_confirmed
- company_eps_fcf_bridge_confirmed
- foreign_flow_or_market_access_flow_confirmed
- drilling_result_confirmed
- resource_economic_viability_confirmed
- CAPEX_IRR_confirmed
- sanction_export_control_exposure_cleared
- service_or_production_continuity_confirmed
- disaster_claims_budget_contract_confirmed
- defense_delivery_margin_cash_collection_confirmed
- tax_policy_consistency_confirmed
- price_path_after_evidence

## Forbidden Patterns

- government_announcement_only
- presidential_headline_only
- resource_estimate_without_drilling
- policy_beneficiary_theme_only
- sanction_ignored_order_backlog
- tax_reform_without_market_consistency
- market_access_reform_without_foreign_flow
- disaster_recovery_without_budget_contract
- defense_order_without_delivery_margin
- labor_relief_without_production_continuity

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| policy_implementation_certainty | raise | 5 | 정책은 발표보다 법안, 예산, 시행, 기업 EPS bridge가 중요하다. |
| legal_regulatory_finality | raise | 5 | 우선협상, 완화 발언, clarification은 final law/contract와 다르다. |
| geopolitical_counterparty_risk | raise | 5 | 제재와 export-control은 수주잔고보다 먼저 거래 가능성을 흔든다. |
| political_liquidity_risk | raise | 5 | 계엄·헌정 충격은 환율, 외국인 신뢰, 유동성 프리미엄을 재가격화한다. |
| tax_policy_consistency | raise | 5 | Value-Up narrative도 세제 일관성이 깨지면 시장 신뢰가 훼손된다. |
| market_access_foreign_flow | raise | 4 | 시장접근성 개혁은 실제 외국인 flow와 증권사 수익으로 닫혀야 한다. |
| service_continuity_under_policy | raise | 4 | 의료개혁은 서비스 capacity가 깨지면 수혜보다 disruption이 먼저다. |
| disaster_damage_to_cashflow | raise | 4 | 재난은 복구테마보다 claims, budget, contract, margin을 먼저 본다. |
| labor_continuity_systemic_risk | raise | 5 | 시스템 수출기업 파업은 단일 노사 이슈가 아니라 공급망 gate다. |
| government_announcement_only | lower | -5 | 대통령 발표만으로 Green을 만들지 않는다. |
| resource_estimate_without_drilling | lower | -5 | 매장량 가능성은 시추·경제성 전에는 event premium이다. |
| sanction_ignored_order_backlog | lower | -5 | 제재가 거래를 막으면 order backlog가 방어막이 아니다. |
| tax_reform_without_market_consistency | lower | -5 | 세제 충격은 shareholder return rerating을 막을 수 있다. |
| market_access_reform_without_foreign_flow | lower | -4 | 제도개편만 있고 외국인 flow가 없으면 Stage 2에 머문다. |
| defense_order_without_delivery_margin | lower | -4 | 방산 수주는 납품, margin, cash collection 전에는 Green이 아니다. |

## Easy Examples
- `14B boe resource possibility` is not Green until drilling and economics prove it.
- `short-selling reform` is Stage 2 until foreign flow and brokerage earnings appear.
- `wildfire recovery theme` is not Green until claims, budget, contracts and margins are visible.
