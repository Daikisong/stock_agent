# Round 239 R9 Loop 10 Mobility Transport Leisure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_239.md
- analyst_round_id: round_167
- large_sector: MOBILITY_TRANSPORT_LEISURE
- cases: 8
- success_candidate: 4
- cyclical_success: 1
- event_premium: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- 4C-watch cases: 2
- hard_4c_case_count: 1
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r9_loop10_hyundai_kia_future_mobility_capex_4b | 현대차/기아 | success_candidate | success_candidate_event_premium_labor_capex_watch | 2026-02-25 |  | 2026-02-25 | 2026-01-22 | false | event_premium_success_candidate | Future-mobility capex is Stage 2 and 4B-watch; robot/software revenue and FCF are required before Green. |
| r9_loop10_hyundai_mobis_iccu_quality_recall_watch | 현대모비스 | 4c_thesis_break | 4c_watch_evidence_good_but_quality_failed |  |  |  | 2024-05-01 | false | thesis_break_watch | EV-parts exposure cannot become Green while recurring ICCU defect threatens earnings and reputation. |
| r9_loop10_hyundai_rotem_morocco_rail_order | 현대로템 | success_candidate | success_candidate_rail_export_order | 2025-02-26 |  |  |  | false | success_candidate | Rail export order is Stage 2; delivery, margin, working capital and cash collection are required before Green. |
| r9_loop10_tway_europe_route_allocation | 티웨이항공 | success_candidate | success_candidate_long_haul_lcc_route_allocation | 2024-03-07 |  |  |  | false | success_candidate | Route allocation is Stage 2; load factor, yield, aircraft cost, crew cost, fuel and safety/service execution are required before Green. |
| r9_loop10_jin_air_air_busan_air_seoul_integration | 진에어/에어부산/에어서울 | success_candidate | success_candidate_lcc_consolidation_integration | 2024-11-29 |  |  |  | false | success_candidate | LCC consolidation is Stage 2; integration cost, route optimization, load factor/yield and safety/service quality are required before Green. |
| r9_loop10_pan_ocean_dry_bulk_cycle | 팬오션 | cyclical_success | cyclical_success_dry_bulk_lng_fleet_expansion | 2024-05-31 |  |  |  | false | cyclical_success_evidence_good_but_price_failed | Dry bulk/fleet expansion is Stage 2/cycle; freight-rate floor, contract coverage, FCF and deleveraging are required before Green. |
| r9_loop10_lotte_tour_yellow_balloon_china_japan_redirect | 롯데관광개발/노랑풍선/신세계 | event_premium | event_premium_price_moved_without_evidence | 2025-11-21 |  | 2025-11-21 |  | false | event_premium | China-Japan redirect expectation drove price before actual arrivals, occupancy, casino drop, ADR and FCF. |
| r9_loop10_jeju_air_fatal_crash_hard_4c | 제주항공 | 4c_thesis_break | hard_4c_operational_safety_trust_break |  |  |  | 2024-12-30 | true | thesis_break | Fatal crash is hard 4C and blocks travel-demand Green. |

## Interpretation
- Hyundai/Kia future mobility is Stage 2 + 4B-watch, not automatic Green.
- Hyundai Mobis and Jeju Air show why quality/safety trust gates matter in R9.
- Rotem rail, T'way routes, and LCC consolidation are Stage 2 until delivery, yield, utilization, and FCF confirm.
- Pan Ocean and tourism redirect rallies are cycle/event premium until freight floor or spend conversion confirms.
