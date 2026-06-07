# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | demand_slowdown_calloff_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. After local C08/C09/C01/C07/C06/C10 supplementation, C14 is the next unsupplemented Priority 0 archetype. Prior C14 symbols 361610 / 393890 / 025900 are avoided.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
demand_slowdown_calloff_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 98
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C14 is not a normal “positive-rerating” archetype. It is a brake system. The key question is whether EV demand, call-off, utilization and margin are breaking enough that the model should refuse Stage2/Stage3 promotion and route the row to 4B/4C.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C = 21 rows / Priority 0
previous C14 symbols avoided: 361610, 393890, 025900
recent local C08/C09/C01/C07/C06/C10 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C14 trigger families:

```text
247540 / Stage4C / 2024-02-28
373220 / Stage2-Actionable / 2024-02-16
003670 / Stage4B / 2024-02-15
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 247540 | atlas/symbol_profiles/247/247540.json | selected 2024 window clean after old 2022 CA candidates |
| 373220 | atlas/symbol_profiles/373/373220.json | no corporate-action candidate |
| 003670 | atlas/symbol_profiles/003/003670.json | selected 2024 window clean after old 2015/2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L98_C14_ECOPROBM_2024_CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION | 247540 | 2024-02-28 | yes | 180 | yes | yes | true |
| R3L98_C14_LGES_2024_CELLMAKER_UTILIZATION_FALSE_STAGE2 | 373220 | 2024-02-16 | yes | 180 | yes | yes | true |
| R3L98_C14_POSCOFUTUREM_2024_CATHODE_EVENT_CAP_4B | 003670 | 2024-02-15 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION | Protective success: rebound must be blocked when call-off/utilization/margin break persists. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | CELL_MAKER_UTILIZATION_FALSE_STAGE2 | Cell-maker rebound without call-off/utilization/margin bridge can become false Stage2. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | CATHODE_EVENT_CAP_4B | Cathode rebound premium should route to 4B when call-off and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L98_C14_ECOPROBM_2024_CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION | 247540 | 에코프로비엠 | protective positive | The rebound produced moderate MFE, but later high MAE made 4C/4B protection the right behavior. |
| R3L98_C14_LGES_2024_CELLMAKER_UTILIZATION_FALSE_STAGE2 | 373220 | LG에너지솔루션 | counterexample | Cell-maker utilization rebound watch had tiny MFE and high MAE without call-off/margin bridge. |
| R3L98_C14_POSCOFUTUREM_2024_CATHODE_EVENT_CAP_4B | 003670 | 포스코퓨처엠 | counterexample / 4B | Cathode recovery premium capped around the March rebound and later de-rated. |

## 8. Positive vs Counterexample Balance

```text
protective_positive_count = 1
positive_case_count = 0
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| EcoPro BM cathode demand-slowdown protection | historical public/news-report proxy | true | true | 4C protection |
| LGES cell-maker utilization false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| POSCO Future M cathode event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json |
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv | atlas/symbol_profiles/003/003670.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION | 247540 | Stage4C | 2024-02-28 | 256000 | protective positive | hard 4C protection succeeded |
| R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH | 373220 | Stage2-Actionable | 2024-02-16 | 410000 | counterexample | cell-maker utilization false Stage2 |
| R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP | 003670 | Stage4B | 2024-02-15 | 300500 | counterexample/4B | cathode event-cap guard |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION | 256000 | 16.60 | -10.94 | 16.60 | -31.56 | 16.60 | -38.48 | 2024-03-27 | 298500 | -47.24 |
| R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH | 410000 | 2.93 | -5.61 | 2.93 | -21.34 | 8.29 | -23.66 | 2024-03-13 | 422000 | -25.83 |
| R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP | 300500 | 13.48 | -9.98 | 13.48 | -17.14 | 13.48 | -32.61 | 2024-03-13 | 341000 | -40.62 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C14 Stage2-like rebound requires call-off recovery / utilization / ASP-mix / inventory / margin / revision bridge |
| demand_slowdown_calloff_guardrail | strengthen: EV demand-slowdown and call-off risk should block positive-stage promotion |
| local_4b_watch_guard | strengthen: cathode and cell-maker rebound premiums should route to 4B when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE C14 rows cannot promote without durable call-off/margin recovery |
| hard_4c_thesis_break_routes_to_4c | strengthen: confirmed demand/call-off/margin breaks should route to 4C protection |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B / 4C Comparison

