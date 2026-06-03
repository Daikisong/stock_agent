# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R9_loop_13_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round = R9
scheduled_loop = 13
completed_round = R9
completed_loop = 13
next_round = R10
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TRANSPORT_MARGIN_CONVERSION_VS_AIRLINE_VOLUME_GUARD
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
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

The residual question is not whether mobility volume can rerate. It can. The question is **which volume becomes earnings**. In C29 the same passenger or freight count is just the river level; profit arrives only when the channel has pricing, cost control, and margin banks to hold the water.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 13 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | TRANSPORT_MARGIN_CONVERSION_VS_AIRLINE_VOLUME_GUARD |
| valid round-sector pair | yes |
| stock_agent code access | false |
| price atlas access | required and used |

R9 permits L3 when the research target is mobility/transport volume and operating leverage. This loop remains inside R9 and C29, but it avoids the previously used OEM, tire, module, thermal, HMM/PCC logistics, and LCC symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result files before this run contained:

```text
R9 Loop 10 symbols = 005380, 000270, 204320
R9 Loop 11 symbols = 161390, 012330, 011210, 018880
R9 Loop 12 symbols = 011200, 086280, 089590, 091810
this_loop_symbols = 000120, 028670, 003490, 272450
same_symbol_same_trigger_date_research = avoided
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
```

The loop is still the same canonical archetype, but the cases are independent: parcel/contract logistics, dry-bulk shipping, full-service airline overhang, and an LCC holdout.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest fields checked:

| manifest field | observed value |
| --- | --- |
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
calibration_usable_trigger_rows = 7
```

Symbol profile caveats:

| symbol | company | profile path | profile caveat handling |
| --- | --- | --- | --- |
| 000120 | CJ대한통운 | atlas/symbol_profiles/000/000120.json | old corporate-action candidate dates are before 2010; 2023-11-14 representative window is clean |
| 028670 | 팬오션 | atlas/symbol_profiles/028/028670.json | profile candidate dates are before 2016; 2021 representative windows are clean |
| 003490 | 대한항공 | atlas/symbol_profiles/003/003490.json | 2020/2021 profile candidate dates are before 2024 entry; 180D window clean |
| 272450 | 진에어 | atlas/symbol_profiles/272/272450.json | 2020 candidate date is before 2023 entry; 180D window clean |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
| --- | --- | --- |
| PARCEL_CONTRACT_LOGISTICS_MARGIN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Parcel and contract-logistics volume matters only when cost automation and mix convert it into margin. |
| DRYBULK_FREIGHT_YIELD_OPERATING_LEVERAGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Freight-rate/yield is the margin bridge for transport capacity. |
| FSC_PASSENGER_RECOVERY_REGULATORY_COST_OVERHANG | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Passenger recovery is C29, but regulatory integration, fuel/FX and cost overhang can block rerating. |
| LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN_HOLDOUT | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | LCC traffic recovery is not enough without durable yield/cost proof. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | trigger family | new independent? |
| --- | --- | --- | --- | --- | --- | --- |
| R9L13_C29_000120_PARCEL_MARGIN_20231113 | 000120 | CJ대한통운 | structural_success | positive | parcel/contract logistics margin conversion | true |
| R9L13_C29_028670_DRYBULK_YIELD_20210219 | 028670 | 팬오션 | structural_success | positive | dry-bulk freight yield and utilization | true |
| R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130 | 003490 | 대한항공 | failed_rerating | counterexample | FSC passenger recovery with merger/regulatory/cost overhang | true |
| R9L13_C29_272450_LCC_HOLDOUT_20230515 | 272450 | 진에어 | 4C_late | counterexample | LCC passenger recovery holdout | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
minimum_new_independent_case_ratio = 0.60
```

The new contribution is the finer split inside C29:

- **CJ대한통운 / 팬오션**: volume was converted into margin or yield; Stage2/Yellows were useful.
- **대한항공 / 진에어**: volume/recovery existed, but cost, regulatory, or yield durability was insufficient; current profile can over-promote.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| R9L13_C29_000120_PARCEL_MARGIN_20231113 | parcel/contract logistics volume route; early revision signal | margin bridge and financial visibility | valuation/positioning overheat after fast rerating | watch-only after local peak |
| R9L13_C29_028670_DRYBULK_YIELD_20210219 | dry-bulk freight-rate/yield route; relative strength | margin bridge and freight-cycle visibility | freight-cycle overheat/revision slowdown | watch-only after freight-cycle rollover |
| R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130 | FSC passenger recovery plus regulatory optionality | not confirmed at trigger; cost/yield bridge incomplete | regulatory/integration/cost overhang | thesis-break watch only |
| R9L13_C29_272450_LCC_HOLDOUT_20230515 | LCC passenger volume recovery | not confirmed; yield/cost bridge incomplete | price-only local peak, margin slowdown | thesis evidence broken after high-MAE path |

