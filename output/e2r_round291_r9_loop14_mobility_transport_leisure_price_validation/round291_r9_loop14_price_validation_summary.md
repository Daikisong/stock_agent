# Round 291 R9 Loop 14 Mobility Transport Leisure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_291.md
- round_id: round_219
- large_sector: MOBILITY_TRANSPORT_LEISURE
- cases: 9
- success_candidate: 3
- failed_rerating: 1
- event_premium: 2
- watch rows: 1
- hard_4c: 1
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r9_loop14_hyundai_kia_us_tariff_hybrid_mix | Hyundai Motor / Kia | success_candidate + 4C-watch | 2025-10-30 |  | 2025-10-30 | 2025-07-31 | success_candidate_4C_watch | Tariff relief plus hybrid mix is Stage 2; Green needs pass-through, local hedge, incentive control, margin and FCF. |
| r9_loop14_hyundai_glovis_middle_east_logistics_4c_watch | Hyundai Motor / Hyundai Glovis | thesis_break_watch / Middle East route disruption |  |  |  | 2026-04-03 | thesis_break_watch | Middle East route disruption is a 4C-watch gate because delivery delays and logistics cost hit high-margin exports. |
| r9_loop14_korean_air_asiana_integration_stage2 | Korean Air / Asiana Airlines | success_candidate / airline consolidation Stage 2 | 2024-12-12 |  | 2024-12-12 |  | success_candidate_but_price_data_unavailable | Airline consolidation is Stage 2 until yield, load factor, integration cost, LCC consolidation and safety quality close. |
| r9_loop14_tway_air_incheon_airline_remedy_stage2 | T'way Air / Air Incheon | success_candidate + execution watch | 2024-08-07 |  | 2024-08-07 |  | success_candidate_execution_watch | Route rights and cargo assets are Stage 2; Green needs load factor, yield, utilization and customer retention. |
| r9_loop14_jeju_air_safety_hard_4c | Jeju Air | hard 4C / aviation safety trust break |  |  |  | 2024-12-30 | thesis_break | Fatal safety event is hard 4C and overrides travel-demand or valuation recovery language. |
| r9_loop14_hyundai_india_ipo_failed_rerating | Hyundai Motor / Hyundai Motor India | failed_rerating / overseas auto IPO quality gate | 2024-10-14 |  | 2024-10-14 | 2024-10-22 | failed_rerating | India growth and IPO size failed debut and first-earnings validation. |
| r9_loop14_china_tourism_leisure_basket | Paradise / Hotel Shilla / Hyundai Department Store / Hankook Cosmetics | event_premium + 4B-watch | 2025-08-06 |  | 2025-08-06 |  | event_premium_4B_watch | Visitor count and policy rally need spend-per-head, casino drop, hotel ADR/occupancy and margin conversion. |
| r9_loop14_hmm_red_sea_freight_rate_event_premium | HMM / container-shipping read-through | event_premium + 4B-watch | 2024-07-03 |  | 2024-07-03 | 2025-10-09 | event_premium_4B_watch | Spot freight-rate spike is cyclical until contract mix, vessel utilization and route security prove durability. |
| r9_loop14_korea_used_car_export_logistics_shock | Korea used-car export logistics reference | 4C-reference / used-car export route disruption |  |  |  | 2026-03-24 | thesis_break_reference | Destination demand and route availability must both clear for export logistics. |

## Interpretation
- Hyundai/Kia tariff relief plus hybrid mix is Stage 2 until tariff pass-through, local production hedge, margin and FCF close.
- Hyundai/Glovis shows route security and logistics cost can become auto/export 4C-watch gates.
- Korean Air/Asiana and T'way/Air Incheon are Stage 2 until yield, load factor, cargo retention and integration execution are visible.
- Jeju Air is the hard 4C reference because fatal safety events override travel-demand logic.
- Hyundai India shows large overseas IPO size does not prove parent rerating when debut and first earnings fail.
- China tourism and HMM/Red Sea are event premiums until spend conversion and freight durability are proven.
