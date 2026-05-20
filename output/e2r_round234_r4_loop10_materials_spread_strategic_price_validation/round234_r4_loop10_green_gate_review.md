# Round 234 R4 Green Gate Review

Do not apply these weights to production scoring yet.

R4 Stage 3-Green is not `strategic mineral`, `restructuring`, `lithium`, `tariff hedge`, or `M&A optionality`. It requires spread, offtake, cost curve, FCF, and risk clearance.

## Required Fields

- actual_product_spread
- cost_curve_advantage
- supply_discipline_or_capacity_shutdown
- inventory_build_absent
- fcf_after_working_capital
- price_floor_or_offtake
- medium_term_eps_revision
- capex_and_dilution_risk_passed
- policy_tariff_sanction_stress_passed
- price_path_after_evidence

## Forbidden Patterns

- commodity_price_spike_only
- strategic_material_headline_only
- tender_offer_premium
- governance_battle_only
- policy_support_without_fcf
- unconfirmed_media_report
- mna_rumor_without_transaction
- restructuring_plan_without_margin
- lithium_or_polysilicon_price_event_only
- customer_name_contract_headline_without_calloff

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| actual_product_spread | raise | 5 | R4는 원자재 가격보다 제품 spread 확인이 먼저다. |
| fcf_after_working_capital | raise | 5 | 재고와 운전자본 이후 FCF가 남아야 구조적이다. |
| supply_discipline_confirmed | raise | 5 | 설비중단/공급규율이 확인되어야 spread 회복이 지속된다. |
| capacity_shutdown_confirmed | raise | 4 | Daesan NCC shutdown처럼 확정된 설비 조정은 Stage 2 relief다. |
| price_floor_or_offtake | raise | 5 | 전략자원은 offtake/price floor가 있어야 commodity cycle과 분리된다. |
| cost_curve_advantage | raise | 4 | cost curve 우위가 있어야 가격 하락에도 FCF가 버틴다. |
| strategic_customer_or_government_offtake | raise | 4 | 정부/전략 고객의 실제 offtake가 있으면 visibility가 강해진다. |
| inventory_normalization | raise | 4 | 재고 축소는 spread 회복의 품질을 높인다. |
| tariff_resilience | raise | 4 | 관세 환경에서 수출마진이 방어되는지 확인한다. |
| resource_security_with_downstream_margin | raise | 4 | resource security는 downstream margin과 연결될 때 강하다. |
| contract_quality | raise | 5 | 소재 계약은 금액보다 call-off, volume, margin 변환이 중요하다. |
| commodity_price_up_only | lower | -5 | 원자재 가격 상승만으로는 EPS/FCF 체급 변화를 증명하지 못한다. |
| strategic_material_headline_only | lower | -4 | 전략광물 headline만으로 Green 금지다. |
| governance_premium_only | lower | -5 | 경영권/공개매수 premium은 구조적 Stage 3와 분리한다. |
| share_issue_dilution | lower | -5 | 대규모 신주발행과 dilution은 RedTeam 입력이다. |
| restructuring_plan_without_margin | lower | -4 | 구조조정 계획은 margin/FCF 회복 전 Stage 2 watch다. |
| policy_capex_without_funding | lower | -5 | funding/margin 불명확한 정책 CAPEX는 false-positive 위험이다. |
| mna_rumor_without_transaction | lower | -5 | 확정되지 않은 M&A rumor는 event premium이다. |
| unconfirmed_media_report | lower | -5 | 미확정 고객 보도는 Green 근거가 아니다. |
| lithium_price_event | lower | -5 | 리튬 가격 이벤트는 company-level margin/FCF 전 event premium이다. |
| contract_headline_without_calloff | lower | -5 | 고객명과 계약금액 headline만으로 Green 금지다. |
| capex_heavy_project_pre_revenue | lower | -4 | 상업가동 전 대형 CAPEX는 FCF/dilution risk가 크다. |

## Easy Examples
- `lithium price rebound` is event premium until downstream margin and FCF confirm.
- `M&A rumor` is Stage 1 attention or 4B-watch until a signed transaction exists.
- `Tesla customer name` is not Green if actual contract value collapses.
