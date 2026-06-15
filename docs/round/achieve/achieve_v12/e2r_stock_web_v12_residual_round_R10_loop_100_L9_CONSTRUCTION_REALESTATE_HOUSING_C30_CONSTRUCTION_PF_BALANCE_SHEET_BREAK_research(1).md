# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R10
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = CONSTRUCTION_PF_BALANCE_SHEET_SURVIVOR_REBOUND_VS_WEAK_LIQUIDITY_DECAY
output_file = e2r_stock_web_v12_residual_round_R10_loop_100_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are not re-proposed. This loop tests whether C30 needs a sharper Stage2 bridge: construction/PF names should not be promoted from “PF crisis relief” or low-PBR bargain vocabulary alone. The bridge must show solvency, order quality, margin/cash conversion, and absence of balance-sheet break.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R10 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | CONSTRUCTION_PF_BALANCE_SHEET_SURVIVOR_REBOUND_VS_WEAK_LIQUIDITY_DECAY |
| loop_objective | coverage_gap_fill / counterexample_mining / stage2_actionable_bonus_stress_test / 4B_non_price_requirement_stress_test / canonical_archetype_compression |

C30 maps to R10 / L9. This run is not an EPC mega-contract study and not a broad construction beta study. It compresses three deep sub-archetypes into one canonical question: when a PF/balance-sheet scare eases, which construction names are genuine survivors and which are simply weak-balance-sheet value traps?

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used:

| metric | value |
|---|---:|
| C30 existing rows | 3 |
| need to 30 | 27 |
| need to 50 | 47 |
| top existing symbols to avoid | 009410, 034300, 183190 |

This run avoids the existing C30 top-covered symbols and uses 000720, 047040, 002990.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

| symbol | company | profile path | shard path | corporate-action window |
|---:|---|---|---|---|
| 000720 | 현대건설 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | clean_180D_window |
| 047040 | 대우건설 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | clean_180D_window |
| 002990 | 금호건설 | atlas/symbol_profiles/002/002990.json | atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv | clean_180D_window |

## 5. Historical Eligibility Gate

| case_id | entry_date | entry_price | forward_window_trading_days | MFE/MAE 30/90/180 complete | calibration_usable |
|---|---:|---:|---:|---|---|
| C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR | 2024-01-26 | 33100 | 180 | yes | true |
| C30_R10L100_047040_DAEWOO_DELAYED_REBOUND | 2024-01-26 | 4015 | 180 | yes | true |
| C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY | 2024-01-26 | 5030 | 180 | yes | true |

## 6. Canonical Archetype Compression Map

