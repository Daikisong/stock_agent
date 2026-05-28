# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R5
loop = 13
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN
loop_objective = counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
```

This file is historical calibration research only. It is not a live candidate scan, investment recommendation, auto-trading instruction, or production patch.

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

This loop does not repeat the global calibration claim. It stress-tests the current profile inside the consumer export channel archetype, where the same “global channel” phrase can mean very different things: a true reorder flywheel, a seasonal channel spike, or a narrative-only false Green.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
sector = 소비재·유통·브랜드
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN
```

Canonical compression:

```text
Samyang Foods / Buldak export reorder -> C18_CONSUMER_EXPORT_CHANNEL_REORDER
Binggrae / Melona-seasonal export channel -> C18_CONSUMER_EXPORT_CHANNEL_REORDER
Nongshim / global ramen narrative with China drag -> C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts showed that the calibration ingest already covers R1~R13 and loops 1~9, with 1,376 aggregate representative trigger rows, so this loop is treated as post-calibrated residual expansion rather than baseline discovery. The applied global axes are already in place and are not re-proposed globally.

```text
auto_selected_coverage_gap = L5/C18 consumer export channel reorder residual after C20 ODM/brand loops
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_symbol_count = 3
new_trigger_family_count = 3
new_independent_case_ratio = 1.00
```

No `src/e2r` code was read. Only research artifacts and stock-web price atlas files were used.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest fields used:

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
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The price basis is raw/unadjusted marcap OHLC. Corporate-action candidates were checked through symbol profiles; no candidate dates overlap the 2024~2025 windows used here.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward available | entry row exists | clean 180D window | calibration_usable |
|---|---|---|---|---|---|---|
| R5L13_C18_SAMYANG_003230_BULDAK_EXPORT_REORDER | 003230 | 2024-05-17 | True | True | clean_180D_window | True |
| R5L13_C18_BINGGRAE_005180_ICECREAM_EXPORT_SEASONAL_HIGH_MAE | 005180 | 2024-05-17 | True | True | clean_180D_window | True |
| R5L13_C18_NONGSHIM_004370_RAMEN_GLOBAL_NARRATIVE_FAILED_RERATING | 004370 | 2024-05-29 | True | True | clean_180D_window | True |

All three representative cases are calibration-usable for 30D/90D/180D. 2Y fields are `null` because several 2024 entries require dates beyond the stock-web manifest max date of 2026-02-20.

## 6. Canonical Archetype Compression Map

| fine route | canonical_archetype_id | scoring implication |
|---|---|---|
| Buldak export reorder + capacity + realized earnings | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Promote only after export reorder closes through margin/revision evidence. |
| Ice cream/Melona seasonal export spike | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Keep Stage2/Watch unless repeat-order and margin bridge are durable. |
| Global ramen narrative with China drag | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Cap Green when channel drag is disclosed and margin revision is absent. |

## 7. Case Selection Summary

| case_id | symbol | company | role | pos/counter | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R5L13_C18_SAMYANG_003230_BULDAK_EXPORT_REORDER | 003230 | 삼양식품 | structural_success | positive | 2024-05-17 | 446500 | 60.81 | 0.0 | 106.05 | 0.0 | current_profile_correct |
| R5L13_C18_BINGGRAE_005180_ICECREAM_EXPORT_SEASONAL_HIGH_MAE | 005180 | 빙그레 | high_mae_success | positive_but_high_mae | 2024-05-17 | 88300 | 34.09 | -32.96 | 34.09 | -32.96 | current_profile_too_early |
| R5L13_C18_NONGSHIM_004370_RAMEN_GLOBAL_NARRATIVE_FAILED_RERATING | 004370 | 농심 | failed_rerating | counterexample | 2024-05-29 | 478000 | 25.31 | -24.58 | 25.31 | -33.68 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

Samyang is a clean structural success. Binggrae is counted as positive but high-MAE, because the setup generated a large short-window MFE but failed durability. Nongshim is the counterexample: overseas narrative existed, but it did not close into durable revision.

## 9. Evidence Source Map

| symbol | trigger family | evidence used at trigger date | source handling |
|---|---|---|---|
| 003230 | actual earnings + export reorder | Q1 public earnings; later analyst revision shows export ASP/shipment/capacity route | DART / MarketWatch / stock-web OHLC |
| 005180 | seasonal export channel + Q1 earnings | Q1 public earnings and global ice cream distribution route | DART / public brand-distribution sources / stock-web OHLC |
| 004370 | global ramen channel narrative without margin revision | overseas expansion narrative plus China slowdown / execution drag | Financial Times / stock-web OHLC |

Evidence is separated from price action. Price-only moves are not used as Stage2/Stage3 evidence.

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | source row examples |
|---|---|---|---|
| 003230 | atlas/symbol_profiles/003/003230.json | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv, 2025.csv | 2024-05-17 close 446,500; 2024-06-19 high 718,000; 2025-05-16 high 1,233,000 |
| 005180 | atlas/symbol_profiles/005/005180.json | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv, 2025.csv | 2024-05-17 close 88,300; 2024-06-11 high 118,400; 2024-09-09 low 59,200 |
| 004370 | atlas/symbol_profiles/004/004370.json | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv, 2025.csv | 2024-05-29 close 478,000; 2024-06-13 high 599,000; 2024-11-15 low 317,000 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | outcome | current_profile | dedupe |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R5L13_003230_T1_STAGE2_ACTIONABLE_2024-05-16 | 003230 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 446500 | 60.81 | 0.0 | 106.05 | 0.0 | 2025-05-16 | 1233000 | structural_success | current_profile_correct | True |
| R5L13_003230_T2_STAGE3_GREEN_2024-06-17 | 003230 | Stage3-Green | 2024-06-14 | 2024-06-17 | 686000 | 4.66 | -33.6 | 34.11 | -33.6 | 2025-05-16 | 1233000 | green_valid_but_late_vs_stage2 | current_profile_too_late | False |
| R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16 | 005180 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 88300 | 34.09 | -32.96 | 34.09 | -32.96 | 2024-06-11 | 118400 | high_mae_success | current_profile_too_early | True |
| R5L13_005180_T2_STAGE3_GREEN_LOCAL_2024-06-10 | 005180 | Stage3-Green-local | 2024-06-10 | 2024-06-10 | 112100 | 5.62 | -47.19 | 5.62 | -47.19 | 2024-06-11 | 118400 | false_positive_green | current_profile_false_positive | False |
| R5L13_004370_T1_STAGE2_WATCH_2024-05-28 | 004370 | Stage2-Watch | 2024-05-28 | 2024-05-29 | 478000 | 25.31 | -24.58 | 25.31 | -33.68 | 2024-06-13 | 599000 | failed_rerating | current_profile_false_positive | True |
| R5L13_004370_T2_4C_LATE_2024-11-15 | 004370 | 4C | 2024-11-15 | 2024-11-15 | 326000 | 36.2 | -2.76 | 36.2 | -2.76 | 2025-03-20 | 444000 | 4C_late | current_profile_4C_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger metrics:

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak | drawdown_after_peak |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 003230 | 2024-05-17 | 446500 | 60.81 | 0.0 | 60.81 | 0.0 | 106.05 | 0.0 | 176.15 | 0.0 | 2025-05-16 / 1233000 | -12.65 |
| 005180 | 2024-05-17 | 88300 | 34.09 | -9.29 | 34.09 | -32.96 | 34.09 | -32.96 | 34.09 | -32.96 | 2024-06-11 / 118400 | -50.0 |
| 004370 | 2024-05-29 | 478000 | 25.31 | -8.37 | 25.31 | -24.58 | 25.31 | -33.68 | 25.31 | -33.68 | 2024-06-13 / 599000 | -47.08 |

Interpretation:

- `003230` confirms the desired C18 path: export reorder + realized margin/revision created a large MFE with very low MAE from the Stage2-Actionable row.
- `005180` shows why seasonal export excitement needs a high-MAE guard: the first MFE was large, but the later drawdown cut the signal in half.
- `004370` shows the false Green route: global channel narrative generated a local MFE, but the drawdown and late 4C show that narrative was not enough.

## 13. Current Calibrated Profile Stress Test

| case | current proxy likely label | actual path | verdict |
|---|---|---|---|
| Samyang | Stage3-Yellow/Green after revision | large MFE, low MAE | current_profile_correct |
| Binggrae | Stage3-Yellow risk from relative strength | high MFE but high MAE and -50% drawdown from local peak | current_profile_too_early |
| Nongshim | Stage3-Yellow false promotion risk | local MFE followed by -47% drawdown from peak | current_profile_false_positive |

Existing applied axes tested:

```text
stage2_actionable_evidence_bonus = kept
stage3_green_revision_min = strengthened in C18 only
full_4b_requires_non_price_evidence = strengthened in C18 only
hard_4c_thesis_break_routes_to_4c = kept, but C18 needs earlier drag guard before 4C
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/comparison entry | green_lateness_ratio | conclusion |
|---|---:|---:|---:|---|
| Samyang | 446,500 | 686,000 | 0.51 vs 180D peak | Green was valid but materially later than Stage2. |
| Binggrae | 88,300 | 112,100 | 0.79 vs local peak | Green-like upgrade would arrive near the local top and create high MAE. |
| Nongshim | 478,000 | no supported Green | not_applicable | Narrative-only global channel must not become Green. |

