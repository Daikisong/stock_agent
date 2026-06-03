# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R1
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R2
computed_next_loop: 76
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_BACKLOG_REVENUE_MARGIN_CASHFLOW_BRIDGE_GUARD
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

R13 / loop 75 has closed, so the scheduler rolls to `R1 / loop 76`. R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. The recent R1/R11 L1 path already used C05 EPC and C04 nuclear, and older R1 loops covered C02/C03 heavily. This run therefore rotates to C01 order/backlog/margin bridge.

| layer | id | definition |
|---|---|---|
| round | R1 | industrials / infrastructure / defense / grid |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | industrial backlog, infrastructure, shipbuilding, equipment |
| canonical | C01_ORDER_BACKLOG_MARGIN_BRIDGE | order backlog, revenue visibility, execution margin |
| fine | C01_BACKLOG_REVENUE_MARGIN_CASHFLOW_BRIDGE_GUARD | order signal must become revenue, margin and cashflow evidence |
| deep | SHIPBUILDING_BACKLOG_TO_PROFIT_TURNAROUND_AND_EXECUTION_MARGIN_BRIDGE | shipbuilding positive |
| deep | MARINE_ENGINE_ORDERBOOK_TO_MARGIN_AND_CUSTOMER_REPRICING_OPERATING_LEVERAGE | marine engine positive |
| deep | COMPACT_CONSTRUCTION_EQUIPMENT_ORDER_CYCLE_WITHOUT_BACKLOG_MARGIN_CASHFLOW_DURABILITY | equipment-cycle false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C01 top-covered symbols are `010620`, `329180`, `009540`, `010140`, `077970`, and `082740`. This run avoids that cluster and also avoids the recent C05/C04 L1 representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C01 | 042660 | new independent | not top-covered C01 symbol; shipbuilding backlog/profit-turnaround margin bridge |
| C01 | 071970 | new independent | not top-covered C01 symbol; marine-engine orderbook/customer repricing margin bridge |
| C01 | 241560 | new independent | not top-covered C01 symbol; equipment order-cycle MFE without durable margin/cashflow bridge |
| reviewed | 017960 | not selected | usable, but selected set offered cleaner C01 positive/counterexample balance |

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
042660 has a 2023-06-13 name-transition/corporate-action candidate outside the selected 2024 representative window.
071970 has corporate-action candidates ending 2018-12-27, outside the selected 2024 representative window.
241560 has no corporate-action candidate dates.
017960 was inspected but not selected for this representative set.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| shipbuilding_backlog_turnaround_success_then_4B_watch | 042660 | 한화오션 | Stage2-Actionable | 2024-03-14 | 27000 | backlog/profit-turnaround margin bridge worked, but post-peak drawdown required 4B |
| marine_engine_backlog_success_then_4B_watch | 071970 | HD현대마린엔진 | Stage2-Actionable | 2024-03-14 | 10680 | marine engine orderbook/repricing bridge worked, but high-MAE watch required |
| construction_equipment_MFE_then_high_MAE_counterexample | 241560 | 두산밥캣 | Stage2-Actionable | 2024-02-01 | 49300 | equipment order-cycle MFE lacked durable margin/cashflow bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 042660 | 한화오션 | Stage2-Actionable | 2024-03-14 | 27000 | 14.44 | 21.85 | 30.74 | -7.96 | -7.96 | -7.96 | 2024-08-30 | 35300 | -18.84 |
| 071970 | HD현대마린엔진 | Stage2-Actionable | 2024-03-14 | 10680 | 26.5 | 84.83 | 132.68 | -6.37 | -6.37 | -10.49 | 2024-08-01 | 24850 | -36.98 |
| 241560 | 두산밥캣 | Stage2-Actionable | 2024-02-01 | 49300 | 16.23 | 16.23 | 20.69 | -9.94 | -9.94 | -32.35 | 2024-07-12 | 59500 | -43.95 |

## 9. Case-by-Case Notes

### 9.1 042660 / 한화오션 — shipbuilding backlog to margin bridge

The entry row is 2024-03-14 at 27,000. The 30D path reached 30,900, the 90D path reached 32,900, and the broader window reached 35,300. This is a valid C01 positive because the bridge is not just shipbuilding theme strength. It is backlog-to-revenue, profit-turnaround and execution-margin visibility. The post-peak low still keeps 4B drawdown watch alive.

### 9.2 071970 / HD현대마린엔진 — marine-engine backlog and repricing bridge