| fine / deep sub-archetype | canonical_archetype_id | compression note |
|---|---|---|
| LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | A large builder can be Stage2 only if PF stress does not break the balance sheet and operating cash/margin evidence is not deteriorating. |
| BUILDER_POLICY_OR_VALUE_REBOUND_WITH_ORDER_MARGIN_BRIDGE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Rebound can be usable when policy/sector relief is paired with order quality and margin/cash visibility. |
| SMALL_BUILDER_WEAK_LIQUIDITY_DECAY_AFTER_PF_HEADLINE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Low-PBR/PF-relief vocabulary without liquidity and margin bridge is a value-trap/high-MAE counterexample. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR | 000720 | 현대건설 | structural_survivor | Stage2-Actionable | 2024-01-26 | 8.8 | -5.7 | current_profile_correct |
| C30_R10L100_047040_DAEWOO_DELAYED_REBOUND | 047040 | 대우건설 | missed_structural / delayed rebound | Stage2-Actionable | 2024-01-26 | 2.6 | -10.8 | current_profile_too_late |
| C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY | 002990 | 금호건설 | failed_rerating | Stage2-Actionable | 2024-01-26 | 5.0 | -27.5 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
```

This loop deliberately balances two survivor/rebound rows against one weak-liquidity decay row. The 047040 July spike is treated as a Stage4B overlay because the local peak was far ahead of the durable 180D path.

## 9. Evidence Source Map

| symbol | evidence source status | evidence summary |
|---:|---|---|
| 000720 | source_proxy_only / URL pending | Large-builder balance sheet and order/backlog quality helped separate survivor status from sector-wide PF fear. |
| 047040 | source_proxy_only / URL pending | Delayed rebound required more than PF relief; order quality and later policy/sector repricing mattered. |
| 002990 | source_proxy_only / URL pending | Weak-liquidity/small-builder PF vocabulary did not convert into durable margin or balance-sheet improvement. |

## 10. Price Data Source Map

| symbol | entry row source | 30/90/180 path source |
|---:|---|---|
| 000720 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | 2024 tradable shard |
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | 2024/2025 tradable shard for 4B overlay |
| 002990 | atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv | 2024 tradable shard |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_id | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label |
|---|---|---|---:|---:|---:|---|
| C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR | TRG_C30_R10L100_000720_STAGE2A_20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 33100 | large_builder_balance_sheet_survivor_low_mae |
| C30_R10L100_047040_DAEWOO_DELAYED_REBOUND | TRG_C30_R10L100_047040_STAGE2A_20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 4015 | builder_delayed_rebound_after_pf_relief |
| C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY | TRG_C30_R10L100_002990_STAGE2_FALSE_20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 5030 | weak_liquidity_pf_headline_false_stage2 |
| C30_R10L100_047040_DAEWOO_DELAYED_REBOUND | TRG_C30_R10L100_047040_STAGE4B_OVERLAY_20240718 | Stage4B | 2024-07-18 | 2024-07-18 | 4250 | price_spike_local_4b_watch_after_pf_rebound |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 000720 | Stage2-Actionable | 2024-01-26 | 33100 | 7.3 | -3.5 | 8.8 | -5.7 | 8.8 | -12.2 | 2024-05-09 | 36000 | -19.3 |
| 047040 | Stage2-Actionable | 2024-01-26 | 4015 | 2.6 | -5.6 | 2.6 | -10.8 | 23.7 | -12.3 | 2024-07-18 | 4965 | -29.1 |
| 002990 | Stage2-Actionable | 2024-01-26 | 5030 | 5.0 | -4.6 | 5.0 | -27.5 | 5.0 | -41.0 | 2024-02-01 | 5280 | -47.0 |
| 047040 | Stage4B | 2024-07-18 | 4250 | 16.8 | -16.6 | 16.8 | -17.2 | 16.8 | -30.8 | 2024-07-18 | 4965 | -40.8 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | interpretation |
|---|---|---|
| 000720 | current_profile_correct | C30 Stage2 can be acceptable for large-builder survivor rows, but MFE is modest; this is not a Green unlock. |
| 047040 | current_profile_too_late | The later rebound suggests Stage2/Yellows can miss delayed sector repair when balance-sheet break does not materialize. |
| 002990 | current_profile_false_positive | Low-price/PF-relief vocabulary without liquidity and margin bridge produced high MAE and prolonged decay. |

## 14. Stage2 / Yellow / Green Comparison

C30 should not relax Stage3-Green globally. The signal is a Stage2/Yellows bridge rule: survivor status is only valid when balance-sheet risk is bounded and order/margin/cash conversion is visible. Weak-liquidity builders should remain watch/reject even if the sector headline improves.

## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---:|---:|---:|---|---|
| 047040 | 1.0 | 1.0 | price_only / positioning_overheat | July 2024 construction rebound spike was a local full-window peak. Without non-price confirmation, treat as 4B-watch overlay. |

## 16. 4C Protection Audit

No hard 4C is proposed. 002990 is a Stage2 false positive / weak-liquidity decay row; it strengthens earlier balance-sheet-break watch, but this loop does not prove hard 4C routing timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = one canonical archetype in one large sector was tested; no L9-wide threshold change.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
scope = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Candidate rule:

```text
For C30, Stage2-Actionable requires at least two non-price bridges:
1. balance-sheet/PF exposure bounded or refinancing risk easing,
2. order backlog quality or project execution visibility,
3. margin / working-capital / cash-conversion improvement,
4. credible policy/sector repair that affects company cashflow.

