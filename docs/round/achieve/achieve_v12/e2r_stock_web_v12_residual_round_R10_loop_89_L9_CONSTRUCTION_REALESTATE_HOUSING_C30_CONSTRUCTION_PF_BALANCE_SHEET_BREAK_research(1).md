# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This loop continues loop 89 after R9. It adds 3 C30 construction/PF cases: one housing/PF discount repair positive, one construction-beta false Stage2, and one political/construction event-cap 4B counterexample.

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
scheduled_round = R10
scheduled_loop = 89
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 89
```

R10 is the L9 construction/PF round. Previous R10 loop-88 already used 서희건설, 동아지질, 태영건설, so this loop intentionally shifts to different symbols and tests PF discount repair versus construction beta or political construction event premium.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK = 81 rows / 31 symbols / good-bad Stage2 16-29 / 4B-4C 3-4
top covered symbols include 002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4)
previous R10 loop-88 symbols avoided: 035890, 028100, 009410
```

Selected rows avoid those repeated combinations:

```text
010780 / Stage2-Actionable / 2024-01-18
005960 / Stage2-Actionable / 2024-02-01
001470 / Stage4B / 2024-03-15
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
| 010780 | atlas/symbol_profiles/010/010780.json | selected 2024 window clean; CA candidates are 2011 or earlier |
| 005960 | atlas/symbol_profiles/005/005960.json | selected 2024 window clean; CA candidates are 2016 or earlier |
| 001470 | atlas/symbol_profiles/001/001470.json | selected 2024 window clean; CA candidates are 2019 or earlier |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L89_C30_ISDONGSEO_2024_HOUSING_PF_DISCOUNT_REPAIR_POSITIVE | 010780 | 2024-01-18 | yes | 180 | yes | yes | true |
| R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2 | 005960 | 2024-02-01 | yes | 180 | yes | yes | true |
| R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B | 001470 | 2024-03-15 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | HOUSING_PF_DISCOUNT_REPAIR | Positive Stage2 requires PF/cashflow/balance-sheet repair and asset-value recovery. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CONSTRUCTION_BETA_FALSE_STAGE2 | Generic construction beta without PF/cashflow bridge can be weak-MFE false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | POLITICAL_CONSTRUCTION_EVENT_CAP | Political/contract event premium should route to 4B if the balance bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L89_C30_ISDONGSEO_2024_HOUSING_PF_DISCOUNT_REPAIR_POSITIVE | 010780 | 아이에스동서 | positive | Housing/PF discount repair path produced strong MFE90 with shallow early MAE. |
| R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2 | 005960 | 동부건설 | counterexample | Construction beta/PF normalization watch had tiny MFE and later drawdown. |
| R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B | 001470 | 삼부토건 | counterexample / 4B | Political/construction event premium capped at the March spike and collapsed. |

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
| IS Dongseo PF repair | historical public/report proxy | true | true | shadow-only positive |
| Dongbu Construction beta false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Sambu political construction cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 010780 | atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv | atlas/symbol_profiles/010/010780.json |
| 005960 | atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv | atlas/symbol_profiles/005/005960.json |
| 001470 | atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv | atlas/symbol_profiles/001/001470.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR | 010780 | Stage2-Actionable | 2024-01-18 | 23600 | positive | housing/PF repair bridge worked |
| R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA | 005960 | Stage2-Actionable | 2024-02-01 | 5430 | counterexample | construction beta false Stage2 |
| R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 001470 | Stage4B | 2024-03-15 | 2690 | counterexample/4B | political construction event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR | 23600 | 22.25 | -1.06 | 32.20 | -1.06 | 32.20 | -13.77 | 2024-03-22 | 31200 | -34.78 |
| R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA | 5430 | 1.29 | -6.08 | 1.29 | -11.79 | 1.29 | -23.11 | 2024-02-19 | 5500 | -24.09 |
| R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 2690 | 6.51 | -53.72 | 6.51 | -53.72 | 6.51 | -53.72 | 2024-03-15 | 2865 | -56.54 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs PF/cashflow/balance repair bridge |
| local_4b_watch_guard | strengthen: construction beta and political/contract event premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 010780 | good_stage2 | PF/housing repair bridge had strong MFE and low early MAE. |
| 005960 | bad_stage2 | Construction beta had almost no upside without PF/cashflow confirmation. |
| 001470 | good_4B | Political/construction event premium capped and then collapsed. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 005960 construction beta false Stage2 | 0.01 | 0.01 | construction beta watch was false Stage2 due missing PF/cashflow bridge |
| 001470 political construction cap | 1.00 | 1.00 | good full-window 4B timing |
| 010780 housing/PF repair | n/a | n/a | positive Stage2, but later PF repair valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 005960 / 001470
```

