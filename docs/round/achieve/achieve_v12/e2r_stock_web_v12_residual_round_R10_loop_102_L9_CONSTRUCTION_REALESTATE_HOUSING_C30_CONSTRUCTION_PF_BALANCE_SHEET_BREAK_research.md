# E2R Historical Calibration v12 — C30 Construction PF Balance-Sheet Break Residual Research

```text
completed_round = R10
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT

price_source = Songdaiki/stock-web
price_basis = tradable_raw
upstream_source = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still places **C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK** inside Priority 0. The static index shows only 3 representative C30 rows, while the conversation-local ledger has just begun to add C30 rows through the prior R10 loop. C30 remains well below the 30-row floor, so this loop continues the same canonical archetype with a different failure-mode family.

The previous C30 loop concentrated on PF/workout and housing-builder bargain rebound. This loop shifts the lens to a nearby but dangerous contaminant: **general construction / EPC / low-PBR contractor rebound**. The question is whether the profile can separate true PF balance-sheet repair from a price-only contractor or EPC headline that looks similar on the chart but does not carry the same cash bridge.

```text
loop_objective = coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining
```

The mechanism is simple. A contractor can show a rebound in the same way a cracked dam can reflect sunlight: the surface glitters before the concrete is inspected. C30 should ask for the inspection report: PF guarantee reduction, refinancing success, unsold inventory relief, unbilled receivables stabilization, net debt repair, or margin/FCF refresh. Without that bridge, a low-PBR bounce should remain Stage2 watch or local 4B.

## 2. Stock-Web manifest and validation scope

Stock-Web manifest fields used for this pass:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Validation assumptions:

```text
must_use_actual_stock_web_1D_OHLC = true
price_basis = tradable_raw
raw_unadjusted_marcap = true
corporate_action_contaminated_180D_window => calibration_usable=false
forward window judged by stock_web_manifest_max_date, not current date
```

This pass uses actual Stock-Web-derived OHLC path numbers already verified in the local v12 research ledger for the same raw shard paths. Some individual raw URL fetches were intermittently cache-missing in this execution environment, so `price_row_fetch_status` is marked as `local_prior_stock_web_rows_reused_for_same_shard_path`. The rows remain tied to the explicit Stock-Web shard paths below and should be batch re-verified by the ingest agent before production promotion.

## 3. Novelty / no-repeat check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This loop avoids the prior C30 exact keys:

```text
C30|294870|Stage2_Actionable|2024-01-25/2024-01-26
C30|047040|Stage2|2024-01-25/2024-04-03
C30|004960|Stage2|2024-02-01
C30|013580|Stage2_Actionable|2024-02-01
C30|009410|4C/narrative|2024-01-02
C30|006360|Stage2-Actionable|2024-04-03
```

New rows in this loop:

```text
C30|000720|Stage2_Actionable|2024-01-26
C30|028050|Stage2_Actionable|2024-02-28
C30|375500|Stage2_Actionable|2024-04-29
C30|006360|Stage2_Actionable|2024-04-30
```

`006360` is a same-symbol reuse, but not an exact duplicate: previous C30 used the 2024-04-03 early repair-watch trigger; this loop uses the later 2024-04-30 cost/provision recovery trigger family. It is counted as a new trigger family but not a new symbol.

## 4. Case table

| case_id | symbol | name | role | trigger | entry | entry price | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|
| C30_R10L102_000720_20240126 | 000720 | 현대건설 | large builder mixed | Stage2_Actionable | 2024-01-26 | 33,100 | +7.25 / -3.47 | +8.76 / -3.47 | +8.76 / -16.01 | mixed positive, not Green |
| C30_R10L102_028050_20240228 | 028050 | 삼성E&A | EPC/plant contaminant | Stage2_Actionable | 2024-02-28 | 26,000 | +8.27 / -7.88 | +8.27 / -16.92 | +8.27 / -36.42 | counterexample / reroute |
| C30_R10L102_375500_20240429 | 375500 | DL이앤씨 | contractor low-PBR false positive | Stage2_Actionable | 2024-04-29 | 36,650 | +7.78 / -9.82 | +7.78 / -21.28 | +7.78 / -21.28 | counterexample high-MAE |
| C30_R10L102_006360_20240430 | 006360 | GS건설 | delayed repair positive with high MAE | Stage2_Actionable | 2024-04-30 | 16,480 | +1.46 / -12.32 | +31.98 / -12.32 | +31.98 / -12.32 | positive, but delayed and volatile |

## 5. Interpretation by case

### 5.1 현대건설 / 000720 — mixed positive, not enough for C30 Green

The 30D and 90D path was acceptable, but not explosive. The 180D path later faded into a -16.01% MAE despite the early rebound. This is the typical large-builder gray zone: the stock can bounce from orderbook, policy, and value sentiment, yet the durable C30 question is whether cash conversion and balance-sheet repair actually follow.

Result: **Stage2_Actionable or Yellow watch is allowed; Stage3-Green should require PF/working-capital/margin bridge.**

### 5.2 삼성E&A / 028050 — EPC label contaminant

The symbol is not a pure housing/PF name. That is precisely why it is useful for C30 compression. A plant/EPC order or construction-sector label can masquerade as a C30 balance-sheet repair signal. Price produced only +8.27% MFE but -36.42% 180D MAE. This belongs closer to C05 EPC margin-gap unless a housing/PF balance-sheet bridge is explicitly present.

Result: **C30 should reroute EPC/plant order labels away from PF balance-sheet scoring unless PF/housing exposure is the actual thesis.**

### 5.3 DL이앤씨 / 375500 — low-PBR rebound failed without bridge

This is the clean C30 counterexample. A low-PBR contractor rebound produced a small local MFE, but the 90D and 180D MAE fell to -21.28%. Cheapness was not a bridge; it was a signpost standing next to the hole.

Result: **price-only low-PBR / contractor rebound should be capped as Stage2 watch or local 4B unless balance-sheet repair is visible.**

### 5.4 GS건설 / 006360 — delayed repair positive, but high-MAE entry risk

GS건설 is the useful opposite of DL이앤씨. The 90D/180D MFE reached +31.98%, but the path first absorbed -12.32% MAE. That means the profile should not kill the idea, but should delay promotion until repair/cost-provision/margin visibility appears. Early Stage3 would be reckless; delayed Yellow can be correct.

Result: **positive but volatile; require repair bridge before Green.**

## 6. Machine-readable case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L102_000720_20240126","symbol":"000720","company_name":"현대건설","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","case_type":"large_builder_mixed_positive","positive_or_counterexample":"mixed_positive","best_trigger":"Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"large builder early rebound faded by 180D without durable PF/working-capital/margin bridge"}
{"row_type":"case","case_id":"C30_R10L102_028050_20240228","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","case_type":"epc_contaminant_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_risk_confirmed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"EPC/plant order label should route to C05 unless housing/PF balance-sheet exposure is thesis"}
{"row_type":"case","case_id":"C30_R10L102_375500_20240429","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","case_type":"contractor_low_pbr_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_risk_confirmed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"low-PBR contractor rebound failed without PF/working-capital/margin bridge"}
{"row_type":"case","case_id":"C30_R10L102_006360_20240430","symbol":"006360","company_name":"GS건설","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","case_type":"delayed_repair_positive_high_mae","positive_or_counterexample":"positive","best_trigger":"Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_entry_date_and_new_trigger_family_after_prior_2024_04_03_C30_watch","independent_evidence_weight":0.85,"score_price_alignment":"positive_but_high_mae","current_profile_verdict":"current_profile_too_late_or_too_early_depending_on_bridge","price_source":"Songdaiki/stock-web","notes":"later cost/provision repair trigger produced positive MFE but only after high MAE, requiring delayed confirmation"}
```

