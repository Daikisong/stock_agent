# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R10
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 72
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_BALANCE_PF_CREDIT_LIQUIDITY_CASHFLOW_BRIDGE_GUARD
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

R10 maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The prior R10 loop already tested C30 with DL이앤씨/KCC건설/HL D&I. This run avoids those symbols and avoids the top-covered C30 cluster. The residual is the same fire door, but with a narrower hinge: construction/PF rows should only pass upward when rebound is backed by balance-sheet repair, PF-credit relief, refinancing/liquidity, or cashflow visibility.

| layer | id | definition |
|---|---|---|
| round | R10 | construction / real estate / housing |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, real estate, PF, balance-sheet risk |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF / liquidity / balance sheet break or repair |
| fine | C30_BALANCE_PF_CREDIT_LIQUIDITY_CASHFLOW_BRIDGE_GUARD | promotion requires balance/PF-credit/liquidity/cashflow bridge |
| deep | PUBLIC_ORDER_BACKLOG_BALANCE_REPAIR_WITH_CONTAINED_PF_RISK | regional builder low-MAE repair |
| deep | SMALL_BUILDER_BALANCE_REPAIR_REBOUND_BUT_4B_HIGH_MAE_WATCH | small builder repair rebound with guard |
| deep | CONSTRUCTION_VALUE_REBOUND_WITHOUT_BALANCE_REPAIR_OR_CASHFLOW_BRIDGE | PF-credit bridge absent false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols are `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that cluster and also avoids the immediately prior R10 symbols `375500`, `021320`, and `014790`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 013580 | new independent | not top-covered C30 symbol; regional builder low-MAE repair |
| C30 | 004960 | new independent | not top-covered C30 symbol; small-builder repair rebound with drawdown guard |
| C30 | 002990 | new independent | not top-covered C30 symbol; PF-credit bridge absent false start |

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

A hard-4C TaeYoung-style workout row was reviewed but excluded as a representative row because the later 2024 trading-resumption/corporate-action candidate window contaminates a clean 180D calibration window. This MD therefore keeps the hard-4C point as narrative-only background and uses three clean representative C30 rows.

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_low_MAE_repair | 013580 | 계룡건설 | Stage2-Actionable | 2024-01-29 | 14080 | regional builder balance/PF repair bridge worked |
| structural_success_with_drawdown_watch | 004960 | 한신공영 | Stage2-Actionable | 2024-07-08 | 6390 | repair rebound worked, but 4B/high-MAE guard needed |
| failed_rerating_high_MAE | 002990 | 금호건설 | Stage2-Actionable | 2024-01-29 | 5100 | PF-credit bridge absent false start failed |

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
| 013580 | 계룡건설 | Stage2-Actionable | 2024-01-29 | 14080 | 9.59 | 9.59 | 10.65 | -4.9 | -9.09 | -9.09 | 2024-08-21 | 15580 | -12.9 |
| 004960 | 한신공영 | Stage2-Actionable | 2024-07-08 | 6390 | 18.31 | 18.31 | 18.31 | -1.25 | -1.25 | -9.7 | 2024-07-30 | 7560 | -23.68 |
| 002990 | 금호건설 | Stage2-Actionable | 2024-01-29 | 5100 | 3.53 | 3.53 | 3.53 | -2.35 | -17.65 | -38.14 | 2024-02-01 | 5280 | -40.25 |

## 9. Case-by-Case Notes

### 9.1 013580 / 계룡건설 — regional builder low-MAE repair

The entry row is 2024-01-29 at 14,080. The 30D and 90D path was modest, but downside was contained and the full window eventually reached 15,580. This is a C30 positive only in a low-beta repair sense. It supports Stage2/Yelllow when public-order/backlog, balance-sheet repair, and PF-risk containment are visible; it does not support looser Green.

### 9.2 004960 / 한신공영 — small-builder repair rebound with drawdown guard

The entry row is 2024-07-08 at 6,390. The price path reaches 7,560 quickly but later falls to 5,770 in the wider forward window. This is useful C30 evidence because the rebound worked, but the correct overlay is 4B/high-MAE watch. Repair is a bridge, not a castle wall.

### 9.3 002990 / 금호건설 — PF-credit bridge absent false start

The entry row is 2024-01-29 at 5,100. The upside only reaches 5,280 while the 180D low reaches 3,155. This is the C30 failure mode: cheap construction equity and PF relief language cannot become Stage3 without refinancing/liquidity/cashflow evidence. The price path says the floor was paper, not concrete.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats construction/PF relief rebound as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs balance-sheet, PF-credit, liquidity, or cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 002990 and after 004960's rebound. |
| Full 4B non-price requirement appropriate? | Yes. 013580/004960 have better repair bridge; 002990 does not. |
| 4C timing issue? | High-MAE watch should fire before hard 4C. Hard-4C workout rows remain useful but require clean-window handling. |

## 11. Stage2 / Yellow / Green Comparison

```text
013580:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after low-MAE repair bridge
  Stage3-Green = reject unless stronger cashflow/PF-risk repair is confirmed

