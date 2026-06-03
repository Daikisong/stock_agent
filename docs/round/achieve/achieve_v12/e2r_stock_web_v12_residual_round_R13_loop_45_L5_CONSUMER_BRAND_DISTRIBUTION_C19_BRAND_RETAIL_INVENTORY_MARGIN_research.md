# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 45
selection_mode = auto_coverage_gap_fill
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = SNOWPEAK_APPAREL_RETAIL_SELL_THROUGH_MARGIN_BRIDGE | XEXYMIX_DTC_CHANNEL_REORDER_AND_OVERHEAT | NATIONAL_GEOGRAPHIC_INVENTORY_MARGIN_GUARD | GLOBAL_BRAND_TURNAROUND_INVENTORY_ABSORPTION_GUARD
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This Markdown is a standalone historical calibration artifact. It is not a live watchlist, not an investment recommendation, and not a code patch.

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

This loop does not re-prove the global profile. It stress-tests the residual behavior of C19, where a brand story can look like a clean rerating engine, but only some cases actually convert into sell-through, inventory absorption, and margin bridge.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
loop_objective = auto_coverage_gap_fill | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test
auto_selected_coverage_gap = C19 had insufficient post-calibrated positive/counterexample/4B coverage inside L5.
```

The core question is whether brand-retail evidence should be promoted on brand heat alone. The working answer from this loop is no: the positive path needs sell-through plus margin bridge; the counterexample path appears when inventory, discounting, or turnaround language fails to close.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research-artifact access was limited to coverage/duplicate avoidance. A repository search for the selected symbols did not return prior calibration rows for `036620`, `337930`, `298540`, or `081660`, so all four are treated as new independent cases for this C19 loop.

```text
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
required_new_independent_case_ratio = 0.60
actual_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest and schema were read before case construction.

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

```text
historical trigger = true
entry row exists in stock-web tradable shard = true
forward 180 trading days available by stock_web_manifest_max_date = true
high/low/close/volume present = true
MFE/MAE 30D/90D/180D computed = true
corporate_action_contaminated_180D_window = false
```

Profile-level caveat: several symbols have historical corporate-action candidates outside the tested 2024 windows. The candidate dates do not overlap the tested 180D windows, so the representative rows remain usable.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| SNOWPEAK_APPAREL_RETAIL_SELL_THROUGH_MARGIN_BRIDGE | C19_BRAND_RETAIL_INVENTORY_MARGIN | Positive brand-retail case where sell-through and margin bridge converted. |
| XEXYMIX_DTC_CHANNEL_REORDER_AND_OVERHEAT | C19_BRAND_RETAIL_INVENTORY_MARGIN | Positive DTC/channel reorder case with later 4B overlay. |
| NATIONAL_GEOGRAPHIC_INVENTORY_MARGIN_GUARD | C19_BRAND_RETAIL_INVENTORY_MARGIN | Counterexample: brand equity without inventory/margin absorption. |
| GLOBAL_BRAND_TURNAROUND_INVENTORY_ABSORPTION_GUARD | C19_BRAND_RETAIL_INVENTORY_MARGIN | Counterexample: turnaround language without strong rerating path. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|
| R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS | 036620 | 감성코퍼레이션 | positive / structural_success | R13L45_036620_STAGE2_2024-02-22 | current_profile_too_late |
| R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B | 337930 | 브랜드엑스코퍼레이션/젝시믹스 | positive / structural_success | R13L45_337930_STAGE2_2024-05-29 | current_profile_4B_too_late |
| R13L45_C19_298540_NATURE_INVENTORY_FALSE_POSITIVE | 298540 | 더네이쳐홀딩스 | counterexample / failed_rerating | R13L45_298540_STAGE2_FALSE_2024-04-01 | current_profile_false_positive |
| R13L45_C19_081660_FILA_TURNAROUND_FALSE_POSITIVE_4B | 081660 | 휠라홀딩스/미스토홀딩스 | counterexample / failed_rerating | R13L45_081660_STAGE2_FALSE_2024-02-13 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

The result is balanced: two cases show that brand-retail sell-through/margin evidence can work, while two cases show that brand heat alone is a false-positive trap.

## 9. Evidence Source Map

