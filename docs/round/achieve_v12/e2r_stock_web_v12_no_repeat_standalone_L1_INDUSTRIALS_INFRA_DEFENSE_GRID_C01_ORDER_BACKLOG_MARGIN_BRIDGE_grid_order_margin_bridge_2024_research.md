# E2R Stock-Web V12 No-Repeat Standalone Residual Research
## C01_ORDER_BACKLOG_MARGIN_BRIDGE — Grid equipment order backlog / margin bridge, with cable-theme counterexample

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Metadata

```text
selected_round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE
loop_objective = coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test|counterexample_mining
price_source = Songdaiki/stock-web
primary_price_source_url = https://github.com/Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
duplicate_check_basis = docs/core/V12_Research_No_Repeat_Index.md
hard_duplicate_avoided = true
index_update_needed = true
```

## 1. Why this archetype was selected

`C01_ORDER_BACKLOG_MARGIN_BRIDGE` is present in the MAIN EXECUTION PROMPT canonical list, but it is not visible in the No-Repeat Index coverage table. That makes it a true coverage gap rather than another repeat of C03 defense exports, C04 nuclear, or C02 grid/datacenter capex.

This standalone MD therefore tests a narrower residual question:

```text
When industrial names rerate on power-grid / electrification demand,
does the current calibrated profile distinguish
(1) order backlog + margin conversion
from
(2) cable/theme price movement without enough margin bridge?
```

The research deliberately avoids the latest repeated C03/C02 cases and uses a new canonical scope. The selected symbols are all treated as new under C01.

## 2. No-repeat check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Checked against `V12_Research_No_Repeat_Index.md`:

| canonical | symbol | trigger_type | entry_date | duplicate status |
|---|---:|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010120 | Stage2-Actionable | 2024-04-05 | not listed under C01 |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 267260 | Stage2-Actionable | 2023-04-13 | not listed under C01 |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 001440 | Stage2 / failed-rerating counterexample | 2024-05-13 | not listed under C01 |

```text
hard_duplicate_avoided = true
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
new_trigger_family_count = 2
```

## 3. Stock-Web manifest and profile validation

Manifest fields used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Symbol profile checks:

| symbol | name | profile path | corporate-action candidate overlap with entry~D+180 | calibration status |
|---:|---|---|---|---|
| 010120 | LS ELECTRIC | atlas/symbol_profiles/010/010120.json | no 2024 overlap; historical candidates end 2003-04-16 | calibration usable |
| 267260 | HD현대일렉트릭 | atlas/symbol_profiles/267/267260.json | no 2023 overlap; historical candidates end 2019-12-30 | calibration usable |
| 001440 | 대한전선 | atlas/symbol_profiles/001/001440.json | 2024-04-02 candidate before 2024-05-13 entry; no entry~D+180 overlap | calibration usable with caveat noted |

## 4. Case set

### Case A — LS ELECTRIC / 010120 / structural success with later 4B risk

```text
case_id = C01_LS_ELECTRIC_20240405_GRID_ORDER_MARGIN_BRIDGE
symbol = 010120
company_name = LS ELECTRIC
case_role = structural_success_with_4B_watch
trigger_family = grid_equipment_order_backlog_margin_bridge
trigger_type = Stage2-Actionable
trigger_date = 2024-04-04
entry_date = 2024-04-05
entry_price = 118600
```

Evidence separation:

```text
stage2_evidence_fields:
- power-grid / electrification demand route
- order/backlog narrative
- margin bridge beginning to appear in market evidence
- relative strength against industrial peers

stage3_evidence_fields:
- confirmed revision path after the initial order/backlog signal
- multiple earnings/report/proxy evidence families
- durable backlog-to-margin conversion
- old-frame industrial multiple beginning to reprice

stage4b_evidence_fields:
- very fast rerating from 118600 to 274500 high
- valuation / crowding watch required after July peak

stage4c_evidence_fields:
- no hard thesis break inside the 180D validation window
- post-peak drawdown is a 4B/positioning issue, not automatic 4C
```

Stock-Web OHLC validation:

```text
source_shards:
- atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv

entry row:
2024-04-05,o=106300,h=120000,l=105500,c=118600

key forward rows:
2024-05-23,h=212500
2024-07-24,h=274500
2024-11-22,l=130900
```

