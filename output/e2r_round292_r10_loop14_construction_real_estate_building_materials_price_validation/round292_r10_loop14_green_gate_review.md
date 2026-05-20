# Round 292 R10 Green Gate Review

Do not apply these weights to production scoring yet.

R10 Stage 3-Green is not `order`, `policy`, `preferred bidder`, `tariff relief`, or `localization capex`. It requires PF repayment, presales, cost margin, safety trust, EPC completion margin, ASP/volume, capex IRR, and price path after evidence.

## Required Fields

- PF_repayment_visibility_confirmed
- presale_absorption_confirmed
- construction_cost_margin_confirmed
- unbilled_receivables_control_confirmed
- safety_quality_trust_confirmed
- completion_margin_visibility_confirmed
- working_capital_advance_payment_confirmed
- final_contract_signing_confirmed
- building_material_ASP_volume_confirmed
- capex_IRR_funding_clarity_confirmed
- price_path_after_evidence

## Forbidden Patterns

- order_value_headline_only
- policy_support_headline_only
- property_supply_policy_only
- preferred_bidder_without_final_contract
- tariff_relief_without_ASP_margin
- capex_localization_without_IRR
- housing_price_rally_without_presales
- backlog_without_PF_cashflow
- safety_risk_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| PF_repayment_visibility | raise | 5 | 수주잔고보다 PF 상환과 refinancing visibility가 먼저다. |
| presale_absorption | raise | 5 | 분양률과 미분양 감소가 현금회수의 출발점이다. |
| construction_cost_margin | raise | 5 | 건설은 원가율이 닫혀야 이익이 현금으로 남는다. |
| unbilled_receivables_control | raise | 5 | 미청구공사 증가는 EPC/건설 4C-watch다. |
| safety_quality_trust | raise | 5 | 건설 안전과 품질 신뢰는 hard gate다. |
| completion_margin_visibility | raise | 5 | 해외 EPC 수주는 completion margin이 닫혀야 한다. |
| working_capital_advance_payment | raise | 5 | advance payment와 working capital 통제가 EPC 본체다. |
| final_contract_signing | raise | 4 | preferred bidder는 최종계약이 아니다. |
| building_material_ASP_volume | raise | 5 | 건자재는 ASP, 물량, 원가, 재고가 같이 필요하다. |
| capex_IRR_funding_clarity | raise | 5 | localization capex는 IRR과 funding clarity가 필요하다. |
| order_value_headline_only | lower | -5 | 수주금액 headline은 Stage 2일 수 있지만 Green은 아니다. |
| policy_support_headline_only | lower | -5 | 정책지원 headline만으로 PF cashflow를 만들지 않는다. |
| preferred_bidder_without_final_contract | lower | -5 | 우선협상대상자는 확정 매출과 다르다. |
| tariff_relief_without_ASP_margin | lower | -5 | 반덤핑 관세는 ASP와 margin으로 내려와야 한다. |
| capex_localization_without_IRR | lower | -5 | 미국 공장 투자는 IRR과 자금조달 전에는 false positive가 될 수 있다. |
| safety_risk_unresolved | lower | -5 | 안전 리스크 미해소는 Green을 막는다. |

## Easy Examples
- `$6B EPC order` is Stage 2 until margin and working capital close.
- `LTV/supply policy` is not builder Green until permits, starts, presales and PF cashflow appear.
- `fatal apartment collapse` is hard 4C because safety trust breaks before valuation.