| symbol | trigger family | evidence at trigger date | evidence limitation |
|---:|---|---|---|
| 036620 | sell-through + margin bridge | Public filing/market evidence plus strong stock-web confirmation from 2024-02-22. | Exact filing text should be reattached in implementation batch if needed. |
| 337930 | DTC/channel reorder + later 4B | Public filing/IR/news checkpoint plus stock-web breakout from 2024-05-29. | The 4B row is overlay-only. |
| 298540 | inventory/margin absence guard | Brand narrative existed but price path rejected it. | Counterexample is price-confirmed; filing details should be retained as qualitative source. |
| 081660 | turnaround/inventory absorption guard | Turnaround language existed but full-price sell-through/margin bridge was not strong. | Later local high is watch-only, not full 4B without non-price evidence. |

## 10. Price Data Source Map

| symbol | profile_path | key shard paths | profile caveat |
|---:|---|---|---|
| 036620 | atlas/symbol_profiles/036/036620.json | atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv, atlas/ohlcv_tradable_by_symbol_year/036/036620/2025.csv | corporate-action candidates are historical, outside 2024 test windows |
| 337930 | atlas/symbol_profiles/337/337930.json | atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv, atlas/ohlcv_tradable_by_symbol_year/337/337930/2025.csv | corporate-action candidate in 2021, outside test windows |
| 298540 | atlas/symbol_profiles/298/298540.json | atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv, atlas/ohlcv_tradable_by_symbol_year/298/298540/2025.csv | corporate-action candidates in 2021, outside test windows |
| 081660 | atlas/symbol_profiles/081/081660.json | atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv, atlas/ohlcv_tradable_by_symbol_year/081/081660/2025.csv | corporate-action candidate in 2018, outside test windows |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | outcome | current_profile_verdict | aggregate? |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|
| R13L45_036620_STAGE2_2024-02-22 | 036620 | Stage2-Actionable | 2024-02-22 | 3025 | 55.04 | -7.93 | 55.04 | -7.93 | structural_success | current_profile_too_late | True |
| R13L45_036620_STAGE3_GREEN_2024-05-21 | 036620 | Stage3-Green | 2024-05-21 | 4185 | 12.07 | -30.23 | 12.07 | -33.45 | late_green_high_MAE | current_profile_too_late | False |
| R13L45_337930_STAGE2_2024-05-29 | 337930 | Stage2-Actionable | 2024-05-29 | 5750 | 132.7 | -8.7 | 132.7 | -12.17 | structural_success_with_later_4B | current_profile_4B_too_late | True |
| R13L45_337930_STAGE3_GREEN_2024-08-09 | 337930 | Stage3-Green | 2024-08-09 | 11430 | 17.06 | -43.13 | 17.06 | -55.82 | late_green_4B_watch | current_profile_4B_too_late | False |
| R13L45_337930_4B_2024-10-02 | 337930 | Stage4B | 2024-10-02 | 12540 | 6.7 | -59.73 | 6.7 | -59.73 | 4B_overlay_success | current_profile_4B_too_late | False |
| R13L45_298540_STAGE2_FALSE_2024-04-01 | 298540 | Stage2-Actionable | 2024-04-01 | 15780 | 2.03 | -27.38 | 2.03 | -36.63 | failed_rerating | current_profile_false_positive | True |
| R13L45_298540_STAGE3_YELLOW_FALSE_2024-05-31 | 298540 | Stage3-Yellow | 2024-05-31 | 15590 | 3.27 | -35.86 | 3.27 | -35.86 | false_positive_yellow | current_profile_false_positive | False |
| R13L45_081660_STAGE2_FALSE_2024-02-13 | 081660 | Stage2-Actionable | 2024-02-13 | 41900 | 0.0 | -12.77 | 6.32 | -13.13 | failed_rerating | current_profile_false_positive | True |
| R13L45_081660_4B_2024-08-01 | 081660 | Stage4B | 2024-08-01 | 44450 | 0.22 | -18.11 | 0.22 | -18.11 | 4B_overlay_watch_success | current_profile_false_positive | False |

## 12. Trigger-Level OHLC Backtest Tables

### Representative rows

