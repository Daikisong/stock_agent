# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R2
selected_loop = 98
selection_basis = docs/core/V12_Research_No_Repeat_Index.md Priority 0
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_filename = e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
```

This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
active_runtime_profile = e2r_2_2_rolling_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

C09 is not a structural-Green unlock by itself. It is a valuation/positioning blowoff lane inside L2 semiconductor equipment, where price-only strength must be separated from customer qualification, order intake, revenue conversion, margin bridge, and EPS/FCF revision. The practical mechanism is a pressure valve: when a test/probe/equipment stock rallies like steam escaping from a boiler, the system must ask whether there is a real pipe of order/margin conversion behind it. If not, Stage2 should become a watch/risk overlay, not a positive rerating.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R2`
- selected_loop: `98`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`
- fine_archetype_id: `TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE`

Scope is valid because R2 maps to L2, and C09 maps to AI/semiconductor/electronics advanced equipment valuation blowoff.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index shows C09 at only 15 rows, still Priority 0 and 15 rows short of the 30-row minimum stability zone. The new cases deliberately use a C09 valuation-blowoff framing rather than repeating a C08 customer-quality/socket thesis.

Duplicate gate:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
session_previous_output = R2 loop 97 C08
this_output = R2 loop 98 C09
new_independent_case_count = 4
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-Web shard columns used: `d,o,h,l,c,v,a,mc,s,m`.

## 5. Historical Eligibility Gate

All selected entries are from 2024, have tradable close rows, positive OHLCV, and at least 180 forward trading days before the 2026-02-20 manifest max date. Corporate-action candidate dates in symbol profiles do not fall inside the 2024 180D windows for these selected entries. The rows are usable for historical calibration but blocked for promotion because non-price evidence is source-proxy-only.

## 6. Canonical Archetype Compression Map

| source theme | compressed canonical | reason |
|---|---|---|
| socket/test/probe/HBM equipment price spikes | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 tests whether price strength is valuation blowoff rather than order/margin bridge |
| customer qualification vocabulary without confirmed revision | C09 watch / C08 boundary | C08 requires customer quality; C09 handles valuation blowoff when that proof is missing |
| local peak followed by high MAE | C09 4B watch guard | local 4B may be useful risk overlay, but not Green unlock |

## 7. Case Selection Summary

| case_id | symbol | name | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current profile |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD | 095340 | ISC | 4B_overlay_success | Stage4B | 2024-03-28 | 99400 | 8.65 | -27.06 | 8.65 | -58.65 | 8.65 | -58.65 | current_profile_correct |
| C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE | 131290 | 티에스이 | failed_rerating | Stage2 | 2024-04-26 | 79000 | 11.14 | -30.76 | 11.14 | -51.84 | 11.14 | -51.84 | current_profile_false_positive |
| C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL | 425420 | 티에프이 | failed_rerating | Stage2 | 2024-03-20 | 43100 | 1.97 | -22.16 | 1.97 | -48.38 | 1.97 | -65.82 | current_profile_false_positive |
| C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF | 424980 | 마이크로투나노 | 4B_overlay_success | Stage2 | 2024-04-23 | 18200 | 30.49 | -26.81 | 30.49 | -50.0 | 30.49 | -50.0 | current_profile_too_early |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
4B_case_count = 4
4C_case_count = 0
calibration_usable_case_count = 4
```

The one positive case is positive only for the 4B overlay: ISC showed that C09 blowoff detection could protect after the local peak. It is not a positive Stage3-Green long-entry case. The other three cases are counterexamples where price-only equipment narratives produced severe MAE without a confirmed order/margin/revision bridge.

## 9. Evidence Source Map

| symbol | evidence status | source family | promotion status |
|---|---|---|---|
| 095340 | source_proxy_only / exact_url_pending | test-socket/HBM socket + valuation blowoff | usable for ledger, not promotion |
| 131290 | source_proxy_only / exact_url_pending | probe-card/test equipment blowoff | usable for ledger, not promotion |
| 425420 | source_proxy_only / exact_url_pending | test handler/socket equipment blowoff | usable for ledger, not promotion |
| 424980 | source_proxy_only / exact_url_pending | MEMS probe-card blowoff | usable for ledger, not promotion |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json |
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | atlas/symbol_profiles/425/425420.json |
| 424980 | atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv | atlas/symbol_profiles/424/424980.json |

