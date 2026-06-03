# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
scheduled_round = R5
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = C19_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE
loop_objective = counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_rule_candidate
previous_round_state_basis = prior assistant output completed R4/loop71 -> next R5/loop71
output_file = e2r_stock_web_v12_residual_round_R5_loop_71_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
active_runtime_context = e2r_2_2_rolling_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_default_scoring_changed = false
```

The tested existing axes are `stage2_actionable_evidence_bonus`, `stage2_required_bridge`, and `local_4b_watch_guard`.  
The research conclusion is **existing_axis_strengthened**, not a new global axis.

## 2. Round / Large Sector / Canonical Archetype Scope

R5 is mapped to `L5_CONSUMER_BRAND_DISTRIBUTION`.  
The selected canonical archetype is `C19_BRAND_RETAIL_INVENTORY_MARGIN`.

C19 is the “retail shelf” archetype: a product can sit in the store and look abundant, but the model only earns credit when the shelf actually clears, margin survives discounting, and cash conversion follows. Price momentum without sell-through is treated like a display window, not a receipt.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot shows C19 already has meaningful coverage but is not as saturated as C20 and still has a balanced failure set: C19 has 89 rows, 17 symbols, good/bad S2 of 17/14, and 18/7 4B/4C rows. Top covered symbols listed there do not include `282330`, `139480`, or `071840`, so this loop adds three same-archetype new symbols.

```text
hard_duplicate_check = pass
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Source: `Songdaiki/stock-web`  
Price basis: `tradable_raw`  
Price adjustment: `raw_unadjusted_marcap`  
Manifest max date: `2026-02-20`  
Tradable shard root: `atlas/ohlcv_tradable_by_symbol_year`

The stock-web manifest records raw/unadjusted marcap OHLC, tradable row count 14,354,401, and manifest max date 2026-02-20. The schema defines MFE/MAE as max high / min low from entry through N tradable rows.

## 5. Historical Eligibility Gate

