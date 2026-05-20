# Round 250 R7 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- approval_clearance_or_launch_confirmed
- commercial_launch_after_approval
- commercial_revenue_or_royalty_recognition
- prescription_volume_or_procedure_volume
- reimbursement_payer_or_asp_confirmed
- hospital_adoption_or_channel_penetration
- royalty_milestone_or_supply_revenue_confirmed
- gross_margin_or_royalty_margin_confirmed
- capacity_utilization_or_contract_backlog
- cash_runway_and_dilution_risk_passed
- partner_execution_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- fda_approval_only
- clinical_headline_only
- external_validation_without_revenue
- policy_support_without_order
- mna_without_utilization
- facility_acquisition_without_backlog
- partner_pipeline_without_indication_success
- royalty_unconfirmed_platform_story
- medical_ai_auc_without_reimbursement
- patent_litigation_risk_unresolved
- cash_burn_or_dilution_risk

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| commercial_revenue | raise | 5 | 승인 뒤 실제 매출이 들어와야 R7 Stage 3 후보가 된다. |
| royalty_revenue_visibility | raise | 5 | 플랫폼 바이오는 royalty/supply revenue가 확인되어야 현금흐름 전환이다. |
| prescription_volume | raise | 5 | 신약은 처방량이 approval headline을 상업 성과로 바꾸는 증거다. |
| reimbursement_access | raise | 5 | 보험·수가 접근 없이는 병원 도입과 반복 매출 지속성이 약하다. |
| hospital_adoption | raise | 4 | 의료AI와 의료기기는 병원 도입 전까지 validation-only다. |
| capacity_utilization | raise | 5 | CDMO 공장·M&A는 가동률과 backlog가 있어야 이익으로 바뀐다. |
| contract_backlog | raise | 4 | CMO/CDMO는 계약 잔고가 시설 증설을 Stage 3 근거로 만든다. |
| gross_margin_visibility | raise | 4 | 의료 제품은 매출만큼 gross margin과 FCF 확인이 중요하다. |
| cash_runway | raise | 4 | 바이오 섹터는 cash runway와 dilution risk 통과가 필수다. |
| partner_execution_quality | raise | 5 | 대형 파트너도 임상·제조·출시 실행이 깨지면 RedTeam 근거다. |
| approval_news_only | lower | -5 | FDA 승인만으로 Stage 3-Green을 만들지 않는다. |
| clinical_headline_only | lower | -5 | 임상 headline은 revenue conversion 전 Stage 2에 그친다. |
| external_validation_without_revenue | lower | -5 | AUC나 외부검증은 수가·도입·반복매출 전 Green 근거가 아니다. |
| mna_without_utilization | lower | -5 | M&A 발표는 가동률·margin·FCF 전 event premium이다. |
| policy_support_without_order | lower | -4 | 정책지원은 회사별 주문·마진·FCF로 닫히기 전 Green이 아니다. |
| facility_acquisition_without_backlog | lower | -4 | 미국 공장 인수는 product transfer/backlog 전 Stage 2다. |
| partner_program_without_indication_success | lower | -5 | 파트너 pipeline 기대는 indication별 성공 전 Green 금지다. |
| patent_litigation_risk | lower | -4 | 특허분쟁은 royalty durability를 깎는 RedTeam 축이다. |
| cash_burn_or_dilution_risk | lower | -5 | 상업화 전 현금소진/희석 위험은 Green을 막는다. |
| subgroup_performance_risk | lower | -3 | 의료AI subgroup 약점은 실제 도입 리스크다. |

## Easy Examples
- `FDA approval` is Stage 2 attention. It is not Green until prescriptions, reimbursement, revenue, margin and cash runway follow.
- `AUC 0.91 medical AI validation` is useful evidence, but it is not commercial revenue.
- `M&A announcement +11.7%` is 4B/event premium until utilization, backlog, margin and FCF exist.
- `Partner trial failure` belongs in RedTeam even when Korean-stock OHLC is missing.