C18 should not weaken the global Green threshold. It should add a narrower bridge: realized export reorder + margin/revision + durable channel evidence.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B/overlay row | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 005180 | 2024-06-10 Green-local / price-only 4B watch | 0.79 | 0.79 | price_only_local_4B_watch_not_full_4B |
| 004370 | 2024-11-15 thesis break | -1.26 | -1.26 | not_4B_late_4C_thesis_break |

The key lesson is not “sell local peaks by price.” The narrower lesson is that C18 Green must be capped before the peak when same-date evidence already contains channel drag or lacks durable margin bridge.

## 16. 4C Protection Audit

| symbol | 4C row | label | comment |
|---|---|---|---|
| 004370 | 2024-11-15 | hard_4c_late | 4C recognized thesis break only after most of the peak-to-trough drawdown had already occurred. |

`hard_4c_thesis_break_routes_to_4c` remains correct, but C18 needs a prior “channel drag / no revision bridge” guard so the false Green never trains positive entry weights.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c18_seasonal_export_high_mae_guard
scope = L5_CONSUMER_BRAND_DISTRIBUTION
delta = +1 guard
reason = Seasonal export and brand channel spikes can create fast MFE but should not become durable Stage3-Green without repeat order, realized margin bridge, and revision.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c18_green_requires_realized_export_reorder_margin_bridge
scope = C18_CONSUMER_EXPORT_CHANNEL_REORDER
delta = +1 bridge
reason = The same global-channel evidence separates into three paths: reorder flywheel, seasonal high-MAE spike, and narrative-only false Green.
```

Secondary guard:

```text
axis = c18_china_or_channel_drag_guard
delta = +1 guard
effect = cap Stage3-Green when same-date evidence includes China/channel drag and margin/revision is not confirmed
```

## 19. Before / After Backtest Comparison

| profile | profile_id | scope | hypothesis | eligible | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural | late_green | avg_green_lateness | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | global current | keeps global Stage2/Green/4B/4C guards | 3 | 40.07 | -19.18 | 55.15 | -22.21 | 0.33 | 0 | 1 | 0.65 | mixed; Samyang correct, Binggrae/Nongshim too permissive |
| P0b | e2r_2_0_baseline_reference | rollback reference | lower Green revision and weaker 4B/4C guard | 3 | 40.07 | -19.18 | 55.15 | -22.21 | 0.67 | 0 | 1 | 0.65 | worse false-positive control |
| P1 | sector_specific_candidate_profile | L5 seasonal export guard | add high-MAE seasonal export guard | 3 | 40.07 | -19.18 | 55.15 | -22.21 | 0.33 | 0 | 1 | 0.65 | better Binggrae label |
| P2 | canonical_archetype_candidate_profile | C18 export reorder margin bridge | requires realized export reorder + margin/revision bridge | 3 | 40.07 | -19.18 | 55.15 | -22.21 | 0.00 | 0 | 1 | 0.65 | best score-return alignment |
| P3 | counterexample_guard_profile | C18 China/channel drag guard | cap Green when same evidence includes China/channel drag | 3 | 40.07 | -19.18 | 55.15 | -22.21 | 0.00 | 0 | 1 | 0.65 | best false-positive guard |

## 20. Score-Return Alignment Matrix

| symbol | before label | proposed label | score-return alignment |
|---|---|---|---|
| 003230 | Stage3-Yellow/Green | Stage3-Green after realized reorder+revision | improved / keeps positive |
| 005180 | Stage3-Yellow risk | Stage2-Watch / high-MAE success | improved / avoids false durable Green |
| 004370 | Stage3-Yellow false risk | Stage2-Watch or no positive promotion | improved / blocks false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN | 2 | 1 | 2 | 1 | 3 | 0 | 6 | 3 | 2 | True | True | C18 now has positive/high-MAE/counterexample mix; next gap is C18 holdout beyond K-food or C19 retail inventory. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - narrative_only_global_channel_false_positive
  - seasonal_export_high_MAE_success
  - late_4C_after_drawdown
new_axis_proposed:
  - c18_green_requires_realized_export_reorder_margin_bridge
  - c18_seasonal_export_high_mae_guard
  - c18_china_or_channel_drag_guard
existing_axis_strengthened:
  - stage3_green_revision_min in C18 only
  - full_4b_requires_non_price_evidence in C18 only
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high_total_63_avg_21.0
auto_selected_coverage_gap: L5/C18 consumer export channel reorder residual after C20 ODM/brand loops
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema read
- symbol profiles read for 003230, 005180, 004370
- 2024/2025 tradable OHLC rows read for all three symbols
- 30D/90D/180D MFE/MAE calculated from raw unadjusted tradable rows
- same_entry_group_id / representative dedupe applied
- 4B local vs full-window concepts split
- current calibrated profile stress-tested
```