Backtest path:

| metric | value |
|---|---:|
| entry_date | 2024-04-05 |
| entry_price | 118600 |
| MFE_30D_pct | 79.17 |
| MAE_30D_pct | -11.05 |
| MFE_90D_pct | 131.45 |
| MAE_90D_pct | -11.05 |
| MFE_180D_pct | 131.45 |
| MAE_180D_pct | -11.05 |
| peak_date | 2024-07-24 |
| peak_price | 274500 |
| peak_return_from_entry_pct | 131.45 |
| drawdown_after_peak_pct | -52.31 |

Interpretation:

```text
C01 should give Stage2/Stage3 credit only when order/backlog has a margin bridge.
LS ELECTRIC passed that test, but the later price path also proves that C01 needs a 4B watch once rerating becomes very fast.
```

### Case B — HD현대일렉트릭 / 267260 / earlier order backlog margin bridge success

```text
case_id = C01_HDHE_20230413_GRID_ORDER_BACKLOG_MARGIN
symbol = 267260
company_name = HD현대일렉트릭
case_role = structural_success
trigger_family = transformer_order_backlog_margin_bridge
trigger_type = Stage2-Actionable
trigger_date = 2023-04-12
entry_date = 2023-04-13
entry_price = 45500
```

Evidence separation:

```text
stage2_evidence_fields:
- transformer / power-equipment order backlog
- margin conversion route
- early earnings visibility

stage3_evidence_fields:
- later confirmed revision and margin expansion
- multiple public evidence families
- old-frame cyclical equipment view began to fail

stage4b_evidence_fields:
- 90D peak came quickly enough to require crowding watch, but not a price-only 4B

stage4c_evidence_fields:
- no hard 4C thesis break in the 180D validation window
```

Stock-Web OHLC validation:

```text
source_shards:
- atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv

entry row:
2023-04-13,o=40800,h=45850,l=40200,c=45500

key forward rows:
2023-04-25,h=54800
2023-07-26,h=84000
2023-09-01,l=61400
```

Backtest path:

| metric | value |
|---|---:|
| entry_date | 2023-04-13 |
| entry_price | 45500 |
| MFE_30D_pct | 20.44 |
| MAE_30D_pct | -11.65 |
| MFE_90D_pct | 84.62 |
| MAE_90D_pct | -11.65 |
| MFE_180D_pct | 84.62 |
| MAE_180D_pct | -11.65 |
| peak_date | 2023-07-26 |
| peak_price | 84000 |
| peak_return_from_entry_pct | 84.62 |
| drawdown_after_peak_pct | -26.90 |

Interpretation:

```text
This is the clean positive side of C01.
The price path supports an order/backlog-to-margin bridge rule, not just a broad grid theme rule.
```

### Case C — 대한전선 / 001440 / cable-theme counterexample

```text
case_id = C01_TAIHAN_20240513_CABLE_THEME_NO_MARGIN_BRIDGE
symbol = 001440
company_name = 대한전선
case_role = failed_rerating_counterexample
trigger_family = cable_theme_relative_strength_without_margin_bridge
trigger_type = Stage2
trigger_date = 2024-05-13
entry_date = 2024-05-13
entry_price = 18110
positive_or_counterexample = counterexample
```

Evidence separation:

```text
stage2_evidence_fields:
- cable / grid theme relative strength
- market attention around power-grid capex
- trading-value expansion

stage3_evidence_fields:
- insufficient backlog-to-margin bridge
- insufficient durable earnings visibility
- evidence stack weaker than LS ELECTRIC and HD현대일렉트릭

stage4b_evidence_fields:
- local blowoff to 20950 high
- failed to extend after the first local peak
- price-only or theme-heavy rerating must remain watch-only

stage4c_evidence_fields:
- later drawdown confirmed thesis weakness
- not necessarily accounting hard break, but a failed-rerating / margin-bridge failure
```

Stock-Web OHLC validation:

```text
source_shards:
- atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/001/001440/2025.csv

entry row:
2024-05-13,o=15000,h=18900,l=14640,c=18110

key forward rows:
2024-05-21,h=20950
2024-06-13,l=14050
2024-09-09,l=10270
2024-12-09,l=10000
```

