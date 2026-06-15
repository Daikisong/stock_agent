# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R5
selected_loop = 113
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. Existing global axes are treated as baseline rather than re-proposed globally.

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop asks whether C18 export-channel reorder cases need an explicit `channel_reorder + margin/revision bridge` route, while blocking broad overseas-label/capital-allocation false positives.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R5 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| fine_archetype_id | KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE |
| scope logic | C18 belongs to R5/L5. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C18 as Priority 0 with 3 representative rows and a 27-row shortage to the 30-row minimum. Existing top-covered C18 symbols are `003230`, `011150`, and `383220`; this loop avoids them.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected new symbols:

| symbol | name | novelty |
|---:|---|---|
| 004370 | 농심 | new C18 symbol; ramen export/reorder channel evidence |
| 005180 | 빙그레 | new C18 symbol; dairy/ice-cream export channel with high-MAE success |
| 271560 | 오리온 | new C18 counterexample; overseas consumer label interrupted by capital-allocation shock |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| universe | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

All representative rows have stock-web tradable entry rows, complete 30D/90D/180D MFE·MAE, and at least 180 forward trading days before `manifest_max_date = 2026-02-20`. Corporate action candidate dates in the profiles do not contaminate the selected 180D windows.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression logic |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | ramen_export_channel_reorder_margin_bridge | export/channel reorder plus margin/revision bridge can be Stage2-Actionable without contract-like evidence |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | dairy_icecream_export_channel_high_mae_success | strong export-channel rerating can still need 4B watch because drawdown after peak is severe |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | overseas_confectionery_label_capital_allocation_false_positive | broad overseas consumer label is insufficient when capital allocation or non-core event risk interrupts rerating |

## 7. Case Selection Summary

| case_id | symbol | name | role | polarity | trigger | entry | price |
|---|---:|---|---|---|---|---|---:|
| C18_R5L113_004370_20240528 | 004370 | 농심 | structural_success | positive | Stage2-Actionable | 2024-05-28 | 469,000 |
| C18_R5L113_005180_20240517 | 005180 | 빙그레 | high_mae_success | positive | Stage2-Actionable | 2024-05-17 | 88,300 |
| C18_R5L113_271560_20240116 | 271560 | 오리온 | failed_rerating | counterexample | Stage2 | 2024-01-16 | 96,600 |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |
| representative_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 3 |

## 9. Evidence Source Map

| case_id | evidence family | evidence source status | evidence timing note |
|---|---|---|---|
| C18_R5L113_004370_20240528 | ramen export channel reorder, overseas expansion, repeat demand | verified article + source_proxy | external article was available before the 2024-05-28 close; company filing URL still pending |
| C18_R5L113_005180_20240517 | ice-cream/dairy export channel, margin bridge, earnings surprise | source_proxy_only | public exact URL pending; row retained as source_proxy calibration candidate |
| C18_R5L113_271560_20240116 | overseas confectionery label, non-core capital-allocation shock | source_proxy_only | public exact URL pending; used as counterexample, not promotion evidence |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | profile caveat |
|---:|---|---|---|
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv | atlas/symbol_profiles/004/004370.json | old corporate-action candidates before 2004; 2024 window clean |
| 005180 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | atlas/symbol_profiles/005/005180.json | old corporate-action candidates before 1999; 2024 window clean |
| 271560 | atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | atlas/symbol_profiles/271/271560.json | no corporate-action candidate dates |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | name | trigger | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C18_R5L113_004370_20240528 | 004370 | 농심 | Stage2-Actionable | 2024-05-28 | 469,000 | 27.72 | -8.96 | 27.72 | -23.13 | 27.72 | -32.41 | current_profile_too_late |
| C18_R5L113_005180_20240517 | 005180 | 빙그레 | Stage2-Actionable | 2024-05-17 | 88,300 | 34.09 | -9.29 | 34.09 | -32.96 | 34.09 | -32.96 | current_profile_too_late |
| C18_R5L113_271560_20240116 | 271560 | 오리온 | Stage2 | 2024-01-16 | 96,600 | 2.9 | -7.14 | 2.9 | -7.66 | 10.46 | -15.32 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | peak_date | peak_price | drawdown_after_peak_pct | forward_window_trading_days | corporate_action_window_status |
|---|---|---:|---:|---:|---|
| C18_R5L113_004370_20240528_Stage2_Actionable_2024-05-28 | 2024-06-13 | 599,000 | -47.08 | 180 | clean_180D_window |
| C18_R5L113_005180_20240517_Stage2_Actionable_2024-05-17 | 2024-06-11 | 118,400 | -50.00 | 180 | clean_180D_window |
| C18_R5L113_271560_20240116_Stage2_2024-01-16 | 2024-06-18 | 106,700 | -23.34 | 180 | clean_180D_window |
| C18_R5L113_005180_20240517_Stage4B_2024-06-11 | 2024-06-11 | 118,400 | -50.00 | 180 | clean_180D_window |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile verdict | alignment with MFE/MAE | residual error |
|---|---|---|---|
| C18_R5L113_004370_20240528 | current_profile_too_late | 90D MFE positive, but 180D MAE requires watch discipline | consumer export reorder under-credited without contract-like evidence |
| C18_R5L113_005180_20240517 | current_profile_too_late | 30D/90D MFE strong, but drawdown after peak is severe | good Stage2-Actionable, but needs local 4B watch |
| C18_R5L113_271560_20240116 | current_profile_false_positive | MFE90 only 2.90%; no durable rerating | broad overseas channel label over-credited despite capital-allocation/event cap |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop. Green lateness is marked `not_applicable_no_confirmed_Stage3_Green_trigger`. The relevant residual is earlier: C18 Stage2-Actionable should be allowed when export/channel reorder evidence is backed by margin/revision, but overseas-label-only cases should remain Stage1/Stage2 watch.

