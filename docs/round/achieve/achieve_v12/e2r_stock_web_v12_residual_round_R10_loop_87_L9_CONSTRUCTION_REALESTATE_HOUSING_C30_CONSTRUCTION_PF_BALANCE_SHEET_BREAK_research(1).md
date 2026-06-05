# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_87_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This loop adds 3 new independent C30 cases, 2 counterexamples, and 2 current-profile residual errors for R10 / L9 / C30.

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
scheduled_loop = 87
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 87
```

R10 is the construction / real-estate / PF credit round. The selected C30 fine split asks whether the same construction/PF bucket should treat all builders as red-watch credit risk, or whether it must distinguish:

```text
1. large-builder balance/cashflow repair positive,
2. sector beta / order-headline false Stage2,
3. parent-support event premium that belongs in 4B overlay rather than structural Green.
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

High-risk repeated C30 symbols in the index include `002990`, `294870`, `375500`, `004960`, `013580`, and `006360`. This loop avoids those and adds:

```text
000720 / Stage2-Actionable / 2025-01-22
047040 / Stage2-Actionable / 2024-01-02
034300 / Stage4B / 2024-02-07
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

| symbol | profile path | corporate-action status for selected window |
|---|---|---|
| 000720 | atlas/symbol_profiles/000/000720.json | clean modern window; CA candidates are 1998~2004 only |
| 047040 | atlas/symbol_profiles/047/047040.json | clean modern window; CA candidates are 2001/2003/2011 |
| 034300 | atlas/symbol_profiles/034/034300.json | 2024-02-06 CA before selected 2024-02-07 entry; selected forward window treated as clean after CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L87_C30_HDEC_2025_BALANCE_REPAIR_POSITIVE | 000720 | 2025-01-22 | yes | 180 | yes | yes | true |
| R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2 | 047040 | 2024-01-02 | yes | 180 | yes | yes | true |
| R10L87_C30_SSG_2024_PARENT_SUPPORT_EVENT_CAP_4B | 034300 | 2024-02-07 | yes | 180 | yes | yes-after-CA | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LARGE_BUILDER_BALANCE_REPAIR | PF discount can unwind when cashflow/backlog/order visibility is verified. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SECTOR_BETA_FALSE_STAGE2 | Construction beta or overseas-order headline alone is not enough for Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PARENT_SUPPORT_EVENT_CAP_4B | Parent support can create a strong event MFE but should be capped as 4B overlay unless durable cashflow repair appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L87_C30_HDEC_2025_BALANCE_REPAIR_POSITIVE | 000720 | 현대건설 | positive | Large-builder repair path with huge MFE and low early MAE. |
| R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2 | 047040 | 대우건설 | counterexample | Weak MFE / negative asymmetry despite construction beta. |
| R10L87_C30_SSG_2024_PARENT_SUPPORT_EVENT_CAP_4B | 034300 | 신세계건설 | counterexample / 4B | Event premium spike should be 4B overlay, not structural Green. |

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
| HDEC 2025 repair | historical public/report proxy | true | true | shadow-only positive |
| Daewoo 2024 beta | historical public/report proxy | true | true | shadow-only counterexample |
| SSG 2024 support/event cap | historical public/proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000720 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv | atlas/symbol_profiles/000/000720.json |
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | atlas/symbol_profiles/047/047040.json |
| 034300 | atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv | atlas/symbol_profiles/034/034300.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR | 000720 | Stage2-Actionable | 2025-01-22 | 28450 | positive | missed structural if all C30 is red-watch |
| R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA | 047040 | Stage2-Actionable | 2024-01-02 | 4170 | counterexample | false Stage2 if sector beta counts without cashflow bridge |
| R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP | 034300 | Stage4B | 2024-02-07 | 11460 | counterexample/4B | event premium cap, not structural Green |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR | 28450 | 31.99 | -9.14 | 149.91 | -9.14 | 199.12 | -9.14 | 2025-06-25 | 85100 | -36.43 |
| R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA | 4170 | 4.08 | -7.19 | 4.08 | -14.15 | 4.20 | -14.99 | 2024-07-16 | 4345 | -18.99 |
| R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP | 11460 | 11.52 | -9.16 | 62.74 | -14.05 | 62.74 | -14.05 | 2024-05-30 | 18650 | -37.32 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: require cashflow/balance repair evidence, not sector beta |
| local_4b_watch_guard | strengthen: parent support event premium should be 4B watch/cap |
| full_4b_requires_non_price_evidence | keep |
| hard_4c_thesis_break_routes_to_4c | keep, no new hard 4C row |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2 quality:

| symbol | Stage2 quality | explanation |
|---|---|---|
| 000720 | good_stage2 | Strong upside and low early drawdown after repair breakout. |
| 047040 | bad_stage2 | Construction beta did not produce enough MFE and had persistent MAE. |
| 034300 | not positive Stage2 | Event support belongs in 4B overlay due event-cap shape. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 034300 parent support event | 1.00 | 1.00 | good_full_window_4B_timing_but_event_cap_not_structural_green |
| 000720 fast 180D run | n/a | n/a | later valuation watch after structural Stage2 success |
| 047040 sector beta | 0.04 | 0.04 | weak MFE, not useful 4B |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = not_applicable
```

