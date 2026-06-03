# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R10
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 73
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_NAV_BALANCE_PF_LIQUIDITY_CASHFLOW_BRIDGE_GUARD
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

R10 maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The previous R10 runs already covered the better-known C30 construction/PF names and the regional/small-builder repair branch. This run stays within C30, but uses new symbols and a different failure branch: holdco/housing NAV repair versus regional builder false start versus construction-theme trust break.

| layer | id | definition |
|---|---|---|
| round | R10 | construction / real estate / housing |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, housing, real estate, PF and balance-sheet risk |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF, liquidity, balance sheet, trust and cashflow break/repair |
| fine | C30_NAV_BALANCE_PF_LIQUIDITY_CASHFLOW_BRIDGE_GUARD | promotion requires NAV/balance/PF/liquidity/cashflow bridge |
| deep | HOLDCO_HOUSING_NAV_DISCOUNT_REPAIR_WITH_PF_RISK_CONTAINMENT | holdco housing/NAV repair success |
| deep | REGIONAL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_CASHFLOW_OR_PF_REPAIR_CONVERSION | regional builder low-MFE false start |
| deep | CONSTRUCTION_THEME_PRICE_SPIKE_WITHOUT_PF_TRUST_BALANCE_OR_CASHFLOW_REPAIR | construction theme high-MAE trust-break watch |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols are `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that cluster and also avoids prior R10 symbols `375500`, `021320`, `014790`, `013580`, `004960`, and `002990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 012630 | new independent | not top-covered C30 symbol; holdco/housing NAV and PF repair bridge |
| C30 | 002460 | new independent | not top-covered C30 symbol; regional builder low-MFE false start |
| C30 | 001470 | new independent | not top-covered C30 symbol; construction/PF theme high-MAE trust-break watch |

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
012630 has corporate-action candidate dates ending 2018, outside the selected 2024 window.
002460 has corporate-action candidate dates ending 2002, outside the selected 2024 window.
001470 has corporate-action candidate dates ending 2019, outside the selected 2024 window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 012630 | HDC | Stage2-Actionable | 2024-01-29 | 7170 | holdco/housing NAV and PF repair bridge worked |
| failed_rerating_low_MFE_high_MAE | 002460 | HS화성 | Stage2-Actionable | 2024-01-29 | 10500 | regional builder rebound lacked order/cashflow/PF bridge |
| failed_rerating_high_MAE_thesis_break_watch | 001470 | 삼부토건 | Stage2-Actionable | 2024-01-29 | 2020 | construction/PF theme lacked balance/trust/cashflow bridge |

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
| 012630 | HDC | Stage2-Actionable | 2024-01-29 | 7170 | 23.01 | 23.01 | 59.0 | -5.58 | -5.58 | -5.58 | 2024-09-20 | 11400 | -7.28 |
| 002460 | HS화성 | Stage2-Actionable | 2024-01-29 | 10500 | 6.95 | 6.95 | 6.95 | -4.29 | -9.62 | -19.52 | 2024-02-19 | 11230 | -24.76 |
| 001470 | 삼부토건 | Stage2-Actionable | 2024-01-29 | 2020 | 37.62 | 41.83 | 41.83 | -7.82 | -25.25 | -78.22 | 2024-03-15 | 2865 | -84.64 |

## 9. Case-by-Case Notes

### 9.1 012630 / HDC — holdco housing/NAV repair bridge

The entry row is 2024-01-29 at 7,170. The initial path was not a straight line, but the later 180D window reaches 11,400. This is a valid C30 positive because the signal is not just a construction rebound. It is holdco/housing NAV discount repair, PF-risk containment, and asset-value bridge. The delayed path means Yellow plus 4B watch is the right interpretation, not Green loosening.

### 9.2 002460 / HS화성 — regional builder low-MFE false start

The entry row is 2024-01-29 at 10,500. The best forward high is only 11,230, while the 180D low falls to 8,450. This is the regional-builder failure mode: value rebound and housing repair language are not enough unless order backlog, cashflow, margin, and PF-risk repair move with it.

### 9.3 001470 / 삼부토건 — construction theme and trust-break high MAE

