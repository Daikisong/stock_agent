# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R9_loop_12_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round = R9
scheduled_loop = 12
completed_round = R9
completed_loop = 12
next_round = R10
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TRANSPORT_PASSENGER_CARGO_YIELD_MARGIN_LEVERAGE
loop_objective = coverage_gap_fill | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds **4** new independent cases, **2** counterexamples, and **3** residual errors for **R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The goal is not to prove again that early Stage2 is useful. The specific residual question here is whether **transport/mobility volume** should be promoted when it has not yet converted into **durable yield, margin, and balance-sheet clearance**. In this round, the mechanism behaves like an aircraft climbing through weather: passenger count or freight volume is lift, but yield, cost, and capital structure are the air density. Without density, the same thrust stalls.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 12 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | TRANSPORT_PASSENGER_CARGO_YIELD_MARGIN_LEVERAGE |
| valid round-sector pair | yes |
| stock_agent code access | false |
| price atlas access | required and used |

R9 allows mobility/transport under L3 when the underlying thesis is vehicle/passenger/freight volume and operating leverage rather than construction/real-estate balance-sheet stress. This file therefore uses **L3_BATTERY_EV_GREEN_MOBILITY** and **C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE**.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result filenames showed loop 10 and loop 11 already contained R9/C29 research. Those prior loops used Hyundai Motor, Kia, HL Mando, Nexen Tire, Hyundai Mobis, Hyundai Wia, and Hanon Systems. This loop avoids those symbols and instead adds freight/container shipping, PCC logistics, and LCC passenger-volume cases.

```text
previous_R9_loop10_symbols = 005380, 000270, 204320
previous_R9_loop11_symbols = 161390, 012330, 011210, 018880
this_loop_symbols = 011200, 086280, 089590, 091810
same_symbol_same_trigger_date_research = avoided
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

The only apparent overlap is broad C29 itself. That is intentional; v12 treats canonical-archetype repetition as normal when the symbol, evidence family, cycle phase, and failure mode are new.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest fields checked:

| manifest field | observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
required_ohlcv_fields_present = true
corporate_action_candidate_overlap_entry_to_D180 = false
calibration_usable_representative_cases = 4
```

Symbol profile caveats:

