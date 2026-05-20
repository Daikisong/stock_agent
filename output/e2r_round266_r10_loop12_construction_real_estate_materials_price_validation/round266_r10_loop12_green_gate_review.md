# Round 266 R10 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- final_contract_signed
- scope_value_payment_schedule_confirmed
- progress_revenue_or_delivery_milestone_confirmed
- construction_margin_or_opm_confirmed
- working_capital_and_receivables_stable
- cash_collection_quality_confirmed
- legal_appeal_permit_license_risk_cleared
- safety_incident_absent_or_remediated
- presales_unsold_inventory_pf_stability_confirmed
- price_path_after_evidence

## Forbidden Patterns

- preferred_bidder_only
- talks_or_parliament_nod_only
- candidate_consortium_only
- public_infra_headline_only
- housing_policy_only
- safety_incident_unresolved
- legal_appeal_pending
- building_material_demand_break

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| final_contract_signed | raise | 5 | R10 원전/EPC는 preferred bidder가 아니라 final contract가 핵심이다. |
| progress_revenue_visibility | raise | 5 | 공정률과 진행매출이 보여야 수주가 EPS/FCF로 닫힌다. |
| construction_margin_visibility | raise | 5 | 건설은 계약금액보다 원가율과 OPM 확인이 중요하다. |
| working_capital_control | raise | 5 | 미청구공사·매출채권이 흔들리면 수주가 현금으로 닫히지 않는다. |
| cash_collection_quality | raise | 5 | 현금회수 확인 전에는 대형 프로젝트도 Stage 2다. |
| safety_execution_trust | raise | 5 | 건설 안전 신뢰는 R10 hard gate다. |
| permit_and_legal_clearance | raise | 5 | 법적 항소와 인허가가 풀려야 프로젝트가 실적이 된다. |
| presales_and_unsold_inventory | raise | 5 | 주택정책은 분양률, 미분양, PF 안정으로 확인해야 한다. |
| building_material_spread | raise | 4 | 건자재는 수요, spread, inventory, FCF가 함께 회복돼야 한다. |
| public_contract_award_quality | raise | 4 | 공공공사는 실제 낙찰사와 계약금액이 있어야 한다. |
| preferred_bidder_only | lower | -5 | preferred bidder는 Stage 2 후보일 뿐 Green이 아니다. |
| talks_or_MOU_only | lower | -5 | 협상 승인과 MOU는 final EPC contract가 아니다. |
| public_infra_headline_only | lower | -5 | 공공청사 headline은 listed contractor award 전 Green이 아니다. |
| housing_policy_only | lower | -5 | 주택정책은 presales/margin/PF 확인 전 event premium이다. |
| candidate_consortium_only | lower | -5 | 컨소시엄 후보군은 award가 아니다. |
| safety_incident | lower | -5 | 치명적 안전사고는 수주·정책 점수를 덮는 4C gate다. |
| recurring_fatality_risk | lower | -5 | 반복 사망사고는 벌금과 면허 리스크를 만든다. |
| license_revocation_risk | lower | -5 | 면허취소 가능성은 R10 Green을 차단한다. |
| rebar_demand_weakness | lower | -4 | 철근 수요 약화는 건자재 spread와 이익을 깨뜨린다. |
| legal_appeal_pending | lower | -4 | 법적 항소가 남아 있으면 final contract cashflow로 볼 수 없다. |

## Easy Examples
- `preferred bidder` is Stage 2 until final contract, legal clearance, scope, margin and cash collection are visible.
- `housing policy` is event premium until presales, PF stability, unsold inventory and FCF are visible.
- `public-infra headline` is not Green until a listed contractor wins a contract with value and margin.
