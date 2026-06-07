# E2R Stock-Web v12 Residual Research — R6 Loop 92 / L6 / C22

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 92
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: P_AND_C_INSURANCE_LOSS_RATIO_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_SPIKE_AND_BANK_RATE_CROSSLABEL
sector: financial / insurance / reserve / rate cycle / loss ratio / capital return / cross-label financial value-up
output_file: e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 92`.

```text
scheduled_round = R6
scheduled_loop = 92
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

R6 is restricted to financial / capital return / digital-financial names.
C22 is selected because R6 loop91 used C21, so loop92 returns to insurance rate-cycle / reserve residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows = 37
symbols = 12
good/bad Stage2 = 10/11
4B/4C = 2/0
top-covered = 000370, 003690, 082640, 000540, 000810, 005830
```

This loop avoids the C22 top-covered list and recent R6 loop symbols:

```text
R6 loop87 C21: 006800, 039490, 316140
R6 loop88 C22: 138040, 211050, 244920
R6 loop89 C21: 024110, 001510, 001200
R6 loop90 C22: 032830, 088350, 000400
R6 loop91 C21: 005940, 030610, 001290
C22 top-covered: 000370, 003690, 082640, 000540, 000810, 005830
```

Candidate hygiene note:

```text
During this execution path, stale R5/C18, R4/C16, R3/C14 and R2/C08 candidate rows were touched while checking alternatives.
Those rows are not used in this R6/C22 output.
```

Selected symbols:

```text
001450, 085620, 138930
```

The selected pocket is:

```text
P&C insurance loss-ratio / reserve-cycle / capital-return bridge positive-watch
vs
life-insurance price spike without durable reserve / payout / capital-quality bridge
vs
bank financial-holding rate/PBR price-MFE cross-label row that should not be counted as C22 insurance reserve evidence
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"001450","company_name":"현대해상","profile_path":"atlas/symbol_profiles/001/001450.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7761,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2004-07-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"085620","company_name":"미래에셋생명","profile_path":"atlas/symbol_profiles/085/085620.json","first_date":"2015-07-08","last_date":"2026-02-20","trading_day_count":2606,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2018-03-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"138930","company_name":"BNK금융지주","profile_path":"atlas/symbol_profiles/138/138930.json","first_date":"2011-03-30","last_date":"2026-02-20","trading_day_count":3663,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2014-07-25","2016-02-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; cross_label_financial_holding_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","trigger_type":"Stage2-Actionable-PCInsuranceLossRatioReserveCapitalReturnBridge-PositiveWatch","entry_date":"2024-01-29","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and recent R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"085620","trigger_type":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","entry_date":"2024-02-05","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and recent R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"138930","trigger_type":"Stage2-FalsePositive-BankFinancialHoldingRatePBRPriceMFE-NoInsuranceReserveBridge","entry_date":"2024-01-29","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and recent R6 loop symbols; cross-label financial holding stress row, not C21 contribution"}
```

## 4. Research question

C22 is not “금융주가 금리와 저PBR로 올랐다.”
The useful insurance reserve / rate-cycle signal must prove the insurance-specific economics:

```text
loss ratio or claims-cost improvement
reserve adequacy / reserve release risk containment
IFRS17 CSM or insurance-service margin quality
asset duration / reinvestment-rate benefit
capital buffer
dividend payout / buyback / cancellation path
regulatory approval or solvency path
earnings quality
cash-return discipline
```

A rate-cycle headline without this bridge is an insurance ledger with the premium column highlighted and the claims column hidden. E2R needs both sides: premium, reserve, capital, payout, and cash.

Residual question:

```text
Can C22 distinguish:
1. P&C insurer loss-ratio / reserve-cycle / capital-return bridge worth Yellow/positive-watch,
2. life-insurance price spike where no durable reserve / payout bridge exists after the move,
3. bank financial-holding rate/PBR price-MFE that should not be counted as C22 insurance reserve evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C22_R6L92_001450_HYUNDAI_MARINE_PC_RESERVE","symbol":"001450","company_name":"현대해상","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"PC_INSURANCE_LOSS_RATIO_RESERVE_CAPITAL_RETURN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PCInsuranceLossRatioReserveCapitalReturnBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_moderate_MFE90_low_MAE_reserve_capital_return_bridge","current_profile_verdict":"current_profile_correct_if_loss_ratio_reserve_capital_payout_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"P&C insurance rate/reserve/value-up proxy produced moderate MFE and controlled MAE. This is Yellow/positive-watch only, not automatic Green, unless exact loss-ratio, reserve, capital and payout evidence is repaired."}
{"row_type":"case","case_id":"C22_R6L92_085620_MIRAE_LIFE_PRICE_SPIKE","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_PRICE_SPIKE_WITHOUT_DURABLE_RESERVE_PAYOUT_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_after_spike_no_reserve_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_life_insurance_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Life-insurance price spike after the first rally had near-zero forward MFE and deep drawdown when no durable reserve, CSM-quality, payout or capital-return bridge was repaired."}
{"row_type":"case","case_id":"C22_R6L92_138930_BNK_CROSSLABEL_RATE_PBR","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"BANK_FINANCIAL_HOLDING_RATE_PBR_PRICE_MFE_WITHOUT_INSURANCE_RESERVE_BRIDGE","case_type":"cross_label_failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BankFinancialHoldingRatePBRPriceMFE-NoInsuranceReserveBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"score_price_alignment":"counterexample_price_MFE_but_cross_label_no_insurance_reserve_bridge","current_profile_verdict":"current_profile_false_positive_if_bank_rate_PBR_MFE_counted_as_C22_insurance_evidence","price_source":"Songdaiki/stock-web","notes":"Financial-holding rate/PBR MFE can be valid elsewhere, but not as C22 insurance reserve evidence. This is a cross-label 4B stress row, not a C21 contribution."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 001450 현대해상 — P&C insurance loss-ratio / reserve / capital-return bridge positive-watch

Entry row: `2024-01-29 c=31700`.
Observed path: high `2024-02-05 h=36800`, controlled early low `2024-01-29 l=30250`, later Q4 drawdown but not enough to erase the need for bridge-specific evidence.

```jsonl
{"row_type":"trigger","trigger_id":"R6L92_C22_001450_20240129_STAGE2_PC_INSURANCE_RESERVE","case_id":"C22_R6L92_001450_HYUNDAI_MARINE_PC_RESERVE","symbol":"001450","company_name":"현대해상","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"PC_INSURANCE_LOSS_RATIO_RESERVE_CAPITAL_RETURN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PCInsuranceLossRatioReserveCapitalReturnBridge-PositiveWatch","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":31700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_PC_insurance_loss_ratio_reserve_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; P&C loss-ratio/reserve adequacy, capital buffer and payout bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["loss_ratio_improvement_proxy","reserve_cycle_proxy","capital_buffer_proxy","valueup_payout_proxy"],"stage3_evidence_fields":["exact_loss_ratio_source_pending","reserve_or_CSM_quality_source_pending","capital_buffer_source_pending","payout_buyback_source_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","Green_strict_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.09,"MFE_90D_pct":16.09,"MFE_180D_pct":16.09,"MAE_30D_pct":-4.57,"MAE_90D_pct":-4.57,"MAE_180D_pct":-5.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":36800.0,"max_drawdown_low_date":"2024-10-24","max_drawdown_low":29800.0,"drawdown_after_peak_pct":-19.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_only; moderate_MFE_requires_exact_loss_ratio_reserve_capital_payout_evidence_before_Green","four_b_evidence_type":["moderate_MFE_watch","Green_strict_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_watch_moderate_MFE90_low_MAE_reserve_capital_return_bridge","current_profile_verdict":"current_profile_correct_if_loss_ratio_reserve_capital_payout_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"001450_2024-01-29_31700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 can allow Yellow/positive-watch when P&C insurance strength is tied to loss-ratio, reserve adequacy, capital buffer and payout/cash-return bridge. Moderate MFE blocks automatic Green."}
```

### 6.2 085620 미래에셋생명 — life-insurance spike without durable reserve / payout bridge

Entry row: `2024-02-05 c=6390`, after the initial value-up/rate-cycle spike.
Observed path: next-day high `2024-02-06 h=6500`, then rapid decline to `2024-03-19 l=4470` and `2024-04-02 l=4425`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L92_C22_085620_20240205_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_SPIKE","case_id":"C22_R6L92_085620_MIRAE_LIFE_PRICE_SPIKE","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_PRICE_SPIKE_WITHOUT_DURABLE_RESERVE_PAYOUT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":6390.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_life_insurance_valueup_rate_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; life-insurance price spike treated as insufficient without durable reserve, CSM-quality, solvency/capital and payout bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["life_insurance_rate_cycle_vocabulary","valueup_price_spike","relative_strength_after_first_move"],"stage3_evidence_fields":["reserve_quality_missing","CSM_quality_missing","capital_buffer_missing","payout_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","post_spike_entry_watch","deep_MAE","reserve_payout_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv","profile_path":"atlas/symbol_profiles/085/085620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.72,"MFE_90D_pct":1.72,"MFE_180D_pct":1.72,"MAE_30D_pct":-30.05,"MAE_90D_pct":-30.75,"MAE_180D_pct":-30.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":6500.0,"max_drawdown_low_date":"2024-04-02","max_drawdown_low":4425.0,"drawdown_after_peak_pct":-31.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"life_insurance_price_spike_without_reserve_CSM_capital_payout_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","post_spike_entry_watch","deep_MAE","reserve_payout_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_after_spike_no_reserve_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_life_insurance_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"085620_2024-02-05_6390","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not promote life-insurance price spikes unless reserve/CSM quality, solvency capital and payout/cash-return evidence are exact-repaired. Post-spike entries with near-zero MFE and deep MAE route to Watch/4B."}
```

### 6.3 138930 BNK금융지주 — bank financial-holding rate/PBR price MFE without insurance reserve bridge

Entry row: `2024-01-29 c=7420`.
Observed path: MFE from financial value-up/rate vocabulary ultimately expanded, but the row is cross-label: the non-price evidence is not insurance reserve / loss-ratio / CSM / payout evidence.

```jsonl
{"row_type":"trigger","trigger_id":"R6L92_C22_138930_20240129_STAGE2_FALSE_POSITIVE_BANK_RATE_CROSSLABEL","case_id":"C22_R6L92_138930_BNK_CROSSLABEL_RATE_PBR","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"BANK_FINANCIAL_HOLDING_RATE_PBR_PRICE_MFE_WITHOUT_INSURANCE_RESERVE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;cross_label_price_MFE_stress_test","trigger_type":"Stage2-FalsePositive-BankFinancialHoldingRatePBRPriceMFE-NoInsuranceReserveBridge","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":7420.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_bank_financial_holding_valueup_rate_PBR_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; bank financial-holding rate/PBR MFE treated as cross-label stress and insufficient for C22 without insurance reserve/loss-ratio/CSM/payout bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["bank_financial_holding_rate_PBR_vocabulary","price_MFE","valueup_financial_keyword"],"stage3_evidence_fields":["insurance_loss_ratio_missing","reserve_quality_missing","CSM_quality_missing","insurance_payout_bridge_missing"],"stage4b_evidence_fields":["price_MFE","cross_label_bridge_missing_watch","not_C22_insurance_evidence"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.16,"MFE_90D_pct":13.34,"MFE_180D_pct":35.44,"MAE_30D_pct":-3.23,"MAE_90D_pct":-3.23,"MAE_180D_pct":-3.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":10050.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":7180.0,"drawdown_after_peak_pct":-9.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.68,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"bank_rate_PBR_price_MFE_without_insurance_reserve_loss_ratio_CSM_payout_bridge_should_not_be_counted_as_C22_positive","four_b_evidence_type":["price_MFE","cross_label_bridge_missing_watch","not_C22_insurance_evidence"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_but_cross_label_no_insurance_reserve_bridge","current_profile_verdict":"current_profile_false_positive_if_bank_rate_PBR_MFE_counted_as_C22_insurance_evidence","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_label_C21_like_row_used_only_as_C22_false_positive_stress"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"138930_2024-01-29_7420","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not count bank/financial-holding price MFE as insurance reserve validation. It needs insurance-specific loss-ratio, reserve/CSM, solvency capital and payout evidence."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L92_001450_HYUNDAI_MARINE_PC_RESERVE","trigger_id":"R6L92_C22_001450_20240129_STAGE2_PC_INSURANCE_RESERVE","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C22 requires loss-ratio, reserve/CSM quality, capital buffer, solvency and payout/cash-return bridge rather than insurance/value-up vocabulary alone","raw_component_scores_before":{"loss_ratio_score":11,"reserve_quality_score":10,"CSM_quality_score":8,"rate_reinvestment_score":9,"capital_buffer_score":11,"payout_policy_score":10,"regulatory_solvency_score":8,"cash_return_score":8,"relative_strength_score":10,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"loss_ratio_score":14,"reserve_quality_score":13,"CSM_quality_score":10,"rate_reinvestment_score":11,"capital_buffer_score":13,"payout_policy_score":12,"regulatory_solvency_score":10,"cash_return_score":10,"relative_strength_score":11,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"P&C reserve/loss-ratio/capital-return bridge supports Yellow-watch; moderate MFE and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L92_085620_MIRAE_LIFE_PRICE_SPIKE","trigger_id":"R6L92_C22_085620_20240205_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_SPIKE","symbol":"085620","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"life-insurance price spike without reserve/CSM and payout bridge should be blocked","raw_component_scores_before":{"loss_ratio_score":0,"reserve_quality_score":1,"CSM_quality_score":1,"rate_reinvestment_score":3,"capital_buffer_score":1,"payout_policy_score":0,"regulatory_solvency_score":1,"cash_return_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"loss_ratio_score":0,"reserve_quality_score":0,"CSM_quality_score":0,"rate_reinvestment_score":1,"capital_buffer_score":0,"payout_policy_score":0,"regulatory_solvency_score":0,"cash_return_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-26,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE after spike require reserve/CSM/capital/payout evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L92_138930_BNK_CROSSLABEL_RATE_PBR","trigger_id":"R6L92_C22_138930_20240129_STAGE2_FALSE_POSITIVE_BANK_RATE_CROSSLABEL","symbol":"138930","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"bank financial-holding price MFE without insurance-specific reserve/loss-ratio bridge should remain cross-label Watch/4B","raw_component_scores_before":{"loss_ratio_score":0,"reserve_quality_score":0,"CSM_quality_score":0,"rate_reinvestment_score":2,"capital_buffer_score":2,"payout_policy_score":1,"regulatory_solvency_score":1,"cash_return_score":1,"relative_strength_score":12,"valuation_repricing_score":6,"execution_risk_score":-8,"theme_spike_risk":-10,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/CrossLabel","raw_component_scores_after":{"loss_ratio_score":0,"reserve_quality_score":0,"CSM_quality_score":0,"rate_reinvestment_score":1,"capital_buffer_score":1,"payout_policy_score":0,"regulatory_solvency_score":0,"cash_return_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/CrossLabel","component_delta_explanation":"Price MFE is not C22 validation without insurance reserve/loss-ratio/CSM evidence."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L92_C22_P0_CURRENT","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C22 needs explicit insurance reserve/loss-ratio/CSM/capital/payout bridge and cross-label price-MFE taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":10.38,"avg_MAE90_pct":-12.85,"avg_MFE180_pct":17.75,"avg_MAE180_pct":-13.32,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.89,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C22_insurance_reserve_capital_payout_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L92_C22_P1_SECTOR_SPECIFIC","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P1_L6_insurance_reserve_rate_cycle_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 insurance signals need loss-ratio, reserve/CSM quality, capital buffer, regulatory solvency, payout or cash-return bridge before Stage2-Actionable","changed_axes":["reserve_quality_required","loss_ratio_required","payout_capital_required","bank_cross_label_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_loss_ratio_reserve_CSM_capital_payout_or_cash_return_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":10.38,"avg_MAE90_pct":-12.85,"avg_MFE180_pct":17.75,"avg_MAE180_pct":-13.32,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L92_C22_P2_CANONICAL","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P2_C22_reserve_loss_ratio_capital_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C22 should reward insurance reserve/capital-return mechanics, not life-insurance spike or bank-rate price MFE","changed_axes":["C22_loss_ratio_reserve_CSM_capital_payout_bridge_required","C22_life_insurance_post_spike_local_4B_guard","C22_cross_label_bank_rate_PBR_price_MFE_guard","C22_moderate_MFE_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"loss_ratio_or_reserve_quality_plus_capital_or_payout_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":10.38,"avg_MAE90_pct":-12.85,"avg_MFE180_pct":17.75,"avg_MAE180_pct":-13.32,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L92_C22_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P3_C22_near_zero_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If insurance reserve/payout bridge is missing, MFE90<5 or MAE90<=-20 should block Yellow/Green; price MFE without insurance bridge stays 4B-watch","changed_axes":["C22_near_zero_MFE_guardrail","C22_deep_MAE_4B_guardrail","C22_price_MFE_cross_label_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE90_le_minus_20); high_MFE_without_insurance_bridge_not_positive"},"eligible_trigger_count":3,"avg_MFE90_pct":10.38,"avg_MAE90_pct":-12.85,"avg_MFE180_pct":17.75,"avg_MAE180_pct":-13.32,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_PC_INSURANCE_POSITIVE_VS_LIFE_SPIKE_BANK_CROSSLABEL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":10.38,"avg_MAE90_pct":-12.85,"avg_MFE180_pct":17.75,"avg_MAE180_pct":-13.32,"stage2_hit_rate_MFE90_ge15":0.33,"price_MFE_without_insurance_bridge_counterexample_count":1,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C22 needs bridge discipline. 현대해상 shows P&C insurance loss-ratio/reserve/capital-return bridge can support Yellow/positive-watch, while 미래에셋생명 and BNK금융지주 show life-insurance spike or bank-rate/PBR price MFE should not be promoted as C22 without insurance-specific reserve/CSM/capital/payout evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","trigger_type":"Stage2-Actionable-PCInsuranceLossRatioReserveCapitalReturnBridge-PositiveWatch","entry_date":"2024-01-29","stage2_to_90D_outcome":"positive_watch_moderate_MFE_low_MAE","stage2_to_180D_outcome":"P&C_reserve_capital_return_bridge_but_Green_strict","MFE90_ge15":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/positive-watch when insurance strength is tied to loss-ratio, reserve quality, capital and payout/cash bridge; moderate MFE keeps Green strict."}
{"row_type":"stage_transition_summary","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"085620","trigger_type":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","entry_date":"2024-02-05","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE_after_spike","stage2_to_180D_outcome":"failed_life_insurance_spike_no_reserve_payout_bridge","MFE90_ge15":false,"MAE90_le_minus20":true,"transition_note":"Life-insurance spike without reserve/CSM/capital/payout evidence should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"138930","trigger_type":"Stage2-FalsePositive-BankFinancialHoldingRatePBRPriceMFE-NoInsuranceReserveBridge","entry_date":"2024-01-29","stage2_to_90D_outcome":"cross_label_price_MFE_without_insurance_bridge","stage2_to_180D_outcome":"bank_financial_MFE_not_C22_validation","MFE180_ge20":true,"MAE180_le_minus20":false,"transition_note":"Bank/rate/PBR MFE is not C22 insurance evidence unless insurance-specific loss-ratio, reserve/CSM and payout bridge exist."}
{"row_type":"residual_contribution","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"life_insurance_spike_and_bank_rate_PBR_price_MFE_overcredit_without_insurance_reserve_capital_payout_bridge","contribution":"Adds two C22 4B/cross-label counterexamples against one P&C insurance reserve/capital-return positive-watch, avoiding C22 top-covered and recent R6 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_INSURANCE_LOSS_RATIO_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_SPIKE_AND_BANK_RATE_CROSSLABEL","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C22 now has non-top-symbol P&C insurance positive-watch, one life-insurance post-spike weak-bridge counterexample, and one bank financial-holding cross-label price-MFE counterexample; next R6 C22 loops should exact-URL repair loss ratio, reserve/CSM quality, solvency capital, payout policy and cash-return evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_loss_ratio_reserve_CSM_capital_payout_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"001450 supports Yellow-watch only when loss-ratio/reserve/capital-return proxy exists; 085620 and 138930 fail as C22 positives when reserve/CSM/payout evidence is missing."}
{"row_type":"shadow_weight","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_life_insurance_post_spike_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"085620 shows post-spike life-insurance entries can have near-zero MFE and deep MAE without durable reserve/capital bridge."}
{"row_type":"shadow_weight","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_cross_label_bank_rate_PBR_price_MFE_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"138930 shows price MFE from bank/rate/PBR value-up should not validate C22 insurance reserve mechanics."}
{"row_type":"shadow_weight","round":"R6","loop":"92","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_moderate_MFE_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"001450 is a constructive positive-watch but MFE90 is moderate; Green requires exact loss-ratio/reserve/capital-return evidence."}
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
  - life_insurance_post_spike_overcredit
  - bank_financial_holding_rate_PBR_cross_label_overcredit
  - insurance_reserve_CSM_bridge_missing
  - payout_capital_return_bridge_missing
  - moderate_MFE_Green_strict_watch
new_axis_proposed:
  - C22_loss_ratio_reserve_CSM_capital_payout_bridge_required_shadow_only
  - C22_life_insurance_post_spike_local_4B_guard_shadow_only
  - C22_cross_label_bank_rate_PBR_price_MFE_guard_shadow_only
  - C22_moderate_MFE_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C22
  - full_4b_requires_non_price_evidence within C22
  - hard_4c_thesis_break_routes_to_4c within C22
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.
`001450`, `085620`, and `138930` have older corporate-action/name-transition candidates before 2024; those candidates are outside selected 2024 windows.
`138930` is a cross-label financial-holding stress row and must not be double-counted as a C21 contribution from this MD.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
cross_label_stress_only = true for 138930
promotion should prefer hold / evidence repair until exact URLs are added
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
5. Confirm this loop avoided:
   - C22 top-covered symbols
   - previous R6 loop87 C21 symbols
   - previous R6 loop88 C22 symbols
   - previous R6 loop89 C21 symbols
   - previous R6 loop90 C22 symbols
   - previous R6 loop91 C21 symbols
6. Confirm stale R5/C18, R4/C16, R3/C14 and R2/C08 candidate rows are not ingested from this MD.
7. Treat 138930 as C22 cross-label failure-mode stress only, not as a duplicate C21 contribution.
8. If aggregate support remains stable after exact evidence URL repair, consider C22-scoped safe patch candidates:
   - C22_loss_ratio_reserve_CSM_capital_payout_bridge_required
   - C22_life_insurance_post_spike_local_4B_guard
   - C22_cross_label_bank_rate_PBR_price_MFE_guard
   - C22_moderate_MFE_Green_strict_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 92
next_round = R7
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive-watch, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.
```