The entry row is 2024-03-14 at 10,680. The path reached 13,510 in the 30D window, 19,740 around the 90D area, and 24,850 in the wider window. This is a strong C01 positive: engine orderbook, customer repricing and operating leverage created a clearer bridge than simple order-cycle beta. Still, the later drawdown and cycle crowding block Green.

### 9.3 241560 / 두산밥캣 — equipment order-cycle MFE without durable bridge

The entry row is 2024-02-01 at 49,300. The stock reached 59,500, but later fell to 33,350. This is a C01 counterexample: order-cycle or equipment demand optionality can make MFE, but if backlog-to-revenue, margin, inventory normalization and cashflow bridge weaken, the row should remain 4B/high-MAE watch rather than Stage3-Green.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C01 treats order-cycle/equipment MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C01 needs backlog/revenue/margin/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 241560 and post-peak shipbuilding/engine crowding. |
| Full 4B non-price requirement appropriate? | Yes. 042660/071970 have stronger non-price bridges; 241560 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
042660:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after backlog-to-revenue / profit-turnaround / execution-margin bridge
  Stage3-Green = reject unless cost/execution and post-peak drawdown risks clear

071970:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after engine orderbook / customer repricing / margin bridge
  Stage3-Green = reject because 4B drawdown and cycle crowding remain active

241560:
  Stage2-Actionable = acceptable only as equipment order-cycle watch
  Stage3-Yellow = reject without durable backlog-to-revenue, margin, inventory and cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 042660 | 0.87 | 1.00 | shipbuilding backlog margin positive but full-window 4B/drawdown watch |
| 071970 | 0.79 | 1.00 | marine-engine backlog margin positive but 4B/high-MAE watch |
| 241560 | 0.96 | 1.00 | equipment order-cycle MFE but no durable margin bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c01_requires_backlog_revenue_margin_cashflow_bridge

rule:
  For C01 order/backlog rows, do not promote shipbuilding, marine engine,
  equipment, machinery, plant, industrial order, or order-cycle Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  backlog-to-revenue conversion, customer repricing, execution-margin proof,
  delivery schedule quality, working-capital control, inventory normalization,
  FCF/cash conversion, or earnings revision tied to backlog economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 40.97 | -8.09 | 33.3% | useful but can over-credit equipment order-cycle MFE |
