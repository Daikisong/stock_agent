# E2R Stock-Web v12 Residual Research — R2 Loop 83 / L2 / C09

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 83
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: C09_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE_VS_REVENUE_BRIDGE
sector: AI·반도체·전자 / advanced equipment valuation blowoff
output_file: e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Research Metadata

This Markdown file is a standalone v12 historical trigger-level residual research artifact. It follows the `post_calibrated_sector_archetype_residual_research` mode and uses the Stock-Web OHLC atlas as the sole price path source.

```text
scheduled_round = R2
scheduled_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated / e2r_2_2 rolling proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are treated as background, not re-proposed globally:

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
round = R2
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = C09_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE_VS_REVENUE_BRIDGE
```

C09 is the advanced-equipment pressure valve. It should not kill every bottleneck equipment rerating, but it must stop the cases where the machine roars, the stock jumps, and the order/revenue/margin bridge never arrives.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index is used only as a duplicate-avoidance ledger. The relevant snapshot shows:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:
rows = 17
symbols = 11
date range = 2023-07-14~2024-09-24
good/bad S2 = 7/3
4B/4C = 1/0
URL pending/proxy = 7/7
top covered symbols = 322310(3), 348210(3), 089030(2), 140860(2), 031980(1), 064290(1)
```

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This loop avoids the most repeated C09 keys by adding **two same-archetype new symbols** (`403870`, `240810`) and one soft-reused positive-control symbol (`140860`) with a different trigger family. The reused positive-control symbol is retained only to keep the positive/counterexample balance.

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"403870","trigger_type":"Stage2-FalsePositive-HPSP-AdvancedEquipment-Blowoff-HighMAE","entry_date":"2024-02-13","duplicate_status":"same archetype new symbol; exact hard key not present in No-Repeat top-covered list","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"240810","trigger_type":"Stage2-Actionable-Then-4B-Watch-WonIKIPS-MemoryEquipment-RoundTrip","entry_date":"2024-02-29","duplicate_status":"same archetype new symbol; exact hard key not present in No-Repeat top-covered list","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"140860","trigger_type":"Stage2-Actionable-AdvancedAFM-RevenueBridge-Positive","entry_date":"2024-05-14","duplicate_status":"soft symbol reuse, new trigger-family control; exact hard key not reused","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","validation_status":"usable_for_historical_calibration","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"403870","company_name":"HPSP","profile_path":"atlas/symbol_profiles/403/403870.json","first_date":"2022-07-15","last_date":"2026-02-20","trading_day_count":879,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2023-03-16","2023-04-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist in 2023 and do not contaminate the 2024 forward window selected here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"240810","company_name":"원익IPS","profile_path":"atlas/symbol_profiles/240/240810.json","first_date":"2016-05-02","last_date":"2026-02-20","trading_day_count":2405,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"140860","company_name":"파크시스템스","profile_path":"atlas/symbol_profiles/140/140860.json","first_date":"2015-12-17","last_date":"2026-02-20","trading_day_count":2494,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_2025_forward_window"}
```

## 5. Historical Eligibility Gate

All three representative trigger rows satisfy:

```text
entry_date exists in tradable shard
entry_price = entry_date close
forward 180 trading-day window available before Stock-Web manifest max_date
MFE_30D / 90D / 180D and MAE_30D / 90D / 180D calculated from tradable raw OHLC
corporate-action-contaminated 180D window = false
```

## 6. Canonical Archetype Compression Map

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  ├─ HPSP_ADVANCED_PROCESS_EQUIPMENT_BLOWOFF_HIGH_MAE
  ├─ WONIKIPS_MEMORY_EQUIPMENT_RECOVERY_ROUNDTRIP_4B_WATCH
  └─ ADVANCED_METROLOGY_AFM_REVENUE_BRIDGE_WITH_VALUATION_DISCIPLINE
