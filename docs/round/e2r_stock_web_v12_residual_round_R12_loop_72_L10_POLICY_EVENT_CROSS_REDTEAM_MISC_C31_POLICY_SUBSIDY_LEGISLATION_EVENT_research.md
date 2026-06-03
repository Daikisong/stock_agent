# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R12
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R13
computed_next_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_SERVICE_TOURISM_INBOUND_POLICY_TO_REVENUE_BRIDGE_GUARD
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

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or a relevant under-covered service/agri branch. This run uses the L10/C31 service-policy branch and avoids repeating the previous R12 agri-policy branch. The residual target is inbound tourism: policy reopening is not enough unless it turns into visitor demand, casino drop/revenue, hotel occupancy/RevPAR, duty-free sell-through, margin, or cashflow.

| layer | id | definition |
|---|---|---|
| round | R12 | L10 or under-covered service/agri residual |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy/event/misc with service/tourism branch |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/subsidy/legislation event must convert into economics |
| fine | C31_SERVICE_TOURISM_INBOUND_POLICY_TO_REVENUE_BRIDGE_GUARD | reopening policy must become visitor/revenue/sell-through bridge |
| deep | CASINO_REOPENING_VISITOR_RECOVERY_TO_DROP_REVENUE_BRIDGE | casino visitor recovery success |
| deep | CHINA_GROUP_TOUR_JEJU_CASINO_HOTEL_DEMAND_WITH_REVERSAL_RISK | travel/casino MFE with 4B guard |
| deep | CHINA_GROUP_TOUR_DUTYFREE_THEME_WITHOUT_MARGIN_INVENTORY_CONVERSION | duty-free policy theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that cluster and also avoids the prior R12 agri-policy symbols `002900`, `000490`, and `054050`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 114090 | new independent | not top-covered C31 symbol; casino inbound visitor-demand bridge |
| C31 | 032350 | new independent | not top-covered C31 symbol; Jeju casino/hotel reopening MFE with 4B guard |
| C31 | 008770 | new independent | not top-covered C31 symbol; duty-free sell-through/margin counterexample |

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
| structural_success_low_MAE_inbound_reopen | 114090 | GKL | Stage2-Actionable | 2022-09-26 | 14400 | casino visitor-demand/revenue bridge worked |
| structural_success_with_high_MAE_watch | 032350 | 롯데관광개발 | Stage2-Actionable | 2023-08-10 | 13350 | Jeju casino/hotel reopening worked but needed 4B/high-MAE guard |
| failed_rerating_high_MAE | 008770 | 호텔신라 | Stage2-Actionable | 2023-08-10 | 86800 | duty-free reopening theme without sell-through/margin bridge failed |

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
| 114090 | GKL | Stage2-Actionable | 2022-09-26 | 14400 | 10.76 | 47.57 | 47.57 | -3.47 | -3.47 | -3.47 | 2023-02-17 | 21250 | -15.44 |
| 032350 | 롯데관광개발 | Stage2-Actionable | 2023-08-10 | 13350 | 32.43 | 32.43 | 32.43 | -13.11 | -31.61 | -31.61 | 2023-08-31 | 17680 | -48.36 |
| 008770 | 호텔신라 | Stage2-Actionable | 2023-08-10 | 86800 | 8.29 | 8.29 | 8.29 | -9.45 | -33.29 | -33.29 | 2023-08-28 | 94000 | -38.4 |

## 9. Case-by-Case Notes

### 9.1 114090 / GKL — casino inbound reopening to visitor-demand bridge

The entry row is 2022-09-26 at 14,400. The 90D path reaches 21,250 while MAE stays shallow. This is a useful C31 service-policy positive: reopening policy became a visitor-demand and revenue bridge rather than only a travel-theme candle.

### 9.2 032350 / 롯데관광개발 — Jeju casino/hotel reopening with 4B guard

The entry row is 2023-08-10 at 13,350. The path reaches 17,680 quickly, then later reverses into high MAE. This supports Stage2/Yellow only when active 4B/high-MAE guard is attached. Tourism reopening can lift the boat, but leverage and demand durability can still pull water back in.

### 9.3 008770 / 호텔신라 — duty-free reopening theme without sell-through/margin bridge

The entry row is 2023-08-10 at 86,800. The early high reaches only 94,000 and the later path falls to 57,900. This is the service-policy trap: group-tour policy news can sound like demand, but duty-free economics still need sell-through, margin, inventory, and cash conversion.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats tourism/duty-free policy reopening as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C31 service rows need visitor/revenue/sell-through/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for duty-free and high-beta travel/casino reopening rows. |
| Full 4B non-price requirement appropriate? | Yes. 114090/032350 have better demand bridge; 008770 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
114090:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after visitor-demand / revenue bridge
  Stage3-Green = wait for sustained drop/revenue and capital-return durability

