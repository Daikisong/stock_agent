# Round 263 R7 Green Gate Review

Do not apply these weights to production scoring yet.

R7 Stage 3-Green is not `FDA approval`, `M&A`, `AUC`, `K-aesthetic`, `AI diagnosis`, or `medical policy`. It requires procedure/prescription volume, installed base/utilization, consumables or repeat treatment, provider/hospital adoption, reimbursement or self-pay ASP, gross margin/FCF, safety trust, and price path after evidence.

## Required Fields

- procedure_or_prescription_volume_confirmed
- installed_base_or_utilization_confirmed
- consumable_or_repeat_treatment_revenue_confirmed
- provider_or_hospital_adoption_confirmed
- reimbursement_or_selfpay_asp_confirmed
- gross_margin_or_fcf_confirmed
- safety_counterfeit_and_unauthorized_distribution_risk_passed
- policy_or_service_disruption_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- fda_approval_only
- mna_rumor_only
- external_validation_only
- unlisted_or_delisted_asset_only
- device_viral_story_only
- unauthorized_toxin_distribution_risk_present
- medical_service_capacity_disruption_present
- subgroup_performance_weakness_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| procedure_volume | raise | 5 | R7 Green은 실제 시술량이나 처방량이 확인되어야 한다. |
| device_installed_base | raise | 5 | 미용의료기기는 설치대수와 utilization이 반복매출의 출발점이다. |
| consumable_attach_rate | raise | 5 | 소모품 attach-rate가 있어야 단발 장비판매가 아니다. |
| repeat_treatment_frequency | raise | 5 | 반복 시술 빈도가 procedure TAM을 현금흐름으로 바꾼다. |
| provider_adoption | raise | 5 | 톡신과 의료AI는 provider/hospital adoption 전까지 Stage 2다. |
| reimbursement_or_selfpay_conversion | raise | 4 | 보험·수가 또는 self-pay ASP가 매출 지속성을 만든다. |
| gross_margin_visibility | raise | 5 | 의료기기와 톡신은 gross margin과 FCF 확인이 중요하다. |
| regulatory_safety_trust | raise | 5 | 안전·위조·비공식 유통 리스크가 Green을 막는다. |
| commercial_revenue_conversion | raise | 5 | 승인·논문·M&A가 실제 매출로 전환되어야 한다. |
| cash_conversion | raise | 4 | 성장률보다 FCF 전환이 Stage 3 품질을 결정한다. |
| approval_headline_only | lower | -5 | FDA 승인만으로 Stage 3-Green을 만들지 않는다. |
| M&A_rumor_only | lower | -5 | M&A rumor는 확인 전 event premium이다. |
| external_validation_without_revenue | lower | -5 | AUC와 외부검증은 상환·병원도입·매출 전 Green 근거가 아니다. |
| device_viral_demand_only | lower | -4 | viral device 수요만으로 반복매출을 발명하지 않는다. |
| unlisted_subsidiary_or_delisted_tracking_gap | lower | -4 | 비상장·상폐 자산은 상장주 Stage 3 추적을 제한한다. |
| unauthorized_distribution_risk | lower | -5 | 비공식 톡신 유통은 safety/trust 4C-watch다. |
| safety_or_counterfeit_toxin_risk | lower | -5 | 위조·미승인 톡신 리스크는 제품 신뢰를 훼손한다. |
| medical_service_disruption | lower | -4 | 의사파업·정책 disruption은 procedure volume을 교란한다. |
| subgroup_performance_weakness | lower | -4 | 의료AI subgroup weakness는 deployment risk다. |

## Easy Examples
- `FDA approval` is Stage 2; Green needs repeat procedures and ASP/margin.
- `AUC 0.91` is useful validation; Green needs reimbursement and hospital adoption.
- `ZimVie +12.5% on rumor` is M&A event premium, not Korean listed Stage 3.