| symbol | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | verdict |
|---:|---|---:|---:|---:|---:|---|---|
| 036620 | 2024-02-22 | 3025 | 26.45 / -7.93 | 55.04 / -7.93 | 55.04 / -7.93 | 2024-05-24 @ 4690 | structural_success |
| 337930 | 2024-05-29 | 5750 | 58.96 / -8.7 | 132.7 / -8.7 | 132.7 / -12.17 | 2024-10-07 @ 13380 | structural_success_with_later_4B |
| 298540 | 2024-04-01 | 15780 | 0.25 / -17.93 | 2.03 / -27.38 | 2.03 / -36.63 | 2024-06-03 @ 16100 | failed_rerating |
| 081660 | 2024-02-13 | 41900 | 0.0 / -9.19 | 0.0 / -12.77 | 6.32 / -13.13 | 2024-08-01 @ 44550 | failed_rerating |

Representative average:

```text
avg_MFE_90D_pct = 47.44
avg_MAE_90D_pct = -14.2
avg_MFE_180D_pct = 49.02
avg_MAE_180D_pct = -17.46
```

## 13. Current Calibrated Profile Stress Test

1. Current profile would be too late on 036620 if it waited for full Green; the Stage2 trigger had better asymmetry.
2. Current profile would catch 337930 as positive but risks over-extending it if the October blowoff is treated as confirmation instead of 4B watch.
3. Current profile can false-promote 298540 if brand narrative is not guarded by inventory/margin absorption.
4. Current profile can false-promote 081660 if turnaround/inventory clearance language is accepted without full-price sell-through and margin bridge.

```text
current_profile_error_count = 4
existing_axis_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = null
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | later confirmation | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 036620 | 3025 | 4185 | 0.71 | Green captured upside late and carried high MAE. |
| 337930 | 5750 | 11430 | 0.74 | Green/late confirmation was already near overheat watch zone. |
| 298540 | 15780 | no valid Green | n/a | Absence of margin bridge means no positive promotion. |
| 081660 | 41900 | no valid Green | n/a | Turnaround evidence was not enough for rerating. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 reference | 4B entry | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---|
| R13L45_337930_4B_2024-10-02 | 5750 | 12540 | 0.89 | 0.89 | good_full_window_4B_timing |
| R13L45_081660_4B_2024-08-01 | 41900 | 44450 | 0.99 | 0.99 | price-only local 4B watch; not full 4B without non-price evidence |

## 16. 4C Protection Audit

No hard 4C row is proposed in this loop. Both 4B rows are overlay/watch rows. The 4C gap remains open for a future C19 or C20 loop where explicit inventory write-down, channel exit, brand-license loss, or forced liquidation evidence is available.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_price_only_channel_spike_4B_watch
proposal = In L5 brand/retail names, a vertical channel-narrative price spike without fresh non-price evidence should become 4B watch, not Stage3 promotion.
confidence = low_to_medium
production_scoring_changed = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
new_axis_proposed = C19_sell_through_margin_bridge_bonus | C19_inventory_margin_absence_guard
```

Mechanism:

