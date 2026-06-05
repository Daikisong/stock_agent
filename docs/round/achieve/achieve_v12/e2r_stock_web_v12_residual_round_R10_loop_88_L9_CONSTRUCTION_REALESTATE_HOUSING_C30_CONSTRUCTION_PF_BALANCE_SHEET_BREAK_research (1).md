# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_88_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This loop continues loop 88 after R9. It adds 3 C30 construction/PF cases: one regional housing/PF repair positive, one infra-contract beta false Stage2, and one post-workout 4B event-cap counterexample.

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
scheduled_loop = 88
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 88
```

R10 is the L9 construction/PF round. This loop avoids the top repeated C30 symbols and avoids the previous R10 loop-87 symbols. The purpose is to sharpen the distinction between actual PF/cashflow repair and construction beta / workout event premium.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK = 81 rows / 31 symbols / good-bad Stage2 16-29 / 4B-4C 3-4
top covered symbols include 002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4)
previous loop-87 symbols avoided: 000720, 047040, 034300
```

Selected rows:

```text
035890 / Stage2-Actionable / 2024-08-05
028100 / Stage2-Actionable / 2024-01-30
009410 / Stage4B / 2025-03-21
```

The 009410 2023-12 PF-crisis path is not used as the representative calibration row because 2024 contains a trading gap and a 2024-10-31 raw discontinuity / corporate-action candidate. This file uses only the post-CA 2025 workout-event path with reduced evidence weight.

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
| 035890 | atlas/symbol_profiles/035/035890.json | selected 2024 window clean; CA candidates are 2012 or earlier |
| 028100 | atlas/symbol_profiles/028/028100.json | selected 2024 window clean; CA candidate is 2022-02-21 |
| 009410 | atlas/symbol_profiles/009/009410.json | 2023/2024 crisis path blocked; selected 2025 path is post-2024-10-31 CA/discontinuity |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L88_C30_SEOHEE_2024_REGIONAL_HOUSING_PF_REPAIR_POSITIVE | 035890 | 2024-08-05 | yes | 180 | yes | yes | true |
| R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2 | 028100 | 2024-01-30 | yes | 180 | yes | yes | true |
| R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B | 009410 | 2025-03-21 | yes | 180 | yes | post-CA | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REGIONAL_HOUSING_PF_REPAIR | Positive Stage2 requires PF/cashflow/balance repair after sector de-risking. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | TUNNELING_CONTRACT_FALSE_STAGE2 | Contract or infra beta without balance/cashflow bridge can be false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | WORKOUT_EVENT_CAP_4B | Workout/restructuring premium can cap quickly and belongs in 4B overlay. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L88_C30_SEOHEE_2024_REGIONAL_HOUSING_PF_REPAIR_POSITIVE | 035890 | 서희건설 | positive | Post-sector-shock PF repair path had low MAE and steady MFE. |
| R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2 | 028100 | 동아지질 | counterexample | Infra/tunneling contract spike had weak MFE and material MAE. |
| R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B | 009410 | 태영건설 | counterexample / 4B | Workout premium rallied and then faded; not structural Green evidence. |

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
| Seohee PF repair | historical public/report proxy | true | true | shadow-only positive |
| Dong-Ah contract beta | historical public/news proxy | true | true | false-Stage2 guardrail |
| Taeyoung workout event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 035890 | atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv; 2025.csv | atlas/symbol_profiles/035/035890.json |
| 028100 | atlas/ohlcv_tradable_by_symbol_year/028/028100/2024.csv | atlas/symbol_profiles/028/028100.json |
| 009410 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2025.csv | atlas/symbol_profiles/009/009410.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR | 035890 | Stage2-Actionable | 2024-08-05 | 1227 | positive | PF/cashflow repair bridge worked |
| R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA | 028100 | Stage2-Actionable | 2024-01-30 | 14980 | counterexample | infra contract beta false Stage2 |
| R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP | 009410 | Stage4B | 2025-03-21 | 3215 | counterexample/4B | workout event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR | 1227 | 24.21 | -3.01 | 32.11 | -3.01 | 32.27 | -3.01 | 2024-10-10 | 1621 | -13.51 |
| R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA | 14980 | 4.27 | -14.22 | 4.27 | -16.56 | 4.27 | -24.37 | 2024-01-30 | 15620 | -25.80 |
| R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP | 3215 | 26.91 | -28.46 | 26.91 | -42.30 | 26.91 | -44.82 | 2025-03-21 | 4080 | -45.54 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs PF/cashflow/balance repair bridge |
| local_4b_watch_guard | strengthen: contract beta and workout event premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 035890 | good_stage2 | PF repair path produced low drawdown and steady rerating. |
| 028100 | bad_stage2 | Contract beta was not enough without cashflow/balance bridge. |
| 009410 | good_4B | Workout premium was event-capped and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 028100 contract beta | 1.00 | 1.00 | contract_beta_spike_was_event_cap_false_stage2 |
| 009410 workout event cap | 1.00 | 1.00 | good_full_window_4B_timing_workout_event_premium_cap |
| 035890 PF repair | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 028100 / 009410
```

No hard 4C candidate is proposed. R10 loop 88 is about Stage2 bridge quality and 4B event-cap timing, not new hard thesis-break promotion.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF cases, Stage2 requires verified PF, cashflow, debt maturity, or balance-sheet repair bridge. Contract headlines, infrastructure beta, and workout/restructuring event premiums remain watch/4B unless the repair bridge is durable.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split real PF/cashflow repair positives from construction-contract false Stage2 and workout event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 21.10 | -20.62 | 0.67 | mixed; C30 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 21.10 | -20.62 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/cashflow repair required | 2 | 18.19 | -9.79 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 repair vs beta/event-cap split | 2 | 18.19 | -9.79 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject contract/workout caps as positive | 1 | 32.11 | -3.01 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 035890 PF repair | 66 | Stage2-Watch | 73 | Stage2-Actionable | 32.11 | -3.01 | regional_housing_PF_cashflow_repair_positive |
| 028100 contract beta | 65 | Stage2-Actionable | 55 | Stage1/Watch | 4.27 | -16.56 | contract_beta_without_cashflow_bridge_false_stage2 |
| 009410 workout cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 26.91 | -42.30 | workout_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 regional housing/PF repair positive, infra-contract beta false Stage2, and post-workout event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: regional_housing_PF_repair_positive, infra_contract_beta_false_stage2, workout_event_cap_4B
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
- C30 PF/cashflow repair vs contract beta / workout event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_PF_cashflow_balance_bridge,0,"C30 Stage2 should require PF/cashflow/balance repair bridge, not construction beta, contract headline, or workout event premium alone","Seohee positive worked; Dong-Ah and Taeyoung event/beta rows failed positive-stage promotion","R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR|R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA|R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_contract_beta_and_workout_event_premium_as_4B_watch,0,"Infra-contract and workout event premiums can peak before durable PF/cashflow repair appears","Dong-Ah and Taeyoung showed weak/asymmetric forward paths after event or beta spikes","R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA|R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L88_C30_SEOHEE_2024_REGIONAL_HOUSING_PF_REPAIR_POSITIVE", "symbol": "035890", "company_name": "서희건설", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional housing/PF discount repair worked when the entry was after forced sector de-risking and later price path showed low MAE with steady MFE.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_PF_cashflow_repair_not_construction_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of PF/cashflow repair evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2", "symbol": "028100", "company_name": "동아지질", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Tunneling/infra contract beta spike had weak forward MFE and material MAE; C30 should not treat contract headline as PF/balance repair.", "current_profile_verdict": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "New C30 infra-construction symbol; source-proxy only."}
{"row_type": "case", "case_id": "R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "2023-12 PF crisis / 2024-10 raw discontinuity window was blocked; this row uses post-CA 2025 workout-event path only.", "independent_evidence_weight": 0.5, "score_price_alignment": "Workout/restructuring premium rallied sharply and then faded; post-workout event premium belongs in 4B overlay unless durable balance/cashflow repair is confirmed.", "current_profile_verdict": "current_profile_4B_too_late_if_workout_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Reduced evidence weight because earlier PF-crisis window is corporate-action/discontinuity blocked; selected 2025 post-CA row is overlay-only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR", "case_id": "R10L88_C30_SEOHEE_2024_REGIONAL_HOUSING_PF_REPAIR_POSITIVE", "symbol": "035890", "company_name": "서희건설", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "sector": "regional_housing_construction_PF", "primary_archetype": "regional_housing_PF_cashflow_repair", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-05", "entry_date": "2024-08-05", "entry_price": 1227.0, "evidence_available_at_that_date": "regional housing / PF discount repair and cashflow stability proxy after sector de-risking; exact as-of URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["PF_discount_repair_proxy", "cashflow_stability_proxy", "post_sector_shock_recovery", "relative_strength_reversal"], "stage3_evidence_fields": ["low_MAE_recovery_path", "steady_MFE90"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_repair_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv|atlas/ohlcv_tradable_by_symbol_year/035/035890/2025.csv", "profile_path": "atlas/symbol_profiles/035/035890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.21, "MFE_90D_pct": 32.11, "MFE_180D_pct": 32.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.01, "MAE_90D_pct": -3.01, "MAE_180D_pct": -3.01, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-10", "peak_price": 1621.0, "drawdown_after_peak_pct": -13.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed_after_PF_repair_run", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_regional_housing_PF_repair_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L88_C30_035890_2024-08-05_1227", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "case_id": "R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2", "symbol": "028100", "company_name": "동아지질", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "sector": "civil_engineering_tunneling_contract", "primary_archetype": "infra_contract_beta_without_balance_repair", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-30", "entry_date": "2024-01-30", "entry_price": 14980.0, "evidence_available_at_that_date": "tunneling / infrastructure contract beta spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["infra_contract_headline", "relative_strength_spike", "construction_beta"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "cashflow_balance_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028100/2024.csv", "profile_path": "atlas/symbol_profiles/028/028100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.27, "MFE_90D_pct": 4.27, "MFE_180D_pct": 4.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.22, "MAE_90D_pct": -16.56, "MAE_180D_pct": -24.37, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 15620.0, "drawdown_after_peak_pct": -25.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "contract_beta_spike_was_event_cap_false_stage2", "four_b_evidence_type": ["price_only", "positioning_overheat", "contract_headline_without_margin_bridge"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_contract_beta_false_positive", "current_profile_verdict": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L88_C30_028100_2024-01-30_14980", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "case_id": "R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "sector": "construction_workout_PF_restructuring", "primary_archetype": "post_workout_event_premium_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2025-03-21", "entry_date": "2025-03-21", "entry_price": 3215.0, "evidence_available_at_that_date": "post-workout restructuring / PF balance repair event premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["workout_event_premium", "PF_restructuring_headline", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "post_peak_drawdown", "balance_repair_uncertainty"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2025.csv", "profile_path": "atlas/symbol_profiles/009/009410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.91, "MFE_90D_pct": 26.91, "MFE_180D_pct": 26.91, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.46, "MAE_90D_pct": -42.3, "MAE_180D_pct": -44.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-21", "peak_price": 4080.0, "drawdown_after_peak_pct": -45.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_workout_event_premium_cap", "four_b_evidence_type": ["event_premium", "positioning_overheat", "balance_repair_uncertainty"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_workout_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-10-31_CA_window", "same_entry_group_id": "R10L88_C30_009410_2025-03-21_3215", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "post-CA workout event-cap overlay; earlier 2023-12 crisis path blocked by 2024-10-31 corporate-action/discontinuity candidate", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L88_C30_SEOHEE_2024_REGIONAL_HOUSING_PF_REPAIR_POSITIVE", "trigger_id": "R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR", "symbol": "035890", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 50, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "regional_housing_PF_cashflow_repair_positive", "MFE_90D_pct": 32.11, "MAE_90D_pct": -3.01, "score_return_alignment_label": "regional_housing_PF_cashflow_repair_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2", "trigger_id": "R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "symbol": "028100", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 65, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "contract_beta_without_cashflow_bridge_false_stage2", "MFE_90D_pct": 4.27, "MAE_90D_pct": -16.56, "score_return_alignment_label": "contract_beta_without_cashflow_bridge_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "trigger_id": "R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "workout_event_cap_4B_guard", "MFE_90D_pct": 26.91, "MAE_90D_pct": -42.3, "score_return_alignment_label": "workout_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_workout_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "88", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REGIONAL_HOUSING_PF_REPAIR_VS_TUNNELING_CONTRACT_FALSE_STAGE2_AND_WORKOUT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["regional_housing_PF_repair_positive", "infra_contract_beta_false_stage2", "workout_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R10L88_C30_TAEYOUNG_2023_BLOCKED","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"2023-12 PF-crisis path was inspected but not used because 2024 contains trading gap and 2024-10-31 corporate-action/discontinuity candidate; replaced by post-CA 2025 overlay row","price_source":"Songdaiki/stock-web","usage":"blocked_context_not_weight_calibration"}
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
completed_loop = 88
next_round = R11
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
