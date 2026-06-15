# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R5
selected_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery
output_file = e2r_stock_web_v12_residual_round_R5_loop_141_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

This loop targets C18 because the No-Repeat Index marks it as a Priority 0 under-covered archetype with only 3 representative rows and 3 covered symbols. The previously covered C18 symbols are 003230, 011150, and 383220, so this loop adds two new symbols, 004370 and 097950, and reuses 003230 only for a distinct export/regulatory-trigger family.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = C18_shadow_export_channel_reorder_bridge_guard
rollback_reference_profile_id = e2r_2_0_baseline_reference
active_repo_profile_context = e2r_2_2_rolling_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Applied global axes are treated as already present and are not re-proposed globally. This loop stress-tests whether C18 needs a tighter bridge from export/channel headline to repeat demand plus OPM/EPS durability before durable Stage3 confirmation.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R5 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| fine_archetype_id | K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE |
| scope decision | canonical_archetype_specific |
| invalid_round_sector_pair | false |

## 3. Previous Coverage / Duplicate Avoidance Check

| check | result |
|---|---|
| Priority bucket | Priority 0 |
| C18 prior representative rows | 3 |
| C18 prior covered symbols | 003230, 011150, 383220 |
| hard duplicate check | pass; no same `canonical_archetype_id + symbol + trigger_type + entry_date` reused for new-symbol cases |
| reused-symbol handling | 003230 is reused only as a different trigger-family / 4B-regulatory stress-test case |
| minimum new independent case ratio | pass: 2.5 weighted independent cases / 3 usable cases |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web manifest confirms `FinanceData/marcap`, `raw_unadjusted_marcap`, `max_date=2026-02-20`, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| symbol | company | entry_date | forward_window_trading_days | 180D price fields | corporate-action window | calibration_usable |
|---|---|---:|---:|---|---|---|
| 003230 | 삼양식품 | 2024-06-17 | 180 | complete | clean_180D_window | true |
| 004370 | 농심 | 2024-05-28 | 180 | complete | clean_180D_window | true |
| 097950 | CJ제일제당 | 2024-11-22 | 180 | complete | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep sub-archetype | compression rule |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | Buldak export ASP / US-Europe shipment / capacity support | Positive only if export demand is paired with shipment, ASP, or capacity evidence; otherwise late vertical moves need high-MAE guard. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | Shin Ramyun Walmart mainstream shelf / Europe Q1 sales acceleration | Channel expansion can create fast MFE, but durable Stage3 needs OPM/EPS bridge because 180D path can reverse sharply. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | Bibigo/CJ global facility expansion / K-food capacity | Capacity headline without near-term reorder, margin, or EPS bridge is a weak Stage2 and should not unlock Green. |

## 7. Case Selection Summary

| case_id | symbol | role | newness | reason |
|---|---|---|---|---|
| C18_R5_L141_003230_EXPORT_ASP_CAPACITY | 003230 | structural_success / high_MAE_success | reused symbol, new trigger family | Strong export/ASP/capacity evidence after prior C18 symbol coverage; used with partial independent weight. |
| C18_R5_L141_004370_SHIN_CHANNEL_REORDER | 004370 | high_MAE_success | new symbol | Strong US/Europe channel signal had large 30D MFE but later high MAE, making it useful for bridge/guard calibration. |
| C18_R5_L141_097950_BIBIGO_CAPACITY_PROXY | 097950 | failed_rerating | new symbol | Global facility/K-food capacity signal did not convert into near-term price durability. |

## 8. Positive vs Counterexample Balance

| count | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |

Positive here does not mean investment recommendation. It means the historical trigger produced non-price evidence and a measurable positive MFE path. Both positive cases carry high-MAE caveats.

## 9. Evidence Source Map