```text
positive promotion = sell-through evidence + margin bridge + repeat/channel conversion
negative guard = brand narrative without inventory absorption, full-price channel evidence, or revision closure
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE_90D | avg_MAE_90D | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 4 | 47.44 | -14.2 | 2/4 | mixed; positive/negative split requires C19-specific guard |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback | 4 | 47.44 | -14.2 | 2/4 or worse | weaker; no inventory absorption guard |
| P1_L5_sector_specific_candidate_profile | sector_specific | L5_price_only_channel_spike_4B_watch | 4 | 47.44 | -14.2 | reduced from 2/4 to 1/4 watch-only | better overlay alignment |
| P2_C19_canonical_archetype_candidate_profile | canonical_archetype_specific | C19_sell_through_margin_bridge_bonus; C19_inventory_margin_absence_guard | 4 | 47.44 | -14.2 | 0/4 promoted; 2/4 downgraded to watch | best explanatory fit |
| P3_counterexample_guard_profile | guard | C19_inventory_margin_absence_guard_strict | 4 | 47.44 | -14.2 | 0/4 | safe but may be too conservative |

## 20. Score-Return Alignment Matrix

| trigger_id | before score/label | after score/label | MFE_90D | MAE_90D | changed components |
|---|---|---|---:|---:|---|
| R13L45_036620_STAGE2_2024-02-22 | 73.0 / Stage2-Actionable | 78.0 / Stage3-Yellow | 55.04 | -7.93 | C19_sell_through_margin_bridge_bonus |
| R13L45_337930_STAGE2_2024-05-29 | 76.0 / Stage3-Yellow | 82.0 / Stage3-Yellow | 132.7 | -8.7 | C19_DTC_reorder_bonus |
| R13L45_337930_4B_2024-10-02 | 83.0 / Stage3-Green_or_4B_watch | 0.0 / Stage4B-overlay | 6.7 | -59.73 | C19_price_only_channel_spike_4B_watch |
| R13L45_298540_STAGE2_FALSE_2024-04-01 | 71.0 / Stage2-Actionable | 60.0 / Stage2-watch_or_reject | 2.03 | -27.38 | C19_inventory_margin_absence_guard |
| R13L45_081660_STAGE2_FALSE_2024-02-13 | 72.0 / Stage2-Actionable | 62.0 / Stage2-watch_or_reject | 0.0 | -12.77 | C19_turnaround_inventory_absorption_guard |
| R13L45_081660_4B_2024-08-01 | 69.0 / Stage2-watch | 0.0 / Stage4B-watch | 0.22 | -18.11 | C19_price_only_local_peak_watch |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | SNOWPEAK_APPAREL / XEXYMIX_DTC / NATIONAL_GEOGRAPHIC / GLOBAL_BRAND_TURNAROUND | 2 | 2 | 2 | 0 | 4 | 0 | 9 | 4 | 4 | true | true | C19 now has positive, false-positive, and 4B overlay coverage; 4C remains a future gap. |


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
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_too_late | current_profile_false_positive | current_profile_4B_too_late
new_axis_proposed: C19_sell_through_margin_bridge_bonus | C19_inventory_margin_absence_guard | L5_price_only_channel_spike_4B_watch
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus | stage3_yellow_total_min | stage3_green_total_min | stage3_green_revision_min | stage3_cross_evidence_green_buffer | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg ≈ +17; all four are same-archetype new symbols, with two positive paths, two counterexamples, and two 4B overlay paths
auto_selected_coverage_gap: C19 lacked balanced positive/counterexample/4B coverage in L5
do_not_propose_new_weight_delta: false
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema basis.
- Symbol profile availability.
- 2024 tradable OHLC rows for all trigger windows.
- 30D / 90D / 180D MFE and MAE from stock-web raw/unadjusted tradable rows.
- Corporate-action dates not overlapping tested 180D windows.
- Duplicate avoidance by symbol search in allowed research artifacts.
```

Not validated:

