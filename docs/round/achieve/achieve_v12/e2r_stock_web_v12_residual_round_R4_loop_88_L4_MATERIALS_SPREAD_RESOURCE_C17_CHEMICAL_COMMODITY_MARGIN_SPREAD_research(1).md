# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_88_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

This loop continues loop 88 after R3. It adds 3 C17 chemical/commodity spread cases: one spread-to-margin bridge positive, one low-beta false Stage2, and one chemical/battery theme event-cap 4B counterexample.

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
scheduled_round = R4
scheduled_loop = 88
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 88
```

R4 permits L4 materials/spread/resource research. C17 is the chemical/commodity margin-spread bucket. This loop separates true spread-to-margin bridge from low-beta spread hope and theme-driven chemical/battery material spikes.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 21 rows / 15 symbols / good-bad Stage2 8-3 / 4B-4C 4-0
top covered symbols include 004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1)
```

Selected rows avoid the high-repeat C17 top list:

```text
120110 / Stage2-Actionable / 2025-02-05
069260 / Stage2-Actionable / 2024-01-02
161000 / Stage4B / 2023-06-19
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
| 120110 | atlas/symbol_profiles/120/120110.json | selected 2025 window clean; CA candidate is 2010-12-27 |
| 069260 | atlas/symbol_profiles/069/069260.json | selected 2024 window clean; CA candidate is 2010-09-27 |
| 161000 | atlas/symbol_profiles/161/161000.json | selected 2023 window clean; CA candidate is 2021-11-16 and earlier 2016-09-06 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L88_C17_KOLONIND_2025_CHEMICAL_SPREAD_MARGIN_BRIDGE_POSITIVE | 120110 | 2025-02-05 | yes | 180 | yes | yes | true |
| R4L88_C17_TKGHUCHEMS_2024_SPREAD_RECOVERY_FALSE_STAGE2 | 069260 | 2024-01-02 | yes | 180 | yes | yes | true |
| R4L88_C17_AEKYUNGCHEM_2023_CHEMICAL_BATTERY_THEME_EVENT_CAP_4B | 161000 | 2023-06-19 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_SPREAD_MARGIN_BRIDGE | Positive Stage2 requires spread-to-margin conversion and revision bridge. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | LOW_BETA_SPREAD_FALSE_STAGE2 | Stable spread/recovery watch without revision bridge can be weak-MFE false Stage2. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_BATTERY_THEME_EVENT_CAP | Chemical/battery-material theme spikes belong in 4B unless margin bridge is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L88_C17_KOLONIND_2025_CHEMICAL_SPREAD_MARGIN_BRIDGE_POSITIVE | 120110 | 코오롱인더 | positive | Strong MFE180 with modest MAE when spread recovery became margin bridge. |
| R4L88_C17_TKGHUCHEMS_2024_SPREAD_RECOVERY_FALSE_STAGE2 | 069260 | TKG휴켐스 | counterexample | Stable spread watch produced weak MFE and persistent drawdown. |
| R4L88_C17_AEKYUNGCHEM_2023_CHEMICAL_BATTERY_THEME_EVENT_CAP_4B | 161000 | 애경케미칼 | counterexample / 4B | Theme premium capped and drew down deeply before margin bridge confirmation. |

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
| Kolon Industries spread bridge | historical public/report proxy | true | true | shadow-only positive |
| TKG Huchems false spread Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| Aekyung Chemical event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 120110 | atlas/ohlcv_tradable_by_symbol_year/120/120110/2025.csv | atlas/symbol_profiles/120/120110.json |
| 069260 | atlas/ohlcv_tradable_by_symbol_year/069/069260/2024.csv | atlas/symbol_profiles/069/069260.json |
| 161000 | atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv | atlas/symbol_profiles/161/161000.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE | 120110 | Stage2-Actionable | 2025-02-05 | 28400 | positive | spread-to-margin bridge worked |
| R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD | 069260 | Stage2-Actionable | 2024-01-02 | 20950 | counterexample | low-beta spread hope without revision bridge |
| R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP | 161000 | Stage4B | 2023-06-19 | 26650 | counterexample/4B | chemical/battery theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE | 28400 | 27.29 | -2.11 | 27.29 | -7.57 | 72.18 | -7.57 | 2025-07-16 | 48900 | -30.47 |
| R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD | 20950 | 2.39 | -5.92 | 2.39 | -8.83 | 2.39 | -16.95 | 2024-01-02 | 21450 | -18.88 |
| R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP | 26650 | 4.32 | -26.08 | 4.32 | -58.54 | 4.32 | -59.55 | 2023-06-22 | 27800 | -61.22 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C17 Stage2 needs spread-to-margin and revision bridge, not commodity beta or stable spread hope |
| local_4b_watch_guard | strengthen: chemical/battery material theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 120110 | good_stage2 | Spread recovery converted into margin/revision-like upside. |
| 069260 | bad_stage2 | Stable spread watch did not produce enough upside and drifted lower. |
| 161000 | good_4B | Chemical/battery theme premium was capped and then drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 161000 chemical/battery theme event cap | 1.00 | 1.00 | good_full_window_4B_timing_chemical_battery_theme_event_cap |
| 069260 low-beta spread false Stage2 | 0.00 | 0.00 | weak_MFE_false_stage2_spread_recovery_without_revision_bridge |
| 120110 spread margin bridge | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 161000
```

