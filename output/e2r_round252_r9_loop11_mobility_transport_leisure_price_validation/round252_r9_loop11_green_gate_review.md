# Round 252 R9 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- unit_economics_confirmed
- tariff_adjusted_margin_confirmed
- fcf_after_capex_confirmed
- route_yield_confirmed
- load_factor_confirmed
- fleet_utilization_confirmed
- logistics_cost_and_delivery_delay_controlled
- supply_chain_continuity_confirmed
- safety_quality_operational_trust_passed
- tourist_spend_occupancy_casino_drop_opm_confirmed
- price_path_after_evidence

## Forbidden Patterns

- strategy_day_only
- shareholder_return_without_margin
- tariff_relief_headline_only
- fleet_count_without_yield
- merger_without_synergy
- tourism_policy_only
- freight_rate_spike_only
- factory_fire_or_supply_disruption
- workplace_fatality
- logistics_disruption

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| unit_economics | raise | 5 | R9는 판매량보다 단위경제성이 Stage 3 visibility다. |
| tariff_adjusted_margin | raise | 5 | 자동차는 관세 이후 OPM이 지켜져야 한다. |
| hybrid_mix_profitability | raise | 4 | 하이브리드 mix가 ASP·OPM으로 닫혀야 한다. |
| fcf_after_capex | raise | 5 | 전략 투자와 자사주는 FCF로 유지돼야 한다. |
| route_yield | raise | 5 | 항공은 fleet count보다 route yield가 중요하다. |
| load_factor | raise | 5 | 통합 항공사는 load factor가 synergy 확인 축이다. |
| fleet_utilization | raise | 5 | 차량·항공·해운 모두 utilization이 margin으로 연결된다. |
| logistics_cost_control | raise | 5 | 중동 물류 차질은 수요가 좋아도 delivery와 비용을 깨뜨린다. |
| supply_chain_continuity | raise | 5 | 공장 화재나 공급망 사고는 생산 continuity를 직접 훼손한다. |
| safety_trust | raise | 5 | 항공·부품·타이어는 안전과 운영 신뢰가 hard gate다. |
| tourist_spend_conversion | raise | 5 | 관광은 방문객 수보다 spend, occupancy, casino drop, OPM이 중요하다. |
| strategy_day_only | lower | -4 | 전략 발표만으로 Stage 3-Green을 만들지 않는다. |
| shareholder_return_without_margin | lower | -4 | 주주환원은 margin과 FCF가 없으면 Stage 2에 머문다. |
| tariff_relief_headline_only | lower | -5 | 관세 완화 headline은 실제 margin 안정 전 event다. |
| fleet_count_without_yield | lower | -4 | fleet scale은 yield와 load factor가 없으면 Green 증거가 아니다. |
| merger_without_synergy | lower | -5 | 항공 통합은 synergy, debt, service quality 확인 전 Green 금지다. |
| tourism_policy_only | lower | -5 | 무비자·관광정책만으로 spend/OPM을 대체하지 않는다. |
| freight_rate_spike_only | lower | -5 | 운임 급등은 rate floor와 FCF 전 cyclical이다. |
| factory_fire_or_supply_disruption | lower | -5 | 공장 화재와 생산중단은 수요논리를 즉시 훼손한다. |
| workplace_fatality | lower | -5 | 사망사고는 supply-chain safety hard gate다. |
| logistics_disruption | lower | -5 | route closure와 delivery delay는 R9 thesis-break watch다. |

## Easy Examples
- `Shareholder return` is not Green until tariff-adjusted margin and FCF appear.
- `Airline merger` is not enough without route yield, load factor and cost synergy.
- `Tourism visa-free policy` is event premium until spend, occupancy, casino drop and OPM confirm.
- `Factory fire with production suspension` is hard 4C because supply continuity is broken.
