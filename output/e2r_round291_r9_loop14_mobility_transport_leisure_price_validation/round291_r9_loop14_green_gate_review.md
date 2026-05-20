# Round 291 R9 Green Gate Review

Do not apply these weights to production scoring yet.

R9 Stage 3-Green is not `tariff relief`, `hybrid`, `airline merger`, `route rights`, `China tourists`, `freight spike`, or `overseas IPO`. It requires tariff pass-through, margin, route security, yield, safety trust, spend-per-head, freight durability, OP/FCF, and price path after evidence.

## Required Fields

- tariff_pass_through_confirmed
- hybrid_mix_margin_confirmed
- local_production_hedge_confirmed
- route_security_continuity_confirmed
- logistics_cost_control_confirmed
- load_factor_yield_confirmed
- aviation_safety_trust_confirmed
- integration_synergy_execution_confirmed
- tourist_spend_per_head_confirmed
- freight_rate_durability_confirmed
- price_path_after_evidence

## Forbidden Patterns

- tariff_relief_headline_only
- visitor_count_only
- merger_completion_only
- route_rights_without_load_factor
- cargo_asset_purchase_without_customer_retention
- freight_spot_rate_only
- overseas_IPO_size_only
- EV_or_hybrid_mix_without_margin
- safety_risk_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| tariff_pass_through | raise | 5 | 관세 relief가 아니라 가격전가와 margin 회복이 핵심이다. |
| hybrid_mix_margin | raise | 5 | hybrid/high-margin mix가 OP margin으로 닫혀야 한다. |
| local_production_hedge | raise | 5 | 현지생산 hedge가 관세와 물류비를 줄이는지 봐야 한다. |
| route_security_continuity | raise | 5 | 자동차·해운은 항로 안정성이 margin의 하부 구조다. |
| logistics_cost_control | raise | 5 | rerouting과 보관비가 OP를 훼손하지 않아야 한다. |
| load_factor_yield | raise | 5 | 항공은 탑승률보다 yield와 비용을 같이 봐야 한다. |
| aviation_safety_trust | raise | 5 | 항공 안전 신뢰는 hard gate다. |
| integration_synergy_execution | raise | 5 | 항공 통합은 완료보다 synergy 실행이 중요하다. |
| tourist_spend_per_head | raise | 5 | 관광객 수는 객단가와 margin으로 검증해야 한다. |
| freight_rate_durability | raise | 5 | spot 운임보다 contract-rate durability가 중요하다. |
| tariff_relief_headline_only | lower | -5 | 관세 인하 headline만으로 margin 회복을 만들지 않는다. |
| visitor_count_only | lower | -5 | 입국자 수만으로 소비·마진을 만들지 않는다. |
| merger_completion_only | lower | -5 | 합병 완료는 synergy와 yield 전에는 Stage 2다. |
| route_rights_without_load_factor | lower | -5 | 노선권만으로 항공 수익성을 만들지 않는다. |
| cargo_asset_purchase_without_customer_retention | lower | -5 | 화물 자산 인수는 고객 유지와 utilization이 필요하다. |
| freight_spot_rate_only | lower | -5 | spot 운임 spike는 cycle일 수 있다. |
| overseas_IPO_size_only | lower | -5 | 해외 IPO 규모만으로 parent rerating을 만들지 않는다. |
| EV_or_hybrid_mix_without_margin | lower | -4 | EV/hybrid mix는 margin 확인 전에는 부족하다. |
| safety_risk_unresolved | lower | -5 | 안전 리스크 미해소는 Green을 막는다. |

## Easy Examples
- `Hyundai tariff falls from 25% to 15%` is not Green; margin after tariff and incentives must recover.
- `China visitors +48%` is useful, but Green needs spend-per-head, hotel ADR/occupancy and casino drop.
- `Jeju Air fatal crash` is hard 4C because safety trust breaks before any demand thesis.