## 10. Price Data Source Map

| symbol | year shards used | profile path | entry rows checked |
| --- | --- | --- | --- |
| 000120 | 2023, 2024 | atlas/symbol_profiles/000/000120.json | 2023-11-14 close 79,500; 2024-02-02 close 148,500 |
| 028670 | 2021 | atlas/symbol_profiles/028/028670.json | 2021-02-19 close 5,310; 2021-06-29 close 8,530 |
| 003490 | 2024 | atlas/symbol_profiles/003/003490.json | 2024-01-31 close 22,500 |
| 272450 | 2023, 2024 | atlas/symbol_profiles/272/272450.json | 2023-05-15 close 15,490; 2023-10-20 close 10,310 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome | current_profile_verdict | dedupe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_R9L13_000120_STAGE2_20231113 | R9L13_C29_000120_PARCEL_MARGIN_20231113 | 000120 | CJ대한통운 | Stage2-Actionable | 2023-11-13 | 2023-11-14 | 79,500 | 86.92 | -1.01 | 86.92 | -1.01 | structural_success_margin_conversion | current_profile_correct | True |
| T_R9L13_000120_4B_20240202 | R9L13_C29_000120_PARCEL_MARGIN_20231113 | 000120 | CJ대한통운 | Stage4B-Overlay | 2024-02-02 | 2024-02-02 | 148,500 | 0.07 | -36.16 | 0.07 | -40.0 | 4B_overlay_success | current_profile_4B_too_late | False |
| T_R9L13_028670_STAGE2_20210219 | R9L13_C29_028670_DRYBULK_YIELD_20210219 | 028670 | 팬오션 | Stage2-Actionable | 2021-02-19 | 2021-02-19 | 5,310 | 67.98 | -5.84 | 67.98 | -5.84 | structural_success_freight_yield | current_profile_correct | True |
| T_R9L13_028670_4B_20210629 | R9L13_C29_028670_DRYBULK_YIELD_20210219 | 028670 | 팬오션 | Stage4B-Overlay | 2021-06-29 | 2021-06-29 | 8,530 | 4.57 | -31.3 | 4.57 | -40.45 | 4B_overlay_success | current_profile_4B_too_late | False |
| T_R9L13_003490_STAGE2_20240130 | R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130 | 003490 | 대한항공 | Stage2-Actionable | 2024-01-30 | 2024-01-31 | 22,500 | 5.56 | -11.29 | 6.44 | -11.29 | failed_rerating_low_MFE | current_profile_false_positive | True |
| T_R9L13_272450_STAGE2_20230515 | R9L13_C29_272450_LCC_HOLDOUT_20230515 | 272450 | 진에어 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 15,490 | 11.04 | -22.79 | 11.04 | -35.31 | failed_rerating_high_MAE_holdout | current_profile_4C_too_late | True |
| T_R9L13_272450_4C_20231020 | R9L13_C29_272450_LCC_HOLDOUT_20230515 | 272450 | 진에어 | Stage4C-ThesisBreak | 2023-10-20 | 2023-10-20 | 10,310 | 32.59 | -2.81 | 38.6 | -2.81 | 4C_late_watch_only | current_profile_4C_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | corp-action status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_R9L13_000120_STAGE2_20231113 | 2023-11-14 | 79,500 | 63.02 | -1.01 | 86.92 | -1.01 | 86.92 | -1.01 | 2024-02-02 | 148,600 | -40.04 | clean_180D_window; old profile candidates before 2010 only |
| T_R9L13_000120_4B_20240202 | 2024-02-02 | 148,500 | 0.07 | -20.0 | 0.07 | -36.16 | 0.07 | -40.0 | 2024-02-02 | 148,600 | -40.04 | clean_180D_window; old profile candidates before 2010 only |
| T_R9L13_028670_STAGE2_20210219 | 2021-02-19 | 5,310 | 39.17 | -5.84 | 67.98 | -5.84 | 67.98 | -5.84 | 2021-06-29 | 8,920 | -43.05 | clean_180D_window; profile candidates before 2016 only |
| T_R9L13_028670_4B_20210629 | 2021-06-29 | 8,530 | 4.57 | -12.54 | 4.57 | -31.3 | 4.57 | -40.45 | 2021-06-29 | 8,920 | -43.05 | clean_180D_window; profile candidates before 2016 only |
| T_R9L13_003490_STAGE2_20240130 | 2024-01-31 | 22,500 | 5.56 | -2.67 | 5.56 | -11.29 | 6.44 | -11.29 | 2024-06-27 | 23,950 | -16.66 | clean_180D_window; 2020/2021 candidates before entry |
| T_R9L13_272450_STAGE2_20230515 | 2023-05-15 | 15,490 | 11.04 | -6.26 | 11.04 | -22.79 | 11.04 | -35.31 | 2023-06-20 | 17,200 | -41.74 | clean_180D_window; 2020 candidate before entry |
| T_R9L13_272450_4C_20231020 | 2023-10-20 | 10,310 | 13.0 | -2.81 | 32.59 | -2.81 | 38.6 | -2.81 | 2024-04-01 | 14,290 | -37.0 | clean_180D_window; 2020 candidate before entry |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely label | Actual path | verdict | residual note |
| --- | --- | --- | --- | --- |
| R9L13_C29_000120_PARCEL_MARGIN_20231113 | Stage3-Yellow | MFE_90/180 +86.92%, initial MAE -1.01% | current_profile_correct | C29 should reward actual margin conversion. |
| R9L13_C29_028670_DRYBULK_YIELD_20210219 | Stage3-Yellow | MFE_90/180 +67.98%, controlled initial MAE | current_profile_correct | Freight yield behaved as operating leverage; later needs 4B cycle overlay. |
| R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130 | Stage3-Yellow risk | MFE_180 only +6.44%, MAE_90/180 -11.29% | current_profile_false_positive | Passenger recovery plus regulatory optionality was not enough without cost/yield bridge. |
| R9L13_C29_272450_LCC_HOLDOUT_20230515 | Stage3-Yellow risk | MFE_180 +11.04%, MAE_180 -35.31% | current_profile_4C_too_late | LCC holdout confirms that traffic recovery alone needs earlier 4C watch. |