## 7. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L102_000720_20240126_Stage2_Actionable","case_id":"C30_R10L102_000720_20240126","symbol":"000720","company_name":"현대건설","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"PF balance-sheet break vs low-PBR contractor rebound","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2_Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"source_proxy_only: construction value-up/orderbook/PF relief sentiment, but balance-sheet bridge not yet confirmed","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","sector_policy_context"],"stage3_evidence_fields":["margin_bridge_required","financial_visibility_required","PF_or_working_capital_bridge_required"],"stage4b_evidence_fields":["local_price_rebound"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","entry_date":"2024-01-26","entry_price":33100.0,"entry_price_basis":"close","MFE_30D_pct":7.25,"MAE_30D_pct":-3.47,"MFE_90D_pct":8.76,"MAE_90D_pct":-3.47,"MFE_180D_pct":8.76,"MAE_180D_pct":-16.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-02-26","peak_90D_date":"2024-05-09","peak_180D_date":"2024-05-09","trough_180D_date":"2024-10-25","four_b_local_peak_proximity":true,"four_b_full_window_proximity":false,"four_b_timing_verdict":"local_4b_watch_only","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"mixed_positive_not_green","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_known_2024_180D_overlap_in_prior_local_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2_Actionable|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L102_028050_20240228_Stage2_Actionable","case_id":"C30_R10L102_028050_20240228","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","sector":"construction / EPC / real estate contaminant split","primary_archetype":"EPC label contaminant inside C30","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression","trigger_type":"Stage2_Actionable","trigger_date":"2024-02-28","evidence_available_at_that_date":"source_proxy_only: EPC/order/plant label and construction-sector price rebound; no pure PF/housing balance-sheet repair bridge","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","order_or_project_label"],"stage3_evidence_fields":["margin_bridge_missing","PF_balance_sheet_bridge_missing"],"stage4b_evidence_fields":["local_price_extension"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","entry_date":"2024-02-28","entry_price":26000.0,"entry_price_basis":"close","MFE_30D_pct":8.27,"MAE_30D_pct":-7.88,"MFE_90D_pct":8.27,"MAE_90D_pct":-16.92,"MFE_180D_pct":8.27,"MAE_180D_pct":-36.42,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-03-15","peak_90D_date":"2024-03-15","peak_180D_date":"2024-03-15","trough_180D_date":"2024-11-14","four_b_local_peak_proximity":true,"four_b_full_window_proximity":false,"four_b_timing_verdict":"local_price_spike_failed_full_window","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_epc_contaminant","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_known_2024_180D_overlap_in_prior_local_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|028050|Stage2_Actionable|2024-02-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L102_375500_20240429_Stage2_Actionable","case_id":"C30_R10L102_375500_20240429","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"low-PBR contractor rebound without PF cash bridge","loop_objective":"coverage_gap_fill | counterexample_mining | residual_false_positive_mining","trigger_type":"Stage2_Actionable","trigger_date":"2024-04-29","evidence_available_at_that_date":"source_proxy_only: low-PBR contractor rebound and sector repair sentiment; no confirmed PF/working-capital bridge","evidence_source":"source_proxy_only","stage2_evidence_fields":["valuation_rebound","relative_strength","sector_policy_context"],"stage3_evidence_fields":["PF_bridge_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["local_price_rebound"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","entry_date":"2024-04-29","entry_price":36650.0,"entry_price_basis":"close","MFE_30D_pct":7.78,"MAE_30D_pct":-9.82,"MFE_90D_pct":7.78,"MAE_90D_pct":-21.28,"MFE_180D_pct":7.78,"MAE_180D_pct":-21.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-06-13","peak_90D_date":"2024-06-13","peak_180D_date":"2024-06-13","trough_180D_date":"2024-08-08","four_b_local_peak_proximity":true,"four_b_full_window_proximity":false,"four_b_timing_verdict":"failed_local_rebound","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_low_pbr_contractor","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_known_2024_180D_overlap_in_prior_local_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|Stage2_Actionable|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L102_006360_20240430_Stage2_Actionable","case_id":"C30_R10L102_006360_20240430","symbol":"006360","company_name":"GS건설","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_BALANCE_SHEET_BREAK_SECOND_PASS_EPC_CONTRACTOR_LOW_PBR_CONTAMINANT_SPLIT","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"delayed repair positive with high-MAE guard","loop_objective":"coverage_gap_fill | holdout_validation | 4B_non_price_requirement_stress_test","trigger_type":"Stage2_Actionable","trigger_date":"2024-04-30","evidence_available_at_that_date":"source_proxy_only: post-provision/cost-repair recovery and construction repair sentiment; same symbol as prior C30 but later trigger family","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","repair_or_cost_visibility"],"stage3_evidence_fields":["margin_bridge_required","PF_or_working_capital_bridge_required"],"stage4b_evidence_fields":["delayed_price_confirmation"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","entry_date":"2024-04-30","entry_price":16480.0,"entry_price_basis":"close","MFE_30D_pct":1.46,"MAE_30D_pct":-12.32,"MFE_90D_pct":31.98,"MAE_90D_pct":-12.32,"MFE_180D_pct":31.98,"MAE_180D_pct":-12.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-04-30","peak_90D_date":"2024-08-27","peak_180D_date":"2024-08-27","trough_180D_date":"2024-06-19","four_b_local_peak_proximity":false,"four_b_full_window_proximity":false,"four_b_timing_verdict":"delayed_positive_after_high_mae","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_mae_delayed","current_profile_verdict":"current_profile_too_late_or_too_early_depending_on_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_known_2024_180D_overlap_in_prior_local_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|006360|Stage2_Actionable|2024-04-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_entry_date_and_new_trigger_family_after_prior_2024_04_03_C30_watch","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
```

## 8. Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C30_R10L102_000720_20240126","symbol":"000720","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"Stage2_Actionable","entry_date":"2024-01-26","current_calibrated_proxy_stage":"Stage3_Yellow_if_naive_large_builder_value_rebound","desired_shadow_stage":"Stage2_Actionable_or_Yellow_watch_not_Green","raw_component_score_breakdown":{"stage2_actionable_evidence_bonus":2.0,"relative_strength_score":12,"sector_policy_score":10,"PF_balance_sheet_bridge":4,"margin_FCF_bridge":5,"working_capital_visibility":3,"local_4b_watch_guard":true,"high_MAE_guardrail":true},"shadow_delta":-5,"current_profile_error":true,"score_return_alignment_label":"improves_by_preventing_green_on_mixed_180D_fade"}
{"row_type":"score_simulation","case_id":"C30_R10L102_028050_20240228","symbol":"028050","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"Stage2_Actionable","entry_date":"2024-02-28","current_calibrated_proxy_stage":"Stage2_Actionable_if_construction_EPC_label_is_overcounted","desired_shadow_stage":"reroute_to_C05_or_Stage2_watch","raw_component_score_breakdown":{"stage2_actionable_evidence_bonus":2.0,"relative_strength_score":13,"sector_policy_score":8,"PF_balance_sheet_bridge":0,"margin_FCF_bridge":4,"working_capital_visibility":2,"C30_pure_exposure_penalty":-12,"high_MAE_guardrail":true},"shadow_delta":-12,"current_profile_error":true,"score_return_alignment_label":"removes_EPC_contaminant_from_C30"}
{"row_type":"score_simulation","case_id":"C30_R10L102_375500_20240429","symbol":"375500","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"Stage2_Actionable","entry_date":"2024-04-29","current_calibrated_proxy_stage":"Stage2_Actionable_from_low_PBR_contractor_rebound","desired_shadow_stage":"Stage2_watch_or_local_4B_only","raw_component_score_breakdown":{"stage2_actionable_evidence_bonus":2.0,"relative_strength_score":12,"sector_policy_score":9,"PF_balance_sheet_bridge":2,"margin_FCF_bridge":3,"working_capital_visibility":2,"low_PBR_price_only_penalty":-10,"high_MAE_guardrail":true},"shadow_delta":-10,"current_profile_error":true,"score_return_alignment_label":"blocks_low_PBR_false_positive"}
{"row_type":"score_simulation","case_id":"C30_R10L102_006360_20240430","symbol":"006360","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"Stage2_Actionable","entry_date":"2024-04-30","current_calibrated_proxy_stage":"Stage2_Actionable_to_delayed_Yellow_candidate","desired_shadow_stage":"Stage3_Yellow_allowed_after_repair_bridge_but_high_MAE_guard_kept","raw_component_score_breakdown":{"stage2_actionable_evidence_bonus":2.0,"relative_strength_score":12,"sector_policy_score":9,"PF_balance_sheet_bridge":7,"margin_FCF_bridge":8,"working_capital_visibility":5,"high_MAE_guardrail":true,"delayed_positive_bridge":true},"shadow_delta":2,"current_profile_error":true,"score_return_alignment_label":"preserves_delayed_positive_but_blocks_too_early_green"}
```

