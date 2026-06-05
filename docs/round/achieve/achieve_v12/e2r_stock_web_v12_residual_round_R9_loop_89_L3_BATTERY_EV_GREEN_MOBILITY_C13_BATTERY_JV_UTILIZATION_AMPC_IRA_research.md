# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

This loop continues loop 89 after R8. R9 allows L3 mobility/transport-style battery research, so this run uses C13 instead of repeating the previous R9 loop-88 C29 mobility margin set.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R9
scheduled_loop = 89
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 89
```

R9 can be L3 or L9 depending on mobility/transport nature. This file uses the L3 route and focuses on battery utilization, customer demand, margin, and AMPC/JV-like bridge quality.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 23 rows / 16 symbols / good-bad Stage2 9-2 / 4B-4C 2-0
top covered symbols include 005070(3), 020150(3), 003670(2), 025900(2), 348370(2), 002710(1)
previous R9 loop-88 C29 symbols avoided: 161390, 003620, 204320
```

Selected rows avoid those repeated combinations:

```text
004490 / Stage2-Actionable / 2024-01-24
243840 / Stage2-Actionable / 2024-06-26
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
| 004490 | atlas/symbol_profiles/004/004490.json | selected 2024 window clean; CA candidate is 2000-04-03 |
| 243840 | atlas/symbol_profiles/243/243840.json | selected 2024-06-26 post-2024-04-26 CA window |
| 393890 | atlas/symbol_profiles/393/393890.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L89_C13_SEBANG_2024_BATTERY_VOLUME_MARGIN_BRIDGE_POSITIVE | 004490 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2 | 243840 | 2024-06-26 | yes | 180 | yes | post-CA | true |
| R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B | 393890 | 2024-02-22 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | BATTERY_UTILIZATION_MARGIN_BRIDGE | Positive Stage2 requires utilization, customer demand, margin, revision, AMPC/IRA, or capacity bridge. |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | BATTERY_PARTS_CALL_OFF_FALSE_STAGE2 | Battery-parts utilization theme without customer/margin bridge can become high-MAE false Stage2. |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | SEPARATOR_UTILIZATION_EVENT_CAP_4B | Separator/customer utilization premium should route to 4B when bridge is capped or uncertain. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L89_C13_SEBANG_2024_BATTERY_VOLUME_MARGIN_BRIDGE_POSITIVE | 004490 | 세방전지 | positive | Battery utilization/margin bridge produced high MFE with shallow MAE. |
| R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2 | 243840 | 신흥에스이씨 | counterexample | Battery-parts utilization spike lacked customer/margin confirmation and drew down. |
| R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B | 393890 | 더블유씨피 | counterexample / 4B | Separator utilization premium capped at February bounce and then de-rated. |

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
| Sebang battery utilization/margin | historical public/report proxy | true | true | shadow-only positive |
| Shinheung SEC battery parts false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| WCP separator utilization cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 004490 | atlas/ohlcv_tradable_by_symbol_year/004/004490/2024.csv | atlas/symbol_profiles/004/004490.json |
| 243840 | atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv | atlas/symbol_profiles/243/243840.json |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE | 004490 | Stage2-Actionable | 2024-01-24 | 54600 | positive | battery utilization/margin bridge worked |
| R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION | 243840 | Stage2-Actionable | 2024-06-26 | 9640 | counterexample | battery-parts utilization false Stage2 |
| R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP | 393890 | Stage4B | 2024-02-22 | 47100 | counterexample/4B | separator utilization event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE | 54600 | 65.38 | -1.47 | 124.36 | -1.47 | 124.36 | -1.47 | 2024-05-13 | 122500 | -38.69 |
| R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION | 9640 | 8.61 | -20.54 | 8.61 | -33.82 | 8.61 | -33.82 | 2024-06-26 | 10470 | -39.06 |
| R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP | 47100 | 4.88 | -27.07 | 4.88 | -36.41 | 4.88 | -43.52 | 2024-02-22 | 49400 | -48.18 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C13 Stage2 needs utilization/customer/margin/AMPC/JV/capacity bridge |
| local_4b_watch_guard | strengthen: battery-parts and separator utilization premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 004490 | good_stage2 | Utilization/margin bridge created high MFE with very shallow drawdown. |
| 243840 | bad_stage2 | Battery-parts utilization label had weak upside and deep drawdown. |
| 393890 | good_4B | Separator utilization premium capped at the February event peak. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 243840 battery parts false Stage2 | 1.00 | 1.00 | battery-parts utilization spike was false Stage2 event cap |
| 393890 separator utilization cap | 1.00 | 1.00 | good full-window 4B timing |
| 004490 utilization/margin bridge | n/a | n/a | positive Stage2, but later battery valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 243840 / 393890
```