## 11. Case-by-Case Trigger Grid

### C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD

- Trigger: Stage4B valuation blowoff watch.
- Mechanism: price/volume blowoff in a test-socket/HBM socket narrative without enough confirmed revision/margin bridge in the research proxy.
- Entry: 2024-03-28 close 99,400.
- Result: local peak 108,000 on 2024-03-28, then deep drawdown. C09 4B watch would have been directionally useful.

### C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE

- Trigger: Stage2 price-only late chase.
- Mechanism: probe/test equipment price surge after advanced-equipment theme, but no verified incremental order/margin bridge in this loop.
- Entry: 2024-04-26 close 79,000.
- Result: MFE90 +11.14 versus MAE90 -51.84, a classic high-MAE false positive.

### C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL

- Trigger: Stage2 test-handler/socket equipment theme spike.
- Mechanism: relative strength appeared, but the bridge into revision/margin/FCF did not survive price-path stress.
- Entry: 2024-03-20 close 43,100.
- Result: MFE90 +1.97 versus MAE90 -48.38.

### C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF

- Trigger: Stage2 MEMS/probe-card price blowoff.
- Mechanism: very strong price move, but durable customer qualification and margin bridge were not confirmed in this source-proxy loop.
- Entry: 2024-04-23 close 18,200.
- Result: MFE30 +30.49 but MAE90 -50.00; this supports a 4B watch, not a Green unlock.

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | name | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current profile |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD | 095340 | ISC | 4B_overlay_success | Stage4B | 2024-03-28 | 99400 | 8.65 | -27.06 | 8.65 | -58.65 | 8.65 | -58.65 | current_profile_correct |
| C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE | 131290 | 티에스이 | failed_rerating | Stage2 | 2024-04-26 | 79000 | 11.14 | -30.76 | 11.14 | -51.84 | 11.14 | -51.84 | current_profile_false_positive |
| C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL | 425420 | 티에프이 | failed_rerating | Stage2 | 2024-03-20 | 43100 | 1.97 | -22.16 | 1.97 | -48.38 | 1.97 | -65.82 | current_profile_false_positive |
| C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF | 424980 | 마이크로투나노 | 4B_overlay_success | Stage2 | 2024-04-23 | 18200 | 30.49 | -26.81 | 30.49 | -50.0 | 30.49 | -50.0 | current_profile_too_early |

## 13. Current Calibrated Profile Stress Test

1. Current calibrated profile likely blocks full positive Stage3 if bridge evidence is missing.
2. It may still allow too much Stage2 attention when relative strength and equipment vocabulary are strong.
3. The existing Stage2 bonus is useful for true early cases but too permissive for C09 price-only equipment blowoff.
4. Yellow threshold 75 is not the main issue; missing bridge evidence is.
5. Green threshold 87 / revision 55 should not be relaxed.
6. Price-only blowoff guard is directionally correct.
7. Full 4B non-price requirement is correct for full 4B, but C09 can still use price-only blowoff as a watch-only risk flag.
8. Hard 4C is not triggered here because the evidence is mostly price-path/bridge-missing rather than explicit thesis break.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green rows are used. All cases are Stage2 or Stage4B watch tests. The result says: Stage2 price strength inside C09 should remain fragile until order/revenue/margin/revision bridge is visible.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | local peak | full observed peak | verdict |
|---|---:|---:|---|
| 095340 | 108000 | 108000 | good_local_and_full_window_4B_timing |
| 131290 | 87800 | 87800 | price_only_blowoff_then_high_mae |
| 425420 | 43950 | 43950 | price_only_blowoff_guard_needed |
| 424980 | 23750 | 23750 | local_blowoff_good_for_watch_not_long_green |

