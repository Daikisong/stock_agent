# Round 247 R4 Green Gate Review

Do not apply these weights to production scoring yet.

R4 Stage 3-Green is not `commodity price up`, `strategic minerals`, `tariff relief`, `restructuring`, or `unconfirmed customer media`. It requires spread, offtake, cost curve, contract quality, FCF and risk clearance.

## Required Fields

- product_spread_confirmed
- cost_curve_advantage
- supply_discipline_or_capacity_shutdown_confirmed
- offtake_price_floor_or_take_or_pay
- fcf_after_working_capital
- contract_quality_confirmed
- china_tariff_sanction_governance_risk_passed
- capex_burden_and_dilution_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- commodity_price_spike_only
- strategic_material_headline_only
- policy_relief_only
- unconfirmed_media_report
- restructuring_plan_only
- customer_name_only_material_contract
- resource_deal_without_offtake
- governance_dilution_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| product_spread | raise | 5 | R4는 원자재 가격보다 제품 spread 확인이 먼저다. |
| cost_curve_advantage | raise | 5 | 가격 하락에도 FCF가 버티려면 cost curve 우위가 필요하다. |
| offtake_quality | raise | 5 | 전략자원은 offtake, price floor, take-or-pay가 있어야 cycle과 분리된다. |
| contract_quality | raise | 5 | 소재 계약은 고객명보다 call-off, volume, margin 변환이 중요하다. |
| FCF_after_working_capital | raise | 5 | 재고와 운전자본 이후 현금흐름이 남아야 구조적이다. |
| supply_discipline_confirmed | raise | 5 | 설비중단과 공급규율은 spread 지속성을 높인다. |
| capacity_shutdown_confirmed | raise | 4 | Daesan NCC shutdown처럼 확정된 설비 조정은 Stage 2 relief다. |
| China_exposure_reduction | raise | 4 | 중국 공급망 의존 완화는 Stage 2 품질을 높인다. |
| resource_security_with_downstream_margin | raise | 4 | resource security는 downstream margin과 연결될 때 강하다. |
| governance_cleanliness | raise | 4 | 전략광물 프로젝트도 dilution/governance가 깨끗해야 Green 후보가 된다. |
| commodity_price_up_only | lower | -5 | 가격 상승만으로 EPS/FCF 체급 변화를 증명하지 못한다. |
| strategic_material_headline_only | lower | -5 | 전략광물 headline만으로 Green 금지다. |
| policy_relief_only | lower | -5 | 정책 relief는 spread/FCF 확인 전 event premium이다. |
| unconfirmed_media_report | lower | -5 | 미확정 고객 보도는 Stage 3 근거가 아니다. |
| restructuring_plan_without_margin | lower | -4 | 구조조정 계획은 margin 회복 전 Stage 2 watch다. |
| capacity_cut_without_spread_recovery | lower | -4 | capacity cut만으로 petrochemical Green을 만들 수 없다. |
| contract_headline_without_calloff | lower | -5 | 실제 call-off 없는 계약 headline은 L&F hard 4C의 반례다. |
| customer_name_without_volume | lower | -5 | 고객명은 volume/margin 전환 전까지 visibility가 아니다. |
| governance_dilution_risk | lower | -5 | share issuance와 control fight는 RedTeam 입력이다. |
| China_customer_or_supply_chain_concentration | lower | -4 | 중국 고객/공급망 집중은 tariff/sanction risk를 키운다. |

## Easy Examples
- `anti-dumping tariff relief` is Stage 2 attention until steel spread and export margin confirm.
- `SpaceX supply talk` is event premium while the customer and contract are unconfirmed.
- `Tesla customer name` is not Green if the actual contract value collapses.
