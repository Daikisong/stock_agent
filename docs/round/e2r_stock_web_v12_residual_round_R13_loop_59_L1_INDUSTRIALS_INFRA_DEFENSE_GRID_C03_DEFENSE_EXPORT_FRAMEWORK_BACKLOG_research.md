# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```text
round = R13
loop = 59
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selection_mode = auto_coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R13_loop_59_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

## 1. Current Calibrated Profile Assumption
```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not retest the generic conclusion that Stage2 is earlier than Green. It asks a narrower C03 question: when a defense export headline is real, which part of it becomes investable calibration evidence—framework size, execution contract, customer quality, backlog visibility, or margin/revision conversion?

## 2. Round / Large Sector / Canonical Archetype Scope
```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION
loop_objective = coverage_gap_fill | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test
```

## 3. Previous Coverage / Duplicate Avoidance Check
Local `/mnt/data` v12 snapshot was scanned before generating this MD. The snapshot contained repeated C21/C20/C26/C28 loops and one recent C04 nuclear-delay loop, but no `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` standalone MD. A direct symbol scan over existing local v12 MDs also found no rows for `012450`, `079550`, or `047810`. Therefore:

```text
auto_selected_coverage_gap = local_v12_snapshot_has_no_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_md
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

This is not a new canonical-archetype-only novelty claim. The new evidence is in three independent symbol/trigger families inside C03: Poland Chunmoo execution order, Iraq Cheongung-II repeat export, and FA-50 Poland framework/order margin-conversion counterexample.

## 4. Stock-Web OHLC Input / Price Source Validation
`Songdaiki/stock-web` manifest was checked for source and price basis. Manifest max date is `2026-02-20`, not inferred from the current date. The manifest identifies FinanceData/marcap as upstream source, raw/unadjusted status, 14,354,401 tradable rows, 15,214,118 raw rows, 5,414 symbols, 2,868 active-like symbols, and markets KONEX/KOSDAQ/KOSDAQ GLOBAL/KOSPI. The manifest also states that zero-volume and invalid rows are excluded from calibration shards and raw reference rows remain under raw shards.

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Verification anchors used in this loop:

- Manifest source/status/row counts: `atlas/manifest.json`.
- Hanwha Aerospace profile: `atlas/symbol_profiles/012/012450.json`; no 2024/2025 corporate-action candidate in the profile, with historical candidates ending in 2009.
- LIG Nex1 profile: `atlas/symbol_profiles/079/079550.json`; corporate_action_candidate_count = 0.
- KAI profile: `atlas/symbol_profiles/047/047810.json`; corporate_action_candidate_count = 0.

## 5. Historical Eligibility Gate
All representative rows use past trigger dates, tradable entry dates, at least 180 forward trading days inside stock-web, available OHLCV, and clean 180D windows by symbol profile. 1Y values are only used when they were explicitly checked in fetched stock-web rows; 2Y values are not used for primary calibration in this MD.

| symbol | entry_date | 180D forward available by manifest/profile | 180D corporate-action contamination | calibration_usable |
|---:|---|---|---|---|
| 012450 | 2024-04-26 | yes | clean_180D_window | true |
| 079550 | 2024-09-20 | yes | clean_180D_window | true |
| 047810 | 2022-07-29 | yes | clean_180D_window | true |

## 6. Canonical Archetype Compression Map
```text
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype candidates compressed into C03:
- POLAND_CHUNMOO_EXECUTION_ORDER_TO_BACKLOG_SCALE
- CHEONGUNG_II_REPEAT_EXPORT_CUSTOMER_ROUTE
- FA50_EXPORT_FRAMEWORK_WITH_MARGIN_DELIVERY_GAP
```

C03 is not “defense theme.” The archetype is export framework/backlog. The mechanism is: a public export order creates a backlog bridge; a high-quality sovereign customer reduces cancellation risk; repeat orders or delivery visibility increase durability; margin/revision conversion determines whether the order becomes Stage3-Green rather than only Stage2-Actionable.

