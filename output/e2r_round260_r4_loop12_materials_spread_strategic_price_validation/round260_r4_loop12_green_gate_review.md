# Round 260 R4 Green Gate Review

Do not apply these weights to production scoring yet.

R4 Stage 3-Green is not `strategic minerals`, `tariff`, `policy support`, `M&A rumor`, `U.S. CAPEX`, or `restructuring`. It requires spread, offtake, cost curve, working capital, FCF and risk clearance.

## Required Fields

- product_spread_confirmed
- cost_curve_advantage_confirmed
- offtake_price_floor_or_take_or_pay_confirmed
- supply_discipline_or_capacity_shutdown_confirmed
- restructuring_after_opm_fcf_improvement
- working_capital_stable
- china_tariff_rare_earth_end_use_risk_passed
- dilution_governance_risk_passed
- price_path_after_evidence

## Forbidden Patterns

- mna_rumor_only
- policy_relief_only
- strategic_material_headline_only
- us_capex_without_roi
- capacity_shutdown_without_spread_recovery
- restructuring_plan_undisclosed
- rare_earth_end_use_restriction_present
- tariff_export_risk_unresolved
- dilution_for_project_capex_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| product_spread | raise | 5 | R4는 전략자원 headline보다 제품 spread 확인이 먼저다. |
| cost_curve_advantage | raise | 5 | 원가곡선 우위가 있어야 spread가 흔들려도 FCF가 남는다. |
| offtake_quality | raise | 5 | 전략광물은 offtake, price floor, take-or-pay로 cycle과 분리되어야 한다. |
| supply_discipline | raise | 5 | 공급규율과 실제 capacity shutdown은 spread 지속성을 높인다. |
| capacity_shutdown_confirmed | raise | 5 | shutdown이 실제이고 지속될 때만 구조조정 relief 품질이 올라간다. |
| working_capital_control | raise | 5 | 운전자본이 무너지면 spread 회복도 현금흐름으로 닫히지 않는다. |
| FCF_after_restructuring | raise | 5 | 구조조정 뒤 OPM과 FCF가 보여야 Green 후보가 된다. |
| critical_minerals_supply_security | raise | 4 | 전략광물 공급 안정은 실제 supply contract와 inventory로 내려와야 한다. |
| governance_and_dilution_control | raise | 4 | 프로젝트 품질이 좋아도 희석과 지배구조를 통과해야 한다. |
| export_control_resilience | raise | 5 | 중국 end-use 제한과 관세 리스크를 견뎌야 한다. |
| M&A_rumor_only | lower | -5 | M&A rumor는 event premium이지 Green 근거가 아니다. |
| policy_relief_only | lower | -5 | 정책지원은 실제 spread와 FCF 전에는 Stage 2 relief다. |
| strategic_material_headline_only | lower | -5 | 전략자원 headline만으로 EPS/FCF 체급 변화가 증명되지 않는다. |
| US_CAPEX_without_ROI | lower | -5 | 미국 CAPEX는 고객수요, spread, margin, FCF가 확인되어야 한다. |
| capacity_shutdown_without_spread_recovery | lower | -4 | shutdown만 있고 spread 회복이 없으면 crisis relief다. |
| restructuring_plan_undisclosed | lower | -4 | 공개되지 않은 구조조정 계획은 Green 근거가 아니다. |
| China_customer_or_material_concentration | lower | -5 | 중국 원료·고객 집중은 sanction과 tariff risk를 키운다. |
| rare_earth_end_use_restriction | lower | -5 | 희토류 end-use 제한은 sector 4C-watch다. |
| tariff_export_risk | lower | -5 | 수출 관세가 margin을 훼손하면 domestic relief를 상쇄한다. |
| dilution_for_project_capex | lower | -4 | ROI 없는 프로젝트 증자는 RedTeam 입력이다. |

## Easy Examples
- `M&A rumor` moves attention, but it is not business conversion.
- `anti-dumping tariff relief` is Stage 2 only until steel spread and export margin confirm.
- `capacity shutdown` is crisis relief unless OPM and FCF recover after restructuring.
