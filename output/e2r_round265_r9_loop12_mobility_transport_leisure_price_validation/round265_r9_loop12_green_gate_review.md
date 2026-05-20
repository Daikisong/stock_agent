# Round 265 R9 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- route_yield_confirmed
- load_factor_confirmed
- fleet_utilization_confirmed
- safety_trust_risk_passed
- component_asp_to_margin_fcf_confirmed
- transaction_value_and_proceeds_use_confirmed
- freight_rate_floor_and_route_security_confirmed
- tourism_spend_hotel_occupancy_casino_drop_adr_confirmed
- logistics_insurance_fuel_cost_controlled
- price_path_after_evidence

## Forbidden Patterns

- route_rights_only
- fleet_count_only
- tourist_arrival_headline_only
- freight_spike_only
- safety_incident_unresolved
- divestiture_headline_only
- geopolitical_shipping_attack_unresolved
- component_asp_without_margin

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| safety_trust | raise | 5 | 항공은 load factor보다 safety trust가 먼저다. |
| route_yield | raise | 5 | LCC route remedy는 route yield가 확인돼야 Stage 3로 갈 수 있다. |
| load_factor | raise | 5 | 신규 장거리 노선은 load factor가 economics를 닫는다. |
| fleet_utilization | raise | 5 | 항공·렌터카·해운 모두 자산 utilization이 margin으로 이어져야 한다. |
| component_take_rate | raise | 5 | 부품 ASP uplift는 실제 take-rate가 붙어야 한다. |
| component_asp_uplift | raise | 4 | hybrid/EREV 고ASP 부품은 Stage 2 증거지만 margin 확인이 필요하다. |
| transaction_value_and_proceeds | raise | 4 | 부품 포트폴리오 정리는 거래가치와 proceeds use가 확인돼야 한다. |
| freight_rate_floor | raise | 5 | 해운은 spot spike보다 freight floor와 contract coverage가 중요하다. |
| logistics_security | raise | 5 | 선박 공격·항로 리스크는 운임보다 먼저 보는 gate다. |
| tourism_spend_conversion | raise | 5 | 관광은 방문객 수보다 hotel occupancy, casino drop, ADR, package margin이 중요하다. |
| route_rights_only | lower | -5 | 노선권만으로 route economics를 대체하지 않는다. |
| aviation_safety_incident | lower | -5 | 항공 안전사고는 즉시 4C gate로 본다. |
| tourist_arrival_headline_only | lower | -5 | 관광객 headline은 spend/OPM 전 event premium이다. |
| freight_spike_only | lower | -5 | 운임 급등은 freight floor 전 cyclical이다. |
| shipping_security_event | lower | -5 | 선박 공격은 insurance, rerouting, delay cost를 먼저 본다. |
| divestiture_headline_only | lower | -4 | 매각 검토만으로 FCF나 주주환원을 인정하지 않는다. |
| component_asp_without_margin | lower | -4 | ASP premium은 margin과 FCF로 닫히기 전 Stage 2다. |
| fleet_count_without_yield | lower | -4 | 기재 수와 pilot support만으로 수익성을 인정하지 않는다. |
| china_travel_redirect_only | lower | -4 | 중국 관광 redirect는 spend conversion 전 Green이 아니다. |

## Easy Examples
- `route rights` are not Green until yield, load factor and cost are visible.
- `tourism reroute +24%` is event premium until hotel/casino/duty-free spend appears.
- `freight spike` can be cyclical success, but route security and rate floor decide durability.
