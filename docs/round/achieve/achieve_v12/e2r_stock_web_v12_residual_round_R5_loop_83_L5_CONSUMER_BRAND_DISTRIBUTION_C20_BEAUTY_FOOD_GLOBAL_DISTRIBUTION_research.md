# E2R Stock-Web v12 Residual Research — R5 Loop 83 / L5 / C20

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 83
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_K_BEAUTY_GLOBAL_DISTRIBUTION_REPEAT_SELLTHROUGH_VS_CHINA_REBOUND_PRICE_SPIKE
sector: 소비재·브랜드·유통 / K-food·K-beauty 글로벌 유통
output_file: e2r_stock_web_v12_residual_round_R5_loop_83_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Research Metadata

This is a v12 post-calibrated sector/archetype residual research file. It uses the `Songdaiki/stock-web` 1D OHLC atlas as the only price source and writes standalone machine-readable rows for later batch ingestion.

```text
scheduled_round = R5
scheduled_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_K_BEAUTY_GLOBAL_DISTRIBUTION_REPEAT_SELLTHROUGH_VS_CHINA_REBOUND_PRICE_SPIKE
```

## 1. Current Calibrated Profile Assumption

Current calibrated profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rolling_profile_context = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Applied axes treated as already present:

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

This loop does not re-prove the global axes. It tests whether C20 needs a narrower bridge: export/channel/repeat sell-through and OPM/revision must be separated from broad brand/China-rebound price spikes.

## 2. Round / Large Sector / Canonical Archetype Scope

R5 hard-gate:

```text
R5 -> L5_CONSUMER_BRAND_DISTRIBUTION
canonical scope selected = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_sector_consistency = pass
```

C20 is the shelf-space archetype. A product can have a famous label, but the stock only earns C20 credit when the product keeps leaving the shelf, reorder data confirms it, and margin/revision converts that movement into earnings.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used as duplicate ledger only:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION:
rows = 19
symbols = 11
date range = 2023-01-30~2024-06-14
good/bad S2 = 8/2
4B/4C = 4/0
top covered symbols = 226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2)
```

Hard duplicate key rule:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty check:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","trigger_type":"Stage2-Actionable-KFood-ExportRepeatSellthrough","entry_date":"2024-04-09","duplicate_status":"not in top-covered C20 symbols; new C20 positive structural bridge control"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","trigger_type":"Stage2-FalsePositive-KBeauty-ChinaReboundNoRepeatSellthrough","entry_date":"2024-05-31","duplicate_status":"not in top-covered C20 symbols; new C20 brand/China-rebound false-positive counterexample"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"004370","trigger_type":"Stage2-Local4B-KFood-BrandExportRoundtripNoRevisionBridge","entry_date":"2024-05-28","duplicate_status":"not in top-covered C20 symbols; new C20 mature-brand roundtrip/4B-watch counterexample"}
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"price_source_validation","symbol":"003230","company_name":"삼양식품","profile_path":"atlas/symbol_profiles/003/003230.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7704,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2003-07-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Only 2003 corporate-action candidate; 2024 forward window is clean.","price_adjustment_status":"raw_unadjusted_marcap","status_inferred":"active_like"}
{"row_type":"price_source_validation","symbol":"090430","company_name":"아모레퍼시픽","profile_path":"atlas/symbol_profiles/090/090430.json","first_date":"2006-06-29","last_date":"2026-02-20","trading_day_count":4834,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-05-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Only 2015 corporate-action candidate; 2024/2025 forward window is clean.","price_adjustment_status":"raw_unadjusted_marcap","status_inferred":"active_like"}
{"row_type":"price_source_validation","symbol":"004370","company_name":"농심","profile_path":"atlas/symbol_profiles/004/004370.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7742,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2000-07-28","2003-07-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Only old corporate-action candidates; 2024/2025 forward window is clean.","price_adjustment_status":"raw_unadjusted_marcap","status_inferred":"active_like"}
```

## 5. Historical Eligibility Gate

All representative triggers in this loop satisfy:

```text
entry_date exists in stock-web tradable shard = true
entry_price = close column on entry_date
forward_180D window available by manifest_max_date = true
MFE/MAE 30D/90D/180D calculated = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

```text
K_FOOD_EXPORT_REPEAT_SELLTHROUGH_OPM_REVISION
  -> C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

K_BEAUTY_CHINA_REBOUND_NO_REPEAT_SELLTHROUGH
  -> C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

MATURE_K_FOOD_BRAND_EXPORT_SPIKE_WITHOUT_REVISION_BRIDGE
  -> C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

