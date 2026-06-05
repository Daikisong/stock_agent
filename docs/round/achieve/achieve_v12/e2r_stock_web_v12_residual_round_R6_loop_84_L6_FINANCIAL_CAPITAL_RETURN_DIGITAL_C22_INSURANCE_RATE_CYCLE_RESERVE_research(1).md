# E2R Stock-Web v12 Residual Research — R6 Loop 84 / L6 / C22

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 84
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: IFRS17_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_VALUEUP_BETA_SPIKE
sector: financials / insurance / rate-cycle / reserve quality / capital return
output_file: e2r_stock_web_v12_residual_round_R6_loop_84_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 84`.

```text
scheduled_round = R6
scheduled_loop = 84
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

R6 is restricted to L6 financial / capital return / digital.  
C22 is selected because the previous R6 loop handled C21, while C22 still needs a sharper separation between true insurance reserve/CSM/capital-return bridge and generic insurance beta/value-up price spikes.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"032830","company_name":"삼성생명","profile_path":"atlas/symbol_profiles/032/032830.json","first_date":"2010-05-12","last_date":"2026-02-20","trading_day_count":3883,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"001450","company_name":"현대해상","profile_path":"atlas/symbol_profiles/001/001450.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7761,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2004-07-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"088350","company_name":"한화생명","profile_path":"atlas/symbol_profiles/088/088350.json","first_date":"2010-03-17","last_date":"2026-02-20","trading_day_count":3922,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C22, the top-covered symbols are `000370`, `003690`, `082640`, `000540`, `000810`, and `005830`. This loop avoids that repeated set and introduces three other insurance symbols.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"032830","trigger_type":"Stage2-Actionable-LifeInsuranceCSMCapitalReturnBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","trigger_type":"Stage2-FalsePositive-NonLifeValueupSpike-ReserveQualityUnverified","entry_date":"2024-02-05","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","trigger_type":"Stage2-FalsePositive-LifeInsuranceBetaSpike-NoCSMReturnBridge","entry_date":"2024-02-05","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C22 should not treat every insurance rally as a reserve-cycle rerating. Insurance is a balance-sheet machine: premium rate, loss ratio, reserve adequacy, CSM quality, solvency, and capital return must interlock. A value-up beta spike without those gears becomes a drawdown trap.

Residual question:

```text
Can C22 distinguish:
1. life-insurance CSM/capital-return bridge with sustained rerating path,
2. non-life insurance value-up spike where reserve quality and loss-ratio bridge are not verified,
3. life-insurance beta spike without durable CSM/shareholder-return bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C22_R6L84_032830_SAMSUNGLIFE_CSM_CAPITAL_RETURN_BRIDGE","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_CSM_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-LifeInsuranceCSMCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_CSM_and_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Life insurance rerating worked when CSM/capital-return proxy and price path aligned. Supports Stage2/Yellow, not Green loosening without exact source evidence."}
{"row_type":"case","case_id":"C22_R6L84_001450_HYUNDAIMARINE_VALUEUP_SPIKE_RESERVE_UNVERIFIED","symbol":"001450","company_name":"현대해상","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_INSURANCE_VALUEUP_SPIKE_WITH_RESERVE_QUALITY_UNVERIFIED","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NonLifeValueupSpike-ReserveQualityUnverified","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_valueup_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Non-life insurance value-up spike had low MFE and later high MAE; reserve/loss-ratio bridge should be required before actionable upgrade."}
{"row_type":"case","case_id":"C22_R6L84_088350_HANWHALIFE_BETA_SPIKE_NO_CSM_RETURN_BRIDGE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_BETA_SPIKE_WITHOUT_CSM_SHAREHOLDER_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LifeInsuranceBetaSpike-NoCSMReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_life_beta_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Life-insurance beta spike after value-up rally did not hold; CSM/shareholder-return and reserve-quality evidence should gate Stage2/Yellow."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 032830 삼성생명 — life insurance CSM/capital-return bridge positive

Entry row: `2024-01-29 c=65700`.  
Forward path: high reached `2024-03-08 h=108500`, while same-window low was `2024-01-29 l=63800`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L84_C22_032830_20240129_STAGE2_LIFE_CSM_CAPITAL_RETURN_BRIDGE","case_id":"C22_R6L84_032830_SAMSUNGLIFE_CSM_CAPITAL_RETURN_BRIDGE","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_CSM_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-LifeInsuranceCSMCapitalReturnBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":65700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_CSM_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; life-insurance CSM/capital-return thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["CSM_quality_proxy","capital_return_proxy","relative_strength_turn"],"stage3_evidence_fields":["reserve_quality_proxy","solvency_ratio_proxy","multi_quarter_CSM_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":65.14,"MFE_90D_pct":65.14,"MFE_180D_pct":65.14,"MAE_30D_pct":-2.89,"MAE_90D_pct":-2.89,"MAE_180D_pct":-2.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":108500.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":63800.0,"drawdown_after_peak_pct":-29.40,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_CSM_and_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"032830_2024-01-29_65700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 can support Stage2/Yellow when CSM/capital-return bridge exists and price path confirms with shallow MAE. Green still requires exact source and reserve/solvency confirmation."}
```

