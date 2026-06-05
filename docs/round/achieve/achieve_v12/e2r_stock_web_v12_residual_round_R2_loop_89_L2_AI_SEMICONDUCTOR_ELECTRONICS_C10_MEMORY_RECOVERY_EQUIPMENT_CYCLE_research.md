# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

This loop continues loop 89 after R1. It adds 3 C10 memory-recovery equipment cases: one order/revision bridge positive, one deposition-equipment false Stage2, and one memory-equipment 4B event-cap counterexample.

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
scheduled_round = R2
scheduled_loop = 89
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 89
```

R2 permits AI/semiconductor/electronics research. Previous R2 loop-88 used C09, so this loop moves to C10 and targets the residual split inside memory-recovery equipment: true order/revision bridge versus equipment-cycle theme cap.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 29 rows / 18 symbols / good-bad Stage2 15-5 / 4B-4C 1-0
top covered symbols include 089970(3), 281820(3), 319660(3), 042700(2), 064290(2), 079370(2)
previous R2 loop-88 C09 symbols avoided: 039030, 140860, 101490
```

Selected rows avoid those repeated combinations:

```text
036930 / Stage2-Actionable / 2024-02-13
095610 / Stage2-Actionable / 2024-04-17
084370 / Stage4B / 2024-04-08
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
| 036930 | atlas/symbol_profiles/036/036930.json | selected 2024 window clean; CA candidate is old 2000-06-22 |
| 095610 | atlas/symbol_profiles/095/095610.json | selected 2024 window clean; CA candidates are 2011/2016 |
| 084370 | atlas/symbol_profiles/084/084370.json | selected 2024 window clean; CA candidates are 2007/2010/2012 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L89_C10_JUSUNG_2024_MEMORY_EQUIPMENT_REORDER_POSITIVE | 036930 | 2024-02-13 | yes | 180 | yes | yes | true |
| R2L89_C10_TES_2024_DEPOSITION_EQUIPMENT_FALSE_STAGE2 | 095610 | 2024-04-17 | yes | 180 | yes | yes | true |
| R2L89_C10_EUGENETECH_2024_MEMORY_EQUIPMENT_EVENT_CAP_4B | 084370 | 2024-04-08 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE | Positive Stage2 requires customer, order, revision, capacity, or margin bridge. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | DEPOSITION_THEME_FALSE_STAGE2 | Deposition-equipment theme spike without bridge can be high-MAE false Stage2. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_EQUIPMENT_EVENT_CAP_4B | Equipment-cycle premium should route to 4B when bridge stops improving. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L89_C10_JUSUNG_2024_MEMORY_EQUIPMENT_REORDER_POSITIVE | 036930 | 주성엔지니어링 | positive | Order/revision-like memory equipment path produced strong MFE30/90 with controlled MAE90. |
| R2L89_C10_TES_2024_DEPOSITION_EQUIPMENT_FALSE_STAGE2 | 095610 | 테스 | counterexample | Deposition-equipment spike had insufficient follow-through and high MAE. |
| R2L89_C10_EUGENETECH_2024_MEMORY_EQUIPMENT_EVENT_CAP_4B | 084370 | 유진테크 | counterexample / 4B | April memory-equipment premium capped and drew down deeply. |

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
| Jusung memory-equipment bridge | historical public/report proxy | true | true | shadow-only positive |
| TES deposition-equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| EugeneTech memory-equipment cap | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 036930 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv | atlas/symbol_profiles/036/036930.json |
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json |
| 084370 | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | atlas/symbol_profiles/084/084370.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER | 036930 | Stage2-Actionable | 2024-02-13 | 31950 | positive | memory-equipment order/revision bridge worked |
| R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME | 095610 | Stage2-Actionable | 2024-04-17 | 29300 | counterexample | deposition-equipment theme false Stage2 |
| R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP | 084370 | Stage4B | 2024-04-08 | 50200 | counterexample/4B | memory-equipment event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER | 31950 | 27.54 | -4.85 | 29.73 | -6.10 | 29.73 | -30.67 | 2024-04-08 | 41450 | -46.56 |
| R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME | 29300 | 12.29 | -23.89 | 12.29 | -26.28 | 12.29 | -34.30 | 2024-04-17 | 32900 | -39.42 |
| R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP | 50200 | 4.78 | -35.76 | 4.78 | -56.08 | 4.78 | -56.08 | 2024-04-08 | 52600 | -58.08 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C10 Stage2 needs customer/order/revision/margin bridge |
| local_4b_watch_guard | strengthen: memory/deposition equipment theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 036930 | good_stage2 | Early memory-equipment order/revision bridge worked before the later cycle drawdown. |
| 095610 | bad_stage2 | Deposition theme spike had insufficient follow-through and high MAE. |
| 084370 | good_4B | Memory-equipment premium was capped at the April peak and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 084370 memory equipment cap | 1.00 | 1.00 | good_full_window_4B_timing_memory_equipment_event_cap |
| 095610 deposition theme false Stage2 | 1.00 | 1.00 | stage2_false_positive_deposition_theme_event_cap |
| 036930 memory-equipment bridge | n/a | n/a | positive Stage2, but later cycle valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 095610 / 084370
```

