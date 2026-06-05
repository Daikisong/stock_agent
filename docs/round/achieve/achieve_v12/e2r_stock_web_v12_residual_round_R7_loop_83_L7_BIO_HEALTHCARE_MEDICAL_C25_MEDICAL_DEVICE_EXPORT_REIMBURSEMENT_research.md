# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 83
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DENTAL_CGM_COMMERCIALIZATION_SPIKE
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

Current default proxy remains `e2r_2_1_stock_web_calibrated_proxy`.  
This MD does not change production scoring. It only records a canonical-archetype shadow rule candidate for C25.

Already-applied global axes are treated as tested, not re-proposed globally:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 83
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_sector_consistency = pass
```

R7 is restricted to bio/healthcare/medical-device scopes. This run uses C25 rather than C23/C24 because the residual is specific to medical-device export/reimbursement commercialization: strong repeat sell-through works, while dental/CGM commercialization themes without margin/revision bridge behave like high-MAE false positives.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index is used only as a duplicate-prevention ledger. The hard duplicate key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty status:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"214450","trigger_type":"Stage2-Actionable-AestheticDeviceExport-ReimbursementBridge","entry_date":"2024-04-01","duplicate_status":"new C25 symbol/family in this loop"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","trigger_type":"Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge","entry_date":"2024-04-01","duplicate_status":"new C25 symbol/failure mode in this loop"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"099190","trigger_type":"Stage2-FalsePositive-CGMReimbursementCommercialization-NoBridge","entry_date":"2024-01-10","duplicate_status":"soft reuse/holdout; different trigger family and entry group; independent_evidence_weight=0.5"}
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows excluded from tradable shards; corporate-action-contaminated windows are blocked."}
{"row_type":"price_source_validation","symbol":"214450","company_name":"파마리서치","profile_path":"atlas/symbol_profiles/214/214450.json","first_date":"2015-07-24","last_date":"2026-02-20","trading_day_count":2594,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"corporate_action_window_status":"clean_180D_window","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"228670","company_name":"레이","profile_path":"atlas/symbol_profiles/228/228670.json","first_date":"2019-08-08","last_date":"2026-02-20","trading_day_count":1603,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-06-03","2021-06-23"],"has_major_raw_discontinuity":true,"corporate_action_window_status":"clean_for_2024_window","profile_check":"2024 forward window clean; historical 2021 corporate-action candidates outside selected window"}
{"row_type":"price_source_validation","symbol":"099190","company_name":"아이센스","profile_path":"atlas/symbol_profiles/099/099190.json","first_date":"2013-01-30","last_date":"2026-02-20","trading_day_count":3205,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2015-10-02","2023-03-14","2023-04-10"],"has_major_raw_discontinuity":true,"corporate_action_window_status":"clean_for_2024_window","profile_check":"2024 forward window clean; corporate-action candidates before selected 2024 entry window"}
```

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

```text
entry_date exists in stock-web tradable shard
forward 180 trading-day window is available by manifest max_date 2026-02-20
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window or clean_for_2024_window
```

## 6. Canonical Archetype Compression Map

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  -> AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_BRIDGE
  -> DENTAL_DEVICE_EXPORT_SPIKE_WITHOUT_REIMBURSEMENT_OR_MARGIN_BRIDGE
  -> CGM_COMMERCIALIZATION_REIMBURSEMENT_SPIKE_WITHOUT_DELIVERY_BRIDGE
```

Fine-archetype tags are subordinate to C25 and do not replace canonical classification.

## 7. Case Selection Summary

```jsonl
{"row_type":"case","case_id":"R7L83_C25_214450_PHARMARESEARCH_AESTHETIC_EXPORT_BRIDGE","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AestheticDeviceExport-ReimbursementBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Aesthetic/medical-device export and reimbursement/sell-through proxy supports C25 Stage2/Yellow, but Green remains blocked by source proxy."}
{"row_type":"case","case_id":"R7L83_C25_228670_RAY_DENTAL_DEVICE_EXPORT_SPIKE_FAILED","symbol":"228670","company_name":"레이","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DEVICE_EXPORT_SPIKE_WITHOUT_REIMBURSEMENT_OR_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Dental device export narrative had weak forward path; high MAE says C25 needs repeat-order/margin/reimbursement bridge."}
{"row_type":"case","case_id":"R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED","symbol":"099190","company_name":"아이센스","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_COMMERCIALIZATION_REIMBURSEMENT_SPIKE_WITHOUT_DELIVERY_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CGMReimbursementCommercialization-NoBridge","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C25 top-covered symbol exists, but this uses a different CGM commercialization/reimbursement false-positive trigger family and 2024 high-MAE path.","independent_evidence_weight":0.5,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"CGM commercialization/reimbursement narrative did not convert into near-term margin/revision; local C25 watch guard is reinforced."}
```

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 2
reused_case_count = 1
```

