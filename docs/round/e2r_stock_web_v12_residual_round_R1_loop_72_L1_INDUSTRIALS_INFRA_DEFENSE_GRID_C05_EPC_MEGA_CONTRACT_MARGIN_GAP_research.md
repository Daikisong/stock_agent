# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R1
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R2
computed_next_loop: 72
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: C05_EPC_PLANT_ORDER_MARGIN_WORKING_CAPITAL_BRIDGE_GUARD
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

R13 / Loop 71 has closed, so the scheduler rolls to `R1 / Loop 72`. R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. Inside R1, C05 has thin coverage versus C02/C03 and has a meaningful error mode: EPC or plant contract size can look impressive while margin, working capital, and revenue conversion remain weak.

| layer | id | definition |
|---|---|---|
| round | R1 | industrials / infrastructure / defense / grid |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | infrastructure, plant, defense, power/grid industrials |
| canonical | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC / plant contract amount versus margin and working-capital conversion |
| fine | C05_EPC_PLANT_ORDER_MARGIN_WORKING_CAPITAL_BRIDGE_GUARD | contract/order must become revenue, margin, and cash conversion |
| deep | HEAT_EXCHANGER_EXPORT_ORDER_TO_MARGIN_BRIDGE | plant equipment order conversion |
| deep | BOILER_HRSG_ORDER_TO_REVENUE_BUT_PEAK_RISK | plant equipment order plus 4B drawdown watch |
| deep | PLANT_ENGINEERING_CONTRACT_HEADLINE_WITH_WORKING_CAPITAL_RISK | contract headline false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C05 top-covered symbols are `006360`, `047040`, `000720`, `028050`, `375500`, and `034300`. This run avoids that cluster and fills new-symbol C05 plant/EPC bridge evidence.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C05 | 100840 | new independent | not top-covered C05 symbol; plant equipment order/margin bridge |
| C05 | 083650 | new independent | not top-covered C05 symbol; power-plant boiler order bridge with 4B watch |
| C05 | 023960 | new independent | not top-covered C05 symbol; engineering contract headline counterexample |

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
| structural_success | 100840 | SNT에너지 | Stage2-Actionable | 2023-04-21 | 21800 | plant equipment order/margin conversion worked |
| structural_success_with_4B_drawdown_watch | 083650 | 비에이치아이 | Stage2-Actionable | 2023-03-31 | 7720 | power-plant boiler/order bridge worked, but 4B/high-MAE guard needed |
| failed_rerating_high_MAE | 023960 | 에쓰씨엔지니어링 | Stage2-Actionable | 2023-04-21 | 2695 | EPC contract headline without margin/working-capital bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 100840 | SNT에너지 | Stage2-Actionable | 2023-04-21 | 21800 | 13.3 | 13.76 | 50.0 | -7.11 | -8.26 | -8.26 | 2023-10-23 | 32700 | -39.33 |
| 083650 | 비에이치아이 | Stage2-Actionable | 2023-03-31 | 7720 | 38.08 | 51.17 | 51.17 | -10.23 | -14.64 | -14.64 | 2023-07-14 | 11670 | -43.53 |
| 023960 | 에쓰씨엔지니어링 | Stage2-Actionable | 2023-04-21 | 2695 | 43.23 | 43.23 | 43.23 | -25.79 | -38.78 | -38.78 | 2023-05-15 | 3860 | -57.25 |

## 9. Case-by-Case Notes

### 9.1 100840 / SNT에너지 — plant equipment order to margin conversion

The entry row is 2023-04-21 at 21,800. The path is not a one-day spike; it travels slowly and eventually reaches 32,700. This is the cleanest C05 positive in this run because the evidence family is not just “large order” but order-to-revenue and margin conversion.

### 9.2 083650 / 비에이치아이 — power-plant equipment bridge with 4B watch

The entry row is 2023-03-31 at 7,720. The price path reaches 11,670, but the post-peak drawdown is deep. This validates the order bridge but argues that C05 winners still need 4B/high-MAE watch; the contract/order is the match, but margin conversion is the oxygen.