Not validated:

```text
- No production score code was opened.
- No stock_agent src/e2r path was read.
- No live/current candidate scan was run.
- No broker/API/trading action was used.
- No current 2026 investment recommendation is implied.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_green_requires_realized_export_reorder_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 Green should require export reorder to close through realized margin/revision rather than narrative-only global expansion.","Improves Nongshim false positive and Binggrae high-MAE label while preserving Samyang positive.","R5L13_003230_T1_STAGE2_ACTIONABLE_2024-05-16|R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16|R5L13_004370_T1_STAGE2_WATCH_2024-05-28",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_seasonal_export_high_mae_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Seasonal export spikes can create large MFE but should not be treated as durable Green without repeat-order/margin bridge.","Lowers false Green risk in Binggrae-like cases.","R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16|R5L13_005180_T2_STAGE3_GREEN_LOCAL_2024-06-10",2,1,0,low,sector_shadow_only,"not production; high-MAE guard"
shadow_weight,c18_china_or_channel_drag_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Global channel narrative is capped when same-date evidence includes China/channel drag and no margin revision.","Caps Nongshim-type narrative positives before hard 4C is visible.","R5L13_004370_T1_STAGE2_WATCH_2024-05-28|R5L13_004370_T2_4C_LATE_2024-11-15",2,1,1,medium,canonical_shadow_only,"not production; counterexample guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L13_C18_SAMYANG_003230_BULDAK_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L13_003230_T1_STAGE2_ACTIONABLE_2024-05-16","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Buldak export reorder moved from narrative to realized earnings and revision; Stage2-Actionable remained useful before full Green confirmation."}
{"row_type":"case","case_id":"R5L13_C18_BINGGRAE_005180_ICECREAM_EXPORT_SEASONAL_HIGH_MAE","symbol":"005180","company_name":"빙그레","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","case_type":"high_mae_success","positive_or_counterexample":"positive_but_high_mae","best_trigger":"R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_high_MFE_high_MAE","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Export/seasonality narrative produced a fast MFE, but absence of durable reorder and margin bridge made the move fragile."}
{"row_type":"case","case_id":"R5L13_C18_NONGSHIM_004370_RAMEN_GLOBAL_NARRATIVE_FAILED_RERATING","symbol":"004370","company_name":"농심","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L13_004370_T1_STAGE2_WATCH_2024-05-28","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Global expansion narrative had real overseas content, but China slowdown / execution drag and missing margin-revision confirmation made it a C18 guard example."}
{"row_type":"trigger","trigger_id":"R5L13_003230_T1_STAGE2_ACTIONABLE_2024-05-16","case_id":"R5L13_C18_SAMYANG_003230_BULDAK_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":446500,"evidence_available_at_that_date":"Q1 earnings disclosure made export-led profit step-up visible; next tradable close used because public timing is treated as after/uncertain close.","evidence_source":"DART 2024Q1 filing; stock-web 2024 row; later MarketWatch analyst revision confirms export ASP/shipment/capacity route.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":60.81,"MFE_90D_pct":60.81,"MFE_180D_pct":106.05,"MFE_1Y_pct":176.15,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":0.0,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-05-16","peak_price":1233000,"drawdown_after_peak_pct":-12.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L13_003230_2024-05-17_446500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L13_003230_T2_STAGE3_GREEN_2024-06-17","case_id":"R5L13_C18_SAMYANG_003230_BULDAK_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test","trigger_type":"Stage3-Green","trigger_date":"2024-06-14","entry_date":"2024-06-17","entry_price":686000,"evidence_available_at_that_date":"Analyst revision and export ASP/shipment/capacity route became broadly visible after the initial earnings gap.","evidence_source":"MarketWatch 2024-06-14; stock-web 2024 row.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.66,"MFE_90D_pct":4.66,"MFE_180D_pct":34.11,"MFE_1Y_pct":79.74,"MFE_2Y_pct":null,"MAE_30D_pct":-8.89,"MAE_90D_pct":-33.6,"MAE_180D_pct":-33.6,"MAE_1Y_pct":-33.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-05-16","peak_price":1233000,"drawdown_after_peak_pct":-12.65,"green_lateness_ratio":0.51,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_valid_but_late_vs_stage2","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L13_003230_2024-06-17_686000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16","case_id":"R5L13_C18_BINGGRAE_005180_ICECREAM_EXPORT_SEASONAL_HIGH_MAE","symbol":"005180","company_name":"빙그레","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":88300,"evidence_available_at_that_date":"Q1/seasonal ice-cream export route and established Melona/global distribution gave a tradable Stage2 event, but not a durable Green.","evidence_source":"DART 2024Q1 filing; Melona/Binggrae public global distribution references; stock-web row.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.09,"MFE_90D_pct":34.09,"MFE_180D_pct":34.09,"MFE_1Y_pct":34.09,"MFE_2Y_pct":null,"MAE_30D_pct":-9.29,"MAE_90D_pct":-32.96,"MAE_180D_pct":-32.96,"MAE_1Y_pct":-32.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L13_005180_2024-05-17_88300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L13_005180_T2_STAGE3_GREEN_LOCAL_2024-06-10","case_id":"R5L13_C18_BINGGRAE_005180_ICECREAM_EXPORT_SEASONAL_HIGH_MAE","symbol":"005180","company_name":"빙그레","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test","trigger_type":"Stage3-Green-local","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":112100,"evidence_available_at_that_date":"Strong price/volume plus seasonal export thesis would tempt a Green upgrade, but realized durable revision was not sufficiently confirmed.","evidence_source":"stock-web row; public distribution references only.","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":5.62,"MFE_2Y_pct":null,"MAE_30D_pct":-14.63,"MAE_90D_pct":-47.19,"MAE_180D_pct":-47.19,"MAE_1Y_pct":-47.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":0.79,"four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":0.79,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L13_005180_2024-06-10_112100","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L13_004370_T1_STAGE2_WATCH_2024-05-28","case_id":"R5L13_C18_NONGSHIM_004370_RAMEN_GLOBAL_NARRATIVE_FAILED_RERATING","symbol":"004370","company_name":"농심","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test","trigger_type":"Stage2-Watch","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":478000,"evidence_available_at_that_date":"Global noodle expansion narrative was public, but the same article carried China slowdown / execution drag; next tradable close used.","evidence_source":"Financial Times 2024-05-27; stock-web row.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.31,"MFE_90D_pct":25.31,"MFE_180D_pct":25.31,"MFE_1Y_pct":25.31,"MFE_2Y_pct":null,"MAE_30D_pct":-8.37,"MAE_90D_pct":-24.58,"MAE_180D_pct":-33.68,"MAE_1Y_pct":-33.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L13_004370_2024-05-29_478000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L13_004370_T2_4C_LATE_2024-11-15","case_id":"R5L13_C18_NONGSHIM_004370_RAMEN_GLOBAL_NARRATIVE_FAILED_RERATING","symbol":"004370","company_name":"농심","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_GLOBAL_NARRATIVE_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":326000,"evidence_available_at_that_date":"Price collapse and margin/revision disappointment made thesis-break visible, but it arrived after a large part of the drawdown.","evidence_source":"stock-web row; public quarterly earnings context.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.26,"MFE_90D_pct":36.2,"MFE_180D_pct":36.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.76,"MAE_90D_pct":-2.76,"MAE_180D_pct":-2.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-20","peak_price":444000,"drawdown_after_peak_pct":-16.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":-1.26,"four_b_full_window_peak_proximity":-1.26,"four_b_timing_verdict":"not_4B_late_4C_thesis_break","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L13_004370_2024-11-15_326000","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L13_C18_SAMYANG_003230_BULDAK_EXPORT_REORDER","trigger_id":"R5L13_003230_T1_STAGE2_ACTIONABLE_2024-05-16","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":18,"revision_score":20,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow_high","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":20,"revision_score":24,"relative_strength_score":14,"customer_quality_score":14,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":-1,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":91,"stage_label_after":"Stage3-Green","changed_components":["c18_export_reorder_margin_bridge_bonus","+c18_customer_channel_quality"],"component_delta_explanation":"Samyang receives the proposed C18 Green upgrade only after export ASP/shipment/capacity evidence is paired with realized earnings revision.","MFE_90D_pct":60.81,"MAE_90D_pct":0.0,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L13_C18_BINGGRAE_005180_ICECREAM_EXPORT_SEASONAL_HIGH_MAE","trigger_id":"R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":8,"revision_score":10,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":8,"revision_score":9,"relative_strength_score":16,"customer_quality_score":7,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":7,"execution_risk_score":-9,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","changed_components":["c18_seasonal_export_high_mae_guard","-durability_without_repeat_order"],"component_delta_explanation":"Binggrae keeps Stage2/Watch because seasonal export excitement had high MFE but poor MAE and drawdown after local peak.","MFE_90D_pct":34.09,"MAE_90D_pct":-32.96,"score_return_alignment_label":"mixed_high_MFE_high_MAE","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L13_C18_NONGSHIM_004370_RAMEN_GLOBAL_NARRATIVE_FAILED_RERATING","trigger_id":"R5L13_004370_T1_STAGE2_WATCH_2024-05-28","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":6,"revision_score":8,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":8,"valuation_repricing_score":"unknown_or_not_supported","execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":4,"revision_score":5,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":8,"valuation_repricing_score":"unknown_or_not_supported","execution_risk_score":-12,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":60,"stage_label_after":"Stage2-Watch_or_No_Promotion","changed_components":["c18_china_or_channel_drag_guard","-margin_bridge_without_revision"],"component_delta_explanation":"Nongshim is downgraded because overseas narrative was accompanied by China slowdown / margin drag and no confirmed revision bridge.","MFE_90D_pct":25.31,"MAE_90D_pct":-24.58,"score_return_alignment_label":"false_positive_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["narrative_only_global_channel_false_positive","seasonal_export_high_MAE_success","late_4C_after_drawdown"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L5/C18 consumer export channel reorder residual after C20 ODM/brand loops; adds K-food positive/high-MAE/counterexample balance."}
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
next_round = R5_C18_holdout_or_C19_brand_retail_inventory_margin
suggested_next_scope = L5_CONSUMER_BRAND_DISTRIBUTION / C19_BRAND_RETAIL_INVENTORY_MARGIN
avoid_next = repeating 003230 2024-05-17 or 005180 2024-05-17 as representative triggers
carry_forward_guard = c18_green_requires_realized_export_reorder_margin_bridge
```

## 28. Source Notes

```text
stock_agent artifacts:
- reports/e2r_calibration/ingest_summary.md
- reports/e2r_calibration/applied_scoring_diff.md

stock-web files:
- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/003/003230.json
- atlas/symbol_profiles/005/005180.json
- atlas/symbol_profiles/004/004370.json
- atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv
- atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/004/004370/2025.csv
```