| symbol | profile path | entry row | 180D forward window | corporate action overlap | calibration usable |
|---|---|---|---|---|---|
| 282330 | atlas/symbol_profiles/282/282330.json | 2022-02-11 close 167,500 | pass | clean, profile has 0 corporate-action candidates | true |
| 139480 | atlas/symbol_profiles/139/139480.json | 2023-02-15 close 115,500 | pass | clean, profile has 0 corporate-action candidates | true |
| 071840 | atlas/symbol_profiles/071/071840.json | 2022-03-16 close 25,200 | pass | clean, profile has 0 corporate-action candidates | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| CONVENIENCE_RETAIL_SELLTHROUGH_MARGIN_BRIDGE | C19_BRAND_RETAIL_INVENTORY_MARGIN | convenience retail requires repeat traffic, sell-through, margin proof |
| BIGBOX_RETAIL_INVENTORY_MARGIN_FALSE_START | C19_BRAND_RETAIL_INVENTORY_MARGIN | big-box rebound fails when inventory/cash conversion is not confirmed |
| APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK | C19_BRAND_RETAIL_INVENTORY_MARGIN | durable goods retailer is inventory-cycle first |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | why selected |
|---|---|---|---|---|---|
| R5L71_C19_282330_CU_CONVENIENCE_SELLTHROUGH_20220211 | 282330 | BGF리테일 | structural_success | Stage2-Actionable | new C19 symbol; positive asymmetry with recurring convenience sell-through |
| R5L71_C19_139480_BIGBOX_MARGIN_FALSE_START_20230215 | 139480 | 이마트 | failed_rerating | Stage2 | new C19 symbol; reopen/valuation bounce failed as margin/inventory bridge broke |
| R5L71_C19_071840_APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK_20220316 | 071840 | 롯데하이마트 | failed_rerating | Stage2 | new C19 symbol; durable-goods demand normalization caused high MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
4B_or_4C_case_count = 2
counterexample_search_incomplete = false
```

## 9. Evidence Source Map

| symbol | evidence family | evidence status | source note |
|---|---|---|---|
| 282330 | recurring demand / sell-through / margin bridge | source proxy only | public earnings/report proxy; exact URL pending |
| 139480 | inventory-margin false start / weak cash conversion | source proxy only | public earnings/report proxy; exact URL pending |
| 071840 | appliance retail demand break / inventory risk | source proxy only | public retail-cycle proxy; exact URL pending |

Data-quality note: these rows are usable for stock-web price-path calibration, but source verification remains a promotion blocker until exact DART/report/news URLs are attached.

## 10. Price Data Source Map

| symbol | price shard | profile | entry_date | entry_price |
|---|---|---|---:|---:|
| 282330 | atlas/ohlcv_tradable_by_symbol_year/282/282330/2022.csv | atlas/symbol_profiles/282/282330.json | 2022-02-11 | 167,500 |
| 139480 | atlas/ohlcv_tradable_by_symbol_year/139/139480/2023.csv | atlas/symbol_profiles/139/139480.json | 2023-02-15 | 115,500 |
| 071840 | atlas/ohlcv_tradable_by_symbol_year/071/071840/2022.csv | atlas/symbol_profiles/071/071840.json | 2022-03-16 | 25,200 |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| 282330 | Stage2-Actionable | 167,500 | +21.79% | -5.07% | +21.79% | -8.96% | current_profile_correct |
| 139480 | Stage2 | 115,500 | +3.81% | -34.11% | +3.81% | -41.13% | current_profile_false_positive |
| 071840 | Stage2 | 25,200 | +1.19% | -35.71% | +1.19% | -51.98% | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | peak_date | peak_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | drawdown_after_peak |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 282330 | 2022-02-11 | 167,500 | 2022-05-16 | 204,000 | +10.75 | -5.07 | +21.79 | -5.07 | +21.79 | -8.96 | -25.25 |
| 139480 | 2023-02-15 | 115,500 | 2023-02-23 | 119,900 | +3.81 | -11.26 | +3.81 | -34.11 | +3.81 | -41.13 | -43.29 |
| 071840 | 2022-03-16 | 25,200 | 2022-03-17 | 25,450 | +1.19 | -6.55 | +1.19 | -35.71 | +1.19 | -51.98 | -52.46 |

## 13. Current Calibrated Profile Stress Test

1. current calibrated profile would keep 282330 as Stage2-Actionable, and that aligns with MFE/MAE.
2. current calibrated profile can over-promote 139480/071840 if price rebound or low valuation is treated as evidence without sell-through/cash conversion.
3. Stage2 bonus is appropriate only when paired with non-price retail proof.
4. Yellow threshold is not the issue in this loop.
5. Green strictness is appropriate; no Green should be relaxed.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement remains appropriate.
8. hard 4C routing was too late for the two failed retail cases.

Conclusion: `existing_axis_strengthened`.

## 14. Stage2 / Yellow / Green Comparison

C19 Stage2 should require at least one of:

- sell-through or traffic proof,
- inventory normalization without discount-driven margin damage,
- gross/operating margin bridge,
- cash conversion or working-capital stability.

If the only evidence is relative strength, reopen narrative, valuation bounce, or one-quarter noise, Stage2 should stay at Watch.

## 15. 4B Local vs Full-window Timing Audit

The two failed cases show a repeated pattern: price local highs formed early, but non-price evidence of margin/inventory weakness arrived later. Price-only 4B is still too early as a full 4B, but useful as local watch. Thus `local_4b_watch_guard` is strengthened, not weakened.

## 16. 4C Protection Audit

| symbol | 4C label | interpretation |
|---|---|---|
| 139480 | hard_4c_late | thesis break became obvious after the entry already suffered high MAE |
| 071840 | hard_4c_late | appliance demand/inventory break should have been watched before severe drawdown |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = only one canonical archetype inside L5 was tested in this loop
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C19_BRAND_RETAIL_INVENTORY_MARGIN
rule = C19 Stage2 requires sell-through/inventory/cash-conversion bridge; price/reopen valuation rebound alone must remain Stage1/Watch.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive count | missed structural count |
|---|---:|---:|---:|---:|---:|
| P0 e2r_2_1 proxy | 3 | 8.93 | -24.96 | 2 | 0 |
| P2 C19 bridge guard | 1 selected positive + 2 demoted watches | 21.79 selected | -5.07 selected | 0 | 0 |

## 20. Score-Return Alignment Matrix

| symbol | before score | before stage | after score | after stage | alignment |
|---|---:|---|---:|---|---|
| 282330 | 71 | Stage2-Actionable | 73 | Stage2-Actionable | aligned_positive |
| 139480 | 68 | Stage2 | 58 | Stage1/Watch | false_positive_removed |
| 071840 | 66 | Stage2 | 54 | Stage1/Watch | false_positive_removed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE | 1 | 2 | 2 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | evidence URL/proxy quality remains gap |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | stage2_required_bridge | local_4b_watch_guard
residual_error_types_found: stage2_false_positive_from_price_reopen_narrative | high_mae_inventory_margin_break | late_4c_after_retail_thesis_break
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min | full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web OHLC rows,
- entry date and entry price,
- 30D/90D/180D MFE/MAE proxy calculations,
- clean corporate-action window by profile candidate dates,
- no-repeat novelty against top covered C19 symbols.

Not validated:

- exact DART/news/report URLs,
- full production parser extraction,
- 1Y/2Y metrics.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,require_sellthrough_inventory_cash_conversion_bridge,+guardrail,"C19 positive path had recurring sell-through/margin evidence; two counterexamples had price/reopen narratives but no inventory/cash conversion proof and suffered high MAE.","avg_MFE90=8.93 avg_MAE90=-24.96; guard demotes 2 false starts while preserving 282330","R5L71_C19_282330_STAGE2A_20220211|R5L71_C19_139480_STAGE2_FALSE_START_20230215|R5L71_C19_071840_STAGE2_FALSE_START_20220316",3,3,2,low_medium,canonical_shadow_only,"not production; evidence URLs pending"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "Stage2-Actionable / 2022-02-11 close", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_282330_CU_CONVENIENCE_SELLTHROUGH_20220211", "case_type": "structural_success", "company_name": "BGF리테일", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "CONVENIENCE_RETAIL_SELLTHROUGH_MARGIN_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "notes": "편의점 traffic/sell-through와 점포망 방어력이 가격경로를 설명한 positive C19 holdout.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "good_stage2_positive_asymmetry_but_not_green_unlock", "symbol": "282330"}
{"best_trigger": "Stage2 / 2023-02-15 close", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_139480_BIGBOX_MARGIN_FALSE_START_20230215", "case_type": "failed_rerating", "company_name": "이마트", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "BIGBOX_RETAIL_INVENTORY_MARGIN_FALSE_START", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "notes": "대형마트/온라인 적자/재고·마진 개선 미확인 상태의 반등은 C19 Stage2 bridge로 쓰면 안 되는 반례.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "bad_stage2_high_mae", "symbol": "139480"}
{"best_trigger": "Stage2 / 2022-03-16 close", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_071840_APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK_20220316", "case_type": "failed_rerating", "company_name": "롯데하이마트", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "notes": "가전 리테일은 COVID 내구재 수요 이후 inventory/demand break가 발생하면 early price/reopen signal을 Stage2로 승격하면 안 됨.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R5", "row_type": "case", "score_price_alignment": "bad_stage2_high_mae", "symbol": "071840"}
{"MAE_180D_pct": -8.96, "MAE_1Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -5.07, "MAE_90D_pct": -5.07, "MFE_180D_pct": 21.79, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MFE_30D_pct": 10.75, "MFE_90D_pct": 21.79, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_282330_CU_CONVENIENCE_SELLTHROUGH_20220211", "company_name": "BGF리테일", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -25.25, "entry_date": "2022-02-11", "entry_price": 167500, "evidence_available_at_that_date": "public earnings / convenience-store sell-through proxy available by result window; exact URL pending", "evidence_source": "public_earnings_report_proxy", "evidence_url_pending": true, "fine_archetype_id": "CONVENIENCE_RETAIL_SELLTHROUGH_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": null, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": null, "four_c_protection_label": null, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "loop_objective": "holdout_validation|canonical_archetype_rule_candidate", "peak_date": "2022-05-16", "peak_price": 204000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/282/282330/2022.csv", "primary_archetype": "brand_retail_sellthrough_margin", "profile_path": "atlas/symbol_profiles/282/282330.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L71_C19_282330_20220211_167500", "sector": "consumer_retail_convenience", "source_proxy_only": true, "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "recurring_consumer_demand", "sellthrough_or_store_traffic"], "stage3_evidence_fields": ["financial_visibility", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "282330", "trigger_date": "2022-02-10", "trigger_id": "R5L71_C19_282330_STAGE2A_20220211", "trigger_outcome_label": "good_stage2_positive_asymmetry", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -41.13, "MAE_1Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -11.26, "MAE_90D_pct": -34.11, "MFE_180D_pct": 3.81, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MFE_30D_pct": 3.81, "MFE_90D_pct": 3.81, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_139480_BIGBOX_MARGIN_FALSE_START_20230215", "company_name": "이마트", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.29, "entry_date": "2023-02-15", "entry_price": 115500, "evidence_available_at_that_date": "earnings-turnaround / retail-reopening narrative without confirmed sell-through and cash conversion; exact URL pending", "evidence_source": "public_earnings_report_proxy", "evidence_url_pending": true, "fine_archetype_id": "BIGBOX_RETAIL_INVENTORY_MARGIN_FALSE_START", "forward_window_trading_days": 180, "four_b_evidence_type": "price_only|margin_or_backlog_slowdown", "four_b_full_window_peak_proximity": 0.13, "four_b_local_peak_proximity": 0.13, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_c_protection_label": "hard_4c_late", "green_lateness_ratio": "not_applicable_false_start", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "loop_objective": "counterexample_mining|stage2_actionable_bonus_stress_test", "peak_date": "2023-02-23", "peak_price": 119900, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139480/2023.csv", "primary_archetype": "inventory_margin_false_start", "profile_path": "atlas/symbol_profiles/139/139480.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L71_C19_139480_20230215_115500", "sector": "consumer_retail_bigbox", "source_proxy_only": true, "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken", "cashflow_or_margin_deterioration"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "139480", "trigger_date": "2023-02-14", "trigger_id": "R5L71_C19_139480_STAGE2_FALSE_START_20230215", "trigger_outcome_label": "failed_rerating_high_mae", "trigger_type": "Stage2"}
{"MAE_180D_pct": -51.98, "MAE_1Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -6.55, "MAE_90D_pct": -35.71, "MFE_180D_pct": 1.19, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MFE_30D_pct": 1.19, "MFE_90D_pct": 1.19, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_071840_APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK_20220316", "company_name": "롯데하이마트", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.46, "entry_date": "2022-03-16", "entry_price": 25200, "evidence_available_at_that_date": "post-COVID durable-goods demand normalization risk visible through appliance-retail cycle; exact URL pending", "evidence_source": "public_retail_cycle_proxy", "evidence_url_pending": true, "fine_archetype_id": "APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK", "forward_window_trading_days": 180, "four_b_evidence_type": "price_only|margin_or_backlog_slowdown", "four_b_full_window_peak_proximity": 0.04, "four_b_local_peak_proximity": 0.04, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_c_protection_label": "hard_4c_late", "green_lateness_ratio": "not_applicable_false_start", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "loop_objective": "counterexample_mining|stage2_actionable_bonus_stress_test|4C_thesis_break_timing_test", "peak_date": "2022-03-17", "peak_price": 25450, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071840/2022.csv", "primary_archetype": "durable_goods_inventory_break", "profile_path": "atlas/symbol_profiles/071/071840.json", "reuse_reason": null, "round": "R5", "row_type": "trigger", "same_entry_group_id": "R5L71_C19_071840_20220316_25200", "sector": "consumer_appliance_retail", "source_proxy_only": true, "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken", "inventory_demand_break"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "071840", "trigger_date": "2022-03-15", "trigger_id": "R5L71_C19_071840_STAGE2_FALSE_START_20220316", "trigger_outcome_label": "failed_rerating_high_mae", "trigger_type": "Stage2"}
{"MAE_90D_pct": -5.07, "MFE_90D_pct": 21.79, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_282330_CU_CONVENIENCE_SELLTHROUGH_20220211", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C19 needs verified sell-through, inventory normalization and cash conversion before Stage2 promotion; price-only/reopen relative strength is insufficient.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "contract_score": 0, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "margin_bridge_score": 60, "policy_or_regulatory_score": 0, "relative_strength_score": 60, "revision_score": 55, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "contract_score": 0, "customer_quality_score": 65, "dilution_cb_risk_score": 0, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "margin_bridge_score": 55, "policy_or_regulatory_score": 0, "relative_strength_score": 60, "revision_score": 55, "valuation_repricing_score": 45}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_positive", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2-Actionable", "symbol": "282330", "trigger_id": "R5L71_C19_282330_STAGE2A_20220211", "weighted_score_after": 73, "weighted_score_before": 71}
{"MAE_90D_pct": -34.11, "MFE_90D_pct": 3.81, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_139480_BIGBOX_MARGIN_FALSE_START_20230215", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C19 needs verified sell-through, inventory normalization and cash conversion before Stage2 promotion; price-only/reopen relative strength is insufficient.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "contract_score": 0, "customer_quality_score": 15, "dilution_cb_risk_score": 0, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "margin_bridge_score": 20, "policy_or_regulatory_score": 0, "relative_strength_score": 70, "revision_score": 35, "valuation_repricing_score": 55}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "contract_score": 0, "customer_quality_score": 25, "dilution_cb_risk_score": 0, "execution_risk_score": 65, "legal_or_contract_risk_score": 0, "margin_bridge_score": 35, "policy_or_regulatory_score": 0, "relative_strength_score": 70, "revision_score": 35, "valuation_repricing_score": 55}, "row_type": "score_simulation", "score_return_alignment_label": "score_overstated_by_price_and_reopen_narrative", "stage_label_after": "Stage1/Watch", "stage_label_before": "Stage2", "symbol": "139480", "trigger_id": "R5L71_C19_139480_STAGE2_FALSE_START_20230215", "weighted_score_after": 58, "weighted_score_before": 68}
{"MAE_90D_pct": -35.71, "MFE_90D_pct": 1.19, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "R5L71_C19_071840_APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK_20220316", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C19 needs verified sell-through, inventory normalization and cash conversion before Stage2 promotion; price-only/reopen relative strength is insufficient.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "contract_score": 0, "customer_quality_score": 10, "dilution_cb_risk_score": 0, "execution_risk_score": 85, "legal_or_contract_risk_score": 0, "margin_bridge_score": 15, "policy_or_regulatory_score": 0, "relative_strength_score": 65, "revision_score": 25, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 0, "contract_score": 0, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "margin_bridge_score": 25, "policy_or_regulatory_score": 0, "relative_strength_score": 65, "revision_score": 25, "valuation_repricing_score": 45}, "row_type": "score_simulation", "score_return_alignment_label": "stage2_should_be_blocked_by_inventory_demand_break", "stage_label_after": "Stage1/Watch", "stage_label_before": "Stage2", "symbol": "071840", "trigger_id": "R5L71_C19_071840_STAGE2_FALSE_START_20220316", "weighted_score_after": 54, "weighted_score_before": 66}
{"axis": "stage2_required_bridge", "backtest_effect": "selected three representative Stage2 triggers: avg_MFE90=8.93, avg_MAE90=-24.96; guard would demote 2 false starts while preserving BGF Retail as Stage2-Actionable.", "baseline_value": 0, "calibration_usable_count": 3, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "confidence": "low_medium", "counterexample_count": 2, "delta": "+guardrail", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "new_independent_case_count": 3, "notes": "not production; source_proxy_only/evidence_url_pending must be cleared before promotion", "proposal_type": "canonical_shadow_only", "reason": "C19 positive path had recurring sell-through/margin evidence; two counterexamples had price/reopen narratives but no inventory/cash conversion proof and suffered high MAE.", "row_type": "shadow_weight", "scope": "canonical_archetype_specific", "tested_value": "require_sellthrough_inventory_cash_conversion_bridge", "trigger_ids": "R5L71_C19_282330_STAGE2A_20220211|R5L71_C19_139480_STAGE2_FALSE_START_20230215|R5L71_C19_071840_STAGE2_FALSE_START_20220316"}
{"canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "do_not_propose_new_weight_delta": false, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "loop": "71", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 3, "new_symbol_count": 3, "new_trigger_family_count": 3, "residual_error_types_found": ["stage2_false_positive_from_price_reopen_narrative", "high_mae_inventory_margin_break", "late_4c_after_retail_thesis_break"], "reused_case_count": 0, "round": "R5", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage2_required_bridge", "local_4b_watch_guard"]}
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
completed_round = R5
completed_loop = 71
next_round = R6
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest: max date 2026-02-20, price adjustment status raw_unadjusted_marcap, calibration shard root atlas/ohlcv_tradable_by_symbol_year.
- `282330` profile: no corporate-action candidates.
- `139480` profile: no corporate-action candidates.
- `071840` profile: no corporate-action candidates.
- Evidence URLs are pending; this MD is intended as shadow-only residual calibration until exact source URLs are attached.