```

Compression rule:

```text
Do not split C09 into a new scoring archetype. Use fine_archetype_id only to separate:
- advanced-equipment price blowoff,
- memory-equipment recovery round-trip requiring 4B watch,
- advanced-metrology revenue bridge with shallow drawdown.
```

## 7. Case Selection Summary

```jsonl
{"row_type":"case","case_id":"C09_R2L83_403870_HPSP_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE","symbol":"403870","company_name":"HPSP","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HPSP_ADVANCED_PROCESS_EQUIPMENT_BLOWOFF_HIGH_MAE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New C09 symbol; large February blowoff produced limited MFE and deep 90/180D MAE. Requires bridge/4B-watch guard."}
{"row_type":"case","case_id":"C09_R2L83_240810_WONIKIPS_MEMORY_EQUIPMENT_ROUNDTRIP_4B_WATCH","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"WONIKIPS_MEMORY_EQUIPMENT_RECOVERY_ROUNDTRIP_4B_WATCH","case_type":"4B_too_late","positive_or_counterexample":"counterexample","best_trigger":"R2L83_C09_240810_20240229_STAGE2_ACTIONABLE_THEN_4B_WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early_MFE_then_180D_roundtrip","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"New C09 symbol; early +36.7% MFE then 180D MAE below -32%. It supports local 4B/watch timing rather than Green relaxation."}
{"row_type":"case","case_id":"C09_R2L83_140860_PARKSYSTEMS_AFM_REVENUE_BRIDGE","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_AFM_REVENUE_BRIDGE_WITH_VALUATION_DISCIPLINE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L83_C09_140860_20240514_STAGE2_ADVANCED_AFM_REVENUE_BRIDGE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"soft_symbol_reuse_new_trigger_family","independent_evidence_weight":0.5,"score_price_alignment":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Soft-reuse positive control. Clean profile and low drawdown path show that C09 can support Stage2/Yellow when advanced metrology has a revenue bridge proxy; no Green relaxation due URL pending."}
```

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
representative_trigger_count = 3
new_symbol_count = 2
same_archetype_new_symbol_count = 2
same_archetype_new_trigger_family_count = 3
```

This is deliberately counterexample-heavy because C09’s residual risk is not “missing every advanced-equipment winner”; it is allowing too much Stage2/Yellow credit when a price spike wears an AI-equipment mask but has no verified order/revenue/margin bridge or when an early equipment recovery round-trip needs a local 4B watch.

## 9. Evidence Source Map

The non-price evidence layer in this MD is intentionally conservative:

```text
evidence_source_type = historical_public_report_consensus_proxy
evidence_url_pending = true
source_proxy_only = true
```

Interpretation:

```text
- Price-path residual analysis is usable.
- Promotion should prefer hold/data-quality repair until exact URLs are attached.
- The shadow rule is calibration-planning evidence, not production scoring evidence.
```

## 10. Price Data Source Map

```text
403870:
  profile = atlas/symbol_profiles/403/403870.json
  tradable_shard = atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv

240810:
  profile = atlas/symbol_profiles/240/240810.json
  tradable_shard = atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv

140860:
  profile = atlas/symbol_profiles/140/140860.json
  tradable_shards = atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv + 2025.csv
```

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | entry_date | entry_price | role | outcome |
|---|---:|---|---:|---:|---|---|
| C09_R2L83_403870_HPSP_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE | 403870 | Stage2-FalsePositive-HPSP-AdvancedEquipment-Blowoff-HighMAE | 2024-02-13 | 59300 | counterexample | MFE180 +7.76 / MAE180 -52.78 |
| C09_R2L83_240810_WONIKIPS_MEMORY_EQUIPMENT_ROUNDTRIP_4B_WATCH | 240810 | Stage2-Actionable-Then-4B-Watch-WonIKIPS-MemoryEquipment-RoundTrip | 2024-02-29 | 32800 | counterexample / 4B watch | MFE180 +36.74 / MAE180 -32.32 |
| C09_R2L83_140860_PARKSYSTEMS_AFM_REVENUE_BRIDGE | 140860 | Stage2-Actionable-AdvancedAFM-RevenueBridge-Positive | 2024-05-14 | 164600 | positive | MFE180 +51.88 / MAE180 -5.16 |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 403870 HPSP — advanced equipment blowoff / high-MAE counterexample