## 9. Aggregate rows

```jsonl
{"row_type":"aggregate_metrics","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_reused_symbol_new_trigger_family_count":1,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"median_mfe_30d_pct":7.52,"median_mae_30d_pct":-8.85,"median_mfe_90d_pct":8.02,"median_mae_90d_pct":-14.62,"median_mfe_180d_pct":8.52,"median_mae_180d_pct":-18.65,"dominant_residual_error":"C30_overcredits_construction_low_PBR_or_EPC_label_without_balance_sheet_cash_bridge","coverage_gap_after_acceptance_static":"C30 rows 3 -> 7 if accepted","coverage_gap_after_acceptance_conversation_local":"C30 approx rows 11 -> 15 if accepted"}
{"row_type":"residual_contribution","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_contribution_label":"canonical_archetype_rule_candidate","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"do_not_propose_new_weight_delta":false,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["current_profile_false_positive","current_profile_too_late","C30_C05_contaminant_reroute","low_PBR_price_only_local_4B_cap"]}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","scope":"canonical_archetype_specific","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C30_PF_WORKING_CAPITAL_CASH_BRIDGE_REQUIRED","C30_LOW_PBR_CONTRACTOR_PRICE_ONLY_LOCAL_4B_CAP","C30_EPC_PLANT_LABEL_REROUTE_TO_C05_UNLESS_PF_EXPOSURE_PRESENT","C30_DELAYED_REPAIR_POSITIVE_ALLOWED_WITH_HIGH_MAE_GUARD","C30_UNSOLD_INVENTORY_UNBILLED_RECEIVABLES_NET_DEBT_CHECK"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"candidate_rule_text":"For C30, do not promote a construction or contractor rebound to Stage3 unless the thesis includes a company-level balance-sheet bridge: PF guarantee reduction, refinancing success, net debt/working-capital repair, unsold inventory relief, unbilled receivables stabilization, or margin/FCF refresh. Low-PBR or EPC/plant labels without PF exposure are capped as Stage2 watch/local 4B or rerouted to C05. Delayed positives like GS E&C can be preserved, but only after repair evidence and with high-MAE guard."}
```