### 9.3 023960 / 에쓰씨엔지니어링 — contract headline without durable margin bridge

The entry row is 2023-04-21 at 2,695. The path reaches 3,860, but MAE expands to -38.78% and drawdown after peak reaches -57.25%. This is the C05 trap: contract amount looks like a door opening, but if working capital and margin quality do not walk through, the door shuts hard.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C05 treats EPC contract amount / price spike as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C05 needs margin + working-capital + order-to-revenue bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes for 023960 and as watch discipline after 083650/100840 peaks. |
| Full 4B non-price requirement appropriate? | Yes. 100840/083650 have non-price order bridge; 023960 is headline/price-heavy. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
100840:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after order-to-revenue / margin bridge
  Stage3-Green = wait for stronger FCF and margin durability

083650:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with 4B/high-MAE watch active
  Stage3-Green = reject unless margin durability clears drawdown risk

023960:
  Stage2-Actionable = too generous if based on contract headline and price spike
  Stage3-Yellow = reject without margin/working-capital bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 100840 | 0.88 | 1.00 | good full-window 4B watch after order/margin conversion |
| 083650 | 0.93 | 1.00 | good full-window 4B watch but requires drawdown guard |
| 023960 | 1.00 | 1.00 | price-only or margin-weak local 4B watch, not full positive 4B |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c05_requires_margin_working_capital_order_to_revenue_bridge

rule:
  For C05 EPC/plant contract rows, do not promote contract headline or order amount
  from Stage2-Actionable into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  margin conversion, working-capital containment, order-to-revenue schedule,
  credible customer/project quality, or FCF/cash collection evidence.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 36.05 | -20.56 | 33.3% | useful but can over-credit EPC headline/price spike |