## 7. Case Selection Summary

```jsonl
{"row_type":"case","case_id":"C20_R5L83_003230_SAMYANG_KFOOD_REPEAT_EXPORT_BRIDGE","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_EXPORT_REPEAT_SELLTHROUGH_OPM_REVISION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L83_C20_003230_20240409_STAGE2_KFOOD_REPEAT_EXPORT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C20 positive control: non-price proxy is export/channel/repeat sell-through and OPM/revision bridge; price path confirms large MFE with shallow MAE."}
{"row_type":"case","case_id":"C20_R5L83_090430_AMORE_CHINA_REBOUND_FALSE_POSITIVE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CHINA_REBOUND_NO_REPEAT_SELLTHROUGH","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L83_C20_090430_20240531_STAGE2_KBEAUTY_CHINA_REBOUND_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Broad beauty rebound and brand recovery price spike failed without durable global repeat sell-through / OPM bridge."}
{"row_type":"case","case_id":"C20_R5L83_004370_NONGSHIM_MATURE_BRAND_ROUNDTRIP","symbol":"004370","company_name":"농심","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"MATURE_K_FOOD_BRAND_EXPORT_SPIKE_WITHOUT_REVISION_BRIDGE","case_type":"4B_too_late","positive_or_counterexample":"counterexample","best_trigger":"R5L83_C20_004370_20240528_LOCAL4B_MATURE_BRAND_ROUNDTRIP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_early_MFE_late_MAE_roundtrip","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Mature K-food brand produced local MFE but lacked repeat-sellthrough/revision bridge and later suffered >30% 180D drawdown from entry."}
```

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 3
new_symbol_count = 3
```

Interpretation: this loop deliberately adds counterexample pressure to C20, where the prior snapshot had only two bad Stage2 rows against eight good Stage2 rows.

## 9. Evidence Source Map

Evidence is intentionally marked source-proxy level. It is enough for price-path residual stress testing, not enough for immediate promotion without URL repair.

```text
003230 non-price proxy:
  export growth + overseas channel expansion + repeat demand + margin/revision bridge.

090430 non-price proxy:
  brand/China-beauty rebound narrative without durable global repeat sell-through proof.

004370 non-price proxy:
  mature K-food export/brand momentum without enough revision/OPM bridge to justify full C20 promotion after local peak.
