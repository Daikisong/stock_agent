# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R2
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R3
computed_next_loop: 74
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: C08_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`. The previous R2 loop used C09 advanced-equipment valuation blowoff, and earlier loops already touched C10 memory recovery. This run shifts to C08, but avoids the top-covered socket/probe names. The residual target is the line between a real customer-quality socket/test bridge and a probe-card or IPO theme that only produces MFE before high MAE.

| layer | id | definition |
|---|---|---|
| round | R2 | AI / semiconductor / electronics |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | semiconductor, HBM, equipment, test/socket, electronics |
| canonical | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | semiconductor test socket, probe card, customer-quality bridge |
| fine | C08_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_GUARD | socket/probe signal must become customer/repeat-order/margin bridge |
| deep | TEST_INTERFACE_BURNIN_SOCKET_CUSTOMER_QUALITY_TO_ORDER_REVENUE_BRIDGE | test-interface customer-quality guarded positive |
| deep | CERAMIC_STF_TEST_SOCKET_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CONVERSION | ceramic/probe-card MFE with no durable bridge |
| deep | MEMS_PROBE_CARD_IPO_OPTIONALITY_WITHOUT_CUSTOMER_QUALITY_MARGIN_BRIDGE | MEMS probe-card IPO optionality false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C08 top-covered symbols are `098120`, `080580`, `058470`, `095340`, `131290`, and `219130`. This run avoids that cluster and also avoids the immediately prior R2/C09 and C10 representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C08 | 425420 | new independent | not top-covered C08 symbol; test-interface/customer-quality bridge with 4B/high-MAE guard |
| C08 | 252990 | new independent | not top-covered C08 symbol; ceramic STF/probe-card theme MFE without durable bridge |
| C08 | 424980 | new independent | not top-covered C08 symbol; MEMS probe-card IPO optionality counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
425420 has no corporate-action candidate dates.
252990 has no corporate-action candidate dates.
424980 has no corporate-action candidate dates.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_with_high_MAE_watch | 425420 | 티에프이 | Stage2-Actionable | 2024-02-08 | 35200 | customer-quality/order bridge worked, but 4B/high-MAE guard required |
| theme_MFE_then_high_MAE_counterexample | 252990 | 샘씨엔에스 | Stage2-Actionable | 2024-01-23 | 6860 | ceramic STF/probe-card theme had MFE but no durable customer bridge |
| IPO_optional_MFE_then_high_MAE_counterexample | 424980 | 마이크로투나노 | Stage2-Actionable | 2024-01-25 | 16280 | MEMS probe-card IPO optionality had MFE but lacked customer/revenue bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 425420 | 티에프이 | Stage2-Actionable | 2024-02-08 | 35200 | 24.86 | 24.86 | 24.86 | -14.77 | -21.88 | -30.82 | 2024-03-21 | 43950 | -44.6 |
| 252990 | 샘씨엔에스 | Stage2-Actionable | 2024-01-23 | 6860 | 28.86 | 28.86 | 28.86 | -7.0 | -7.0 | -30.76 | 2024-02-07 | 8840 | -46.27 |
| 424980 | 마이크로투나노 | Stage2-Actionable | 2024-01-25 | 16280 | 2.58 | 45.88 | 45.88 | -24.32 | -27.15 | -41.65 | 2024-05-03 | 23750 | -60.0 |

## 9. Case-by-Case Notes

### 9.1 425420 / 티에프이 — test-interface customer-quality bridge

The entry row is 2024-02-08 at 35,200. The path reaches 43,950, but then later falls sharply. This is a valid C08 positive only under a guarded reading: the test-interface and socket/customer-quality bridge can support Stage2/Yellow, but the high-MAE path blocks Green. The socket is a connector; without durable customer pull-through, it can also become a loose contact.

### 9.2 252990 / 샘씨엔에스 — ceramic STF/probe-card theme without durable bridge

The entry row is 2024-01-23 at 6,860. The price path reaches 8,840, but the later low reaches 4,750. MFE existed, yet the durable bridge was weak. This should remain 4B/high-MAE watch unless repeat customer order, utilization, margin, or order-to-revenue visibility appears.

### 9.3 424980 / 마이크로투나노 — MEMS probe-card IPO optionality false positive

The entry row is 2024-01-25 at 16,280. The later path reaches 23,750, but the low falls to 9,500. This is the IPO/optionality version of C08: probe-card technology can be promising, but without customer-quality and repeat-revenue proof, MFE is not evidence of Stage3 durability.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C08 treats socket/probe-card/IPO theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C08 needs customer-quality/repeat-order/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 252990 and 424980. |
| Full 4B non-price requirement appropriate? | Yes. MFE alone does not promote the two theme rows. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
425420:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer-quality/order bridge
  Stage3-Green = reject because high-MAE watch remains active

252990:
  Stage2-Actionable = acceptable only as theme/watch
  Stage3-Yellow = reject without repeat-order, margin, or utilization bridge
  Stage3-Green = reject despite MFE

424980:
  Stage2-Actionable = acceptable only as IPO/technology watch
  Stage3-Yellow = reject without customer-quality/revenue bridge
  Stage3-Green = reject despite full-window MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 425420 | 1.00 | 1.00 | test-interface bridge positive but local 4B/high-MAE watch |
| 252990 | 1.00 | 1.00 | probe-card theme MFE but no customer bridge; keep 4B/high-MAE watch |
| 424980 | 0.70 | 1.00 | full-window MFE but no source bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c08_requires_customer_quality_repeat_order_margin_utilization_bridge

rule:
  For C08 semiconductor test/socket/probe-card rows, do not promote socket,
  probe-card, ceramic STF, MEMS probe-card, IPO optionality, or test-interface
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  customer-quality confirmation, repeat order, order-to-revenue conversion,
  utilization, margin conversion, advanced-package pull-through, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 33.2 | -18.68 | 66.7% | too generous to socket/probe-card theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 33.2 | -18.68 | 33.3% | safer but may miss 425420 |
| P1 sector_specific_candidate_profile | 3 | 33.2 | -18.68 | 66.7% | no broad L2 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 24.86 | -21.88 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 37.37 | -17.07 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 425420 | current_profile_partially_correct | bridge worked, but high-MAE requires 4B watch |
| 252990 | current_profile_false_positive_if_green | MFE existed but no durable customer bridge |
| 424980 | current_profile_false_positive_if_green | IPO/probe-card optionality produced MFE but no durable source bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | C08 non-top-covered socket/probe-card residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- probe-card theme MFE without customer-quality bridge
- IPO probe-card optionality high-MAE
- test-interface bridge winner needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c08_requires_customer_quality_repeat_order_margin_utilization_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 test/socket/probe-card rows should not promote toward Stage3-Yellow/Green unless socket or probe-card signal converts into customer-quality, repeat order, order-to-revenue, utilization, margin, or advanced-package pull-through bridge","425420 survives only as guarded positive after customer-quality/order bridge; 252990 and 424980 remain 4B/high-MAE watch because MFE came from theme or IPO optionality without durable source bridge","TRG_R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE|TRG_R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE|TRG_R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c08_socket_probe_card_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,1,1,0,"Test/socket winners and probe-card theme rows can peak before customer and repeat-order durability is confirmed; local/full-window 4B and high-MAE watch must remain active","preserves 425420 guarded positive while preventing 252990/424980 Green false positives","TRG_R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE|TRG_R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE|TRG_R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE","symbol":"425420","company_name":"티에프이","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_INTERFACE_BOARD_CUSTOMER_QUALITY_BRIDGE","deep_sub_archetype_id":"TEST_INTERFACE_BURNIN_SOCKET_CUSTOMER_QUALITY_TO_ORDER_REVENUE_BRIDGE","case_type":"structural_success_with_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C08 test/socket/probe-card rows require customer-quality, repeat order, order-to-revenue, utilization, margin, or advanced-package pull-through bridge; socket/probe-card/IPO theme alone is insufficient."}
{"row_type":"case","case_id":"R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_PROBE_CARD_CERAMIC_STF_THEME_WITHOUT_DURABLE_CUSTOMER_BRIDGE","deep_sub_archetype_id":"CERAMIC_STF_TEST_SOCKET_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CONVERSION","case_type":"theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C08 test/socket/probe-card rows require customer-quality, repeat order, order-to-revenue, utilization, margin, or advanced-package pull-through bridge; socket/probe-card/IPO theme alone is insufficient."}
{"row_type":"case","case_id":"R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_MEMS_PROBE_CARD_OPTIONALITY_WITHOUT_CUSTOMER_REVENUE_BRIDGE","deep_sub_archetype_id":"MEMS_PROBE_CARD_IPO_OPTIONALITY_WITHOUT_CUSTOMER_QUALITY_MARGIN_BRIDGE","case_type":"IPO_optional_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C08 test/socket/probe-card rows require customer-quality, repeat order, order-to-revenue, utilization, margin, or advanced-package pull-through bridge; socket/probe-card/IPO theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE","case_id":"R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE","symbol":"425420","company_name":"티에프이","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_INTERFACE_BOARD_CUSTOMER_QUALITY_BRIDGE","deep_sub_archetype_id":"TEST_INTERFACE_BURNIN_SOCKET_CUSTOMER_QUALITY_TO_ORDER_REVENUE_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":35200,"evidence_available_at_that_date":"source_proxy_test_interface_board_customer_quality_order_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_test_interface_board_customer_quality_order_revenue_bridge; evidence_url_pending","bridge_summary":"test-interface and socket/customer-quality signal converted into order/revenue visibility, but high-MAE path requires 4B watch rather than Green loosening","stage2_evidence_fields":["test_interface_board","socket_customer_quality","relative_strength","order_revenue_proxy"],"stage3_evidence_fields":["customer_quality_bridge","order_to_revenue_visibility","advanced_package_test_pullthrough"],"stage4b_evidence_fields":["post_MFE_peak_watch","test_socket_crowding_after_customer_quality_rerating"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.86,"MFE_90D_pct":24.86,"MFE_180D_pct":24.86,"MFE_1Y_pct":24.86,"MFE_2Y_pct":24.86,"MAE_30D_pct":-14.77,"MAE_90D_pct":-21.88,"MAE_180D_pct":-30.82,"MAE_1Y_pct":-30.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43950,"drawdown_after_peak_pct":-44.6,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_interface_bridge_positive_but_local_4B_high_MAE_watch","four_b_evidence_type":"non_price_customer_quality_order_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE","case_id":"R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_PROBE_CARD_CERAMIC_STF_THEME_WITHOUT_DURABLE_CUSTOMER_BRIDGE","deep_sub_archetype_id":"CERAMIC_STF_TEST_SOCKET_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-23","entry_date":"2024-01-23","entry_price":6860,"evidence_available_at_that_date":"source_proxy_ceramic_STF_probe_card_test_socket_theme_without_repeat_order_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_ceramic_STF_probe_card_test_socket_theme_without_repeat_order_margin_bridge; evidence_url_pending","bridge_summary":"ceramic STF/probe-card optionality produced MFE, but repeat customer order, margin, and utilization bridge were not durable enough and the path later became high-MAE watch","stage2_evidence_fields":["probe_card_ceramic_STF_theme","test_socket_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","repeat_order_bridge_absent","margin_utilization_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_repeat_order_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv","profile_path":"atlas/symbol_profiles/252/252990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.86,"MFE_90D_pct":28.86,"MFE_180D_pct":28.86,"MFE_1Y_pct":28.86,"MFE_2Y_pct":28.86,"MAE_30D_pct":-7.0,"MAE_90D_pct":-7.0,"MAE_180D_pct":-30.76,"MAE_1Y_pct":-30.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-07","peak_price":8840,"drawdown_after_peak_pct":-46.27,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"probe_card_theme_MFE_but_no_customer_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"theme_or_IPO_without_customer_quality_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE","case_id":"R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_MEMS_PROBE_CARD_OPTIONALITY_WITHOUT_CUSTOMER_REVENUE_BRIDGE","deep_sub_archetype_id":"MEMS_PROBE_CARD_IPO_OPTIONALITY_WITHOUT_CUSTOMER_QUALITY_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":16280,"evidence_available_at_that_date":"source_proxy_MEMS_probe_card_IPO_optionality_without_customer_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_MEMS_probe_card_IPO_optionality_without_customer_revenue_margin_bridge; evidence_url_pending","bridge_summary":"MEMS probe-card and IPO optionality produced later MFE, but no durable customer-quality, revenue, margin, or repeat-order bridge followed","stage2_evidence_fields":["MEMS_probe_card_optionality","IPO_relative_strength","test_socket_theme"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_theme_peak","customer_quality_bridge_absent","repeat_revenue_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_customer_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv","profile_path":"atlas/symbol_profiles/424/424980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.58,"MFE_90D_pct":45.88,"MFE_180D_pct":45.88,"MFE_1Y_pct":45.88,"MFE_2Y_pct":45.88,"MAE_30D_pct":-24.32,"MAE_90D_pct":-27.15,"MAE_180D_pct":-41.65,"MAE_1Y_pct":-41.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":23750,"drawdown_after_peak_pct":-60.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"full_window_MFE_but_no_source_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"theme_or_IPO_without_customer_quality_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"IPO_optionality_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE","trigger_id":"TRG_R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"test_socket_score":12,"customer_quality_score":12,"repeat_order_score":10,"margin_utilization_score":9,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"test_socket_score":13,"customer_quality_score":15,"repeat_order_score":13,"margin_utilization_score":11,"relative_strength_score":8,"theme_risk_penalty":9},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["test_socket_score","customer_quality_score","repeat_order_score","margin_utilization_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C08 row is promoted only because test-interface strength converts into customer-quality and order/revenue bridge; high-MAE prevents Green.","MFE_90D_pct":24.86,"MAE_90D_pct":-21.88,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE","trigger_id":"TRG_R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE","symbol":"252990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"test_socket_score":10,"customer_quality_score":2,"repeat_order_score":1,"margin_utilization_score":1,"relative_strength_score":12,"theme_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"test_socket_score":5,"customer_quality_score":0,"repeat_order_score":0,"margin_utilization_score":0,"relative_strength_score":5,"theme_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["test_socket_score","customer_quality_score","repeat_order_score","margin_utilization_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C08 guard demotes probe-card/socket/IPO theme rows when customer-quality, repeat-order, revenue, margin or utilization bridge is absent.","MFE_90D_pct":28.86,"MAE_90D_pct":-7.0,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE","trigger_id":"TRG_R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE","symbol":"424980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"test_socket_score":10,"customer_quality_score":2,"repeat_order_score":1,"margin_utilization_score":1,"relative_strength_score":12,"theme_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"test_socket_score":5,"customer_quality_score":0,"repeat_order_score":0,"margin_utilization_score":0,"relative_strength_score":5,"theme_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["test_socket_score","customer_quality_score","repeat_order_score","margin_utilization_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C08 guard demotes probe-card/socket/IPO theme rows when customer-quality, repeat-order, revenue, margin or utilization bridge is absent.","MFE_90D_pct":45.88,"MAE_90D_pct":-27.15,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c08_requires_customer_quality_repeat_order_margin_utilization_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 test/socket/probe-card rows should not promote toward Stage3-Yellow/Green unless socket or probe-card signal converts into customer-quality, repeat order, order-to-revenue, utilization, margin, or advanced-package pull-through bridge","425420 survives only as guarded positive after customer-quality/order bridge; 252990 and 424980 remain 4B/high-MAE watch because MFE came from theme or IPO optionality without durable source bridge","TRG_R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE|TRG_R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE|TRG_R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c08_socket_probe_card_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,1,1,0,"Test/socket winners and probe-card theme rows can peak before customer and repeat-order durability is confirmed; local/full-window 4B and high-MAE watch must remain active","preserves 425420 guarded positive while preventing 252990/424980 Green false positives","TRG_R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE|TRG_R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE|TRG_R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["probe_card_theme_MFE_without_customer_quality_bridge","IPO_probe_card_optionality_high_MAE","test_interface_bridge_winner_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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
- price-only/socket-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C08 test/socket/probe-card rows cannot promote without customer-quality, repeat order, order-to-revenue, utilization, margin, advanced-package pull-through, or earnings-revision bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R2
completed_loop = 74
next_round = R3
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/425/425420.json
atlas/symbol_profiles/252/252990.json
atlas/symbol_profiles/424/424980.json
atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv
atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv
```

This loop continues loop 74 with R2 and adds 3 new independent C08 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R2/L2.