| symbol | trigger_date | evidence_source | evidence summary | evidence quality |
|---|---:|---|---|---|
| 003230 | 2024-06-14 | MarketWatch / WSJ Market Talk, “Samyang Foods Set to Post Strong 2Q Earnings” | Kiwoom raised 2Q OP estimate on Buldak exports, higher ASP, increased US/Europe shipments, and capacity support. | verified_url |
| 004370 | 2024-05-27 | Financial Times, “Maker of Shin instant ramen expands overseas…” | Shin Ramyun 2023 sales W1.2tn with nearly 60% abroad; Walmart mainstream shelf migration; Europe Q1 sales >30%; US target expansion. | verified_url |
| 097950 | 2024-11-21 | CJ Group source-proxy record for CJ Foods production facilities | Hungary and South Dakota facilities framed as K-food demand/capacity expansion, but without near-term margin/reorder proof. | source_proxy_only |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | profile status |
|---|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv; atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv | atlas/symbol_profiles/003/003230.json | active_like; corporate-action candidates only old 2003 date |
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv; atlas/ohlcv_tradable_by_symbol_year/004/004370/2025.csv | atlas/symbol_profiles/004/004370.json | active_like; corporate-action candidates 1997/2000/2003 only |
| 097950 | atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv; atlas/ohlcv_tradable_by_symbol_year/097/097950/2025.csv | atlas/symbol_profiles/097/097950.json | active_like; no corporate-action candidates |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | outcome label | current profile verdict |
|---|---|---|---:|---:|---:|---|---|
| C18_R5_L141_003230_T1 | 003230 | Stage2-Actionable | 2024-06-14 | 2024-06-17 | 686000 | buldak_export_asp_capacity_positive_high_mae | current_profile_correct |
| C18_R5_L141_004370_T1 | 004370 | Stage2-Actionable | 2024-05-27 | 2024-05-28 | 469000 | shin_channel_expansion_high_mfe_high_mae | current_profile_false_positive |
| C18_R5_L141_097950_T1 | 097950 | Stage2 | 2024-11-21 | 2024-11-22 | 272000 | kfood_capacity_headline_without_reorder_margin_bridge | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 003230 | 686000 | 4.66 | -15.31 | 4.66 | -33.60 | 37.03 | -33.60 | 2025-03-07 | 940000 | -20.43 |
| 004370 | 469000 | 27.72 | -8.96 | 27.72 | -23.13 | 27.72 | -32.41 | 2024-06-13 | 599000 | -47.08 |
| 097950 | 272000 | 2.39 | -9.93 | 2.39 | -14.71 | 2.39 | -19.12 | 2024-11-22 | 278500 | -21.01 |

## 13. Current Calibrated Profile Stress Test

| symbol | expected P0 behavior | actual path | verdict |
|---|---|---|---|
| 003230 | Allow Stage2-Actionable; delay Green unless export bridge persists. | 180D MFE strong but MAE severe. | current_profile_correct with high-MAE guard strengthened |
| 004370 | Export/channel evidence could trigger Stage2-Actionable. | 30D MFE was strong, then 90/180D MAE became severe. | current_profile_false_positive if treated as durable rerating too early |
| 097950 | Capacity/global K-food headline likely weak Stage2 only. | MFE barely positive and downside persisted. | current_profile_false_positive if Stage2 bonus is granted without reorder/margin bridge |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned in this loop. `green_lateness_ratio = not_applicable` for all cases because this research tests whether C18 should remain at Stage2/Stage2-Actionable until repeat demand, margin bridge, and EPS revision become visible.

## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_evidence_type | local/full split | timing verdict |
|---|---|---|---|
| 003230 | valuation_blowoff; positioning_overheat; regulatory_recall_watch | local price risk appeared after the sharp June move, but full-window high was later in the 180D path | price_only_local_4B_too_early |
| 004370 | valuation_blowoff; margin_or_backlog_slowdown | 2024-06-13 local/full peak was useful, but only after non-price follow-through weakened | good_full_window_4B_timing_candidate |
| 097950 | price_only; weak capacity headline | no meaningful overheat; weak MFE means no 4B promotion | not_applicable |

## 16. 4C Protection Audit