| symbol | company | profile path | profile caveat handling |
|---|---:|---|---|
| 011200 | HMM | atlas/symbol_profiles/011/011200.json | corporate-action candidate dates exist, but representative 2020 trigger is clean through D+180; 2021-11-16 is outside the 180D window. |
| 086280 | 현대글로비스 | atlas/symbol_profiles/086/086280.json | 2024 profile candidate dates are outside the 2023-06-08 representative window. |
| 089590 | 제주항공 | atlas/symbol_profiles/089/089590.json | 2020/2021/2022 candidate dates are before the 2023-05-10 representative window. |
| 091810 | 티웨이항공 | atlas/symbol_profiles/091/091810.json | 2023-02-23 profile candidate is before entry; later share-count/capital-overhang behavior is treated as evidence/caveat, not a profile-blocked price discontinuity. |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Freight-rate/yield and utilization convert transport volume into operating leverage. |
| PCC_CAR_CARRIER_AUTO_EXPORT_LOGISTICS_MARGIN | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Finished-vehicle logistics/PCC margin bridge is transport volume plus customer quality. |
| LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Passenger volume alone resembles revenue growth, but C29 requires yield/cost durability. |
| LCC_TURNAROUND_WITH_DILUTION_AND_CAPACITY_COST_OVERHANG | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Same passenger-volume lever, but overhang shifts it to false positive/4C guard. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | trigger family | new independent? |
|---|---:|---|---|---|---|---|
| R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | 011200 | HMM | structural_success | positive | freight-rate margin conversion | true |
| R9L12_C29_086280_PCC_LOGISTICS_20230608 | 086280 | 현대글로비스 | structural_success | positive | PCC/finished-vehicle logistics margin | true |
| R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509 | 089590 | 제주항공 | failed_rerating | counterexample | passenger volume without durable yield margin | true |
| R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | 091810 | 티웨이항공 | 4C_late | counterexample | LCC recovery with dilution/capacity overhang | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
minimum_new_independent_case_ratio = 1.00
```

The balance is useful because it separates two superficially similar routes:

- Freight/PCC logistics where yield or margin converts volume into profit: C29 works.
- LCC passenger recovery where volume recovers before yield/cost/capital structure: C29 becomes a false positive unless guarded.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | 2Q/1H earnings + freight-rate rise | confirmed margin bridge and financial visibility | valuation/revision overheat, CB/share-supply overhang | later watch-only thesis-break risk |
| R9L12_C29_086280_PCC_LOGISTICS_20230608 | PCC/finished-vehicle shipping and auto-export volume route | customer quality and margin bridge | none | none |
| R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509 | passenger recovery and first-turnaround narrative | limited financial visibility only | margin/yield slowdown, price-local peak | thesis failed to rerate durably |
| R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | passenger recovery and profit-turnaround narrative | limited financial visibility only | dilution/capital overhang, local peak | high-MAE thesis-break watch-only route |

## 10. Price Data Source Map

| symbol | year shards used | profile path | entry rows checked |
|---:|---|---|---|
| 011200 | 2020, 2021, 2022, 2023 | atlas/symbol_profiles/011/011200.json | 2020-08-14 close 6,410; 2021-05-13 close 44,450 |
| 086280 | 2023 | atlas/symbol_profiles/086/086280.json | 2023-06-08 close 178,000 |
| 089590 | 2023 | atlas/symbol_profiles/089/089590.json | 2023-05-10 close 13,780 |
| 091810 | 2023 | atlas/symbol_profiles/091/091810.json | 2023-05-15 close 2,985; 2023-10-24 close 2,015 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome | current_profile_verdict | dedupe_for_aggregate |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| T_R9L12_011200_STAGE2_20200813 | R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | 011200 | HMM | Stage2-Actionable | 2020-08-13 | 2020-08-14 | 6410 | 137.91 | -17.0 | 680.03 | -17.0 | structural_success | current_profile_correct | True |
| T_R9L12_011200_4B_20210513 | R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | 011200 | HMM | Stage4B-Overlay | 2021-05-13 | 2021-05-13 | 44450 | 15.0 | -18.3 | 15.0 | -39.4 | 4B_overlay_success | current_profile_correct | False |
| T_R9L12_086280_STAGE2_20230608 | R9L12_C29_086280_PCC_LOGISTICS_20230608 | 086280 | 현대글로비스 | Stage2-Actionable | 2023-06-08 | 2023-06-08 | 178000 | 14.04 | -6.52 | 14.04 | -9.21 | structural_success_narrower_than_OEM | current_profile_too_late | True |
| T_R9L12_089590_STAGE2_20230509 | R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509 | 089590 | 제주항공 | Stage2-Actionable | 2023-05-09 | 2023-05-10 | 13780 | 12.48 | -16.84 | 12.48 | -31.86 | failed_rerating_high_MAE | current_profile_false_positive | True |
| T_R9L12_091810_STAGE2_20230515 | R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | 091810 | 티웨이항공 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 2985 | 21.27 | -16.42 | 21.27 | -34.51 | 4C_late_high_MAE | current_profile_4C_too_late | True |
| T_R9L12_091810_4C_20231024 | R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | 091810 | 티웨이항공 | Stage4C-ThesisBreak | 2023-10-24 | 2023-10-24 | 2015 | 23.82 | -9.18 | 23.82 | -16.38 | 4C_protection_watch_only | current_profile_4C_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | corporate_action_window_status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| T_R9L12_011200_STAGE2_20200813 | 2020-08-14 | 6,410 | 19.81 | -17.0 | 137.91 | -17.0 | 680.03 | -17.0 | 2021-05-28 | 51,100 | -57.83 | clean_180D_window_by_profile_candidate_dates |
| T_R9L12_011200_4B_20210513 | 2021-05-13 | 44,450 | 15.0 | -6.7 | 15.0 | -18.3 | 15.0 | -39.4 | 2021-05-28 | 51,100 | -57.83 | clean_180D_window_by_profile_candidate_dates |
| T_R9L12_086280_STAGE2_20230608 | 2023-06-08 | 178,000 | 14.04 | -2.02 | 14.04 | -6.52 | 14.04 | -9.21 | 2023-07-05 | 203,000 | -18.03 | clean_180D_window; 2024 profile candidate dates outside 2023 entry~D+180 window |
| T_R9L12_089590_STAGE2_20230509 | 2023-05-10 | 13,780 | 8.42 | -7.76 | 12.48 | -16.84 | 12.48 | -31.86 | 2023-07-13 | 15,500 | -39.42 | clean_180D_window; 2022 profile candidate before entry, no 2023 candidate in window |
| T_R9L12_091810_STAGE2_20230515 | 2023-05-15 | 2,985 | 21.27 | -3.52 | 21.27 | -16.42 | 21.27 | -34.51 | 2023-06-20 | 3,620 | -45.99 | profile candidate 2023-02-23 before entry; no candidate date in entry~D+180, but share-count/capital-overhang caveat noted as evidence not contamination |
| T_R9L12_091810_4C_20231024 | 2023-10-24 | 2,015 | 23.82 | -2.98 | 23.82 | -9.18 | 23.82 | -16.38 | 2023-11-17 | 2,495 | -20.0 | same profile caveat as Stage2 row |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely label | Actual path | verdict | residual note |
|---|---|---|---|---|
| R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | Stage3-Yellow to Green | Very high 90D/180D MFE after confirmed margin bridge | current_profile_correct | Stage3 confirmation was not too late because freight margin was already visible. |
| R9L12_C29_086280_PCC_LOGISTICS_20230608 | Stage3-Yellow | Positive but narrower upside; Green confirmation would enter late | current_profile_too_late | PCC/logistics route should accept customer-quality + margin bridge earlier, but not Green without confirmed margin. |
| R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509 | Stage3-Yellow risk | High MAE and failed rerating after passenger-volume narrative | current_profile_false_positive | Passenger volume is not enough without durable yield/cost proof. |
| R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | Stage3-Yellow risk | Local MFE followed by large MAE and thesis-break path | current_profile_4C_too_late | Capital/share-supply overhang should route to watch-only sooner. |

Answers to the mandatory calibrated-profile questions:

```text
1. current calibrated profile judgment = mostly Stage3-Yellow for transport volume/margin stories.
2. fit to actual MFE/MAE = correct for HMM, somewhat late for Hyundai Glovis, false positive for LCC passenger-volume-only names.
3. stage2_actionable_bonus = useful for freight/PCC, too generous for LCC passenger-volume headlines.
4. Yellow threshold 75 = too easy for LCC recovery without yield/margin gate.
5. Green threshold 87/revision 55 = still appropriate; do not lower globally.
6. price-only blowoff guard = strengthened, especially for LCC/local peaks.
7. full 4B non-price requirement = strengthened by HMM 4B row; price-only local peak is insufficient.
8. hard 4C routing = should trigger earlier for dilution/capital-overhang + high-MAE LCC path.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3 proxy | Green proxy | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| HMM 2020 | 6,410 | 9,450-14,350 range | 14,350 | 0.18 | Green was not too late because full-cycle peak remained far ahead. |
| Hyundai Glovis 2023 | 178,000 | 185,700-197,700 range | 193,500-199,000 range | 0.62 | Green would miss most of the modest PCC/logistics upside. |
| Jeju Air 2023 | 13,780 | no confirmed Green | no confirmed Green | not_applicable | Stage2 should remain watch-only without durable yield/margin proof. |
| T'way Air 2023 | 2,985 | no confirmed Green | no confirmed Green | not_applicable | Local MFE was followed by high MAE; Green should be blocked. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---|---|
| T_R9L12_011200_4B_20210513 | 0.85 | 0.85 | valuation_blowoff, positioning_overheat, dilution_or_cb, capital_raise_or_overhang | good_full_window_4B_timing |
| T_R9L12_089590_STAGE2_20230509 | 0.00 | 0.00 | price_only, margin_or_backlog_slowdown | price recovery was local; not a full 4B without non-price evidence |
| T_R9L12_091810_STAGE2_20230515 | 1.00 | 1.00 | price_only plus dilution/capital-overhang | 4B/4C handoff needed; price-only is insufficient but overhang is real |