No hard 4C candidate is proposed. R10 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF cases, Stage2 requires verified PF, cashflow, debt maturity, balance-sheet repair, asset-value recovery, or margin/revision bridge. Construction beta, political theme, and contract/event premium alone remain watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split real PF/cashflow repair positives from construction-beta false Stage2 and political/construction event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 13.33 | -22.19 | 0.67 | mixed; C30 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 13.33 | -22.19 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/cashflow repair required | 2 | 16.75 | -6.43 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 repair vs beta/event-cap split | 2 | 16.75 | -6.43 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction themes as positive | 1 | 32.20 | -1.06 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 010780 PF repair | 66 | Stage2-Watch | 74 | Stage2-Actionable | 32.20 | -1.06 | housing_PF_discount_repair_positive |
| 005960 construction beta false | 66 | Stage2-Actionable | 54 | Stage1/Watch | 1.29 | -11.79 | construction_beta_false_stage2 |
| 001470 political event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.51 | -53.72 | political_construction_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 housing/PF discount repair positive, construction-beta false Stage2, and political construction event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: housing_PF_discount_repair_positive, construction_beta_false_stage2, political_construction_event_cap_4B
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
- C30 PF/cashflow repair vs construction-beta / political-event cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_PF_cashflow_balance_repair_bridge,0,"C30 Stage2 should require verified PF/cashflow/balance-sheet repair, not construction beta or political/contract event label alone","IS Dongseo positive worked; Dongbu Construction and Sambu Construction event/beta rows failed positive-stage promotion","R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR|R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA|R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_construction_beta_and_political_event_premiums_as_4B_watch,0,"Construction beta and political/contract-event premiums can peak before durable PF/cashflow repair appears","Dongbu showed weak MFE; Sambu showed full-window event-cap behavior with severe MAE","R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA|R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L89_C30_ISDONGSEO_2024_HOUSING_PF_DISCOUNT_REPAIR_POSITIVE", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Housing/PF discount repair produced strong 90D MFE with low early MAE; later 180D drawdown confirms that the positive Stage2 still needs 4B valuation watch after repair run.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_PF_cashflow_balance_repair_not_construction_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; CA candidates are 2011 or earlier. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "case_type": "failed_rerating_balance_risk", "positive_or_counterexample": "counterexample", "best_trigger": "R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Construction-beta / PF-recovery watch had almost no forward upside and later persistent MAE; C30 Stage2 should not be granted without PF/cashflow/balance bridge.", "current_profile_verdict": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; CA candidates are 2016 or earlier. Source-proxy only."}
{"row_type": "case", "case_id": "R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Political/construction contract-event premium peaked around the March spike and then collapsed; bridge-missing construction event premium should route to 4B/watch, not Stage3-Green.", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; CA candidates are 2019 or earlier. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR", "case_id": "R10L89_C30_ISDONGSEO_2024_HOUSING_PF_DISCOUNT_REPAIR_POSITIVE", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "sector": "housing_construction_PF_discount_repair", "primary_archetype": "housing_PF_cashflow_balance_repair", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-18", "entry_date": "2024-01-18", "entry_price": 23600.0, "evidence_available_at_that_date": "housing/PF discount repair, cashflow/balance-sheet repair, and asset-value recovery proxy; exact as-of URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["PF_discount_repair_proxy", "cashflow_balance_bridge_proxy", "housing_asset_value_recovery", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "low_entry_MAE"], "stage4b_evidence_fields": ["valuation_watch_after_PF_repair_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.25, "MFE_90D_pct": 32.2, "MFE_180D_pct": 32.2, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.06, "MAE_90D_pct": -1.06, "MAE_180D_pct": -13.77, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-22", "peak_price": 31200.0, "drawdown_after_peak_pct": -34.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_PF_repair_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_housing_PF_discount_repair_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L89_C30_010780_2024-01-18_23600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "case_id": "R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "sector": "construction_beta_PF_watch", "primary_archetype": "construction_beta_without_PF_cashflow_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 5430.0, "evidence_available_at_that_date": "construction sector rebound / PF-risk normalization watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["construction_beta", "PF_normalization_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "cashflow_balance_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.29, "MFE_90D_pct": 1.29, "MFE_180D_pct": 1.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.08, "MAE_90D_pct": -11.79, "MAE_180D_pct": -23.11, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 5500.0, "drawdown_after_peak_pct": -24.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.01, "four_b_full_window_peak_proximity": 0.01, "four_b_timing_verdict": "construction_beta_watch_was_false_stage2_due_missing_PF_cashflow_bridge", "four_b_evidence_type": ["price_only", "positioning_overheat", "cashflow_balance_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_construction_beta_without_bridge", "current_profile_verdict": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L89_C30_005960_2024-02-01_5430", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "case_id": "R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "sector": "political_construction_event_premium", "primary_archetype": "political_construction_contract_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-15", "entry_date": "2024-03-15", "entry_price": 2690.0, "evidence_available_at_that_date": "political/construction contract-event premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["political_construction_theme", "contract_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv", "profile_path": "atlas/symbol_profiles/001/001470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.51, "MFE_90D_pct": 6.51, "MFE_180D_pct": 6.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -53.72, "MAE_90D_pct": -53.72, "MAE_180D_pct": -53.72, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 2865.0, "drawdown_after_peak_pct": -56.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_political_construction_event_cap", "four_b_evidence_type": ["event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L89_C30_001470_2024-03-15_2690", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L89_C30_ISDONGSEO_2024_HOUSING_PF_DISCOUNT_REPAIR_POSITIVE", "trigger_id": "R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR", "symbol": "010780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 50, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "housing_PF_discount_repair_positive", "MFE_90D_pct": 32.2, "MAE_90D_pct": -1.06, "score_return_alignment_label": "housing_PF_discount_repair_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "trigger_id": "R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "symbol": "005960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "construction_beta_false_stage2", "MFE_90D_pct": 1.29, "MAE_90D_pct": -11.79, "score_return_alignment_label": "construction_beta_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "trigger_id": "R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "symbol": "001470", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "political_construction_event_cap_4B_guard", "MFE_90D_pct": 6.51, "MAE_90D_pct": -53.72, "score_return_alignment_label": "political_construction_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "89", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_PF_DISCOUNT_REPAIR_VS_CONSTRUCTION_BETA_AND_POLITICAL_CONTRACT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["housing_PF_discount_repair_positive", "construction_beta_false_stage2", "political_construction_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R10
completed_loop = 89
next_round = R11
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
