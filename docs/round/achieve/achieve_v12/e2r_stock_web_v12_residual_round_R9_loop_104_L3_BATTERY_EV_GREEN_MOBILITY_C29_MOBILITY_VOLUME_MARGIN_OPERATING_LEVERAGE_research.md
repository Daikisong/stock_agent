# E2R v12 Residual Research — R9 / Loop 104 / C29 Mobility Volume-Margin Operating Leverage

```text
schema_version = v12_residual_research
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R9
selected_loop = 104
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE
selected_priority_bucket = Priority 0
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

The static No-Repeat Index still lists C29 as a Priority 0 archetype with only 3 representative rows and 27 more rows needed to reach the 30-row floor. In the conversation-local ledger, C29 has been expanded through loops 100~103, but it remains behind the local floor and still contains one important data-quality weakness: several C29 loop 102 rows used descriptive trigger labels such as `C29_TIRE_MARGIN_REBOUND_LOCAL_4B_REVERSAL` rather than canonical stage labels.

This loop therefore performs a C29 canonical-trigger-label repair and residual rule pass. It reuses already stock-web-verified symbol-year price paths from C29 loop 102, but converts the representative triggers into canonical stage labels while preserving complete 30D/90D/180D MFE/MAE fields. Because the previous row family may be fragile for strict v12 validation, the rows below are treated as calibration-usable repair rows with `batch_reverification_required = true`.

## 2. Price source validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
batch_reverification_required = true
```

The underlying price paths are the same symbol-year stock-web shards previously used in C29 loop 102:

| symbol | name | profile path | price shard path | prior issue repaired here |
|---|---|---|---|---|
| 161390 | 한국타이어앤테크놀로지 | `atlas/symbol_profiles/161/161390.json` | `atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv` | descriptive trigger label → canonical Stage4B |
| 073240 | 금호타이어 | `atlas/symbol_profiles/073/073240.json` | `atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv` | descriptive trigger label → canonical Stage2-Actionable |
| 002350 | 넥센타이어 | `atlas/symbol_profiles/002/002350.json` | `atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv` | descriptive trigger label → canonical Stage2 |
| 011210 | 현대위아 | `atlas/symbol_profiles/011/011210.json` | `atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv` | descriptive trigger label → canonical Stage2 |
| 005850 | 에스엘 | `atlas/symbol_profiles/005/005850.json` | `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv` | descriptive trigger label → canonical Stage3-Yellow |

## 3. Case table

| case | symbol | name | canonical trigger | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | label | residual error |
|---|---|---|---|---|---:|---:|---:|---:|---|---|
| C29-R9L104-01 | 161390 | 한국타이어앤테크놀로지 | Stage4B | 2024-01-25 | 49,450 | +20.5 / -3.5 | +28.0 / -14.8 | +28.0 / -21.9 | mixed_positive | tire margin rebound can be overpromoted after local 4B |
| C29-R9L104-02 | 073240 | 금호타이어 | Stage2-Actionable | 2024-04-11 | 6,490 | +29.0 / -1.4 | +29.0 / -16.6 | +29.0 / -16.6 | mixed_positive | turnaround rally needs margin and balance-sheet bridge |
| C29-R9L104-03 | 002350 | 넥센타이어 | Stage2 | 2024-04-11 | 9,500 | +1.1 / -11.0 | +1.1 / -18.7 | +1.1 / -19.7 | counterexample | sector tire beta does not transfer to laggard without relative strength |
| C29-R9L104-04 | 011210 | 현대위아 | Stage2 | 2024-02-02 | 64,500 | +3.9 / -10.9 | +3.9 / -14.4 | +3.9 / -14.9 | counterexample | parent OEM beta did not create company-level operating leverage |
| C29-R9L104-05 | 005850 | 에스엘 | Stage3-Yellow | 2024-04-29 | 34,150 | +8.1 / -3.7 | +39.5 / -3.7 | +39.5 / -12.8 | positive | lighting mix/ASP bridge allowed durable C29 positive path |

## 4. Interpretation

C29 is not simply “auto sector up.” The mechanism is a gear train: volume must turn mix, mix must turn margin, and margin must finally turn cash or revision. If the first gear spins but the last gear does not move, the model sees noise as torque.

The five repaired rows sharpen three rules.

First, tire-sector rebounds are not interchangeable. 한국타이어앤테크놀로지 and 금호타이어 produced meaningful local MFE, but their 180D MAE was large enough to require a local-4B/watch cap unless margin confirmation continues. 넥센타이어 is the cleaner counterexample: sector-wide tire excitement did not create a durable symbol-level path.