Mandatory calibrated-profile answers:

```text
1. current calibrated profile judgment = likely Yellow for broad C29 volume/recovery bundles.
2. fit to actual MFE/MAE = correct for CJ대한통운 and 팬오션, false positive / 4C late for 대한항공 and 진에어.
3. stage2_actionable_bonus = useful when volume converts to yield/margin; too generous for airline volume-only.
4. Yellow threshold 75 = too easy for passenger-recovery headlines without yield/cost proof.
5. Green threshold 87/revision 55 = kept; do not lower globally.
6. price-only blowoff guard = strengthened, because CJ and Pan Ocean 4B needed non-price overheat/cycle context.
7. full 4B non-price requirement = strengthened, not weakened.
8. hard 4C routing = should fire earlier for LCC high-MAE paths when yield/cost bridge is not confirmed.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3 proxy | Green proxy | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- | --- |
| CJ대한통운 2023 | 79,500 | 113,000-130,000 range | near 140,000-148,500 range | 0.54 | Green confirmation would catch some upside but miss early rerating; Yellow is appropriate when margin bridge is visible. |
| 팬오션 2021 | 5,310 | 6,400-7,400 range | 8,500+ range | 0.43 | Green is not too late if freight/yield evidence is already clear, but 4B overlay must arrive near peak. |
| 대한항공 2024 | 22,500 | not confirmed | not confirmed | not_applicable | Volume/recovery remained watch-only without durable yield/cost proof. |
| 진에어 2023 | 15,490 | not confirmed | not confirmed | not_applicable | Local MFE was followed by high MAE; Green should be blocked. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
| --- | --- | --- | --- | --- |
| T_R9L13_000120_4B_20240202 | 1.00 | 1.00 | valuation_blowoff, positioning_overheat, price_only | good overlay timing; needs non-price context |
| T_R9L13_028670_4B_20210629 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat, revision_slowdown | good full-window 4B if freight-cycle evidence exists |
| T_R9L13_003490_STAGE2_20240130 | not_applicable | not_applicable | legal_or_regulatory_block, margin_or_backlog_slowdown | not full 4B; Stage2 should stay capped |
| T_R9L13_272450_STAGE2_20230515 | not_applicable | not_applicable | price_only, margin_or_backlog_slowdown | price-only local peak too early; high-MAE path needs 4C watch |

## 16. 4C Protection Audit

| case_id | 4C label | protection comment |
| --- | --- | --- |
| R9L13_C29_000120_PARCEL_MARGIN_20231113 | thesis_break_watch_only | 4B overlay mattered after local peak; initial thesis was valid and should not be hard-routed to 4C. |
| R9L13_C29_028670_DRYBULK_YIELD_20210219 | thesis_break_watch_only | Freight-cycle rollover required overlay, not immediate Stage2 rejection. |
| R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130 | thesis_break_watch_only | Regulatory/cost overhang should cap promotion rather than fire hard 4C at entry. |
| R9L13_C29_272450_LCC_HOLDOUT_20230515 | hard_4c_late | After high-MAE deterioration, earlier 4C watch would have protected from treating traffic recovery as durable rerating. |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = this is still one large_sector/canonical-archetype file, and R9/C29 already has several sector slices; proposed deltas remain canonical_archetype_specific rather than broad L3 sector-wide.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
candidate_rule_1 = C29_transport_margin_conversion_bonus
candidate_rule_2 = C29_airline_volume_without_yield_cost_cap
candidate_rule_3 = C29_transport_cycle_4B_non_price_overheat
```

