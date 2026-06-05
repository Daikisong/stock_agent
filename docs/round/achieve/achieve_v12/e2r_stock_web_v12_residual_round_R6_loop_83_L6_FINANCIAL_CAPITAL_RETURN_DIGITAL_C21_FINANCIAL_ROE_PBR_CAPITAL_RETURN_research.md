# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 83
scheduled_round: R6
scheduled_loop: 83
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_BETA_PRICE_SPIKE
sector: financial / capital return / digital brokerage beta
output_file: e2r_stock_web_v12_residual_round_R6_loop_83_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Existing global axes are not re-proposed. They are stress-tested locally inside C21:

```text
stage2_actionable_evidence_bonus: existing_axis_tested
stage3_yellow_total_min: existing_axis_kept
stage3_green_total_min: existing_axis_kept
stage3_green_revision_min: existing_axis_kept
price_only_blowoff_blocks_positive_stage: existing_axis_strengthened_within_C21
full_4b_requires_non_price_evidence: existing_axis_strengthened_within_C21
hard_4c_thesis_break_routes_to_4c: existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 83
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_BETA_PRICE_SPIKE
round_sector_consistency = pass
```

R6 must stay inside L6. C21 is selected over C22 because the residual question here is not insurance reserve/rate-cycle accounting; it is whether the value-up/PBR rerating signal in financials distinguishes durable ROE + capital return bridge from brokerage beta price spikes.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index is used only as a duplicate-avoidance ledger. C21 already has a large corpus, and the heavily repeated C21 combinations include 006220, 016360, 071050, 105560, 138040, and 139130. This loop therefore avoids those top-covered symbol clusters and introduces three different symbol/trigger-family combinations.