```text
- No production code inspected.
- No live candidate scan.
- No current recommendation.
- No broker API.
- No production scoring change.
- Filing/news evidence text should be reattached by implementation agent if the ledger needs formal source URLs.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_sell_through_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,C19 winners required sell-through + margin bridge evidence before full Green confirmation.,Positive reps had high 90D MFE; early entries avoided Green lateness.,R13L45_036620_STAGE2_2024-02-22|R13L45_337930_STAGE2_2024-05-29,2,2,0,medium,canonical_archetype_shadow_only,not production; post-calibrated residual
shadow_weight,C19_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1_guard,Brand narrative without inventory/margin absorption produced false positives.,Counterexamples had low MFE and large MAE: 298540 and 081660.,R13L45_298540_STAGE2_FALSE_2024-04-01|R13L45_081660_STAGE2_FALSE_2024-02-13,2,2,2,medium,canonical_archetype_shadow_only,blocks promotion; does not alter production global thresholds
shadow_weight,L5_price_only_channel_spike_4B_watch,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1_watch,"Price-only or valuation-driven local peaks in L5 brand retail should become 4B watch, not positive-stage evidence.",337930 4B proximity 0.89 and 081660 4B proximity 0.99 both preceded material drawdowns.,R13L45_337930_4B_2024-10-02|R13L45_081660_4B_2024-08-01,2,2,1,low_to_medium,sector_shadow_only,full 4B still requires non-price evidence; price-only remains watch
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS","symbol":"036620","company_name":"감성코퍼레이션","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"SNOWPEAK_APPAREL_RETAIL_SELL_THROUGH_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L45_036620_STAGE2_2024-02-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early sell-through/margin evidence aligned with 55.04% 90D MFE; later Green carried much worse MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Early 2024 apparel-brand sell-through and margin bridge acted like a valid Stage2-Actionable trigger; waiting for full Green left the entry close to the local top."}
{"row_type":"case","case_id":"R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B","symbol":"337930","company_name":"브랜드엑스코퍼레이션/젝시믹스","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"XEXYMIX_DTC_CHANNEL_REORDER_AND_OVERHEAT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L45_337930_STAGE2_2024-05-29","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"channel reorder + relative strength aligned with 132.70% 90D MFE; 4B watch was needed after price/valuation blowoff","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"This is a positive C19 case with a separate 4B overlay. The model should not treat the October price blowoff as more Stage3 evidence."}
{"row_type":"case","case_id":"R13L45_C19_298540_NATURE_INVENTORY_FALSE_POSITIVE","symbol":"298540","company_name":"더네이쳐홀딩스","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"NATIONAL_GEOGRAPHIC_INVENTORY_MARGIN_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L45_298540_STAGE2_FALSE_2024-04-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"brand narrative failed without inventory/margin absorption; 180D MFE only 2.03% against -36.63% MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"This is the counterexample that defines the guard: brand equity is not enough unless inventory days, full-price channel, or margin bridge actually closes."}
{"row_type":"case","case_id":"R13L45_C19_081660_FILA_TURNAROUND_FALSE_POSITIVE_4B","symbol":"081660","company_name":"휠라홀딩스/미스토홀딩스","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_TURNAROUND_INVENTORY_ABSORPTION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L45_081660_STAGE2_FALSE_2024-02-13","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"turnaround narrative did not become an EPS rerating; 180D MFE 6.32% vs -13.13% MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The late-summer local high should be a watch/4B overlay, not a delayed confirmation of the original turnaround thesis."}
```

### 25.3 trigger rows

