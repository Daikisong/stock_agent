# Round 276 R7 Loop 13 Bio Healthcare Medical Device Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_276.md
- round_id: round_204
- large_sector: BIOTECH_HEALTHCARE_DEVICE
- cases: 8
- success_candidate: 6
- event_premium: 3
- failed_rerating: 1
- hard_4c: 0
- hard_4c_reference: 1
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r7_loop13_yuhan_lazertinib_global_fda_approval | Yuhan / lazertinib / J&J Rybrevant combo | success_candidate / FDA approval Stage 2 | 2024-08-20 |  |  | 2024-12-16 | success_candidate_but_price_data_unavailable | FDA approval is strong Stage 2; Green requires royalty/milestone cashflow and prescription ramp. |
| r7_loop13_alteogen_merck_sc_keytruda_platform | Alteogen / Merck SC Keytruda enzyme | structural_success_candidate + 4B-watch + 4C-watch | 2025-03-27 |  | 2025-03-27 | 2025-03-27 | structural_success_candidate_but_4B_and_patent_watch | Platform optionality is large, but royalty cashflow, patent clearance and launch adoption are required. |
| r7_loop13_samsung_biologics_gsk_rockville_facility | Samsung Biologics | success_candidate + evidence_good_but_price_failed | 2025-12-22 |  | 2025-12-22 | 2025-12-22 | evidence_good_but_price_failed | U.S. facility is Stage 2; utilization, customer transfer, FDA inspection, margin and FCF are required. |
| r7_loop13_celltrion_us_factory_tariff_hedge | Celltrion | success_candidate / U.S. factory tariff hedge | 2025-07-29 |  | 2025-11-19 | 2025-11-19 | success_candidate_but_price_data_unavailable | Factory acquisition and expansion are Stage 2; product transfer, utilization, tariff saving and FCF are required. |
| r7_loop13_sk_bioscience_idt_biologika_cdmomna | SK Bioscience / IDT Biologika | success_candidate + event_premium | 2024-06-27 |  | 2024-06-27 |  | event_premium_success_candidate | European CDMO acquisition is Stage 2; order book, integration, utilization and margin are required. |
| r7_loop13_jeisys_medical_archimed_aesthetic_device_takeout | Jeisys Medical | success_candidate + takeout event | 2024-09-11 |  | 2024-09-11 |  | success_candidate_takeout_event | Real device benchmark, but take-private means not a tradable Stage 3 row. |
| r7_loop13_biopharma_tariff_support_policy_rally | Samsung Biologics / Celltrion / Korean pharma sector | event_premium + policy_relief | 2025-05-21 |  | 2025-05-21 | 2025-05-21 | event_premium_policy_relief | Policy support is relief, not Green; company margin and FCF bridge are required. |
| r7_loop13_sk_bioscience_skycovione_demand_collapse_reference | SK Bioscience / SkyCovione | vaccine demand-collapse hard reference |  |  |  | 2022-11-01 | failed_rerating_reference | Approval and government procurement did not become actual demand; use as vaccine demand-collapse reference. |

## Interpretation
- FDA approval and global partner validation are Stage 2 until prescription ramp and royalty/milestone cashflow appear.
- CDMO and U.S. factory rows need utilization, customer transfer, regulatory quality, margin and FCF.
- Aesthetic device takeout validates business quality, but take-private is not a tradable Stage 3 path.
- Policy-support rallies and M&A pops are 4B/event premium before company-level economics.
- SkyCovione is a demand-collapse reference: procurement is not administered demand.
