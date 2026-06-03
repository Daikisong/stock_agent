# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R10
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 76
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_ORDER_BALANCE_PRICE_COST_MARGIN_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
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

R10 maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The immediately previous R9 loop already used the allowed L9/C30 branch with formwork rental, regional policy construction and concrete pile. This R10 run therefore stays in the direct L9 branch but rotates the fine branch to cement price-cost margin and regional contractor rebound.

| layer | id | definition |
|---|---|---|
| round | R10 | construction / real estate / housing |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, housing, real estate, PF, cement/materials and balance sheet |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF, liquidity, balance sheet, order/cashflow repair |
| fine | C30_ORDER_BALANCE_PRICE_COST_MARGIN_CASHFLOW_BRIDGE_GUARD | construction signal must become order, balance, spread, margin and cashflow evidence |
| deep | CEMENT_PRICE_COST_SPREAD_AND_VOLUME_TO_MARGIN_CASHFLOW_STABILITY | cement positive |
| deep | LARGE_CEMENT_SCALE_PRICE_COST_SPREAD_TO_MARGIN_OPERATING_LEVERAGE_AND_CASHFLOW | large cement positive |
| deep | REGIONAL_CONTRACTOR_POLICY_REBOUND_WITHOUT_ORDERBOOK_PF_RISK_BALANCE_OR_CASHFLOW_CONVERSION | contractor rebound false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols remain `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run also avoids recent C30 representatives `035890`, `007210`, `010780`, `018310`, `025950`, `228340`, `003070`, `010960`, `002410`, `034300`, `013360`, `002780`, `012630`, `002460`, `001470`, `375500`, `021320`, `014790`, `013580`, `004960`, and `002990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 183190 | new independent | not top-covered C30 symbol; cement price-cost margin/cashflow bridge |
| C30 | 300720 | new independent | not top-covered C30 symbol; large cement scale price-cost margin bridge |
| C30 | 001260 | new independent | not top-covered C30 symbol; regional contractor rebound without durable orderbook/cashflow bridge |

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
MFE/MAE/peak/drawdown computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
183190 has a 2022-04-06 corporate-action candidate, outside the selected 2024 representative window.
300720 has corporate-action candidates ending 2021-09-13, outside the selected 2024 representative window.
001260 has corporate-action candidates ending 2016-02-05, outside the selected 2024 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| cement_price_cost_margin_success_then_4B_watch | 183190 | 아세아시멘트 | Stage2-Actionable | 2024-01-29 | 10260 | cement price-cost margin/cashflow bridge worked, but 4B drawdown watch required |
| large_cement_margin_repricing_success_then_4B_watch | 300720 | 한일시멘트 | Stage2-Actionable | 2024-02-01 | 12100 | large cement scale/spread margin bridge worked, but post-peak spread-cycle guard required |
| regional_contractor_rebound_MFE_then_high_MAE_counterexample | 001260 | 남광토건 | Stage2-Actionable | 2024-01-29 | 6860 | regional contractor rebound MFE lacked orderbook/PF/balance/cashflow bridge |

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
| 183190 | 아세아시멘트 | Stage2-Actionable | 2024-01-29 | 10260 | 13.16 | 13.16 | 15.98 | -2.34 | -4.58 | -4.58 | 2024-07-31 | 11900 | -14.62 |
| 300720 | 한일시멘트 | Stage2-Actionable | 2024-02-01 | 12100 | 6.69 | 12.73 | 29.75 | -2.73 | -2.73 | -2.73 | 2024-08-23 | 15700 | -16.82 |
| 001260 | 남광토건 | Stage2-Actionable | 2024-01-29 | 6860 | 11.66 | 11.66 | 24.64 | -3.79 | -12.24 | -13.27 | 2024-07-30 | 8550 | -30.41 |

## 9. Case-by-Case Notes

### 9.1 183190 / 아세아시멘트 — cement price-cost margin bridge

The entry row is 2024-01-29 at 10,260. The early path reached 11,610 and the broader path reached 11,900. This is a valid C30 positive because the bridge is not construction-theme MFE. The bridge is cement price-cost spread, fuel-cost relief, disciplined volume/mix, margin and cashflow stability. The later drawdown after the full-window peak keeps 4B active and blocks Green.

### 9.2 300720 / 한일시멘트 — large cement scale and margin bridge

The entry row is 2024-02-01 at 12,100. The path reached 12,910 early, 13,640 in the wider 90D area, and 15,700 around the full-window peak. This is a positive C30 cement branch because scale, price-cost spread and operating leverage created a margin/cashflow bridge. It is still guarded Yellow because cement demand and spread-cycle sensitivity remain active after the peak.

### 9.3 001260 / 남광토건 — regional contractor rebound without durable source bridge