Hard duplicate key rule:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty keys:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"055550","trigger_type":"Stage2-Actionable-Bank-ValueUp-CapitalReturn-Bridge","entry_date":"2024-02-02","duplicate_status":"new_symbol_or_non_top_covered_combination; treated as independent positive bridge case"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","trigger_type":"Stage2-FalsePositive-Brokerage-Beta-PriceSpike-NoROEBridge","entry_date":"2024-02-02","duplicate_status":"new failure mode inside C21; brokerage beta without capital-return bridge"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"039490","trigger_type":"Stage2-FalsePositive-RetailBrokerage-ROEVolatility-LateEntry","entry_date":"2024-03-14","duplicate_status":"new trigger family; late retail-brokerage/market-beta price spike case"}
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"price_source_validation","symbol":"055550","company_name":"신한지주","profile_path":"atlas/symbol_profiles/055/055550.json","first_date":"2001-09-10","last_date":"2026-02-20","trading_day_count":6031,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"006800","company_name":"미래에셋증권","profile_path":"atlas/symbol_profiles/006/006800.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7765,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1999-09-27","1999-10-14","2000-05-22","2001-11-23","2011-11-16","2017-01-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates do not overlap the selected 2024 180D forward window.","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_for_selected_2024_window"}
{"row_type":"price_source_validation","symbol":"039490","company_name":"키움증권","profile_path":"atlas/symbol_profiles/039/039490.json","first_date":"2004-04-23","last_date":"2026-02-20","trading_day_count":5390,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2008-12-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate does not overlap the selected 2024 180D forward window.","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_for_selected_2024_window"}
```

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

```text
entry_date exists in Stock-Web tradable shard = true
entry_price uses c column = true
forward 180 trading-day window available by stock_web_manifest_max_date = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  ├─ BANK_VALUEUP_CAPITAL_RETURN_BRIDGE
  │   └─ 055550 / 신한지주 / capital-return bridge positive control
  ├─ BROKERAGE_BETA_PRICE_SPIKE_NO_ROE_BRIDGE
  │   └─ 006800 / 미래에셋증권 / PBR/value-up beta without durable ROE bridge
  └─ RETAIL_BROKERAGE_ROE_VOLATILITY_LATE_ENTRY
      └─ 039490 / 키움증권 / late entry after brokerage momentum spike
```

## 7. Case Selection Summary

```jsonl
{"row_type":"case","case_id":"R6L83_C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_BRIDGE","symbol":"055550","company_name":"신한지주","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-Bank-ValueUp-CapitalReturn-Bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_with_shallow_enough_MAE_and_180D_followthrough","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Bank value-up/capital-return bridge produced a higher-quality C21 path than brokerage beta spikes."}
{"row_type":"case","case_id":"R6L83_C21_006800_MIRAE_BROKERAGE_BETA_NO_ROE_BRIDGE","symbol":"006800","company_name":"미래에셋증권","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_BETA_PRICE_SPIKE_NO_ROE_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-Brokerage-Beta-PriceSpike-NoROEBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"low_MFE_with_near_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Early value-up/brokerage beta spike did not convert into durable ROE/capital-return repricing."}
{"row_type":"case","case_id":"R6L83_C21_039490_KIWOOM_LATE_RETAIL_BROKERAGE_PRICE_SPIKE","symbol":"039490","company_name":"키움증권","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"RETAIL_BROKERAGE_ROE_VOLATILITY_LATE_ENTRY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RetailBrokerage-ROEVolatility-LateEntry","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late_entry_low_incremental_upside","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"After the brokerage momentum leg, later Stage2-style entry had weak incremental upside and meaningful drawdown."}
```

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
representative_trigger_count = 3
```

Interpretation: C21 should not reward all financial value-up beta equally. Bank capital return with stable ROE/PBR repricing can qualify for Stage2-Actionable/Yellow watch, while brokerage beta needs a stricter bridge: shareholder return execution, ROE durability, and no high-MAE/low-MFE path.

## 9. Evidence Source Map

Non-price evidence is intentionally stored as source-name/proxy-level research evidence in this MD. Exact evidence URLs remain pending, so this loop is usable for price-path residual calibration, not for production promotion.

```text
evidence_url_pending = true
source_proxy_only = true
promotion_policy = hold_for_exact_url_repair_before_any_runtime_patch
```

## 10. Price Data Source Map

```text
055550 price_shard_path = atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv
006800 price_shard_path = atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv
039490 price_shard_path = atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv
profile_path pattern = atlas/symbol_profiles/<prefix>/<ticker>.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 11. Case-by-Case Trigger Grid

| case_id | symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R6L83_C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_BRIDGE | 055550 | 2024-02-02 | 45300 | 13.69 | -12.03 | 13.69 | -12.03 | 32.23 | -12.03 | current_profile_correct |
| R6L83_C21_006800_MIRAE_BROKERAGE_BETA_NO_ROE_BRIDGE | 006800 | 2024-02-02 | 8620 | 6.73 | -10.09 | 6.73 | -19.61 | 7.08 | -19.61 | current_profile_false_positive |
| R6L83_C21_039490_KIWOOM_LATE_RETAIL_BROKERAGE_PRICE_SPIKE | 039490 | 2024-03-14 | 134700 | 1.41 | -12.69 | 8.69 | -12.69 | 8.69 | -17.97 | current_profile_too_early |

## 12. Trigger-Level OHLC Backtest Tables

```jsonl
{"row_type":"trigger","trigger_id":"R6L83_C21_055550_20240202_STAGE2_BANK_VALUEUP_CAPITAL_RETURN","case_id":"R6L83_C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_BRIDGE","symbol":"055550","company_name":"신한지주","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_BRIDGE","sector":"financial_capital_return","primary_archetype":"ROE_PBR_capital_return","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable-Bank-ValueUp-CapitalReturn-Bridge","trigger_date":"2024-02-02","evidence_available_at_that_date":"source-name-level proxy for Korean value-up, bank PBR repricing and capital-return expectation; exact URL pending","evidence_source":"historical_public_report_consensus_proxy; exact URL pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","capital_return_optionality"],"stage3_evidence_fields":["confirmed_revision_proxy","financial_visibility_proxy","low_red_team_risk_proxy"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":45300.0,"MFE_30D_pct":13.69,"MFE_90D_pct":13.69,"MFE_180D_pct":32.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.03,"MAE_90D_pct":-12.03,"MAE_180D_pct":-12.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":59900.0,"drawdown_after_peak_pct":-9.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L83_C21_055550_20240202_45300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive"}
{"row_type":"trigger","trigger_id":"R6L83_C21_006800_20240202_STAGE2_BROKERAGE_BETA_NO_ROE_BRIDGE","case_id":"R6L83_C21_006800_MIRAE_BROKERAGE_BETA_NO_ROE_BRIDGE","symbol":"006800","company_name":"미래에셋증권","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_BETA_PRICE_SPIKE_NO_ROE_BRIDGE","sector":"financial_capital_return","primary_archetype":"brokerage_beta_without_ROE_bridge","loop_objective":"residual_false_positive_mining;counterexample_mining","trigger_type":"Stage2-FalsePositive-Brokerage-Beta-PriceSpike-NoROEBridge","trigger_date":"2024-02-02","evidence_available_at_that_date":"source-name-level proxy for brokerage/value-up beta; exact URL pending; no verified ROE/capital-return execution bridge","evidence_source":"historical_public_report_consensus_proxy; exact URL pending","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv","profile_path":"atlas/symbol_profiles/006/006800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":8620.0,"MFE_30D_pct":6.73,"MFE_90D_pct":6.73,"MFE_180D_pct":7.08,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.09,"MAE_90D_pct":-19.61,"MAE_180D_pct":-19.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-30","peak_price":9230.0,"drawdown_after_peak_pct":-3.90,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_near_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L83_C21_006800_20240202_8620","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample"}
{"row_type":"trigger","trigger_id":"R6L83_C21_039490_20240314_STAGE2_RETAIL_BROKERAGE_LATE_ENTRY","case_id":"R6L83_C21_039490_KIWOOM_LATE_RETAIL_BROKERAGE_PRICE_SPIKE","symbol":"039490","company_name":"키움증권","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"RETAIL_BROKERAGE_ROE_VOLATILITY_LATE_ENTRY","sector":"financial_capital_return","primary_archetype":"retail_brokerage_ROE_volatility_late_entry","loop_objective":"residual_false_positive_mining;late_entry_guardrail","trigger_type":"Stage2-FalsePositive-RetailBrokerage-ROEVolatility-LateEntry","trigger_date":"2024-03-14","evidence_available_at_that_date":"source-name-level proxy for retail brokerage/value-up momentum; exact URL pending; post-spike late entry without durable capital return bridge","evidence_source":"historical_public_report_consensus_proxy; exact URL pending","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv","profile_path":"atlas/symbol_profiles/039/039490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-14","entry_price":134700.0,"MFE_30D_pct":1.41,"MFE_90D_pct":8.69,"MFE_180D_pct":8.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.69,"MAE_90D_pct":-12.69,"MAE_180D_pct":-17.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":146400.0,"drawdown_after_peak_pct":-24.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_late_entry_low_incremental_upside","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L83_C21_039490_20240314_134700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample"}
```

## 13. Current Calibrated Profile Stress Test

```text
1. current calibrated profile likely allows 055550 as Stage2-Actionable/Yellow watch when non-price capital-return bridge exists. This aligns with 180D follow-through.
2. For 006800, the profile can over-credit value-up/brokerage beta if ROE/capital-return bridge is weak. The price path shows low MFE and near high-MAE.
3. For 039490, the entry is too late after brokerage momentum. Incremental upside is limited and drawdown after peak is large.
4. Stage2 bonus is useful for banks with capital return bridge, but too loose for brokerage beta without ROE durability.
5. Yellow/Green thresholds should not be loosened in C21.
6. price-only blowoff guard is appropriate and should be strengthened locally for brokerage beta.
7. full 4B non-price requirement remains correct: 006800/039490 are local 4B watch rows, not full 4B.
8. Hard 4C routing is not triggered; these are watch/guardrail counterexamples rather than thesis-break hard 4C.
```

## 14. Stage2 / Yellow / Green Comparison

```text
055550: Stage2-Actionable acceptable; Yellow watch acceptable if exact capital-return evidence URL is later repaired. Green not supported inside this MD because evidence is proxy-only.
006800: Stage2-Watch only; block Yellow/Green unless ROE + shareholder-return bridge is verified.
039490: Stage2-Watch only; late momentum entry should not become Yellow/Green without durable earnings/capital-return confirmation.
```

## 15. 4B Local vs Full-window Timing Audit

```text
006800: local 4B watch. Price-only peak/recovery did not provide enough non-price 4B evidence. Do not count as full 4B.
039490: local 4B watch. Late brokerage momentum then drawdown supports watch guard, not full 4B.
055550: no 4B row. Positive bridge remains Stage2/Yellow watch, not overheat.
```

## 16. 4C Protection Audit

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_case_count = 0
```

No hard 4C route is proposed. The relevant C21 residual is false-positive Stage2/Yellow risk, not confirmed thesis break.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = evidence is inside one canonical archetype, not broad enough across L6/C21+C22.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate_rule = require ROE/PBR + explicit capital-return bridge for C21 Stage2-Actionable/Yellow; treat brokerage beta price spike as Watch unless ROE durability and shareholder-return execution are verified.
```

## 19. Before / After Backtest Comparison

```jsonl
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"Global calibrated rules can catch price-only blowoff, but may still over-credit C21 brokerage beta as capital-return rerating.","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":9.70,"avg_MAE_90D_pct":-14.78,"avg_MFE_180D_pct":16.00,"avg_MAE_180D_pct":-16.54,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.63,"avg_four_b_full_window_peak_proximity":0.63,"score_return_alignment_verdict":"mixed; one good bank bridge and two brokerage-beta false positives"}
{"row_type":"profile_comparison","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L6-wide tightening is premature because insurance and banks differ; no L6 global patch from this loop.","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":9.70,"avg_MAE_90D_pct":-14.78,"avg_MFE_180D_pct":16.00,"avg_MAE_180D_pct":-16.54,"false_positive_rate":0.67,"score_return_alignment_verdict":"hold as canonical-only"}
{"row_type":"profile_comparison","profile_id":"P2_C21_capital_return_bridge_required","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 Stage2-Actionable/Yellow requires verified capital-return bridge and ROE durability; brokerage beta remains Watch.","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":13.69,"avg_MAE_90D_pct":-12.03,"avg_MFE_180D_pct":32.23,"avg_MAE_180D_pct":-12.03,"false_positive_rate":0.0,"score_return_alignment_verdict":"better alignment for accepted rows; two false positives blocked"}
{"row_type":"profile_comparison","profile_id":"P3_C21_brokerage_beta_guard","profile_scope":"counterexample_guard_profile","profile_hypothesis":"If C21 case is brokerage/market-beta led and MFE90 < 10 with MAE90 <= -12, block Yellow/Green until evidence-quality repair.","eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":7.71,"avg_MAE_90D_pct":-16.15,"avg_MFE_180D_pct":7.89,"avg_MAE_180D_pct":-18.79,"false_positive_rate":1.0,"score_return_alignment_verdict":"guardrail justified as shadow only"}
```

## 20. Score-Return Alignment Matrix

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L83_C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_BRIDGE","trigger_id":"R6L83_C21_055550_20240202_STAGE2_BANK_VALUEUP_CAPITAL_RETURN","symbol":"055550","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":12,"relative_strength_score":13,"customer_quality_score":8,"policy_or_regulatory_score":8,"valuation_repricing_score":14,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":18},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":12,"relative_strength_score":13,"customer_quality_score":8,"policy_or_regulatory_score":8,"valuation_repricing_score":14,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":20},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable/Yellow-Watch","changed_components":["roe_pbr_capital_return_score"],"component_delta_explanation":"Capital-return bridge is preserved, but Green remains blocked by source_proxy_only/evidence_url_pending.","MFE_90D_pct":13.69,"MAE_90D_pct":-12.03,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L83_C21_006800_MIRAE_BROKERAGE_BETA_NO_ROE_BRIDGE","trigger_id":"R6L83_C21_006800_20240202_STAGE2_BROKERAGE_BETA_NO_ROE_BRIDGE","symbol":"006800","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":6,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":7},"weighted_score_before":66,"stage_label_before":"Stage2-Watch/FalsePositiveRisk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":3},"weighted_score_after":53,"stage_label_after":"Stage1/Stage2-Watch-Blocked","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","roe_pbr_capital_return_score"],"component_delta_explanation":"Brokerage beta without ROE/capital-return bridge should not receive C21 Stage2-Actionable credit.","MFE_90D_pct":6.73,"MAE_90D_pct":-19.61,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L83_C21_039490_KIWOOM_LATE_RETAIL_BROKERAGE_PRICE_SPIKE","trigger_id":"R6L83_C21_039490_20240314_STAGE2_RETAIL_BROKERAGE_LATE_ENTRY","symbol":"039490","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":8,"relative_strength_score":14,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":13,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":8},"weighted_score_before":69,"stage_label_before":"Stage2-Watch/YellowRisk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":-13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":4},"weighted_score_after":53,"stage_label_after":"Stage2-Watch-Blocked","changed_components":["relative_strength_score","revision_score","valuation_repricing_score","execution_risk_score","roe_pbr_capital_return_score"],"component_delta_explanation":"Late brokerage entry after price spike needs ROE durability and capital return evidence; otherwise low incremental upside is penalized.","MFE_90D_pct":8.69,"MAE_90D_pct":-12.69,"score_return_alignment_label":"late_entry_false_positive_blocked","current_profile_verdict":"current_profile_too_early"}
```

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_BETA_PRICE_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"Need exact evidence URL repair; test additional non-bank capital-return cases later without repeating top-covered C21 symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; stage2_actionable_evidence_bonus
residual_error_types_found: brokerage_beta_false_positive; late_entry_low_incremental_upside; C21_ROE_capital_return_bridge_missing
new_axis_proposed: C21_capital_return_bridge_required_shadow_only; C21_brokerage_beta_local_4B_watch_guard_shadow_only
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage within C21; full_4b_requires_non_price_evidence within C21
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-Web OHLC row existence
- 30D/90D/180D MFE/MAE
- clean selected 2024 forward windows
- large_sector_id / canonical_archetype_id consistency
- novelty against No-Repeat index summary
```

Non-validation scope:

```text
- exact disclosure/report URL verification
- live candidate recommendation
- production profile patch
- stock_agent source-code change
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_capital_return_bridge_required,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Require explicit ROE/PBR plus capital-return bridge before C21 Stage2-Actionable/Yellow","Blocks brokerage beta false positives while preserving 055550 bank bridge","R6L83_C21_055550_20240202_STAGE2_BANK_VALUEUP_CAPITAL_RETURN|R6L83_C21_006800_20240202_STAGE2_BROKERAGE_BETA_NO_ROE_BRIDGE|R6L83_C21_039490_20240314_STAGE2_RETAIL_BROKERAGE_LATE_ENTRY",3,3,2,medium,canonical_shadow_only,"not production; exact evidence URL repair required"
shadow_weight,C21_brokerage_beta_local_4B_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Brokerage beta price spikes with MFE90<10 and MAE90<=-12 should remain Watch unless capital-return bridge is verified","Turns 006800 and 039490 into watch/guard rows, not positive rerating rows","R6L83_C21_006800_20240202_STAGE2_BROKERAGE_BETA_NO_ROE_BRIDGE|R6L83_C21_039490_20240314_STAGE2_RETAIL_BROKERAGE_LATE_ENTRY",3,3,2,medium,canonical_shadow_only,"not full 4B; local guardrail only"
```

## 25. Machine-Readable Rows

The machine-readable rows are embedded in the sections above and include:

```text
price_source_validation: 4 rows
case: 3 rows
trigger: 3 rows
score_simulation: 3 rows
profile_comparison: 4 rows
coverage_matrix: 1 row
shadow_weight: 2 rows
```

Additional residual row:

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"83","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["brokerage_beta_false_positive","late_entry_low_incremental_upside","capital_return_bridge_missing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.

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
completed_round = R6
completed_loop = 83
next_round = R7
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 28. Source Notes

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
non_price_evidence_status = source_proxy_only; evidence_url_pending
investment_recommendation = none
```