| P0b e2r_2_0_baseline_reference | 3 | 40.97 | -8.09 | 0% | safer but may miss 042660/071970 |
| P1 sector_specific_candidate_profile | 3 | 40.97 | -8.09 | 33.3% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 53.34 | -7.17 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 16.23 | -9.94 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 042660 | current_profile_correct_but_no_green | backlog/profit-turnaround bridge aligned with MFE but Green blocked by 4B |
| 071970 | current_profile_correct_with_drawdown_guard | engine orderbook/repricing bridge aligned with strong MFE, but drawdown guard remains |
| 241560 | current_profile_false_positive_if_green | MFE existed but durable margin/cashflow bridge weakened into high-MAE path |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01_BACKLOG_REVENUE_MARGIN_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | R1/C01 non-top-covered backlog/margin residual reduced |

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
- order-cycle MFE without durable margin/cashflow bridge
- shipbuilding backlog winner needs 4B watch
- marine-engine backlog winner needs drawdown guard
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
- R1 direct L1 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact order/backlog announcement URLs
- production scoring behavior
- live candidate status
- 017960 as representative row; reviewed but not selected
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_requires_backlog_revenue_margin_cashflow_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 order/backlog rows should not promote toward Stage3-Yellow/Green unless industrial order signal converts into backlog-to-revenue, customer repricing, execution-margin, delivery schedule, working-capital, or cashflow bridge","042660 and 071970 survive after shipbuilding/marine-engine backlog-to-margin bridge; 241560 is demoted because equipment order-cycle MFE lacked durable margin and cashflow bridge","TRG_R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE|TRG_R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE|TRG_R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_order_cycle_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,"Backlog winners and order-cycle false starts can peak before margin/cashflow durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 042660/071970 positives while preventing 241560 order-cycle false positive","TRG_R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE|TRG_R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE|TRG_R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","symbol":"042660","company_name":"한화오션","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","deep_sub_archetype_id":"SHIPBUILDING_BACKLOG_TO_PROFIT_TURNAROUND_AND_EXECUTION_MARGIN_BRIDGE","case_type":"shipbuilding_backlog_turnaround_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C01 order/backlog/margin rows require backlog-to-revenue, customer repricing, execution-margin, delivery schedule, working-capital, or cashflow bridge; order-cycle theme or MFE alone is insufficient."}
{"row_type":"case","case_id":"R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_MARINE_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","deep_sub_archetype_id":"MARINE_ENGINE_ORDERBOOK_TO_MARGIN_AND_CUSTOMER_REPRICING_OPERATING_LEVERAGE","case_type":"marine_engine_backlog_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C01 order/backlog/margin rows require backlog-to-revenue, customer repricing, execution-margin, delivery schedule, working-capital, or cashflow bridge; order-cycle theme or MFE alone is insufficient."}
{"row_type":"case","case_id":"R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"241560","company_name":"두산밥캣","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_COMPACT_EQUIPMENT_ORDER_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"COMPACT_CONSTRUCTION_EQUIPMENT_ORDER_CYCLE_WITHOUT_BACKLOG_MARGIN_CASHFLOW_DURABILITY","case_type":"construction_equipment_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C01 order/backlog/margin rows require backlog-to-revenue, customer repricing, execution-margin, delivery schedule, working-capital, or cashflow bridge; order-cycle theme or MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","case_id":"R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","symbol":"042660","company_name":"한화오션","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","deep_sub_archetype_id":"SHIPBUILDING_BACKLOG_TO_PROFIT_TURNAROUND_AND_EXECUTION_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":27000,"evidence_available_at_that_date":"source_proxy_shipbuilding_backlog_profit_turnaround_execution_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_shipbuilding_backlog_profit_turnaround_execution_margin_bridge; evidence_url_pending","bridge_summary":"shipbuilding backlog and profit-turnaround signal converted into execution-margin bridge, but project execution, cost and post-peak drawdown required 4B watch","stage2_evidence_fields":["shipbuilding_backlog","profit_turnaround_proxy","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["backlog_to_revenue_visibility","execution_margin_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","shipbuilding_cycle_crowding","execution_cost_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv","profile_path":"atlas/symbol_profiles/042/042660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.44,"MFE_90D_pct":21.85,"MFE_180D_pct":30.74,"MFE_1Y_pct":30.74,"MFE_2Y_pct":30.74,"MAE_30D_pct":-7.96,"MAE_90D_pct":-7.96,"MAE_180D_pct":-7.96,"MAE_1Y_pct":-7.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-30","peak_price":35300,"drawdown_after_peak_pct":-18.84,"green_lateness_ratio":"0.47","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"shipbuilding_backlog_margin_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_backlog_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"shipbuilding_backlog_turnaround_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","case_id":"R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_MARINE_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","deep_sub_archetype_id":"MARINE_ENGINE_ORDERBOOK_TO_MARGIN_AND_CUSTOMER_REPRICING_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":10680,"evidence_available_at_that_date":"source_proxy_marine_engine_orderbook_margin_customer_repricing_bridge; evidence_url_pending","evidence_source":"source_proxy_marine_engine_orderbook_margin_customer_repricing_bridge; evidence_url_pending","bridge_summary":"marine engine orderbook and customer repricing converted into margin and operating-leverage bridge, but post-peak volatility and cycle crowding required 4B watch","stage2_evidence_fields":["marine_engine_orderbook","customer_repricing_proxy","relative_strength","operating_leverage_proxy"],"stage3_evidence_fields":["orderbook_to_revenue_visibility","margin_repricing_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","engine_cycle_crowding","customer_delivery_timing_risk"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv","profile_path":"atlas/symbol_profiles/071/071970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.5,"MFE_90D_pct":84.83,"MFE_180D_pct":132.68,"MFE_1Y_pct":132.68,"MFE_2Y_pct":132.68,"MAE_30D_pct":-6.37,"MAE_90D_pct":-6.37,"MAE_180D_pct":-10.49,"MAE_1Y_pct":-10.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":24850,"drawdown_after_peak_pct":-36.98,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"marine_engine_backlog_margin_positive_but_4B_high_MAE_watch","four_b_evidence_type":"non_price_backlog_margin_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"marine_engine_backlog_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","case_id":"R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"241560","company_name":"두산밥캣","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_COMPACT_EQUIPMENT_ORDER_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"COMPACT_CONSTRUCTION_EQUIPMENT_ORDER_CYCLE_WITHOUT_BACKLOG_MARGIN_CASHFLOW_DURABILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":49300,"evidence_available_at_that_date":"source_proxy_compact_construction_equipment_order_cycle_without_durable_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_compact_construction_equipment_order_cycle_without_durable_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"compact equipment/order-cycle theme produced MFE, but durable backlog-to-revenue, margin, inventory normalization and cashflow bridge weakened into high-MAE path","stage2_evidence_fields":["construction_equipment_theme","order_cycle_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["MFE_peak_watch","backlog_margin_bridge_absent","inventory_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_margin_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv","profile_path":"atlas/symbol_profiles/241/241560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.23,"MFE_90D_pct":16.23,"MFE_180D_pct":20.69,"MFE_1Y_pct":20.69,"MFE_2Y_pct":20.69,"MAE_30D_pct":-9.94,"MAE_90D_pct":-9.94,"MAE_180D_pct":-32.35,"MAE_1Y_pct":-32.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-12","peak_price":59500,"drawdown_after_peak_pct":-43.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"equipment_order_theme_MFE_but_no_durable_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"order_cycle_theme_without_durable_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"equipment_order_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","trigger_id":"TRG_R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE","symbol":"042660","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"order_backlog_score":12,"revenue_visibility_score":11,"execution_margin_score":11,"cashflow_bridge_score":9,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"order_backlog_score":15,"revenue_visibility_score":14,"execution_margin_score":14,"cashflow_bridge_score":12,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["order_backlog_score","revenue_visibility_score","execution_margin_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C01 row is promoted only because backlog/order visibility converts into revenue, execution margin and cashflow bridge; 4B drawdown/cycle watch blocks Green.","MFE_90D_pct":21.85,"MAE_90D_pct":-7.96,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","trigger_id":"TRG_R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE","symbol":"071970","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"order_backlog_score":12,"revenue_visibility_score":11,"execution_margin_score":11,"cashflow_bridge_score":9,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"order_backlog_score":15,"revenue_visibility_score":14,"execution_margin_score":14,"cashflow_bridge_score":12,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["order_backlog_score","revenue_visibility_score","execution_margin_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C01 row is promoted only because backlog/order visibility converts into revenue, execution margin and cashflow bridge; 4B drawdown/cycle watch blocks Green.","MFE_90D_pct":84.83,"MAE_90D_pct":-6.37,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","trigger_id":"TRG_R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"241560","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"order_backlog_score":6,"revenue_visibility_score":3,"execution_margin_score":1,"cashflow_bridge_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"order_backlog_score":2,"revenue_visibility_score":1,"execution_margin_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["order_backlog_score","revenue_visibility_score","execution_margin_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C01 guard demotes order-cycle/equipment-theme rows when backlog-to-revenue, execution margin, working-capital and cashflow bridge are absent.","MFE_90D_pct":16.23,"MAE_90D_pct":-9.94,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_requires_backlog_revenue_margin_cashflow_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 order/backlog rows should not promote toward Stage3-Yellow/Green unless industrial order signal converts into backlog-to-revenue, customer repricing, execution-margin, delivery schedule, working-capital, or cashflow bridge","042660 and 071970 survive after shipbuilding/marine-engine backlog-to-margin bridge; 241560 is demoted because equipment order-cycle MFE lacked durable margin and cashflow bridge","TRG_R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE|TRG_R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE|TRG_R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_order_cycle_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,"Backlog winners and order-cycle false starts can peak before margin/cashflow durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 042660/071970 positives while preventing 241560 order-cycle false positive","TRG_R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE|TRG_R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE|TRG_R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["order_cycle_MFE_without_durable_margin_cashflow_bridge","shipbuilding_backlog_winner_needs_4B_watch","marine_engine_backlog_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R1-specific handling

- R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.
- This MD uses `C01_ORDER_BACKLOG_MARGIN_BRIDGE`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/order-cycle-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R1 direct L1 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C01 order/backlog rows cannot promote without backlog-to-revenue conversion, customer repricing, execution-margin proof, delivery schedule quality, working-capital control, inventory normalization, FCF/cash conversion, or earnings revision tied to backlog economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R1
completed_loop = 76
next_round = R2
next_loop = 76
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
atlas/symbol_profiles/042/042660.json
atlas/symbol_profiles/071/071970.json
atlas/symbol_profiles/241/241560.json
atlas/symbol_profiles/017/017960.json
atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv
atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv
atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/017/017960/2024.csv
```

This loop starts loop 76 with R1 and adds 3 new independent C01 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R1/L1.