The entry row is 2024-01-29 at 6,860. It produced MFE later, reaching 8,550, but also fell to 5,950 after the peak. This is a counterexample because the price rebound did not prove orderbook, PF-risk containment, balance repair, margin or cashflow. The row is useful precisely because MFE exists: it tests that the model does not confuse delayed price recovery with a source bridge.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats regional contractor rebound MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs price-cost/margin/cashflow or orderbook/balance bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 001260 delayed MFE without source bridge. |
| Full 4B non-price requirement appropriate? | Yes. 183190/300720 have stronger non-price bridges; 001260 does not. |
| 4C timing issue? | High-MAE and delayed-MFE watch are useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
183190:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after cement price-cost spread / margin / cashflow bridge
  Stage3-Green = reject unless construction-cycle and spread-reversal risk clear

300720:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after scale / price-cost spread / operating-leverage bridge
  Stage3-Green = reject because post-peak spread-cycle guard remains active

001260:
  Stage2-Actionable = acceptable only as regional contractor rebound watch
  Stage3-Yellow = reject without orderbook, PF-risk containment, balance repair, margin and cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 183190 | 0.98 | 1.00 | cement price-cost margin bridge positive but full-window 4B watch |
| 300720 | 0.82 | 1.00 | large cement margin bridge positive but full-window 4B drawdown watch |
| 001260 | 0.90 | 1.00 | regional contractor rebound MFE but no order/cashflow bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_order_balance_price_cost_margin_cashflow_bridge

rule:
  For C30 construction/PF rows, do not promote construction, cement,
  construction-material, regional contractor, housing, developer, remodeling,
  infrastructure policy or balance-sheet-rebound Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  orderbook/backlog, site-order visibility, price-cost spread improvement,
  asset utilization, balance repair, PF-risk containment, liquidity/refinancing,
  order-to-cashflow visibility, working-capital control, margin conversion,
  FCF/cash conversion, asset support, or credible capital-structure improvement.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 12.52 | -6.52 | 33.3% | useful but can over-credit contractor rebound MFE |
