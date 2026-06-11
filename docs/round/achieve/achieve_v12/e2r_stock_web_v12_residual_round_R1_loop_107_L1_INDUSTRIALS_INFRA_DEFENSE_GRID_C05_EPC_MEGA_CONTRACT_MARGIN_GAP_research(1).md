---
research_mode: stock_web_v12_sector_archetype_residual_calibration
selected_round: R1
selected_loop: 107
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
upstream_source: FinanceData/marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
new_independent_case_count: 9
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_symbol_new_trigger_family_count: 4
calibration_usable_case_count: 9
calibration_usable_trigger_count: 9
positive_case_count: 3
mixed_positive_count: 1
counterexample_count: 5
local_4b_watch_count: 3
current_profile_error_count: 9
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
---
# stock-web v12 residual calibration — R1 / C05_EPC_MEGA_CONTRACT_MARGIN_GAP / loop 107

## 0. Execution state

This standalone Markdown follows the v12 historical calibration runner. It is not a live scan, not an investment recommendation, not an auto-trading instruction, and not a stock_agent code patch. The file is designed as a later batch-ingest input.

```text
completed_round = R1
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 1. Why C05 was selected

The static No-Repeat Index still places `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` in Priority 0 with 13 representative rows and 17 rows still needed to reach the 30-row floor. Conversation-local C05 had only about 8 usable rows after loops 101 and 106. This pass adds 9 usable canonical-stage rows, moving local C05 coverage from roughly 8 to roughly 17.

The key research question is not whether a contractor has an order headline. C05 asks whether the order becomes gross margin, OPM, working-capital release, and FCF. EPC is a pipeline: backlog enters at one end, but cost overruns, claims, delayed acceptance, and cash conversion leaks can drain it before it reaches shareholders.

## 2. Price source and validation caveat

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Fresh individual raw shard calls were intermittently unstable in this session. Therefore this C05 second pass reuses stock-web price paths already verified in local C05/C30 v12 files, then re-maps them into the C05 canonical lens only when the case is EPC/order/margin relevant. Every reused row is marked `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`.

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_or_cross_canonical_shard_paths
cross_canonical_price_row_reuse_count = 9
batch_reverification_required = true
```

## 3. Novelty and no-repeat gate

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This pass avoids exact C05 duplicates from loops 101 and 106. Some symbols overlap with previous C05/C30 research, but the `entry_date`, `trigger_type`, or C05 trigger family is different. Cross-canonical reuse from C30 is deliberate: C30 identifies PF/balance-sheet repair; C05 asks whether the same contractor price path should be scored as an EPC/order/margin bridge or capped as a contractor/PF contaminant.

## 4. Representative trigger table