No confirmed Stage3-Green row is introduced. C14 is protective by design: its best contribution is blocking false positive rebounds.

| symbol | stage quality | explanation |
|---|---|---|
| 247540 | good_4C_protection | Moderate rebound MFE was followed by large MAE; hard 4C/4B protection should block positive-stage promotion. |
| 373220 | bad_stage2 | Cell-maker rebound lacked call-off/utilization/margin bridge and produced tiny MFE. |
| 003670 | good_4B | Cathode rebound premium capped around March and later de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 247540 cathode demand slowdown protection | 0.86 | 0.86 | good 4C/4B protective timing after rebound failed |
| 373220 cell-maker false Stage2 | 0.97 | 0.97 | false Stage2 due missing call-off/utilization/margin bridge |
| 003670 cathode event cap | 0.88 | 0.88 | good 4B timing after cathode recovery premium |

## 16. 4C Protection Audit

```text
4C_case_count = 1
four_c_protection_label = hard_4C_protection_success for 247540
```

C14 should be allowed to contribute protective evidence even when it does not contribute a long-positive case. The guardrail is the signal.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 EV demand-slowdown cases, Stage2/Stage3 promotion is blocked unless customer call-off recovery, utilization recovery, ASP/mix, inventory normalization, margin, and revision bridge are visible. Price rebound, cathode sympathy, cell-maker recovery, IRA/AMPC theme, or relative-strength label alone remains 4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
rule = C14 should be scored as a protective/risk archetype: confirmed demand slowdown, call-off risk, utilization decline, inventory pressure, or margin break routes to 4B/4C protection, not positive-stage evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false-positive/protection rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 11.00 | -23.35 | 1.00 | C14 must remain protective |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 11.00 | -23.35 | 1.00 | weaker protection split |
| P1 sector_specific_candidate_profile | L3 call-off/utilization bridge required | 2 | 8.21 | -19.24 | 1.00 | better |
| P2 canonical_archetype_candidate_profile | C14 protective 4B/4C split | 3 | 11.00 | -23.35 | 1.00 | best explanatory fit |
| P3 relaxed-rebound profile | price rebound can promote positive stage | 3 | 11.00 | -23.35 | 0.00 | rejected |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 247540 demand slowdown protection | 66 | Stage2-Actionable-like rebound | 48 | Stage4C-protection | 16.60 | -31.56 | hard_4C_protection_success |
| 373220 cell-maker false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.93 | -21.34 | cellmaker_utilization_false_stage2 |
| 003670 cathode cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.48 | -17.14 | cathode_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "protective_positive_count": 1, "positive_case_count": 0, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 1, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C14 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10 supplementation. This run adds EcoPro BM, LG Energy Solution, and POSCO Future M while avoiding prior C14 symbols 361610, 393890, 025900."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, demand_slowdown_calloff_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: hard_4C_demand_slowdown_protection, cellmaker_utilization_false_stage2, cathode_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, demand_slowdown_calloff_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_guardrail_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C14 EV demand slowdown / 4B / 4C bridge vs false Stage2 split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,C14_blocks_positive_stage_when_calloff_utilization_margin_bridge_breaks,0,"C14 should not behave like normal positive-stage archetypes. It should block Stage2/Stage3 promotion when EV demand slowdown, call-off risk, utilization decline, inventory pressure, ASP/mix, or margin break is visible","EcoPro BM hard-4C protection worked; LGES and POSCO Future M rows failed positive-stage promotion","R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION|R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH|R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP",3,3,2,medium,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,hard_4c_thesis_break_routes_to_4c,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,route_confirmed_demand_slowdown_calloff_margin_break_to_4C_protection,0,"C14 is most useful when it turns EV-demand slowdown and call-off break into protection rather than positive-stage evidence","EcoPro BM rebound was correctly treated as protection success, not long-positive signal","R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION",1,1,0,medium,guardrail_shadow_only,"4C protection axis; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,block_positive_stage_when_EV_demand_rebound_has_high_or_persistent_MAE_without_calloff_margin_bridge,0,"High or persistent MAE after bridge-missing C14 entries should block Stage2/Stage3 promotion unless call-off recovery, utilization, ASP/mix and margin evidence survives","EcoPro BM MAE90=-31.56, LGES MAE90=-21.34, POSCO Future M MAE180=-32.61","R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION|R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH|R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP",3,3,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L98_C14_ECOPROBM_2024_CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "case_type": "hard_4C_protection_success_after_demand_slowdown_rebound", "positive_or_counterexample": "protective_positive", "best_trigger": "R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cathode demand-slowdown / call-off risk protection worked: the February rebound had moderate MFE but then rolled into persistent high MAE. For C14, the positive evidence is not long-side promotion; it is successful refusal to promote and hard 4C/4B protection.", "current_profile_verdict": "current_profile_kept_but_C14_should_route_demand_slowdown_calloff_margin_breaks_to_4B_4C_not_positive_stage", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L98_C14_LGES_2024_CELLMAKER_UTILIZATION_FALSE_STAGE2", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "case_type": "failed_rerating_cell_maker_utilization_rebound_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cell-maker utilization / EV-demand recovery watch had tiny 90D MFE and then high MAE. C14 Stage2 should not be awarded without confirmed customer call-off recovery, utilization, ASP/mix, margin, inventory and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_cellmaker_rebound_watch_counts_without_calloff_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R3L98_C14_POSCOFUTUREM_2024_CATHODE_EVENT_CAP_4B", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cathode / EV-demand recovery event premium capped around the March rebound and then de-rated. C14 should route bridge-missing cathode recovery premiums to 4B unless call-off recovery, utilization, ASP/mix, inventory normalization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_cathode_demand_recovery_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015/2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION", "case_id": "R3L98_C14_ECOPROBM_2024_CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "sector": "cathode_EV_demand_slowdown_customer_calloff_margin_break", "primary_archetype": "demand_slowdown_calloff_utilization_margin_break_protection", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | demand_slowdown_calloff_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 256000.0, "evidence_available_at_that_date": "cathode demand-slowdown / customer call-off / utilization and margin-break protection proxy during February battery rebound; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_report_proxy", "stage2_evidence_fields": ["battery_rebound_price_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["moderate_rebound_MFE_then_high_MAE", "calloff_utilization_margin_recheck"], "stage4c_evidence_fields": ["demand_slowdown_thesis_break_watch", "persistent_MAE_after_rebound", "positive_stage_blocked"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.6, "MFE_90D_pct": 16.6, "MFE_180D_pct": 16.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.94, "MAE_90D_pct": -31.56, "MAE_180D_pct": -38.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-27", "peak_price": 298500.0, "drawdown_after_peak_pct": -47.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "good_4C_protection_after_cathode_rebound_because_high_MAE_followed_without_calloff_margin_bridge", "four_b_evidence_type": ["demand_slowdown", "calloff_risk", "margin_break"], "four_c_protection_label": "hard_4C_protection_success", "trigger_outcome_label": "protective_success_hard_4C_cathode_demand_slowdown", "current_profile_verdict": "current_profile_kept_but_hard_4C_watch_should_block_positive_stage", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R3L98_C14_247540_2024-02-28_256000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_protection", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH", "case_id": "R3L98_C14_LGES_2024_CELLMAKER_UTILIZATION_FALSE_STAGE2", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "sector": "cellmaker_EV_demand_utilization_rebound_watch", "primary_archetype": "cellmaker_rebound_watch_without_calloff_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | demand_slowdown_calloff_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 410000.0, "evidence_available_at_that_date": "cell-maker utilization / EV-demand recovery watch without confirmed customer call-off, utilization, ASP/mix, inventory normalization or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cellmaker_rebound_watch", "EV_demand_recovery_theme", "relative_strength_bounce"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "high_MAE90", "calloff_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.93, "MFE_90D_pct": 2.93, "MFE_180D_pct": 8.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.61, "MAE_90D_pct": -21.34, "MAE_180D_pct": -23.66, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 422000.0, "drawdown_after_peak_pct": -25.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "cellmaker_utilization_rebound_watch_was_false_stage2_due_missing_calloff_utilization_margin_revision_bridge", "four_b_evidence_type": ["cellmaker_rebound_premium", "bridge_missing", "tiny_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_cellmaker_utilization_rebound_without_calloff_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_cellmaker_rebound_watch_counts_without_calloff_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L98_C14_373220_2024-02-16_410000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP", "case_id": "R3L98_C14_POSCOFUTUREM_2024_CATHODE_EVENT_CAP_4B", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "sector": "cathode_EV_demand_recovery_event_premium", "primary_archetype": "cathode_demand_slowdown_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | demand_slowdown_calloff_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 300500.0, "evidence_available_at_that_date": "cathode / EV-demand recovery event premium without confirmed call-off recovery, utilization, ASP/mix, inventory normalization, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cathode_rebound_event", "EV_demand_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "calloff_utilization_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.48, "MFE_90D_pct": 13.48, "MFE_180D_pct": 13.48, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.98, "MAE_90D_pct": -17.14, "MAE_180D_pct": -32.61, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 341000.0, "drawdown_after_peak_pct": -40.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_cathode_recovery_event_cap_due_missing_calloff_utilization_margin_bridge", "four_b_evidence_type": ["cathode_rebound_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_cathode_demand_slowdown_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_cathode_demand_recovery_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2015_2021_CA", "same_entry_group_id": "R3L98_C14_003670_2024-02-15_300500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R3L98_C14_ECOPROBM_2024_CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION", "trigger_id": "R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable-like rebound", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 48, "stage_label_after": "Stage4C-protection", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "cathode_demand_slowdown_hard_4C_protection", "MFE_90D_pct": 16.6, "MAE_90D_pct": -31.56, "score_return_alignment_label": "hard_4C_protection_success", "current_profile_verdict": "current_profile_kept_but_hard_4C_watch_should_block_positive_stage"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R3L98_C14_LGES_2024_CELLMAKER_UTILIZATION_FALSE_STAGE2", "trigger_id": "R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cellmaker_utilization_false_stage2", "MFE_90D_pct": 2.93, "MAE_90D_pct": -21.34, "score_return_alignment_label": "cellmaker_utilization_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_cellmaker_rebound_watch_counts_without_calloff_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R3L98_C14_POSCOFUTUREM_2024_CATHODE_EVENT_CAP_4B", "trigger_id": "R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cathode_demand_slowdown_event_cap_4B_guard", "MFE_90D_pct": 13.48, "MAE_90D_pct": -17.14, "score_return_alignment_label": "cathode_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_cathode_demand_recovery_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION_VS_CELL_MAKER_UTILIZATION_FALSE_STAGE2_AND_CATHODE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "protective_positive_count": 1, "positive_case_count": 0, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 1, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "demand_slowdown_calloff_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["hard_4C_demand_slowdown_protection", "cellmaker_utilization_false_stage2", "cathode_event_cap_4B"], "loop_contribution_label": "canonical_archetype_guardrail_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- C14 is primarily a protective archetype, so hard 4C / 4B protection success should not be converted into long-positive evidence.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C14 rows need explicit customer call-off recovery, utilization recovery, ASP/mix, inventory normalization, margin and revision bridge before positive promotion.
- In C14, bridge-missing EV-demand rebound rows with high/persistent MAE should route to 4B/4C, not Stage3.
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
9. Report new independent cases, counterexamples, protective positives, and residual error types.
10. Add tests that bridge-missing C14 EV-demand slowdown rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R3
completed_loop = 98
completed_canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