## 15. 4B Local vs Full-window Timing Audit

| overlay | local_peak | full_window_peak | verdict |
|---|---:|---:|---|
| 005180 Stage4B 2024-06-11 | 118,400 | 118,400 | local peak watch worked as risk overlay; not a full 4B without non-price slowdown evidence |

The 4B lesson is not “sell all export winners at local peak.” It is narrower: C18 high-MFE names can require a local overheat watch because 90D/180D drawdown after the first peak can exceed 30%.

## 16. 4C Protection Audit

No hard 4C row is proposed. C18 false positives here are handled by Stage2 bridge discipline and 4B watch, not by hard thesis-break routing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
proposal = In L5 consumer export/channel cases, Stage2-Actionable may accept export-channel/reorder evidence instead of formal backlog/contract evidence only when margin or revision bridge is present.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
proposal = For C18, require channel_reorder + margin_or_revision_bridge for promotion; if only overseas-label or one-off event exists, keep as Stage1/Stage2 watch. Add high-MAE local 4B watch for fast export rerating spikes.
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | before score/stage | after score/stage | score-return verdict |
|---|---|---|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline tends to under-credit export reorder without contract-like evidence | 66 / Stage2 | 69 / Stage2-Actionable | improves C18 separation |
| P0b_e2r_2_0_baseline_reference | older baseline misses consumer export bridge more often | 60 / Stage1 | 64 / Stage2 | improves C18 separation |
| P1_sector_specific_candidate_profile | L5 channel/reorder/OPM bridge gets explicit Stage2 bridge credit | 70 / Stage2-Actionable | 72 / Stage2-Actionable | improves C18 separation |
| P2_canonical_archetype_candidate_profile | C18 requires channel reorder + margin/revision bridge; blocks capital-allocation false positives | 71 / Stage2-Actionable | 74 / Stage2-Actionable | improves C18 separation |
| P3_counterexample_guard_profile | event/capital allocation override prevents overseas-label false positive | 57 / Stage1 | 60 / Stage1 | improves C18 separation |

## 20. Score-Return Alignment Matrix