No hard 4C candidate is proposed. C17 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 chemical/spread cases, Stage2 requires verified spread-to-margin conversion and revision bridge. Commodity beta, stable spread hope, or chemical/battery theme momentum alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rule = C17 should split margin-bridge positives from low-beta spread false Stage2 and chemical-material theme event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 11.33 | -24.98 | 0.67 | mixed; C17 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 11.33 | -24.98 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L4 spread bridge required | 2 | 14.84 | -8.20 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C17 bridge vs event-cap split | 2 | 14.84 | -8.20 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject low-beta/theme caps as positive | 1 | 27.29 | -7.57 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 120110 spread bridge | 66 | Stage2-Watch | 73 | Stage2-Actionable | 27.29 | -7.57 | chemical_spread_margin_bridge_positive |
| 069260 low-beta spread | 64 | Stage2-Actionable | 55 | Stage1/Watch | 2.39 | -8.83 | low_beta_spread_recovery_false_stage2 |
| 161000 chemical/battery cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.32 | -58.54 | chemical_battery_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C17 chemical spread margin-bridge positive, low-beta spread false Stage2, and chemical/battery theme event-cap 4B split."}
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
residual_error_types_found: chemical_spread_without_margin_revision_bridge, low_beta_false_stage2, chemical_battery_theme_event_cap_4B
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
- C17 chemical spread bridge vs low-beta false Stage2 vs theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,chemical_spread_requires_margin_revision_bridge,0,"C17 Stage2 should require verified spread-to-margin and revision bridge, not commodity price recovery or stable-spread hope alone","Kolon Industries positive worked; TKG Huchems false Stage2 and Aekyung theme-cap failed positive-stage promotion","R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE|R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD|R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,cap_chemical_theme_premium_as_4B_watch,0,"Chemical/battery material theme premiums can peak before actual margin conversion and then draw down heavily","Aekyung Chemical 2023 had low MFE90 and high MAE90 after the theme spike","R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP",1,1,1,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L88_C17_KOLONIND_2025_CHEMICAL_SPREAD_MARGIN_BRIDGE_POSITIVE", "symbol": "120110", "company_name": "코오롱인더", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Chemical/material spread recovery worked when the path looked like margin bridge rather than pure commodity price beta; strong 180D MFE with modest MAE.", "current_profile_verdict": "current_profile_kept_but_C17_positive_requires_spread_to_margin_bridge_not_price_recovery_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of report/disclosure URLs remain pending, so no production weight delta."}
{"row_type": "case", "case_id": "R4L88_C17_TKGHUCHEMS_2024_SPREAD_RECOVERY_FALSE_STAGE2", "symbol": "069260", "company_name": "TKG휴켐스", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stable chemical spread/recovery watch produced almost no MFE and persistent drawdown; C17 Stage2 should not be awarded to low-beta price-only spread hope.", "current_profile_verdict": "current_profile_false_positive_if_commodity_spread_watch_counts_without_revision_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "New C17 symbol; source-proxy only."}
{"row_type": "case", "case_id": "R4L88_C17_AEKYUNGCHEM_2023_CHEMICAL_BATTERY_THEME_EVENT_CAP_4B", "symbol": "161000", "company_name": "애경케미칼", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Chemical/battery-material theme premium capped before margin confirmation; very low forward MFE and deep MAE support 4B/watch routing.", "current_profile_verdict": "current_profile_4B_too_late_if_chemical_battery_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "New C17 symbol; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE", "case_id": "R4L88_C17_KOLONIND_2025_CHEMICAL_SPREAD_MARGIN_BRIDGE_POSITIVE", "symbol": "120110", "company_name": "코오롱인더", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "sector": "chemical_materials_spread", "primary_archetype": "chemical_spread_margin_bridge_recovery", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-05", "entry_date": "2025-02-05", "entry_price": 28400.0, "evidence_available_at_that_date": "chemical/material spread recovery and margin-bridge proxy; exact as-of report/disclosure URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["spread_recovery_proxy", "margin_bridge_proxy", "revision_watch", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_180D_MFE", "low_MAE_to_recovery_path"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_180D_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/120/120110/2025.csv", "profile_path": "atlas/symbol_profiles/120/120110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.29, "MFE_90D_pct": 27.29, "MFE_180D_pct": 72.18, "MFE_1Y_pct": "insufficient_forward_window_in_stock_web_or_not_calculated", "MFE_2Y_pct": "insufficient_forward_window_in_stock_web", "MAE_30D_pct": -2.11, "MAE_90D_pct": -7.57, "MAE_180D_pct": -7.57, "MAE_1Y_pct": "insufficient_forward_window_in_stock_web_or_not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-16", "peak_price": 48900.0, "drawdown_after_peak_pct": -30.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_chemical_spread_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L88_C17_120110_2025-02-05_28400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD", "case_id": "R4L88_C17_TKGHUCHEMS_2024_SPREAD_RECOVERY_FALSE_STAGE2", "symbol": "069260", "company_name": "TKG휴켐스", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "sector": "chemical_commodity_margin_spread", "primary_archetype": "low_beta_spread_recovery_false_stage2", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 20950.0, "evidence_available_at_that_date": "chemical spread / stable cashflow recovery proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["spread_recovery_watch", "stable_cashflow_proxy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE", "no_revision_bridge", "slow_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/069/069260/2024.csv", "profile_path": "atlas/symbol_profiles/069/069260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.39, "MFE_90D_pct": 2.39, "MFE_180D_pct": 2.39, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.92, "MAE_90D_pct": -8.83, "MAE_180D_pct": -16.95, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 21450.0, "drawdown_after_peak_pct": -18.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "weak_MFE_false_stage2_spread_recovery_without_revision_bridge", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_low_MFE_spread_recovery_false_positive", "current_profile_verdict": "current_profile_false_positive_if_spread_watch_counts_without_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L88_C17_069260_2024-01-02_20950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP", "case_id": "R4L88_C17_AEKYUNGCHEM_2023_CHEMICAL_BATTERY_THEME_EVENT_CAP_4B", "symbol": "161000", "company_name": "애경케미칼", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "sector": "chemical_battery_material_theme", "primary_archetype": "chemical_battery_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-06-19", "entry_date": "2023-06-19", "entry_price": 26650.0, "evidence_available_at_that_date": "chemical/battery-material theme premium and commodity-spread uncertainty proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_material_theme", "chemical_spread_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv", "profile_path": "atlas/symbol_profiles/161/161000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.32, "MFE_90D_pct": 4.32, "MFE_180D_pct": 4.32, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -26.08, "MAE_90D_pct": -58.54, "MAE_180D_pct": -59.55, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-22", "peak_price": 27800.0, "drawdown_after_peak_pct": -61.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_chemical_battery_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_chemical_battery_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L88_C17_161000_2023-06-19_26650", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L88_C17_KOLONIND_2025_CHEMICAL_SPREAD_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE", "symbol": "120110", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 60, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "chemical_spread_margin_bridge_positive", "MFE_90D_pct": 27.29, "MAE_90D_pct": -7.57, "score_return_alignment_label": "chemical_spread_margin_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L88_C17_TKGHUCHEMS_2024_SPREAD_RECOVERY_FALSE_STAGE2", "trigger_id": "R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD", "symbol": "069260", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "low_beta_spread_recovery_false_stage2", "MFE_90D_pct": 2.39, "MAE_90D_pct": -8.83, "score_return_alignment_label": "low_beta_spread_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_spread_watch_counts_without_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L88_C17_AEKYUNGCHEM_2023_CHEMICAL_BATTERY_THEME_EVENT_CAP_4B", "trigger_id": "R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP", "symbol": "161000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "chemical_battery_theme_event_cap_4B_guard", "MFE_90D_pct": 4.32, "MAE_90D_pct": -58.54, "score_return_alignment_label": "chemical_battery_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_chemical_battery_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "88", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_THEME_SPIKE_AND_COMMODITY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["chemical_spread_without_margin_revision_bridge", "low_beta_false_stage2", "chemical_battery_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R4
completed_loop = 88
next_round = R5
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