```

## 10. Price Data Source Map

```text
003230 tradable shard = atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv
090430 tradable shard = atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv + 2025.csv
004370 tradable shard = atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv
```

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| C20_R5L83_003230_SAMYANG_KFOOD_REPEAT_EXPORT_BRIDGE | 003230 | Stage2-Actionable-KFood-ExportRepeatSellthrough | 2024-04-09 | 222500 | 222.70 | -4.27 | 259.55 | -4.27 | positive |
| C20_R5L83_090430_AMORE_CHINA_REBOUND_FALSE_POSITIVE | 090430 | Stage2-FalsePositive-KBeauty-ChinaReboundNoRepeatSellthrough | 2024-05-31 | 194200 | 3.24 | -37.59 | 3.24 | -48.76 | counterexample |
| C20_R5L83_004370_NONGSHIM_MATURE_BRAND_ROUNDTRIP | 004370 | Stage2-Local4B-KFood-BrandExportRoundtripNoRevisionBridge | 2024-05-28 | 469000 | 27.72 | -18.44 | 27.72 | -32.41 | counterexample / local 4B |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 003230 삼양식품 — positive C20 export/repeat-sellthrough bridge

Key observed Stock-Web rows:

```text
2024-04-09: o=218000 h=224000 l=215000 c=222500
2024-05-20: o=487500 h=579000 l=487500 c=502000
2024-06-19: o=695000 h=718000 l=651000 c=673000
2024-12-26: o=794000 h=800000 l=755000 c=765000
```

```jsonl
{"row_type":"trigger","trigger_id":"R5L83_C20_003230_20240409_STAGE2_KFOOD_REPEAT_EXPORT","case_id":"C20_R5L83_003230_SAMYANG_KFOOD_REPEAT_EXPORT_BRIDGE","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_EXPORT_REPEAT_SELLTHROUGH_OPM_REVISION","sector":"consumer_brand_distribution","primary_archetype":"K-food global distribution repeat sell-through","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;holdout_validation","trigger_type":"Stage2-Actionable-KFood-ExportRepeatSellthrough","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":222500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public export/channel/repeat-demand/revision proxy available by trigger date; exact URL pending","evidence_source":"source-name-level proxy; exact report/disclosure/export-data URL pending","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","channel_reorder_score"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":160.22,"MFE_90D_pct":222.70,"MFE_180D_pct":259.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.27,"MAE_90D_pct":-4.27,"MAE_180D_pct":-4.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-26","peak_price":800000.0,"drawdown_after_peak_pct":-6.13,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_positive_structural_path","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_low_MAE_high_MFE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_003230_20240409_222500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 12.2 090430 아모레퍼시픽 — beauty rebound false positive

Key observed Stock-Web rows:

```text
2024-05-31: o=191300 h=200500 l=188000 c=194200
2024-07-04: o=150200 h=150700 l=145900 c=148700
2024-10-25: o=123800 h=123800 l=117000 c=117300
2024-12-09: o=101100 h=102600 l=99500 c=99500
```

```jsonl
{"row_type":"trigger","trigger_id":"R5L83_C20_090430_20240531_STAGE2_KBEAUTY_CHINA_REBOUND_FALSE_POSITIVE","case_id":"C20_R5L83_090430_AMORE_CHINA_REBOUND_FALSE_POSITIVE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CHINA_REBOUND_NO_REPEAT_SELLTHROUGH","sector":"consumer_brand_distribution","primary_archetype":"K-beauty brand rebound without repeat global sell-through","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-KBeauty-ChinaReboundNoRepeatSellthrough","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":194200.0,"entry_price_basis":"close","evidence_available_at_that_date":"brand/China-rebound and cosmetics recovery proxy available; repeat global sell-through and OPM/revision bridge not verified","evidence_source":"source-name-level proxy; exact URL pending","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MFE_90D_pct":3.24,"MFE_180D_pct":3.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.87,"MAE_90D_pct":-37.59,"MAE_180D_pct":-48.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500.0,"drawdown_after_peak_pct":-50.37,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_but_full_4B_requires_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_090430_20240531_194200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 12.3 004370 농심 — mature K-food brand local 4B / roundtrip counterexample

Key observed Stock-Web rows:

```text
2024-05-28: o=432000 h=474500 l=427000 c=469000
2024-06-13: o=561000 h=599000 l=544000 c=547000
2024-09-25: o=385000 h=385000 l=376000 c=376500
2024-11-15: o=361500 h=361500 l=317000 c=326000
```

```jsonl
{"row_type":"trigger","trigger_id":"R5L83_C20_004370_20240528_LOCAL4B_MATURE_BRAND_ROUNDTRIP","case_id":"C20_R5L83_004370_NONGSHIM_MATURE_BRAND_ROUNDTRIP","symbol":"004370","company_name":"농심","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"MATURE_K_FOOD_BRAND_EXPORT_SPIKE_WITHOUT_REVISION_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"mature K-food brand export momentum without durable revision bridge","loop_objective":"4B_non_price_requirement_stress_test;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-Local4B-KFood-BrandExportRoundtripNoRevisionBridge","trigger_date":"2024-05-28","entry_date":"2024-05-28","entry_price":469000.0,"entry_price_basis":"close","evidence_available_at_that_date":"K-food brand/export narrative and relative strength proxy available; OPM/revision/reorder acceleration bridge not sufficiently verified","evidence_source":"source-name-level proxy; exact URL pending","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["relative_strength","public_event_or_disclosure","channel_reorder_score"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.72,"MFE_90D_pct":27.72,"MFE_180D_pct":27.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.54,"MAE_90D_pct":-19.83,"MAE_180D_pct":-32.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000.0,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_should_activate_after_price_peak_without_revision_bridge","four_b_evidence_type":["price_only","valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_roundtrip_high_MAE_after_local_MFE","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_004370_20240528_469000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current calibrated profile judgement | It should allow 003230 Stage2/Yellow because export/repeat demand bridge exists; it should block 090430/004370 from Green without repeat sell-through / OPM bridge. |
| actual MFE/MAE alignment | 003230 confirms; 090430 strongly rejects; 004370 shows local MFE but later roundtrip, so needs C20 local 4B watch. |
| Stage2 bonus too much? | Too much for brand/China rebound without repeat sell-through; appropriate for K-food export repeat bridge. |
| Yellow threshold 75 | Reasonable; but C20 needs bridge component rather than raw brand momentum. |
| Green threshold 87 / revision 55 | Keep strict; no C20 Green relaxation. |
| price-only blowoff guard | Existing axis strengthened inside C20. |
| full 4B non-price requirement | Existing axis strengthened: 004370 local peak should be watch, not full 4B, without non-price deterioration. |
| hard 4C routing | No hard 4C; both counterexamples are watch/4B-thesis-risk, not hard thesis break. |

## 14. Stage2 / Yellow / Green Comparison

```text
003230:
  Stage2/Yellow should appear early if export/channel/repeat sell-through + OPM/revision evidence exists.
  Green still requires confirmed revision and multiple public sources.

090430:
  Stage2 should be Watch only because the narrative is broad brand/China rebound.
  Yellow/Green should be blocked unless global repeat sell-through and OPM/revision bridge appear.

004370:
  Stage2 may be watchable, but 4B-local watch should activate when the price path reaches local peak without sustained revision bridge.
```

## 15. 4B Local vs Full-window Timing Audit

```text
090430:
  local peak = 2024-05-31 high 200500
  full observed peak within selected window = 2024-05-31 high 200500
  verdict = price_only_local_peak_but_full_4B_requires_non_price_evidence

004370:
  local/full peak = 2024-06-13 high 599000
  entry = 2024-05-28 close 469000
  later 180D MAE = -32.41%
  verdict = local_4B_watch_should_activate_after_price_peak_without_revision_bridge
```

## 16. 4C Protection Audit

No hard 4C row is proposed. Both negative cases are thesis-break-watch / 4B-local-watch cases, not hard cancellation/accounting/trust breaks.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_confirmation = false
```

## 17. Sector-Specific Rule Candidate

```jsonl
{"row_type":"sector_rule_candidate","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","rule_scope":"sector_specific","candidate_rule":"No broad L5 rule proposed; C20 signal should stay canonical-specific because C18/C19 have different export-channel and inventory-margin mechanics.","proposal_status":"no_new_sector_rule","confidence":"low"}
```

## 18. Canonical-Archetype Rule Candidate

```jsonl
{"row_type":"canonical_archetype_rule_candidate","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","rule_scope":"canonical_archetype_specific","candidate_rule":"C20 Stage2/Yellow requires at least one repeat-sellthrough bridge: export/channel reorder, OPM margin bridge, or EPS/revision confirmation. Brand/China rebound or single price spike remains Watch.","positive_support_count":1,"counterexample_support_count":2,"calibration_usable_count":3,"confidence":"medium","production_change_now":false}
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | avg MFE90 | avg MAE90 | false-positive pressure | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 84.55 | -20.56 | 2/3 | Needs C20 bridge separation |
| P1 sector_specific_candidate_profile | 3 | 84.55 | -20.56 | 2/3 | Too broad for all L5 |
| P2 canonical_C20_bridge_required | 3 | 84.55 | -20.56 | 1/3 after bridge filter | Preferred shadow-only |
| P3 C20_local_4B_watch_guard | 2 risk rows | 15.48 | -28.71 | 2/2 risk rows caught | Guardrail candidate |

## 20. Score-Return Alignment Matrix

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L83_003230_SAMYANG_KFOOD_REPEAT_EXPORT_BRIDGE","trigger_id":"R5L83_C20_003230_20240409_STAGE2_KFOOD_REPEAT_EXPORT","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":16,"revision_score":17,"relative_strength_score":16,"customer_quality_score":13,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":19},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":18,"revision_score":18,"relative_strength_score":16,"customer_quality_score":14,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":12,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":22},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow candidate; Green still URL/revision gated","changed_components":["margin_bridge_score","revision_score","channel_reorder_score"],"component_delta_explanation":"C20 bridge recognizes export/channel/repeat sell-through and margin/revision support.","MFE_90D_pct":222.70,"MAE_90D_pct":-4.27,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L83_090430_AMORE_CHINA_REBOUND_FALSE_POSITIVE","trigger_id":"R5L83_C20_090430_20240531_STAGE2_KBEAUTY_CHINA_REBOUND_FALSE_POSITIVE","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":5,"revision_score":5,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":14,"execution_risk_score":15,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":4},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable false-positive risk","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":4,"revision_score":4,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":18,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":3},"weighted_score_after":61,"stage_label_after":"Stage2-Watch / no Yellow","changed_components":["relative_strength_score","channel_reorder_score","execution_risk_score"],"component_delta_explanation":"Brand/China rebound lacks repeat global sell-through and OPM/revision bridge; risk score rises after price-path stress.","MFE_90D_pct":3.24,"MAE_90D_pct":-37.59,"score_return_alignment_label":"negative_alignment_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L83_004370_NONGSHIM_MATURE_BRAND_ROUNDTRIP","trigger_id":"R5L83_C20_004370_20240528_LOCAL4B_MATURE_BRAND_ROUNDTRIP","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":8,"revision_score":7,"relative_strength_score":17,"customer_quality_score":10,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":14,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable / local peak risk","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":7,"revision_score":6,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":11,"execution_risk_score":16,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":6},"weighted_score_after":64,"stage_label_after":"Stage2-Watch + local 4B watch","changed_components":["execution_risk_score","relative_strength_score","revision_score"],"component_delta_explanation":"Mature brand price spike generated MFE but later roundtrip; without revision/OPM bridge the C20 local 4B watch should activate.","MFE_90D_pct":27.72,"MAE_90D_pct":-19.83,"score_return_alignment_label":"mixed_roundtrip_alignment","current_profile_verdict":"current_profile_4B_too_late"}
```

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_K_BEAUTY_GLOBAL_DISTRIBUTION_REPEAT_SELLTHROUGH_VS_CHINA_REBOUND_PRICE_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C20 still needs exact evidence URL repair and more non-top-symbol K-beauty/K-food counterexamples; this loop improves counterexample balance and local 4B watch evidence."}
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
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C20 brand/China-rebound false positive
  - C20 mature K-food local MFE then 180D roundtrip
  - C20 Stage2 bridge requires repeat sell-through and OPM/revision
new_axis_proposed:
  - C20_repeat_sellthrough_revision_bridge_required_shadow_only
  - C20_local_4B_watch_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C20
  - full_4b_requires_non_price_evidence within C20
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C20 brand/China-rebound false positive","C20 mature K-food local MFE then 180D roundtrip","C20 repeat-sellthrough bridge requirement"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- actual Stock-Web tradable raw OHLC rows
- entry_date / entry_price / MFE / MAE / peak / drawdown
- round-sector-canonical consistency
- novelty against No-Repeat Index top-covered symbols
```