The entry row is 2024-01-29 at 2,020. It reaches 2,865, but then falls to 440 in the broad forward window. This is exactly why C30 needs a trust-quality and balance-sheet guard. A construction/PF theme can make the first candle tall; without liquidity, cashflow, PF-credit repair, and accounting/trust quality, the same candle becomes a warning flare.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats construction/PF theme or value rebound as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs NAV/balance/PF/liquidity/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 001470 and weak local peaks. |
| Full 4B non-price requirement appropriate? | Yes. 012630 has a better non-price bridge; 002460/001470 do not. |
| 4C timing issue? | High-MAE and earlier thesis-break watch should fire before hard 4C. No immediate production hard-4C delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
012630:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after NAV/PF-risk repair and balance bridge
  Stage3-Green = reject unless cashflow/liquidity durability and 4B review clear

002460:
  Stage2-Actionable = too generous if based only on regional builder value rebound
  Stage3-Yellow = reject without order/cashflow/PF repair bridge
  Stage3-Green = reject

001470:
  Stage2-Actionable = too generous if based only on construction/PF theme price strength
  Stage3-Yellow = reject without balance, liquidity, trust-quality, or cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 012630 | 0.77 | 1.00 | delayed full-window 4B watch after NAV/PF repair bridge |
| 002460 | 1.00 | 1.00 | weak local 4B watch, not positive stage |
| 001470 | 1.00 | 1.00 | theme local 4B watch and high-MAE/thesis-break guard |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_nav_balance_pf_liquidity_cashflow_bridge

rule:
  For C30 construction/PF rows, do not promote housing, construction, PF relief,
  regional builder, or value-rebound Stage2 signals into Stage3-Yellow/Green unless
  at least one non-price bridge is visible:
  NAV discount repair, balance-sheet repair, PF-credit exposure reduction,
  liquidity/refinancing support, trust-quality repair, order/cashflow visibility,
  asset sale, or credible capital-structure improvement.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 23.93 | -13.48 | 66.7% | too generous to construction/PF theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 23.93 | -13.48 | 33.3% | safer but may miss 012630 |