No hard 4C candidate is proposed. R2 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 memory-recovery equipment cases, Stage2 requires verified customer/order/revision/margin bridge. Memory recovery, deposition equipment, HBM, AI, or equipment-cycle label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rule = C10 should split equipment order/revision positives from deposition/memory-equipment theme false Stage2 and 4B event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 15.60 | -29.49 | 0.67 | mixed; C10 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 15.60 | -29.49 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L2 customer/order bridge required | 2 | 21.01 | -16.19 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C10 bridge vs event-cap split | 2 | 21.01 | -16.19 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing equipment themes as positive | 1 | 29.73 | -6.10 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 036930 order/revision bridge | 66 | Stage2-Watch | 73 | Stage2-Actionable | 29.73 | -6.10 | memory_equipment_order_revision_positive |
| 095610 deposition false Stage2 | 66 | Stage2-Actionable | 54 | Stage1/Watch | 12.29 | -26.28 | deposition_equipment_theme_false_stage2 |
| 084370 event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.78 | -56.08 | memory_equipment_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C10 memory-equipment order/revision positive, deposition-equipment false Stage2, and memory-equipment event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: memory_equipment_order_revision_positive, deposition_equipment_theme_false_stage2, memory_equipment_event_cap_4B
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
- C10 memory recovery equipment bridge vs equipment-theme event cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,C10_requires_customer_order_revision_margin_bridge,0,"C10 Stage2 should require customer/order/revision/margin bridge, not memory-recovery or equipment-cycle label alone","Jusung positive worked; TES and EugeneTech theme/event rows failed positive-stage promotion","R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER|R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME|R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,cap_equipment_theme_premium_as_4B_watch,0,"Memory/deposition equipment premiums can peak before durable order/revision bridge appears and then draw down heavily","TES and EugeneTech showed low/limited MFE90 with high MAE90 after equipment-theme spikes","R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME|R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L89_C10_JUSUNG_2024_MEMORY_EQUIPMENT_REORDER_POSITIVE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory-recovery equipment rerating worked when entry preceded the early 2024 equipment order/revision path; 30D/90D MFE was strong while 90D MAE stayed controlled.", "current_profile_verdict": "current_profile_kept_but_C10_positive_requires_order_revision_customer_bridge_not_memory_recovery_label_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of customer/order/revision evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R2L89_C10_TES_2024_DEPOSITION_EQUIPMENT_FALSE_STAGE2", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Deposition/memory-equipment theme spike carried forward upside only briefly; later high MAE means Stage2 should not be granted without customer/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_deposition_equipment_theme_counts_without_customer_order_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "New C10 symbol; source-proxy only."}
{"row_type": "case", "case_id": "R2L89_C10_EUGENETECH_2024_MEMORY_EQUIPMENT_EVENT_CAP_4B", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory-equipment premium peaked near the April spike and then suffered deep drawdown; equipment cycle premium should route to 4B when order/revision bridge is no longer improving.", "current_profile_verdict": "current_profile_4B_too_late_if_memory_equipment_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Event-cap counterexample; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER", "case_id": "R2L89_C10_JUSUNG_2024_MEMORY_EQUIPMENT_REORDER_POSITIVE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "sector": "memory_equipment_deposition_recovery", "primary_archetype": "memory_equipment_order_revision_customer_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 31950.0, "evidence_available_at_that_date": "memory recovery / deposition equipment order and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["memory_recovery_cycle", "equipment_order_bridge_proxy", "customer_process_relevance", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_equipment_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.54, "MFE_90D_pct": 29.73, "MFE_180D_pct": 29.73, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.85, "MAE_90D_pct": -6.1, "MAE_180D_pct": -30.67, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_equipment_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_memory_equipment_order_revision_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L89_C10_036930_2024-02-13_31950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME", "case_id": "R2L89_C10_TES_2024_DEPOSITION_EQUIPMENT_FALSE_STAGE2", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "sector": "deposition_memory_equipment", "primary_archetype": "deposition_equipment_theme_without_customer_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-17", "entry_date": "2024-04-17", "entry_price": 29300.0, "evidence_available_at_that_date": "deposition/memory-equipment theme spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["memory_equipment_theme", "deposition_equipment_spike", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_follow_through", "customer_revision_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.29, "MFE_90D_pct": 12.29, "MFE_180D_pct": 12.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.89, "MAE_90D_pct": -26.28, "MAE_180D_pct": -34.3, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-17", "peak_price": 32900.0, "drawdown_after_peak_pct": -39.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "stage2_false_positive_deposition_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_deposition_equipment_theme_without_bridge", "current_profile_verdict": "current_profile_false_positive_if_deposition_equipment_theme_counts_without_customer_order_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L89_C10_095610_2024-04-17_29300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP", "case_id": "R2L89_C10_EUGENETECH_2024_MEMORY_EQUIPMENT_EVENT_CAP_4B", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "sector": "memory_equipment_cycle", "primary_archetype": "memory_equipment_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-08", "entry_date": "2024-04-08", "entry_price": 50200.0, "evidence_available_at_that_date": "memory-equipment cycle premium after April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["memory_equipment_cycle", "relative_strength_spike", "equipment_recovery_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "profile_path": "atlas/symbol_profiles/084/084370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.78, "MFE_90D_pct": 4.78, "MFE_180D_pct": 4.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -35.76, "MAE_90D_pct": -56.08, "MAE_180D_pct": -56.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 52600.0, "drawdown_after_peak_pct": -58.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_memory_equipment_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_memory_equipment_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L89_C10_084370_2024-04-08_50200", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L89_C10_JUSUNG_2024_MEMORY_EQUIPMENT_REORDER_POSITIVE", "trigger_id": "R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER", "symbol": "036930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 40, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_equipment_order_revision_positive", "MFE_90D_pct": 29.73, "MAE_90D_pct": -6.1, "score_return_alignment_label": "memory_equipment_order_revision_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L89_C10_TES_2024_DEPOSITION_EQUIPMENT_FALSE_STAGE2", "trigger_id": "R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME", "symbol": "095610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "deposition_equipment_theme_false_stage2", "MFE_90D_pct": 12.29, "MAE_90D_pct": -26.28, "score_return_alignment_label": "deposition_equipment_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_deposition_equipment_theme_counts_without_customer_order_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L89_C10_EUGENETECH_2024_MEMORY_EQUIPMENT_EVENT_CAP_4B", "trigger_id": "R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP", "symbol": "084370", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_equipment_event_cap_4B_guard", "MFE_90D_pct": 4.78, "MAE_90D_pct": -56.08, "score_return_alignment_label": "memory_equipment_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_memory_equipment_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "89", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_REORDER_REVISION_BRIDGE_VS_DEPOSITION_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["memory_equipment_order_revision_positive", "deposition_equipment_theme_false_stage2", "memory_equipment_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 89
next_round = R3
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