The profile contains corporate-action candidates in 2023 only. The selected 2024 forward window is clean. Entry row is `2024-02-13 c=59300`. The near-term peak was `2024-02-15 h=63900`; the 90D low was `2024-05-10 l=35650`; the 180D low was `2024-10-31 l=28000`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE","case_id":"C09_R2L83_403870_HPSP_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE","symbol":"403870","company_name":"HPSP","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HPSP_ADVANCED_PROCESS_EQUIPMENT_BLOWOFF_HIGH_MAE","sector":"AI·반도체·전자","primary_archetype":"advanced_process_equipment","loop_objective":"residual_false_positive_mining;4B_non_price_requirement_stress_test;counterexample_mining","trigger_type":"Stage2-FalsePositive-HPSP-AdvancedEquipment-Blowoff-HighMAE","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":59300.0,"entry_price_basis":"close","entry_row_exists":true,"evidence_available_at_that_date":"historical public narrative proxy; exact URL pending","evidence_source_type":"historical_public_report_consensus_proxy","evidence_source":"source-name-level proxy; exact URL pending; high-pressure advanced process equipment narrative treated as insufficient without order/revenue/margin bridge","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"evidence_url_pending":true,"source_proxy_only":true,"evidence_family":"price;research_report_proxy","non_price_evidence_bridge":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv","profile_path":"atlas/symbol_profiles/403/403870.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.76,"MAE_30D_pct":-18.13,"MFE_90D_pct":7.76,"MAE_90D_pct":-39.88,"MFE_180D_pct":7.76,"MAE_180D_pct":-52.78,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":63900.0,"peak_date_30D":"2024-02-15","peak_price_30D":63900.0,"peak_date_90D":"2024-02-15","peak_price_90D":63900.0,"peak_date_180D":"2024-02-15","peak_price_180D":63900.0,"max_drawdown_low_30D_date":"2024-03-27","max_drawdown_low_30D":48550.0,"max_drawdown_low_90D_date":"2024-05-10","max_drawdown_low_90D":35650.0,"max_drawdown_low_180D_date":"2024-10-31","max_drawdown_low_180D":28000.0,"drawdown_after_peak_pct":-56.18,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","current_profile_residual":"C09 advanced-equipment momentum created less than +8% MFE and more than -39% MAE90. Stage2/Yellow needs a verified bridge; otherwise local high-MAE guard should dominate.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_403870_2024-02-13_59300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 12.2 240810 원익IPS — early MFE then 4B/watch round-trip

