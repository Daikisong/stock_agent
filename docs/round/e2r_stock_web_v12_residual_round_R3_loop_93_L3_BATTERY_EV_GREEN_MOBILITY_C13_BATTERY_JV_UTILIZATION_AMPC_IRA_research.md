# E2R Stock-Web v12 Residual Research — R3 Loop 93 / L3 / C13

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 93
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: CATHODE_JV_UTILIZATION_IRA_BRIDGE_VS_AMPC_HOLDCO_AND_ELECTROLYTE_CAPACITY_VOCABULARY_DECAY
sector: battery / EV / cathode / JV / utilization / AMPC / IRA / localization / electrolyte / capacity / margin / FCF
output_file: e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19, C27, C24 and C12.

```text
selected_round = R3
selected_loop = 93
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

Reason for selecting C13:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 / under-30 snapshot used as duplicate-avoidance ledger:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 27 rows / need_to_30 = 3
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 27 rows / need_to_30 = 3
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 29 rows / need_to_30 = 1
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION = 29 rows / need_to_30 = 1
```

C12 was just brought to the 30-row minimum-stability threshold in the previous valid local output. C13 can also reach the 30-row minimum threshold with exactly three additional representative rows.

This loop avoids recent R3 symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
R3 loop90 C12: 114190, 450080, 417200
R3 loop91 C13: 036830, 014820, 095500
R3 loop92 C14: 006110, 101360, 282880
R3 loop93 C11: 348370, 121600, 020150
R3 loop93 C12: 373220, 006400, 005070
```

Candidate hygiene note:

```text
During this execution path, a stale C12 candidate set was touched first.
Those rows are not used in this C13 output.
```

Selected symbols:

```text
003670, 086520, 278280
```

The selected pocket is:

```text
cathode JV / utilization / IRA-localization reset positive-watch
vs
AMPC/IRA holding-company and cathode-cycle vocabulary without direct JV utilization/margin/FCF bridge
vs
electrolyte capacity/JV vocabulary with market-segment change and missing utilization/margin/FCF bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"003670","company_name":"포스코퓨처엠","profile_path":"atlas/symbol_profiles/003/003670.json","first_date":"2001-11-01","last_date":"2026-02-20","trading_day_count":5985,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-05-04","2021-02-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"086520","company_name":"에코프로","profile_path":"atlas/symbol_profiles/086/086520.json","first_date":"2007-07-20","last_date":"2026-02-20","trading_day_count":4552,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2007-08-02","2009-06-09","2021-11-19","2024-04-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-04-25 corporate-action/share-count candidate is inside the 2024 row stream. Use only as data-quality/cross-label stress unless post-event price path is repaired.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"post_2024-04-25_window_usable_as_data_quality_watch"}
{"row_type":"price_source_validation","symbol":"278280","company_name":"천보","profile_path":"atlas/symbol_profiles/278/278280.json","first_date":"2019-02-11","last_date":"2026-02-20","trading_day_count":1727,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Market history includes KOSDAQ GLOBAL through 2024-06-13 and KOSDAQ thereafter; keep market-segment watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; market_segment_change_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"003670","trigger_type":"Stage2-Actionable-CathodeJVUtilizationIRALocalizationBridge-PositiveWatch","entry_date":"2024-01-25","duplicate_status":"new C13 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"086520","trigger_type":"Stage2-FalsePositive-AMPCHoldcoCathodeCycleVocabularyNoDirectJVUtilizationMarginBridge","entry_date":"2024-04-26","duplicate_status":"new C13 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 symbols; 2024-04-25 CA/share-count watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"278280","trigger_type":"Stage2-FalsePositive-ElectrolyteCapacityJVVocabularyNoUtilizationMarginFCFBridge","entry_date":"2024-02-08","duplicate_status":"new C13 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 symbols; market-segment watch"}
```

## 4. Research question

C13 is not “IRA/AMPC/JV 단어가 있다.”
The useful JV/utilization/AMPC signal must prove the subsidy-to-cash chain:

```text
qualified plant / JV / customer relationship
utilization or ramp schedule
eligible production volume
AMPC / IRA economics
ASP or pass-through discipline
yield and conversion cost
gross-margin / operating-margin bridge
working-capital discipline
FCF conversion
funding or dilution risk containment
```

An AMPC headline without this bridge is a tax-credit stamp on an idle machine. The stamp has value only if the line runs, ships qualified volume, protects margin, and converts to cash.

Residual question:

```text
Can C13 distinguish:
1. cathode JV/utilization reset that can support positive-watch,
2. AMPC/IRA holding-company or cathode-cycle vocabulary where direct utilization/margin/FCF bridge is missing,
3. electrolyte capacity/JV vocabulary where segment-change and deep drawdown block promotion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C13_R3L93_003670_POSCO_FUTUREM_JV_UTILIZATION","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_JV_UTILIZATION_IRA_LOCALIZATION_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CathodeJVUtilizationIRALocalizationBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_high_MFE90_low_initial_MAE_but_late_utilization_drawdown","current_profile_verdict":"current_profile_correct_if_JV_utilization_IRA_margin_FCF_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"After an early-2024 battery-material reset, cathode/JV/IRA-localization proxy produced high MFE90 and low initial MAE. Later utilization-cycle drawdown keeps this positive-watch only unless exact JV, ramp, margin and FCF evidence is repaired."}
{"row_type":"case","case_id":"C13_R3L93_086520_ECOPRO_AMPC_HOLDCO_DECAY","symbol":"086520","company_name":"에코프로","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_HOLDCO_CATHODE_CYCLE_VOCABULARY_WITHOUT_DIRECT_JV_UTILIZATION_MARGIN_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AMPCHoldcoCathodeCycleVocabularyNoDirectJVUtilizationMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"counterexample_low_MFE_deep_MAE_CA_share_count_watch_no_direct_utilization_bridge","current_profile_verdict":"current_profile_false_positive_if_AMPC_holdco_or_cathode_cycle_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"AMPC/IRA and cathode-cycle vocabulary after the 2024 share-count/corporate-action candidate had weak forward MFE and deep drawdown without direct JV utilization, eligible-volume, margin or FCF bridge."}
{"row_type":"case","case_id":"C13_R3L93_278280_CHUNBO_ELECTROLYTE_CAPACITY_DECAY","symbol":"278280","company_name":"천보","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_CAPACITY_JV_VOCABULARY_WITHOUT_UTILIZATION_MARGIN_FCF_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ElectrolyteCapacityJVVocabularyNoUtilizationMarginFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_market_segment_watch_no_utilization_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_electrolyte_capacity_JV_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Electrolyte capacity/JV vocabulary had low MFE and extreme later MAE without utilization, eligible volume, margin or FCF bridge. Market-segment change requires repair."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 003670 포스코퓨처엠 — cathode JV / utilization / IRA-localization bridge positive-watch

Entry row: `2024-01-25 c=251000`, after the January battery-material selloff.
Observed path: local high `2024-03-04 h=336500`, low initial drawdown `2024-02-01 l=240500`, and later full-cycle drawdown to `2024-08-05 l=195500`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C13_003670_20240125_STAGE2_CATHODE_JV_UTILIZATION_IRA","case_id":"C13_R3L93_003670_POSCO_FUTUREM_JV_UTILIZATION","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_JV_UTILIZATION_IRA_LOCALIZATION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CathodeJVUtilizationIRALocalizationBridge-PositiveWatch","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":251000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cathode_JV_utilization_IRA_localization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cathode JV/localization, eligible volume, utilization recovery, margin and FCF bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cathode_JV_proxy","IRA_localization_proxy","utilization_recovery_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_JV_customer_source_pending","utilization_ramp_source_pending","eligible_volume_AMPC_source_pending","margin_FCF_bridge_pending"],"stage4b_evidence_fields":["late_drawdown_watch","Green_strict_watch"],"stage4c_evidence_fields":["utilization_reversal_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.88,"MFE_90D_pct":34.06,"MFE_180D_pct":34.06,"MAE_30D_pct":-4.18,"MAE_90D_pct":-4.18,"MAE_180D_pct":-22.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-04","peak_price":336500.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":195500.0,"drawdown_after_peak_pct":-41.90,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_JV_utilization_eligible_volume_margin_FCF_evidence_and_late_drawdown_review","four_b_evidence_type":["late_drawdown_watch","Green_strict_watch"],"four_c_protection_label":"utilization_reversal_watch_only","trigger_outcome_label":"positive_watch_high_MFE90_low_initial_MAE_but_late_utilization_drawdown","current_profile_verdict":"current_profile_correct_if_JV_utilization_IRA_margin_FCF_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"003670_2024-01-25_251000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 can allow Yellow/positive-watch when JV/localization strength is tied to utilization ramp, eligible volume, AMPC/IRA economics, margin and FCF. Late drawdown and source-proxy evidence block automatic Green."}
```

### 6.2 086520 에코프로 — AMPC/IRA holdco or cathode-cycle vocabulary without direct utilization bridge

Entry row: `2024-04-26 c=106000`, after the 2024-04-25 share-count/corporate-action candidate.
Observed path: local high `2024-06-07 h=109200`, then decline to `2024-08-05 l=80400`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C13_086520_20240426_STAGE2_FALSE_POSITIVE_AMPC_HOLDCO","case_id":"C13_R3L93_086520_ECOPRO_AMPC_HOLDCO_DECAY","symbol":"086520","company_name":"에코프로","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_HOLDCO_CATHODE_CYCLE_VOCABULARY_WITHOUT_DIRECT_JV_UTILIZATION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AMPCHoldcoCathodeCycleVocabularyNoDirectJVUtilizationMarginBridge","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":106000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AMPC_IRA_holdco_cathode_cycle_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AMPC/IRA holding-company and cathode-cycle vocabulary treated as insufficient without direct JV utilization, eligible volume, margin and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AMPC_IRA_vocabulary","cathode_cycle_keyword","holdco_exposure_keyword"],"stage3_evidence_fields":["direct_JV_utilization_missing","eligible_volume_missing","margin_cash_bridge_missing","share_count_repair_pending"],"stage4b_evidence_fields":["low_MFE","deep_MAE","CA_share_count_watch","direct_utilization_bridge_missing_watch"],"stage4c_evidence_fields":["utilization_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086520/2024.csv","profile_path":"atlas/symbol_profiles/086/086520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.02,"MFE_90D_pct":3.02,"MFE_180D_pct":3.02,"MAE_30D_pct":-14.81,"MAE_90D_pct":-24.15,"MAE_180D_pct":-24.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":109200.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":80400.0,"drawdown_after_peak_pct":-26.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.03,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"AMPC_IRA_holdco_or_cathode_cycle_vocabulary_without_direct_JV_utilization_margin_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","deep_MAE","CA_share_count_watch","direct_utilization_bridge_missing_watch"],"four_c_protection_label":"utilization_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_CA_share_count_watch_no_direct_utilization_bridge","current_profile_verdict":"current_profile_false_positive_if_AMPC_holdco_or_cathode_cycle_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-04-25_corporate_action_share_count_candidate_watch","holdco_not_direct_JV_utilization_bridge"],"corporate_action_window_status":"selected_entry_after_2024-04-25_candidate; data_quality_watch","same_entry_group_id":"086520_2024-04-26_106000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should not promote AMPC/IRA or cathode-cycle vocabulary unless direct JV utilization, eligible production volume, margin and FCF evidence are repaired. 2024 share-count candidate requires data-quality repair."}
```

### 6.3 278280 천보 — electrolyte capacity/JV vocabulary without utilization / margin / FCF bridge

Entry row: `2024-02-08 c=95000`, after a battery-material rebound.
Observed path: local high `2024-02-21 h=99800`, then persistent decline to `2024-11-15 l=35500`. The market segment changes from KOSDAQ GLOBAL to KOSDAQ after mid-June.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C13_278280_20240208_STAGE2_FALSE_POSITIVE_ELECTROLYTE_CAPACITY","case_id":"C13_R3L93_278280_CHUNBO_ELECTROLYTE_CAPACITY_DECAY","symbol":"278280","company_name":"천보","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_CAPACITY_JV_VOCABULARY_WITHOUT_UTILIZATION_MARGIN_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;market_segment_change_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ElectrolyteCapacityJVVocabularyNoUtilizationMarginFCFBridge","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":95000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_electrolyte_capacity_JV_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; electrolyte capacity/JV vocabulary treated as insufficient without utilization ramp, eligible volume, ASP/margin and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["electrolyte_capacity_keyword","JV_vocabulary","battery_material_recovery_vocabulary"],"stage3_evidence_fields":["utilization_ramp_missing","eligible_volume_missing","ASP_margin_bridge_missing","FCF_bridge_missing"],"stage4b_evidence_fields":["low_MFE","extreme_MAE","market_segment_change_watch","utilization_margin_FCF_bridge_missing_watch"],"stage4c_evidence_fields":["utilization_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.05,"MFE_90D_pct":5.05,"MFE_180D_pct":5.05,"MAE_30D_pct":-12.53,"MAE_90D_pct":-14.84,"MAE_180D_pct":-62.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":99800.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":35500.0,"drawdown_after_peak_pct":-64.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"electrolyte_capacity_JV_vocabulary_without_utilization_ASP_margin_FCF_bridge_should_be_4B_watch_not_C13_positive","four_b_evidence_type":["low_MFE","extreme_MAE","market_segment_change_watch","utilization_margin_FCF_bridge_missing_watch"],"four_c_protection_label":"utilization_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_market_segment_watch_no_utilization_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_electrolyte_capacity_JV_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_GLOBAL_to_KOSDAQ_after_2024-06-13"],"corporate_action_window_status":"clean; market_segment_change_watch","same_entry_group_id":"278280_2024-02-08_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should not count electrolyte capacity/JV vocabulary as AMPC/JV utilization evidence unless utilization ramp, eligible volume, ASP/margin and FCF evidence are exact-repaired. Market-segment rows require repair."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L93_003670_POSCO_FUTUREM_JV_UTILIZATION","trigger_id":"R3L93_C13_003670_20240125_STAGE2_CATHODE_JV_UTILIZATION_IRA","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C13 requires JV utilization, eligible volume, AMPC/IRA economics, margin and FCF bridge rather than IRA vocabulary alone","raw_component_scores_before":{"JV_customer_quality_score":11,"utilization_ramp_score":10,"eligible_volume_score":9,"AMPC_IRA_economics_score":8,"ASP_pass_through_score":8,"yield_conversion_cost_score":7,"margin_bridge_score":8,"FCF_bridge_score":6,"relative_strength_score":10,"funding_dilution_risk":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"JV_customer_quality_score":14,"utilization_ramp_score":13,"eligible_volume_score":12,"AMPC_IRA_economics_score":10,"ASP_pass_through_score":10,"yield_conversion_cost_score":9,"margin_bridge_score":10,"FCF_bridge_score":8,"relative_strength_score":12,"funding_dilution_risk":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Cathode/JV/localization bridge supports Yellow-watch; late drawdown and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L93_086520_ECOPRO_AMPC_HOLDCO_DECAY","trigger_id":"R3L93_C13_086520_20240426_STAGE2_FALSE_POSITIVE_AMPC_HOLDCO","symbol":"086520","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"AMPC/IRA holding-company vocabulary without direct utilization and FCF bridge should be blocked","raw_component_scores_before":{"JV_customer_quality_score":1,"utilization_ramp_score":0,"eligible_volume_score":0,"AMPC_IRA_economics_score":2,"ASP_pass_through_score":0,"yield_conversion_cost_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":1,"funding_dilution_risk":-12,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"JV_customer_quality_score":0,"utilization_ramp_score":0,"eligible_volume_score":0,"AMPC_IRA_economics_score":0,"ASP_pass_through_score":0,"yield_conversion_cost_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":0,"funding_dilution_risk":-22,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Low MFE, deep MAE and CA/share-count watch require direct utilization and margin/FCF evidence before any promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L93_278280_CHUNBO_ELECTROLYTE_CAPACITY_DECAY","trigger_id":"R3L93_C13_278280_20240208_STAGE2_FALSE_POSITIVE_ELECTROLYTE_CAPACITY","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"electrolyte capacity/JV vocabulary without utilization, ASP/margin and FCF bridge should remain Watch/4B","raw_component_scores_before":{"JV_customer_quality_score":1,"utilization_ramp_score":0,"eligible_volume_score":0,"AMPC_IRA_economics_score":0,"ASP_pass_through_score":0,"yield_conversion_cost_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":2,"funding_dilution_risk":-10,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"JV_customer_quality_score":0,"utilization_ramp_score":0,"eligible_volume_score":0,"AMPC_IRA_economics_score":0,"ASP_pass_through_score":0,"yield_conversion_cost_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":0,"funding_dilution_risk":-18,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Low MFE, extreme MAE and market-segment change require utilization and FCF evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L93_C13_P0_CURRENT","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C13 needs explicit JV utilization, eligible volume, AMPC economics, ASP/margin, FCF, and data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":14.04,"avg_MAE90_pct":-14.39,"avg_MFE180_pct":14.04,"avg_MAE180_pct":-36.30,"false_positive_rate":0.67,"data_quality_watch_count":2,"score_return_alignment_verdict":"mixed_without_C13_JV_utilization_AMPC_margin_FCF_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C13_P1_SECTOR_SPECIFIC","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P1_L3_battery_JV_utilization_AMPC_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 JV/AMPC signals need JV/customer quality, utilization ramp, eligible volume, ASP pass-through, margin or FCF conversion before Stage2-Actionable","changed_axes":["JV_utilization_required","eligible_volume_AMPC_required","margin_FCF_required","data_quality_guard"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_JV_quality_utilization_eligible_volume_margin_or_FCF_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C13_P2_CANONICAL","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P2_C13_JV_utilization_AMPC_margin_FCF_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C13 should reward utilization-to-AMPC/FCF mechanics, not AMPC/IRA/JV vocabulary","changed_axes":["C13_JV_utilization_eligible_volume_margin_FCF_bridge_required","C13_AMPC_holdco_electrolyte_capacity_vocabulary_local_4B_guard","C13_CA_share_count_market_segment_data_quality_guard","C13_late_drawdown_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"JV_or_customer_quality_plus_utilization_or_eligible_volume_margin_FCF_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C13_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P3_C13_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If utilization/FCF bridge is missing, MFE90<10 or MAE180<=-25 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C13_low_MFE_guardrail","C13_deep_MAE_4B_guardrail","C13_data_quality_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus25)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_CATHODE_JV_POSITIVE_VS_AMPC_HOLDCO_ELECTROLYTE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":2,"avg_MFE90_pct":14.04,"avg_MAE90_pct":-14.39,"avg_MFE180_pct":14.04,"avg_MAE180_pct":-36.30,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C13 needs utilization discipline. 포스코퓨처엠 shows cathode/JV/localization bridge can support Yellow/positive-watch after reset, while 에코프로 and 천보 show AMPC/IRA, holdco, cathode-cycle or electrolyte-capacity vocabulary should not be promoted without direct utilization, eligible volume, margin and FCF evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"003670","trigger_type":"Stage2-Actionable-CathodeJVUtilizationIRALocalizationBridge-PositiveWatch","entry_date":"2024-01-25","stage2_to_90D_outcome":"positive_watch_high_MFE90_low_initial_MAE","stage2_to_180D_outcome":"JV_utilization_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/positive-watch when JV/localization connects to utilization, eligible volume, margin and FCF; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"086520","trigger_type":"Stage2-FalsePositive-AMPCHoldcoCathodeCycleVocabularyNoDirectJVUtilizationMarginBridge","entry_date":"2024-04-26","stage2_to_90D_outcome":"bad_stage2_low_MFE_data_quality_watch","stage2_to_180D_outcome":"failed_AMPC_holdco_cathode_cycle_vocabulary_no_direct_utilization_bridge","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"AMPC/IRA or holdco vocabulary without direct utilization and margin/FCF bridge should remain Watch/4B; CA/share-count repair required."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"278280","trigger_type":"Stage2-FalsePositive-ElectrolyteCapacityJVVocabularyNoUtilizationMarginFCFBridge","entry_date":"2024-02-08","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_electrolyte_capacity_JV_extreme_MAE_market_segment_watch","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Electrolyte capacity/JV vocabulary without utilization and FCF bridge should stay Watch/4B; market-segment repair required."}
{"row_type":"residual_contribution","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_type":"AMPC_IRA_JV_vocabulary_overcredit_without_direct_utilization_margin_FCF_bridge","contribution":"Adds two C13 4B counterexamples against one cathode/JV utilization positive-watch, bringing C13 from 27 toward the 30-row minimum stability threshold.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_JV_UTILIZATION_IRA_BRIDGE_VS_AMPC_HOLDCO_AND_ELECTROLYTE_CAPACITY_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C13 now has one cathode/JV utilization positive-watch and two AMPC/electrolyte weak-bridge counterexamples; next C13 loops should exact-URL repair JV/customer quality, utilization ramp, eligible volume, AMPC/IRA economics, ASP/margin and FCF evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_JV_utilization_eligible_volume_margin_FCF_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"003670 worked only as positive-watch when cathode/JV/utilization proxy existed; 086520 and 278280 failed when direct utilization/margin/FCF evidence was missing."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_AMPC_holdco_electrolyte_capacity_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"086520 and 278280 showed low MFE and deep MAE when AMPC/IRA, holdco or electrolyte capacity vocabulary lacked direct utilization and FCF bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_CA_share_count_market_segment_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"086520 has 2024-04-25 corporate-action/share-count candidate and 278280 has market-segment change; production patching requires price-path/evidence repair."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"003670 had high MFE90 but later drawdown; Green requires exact utilization, eligible-volume and FCF evidence."}
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
  - AMPC_IRA_vocabulary_overcredit
  - holdco_cathode_cycle_vocabulary_overcredit
  - electrolyte_capacity_JV_vocabulary_overcredit
  - direct_utilization_bridge_missing
  - margin_FCF_bridge_missing
  - CA_share_count_market_segment_data_quality_watch