No hard 4C candidate is proposed. This loop deliberately avoids converting construction/PF stress into hard 4C unless non-price thesis-break evidence is durable.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF, Stage2 requires a verified balance/cashflow repair bridge. Large-builder repair can be positive, but sector beta or order headlines without cashflow/PF bridge remain watch-only.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should route parent-support / rescue / delisting-like event premiums to 4B overlay, not structural Green, while allowing verified large-builder balance repair into Stage2-Actionable.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 72.24 | -12.45 | 0.67 | mixed, needs C30 split |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 72.24 | -12.45 | 0.67 | weaker C30 separation |
| P1 sector_specific_candidate_profile | L9 repair bridge required | 2 | 77.00 | -11.65 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 split by repair/beta/event-cap | 2 | 77.00 | -11.65 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject beta + event-cap positive promotion | 1 | 149.91 | -9.14 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000720 repair | 66 | Stage2-Watch | 74 | Stage2-Actionable | 149.91 | -9.14 | positive_large_builder_repair |
| 047040 sector beta | 64 | Stage2-Actionable | 55 | Stage1/Watch | 4.08 | -14.15 | counterexample_sector_beta_false_stage2 |
| 034300 event cap | 68 | Stage3-Yellow-like | 58 | Stage4B-watch | 62.74 | -14.05 | event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds large-builder balance repair positive, sector-beta false Stage2, and parent-support event-cap 4B split for C30."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence
residual_error_types_found: large_builder_structural_repair_missed, sector_beta_false_stage2, parent_support_event_cap_not_structural_green
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
- C30 repair vs beta vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,refine_to_balance_cashflow_bridge,0,"C30 Stage2 must separate verified large-builder repair from sector beta/order headline","HDEC positive worked; Daewoo beta failed","R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR|R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA",2,2,1,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,keep_parent_support_event_cap_as_4B_watch,0,"Parent-support event premium can produce strong MFE but should not become structural Green without durable cashflow repair","SSG high MFE path was event-cap / delisting-like, not open-ended Green","R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP",1,1,1,low,guardrail_shadow_only,"event premium belongs in 4B overlay calibration"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L87_C30_HDEC_2025_BALANCE_REPAIR_POSITIVE", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Large-builder balance/PF discount repair with order/backlog and nuclear-policy visibility aligned with very strong 90D/180D MFE.", "current_profile_verdict": "current_profile_missed_structural_if_C30_treats_all_builders_as_credit_risk_only", "price_source": "Songdaiki/stock-web", "notes": "Positive path remains shadow-only because detailed point-in-time evidence URL verification is pending."}
{"row_type": "case", "case_id": "R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2-like sector beta and overseas-order expectation produced weak MFE and persistent MAE without a clean balance/cashflow repair bridge.", "current_profile_verdict": "current_profile_false_positive_if_stage2_required_bridge_ignores_PF_cashflow_gap", "price_source": "Songdaiki/stock-web", "notes": "Counterexample for large-builder headline/order beta without verified PF/cashflow bridge."}
{"row_type": "case", "case_id": "R10L87_C30_SSG_2024_PARENT_SUPPORT_EVENT_CAP_4B", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Parent-support / balance repair event created a sharp MFE, but the path behaved like event-premium cap / 4B overlay rather than open-ended structural Green.", "current_profile_verdict": "current_profile_4B_too_late_if_parent_support_event_cap_not_detected", "price_source": "Songdaiki/stock-web", "notes": "C30/C32 boundary case compressed into C30 because PF balance repair was the operating problem; event-premium guard is the residual finding."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR", "case_id": "R10L87_C30_HDEC_2025_BALANCE_REPAIR_POSITIVE", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "sector": "construction_large_builder", "primary_archetype": "large_builder_balance_repair_order_visibility", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-22", "entry_date": "2025-01-22", "entry_price": 28450.0, "evidence_available_at_that_date": "large-builder discount repair / order backlog / policy-project visibility proxy; exact as-of URLs pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["balance_repair_proxy", "order_backlog_visibility", "policy_project_visibility", "relative_strength_breakout"], "stage3_evidence_fields": ["confirmed_low_MAE_high_MFE_path", "sustained_order_visibility"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_fast_180D_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.99, "MFE_90D_pct": 149.91, "MFE_180D_pct": 199.12, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.14, "MAE_90D_pct": -9.14, "MAE_180D_pct": -9.14, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-25", "peak_price": 85100.0, "drawdown_after_peak_pct": -36.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "valuation_watch_after_fast_180D_run", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_large_builder_balance_repair_success", "current_profile_verdict": "current_profile_missed_structural_if_large_builder_repair_excluded_by_C30_red_watch", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L87_C30_HDEC_2025_2025-01-22_28450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "case_id": "R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "sector": "construction_large_builder", "primary_archetype": "sector_beta_order_headline_without_balance_repair", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 4170.0, "evidence_available_at_that_date": "construction sector rebound / overseas-order expectation proxy; exact as-of URLs pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["sector_beta_rebound", "order_headline_proxy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_follow_through", "PF_cashflow_bridge_missing"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.08, "MFE_90D_pct": 4.08, "MFE_180D_pct": 4.2, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.19, "MAE_90D_pct": -14.15, "MAE_180D_pct": -14.99, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-16", "peak_price": 4345.0, "drawdown_after_peak_pct": -18.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.04, "four_b_full_window_peak_proximity": 0.04, "four_b_timing_verdict": "sector_beta_stage2_false_positive_with_weak_MFE", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_weak_MFE_negative_asymmetry", "current_profile_verdict": "current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L87_C30_DAEWOO_2024_2024-01-02_4170", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP", "case_id": "R10L87_C30_SSG_2024_PARENT_SUPPORT_EVENT_CAP_4B", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "sector": "construction_parent_support", "primary_archetype": "parent_support_event_cap_4b", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 11460.0, "evidence_available_at_that_date": "PF/balance-sheet parent-support and capital/liquidity repair proxy; exact as-of URLs pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["parent_support_proxy", "liquidity_repair_proxy"], "stage3_evidence_fields": ["event_support_repricing"], "stage4b_evidence_fields": ["event_premium_cap", "low_float_support_spike", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.52, "MFE_90D_pct": 62.74, "MFE_180D_pct": 62.74, "MFE_1Y_pct": "insufficient_forward_window_in_stock_web_due_2025_inactive_or_delisted_like", "MFE_2Y_pct": "insufficient_forward_window_in_stock_web", "MAE_30D_pct": -9.16, "MAE_90D_pct": -14.05, "MAE_180D_pct": -14.05, "MAE_1Y_pct": "insufficient_forward_window_in_stock_web", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-30", "peak_price": 18650.0, "drawdown_after_peak_pct": -37.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_but_event_cap_not_structural_green", "four_b_evidence_type": ["capital_raise_or_overhang", "control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_parent_support_event_cap_not_detected", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2024-02-06_CA", "same_entry_group_id": "R10L87_C30_SSG_2024_2024-02-07_11460", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L87_C30_HDEC_2025_BALANCE_REPAIR_POSITIVE", "trigger_id": "R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR", "symbol": "000720", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 75, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 25, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "positive_large_builder_repair", "MFE_90D_pct": 149.91, "MAE_90D_pct": -9.14, "score_return_alignment_label": "positive_large_builder_repair", "current_profile_verdict": "current_profile_missed_structural_if_large_builder_repair_excluded_by_C30_red_watch"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "trigger_id": "R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 45, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "counterexample_sector_beta_false_stage2", "MFE_90D_pct": 4.08, "MAE_90D_pct": -14.15, "score_return_alignment_label": "counterexample_sector_beta_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L87_C30_SSG_2024_PARENT_SUPPORT_EVENT_CAP_4B", "trigger_id": "R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP", "symbol": "034300", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 35, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 35, "accounting_trust_risk_score": 10}, "weighted_score_before": 68, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 35, "revision_score": 20, "relative_strength_score": 40, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 70, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 58, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "event_cap_4B_guard", "MFE_90D_pct": 62.74, "MAE_90D_pct": -14.05, "score_return_alignment_label": "event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_parent_support_event_cap_not_detected"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_BALANCE_REPAIR_VS_PF_SECTOR_BETA_AND_PARENT_SUPPORT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["large_builder_structural_repair_missed", "sector_beta_false_stage2", "parent_support_event_cap_not_structural_green"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 87
next_round = R11
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
