# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R2
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R3
computed_next_loop: 72
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_MEMORY_RECOVERY_CUSTOMER_CAPEX_ORDER_BRIDGE_GUARD
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

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`. Inside R2, C10 has thinner coverage than the HBM equipment/test-socket clusters and, in the No-Repeat snapshot, only 2 4B rows and 0 4C rows. This run therefore uses non-top-covered C10 symbols to test whether memory recovery equipment signals need customer capex/order/revision bridges before Yellow or Green.

| layer | id | definition |
|---|---|---|
| round | R2 | AI / semiconductor / electronics |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | semiconductors, HBM, memory, equipment, electronics |
| canonical | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | memory cycle recovery and equipment restart |
| fine | C10_MEMORY_RECOVERY_CUSTOMER_CAPEX_ORDER_BRIDGE_GUARD | recovery theme must become customer capex/order/revision |
| deep | DRAM_CAPEX_RESTART_ETCH_TOOL_REVENUE_CONVERSION | successful etch equipment bridge |
| deep | UTILITY_EQUIPMENT_THEME_WITHOUT_CONFIRMED_MEMORY_ORDER_CONVERSION | weak scrubber/chiller bridge |
| deep | TESTER_RECOVERY_THEME_WITHOUT_CUSTOMER_ORDER_VISIBILITY | weak tester false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C10 top-covered symbols are `036930`, `240810`, `084370`, `095610`, `테스`, and `000660`. This run avoids that cluster and fills new-symbol C10 memory-recovery equipment coverage.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C10 | 089970 | new independent | not top-covered C10 symbol; etch equipment order/capex bridge |
| C10 | 036200 | new independent | not top-covered C10 symbol; scrubber/chiller recovery-theme weak bridge |
| C10 | 086390 | new independent | not top-covered C10 symbol; tester recovery false start |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 089970 | 에이피티씨/브이엠 | Stage2-Actionable | 2023-05-19 | 11980 | memory etch equipment order/capex bridge worked |
| failed_rerating_high_MAE | 036200 | 유니셈 | Stage2-Actionable | 2023-03-31 | 9090 | scrubber/chiller recovery theme had weak order bridge |
| failed_rerating_low_MFE_high_MAE | 086390 | 유니테스트 | Stage2-Actionable | 2023-03-31 | 14080 | memory tester recovery false start |

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
| 089970 | 에이피티씨/브이엠 | Stage2-Actionable | 2023-05-19 | 11980 | 63.19 | 75.29 | 75.29 | -1.34 | -1.34 | -1.34 | 2023-07-21 | 21000 | -39.33 |
| 036200 | 유니셈 | Stage2-Actionable | 2023-03-31 | 9090 | 5.61 | 15.95 | 15.95 | -21.78 | -21.78 | -21.78 | 2023-07-17 | 10540 | -24.67 |
| 086390 | 유니테스트 | Stage2-Actionable | 2023-03-31 | 14080 | 5.89 | 11.01 | 11.01 | -15.27 | -15.27 | -15.27 | 2023-06-20 | 15630 | -12.28 |

## 9. Case-by-Case Notes

### 9.1 089970 / 에이피티씨·브이엠 — memory etch equipment order recovery positive

The entry row is 2023-05-19 at 11,980. The path reaches 19,550 within the first 30-trading-day window and 21,000 by the later window. This is the C10 success condition: the memory recovery signal is not merely a theme; it walks into etch-equipment order/customer-capex visibility.

### 9.2 036200 / 유니셈 — scrubber/chiller recovery theme with weak order bridge

The entry row is 2023-03-31 at 9,090. The path eventually reaches 10,540, but only after a deep early drawdown to 7,110. This is not a clean Yellow/Green case. The equipment category sits near the memory recovery breeze, but the non-price bridge is too weak and MAE arrives before durable MFE.

### 9.3 086390 / 유니테스트 — memory tester recovery false start

The entry row is 2023-03-31 at 14,080. The 90D high reaches 15,630, while 30D/90D MAE reaches -15.27%. This is a false-start shape: the tester recovery theme made a little flame, but without customer order/revision visibility it did not become a furnace.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C10 treats memory-recovery theme/relative strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C10 should require customer capex/order/revision bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for low-MFE/high-MAE recovery-theme rows. |
| Full 4B non-price requirement appropriate? | Yes. 089970 has non-price bridge; 036200/086390 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
089970:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer capex/order bridge
  Stage3-Green = wait for stronger revision/FCF durability and 4B risk check

036200:
  Stage2-Actionable = too generous if based only on memory recovery theme
  Stage3-Yellow = reject without customer order/revenue bridge
  Stage3-Green = reject

086390:
  Stage2-Actionable = too generous if based only on tester recovery theme
  Stage3-Yellow = reject without order/revision visibility
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 089970 | 0.96 | 1.00 | good full-window 4B watch after order recovery bridge |
| 036200 | 0.86 | 1.00 | weak MFE/high MAE local 4B watch only |
| 086390 | 0.91 | 1.00 | low MFE/high MAE watch, not full cycle success |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c10_requires_customer_capex_order_revision_bridge

rule:
  For C10 memory recovery equipment rows, do not promote recovery-theme or relative-strength
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  customer capex restart, signed/credible order, order-to-revenue visibility,
  earnings revision, or repeat equipment demand.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 34.08 | -12.8 | 66.7% | too generous to weak recovery-theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 34.08 | -12.8 | 33.3% | safer but may miss 089970 |
| P1 sector_specific_candidate_profile | 3 | 34.08 | -12.8 | 66.7% | no broad L2 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 75.29 | -1.34 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 13.48 | -18.52 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 089970 | current_profile_correct | equipment order/capex bridge aligned with strong MFE |
| 036200 | current_profile_false_positive | recovery theme produced high MAE before durable MFE |
| 086390 | current_profile_false_positive | tester recovery theme produced shallow MFE and meaningful MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_MEMORY_RECOVERY_CUSTOMER_CAPEX_ORDER_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C10 non-top-covered memory recovery equipment residual reduced |

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
- memory recovery theme without customer order bridge
- low MFE / high MAE false start
- successful etch equipment recovery still needs 4B watch
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
shadow_weight,c10_requires_customer_capex_order_revision_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 memory recovery/equipment rows should not promote toward Stage3-Yellow/Green unless recovery theme converts into customer capex, order, revenue, or revision bridge","089970 survives with strong MFE; 036200 and 086390 show weak MFE/high MAE when bridge is absent","TRG_R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY|TRG_R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE|TRG_R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c10_recovery_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,1,1,0,"Memory recovery equipment rows can peak quickly or fail before revision confirmation; local 4B/high-MAE watch should stay active","preserves 089970 positive while preventing 036200/086390 recovery-theme false positives","TRG_R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY|TRG_R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE|TRG_R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY","symbol":"089970","company_name":"에이피티씨/브이엠","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY_BRIDGE","deep_sub_archetype_id":"DRAM_CAPEX_RESTART_ETCH_TOOL_REVENUE_CONVERSION","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C10 memory recovery/equipment rows require customer capex/order/revision bridge; recovery-theme relative strength alone is insufficient."}
{"row_type":"case","case_id":"R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE","symbol":"036200","company_name":"유니셈","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_CHILLER_SCRUBBER_MEMORY_RECOVERY_WEAK_ORDER_BRIDGE","deep_sub_archetype_id":"UTILITY_EQUIPMENT_THEME_WITHOUT_CONFIRMED_MEMORY_ORDER_CONVERSION","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C10 memory recovery/equipment rows require customer capex/order/revision bridge; recovery-theme relative strength alone is insufficient."}
{"row_type":"case","case_id":"R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START","symbol":"086390","company_name":"유니테스트","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_RECOVERY_FALSE_START_GUARD","deep_sub_archetype_id":"TESTER_RECOVERY_THEME_WITHOUT_CUSTOMER_ORDER_VISIBILITY","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C10 memory recovery/equipment rows require customer capex/order/revision bridge; recovery-theme relative strength alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY","case_id":"R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY","symbol":"089970","company_name":"에이피티씨/브이엠","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY_BRIDGE","deep_sub_archetype_id":"DRAM_CAPEX_RESTART_ETCH_TOOL_REVENUE_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-19","entry_date":"2023-05-19","entry_price":11980,"evidence_available_at_that_date":"source_proxy_memory_capex_restart_etch_equipment_order_bridge; evidence_url_pending","evidence_source":"source_proxy_memory_capex_restart_etch_equipment_order_bridge; evidence_url_pending","bridge_summary":"memory capex restart/etch equipment order bridge converted into a strong 30D/90D MFE path","stage2_evidence_fields":["memory_capex_restart_proxy","etch_equipment_order_bridge","relative_strength","customer_capex_visibility"],"stage3_evidence_fields":["order_to_revenue_visibility","non_price_customer_capex_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","valuation_repricing_after_cycle_recovery"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089970/2023.csv|atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv","profile_path":"atlas/symbol_profiles/089/089970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":63.19,"MFE_90D_pct":75.29,"MFE_180D_pct":75.29,"MFE_1Y_pct":75.29,"MFE_2Y_pct":75.29,"MAE_30D_pct":-1.34,"MAE_90D_pct":-1.34,"MAE_180D_pct":-1.34,"MAE_1Y_pct":-1.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-21","peak_price":21000,"drawdown_after_peak_pct":-39.33,"green_lateness_ratio":"0.26","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_order_recovery_bridge","four_b_evidence_type":"non_price_order_capex_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE","case_id":"R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE","symbol":"036200","company_name":"유니셈","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_CHILLER_SCRUBBER_MEMORY_RECOVERY_WEAK_ORDER_BRIDGE","deep_sub_archetype_id":"UTILITY_EQUIPMENT_THEME_WITHOUT_CONFIRMED_MEMORY_ORDER_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-31","entry_date":"2023-03-31","entry_price":9090,"evidence_available_at_that_date":"source_proxy_chiller_scrubber_memory_recovery_theme_without_confirmed_order_bridge; evidence_url_pending","evidence_source":"source_proxy_chiller_scrubber_memory_recovery_theme_without_confirmed_order_bridge; evidence_url_pending","bridge_summary":"memory recovery theme appeared, but chiller/scrubber order conversion was not strong enough to avoid high MAE","stage2_evidence_fields":["memory_recovery_theme","utility_equipment_relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_peak_watch","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_order_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036200/2023.csv","profile_path":"atlas/symbol_profiles/036/036200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.61,"MFE_90D_pct":15.95,"MFE_180D_pct":15.95,"MFE_1Y_pct":15.95,"MFE_2Y_pct":15.95,"MAE_30D_pct":-21.78,"MAE_90D_pct":-21.78,"MAE_180D_pct":-21.78,"MAE_1Y_pct":-21.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":10540,"drawdown_after_peak_pct":-24.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_MFE_high_MAE_local_4B_watch_only","four_b_evidence_type":"weak_recovery_theme_or_price_only","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START","case_id":"R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START","symbol":"086390","company_name":"유니테스트","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_TESTER_RECOVERY_FALSE_START_GUARD","deep_sub_archetype_id":"TESTER_RECOVERY_THEME_WITHOUT_CUSTOMER_ORDER_VISIBILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-31","entry_date":"2023-03-31","entry_price":14080,"evidence_available_at_that_date":"source_proxy_memory_tester_recovery_theme_without_customer_order_visibility; evidence_url_pending","evidence_source":"source_proxy_memory_tester_recovery_theme_without_customer_order_visibility; evidence_url_pending","bridge_summary":"tester recovery theme lacked customer order/revision visibility, producing only shallow MFE with meaningful MAE","stage2_evidence_fields":["memory_tester_recovery_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","low_MFE_high_MAE_watch"],"stage4c_evidence_fields":["bridge_absent_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086390/2023.csv","profile_path":"atlas/symbol_profiles/086/086390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.89,"MFE_90D_pct":11.01,"MFE_180D_pct":11.01,"MFE_1Y_pct":11.01,"MFE_2Y_pct":11.01,"MAE_30D_pct":-15.27,"MAE_90D_pct":-15.27,"MAE_180D_pct":-15.27,"MAE_1Y_pct":-15.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-20","peak_price":15630,"drawdown_after_peak_pct":-12.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_MFE_high_MAE_watch_not_full_cycle_success","four_b_evidence_type":"weak_recovery_theme_or_price_only","four_c_protection_label":"bridge_absent_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY","trigger_id":"TRG_R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY","symbol":"089970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_recovery_score":11,"equipment_order_bridge_score":12,"customer_capex_visibility_score":10,"revision_score":8,"relative_strength_score":12,"risk_penalty":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_recovery_score":10,"equipment_order_bridge_score":16,"customer_capex_visibility_score":14,"revision_score":10,"relative_strength_score":10,"risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["memory_recovery_score","equipment_order_bridge_score","customer_capex_visibility_score","revision_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C10 memory recovery row is promoted only because recovery theme converts into equipment order/customer capex bridge.","MFE_90D_pct":75.29,"MAE_90D_pct":-1.34,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE","trigger_id":"TRG_R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE","symbol":"036200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_recovery_score":10,"equipment_order_bridge_score":2,"customer_capex_visibility_score":2,"revision_score":2,"relative_strength_score":10,"risk_penalty":7},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_recovery_score":5,"equipment_order_bridge_score":0,"customer_capex_visibility_score":0,"revision_score":1,"relative_strength_score":5,"risk_penalty":13},"weighted_score_after":44,"stage_label_after":"Stage1-Watch","changed_components":["memory_recovery_score","equipment_order_bridge_score","customer_capex_visibility_score","revision_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C10 guard demotes recovery-theme equipment rows without customer order/revision bridge.","MFE_90D_pct":15.95,"MAE_90D_pct":-21.78,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START","trigger_id":"TRG_R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START","symbol":"086390","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_recovery_score":10,"equipment_order_bridge_score":2,"customer_capex_visibility_score":2,"revision_score":2,"relative_strength_score":10,"risk_penalty":7},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_recovery_score":5,"equipment_order_bridge_score":0,"customer_capex_visibility_score":0,"revision_score":1,"relative_strength_score":5,"risk_penalty":13},"weighted_score_after":44,"stage_label_after":"Stage1-Watch","changed_components":["memory_recovery_score","equipment_order_bridge_score","customer_capex_visibility_score","revision_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C10 guard demotes recovery-theme equipment rows without customer order/revision bridge.","MFE_90D_pct":11.01,"MAE_90D_pct":-15.27,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c10_requires_customer_capex_order_revision_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 memory recovery/equipment rows should not promote toward Stage3-Yellow/Green unless recovery theme converts into customer capex, order, revenue, or revision bridge","089970 survives with strong MFE; 036200 and 086390 show weak MFE/high MAE when bridge is absent","TRG_R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY|TRG_R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE|TRG_R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c10_recovery_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,1,1,0,"Memory recovery equipment rows can peak quickly or fail before revision confirmation; local 4B/high-MAE watch should stay active","preserves 089970 positive while preventing 036200/086390 recovery-theme false positives","TRG_R2L72_C10_089970_20230519_MEMORY_ETCH_EQUIPMENT_ORDER_RECOVERY|TRG_R2L72_C10_036200_20230331_CHILLER_SCRUBBER_RECOVERY_WEAK_BRIDGE|TRG_R2L72_C10_086390_20230331_MEMORY_TESTER_RECOVERY_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["memory_recovery_theme_without_customer_order_bridge","low_MFE_high_MAE_false_start","successful_etch_equipment_recovery_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

## 22. Next Round State

```text
completed_round = R2
completed_loop = 72
next_round = R3
next_loop = 72
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
atlas/symbol_profiles/089/089970.json
atlas/symbol_profiles/036/036200.json
atlas/symbol_profiles/086/086390.json
atlas/ohlcv_tradable_by_symbol_year/089/089970/2023.csv
atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv
atlas/ohlcv_tradable_by_symbol_year/036/036200/2023.csv
atlas/ohlcv_tradable_by_symbol_year/086/086390/2023.csv
```

This loop adds 3 new independent C10 cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R2/L2.