| P0b e2r_2_0_baseline_reference | 3 | 36.05 | -20.56 | 0% | safer but may miss plant equipment bridge winners |
| P1 sector_specific_candidate_profile | 3 | 36.05 | -20.56 | 33.3% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 32.47 | -11.45 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 43.23 | -38.78 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 100840 | current_profile_correct | order/margin bridge aligned with strong 180D MFE |
| 083650 | current_profile_partially_correct | order bridge worked, but 4B/high-MAE watch is mandatory |
| 023960 | current_profile_false_positive | contract headline produced MFE but later high MAE/drawdown |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05_EPC_PLANT_ORDER_MARGIN_WORKING_CAPITAL_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C05 non-top-covered plant/EPC margin-bridge residual reduced |

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
- contract headline without margin bridge
- plant order success needs 4B watch
- EPC working-capital high-MAE after price spike
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
shadow_weight,c05_requires_margin_working_capital_order_to_revenue_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"C05 EPC/plant rows should not promote toward Stage3-Yellow/Green unless contract/order amount converts into margin, working-capital, and revenue visibility","100840 and 083650 survive because plant equipment/order bridge exists; 023960 fails as contract headline/price spike without margin bridge","TRG_R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION|TRG_R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B|TRG_R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c05_contract_headline_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,1,1,0,"C05 winners and failures can peak quickly; local/full-window 4B watch must stay separate from positive Stage3 evidence","preserves 100840/083650 positives while preventing 023960 contract-headline false positive","TRG_R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION|TRG_R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B|TRG_R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch behavior without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","symbol":"100840","company_name":"SNT에너지","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","deep_sub_archetype_id":"HEAT_EXCHANGER_EXPORT_ORDER_TO_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C05 EPC/plant-engineering rows require margin, working-capital, and order-to-revenue bridge; headline contract amount alone is insufficient."}
{"row_type":"case","case_id":"R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B","symbol":"083650","company_name":"비에이치아이","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_POWER_PLANT_BOILER_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"BOILER_HRSG_ORDER_TO_REVENUE_BUT_PEAK_RISK","case_type":"structural_success_with_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C05 EPC/plant-engineering rows require margin, working-capital, and order-to-revenue bridge; headline contract amount alone is insufficient."}
{"row_type":"case","case_id":"R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK","symbol":"023960","company_name":"에쓰씨엔지니어링","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_AMOUNT_HIGH_MARGIN_WEAK_BRIDGE","deep_sub_archetype_id":"PLANT_ENGINEERING_CONTRACT_HEADLINE_WITH_WORKING_CAPITAL_RISK","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C05 EPC/plant-engineering rows require margin, working-capital, and order-to-revenue bridge; headline contract amount alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","case_id":"R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","symbol":"100840","company_name":"SNT에너지","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","deep_sub_archetype_id":"HEAT_EXCHANGER_EXPORT_ORDER_TO_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-21","entry_date":"2023-04-21","entry_price":21800,"evidence_available_at_that_date":"source_proxy_plant_equipment_order_and_margin_conversion; evidence_url_pending","evidence_source":"source_proxy_plant_equipment_order_and_margin_conversion; evidence_url_pending","bridge_summary":"plant equipment/order backlog translated into margin/earnings visibility, not merely a contract headline","stage2_evidence_fields":["plant_equipment_order","export_or_customer_quality","relative_strength","margin_conversion_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","margin_bridge","non_price_contract_quality"],"stage4b_evidence_fields":["post_repricing_valuation_watch","local_overheat_after_order_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/100/100840/2023.csv|atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv","profile_path":"atlas/symbol_profiles/100/100840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.3,"MFE_90D_pct":13.76,"MFE_180D_pct":50.0,"MFE_1Y_pct":50.0,"MFE_2Y_pct":50.0,"MAE_30D_pct":-7.11,"MAE_90D_pct":-8.26,"MAE_180D_pct":-8.26,"MAE_1Y_pct":-8.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-23","peak_price":32700,"drawdown_after_peak_pct":-39.33,"green_lateness_ratio":"0.46","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_order_margin_conversion","four_b_evidence_type":"non_price_order_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B","case_id":"R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B","symbol":"083650","company_name":"비에이치아이","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_POWER_PLANT_BOILER_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"BOILER_HRSG_ORDER_TO_REVENUE_BUT_PEAK_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-31","entry_date":"2023-03-31","entry_price":7720,"evidence_available_at_that_date":"source_proxy_power_plant_boiler_order_bridge_with_repricing; evidence_url_pending","evidence_source":"source_proxy_power_plant_boiler_order_bridge_with_repricing; evidence_url_pending","bridge_summary":"power-plant equipment/order bridge validated the move, but post-peak drawdown requires 4B watch","stage2_evidence_fields":["power_plant_equipment_order","order_backlog_visibility","relative_strength","margin_conversion_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","customer_or_project_quality","non_price_bridge"],"stage4b_evidence_fields":["post_MFE_reversal_watch","local_and_full_window_peak_proximity"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083650/2023.csv","profile_path":"atlas/symbol_profiles/083/083650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.08,"MFE_90D_pct":51.17,"MFE_180D_pct":51.17,"MFE_1Y_pct":51.17,"MFE_2Y_pct":51.17,"MAE_30D_pct":-10.23,"MAE_90D_pct":-14.64,"MAE_180D_pct":-14.64,"MAE_1Y_pct":-14.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-14","peak_price":11670,"drawdown_after_peak_pct":-43.53,"green_lateness_ratio":"0.39","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_but_requires_drawdown_guard","four_b_evidence_type":"non_price_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK","case_id":"R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK","symbol":"023960","company_name":"에쓰씨엔지니어링","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_AMOUNT_HIGH_MARGIN_WEAK_BRIDGE","deep_sub_archetype_id":"PLANT_ENGINEERING_CONTRACT_HEADLINE_WITH_WORKING_CAPITAL_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-21","entry_date":"2023-04-21","entry_price":2695,"evidence_available_at_that_date":"source_proxy_EPC_contract_headline_without_margin_working_capital_bridge; evidence_url_pending","evidence_source":"source_proxy_EPC_contract_headline_without_margin_working_capital_bridge; evidence_url_pending","bridge_summary":"contract headline moved price, but no durable margin/working-capital bridge appeared","stage2_evidence_fields":["EPC_contract_headline","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through","working_capital_risk_watch"],"stage4c_evidence_fields":["high_MAE_without_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/023/023960/2023.csv","profile_path":"atlas/symbol_profiles/023/023960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.23,"MFE_90D_pct":43.23,"MFE_180D_pct":43.23,"MFE_1Y_pct":43.23,"MFE_2Y_pct":43.23,"MAE_30D_pct":-25.79,"MAE_90D_pct":-38.78,"MAE_180D_pct":-38.78,"MAE_1Y_pct":-38.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-15","peak_price":3860,"drawdown_after_peak_pct":-57.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_or_margin_weak_local_4B_watch_not_full_4B","four_b_evidence_type":"price_only_or_margin_weak_contract_headline","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","trigger_id":"TRG_R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION","symbol":"100840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_amount_score":10,"margin_bridge_score":9,"working_capital_quality_score":7,"order_to_revenue_score":12,"relative_strength_score":9,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_amount_score":8,"margin_bridge_score":14,"working_capital_quality_score":10,"order_to_revenue_score":15,"relative_strength_score":8,"risk_penalty":4},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["contract_amount_score","margin_bridge_score","working_capital_quality_score","order_to_revenue_score","risk_penalty"],"component_delta_explanation":"C05 row is promoted only when contract/order bridge has margin and revenue conversion evidence.","MFE_90D_pct":13.76,"MAE_90D_pct":-8.26,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B","trigger_id":"TRG_R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B","symbol":"083650","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_amount_score":10,"margin_bridge_score":8,"working_capital_quality_score":6,"order_to_revenue_score":11,"relative_strength_score":10,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_amount_score":8,"margin_bridge_score":12,"working_capital_quality_score":7,"order_to_revenue_score":13,"relative_strength_score":7,"risk_penalty":9},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["contract_amount_score","margin_bridge_score","working_capital_quality_score","order_to_revenue_score","risk_penalty"],"component_delta_explanation":"C05 order bridge works, but post-MFE drawdown prevents Green loosening.","MFE_90D_pct":51.17,"MAE_90D_pct":-14.64,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK","trigger_id":"TRG_R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK","symbol":"023960","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_amount_score":12,"margin_bridge_score":2,"working_capital_quality_score":1,"order_to_revenue_score":3,"relative_strength_score":11,"risk_penalty":7},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_amount_score":5,"margin_bridge_score":0,"working_capital_quality_score":0,"order_to_revenue_score":1,"relative_strength_score":5,"risk_penalty":14},"weighted_score_after":43,"stage_label_after":"Stage1-Watch","changed_components":["contract_amount_score","margin_bridge_score","working_capital_quality_score","order_to_revenue_score","risk_penalty"],"component_delta_explanation":"C05 guard demotes EPC contract headline when margin/working-capital bridge is absent.","MFE_90D_pct":43.23,"MAE_90D_pct":-38.78,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_requires_margin_working_capital_order_to_revenue_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"C05 EPC/plant rows should not promote toward Stage3-Yellow/Green unless contract/order amount converts into margin, working-capital, and revenue visibility","100840 and 083650 survive because plant equipment/order bridge exists; 023960 fails as contract headline/price spike without margin bridge","TRG_R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION|TRG_R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B|TRG_R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c05_contract_headline_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,1,1,0,"C05 winners and failures can peak quickly; local/full-window 4B watch must stay separate from positive Stage3 evidence","preserves 100840/083650 positives while preventing 023960 contract-headline false positive","TRG_R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION|TRG_R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B|TRG_R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch behavior without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"72","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["contract_headline_without_margin_bridge","plant_order_success_needs_4B_watch","EPC_working_capital_high_MAE_after_price_spike"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 72
next_round = R2
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
atlas/symbol_profiles/100/100840.json
atlas/symbol_profiles/083/083650.json
atlas/symbol_profiles/023/023960.json
atlas/ohlcv_tradable_by_symbol_year/100/100840/2023.csv
atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv
atlas/ohlcv_tradable_by_symbol_year/083/083650/2023.csv
atlas/ohlcv_tradable_by_symbol_year/023/023960/2023.csv
```

This loop starts Loop 72 with R1 and adds 3 new independent C05 cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate.