```jsonl
{"trigger_id":"R13L45_036620_STAGE2_2024-02-22","case_id":"R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS","symbol":"036620","company_name":"감성코퍼레이션","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":3025,"evidence_available_at_that_date":"Snow Peak apparel sell-through/margin bridge narrative and early revision visibility; confirmed by public filings and stock-web price response.","evidence_source":"DART annual/quarterly filing checkpoint + stock-web 2024 shard rows around 2024-02-22","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv","profile_path":"atlas/symbol_profiles/036/036620.json","MFE_30D_pct":26.45,"MFE_90D_pct":55.04,"MFE_180D_pct":55.04,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.93,"MAE_90D_pct":-7.93,"MAE_180D_pct":-7.93,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-24","peak_price":4690,"drawdown_after_peak_pct":-40.62,"green_lateness_ratio":"0.71_vs_Stage3Green_2024-05-21","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_036620_2024-02-22_3025","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"SNOWPEAK_APPAREL_RETAIL_SELL_THROUGH_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_036620_STAGE3_GREEN_2024-05-21","case_id":"R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS","symbol":"036620","company_name":"감성코퍼레이션","trigger_type":"Stage3-Green","trigger_date":"2024-05-21","entry_date":"2024-05-21","entry_price":4185,"evidence_available_at_that_date":"Later confirmation after most of the upside had already been captured by Stage2.","evidence_source":"DART/market confirmation + stock-web 2024 shard rows around 2024-05-21","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv","profile_path":"atlas/symbol_profiles/036/036620.json","MFE_30D_pct":12.07,"MFE_90D_pct":12.07,"MFE_180D_pct":12.07,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.08,"MAE_90D_pct":-30.23,"MAE_180D_pct":-33.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-24","peak_price":4690,"drawdown_after_peak_pct":-40.62,"green_lateness_ratio":0.71,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"late_green_near_local_peak","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_high_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_036620_2024-05-21_4185","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"SNOWPEAK_APPAREL_RETAIL_SELL_THROUGH_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_337930_STAGE2_2024-05-29","case_id":"R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B","symbol":"337930","company_name":"브랜드엑스코퍼레이션/젝시믹스","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-29","entry_date":"2024-05-29","entry_price":5750,"evidence_available_at_that_date":"DTC/channel reorder and margin visibility before the summer-to-autumn price extension.","evidence_source":"DART Q1/IR/news checkpoint + stock-web 2024 shard rows around 2024-05-29","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv","profile_path":"atlas/symbol_profiles/337/337930.json","MFE_30D_pct":58.96,"MFE_90D_pct":132.7,"MFE_180D_pct":132.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.7,"MAE_90D_pct":-8.7,"MAE_180D_pct":-12.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":13380,"drawdown_after_peak_pct":-62.26,"green_lateness_ratio":"0.74_vs_Stage3Green_2024-08-09","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_later_4B","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_337930_2024-05-29_5750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"XEXYMIX_DTC_CHANNEL_REORDER_AND_OVERHEAT","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_337930_STAGE3_GREEN_2024-08-09","case_id":"R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B","symbol":"337930","company_name":"브랜드엑스코퍼레이션/젝시믹스","trigger_type":"Stage3-Green","trigger_date":"2024-08-09","entry_date":"2024-08-09","entry_price":11430,"evidence_available_at_that_date":"Later confirmation after July/August vertical price move.","evidence_source":"DART/market confirmation + stock-web 2024 shard rows around 2024-08-09","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv","profile_path":"atlas/symbol_profiles/337/337930.json","MFE_30D_pct":7.44,"MFE_90D_pct":17.06,"MFE_180D_pct":17.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.37,"MAE_90D_pct":-43.13,"MAE_180D_pct":-55.82,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":13380,"drawdown_after_peak_pct":-62.26,"green_lateness_ratio":0.74,"four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"green_already_in_4B_watch_zone","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_4B_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_337930_2024-08-09_11430","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"XEXYMIX_DTC_CHANNEL_REORDER_AND_OVERHEAT","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_337930_4B_2024-10-02","case_id":"R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B","symbol":"337930","company_name":"브랜드엑스코퍼레이션/젝시믹스","trigger_type":"Stage4B","trigger_date":"2024-10-02","entry_date":"2024-10-02","entry_price":12540,"evidence_available_at_that_date":"Price/valuation overheat after the channel-reorder run; not a new positive Stage3 trigger.","evidence_source":"stock-web price/volume path + public valuation/revision watch evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv","profile_path":"atlas/symbol_profiles/337/337930.json","MFE_30D_pct":6.7,"MFE_90D_pct":6.7,"MFE_180D_pct":6.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-33.81,"MAE_90D_pct":-59.73,"MAE_180D_pct":-59.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":13380,"drawdown_after_peak_pct":-62.26,"green_lateness_ratio":"not_applicable_4B","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_337930_2024-10-02_12540","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"XEXYMIX_DTC_CHANNEL_REORDER_AND_OVERHEAT","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_298540_STAGE2_FALSE_2024-04-01","case_id":"R13L45_C19_298540_NATURE_INVENTORY_FALSE_POSITIVE","symbol":"298540","company_name":"더네이쳐홀딩스","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":15780,"evidence_available_at_that_date":"Brand/channel narrative existed, but inventory/margin absorption was not sufficiently supported.","evidence_source":"DART/IR checkpoint + stock-web 2024 shard rows around 2024-04-01","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv","profile_path":"atlas/symbol_profiles/298/298540.json","MFE_30D_pct":0.25,"MFE_90D_pct":2.03,"MFE_180D_pct":2.03,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.93,"MAE_90D_pct":-27.38,"MAE_180D_pct":-36.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-03","peak_price":16100,"drawdown_after_peak_pct":-37.89,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"counterexample_inventory_guard_needed","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_298540_2024-04-01_15780","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"NATIONAL_GEOGRAPHIC_INVENTORY_MARGIN_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_298540_STAGE3_YELLOW_FALSE_2024-05-31","case_id":"R13L45_C19_298540_NATURE_INVENTORY_FALSE_POSITIVE","symbol":"298540","company_name":"더네이쳐홀딩스","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":15590,"evidence_available_at_that_date":"Local bounce without durable inventory/margin confirmation.","evidence_source":"stock-web 2024 shard rows around 2024-05-31 + public filing checkpoint","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv","profile_path":"atlas/symbol_profiles/298/298540.json","MFE_30D_pct":3.27,"MFE_90D_pct":3.27,"MFE_180D_pct":3.27,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.49,"MAE_90D_pct":-35.86,"MAE_180D_pct":-35.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-03","peak_price":16100,"drawdown_after_peak_pct":-37.89,"green_lateness_ratio":"not_applicable_false_yellow","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_but_negative_thesis","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_yellow","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_298540_2024-05-31_15590","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"NATIONAL_GEOGRAPHIC_INVENTORY_MARGIN_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_081660_STAGE2_FALSE_2024-02-13","case_id":"R13L45_C19_081660_FILA_TURNAROUND_FALSE_POSITIVE_4B","symbol":"081660","company_name":"휠라홀딩스/미스토홀딩스","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":41900,"evidence_available_at_that_date":"Global brand turnaround / inventory clearance narrative existed, but full-price sell-through and margin bridge were not strong enough.","evidence_source":"DART/IR checkpoint + stock-web 2024 shard rows around 2024-02-13","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv","profile_path":"atlas/symbol_profiles/081/081660.json","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":6.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.19,"MAE_90D_pct":-12.77,"MAE_180D_pct":-13.13,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":44550,"drawdown_after_peak_pct":-18.29,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"turnaround_false_positive_guard_needed","four_b_evidence_type":["explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_081660_2024-02-13_41900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_TURNAROUND_INVENTORY_ABSORPTION_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R13L45_081660_4B_2024-08-01","case_id":"R13L45_C19_081660_FILA_TURNAROUND_FALSE_POSITIVE_4B","symbol":"081660","company_name":"휠라홀딩스/미스토홀딩스","trigger_type":"Stage4B","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":44450,"evidence_available_at_that_date":"Local overheat after a weak original thesis; should be overlay/watch, not positive Stage3.","evidence_source":"stock-web 2024 shard rows around 2024-08-01","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv","profile_path":"atlas/symbol_profiles/081/081660.json","MFE_30D_pct":0.22,"MFE_90D_pct":0.22,"MFE_180D_pct":0.22,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.76,"MAE_90D_pct":-18.11,"MAE_180D_pct":-18.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":44550,"drawdown_after_peak_pct":-18.29,"green_lateness_ratio":"not_applicable_4B","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_but_good_watch","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_watch_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L45_081660_2024-08-01_44450","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_TURNAROUND_INVENTORY_ABSORPTION_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"brand retail inventory margin / channel sell-through / margin absorption","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow","case_id":"R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS","trigger_id":"R13L45_036620_STAGE2_2024-02-22","symbol":"036620","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":70,"revision_score":48,"relative_strength_score":80,"customer_quality_score":78,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":55,"execution_risk_score":35,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":78,"revision_score":53,"relative_strength_score":80,"customer_quality_score":82,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":58,"execution_risk_score":35,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":78.0,"stage_label_after":"Stage3-Yellow","changed_components":["C19_sell_through_margin_bridge_bonus"],"component_delta_explanation":"C19 profile gives credit to visible sell-through + margin bridge before full revision confirmation.","MFE_90D_pct":55.04,"MAE_90D_pct":-7.93,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow","case_id":"R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B","trigger_id":"R13L45_337930_STAGE2_2024-05-29","symbol":"337930","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":68,"revision_score":50,"relative_strength_score":85,"customer_quality_score":76,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":58,"execution_risk_score":40,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":76,"revision_score":53,"relative_strength_score":88,"customer_quality_score":82,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":60,"execution_risk_score":40,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow","changed_components":["C19_DTC_reorder_bonus"],"component_delta_explanation":"DTC/reorder evidence increases conviction, but not enough to override later 4B overheat guard.","MFE_90D_pct":132.7,"MAE_90D_pct":-8.7,"score_return_alignment_label":"structural_success_with_later_4B","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow","case_id":"R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B","trigger_id":"R13L45_337930_4B_2024-10-02","symbol":"337930","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":95,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":88,"execution_risk_score":65,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":83.0,"stage_label_before":"Stage3-Green_or_4B_watch","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":95,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":92,"execution_risk_score":75,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":0.0,"stage_label_after":"Stage4B-overlay","changed_components":["C19_price_only_channel_spike_4B_watch"],"component_delta_explanation":"After the full-window proximity reached 0.89, score promotion should stop; this row becomes risk overlay.","MFE_90D_pct":6.7,"MAE_90D_pct":-59.73,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow","case_id":"R13L45_C19_298540_NATURE_INVENTORY_FALSE_POSITIVE","trigger_id":"R13L45_298540_STAGE2_FALSE_2024-04-01","symbol":"298540","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":35,"revision_score":25,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":"unknown_or_not_supported","execution_risk_score":68,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":71.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":25,"revision_score":20,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":"unknown_or_not_supported","execution_risk_score":78,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":60.0,"stage_label_after":"Stage2-watch_or_reject","changed_components":["C19_inventory_margin_absence_guard"],"component_delta_explanation":"Brand narrative is penalized when inventory/margin absorption is absent; the 180D path supports guard.","MFE_90D_pct":2.03,"MAE_90D_pct":-27.38,"score_return_alignment_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow","case_id":"R13L45_C19_081660_FILA_TURNAROUND_FALSE_POSITIVE_4B","trigger_id":"R13L45_081660_STAGE2_FALSE_2024-02-13","symbol":"081660","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":42,"revision_score":30,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":45,"execution_risk_score":55,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":30,"revision_score":25,"relative_strength_score":43,"customer_quality_score":55,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":40,"execution_risk_score":70,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":62.0,"stage_label_after":"Stage2-watch_or_reject","changed_components":["C19_turnaround_inventory_absorption_guard"],"component_delta_explanation":"Turnaround narratives need inventory clearance plus full-price channel evidence; otherwise promotion is blocked.","MFE_90D_pct":0.0,"MAE_90D_pct":-12.77,"score_return_alignment_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow","case_id":"R13L45_C19_081660_FILA_TURNAROUND_FALSE_POSITIVE_4B","trigger_id":"R13L45_081660_4B_2024-08-01","symbol":"081660","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":72,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":70,"execution_risk_score":58,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":69.0,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":72,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":82,"execution_risk_score":70,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":0.0,"stage_label_after":"Stage4B-watch","changed_components":["C19_price_only_local_peak_watch"],"component_delta_explanation":"Local high should be overlay/watch; lack of non-price 4B evidence prevents full 4B, but also blocks positive promotion.","MFE_90D_pct":0.22,"MAE_90D_pct":-18.11,"score_return_alignment_label":"4B_overlay_watch_success","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_sell_through_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,C19 winners required sell-through + margin bridge evidence before full Green confirmation.,Positive reps had high 90D MFE; early entries avoided Green lateness.,R13L45_036620_STAGE2_2024-02-22|R13L45_337930_STAGE2_2024-05-29,2,2,0,medium,canonical_archetype_shadow_only,not production; post-calibrated residual
shadow_weight,C19_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1_guard,Brand narrative without inventory/margin absorption produced false positives.,Counterexamples had low MFE and large MAE: 298540 and 081660.,R13L45_298540_STAGE2_FALSE_2024-04-01|R13L45_081660_STAGE2_FALSE_2024-02-13,2,2,2,medium,canonical_archetype_shadow_only,blocks promotion; does not alter production global thresholds
shadow_weight,L5_price_only_channel_spike_4B_watch,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1_watch,"Price-only or valuation-driven local peaks in L5 brand retail should become 4B watch, not positive-stage evidence.",337930 4B proximity 0.89 and 081660 4B proximity 0.99 both preceded material drawdowns.,R13L45_337930_4B_2024-10-02|R13L45_081660_4B_2024-08-01,2,2,1,low_to_medium,sector_shadow_only,full 4B still requires non-price evidence; price-only remains watch
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"45","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C19 had limited post-calibrated positive/counterexample/4B coverage in L5 compared with C18/C20"}
```

### 25.7 narrative_only rows

```jsonl
```

No narrative-only rows were used for quantitative calibration in this loop.

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
next_round = R13_loop_46
recommended_scope = L5_CONSUMER_BRAND_DISTRIBUTION / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
reason = C18 and C19 now have coverage; C20 still needs balanced beauty/food export distribution positive + counterexample + 4B/4C coverage.
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_web_profiles = 036620 / 337930 / 298540 / 081660
stock_web_price_shards = 2024 tradable shards for all trigger rows
research_artifact_duplicate_check = stock_agent file search for 036620 337930 298540 081660 returned no prior rows
```

This MD intentionally leaves production scoring unchanged. All proposals are shadow-only and scoped to L5/C19 unless promoted later by an explicit batch implementation step.