| evidence split | expected treatment | observed price alignment |
|---|---|---|
| export channel + repeat demand + margin bridge | Stage2-Actionable allowed | 004370 and 005180 both produced >25% MFE30/90 |
| export label + capital allocation shock | Stage2 watch / no promotion | 271560 produced only 2.90% MFE90 |
| price-only local peak after export rerating | 4B watch overlay only | 005180 local peak watch avoided large subsequent drawdown |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | C18 moves from 3 to 6 representative rows if accepted; still Priority 0 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_too_late, current_profile_false_positive, high_MAE_success_needs_4B_watch
new_axis_proposed: C18_channel_reorder_margin_revision_bridge
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 3 new independent cases, 1 counterexample, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web tradable_raw OHLC rows
- 30D/90D/180D MFE·MAE
- clean 180D corporate action window
- selected C18 duplicate avoidance
- trigger_type canonical stage labels
```

Non-validation scope:

```text
- no production scoring patch
- no live candidate scan
- no broker/API connection
- no current investment recommendation
- exact filing URLs for 005180 and 271560 remain evidence_url_pending/source_proxy_only
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,false,true,+1,"require channel reorder plus margin/revision bridge","separates 004370/005180 from 271560","C18_R5L113_004370_20240528_Stage2_Actionable_2024-05-28|C18_R5L113_005180_20240517_Stage2_Actionable_2024-05-17|C18_R5L113_271560_20240116_Stage2_2024-01-16",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,false,true,+1,"fast export rerating can suffer large drawdown after local peak","005180 4B overlay captures risk without full 4B thesis break","C18_R5L113_005180_20240517_Stage4B_2024-06-11",1,1,0,medium,canonical_shadow_only,"4B overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C18_R5L113_004370_20240528","symbol":"004370","company_name":"농심","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"ramen_export_channel_reorder_positive_high_mae"}
{"row_type":"trigger","trigger_id":"C18_R5L113_004370_20240528_Stage2_Actionable_2024-05-28","case_id":"C18_R5L113_004370_20240528","symbol":"004370","company_name":"농심","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","sector":"consumer / brand / distribution / K-food / export channel / reorder / repeat demand","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-27","evidence_available_at_that_date":"FT/Nongshim overseas expansion article published 2024-05-27 plus source-proxy 2024 export/channel reorder evidence; exact company filing URL pending","evidence_source":"verified_article_plus_source_proxy","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-28","entry_price":469000,"MFE_30D_pct":27.72,"MFE_90D_pct":27.72,"MFE_180D_pct":27.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.96,"MAE_90D_pct":-23.13,"MAE_180D_pct":-32.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ramen_export_channel_reorder_positive_high_mae","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_corporate_action_dates_before_2004","same_entry_group_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|004370|2024-05-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C18_R5L113_005180_20240517","symbol":"005180","company_name":"빙그레","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"icecream_export_channel_reorder_high_mae_success"}
{"row_type":"trigger","trigger_id":"C18_R5L113_005180_20240517_Stage2_Actionable_2024-05-17","case_id":"C18_R5L113_005180_20240517","symbol":"005180","company_name":"빙그레","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","sector":"consumer / brand / distribution / K-food / export channel / reorder / repeat demand","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","evidence_available_at_that_date":"source_proxy_only: Q1 2024 earnings/export ice-cream channel and margin bridge; exact URL pending","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":88300,"MFE_30D_pct":34.09,"MFE_90D_pct":34.09,"MFE_180D_pct":34.09,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.29,"MAE_90D_pct":-32.96,"MAE_180D_pct":-32.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"icecream_export_channel_reorder_high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_corporate_action_dates_before_1999","same_entry_group_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|005180|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C18_R5L113_271560_20240116","symbol":"271560","company_name":"오리온","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_mfe_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"overseas_confectionery_channel_label_capital_allocation_false_positive"}
{"row_type":"trigger","trigger_id":"C18_R5L113_271560_20240116_Stage2_2024-01-16","case_id":"C18_R5L113_271560_20240116","symbol":"271560","company_name":"오리온","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","sector":"consumer / brand / distribution / K-food / export channel / reorder / repeat demand","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-16","evidence_available_at_that_date":"source_proxy_only: overseas confectionery channel label was interrupted by non-core bio capital allocation shock; exact URL pending","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["capital_raise_or_overhang","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","profile_path":"atlas/symbol_profiles/271/271560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-16","entry_price":96600,"MFE_30D_pct":2.9,"MFE_90D_pct":2.9,"MFE_180D_pct":10.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.14,"MAE_90D_pct":-7.66,"MAE_180D_pct":-15.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":106700,"drawdown_after_peak_pct":-23.34,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"overseas_confectionery_channel_label_capital_allocation_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_no_corporate_action_candidate","same_entry_group_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|271560|2024-01-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C18_R5L113_005180_20240517_Stage4B_2024-06-11","case_id":"C18_R5L113_005180_20240517","symbol":"005180","company_name":"빙그레","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_RAMEN_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONFECTIONERY_CAPITAL_ALLOCATION_FALSE_POSITIVE","sector":"consumer / brand / distribution / K-food / export channel / reorder / repeat demand","primary_archetype":"consumer_export_channel_reorder","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-06-11","evidence_available_at_that_date":"local price/volume overheat after export reorder rerating; non-price slowdown not confirmed","evidence_source":"price_path_overlay_only","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-11","entry_price":109000,"MFE_30D_pct":8.62,"MFE_90D_pct":8.62,"MFE_180D_pct":8.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.5,"MAE_90D_pct":-45.69,"MAE_180D_pct":-45.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"local_4B_watch_usable_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"local_peak_4b_watch_after_export_reorder_rerating","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_corporate_action_dates_before_1999","same_entry_group_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|005180|2024-06-11","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L113_AGGREGATE","trigger_id":"aggregate_selected_representatives","symbol":"MULTI","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"baseline tends to under-credit export reorder without contract-like evidence","MFE_90D_pct":34.0,"MAE_90D_pct":-23.0,"score_return_alignment_label":"improves_positive_vs_counterexample_separation","current_profile_verdict":"mixed_current_profile_too_late_for_positives_false_positive_for_orion"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","case_id":"C18_R5L113_AGGREGATE","trigger_id":"aggregate_selected_representatives","symbol":"MULTI","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"older baseline misses consumer export bridge more often","MFE_90D_pct":34.0,"MAE_90D_pct":-23.0,"score_return_alignment_label":"improves_positive_vs_counterexample_separation","current_profile_verdict":"mixed_current_profile_too_late_for_positives_false_positive_for_orion"}
{"row_type":"score_simulation","profile_id":"P1_sector_specific_candidate_profile","case_id":"C18_R5L113_AGGREGATE","trigger_id":"aggregate_selected_representatives","symbol":"MULTI","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"L5 channel/reorder/OPM bridge gets explicit Stage2 bridge credit","MFE_90D_pct":34.0,"MAE_90D_pct":-23.0,"score_return_alignment_label":"improves_positive_vs_counterexample_separation","current_profile_verdict":"mixed_current_profile_too_late_for_positives_false_positive_for_orion"}
{"row_type":"score_simulation","profile_id":"P2_canonical_archetype_candidate_profile","case_id":"C18_R5L113_AGGREGATE","trigger_id":"aggregate_selected_representatives","symbol":"MULTI","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C18 requires channel reorder + margin/revision bridge; blocks capital-allocation false positives","MFE_90D_pct":34.0,"MAE_90D_pct":-23.0,"score_return_alignment_label":"improves_positive_vs_counterexample_separation","current_profile_verdict":"mixed_current_profile_too_late_for_positives_false_positive_for_orion"}
{"row_type":"score_simulation","profile_id":"P3_counterexample_guard_profile","case_id":"C18_R5L113_AGGREGATE","trigger_id":"aggregate_selected_representatives","symbol":"MULTI","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":57,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"event/capital allocation override prevents overseas-label false positive","MFE_90D_pct":34.0,"MAE_90D_pct":-23.0,"score_return_alignment_label":"improves_positive_vs_counterexample_separation","current_profile_verdict":"mixed_current_profile_too_late_for_positives_false_positive_for_orion"}
{"row_type":"residual_contribution","round":"R5","loop":"113","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","high_MAE_success_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 113
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest_max_date = 2026-02-20
stock_web_manifest_path = atlas/manifest.json
stock_web_schema_path = atlas/schema.json
no_repeat_index_path = docs/core/V12_Research_No_Repeat_Index.md
source_url_status = mixed_verified_article_and_source_proxy_only
evidence_url_pending_symbols = 005180, 271560
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 3
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 1
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
