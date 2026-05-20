# Round 285 R3 Green Gate Review

Do not apply these weights to production scoring yet.

R3 Stage 3-Green is not `battery`, `EV`, `IRA`, `solar`, `hydrogen`, `ESS`, or `silicon anode` as a label. It requires customer call-off, utilization, battery content, policy durability, customs clearance, PO value, margin and FCF.

## Required Fields

- customer_calloff_visibility_confirmed
- contract_cancellation_risk_cleared
- plant_utilization_confirmed
- EV_model_mix_battery_content_confirmed
- subsidy_tariff_policy_stability_confirmed
- ESS_PO_value_and_margin_confirmed
- supply_chain_customs_clearance_confirmed
- localization_execution_confirmed
- raw_material_cost_pass_through_confirmed
- listed_value_bridge_for_unlisted_tech_confirmed
- price_path_after_evidence

## Forbidden Patterns

- EV_growth_headline_only
- signed_contract_without_calloff
- capacity_capex_without_utilization
- IRA_or_policy_loan_only
- ESS_pivot_without_contract_value
- hybrid_shift_ignored
- unlisted_material_tech_readthrough
- solar_factory_without_customs_clearance
- hydrogen_capex_without_demand

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| customer_calloff_visibility | raise | 5 | 배터리 계약은 실제 call-off와 shipment가 보여야 강하다. |
| contract_cancellation_risk | raise | 5 | 대형 고객 계약 취소는 expected revenue와 utilization을 직접 깬다. |
| plant_utilization | raise | 5 | 공장·JV·capex는 utilization이 있어야 EPS/FCF로 연결된다. |
| EV_model_mix_battery_content | raise | 5 | BEV에서 hybrid/EREV로 바뀌면 차량당 battery content가 줄 수 있다. |
| subsidy_tariff_policy_stability | raise | 5 | IRA/AMPC/관세/보조금은 지속성과 실질 이익 품질을 확인해야 한다. |
| ESS_PO_value_and_margin | raise | 5 | ESS pivot은 PO value, installation, margin이 있어야 Stage 3로 간다. |
| supply_chain_customs_clearance | raise | 5 | 태양광·배터리 현지화는 customs clearance가 막히면 utilization이 무너진다. |
| localization_execution | raise | 4 | 현지화는 공장 착공보다 부품 흐름, 인력, 가동률이 중요하다. |
| raw_material_cost_pass_through | raise | 4 | 소재주는 원재료 가격과 판가연동, 재고손실을 같이 봐야 한다. |
| listed_value_bridge_for_unlisted_tech | raise | 4 | 비상장 소재 기술은 상장사 EPS/value bridge가 있어야 한다. |
| EV_growth_headline_only | lower | -5 | EV 장기성장 단어만으로 Stage 3를 만들지 않는다. |
| signed_contract_without_calloff | lower | -5 | 계약 체결만 있고 실제 call-off가 없으면 제한한다. |
| capacity_capex_without_utilization | lower | -5 | capacity capex는 utilization 전에는 현금소모일 수 있다. |
| IRA_or_policy_loan_only | lower | -5 | 정책자금이나 IRA headline은 이익 품질이 아니다. |
| ESS_pivot_without_contract_value | lower | -5 | ESS pivot은 계약가와 margin이 없으면 Stage 2에 머문다. |
| hybrid_shift_ignored | lower | -5 | hybrid 전환은 battery content 감소 리스크다. |
| unlisted_material_tech_readthrough | lower | -4 | 비상장 기술 성과를 상장사 EPS로 바로 연결하지 않는다. |
| solar_factory_without_customs_clearance | lower | -5 | 태양광 공장은 통관과 부품 흐름 없이는 Green이 아니다. |
| hydrogen_capex_without_demand | lower | -4 | 수소 공장 착공은 고객 수요와 unit economics 전에는 Stage 2다. |

## Easy Examples
- `EV battery contract` becomes weaker if the automaker cancels the model or stops call-off.
- `ESS pivot` is useful Stage 2 evidence, but Green waits for PO value, installation and margin.
- `U.S. solar factory` still fails if components are stuck at customs and utilization drops.