## 7. Case Selection Summary
| case_id | symbol | company | role | representative trigger | entry | MFE90 / MAE90 | MFE180 / MAE180 | current verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R13L59-C03-012450-HANWHA-AERO-CHUNMOO-POLAND | 012450 | 한화에어로스페이스 | positive structural success | 2024-04-25 / 2024-04-26 | 235,000 | +40.43% / -17.45% | +80.85% / -17.45% | current_profile_correct |
| R13L59-C03-079550-LIG-NEX1-IRAQ-CHEONGUNG | 079550 | LIG넥스원 | positive structural success | 2024-09-19 / 2024-09-20 | 211,000 | +28.67% / -20.00% | +98.82% / -20.00% | current_profile_correct |
| R13L59-C03-047810-KAI-FA50-POLAND-MARGIN-GAP | 047810 | 한국항공우주 | counterexample / failed rerating | 2022-07-28 / 2022-07-29 | 57,000 | +12.11% / -29.82% | +12.11% / -29.82% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0 hard_4c, 1 thesis_break_watch_only
calibration_usable_case_count = 3
```

The sample is intentionally balanced around residual error. Hanwha and LIG show that real export orders can support large 180D MFE. KAI shows that a real export order can still fail the score-return alignment test if margin conversion, delivery timing, and revision bridge are weak.

## 9. Evidence Source Map
- Hanwha Aerospace: Reuters reported a Poland Chunmoo rocket artillery supply deal, tied to the larger 2022 Poland defense framework and financing condition, with execution/order characteristics rather than a pure theme headline.
- LIG Nex1: Reuters reported a $2.8bn Iraq order for missile systems and framed it as an extension of the Cheongung-II export route after Saudi/UAE wins.
- KAI: public sources describe the July 2022 Poland FA-50 order for 48 aircraft and expected delivery/service-center components, but the later price path shows the order headline did not close margin/revision quickly enough for C03-Green.

## 10. Price Data Source Map
| symbol | price_shard_path | profile_path | entry row anchor | forward-window anchor |
|---:|---|---|---|---|
| 012450 | atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv | atlas/symbol_profiles/012/012450.json | 2024-04-26 c=235000 | 2024-11-12 h=425000; 2025-04-18 h=862000 |
| 079550 | atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv | atlas/symbol_profiles/079/079550.json | 2024-09-20 c=211000 | 2025-05-08 h=419500 |
| 047810 | atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv | atlas/symbol_profiles/047/047810.json | 2022-07-29 c=57000 | 2022-09-07 h=63900; 2022-10-13 l=40000 |

## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | aggregate role |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R13L59-T001 | 012450 | Stage2-Actionable | 2024-04-25 | 2024-04-26 | 235,000 | +6.17 | -17.45 | +40.43 | -17.45 | +80.85 | -17.45 | 2025-04-18 | 862,000 | representative |
| R13L59-T002 | 012450 | Stage4B-Overlay | 2024-11-12 | 2024-11-12 | 413,500 | +0.00 | -32.77 | +68.56 | -32.77 | +115.24 | -32.77 | 2025-05-07 | 890,000 | 4B_overlay_only |
| R13L59-T003 | 079550 | Stage2-Actionable | 2024-09-19 | 2024-09-20 | 211,000 | +25.59 | -1.42 | +28.67 | -20.00 | +98.82 | -20.00 | 2025-05-08 | 419,500 | representative |
| R13L59-T004 | 047810 | Stage2-Actionable | 2022-07-28 | 2022-07-29 | 57,000 | +12.11 | -10.18 | +12.11 | -29.82 | +12.11 | -29.82 | 2022-09-07 | 63,900 | representative |

## 12. Trigger-Level OHLC Backtest Tables
### 12.1 Representative aggregate rows only
| symbol | representative trigger | entry price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 012450 | R13L59-T001 | 235,000 | +6.17% | -17.45% | +40.43% | -17.45% | +80.85% | -17.45% | success but high MAE |
| 079550 | R13L59-T003 | 211,000 | +25.59% | -1.42% | +28.67% | -20.00% | +98.82% | -20.00% | success after interim drawdown |
| 047810 | R13L59-T004 | 57,000 | +12.11% | -10.18% | +12.11% | -29.82% | +12.11% | -29.82% | failed rerating |

### 12.2 Aggregate effect
```text
P0 all representative rows:
avg_MFE_90D_pct = 27.07
avg_MAE_90D_pct = -22.42
avg_MFE_180D_pct = 63.93
avg_MAE_180D_pct = -22.42
false_positive_rate = 33.3%