C09’s useful signal is not “buy equipment strength”; it is “do not mistake price-only equipment strength for structural rerating.” The blowoff is a flare: useful for risk location, dangerous as a lighthouse.

## 16. 4C Protection Audit

No hard 4C row is asserted. There are no verified customer cancellation, accounting break, regulatory rejection, or explicit thesis-break events in this source-proxy loop.

```text
four_c_protection_label = not_applicable_no_hard_4c
```

## 17. Sector-Specific Rule Candidate

No L2-wide rule is proposed. This loop is C09-specific and should not change all semiconductor equipment scoring.

```text
sector_specific_rule_candidate = false
```

## 18. Canonical-Archetype Rule Candidate

Shadow-only C09 rule candidate:

```text
if canonical_archetype_id == C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
and relative_strength is high
and valuation_repricing / positioning_overheat is high
and confirmed_order_margin_revision_bridge is missing:
    block Stage3-Green
    demote Stage2-Actionable to Stage2-Watch or Stage4B-Watch
```

Promotion status:

```text
canonical_archetype_rule_candidate = true_shadow_only
do_not_propose_new_weight_delta = true
reason = source_proxy_only / evidence_url_pending
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive risk | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1 proxy | 4 | 13.06 | -52.72 | high | too permissive for C09 price-only Stage2 |
| P1 C09 bridge guard | 4 | watch-only | risk-reduced | lower | keep as shadow |
| P2 C09 4B watch | 4 | not long-entry | drawdown aware | lower | useful risk overlay |
| P3 counterexample guard | 3 | 14.53 | -50.07 | high if ignored | supports bridge requirement |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| ISC | 68 | Stage4B | 64 | Stage4B | correct risk overlay |
| TSE | 72 | Stage2-Actionable | 58 | Stage4B-Watch | better |
| TFE | 72 | Stage2-Actionable | 58 | Stage4B-Watch | better |
| M2N | 72 | Stage2-Actionable | 58 | Stage4B-Watch | better |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE | 1 | 3 | 4 | 0 | 4 | 0 | 4 | 4 | 3 | no | yes_shadow_only | C09 index rows 15 → effective +4 local session rows; still below 30-row stability target |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - price_only_advanced_equipment_blowoff_high_mae
  - stage2_theme_spike_without_order_margin_bridge
  - local_4B_watch_success_but_not_green_unlock
new_axis_proposed: false
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage / C09 shadow only
existing_axis_weakened: false
existing_axis_kept: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true_shadow_only
no_new_signal_reason: null
loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:
- Stock-Web OHLC path exists.
- Entry date and close price exist.
- MFE/MAE 30D/90D/180D are computed.
- New symbols and new trigger families are used.

Non-validation scope:
- Exact non-price evidence URLs are not verified in this loop.
- Business-source proof is source-proxy-only.
- No production patch should be applied from this file alone.

## 24. Shadow Weight Calibration

| axis | scope | tested value | confidence | promotion |
|---|---|---|---|---|
| c09_valuation_blowoff_requires_order_margin_revision_bridge | canonical C09 | require bridge before Stage2-Actionable/Green | low_to_medium | hold |
| c09_price_only_local_4b_not_full_green | canonical C09 | price-only blowoff can be watch, not Green | low_to_medium | hold |

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD","symbol":"095340","company_name":"ISC","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4B_success_price_protected_after_local_peak","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; exact business/evidence URL pending; do not promote without URL verification"}
{"row_type":"case","case_id":"C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mae_after_equipment_blowoff","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; exact business/evidence URL pending; do not promote without URL verification"}
{"row_type":"case","case_id":"C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL","symbol":"425420","company_name":"티에프이","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_stage2_theme_spike_without_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; exact business/evidence URL pending; do not promote without URL verification"}
{"row_type":"case","case_id":"C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_moved_without_durable_evidence_then_roundtrip","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; exact business/evidence URL pending; do not promote without URL verification"}
{"row_type":"trigger","trigger_id":"TRG_C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD","case_id":"C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD","symbol":"095340","company_name":"ISC","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics / advanced test-probe equipment valuation blowoff","primary_archetype":"advanced equipment valuation blowoff versus order/margin/revision bridge","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_type":"Stage4B","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":99400,"evidence_available_at_that_date":"price/volume blowoff over test-socket/HBM socket narrative; exact customer/order URL pending","evidence_source":"source_proxy_only; exact_url_pending","evidence_family":"test_socket_customer_quality_label_plus_valuation_blowoff","stage2_evidence_fields":["customer_or_order_quality_proxy","relative_strength","socket_test_equipment_theme"],"stage3_evidence_fields":["not_confirmed_revision","not_confirmed_margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","MFE_30D_pct":8.65,"MFE_90D_pct":8.65,"MFE_180D_pct":8.65,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.06,"MAE_90D_pct":-58.65,"MAE_180D_pct":-58.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_and_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"4B_success_price_protected_after_local_peak","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_outside_window","same_entry_group_id":"C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE","case_id":"C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics / advanced test-probe equipment valuation blowoff","primary_archetype":"advanced equipment valuation blowoff versus order/margin/revision bridge","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_type":"Stage2","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":79000,"evidence_available_at_that_date":"test/probe equipment price surge after advanced-equipment theme; exact order/margin bridge URL pending","evidence_source":"source_proxy_only; exact_url_pending","evidence_family":"probe_card_test_equipment_price_blowoff_no_incremental_bridge","stage2_evidence_fields":["relative_strength","probe_test_equipment_theme","capacity_optional_proxy"],"stage3_evidence_fields":["not_confirmed_revision","not_confirmed_margin_bridge","not_multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-30.76,"MAE_90D_pct":-51.84,"MAE_180D_pct":-51.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_blowoff_then_high_mae","four_b_evidence_type":["valuation_blowoff","price_only"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"false_positive_high_mae_after_equipment_blowoff","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_outside_window","same_entry_group_id":"C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL","case_id":"C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL","symbol":"425420","company_name":"티에프이","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics / advanced test-probe equipment valuation blowoff","primary_archetype":"advanced equipment valuation blowoff versus order/margin/revision bridge","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_type":"Stage2","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":43100,"evidence_available_at_that_date":"test-handler/socket equipment theme spike; order/revision/margin proof pending","evidence_source":"source_proxy_only; exact_url_pending","evidence_family":"test_handler_socket_equipment_theme_no_order_margin_bridge","stage2_evidence_fields":["relative_strength","test_handler_socket_theme"],"stage3_evidence_fields":["not_confirmed_revision","not_confirmed_margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","MFE_30D_pct":1.97,"MFE_90D_pct":1.97,"MFE_180D_pct":1.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.16,"MAE_90D_pct":-48.38,"MAE_180D_pct":-65.82,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43950,"drawdown_after_peak_pct":-66.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_blowoff_guard_needed","four_b_evidence_type":["valuation_blowoff","price_only"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"counterexample_stage2_theme_spike_without_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_outside_window","same_entry_group_id":"C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","case_id":"C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TEST_SOCKET_PROBE_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics / advanced test-probe equipment valuation blowoff","primary_archetype":"advanced equipment valuation blowoff versus order/margin/revision bridge","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_type":"Stage2","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":18200,"evidence_available_at_that_date":"MEMS probe-card/HBM equipment price surge; customer qualification and durable margin bridge URL pending","evidence_source":"source_proxy_only; exact_url_pending","evidence_family":"mems_probe_card_price_blowoff_without_customer_quality_margin_bridge","stage2_evidence_fields":["relative_strength","probe_card_theme","policy_or_regulatory_optionality_absent"],"stage3_evidence_fields":["not_confirmed_revision","not_confirmed_margin_bridge","not_durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv","profile_path":"atlas/symbol_profiles/424/424980.json","MFE_30D_pct":30.49,"MFE_90D_pct":30.49,"MFE_180D_pct":30.49,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.81,"MAE_90D_pct":-50.0,"MAE_180D_pct":-50.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":23750,"drawdown_after_peak_pct":-61.68,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_blowoff_good_for_watch_not_long_green","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"price_moved_without_durable_evidence_then_roundtrip","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_outside_window","same_entry_group_id":"C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD","trigger_id":"TRG_C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":80,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":60,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage4B","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 demotes price-only advanced-equipment spikes unless order/revision/margin bridge survives 30-90D high-MAE stress.","MFE_90D_pct":8.65,"MAE_90D_pct":-58.65,"score_return_alignment_label":"4B_success_price_protected_after_local_peak","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE","trigger_id":"TRG_C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":80,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":60,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":85,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage4B-Watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 demotes price-only advanced-equipment spikes unless order/revision/margin bridge survives 30-90D high-MAE stress.","MFE_90D_pct":11.14,"MAE_90D_pct":-51.84,"score_return_alignment_label":"false_positive_high_mae_after_equipment_blowoff","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL","trigger_id":"TRG_C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":80,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":60,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":85,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage4B-Watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 demotes price-only advanced-equipment spikes unless order/revision/margin bridge survives 30-90D high-MAE stress.","MFE_90D_pct":1.97,"MAE_90D_pct":-48.38,"score_return_alignment_label":"counterexample_stage2_theme_spike_without_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","trigger_id":"TRG_C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","symbol":"424980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":80,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":60,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":85,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage4B-Watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 demotes price-only advanced-equipment spikes unless order/revision/margin bridge survives 30-90D high-MAE stress.","MFE_90D_pct":30.49,"MAE_90D_pct":-50.0,"score_return_alignment_label":"price_moved_without_durable_evidence_then_roundtrip","current_profile_verdict":"current_profile_too_early"}
{"row_type":"shadow_weight","axis":"c09_valuation_blowoff_requires_order_margin_revision_bridge","scope":"canonical_archetype","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","baseline_value":"watch_only_when_price_only","tested_value":"require_non_price_order_margin_revision_bridge","delta":"+guard","reason":"3/4 new cases had high 90D MAE after price-only blowoff; positive case was 4B overlay success, not Green unlock.","backtest_effect":"demotes Stage2 false positives; preserves Stage4B watch","trigger_ids":"TRG_C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD|TRG_C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE|TRG_C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL|TRG_C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","calibration_usable_count":4,"new_independent_case_count":4,"counterexample_count":3,"confidence":"low_to_medium_due_source_proxy","proposal_type":"canonical_shadow_only","notes":"Do not apply until exact evidence URLs are rematerialized."}
{"row_type":"shadow_weight","axis":"c09_price_only_local_4b_not_full_green","scope":"canonical_archetype","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","baseline_value":"full_4b_requires_non_price_evidence","tested_value":"price_only_blowoff_can_trigger_watch_but_not_structural_green","delta":"keep_axis_strengthened_in_C09","reason":"Local peaks helped risk control but did not validate long rerating without bridge.","backtest_effect":"keeps price-only blowoff as risk overlay rather than positive signal","trigger_ids":"TRG_C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD|TRG_C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":1,"confidence":"low_to_medium_due_source_proxy","proposal_type":"canonical_shadow_only","notes":"Guardrail support only; no global threshold change."}
{"row_type":"residual_contribution","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["price_only_advanced_equipment_blowoff_high_mae","stage2_theme_spike_without_order_margin_bridge","local_4B_watch_success_but_not_green_unlock"],"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas.

This MD is not live candidate research. It is historical calibration research designed to extend the C09 advanced-equipment valuation-blowoff ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not apply new production patch from this MD unless exact evidence URLs are rematerialized.
- Treat this file as C09 shadow evidence for bridge-required demotion of price-only equipment blowoff.
- Do not lower Stage3-Green total/revision thresholds.
- Do not use symbol names as runtime scoring rules.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 98
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: atlas/manifest.json
- Stock-Web schema: atlas/schema.json
- Stock-Web shards:
  - atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv

```text
loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```