## 11. Residual contribution summary

C30 should not be a broad “construction beta” bucket. It is a **balance-sheet break / repair** bucket. If the evidence is merely order headline, plant/EPC label, low PBR, or policy relief, the profile is looking at scaffolding and calling it a building. The shadow rule must ask whether cash, debt, PF guarantees, inventory, and unbilled receivables can actually carry the structure.

Main residual findings:

1. **000720**: large-builder rebound can be real locally but fades by 180D without stronger bridge.
2. **028050**: EPC/plant label contaminates C30; reroute to C05 unless housing/PF exposure is explicit.
3. **375500**: low-PBR contractor rebound is a false positive when PF/working-capital bridge is absent.
4. **006360**: repair positives can arrive late, but they need high-MAE-aware timing rather than instant Green.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When multiple C30 MD files are batch-ingested, test the following canonical-archetype-specific rules:

Target canonical_archetype_id:
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK

Candidate axes:
1. C30_PF_WORKING_CAPITAL_CASH_BRIDGE_REQUIRED
2. C30_LOW_PBR_CONTRACTOR_PRICE_ONLY_LOCAL_4B_CAP
3. C30_EPC_PLANT_LABEL_REROUTE_TO_C05_UNLESS_PF_EXPOSURE_PRESENT
4. C30_DELAYED_REPAIR_POSITIVE_ALLOWED_WITH_HIGH_MAE_GUARD
5. C30_UNSOLD_INVENTORY_UNBILLED_RECEIVABLES_NET_DEBT_CHECK

Expected scoring behavior:
- If evidence is only low-PBR, construction beta, or broad policy relief, cap as Stage2 watch/local 4B.
- If evidence is EPC/plant order without housing/PF exposure, reroute to C05 and do not score as C30.
- If PF/working-capital/cash repair evidence exists and price path confirms, allow Stage3-Yellow.
- Stage3-Green still requires margin/FCF/revision confirmation plus no hard 4C balance-sheet break.
- High MAE within 30D/90D should reduce early promotion even if later 180D MFE is positive.
```

## 13. Next research state

```text
completed_round = R10
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_reused_symbol_new_trigger_family_count = 1
same_archetype_new_trigger_family_count = 4
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4

auto_selected_coverage_gap_static_index = C30 rows 3 -> 7 if accepted; still Priority 0, need 23 to 30
auto_selected_coverage_gap_conversation_local = C30 approx rows 11 -> 15 if accepted; still Priority 0, need about 15 to reach 30

next_recommended_archetypes =
- C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_third_pass_to_30
- C31_POLICY_SUBSIDY_LEGISLATION_EVENT_second_pass_to_30
- C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30
- C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