The point is not to weaken C25 broadly. It is to split the path:

```text
medical-device export/reimbursement bridge with repeat-order/margin evidence -> Stage2/Yellow allowed
commercialization/reimbursement theme without delivery/margin/revision -> Watch/local 4B guard
```

## 9. Evidence Source Map

```text
214450: export/repeat-order/reimbursement bridge proxy; exact URL pending.
228670: dental-device export commercialization narrative proxy; exact URL pending.
099190: CGM commercialization/reimbursement option proxy; exact URL pending.
```

Because all non-price sources are still source-name/proxy level:

```text
source_proxy_only = true
evidence_url_pending = true
promotion should hold until exact URLs are repaired
```

## 10. Price Data Source Map

```text
214450 -> atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv
228670 -> atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv
099190 -> atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv
```

## 11. Case-by-Case Trigger Grid

| symbol | company | trigger | entry | entry c | MFE90 | MAE90 | verdict |
|---|---|---|---:|---:|---:|---:|---|
| 214450 | 파마리서치 | Stage2 export/reimbursement bridge | 2024-04-01 | 108000 | 45.74% | -8.70% | positive |
| 228670 | 레이 | Dental device spike without bridge | 2024-04-01 | 16720 | 1.79% | -37.98% | counterexample |
| 099190 | 아이센스 | CGM/reimbursement spike without bridge | 2024-01-10 | 29500 | 3.05% | -39.32% | counterexample |

## 12. Trigger-Level OHLC Backtest Tables

```jsonl
{"row_type":"trigger","trigger_id":"R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE","case_id":"R7L83_C25_214450_PHARMARESEARCH_AESTHETIC_EXPORT_BRIDGE","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_BRIDGE","sector":"Bio/Healthcare/Medical Device","primary_archetype":"medical_device_export_reimbursement","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable-AestheticDeviceExport-ReimbursementBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":108000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public research/disclosure proxy available by or before trigger date","evidence_source":"source-name-level proxy; exact URL pending; export/repeat-order/reimbursement bridge used only as non-price proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["export_momentum_proxy","repeat_order_or_sellthrough_proxy","relative_strength"],"stage3_evidence_fields":["margin_bridge_proxy","revision_proxy"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv","profile_path":"atlas/symbol_profiles/214/214450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.52,"MFE_90D_pct":45.74,"MFE_180D_pct":147.22,"MAE_30D_pct":-8.7,"MAE_90D_pct":-8.7,"MAE_180D_pct":-8.7,"peak_date":"2024-12-16","peak_price":267000.0,"drawdown_after_peak_pct":-28.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"214450_20240401_108000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE","case_id":"R7L83_C25_228670_RAY_DENTAL_DEVICE_EXPORT_SPIKE_FAILED","symbol":"228670","company_name":"레이","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DEVICE_EXPORT_SPIKE_WITHOUT_REIMBURSEMENT_OR_MARGIN_BRIDGE","sector":"Bio/Healthcare/Medical Device","primary_archetype":"medical_device_export_reimbursement","loop_objective":"residual_false_positive_mining;counterexample_mining","trigger_type":"Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":16720.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public research/disclosure proxy available by or before trigger date","evidence_source":"source-name-level proxy; exact URL pending; dental equipment export narrative treated as insufficient without repeat-order/margin bridge","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["export_theme_proxy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","execution_or_delivery_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.79,"MFE_90D_pct":1.79,"MFE_180D_pct":1.79,"MAE_30D_pct":-23.33,"MAE_90D_pct":-37.98,"MAE_180D_pct":-69.62,"peak_date":"2024-04-04","peak_price":17020.0,"drawdown_after_peak_pct":-70.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early_but_watch_guard_valid","four_b_evidence_type":["price_only","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"228670_20240401_16720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","case_id":"R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED","symbol":"099190","company_name":"아이센스","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_COMMERCIALIZATION_REIMBURSEMENT_SPIKE_WITHOUT_DELIVERY_BRIDGE","sector":"Bio/Healthcare/Medical Device","primary_archetype":"medical_device_export_reimbursement","loop_objective":"residual_false_positive_mining;counterexample_mining;holdout_validation","trigger_type":"Stage2-FalsePositive-CGMReimbursementCommercialization-NoBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":29500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public research/disclosure proxy available by or before trigger date","evidence_source":"source-name-level proxy; exact URL pending; CGM commercialization/reimbursement theme treated as insufficient until margin/revision bridge","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["commercialization_proxy","reimbursement_optionality_proxy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","commercialization_delay_or_margin_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","profile_path":"atlas/symbol_profiles/099/099190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.05,"MFE_90D_pct":3.05,"MFE_180D_pct":3.05,"MAE_30D_pct":-30.34,"MAE_90D_pct":-39.32,"MAE_180D_pct":-49.25,"peak_date":"2024-01-12","peak_price":30400.0,"drawdown_after_peak_pct":-50.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_peak_followed_by_long_drawdown","four_b_evidence_type":["price_only","commercialization_delay_or_margin_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"099190_20240110_29500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same C25 symbol may exist in prior corpus, but trigger family and entry group are used as commercialization/reimbursement false-positive holdout","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

## 13. Current Calibrated Profile Stress Test

```text
1. Current profile should allow 214450 as Stage2/Yellow only because non-price bridge exists.
2. Current profile should block 228670 and 099190 from Stage2-Actionable because the return path is high-MAE/low-MFE.
3. Stage2 bonus is not globally wrong; it is too generous when C25 has only commercialization/reimbursement optionality.
4. Yellow threshold 75 is acceptable if bridge exists; it is too loose if bridge is only narrative.
5. Green threshold 87 / revision 55 should not be loosened.
6. price_only_blowoff guard is strengthened inside C25.
7. full 4B non-price requirement is kept; price-only local 4B remains watch.
8. hard 4C routing is not tested as a hard thesis break in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