032350:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with 4B/high-MAE watch active
  Stage3-Green = reject unless demand durability and balance-sheet sensitivity are cleared

008770:
  Stage2-Actionable = too generous if based only on China group-tour/duty-free policy theme
  Stage3-Yellow = reject without sell-through/margin/inventory bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 114090 | 0.93 | 1.00 | low-MAE 4B watch after casino inbound demand bridge |
| 032350 | 0.97 | 1.00 | good MFE but requires 4B/high-MAE watch after reopening bridge |
| 008770 | 1.00 | 1.00 | price/theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_service_policy_requires_visitor_revenue_sellthrough_margin_bridge

rule:
  For C31 service/tourism policy rows, do not promote reopening, visa, group-tour,
  travel, casino, hotel, or duty-free policy Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price economic bridge is visible:
  visitor recovery, casino drop/revenue, hotel occupancy/RevPAR, duty-free sell-through,
  margin mix, inventory normalization, cashflow conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 29.43 | -22.79 | 33.3% | useful but can over-credit duty-free reopening theme |
| P0b e2r_2_0_baseline_reference | 3 | 29.43 | -22.79 | 0% | safer but may miss 114090/032350 |
| P1 sector_specific_candidate_profile | 3 | 29.43 | -22.79 | 33.3% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 40.0 | -17.54 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 8.29 | -33.29 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 114090 | current_profile_correct | casino visitor-demand bridge aligned with high MFE and low MAE |
| 032350 | current_profile_partially_correct | reopening worked, but drawdown requires 4B/high-MAE watch |
| 008770 | current_profile_false_positive | duty-free tourism theme produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_SERVICE_TOURISM_INBOUND_POLICY_TO_REVENUE_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | R12 service/tourism policy branch reduced |

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
- tourism policy without sell-through/margin bridge
- inbound policy winner needs 4B watch
- casino reopening success low-MAE bridge
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
shadow_weight,c31_service_policy_requires_visitor_revenue_sellthrough_margin_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"R12 service branch: tourism/inbound policy rows should not promote toward Stage3-Yellow/Green unless reopening policy converts into visitor demand, revenue, sell-through, margin, or cashflow bridge","114090 survives with cleaner MFE/MAE after casino visitor-demand bridge; 032350 has MFE but requires 4B/high-MAE watch; 008770 fails when duty-free theme lacks sell-through/margin bridge","TRG_R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE|TRG_R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH|TRG_R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_tourism_reopening_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Tourism reopening winners and duty-free failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 114090/032350 positives while preventing 008770 tourism-theme false positive","TRG_R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE|TRG_R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH|TRG_R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE","symbol":"114090","company_name":"GKL","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_INBOUND_CASINO_POLICY_TO_VISITOR_DEMAND_BRIDGE","deep_sub_archetype_id":"CASINO_REOPENING_VISITOR_RECOVERY_TO_DROP_REVENUE_BRIDGE","case_type":"structural_success_low_MAE_inbound_reopen","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"R12 service branch: C31 tourism/inbound policy rows require visitor-demand, revenue, sell-through, margin, or cashflow bridge; reopening theme alone is insufficient."}
{"row_type":"case","case_id":"R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH","symbol":"032350","company_name":"롯데관광개발","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_JEJU_CASINO_TRAVEL_POLICY_DEMAND_WITH_4B_GUARD","deep_sub_archetype_id":"CHINA_GROUP_TOUR_JEJU_CASINO_HOTEL_DEMAND_WITH_REVERSAL_RISK","case_type":"structural_success_with_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"R12 service branch: C31 tourism/inbound policy rows require visitor-demand, revenue, sell-through, margin, or cashflow bridge; reopening theme alone is insufficient."}
{"row_type":"case","case_id":"R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE","symbol":"008770","company_name":"호텔신라","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_DUTYFREE_TOURISM_POLICY_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","deep_sub_archetype_id":"CHINA_GROUP_TOUR_DUTYFREE_THEME_WITHOUT_MARGIN_INVENTORY_CONVERSION","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R12 service branch: C31 tourism/inbound policy rows require visitor-demand, revenue, sell-through, margin, or cashflow bridge; reopening theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE","case_id":"R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE","symbol":"114090","company_name":"GKL","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_INBOUND_CASINO_POLICY_TO_VISITOR_DEMAND_BRIDGE","deep_sub_archetype_id":"CASINO_REOPENING_VISITOR_RECOVERY_TO_DROP_REVENUE_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-09-26","entry_date":"2022-09-26","entry_price":14400,"evidence_available_at_that_date":"source_proxy_casino_inbound_reopening_visitor_drop_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_casino_inbound_reopening_visitor_drop_revenue_bridge; evidence_url_pending","bridge_summary":"casino/inbound reopening policy converted into visitor recovery and drop/revenue visibility rather than pure travel-theme price strength","stage2_evidence_fields":["inbound_reopening_policy","casino_visitor_recovery_proxy","relative_strength","demand_to_revenue_bridge"],"stage3_evidence_fields":["visitor_to_drop_revenue_visibility","low_MAE_confirmation","non_price_service_demand_bridge"],"stage4b_evidence_fields":["post_reopening_rerating_watch","casino_reopening_crowding"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/114/114090/2022.csv|atlas/ohlcv_tradable_by_symbol_year/114/114090/2023.csv","profile_path":"atlas/symbol_profiles/114/114090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.76,"MFE_90D_pct":47.57,"MFE_180D_pct":47.57,"MFE_1Y_pct":47.57,"MFE_2Y_pct":47.57,"MAE_30D_pct":-3.47,"MAE_90D_pct":-3.47,"MAE_180D_pct":-3.47,"MAE_1Y_pct":-3.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-17","peak_price":21250,"drawdown_after_peak_pct":-15.44,"green_lateness_ratio":"0.45","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_MAE_4B_watch_after_casino_inbound_demand_bridge","four_b_evidence_type":"non_price_inbound_revenue_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH","case_id":"R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH","symbol":"032350","company_name":"롯데관광개발","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_JEJU_CASINO_TRAVEL_POLICY_DEMAND_WITH_4B_GUARD","deep_sub_archetype_id":"CHINA_GROUP_TOUR_JEJU_CASINO_HOTEL_DEMAND_WITH_REVERSAL_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","entry_date":"2023-08-10","entry_price":13350,"evidence_available_at_that_date":"source_proxy_China_group_tour_reopening_Jeju_casino_hotel_demand_bridge; evidence_url_pending","evidence_source":"source_proxy_China_group_tour_reopening_Jeju_casino_hotel_demand_bridge; evidence_url_pending","bridge_summary":"Jeju casino/travel reopening produced a real MFE path, but demand durability and balance-sheet sensitivity required 4B/high-MAE watch","stage2_evidence_fields":["China_group_tour_reopening","Jeju_casino_hotel_demand","relative_strength","visitor_recovery_proxy"],"stage3_evidence_fields":["casino_hotel_demand_conversion","tourism_policy_to_revenue_visibility"],"stage4b_evidence_fields":["post_MFE_peak_watch","tourism_reopening_crowding","balance_sheet_sensitivity_watch"],"stage4c_evidence_fields":["high_MAE_after_reopening_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032350/2023.csv","profile_path":"atlas/symbol_profiles/032/032350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.43,"MFE_90D_pct":32.43,"MFE_180D_pct":32.43,"MFE_1Y_pct":32.43,"MFE_2Y_pct":32.43,"MAE_30D_pct":-13.11,"MAE_90D_pct":-31.61,"MAE_180D_pct":-31.61,"MAE_1Y_pct":-31.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-31","peak_price":17680,"drawdown_after_peak_pct":-48.36,"green_lateness_ratio":"0.33","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_MFE_but_requires_4B_high_MAE_watch_after_reopening_bridge","four_b_evidence_type":"non_price_inbound_revenue_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE","case_id":"R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE","symbol":"008770","company_name":"호텔신라","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_DUTYFREE_TOURISM_POLICY_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","deep_sub_archetype_id":"CHINA_GROUP_TOUR_DUTYFREE_THEME_WITHOUT_MARGIN_INVENTORY_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","entry_date":"2023-08-10","entry_price":86800,"evidence_available_at_that_date":"source_proxy_China_group_tour_dutyfree_policy_theme_without_sellthrough_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_China_group_tour_dutyfree_policy_theme_without_sellthrough_margin_bridge; evidence_url_pending","bridge_summary":"China group-tour reopening lifted duty-free theme price briefly, but sell-through, margin, and inventory conversion bridge was weak and the path reversed into high MAE","stage2_evidence_fields":["China_group_tour_reopening","dutyfree_tourism_theme","relative_strength","price_gap"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","sellthrough_margin_bridge_absent","inventory_or_margin_risk"],"stage4c_evidence_fields":["high_MAE_without_sellthrough_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv","profile_path":"atlas/symbol_profiles/008/008770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.29,"MFE_90D_pct":8.29,"MFE_180D_pct":8.29,"MFE_1Y_pct":8.29,"MFE_2Y_pct":8.29,"MAE_30D_pct":-9.45,"MAE_90D_pct":-33.29,"MAE_180D_pct":-33.29,"MAE_1Y_pct":-33.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-28","peak_price":94000,"drawdown_after_peak_pct":-38.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_sellthrough_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE","trigger_id":"TRG_R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE","symbol":"114090","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_reopening_score":10,"visitor_demand_bridge_score":12,"revenue_conversion_score":11,"sellthrough_margin_score":8,"relative_strength_score":9,"theme_reversal_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_reopening_score":8,"visitor_demand_bridge_score":16,"revenue_conversion_score":14,"sellthrough_margin_score":10,"relative_strength_score":7,"theme_reversal_risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["policy_reopening_score","visitor_demand_bridge_score","revenue_conversion_score","sellthrough_margin_score","relative_strength_score","theme_reversal_risk_penalty"],"component_delta_explanation":"C31 service-policy row is promoted only because reopening policy converts into visitor demand and revenue visibility.","MFE_90D_pct":47.57,"MAE_90D_pct":-3.47,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH","trigger_id":"TRG_R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH","symbol":"032350","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_reopening_score":11,"visitor_demand_bridge_score":10,"revenue_conversion_score":8,"sellthrough_margin_score":5,"relative_strength_score":12,"theme_reversal_risk_penalty":7},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_reopening_score":8,"visitor_demand_bridge_score":13,"revenue_conversion_score":10,"sellthrough_margin_score":6,"relative_strength_score":8,"theme_reversal_risk_penalty":10},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["policy_reopening_score","visitor_demand_bridge_score","revenue_conversion_score","sellthrough_margin_score","relative_strength_score","theme_reversal_risk_penalty"],"component_delta_explanation":"C31 service-policy bridge works, but high-MAE/reversal risk prevents Green loosening.","MFE_90D_pct":32.43,"MAE_90D_pct":-31.61,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE","trigger_id":"TRG_R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE","symbol":"008770","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_reopening_score":12,"visitor_demand_bridge_score":3,"revenue_conversion_score":1,"sellthrough_margin_score":0,"relative_strength_score":12,"theme_reversal_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_reopening_score":5,"visitor_demand_bridge_score":0,"revenue_conversion_score":0,"sellthrough_margin_score":0,"relative_strength_score":5,"theme_reversal_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["policy_reopening_score","visitor_demand_bridge_score","revenue_conversion_score","sellthrough_margin_score","relative_strength_score","theme_reversal_risk_penalty"],"component_delta_explanation":"C31 guard demotes tourism/duty-free policy theme when sell-through, revenue, margin, or inventory bridge is absent.","MFE_90D_pct":8.29,"MAE_90D_pct":-33.29,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_service_policy_requires_visitor_revenue_sellthrough_margin_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"R12 service branch: tourism/inbound policy rows should not promote toward Stage3-Yellow/Green unless reopening policy converts into visitor demand, revenue, sell-through, margin, or cashflow bridge","114090 survives with cleaner MFE/MAE after casino visitor-demand bridge; 032350 has MFE but requires 4B/high-MAE watch; 008770 fails when duty-free theme lacks sell-through/margin bridge","TRG_R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE|TRG_R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH|TRG_R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_tourism_reopening_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Tourism reopening winners and duty-free failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 114090/032350 positives while preventing 008770 tourism-theme false positive","TRG_R12L72_C31_114090_20220926_CASINO_INBOUND_POLICY_DEMAND_BRIDGE|TRG_R12L72_C31_032350_20230810_JEJU_CASINO_TRAVEL_REOPENING_4B_WATCH|TRG_R12L72_C31_008770_20230810_DUTYFREE_TOURISM_POLICY_NO_SELLTHROUGH_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["tourism_policy_without_sellthrough_margin_bridge","inbound_policy_winner_needs_4B_watch","casino_reopening_success_low_MAE_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
11. Add validation that C31 service/tourism policy rows cannot promote without visitor/revenue/sell-through/margin bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R12
completed_loop = 72
next_round = R13
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
atlas/symbol_profiles/114/114090.json
atlas/symbol_profiles/032/032350.json
atlas/symbol_profiles/008/008770.json
atlas/ohlcv_tradable_by_symbol_year/114/114090/2022.csv
atlas/ohlcv_tradable_by_symbol_year/114/114090/2023.csv
atlas/ohlcv_tradable_by_symbol_year/032/032350/2023.csv
atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv
```

This loop adds 3 new independent C31 representative service/tourism-policy cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R12/L10.
