# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
```

This loop continues loop 90 after R1. It adds 3 C07 HBM equipment / order relative-strength cases: one HBM test-equipment order/RS positive, one scrubber/equipment false Stage2, and one HBM reflow equipment 4B event-cap counterexample.

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
scheduled_loop = 90
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 90
```

R2 permits L2 AI/semiconductor/electronics research. Previous R2 loop 89 used C10, so this loop shifts to C07 and tests whether HBM/equipment relative strength is supported by customer order, tester capacity, backlog, delivery, margin, or revision bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 11 rows / 9 symbols / good-bad Stage2 7-0 / 4B-4C 1-0
top covered symbols include 042700(2), 064760(2), 003160(1), 036200(1), 036540(1), 039440(1)
previous R2 loop-88 C09 symbols avoided: 039030, 140860, 101490
previous R2 loop-89 C10 symbols avoided: 036930, 095610, 084370
```

Selected rows avoid hard duplicates:

```text
232140 / Stage2-Actionable / 2024-02-27
036200 / Stage2-Actionable / 2024-06-28
039440 / Stage4B / 2024-03-13
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
| 232140 | atlas/symbol_profiles/232/232140.json | selected 2024 window clean after old 2017 SPAC/merger CA |
| 036200 | atlas/symbol_profiles/036/036200.json | selected 2024 window clean; CA candidates are 2017 or earlier |
| 039440 | atlas/symbol_profiles/039/039440.json | selected 2024 window clean; CA candidates are 2018 or earlier |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L90_C07_YC_2024_HBM_TEST_EQUIPMENT_ORDER_RS_POSITIVE | 232140 | 2024-02-27 | yes | 180 | yes | yes | true |
| R2L90_C07_UNISEM_2024_SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2 | 036200 | 2024-06-28 | yes | 180 | yes | yes | true |
| R2L90_C07_STI_2024_HBM_REFLOW_THEME_EVENT_CAP_4B | 039440 | 2024-03-13 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE | Positive Stage2 requires customer order, tester capacity, backlog, delivery, margin, or revision bridge. |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2 | HBM-adjacent equipment theme without customer/order bridge can become high-MAE false Stage2. |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_REFLOW_THEME_EVENT_CAP_4B | Reflow/equipment theme premium should route to 4B when order/revision bridge stops improving. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L90_C07_YC_2024_HBM_TEST_EQUIPMENT_ORDER_RS_POSITIVE | 232140 | 와이씨 | positive | HBM test-equipment order/RS path produced explosive MFE with shallow entry MAE. |
| R2L90_C07_UNISEM_2024_SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2 | 036200 | 유니셈 | counterexample | Equipment/scrubber theme spike had weak MFE and deep MAE. |
| R2L90_C07_STI_2024_HBM_REFLOW_THEME_EVENT_CAP_4B | 039440 | 에스티아이 | counterexample / 4B | HBM reflow/equipment premium capped at the March spike and de-rated. |

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
| YC HBM test-equipment bridge | historical public/report proxy | true | true | shadow-only positive |
| Unisem scrubber/equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| STI HBM reflow theme cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 232140 | atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv | atlas/symbol_profiles/232/232140.json |
| 036200 | atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv | atlas/symbol_profiles/036/036200.json |
| 039440 | atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv | atlas/symbol_profiles/039/039440.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS | 232140 | Stage2-Actionable | 2024-02-27 | 5900 | positive | HBM test equipment order/RS bridge worked |
| R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME | 036200 | Stage2-Actionable | 2024-06-28 | 11570 | counterexample | scrubber/equipment false Stage2 |
| R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP | 039440 | Stage4B | 2024-03-13 | 38750 | counterexample/4B | HBM reflow event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS | 5900 | 43.56 | -4.41 | 227.12 | -4.41 | 227.12 | -4.41 | 2024-06-26 | 19300 | -43.89 |
| R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME | 11570 | 7.87 | -25.07 | 7.87 | -46.76 | 7.87 | -47.54 | 2024-07-04 | 12480 | -50.64 |
| R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP | 38750 | 11.61 | -19.74 | 11.61 | -19.74 | 11.61 | -50.45 | 2024-03-13 | 43250 | -55.61 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C07 Stage2 needs customer/order/capacity/revision bridge |
| local_4b_watch_guard | strengthen: HBM-adjacent equipment themes should route to 4B watch if bridge is missing |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 232140 | good_stage2 | HBM tester/customer order bridge produced explosive upside. |
| 036200 | bad_stage2 | Equipment theme had weak MFE and high MAE without HBM-specific bridge. |
| 039440 | good_4B | HBM reflow/equipment theme premium capped and de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 036200 scrubber/equipment false Stage2 | 1.00 | 1.00 | equipment theme spike was false Stage2 event cap |
| 039440 HBM reflow cap | 1.00 | 1.00 | good full-window 4B timing |
| 232140 HBM test-equipment bridge | n/a | n/a | positive Stage2, but later HBM equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 036200 / 039440
```

No hard 4C candidate is proposed. R2 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 HBM equipment/order RS cases, Stage2 requires verified customer order, capacity, backlog, delivery schedule, margin, or revision bridge. HBM, test equipment, scrubber, reflow, or semiconductor equipment theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rule = C07 should split customer/order/capacity positives from HBM-adjacent equipment false Stage2 and equipment-theme event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 82.20 | -23.64 | 0.67 | mixed; C07 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 82.20 | -23.64 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L2 HBM order bridge required | 2 | 117.50 | -25.59 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C07 bridge vs event-cap split | 2 | 117.50 | -25.59 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing equipment themes as positive | 1 | 227.12 | -4.41 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 232140 HBM order/RS bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 227.12 | -4.41 | HBM_test_equipment_order_RS_positive |
| 036200 scrubber false Stage2 | 66 | Stage2-Actionable | 53 | Stage1/Watch | 7.87 | -46.76 | scrubber_equipment_theme_false_stage2 |
| 039440 reflow cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.61 | -19.74 | HBM_reflow_equipment_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C07 HBM test-equipment order/RS positive, scrubber-equipment false Stage2, and HBM reflow equipment event-cap 4B split."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 1
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: HBM_test_equipment_order_RS_positive, scrubber_equipment_theme_false_stage2, HBM_reflow_equipment_event_cap_4B
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
- C07 HBM equipment order/RS bridge vs equipment-theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,C07_requires_customer_order_capacity_revision_bridge,0,"C07 Stage2 should require customer order, tester capacity, backlog, delivery, margin, or revision bridge, not HBM/equipment/theme label alone","YC positive worked; Unisem and STI theme/event rows failed positive-stage promotion","R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS|R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME|R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,cap_equipment_theme_premiums_as_4B_watch,0,"HBM-adjacent equipment theme premiums can peak before durable customer/order/revision bridge appears","Unisem showed high-MAE false Stage2; STI showed event-cap behavior with severe 180D MAE","R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME|R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L90_C07_YC_2024_HBM_TEST_EQUIPMENT_ORDER_RS_POSITIVE", "symbol": "232140", "company_name": "와이씨", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM test-equipment order / relative-strength bridge produced explosive 30D/90D/180D MFE with shallow entry MAE; C07 works when customer order, tester capacity, and revision bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C07_positive_requires_customer_order_capacity_revision_bridge_not_HBM_equipment_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017 SPAC/merger CA candidate; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L90_C07_UNISEM_2024_SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2", "symbol": "036200", "company_name": "유니셈", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion only; same archetype symbol exists in coverage, but selected date/failure mode is new.", "independent_evidence_weight": 0.5, "score_price_alignment": "Scrubber/equipment theme spike had very small forward MFE and severe 90D/180D MAE; C07 Stage2 should not be awarded without HBM-specific order/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_equipment_theme_counts_without_HBM_customer_order_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Reduced weight because this is a soft expansion of a once-covered C07 symbol; modern window clean."}
{"row_type": "case", "case_id": "R2L90_C07_STI_2024_HBM_REFLOW_THEME_EVENT_CAP_4B", "symbol": "039440", "company_name": "에스티아이", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion only; same archetype symbol exists in coverage, but selected event-cap/4B role is new.", "independent_evidence_weight": 0.5, "score_price_alignment": "HBM reflow/equipment theme premium capped around the March spike and then de-rated; theme premium should route to 4B unless order/revision bridge keeps expanding.", "current_profile_verdict": "current_profile_4B_too_late_if_HBM_reflow_equipment_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Reduced weight because this is a soft expansion of a once-covered C07 symbol; selected 2024 window clean after old CA candidates."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS", "case_id": "R2L90_C07_YC_2024_HBM_TEST_EQUIPMENT_ORDER_RS_POSITIVE", "symbol": "232140", "company_name": "와이씨", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "sector": "HBM_test_equipment_order_relative_strength", "primary_archetype": "HBM_test_equipment_customer_order_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-27", "entry_date": "2024-02-27", "entry_price": 5900.0, "evidence_available_at_that_date": "HBM memory test equipment, customer order, tester capacity, and revision bridge proxy; exact as-of URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["HBM_test_equipment_order_proxy", "customer_capacity_visibility", "relative_strength_reversal", "revision_bridge_proxy"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "low_entry_MAE"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_HBM_equipment_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "profile_path": "atlas/symbol_profiles/232/232140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 43.56, "MFE_90D_pct": 227.12, "MFE_180D_pct": 227.12, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.41, "MAE_90D_pct": -4.41, "MAE_180D_pct": -4.41, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 19300.0, "drawdown_after_peak_pct": -43.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_HBM_equipment_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_test_equipment_order_RS_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2017_SPAC_CA", "same_entry_group_id": "R2L90_C07_232140_2024-02-27_5900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME", "case_id": "R2L90_C07_UNISEM_2024_SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2", "symbol": "036200", "company_name": "유니셈", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "sector": "semiconductor_scrubber_equipment_theme", "primary_archetype": "scrubber_equipment_theme_without_HBM_order_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-28", "entry_date": "2024-06-28", "entry_price": 11570.0, "evidence_available_at_that_date": "semiconductor equipment / scrubber theme and HBM-adjacent equipment spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["equipment_theme_spike", "HBM_adjacent_narrative", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "customer_order_revision_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv", "profile_path": "atlas/symbol_profiles/036/036200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.87, "MFE_90D_pct": 7.87, "MFE_180D_pct": 7.87, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -25.07, "MAE_90D_pct": -46.76, "MAE_180D_pct": -47.54, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-04", "peak_price": 12480.0, "drawdown_after_peak_pct": -50.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "scrubber_equipment_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["price_only", "positioning_overheat", "order_revision_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_scrubber_equipment_theme_without_HBM_order_bridge", "current_profile_verdict": "current_profile_false_positive_if_equipment_theme_counts_without_HBM_customer_order_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L90_C07_036200_2024-06-28_11570", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C07_symbol_new_failure_mode", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP", "case_id": "R2L90_C07_STI_2024_HBM_REFLOW_THEME_EVENT_CAP_4B", "symbol": "039440", "company_name": "에스티아이", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "sector": "HBM_reflow_equipment_theme", "primary_archetype": "HBM_reflow_equipment_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-13", "entry_date": "2024-03-13", "entry_price": 38750.0, "evidence_available_at_that_date": "HBM reflow / semiconductor equipment premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["HBM_reflow_equipment_theme", "relative_strength_spike", "equipment_cycle_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv", "profile_path": "atlas/symbol_profiles/039/039440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.61, "MFE_90D_pct": 11.61, "MFE_180D_pct": 11.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.74, "MAE_90D_pct": -19.74, "MAE_180D_pct": -50.45, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 43250.0, "drawdown_after_peak_pct": -55.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_HBM_reflow_equipment_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_HBM_reflow_equipment_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L90_C07_039440_2024-03-13_38750", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C07_symbol_new_4B_event_cap_role", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L90_C07_YC_2024_HBM_TEST_EQUIPMENT_ORDER_RS_POSITIVE", "trigger_id": "R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS", "symbol": "232140", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 50, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_test_equipment_order_RS_positive", "MFE_90D_pct": 227.12, "MAE_90D_pct": -4.41, "score_return_alignment_label": "HBM_test_equipment_order_RS_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L90_C07_UNISEM_2024_SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2", "trigger_id": "R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME", "symbol": "036200", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "scrubber_equipment_theme_false_stage2", "MFE_90D_pct": 7.87, "MAE_90D_pct": -46.76, "score_return_alignment_label": "scrubber_equipment_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_equipment_theme_counts_without_HBM_customer_order_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L90_C07_STI_2024_HBM_REFLOW_THEME_EVENT_CAP_4B", "trigger_id": "R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP", "symbol": "039440", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_reflow_equipment_event_cap_4B_guard", "MFE_90D_pct": 11.61, "MAE_90D_pct": -19.74, "score_return_alignment_label": "HBM_reflow_equipment_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_HBM_reflow_equipment_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "90", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_SCRUBBER_AND_REFLOW_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 1, "same_archetype_new_symbol_count": 1, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["HBM_test_equipment_order_RS_positive", "scrubber_equipment_theme_false_stage2", "HBM_reflow_equipment_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 90
next_round = R3
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
