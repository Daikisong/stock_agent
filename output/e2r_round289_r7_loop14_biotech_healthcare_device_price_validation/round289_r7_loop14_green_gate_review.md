# Round 289 R7 Green Gate Review

Do not apply these weights to production scoring yet.

R7 Stage 3-Green is not `FDA approval`, `CMO facility`, `tech export`, `Keytruda`, `U.S. factory`, or `medical-aesthetic launch`. It requires launch conversion, utilization, royalty probability, partner execution, IP freedom, reimbursement, physician adoption, and price path after evidence.

## Required Fields

- fda_approval_to_launch_conversion_confirmed
- royalty_milestone_probability_confirmed
- facility_utilization_confirmed
- fda_inspection_and_tech_transfer_confirmed
- cmo_recurring_order_visibility_confirmed
- clinical_endpoint_quality_confirmed
- partner_execution_quality_confirmed
- patent_ip_freedom_to_operate_confirmed
- reimbursement_and_market_access_confirmed
- physician_adoption_sellthrough_confirmed
- price_path_after_evidence

## Forbidden Patterns

- FDA_headline_only
- facility_acquisition_only
- CMO_capacity_without_utilization
- tech_export_upfront_only
- early_stage_deal_without_phase2_3
- approval_without_reimbursement
- aesthetic_launch_without_doctor_adoption
- patent_dispute_unresolved
- clinical_hold_or_CRL

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| FDA_approval_to_launch_conversion | raise | 5 | 승인 headline은 launch와 접근성으로 닫혀야 한다. |
| royalty_milestone_probability | raise | 5 | 기술수출과 라이선스는 마일스톤/로열티 확률이 중요하다. |
| facility_utilization | raise | 5 | CMO/CDMO 시설은 capacity가 아니라 가동률이 Green 근거다. |
| FDA_inspection_and_tech_transfer | raise | 5 | 미국 공장과 바이오 생산은 inspection/tech transfer gate를 통과해야 한다. |
| CMO_recurring_order_visibility | raise | 5 | 반복 주문과 batch slot이 있어야 매출 visibility가 생긴다. |
| clinical_endpoint_quality | raise | 5 | 임상은 headline보다 endpoint quality가 valuation을 지탱한다. |
| partner_execution_quality | raise | 5 | global partner 이름보다 실제 실행력이 중요하다. |
| patent_IP_freedom_to_operate | raise | 5 | SC formulation과 platform tech는 patent/IP gate가 핵심이다. |
| reimbursement_and_market_access | raise | 5 | 승인 후 보험/market access가 있어야 매출 전환이 가능하다. |
| physician_adoption_sellthrough | raise | 4 | 의료미용은 doctor adoption과 sell-through가 실제 수요다. |
| FDA_headline_only | lower | -5 | FDA headline만으로 Stage 3-Green을 만들지 않는다. |
| facility_acquisition_only | lower | -5 | 공장 인수만으로 가동률과 마진을 발명하지 않는다. |
| CMO_capacity_without_utilization | lower | -5 | CMO capacity는 utilization 전에는 Stage 2다. |
| tech_export_upfront_only | lower | -5 | upfront만 있고 Phase 2/3·마일스톤 확률이 없으면 Green이 아니다. |
| early_stage_deal_without_phase2_3 | lower | -5 | 초기 임상 기술수출은 strong option이지 Green 근거가 아니다. |
| approval_without_reimbursement | lower | -4 | 승인 후 접근성/보험이 없으면 매출 bridge가 약하다. |
| aesthetic_launch_without_doctor_adoption | lower | -4 | 의료미용 launch는 physician adoption 전에는 과열 가능성이 있다. |
| patent_dispute_unresolved | lower | -5 | patent dispute가 남으면 royalty/adoption을 유예한다. |
| clinical_hold_or_CRL | lower | -5 | clinical hold/CRL은 hard 4C 후보로 본다. |

## Easy Examples
- `Samsung Bio U.S. facility` is Stage 2; Green needs utilization and margin.
- `Alteogen Keytruda Qlex approval` is a Stage 3 candidate; Green waits for adoption, royalty and patent clarity.
- `ADEL $1.04B deal` is Stage 2 reference; Green cannot be inferred from upfront alone.