Non-validation scope:

```text
- exact evidence URLs are pending
- non-price evidence is source-name/proxy level
- no production scoring change is made
- no current/live candidate scan is performed
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_repeat_sellthrough_revision_bridge_required,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Brand/China rebound failed while export/repeat sell-through succeeded","Reduces 090430-style false positives while preserving 003230-style positives","R5L83_C20_003230_20240409_STAGE2_KFOOD_REPEAT_EXPORT|R5L83_C20_090430_20240531_STAGE2_KBEAUTY_CHINA_REBOUND_FALSE_POSITIVE",3,3,2,medium,canonical_shadow_only,"not production; evidence URL repair required"
shadow_weight,C20_local_4B_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Mature brand price spike can generate MFE but later roundtrip without revision bridge","Adds local 4B watch for 004370-type price peaks","R5L83_C20_004370_20240528_LOCAL4B_MATURE_BRAND_ROUNDTRIP",3,3,2,medium,canonical_shadow_only,"not production; full 4B still needs non-price evidence"
```

## 25. Machine-Readable Rows

Machine-readable rows are embedded throughout sections 3, 4, 7, 12, 17, 18, 20, 21, 22, and 24.

Required field summary:

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_K_BEAUTY_GLOBAL_DISTRIBUTION_REPEAT_SELLTHROUGH_VS_CHINA_REBOUND_PRICE_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":1,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":84.55,"avg_MAE90_pct":-20.56,"avg_MFE180_pct":96.84,"avg_MAE180_pct":-28.48,"stage2_hit_rate_MFE90_ge_20":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.33,"interpretation":"C20 positives need repeat sell-through + OPM/revision bridge; broad brand/China rebound and mature-brand price spikes need Watch/local 4B treatment."}
{"row_type":"stage_transition_summary","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","trigger_type":"Stage2-Actionable-KFood-ExportRepeatSellthrough","entry_date":"2024-04-09","stage2_to_90D_outcome":"good_stage2","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Repeat export/sell-through bridge aligns with price path."}
{"row_type":"stage_transition_summary","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","trigger_type":"Stage2-FalsePositive-KBeauty-ChinaReboundNoRepeatSellthrough","entry_date":"2024-05-31","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"false_positive_watch","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Brand/China rebound narrative lacked repeat sell-through bridge."}
{"row_type":"stage_transition_summary","round":"R5","loop":"83","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"004370","trigger_type":"Stage2-Local4B-KFood-BrandExportRoundtripNoRevisionBridge","entry_date":"2024-05-28","stage2_to_90D_outcome":"local_MFE_then_watch","stage2_to_180D_outcome":"roundtrip_high_MAE_after_local_peak","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Mature-brand price peak needed local 4B watch when revision bridge did not persist."}
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
- Price-only rows cannot promote Stage2/Stage3.
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
completed_round = R5
completed_loop = 83
next_round = R6
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
```
