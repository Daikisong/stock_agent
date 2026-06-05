# E2R Stock-Web v12 Residual Research — R6 Loop 85 / L6 / C21

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 85
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_FINANCE_BETA_SPIKE
sector: financials / bank / capital return / digital finance
output_file: e2r_stock_web_v12_residual_round_R6_loop_85_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 85`.

```text
scheduled_round = R6
scheduled_loop = 85
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

R6 is restricted to financial / capital return / digital finance.  
C21 is selected because the previous R6 loop used C22 insurance reserve-cycle evidence, while C21 remains the core bank/financial ROE-PBR-capital-return bucket.

The selected symbols avoid the C21 top-covered list in the No-Repeat Index:

```text
006220, 016360, 071050, 105560, 138040, 139130
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"086790","company_name":"하나금융지주","profile_path":"atlas/symbol_profiles/086/086790.json","first_date":"2005-12-12","last_date":"2026-02-20","trading_day_count":4980,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"323410","company_name":"카카오뱅크","profile_path":"atlas/symbol_profiles/323/323410.json","first_date":"2021-08-06","last_date":"2026-02-20","trading_day_count":1109,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"377300","company_name":"카카오페이","profile_path":"atlas/symbol_profiles/377/377300.json","first_date":"2021-11-03","last_date":"2026-02-20","trading_day_count":1050,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"086790","trigger_type":"Stage2-Actionable-BankROEPBRCapitalReturnBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"323410","trigger_type":"Stage2-FalsePositive-DigitalBankBetaSpike-NoCapitalReturnBridge","entry_date":"2024-01-15","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"377300","trigger_type":"Stage2-FalsePositive-FintechPaymentBetaSpike-NoROEBridge","entry_date":"2024-01-15","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C21 is not simply “financial stock goes up on value-up.” It is a capital-return machine. The real bridge is sustainable ROE, PBR discount repair, CET1/capital buffer, dividend or buyback credibility, credit-cost control, and valuation-to-shareholder-return conversion.

Residual question:

```text
Can C21 distinguish:
1. bank/financial holding capital-return bridge with sustained MFE and shallow MAE,
2. digital-bank beta spike without shareholder-return and capital-buffer bridge,
3. fintech/payment beta spike without ROE/PBR/capital-return bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C21_R6L85_086790_HANA_BANK_ROE_PBR_CAPITAL_RETURN","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BankROEPBRCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Bank ROE/PBR/capital-return proxy produced high MFE and shallow MAE; supports Stage2/Yellow, not automatic Green without exact capital-return and CET1 evidence."}
{"row_type":"case","case_id":"C21_R6L85_323410_KAKAOBANK_DIGITAL_BETA_NO_CAPITAL_RETURN","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_BETA_SPIKE_WITHOUT_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DigitalBankBetaSpike-NoCapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_digital_bank_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Digital-bank beta spike lacked dividend/buyback and PBR repair bridge; local upside was tiny while forward MAE was severe."}
{"row_type":"case","case_id":"C21_R6L85_377300_KAKAOPAY_FINTECH_BETA_NO_ROE_BRIDGE","symbol":"377300","company_name":"카카오페이","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"FINTECH_PAYMENT_BETA_SPIKE_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-FintechPaymentBetaSpike-NoROEBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_fintech_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Fintech/payment beta spike did not have bank-style ROE/PBR/capital-return mechanics; forward path shows extreme MAE."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 086790 하나금융지주 — bank ROE/PBR capital-return bridge positive

Entry row: `2024-01-29 c=46400`.  
Observed path: entry-week low `2024-01-31 l=45750`, 30D/90D high `2024-05-13 h=65300`, and later high `2024-10-25 h=69200`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L85_C21_086790_20240129_STAGE2_BANK_CAPITAL_RETURN_BRIDGE","case_id":"C21_R6L85_086790_HANA_BANK_ROE_PBR_CAPITAL_RETURN","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BankROEPBRCapitalReturnBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":46400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_bank_valueup_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; bank ROE/PBR/capital-return thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ROE_quality_proxy","PBR_discount_repair_proxy","capital_return_proxy","relative_strength_turn"],"stage3_evidence_fields":["CET1_or_capital_buffer_pending","dividend_buyback_confirmation_pending","credit_cost_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.22,"MFE_90D_pct":40.73,"MFE_180D_pct":49.14,"MAE_30D_pct":-1.40,"MAE_90D_pct":-1.40,"MAE_180D_pct":-1.40,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":69200.0,"max_drawdown_low_date":"2024-01-31","max_drawdown_low":45750.0,"drawdown_after_peak_pct":-18.50,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"086790_2024-01-29_46400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 can allow Stage2/Yellow when ROE/PBR discount repair is tied to credible capital-return bridge. Green still requires exact CET1, dividend/buyback and credit-cost evidence."}
```

### 6.2 323410 카카오뱅크 — digital-bank beta spike without capital-return bridge

Entry row: `2024-01-15 c=31450`.  
Observed path: local high `2024-01-15 h=31500`, then lows reached `2024-05-30 l=21850`, `2024-06-27 l=20050`, and later the low-20k range.

```jsonl
{"row_type":"trigger","trigger_id":"R6L85_C21_323410_20240115_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_BETA","case_id":"C21_R6L85_323410_KAKAOBANK_DIGITAL_BETA_NO_CAPITAL_RETURN","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_BETA_SPIKE_WITHOUT_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DigitalBankBetaSpike-NoCapitalReturnBridge","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":31450.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_digital_bank_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; digital-bank/value-up beta treated as insufficient without ROE/PBR discount repair, CET1, dividend or buyback bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["digital_bank_beta_spike","relative_strength_spike"],"stage3_evidence_fields":["capital_return_bridge_missing","PBR_discount_repair_missing","credit_cost_bridge_missing","shareholder_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","capital_return_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.16,"MFE_90D_pct":0.16,"MFE_180D_pct":0.16,"MAE_30D_pct":-15.74,"MAE_90D_pct":-30.52,"MAE_180D_pct":-36.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-15","peak_price":31500.0,"max_drawdown_low_date":"2024-06-27","max_drawdown_low":20050.0,"drawdown_after_peak_pct":-36.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_bank_beta_peak_without_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","capital_return_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_digital_bank_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"323410_2024-01-15_31450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not treat digital-bank beta as bank capital-return bridge. Without shareholder-return and PBR repair evidence, local peak plus high MAE should route to Watch/4B-risk."}
```

### 6.3 377300 카카오페이 — fintech/payment beta spike without ROE/capital-return bridge

Entry row: `2024-01-15 c=58800`.  
Observed path: local high `2024-01-15 h=59000`, then lows reached `2024-02-29 l=44050`, `2024-06-27 l=26100`, and `2024-11-15 l=21200`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L85_C21_377300_20240115_STAGE2_FALSE_POSITIVE_FINTECH_PAYMENT_BETA","case_id":"C21_R6L85_377300_KAKAOPAY_FINTECH_BETA_NO_ROE_BRIDGE","symbol":"377300","company_name":"카카오페이","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"FINTECH_PAYMENT_BETA_SPIKE_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-FintechPaymentBetaSpike-NoROEBridge","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":58800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_fintech_payment_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; fintech/payment beta treated as insufficient for C21 unless ROE, PBR repair, capital return or durable profitability bridge is verified","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["fintech_payment_beta_spike","relative_strength_spike"],"stage3_evidence_fields":["ROE_bridge_missing","PBR_discount_repair_missing","capital_return_bridge_missing","durable_profitability_missing"],"stage4b_evidence_fields":["price_only_local_peak","profitability_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv","profile_path":"atlas/symbol_profiles/377/377300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.34,"MFE_90D_pct":0.34,"MFE_180D_pct":0.34,"MAE_30D_pct":-22.96,"MAE_90D_pct":-44.64,"MAE_180D_pct":-63.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-15","peak_price":59000.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":21200.0,"drawdown_after_peak_pct":-64.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fintech_beta_peak_without_ROE_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","profitability_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_fintech_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"377300_2024-01-15_58800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should block fintech/payment beta when ROE, durable profitability and capital-return bridge are absent. Price-only spike produced almost no MFE and extreme MAE."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L85_086790_HANA_BANK_ROE_PBR_CAPITAL_RETURN","trigger_id":"R6L85_C21_086790_20240129_STAGE2_BANK_CAPITAL_RETURN_BRIDGE","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C21 requires ROE/PBR/capital-return bridge, not value-up beta alone","raw_component_scores_before":{"ROE_quality_score":15,"PBR_discount_repair_score":15,"capital_return_score":14,"CET1_or_capital_buffer_score":11,"credit_cost_control_score":9,"relative_strength_score":13,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"ROE_quality_score":18,"PBR_discount_repair_score":18,"capital_return_score":17,"CET1_or_capital_buffer_score":13,"credit_cost_control_score":11,"relative_strength_score":14,"valuation_repricing_score":12,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Capital-return bridge and shallow MAE support Yellow-watch; exact CET1/dividend/buyback evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L85_323410_KAKAOBANK_DIGITAL_BETA_NO_CAPITAL_RETURN","trigger_id":"R6L85_C21_323410_20240115_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_BETA","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"digital-bank beta without capital-return bridge should be blocked","raw_component_scores_before":{"ROE_quality_score":6,"PBR_discount_repair_score":4,"capital_return_score":1,"CET1_or_capital_buffer_score":4,"credit_cost_control_score":4,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":28,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_quality_score":3,"PBR_discount_repair_score":1,"capital_return_score":0,"CET1_or_capital_buffer_score":2,"credit_cost_control_score":2,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert digital-bank beta into capital-return bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L85_377300_KAKAOPAY_FINTECH_BETA_NO_ROE_BRIDGE","trigger_id":"R6L85_C21_377300_20240115_STAGE2_FALSE_POSITIVE_FINTECH_PAYMENT_BETA","symbol":"377300","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"fintech/payment beta without ROE and durable profitability bridge should remain Watch/blocked","raw_component_scores_before":{"ROE_quality_score":2,"PBR_discount_repair_score":2,"capital_return_score":0,"CET1_or_capital_buffer_score":0,"credit_cost_control_score":0,"relative_strength_score":15,"valuation_repricing_score":7,"execution_risk_score":-14,"theme_spike_risk":-15,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_quality_score":0,"PBR_discount_repair_score":0,"capital_return_score":0,"CET1_or_capital_buffer_score":0,"credit_cost_control_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Fintech beta has no ROE/PBR/capital-return bridge; extreme MAE forces 4B/watch or blocked state."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L85_C21_P0_CURRENT","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C21 needs explicit ROE/PBR/capital-return bridge distinction for digital-finance beta names","eligible_trigger_count":3,"avg_MFE90_pct":13.74,"avg_MAE90_pct":-25.52,"avg_MFE180_pct":16.55,"avg_MAE180_pct":-33.87,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C21_capital_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L85_C21_P1_SECTOR_SPECIFIC","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P1_L6_bank_capital_return_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 financial signals need ROE, PBR repair, capital return, capital buffer or credit-cost bridge before Stage2-Actionable","changed_axes":["ROE_quality_required","capital_return_required","digital_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_ROE_PBR_capital_return_or_capital_buffer_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":13.74,"avg_MAE90_pct":-25.52,"avg_MFE180_pct":16.55,"avg_MAE180_pct":-33.87,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L85_C21_P2_CANONICAL","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P2_C21_ROE_PBR_capital_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 should reward real bank capital-return mechanics, not fintech/digital-finance beta","changed_axes":["C21_ROE_PBR_capital_return_bridge_required","C21_digital_finance_beta_penalty","C21_price_only_beta_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"ROE_PBR_or_capital_return_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":13.74,"avg_MAE90_pct":-25.52,"avg_MFE180_pct":16.55,"avg_MAE180_pct":-33.87,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L85_C21_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P3_C21_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-25 while capital-return bridge is missing, block Yellow/Green","changed_axes":["C21_high_MAE_guardrail","C21_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":13.74,"avg_MAE90_pct":-25.52,"avg_MFE180_pct":16.55,"avg_MAE180_pct":-33.87,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_CAPITAL_RETURN_VS_DIGITAL_FINANCE_BETA","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":13.74,"avg_MAE90_pct":-25.52,"avg_MFE180_pct":16.55,"avg_MAE180_pct":-33.87,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C21 needs bridge discipline. 하나금융지주 shows bank ROE/PBR/capital-return mechanics can rerate with shallow MAE, while 카카오뱅크 and 카카오페이 show digital-finance beta spikes fail without shareholder-return, ROE and PBR repair bridge."}
{"row_type":"stage_transition_summary","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"086790","trigger_type":"Stage2-Actionable-BankROEPBRCapitalReturnBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_capital_return_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when ROE/PBR and capital-return bridge exists; Green requires exact CET1/dividend/buyback evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"323410","trigger_type":"Stage2-FalsePositive-DigitalBankBetaSpike-NoCapitalReturnBridge","entry_date":"2024-01-15","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_digital_bank_beta_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Digital-bank beta without shareholder-return and capital-buffer bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"377300","trigger_type":"Stage2-FalsePositive-FintechPaymentBetaSpike-NoROEBridge","entry_date":"2024-01-15","stage2_to_90D_outcome":"bad_stage2_low_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_fintech_beta_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Fintech/payment beta without ROE/PBR and capital-return bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"digital_finance_beta_overcredit_without_ROE_PBR_capital_return_bridge","contribution":"Adds two C21 local 4B/high-MAE counterexamples against one bank capital-return bridge positive, avoiding C21 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_FINANCE_BETA_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C21 now has non-top-symbol digital-finance beta counterexamples; next R6 loops should exact-URL repair CET1, dividend/buyback, credit cost, ROE and PBR-discount evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_ROE_PBR_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"086790 worked with bank ROE/PBR/capital-return bridge proxy; 323410 and 377300 failed when only digital-finance beta was present."}
{"row_type":"shadow_weight","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_digital_finance_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Digital bank and fintech/payment beta spikes showed near-zero MFE and high/extreme MAE without capital-return mechanics."}
{"row_type":"shadow_weight","round":"R6","loop":"85","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE90<=-25 while ROE/PBR/capital-return bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - digital_finance_beta_overcredit
  - digital_bank_no_capital_return_bridge
  - fintech_payment_no_ROE_bridge
  - price_only_financial_beta_local_peak
new_axis_proposed:
  - C21_ROE_PBR_capital_return_bridge_required_shadow_only
  - C21_digital_finance_beta_local_4B_watch_guard_shadow_only
  - C21_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C21
  - full_4b_requires_non_price_evidence within C21
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
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
3. Confirm R6 / L6 / C21 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C21 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C21-scoped safe patch candidates:
   - C21_ROE_PBR_capital_return_bridge_required
   - C21_digital_finance_beta_local_4B_watch_guard
   - C21_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 85
next_round = R7
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
```