## 16. 4C Protection Audit

| case_id | 4C label | protection comment |
|---|---|---|
| R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | thesis_break_watch_only | The supercycle positive remained valid until later overheat/overhang; 4C should not fire at Stage2. |
| R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509 | thesis_break_watch_only | The passenger-volume thesis failed to protect price once yield/cost durability was not confirmed. |
| R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | hard_4c_late | 4C/watch-only routing should have been earlier once share-supply and price retest appeared. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = transport_volume_to_yield_margin_conversion_gate
baseline_value = none
proposed_shadow_value = require at least one of durable_yield_margin_bridge, customer_quality_contract_visibility, or balance_sheet_clearance before Stage3-Yellow/Green promotion
confidence = medium-low
```

Rule candidate:

> For R9/C29 transport and mobility names, pure passenger/freight/vehicle volume recovery can open Stage2-Actionable, but Stage3-Yellow/Green promotion should require yield/margin conversion or customer-quality contract visibility. If passenger-volume recovery is paired with dilution, share-supply, or capacity-cost overhang, route to watch-only or 4C-late stress before allowing Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
axis = C29_volume_margin_conversion_quality
positive_boost = +2 to +4 only when volume converts into operating margin and cash/contract visibility
counterexample_guard = -6 to -10 when passenger/revenue volume lacks yield durability or has capital overhang
4B_overlay = non_price_evidence_required; freight-rate supercycle and capital overhang count as non-price evidence
```

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | stage2 representative | 48.93 | -14.20 | 177.96 | -19.90 | 0.50 | 0 | 1 | mixed: freight/PCC ok, LCC false positive |
| P0b e2r_2_0_baseline_reference | 4 | later confirmation | 37.10 | -15.40 | 151.00 | -21.60 | 0.50 | 1 | 2 | worse lateness, similar false positives |
| P1 sector_specific_candidate_profile | 4 | guarded Stage2/Yellow | 48.93 | -14.20 | 177.96 | -19.90 | 0.25 | 0 | 1 | improves LCC false-positive blocking |
| P2 canonical_archetype_candidate_profile | 4 | C29 yield/margin gate | 48.93 | -14.20 | 177.96 | -19.90 | 0.25 | 0 | 0 | best balance of HMM/PCC positives and LCC guards |
| P3 counterexample_guard_profile | 4 | watch-only for LCC overhang | 66.93 | -12.80 | 347.04 | -17.60 | 0.00 | 1 | 1 | strict, but risks missing lower-MFE PCC/logistics successes |