new_axis_proposed:
  - C13_JV_utilization_eligible_volume_margin_FCF_bridge_required_shadow_only
  - C13_AMPC_holdco_electrolyte_capacity_vocabulary_local_4B_guard_shadow_only
  - C13_CA_share_count_market_segment_data_quality_guard_shadow_only
  - C13_late_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C13
  - full_4b_requires_non_price_evidence within C13
  - hard_4c_thesis_break_routes_to_4c within C13
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`003670` has historical corporate-action/name-transition candidates before the selected 2024 window; selected 2024 window is usable.
`086520` has a 2024-04-25 corporate-action/share-count candidate immediately before the selected entry, so it remains data-quality watch before production patching.
`278280` has no corporate-action candidate, but market segment shifts from KOSDAQ GLOBAL to KOSDAQ after 2024-06-13, so it remains market-segment data-quality watch.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
CA_share_count_watch = true for 086520
market_segment_change_watch = true for 278280
promotion should prefer hold / exact evidence repair until exact URLs are added
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
3. Confirm R3 / L3 / C13 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first and brings C13 closer to the 30-row minimum stability threshold.
6. Confirm this loop avoided:
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
   - previous R3 loop88 C14 symbols
   - previous R3 loop89 C11 symbols
   - previous R3 loop90 C12 symbols
   - previous R3 loop91 C13 symbols
   - previous R3 loop92 C14 symbols
   - previous R3 loop93 C11 symbols
   - previous R3 loop93 C12 symbols
7. Confirm stale C12 candidate rows touched earlier in the execution path are not ingested from this MD.
8. Keep 086520 in CA/share-count data-quality watch before patch consideration.
9. Keep 278280 in market-segment data-quality watch before patch consideration.
10. Treat 003670 as Yellow/positive-watch only, not Green, until exact JV/utilization/eligible-volume/margin/FCF evidence is repaired.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C13-scoped safe patch candidates:
   - C13_JV_utilization_eligible_volume_margin_FCF_bridge_required
   - C13_AMPC_holdco_electrolyte_capacity_vocabulary_local_4B_guard
   - C13_CA_share_count_market_segment_data_quality_guard
   - C13_late_drawdown_Green_strict_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION or C17_CHEMICAL_COMMODITY_MARGIN_SPREAD or C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION depending on newest coverage pressure and recent-loop avoidance
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 cathode/JV utilization positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
```