If the row is only low-PBR / PF relief / bargain rebound vocabulary without company-level solvency and margin bridge, route to Stage1/weak-watch or Stage4B-watch if price already spiked.
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 5.5 | -14.7 | 0.33 | mixed |
| P2 C30 canonical guard profile | 3 | 5.7 accepted survivor/rebound / 5.0 rejected weak-liquidity | -8.3 accepted survivor/rebound / -27.5 rejected weak-liquidity | 0.00 after guard | improved |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR | 73 | Stage2-Actionable | 75 | Stage3-Yellow | 8.8 | -5.7 | stable_low_mae_positive |
| C30_R10L100_047040_DAEWOO_DELAYED_REBOUND | 69 | Stage2 | 76 | Stage3-Yellow | 2.6 | -10.8 | delayed_rebound_positive_180D |
| C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY | 66 | Stage2-Actionable | 54 | Stage1/weak-watch | 5.0 | -27.5 | false_positive_guard_needed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CONSTRUCTION_PF_BALANCE_SHEET_SURVIVOR_REBOUND_VS_WEAK_LIQUIDITY_DECAY | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 2 | false | true | 24 to 30 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - weak_liquidity_pf_headline_false_stage2
  - delayed_rebound_after_pf_relief
new_axis_proposed: null
existing_axis_strengthened:
  - C30_stage2_required_balance_sheet_cash_bridge
  - C30_local_4b_watch_guard_for_price_only_rebound_spike
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web 1D OHLCV path validation
- 30D / 90D / 180D MFE and MAE
- clean 180D corporate-action window check by symbol profile
- C30 canonical compression
- current calibrated profile stress test
```

Non-validation scope:

```text
- no live candidate scan
- no current recommendation
- no production scoring patch
- no broker/API action
- no stock_agent source-code inspection
- source URLs are pending and marked source_proxy_only
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_balance_sheet_cash_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Require balance-sheet/PF + cash/margin bridge before Stage2-Actionable","Rejected 002990 weak-liquidity false positive while keeping 000720/047040",TRG_C30_R10L100_000720_STAGE2A_20240125|TRG_C30_R10L100_047040_STAGE2A_20240125|TRG_C30_R10L100_002990_STAGE2_FALSE_20240125,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Construction rebound spike without non-price follow-through should be 4B-watch","047040 July spike led to large drawdown after local peak",TRG_C30_R10L100_047040_STAGE4B_OVERLAY_20240718,1,1,0,low,guardrail_shadow_only,"overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR","symbol":"000720","company_name":"현대건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE","case_type":"structural_survivor","positive_or_counterexample":"positive","best_trigger":"TRG_C30_R10L100_000720_STAGE2A_20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stable_low_mae_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"large-builder survivor row; modest MFE but low MAE"}
{"row_type":"case","case_id":"C30_R10L100_047040_DAEWOO_DELAYED_REBOUND","symbol":"047040","company_name":"대우건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"BUILDER_POLICY_OR_VALUE_REBOUND_WITH_ORDER_MARGIN_BRIDGE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"TRG_C30_R10L100_047040_STAGE2A_20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"delayed_rebound_positive_180D","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"rebound arrived after early PF relief; needs bridge rather than price-only chase"}
{"row_type":"case","case_id":"C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY","symbol":"002990","company_name":"금호건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_WEAK_LIQUIDITY_DECAY_AFTER_PF_HEADLINE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C30_R10L100_002990_STAGE2_FALSE_20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"PF relief vocabulary did not prevent high MAE and decay"}
{"row_type":"trigger","trigger_id":"TRG_C30_R10L100_000720_STAGE2A_20240125","case_id":"C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR","symbol":"000720","company_name":"현대건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":33100,"evidence_available_at_that_date":"source_proxy_only: large-builder balance-sheet survivor and order-quality bridge visible by Jan-2024","evidence_source":"source_proxy_only_url_pending","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.3,"MFE_90D_pct":8.8,"MFE_180D_pct":8.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.5,"MAE_90D_pct":-5.7,"MAE_180D_pct":-12.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":36000,"drawdown_after_peak_pct":-19.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"large_builder_balance_sheet_survivor_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_000720_20240126_33100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C30_R10L100_047040_STAGE2A_20240125","case_id":"C30_R10L100_047040_DAEWOO_DELAYED_REBOUND","symbol":"047040","company_name":"대우건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"BUILDER_POLICY_OR_VALUE_REBOUND_WITH_ORDER_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":4015,"evidence_available_at_that_date":"source_proxy_only: PF relief plus order/margin bridge partially visible; rebound confirmation lagged","evidence_source":"source_proxy_only_url_pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.6,"MFE_90D_pct":2.6,"MFE_180D_pct":23.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.6,"MAE_90D_pct":-10.8,"MAE_180D_pct":-12.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":4965,"drawdown_after_peak_pct":-29.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"builder_delayed_rebound_after_pf_relief","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_047040_20240126_4015","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C30_R10L100_002990_STAGE2_FALSE_20240125","case_id":"C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY","symbol":"002990","company_name":"금호건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_WEAK_LIQUIDITY_DECAY_AFTER_PF_HEADLINE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":5030,"evidence_available_at_that_date":"source_proxy_only: weak-liquidity builder exposed to PF/real-estate balance-sheet concern","evidence_source":"source_proxy_only_url_pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv","profile_path":"atlas/symbol_profiles/002/002990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.0,"MFE_90D_pct":5.0,"MFE_180D_pct":5.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.6,"MAE_90D_pct":-27.5,"MAE_180D_pct":-41.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":5280,"drawdown_after_peak_pct":-47.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"weak_liquidity_pf_headline_false_stage2","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_002990_20240126_5030","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C30_R10L100_047040_STAGE4B_OVERLAY_20240718","case_id":"C30_R10L100_047040_DAEWOO_DELAYED_REBOUND","symbol":"047040","company_name":"대우건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"BUILDER_POLICY_REBOUND_LOCAL_4B_WATCH","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":4250,"evidence_available_at_that_date":"price spike after construction/PF rebound vocabulary; non-price confirmation insufficient for full 4B production action","evidence_source":"source_proxy_only_url_pending","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.8,"MFE_90D_pct":16.8,"MFE_180D_pct":16.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.6,"MAE_90D_pct":-17.2,"MAE_180D_pct":-30.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":4965,"drawdown_after_peak_pct":-40.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_spike_local_4b_watch_after_pf_rebound","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_047040_20240718_4250","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same symbol as delayed rebound case but different trigger family: 4B timing overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L100_000720_HDEC_BALANCE_SHEET_SURVIVOR","trigger_id":"TRG_C30_R10L100_000720_STAGE2A_20240125","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":12,"margin_bridge_score":8,"revision_score":4,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":14,"margin_bridge_score":10,"revision_score":4,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"large-builder survivor row gets small bridge credit, not Green unlock","MFE_90D_pct":8.8,"MAE_90D_pct":-5.7,"score_return_alignment_label":"stable_low_mae_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"C30_R10L100_047040_DAEWOO_DELAYED_REBOUND","trigger_id":"TRG_C30_R10L100_047040_STAGE2A_20240125","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":-7,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":6,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"delayed rebound can be promoted to Yellow only after bridge improves","MFE_90D_pct":2.6,"MAE_90D_pct":-10.8,"score_return_alignment_label":"delayed_rebound_positive_180D","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY","trigger_id":"TRG_C30_R10L100_002990_STAGE2_FALSE_20240125","symbol":"002990","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":4,"valuation_repricing_score":6,"execution_risk_score":-10,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-4},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":-16,"legal_or_contract_risk_score":-10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-6},"weighted_score_after":54,"stage_label_after":"Stage1/weak-watch","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score","valuation_repricing_score"],"component_delta_explanation":"PF relief vocabulary without solvency and margin bridge is blocked","MFE_90D_pct":5.0,"MAE_90D_pct":-27.5,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate_metric","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_count":4,"representative_trigger_count":3,"calibration_usable_trigger_count":4,"positive_case_count":2,"counterexample_count":1,"four_b_case_count":1,"four_c_case_count":0,"avg_MFE_90D_pct":5.5,"avg_MAE_90D_pct":-14.7,"current_profile_error_count":2}
{"row_type":"residual_contribution","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["weak_liquidity_pf_headline_false_stage2","delayed_rebound_after_pf_relief"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 3
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