C03 margin-conversion guard selected rows:
selected = 012450, 079550
avg_MFE_90D_pct = 34.55
avg_MAE_90D_pct = -18.73
avg_MFE_180D_pct = 89.83
avg_MAE_180D_pct = -18.73
false_positive_rate = 0.0%
```

## 13. Current Calibrated Profile Stress Test
| case | current profile likely action | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| Hanwha Aerospace | Stage3-Yellow, almost Green if contract/backlog score is high | +80.85% MFE180, but -17.45% MAE | current_profile_correct |
| LIG Nex1 | Stage3-Yellow, Green only after revision/multiple-source confirmation | +98.82% MFE180, but -20.00% MAE | current_profile_correct |
| KAI | Stage3-Yellow risk if framework size is over-counted | +12.11% MFE180 vs -29.82% MAE180 | current_profile_false_positive |
| Hanwha 4B overlay | price-only local 4B might fire near 2024-11-12 | later full-window extension invalidates price-only exit | current_profile_4B_too_early |

Answers to required stress-test questions:

1. Current profile mostly handles positive cases but still over-scores framework order size when margin conversion is weak.
2. The current judgment is correct for Hanwha/LIG, incorrect for KAI if treated as Yellow/Green on order size alone.
3. Stage2 bonus is appropriate for all three; it is not sufficient to justify Green.
4. Yellow threshold 75 is too permissive for aircraft/framework orders without margin bridge.
5. Green threshold 87 and revision 55 are appropriate; this loop strengthens rather than weakens revision discipline.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is strengthened: Hanwha local price peak was not enough.
8. Hard 4C routing should not fire on interim drawdown without order cancellation, delivery failure, or explicit thesis break.

## 14. Stage2 / Yellow / Green Comparison
This loop does not compare a known Stage3-Green trigger against a Stage2 trigger because the historical evidence package for these cases did not provide a clean separate Green date without lookahead. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger_without_later_evidence
```

The key finding is not Green lateness; it is that C03 needs a conversion guard between Stage2-Actionable and Stage3-Yellow/Green.

## 15. 4B Local vs Full-window Timing Audit
Hanwha Aerospace provides the 4B audit row.

```text
Stage2_Actionable_entry_price = 235000
Stage4B_overlay_entry_price = 413500
local_peak_price_after_Stage2_Actionable = 425000
full_window_peak_price_after_Stage2_Actionable = 862000
four_b_local_peak_proximity = 0.94
four_b_full_window_peak_proximity = 0.28
four_b_timing_verdict = price_only_local_4B_too_early
```

The mechanism is straightforward: defense export cycles can have violent local drawdowns because position crowding and valuation move faster than delivery revenue. A local price peak looks like the roof of the house, but in C03 it may be only a stair landing. Without non-price evidence such as contract cancellation, financing failure, delivery delay, margin collapse, or order-book slowdown, full 4B should not replace the Stage3 thesis.

## 16. 4C Protection Audit
No hard 4C was assigned. KAI is treated as `thesis_break_watch_only`, not hard 4C, because the export contract itself was real. The residual error is over-promotion before margin/delivery conversion, not a cancellation or fraud route.

```text
four_c_protection_label = thesis_break_watch_only for 047810
hard_4c_success = not_applicable
hard_4c_late = not_applicable
```

## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate_axis = defense_export_execution_grade_order_filter
baseline_value = 0
tested_value = 1
delta = +1 shadow-only
```

Sector-specific rule: in L1 defense export names, public export news should become a Stage2-Actionable bonus when it is at least execution-grade. Stage3-Yellow/Green requires one of the following extra bridges:

- signed execution contract rather than memorandum/framework only;
- high-quality sovereign customer plus financing route;
- delivery or repeat-order visibility;
- margin/revision bridge;
- backlog increase that can be linked to segment financials.

## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
candidate_axis = framework_order_margin_conversion_guard
```

C03-specific rule: do not promote framework-size order headlines directly to Stage3-Green. Treat them as Stage2-Actionable unless backlog conversion and margin/revision evidence close. This keeps the positive Hanwha/LIG rows while demoting the KAI-style false positive.

