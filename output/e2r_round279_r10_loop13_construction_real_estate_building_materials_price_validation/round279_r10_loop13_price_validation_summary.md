# Round 279 R10 Loop 13 Construction Real Estate Building Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_279.md
- round_id: round_207
- large_sector: CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
- cases: 8
- success_candidate: 4
- event_premium: 3
- policy_relief: 4
- hard_4c: 1
- direct_listed_hard_4c: 0
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r10_loop13_real_estate_pf_taeyoung_liquidity_watch | Taeyoung E&C reference / Korea real-estate PF | 4C-watch + policy_relief | 2024-03-27 |  |  | 2024-05-13 | thesis_break_watch_plus_policy_relief | PF support is relief; Green waits for refinancing, presales, profitability and cash collection. |
| r10_loop13_samsung_ena_gs_fadhili_epc_order_stage2 | Samsung E&A / GS E&C Fadhili EPC | success_candidate + event_premium | 2024-04-03 |  | 2024-04-03 |  | event_premium_success_candidate | Large EPC order is Stage 2; Green needs margin, working capital, receivables and cash collection. |
| r10_loop13_czech_nuclear_infra_preferred_bidder_legal_watch | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO Czech nuclear basket | success_candidate + legal 4C-watch | 2024-07-17 |  | 2024-07-17 | 2024-10-30 | success_candidate_4C_watch | Czech nuclear is a strong Stage 2 candidate, but preferred bidder is not final contract. |
| r10_loop13_hyundai_steel_construction_material_demand_break | Hyundai Steel | evidence_good_but_price_failed + tariff relief watch | 2025-02-20 |  | 2025-02-20 | 2024-06-21 | evidence_good_but_price_failed_then_relief | Hyundai Steel shows demand break first; later tariff relief is not Green without demand and spread. |
| r10_loop13_seoul_property_policy_ratecut_macro_gate | Seoul property policy / rate-cut macroprudential basket | event_premium + macroprudential 4C-watch | 2025-03-19 |  | 2025-03-19 | 2025-11-27 | event_premium_macroprudential_watch | Seoul property policy is event premium; developer Green needs presales, PF refinancing, margin and FCF. |
| r10_loop13_anseong_highway_construction_safety_reference | Anseong highway construction collapse reference | hard 4C reference |  |  |  | 2025-02-25 | thesis_break_reference | Fatal construction-site event is a hard reference even when listed-company price data is unavailable. |
| r10_loop13_builder_liquidity_package_policy_relief | Korean builders liquidity support package | success_candidate_policy_relief | 2024-03-27 |  | 2024-03-27 |  | success_candidate_policy_relief | Builder support package is Stage 2 relief, not Green before profitable-project cashflow. |
| r10_loop13_steel_plate_anti_dumping_construction_relief | Hyundai Steel / POSCO Holdings / construction steel plate basket | event_premium_policy_relief | 2025-02-20 |  | 2025-02-20 | 2025-02-20 | event_premium_policy_relief | Anti-dumping relief is event premium; Green needs actual construction demand, spread and FCF. |

## Interpretation
- PF support and builder liquidity are relief, not Green, until project cashflow proves out.
- Overseas EPC mega-orders are Stage 2 until EPC margin, working capital and receivables are visible.
- Czech nuclear preferred-bidder status is Stage 2; final contract and legal clearance remain gates.
- Anti-dumping and property/rate-cut headlines can move price, but do not prove spread, presales or FCF.
- Fatal construction-site safety events are hard references for R10 RedTeam gates.
