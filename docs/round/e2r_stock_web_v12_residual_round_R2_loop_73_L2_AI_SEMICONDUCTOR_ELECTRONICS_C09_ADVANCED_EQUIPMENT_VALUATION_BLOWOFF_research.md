# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R2
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R3
computed_next_loop: 73
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_VALUATION_GUARD
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

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`. The prior R2 loop used C10 memory recovery equipment, so this run shifts to C09. C09 is where advanced-equipment narratives can become dangerous: the market often sees a clean-room machine and prices it like a mint, but the calibration question is whether customer order, revenue conversion, margin, and capacity pull-through are actually visible.

| layer | id | definition |
|---|---|---|
| round | R2 | AI / semiconductor / electronics |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | semiconductor, HBM, equipment, electronics |
| canonical | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | advanced equipment, valuation blowoff, peak-risk guard |
| fine | C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_VALUATION_GUARD | valuation needs order/revenue/margin bridge |
| deep | HBM_TEST_HANDLER_ORDER_TO_REVENUE_RELATIVE_STRENGTH_WITH_PEAK_GUARD | HBM handler order bridge success |
| deep | OVERLAY_METROLOGY_THEME_WITHOUT_CUSTOMER_ORDER_REVENUE_CONVERSION | metrology theme false positive |
| deep | FCBGA_SUBSTRATE_INSPECTION_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_BRIDGE | IPO/substrate inspection valuation blowoff |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C09 top-covered symbols are `240810`, `036930`, `039030`, `403870`, `003160`, and `042700`. This run avoids that top-covered C09 cluster and also avoids repeating the prior R2/C10 memory-recovery set.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C09 | 089030 | new independent | not top-covered C09 symbol; HBM handler order/revenue positive with 4B watch |
| C09 | 322310 | new independent | not top-covered C09 symbol; advanced metrology valuation spike counterexample |
| C09 | 420770 | new independent | not top-covered C09 symbol; substrate inspection IPO valuation blowoff counterexample |

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
089030 has old corporate-action candidate dates in 2022, outside this 2024 representative window.
322310 and 420770 have no corporate-action candidate dates in their profiles.
All representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 089030 | 테크윙 | Stage2-Actionable | 2024-01-19 | 14600 | HBM handler order/revenue bridge worked |
| failed_rerating_high_MAE_after_equipment_spike | 322310 | 오로스테크놀로지 | Stage2-Actionable | 2024-01-24 | 34650 | metrology valuation spike lacked order/revenue bridge |
| failed_rerating_IPO_valuation_blowoff | 420770 | 기가비스 | Stage2-Actionable | 2023-07-14 | 97400 | substrate inspection IPO/valuation blowoff lacked durable bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 089030 | 테크윙 | Stage2-Actionable | 2024-01-19 | 14600 | 56.85 | 224.66 | 384.93 | -11.71 | -11.71 | -11.71 | 2024-07-11 | 70800 | -31.5 |
| 322310 | 오로스테크놀로지 | Stage2-Actionable | 2024-01-24 | 34650 | 17.6 | 17.6 | 17.6 | -22.94 | -36.51 | -40.26 | 2024-02-27 | 40750 | -49.2 |
| 420770 | 기가비스 | Stage2-Actionable | 2023-07-14 | 97400 | 11.6 | 11.6 | 11.6 | -16.43 | -22.38 | -37.89 | 2023-07-14 | 108700 | -44.34 |

## 9. Case-by-Case Notes

### 9.1 089030 / 테크윙 — HBM handler order bridge positive

The entry row is 2024-01-19 at 14,600. The 90D path reaches 47,400 and the wider window reaches 70,800. This is the C09 success condition: advanced equipment strength was not just chart heat. It had an HBM handler/order/revenue bridge. The correct output is still Yellow plus 4B watch, because valuation expanded very quickly.

### 9.2 322310 / 오로스테크놀로지 — advanced metrology spike without bridge

The entry row is 2024-01-24 at 34,650. The local spike reaches 40,750, but the later path drops deeply. This is the C09 false-positive shape: overlay/metrology optionality looks like advanced equipment scarcity, but without customer order and revenue conversion, valuation becomes the ceiling rather than the engine.

### 9.3 420770 / 기가비스 — substrate inspection IPO blowoff

The entry row is 2023-07-14 at 97,400. The upside was shallow relative to the later drawdown. This is the IPO version of C09: substrate inspection and FCBGA optionality can be structurally interesting, but if repeat orders, margin, and customer-capex evidence do not follow, the rerating stays brittle.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C09 treats advanced-equipment theme, IPO, or valuation spike as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C09 needs customer order/revenue/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 322310 and 420770. |
| Full 4B non-price requirement appropriate? | Yes. 089030 has a better non-price bridge; 322310/420770 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
089030:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after HBM handler order/revenue bridge
  Stage3-Green = wait for stronger margin/FCF durability and post-MFE 4B check

322310:
  Stage2-Actionable = too generous if based only on advanced metrology price spike
  Stage3-Yellow = reject without customer order/revenue bridge
  Stage3-Green = reject

420770:
  Stage2-Actionable = too generous if based on IPO/substrate-inspection valuation optionality alone
  Stage3-Yellow = reject without repeat-order/margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 089030 | 0.91 | 1.00 | good full-window 4B watch after HBM order/revenue bridge |
| 322310 | 1.00 | 1.00 | price/theme local 4B watch, not positive stage |
| 420770 | 1.00 | 1.00 | IPO valuation local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c09_requires_customer_order_revenue_margin_bridge

rule:
  For C09 advanced-equipment rows, do not promote equipment scarcity, AI/HBM association,
  IPO optionality, or valuation momentum Stage2 signals into Stage3-Yellow/Green unless
  at least one non-price bridge is visible:
  customer order, order-to-revenue conversion, capacity pull-through, repeat equipment demand,
  margin conversion, or earnings revision tied to actual equipment shipment.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 84.62 | -23.53 | 66.7% | too generous to valuation-heavy advanced-equipment rows |
| P0b e2r_2_0_baseline_reference | 3 | 84.62 | -23.53 | 33.3% | safer but may miss 089030 |
| P1 sector_specific_candidate_profile | 3 | 84.62 | -23.53 | 66.7% | no broad L2 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 224.66 | -11.71 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 14.6 | -29.45 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 089030 | current_profile_correct | HBM order/revenue bridge aligned with strong MFE |
| 322310 | current_profile_false_positive | metrology valuation spike produced high MAE |
| 420770 | current_profile_false_positive | IPO/equipment optionality produced weak MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_VALUATION_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C09 non-top-covered advanced-equipment valuation residual reduced |

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
- advanced equipment theme without order bridge
- IPO valuation blowoff without margin bridge
- HBM equipment winner needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
shadow_weight,c09_requires_customer_order_revenue_margin_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"C09 advanced-equipment rows should not promote toward Stage3-Yellow/Green unless advanced equipment strength converts into customer order, revenue conversion, margin, or capacity pull-through bridge","089030 survives with strong MFE after HBM handler order/revenue bridge; 322310 and 420770 fail when metrology/substrate inspection theme or IPO valuation lacks durable bridge","TRG_R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B|TRG_R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE|TRG_R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c09_advanced_equipment_valuation_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,1,1,0,"Advanced-equipment winners and IPO/theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 089030 positive while preventing 322310/420770 valuation blowoff false positives","TRG_R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B|TRG_R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE|TRG_R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B","symbol":"089030","company_name":"테크윙","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_HBM_HANDLER_ADVANCED_EQUIPMENT_ORDER_VALUATION_GUARD","deep_sub_archetype_id":"HBM_TEST_HANDLER_ORDER_TO_REVENUE_RELATIVE_STRENGTH_WITH_PEAK_GUARD","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C09 advanced-equipment rows require customer order, revenue conversion, margin bridge, or capacity pull-through; advanced-equipment theme, IPO, or valuation spike alone is insufficient."}
{"row_type":"case","case_id":"R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_METROLOGY_PRICE_SPIKE_WITHOUT_ORDER_BRIDGE","deep_sub_archetype_id":"OVERLAY_METROLOGY_THEME_WITHOUT_CUSTOMER_ORDER_REVENUE_CONVERSION","case_type":"failed_rerating_high_MAE_after_equipment_spike","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C09 advanced-equipment rows require customer order, revenue conversion, margin bridge, or capacity pull-through; advanced-equipment theme, IPO, or valuation spike alone is insufficient."}
{"row_type":"case","case_id":"R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE","symbol":"420770","company_name":"기가비스","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_SUBSTRATE_INSPECTION_IPO_VALUATION_BLOWOFF_GUARD","deep_sub_archetype_id":"FCBGA_SUBSTRATE_INSPECTION_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating_IPO_valuation_blowoff","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C09 advanced-equipment rows require customer order, revenue conversion, margin bridge, or capacity pull-through; advanced-equipment theme, IPO, or valuation spike alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B","case_id":"R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B","symbol":"089030","company_name":"테크윙","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_HBM_HANDLER_ADVANCED_EQUIPMENT_ORDER_VALUATION_GUARD","deep_sub_archetype_id":"HBM_TEST_HANDLER_ORDER_TO_REVENUE_RELATIVE_STRENGTH_WITH_PEAK_GUARD","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":14600,"evidence_available_at_that_date":"source_proxy_HBM_handler_order_relative_strength_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_HBM_handler_order_relative_strength_revenue_bridge; evidence_url_pending","bridge_summary":"HBM handler/test-equipment order route converted into revenue and customer-demand visibility; valuation risk still required 4B watch","stage2_evidence_fields":["HBM_equipment_order","relative_strength","customer_capacity_pullthrough","order_to_revenue_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","customer_quality_proxy","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","valuation_repricing_after_HBM_equipment_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":56.85,"MFE_90D_pct":224.66,"MFE_180D_pct":384.93,"MFE_1Y_pct":384.93,"MFE_2Y_pct":384.93,"MAE_30D_pct":-11.71,"MAE_90D_pct":-11.71,"MAE_180D_pct":-11.71,"MAE_1Y_pct":-11.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-31.5,"green_lateness_ratio":"0.28","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_HBM_order_revenue_bridge","four_b_evidence_type":"non_price_order_revenue_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE","case_id":"R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_METROLOGY_PRICE_SPIKE_WITHOUT_ORDER_BRIDGE","deep_sub_archetype_id":"OVERLAY_METROLOGY_THEME_WITHOUT_CUSTOMER_ORDER_REVENUE_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":34650,"evidence_available_at_that_date":"source_proxy_advanced_metrology_equipment_theme_without_customer_order_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_advanced_metrology_equipment_theme_without_customer_order_revenue_bridge; evidence_url_pending","bridge_summary":"advanced metrology/overlay theme price spike lacked durable customer-order and revenue bridge; valuation peak reversed into high MAE","stage2_evidence_fields":["advanced_metrology_theme","relative_strength","price_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","valuation_blowoff","weak_order_revenue_bridge"],"stage4c_evidence_fields":["high_MAE_without_customer_order_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.6,"MFE_90D_pct":17.6,"MFE_180D_pct":17.6,"MFE_1Y_pct":17.6,"MFE_2Y_pct":17.6,"MAE_30D_pct":-22.94,"MAE_90D_pct":-36.51,"MAE_180D_pct":-40.26,"MAE_1Y_pct":-40.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":40750,"drawdown_after_peak_pct":-49.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_valuation_theme_without_order_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE","case_id":"R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE","symbol":"420770","company_name":"기가비스","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_SUBSTRATE_INSPECTION_IPO_VALUATION_BLOWOFF_GUARD","deep_sub_archetype_id":"FCBGA_SUBSTRATE_INSPECTION_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-14","entry_date":"2023-07-14","entry_price":97400,"evidence_available_at_that_date":"source_proxy_FCBGA_substrate_inspection_IPO_equipment_optionality_without_repeat_order_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_FCBGA_substrate_inspection_IPO_equipment_optionality_without_repeat_order_margin_bridge; evidence_url_pending","bridge_summary":"substrate inspection / advanced equipment optionality remained IPO and valuation-heavy without repeat-order, margin, or customer-capex bridge","stage2_evidence_fields":["advanced_substrate_inspection_theme","IPO_relative_strength","valuation_rerating"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["IPO_price_peak","valuation_blowoff","repeat_order_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_margin_or_customer_order_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/420/420770/2023.csv|atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv","profile_path":"atlas/symbol_profiles/420/420770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.6,"MFE_90D_pct":11.6,"MFE_180D_pct":11.6,"MFE_1Y_pct":11.6,"MFE_2Y_pct":11.6,"MAE_30D_pct":-16.43,"MAE_90D_pct":-22.38,"MAE_180D_pct":-37.89,"MAE_1Y_pct":-37.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-14","peak_price":108700,"drawdown_after_peak_pct":-44.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"IPO_valuation_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_valuation_theme_without_order_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_IPO_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B","trigger_id":"TRG_R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"advanced_equipment_score":12,"customer_order_bridge_score":12,"revenue_conversion_score":10,"valuation_risk_score":5,"relative_strength_score":12,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"advanced_equipment_score":11,"customer_order_bridge_score":16,"revenue_conversion_score":14,"valuation_risk_score":8,"relative_strength_score":9,"risk_penalty":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["advanced_equipment_score","customer_order_bridge_score","revenue_conversion_score","valuation_risk_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C09 row is promoted only when advanced-equipment strength converts into customer order and revenue bridge; valuation risk remains a 4B overlay.","MFE_90D_pct":224.66,"MAE_90D_pct":-11.71,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE","trigger_id":"TRG_R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE","symbol":"322310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"advanced_equipment_score":10,"customer_order_bridge_score":1,"revenue_conversion_score":1,"valuation_risk_score":11,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"advanced_equipment_score":5,"customer_order_bridge_score":0,"revenue_conversion_score":0,"valuation_risk_score":15,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["advanced_equipment_score","customer_order_bridge_score","revenue_conversion_score","valuation_risk_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C09 guard demotes advanced-equipment/IPO/valuation spikes when customer order, revenue, margin, or capacity bridge is absent.","MFE_90D_pct":17.6,"MAE_90D_pct":-36.51,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE","trigger_id":"TRG_R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE","symbol":"420770","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"advanced_equipment_score":10,"customer_order_bridge_score":1,"revenue_conversion_score":1,"valuation_risk_score":11,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"advanced_equipment_score":5,"customer_order_bridge_score":0,"revenue_conversion_score":0,"valuation_risk_score":15,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["advanced_equipment_score","customer_order_bridge_score","revenue_conversion_score","valuation_risk_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C09 guard demotes advanced-equipment/IPO/valuation spikes when customer order, revenue, margin, or capacity bridge is absent.","MFE_90D_pct":11.6,"MAE_90D_pct":-22.38,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c09_requires_customer_order_revenue_margin_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"C09 advanced-equipment rows should not promote toward Stage3-Yellow/Green unless advanced equipment strength converts into customer order, revenue conversion, margin, or capacity pull-through bridge","089030 survives with strong MFE after HBM handler order/revenue bridge; 322310 and 420770 fail when metrology/substrate inspection theme or IPO valuation lacks durable bridge","TRG_R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B|TRG_R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE|TRG_R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c09_advanced_equipment_valuation_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,1,1,0,"Advanced-equipment winners and IPO/theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 089030 positive while preventing 322310/420770 valuation blowoff false positives","TRG_R2L73_C09_089030_20240119_HBM_HANDLER_ORDER_RS_VALUATION_4B|TRG_R2L73_C09_322310_20240124_METROLOGY_VALUATION_SPIKE_WEAK_BRIDGE|TRG_R2L73_C09_420770_20230714_SUBSTRATE_INSPECTION_IPO_BLOWOFF_NO_DURABLE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["advanced_equipment_theme_without_order_bridge","IPO_valuation_blowoff_without_margin_bridge","HBM_equipment_winner_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/valuation-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C09 advanced-equipment rows cannot promote without customer order/revenue/margin bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R2
completed_loop = 73
next_round = R3
next_loop = 73
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
atlas/symbol_profiles/089/089030.json
atlas/symbol_profiles/322/322310.json
atlas/symbol_profiles/420/420770.json
atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv
atlas/ohlcv_tradable_by_symbol_year/420/420770/2023.csv
atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv
```

This loop continues loop 73 with R2 and adds 3 new independent C09 representative cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R2/L2.