| P0b e2r_2_0_baseline_reference | 3 | 12.52 | -6.52 | 0% | safer but may miss 183190/300720 |
| P1 sector_specific_candidate_profile | 3 | 12.52 | -6.52 | 33.3% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 12.95 | -3.66 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 11.66 | -12.24 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 183190 | current_profile_correct_but_no_green | price-cost/margin/cashflow bridge aligned with MFE, but 4B watch remains |
| 300720 | current_profile_correct_with_drawdown_guard | cement scale/margin bridge aligned with MFE, but drawdown guard remains |
| 001260 | current_profile_false_positive_if_green | regional contractor delayed MFE lacked orderbook/cashflow bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_ORDER_BALANCE_PRICE_COST_MARGIN_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | R10/L9 C30 cement and contractor residual reduced |

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
- regional contractor rebound without order/cashflow bridge
- cement price-cost margin winner needs 4B watch
- cement scale margin winner needs drawdown guard
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
- R10 direct L9 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/report URLs
- exact cement price-cost or construction orderbook disclosure URLs
- production scoring behavior
- live candidate status
- additional reviewed but unused C30 materials/engineering candidates
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_order_balance_price_cost_margin_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction/cement/contractor signal converts into orderbook/backlog, price-cost spread, asset utilization, balance repair, PF-risk containment, liquidity/refinancing, margin, working-capital or cashflow bridge","183190 and 300720 survive as guarded positives after cement price-cost margin/cashflow bridge; 001260 is demoted because regional contractor rebound MFE lacked orderbook, PF-risk, balance and cashflow bridge","TRG_R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE|TRG_R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE|TRG_R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; R10 direct L9 branch"
shadow_weight,c30_cement_contractor_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Cement winners and contractor/policy false starts can peak before spread, orderbook and cashflow durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 183190/300720 guarded positives while preventing 001260 contractor-rebound false positive","TRG_R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE|TRG_R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE|TRG_R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens delayed-MFE/local-full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","symbol":"183190","company_name":"아세아시멘트","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CEMENT_PRICE_COST_SPREAD_AND_VOLUME_TO_MARGIN_CASHFLOW_STABILITY","case_type":"cement_price_cost_margin_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R10 direct L9 branch. C30 construction/PF/balance-sheet rows require orderbook/backlog, price-cost spread, asset utilization, balance repair, PF-risk containment, liquidity, margin, working-capital or cashflow bridge; cement/contractor policy MFE alone is insufficient."}
{"row_type":"case","case_id":"R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","symbol":"300720","company_name":"한일시멘트","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","deep_sub_archetype_id":"LARGE_CEMENT_SCALE_PRICE_COST_SPREAD_TO_MARGIN_OPERATING_LEVERAGE_AND_CASHFLOW","case_type":"large_cement_margin_repricing_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"R10 direct L9 branch. C30 construction/PF/balance-sheet rows require orderbook/backlog, price-cost spread, asset utilization, balance repair, PF-risk containment, liquidity, margin, working-capital or cashflow bridge; cement/contractor policy MFE alone is insufficient."}
{"row_type":"case","case_id":"R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE","symbol":"001260","company_name":"남광토건","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_CONTRACTOR_REBOUND_WITHOUT_ORDER_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_CONTRACTOR_POLICY_REBOUND_WITHOUT_ORDERBOOK_PF_RISK_BALANCE_OR_CASHFLOW_CONVERSION","case_type":"regional_contractor_rebound_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R10 direct L9 branch. C30 construction/PF/balance-sheet rows require orderbook/backlog, price-cost spread, asset utilization, balance repair, PF-risk containment, liquidity, margin, working-capital or cashflow bridge; cement/contractor policy MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","case_id":"R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","symbol":"183190","company_name":"아세아시멘트","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CEMENT_PRICE_COST_SPREAD_AND_VOLUME_TO_MARGIN_CASHFLOW_STABILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10260,"evidence_available_at_that_date":"source_proxy_cement_price_cost_spread_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_cement_price_cost_spread_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"cement price-cost spread, fuel-cost relief and disciplined volume/mix converted into margin and cashflow stability bridge, but construction-cycle and spread-reversal risk required 4B watch","stage2_evidence_fields":["cement_price_cost_spread","fuel_cost_relief_proxy","relative_strength","cashflow_stability_proxy"],"stage3_evidence_fields":["price_cost_spread_to_margin_visibility","volume_mix_stability","cashflow_conversion_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","cement_cycle_crowding","spread_reversal_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/183/183190/2024.csv","profile_path":"atlas/symbol_profiles/183/183190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.16,"MFE_90D_pct":13.16,"MFE_180D_pct":15.98,"MFE_1Y_pct":15.98,"MFE_2Y_pct":15.98,"MAE_30D_pct":-2.34,"MAE_90D_pct":-4.58,"MAE_180D_pct":-4.58,"MAE_1Y_pct":-4.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":11900,"drawdown_after_peak_pct":-14.62,"green_lateness_ratio":"0.48","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cement_price_cost_margin_bridge_positive_but_full_window_4B_watch","four_b_evidence_type":"non_price_price_cost_margin_cashflow_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"cement_price_cost_margin_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","case_id":"R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","symbol":"300720","company_name":"한일시멘트","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","deep_sub_archetype_id":"LARGE_CEMENT_SCALE_PRICE_COST_SPREAD_TO_MARGIN_OPERATING_LEVERAGE_AND_CASHFLOW","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12100,"evidence_available_at_that_date":"source_proxy_large_cement_price_cost_spread_scale_margin_operating_leverage_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_large_cement_price_cost_spread_scale_margin_operating_leverage_cashflow_bridge; evidence_url_pending","bridge_summary":"large cement scale, price-cost spread and operating leverage converted into margin/cashflow rerating bridge, but post-peak spread-cycle and construction demand sensitivity required 4B watch","stage2_evidence_fields":["cement_scale","price_cost_spread_recovery","relative_strength","operating_leverage_proxy"],"stage3_evidence_fields":["spread_to_margin_visibility","scale_cashflow_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","cement_cycle_crowding","construction_demand_sensitivity"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/300/300720/2024.csv","profile_path":"atlas/symbol_profiles/300/300720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.69,"MFE_90D_pct":12.73,"MFE_180D_pct":29.75,"MFE_1Y_pct":29.75,"MFE_2Y_pct":29.75,"MAE_30D_pct":-2.73,"MAE_90D_pct":-2.73,"MAE_180D_pct":-2.73,"MAE_1Y_pct":-2.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-23","peak_price":15700,"drawdown_after_peak_pct":-16.82,"green_lateness_ratio":"0.44","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_cement_margin_repricing_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_price_cost_margin_cashflow_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"large_cement_margin_repricing_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE","case_id":"R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE","symbol":"001260","company_name":"남광토건","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_CONTRACTOR_REBOUND_WITHOUT_ORDER_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_CONTRACTOR_POLICY_REBOUND_WITHOUT_ORDERBOOK_PF_RISK_BALANCE_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":6860,"evidence_available_at_that_date":"source_proxy_regional_contractor_policy_rebound_without_orderbook_PF_balance_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_contractor_policy_rebound_without_orderbook_PF_balance_cashflow_bridge; evidence_url_pending","bridge_summary":"regional contractor/policy rebound eventually produced MFE, but orderbook, PF-risk containment, balance repair, margin and cashflow bridge were weak; high MAE remained active","stage2_evidence_fields":["regional_contractor_rebound","construction_policy_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["delayed_MFE_peak","orderbook_bridge_absent","balance_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_orderbook_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv","profile_path":"atlas/symbol_profiles/001/001260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.66,"MFE_90D_pct":11.66,"MFE_180D_pct":24.64,"MFE_1Y_pct":24.64,"MFE_2Y_pct":24.64,"MAE_30D_pct":-3.79,"MAE_90D_pct":-12.24,"MAE_180D_pct":-13.27,"MAE_1Y_pct":-13.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":8550,"drawdown_after_peak_pct":-30.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regional_contractor_rebound_MFE_but_no_order_cashflow_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"contractor_policy_rebound_without_order_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"regional_contractor_rebound_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","trigger_id":"TRG_R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","symbol":"183190","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":7,"asset_balance_score":8,"PF_risk_bridge_score":5,"price_cost_margin_score":12,"liquidity_cashflow_score":11,"relative_strength_score":9,"risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":8,"asset_balance_score":9,"PF_risk_bridge_score":6,"price_cost_margin_score":15,"liquidity_cashflow_score":14,"relative_strength_score":8,"risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["orderbook_score","asset_balance_score","PF_risk_bridge_score","price_cost_margin_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 cement row is promoted only because construction-material signal converts into price-cost spread, margin and cashflow bridge; construction-cycle and post-peak 4B watch block Green.","MFE_90D_pct":13.16,"MAE_90D_pct":-4.58,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","trigger_id":"TRG_R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE","symbol":"300720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":7,"asset_balance_score":8,"PF_risk_bridge_score":5,"price_cost_margin_score":12,"liquidity_cashflow_score":11,"relative_strength_score":9,"risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":8,"asset_balance_score":9,"PF_risk_bridge_score":6,"price_cost_margin_score":15,"liquidity_cashflow_score":14,"relative_strength_score":8,"risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["orderbook_score","asset_balance_score","PF_risk_bridge_score","price_cost_margin_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 cement row is promoted only because construction-material signal converts into price-cost spread, margin and cashflow bridge; construction-cycle and post-peak 4B watch block Green.","MFE_90D_pct":12.73,"MAE_90D_pct":-2.73,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE","trigger_id":"TRG_R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE","symbol":"001260","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"asset_balance_score":2,"PF_risk_bridge_score":1,"price_cost_margin_score":2,"liquidity_cashflow_score":0,"relative_strength_score":9,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"asset_balance_score":0,"PF_risk_bridge_score":0,"price_cost_margin_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","asset_balance_score","PF_risk_bridge_score","price_cost_margin_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes regional contractor/policy rebound rows when orderbook, PF-risk containment, balance repair, margin and cashflow bridge are absent.","MFE_90D_pct":11.66,"MAE_90D_pct":-12.24,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_order_balance_price_cost_margin_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction/cement/contractor signal converts into orderbook/backlog, price-cost spread, asset utilization, balance repair, PF-risk containment, liquidity/refinancing, margin, working-capital or cashflow bridge","183190 and 300720 survive as guarded positives after cement price-cost margin/cashflow bridge; 001260 is demoted because regional contractor rebound MFE lacked orderbook, PF-risk, balance and cashflow bridge","TRG_R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE|TRG_R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE|TRG_R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; R10 direct L9 branch"
shadow_weight,c30_cement_contractor_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Cement winners and contractor/policy false starts can peak before spread, orderbook and cashflow durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 183190/300720 guarded positives while preventing 001260 contractor-rebound false positive","TRG_R10L76_C30_183190_20240129_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE|TRG_R10L76_C30_300720_20240201_CEMENT_SCALE_PRICE_COST_MARGIN_BRIDGE|TRG_R10L76_C30_001260_20240129_REGIONAL_CONTRACTOR_REBOUND_NO_ORDER_CASHFLOW_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens delayed-MFE/local-full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["regional_contractor_rebound_without_order_cashflow_bridge","cement_price_cost_margin_winner_needs_4B_watch","cement_scale_margin_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R10-specific handling

- R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`.
- This MD uses `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`.
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
- Positive score promotion requires non-price evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/construction-cement-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R10 direct L9 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C30 construction/PF rows cannot promote without orderbook/backlog, site-order visibility, price-cost spread improvement, asset utilization, balance repair, PF-risk containment, liquidity/refinancing, order-to-cashflow visibility, working-capital control, margin conversion, FCF/cash conversion, asset support, or capital-structure improvement.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R10
completed_loop = 76
next_round = R11
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
atlas/symbol_profiles/183/183190.json
atlas/symbol_profiles/300/300720.json
atlas/symbol_profiles/001/001260.json
atlas/ohlcv_tradable_by_symbol_year/183/183190/2024.csv
atlas/ohlcv_tradable_by_symbol_year/300/300720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv
```

This loop continues loop 76 with R10 and adds 3 new independent C30 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R10/L9.
