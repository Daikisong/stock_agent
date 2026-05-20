# Round 278 R9 Loop 13 Mobility Transport Leisure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_278.md
- round_id: round_206
- large_sector: MOBILITY_TRANSPORT_LEISURE
- cases: 8
- success_candidate: 4
- failed_rerating: 1
- cyclical_success: 1
- event_premium: 1
- hard_4c: 1
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r9_loop13_hyundai_motor_hybrid_shareholder_return_tariff_watch | Hyundai Motor | success_candidate + tariff 4C-watch | 2024-08-28 |  | 2024-08-28 | 2025-04-24 | success_candidate_4C_watch | Strong Stage 2 mobility case, but Green waits for OP margin after tariff, price pass-through and FCF. |
| r9_loop13_kia_us_tariff_margin_break | Kia Corp | evidence_good_but_price_failed / auto tariff 4C-watch |  |  |  | 2025-07-25 | evidence_good_but_price_failed | Kia is the simple example: unit sales grew, but tariff cost broke OP margin. |
| r9_loop13_hyundai_motor_india_ipo_capital_recycling | Hyundai Motor / Hyundai Motor India | failed_rerating / capital recycling watch | 2024-10-14 |  | 2024-10-14 | 2024-10-22 | failed_rerating_watch | Subsidiary IPO is useful only if proceeds use and parent capital-return bridge are visible. |
| r9_loop13_korean_air_asiana_consolidation_fleet_capex_watch | Korean Air / Asiana / Jin Air | success_candidate + fleet capex watch | 2024-12-12 |  | 2025-08-25 |  | success_candidate_4B_watch | Korean Air/Asiana is Stage 2; Green needs integration synergy, fleet ROI, safety trust and margin. |
| r9_loop13_jeju_air_fatal_crash_aviation_safety_hard_4c | Jeju Air | 4C-thesis-break / aviation safety hard 4C |  |  |  | 2024-12-30 | thesis_break | A fatal aviation accident breaks safety trust; demand recovery language cannot override it. |
| r9_loop13_hyundai_mobis_lighting_portfolio_recycling | Hyundai Mobis lighting business | success_candidate / asset recycling | 2026-01-27 |  | 2026-01-27 |  | success_candidate_but_insufficient_price_data | Asset recycling is Stage 2 until final deal value, proceeds use and remaining-business ROIC are proven. |
| r9_loop13_hmm_pan_ocean_red_sea_freight_cycle_watch | HMM / Pan Ocean | cyclical_success + Red Sea 4B/4C-watch | 2024-06-25 |  | 2025-10-09 | 2025-12-04 | cyclical_success_4B_watch | Red Sea rerouting can create cyclical success, but Green is restricted without contract freight durability. |
| r9_loop13_china_tourism_leisure_event_premium | China tourism / leisure basket | event_premium + 4B-watch | 2025-08-06 |  | 2025-11-21 |  | event_premium_4B_watch | Tourism policy can move prices, but Green requires booking, occupancy, ADR, casino drop and margin. |

## Interpretation
- Hyundai Motor is Stage 2; Green needs OP margin after tariff, price pass-through and FCF.
- Kia is the margin-break example: unit sales are not enough when tariff cost crushes OP.
- Korean Air/Asiana is consolidation Stage 2 until integration synergy, fleet ROI and safety trust are visible.
- Jeju Air is the hard 4C reference because fatal safety events break aviation trust.
- HMM/Pan Ocean and China tourism are event/cycle paths until durability or booking-margin evidence appears.
