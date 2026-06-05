# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

This file is the corrected final output for this execution. The scheduler state after R2 loop 92 is R3 / loop 92. It fills C13 battery JV/utilization/AMPC-IRA behavior, after the prior R3 loop 91 used C14 and R3 loop 90 used C12.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 92
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 92
```

R3 permits L3 battery/EV/green mobility research. This run avoids recent R3 C14/C12 symbols and uses a fresh C13 split around JV utilization, AMPC/IRA economics, customer call-off and margin bridge quality.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 23 rows / 16 symbols / good-bad Stage2 9-2 / 4B-4C 2-0
top covered symbols include 005070(3), 020150(3), 003670(2), 025900(2), 348370(2), 002710(1)
previous R3 loop-88 C14 symbols avoided: 361610, 051910, 011790
previous R3 loop-90 C12 symbols avoided: 002710, 290670, 396300
previous R3 loop-91 C14 symbols avoided: 066970, 089980, 336370
previous R2 loop-92 C08 symbols avoided: 058470, 098120, 080580
```

Selected rows avoid hard duplicates and top repeated C13 symbols:

```text
006400 / Stage2-Actionable / 2024-01-24
373220 / Stage2-Actionable / 2024-02-16
393890 / Stage4B / 2024-02-22
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
| 006400 | atlas/symbol_profiles/006/006400.json | selected 2024 window clean after old 2014 CA |
| 373220 | atlas/symbol_profiles/373/373220.json | no corporate-action candidate |
| 393890 | atlas/symbol_profiles/393/393890.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L92_C13_SAMSDI_2024_CELL_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE | 006400 | 2024-01-24 | yes | 180 | yes | yes | true |
| R3L92_C13_LGES_2024_CELL_AMPC_UTILIZATION_FALSE_STAGE2 | 373220 | 2024-02-16 | yes | 180 | yes | yes | true |
| R3L92_C13_WCP_2024_SEPARATOR_AMPC_EVENT_CAP_4B | 393890 | 2024-02-22 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE | Positive Stage2 requires JV utilization, customer volume/call-off, AMPC/IRA economics, margin and revision bridge. |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | CELL_AMPC_UTILIZATION_FALSE_STAGE2 | Battery-cell utilization/AMPC label without volume and margin bridge can become false Stage2. |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | SEPARATOR_AMPC_EVENT_CAP_4B | Separator AMPC/IRA event premium should route to 4B when utilization/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L92_C13_SAMSDI_2024_CELL_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE | 006400 | 삼성SDI | positive | JV/utilization/AMPC bridge produced strong MFE with shallow early MAE. |
| R3L92_C13_LGES_2024_CELL_AMPC_UTILIZATION_FALSE_STAGE2 | 373220 | LG에너지솔루션 | counterexample | Cell AMPC/utilization rebound had weak 90D MFE and material drawdown without durable margin bridge. |
| R3L92_C13_WCP_2024_SEPARATOR_AMPC_EVENT_CAP_4B | 393890 | 더블유씨피 | counterexample / 4B | Separator AMPC event premium capped at the February spike and then de-rated sharply. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Samsung SDI cell JV/utilization bridge | historical public/report proxy | true | true | shadow-only positive |
| LGES cell AMPC false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| WCP separator AMPC cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | atlas/symbol_profiles/006/006400.json |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE | 006400 | Stage2-Actionable | 2024-01-24 | 354000 | positive | cell JV/utilization AMPC bridge worked |
| R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND | 373220 | Stage2-Actionable | 2024-02-16 | 410000 | counterexample | cell AMPC/utilization false Stage2 |
| R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP | 393890 | Stage4B | 2024-02-22 | 47100 | counterexample/4B | separator AMPC event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE | 354000 | 25.00 | -3.39 | 39.69 | -3.39 | 39.69 | -8.90 | 2024-03-25 | 494500 | -34.78 |
| R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND | 410000 | 2.93 | -8.29 | 2.93 | -20.49 | 8.29 | -24.15 | 2024-10-08 | 444000 | -26.46 |
| R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP | 47100 | 4.88 | -27.07 | 4.88 | -27.07 | 4.88 | -58.49 | 2024-02-22 | 49400 | -63.36 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C13 Stage2 needs JV utilization / customer volume / AMPC economics / margin / revision bridge |
| local_4b_watch_guard | strengthen: separator and cell AMPC event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE AMPC/utilization rows cannot promote without durable customer-volume and margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is AMPC/utilization bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 006400 | good_stage2_with_later_watch | JV/utilization AMPC bridge produced strong MFE, but battery-cycle 4B watch remains needed. |
| 373220 | bad_stage2 | Cell AMPC/utilization rebound had weak 90D MFE and lacked durable margin bridge. |
| 393890 | good_4B | Separator AMPC event premium capped near entry and de-rated sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 373220 cell AMPC false Stage2 | 0.92 | 0.92 | false Stage2 due missing customer-volume/margin bridge |
| 393890 separator AMPC cap | 1.00 | 1.00 | good full-window 4B timing |
| 006400 cell JV utilization bridge | n/a | n/a | positive Stage2, but later battery-cell cycle 4B watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 373220 / 393890
```

