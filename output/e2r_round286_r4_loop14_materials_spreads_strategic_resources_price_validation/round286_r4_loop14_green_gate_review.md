# Round 286 R4 Green Gate Review

Do not apply these weights to production scoring yet.

R4 Stage 3-Green is not `spread`, `tariff`, `control premium`, `lithium`, or `rare earth` as a label. It requires spread/margin realization, executed restructuring, customer call-off, offtake utilization, export-license continuity and FCF-quality evidence.

## Required Fields

- spread_margin_realization_confirmed
- capacity_cut_actual_execution_confirmed
- plant_shutdown_discipline_confirmed
- commodity_price_sensitivity_measured
- customer_calloff_visibility_confirmed
- contract_value_durability_confirmed
- resource_offtake_utilization_confirmed
- export_license_continuity_confirmed
- governance_dilution_control_confirmed
- inventory_valuation_risk_controlled
- price_path_after_evidence

## Forbidden Patterns

- commodity_rebound_headline_only
- tariff_relief_only
- control_premium_only
- capacity_restructuring_policy_only
- mine_stake_without_processing_margin
- CATL_license_suspension_sentiment
- nonbinding_supply_agreement
- signed_contract_without_calloff
- rare_earth_truce_without_actual_exports

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| spread_margin_realization | raise | 5 | 소재/화학은 가격보다 제품 스프레드와 현금마진이 먼저다. |
| capacity_cut_actual_execution | raise | 5 | 구조조정은 발표가 아니라 실제 shutdown과 공급규율이 필요하다. |
| customer_calloff_visibility | raise | 5 | 장기 소재 계약은 실제 고객 call-off가 있어야 매출이 된다. |
| contract_value_durability | raise | 5 | 초기 계약금액이 줄어들면 Stage 4C가 될 수 있다. |
| resource_offtake_utilization | raise | 5 | 광산 지분은 offtake와 가공설비 utilization으로 닫혀야 한다. |
| export_license_continuity | raise | 5 | 희토류/전략자원은 실제 수출허가와 선적 지속성이 핵심이다. |
| governance_dilution_control | raise | 5 | 지배권 프리미엄은 희석·거버넌스 통과 전에는 operating Green이 아니다. |
| inventory_valuation_risk_controlled | raise | 4 | 리튬·양극재는 재고평가손실과 판가연동을 같이 봐야 한다. |
| commodity_rebound_headline_only | lower | -5 | 상품가격 반등 headline만으로 Green을 만들지 않는다. |
| tariff_relief_only | lower | -5 | 반덤핑 관세는 수요와 스프레드가 없으면 event premium이다. |
| control_premium_only | lower | -5 | 지배권 프리미엄은 FCF 증거가 아니다. |
| capacity_restructuring_policy_only | lower | -5 | 정책 지원만 있고 스프레드 회복이 없으면 Stage 2다. |
| mine_stake_without_processing_margin | lower | -5 | 광산 지분만 있고 가공마진이 없으면 Green 금지다. |
| CATL_license_suspension_sentiment | lower | -5 | CATL 허가 중단 감성 랠리는 마진 확인 전 event premium이다. |
| nonbinding_supply_agreement | lower | -5 | non-binding lithium agreement는 계약/마진으로 보지 않는다. |
| signed_contract_without_calloff | lower | -5 | 서명 계약만 있고 실제 발주가 없으면 Stage 4C 리스크다. |
| rare_earth_truce_without_actual_exports | lower | -5 | 희토류 휴전 headline은 실제 수출량 회복 전 Green이 아니다. |

## Easy Examples
- `anti-dumping tariff` can lift steel shares, but without actual steel spread and demand it remains event premium.
- `mine stake acquisition` is Stage 2 until offtake, processing utilization and customer call-off confirm.
- `rare-earth export control` is a supply-chain RedTeam input; it is not automatic beneficiary evidence.
