# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R10
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 74
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_LIQUIDITY_BALANCE_PF_CASHFLOW_BRIDGE_GUARD
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

R10 maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The immediately prior R9 file also used the allowed L9/C30 branch, so this R10 run avoids that set and chooses a different fine branch: liquidity-supported builder repair versus regional/small-builder PF theme failures.

| layer | id | definition |
|---|---|---|
| round | R10 | construction / real estate / housing |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, real estate, housing, PF and balance-sheet risk |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF, liquidity, balance sheet, trust and cashflow break/repair |
| fine | C30_LIQUIDITY_BALANCE_PF_CASHFLOW_BRIDGE_GUARD | promotion requires liquidity, balance, PF-risk, order or cashflow bridge |
| deep | RETAIL_AFFILIATED_BUILDER_LIQUIDITY_SUPPORT_AND_PF_RISK_CONTAINMENT_TO_RERATING | liquidity repair positive |
| deep | REGIONAL_BUILDER_POLITICAL_OR_HOUSING_THEME_WITHOUT_ORDER_BALANCE_CASHFLOW_CONVERSION | regional builder theme watch |
| deep | SMALL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_PF_BALANCE_LIQUIDITY_CASHFLOW_REPAIR | small builder false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols are `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that cluster and also avoids recent C30 representatives including `003070`, `010960`, `002410`, `012630`, `002460`, `001470`, `375500`, `021320`, `014790`, `013580`, `004960`, and `002990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 034300 | new independent | not top-covered C30 symbol; liquidity/balance/PF repair bridge |
| C30 | 013360 | new independent | not top-covered C30 symbol; regional builder theme MFE without cashflow bridge |
| C30 | 002780 | new independent | not top-covered C30 symbol; small-builder value rebound false start |
| excluded | 001880 | blocked | 2024 forward window insufficient due 2024-02-07 tradable last date |

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
034300 has a 2024-02-06 corporate-action candidate, so the selected 2024-03-05 entry is after the blocked date.
013360 has corporate-action candidates ending 2017, outside the selected 2024 representative window.
002780 has corporate-action candidates ending 2015, outside the selected 2024 representative window.
001880/DL건설 was inspected but excluded because the profile's tradable last_date is 2024-02-07, so a clean 180D forward window is unavailable.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch_after_liquidity_repair | 034300 | 신세계건설 | Stage2-Actionable | 2024-03-05 | 10730 | liquidity/balance/PF repair bridge worked |
| theme_MFE_then_high_MAE_counterexample | 013360 | 일성건설 | Stage2-Actionable | 2024-01-29 | 1285 | regional builder theme had MFE but no durable cashflow bridge |
| failed_rerating_low_MFE_high_MAE_counterexample | 002780 | 진흥기업 | Stage2-Actionable | 2024-01-29 | 1046 | small-builder PF value rebound lacked balance/liquidity/cashflow bridge |

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
| 034300 | 신세계건설 | Stage2-Actionable | 2024-03-05 | 10730 | 7.74 | 73.81 | 73.81 | -6.99 | -8.2 | -8.2 | 2024-05-30 | 18650 | -40.16 |
| 013360 | 일성건설 | Stage2-Actionable | 2024-01-29 | 1285 | 5.6 | 23.19 | 44.75 | -13.62 | -13.62 | -13.62 | 2024-07-23 | 1860 | -31.72 |
| 002780 | 진흥기업 | Stage2-Actionable | 2024-01-29 | 1046 | 9.85 | 9.85 | 9.85 | -5.64 | -9.27 | -24.0 | 2024-02-26 | 1149 | -30.81 |

## 9. Case-by-Case Notes

### 9.1 034300 / 신세계건설 — liquidity-supported PF repair

The entry row is 2024-03-05 at 10,730. The 30D window reaches only 11,560, but the 90D/180D window reaches 18,650. This is a valid C30 repair case because the move is tied to liquidity support, balance repair, and PF-risk containment rather than a generic construction candle. The post-peak low still requires 4B and drawdown watch.

### 9.2 013360 / 일성건설 — regional builder theme without durable source bridge

