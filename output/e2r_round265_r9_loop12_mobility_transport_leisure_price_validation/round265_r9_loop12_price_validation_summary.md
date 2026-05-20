# Round 265 R9 Loop 12 Mobility Transport Leisure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_265.md
- analyst_round_id: round_193
- large_sector: MOBILITY_TRANSPORT_LEISURE
- cases: 8
- success_candidate: 3
- cyclical_success: 1
- event_premium: 1
- hard_4c_case_count: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 5
- 4C-watch cases: 3
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r9_loop12_jeju_air_muan_crash_hard_4c | Jeju Air | 4c_thesis_break | hard_4c_aviation_safety_trust_break |  |  |  | 2024-12-30 | true | thesis_break | Fatal accident is hard 4C; safety trust overrides route/load-factor thesis. |
| r9_loop12_air_busan_plane_fire_4c_watch | Air Busan | 4c_thesis_break | aviation_safety_incident_4c_watch_not_hard |  |  |  | 2025-01-31 | false | thesis_break_watch | Non-fatal fire is 4C-watch, not hard 4C, but safety gate must be elevated. |
| r9_loop12_tway_eu_route_remedy | T'way Air | success_candidate | success_candidate_route_remedy_stage2 | 2024-03-07 |  |  |  | false | success_candidate_but_insufficient_price_data | Route rights are Stage 2; route yield, load factor, fuel/lease cost and execution required before Green. |
| r9_loop12_hl_mando_hybrid_erev_component_asp | HL Mando | success_candidate | success_candidate_component_asp_stage2 | 2024-06-25 |  | 2024-06-25 |  | false | success_candidate | Component ASP uplift is Stage 2; customer take-rate, backlog, margin and FCF required before Green. |
| r9_loop12_hyundai_mobis_lighting_divestiture | Hyundai Mobis | success_candidate | success_candidate_portfolio_restructuring_stage2 | 2026-01-27 |  | 2026-01-27 |  | false | success_candidate_but_price_data_unavailable | Divestiture is Stage 2 until transaction value, proceeds use, margin improvement and shareholder return confirm. |
| r9_loop12_hmm_namu_hormuz_shipping_security | HMM | 4c_thesis_break | shipping_security_4c_watch |  |  |  | 2026-05-11 | false | thesis_break_watch | Direct Korean shipper security event; insurance, rerouting, delay and security cost must be monitored. |
| r9_loop12_hmm_panocean_freight_normalization_watch | HMM / Pan Ocean shipping basket | cyclical_success | cyclical_success_plus_freight_normalization_4c_watch |  |  | 2025-01-01 | 2026-02-05 | false | cyclical_success_plus_4C_watch | Freight spike is cyclical; rate floor, contract coverage, FCF and deleveraging required before Green. |
| r9_loop12_lotte_yellowballoon_tourism_redirect | Lotte Tour Development / Yellow Balloon / Shinsegae | event_premium | event_premium_tourism_redirect_before_spend | 2025-11-17 |  | 2025-11-21 |  | false | event_premium | Tourism redirect is 4B/event premium until hotel occupancy, casino drop, duty-free spend and package margin confirm. |

## Interpretation
- Jeju Air is direct hard 4C because safety trust breaks before load factor or route growth matters.
- Air Busan is 4C-watch: non-fatal, but still an elevated aviation safety gate.
- T'way route remedy is Stage 2; route yield and load factor decide promotion.
- HL Mando is component ASP Stage 2; take-rate, margin and FCF are required before Green.
- Hyundai Mobis lighting divestiture is Stage 2 until transaction value, proceeds and margin improvement are visible.
- HMM Namu attack is shipping-security 4C-watch, not a freight-rate positive.
- HMM/Pan Ocean freight cycle is cyclical success plus normalization 4C-watch.
- Tourism redirect is event premium until hotel/casino/duty-free spend conversion appears.