| # | ticker | name | entry_date | trigger | role | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | result |
|---:|---|---|---|---|---|---:|---:|---:|---|
| 1 | 294870 | HDC현대산업개발 | 2024-01-26 | Stage2-Actionable | housing_developer_repair_to_EPC_margin_bridge_stress | +18.37 / -2.11 | +18.37 / -8.33 | +60.87 / -8.33 | positive |
| 2 | 006360 | GS건설 | 2024-04-03 | Stage2-Actionable | cost_provision_repair_to_order_margin_bridge | +5.89 / -4.86 | +30.52 / -5.31 | +39.16 / -5.31 | positive_with_repair_lag |
| 3 | 047040 | 대우건설 | 2024-04-03 | Stage2 | generic_builder_rebound_without_project_margin_bridge | +1.58 / -2.50 | +4.07 / -7.49 | +6.44 / -14.32 | counterexample |
| 4 | 294870 | HDC현대산업개발 | 2024-08-26 | Stage4B | post_peak_contractor_repair_local_4b_without_nonprice_bridge | +5.62 / -15.54 | +5.62 / -24.16 | +8.99 / -24.16 | local_4b_counterexample |
| 5 | 294870 | HDC현대산업개발 | 2024-04-24 | Stage2-Actionable | spring_repair_followthrough_margin_bridge_candidate | +3.57 / -2.94 | +22.80 / -4.70 | +59.59 / -4.70 | positive_followthrough |
| 6 | 047040 | 대우건설 | 2024-07-17 | Stage4B | post_peak_broad_builder_price_confirmation_without_cash_bridge | +0.00 / -6.20 | +0.00 / -10.45 | +0.00 / -14.47 | counterexample_full_4b_block |
| 7 | 375500 | DL이앤씨 | 2024-06-13 | Stage4B | low_pbr_contractor_local_peak_without_margin_bridge | +0.00 / -12.66 | +0.00 / -26.96 | +0.00 / -26.96 | counterexample_high_mae |
| 8 | 013580 | 계룡건설 | 2024-04-29 | Stage2-Actionable | regional_builder_contract_repair_stage2_not_green | +2.19 / -5.40 | +13.07 / -5.40 | +13.07 / -13.21 | mixed_positive_stage2_only |
| 9 | 004960 | 한신공영 | 2024-04-29 | Stage2 | small_builder_low_pbr_without_epc_margin_bridge | +2.29 / -8.70 | +2.29 / -15.88 | +2.29 / -19.85 | counterexample_small_builder_drawdown |

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_294870_20240126","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Actionable","trigger_family":"housing_developer_repair_to_EPC_margin_bridge_stress","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":17530,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","MFE_30D_pct":18.37,"MAE_30D_pct":-2.11,"MFE_90D_pct":18.37,"MAE_90D_pct":-8.33,"MFE_180D_pct":60.87,"MAE_180D_pct":-8.33,"peak_180D_date":"2024-08-26","peak_180D_price":28200,"trigger_outcome_label":"positive","current_profile_verdict":"C05 can admit early contractor repair only when project margin and cash conversion bridge are visible; otherwise reroute to C30.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2-Actionable|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_006360_20240403","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"006360","name":"GS건설","trigger_type":"Stage2-Actionable","trigger_family":"cost_provision_repair_to_order_margin_bridge","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":15630,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","MFE_30D_pct":5.89,"MAE_30D_pct":-4.86,"MFE_90D_pct":30.52,"MAE_90D_pct":-5.31,"MFE_180D_pct":39.16,"MAE_180D_pct":-5.31,"peak_180D_date":"2024-08-27","peak_180D_price":21750,"trigger_outcome_label":"positive_with_repair_lag","current_profile_verdict":"Delayed repair worked only because cost/provision/PF stress had begun to fade; full Green still needs margin and cash bridge.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_047040_20240403","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"047040","name":"대우건설","trigger_type":"Stage2","trigger_family":"generic_builder_rebound_without_project_margin_bridge","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":3805,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","MFE_30D_pct":1.58,"MAE_30D_pct":-2.5,"MFE_90D_pct":4.07,"MAE_90D_pct":-7.49,"MFE_180D_pct":6.44,"MAE_180D_pct":-14.32,"peak_180D_date":"2024-07-12","peak_180D_price":4050,"trigger_outcome_label":"counterexample","current_profile_verdict":"Generic construction recovery label is not C05 unless order backlog turns into project margin and working-capital conversion.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_294870_20240826","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","trigger_family":"post_peak_contractor_repair_local_4b_without_nonprice_bridge","trigger_date":"2024-08-26","entry_date":"2024-08-26","entry_price":26700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","MFE_30D_pct":5.62,"MAE_30D_pct":-15.54,"MFE_90D_pct":5.62,"MAE_90D_pct":-24.16,"MFE_180D_pct":8.99,"MAE_180D_pct":-24.16,"peak_180D_date":"2024-08-26","peak_180D_price":28200,"trigger_outcome_label":"local_4b_counterexample","current_profile_verdict":"After the repair move, price confirmation alone is a trap; C05 full 4B requires fresh non-price cost/margin bridge.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage4B|2024-08-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_294870_20240424","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Actionable","trigger_family":"spring_repair_followthrough_margin_bridge_candidate","trigger_date":"2024-04-23","entry_date":"2024-04-24","entry_price":17670,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","MFE_30D_pct":3.57,"MAE_30D_pct":-2.94,"MFE_90D_pct":22.8,"MAE_90D_pct":-4.7,"MFE_180D_pct":59.59,"MAE_180D_pct":-4.7,"peak_180D_date":"2024-08-26","peak_180D_price":28200,"trigger_outcome_label":"positive_followthrough","current_profile_verdict":"A clean early repair window can become C05 positive only if orderbook/PF relief is joined by cost and margin follow-through.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2-Actionable|2024-04-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_047040_20240717","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"047040","name":"대우건설","trigger_type":"Stage4B","trigger_family":"post_peak_broad_builder_price_confirmation_without_cash_bridge","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":4355,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","MFE_30D_pct":0.0,"MAE_30D_pct":-6.2,"MFE_90D_pct":0.0,"MAE_90D_pct":-10.45,"MFE_180D_pct":0.0,"MAE_180D_pct":-14.47,"peak_180D_date":"2024-07-17","peak_180D_price":4355,"trigger_outcome_label":"counterexample_full_4b_block","current_profile_verdict":"Local peak with no fresh project margin evidence should remain local 4B watch, not a C05 promotion.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4B|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_375500_20240613","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage4B","trigger_family":"low_pbr_contractor_local_peak_without_margin_bridge","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":39500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","MFE_30D_pct":0.0,"MAE_30D_pct":-12.66,"MFE_90D_pct":0.0,"MAE_90D_pct":-26.96,"MFE_180D_pct":0.0,"MAE_180D_pct":-26.96,"peak_180D_date":"2024-06-13","peak_180D_price":39500,"trigger_outcome_label":"counterexample_high_mae","current_profile_verdict":"Low-PBR contractor rally with no margin/working-capital bridge is a C05 false positive and high-MAE guard row.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-06-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_013580_20240429","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"013580","name":"계룡건설","trigger_type":"Stage2-Actionable","trigger_family":"regional_builder_contract_repair_stage2_not_green","trigger_date":"2024-04-26","entry_date":"2024-04-29","entry_price":13700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv","profile_path":"atlas/symbol_profiles/013/013580.json","MFE_30D_pct":2.19,"MAE_30D_pct":-5.4,"MFE_90D_pct":13.07,"MAE_90D_pct":-5.4,"MFE_180D_pct":13.07,"MAE_180D_pct":-13.21,"peak_180D_date":"2024-07-17","peak_180D_price":15490,"trigger_outcome_label":"mixed_positive_stage2_only","current_profile_verdict":"Regional builder repair deserves Stage2 monitoring, but Green needs explicit backlog-to-margin and cash bridge.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|013580|Stage2-Actionable|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger_row_representative","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","research_file":"e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","case_id":"C05_R1L107_004960_20240429","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE","symbol":"004960","name":"한신공영","trigger_type":"Stage2","trigger_family":"small_builder_low_pbr_without_epc_margin_bridge","trigger_date":"2024-04-26","entry_date":"2024-04-29","entry_price":6550,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv","profile_path":"atlas/symbol_profiles/004/004960.json","MFE_30D_pct":2.29,"MAE_30D_pct":-8.7,"MFE_90D_pct":2.29,"MAE_90D_pct":-15.88,"MFE_180D_pct":2.29,"MAE_180D_pct":-19.85,"peak_180D_date":"2024-05-16","peak_180D_price":6700,"trigger_outcome_label":"counterexample_small_builder_drawdown","current_profile_verdict":"Cheap small builder/PF relief is not C05 unless orderbook quality, cost containment and working-capital repair are visible.","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|004960|Stage2|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_C30_or_prior_C05_price_path_reused_due_current_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
```

## 6. Score simulation JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C05_R1L107_294870_20240126","symbol":"294870","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":14,"working_capital_cash_bridge":12,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-4,"evidence_quality_penalty":-5},"simulated_total_before_shadow":76,"simulated_stage_before_shadow":"Stage3-Yellow","shadow_rule_delta":3,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_006360_20240403","symbol":"006360","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":14,"working_capital_cash_bridge":12,"price_path_confirmation":8,"cost_overrun_or_high_MAE_penalty":-4,"evidence_quality_penalty":-5},"simulated_total_before_shadow":76,"simulated_stage_before_shadow":"Stage3-Yellow","shadow_rule_delta":3,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_047040_20240403","symbol":"047040","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":3,"working_capital_cash_bridge":1,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-14,"evidence_quality_penalty":-5},"simulated_total_before_shadow":55,"simulated_stage_before_shadow":"Stage2","shadow_rule_delta":-9,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_294870_20240826","symbol":"294870","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":3,"working_capital_cash_bridge":1,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-14,"evidence_quality_penalty":-5},"simulated_total_before_shadow":59,"simulated_stage_before_shadow":"Stage2","shadow_rule_delta":-9,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_294870_20240424","symbol":"294870","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":14,"working_capital_cash_bridge":12,"price_path_confirmation":8,"cost_overrun_or_high_MAE_penalty":-4,"evidence_quality_penalty":-5},"simulated_total_before_shadow":76,"simulated_stage_before_shadow":"Stage3-Yellow","shadow_rule_delta":3,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_047040_20240717","symbol":"047040","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":3,"working_capital_cash_bridge":1,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-14,"evidence_quality_penalty":-5},"simulated_total_before_shadow":59,"simulated_stage_before_shadow":"Stage2","shadow_rule_delta":-9,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_375500_20240613","symbol":"375500","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":3,"working_capital_cash_bridge":1,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-14,"evidence_quality_penalty":-5},"simulated_total_before_shadow":59,"simulated_stage_before_shadow":"Stage2","shadow_rule_delta":-9,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_013580_20240429","symbol":"013580","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":7,"working_capital_cash_bridge":5,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-8,"evidence_quality_penalty":-5},"simulated_total_before_shadow":65,"simulated_stage_before_shadow":"Stage2-Actionable","shadow_rule_delta":-5,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
{"row_type":"score_simulation","case_id":"C05_R1L107_004960_20240429","symbol":"004960","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"order_or_contract_label":14,"project_margin_bridge":3,"working_capital_cash_bridge":1,"price_path_confirmation":4,"cost_overrun_or_high_MAE_penalty":-14,"evidence_quality_penalty":-5},"simulated_total_before_shadow":55,"simulated_stage_before_shadow":"Stage2","shadow_rule_delta":-9,"proposed_shadow_rule":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED"}
```

