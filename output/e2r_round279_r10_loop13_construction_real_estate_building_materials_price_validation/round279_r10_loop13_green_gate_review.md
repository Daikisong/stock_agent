# Round 279 R10 Green Gate Review

Do not apply these weights to production scoring yet.

R10 Stage 3-Green is not `PF support`, `order headline`, `preferred bidder`, `property price rebound`, `rate-cut expectation`, or `tariff relief`. It requires refinancing, presales, EPC margin, working capital, final contract, spread, safety trust and FCF.

## Required Fields

- PF_refinancing_success_confirmed
- project_profitability_filter_confirmed
- pre_sale_ratio_confirmed
- unsold_inventory_reduction_confirmed
- EPC_margin_visibility_confirmed
- working_capital_control_confirmed
- unbilled_receivables_control_confirmed
- final_contract_signed_confirmed
- legal_appeal_clearance_confirmed
- construction_safety_trust_confirmed
- building_material_demand_spread_confirmed
- price_path_after_evidence

## Forbidden Patterns

- order_headline_only
- preferred_bidder_only
- policy_support_only
- tariff_relief_only
- rate_cut_property_expectation_only
- housing_price_rebound_without_cashflow
- PF_support_without_profitability
- EPC_backlog_without_margin
- safety_incident_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| PF_refinancing_success | raise | 5 | PF 지원이 아니라 실제 차환 성공을 봐야 한다. |
| project_profitability_filter | raise | 5 | 지원 대상 프로젝트가 수익성 있는지 확인해야 한다. |
| pre_sale_ratio | raise | 5 | 분양률이 현금회수의 출발점이다. |
| unsold_inventory_reduction | raise | 5 | 미분양 감소 없이는 주택 Green이 어렵다. |
| EPC_margin_visibility | raise | 5 | 해외 EPC 수주는 마진이 닫혀야 한다. |
| working_capital_control | raise | 5 | 건설은 운전자본과 현금회수가 늦으면 이익이 훼손된다. |
| unbilled_receivables_control | raise | 5 | 미청구공사 증가는 EPC/건설 4C-watch다. |
| final_contract_signed | raise | 5 | preferred bidder는 최종계약이 아니다. |
| legal_appeal_clearance | raise | 5 | 원전/인프라는 법적 이의제기가 해소되어야 한다. |
| construction_safety_trust | raise | 5 | 사망 안전사고는 hard gate다. |
| order_headline_only | lower | -5 | 수주 headline은 Stage 2일 수 있지만 Green은 아니다. |
| preferred_bidder_only | lower | -5 | 우선협상대상자는 최종계약과 다르다. |
| policy_support_only | lower | -5 | 정책지원만으로 현금흐름을 만들지 않는다. |
| tariff_relief_only | lower | -5 | 반덤핑 관세는 relief이지 건자재 실수요 증거가 아니다. |
| safety_incident_unresolved | lower | -5 | 안전 사고가 풀리지 않으면 수주보다 먼저 차단한다. |

## Easy Examples
- `Samsung E&A +8.5% on Fadhili order` is not Green until EPC margin and cash collection are visible.
- `Czech nuclear preferred bidder` is not final contract; legal appeals can keep it in 4C-watch.
- `40.6T KRW builder support` is relief, like oxygen. It is not proof the project can run and repay debt.