The entry row is 2024-01-29 at 1,285. The path reaches 1,860, but early MAE and the absence of a verified order/cashflow/balance bridge mean the row should not be Green. It is the classic regional-builder theme shape: the price can jump, but the balance sheet must still breathe.

### 9.3 002780 / 진흥기업 — small-builder value rebound false start

The entry row is 2024-01-29 at 1,046. The high only reaches 1,149 while the 180D low falls to 795. This is a cleaner counterexample. A small-builder/PF relief narrative without orderbook, liquidity, balance repair, trust quality, and cashflow should be demoted to Watch or 4B/high-MAE guard.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats regional/small-builder PF theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs liquidity/balance/PF/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 013360/002780. |
| Full 4B non-price requirement appropriate? | Yes. 034300 has a non-price bridge; 013360/002780 do not. |
| 4C timing issue? | High-MAE watch is sufficient for these representatives; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
034300:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after liquidity/balance/PF repair bridge
  Stage3-Green = reject unless drawdown and repair durability clear after 4B review

013360:
  Stage2-Actionable = acceptable only as theme/watch
  Stage3-Yellow = reject without orderbook, balance, PF-risk and cashflow bridge
  Stage3-Green = reject despite MFE

002780:
  Stage2-Actionable = too generous if based only on small-builder value rebound
  Stage3-Yellow = reject without liquidity, balance repair, order and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 034300 | 1.00 | 1.00 | liquidity repair positive but local/full-window 4B watch |
| 013360 | 0.69 | 1.00 | theme MFE but no source bridge; keep 4B/high-MAE watch |
| 002780 | 1.00 | 1.00 | small-builder local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_liquidity_balance_pf_cashflow_bridge

rule:
  For C30 construction/PF rows, do not promote construction, housing,
  regional-builder, PF relief, or value-rebound Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  orderbook/backlog, NAV or balance repair, PF-risk containment, liquidity/refinancing,
  trust-quality repair, order-to-cashflow visibility, asset support, or credible capital-structure improvement.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 35.62 | -10.36 | 66.7% | too generous to regional/small-builder theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 35.62 | -10.36 | 33.3% | safer but may miss 034300 |