## 7. Aggregate and residual contribution

```json
{
  "row_type": "aggregate_metrics",
  "selected_round": "R1",
  "selected_loop": 107,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "C05_EPC_CONTRACT_MARGIN_GAP_SECOND_PASS_CROSS_C30_REPAIR_REROUTE",
  "new_independent_case_count": 9,
  "same_archetype_new_symbol_count": 5,
  "same_symbol_new_trigger_family_count": 4,
  "calibration_usable_case_count": 9,
  "calibration_usable_trigger_count": 9,
  "positive_case_count": 3,
  "mixed_positive_count": 1,
  "counterexample_count": 5,
  "local_4b_watch_count": 3,
  "current_profile_error_count": 9,
  "avg_MFE_30D_pct": 4.39,
  "avg_MAE_30D_pct": -6.77,
  "avg_MFE_90D_pct": 10.75,
  "avg_MAE_90D_pct": -12.08,
  "avg_MFE_180D_pct": 21.16,
  "avg_MAE_180D_pct": -14.59,
  "auto_selected_coverage_gap_static_index": "C05 rows 13 -> 22 if accepted; still Priority 0, need 8 to 30 by static index",
  "auto_selected_coverage_gap_conversation_local": "C05 approx rows 8 -> 17 if accepted; still need about 13 to reach local 30-row floor",
  "loop_contribution_label": "canonical_archetype_rule_candidate_cross_canonical_reroute"
}
```

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED","proposal":"C05 Stage3 requires order/backlog headline plus project gross margin or OPM bridge, cost-overrun containment, working-capital/cash conversion, and delivery schedule visibility.","direction":"tighten_stage3","production_scoring_changed":false}
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_CROSS_CANONICAL_C30_REROUTE_GUARD","proposal":"If a contractor move is mainly PF/balance-sheet or low-PBR housing relief, reroute to C30 unless EPC project margin and cash bridge are explicit.","direction":"reroute_guard","production_scoring_changed":false}
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_POST_PEAK_LOCAL_4B_CAP","proposal":"Post-peak contractor/EPC price confirmation without fresh non-price bridge remains local 4B watch and must not become full 4B or Stage3.","direction":"tighten_4b_to_stage3","production_scoring_changed":false}
```

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate_cross_canonical_reroute
do_not_propose_new_weight_delta = false
new_axis_proposed = C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED | C05_CROSS_CANONICAL_C30_REROUTE_GUARD | C05_POST_PEAK_LOCAL_4B_CAP | C05_COST_OVERRUN_PROVISION_VISIBILITY_REQUIRED
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the batch implementation agent for E2R 2.1 calibration.

Do not apply this Markdown directly as a production patch. Use it as one v12 residual research input.

Tasks:
1. Parse only trigger rows with calibration_usable=true and complete 30D/90D/180D MFE/MAE fields.
2. Re-open stock-web shards for every row with batch_reverification_required=true.
3. Check duplicate keys using canonical_archetype_id + symbol + trigger_type + entry_date.
4. Compare this C05 file against C01, C30, and C31 rows to separate order backlog, EPC margin gap, PF balance-sheet repair, and policy subsidy contamination.
5. If multiple independent rows agree, stage a shadow rule candidate only:
   - C05_PROJECT_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIRED
   - C05_CROSS_CANONICAL_C30_REROUTE_GUARD
   - C05_POST_PEAK_LOCAL_4B_CAP
6. Do not change production scoring from this file alone.
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP_third_pass_to_30, C13_BATTERY_JV_UTILIZATION_AMPC_IRA_second_pass_to_30, C24_BIO_TRIAL_DATA_EVENT_RISK_third_pass_to_30, C02_POWER_GRID_DATACENTER_CAPEX_static_gap_repair, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_url_repair, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_url_repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
