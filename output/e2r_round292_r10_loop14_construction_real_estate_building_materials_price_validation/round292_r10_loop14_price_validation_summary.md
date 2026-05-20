# Round 292 R10 Loop 14 Construction Real Estate Building Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_292.md
- round_id: round_220
- large_sector: CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
- cases: 8
- success_candidate: 2
- failed_rerating: 2
- event_premium: 3
- watch rows: 1
- hard_4c: 2
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r10_loop14_taeyoung_pf_liquidity_hard_watch | Taeyoung Engineering & Construction / PF liquidity reference | hard_4c_watch / PF liquidity |  |  |  | 2024-05-13 | thesis_break_watch | PF liquidity is a hard watch because refinancing and project cashflow come before backlog scoring. |
| r10_loop14_seoul_property_policy_stage2_not_green | Seoul property policy / construction-developer basket | policy_stage2 + 4B-watch | 2025-09-07 |  | 2025-10-23 |  | policy_stage2_not_green | Policy supply and LTV changes are Stage 2 until actual permits, starts, presales and PF cashflow close. |
| r10_loop14_hdc_gwangju_construction_safety_hard_4c | HDC Hyundai Development | hard_4c_reference / construction safety |  |  |  | 2022-03-14 | thesis_break_reference | Fatal construction-quality event overrides housing backlog and brand premium. |
| r10_loop14_samsung_ena_fadhili_epc_order_4b | Samsung E&A | success_candidate + event_premium | 2024-04-03 |  | 2024-04-03 |  | event_premium_success_candidate | Mega-order is Stage 2; advance payment, working capital and completion margin are Green gates. |
| r10_loop14_czech_nuclear_construction_export_stage2 | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KHNP | success_candidate + legal_4C_watch | 2024-07-17 |  | 2024-07-17 | 2025-05-06 | event_premium_success_candidate | Preferred bidder is not booked margin until final contract and legal challenge clear. |
| r10_loop14_hyundai_steel_rebar_weak_construction_demand | Hyundai Steel | failed_rerating / weak construction demand |  |  |  | 2024-06-21 | failed_rerating | Weak construction demand and rebar-price decline damaged earnings estimates. |
| r10_loop14_hyundai_posco_steel_plate_antidumping_event | Hyundai Steel / POSCO Holdings | event_premium_policy_relief | 2025-02-20 |  | 2025-02-20 |  | event_premium_policy_relief | Tariff relief is not Green until ASP, volume, utilization and spread improve. |
| r10_loop14_hyundai_steel_us_plant_capex_false_positive | Hyundai Steel | false_positive_score / localization capex |  |  |  | 2025-04-22 | false_positive_score | Localization capex is not Green without funding clarity, IRR and tariff-saving proof. |

## Interpretation
- Taeyoung/PF is a hard 4C-watch because backlog is not Green if PF repayment and refinancing fail.
- Seoul housing policy is Stage 2 until permits, starts, presales, PF refinancing and cash collection are visible.
- HDC/Gwangju is a construction safety hard reference; fatal quality events override backlog and brand premium.
- Samsung E&A and Czech nuclear are Stage 2 / 4B-watch until final contract, working capital and completion margin close.
- Hyundai Steel cases split weak-demand failed rerating, tariff-relief event premium, and localization-capex false positive.