Proposed compression:

```text
if C29 volume evidence has confirmed yield/cost/margin conversion:
    allow Stage2-Actionable to Stage3-Yellow promotion
elif C29 evidence is passenger-volume or regulatory optionality without yield/cost bridge:
    cap at Stage2-Watch / Stage2-Actionable, block Green
if C29 rerating reaches local peak and non-price overheat/cycle evidence appears:
    allow 4B overlay
if airline/LCC path shows high-MAE deterioration and thesis evidence remains unconfirmed:
    route to 4C watch earlier
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural | avg_green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | headline volume can reach Yellow if evidence bundle is broad | none | 4 | 42.88 | -10.23 | 43.09 | -13.36 | 50% | 0 | 0.49 | mixed; good positives but airline false positives |
| P0b e2r_2_0_baseline_reference | rollback reference | looser Yellow/Green and less 4B/4C separation | reference only | 4 | 42.88 | -10.23 | 43.09 | -13.36 | 50% | 0 | 0.49 | worse false-positive control |
| P1 sector_specific_candidate_profile | sector shadow | transport-volume needs yield/cost/margin conversion | add margin-conversion gate | 4 | 77.45 | -3.43 | 77.45 | -3.43 | 0% | 0 | 0.49 | better; positives retained, airline false positives blocked |
| P2 canonical_archetype_candidate_profile | C29 shadow | C29 should separate volume, yield, cost, and regulatory overhang | C29_transport_margin_bridge_required | 4 | 77.45 | -3.43 | 77.45 | -3.43 | 0% | 0 | 0.49 | best candidate |
| P3 counterexample_guard_profile | guard profile | airline passenger-volume-only and FSC regulatory overhang stay watch-only | airline volume cap + 4C earlier | 4 | 77.45 | -3.43 | 77.45 | -3.43 | 0% | 0 | 0.49 | best risk-control profile |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D | MAE_90D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R9L13_C29_000120_PARCEL_MARGIN_20231113 | 82 | Stage3-Yellow | 86 | Stage3-Yellow+ | 86.92 | -1.01 | aligned_positive_margin_bridge |
| R9L13_C29_028670_DRYBULK_YIELD_20210219 | 80 | Stage3-Yellow | 84 | Stage3-Yellow+ | 67.98 | -5.84 | aligned_positive_freight_yield |
| R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130 | 76 | Stage3-Yellow | 66 | Stage2-Watch | 5.56 | -11.29 | improved_false_positive_control |
| R9L13_C29_272450_LCC_HOLDOUT_20230515 | 75 | Stage3-Yellow | 61 | Stage2-Watch/Blocked | 11.04 | -22.79 | improved_high_MAE_4C_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | PARCEL_CONTRACT_LOGISTICS_MARGIN_BRIDGE | DRYBULK_FREIGHT_YIELD_OPERATING_LEVERAGE | FSC/LCC_AIRLINE_VOLUME_GUARD | 2 | 2 | 2 | 1 | 4 | 0 | 7 | 4 | 3 | false | true | parcel/dry-bulk positives added; airline volume-only guard still needs more holdout cases |

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
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_4B_too_late
  - current_profile_4C_too_late
new_axis_proposed:
  - c29_transport_margin_conversion_bonus
  - c29_airline_volume_without_yield_cost_cap
  - c29_transport_cycle_4b_non_price_overheat
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Uses Songdaiki/stock-web tradable_raw OHLC rows only for price path.
- Uses manifest max_date = 2026-02-20 for forward-window eligibility.
- Uses representative trigger rows only for aggregate metrics.
- Deduplicates same-case 4B/4C overlays from aggregate.
- Treats score as research proxy, not production score.
```