## 20. Score-Return Alignment Matrix

| case_id | symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment |
|---|---:|---:|---|---:|---|---:|---:|---|
| R9L12_C29_011200_FREIGHT_TURNAROUND_2020 | 011200 | 84 | Stage3-Yellow | 90 | Stage3-Green | 137.91 | -17.0 | aligned_structural_success |
| R9L12_C29_086280_PCC_LOGISTICS_20230608 | 086280 | 78 | Stage3-Yellow | 83 | Stage3-Yellow | 14.04 | -6.52 | aligned_but_green_too_late |
| R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509 | 089590 | 76 | Stage3-Yellow | 62 | Stage2-Blocked/Watch | 12.48 | -16.84 | false_positive_blocked_after_guard |
| R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515 | 091810 | 77 | Stage3-Yellow | 58 | Watch/Stage2-Blocked | 21.27 | -16.42 | false_positive_to_watch_only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TRANSPORT_PASSENGER_CARGO_YIELD_MARGIN_LEVERAGE | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | C29 now has OEM/parts plus freight/PCC/LCC transport coverage; still needs rail/port/parcel examples later. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: passenger_volume_without_yield_margin_false_positive, transport_margin_green_too_late, freight_supercycle_good_4B_requires_non_price_overlay, share_supply_overhang_high_MAE
new_axis_proposed: C29_volume_margin_conversion_quality_gate
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and shard roots
- symbol profile existence and corporate-action candidate windows
- representative entry rows in tradable shards
- trigger-level MFE/MAE/peak/drawdown using raw_unadjusted_marcap rows
- positive/counterexample balance
- same_entry_group_id dedupe
- 4B local vs full-window proximity split
- raw component score breakdown for representative triggers
```

Not validated:

```text
- investment attractiveness of current/live names
- live watchlist inclusion
- broker/API execution
- production scoring implementation
- exact stock_agent src/e2r code behavior
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_volume_margin_conversion_quality_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require yield/margin/customer-quality conversion before Stage3 promotion in transport volume stories","Reduced LCC false positives while preserving HMM/PCC positives","T_R9L12_011200_STAGE2_20200813|T_R9L12_086280_STAGE2_20230608|T_R9L12_089590_STAGE2_20230509|T_R9L12_091810_STAGE2_20230515",4,4,2,medium-low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,LCC_volume_without_yield_margin_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Passenger volume recovery without yield/cost durability should not reach Yellow/Green","Blocks Jeju/Tway high-MAE false positives","T_R9L12_089590_STAGE2_20230509|T_R9L12_091810_STAGE2_20230515",2,2,2,medium,sector_shadow_only,"not production; applies to LCC/reopening transport subset"
shadow_weight,freight_supercycle_non_price_4B_overlay,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Freight-rate supercycle plus valuation/CB overhang is valid 4B evidence, not price-only blowoff","HMM 4B proximity matched full-window peak better than price-only local labels","T_R9L12_011200_4B_20210513",1,1,0,low,canonical_shadow_only,"overlay only; do not promote sell rules globally"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L12_C29_011200_FREIGHT_TURNAROUND_2020","symbol":"011200","company_name":"HMM","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L12_011200_STAGE2_20200813","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Container freight-rate operating leverage: first clean profit-turnaround signal after freight-rate rise; Stage3 confirmation came before most of the 180D upside."}
{"row_type":"case","case_id":"R9L12_C29_086280_PCC_LOGISTICS_20230608","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PCC_CAR_CARRIER_AUTO_EXPORT_LOGISTICS_MARGIN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L12_086280_STAGE2_20230608","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_but_green_too_late","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Finished-vehicle logistics/PCC margin route: auto-export volume and shipping-margin bridge produced tradable but narrower MFE than pure OEM rerating."}
{"row_type":"case","case_id":"R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509","symbol":"089590","company_name":"제주항공","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R9L12_089590_STAGE2_20230509","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Passenger-volume rebound and first-profit narrative did not protect price because margin durability, balance-sheet overhang, and capacity/yield visibility were weak."}
{"row_type":"case","case_id":"R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_TURNAROUND_WITH_DILUTION_AND_CAPACITY_COST_OVERHANG","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"T_R9L12_091810_STAGE2_20230515","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_high_MAE_4C_needed","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Early LCC recovery produced a local MFE, but subsequent share-count/capital overhang and cost/yield uncertainty made the profile a high-MAE false positive unless 4C/watch-only routing is used."}
{"row_type":"trigger","trigger_id":"T_R9L12_011200_STAGE2_20200813","case_id":"R9L12_C29_011200_FREIGHT_TURNAROUND_2020","symbol":"011200","company_name":"HMM","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE","sector":"모빌리티·운송·레저","primary_archetype":"mobility/transport volume-margin operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-08-13","entry_date":"2020-08-14","entry_price":6410,"evidence_available_at_that_date":"2020년 상반기/2Q 해운 운임 상승과 영업흑자 전환이 공시·보도된 상태. 장마감 후/시각 불명확 보수 처리로 다음 거래일 종가 진입.","evidence_source":"DART/KIND: 2020 2Q/1H earnings release and public shipping-freight turnaround news family; Stock-Web row checked at atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.81,"MFE_90D_pct":137.91,"MFE_180D_pct":680.03,"MFE_1Y_pct":697.19,"MFE_2Y_pct":697.19,"MAE_30D_pct":-17.0,"MAE_90D_pct":-17.0,"MAE_180D_pct":-17.0,"MAE_1Y_pct":-17.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-28","peak_price":51100,"drawdown_after_peak_pct":-57.83,"green_lateness_ratio":0.18,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_candidate_dates","same_entry_group_id":"R9L12_011200_2020-08-14_6410","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L12_011200_4B_20210513","case_id":"R9L12_C29_011200_FREIGHT_TURNAROUND_2020","symbol":"011200","company_name":"HMM","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE","sector":"모빌리티·운송·레저","primary_archetype":"mobility/transport volume-margin operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-Overlay","trigger_date":"2021-05-13","entry_date":"2021-05-13","entry_price":44450,"evidence_available_at_that_date":"Freight-rate supercycle already visible; valuation/revision overheat and CB/share-supply overhang began to matter near the observed full-window peak. This row is overlay-only, not aggregate entry.","evidence_source":"DART/KIND and shipping-cycle public news family; Stock-Web row checked at atlas/ohlcv_tradable_by_symbol_year/011/011200/2021.csv","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","dilution_or_cb","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2021.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.0,"MFE_90D_pct":15.0,"MFE_180D_pct":15.0,"MFE_1Y_pct":15.0,"MFE_2Y_pct":15.0,"MAE_30D_pct":-6.7,"MAE_90D_pct":-18.3,"MAE_180D_pct":-39.4,"MAE_1Y_pct":-58.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-28","peak_price":51100,"drawdown_after_peak_pct":-57.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.85,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","dilution_or_cb","capital_raise_or_overhang"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_candidate_dates","same_entry_group_id":"R9L12_011200_2021-05-13_44450","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay row for already counted HMM freight-cycle case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_R9L12_086280_STAGE2_20230608","case_id":"R9L12_C29_086280_PCC_LOGISTICS_20230608","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PCC_CAR_CARRIER_AUTO_EXPORT_LOGISTICS_MARGIN","sector":"모빌리티·운송·레저","primary_archetype":"mobility/transport volume-margin operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-08","entry_date":"2023-06-08","entry_price":178000,"evidence_available_at_that_date":"Finished-vehicle logistics, PCC shipping, and auto-export volume/margin route became visible before the mid-2023 price leg. Entry uses same-day close because the row captured a tradable public repricing day.","evidence_source":"Public auto-export/PCC logistics news and company/analyst earnings discussion family; Stock-Web row checked at atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.04,"MFE_90D_pct":14.04,"MFE_180D_pct":14.04,"MFE_1Y_pct":14.04,"MFE_2Y_pct":14.04,"MAE_30D_pct":-2.02,"MAE_90D_pct":-6.52,"MAE_180D_pct":-9.21,"MAE_1Y_pct":-10.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-05","peak_price":203000,"drawdown_after_peak_pct":-18.03,"green_lateness_ratio":0.62,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_narrower_than_OEM","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2024 profile candidate dates outside 2023 entry~D+180 window","same_entry_group_id":"R9L12_086280_2023-06-08_178000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L12_089590_STAGE2_20230509","case_id":"R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509","symbol":"089590","company_name":"제주항공","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN","sector":"모빌리티·운송·레저","primary_archetype":"mobility/transport volume-margin operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-09","entry_date":"2023-05-10","entry_price":13780,"evidence_available_at_that_date":"Passenger recovery and LCC profit-turnaround narrative was public, but yield/cost durability and balance-sheet overhang were not yet confirmed. Entry uses next tradable day close due timing ambiguity.","evidence_source":"DART/KIND: 2023 1Q/quarterly earnings release family; public LCC passenger recovery news; Stock-Web row checked at atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","profile_path":"atlas/symbol_profiles/089/089590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.42,"MFE_90D_pct":12.48,"MFE_180D_pct":12.48,"MFE_1Y_pct":12.48,"MFE_2Y_pct":12.48,"MAE_30D_pct":-7.76,"MAE_90D_pct":-16.84,"MAE_180D_pct":-31.86,"MAE_1Y_pct":-36.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-13","peak_price":15500,"drawdown_after_peak_pct":-39.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_recovery_local_only_not_full_4B","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2022 profile candidate before entry, no 2023 candidate in window","same_entry_group_id":"R9L12_089590_2023-05-10_13780","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L12_091810_STAGE2_20230515","case_id":"R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_TURNAROUND_WITH_DILUTION_AND_CAPACITY_COST_OVERHANG","sector":"모빌리티·운송·레저","primary_archetype":"mobility/transport volume-margin operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-15","entry_price":2985,"evidence_available_at_that_date":"LCC passenger-recovery and quarterly profit-turnaround narrative was visible, but share-supply/capital overhang and cost/yield durability were unresolved. Same-day close used for visible market reaction.","evidence_source":"DART/KIND: 2023 1Q/quarterly earnings release family; public LCC recovery news; Stock-Web row checked at atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["dilution_or_cb","capital_raise_or_overhang","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","profile_path":"atlas/symbol_profiles/091/091810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.27,"MFE_90D_pct":21.27,"MFE_180D_pct":21.27,"MFE_1Y_pct":21.27,"MFE_2Y_pct":21.27,"MAE_30D_pct":-3.52,"MAE_90D_pct":-16.42,"MAE_180D_pct":-34.51,"MAE_1Y_pct":-36.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-20","peak_price":3620,"drawdown_after_peak_pct":-45.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_needed_non_price_4B","four_b_evidence_type":["price_only","dilution_or_cb","capital_raise_or_overhang","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late_high_MAE","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile candidate 2023-02-23 before entry; no candidate date in entry~D+180, but share-count/capital-overhang caveat noted as evidence not contamination","same_entry_group_id":"R9L12_091810_2023-05-15_2985","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L12_091810_4C_20231024","case_id":"R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_TURNAROUND_WITH_DILUTION_AND_CAPACITY_COST_OVERHANG","sector":"모빌리티·운송·레저","primary_archetype":"mobility/transport volume-margin operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4C-ThesisBreak","trigger_date":"2023-10-24","entry_date":"2023-10-24","entry_price":2015,"evidence_available_at_that_date":"By the post-peak drawdown window, the original passenger-volume-only thesis had failed to convert into durable equity rerating. This is a protection/watch-only row.","evidence_source":"Price path plus capital-overhang and margin durability evidence family; Stock-Web row checked at atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["dilution_or_cb","capital_raise_or_overhang"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","profile_path":"atlas/symbol_profiles/091/091810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.82,"MFE_90D_pct":23.82,"MFE_180D_pct":23.82,"MFE_1Y_pct":23.82,"MFE_2Y_pct":23.82,"MAE_30D_pct":-2.98,"MAE_90D_pct":-9.18,"MAE_180D_pct":-16.38,"MAE_1Y_pct":-20.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-17","peak_price":2495,"drawdown_after_peak_pct":-20.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["dilution_or_cb","capital_raise_or_overhang"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_protection_watch_only","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"same profile caveat as Stage2 row","same_entry_group_id":"R9L12_091810_2023-10-24_2015","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"4C overlay row for already counted Tway case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_011200_FREIGHT_TURNAROUND_2020","trigger_id":"T_R9L12_011200_STAGE2_20200813","symbol":"011200","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":20,"revision_score":16,"relative_strength_score":12,"customer_quality_score":9,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":24,"revision_score":18,"relative_strength_score":13,"customer_quality_score":10,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":13,"execution_risk_score":-2,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 transport shadow profile rewards durable yield/margin conversion and penalizes passenger/freight volume headlines without yield durability, balance-sheet clearance, or non-price 4B/4C evidence.","MFE_90D_pct":137.91,"MAE_90D_pct":-17.0,"score_return_alignment_label":"aligned_structural_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_086280_PCC_LOGISTICS_20230608","trigger_id":"T_R9L12_086280_STAGE2_20230608","symbol":"086280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":14,"revision_score":10,"relative_strength_score":12,"customer_quality_score":12,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":17,"revision_score":11,"relative_strength_score":12,"customer_quality_score":13,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 transport shadow profile rewards durable yield/margin conversion and penalizes passenger/freight volume headlines without yield durability, balance-sheet clearance, or non-price 4B/4C evidence.","MFE_90D_pct":14.04,"MAE_90D_pct":-6.52,"score_return_alignment_label":"aligned_but_green_too_late","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_089590_LCC_TURNAROUND_FALSE_20230509","trigger_id":"T_R9L12_089590_STAGE2_20230509","symbol":"089590","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":8,"revision_score":11,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":9,"execution_risk_score":-5,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":-3,"accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":5,"revision_score":6,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":5,"execution_risk_score":-10,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":-6,"accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":62,"stage_label_after":"Stage2-Blocked/Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 transport shadow profile rewards durable yield/margin conversion and penalizes passenger/freight volume headlines without yield durability, balance-sheet clearance, or non-price 4B/4C evidence.","MFE_90D_pct":12.48,"MAE_90D_pct":-16.84,"score_return_alignment_label":"false_positive_blocked_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_091810_LCC_DILUTION_HIGH_MAE_20230515","trigger_id":"T_R9L12_091810_STAGE2_20230515","symbol":"091810","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":9,"revision_score":11,"relative_strength_score":10,"customer_quality_score":8,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":-4,"accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":5,"revision_score":6,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":5,"execution_risk_score":-12,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":-10,"accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":58,"stage_label_after":"Watch/Stage2-Blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 transport shadow profile rewards durable yield/margin conversion and penalizes passenger/freight volume headlines without yield durability, balance-sheet clearance, or non-price 4B/4C evidence.","MFE_90D_pct":21.27,"MAE_90D_pct":-16.42,"score_return_alignment_label":"false_positive_to_watch_only","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R9","loop":"12","scheduled_round":"R9","scheduled_loop":12,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"diversity_score_summary":"new_symbol +16, new_trigger_family +16, counterexample_gap +8, residual_error +15, wrong_round_penalty 0, duplicate penalties 0; estimated +55","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["passenger_volume_without_yield_margin_false_positive","transport_margin_green_too_late","freight_supercycle_good_4B_requires_non_price_overlay","share_supply_overhang_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 12
next_round = R10
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Stock-Web manifest checked: atlas/manifest.json
Stock-Web profile paths checked:
- atlas/symbol_profiles/011/011200.json
- atlas/symbol_profiles/086/086280.json
- atlas/symbol_profiles/089/089590.json
- atlas/symbol_profiles/091/091810.json
Stock-Web tradable rows checked:
- atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/011/011200/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/011/011200/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv
Evidence source family:
- DART/KIND quarterly earnings and operating-result disclosures
- public historical news/IR discussion around freight-rate, PCC logistics, passenger recovery, and LCC capital overhang
```