No hard 4C candidate is proposed. R3 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery JV/utilization/AMPC cases, Stage2 requires verified customer volume/call-off, JV utilization, IRA/AMPC economics, gross-margin recovery, or revision bridge. Battery-cell, separator, IRA, AMPC, JV, or utilization label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rule = C13 should split true JV/utilization/AMPC positives from battery-cell false Stage2 and separator AMPC event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 15.83 | -16.98 | 0.67 | mixed; C13 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 15.83 | -16.98 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 customer-volume/AMPC bridge required | 2 | 21.31 | -11.94 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C13 bridge vs event-cap split | 2 | 21.31 | -11.94 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery AMPC themes as positive | 1 | 39.69 | -3.39 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 006400 cell JV/utilization bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 39.69 | -3.39 | cell_JV_utilization_AMPC_positive |
| 373220 cell AMPC false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 2.93 | -20.49 | cell_AMPC_utilization_false_stage2 |
| 393890 separator AMPC cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.88 | -27.07 | separator_AMPC_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C13 battery-cell JV/utilization/AMPC positive, cell utilization false Stage2, and separator AMPC event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: cell_JV_utilization_AMPC_positive, cell_AMPC_utilization_false_stage2, separator_AMPC_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C13 battery JV/utilization/AMPC bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,C13_requires_JV_utilization_customer_volume_AMPC_margin_revision_bridge,0,"C13 Stage2 should require JV utilization, customer volume/call-off, IRA/AMPC economics, margin, or revision bridge, not battery/IRA/utilization label alone","Samsung SDI positive worked; LG Energy Solution and WCP theme/event rows failed positive-stage promotion","R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE|R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND|R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,cap_bridge_missing_cell_and_separator_AMPC_premiums_as_4B_watch,0,"Battery-cell and separator AMPC/IRA premiums can peak before utilization and margin bridge is proven","LGES had weak 90D MFE; WCP showed full-window event-cap behavior after February spike","R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND|R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,block_positive_stage_when_AMPC_utilization_theme_has_high_MAE_without_margin_bridge,0,"High MAE after a battery JV/AMPC/utilization entry should block Stage2/Stage3 promotion unless customer volume and margin evidence survives","LGES MAE180=-24.15 and WCP MAE180=-58.49","R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND|R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L92_C13_SAMSDI_2024_CELL_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "case_type": "structural_success_with_later_cycle_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-cell JV/utilization and IRA/AMPC recovery bridge produced strong 30D/90D MFE with shallow initial MAE, but later cycle weakness required 4B watch. C13 works only when utilization, customer volume, AMPC/IRA economics, and margin/revision bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C13_positive_requires_JV_utilization_AMPC_margin_revision_bridge_not_battery_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2014 CA candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L92_C13_LGES_2024_CELL_AMPC_UTILIZATION_FALSE_STAGE2", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "case_type": "failed_rerating_utilization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-cell AMPC/utilization rebound watch had weak 90D MFE and meaningful drawdown when EV demand, utilization and margin/revision bridge were not yet durable. C13 Stage2 should not be awarded from battery-cell recovery label alone.", "current_profile_verdict": "current_profile_false_positive_if_cell_AMPC_utilization_rebound_counts_without_customer_volume_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R3L92_C13_WCP_2024_SEPARATOR_AMPC_EVENT_CAP_4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Separator / IRA-AMPC event premium capped near the February spike and then de-rated sharply. C13 bridge-missing separator/JV/utilization premiums should route to 4B unless utilization, customer call-off, margin, and AMPC bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_separator_AMPC_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE", "case_id": "R3L92_C13_SAMSDI_2024_CELL_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "sector": "battery_cell_JV_utilization_AMPC_IRA", "primary_archetype": "cell_JV_utilization_customer_volume_AMPC_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 354000.0, "evidence_available_at_that_date": "battery-cell JV/utilization recovery, customer volume, IRA/AMPC economics and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["JV_utilization_proxy", "IRA_AMPC_economics_proxy", "customer_volume_bridge", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_battery_cycle_valuation_watch", "utilization_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.0, "MFE_90D_pct": 39.69, "MFE_180D_pct": 39.69, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.39, "MAE_90D_pct": -3.39, "MAE_180D_pct": -8.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 494500.0, "drawdown_after_peak_pct": -34.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_cell_utilization_cycle_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "AMPC_utilization_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_cell_JV_utilization_AMPC_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2014_CA", "same_entry_group_id": "R3L92_C13_006400_2024-01-24_354000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND", "case_id": "R3L92_C13_LGES_2024_CELL_AMPC_UTILIZATION_FALSE_STAGE2", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "sector": "battery_cell_AMPC_utilization_rebound_watch", "primary_archetype": "cell_AMPC_utilization_rebound_without_customer_volume_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 410000.0, "evidence_available_at_that_date": "battery-cell AMPC/utilization rebound and EV demand recovery watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["cell_AMPC_utilization_rebound", "EV_demand_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "customer_volume_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.93, "MFE_90D_pct": 2.93, "MFE_180D_pct": 8.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.29, "MAE_90D_pct": -20.49, "MAE_180D_pct": -24.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-08", "peak_price": 444000.0, "drawdown_after_peak_pct": -26.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "cell_AMPC_utilization_rebound_was_false_stage2_due_missing_customer_volume_margin_bridge", "four_b_evidence_type": ["AMPC_utilization_watch", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_cell_AMPC_utilization_rebound_without_customer_volume_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_cell_AMPC_utilization_rebound_counts_without_customer_volume_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L92_C13_373220_2024-02-16_410000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP", "case_id": "R3L92_C13_WCP_2024_SEPARATOR_AMPC_EVENT_CAP_4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "sector": "battery_separator_AMPC_event_premium", "primary_archetype": "separator_AMPC_utilization_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 47100.0, "evidence_available_at_that_date": "battery separator / IRA-AMPC utilization event premium after February spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["separator_AMPC_theme", "utilization_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "customer_calloff_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.88, "MFE_90D_pct": 4.88, "MFE_180D_pct": 4.88, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.07, "MAE_90D_pct": -27.07, "MAE_180D_pct": -58.49, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 49400.0, "drawdown_after_peak_pct": -63.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_separator_AMPC_event_cap", "four_b_evidence_type": ["separator_AMPC_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_separator_AMPC_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_separator_AMPC_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L92_C13_393890_2024-02-22_47100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L92_C13_SAMSDI_2024_CELL_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE", "trigger_id": "R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 55, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "cell_JV_utilization_AMPC_positive", "MFE_90D_pct": 39.69, "MAE_90D_pct": -3.39, "score_return_alignment_label": "cell_JV_utilization_AMPC_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L92_C13_LGES_2024_CELL_AMPC_UTILIZATION_FALSE_STAGE2", "trigger_id": "R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "cell_AMPC_utilization_false_stage2", "MFE_90D_pct": 2.93, "MAE_90D_pct": -20.49, "score_return_alignment_label": "cell_AMPC_utilization_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_cell_AMPC_utilization_rebound_counts_without_customer_volume_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L92_C13_WCP_2024_SEPARATOR_AMPC_EVENT_CAP_4B", "trigger_id": "R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "separator_AMPC_event_cap_4B_guard", "MFE_90D_pct": 4.88, "MAE_90D_pct": -27.07, "score_return_alignment_label": "separator_AMPC_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_separator_AMPC_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_CELL_JV_UTILIZATION_AMPC_BRIDGE_VS_CELL_FALSE_STAGE2_AND_SEPARATOR_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["cell_JV_utilization_AMPC_positive", "cell_AMPC_utilization_false_stage2", "separator_AMPC_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
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
10. Add tests that bridge-missing C13 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 92
next_round = R4
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