| P1 sector_specific_candidate_profile | 3 | 23.93 | -13.48 | 66.7% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 23.01 | -5.58 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 24.39 | -17.43 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 012630 | current_profile_correct | NAV/PF repair bridge aligned with delayed strong MFE |
| 002460 | current_profile_false_positive | regional builder rebound produced low MFE and high MAE |
| 001470 | current_profile_false_positive | construction/PF theme produced high-MAE thesis-break watch path |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_NAV_BALANCE_PF_LIQUIDITY_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C30 non-top-covered NAV/PF repair and trust-break residual reduced |

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
- construction theme without balance/cashflow bridge
- regional builder low-MFE high-MAE false start
- holdco housing NAV/PF repair success needs 4B watch
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
shadow_weight,c30_requires_nav_balance_pf_liquidity_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction/housing rebound converts into NAV repair, balance-sheet repair, PF-credit containment, liquidity/refinancing, trust-quality, or cashflow bridge","012630 survives with delayed MFE after NAV/PF-repair bridge; 002460 and 001470 fail when construction/PF theme lacks cashflow or balance bridge","TRG_R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE|TRG_R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START|TRG_R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_pf_theme_4b_high_mae_thesis_break_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Construction/PF winners and theme failures can peak quickly; local 4B/high-MAE/thesis-break watch must remain active after MFE","preserves 012630 positive while preventing 002460/001470 construction-theme false positives","TRG_R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE|TRG_R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START|TRG_R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE and earlier thesis-break watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","symbol":"012630","company_name":"HDC","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","deep_sub_archetype_id":"HOLDCO_HOUSING_NAV_DISCOUNT_REPAIR_WITH_PF_RISK_CONTAINMENT","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require NAV/balance repair, PF-credit containment, liquidity/refinancing, order/cashflow, or trust-quality bridge; construction/PF theme alone is insufficient."}
{"row_type":"case","case_id":"R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START","symbol":"002460","company_name":"HS화성","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_REPAIR_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_CASHFLOW_OR_PF_REPAIR_CONVERSION","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require NAV/balance repair, PF-credit containment, liquidity/refinancing, order/cashflow, or trust-quality bridge; construction/PF theme alone is insufficient."}
{"row_type":"case","case_id":"R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE","symbol":"001470","company_name":"삼부토건","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CONSTRUCTION_THEME_WITHOUT_BALANCE_TRUST_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONSTRUCTION_THEME_PRICE_SPIKE_WITHOUT_PF_TRUST_BALANCE_OR_CASHFLOW_REPAIR","case_type":"failed_rerating_high_MAE_thesis_break_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF rows require NAV/balance repair, PF-credit containment, liquidity/refinancing, order/cashflow, or trust-quality bridge; construction/PF theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","case_id":"R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","symbol":"012630","company_name":"HDC","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","deep_sub_archetype_id":"HOLDCO_HOUSING_NAV_DISCOUNT_REPAIR_WITH_PF_RISK_CONTAINMENT","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":7170,"evidence_available_at_that_date":"source_proxy_holdco_housing_NAV_discount_repair_PF_risk_containment; evidence_url_pending","evidence_source":"source_proxy_holdco_housing_NAV_discount_repair_PF_risk_containment; evidence_url_pending","bridge_summary":"holdco/housing NAV discount repair and PF-risk containment produced a delayed but durable MFE path; this is repair evidence, not a construction theme candle","stage2_evidence_fields":["housing_valueup_repair","NAV_discount_repair_proxy","PF_risk_containment_proxy","relative_strength"],"stage3_evidence_fields":["NAV_repair_visibility","balance_sheet_PF_risk_containment","cashflow_or_asset_value_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","housing_repair_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv","profile_path":"atlas/symbol_profiles/012/012630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.01,"MFE_90D_pct":23.01,"MFE_180D_pct":59.0,"MFE_1Y_pct":59.0,"MFE_2Y_pct":59.0,"MAE_30D_pct":-5.58,"MAE_90D_pct":-5.58,"MAE_180D_pct":-5.58,"MAE_1Y_pct":-5.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-20","peak_price":11400,"drawdown_after_peak_pct":-7.28,"green_lateness_ratio":"0.55","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"delayed_full_window_4B_watch_after_NAV_PF_repair_bridge","four_b_evidence_type":"non_price_NAV_balance_PF_repair_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START","case_id":"R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START","symbol":"002460","company_name":"HS화성","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_REPAIR_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_CASHFLOW_OR_PF_REPAIR_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10500,"evidence_available_at_that_date":"source_proxy_regional_builder_value_rebound_without_order_cashflow_PF_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_builder_value_rebound_without_order_cashflow_PF_bridge; evidence_url_pending","bridge_summary":"regional builder repair/value rebound failed to convert into cashflow, order backlog, margin, or PF-credit repair; upside stayed shallow while MAE expanded","stage2_evidence_fields":["regional_builder_value_rebound","housing_repair_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","order_cashflow_bridge_absent","PF_credit_repair_unconfirmed"],"stage4c_evidence_fields":["high_MAE_without_cashflow_or_PF_repair_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv","profile_path":"atlas/symbol_profiles/002/002460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.95,"MFE_90D_pct":6.95,"MFE_180D_pct":6.95,"MFE_1Y_pct":6.95,"MFE_2Y_pct":6.95,"MAE_30D_pct":-4.29,"MAE_90D_pct":-9.62,"MAE_180D_pct":-19.52,"MAE_1Y_pct":-19.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":11230,"drawdown_after_peak_pct":-24.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_balance_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE","case_id":"R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE","symbol":"001470","company_name":"삼부토건","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CONSTRUCTION_THEME_WITHOUT_BALANCE_TRUST_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONSTRUCTION_THEME_PRICE_SPIKE_WITHOUT_PF_TRUST_BALANCE_OR_CASHFLOW_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":2020,"evidence_available_at_that_date":"source_proxy_construction_theme_price_spike_without_PF_trust_balance_cashflow_repair; evidence_url_pending","evidence_source":"source_proxy_construction_theme_price_spike_without_PF_trust_balance_cashflow_repair; evidence_url_pending","bridge_summary":"construction/PF relief and theme price strength lacked balance-sheet repair, trust-quality, liquidity, and cashflow bridge; the path later turned into a high-MAE thesis-break watch","stage2_evidence_fields":["construction_theme","PF_relief_expectation","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","trust_balance_bridge_absent","liquidity_or_cashflow_risk"],"stage4c_evidence_fields":["high_MAE_after_balance_trust_break_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv","profile_path":"atlas/symbol_profiles/001/001470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.62,"MFE_90D_pct":41.83,"MFE_180D_pct":41.83,"MFE_1Y_pct":41.83,"MFE_2Y_pct":41.83,"MAE_30D_pct":-7.82,"MAE_90D_pct":-25.25,"MAE_180D_pct":-78.22,"MAE_1Y_pct":-78.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":2865,"drawdown_after_peak_pct":-84.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_local_4B_watch_not_positive_stage_and_high_MAE_guard","four_b_evidence_type":"price_theme_without_balance_cashflow_bridge","four_c_protection_label":"high_MAE_thesis_break_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","trigger_id":"TRG_R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE","symbol":"012630","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"NAV_repair_score":12,"balance_sheet_repair_score":11,"PF_credit_bridge_score":12,"liquidity_cashflow_score":8,"relative_strength_score":9,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"NAV_repair_score":15,"balance_sheet_repair_score":14,"PF_credit_bridge_score":14,"liquidity_cashflow_score":10,"relative_strength_score":7,"risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["NAV_repair_score","balance_sheet_repair_score","PF_credit_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 row is promoted only because housing/NAV repair is tied to PF-risk containment, asset-value bridge, and balance-sheet repair.","MFE_90D_pct":23.01,"MAE_90D_pct":-5.58,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START","trigger_id":"TRG_R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START","symbol":"002460","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"NAV_repair_score":4,"balance_sheet_repair_score":1,"PF_credit_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":11,"risk_penalty":9},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"NAV_repair_score":1,"balance_sheet_repair_score":0,"PF_credit_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["NAV_repair_score","balance_sheet_repair_score","PF_credit_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction/PF rebound when balance repair, PF-credit bridge, liquidity, trust-quality, or cashflow evidence is absent.","MFE_90D_pct":6.95,"MAE_90D_pct":-9.62,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE","trigger_id":"TRG_R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE","symbol":"001470","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"NAV_repair_score":4,"balance_sheet_repair_score":1,"PF_credit_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":11,"risk_penalty":9},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"NAV_repair_score":1,"balance_sheet_repair_score":0,"PF_credit_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["NAV_repair_score","balance_sheet_repair_score","PF_credit_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction/PF rebound when balance repair, PF-credit bridge, liquidity, trust-quality, or cashflow evidence is absent.","MFE_90D_pct":41.83,"MAE_90D_pct":-25.25,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_nav_balance_pf_liquidity_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction/housing rebound converts into NAV repair, balance-sheet repair, PF-credit containment, liquidity/refinancing, trust-quality, or cashflow bridge","012630 survives with delayed MFE after NAV/PF-repair bridge; 002460 and 001470 fail when construction/PF theme lacks cashflow or balance bridge","TRG_R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE|TRG_R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START|TRG_R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_pf_theme_4b_high_mae_thesis_break_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Construction/PF winners and theme failures can peak quickly; local 4B/high-MAE/thesis-break watch must remain active after MFE","preserves 012630 positive while preventing 002460/001470 construction-theme false positives","TRG_R10L73_C30_012630_20240129_HOLDCO_HOUSING_NAV_PF_REPAIR_BRIDGE|TRG_R10L73_C30_002460_20240129_REGIONAL_BUILDER_LOW_MFE_REPAIR_FALSE_START|TRG_R10L73_C30_001470_20240129_CONSTRUCTION_THEME_PF_TRUST_BREAK_HIGH_MAE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE and earlier thesis-break watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"73","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail","earlier_thesis_break_watch"],"residual_error_types_found":["construction_theme_without_balance_cashflow_bridge","regional_builder_low_MFE_high_MAE_false_start","holdco_housing_NAV_PF_repair_success_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/construction-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C30 construction/PF rows cannot promote without NAV repair, balance repair, PF-credit containment, liquidity/refinancing, trust-quality, order/cashflow, or capital-structure bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R10
completed_loop = 73
next_round = R11
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
atlas/symbol_profiles/012/012630.json
atlas/symbol_profiles/002/002460.json
atlas/symbol_profiles/001/001470.json
atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv
atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv
```

This loop continues loop 73 with R10 and adds 3 new independent C30 representative cases, 1 positive, 2 counterexamples, and 2 residual errors for R10/L9/C30.
