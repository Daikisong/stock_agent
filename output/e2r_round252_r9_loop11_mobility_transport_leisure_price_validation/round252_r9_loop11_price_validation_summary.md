# Round 252 R9 Loop 11 Mobility Transport Leisure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_252.md
- analyst_round_id: round_180
- large_sector: MOBILITY_TRANSPORT_LEISURE
- cases: 8
- success_candidate: 2
- failed_rerating: 2
- cyclical_success: 1
- event_premium: 1
- hard_4c_case_count: 2
- Stage 3 dated cases: 0
- 4B-watch cases: 4
- 4C-watch cases: 2
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r9_loop11_hyundai_hybrid_shareholder_return | Hyundai Motor | success_candidate | success_candidate_hybrid_shareholder_return_stage2 | 2024-08-28 |  |  |  | false | success_candidate | Strong Stage 2; hybrid mix, tariff-adjusted margin and FCF required before Green. |
| r9_loop11_hyundai_kia_us_tariff_margin_shock | Hyundai Motor / Kia | failed_rerating | 4c_watch_us_tariff_margin_shock |  |  |  | 2025-03-27 | false | thesis_break_watch | Tariff cost directly hit OP and stock reaction; 4C-watch until tariff-adjusted margins stabilize. |
| r9_loop11_hyundai_glovis_middle_east_logistics_disruption | Hyundai Motor / Hyundai Glovis | failed_rerating | 4c_watch_middle_east_logistics_disruption |  |  |  | 2026-04-03 | false | thesis_break_watch | Middle East logistics disruption hit auto export chain; Green requires logistics cost and delivery stability. |
| r9_loop11_korean_air_asiana_consolidation | Korean Air / Asiana / Jin Air / Air Busan | success_candidate | success_candidate_airline_consolidation_stage2 | 2024-12-12 |  |  |  | false | success_candidate | Airline merger is Stage 2; load factor, yield, cost synergy, debt and safety/service quality required before Green. |
| r9_loop11_kumho_tire_gwangju_factory_fire_hard_4c | Kumho Tire | 4c_thesis_break | hard_4c_factory_fire_supply_disruption |  |  |  | 2025-05-17 | true | thesis_break | Factory fire suspended nearly 20% of global capacity; direct-listed hard 4C. |
| r9_loop11_daejeon_auto_parts_supplier_fire_sector_hard_4c | Anjun Industrial / Hyundai-Kia supplier network | 4c_thesis_break | sector_hard_4c_workplace_safety_supply_chain_risk |  |  |  | 2026-03-20 | true | thesis_break | Unlisted supplier, but Hyundai/Kia supply-chain safety hard gate. |
| r9_loop11_pan_ocean_shipping_freight_cycle | Pan Ocean | cyclical_success | cyclical_success_freight_normalization_watch | 2024-05-01 |  | 2025-01-01 |  | false | cyclical_success | Freight-cycle benefit is Stage 2/cyclical; rate floor, contract coverage, FCF and deleveraging required before Green. |
| r9_loop11_lotte_tour_yellow_balloon_tourism_redirect | Lotte Tour / Yellow Balloon / Shinsegae / tourism basket | event_premium | event_premium_tourism_redirect_policy_watch | 2025-09-29 |  | 2025-11-21 |  | false | event_premium | Tourism policy/redirect event is Stage 2 and 4B; spend, occupancy, casino drop/hold and OPM required before Green. |

## Interpretation
- Hyundai Motor is Stage 2; hybrid mix, tariff-adjusted margin and FCF are required before Green.
- Hyundai/Kia tariff shock is 4C-watch because tariff cost reached OP and share-price anchors.
- Hyundai/Glovis logistics disruption is 4C-watch because route closure can break delivery and cost.
- Korean Air/Asiana consolidation is Stage 2; yield, load factor, synergy, debt and safety decide promotion.
- Kumho Tire factory fire is hard 4C because production capacity and revenue target were directly impaired.
- Daejeon supplier fire is sector hard 4C for Hyundai/Kia supply-chain safety.
- Pan Ocean is cyclical_success, not structural Green before rate floor, FCF and deleveraging.
- Tourism redirect is event premium before spend, occupancy, casino drop/hold and OPM.