```text
214450: Stage2/Yellow watch aligns with MFE90 +45.74 and MAE90 -8.70.
228670: Stage2 watch would have produced poor asymmetry; MFE90 +1.79 vs MAE90 -37.98.
099190: Stage2 watch would have produced poor asymmetry; MFE90 +3.05 vs MAE90 -39.32.
```

Green is not promoted in this MD due `source_proxy_only=true`.

## 15. 4B Local vs Full-window Timing Audit

For 228670 and 099190, the local price peak appeared early and was not backed by non-price 4B evidence. These are not full 4B exits; they are local watch-guard examples.

```text
228670: local peak 2024-04-04 high 17020; full forward low 2024-12-09 low 5080.
099190: local peak 2024-01-12 high 30400; full forward low 2024-12-27 low 14970.
```

## 16. 4C Protection Audit

No hard 4C is asserted. The two counterexamples are `thesis_break_watch_only` because the MD uses source proxy evidence and focuses on high-MAE guardrail calibration.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

This is not broad enough to cover all L7; it is C25-specific.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
new_axis_proposed = C25_repeat_order_reimbursement_bridge_required_shadow_only
```

Candidate rule:

```text
For C25, Stage2-Actionable/Yellow requires at least one non-price bridge:
- repeat order or sell-through evidence,
- reimbursement/adoption confirmation,
- margin or revision bridge,
- durable customer/export channel conversion.