No hard 4C candidate is proposed. R9 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery utilization/JV/AMPC cases, Stage2 requires verified utilization, customer demand, AMPC/IRA economics, JV/capacity, margin, or revision bridge. Battery-parts, separator, or EV-demand recovery label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rule = C13 should split utilization/margin bridge positives from battery-parts false Stage2 and separator customer-utilization event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 45.95 | -23.90 | 0.67 | mixed; C13 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 45.95 | -23.90 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 utilization/margin bridge required | 2 | 66.49 | -17.65 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C13 bridge vs event-cap split | 2 | 66.49 | -17.65 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery themes as positive | 1 | 124.36 | -1.47 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 004490 utilization/margin bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 124.36 | -1.47 | battery_utilization_margin_bridge_positive |
| 243840 battery-parts false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 8.61 | -33.82 | battery_parts_utilization_false_stage2 |
| 393890 separator cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.88 | -36.41 | separator_utilization_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C13 battery utilization/margin positive, battery-parts call-off false Stage2, and separator utilization event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: battery_utilization_margin_bridge_positive, battery_parts_utilization_false_stage2, separator_utilization_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
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
- C13 battery utilization/JV/AMPC bridge vs battery-parts/separator event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,C13_requires_utilization_customer_margin_AMPC_or_capacity_bridge,0,"C13 Stage2 should require utilization, customer demand, AMPC/IRA economics, JV/capacity, margin, or revision bridge, not battery-parts or separator label alone","Sebang positive worked; Shinheung SEC and WCP event/call-off rows failed positive-stage promotion","R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE|R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION|R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,cap_battery_parts_and_separator_utilization_premiums_as_4B_watch,0,"Battery parts and separator utilization premiums can peak before confirmed customer/margin bridge appears","Shinheung SEC and WCP showed weak MFE90 with high MAE90 after bridge-missing spikes","R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION|R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L89_C13_SEBANG_2024_BATTERY_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "004490", "company_name": "세방전지", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery volume/margin and mobility battery demand bridge produced high MFE with very shallow entry MAE; C13 works only when utilization and margin bridge are visible, not from battery label alone.", "current_profile_verdict": "current_profile_kept_but_C13_positive_requires_utilization_margin_or_AMPC_like_bridge_not_battery_label_only", "price_source": "Songdaiki/stock-web", "notes": "Old 2000 corporate-action candidate only; selected 2024 window clean. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2", "symbol": "243840", "company_name": "신흥에스이씨", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "case_type": "failed_rerating_customer_calloff", "positive_or_counterexample": "counterexample", "best_trigger": "R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "2024-04-26 corporate-action candidate was blocked; selected post-CA 2024-06-26 spike window only.", "independent_evidence_weight": 0.5, "score_price_alignment": "Battery parts/utilization spike had weak forward MFE and deep MAE; C13 Stage2 should not be awarded without confirmed customer demand, utilization, and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Reduced weight because selected row is post-CA and source-proxy only."}
{"row_type": "case", "case_id": "R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Separator/customer utilization premium capped after the February bounce and then drew down; bridge-missing separator utilization premium should route to 4B/watch.", "current_profile_verdict": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE", "case_id": "R9L89_C13_SEBANG_2024_BATTERY_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "004490", "company_name": "세방전지", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "sector": "battery_mobility_volume_margin", "primary_archetype": "battery_utilization_volume_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 54600.0, "evidence_available_at_that_date": "battery demand/utilization, mobility replacement or ESS volume, and margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["battery_volume_demand_proxy", "utilization_margin_bridge_proxy", "mobility_or_ESS_demand", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "low_entry_MAE"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_battery_margin_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004490/2024.csv", "profile_path": "atlas/symbol_profiles/004/004490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 65.38, "MFE_90D_pct": 124.36, "MFE_180D_pct": 124.36, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.47, "MAE_90D_pct": -1.47, "MAE_180D_pct": -1.47, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 122500.0, "drawdown_after_peak_pct": -38.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_margin_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_battery_volume_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L89_C13_004490_2024-01-24_54600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "case_id": "R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2", "symbol": "243840", "company_name": "신흥에스이씨", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "sector": "battery_parts_customer_utilization", "primary_archetype": "battery_parts_customer_calloff_false_stage2", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 9640.0, "evidence_available_at_that_date": "battery parts/customer utilization and EV demand recovery proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_parts_utilization_theme", "customer_demand_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "customer_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv", "profile_path": "atlas/symbol_profiles/243/243840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.61, "MFE_90D_pct": 8.61, "MFE_180D_pct": 8.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.54, "MAE_90D_pct": -33.82, "MAE_180D_pct": -33.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 10470.0, "drawdown_after_peak_pct": -39.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "battery_parts_utilization_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["price_only", "positioning_overheat", "customer_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_battery_parts_utilization_without_customer_bridge", "current_profile_verdict": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-04-26_CA_window", "same_entry_group_id": "R9L89_C13_243840_2024-06-26_9640", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "post-CA row only; 2024-04-26 corporate-action candidate blocked from entry selection", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "case_id": "R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "sector": "battery_separator_customer_utilization", "primary_archetype": "separator_utilization_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 47100.0, "evidence_available_at_that_date": "separator customer utilization / EV battery demand recovery premium after February bounce; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["separator_utilization_premium", "customer_demand_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.88, "MFE_90D_pct": 4.88, "MFE_180D_pct": 4.88, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.07, "MAE_90D_pct": -36.41, "MAE_180D_pct": -43.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 49400.0, "drawdown_after_peak_pct": -48.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_separator_customer_utilization_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "customer_utilization_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L89_C13_393890_2024-02-22_47100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L89_C13_SEBANG_2024_BATTERY_VOLUME_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE", "symbol": "004490", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_utilization_margin_bridge_positive", "MFE_90D_pct": 124.36, "MAE_90D_pct": -1.47, "score_return_alignment_label": "battery_utilization_margin_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2", "trigger_id": "R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "symbol": "243840", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_parts_utilization_false_stage2", "MFE_90D_pct": 8.61, "MAE_90D_pct": -33.82, "score_return_alignment_label": "battery_parts_utilization_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B", "trigger_id": "R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "separator_utilization_event_cap_4B_guard", "MFE_90D_pct": 4.88, "MAE_90D_pct": -36.41, "score_return_alignment_label": "separator_utilization_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_UTILIZATION_MARGIN_BRIDGE_VS_PARTS_AND_SEPARATOR_CALL_OFF_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["battery_utilization_margin_bridge_positive", "battery_parts_utilization_false_stage2", "separator_utilization_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reason":"all selected rows have usable 180D stock-web windows; 243840 entry was shifted after the 2024-04-26 corporate-action candidate","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 89
next_round = R10
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