Profile has no corporate-action candidate dates. Entry row is `2024-02-29 c=32800`; the 30D/90D/180D peak is `2024-04-08 h=44850`; the 180D low is `2024-11-14 l=22200`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L83_C09_240810_20240229_STAGE2_ACTIONABLE_THEN_4B_WATCH","case_id":"C09_R2L83_240810_WONIKIPS_MEMORY_EQUIPMENT_ROUNDTRIP_4B_WATCH","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"WONIKIPS_MEMORY_EQUIPMENT_RECOVERY_ROUNDTRIP_4B_WATCH","sector":"AI·반도체·전자","primary_archetype":"advanced_memory_equipment_roundtrip","loop_objective":"4B_non_price_requirement_stress_test;yellow_threshold_stress_test;counterexample_mining","trigger_type":"Stage2-Actionable-Then-4B-Watch-WonIKIPS-MemoryEquipment-RoundTrip","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":32800.0,"entry_price_basis":"close","entry_row_exists":true,"evidence_available_at_that_date":"historical memory-equipment recovery proxy; exact URL pending","evidence_source_type":"historical_public_report_consensus_proxy","evidence_source":"source-name-level proxy; exact URL pending; memory equipment recovery treated as Stage2/Watch unless margin/order bridge persists beyond price rebound","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","revision_slowdown"],"stage4c_evidence_fields":[],"evidence_url_pending":true,"source_proxy_only":true,"evidence_family":"price;research_report_proxy;revision_proxy","non_price_evidence_bridge":true,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.74,"MAE_30D_pct":-12.8,"MFE_90D_pct":36.74,"MAE_90D_pct":-12.8,"MFE_180D_pct":36.74,"MAE_180D_pct":-32.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":44850.0,"peak_date_30D":"2024-04-08","peak_price_30D":44850.0,"peak_date_90D":"2024-04-08","peak_price_90D":44850.0,"peak_date_180D":"2024-04-08","peak_price_180D":44850.0,"max_drawdown_low_30D_date":"2024-02-29","max_drawdown_low_30D":28600.0,"max_drawdown_low_90D_date":"2024-02-29","max_drawdown_low_90D":28600.0,"max_drawdown_low_180D_date":"2024-11-14","max_drawdown_low_180D":22200.0,"drawdown_after_peak_pct":-50.5,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_needed_after_early_MFE_roundtrip","four_b_evidence_type":["price_only","valuation_blowoff","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"early_positive_then_high_MAE_roundtrip","current_profile_verdict":"current_profile_4B_too_late","current_profile_residual":"The Stage2/Yellow window was tradable, but without timely local 4B/watch the case round-tripped into -32% MAE180. C09 needs a 4B/watch overlay when early MFE is strong but evidence quality does not upgrade to durable margin bridge.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_240810_2024-02-29_32800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 12.3 140860 파크시스템스 — positive bridge control

Stock-Web profile has no corporate-action candidate dates and the 2024/2025 forward window is clean. Entry row is `2024-05-14 c=164600`; the 30D peak is `2024-06-19 h=192300`, the 90D peak is `2024-08-21 h=198800`, and the 180D peak is `2025-01-22 h=250000`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L83_C09_140860_20240514_STAGE2_ADVANCED_AFM_REVENUE_BRIDGE_POSITIVE","case_id":"C09_R2L83_140860_PARKSYSTEMS_AFM_REVENUE_BRIDGE","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_AFM_REVENUE_BRIDGE_WITH_VALUATION_DISCIPLINE","sector":"AI·반도체·전자","primary_archetype":"advanced_metrology_equipment","loop_objective":"residual_missed_structural_mining;green_strictness_stress_test;sector_specific_rule_discovery","trigger_type":"Stage2-Actionable-AdvancedAFM-RevenueBridge-Positive","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":164600.0,"entry_price_basis":"close","entry_row_exists":true,"evidence_available_at_that_date":"historical source proxy available by trigger date; exact URL pending","evidence_source_type":"historical_public_report_consensus_proxy","evidence_source":"source-name-level proxy; exact URL pending; advanced metrology/AFM revenue-bridge thesis only used as non-price proxy, not as final citation-grade evidence","stage2_evidence_fields":["early_revision_signal","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"evidence_url_pending":true,"source_proxy_only":true,"evidence_family":"financial_actual;research_report_proxy;revision_proxy","non_price_evidence_bridge":true,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/140/140860.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.83,"MAE_30D_pct":-2.43,"MFE_90D_pct":20.78,"MAE_90D_pct":-5.16,"MFE_180D_pct":51.88,"MAE_180D_pct":-5.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-22","peak_price":250000.0,"peak_date_30D":"2024-06-19","peak_price_30D":192300.0,"peak_date_90D":"2024-08-21","peak_price_90D":198800.0,"peak_date_180D":"2025-01-22","peak_price_180D":250000.0,"max_drawdown_low_30D_date":"2024-05-14","max_drawdown_low_30D":160600.0,"max_drawdown_low_90D_date":"2024-07-18","max_drawdown_low_90D":156100.0,"max_drawdown_low_180D_date":"2024-07-18","max_drawdown_low_180D":156100.0,"drawdown_after_peak_pct":-27.4,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","current_profile_residual":"C09 should not be pure blowoff-only. Advanced metrology can work when drawdown is shallow and 90/180D path confirms structural bridge; however exact evidence URL remains pending, so this row supports watch-to-Yellow rather than Green relaxation.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_140860_2024-05-14_164600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"soft_symbol_reuse_new_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Current calibrated profile judgement | It should allow 140860 as Stage2/Yellow-watch but block 403870 from Yellow/Green and mark 240810 as local 4B/watch after early MFE. |
| MFE/MAE alignment | 140860 aligns positively; 403870 is low-MFE/high-MAE; 240810 is early-MFE then deep round-trip. |
| Stage2 bonus too much or too little | Too much for C09 if applied to price/research-proxy-only cases; acceptable when non-price revenue bridge exists. |
| Yellow threshold 75 | Correct if evidence bridge required; too lenient if C09 price-only momentum can pass. |
| Green threshold 87 / revision 55 | Keep strict; no Green relaxation. |
| price-only blowoff guard | Kept and locally strengthened for C09. |
| full 4B non-price requirement | Kept; price-only local peaks should be Watch not full 4B. |
| hard 4C routing | Not directly tested; these are thesis-break watch / high-MAE cases, not hard 4C. |

## 14. Stage2 / Yellow / Green Comparison

```text
403870:
  Stage2 price/research proxy without verified bridge would be too early.
  Yellow/Green should be blocked due MFE90 7.76 and MAE90 -39.88.

240810:
  Stage2 was tradable but needs timely 4B/watch.
  Early MFE90 +36.74 later became MAE180 -32.32, so Green should not be relaxed.

140860:
  Stage2/Yellow-watch works when non-price revenue bridge exists.
  Green remains blocked by evidence URL pending / source proxy only.
```

Green lateness ratio is not applicable because the selected triggers are Stage2/Watch/false-positive tests, not confirmed Stage3-Green triggers.

## 15. 4B Local vs Full-window Timing Audit

```text
403870:
  local and full-window peak occurred within the immediate blowoff.
  four_b_evidence_type = price_only + valuation_blowoff + positioning_overheat
  verdict = price-only local peak cannot become full 4B without non-price evidence.

240810:
  full-window peak occurred after +36.74% MFE, then 180D MAE reached -32.32%.
  verdict = local 4B/watch needed after early MFE when margin/revision bridge does not persist.

140860:
  no 4B overlay proposed.
```

## 16. 4C Protection Audit

```text
hard_4C = not directly tested
thesis_break_watch_only = 403870, 240810
false_break = none
```

The C09 residual here is closer to 4B/watch and high-MAE guard than hard 4C confirmation.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

Reason: the evidence is C09-specific, not broad enough across L2 sub-archetypes. It should not change all L2 AI/semiconductor/electronics scoring.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

Candidate:

```text
For C09, Stage2/Yellow requires at least one non-price order/revenue/margin conversion bridge.
If evidence is price/research-proxy only and MFE90<10 with MAE90<=-25 in historical calibration, route to Watch/high-MAE guard instead of positive Stage2/Yellow.
If early MFE90>=30 but MAE180<=-30 and bridge quality does not upgrade, add local 4B/watch timing rather than Green relaxation.
```

## 19. Before / After Backtest Comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L83_C09_P0_BASELINE","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile":"P0_e2r_2_0_baseline","profile_role":"rollback_reference","expected_error":"Would over-credit advanced equipment price/bottleneck momentum and under-detect 90/180D MAE."}
{"row_type":"profile_comparison","comparison_id":"R2L83_C09_P0B_CURRENT","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile":"P0b_e2r_2_2_rolling_calibrated","profile_role":"current_default_proxy","expected_error":"Global price-only guard works, but C09 still needs a local rule separating advanced-metrology revenue bridge from valuation blowoff and round-trip 4B/watch."}
{"row_type":"profile_comparison","comparison_id":"R2L83_C09_P1_BRIDGE_REQUIRED","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile":"P1_shadow_C09_stage2_required_bridge","profile_role":"shadow_candidate","expected_effect":"Stage2/Yellow requires at least one non-price order/revenue/margin conversion bridge; price spike only remains Watch."}
{"row_type":"profile_comparison","comparison_id":"R2L83_C09_P2_HIGH_MAE_GUARD","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile":"P2_shadow_C09_high_MAE_guard","profile_role":"shadow_candidate","expected_effect":"If MFE90 < 10 and MAE90 <= -25 in historical calibration, future C09 cases need stronger evidence bridge before Yellow/Green."}
{"row_type":"profile_comparison","comparison_id":"R2L83_C09_P3_RECOMMENDED","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile":"P3_recommended_shadow_only","profile_role":"recommended_shadow_rule","expected_effect":"No production change now; record local 4B/watch guard and Stage2 bridge candidate for later batch planner."}
```

## 20. Score-Return Alignment Matrix

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L83_403870_HPSP_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE","trigger_id":"R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE","symbol":"403870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":9,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage2-Watch/Possible-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-Watch / high_MAE_guard","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"High MAE and low MFE show price/research-proxy-only equipment excitement should be guarded.","MFE_90D_pct":7.76,"MAE_90D_pct":-39.88,"score_return_alignment_label":"misaligned_before_aligned_after","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L83_240810_WONIKIPS_MEMORY_EQUIPMENT_ROUNDTRIP_4B_WATCH","trigger_id":"R2L83_C09_240810_20240229_STAGE2_ACTIONABLE_THEN_4B_WATCH","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Watch / local_4B_guard","changed_components":["revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Early MFE was real, but later round-trip shows C09 needs 4B/watch timing if durable bridge is not confirmed.","MFE_90D_pct":36.74,"MAE_90D_pct":-12.8,"score_return_alignment_label":"early_aligned_then_4B_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L83_140860_PARKSYSTEMS_AFM_REVENUE_BRIDGE","trigger_id":"R2L83_C09_140860_20240514_STAGE2_ADVANCED_AFM_REVENUE_BRIDGE_POSITIVE","symbol":"140860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":4,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","changed_components":["no_green_relaxation"],"component_delta_explanation":"Positive path comes from revision/revenue bridge and shallow MAE, not price-only multiple expansion.","MFE_90D_pct":20.78,"MAE_90D_pct":-5.16,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
```

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","round":"R2","loop":"83","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_LOCAL_ADVANCED_EQUIPMENT_BLOWOFF_STRESS","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"new_trigger_family_count":3,"same_archetype_new_trigger_family_count":3,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C09 still needs exact evidence URL repair and less-covered symbol expansion; this file adds two same-archetype new symbols and high-MAE residual stress rows."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_total_min
residual_error_types_found:
  - C09 high-MAE low-MFE false positive
  - advanced-equipment price/research-proxy-only blowoff
  - early MFE then 180D round-trip requiring local 4B/watch
new_axis_proposed: C09_high_MAE_bridge_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C09
  - full_4b_requires_non_price_evidence within C09
existing_axis_weakened: null
existing_axis_kept:
  - Stage3-Green strictness
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-Web tradable raw OHLC rows
- profile corporate-action contamination check
- entry_date / entry_price
- MFE / MAE / peak / drawdown
- current calibrated profile stress test
- no-repeat hard-key avoidance
```

Non-validation scope:

```text
- exact public disclosure/report URLs
- production scoring patch
- live stock recommendation
- broker/API connection
- current 2026 candidate scan
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"C09 Stage2/Yellow should require non-price order/revenue/margin bridge","Blocks 403870 false positive while preserving 140860 bridge case","R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE|R2L83_C09_240810_20240229_STAGE2_ACTIONABLE_THEN_4B_WATCH|R2L83_C09_140860_20240514_STAGE2_ADVANCED_AFM_REVENUE_BRIDGE_POSITIVE",3,3,2,medium,canonical_shadow_only,"not production; URL repair needed"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Price-only or early-MFE C09 peaks should remain Watch unless durable non-price evidence exists","Captures 240810 round-trip and 403870 blowoff without weakening 140860 positive bridge","R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE|R2L83_C09_240810_20240229_STAGE2_ACTIONABLE_THEN_4B_WATCH",3,3,2,medium,canonical_shadow_only,"existing axis strengthened locally"
shadow_weight,high_mae_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"If MFE90<10 and MAE90<=-25, require evidence-quality repair before Yellow/Green","Captures 403870 as high-MAE false positive","R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not global; C09 pressure-valve rule"
```

## 25. Machine-Readable Rows

All machine-readable rows are embedded above by section:

```text
price_source_validation rows: 4
case rows: 3
trigger rows: 3
score_simulation rows: 3
profile_comparison rows: 5
coverage_matrix rows: 1
shadow_weight rows: 3
narrative_only rows: 3
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated / e2r_2_2 rolling profile.

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

### C09-specific implementation hint

If later evidence URL repair confirms the non-price proxies, consider a C09-scoped safe patch only:

```text
stage2_required_bridge:
  C09 Stage2/Yellow must have at least one verified non-price order/revenue/margin bridge.

local_4b_watch_guard:
  C09 price-only or early-MFE peak remains Watch, not Green/full 4B, unless durable non-price evidence exists.

high_mae_guardrail:
  If C09 historical class shows MFE90<10 and MAE90<=-25, require evidence-quality repair before Yellow/Green promotion.
```

Do not loosen Stage3-Green. Do not use future MFE/MAE in runtime scoring. Use this only for calibration profile planning.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 83
next_round = R3
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 28. Source Notes

Price source notes:

```text
Songdaiki/stock-web manifest:
  source_name = FinanceData/marcap
  price_adjustment_status = raw_unadjusted_marcap
  min_date = 1995-05-02
  max_date = 2026-02-20
  tradable_row_count = 14354401
  symbol_count = 5414
  active_like_symbol_count = 2868
```

Non-price source notes:

```text
This MD intentionally keeps evidence_source at source-name/proxy level and sets evidence_url_pending=true.
Later URL repair is required before promotion.
```