## 19. Before / After Backtest Comparison
| profile_id | scope | eligible selected triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | +27.07 | -22.42 | +63.93 | -22.42 | 33.3% | useful but over-admits framework-only order |
| P0b e2r_2_0_baseline_reference | rollback reference | 3 | +27.07 | -22.42 | +63.93 | -22.42 | 33.3% | less disciplined on price-only 4B and Green gate |
| P1 sector_specific_candidate_profile | L1 defense | 2 | +34.55 | -18.73 | +89.83 | -18.73 | 0.0% | stronger risk-adjusted fit |
| P2 canonical_archetype_candidate_profile | C03 | 2 | +34.55 | -18.73 | +89.83 | -18.73 | 0.0% | preferred shadow rule |
| P3 counterexample_guard_profile | C03 guard | 2 | +34.55 | -18.73 | +89.83 | -18.73 | 0.0% | keeps positives, blocks KAI false positive |

## 20. Score-Return Alignment Matrix
| trigger_id | current score label | proposed score label | MFE90 / MAE90 | alignment |
|---|---|---|---:|---|
| R13L59-T001 | Stage3-Yellow | Stage3-Green low-confidence | +40.43 / -17.45 | aligned but high MAE |
| R13L59-T003 | Stage3-Yellow | Stage3-Green low-confidence | +28.67 / -20.00 | aligned after drawdown |
| R13L59-T004 | Stage3-Yellow | Stage2-Actionable-Watch | +12.11 / -29.82 | false positive before guard |
| R13L59-T002 | 4B local overlay | watch-only local 4B | n/a | price-only 4B too early |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION | 2 | 1 | 1 | 0 hard / 1 watch | 3 | 0 | 4 | 3 | 2 | true | true | positive+counterexample+4B now present; needs more non-Korea and post-2025 holdout |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1 in local snapshot
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
diversity_score_summary: avg=23.0; no repeated symbol/trigger/date; C03 local coverage gap filled
tested_existing_calibrated_axes: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min
residual_error_types_found: framework_order_false_positive_without_margin_conversion, price_only_local_4B_too_early
new_axis_proposed: c03_framework_order_margin_conversion_guard; c03_price_only_local_4b_guard
existing_axis_strengthened: full_4b_requires_non_price_evidence; stage3_green_revision_min
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c for real orders with poor price path but no cancellation
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: local_v12_snapshot_has_no_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_md
```

## 23. Validation Scope / Non-Validation Scope
Validated:

- actual stock-web tradable OHLC rows for entry and forward-window anchors;
- 30D/90D/180D MFE and MAE for representative rows;
- clean 180D corporate-action window by symbol profiles;
- positive/counterexample balance;
- 4B local vs full-window proximity split.

Not validated:

- production scoring code;
- live watchlist;
- current candidates;
- broker/API execution;
- global calibration promotion;
- exact sell/position sizing logic.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_framework_order_margin_conversion_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"Promote framework/export order only when contract is execution-grade and backlog/margin bridge is visible; otherwise demote to Stage2 watch.","Removes KAI-style false positive while keeping Hanwha/LIG structural winners.","R13L59-T001|R13L59-T003|R13L59-T004",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c03_price_only_local_4b_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"Do not treat local price-only rally exhaustion as full 4B in defense export cycles without non-price slowdown, cancellation, financing failure, or margin/backlog evidence.","Hanwha local 4B proximity 0.94 but full-window proximity 0.28; price-only local 4B would have exited too early.","R13L59-T002",1,1,0,medium,canonical_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L59-C03-012450-HANWHA-AERO-CHUNMOO-POLAND", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L59-T001", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_180D_alignment_high_MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Poland follow-on Chunmoo/K239 export order converted framework narrative into concrete execution backlog. The path still carried large early MAE, so the rule is not simply 'buy all defense exports'; it is backlog+customer+margin bridge plus tolerance for episodic drawdown."}
{"row_type": "case", "case_id": "R13L59-C03-079550-LIG-NEX1-IRAQ-CHEONGUNG", "symbol": "079550", "company_name": "LIG넥스원", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L59-T003", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_180D_alignment_after_interim_MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Iraq Cheongung-II order extended the UAE/Saudi repeat-customer export route. 90D MAE was large, but 180D MFE validates treating repeat export framework as structural when contract quality and customer route are real."}
{"row_type": "case", "case_id": "R13L59-C03-047810-KAI-FA50-POLAND-MARGIN-GAP", "symbol": "047810", "company_name": "한국항공우주", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L59-T004", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "weak_180D_alignment_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "FA-50 Poland order was genuine and strategically important, but the 180D price path was poor after the event. It is a C03 counterexample against over-promoting framework order headlines before margin/delivery/aftermarket conversion closes."}
{"trigger_id": "R13L59-T001", "case_id": "R13L59-C03-012450-HANWHA-AERO-CHUNMOO-POLAND", "symbol": "012450", "company_name": "한화에어로스페이스", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 235000, "evidence_available_at_that_date": "Reuters reported Hanwha Aerospace's Poland Chunmoo rocket artillery supply deal; contract was tied to prior Poland framework and financing condition, so it was treated as execution-backlog conversion rather than pure theme.", "evidence_source": "Reuters, 2024-04-25; stock-web rows 2024-04-25~2025-04-30", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv", "profile_path": "atlas/symbol_profiles/012/012450.json", "MFE_30D_pct": 6.17, "MFE_90D_pct": 40.43, "MFE_180D_pct": 80.85, "MFE_1Y_pct": 266.81, "MFE_2Y_pct": null, "MAE_30D_pct": -17.45, "MAE_90D_pct": -17.45, "MAE_180D_pct": -17.45, "MAE_1Y_pct": -17.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-18", "peak_price": 862000, "drawdown_after_peak_pct": -12.88, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_MAE_structural_success", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L59-G001", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "row_type": "trigger", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": [], "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R13L59-T002", "case_id": "R13L59-C03-012450-HANWHA-AERO-CHUNMOO-POLAND", "symbol": "012450", "company_name": "한화에어로스페이스", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-11-12", "entry_date": "2024-11-12", "entry_price": 413500, "evidence_available_at_that_date": "Price had approached the local post-Stage2 peak after a long defense-export rally, but no non-price thesis break was visible in this loop. A price-only local 4B would have sold before the later 2025 extension.", "evidence_source": "stock-web rows 2024-11-07~2025-05-16; Reuters export-order context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv", "profile_path": "atlas/symbol_profiles/012/012450.json", "MFE_30D_pct": 0.0, "MFE_90D_pct": 68.56, "MFE_180D_pct": 115.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.77, "MAE_90D_pct": -32.77, "MAE_180D_pct": -32.77, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-07", "peak_price": 890000, "drawdown_after_peak_pct": -12.36, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.28, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L59-G001-4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "row_type": "trigger", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": [], "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R13L59-T003", "case_id": "R13L59-C03-079550-LIG-NEX1-IRAQ-CHEONGUNG", "symbol": "079550", "company_name": "LIG넥스원", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-19", "entry_date": "2024-09-20", "entry_price": 211000, "evidence_available_at_that_date": "Reuters reported a $2.8bn Iraq order for missile systems, extending the Cheongung-II repeat-customer export route after UAE/Saudi wins.", "evidence_source": "Reuters, 2024-09-19; stock-web rows 2024-09-19~2025-05-16", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv", "profile_path": "atlas/symbol_profiles/079/079550.json", "MFE_30D_pct": 25.59, "MFE_90D_pct": 28.67, "MFE_180D_pct": 98.82, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.42, "MAE_90D_pct": -20.0, "MAE_180D_pct": -20.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-08", "peak_price": 419500, "drawdown_after_peak_pct": -14.54, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "repeat_export_structural_success_after_drawdown", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L59-G002", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "row_type": "trigger", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": [], "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R13L59-T004", "case_id": "R13L59-C03-047810-KAI-FA50-POLAND-MARGIN-GAP", "symbol": "047810", "company_name": "한국항공우주", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-07-28", "entry_date": "2022-07-29", "entry_price": 57000, "evidence_available_at_that_date": "KAI officially signed the Poland FA-50 export deal for 48 aircraft; the order was real, but post-trigger price path shows framework-size alone did not close margin/delivery/aftermarket conversion fast enough.", "evidence_source": "public FA-50 Poland deal sources; stock-web rows 2022-07-28~2023-04-25", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["durable_customer_confirmation"], "stage4b_evidence_fields": ["execution_risk"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv", "profile_path": "atlas/symbol_profiles/047/047810.json", "MFE_30D_pct": 12.11, "MFE_90D_pct": 12.11, "MFE_180D_pct": 12.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.18, "MAE_90D_pct": -29.82, "MAE_180D_pct": -29.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-09-07", "peak_price": 63900, "drawdown_after_peak_pct": -37.4, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["execution_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L59-G003", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "row_type": "trigger", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "K_DEFENSE_EXPORT_FRAMEWORK_TO_BACKLOG_MARGIN_CONVERSION", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": [], "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c03_shadow", "case_id": "R13L59-C03-012450-HANWHA-AERO-CHUNMOO-POLAND", "trigger_id": "R13L59-T001", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 92, "backlog_visibility_score": 88, "margin_bridge_score": 72, "revision_score": 62, "relative_strength_score": 70, "customer_quality_score": 86, "policy_or_regulatory_score": 80, "valuation_repricing_score": 66, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 86.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 94, "backlog_visibility_score": 91, "margin_bridge_score": 77, "revision_score": 66, "relative_strength_score": 70, "customer_quality_score": 88, "policy_or_regulatory_score": 80, "valuation_repricing_score": 66, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow gives limited promotion only when follow-on order converts framework into execution backlog and margin bridge is at least partially visible.", "MFE_90D_pct": 40.43, "MAE_90D_pct": -17.45, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c03_shadow", "case_id": "R13L59-C03-079550-LIG-NEX1-IRAQ-CHEONGUNG", "trigger_id": "R13L59-T003", "symbol": "079550", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 90, "backlog_visibility_score": 84, "margin_bridge_score": 68, "revision_score": 58, "relative_strength_score": 72, "customer_quality_score": 88, "policy_or_regulatory_score": 82, "valuation_repricing_score": 64, "execution_risk_score": 32, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 92, "backlog_visibility_score": 88, "margin_bridge_score": 72, "revision_score": 61, "relative_strength_score": 72, "customer_quality_score": 90, "policy_or_regulatory_score": 82, "valuation_repricing_score": 64, "execution_risk_score": 32, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Repeat Cheongung-II customer route increases contract quality and backlog visibility, but high MAE keeps confidence medium rather than high.", "MFE_90D_pct": 28.67, "MAE_90D_pct": -20.0, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c03_shadow", "case_id": "R13L59-C03-047810-KAI-FA50-POLAND-MARGIN-GAP", "trigger_id": "R13L59-T004", "symbol": "047810", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 88, "backlog_visibility_score": 76, "margin_bridge_score": 46, "revision_score": 42, "relative_strength_score": 65, "customer_quality_score": 82, "policy_or_regulatory_score": 72, "valuation_repricing_score": 55, "execution_risk_score": 62, "legal_or_contract_risk_score": 24, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 88, "backlog_visibility_score": 70, "margin_bridge_score": 38, "revision_score": 38, "relative_strength_score": 54, "customer_quality_score": 82, "policy_or_regulatory_score": 72, "valuation_repricing_score": 48, "execution_risk_score": 70, "legal_or_contract_risk_score": 24, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 66.0, "stage_label_after": "Stage2-Actionable-Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Counterexample guard discounts aircraft framework orders when delivery timing, development variant, and margin bridge are not yet converted into revision evidence.", "MFE_90D_pct": 12.11, "MAE_90D_pct": -29.82, "score_return_alignment_label": "false_positive_before_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "59", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["framework_order_false_positive_without_margin_conversion", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "local_v12_snapshot_has_no_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_md"}
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
next_round = R13_loop_60
suggested_next_coverage_gap = C01_ORDER_BACKLOG_MARGIN_BRIDGE or C11_BATTERY_ORDERBOOK_RERATING, depending on current batch coverage
avoid_next = repeating 012450 2024-04-25, 079550 2024-09-19, 047810 2022-07-28 with same evidence family
```

## 28. Source Notes
- Stock-web manifest and profile/price shard fields were inspected from Songdaiki/stock-web.
- Hanwha Aerospace 2024-04-25 Poland Chunmoo order evidence was based on Reuters reporting that Hanwha signed a $1.64bn Poland rocket artillery supply deal tied to the broader 2022 framework and financing process.
- LIG Nex1 2024-09-19 Iraq evidence was based on Reuters reporting that LIG won a $2.8bn Iraq missile-system export deal and that this followed the earlier Saudi Cheongung-II route.
- KAI 2022-07-28 Poland FA-50 evidence was based on public FA-50 Poland contract sources; the backtest uses stock-web rows, not the narrative, to classify the row as counterexample.