004960:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with active 4B/high-MAE watch
  Stage3-Green = reject unless drawdown and credit-risk guard clear

002990:
  Stage2-Actionable = too generous if based only on construction value/PF-relief rebound
  Stage3-Yellow = reject without PF-credit/liquidity/cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 013580 | 0.94 | 1.00 | low-volatility 4B watch after balance repair bridge |
| 004960 | 0.98 | 1.00 | good 4B watch but requires credit drawdown guard |
| 002990 | 1.00 | 1.00 | weak local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_balance_pf_credit_liquidity_cashflow_bridge

rule:
  For C30 construction/PF rows, do not promote construction-value, housing, or PF-relief
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  balance-sheet repair, PF-credit exposure reduction, debt refinancing,
  liquidity support, cashflow quality improvement, public-order backlog durability,
  asset sale, or credible capital structure repair.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 10.48 | -9.33 | 33.3% | useful but can over-credit PF relief rebound |
| P0b e2r_2_0_baseline_reference | 3 | 10.48 | -9.33 | 0% | safer but may miss repair/low-MAE positives |
| P1 sector_specific_candidate_profile | 3 | 10.48 | -9.33 | 33.3% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 13.95 | -5.17 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 3.53 | -17.65 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 013580 | current_profile_correct | low-MAE repair bridge aligned with positive path |
| 004960 | current_profile_partially_correct | rebound worked, but drawdown requires 4B/high-MAE watch |
| 002990 | current_profile_false_positive | weak PF relief rebound produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_BALANCE_PF_CREDIT_LIQUIDITY_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C30 non-top-covered regional/small-builder repair residual reduced |

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
- earlier_thesis_break_watch
residual_error_types_found:
- PF-credit bridge absent false start
- small-builder repair rebound needs drawdown guard
- regional builder low-MAE repair success
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_MAE_watch_guard
- earlier_thesis_break_watch
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
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- excluded TaeYoung-style hard-4C row due to 180D clean-window contamination
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_balance_pf_credit_liquidity_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction rebound converts into balance-sheet repair, PF-credit bridge, refinancing/liquidity, or cashflow visibility","013580 and 004960 survive as repair/rebound cases; 002990 fails with low MFE and high MAE when repair bridge is absent","TRG_R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE|TRG_R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD|TRG_R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_pf_credit_rebound_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Construction repair winners and failed PF relief rebounds can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 013580/004960 positives while preventing 002990 PF-rebound false positive","TRG_R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE|TRG_R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD|TRG_R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE","symbol":"013580","company_name":"계룡건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_BALANCE_SHEET_REPAIR_LOW_MAE","deep_sub_archetype_id":"PUBLIC_ORDER_BACKLOG_BALANCE_REPAIR_WITH_CONTAINED_PF_RISK","case_type":"structural_success_low_MAE_repair","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require balance-sheet repair, PF/credit bridge, refinancing/liquidity evidence, or cashflow bridge; construction value rebound alone is insufficient."}
{"row_type":"case","case_id":"R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD","symbol":"004960","company_name":"한신공영","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_SMALL_BUILDER_REPAIR_REBOUND_WITH_CREDIT_GUARD","deep_sub_archetype_id":"SMALL_BUILDER_BALANCE_REPAIR_REBOUND_BUT_4B_HIGH_MAE_WATCH","case_type":"structural_success_with_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require balance-sheet repair, PF/credit bridge, refinancing/liquidity evidence, or cashflow bridge; construction value rebound alone is insufficient."}
{"row_type":"case","case_id":"R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","symbol":"002990","company_name":"금호건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","deep_sub_archetype_id":"CONSTRUCTION_VALUE_REBOUND_WITHOUT_BALANCE_REPAIR_OR_CASHFLOW_BRIDGE","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require balance-sheet repair, PF/credit bridge, refinancing/liquidity evidence, or cashflow bridge; construction value rebound alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE","case_id":"R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE","symbol":"013580","company_name":"계룡건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_BALANCE_SHEET_REPAIR_LOW_MAE","deep_sub_archetype_id":"PUBLIC_ORDER_BACKLOG_BALANCE_REPAIR_WITH_CONTAINED_PF_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":14080,"evidence_available_at_that_date":"source_proxy_regional_builder_balance_sheet_repair_public_order_backlog; evidence_url_pending","evidence_source":"source_proxy_regional_builder_balance_sheet_repair_public_order_backlog; evidence_url_pending","bridge_summary":"regional construction rerating worked only as a low-volatility repair case because public-order/backlog and balance-sheet repair proxies kept MAE contained","stage2_evidence_fields":["regional_builder_repair","public_order_backlog_proxy","balance_sheet_repair_proxy","low_MAE_confirmation"],"stage3_evidence_fields":["repair_visibility","order_backlog_to_cashflow_proxy","PF_credit_risk_contained"],"stage4b_evidence_fields":["low_beta_repricing_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv","profile_path":"atlas/symbol_profiles/013/013580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.59,"MFE_90D_pct":9.59,"MFE_180D_pct":10.65,"MFE_1Y_pct":10.65,"MFE_2Y_pct":10.65,"MAE_30D_pct":-4.9,"MAE_90D_pct":-9.09,"MAE_180D_pct":-9.09,"MAE_1Y_pct":-9.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":15580,"drawdown_after_peak_pct":-12.9,"green_lateness_ratio":"0.54","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_volatility_4B_watch_after_balance_repair_bridge","four_b_evidence_type":"non_price_balance_repair_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD","case_id":"R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD","symbol":"004960","company_name":"한신공영","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_SMALL_BUILDER_REPAIR_REBOUND_WITH_CREDIT_GUARD","deep_sub_archetype_id":"SMALL_BUILDER_BALANCE_REPAIR_REBOUND_BUT_4B_HIGH_MAE_WATCH","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-08","entry_date":"2024-07-08","entry_price":6390,"evidence_available_at_that_date":"source_proxy_small_builder_balance_repair_rebound_with_credit_guard; evidence_url_pending","evidence_source":"source_proxy_small_builder_balance_repair_rebound_with_credit_guard; evidence_url_pending","bridge_summary":"small-builder repair rebound produced tradable MFE only when balance/PF watch remained active; later drawdown argues against Green loosening","stage2_evidence_fields":["small_builder_repair_rebound","credit_risk_watch","relative_strength_after_base","non_price_repair_proxy"],"stage3_evidence_fields":["repair_path_visibility","drawdown_guard_needed"],"stage4b_evidence_fields":["post_repair_rebound_peak_watch","credit_spread_or_PF_watch"],"stage4c_evidence_fields":["high_MAE_watch_after_rebound"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv|atlas/ohlcv_tradable_by_symbol_year/004/004960/2025.csv","profile_path":"atlas/symbol_profiles/004/004960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.31,"MFE_90D_pct":18.31,"MFE_180D_pct":18.31,"MFE_1Y_pct":18.31,"MFE_2Y_pct":18.31,"MAE_30D_pct":-1.25,"MAE_90D_pct":-1.25,"MAE_180D_pct":-9.7,"MAE_1Y_pct":-9.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":7560,"drawdown_after_peak_pct":-23.68,"green_lateness_ratio":"0.40","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_credit_drawdown_guard","four_b_evidence_type":"non_price_balance_repair_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","case_id":"R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","symbol":"002990","company_name":"금호건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","deep_sub_archetype_id":"CONSTRUCTION_VALUE_REBOUND_WITHOUT_BALANCE_REPAIR_OR_CASHFLOW_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":5100,"evidence_available_at_that_date":"source_proxy_construction_value_rebound_without_PF_credit_balance_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_construction_value_rebound_without_PF_credit_balance_repair_bridge; evidence_url_pending","bridge_summary":"construction value/PF relief narrative lacked actual balance-sheet, refinancing, liquidity, or cashflow bridge and rolled into high MAE","stage2_evidence_fields":["construction_value_rebound","PF_relief_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","credit_risk_unresolved","price_only_rebound"],"stage4c_evidence_fields":["high_MAE_without_balance_sheet_repair"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv","profile_path":"atlas/symbol_profiles/002/002990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.53,"MFE_90D_pct":3.53,"MFE_180D_pct":3.53,"MFE_1Y_pct":3.53,"MFE_2Y_pct":3.53,"MAE_30D_pct":-2.35,"MAE_90D_pct":-17.65,"MAE_180D_pct":-38.14,"MAE_1Y_pct":-38.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":5280,"drawdown_after_peak_pct":-40.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_PF_credit_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE","trigger_id":"TRG_R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE","symbol":"013580","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"balance_sheet_repair_score":12,"PF_credit_bridge_score":10,"liquidity_refinancing_score":8,"cashflow_visibility_score":8,"relative_strength_score":8,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"balance_sheet_repair_score":15,"PF_credit_bridge_score":13,"liquidity_refinancing_score":10,"cashflow_visibility_score":10,"relative_strength_score":6,"risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["balance_sheet_repair_score","PF_credit_bridge_score","liquidity_refinancing_score","cashflow_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 row is promoted only because balance-sheet/PF-credit repair and low-MAE confirmation support the rebound.","MFE_90D_pct":9.59,"MAE_90D_pct":-9.09,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD","trigger_id":"TRG_R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD","symbol":"004960","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"balance_sheet_repair_score":10,"PF_credit_bridge_score":8,"liquidity_refinancing_score":6,"cashflow_visibility_score":6,"relative_strength_score":10,"risk_penalty":7},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"balance_sheet_repair_score":12,"PF_credit_bridge_score":10,"liquidity_refinancing_score":7,"cashflow_visibility_score":7,"relative_strength_score":7,"risk_penalty":9},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["balance_sheet_repair_score","PF_credit_bridge_score","liquidity_refinancing_score","cashflow_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 repair rebound works, but post-MFE drawdown and credit risk prevent Green loosening.","MFE_90D_pct":18.31,"MAE_90D_pct":-1.25,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","trigger_id":"TRG_R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START","symbol":"002990","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"balance_sheet_repair_score":3,"PF_credit_bridge_score":1,"liquidity_refinancing_score":1,"cashflow_visibility_score":1,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"balance_sheet_repair_score":0,"PF_credit_bridge_score":0,"liquidity_refinancing_score":0,"cashflow_visibility_score":0,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["balance_sheet_repair_score","PF_credit_bridge_score","liquidity_refinancing_score","cashflow_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction/PF rebound when balance-sheet, refinancing, liquidity, or cashflow bridge is absent.","MFE_90D_pct":3.53,"MAE_90D_pct":-17.65,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_balance_pf_credit_liquidity_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction rebound converts into balance-sheet repair, PF-credit bridge, refinancing/liquidity, or cashflow visibility","013580 and 004960 survive as repair/rebound cases; 002990 fails with low MFE and high MAE when repair bridge is absent","TRG_R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE|TRG_R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD|TRG_R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_pf_credit_rebound_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Construction repair winners and failed PF relief rebounds can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 013580/004960 positives while preventing 002990 PF-rebound false positive","TRG_R10L72_C30_013580_20240129_REGIONAL_BUILDER_BALANCE_REPAIR_LOW_MAE|TRG_R10L72_C30_004960_20240708_SMALL_BUILDER_REPAIR_REBOUND_WITH_DRAWDOWN_GUARD|TRG_R10L72_C30_002990_20240129_PF_CREDIT_BRIDGE_ABSENT_FALSE_START",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail","earlier_thesis_break_watch"],"residual_error_types_found":["PF_credit_bridge_absent_false_start","small_builder_repair_rebound_needs_drawdown_guard","regional_builder_low_MAE_repair_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
11. Add validation that hard-4C workout rows with trading-resumption / corporate-action contamination are accepted only as narrative or blocked rows unless a clean forward window is available.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R10
completed_loop = 72
next_round = R11
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
atlas/symbol_profiles/013/013580.json
atlas/symbol_profiles/004/004960.json
atlas/symbol_profiles/002/002990.json
atlas/symbol_profiles/009/009410.json
atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv
atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv
atlas/ohlcv_tradable_by_symbol_year/004/004960/2025.csv
atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv
```

This loop adds 3 new independent C30 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R10/L9.
