# Round 276 R7 Green Gate Review

Do not apply these weights to production scoring yet.

R7 Stage 3-Green is not `FDA approval`, `CDMO facility`, `platform technology`, `medical-device M&A`, `policy support`, or `government procurement`. It requires prescription ramp, royalty/milestone cash, capacity utilization, regulatory quality, device usage, reimbursement, and FCF.

## Required Fields

- actual_prescription_ramp_confirmed
- royalty_milestone_cashflow_confirmed
- commercial_launch_execution_confirmed
- cdmo_capacity_utilization_confirmed
- customer_transfer_success_confirmed
- regulatory_quality_clearance_confirmed
- reimbursement_and_access_confirmed
- device_clinic_utilization_confirmed
- recurring_consumables_or_service_revenue_confirmed
- ex_policy_margin_fcf_confirmed
- price_path_after_evidence

## Forbidden Patterns

- FDA_approval_without_sales_bridge
- platform_tech_without_royalty_cash
- CDMO_facility_acquisition_only
- policy_tariff_support_only
- M&A_without_utilization
- vaccine_procurement_without_demand
- device_takeout_not_tradeable
- patent_or_CRL_overhang

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| actual_prescription_ramp | raise | 5 | 신약 Green은 승인보다 실제 처방 ramp가 중요하다. |
| royalty_milestone_cashflow | raise | 5 | 플랫폼/라이선스는 royalty와 milestone 현금흐름으로 닫혀야 한다. |
| commercial_launch_execution | raise | 5 | 승인 이후 출시 실행과 접근성이 확인되어야 한다. |
| CDMO_capacity_utilization | raise | 5 | CDMO 시설은 capacity가 아니라 utilization이 Green 근거다. |
| customer_transfer_success | raise | 5 | 미국 공장은 고객 이전과 제품 이전이 확인되어야 한다. |
| regulatory_quality_clearance | raise | 5 | CMC/FDA inspection과 patent gate를 통과해야 한다. |
| reimbursement_and_access | raise | 5 | 처방·시술은 reimbursement/access가 있어야 매출로 전환된다. |
| device_clinic_utilization | raise | 5 | 의료기기는 clinic utilization이 실제 수요다. |
| recurring_consumables_or_service | raise | 4 | 장비 판매보다 반복 소모품/서비스 매출이 질을 만든다. |
| ex_policy_margin_FCF | raise | 5 | 정책 지원 후에도 margin과 FCF로 닫혀야 한다. |
| FDA_approval_without_sales_bridge | lower | -4 | FDA approval만으로 Stage 3-Green을 만들지 않는다. |
| platform_tech_without_royalty_cash | lower | -5 | 플랫폼 기술 headline은 royalty cash 전에는 option이다. |
| CDMO_facility_acquisition_only | lower | -5 | 공장 인수만으로 utilization과 margin을 발명하지 않는다. |
| policy_tariff_support_only | lower | -5 | 정책지원은 company margin bridge 전에는 event premium이다. |
| M&A_without_utilization | lower | -5 | M&A pop은 order book/utilization 전에는 4B-watch다. |
| vaccine_procurement_without_demand | lower | -5 | 정부 구매가 실제 접종 수요를 뜻하지 않는다. |
| device_takeout_not_tradeable | lower | -3 | take-private benchmark는 상장 Stage 3 추적이 어렵다. |
| patent_or_CRL_overhang | lower | -5 | CRL/patent overhang은 launch ramp를 막을 수 있다. |

## Easy Examples
- `Yuhan FDA approval` is Stage 2; Green needs prescription ramp and royalty cashflow.
- `Samsung Bio U.S. facility` is Stage 2; Green needs utilization and customer transfer.
- `SkyCovione 10M doses purchased` failed because only 3,787 shots were administered.