### 6.2 001450 현대해상 — non-life value-up spike with reserve bridge unverified

Entry row: `2024-02-05 c=35750`.  
Forward path: high reached only `2024-02-05 h=36800`, while later low reached `2024-04-15 l=28450`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L84_C22_001450_20240205_STAGE2_FALSE_POSITIVE_NONLIFE_VALUEUP_RESERVE_UNVERIFIED","case_id":"C22_R6L84_001450_HYUNDAIMARINE_VALUEUP_SPIKE_RESERVE_UNVERIFIED","symbol":"001450","company_name":"현대해상","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_INSURANCE_VALUEUP_SPIKE_WITH_RESERVE_QUALITY_UNVERIFIED","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-NonLifeValueupSpike-ReserveQualityUnverified","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":35750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_valueup_nonlife_insurance_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; non-life insurance value-up/beta narrative treated as insufficient without reserve quality, loss-ratio, rate-cycle and capital-return bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["valueup_beta_proxy","relative_strength_spike"],"stage3_evidence_fields":["reserve_quality_missing","loss_ratio_bridge_missing","capital_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","reserve_or_loss_ratio_slowdown_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.94,"MFE_90D_pct":2.94,"MFE_180D_pct":2.94,"MAE_30D_pct":-13.71,"MAE_90D_pct":-20.42,"MAE_180D_pct":-20.42,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":36800.0,"max_drawdown_low_date":"2024-04-15","max_drawdown_low":28450.0,"drawdown_after_peak_pct":-22.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_reserve_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","reserve_quality_missing"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_valueup_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001450_2024-02-05_35750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 needs reserve/loss-ratio/capital-return bridge before Stage2-Actionable. Non-life value-up beta spike alone created low MFE and high MAE."}
```

### 6.3 088350 한화생명 — life-insurance beta spike without CSM/shareholder-return bridge

Entry row: `2024-02-05 c=3690`.  
Forward path: local high reached `2024-02-13 h=3815`, then low reached `2024-04-16 l=2580`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L84_C22_088350_20240205_STAGE2_FALSE_POSITIVE_LIFE_BETA_SPIKE_NO_CSM_RETURN","case_id":"C22_R6L84_088350_HANWHALIFE_BETA_SPIKE_NO_CSM_RETURN_BRIDGE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_BETA_SPIKE_WITHOUT_CSM_SHAREHOLDER_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LifeInsuranceBetaSpike-NoCSMReturnBridge","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":3690.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_life_insurance_valueup_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; life-insurance beta/value-up spike treated as insufficient without CSM quality, reserve adequacy, solvency and shareholder-return bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["life_insurance_beta_proxy","relative_strength_spike"],"stage3_evidence_fields":["CSM_quality_missing","reserve_quality_missing","shareholder_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.39,"MFE_90D_pct":3.39,"MFE_180D_pct":3.39,"MAE_30D_pct":-17.89,"MAE_90D_pct":-30.08,"MAE_180D_pct":-30.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815.0,"max_drawdown_low_date":"2024-04-16","max_drawdown_low":2580.0,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_CSM_shareholder_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_life_beta_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"088350_2024-02-05_3690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should block life-insurance beta spikes when CSM/shareholder-return and reserve-quality bridge is missing. Low MFE and high MAE argue for a local guard."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L84_032830_SAMSUNGLIFE_CSM_CAPITAL_RETURN_BRIDGE","trigger_id":"R6L84_C22_032830_20240129_STAGE2_LIFE_CSM_CAPITAL_RETURN_BRIDGE","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C22 requires CSM/reserve/capital-return bridge","raw_component_scores_before":{"roe_csm_score":15,"reserve_quality_score":12,"loss_ratio_or_rate_cycle_score":8,"capital_return_score":14,"solvency_score":10,"relative_strength_score":15,"valuation_repricing_score":12,"execution_risk_score":-4,"accounting_trust_risk_score":-1,"information_confidence":5},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"roe_csm_score":18,"reserve_quality_score":15,"loss_ratio_or_rate_cycle_score":10,"capital_return_score":17,"solvency_score":12,"relative_strength_score":16,"valuation_repricing_score":13,"execution_risk_score":-3,"accounting_trust_risk_score":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"CSM/capital-return bridge and shallow MAE support upgrade, but exact evidence URL and reserve/solvency proof still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L84_001450_HYUNDAIMARINE_VALUEUP_SPIKE_RESERVE_UNVERIFIED","trigger_id":"R6L84_C22_001450_20240205_STAGE2_FALSE_POSITIVE_NONLIFE_VALUEUP_RESERVE_UNVERIFIED","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"value-up beta without reserve/loss-ratio bridge should not be actionable","raw_component_scores_before":{"roe_csm_score":9,"reserve_quality_score":4,"loss_ratio_or_rate_cycle_score":5,"capital_return_score":8,"solvency_score":7,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-10,"accounting_trust_risk_score":-2,"information_confidence":4},"weighted_score_before":47,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"roe_csm_score":6,"reserve_quality_score":1,"loss_ratio_or_rate_cycle_score":2,"capital_return_score":5,"solvency_score":5,"relative_strength_score":7,"valuation_repricing_score":4,"execution_risk_score":-15,"accounting_trust_risk_score":-3,"information_confidence":3},"weighted_score_after":20,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Reserve/loss-ratio bridge missing and high MAE convert non-life value-up spike into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L84_088350_HANWHALIFE_BETA_SPIKE_NO_CSM_RETURN_BRIDGE","trigger_id":"R6L84_C22_088350_20240205_STAGE2_FALSE_POSITIVE_LIFE_BETA_SPIKE_NO_CSM_RETURN","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"life-insurance beta spike without CSM/shareholder-return bridge should stay Watch/blocked","raw_component_scores_before":{"roe_csm_score":7,"reserve_quality_score":4,"loss_ratio_or_rate_cycle_score":4,"capital_return_score":6,"solvency_score":6,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-12,"accounting_trust_risk_score":-2,"information_confidence":4},"weighted_score_before":39,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"roe_csm_score":4,"reserve_quality_score":1,"loss_ratio_or_rate_cycle_score":2,"capital_return_score":3,"solvency_score":4,"relative_strength_score":6,"valuation_repricing_score":4,"execution_risk_score":-18,"accounting_trust_risk_score":-3,"information_confidence":3},"weighted_score_after":6,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Life-insurance beta spike fails without CSM quality and shareholder-return bridge; high MAE confirms the guardrail."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L84_C22_P0_CURRENT","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C22 needs explicit reserve/CSM/capital-return bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":23.82,"avg_MAE_90D_pct":-17.80,"avg_MFE_180D_pct":23.82,"avg_MAE_180D_pct":-17.80,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C22_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L84_C22_P1_SECTOR_SPECIFIC","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P1_L6_insurance_reserve_capital_return_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 insurance signals need CSM/reserve/capital-return bridge before Stage2-Actionable","changed_axes":["reserve_quality_required","CSM_quality_required","capital_return_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_CSM_reserve_or_capital_return_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":23.82,"avg_MAE_90D_pct":-17.80,"avg_MFE_180D_pct":23.82,"avg_MAE_180D_pct":-17.80,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L84_C22_P2_CANONICAL","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P2_C22_reserve_CSM_capital_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C22 should reward true reserve/CSM/capital-return bridge, not insurance beta spikes","changed_axes":["C22_reserve_quality_bridge_required","C22_CSM_capital_return_bridge_required","C22_valueup_beta_spike_penalty"],"changed_thresholds":{"stage2_yellow_gate":"reserve_or_CSM_or_capital_return_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":23.82,"avg_MAE_90D_pct":-17.80,"avg_MFE_180D_pct":23.82,"avg_MAE_180D_pct":-17.80,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L84_C22_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P3_C22_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-20 while reserve/CSM/capital-return bridge is missing, block Yellow/Green","changed_axes":["C22_high_MAE_guardrail","C22_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE_90D_pct":23.82,"avg_MAE_90D_pct":-17.80,"avg_MFE_180D_pct":23.82,"avg_MAE_180D_pct":-17.80,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_IFRS17_CSM_RESERVE_BRIDGE_VS_INSURANCE_BETA_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":23.82,"avg_MAE90_pct":-17.80,"avg_MFE180_pct":23.82,"avg_MAE180_pct":-17.80,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C22 needs bridge discipline. 삼성생명 shows a valid CSM/capital-return path, while 현대해상 and 한화생명 show insurance beta/value-up spikes that fail without reserve/CSM/capital-return bridge."}
{"row_type":"stage_transition_summary","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"032830","trigger_type":"Stage2-Actionable-LifeInsuranceCSMCapitalReturnBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when CSM/capital-return bridge exists; Green requires exact reserve/solvency and source-quality repair."}
{"row_type":"stage_transition_summary","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","trigger_type":"Stage2-FalsePositive-NonLifeValueupSpike-ReserveQualityUnverified","entry_date":"2024-02-05","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_reserve_quality_unverified","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Non-life insurance value-up spike without reserve/loss-ratio bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","trigger_type":"Stage2-FalsePositive-LifeInsuranceBetaSpike-NoCSMReturnBridge","entry_date":"2024-02-05","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_life_beta_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Life-insurance beta spike without CSM/shareholder-return bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_beta_valueup_overcredit_without_reserve_CSM_capital_return_bridge","contribution":"Adds two high-MAE C22 counterexamples against one CSM/capital-return bridge positive, improving C22 local guardrail evidence outside the top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_VALUEUP_BETA_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C22 now has non-top-symbol counterexamples for value-up/beta spikes; next R6 loops should exact-URL repair reserve/CSM/capital-return evidence and add 4C reserve-break rows."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_reserve_CSM_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"032830 worked with CSM/capital-return bridge proxy; 001450 and 088350 failed when reserve/CSM/shareholder-return bridge was missing."}
{"row_type":"shadow_weight","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_valueup_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Insurance value-up beta spikes showed low MFE and high MAE without reserve/CSM/capital-return evidence."}
{"row_type":"shadow_weight","round":"R6","loop":"84","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE90<=-20 while reserve/CSM/capital-return bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
residual_error_types_found:
  - insurance_valueup_beta_overcredit
  - nonlife_reserve_quality_unverified_high_MAE
  - life_insurance_CSM_shareholder_return_bridge_missing
new_axis_proposed:
  - C22_reserve_CSM_capital_return_bridge_required_shadow_only
  - C22_valueup_beta_local_4B_watch_guard_shadow_only
  - C22_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C22
  - full_4b_requires_non_price_evidence within C22
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
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
3. Confirm R6 / L6 / C22 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C22-scoped safe patch candidates:
   - C22_reserve_CSM_capital_return_bridge_required
   - C22_valueup_beta_local_4B_watch_guard
   - C22_high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 84
next_round = R7
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.
```
