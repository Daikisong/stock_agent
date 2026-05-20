# Round 237 R7 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- approval_clearance_or_launch_confirmed
- commercial_launch_after_approval
- commercial_revenue_or_royalty_recognition
- prescription_procedure_volume_or_hospital_adoption
- reimbursement_payer_access_or_asp_confirmed
- capacity_utilization_or_channel_penetration
- gross_margin_or_fcf_visibility
- repeat_treatment_consumables_or_contract_backlog
- cash_runway_and_dilution_risk_passed
- partner_execution_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- approval_news_only
- clinical_headline_only
- external_validation_without_revenue
- mna_without_utilization
- take_private_premium_only
- fda_approval_without_commercial_sales
- partner_pipeline_without_indication_success
- pre_revenue_medical_ai_story
- cash_burn_or_dilution_risk
- subgroup_performance_risk
- facility_acquisition_without_product_transfer
- us_launch_without_channel_sales

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| commercial_revenue | raise | 5 | 승인·출시 이후 실제 매출이 보여야 R7 Stage 3 후보가 된다. |
| prescription_or_procedure_volume | raise | 5 | 처방량·시술량은 제품이 실제 사용으로 바뀌는 증거다. |
| channel_penetration | raise | 5 | 미국 launch나 미용기기는 병의원 채널 침투가 핵심이다. |
| reimbursement_access | raise | 5 | 보험·수가 접근이 없으면 의료 제품 매출 지속성이 약하다. |
| capacity_utilization | raise | 5 | CDMO/CMO는 공장 보유보다 가동률과 제품 이전이 핵심이다. |
| contract_backlog | raise | 4 | CMO/CDMO는 고객 계약과 backlog가 Stage 3 visibility를 만든다. |
| gross_margin_visibility | raise | 4 | 매출이 있어도 gross margin이 확인돼야 EPS/FCF 체급 변화로 이어진다. |
| cash_runway | raise | 4 | 상업화 전 현금 runway가 부족하면 희석 리스크가 먼저다. |
| repeat_treatment_or_consumables | raise | 4 | 미용기기와 보툴리눔은 반복 시술·소모품 구조가 visibility를 만든다. |
| hospital_adoption | raise | 4 | 의료AI는 논문보다 병원 도입과 반복 사용이 중요하다. |
| approval_news_only | lower | -5 | 승인 뉴스만으로는 Stage 3-Green을 만들 수 없다. |
| clinical_headline_only | lower | -5 | 임상 헤드라인은 처방·매출·로열티 전까지 Stage 2 watch다. |
| external_validation_without_revenue | lower | -4 | 논문 성능은 좋지만 수가·도입·반복매출 없이는 Green 금지다. |
| mna_without_utilization | lower | -5 | M&A 발표만 있고 가동률·마진이 없으면 event premium이다. |
| take_private_premium_only | lower | -4 | take-private valuation은 peer Green 조건이 아니라 Stage 2 이벤트다. |
| fda_approval_without_commercial_sales | lower | -4 | FDA approval 이후 상업 매출이 없으면 Stage 3 보류다. |
| partner_pipeline_without_indication_success | lower | -4 | 파트너 pipeline 기대는 indication별 성공 전까지 제한한다. |
| pre_revenue_medical_ai_story | lower | -5 | pre-revenue 의료AI는 수가와 병원 도입 전 Green 금지다. |
| cash_burn_or_dilution_risk | lower | -5 | 대규모 희석이나 cash runway 붕괴는 Green hard blocker다. |
| subgroup_performance_risk | lower | -3 | 의료AI subgroup 성능 약점은 실제 도입 리스크다. |

## Easy Examples
- `FDA approval` means Stage 2 attention. It is not Green until sales, reimbursement, margin, and cash runway follow.
- `M&A announcement + same-day price spike` is 4B/event premium until utilization, backlog, margin, and FCF exist.
- `AUC 0.91 medical AI validation` is useful evidence, but reimbursement and hospital adoption are the Green gate.
- `Partner trial failure` is RedTeam evidence even when the Korean stock OHLC is missing.