No hard 4C row is proposed. 003230's Denmark recall/regulatory watch did not become a hard thesis break; 004370 and 097950 are better classified as Stage2 false-positive / high-MAE guard cases.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = evidence concentrated in C18; not enough to generalize across all L5 consumer/brand/distribution scopes.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
candidate = C18 export/channel headline should remain Stage2-watch unless at least two of: repeat reorder evidence, retailer shelf/channel expansion, OPM or gross-margin bridge, EPS/revision follow-through, capacity utilization proof.
```

This is not a Green loosening rule. It is a bridge/guard rule: export headlines can be early tinder, but the candle only becomes a durable rerating when repeat demand and margin oxygen keep it burning.

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | false-positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | generic Stage2 bridge + price-only guard | 3 | 11.59 | -23.81 | 0.67 | mixed |
| P0b e2r_2_0_baseline_reference | looser export headline treatment | 3 | 11.59 | -23.81 | 0.67 | weak |
| P1 L5 sector-specific candidate | consumer export proof broader than C18 | 3 | 11.59 | -23.81 | 0.67 | not enough breadth |
| P2 C18 canonical candidate | require repeat/channel/margin/revision bridge | 3 | 11.59 | -23.81 | 0.33 | improved |
| P3 counterexample guard | block capacity/headline-only Stage2 bonus | 3 | 11.59 | -23.81 | 0.33 | improved |

## 20. Score-Return Alignment Matrix

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | component_delta_explanation |
|---|---|---:|---|---|---:|---|---|
| C18_R5_L141_003230_EXPORT_ASP_CAPACITY | contract=0; backlog=1; margin=2; revision=2; relative_strength=2; customer_quality=2; policy=0; valuation=1; execution_risk=2; legal_risk=1; dilution=0; trust=0 | 76 | Stage2-Actionable | contract=0; backlog=1; margin=2; revision=2; relative_strength=2; customer_quality=2; policy=0; valuation=1; execution_risk=2; legal_risk=1; dilution=0; trust=0 | 76 | Stage2-Actionable | No upgrade; high-MAE guard keeps Green delayed. |
| C18_R5_L141_004370_SHIN_CHANNEL_REORDER | contract=0; backlog=1; margin=1; revision=1; relative_strength=2; customer_quality=2; policy=0; valuation=1; execution_risk=2; legal_risk=0; dilution=0; trust=0 | 73 | Stage2-Actionable | contract=0; backlog=1; margin=0; revision=1; relative_strength=2; customer_quality=2; policy=0; valuation=1; execution_risk=3; legal_risk=0; dilution=0; trust=0 | 68 | Stage2-watch | Downgrade durability because channel headline outran margin/revision proof. |
| C18_R5_L141_097950_BIBIGO_CAPACITY_PROXY | contract=0; backlog=1; margin=0; revision=0; relative_strength=0; customer_quality=1; policy=0; valuation=0; execution_risk=2; legal_risk=0; dilution=0; trust=0 | 65 | Stage2 | contract=0; backlog=1; margin=0; revision=0; relative_strength=0; customer_quality=1; policy=0; valuation=0; execution_risk=3; legal_risk=0; dilution=0; trust=0 | 59 | Stage1/weak-watch | Capacity headline without reorder/margin bridge loses Stage2 bonus. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE | 2 | 1 | 1 | 0 | 3 | 1 | 3 | 3 | 2 | false | true | 24 to 30-row minimum |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: C18_R5_L141_003230_EXPORT_ASP_CAPACITY
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage
residual_error_types_found: export_headline_high_MFE_high_MAE, capacity_headline_without_reorder_margin_bridge, local_4B_too_early_on_regulatory_watch
new_axis_proposed: null
existing_axis_strengthened: C18_stage2_required_bridge; C18_high_MAE_guard
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 3 usable cases, 1 counterexample, and 2 current-profile residual errors for R5/L5/C18.

## 23. Validation Scope / Non-Validation Scope

Validation scope: stock-web raw/unadjusted OHLC path, 30/90/180D MFE/MAE, trigger-stage classification, duplicate avoidance, C18-specific bridge rule candidate.

Non-validation scope: no live stock recommendation, no production scoring patch, no immediate repo code modification, no brokerage/API usage, no future price input into runtime scoring.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,false,true,+1,"C18 export/channel headlines need repeat demand plus margin/revision bridge","reduced headline-only false positives from 2 to 1 in this sample","C18_R5_L141_004370_T1|C18_R5_L141_097950_T1",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,high_mae_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,false,true,+1,"strong MFE coexists with -30% MAE in C18 export names","keeps high-MAE winners from automatic Green","C18_R5_L141_003230_T1|C18_R5_L141_004370_T1",3,3,1,medium,canonical_shadow_only,"not production; use as guard"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,true,true,0,"price-only or regulatory local peak can be too early","kept, not loosened","C18_R5_L141_003230_T1",3,3,1,low,axis_kept,"do not convert local watch to hard 4B without non-price deterioration"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C18_R5_L141_003230_EXPORT_ASP_CAPACITY","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C18_R5_L141_003230_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol appears in prior C18 coverage but this loop tests a distinct export-ASP-capacity and high-MAE trigger family","independent_evidence_weight":0.5,"score_price_alignment":"positive 180D MFE but severe MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"reused symbol but new trigger family; count with partial independent weight"}
{"row_type":"case","case_id":"C18_R5_L141_004370_SHIN_CHANNEL_REORDER","symbol":"004370","company_name":"농심","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C18_R5_L141_004370_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early MFE but failed durability","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C18 symbol; strong channel evidence but high-MAE durability risk"}
{"row_type":"case","case_id":"C18_R5_L141_097950_BIBIGO_CAPACITY_PROXY","symbol":"097950","company_name":"CJ제일제당","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C18_R5_L141_097950_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"low MFE with persistent downside","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C18 symbol; capacity/global K-food headline without near-term reorder/margin proof"}
{"row_type":"trigger","trigger_id":"C18_R5_L141_003230_T1","case_id":"C18_R5_L141_003230_EXPORT_ASP_CAPACITY","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE","sector":"consumer/food/export","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-14","evidence_available_at_that_date":"MarketWatch/WSJ Market Talk: Kiwoom raised Samyang 2Q OP estimate on Buldak exports, ASP, US/Europe shipments and capacity support; published after Korea close, next trading-day entry used.","evidence_source":"https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-17","entry_price":686000,"MFE_30D_pct":4.66,"MFE_90D_pct":4.66,"MFE_180D_pct":37.03,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.31,"MAE_90D_pct":-33.60,"MAE_180D_pct":-33.60,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-07","peak_price":940000,"drawdown_after_peak_pct":-20.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"buldak_export_asp_capacity_positive_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C18_R5_L141_003230_2024-06-17_686000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol prior C18 coverage; distinct trigger family and entry group","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C18_R5_L141_004370_T1","case_id":"C18_R5_L141_004370_SHIN_CHANNEL_REORDER","symbol":"004370","company_name":"농심","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE","sector":"consumer/food/export","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-27","evidence_available_at_that_date":"Financial Times: Nongshim accelerating overseas expansion; Shin Ramyun 2023 sales W1.2tn with nearly 60% abroad; Walmart mainstream shelf move; Europe Q1 sales >30%.","evidence_source":"https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv|atlas/ohlcv_tradable_by_symbol_year/004/004370/2025.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-28","entry_price":469000,"MFE_30D_pct":27.72,"MFE_90D_pct":27.72,"MFE_180D_pct":27.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.96,"MAE_90D_pct":-23.13,"MAE_180D_pct":-32.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_candidate_after_non_price_followthrough_weakens","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"shin_channel_expansion_high_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C18_R5_L141_004370_2024-05-28_469000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C18_R5_L141_097950_T1","case_id":"C18_R5_L141_097950_BIBIGO_CAPACITY_PROXY","symbol":"097950","company_name":"CJ제일제당","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_RETAIL_SHELF_EXPANSION_VS_EXPORT_HEADLINE_WEAK_MARGIN_BRIDGE","sector":"consumer/food/export","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-11-21","evidence_available_at_that_date":"CJ Group source-proxy record: CJ Foods constructing Hungary and South Dakota production facilities to meet global K-food demand; source-proxy only, no near-term reorder or margin proof.","evidence_source":"https://en.wikipedia.org/wiki/CJ_Group","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv|atlas/ohlcv_tradable_by_symbol_year/097/097950/2025.csv","profile_path":"atlas/symbol_profiles/097/097950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-22","entry_price":272000,"MFE_30D_pct":2.39,"MFE_90D_pct":2.39,"MFE_180D_pct":2.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.93,"MAE_90D_pct":-14.71,"MAE_180D_pct":-19.12,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-22","peak_price":278500,"drawdown_after_peak_pct":-21.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"kfood_capacity_headline_without_reorder_margin_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C18_R5_L141_097950_2024-11-22_272000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5_L141_004370_SHIN_CHANNEL_REORDER","trigger_id":"C18_R5_L141_004370_T1","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 channel expansion needs repeat demand plus OPM/revision proof before durable Stage2/Green promotion.","MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"score_return_alignment_label":"high_mfe_high_mae_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"141","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["export_headline_high_MFE_high_MAE","capacity_headline_without_reorder_margin_bridge","local_4B_too_early_on_regulatory_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 3
calibration_usable_trigger_count: 3
representative_trigger_count: 3
new_weight_evidence_candidate_count: 2
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