| P1 sector_specific_candidate_profile | 3 | 35.62 | -10.36 | 66.7% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 73.81 | -8.2 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 16.52 | -11.45 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 034300 | current_profile_correct_with_drawdown_guard | liquidity/PF repair bridge aligned with strong MFE, but needs 4B |
| 013360 | current_profile_false_positive_if_green | regional-builder theme MFE lacked durable cashflow/balance bridge |
| 002780 | current_profile_false_positive | small-builder rebound produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_LIQUIDITY_BALANCE_PF_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R10 C30 liquidity/balance/PF cashflow residual reduced |

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
- regional builder theme without cashflow bridge
- liquidity repair winner needs 4B watch
- small-builder/PF value rebound low-MFE high-MAE
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
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- 001880/DL건설 as representative row because clean 180D forward window was unavailable
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_liquidity_balance_pf_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction/housing rebound converts into orderbook, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, asset support, or capital-structure bridge","034300 survives with strong MFE after liquidity/PF repair bridge; 013360 and 002780 remain 4B/high-MAE watch because regional-builder theme lacks durable cashflow and balance bridge","TRG_R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE|TRG_R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE|TRG_R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_regional_builder_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Regional-builder and PF repair rows can peak before cashflow and balance repair is proven; local/full-window 4B and high-MAE watch should remain active","preserves 034300 guarded positive while preventing 013360/002780 regional-builder false positives","TRG_R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE|TRG_R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE|TRG_R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_RETAIL_BUILDER_LIQUIDITY_BALANCE_PF_REPAIR_BRIDGE","deep_sub_archetype_id":"RETAIL_AFFILIATED_BUILDER_LIQUIDITY_SUPPORT_AND_PF_RISK_CONTAINMENT_TO_RERATING","case_type":"structural_success_then_4B_watch_after_liquidity_repair","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require orderbook, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, asset support, or capital-structure bridge; construction/PF price theme alone is insufficient."}
{"row_type":"case","case_id":"R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE","symbol":"013360","company_name":"일성건설","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_THEME_WITHOUT_ORDER_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_BUILDER_POLITICAL_OR_HOUSING_THEME_WITHOUT_ORDER_BALANCE_CASHFLOW_CONVERSION","case_type":"theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require orderbook, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, asset support, or capital-structure bridge; construction/PF price theme alone is insufficient."}
{"row_type":"case","case_id":"R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START","symbol":"002780","company_name":"진흥기업","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_SMALL_BUILDER_PF_VALUE_REBOUND_WITHOUT_LIQUIDITY_BRIDGE","deep_sub_archetype_id":"SMALL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_PF_BALANCE_LIQUIDITY_CASHFLOW_REPAIR","case_type":"failed_rerating_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require orderbook, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, asset support, or capital-structure bridge; construction/PF price theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE","case_id":"R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_RETAIL_BUILDER_LIQUIDITY_BALANCE_PF_REPAIR_BRIDGE","deep_sub_archetype_id":"RETAIL_AFFILIATED_BUILDER_LIQUIDITY_SUPPORT_AND_PF_RISK_CONTAINMENT_TO_RERATING","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":10730,"evidence_available_at_that_date":"source_proxy_retail_affiliated_builder_liquidity_support_PF_risk_containment_balance_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_retail_affiliated_builder_liquidity_support_PF_risk_containment_balance_repair_bridge; evidence_url_pending","bridge_summary":"retail-affiliated builder liquidity/balance repair and PF-risk containment converted into strong MFE, but post-peak drawdown required 4B watch rather than Green loosening","stage2_evidence_fields":["construction_PF_repair","liquidity_support_proxy","balance_sheet_repair_proxy","relative_strength"],"stage3_evidence_fields":["PF_risk_containment","liquidity_to_balance_visibility","asset_or_support_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","construction_repair_crowding_after_liquidity_event"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv","profile_path":"atlas/symbol_profiles/034/034300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.74,"MFE_90D_pct":73.81,"MFE_180D_pct":73.81,"MFE_1Y_pct":73.81,"MFE_2Y_pct":73.81,"MAE_30D_pct":-6.99,"MAE_90D_pct":-8.2,"MAE_180D_pct":-8.2,"MAE_1Y_pct":-8.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-30","peak_price":18650,"drawdown_after_peak_pct":-40.16,"green_lateness_ratio":"0.39","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"liquidity_repair_positive_but_local_full_window_4B_watch","four_b_evidence_type":"non_price_liquidity_balance_PF_repair_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE","case_id":"R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE","symbol":"013360","company_name":"일성건설","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_THEME_WITHOUT_ORDER_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_BUILDER_POLITICAL_OR_HOUSING_THEME_WITHOUT_ORDER_BALANCE_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1285,"evidence_available_at_that_date":"source_proxy_regional_builder_political_or_housing_theme_without_order_balance_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_builder_political_or_housing_theme_without_order_balance_cashflow_bridge; evidence_url_pending","bridge_summary":"regional-builder/housing theme produced MFE, but durable orderbook, balance repair, PF containment, liquidity and cashflow bridge were not visible enough","stage2_evidence_fields":["regional_builder_theme","housing_policy_or_political_beta","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_MFE_peak","orderbook_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv","profile_path":"atlas/symbol_profiles/013/013360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.6,"MFE_90D_pct":23.19,"MFE_180D_pct":44.75,"MFE_1Y_pct":44.75,"MFE_2Y_pct":44.75,"MAE_30D_pct":-13.62,"MAE_90D_pct":-13.62,"MAE_180D_pct":-13.62,"MAE_1Y_pct":-13.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":1860,"drawdown_after_peak_pct":-31.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_MFE_but_no_source_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"construction_theme_without_liquidity_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START","case_id":"R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START","symbol":"002780","company_name":"진흥기업","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_SMALL_BUILDER_PF_VALUE_REBOUND_WITHOUT_LIQUIDITY_BRIDGE","deep_sub_archetype_id":"SMALL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_PF_BALANCE_LIQUIDITY_CASHFLOW_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1046,"evidence_available_at_that_date":"source_proxy_small_builder_PF_value_rebound_without_order_balance_liquidity_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_small_builder_PF_value_rebound_without_order_balance_liquidity_cashflow_bridge; evidence_url_pending","bridge_summary":"small-builder/PF value rebound lacked orderbook, balance repair, liquidity/refinancing, trust-quality and cashflow bridge; forward path degraded into high MAE","stage2_evidence_fields":["small_builder_value_rebound","PF_relief_expectation","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","liquidity_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_balance_or_liquidity_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv","profile_path":"atlas/symbol_profiles/002/002780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.85,"MFE_90D_pct":9.85,"MFE_180D_pct":9.85,"MFE_1Y_pct":9.85,"MFE_2Y_pct":9.85,"MAE_30D_pct":-5.64,"MAE_90D_pct":-9.27,"MAE_180D_pct":-24.0,"MAE_1Y_pct":-24.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-26","peak_price":1149,"drawdown_after_peak_pct":-30.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_builder_local_4B_watch_not_positive_stage","four_b_evidence_type":"construction_theme_without_liquidity_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE","trigger_id":"TRG_R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE","symbol":"034300","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":10,"balance_repair_score":12,"PF_risk_bridge_score":12,"liquidity_cashflow_score":12,"relative_strength_score":9,"risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":12,"balance_repair_score":15,"PF_risk_bridge_score":15,"liquidity_cashflow_score":15,"relative_strength_score":8,"risk_penalty":7},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 row is promoted only because builder/PF signal converts into liquidity support, balance repair and PF-risk containment; 4B guard remains active.","MFE_90D_pct":73.81,"MAE_90D_pct":-8.2,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE","trigger_id":"TRG_R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE","symbol":"013360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"balance_repair_score":1,"PF_risk_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"balance_repair_score":0,"PF_risk_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction/PF or regional-builder theme rows when orderbook, balance repair, liquidity and cashflow bridge are absent.","MFE_90D_pct":23.19,"MAE_90D_pct":-13.62,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START","trigger_id":"TRG_R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START","symbol":"002780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"balance_repair_score":1,"PF_risk_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"balance_repair_score":0,"PF_risk_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction/PF or regional-builder theme rows when orderbook, balance repair, liquidity and cashflow bridge are absent.","MFE_90D_pct":9.85,"MAE_90D_pct":-9.27,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_liquidity_balance_pf_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction/housing rebound converts into orderbook, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, asset support, or capital-structure bridge","034300 survives with strong MFE after liquidity/PF repair bridge; 013360 and 002780 remain 4B/high-MAE watch because regional-builder theme lacks durable cashflow and balance bridge","TRG_R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE|TRG_R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE|TRG_R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_regional_builder_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Regional-builder and PF repair rows can peak before cashflow and balance repair is proven; local/full-window 4B and high-MAE watch should remain active","preserves 034300 guarded positive while preventing 013360/002780 regional-builder false positives","TRG_R10L74_C30_034300_20240305_RETAIL_BUILDER_PF_LIQUIDITY_REPAIR_BRIDGE|TRG_R10L74_C30_013360_20240129_REGIONAL_BUILDER_POLITICAL_THEME_NO_CASHFLOW_BRIDGE|TRG_R10L74_C30_002780_20240129_SMALL_BUILDER_PF_VALUE_REBOUND_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["regional_builder_theme_without_cashflow_bridge","liquidity_repair_winner_needs_4B_watch","small_builder_PF_value_rebound_low_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R10-specific handling

- R10 must use `L9_CONSTRUCTION_REALESTATE_HOUSING`.
- This MD uses `L9_CONSTRUCTION_REALESTATE_HOUSING / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`.
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
- price-only/construction-theme-only rows cannot promote Stage2/Stage3.
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
12. Add validation that C30 construction/PF rows cannot promote without orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality repair, order-to-cashflow visibility, asset support, or capital-structure bridge.
13. Add validation that insufficient forward-window candidates like 001880/DL건설 are blocked from representative calibration rows.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R10
completed_loop = 74
next_round = R11
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
atlas/symbol_profiles/034/034300.json
atlas/symbol_profiles/013/013360.json
atlas/symbol_profiles/002/002780.json
atlas/symbol_profiles/001/001880.json
atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv
```

This loop continues loop 74 with R10 and adds 3 new independent C30 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R10/L9.
