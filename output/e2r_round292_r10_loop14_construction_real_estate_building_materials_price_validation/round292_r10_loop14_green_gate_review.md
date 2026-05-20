# Round 292 R10 Green Gate Review

Do not apply these weights to production scoring yet.

R10 Stage 3-Green is not `large order`, `policy support`, `preferred bidder`, `tariff relief`, or `localization capex`. It requires PF repayment, presale absorption, cost margin, unbilled receivables control, safety/quality trust, completion margin, working capital, final contract, ASP/volume, capex IRR/funding clarity, and price path after evidence.

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
| PF_repayment_visibility | raise | 5 | 건설사는 수주잔고보다 PF 상환과 차환 비용이 먼저다. |
| presale_absorption | raise | 5 | 분양률과 미분양 감소가 현금회수의 출발점이다. |
| construction_cost_margin | raise | 5 | 원가율이 닫히지 않으면 매출 증가가 이익으로 내려오지 않는다. |
| unbilled_receivables_control | raise | 5 | 미청구공사 증가는 EPC/건설의 핵심 4C-watch다. |
| safety_quality_trust | raise | 5 | 사망 안전사고와 품질 붕괴는 hard gate다. |
| completion_margin_visibility | raise | 5 | 해외 EPC는 완공마진과 claim risk까지 봐야 한다. |
| working_capital_advance_payment | raise | 5 | advance payment와 운전자본 통제가 cashflow를 만든다. |
| final_contract_signing | raise | 4 | preferred bidder는 최종계약이 아니다. |
| building_material_ASP_volume | raise | 5 | 건자재는 ASP와 물량, 원가 spread가 같이 닫혀야 한다. |
| capex_IRR_funding_clarity | raise | 5 | localization capex는 IRR과 funding plan이 없으면 Green이 아니다. |
| order_value_headline_only | lower | -5 | 수주금액 headline만으로 completion margin을 만들지 않는다. |
| policy_support_headline_only | lower | -5 | 정책지원 headline만으로 PF 현금흐름을 만들지 않는다. |
| property_supply_policy_only | lower | -5 | 공급정책만으로 착공·분양·현금회수가 생기지 않는다. |
| preferred_bidder_without_final_contract | lower | -5 | 우선협상대상자는 booked margin이 아니다. |
| tariff_relief_without_ASP_margin | lower | -5 | 관세 relief는 ASP와 margin 확인 전에는 event premium이다. |
| capex_localization_without_IRR | lower | -5 | 미국공장 headline은 IRR/funding 전에는 false positive가 될 수 있다. |
| backlog_without_PF_cashflow | lower | -5 | PF cashflow가 막히면 backlog는 Green 방어가 안 된다. |
| safety_risk_unresolved | lower | -5 | 안전 리스크 미해소는 건설 Green을 막는다. |

## Easy Examples
- `6B USD EPC order` is useful, but Green needs advance payment, cost lock-in and completion margin.
- `LTV changes or state-land supply` is useful, but Green needs actual starts, presales and cash collection.
- `fatal construction collapse` is hard 4C because safety and quality trust breaks before any backlog thesis.