Non-validation scope:

```text
- No current/live candidate discovery.
- No stock_agent src/e2r code access.
- No production scoring changes.
- No brokerage or auto-trading action.
- Evidence-source URL enrichment is deferred; this MD records historical evidence family and trigger date, not a full source dossier.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_transport_margin_conversion_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Parcel and dry-bulk cases with yield/cost/margin conversion had strong MFE and controlled MAE","positive cases retained while volume-only cases are not promoted","T_R9L13_000120_STAGE2_20231113|T_R9L13_028670_STAGE2_20210219",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_airline_volume_without_yield_cost_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"FSC/LCC passenger-volume narratives without durable yield/cost/regulatory clearance produced low MFE or high MAE","false positives reduced; 4C watch fires earlier","T_R9L13_003490_STAGE2_20240130|T_R9L13_272450_STAGE2_20230515",2,2,2,medium,canonical_shadow_only,"not production; strengthens existing airline/LCC guard"
shadow_weight,c29_transport_cycle_4b_non_price_overheat,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"CJ Logistics and Pan Ocean needed 4B overlay only after non-price cycle/valuation context, not from price alone","keeps full 4B separate from price-only local peaks","T_R9L13_000120_4B_20240202|T_R9L13_028670_4B_20210629",2,2,0,low,overlay_shadow_only,"not production"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L13_C29_000120_PARCEL_MARGIN_20231113", "symbol": "000120", "company_name": "CJ대한통운", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "PARCEL_CONTRACT_LOGISTICS_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R9L13_000120_STAGE2_20231113", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Parcel and contract-logistics margin bridge converted volume into operating leverage; price path had very high MFE with almost no initial MAE."}
{"row_type": "case", "case_id": "R9L13_C29_028670_DRYBULK_YIELD_20210219", "symbol": "028670", "company_name": "팬오션", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_FREIGHT_YIELD_OPERATING_LEVERAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R9L13_028670_STAGE2_20210219", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Freight-rate/yield upcycle created C29 operating leverage, but later 4B needed freight-cycle awareness."}
{"row_type": "case", "case_id": "R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130", "symbol": "003490", "company_name": "대한항공", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "FSC_PASSENGER_RECOVERY_REGULATORY_COST_OVERHANG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_R9L13_003490_STAGE2_20240130", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Passenger recovery and regulatory event optionality did not become durable margin rerating; current profile risks over-promoting volume without cost/yield proof."}
{"row_type": "case", "case_id": "R9L13_C29_272450_LCC_HOLDOUT_20230515", "symbol": "272450", "company_name": "진에어", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN_HOLDOUT", "case_type": "4C_late", "positive_or_counterexample": "counterexample", "best_trigger": "T_R9L13_272450_STAGE2_20230515", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_high_MAE", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Holdout LCC case: local MFE existed, but 180D high-MAE path confirms that passenger volume alone must not carry C29 Green."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "T_R9L13_000120_STAGE2_20231113", "case_id": "R9L13_C29_000120_PARCEL_MARGIN_20231113", "symbol": "000120", "company_name": "CJ대한통운", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "PARCEL_CONTRACT_LOGISTICS_MARGIN_BRIDGE", "sector": "mobility_transport_logistics", "primary_archetype": "transport volume to margin operating leverage", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-13", "entry_date": "2023-11-14", "entry_price": 79500, "evidence_available_at_that_date": "3Q/late-2023 parcel and contract-logistics margin narrative; price row checked on next tradable date", "evidence_source": "historical public earnings/disclosure event; exact URL enrichment deferred", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000120/2023.csv|atlas/ohlcv_tradable_by_symbol_year/000/000120/2024.csv", "profile_path": "atlas/symbol_profiles/000/000120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 63.02, "MFE_90D_pct": 86.92, "MFE_180D_pct": 86.92, "MFE_1Y_pct": 86.92, "MFE_2Y_pct": null, "MAE_30D_pct": -1.01, "MAE_90D_pct": -1.01, "MAE_180D_pct": -1.01, "MAE_1Y_pct": -40.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 148600, "drawdown_after_peak_pct": -40.04, "green_lateness_ratio": 0.54, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_margin_conversion", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; old profile candidates before 2010 only", "same_entry_group_id": "000120_2023-11-14_79500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L13_000120_4B_20240202", "case_id": "R9L13_C29_000120_PARCEL_MARGIN_20231113", "symbol": "000120", "company_name": "CJ대한통운", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "PARCEL_CONTRACT_LOGISTICS_MARGIN_BRIDGE", "sector": "mobility_transport_logistics", "primary_archetype": "transport volume to margin operating leverage", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 148500, "evidence_available_at_that_date": "fast rerating/local overheat after margin bridge; overlay only, not a thesis break", "evidence_source": "stock-web local peak plus prior margin-bridge context; exact URL enrichment deferred", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000120/2024.csv", "profile_path": "atlas/symbol_profiles/000/000120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.07, "MFE_90D_pct": 0.07, "MFE_180D_pct": 0.07, "MFE_1Y_pct": 0.07, "MFE_2Y_pct": null, "MAE_30D_pct": -20.0, "MAE_90D_pct": -36.16, "MAE_180D_pct": -40.0, "MAE_1Y_pct": -40.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 148600, "drawdown_after_peak_pct": -40.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_overlay_timing_but_requires_non_price_context", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; old profile candidates before 2010 only", "same_entry_group_id": "000120_2024-02-02_148500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used as 4B overlay timing row", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R9L13_028670_STAGE2_20210219", "case_id": "R9L13_C29_028670_DRYBULK_YIELD_20210219", "symbol": "028670", "company_name": "팬오션", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_FREIGHT_YIELD_OPERATING_LEVERAGE", "sector": "mobility_transport_shipping", "primary_archetype": "freight yield to transport operating leverage", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-02-19", "entry_date": "2021-02-19", "entry_price": 5310, "evidence_available_at_that_date": "dry-bulk freight/yield upcycle and volume-utilization operating leverage setup", "evidence_source": "historical public earnings/freight-cycle context; exact URL enrichment deferred", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv", "profile_path": "atlas/symbol_profiles/028/028670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.17, "MFE_90D_pct": 67.98, "MFE_180D_pct": 67.98, "MFE_1Y_pct": 67.98, "MFE_2Y_pct": null, "MAE_30D_pct": -5.84, "MAE_90D_pct": -5.84, "MAE_180D_pct": -5.84, "MAE_1Y_pct": -43.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-29", "peak_price": 8920, "drawdown_after_peak_pct": -43.05, "green_lateness_ratio": 0.43, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_freight_yield", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates before 2016 only", "same_entry_group_id": "028670_2021-02-19_5310", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L13_028670_4B_20210629", "case_id": "R9L13_C29_028670_DRYBULK_YIELD_20210219", "symbol": "028670", "company_name": "팬오션", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_FREIGHT_YIELD_OPERATING_LEVERAGE", "sector": "mobility_transport_shipping", "primary_archetype": "freight yield to transport operating leverage", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2021-06-29", "entry_date": "2021-06-29", "entry_price": 8530, "evidence_available_at_that_date": "freight-cycle local peak/positioning overheat after dry-bulk rerating", "evidence_source": "stock-web local peak plus historical freight-cycle context; exact URL enrichment deferred", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "revision_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv", "profile_path": "atlas/symbol_profiles/028/028670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.57, "MFE_90D_pct": 4.57, "MFE_180D_pct": 4.57, "MFE_1Y_pct": 4.57, "MFE_2Y_pct": null, "MAE_30D_pct": -12.54, "MAE_90D_pct": -31.3, "MAE_180D_pct": -40.45, "MAE_1Y_pct": -43.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-29", "peak_price": 8920, "drawdown_after_peak_pct": -43.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_if_freight_cycle_evidence_confirmed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates before 2016 only", "same_entry_group_id": "028670_2021-06-29_8530", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used as 4B freight-cycle overlay row", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R9L13_003490_STAGE2_20240130", "case_id": "R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130", "symbol": "003490", "company_name": "대한항공", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "FSC_PASSENGER_RECOVERY_REGULATORY_COST_OVERHANG", "sector": "mobility_transport_airline", "primary_archetype": "passenger recovery to airline operating leverage", "loop_objective": "counterexample_mining|residual_false_positive_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-30", "entry_date": "2024-01-31", "entry_price": 22500, "evidence_available_at_that_date": "FSC passenger recovery and merger/regulatory optionality; cost, FX, integration and regulatory overhang remained unresolved", "evidence_source": "historical public regulatory/earnings context; exact URL enrichment deferred", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003490/2024.csv", "profile_path": "atlas/symbol_profiles/003/003490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.56, "MFE_90D_pct": 5.56, "MFE_180D_pct": 6.44, "MFE_1Y_pct": 6.44, "MFE_2Y_pct": null, "MAE_30D_pct": -2.67, "MAE_90D_pct": -11.29, "MAE_180D_pct": -11.29, "MAE_1Y_pct": -11.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-27", "peak_price": 23950, "drawdown_after_peak_pct": -16.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_low_MFE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2020/2021 candidates before entry", "same_entry_group_id": "003490_2024-01-31_22500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L13_272450_STAGE2_20230515", "case_id": "R9L13_C29_272450_LCC_HOLDOUT_20230515", "symbol": "272450", "company_name": "진에어", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN_HOLDOUT", "sector": "mobility_transport_airline", "primary_archetype": "passenger recovery to airline operating leverage", "loop_objective": "holdout_validation|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "entry_date": "2023-05-15", "entry_price": 15490, "evidence_available_at_that_date": "LCC passenger-volume recovery and profit-turnaround narrative without durable yield/cost bridge", "evidence_source": "historical public earnings/passenger recovery context; exact URL enrichment deferred", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv|atlas/ohlcv_tradable_by_symbol_year/272/272450/2024.csv", "profile_path": "atlas/symbol_profiles/272/272450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.04, "MFE_90D_pct": 11.04, "MFE_180D_pct": 11.04, "MFE_1Y_pct": 11.04, "MFE_2Y_pct": null, "MAE_30D_pct": -6.26, "MAE_90D_pct": -22.79, "MAE_180D_pct": -35.31, "MAE_1Y_pct": -35.31, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-20", "peak_price": 17200, "drawdown_after_peak_pct": -41.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_local_4B_too_early_without_non_price_evidence", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating_high_MAE_holdout", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2020 candidate before entry", "same_entry_group_id": "272450_2023-05-15_15490", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L13_272450_4C_20231020", "case_id": "R9L13_C29_272450_LCC_HOLDOUT_20230515", "symbol": "272450", "company_name": "진에어", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LCC_PASSENGER_VOLUME_WITHOUT_DURABLE_YIELD_MARGIN_HOLDOUT", "sector": "mobility_transport_airline", "primary_archetype": "passenger recovery to airline operating leverage", "loop_objective": "4C_thesis_break_timing_test", "trigger_type": "Stage4C-ThesisBreak", "trigger_date": "2023-10-20", "entry_date": "2023-10-20", "entry_price": 10310, "evidence_available_at_that_date": "post-local-peak high-MAE path shows passenger-volume thesis did not sustain rerating", "evidence_source": "stock-web price path plus historical LCC yield/cost context; exact URL enrichment deferred", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv|atlas/ohlcv_tradable_by_symbol_year/272/272450/2024.csv", "profile_path": "atlas/symbol_profiles/272/272450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.0, "MFE_90D_pct": 32.59, "MFE_180D_pct": 38.6, "MFE_1Y_pct": 38.6, "MFE_2Y_pct": null, "MAE_30D_pct": -2.81, "MAE_90D_pct": -2.81, "MAE_180D_pct": -2.81, "MAE_1Y_pct": -2.81, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 14290, "drawdown_after_peak_pct": -37.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "4C_after_large_damage_but_before_full_recovery_noise", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4C_late_watch_only", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2020 candidate before entry", "same_entry_group_id": "272450_2023-10-20_10310", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used as 4C protection row", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L13_C29_000120_PARCEL_MARGIN_20231113", "trigger_id": "T_R9L13_000120_STAGE2_20231113", "symbol": "000120", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 18, "revision_score": 13, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 20, "revision_score": 14, "relative_strength_score": 16, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow+", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C29 shadow profile rewards actual transport volume to margin conversion and penalizes passenger/freight volume without durable yield, cost, or regulatory clearance.", "MFE_90D_pct": 86.92, "MAE_90D_pct": -1.01, "score_return_alignment_label": "aligned_positive_margin_bridge", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L13_C29_028670_DRYBULK_YIELD_20210219", "trigger_id": "T_R9L13_028670_STAGE2_20210219", "symbol": "028670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 17, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 19, "revision_score": 13, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow+", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C29 shadow profile rewards actual transport volume to margin conversion and penalizes passenger/freight volume without durable yield, cost, or regulatory clearance.", "MFE_90D_pct": 67.98, "MAE_90D_pct": -5.84, "score_return_alignment_label": "aligned_positive_freight_yield", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L13_C29_003490_FSC_RECOVERY_OVERHANG_20240130", "trigger_id": "T_R9L13_003490_STAGE2_20240130", "symbol": "003490", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 10, "valuation_repricing_score": 7, "execution_risk_score": -7, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 3, "customer_quality_score": 10, "policy_or_regulatory_score": 7, "valuation_repricing_score": 4, "execution_risk_score": -10, "legal_or_contract_risk_score": -7, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 66, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C29 shadow profile rewards actual transport volume to margin conversion and penalizes passenger/freight volume without durable yield, cost, or regulatory clearance.", "MFE_90D_pct": 5.56, "MAE_90D_pct": -11.29, "score_return_alignment_label": "improved_false_positive_control", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L13_C29_272450_LCC_HOLDOUT_20230515", "trigger_id": "T_R9L13_272450_STAGE2_20230515", "symbol": "272450", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C29 shadow profile rewards actual transport volume to margin conversion and penalizes passenger/freight volume without durable yield, cost, or regulatory clearance.", "MFE_90D_pct": 11.04, "MAE_90D_pct": -22.79, "score_return_alignment_label": "improved_high_MAE_4C_guard", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_transport_margin_conversion_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Parcel and dry-bulk cases with yield/cost/margin conversion had strong MFE and controlled MAE","positive cases retained while volume-only cases are not promoted","T_R9L13_000120_STAGE2_20231113|T_R9L13_028670_STAGE2_20210219",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_airline_volume_without_yield_cost_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"FSC/LCC passenger-volume narratives without durable yield/cost/regulatory clearance produced low MFE or high MAE","false positives reduced; 4C watch fires earlier","T_R9L13_003490_STAGE2_20240130|T_R9L13_272450_STAGE2_20230515",2,2,2,medium,canonical_shadow_only,"not production; strengthens existing airline/LCC guard"
shadow_weight,c29_transport_cycle_4b_non_price_overheat,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"CJ Logistics and Pan Ocean needed 4B overlay only after non-price cycle/valuation context, not from price alone","keeps full 4B separate from price-only local peaks","T_R9L13_000120_4B_20240202|T_R9L13_028670_4B_20210629",2,2,0,low,overlay_shadow_only,"not production"

```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "same_archetype_new_symbol +16; new_symbol +12; same_archetype_new_trigger_family +16; counterexample_gap +4; residual_error +15; wrong_round_penalty 0; estimated +63", "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_false_positive", "current_profile_4B_too_late", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected cases have forward 180D windows and clean representative calibration rows","price_source":"Songdaiki/stock-web","usage":"not_applicable"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 13
next_round = R10
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_web_universe = atlas/universe/all_symbols.csv
diagnostics_bundle = diagnostics/chatgpt_bundle.txt
profile_000120 = atlas/symbol_profiles/000/000120.json
profile_028670 = atlas/symbol_profiles/028/028670.json
profile_003490 = atlas/symbol_profiles/003/003490.json
profile_272450 = atlas/symbol_profiles/272/272450.json
price_rows_000120 = atlas/ohlcv_tradable_by_symbol_year/000/000120/2023.csv and 2024.csv
price_rows_028670 = atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv
price_rows_003490 = atlas/ohlcv_tradable_by_symbol_year/003/003490/2024.csv
price_rows_272450 = atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv and 2024.csv
research_artifact_access = local prior v12 MD filenames only for duplicate avoidance
stock_agent_code_accessed = false
stock_agent_patch_written = false
```