Without that bridge, commercialization/reimbursement headlines remain Watch/local 4B guard.
```

## 19. Before / After Backtest Comparison

```text
P0 current proxy: average MFE90 16.86 / average MAE90 -28.67, false positive rate 0.67.
P3 C25 bridge guard: preserves 214450 positive, blocks 228670 and 099190 positive promotion.
```

## 20. Score-Return Alignment Matrix

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L83_C25_214450_PHARMARESEARCH_AESTHETIC_EXPORT_BRIDGE","trigger_id":"R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE","symbol":"214450","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":15,"revision_score":14,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":16,"revision_score":15,"relative_strength_score":13,"customer_quality_score":13,"policy_or_regulatory_score":5,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable/Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"Non-price repeat-order/export/reimbursement bridge justifies C25 Stage2/Yellow, not Green because exact URLs remain pending.","MFE_90D_pct":45.74,"MAE_90D_pct":-8.7,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L83_C25_228670_RAY_DENTAL_DEVICE_EXPORT_SPIKE_FAILED","trigger_id":"R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE","symbol":"228670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":13,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":16,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":55,"stage_label_after":"Stage2-FalsePositive-Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"Dental export theme without delivery/margin/reimbursement bridge should lose C25 credit and route to high-MAE watch.","MFE_90D_pct":1.79,"MAE_90D_pct":-37.98,"score_return_alignment_label":"score_return_misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED","trigger_id":"R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","symbol":"099190","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":57,"stage_label_after":"Stage2-FalsePositive-Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"CGM reimbursement/commercialization option should not count as Stage2-Actionable without reimbursed adoption and margin/revision bridge.","MFE_90D_pct":3.05,"MAE_90D_pct":-39.32,"score_return_alignment_label":"score_return_misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
```

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DENTAL_CGM_COMMERCIALIZATION_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":2,"reused_case_count":1,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"Need exact source URL repair before promotion; add true reimbursement-confirmed holdout in later R7 loop."}
```

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 2
reused_case_count: 1
reused_case_ids:
  - R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage2_actionable_evidence_bonus
residual_error_types_found:
  - medical_device_commercialization_theme_false_positive
  - reimbursement_optionality_without_margin_bridge
  - high_MAE_low_MFE_stage2_watch
new_axis_proposed:
  - C25_repeat_order_reimbursement_bridge_required_shadow_only
  - C25_local_4B_watch_guard_for_commercialization_spike
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C25
  - full_4b_requires_non_price_evidence within C25
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

One-line contribution:

```text
This loop adds 2 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date
- symbol profiles
- tradable raw OHLC rows
- entry_date / entry_price
- 30D / 90D / 180D MFE and MAE approximated from inspected Stock-Web rows
- corporate-action candidate windows
```

Not validated:

```text
- exact public evidence URLs
- production scoring code
- live/current candidate status
- investment recommendation
```

## 24. Shadow Weight Calibration

```jsonl
{"row_type":"shadow_weight","axis":"C25_repeat_order_reimbursement_bridge_required","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Positive path had repeat-order/export/margin bridge; two false positives lacked conversion evidence.","backtest_effect":"Blocks two high-MAE Stage2-Watch false positives while preserving one strong positive.","trigger_ids":"R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE|R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE|R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","calibration_usable_count":3,"new_independent_case_count":2,"counterexample_count":2,"confidence":"low_to_medium","proposal_type":"canonical_archetype_shadow_only","notes":"Not production; exact URLs pending."}
{"row_type":"shadow_weight","axis":"C25_local_4B_watch_guard_for_commercialization_spike","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Dental/CGM device spikes showed low MFE and deep MAE without non-price 4B confirmation.","backtest_effect":"Routes price-only commercialization spikes to Watch/local 4B rather than Stage2-Actionable.","trigger_ids":"R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE|R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","calibration_usable_count":2,"new_independent_case_count":1,"counterexample_count":2,"confidence":"low","proposal_type":"canonical_archetype_shadow_only","notes":"Reinforces existing price-only blowoff and full-4B non-price evidence axes within C25."}
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows excluded from tradable shards; corporate-action-contaminated windows are blocked."}
{"row_type":"price_source_validation","symbol":"214450","company_name":"파마리서치","profile_path":"atlas/symbol_profiles/214/214450.json","first_date":"2015-07-24","last_date":"2026-02-20","trading_day_count":2594,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"corporate_action_window_status":"clean_180D_window","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"228670","company_name":"레이","profile_path":"atlas/symbol_profiles/228/228670.json","first_date":"2019-08-08","last_date":"2026-02-20","trading_day_count":1603,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-06-03","2021-06-23"],"has_major_raw_discontinuity":true,"corporate_action_window_status":"clean_for_2024_window","profile_check":"2024 forward window clean; historical 2021 corporate-action candidates outside selected window"}
{"row_type":"price_source_validation","symbol":"099190","company_name":"아이센스","profile_path":"atlas/symbol_profiles/099/099190.json","first_date":"2013-01-30","last_date":"2026-02-20","trading_day_count":3205,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2015-10-02","2023-03-14","2023-04-10"],"has_major_raw_discontinuity":true,"corporate_action_window_status":"clean_for_2024_window","profile_check":"2024 forward window clean; corporate-action candidates before selected 2024 entry window"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L83_C25_214450_PHARMARESEARCH_AESTHETIC_EXPORT_BRIDGE","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AestheticDeviceExport-ReimbursementBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Aesthetic/medical-device export and reimbursement/sell-through proxy supports C25 Stage2/Yellow, but Green remains blocked by source proxy."}
{"row_type":"case","case_id":"R7L83_C25_228670_RAY_DENTAL_DEVICE_EXPORT_SPIKE_FAILED","symbol":"228670","company_name":"레이","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DEVICE_EXPORT_SPIKE_WITHOUT_REIMBURSEMENT_OR_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Dental device export narrative had weak forward path; high MAE says C25 needs repeat-order/margin/reimbursement bridge."}
{"row_type":"case","case_id":"R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED","symbol":"099190","company_name":"아이센스","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_COMMERCIALIZATION_REIMBURSEMENT_SPIKE_WITHOUT_DELIVERY_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CGMReimbursementCommercialization-NoBridge","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C25 top-covered symbol exists, but this uses a different CGM commercialization/reimbursement false-positive trigger family and 2024 high-MAE path.","independent_evidence_weight":0.5,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"CGM commercialization/reimbursement narrative did not convert into near-term margin/revision; local C25 watch guard is reinforced."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE","case_id":"R7L83_C25_214450_PHARMARESEARCH_AESTHETIC_EXPORT_BRIDGE","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_BRIDGE","sector":"Bio/Healthcare/Medical Device","primary_archetype":"medical_device_export_reimbursement","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable-AestheticDeviceExport-ReimbursementBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":108000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public research/disclosure proxy available by or before trigger date","evidence_source":"source-name-level proxy; exact URL pending; export/repeat-order/reimbursement bridge used only as non-price proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["export_momentum_proxy","repeat_order_or_sellthrough_proxy","relative_strength"],"stage3_evidence_fields":["margin_bridge_proxy","revision_proxy"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv","profile_path":"atlas/symbol_profiles/214/214450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.52,"MFE_90D_pct":45.74,"MFE_180D_pct":147.22,"MAE_30D_pct":-8.7,"MAE_90D_pct":-8.7,"MAE_180D_pct":-8.7,"peak_date":"2024-12-16","peak_price":267000.0,"drawdown_after_peak_pct":-28.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"214450_20240401_108000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE","case_id":"R7L83_C25_228670_RAY_DENTAL_DEVICE_EXPORT_SPIKE_FAILED","symbol":"228670","company_name":"레이","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DEVICE_EXPORT_SPIKE_WITHOUT_REIMBURSEMENT_OR_MARGIN_BRIDGE","sector":"Bio/Healthcare/Medical Device","primary_archetype":"medical_device_export_reimbursement","loop_objective":"residual_false_positive_mining;counterexample_mining","trigger_type":"Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":16720.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public research/disclosure proxy available by or before trigger date","evidence_source":"source-name-level proxy; exact URL pending; dental equipment export narrative treated as insufficient without repeat-order/margin bridge","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["export_theme_proxy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","execution_or_delivery_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.79,"MFE_90D_pct":1.79,"MFE_180D_pct":1.79,"MAE_30D_pct":-23.33,"MAE_90D_pct":-37.98,"MAE_180D_pct":-69.62,"peak_date":"2024-04-04","peak_price":17020.0,"drawdown_after_peak_pct":-70.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early_but_watch_guard_valid","four_b_evidence_type":["price_only","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"228670_20240401_16720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","case_id":"R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED","symbol":"099190","company_name":"아이센스","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_COMMERCIALIZATION_REIMBURSEMENT_SPIKE_WITHOUT_DELIVERY_BRIDGE","sector":"Bio/Healthcare/Medical Device","primary_archetype":"medical_device_export_reimbursement","loop_objective":"residual_false_positive_mining;counterexample_mining;holdout_validation","trigger_type":"Stage2-FalsePositive-CGMReimbursementCommercialization-NoBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":29500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public research/disclosure proxy available by or before trigger date","evidence_source":"source-name-level proxy; exact URL pending; CGM commercialization/reimbursement theme treated as insufficient until margin/revision bridge","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["commercialization_proxy","reimbursement_optionality_proxy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","commercialization_delay_or_margin_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","profile_path":"atlas/symbol_profiles/099/099190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.05,"MFE_90D_pct":3.05,"MFE_180D_pct":3.05,"MAE_30D_pct":-30.34,"MAE_90D_pct":-39.32,"MAE_180D_pct":-49.25,"peak_date":"2024-01-12","peak_price":30400.0,"drawdown_after_peak_pct":-50.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_peak_followed_by_long_drawdown","four_b_evidence_type":["price_only","commercialization_delay_or_margin_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"099190_20240110_29500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same C25 symbol may exist in prior corpus, but trigger family and entry group are used as commercialization/reimbursement false-positive holdout","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L83_C25_214450_PHARMARESEARCH_AESTHETIC_EXPORT_BRIDGE","trigger_id":"R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE","symbol":"214450","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":15,"revision_score":14,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":16,"revision_score":15,"relative_strength_score":13,"customer_quality_score":13,"policy_or_regulatory_score":5,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable/Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"Non-price repeat-order/export/reimbursement bridge justifies C25 Stage2/Yellow, not Green because exact URLs remain pending.","MFE_90D_pct":45.74,"MAE_90D_pct":-8.7,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L83_C25_228670_RAY_DENTAL_DEVICE_EXPORT_SPIKE_FAILED","trigger_id":"R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE","symbol":"228670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":13,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":16,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":55,"stage_label_after":"Stage2-FalsePositive-Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"Dental export theme without delivery/margin/reimbursement bridge should lose C25 credit and route to high-MAE watch.","MFE_90D_pct":1.79,"MAE_90D_pct":-37.98,"score_return_alignment_label":"score_return_misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L83_C25_099190_ISENS_CGM_COMMERCIALIZATION_PRICE_SPIKE_FAILED","trigger_id":"R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","symbol":"099190","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":57,"stage_label_after":"Stage2-FalsePositive-Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"CGM reimbursement/commercialization option should not count as Stage2-Actionable without reimbursed adoption and margin/revision bridge.","MFE_90D_pct":3.05,"MAE_90D_pct":-39.32,"score_return_alignment_label":"score_return_misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 aggregate_metric row

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DENTAL_CGM_COMMERCIALIZATION_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":16.86,"avg_MAE90_pct":-28.67,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C25 needs export/reimbursement/repeat-order bridge; mere device commercialization theme produced high-MAE false positives."}
```

### 25.6 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","axis":"C25_repeat_order_reimbursement_bridge_required","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Positive path had repeat-order/export/margin bridge; two false positives lacked conversion evidence.","backtest_effect":"Blocks two high-MAE Stage2-Watch false positives while preserving one strong positive.","trigger_ids":"R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE|R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE|R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","calibration_usable_count":3,"new_independent_case_count":2,"counterexample_count":2,"confidence":"low_to_medium","proposal_type":"canonical_archetype_shadow_only","notes":"Not production; exact URLs pending."}
{"row_type":"shadow_weight","axis":"C25_local_4B_watch_guard_for_commercialization_spike","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Dental/CGM device spikes showed low MFE and deep MAE without non-price 4B confirmation.","backtest_effect":"Routes price-only commercialization spikes to Watch/local 4B rather than Stage2-Actionable.","trigger_ids":"R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE|R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","calibration_usable_count":2,"new_independent_case_count":1,"counterexample_count":2,"confidence":"low","proposal_type":"canonical_archetype_shadow_only","notes":"Reinforces existing price-only blowoff and full-4B non-price evidence axes within C25."}
```

### 25.7 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"83","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":2,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["medical_device_commercialization_theme_false_positive","reimbursement_optionality_without_margin_bridge","high_MAE_low_MFE_stage2_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- Price-only rows cannot promote Stage2/Stage3.
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

## 27. Next Round State

```text
completed_round = R7
completed_loop = 83
next_round = R8
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 28. Source Notes

```text
Stock-Web rows inspected:
- atlas/manifest.json
- atlas/symbol_profiles/214/214450.json
- atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv
- atlas/symbol_profiles/228/228670.json
- atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv
- atlas/symbol_profiles/099/099190.json
- atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv

No investment recommendation language is intended.
```
