# Round 292 R10 Loop 14 Construction Real Estate Building Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_292.md
- round_id: round_220
- large_sector: CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
- cases: 8
- success_candidate: 2
- failed_rerating: 2
- event_premium: 4
- hard_4c: 2
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r10_loop14_taeyoung_pf_liquidity_hard_watch | Taeyoung Engineering & Construction / PF liquidity reference | PF hard 4C-watch |  |  |  | 2024-05-13 | thesis_break_watch | PF liquidity is a hard watch because backlog cannot protect equity if refinancing and cash collection fail. |
| r10_loop14_seoul_property_policy_stage2_not_green | Seoul property policy / construction-developer basket | policy_stage2 + 4B-watch | 2025-09-07 |  | 2025-10-23 |  | policy_stage2_not_green | Property policy is Stage 2 until permits, starts, presales, PF refinancing, margin and cash collection confirm. |
| r10_loop14_hdc_gwangju_construction_safety_hard_4c | HDC Hyundai Development | hard 4C / construction safety trust break |  |  |  | 2022-03-14 | thesis_break_reference | Fatal construction-quality event overrides housing backlog and brand premium. |
| r10_loop14_samsung_ena_fadhili_epc_order_4b | Samsung E&A | success_candidate + event_premium | 2024-04-03 |  | 2024-04-03 |  | event_premium_success_candidate | Mega-order is Stage 2; advance payment, cost lock-in, working capital and completion margin are required. |
| r10_loop14_czech_nuclear_construction_export_stage2 | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KHNP | success_candidate + legal 4C-watch | 2024-07-17 |  | 2024-07-17 | 2025-05-06 | event_premium_success_candidate | Preferred bidder is not booked margin until final contract and legal challenge clear. |
| r10_loop14_hyundai_steel_rebar_weak_construction_demand | Hyundai Steel | failed_rerating / weak construction demand |  |  |  | 2024-06-21 | failed_rerating | Weak construction demand and rebar-price decline damaged earnings estimates. |
| r10_loop14_hyundai_posco_steel_plate_antidumping_event | Hyundai Steel / POSCO Holdings | event_premium / policy relief | 2025-02-20 |  | 2025-02-20 |  | event_premium_policy_relief | Tariff relief is not Green until ASP, volume, utilization and spread improve. |
| r10_loop14_hyundai_steel_us_plant_capex_false_positive | Hyundai Steel | false_positive_score / localization capex |  |  |  | 2025-04-22 | false_positive_score | Localization capex is not Green without funding clarity, IRR and tariff-saving proof. |

## Interpretation
- PF liquidity and construction safety are hard gates before backlog or policy support.
- Property policy, nuclear preferred-bidder status, tariff relief and localization capex are Stage 2/event signals until cashflow closes.
- Overseas EPC order value is useful, but Green requires margin, advance payment, working capital and claim-risk evidence.
