# Round 278 R9 Green Gate Review

Do not apply these weights to production scoring yet.

R9 Stage 3-Green is not `unit sales`, `IPO valuation`, `tourist flow`, `freight spike`, `fleet order`, or `asset-sale exploration`. It requires margin, ROI, safety trust, booking conversion, durability and FCF.

## Required Fields

- OP_margin_after_tariff_confirmed
- hybrid_SUV_mix_quality_confirmed
- price_pass_through_confirmed
- shareholder_return_execution_confirmed
- integration_synergy_realization_confirmed
- fleet_capex_ROI_confirmed
- aviation_safety_trust_confirmed
- freight_rate_durability_confirmed
- booking_occupancy_conversion_confirmed
- asset_sale_ROIC_confirmed
- OP_FCF_conversion_confirmed
- price_path_after_evidence

## Forbidden Patterns

- unit_sales_without_margin
- IPO_valuation_without_parent_ROI
- tourist_flow_headline_only
- freight_rate_spike_only
- fleet_order_without_ROI
- exploratory_asset_sale_only
- tariff_exposure_unhedged
- fatal_safety_event
- booking_without_margin

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| OP_margin_after_tariff | raise | 5 | 판매량보다 관세 이후 OP margin이 먼저다. |
| hybrid_SUV_mix_quality | raise | 5 | 하이브리드/SUV mix가 ASP와 margin으로 닫혀야 한다. |
| price_pass_through | raise | 5 | 관세와 비용을 가격에 전가할 수 있어야 한다. |
| shareholder_return_execution | raise | 4 | 자사주·배당은 실제 실행과 FCF 재원이 필요하다. |
| integration_synergy_realization | raise | 5 | 항공 합병은 통합 시너지와 노선 수익성이 확인되어야 한다. |
| fleet_capex_ROI | raise | 5 | 항공기 주문은 성장투자이면서 capex 부담이다. |
| aviation_safety_trust | raise | 5 | 항공 안전 신뢰는 hard gate다. |
| freight_rate_durability | raise | 5 | 해운은 spot 운임이 아니라 contract durability가 필요하다. |
| booking_occupancy_conversion | raise | 5 | 관광객 headline은 booking, occupancy, ADR, margin으로 검증해야 한다. |
| asset_sale_ROIC | raise | 4 | 자산매각은 deal value와 proceeds use가 확인되어야 한다. |
| unit_sales_without_margin | lower | -5 | 판매량만 좋고 OP가 깨지면 Green이 아니다. |
| IPO_valuation_without_parent_ROI | lower | -5 | 자회사 IPO valuation은 모회사 ROIC/환원 연결고리 전에는 부족하다. |
| tourist_flow_headline_only | lower | -5 | 관광객 수만으로 소비·마진을 만들지 않는다. |
| freight_rate_spike_only | lower | -5 | 운임 spike는 cycle일 수 있으므로 구조적 Green을 제한한다. |
| fatal_safety_event | lower | -5 | 사망 사고는 safety trust hard 4C다. |

## Easy Examples
- `Kia US sales +5%` is not Green because tariff cost hit OP by 786B KRW.
- `Lotte Tour +20%` is event premium until booking, occupancy, ADR and margin appear.
- `Jeju Air fatal crash` is hard 4C because aviation safety trust is core evidence.