Second, auto parts suppliers need company-level proof. 현대위아 was exposed to OEM and mobility beta, but the price path never turned into sufficient 180D upside. Without volume/mix/margin bridge, C29 should remain Stage2 or watch, not Green.

Third, 에스엘 is the positive anchor. The path had a real MFE90/MFE180 expansion and manageable drawdown, consistent with a stronger mix/ASP/lighting leverage bridge. This is the type of C29 case that may deserve Stage3-Yellow when evidence quality is confirmed.

## 5. Current calibrated profile stress test

| profile component | expected behavior | observed residual |
|---|---|---|
| stage2_required_bridge | prevents theme-only mobility beta | works, but C29 needs explicit volume/mix/margin wording |
| price_only_blowoff_blocks_positive_stage | blocks post-spike tire/parts chase | should be strengthened for local 4B tire rallies |
| full_4b_requires_non_price_evidence | prevents pure price chase | correct, but C29 needs sector-specific relative-strength guard |
| high_MAE_guardrail | penalizes rebound names with large drawdowns | should be applied to supplier/laggard cases even with short MFE |

## 6. JSONL rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_with_batch_reverification","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths"}
{"row_type":"trigger","schema_version":"v12","case_id":"C29_R9L104_161390_20240125_CANONICAL_STAGE4B_REPAIR","trigger_id":"T_C29_R9L104_161390_STAGE4B_20240125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"161390","company_name":"한국타이어앤테크놀로지","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"tire_margin_rebound_local_4b_reversal_guard","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":49450,"mfe_30d_pct":20.5,"mae_30d_pct":-3.5,"mfe_90d_pct":28.0,"mae_90d_pct":-14.8,"mfe_180d_pct":28.0,"mae_180d_pct":-21.9,"peak_180d_date":"2024-02-21","peak_180d_price":58400,"outcome_label":"mixed_positive_then_high_MAE","positive_or_counterexample":"mixed_positive","current_profile_error_type":"tire_margin_rebound_can_be_overpromoted_after_local_4b","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv","profile_path":"atlas/symbol_profiles/161/161390.json","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","same_entry_group_id":"C29|161390|Stage4B|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"schema repair from descriptive prior trigger label into canonical Stage4B","independent_evidence_weight":0.72,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C29_R9L104_073240_20240411_CANONICAL_STAGE2A_REPAIR","trigger_id":"T_C29_R9L104_073240_STAGE2A_20240411","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"073240","company_name":"금호타이어","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"tire_turnaround_spike_margin_bridge_test","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":6490,"mfe_30d_pct":29.0,"mae_30d_pct":-1.4,"mfe_90d_pct":29.0,"mae_90d_pct":-16.6,"mfe_180d_pct":29.0,"mae_180d_pct":-16.6,"peak_180d_date":"2024-05-03","peak_180d_price":8360,"outcome_label":"mixed_positive_local_4B","positive_or_counterexample":"mixed_positive","current_profile_error_type":"turnaround_rebound_requires_margin_and_balance_sheet_bridge","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv","profile_path":"atlas/symbol_profiles/073/073240.json","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","same_entry_group_id":"C29|073240|Stage2-Actionable|2024-04-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"schema repair from descriptive prior trigger label into canonical Stage2-Actionable","independent_evidence_weight":0.72,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C29_R9L104_002350_20240411_CANONICAL_STAGE2_REPAIR","trigger_id":"T_C29_R9L104_002350_STAGE2_20240411","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"002350","company_name":"넥센타이어","market":"KOSPI","trigger_type":"Stage2","trigger_family":"tire_beta_without_relative_margin_confirmation","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":9500,"mfe_30d_pct":1.1,"mae_30d_pct":-11.0,"mfe_90d_pct":1.1,"mae_90d_pct":-18.7,"mfe_180d_pct":1.1,"mae_180d_pct":-19.7,"peak_180d_date":"2024-04-12","peak_180d_price":9550,"outcome_label":"counterexample","positive_or_counterexample":"counterexample","current_profile_error_type":"sector_beta_generalized_to_laggard_symbol","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv","profile_path":"atlas/symbol_profiles/002/002350.json","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","same_entry_group_id":"C29|002350|Stage2|2024-04-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"schema repair from descriptive prior trigger label into canonical Stage2","independent_evidence_weight":0.70,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C29_R9L104_011210_20240202_CANONICAL_STAGE2_REPAIR","trigger_id":"T_C29_R9L104_011210_STAGE2_20240202","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"011210","company_name":"현대위아","market":"KOSPI","trigger_type":"Stage2","trigger_family":"parts_volume_bridge_weak_opm_confirmation","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":64500,"mfe_30d_pct":3.9,"mae_30d_pct":-10.9,"mfe_90d_pct":3.9,"mae_90d_pct":-14.4,"mfe_180d_pct":3.9,"mae_180d_pct":-14.9,"peak_180d_date":"2024-02-05","peak_180d_price":67000,"outcome_label":"counterexample","positive_or_counterexample":"counterexample","current_profile_error_type":"parent_OEM_beta_not_company_level_operating_leverage","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv","profile_path":"atlas/symbol_profiles/011/011210.json","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","same_entry_group_id":"C29|011210|Stage2|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"schema repair from descriptive prior trigger label into canonical Stage2","independent_evidence_weight":0.70,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C29_R9L104_005850_20240429_CANONICAL_STAGE3Y_REPAIR","trigger_id":"T_C29_R9L104_005850_STAGE3Y_20240429","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","company_name":"에스엘","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"auto_lighting_mix_ASP_operating_leverage","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":34150,"mfe_30d_pct":8.1,"mae_30d_pct":-3.7,"mfe_90d_pct":39.5,"mae_90d_pct":-3.7,"mfe_180d_pct":39.5,"mae_180d_pct":-12.8,"peak_180d_date":"2024-06-17","peak_180d_price":47650,"outcome_label":"positive_with_post_peak_guard","positive_or_counterexample":"positive","current_profile_error_type":"none_if_mix_margin_bridge_confirmed","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv","profile_path":"atlas/symbol_profiles/005/005850.json","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","same_entry_group_id":"C29|005850|Stage3-Yellow|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"schema repair from descriptive prior trigger label into canonical Stage3-Yellow","independent_evidence_weight":0.78,"batch_reverification_required":true}
{"row_type":"aggregate_metrics","schema_version":"v12","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_CANONICAL_TRIGGER_LABEL_REPAIR_TIRE_AND_PARTS_VOLUME_MIX_MARGIN_BRIDGE","new_independent_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":0,"same_symbol_new_trigger_family_count":5,"same_archetype_new_trigger_family_count":5,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":5,"avg_mfe_30d_pct":12.52,"avg_mae_30d_pct":-6.9,"avg_mfe_90d_pct":20.3,"avg_mae_90d_pct":-13.64,"avg_mfe_180d_pct":20.3,"avg_mae_180d_pct":-17.18,"coverage_gap_static_rows_before":3,"coverage_gap_static_rows_after_if_accepted":8,"coverage_gap_conversation_local_before_approx":17,"coverage_gap_conversation_local_after_if_accepted_approx":22,"still_need_to_30_approx":8,"loop_contribution_label":"data_quality_repair_plus_canonical_archetype_rule_candidate"}
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C29_CANONICAL_STAGE_LABEL_REPAIR_FOR_VALIDATION","C29_SYMBOL_LEVEL_RELATIVE_STRENGTH_REQUIRED","C29_TIRE_SECTOR_BETA_LAGGARD_GUARD","C29_PARTS_SUPPLIER_PARENT_OEM_BETA_CAP","C29_AUTO_LIGHTING_MIX_ASP_POSITIVE_BRIDGE_ALLOWED","C29_LOCAL_4B_POST_PEAK_HIGH_MAE_GUARD"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":null,"confidence":"medium_low_until_batch_reverification","notes":"This loop repairs prior C29 descriptive trigger labels into canonical stage labels while preserving complete MFE/MAE fields."}
{"row_type":"residual_contribution_summary","completed_round":"R9","completed_loop":104,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger","selected_priority_bucket":"Priority 0","round_schedule_status":"coverage_index_selected","round_sector_consistency":"pass","next_recommended_archetypes":["C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fifth_pass_to_30","C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_second_pass_to_30","C18_CONSUMER_EXPORT_CHANNEL_REORDER_final_3_rows_to_30","C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]}
```

## 7. Deferred Coding Agent Handoff Prompt

Do not apply this MD as a direct production patch. In the later batch implementation session, ingest the JSONL rows only after re-opening the exact stock-web shard paths listed above and recomputing 30D/90D/180D MFE/MAE. The main implementation task is not a new score weight by itself; it is a data-quality repair and canonical-stage-label normalization for C29 rows that previously used descriptive `trigger_type` values. If the recomputed rows match, test the C29-specific rules: symbol-level relative strength, tire-sector laggard guard, parent-OEM beta cap, lighting mix/ASP positive bridge, and local-4B high-MAE cap.