Backtest path:

| metric | value |
|---|---:|
| entry_date | 2024-05-13 |
| entry_price | 18110 |
| MFE_30D_pct | 15.68 |
| MAE_30D_pct | -22.42 |
| MFE_90D_pct | 15.68 |
| MAE_90D_pct | -43.29 |
| MFE_180D_pct | 15.68 |
| MAE_180D_pct | -44.78 |
| peak_date | 2024-05-21 |
| peak_price | 20950 |
| peak_return_from_entry_pct | 15.68 |
| drawdown_after_peak_pct | -52.27 |

Interpretation:

```text
This is the counterexample C01 needs.
A grid/cable theme and price expansion are not enough. Without a visible order/backlog-to-margin bridge, the current profile should avoid Stage3-Green and should keep the case as Stage2 watch or 4B/false-positive guardrail.
```

## 5. Current calibrated profile stress test

Current calibrated profile assumptions tested:

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

Residual errors found:

| residual | affected case | explanation |
|---|---|---|
| current_profile_missed_structural | LS ELECTRIC / 010120 | If mapped only as generic C02 grid/datacenter capex, the profile may miss that the decisive bridge is backlog-to-margin conversion. |
| current_profile_false_positive_risk | 대한전선 / 001440 | If cable/grid relative strength is treated as enough Stage2/Green evidence, the later path shows a false-positive / high-MAE risk. |

```text
current_profile_error_count = 2
existing_axis_tested = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|stage2_actionable_evidence_bonus
existing_axis_kept = true
new_axis_proposed = C01_order_backlog_margin_bridge_requires_margin_visibility
```

## 6. Positive / counterexample balance

| role | count | cases |
|---|---:|---|
| structural_success | 2 | 010120, 267260 |
| failed_rerating_counterexample | 1 | 001440 |
| 4B / 4B-watch path | 2 | 010120, 001440 |
| hard 4C | 0 | none |

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
counterexample_search_incomplete = false
```

## 7. Shadow rule candidate

```text
shadow_rule_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE_V1
scope = canonical_archetype:C01_ORDER_BACKLOG_MARGIN_BRIDGE
rule_type = sector_specific_shadow_rule_candidate
production_scoring_changed = false
```

Proposed shadow behavior:

```text
1. Stage2-Actionable can be allowed when:
   - order/backlog or contract visibility exists,
   - margin bridge or revision bridge exists,
   - price action follows dated non-price evidence.

2. Stage3-Green must remain blocked when:
   - evidence is mostly price/theme,
   - backlog exists but margin conversion is not visible,
   - trading-value expansion is not supported by financial visibility.

3. 4B watch should be raised when:
   - MFE90 or peak_return_from_entry exceeds roughly 80~100% quickly,
   - rerating compresses the remaining valuation runway,
   - non-price evidence remains intact but crowding risk rises.
```

## 8. Residual contribution summary

```text
This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.
```

```text
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
do_not_propose_global_delta = true
index_update_needed = true
```

## 9. Machine-readable rows

### case rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C01_LS_ELECTRIC_20240405_GRID_ORDER_MARGIN_BRIDGE","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE","symbol":"010120","company_name":"LS ELECTRIC","positive_or_counterexample":"positive","case_type":"structural_success_with_4B_watch","trigger_family":"grid_equipment_order_backlog_margin_bridge","evidence_url_pending":false,"source_proxy_only":true,"new_independent_case":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C01_HDHE_20230413_GRID_ORDER_BACKLOG_MARGIN","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE","symbol":"267260","company_name":"HD현대일렉트릭","positive_or_counterexample":"positive","case_type":"structural_success","trigger_family":"transformer_order_backlog_margin_bridge","evidence_url_pending":false,"source_proxy_only":true,"new_independent_case":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C01_TAIHAN_20240513_CABLE_THEME_NO_MARGIN_BRIDGE","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE","symbol":"001440","company_name":"대한전선","positive_or_counterexample":"counterexample","case_type":"failed_rerating","trigger_family":"cable_theme_relative_strength_without_margin_bridge","evidence_url_pending":false,"source_proxy_only":true,"new_independent_case":true}
```

### trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRG_C01_010120_20240405_STAGE2A","case_id":"C01_LS_ELECTRIC_20240405_GRID_ORDER_MARGIN_BRIDGE","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"Stage2-Actionable","trigger_family":"grid_equipment_order_backlog_margin_bridge","trigger_date":"2024-04-04","entry_date":"2024-04-05","entry_price":118600,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","MFE_30D_pct":79.17,"MAE_30D_pct":-11.05,"MFE_90D_pct":131.45,"MAE_90D_pct":-11.05,"MFE_180D_pct":131.45,"MAE_180D_pct":-11.05,"peak_date":"2024-07-24","peak_price":274500,"peak_return_from_entry_pct":131.45,"drawdown_after_peak_pct":-52.31,"forward_window_trading_days":180,"corporate_action_window_status":"clean_no_overlap","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","current_profile_verdict":"current_profile_missed_structural_if_C01_bridge_not_available","trigger_outcome_label":"good_stage2_with_later_4B_watch","evidence_source":"historical_public_earnings_and_report_proxy_plus_stock_web_price_validation","source_proxy_only":true,"evidence_url_pending":false,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRG_C01_267260_20230413_STAGE2A","case_id":"C01_HDHE_20230413_GRID_ORDER_BACKLOG_MARGIN","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE","symbol":"267260","company_name":"HD현대일렉트릭","trigger_type":"Stage2-Actionable","trigger_family":"transformer_order_backlog_margin_bridge","trigger_date":"2023-04-12","entry_date":"2023-04-13","entry_price":45500,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv","MFE_30D_pct":20.44,"MAE_30D_pct":-11.65,"MFE_90D_pct":84.62,"MAE_90D_pct":-11.65,"MFE_180D_pct":84.62,"MAE_180D_pct":-11.65,"peak_date":"2023-07-26","peak_price":84000,"peak_return_from_entry_pct":84.62,"drawdown_after_peak_pct":-26.90,"forward_window_trading_days":180,"corporate_action_window_status":"clean_no_overlap","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","current_profile_verdict":"current_profile_correct_but_C01_bridge_would_explain_signal_cleaner","trigger_outcome_label":"good_stage2","evidence_source":"historical_public_earnings_and_report_proxy_plus_stock_web_price_validation","source_proxy_only":true,"evidence_url_pending":false,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRG_C01_001440_20240513_COUNTER","case_id":"C01_TAIHAN_20240513_CABLE_THEME_NO_MARGIN_BRIDGE","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ORDER_BACKLOG_MARGIN_GRID_EQUIPMENT_CABLE_COUNTEREXAMPLE","symbol":"001440","company_name":"대한전선","trigger_type":"Stage2","trigger_family":"cable_theme_relative_strength_without_margin_bridge","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":18110,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv","MFE_30D_pct":15.68,"MAE_30D_pct":-22.42,"MFE_90D_pct":15.68,"MAE_90D_pct":-43.29,"MFE_180D_pct":15.68,"MAE_180D_pct":-44.78,"peak_date":"2024-05-21","peak_price":20950,"peak_return_from_entry_pct":15.68,"drawdown_after_peak_pct":-52.27,"forward_window_trading_days":180,"corporate_action_window_status":"no_entry_to_d180_overlap_but_2024_04_02_profile_caveat_noted","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","current_profile_verdict":"current_profile_false_positive_risk_if_price_theme_treated_as_bridge","trigger_outcome_label":"bad_stage2_high_mae_failed_rerating","evidence_source":"historical_public_theme_and_capital_action_proxy_plus_stock_web_price_validation","source_proxy_only":true,"evidence_url_pending":false,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C01_LS_ELECTRIC_20240405_GRID_ORDER_MARGIN_BRIDGE","symbol":"010120","as_of_date":"2024-04-05","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores_before":{"eps_fcf_explosion":17,"earnings_visibility":17,"bottleneck_pricing":16,"market_mispricing":12,"valuation_rerating":11,"capital_allocation":3,"information_confidence":4},"raw_component_scores_after":{"eps_fcf_explosion":17,"earnings_visibility":19,"bottleneck_pricing":16,"market_mispricing":12,"valuation_rerating":11,"capital_allocation":3,"information_confidence":4},"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage3-Yellow","current_profile_error":true,"existing_axis_tested":"stage2_actionable_evidence_bonus|stage3_yellow_total_min|full_4b_requires_non_price_evidence"}
{"row_type":"score_simulation","case_id":"C01_HDHE_20230413_GRID_ORDER_BACKLOG_MARGIN","symbol":"267260","as_of_date":"2023-04-13","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores_before":{"eps_fcf_explosion":16,"earnings_visibility":16,"bottleneck_pricing":15,"market_mispricing":11,"valuation_rerating":10,"capital_allocation":3,"information_confidence":4},"raw_component_scores_after":{"eps_fcf_explosion":16,"earnings_visibility":18,"bottleneck_pricing":15,"market_mispricing":11,"valuation_rerating":10,"capital_allocation":3,"information_confidence":4},"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage2-Actionable","current_profile_error":false,"existing_axis_tested":"stage2_actionable_evidence_bonus"}
{"row_type":"score_simulation","case_id":"C01_TAIHAN_20240513_CABLE_THEME_NO_MARGIN_BRIDGE","symbol":"001440","as_of_date":"2024-05-13","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores_before":{"eps_fcf_explosion":10,"earnings_visibility":8,"bottleneck_pricing":12,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":2,"information_confidence":2},"raw_component_scores_after":{"eps_fcf_explosion":10,"earnings_visibility":6,"bottleneck_pricing":8,"market_mispricing":8,"valuation_rerating":6,"capital_allocation":2,"information_confidence":2},"stage_before":"Stage2","stage_after_shadow":"Stage1_or_Stage2_watch","current_profile_error":true,"existing_axis_tested":"price_only_blowoff_blocks_positive_stage|stage2_actionable_evidence_bonus"}
```

### aggregate and shadow rows

```jsonl
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","row_count":3,"unique_symbol_count":3,"positive_case_count":2,"counterexample_count":1,"good_stage2_count":2,"bad_stage2_count":1,"stage2_high_mae_count":1,"good_4b_timing_count":1,"price_only_4b_count":1,"evidence_url_pending_count":0,"source_proxy_only_count":3,"avg_stage2_MFE90":75.9167,"avg_stage2_MAE90":-22.0,"stage2_hit_rate_MFE90_ge_20":0.6667,"stage2_bad_entry_rate_MAE90_le_minus_20":0.3333}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","scope":"canonical_archetype:C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"stage2_required_bridge","shadow_candidate_value":"require_order_backlog_margin_bridge_non_price_evidence","direction":"tighten_stage2_bridge_for_theme_only_cases","reason":"Positive cases had order/backlog-to-margin bridge; the cable-theme counterexample had weak margin bridge and high MAE.","confidence":"low_medium","production_default_scoring_changed":false}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"counterexample_count":1,"current_profile_error_count":2,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"index_update_needed":true}
```

### narrative-only rows

```jsonl
{"row_type":"narrative_only","reason":"Source URLs for earnings/report evidence are represented as historical public evidence proxy in this standalone run; Stock-Web OHLC validation is exact from committed atlas rows.","production_scoring_changed":false,"handoff_prompt_executed_now":false}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

When batch-ingesting this MD later:
1. Parse machine-readable rows for C01_ORDER_BACKLOG_MARGIN_BRIDGE.
2. Keep all rows shadow-only until exact public URLs for evidence proxies are attached.
3. Do not use company name as scoring input.
4. Candidate patch should be scoped to canonical_archetype:C01_ORDER_BACKLOG_MARGIN_BRIDGE.
5. Suggested safe axis is stage2_required_bridge, not Green relaxation.
6. Require non-price evidence of order/backlog plus margin or revision bridge before Stage2-Actionable.
7. Keep 4B watch active when peak_return_from_entry exceeds 80% quickly.
8. Do not apply if subsequent No-Repeat Index shows hard duplicate keys.
```

## 11. Final state

```text
completed_round = R1
completed_loop = standalone_no_repeat
next_round = scheduler_override_not_applicable
next_loop = scheduler_override_not_applicable
round_schedule_status = overridden_by_user
round_sector_consistency = pass
hard_duplicate_avoided = true
index_update_needed = true
```

