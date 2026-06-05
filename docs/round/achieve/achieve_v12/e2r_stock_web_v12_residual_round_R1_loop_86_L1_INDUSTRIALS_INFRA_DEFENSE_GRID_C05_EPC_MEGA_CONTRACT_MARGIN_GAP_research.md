# E2R Stock-Web v12 Residual Research — R1 Loop 86 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 86
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_SELECTIVE_ORDER_MARGIN_RECOVERY_BRIDGE_VS_CONSTRUCTION_CONTRACT_THEME_SPIKE
sector: industrials / EPC / engineering / mega contract / margin gap
output_file: e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 85`.

```text
scheduled_round = R1
scheduled_loop = 86
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

R1 is restricted to L1 industrials / infra / defense / grid.  
C05 is selected because it remains thinner and less balanced than the larger L1 buckets:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows = 10
symbols = 9
good/bad Stage2 = 3/4
4B/4C = 0/0
top-covered = 053690, 002150, 011560, 023350, 023960, 054930
```

This loop avoids those top-covered symbols and also avoids the immediately recent R1 loop85 C04 nuclear path.  
The goal is to separate **EPC / engineering backlog plus margin recovery bridge** from **construction or EPC headline strength with no margin/cash-conversion bridge**.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"028050","company_name":"삼성E&A","profile_path":"atlas/symbol_profiles/028/028050.json","first_date":"1997-01-03","last_date":"2026-02-20","trading_day_count":7265,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1997-08-22","1999-01-13","1999-05-26","1999-09-29","2016-02-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024/2025 forward window used here. Name changed from 삼성엔지니어링 to 삼성E&A on 2024-04-08 without a 2024 price discontinuity candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_2025_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"000720","company_name":"현대건설","profile_path":"atlas/symbol_profiles/000/000720.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7740,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["1998-05-23","1998-11-19","1999-03-05","2001-07-06","2001-07-12","2004-01-13","2004-04-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"047040","company_name":"대우건설","profile_path":"atlas/symbol_profiles/047/047040.json","first_date":"2001-03-23","last_date":"2026-02-20","trading_day_count":6127,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2001-07-13","2003-11-18","2011-01-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028050","trigger_type":"Stage2-Actionable-EPCSelectiveOrderMarginRecoveryBridge-Positive","entry_date":"2024-06-11","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"000720","trigger_type":"Stage2-FalsePositive-LargeConstructionContractTheme-NoFreshMarginCashBridge","entry_date":"2024-04-29","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"047040","trigger_type":"Stage2-FalsePositive-ConstructionMegaContractTheme-NoMarginConversionBridge","entry_date":"2024-07-15","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C05 is not simply “large contract headline.”  
For EPC and engineering names, a megacontract can be a blessing or a burden. E2R should ask whether the backlog is selective, whether risk is priced, whether cost overrun risk is controlled, and whether the order converts into margin, cash, and revision quality. A contract headline without this bridge is like a crane lifting fog: large shape, little load.

Residual question:

```text
Can C05 distinguish:
1. EPC selective-order / margin-recovery bridge after a clean reset,
2. large construction-contract theme with no fresh margin/cash-conversion bridge,
3. construction megacontract or overseas backlog theme that produces a bounce but decays without margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C05_R1L86_028050_SAMSUNGEA_EPC_SELECTIVE_ORDER_MARGIN_RECOVERY","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_SELECTIVE_ORDER_MARGIN_RECOVERY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-EPCSelectiveOrderMarginRecoveryBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_90D_MAE_later_180D_drawdown","current_profile_verdict":"current_profile_correct_if_margin_recovery_bridge_required","price_source":"Songdaiki/stock-web","notes":"After a weak H1 path, the June entry showed selective EPC/margin-recovery price confirmation. Later 180D drawdown means Green still requires exact order mix, margin and cash evidence."}
{"row_type":"case","case_id":"C05_R1L86_000720_HYUNDAICONST_CONTRACT_THEME_NO_MARGIN_CASH","symbol":"000720","company_name":"현대건설","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGE_CONSTRUCTION_CONTRACT_THEME_WITHOUT_FRESH_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LargeConstructionContractTheme-NoFreshMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_contract_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Construction/EPC contract theme had almost no MFE and later deep MAE when margin and cash-conversion bridge failed to appear."}
{"row_type":"case","case_id":"C05_R1L86_047040_DAEWOO_EPC_THEME_NO_MARGIN_CONVERSION","symbol":"047040","company_name":"대우건설","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_MEGA_CONTRACT_THEME_WITHOUT_MARGIN_CONVERSION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ConstructionMegaContractTheme-NoMarginConversionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_bounce_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_backlog_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"A July construction/backlog theme spike produced a tradable bounce, but the forward path decayed when margin conversion and financing confidence did not confirm."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 028050 삼성E&A — EPC selective-order / margin-recovery bridge positive

Entry row: `2024-06-11 c=22300`.  
Observed path: early low `2024-06-18 l=21600`, rebound high `2024-07-30 h=29300`, then later 180D low `2025-02-28 l=16380`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L86_C05_028050_20240611_STAGE2_EPC_MARGIN_RECOVERY","case_id":"C05_R1L86_028050_SAMSUNGEA_EPC_SELECTIVE_ORDER_MARGIN_RECOVERY","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_SELECTIVE_ORDER_MARGIN_RECOVERY_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-EPCSelectiveOrderMarginRecoveryBridge-Positive","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":22300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EPC_selective_order_margin_recovery_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EPC selective-order and margin-recovery bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["selective_order_bridge_proxy","margin_recovery_proxy","backlog_quality_proxy","relative_strength_turn"],"stage3_evidence_fields":["order_mix_source_url_pending","cash_conversion_pending","revision_quality_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.92,"MFE_90D_pct":31.39,"MFE_180D_pct":31.39,"MAE_30D_pct":-3.14,"MAE_90D_pct":-5.38,"MAE_180D_pct":-26.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300.0,"max_drawdown_low_date":"2025-02-28","max_drawdown_low":16380.0,"drawdown_after_peak_pct":-44.10,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_90D_MAE_later_180D_drawdown","current_profile_verdict":"current_profile_correct_if_margin_recovery_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_2025_window","same_entry_group_id":"028050_2024-06-11_22300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 can allow Stage2/Yellow when EPC strength is tied to selective-order and margin-recovery bridge. Green still requires exact order mix, cash conversion and revision-quality evidence."}
```

### 6.2 000720 현대건설 — large construction/EPC contract theme without fresh margin/cash bridge

Entry row: `2024-04-29 c=35400`.  
Observed path: local high `2024-05-09 h=36000`, then lows `2024-06-27 l=31450` and `2024-12-09 l=24100`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L86_C05_000720_20240429_STAGE2_FALSE_POSITIVE_CONTRACT_THEME","case_id":"C05_R1L86_000720_HYUNDAICONST_CONTRACT_THEME_NO_MARGIN_CASH","symbol":"000720","company_name":"현대건설","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGE_CONSTRUCTION_CONTRACT_THEME_WITHOUT_FRESH_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LargeConstructionContractTheme-NoFreshMarginCashBridge","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":35400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_large_construction_contract_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction/EPC contract theme treated as insufficient without fresh margin, cost-control, cash-conversion and backlog-quality bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["large_contract_theme","relative_strength_rebound"],"stage3_evidence_fields":["margin_bridge_missing","cash_conversion_missing","cost_overrun_risk_unresolved","backlog_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.69,"MFE_90D_pct":1.69,"MFE_180D_pct":1.69,"MAE_30D_pct":-8.33,"MAE_90D_pct":-11.16,"MAE_180D_pct":-31.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":36000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":24100.0,"drawdown_after_peak_pct":-33.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"contract_theme_peak_without_fresh_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_contract_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000720_2024-04-29_35400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not upgrade large-contract theme when margin and cash-conversion bridge is missing. Near-zero MFE and deep later MAE argue for Watch/4B-risk."}
```

### 6.3 047040 대우건설 — construction megacontract/backlog theme without margin conversion bridge

Entry row: `2024-07-15 c=4260`.  
Observed path: spike high `2024-07-18 h=4965`, then lows `2024-10-31 l=3525` and `2024-12-30 l=3105`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L86_C05_047040_20240715_STAGE2_FALSE_POSITIVE_MEGA_CONTRACT_THEME","case_id":"C05_R1L86_047040_DAEWOO_EPC_THEME_NO_MARGIN_CONVERSION","symbol":"047040","company_name":"대우건설","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_MEGA_CONTRACT_THEME_WITHOUT_MARGIN_CONVERSION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ConstructionMegaContractTheme-NoMarginConversionBridge","trigger_date":"2024-07-15","entry_date":"2024-07-15","entry_price":4260.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_construction_megacontract_backlog_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction megacontract/backlog theme treated as insufficient without margin conversion, financing confidence and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["megacontract_theme","backlog_theme_relative_strength"],"stage3_evidence_fields":["margin_conversion_missing","cash_conversion_missing","financing_confidence_missing","cost_overrun_risk_unresolved"],"stage4b_evidence_fields":["price_only_local_peak","margin_conversion_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.55,"MFE_90D_pct":16.55,"MFE_180D_pct":16.55,"MAE_30D_pct":-8.22,"MAE_90D_pct":-17.25,"MAE_180D_pct":-27.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":4965.0,"max_drawdown_low_date":"2024-12-30","max_drawdown_low":3105.0,"drawdown_after_peak_pct":-37.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"initial_backlog_bounce_without_margin_conversion_should_remain_4B_watch","four_b_evidence_type":["price_only","margin_conversion_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_bounce_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_backlog_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"047040_2024-07-15_4260","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should treat an initial construction/backlog bounce as Watch unless margin conversion and cash bridge follow. The later drawdown shows why price-only backlog themes need 4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L86_028050_SAMSUNGEA_EPC_SELECTIVE_ORDER_MARGIN_RECOVERY","trigger_id":"R1L86_C05_028050_20240611_STAGE2_EPC_MARGIN_RECOVERY","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C05 requires margin and cash-conversion bridge rather than contract headline alone","raw_component_scores_before":{"order_backlog_quality_score":13,"selective_order_score":12,"margin_recovery_score":12,"cash_conversion_score":7,"cost_overrun_risk_score":-5,"customer_project_quality":9,"relative_strength_score":11,"valuation_repricing_score":8,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"order_backlog_quality_score":16,"selective_order_score":15,"margin_recovery_score":15,"cash_conversion_score":9,"cost_overrun_risk_score":-4,"customer_project_quality":11,"relative_strength_score":12,"valuation_repricing_score":9,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Selective-order/margin bridge and 90D MFE support Yellow-watch; later 180D drawdown blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L86_000720_HYUNDAICONST_CONTRACT_THEME_NO_MARGIN_CASH","trigger_id":"R1L86_C05_000720_20240429_STAGE2_FALSE_POSITIVE_CONTRACT_THEME","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"large contract theme without margin/cash bridge should be blocked","raw_component_scores_before":{"order_backlog_quality_score":7,"selective_order_score":3,"margin_recovery_score":1,"cash_conversion_score":1,"cost_overrun_risk_score":-12,"customer_project_quality":5,"relative_strength_score":8,"valuation_repricing_score":4,"information_confidence":3},"weighted_score_before":20,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_backlog_quality_score":3,"selective_order_score":0,"margin_recovery_score":0,"cash_conversion_score":0,"cost_overrun_risk_score":-18,"customer_project_quality":2,"relative_strength_score":3,"valuation_repricing_score":1,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep 180D MAE convert contract theme into missing margin/cash bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L86_047040_DAEWOO_EPC_THEME_NO_MARGIN_CONVERSION","trigger_id":"R1L86_C05_047040_20240715_STAGE2_FALSE_POSITIVE_MEGA_CONTRACT_THEME","symbol":"047040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"initial backlog bounce without margin conversion should remain Watch/4B-risk","raw_component_scores_before":{"order_backlog_quality_score":8,"selective_order_score":3,"margin_recovery_score":2,"cash_conversion_score":1,"cost_overrun_risk_score":-11,"customer_project_quality":4,"relative_strength_score":11,"valuation_repricing_score":5,"information_confidence":3},"weighted_score_before":26,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_backlog_quality_score":4,"selective_order_score":0,"margin_recovery_score":0,"cash_conversion_score":0,"cost_overrun_risk_score":-16,"customer_project_quality":2,"relative_strength_score":5,"valuation_repricing_score":2,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Initial MFE does not validate Yellow when margin conversion and financing confidence remain missing and 180D MAE deepens."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L86_C05_P0_CURRENT","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C05 needs explicit selective-order, margin recovery and cash-conversion bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":16.54,"avg_MAE90_pct":-11.26,"avg_MFE180_pct":16.54,"avg_MAE180_pct":-28.53,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C05_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L86_C05_P1_SECTOR_SPECIFIC","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P1_L1_EPC_margin_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 EPC signals need selective order, backlog quality, margin recovery, cash conversion or cost-control bridge before Stage2-Actionable","changed_axes":["selective_order_bridge_required","margin_cash_bridge_required","contract_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_selective_order_margin_cash_or_backlog_quality_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":16.54,"avg_MAE90_pct":-11.26,"avg_MFE180_pct":16.54,"avg_MAE180_pct":-28.53,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L86_C05_P2_CANONICAL","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P2_C05_margin_cash_conversion_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C05 should reward margin/cash conversion, not contract-theme price bounces","changed_axes":["C05_margin_cash_bridge_required","C05_contract_theme_local_4B_guard","C05_cost_overrun_risk_penalty"],"changed_thresholds":{"stage2_yellow_gate":"margin_cash_or_selective_order_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":16.54,"avg_MAE90_pct":-11.26,"avg_MFE180_pct":16.54,"avg_MAE180_pct":-28.53,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L86_C05_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P3_C05_deep_180D_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE180<=-25 while margin/cash bridge is missing, block Yellow/Green","changed_axes":["C05_deep_180D_MAE_guardrail","C05_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE180_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":16.54,"avg_MAE90_pct":-11.26,"avg_MFE180_pct":16.54,"avg_MAE180_pct":-28.53,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_MARGIN_BRIDGE_VS_CONTRACT_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":16.54,"avg_MAE90_pct":-11.26,"avg_MFE180_pct":16.54,"avg_MAE180_pct":-28.53,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_20_and_MAE180_le_minus_25":0.67,"stage2_bad_entry_rate_MAE180_le_minus_25":1.0,"interpretation":"C05 needs bridge discipline. 삼성E&A shows selective EPC/margin recovery can create a usable Yellow-watch path, while 현대건설 and 대우건설 show that contract/backlog theme bounces can fail without margin, cost-control and cash-conversion evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028050","trigger_type":"Stage2-Actionable-EPCSelectiveOrderMarginRecoveryBridge-Positive","entry_date":"2024-06-11","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_bridge_but_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when selective-order and margin-recovery bridge exists; Green requires exact order mix, cash and revision evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"000720","trigger_type":"Stage2-FalsePositive-LargeConstructionContractTheme-NoFreshMarginCashBridge","entry_date":"2024-04-29","stage2_to_90D_outcome":"weak_stage2_near_zero_MFE","stage2_to_180D_outcome":"failed_contract_theme_deep_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Large construction/EPC contract theme without fresh margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"047040","trigger_type":"Stage2-FalsePositive-ConstructionMegaContractTheme-NoMarginConversionBridge","entry_date":"2024-07-15","stage2_to_90D_outcome":"mixed_initial_MFE_but_weak_bridge","stage2_to_180D_outcome":"failed_backlog_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Initial backlog bounce without margin conversion and cash bridge should remain Watch; deep 180D MAE supports local guard."}
{"row_type":"residual_contribution","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"EPC_contract_theme_overcredit_without_margin_cash_conversion_bridge","contribution":"Adds two C05 4B/deep-MAE counterexamples against one EPC selective-order margin bridge positive, avoiding C05 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_SELECTIVE_ORDER_MARGIN_RECOVERY_BRIDGE_VS_CONSTRUCTION_CONTRACT_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C05 now has non-top-symbol EPC/construction contract-theme counterexamples; next R1 loops should exact-URL repair order mix, cost-overrun, margin bridge and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_margin_cash_conversion_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"028050 worked when selective-order/margin-recovery bridge was present; 000720 and 047040 failed when contract/backlog theme lacked margin and cash-conversion evidence."}
{"row_type":"shadow_weight","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_contract_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Contract/backlog theme bounces with missing bridge produced low or unstable MFE and deep 180D MAE."}
{"row_type":"shadow_weight","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_deep_180D_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<20 and MAE180<=-25 while margin/cash bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
```

## 11. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - EPC_contract_theme_overcredit
  - margin_cash_conversion_bridge_missing
  - cost_overrun_risk_unresolved
  - initial_backlog_bounce_not_Yellow_validation
new_axis_proposed:
  - C05_margin_cash_conversion_bridge_required_shadow_only
  - C05_contract_theme_local_4B_watch_guard_shadow_only
  - C05_deep_180D_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C05
  - full_4b_requires_non_price_evidence within C05
  - hard_4c_thesis_break_routes_to_4c within C05
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

## 12. Data-quality caveat

All selected triggers use actual Stock-Web tradable raw OHLC rows and clean selected forward windows.  
The non-price evidence layer remains source-name/proxy level.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
3. Confirm R1 / L1 / C05 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C05 top-covered symbols and did not repeat R1 loop85 C04 nuclear evidence.
6. If aggregate support remains stable after exact evidence URL repair, consider C05-scoped safe patch candidates:
   - C05_margin_cash_conversion_bridge_required
   - C05_contract_theme_local_4B_watch_guard
   - C05_deep_180D_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 86
next_round = R2
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
```
