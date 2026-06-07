# E2R Stock-Web v12 Residual Research — R11 Loop 92 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 92
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: CLEANROOM_EPC_ORDER_MARGIN_BRIDGE_VS_SMALL_EPC_ENGINEERING_LATE_SPIKE_NONVALIDATION
sector: industrials / infrastructure / EPC / cleanroom / engineering service / mega contract / working capital / margin gap
output_file: e2r_stock_web_v12_residual_round_R11_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 92`.

```text
scheduled_round = R11
scheduled_loop = 92
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

R11 is the L1 industrial / infrastructure / defense / grid policy lane.
C05 is selected because R11 loop91 used C04 nuclear policy / project delay and the L1 rotation returns to EPC mega-contract margin-gap residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows = 33
need_to_50 = 17
priority_note = Mega EPC 계약, 원가초과, working capital, margin gap
```

This loop avoids known recent L1/C05 and adjacent L1 symbols:

```text
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R11 loop89 C02: 229640, 199820, 006910
R11 loop90 C03: 272210, 095190, 218410
R11 loop91 C04: 126720, 457550, 036190
R1 loop89 C03: 064350, 099320, 214430
R1 loop90 C04: 130660, 105840, 019990
R1 loop91 C05: 100840, 028050, 037350
R1 loop92 C02: 267260, 037030, 237750
```

Candidate hygiene note:

```text
During this execution path, stale R10/C30, R8/C28, R7/C25 and earlier-sector candidate rows were touched while checking alternatives.
Those rows are not used in this R11/C05 output.
```

Selected symbols:

```text
011930, 023960, 023350
```

The selected pocket is:

```text
cleanroom / industrial EPC order-conversion and margin bridge positive-watch
vs
small plant EPC vocabulary where later price spike does not validate original weak order-margin bridge
vs
engineering-service / policy-project vocabulary where later high needs fresh trigger evidence, not old entry validation
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"011930","company_name":"신성이엔지","profile_path":"atlas/symbol_profiles/011/011930.json","first_date":"1996-07-01","last_date":"2026-02-20","trading_day_count":7370,"corporate_action_candidate_count":10,"corporate_action_candidate_dates":["1997-01-03","1997-06-21","1998-05-23","1999-04-26","2008-09-01","2009-02-27","2013-01-07","2015-01-07","2016-05-31","2017-01-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"023960","company_name":"에쓰씨엔지니어링","profile_path":"atlas/symbol_profiles/023/023960.json","first_date":"1997-06-23","last_date":"2026-02-20","trading_day_count":7108,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1999-04-26","2005-11-11","2006-07-31","2018-03-28","2018-04-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window. Late 2024 price spike is not used to validate original weak entry without fresh trigger evidence.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; late_spike_nonvalidation_watch"}
{"row_type":"price_source_validation","symbol":"023350","company_name":"한국종합기술","profile_path":"atlas/symbol_profiles/023/023350.json","first_date":"2011-04-28","last_date":"2026-02-20","trading_day_count":3642,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"No corporate-action candidate in profile. Late December policy/project spike is treated as fresh-trigger-required, not original-entry validation.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; late_spike_nonvalidation_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"011930","trigger_type":"Stage2-Actionable-CleanroomEPCOrderMarginBridge-PositiveWatch","entry_date":"2024-01-29","duplicate_status":"new C05 symbol/trigger/date combination outside recent L1/C05 and adjacent L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"023960","trigger_type":"Stage2-FalsePositive-SmallPlantEPCVocabularyLateSpikeNoOriginalOrderMarginBridge","entry_date":"2024-01-29","duplicate_status":"new C05 symbol/trigger/date combination outside recent L1/C05 and adjacent L1 loop symbols; late spike requires fresh trigger evidence"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"023350","trigger_type":"Stage2-FalsePositive-EngineeringServicePolicyProjectVocabularyLateSpikeNoOriginalMarginBridge","entry_date":"2024-01-10","duplicate_status":"new C05 symbol/trigger/date combination outside recent L1/C05 and adjacent L1 loop symbols; late spike requires fresh trigger evidence"}
```

## 4. Research question

C05 is not “EPC / 수주 / 플랜트 단어가 있다.”
The useful C05 signal must prove the order-to-margin chain:

```text
signed order or credible LOA / NTP
customer identity and project scope
delivery / construction schedule
pass-through or escalation clause
working-capital discipline
cost overrun containment
gross-margin / operating-margin bridge
cash collection
```

A mega-contract headline without this bridge is a crane on the skyline with no cost ledger attached. E2R needs the signed scope, schedule, cost pass-through, working capital, margin, and cash.

Residual question:

```text
Can C05 distinguish:
1. cleanroom / industrial EPC order-conversion and margin bridge that deserves only positive-watch,
2. small plant EPC vocabulary where a later price spike does not repair the original weak order-margin entry,
3. engineering-service / policy-project vocabulary where late high needs a fresh trigger and fresh evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C05_R11L92_011930_SHINSUNG_CLEANROOM_EPC","symbol":"011930","company_name":"신성이엔지","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CLEANROOM_EPC_ORDER_CONVERSION_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CleanroomEPCOrderMarginBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_MFE90_ge30_low_entry_MAE_but_late_drawdown_EPC_margin_bridge","current_profile_verdict":"current_profile_correct_if_signed_order_delivery_cost_pass_through_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Cleanroom/industrial EPC order-conversion proxy produced MFE90 above 30 with low early MAE, but later drawdown keeps it positive-watch only unless exact order, delivery, margin and cash evidence are repaired."}
{"row_type":"case","case_id":"C05_R11L92_023960_SCENG_SMALL_PLANT_EPC_LATE_SPIKE","symbol":"023960","company_name":"에쓰씨엔지니어링","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SMALL_PLANT_EPC_VOCABULARY_LATE_SPIKE_WITHOUT_ORIGINAL_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallPlantEPCVocabularyLateSpikeNoOriginalOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_late_spike_not_original_entry_validation_deep_full_window_MAE","current_profile_verdict":"current_profile_false_positive_if_late_spike_validates_original_small_EPC_vocabulary_entry","price_source":"Songdaiki/stock-web","notes":"Small plant EPC vocabulary had weak original bridge and later Q3/Q4 spike. The late spike needs a fresh trigger and cannot retroactively validate the original order/margin evidence."}
{"row_type":"case","case_id":"C05_R11L92_023350_KOREA_ENGINEERING_POLICY_PROJECT","symbol":"023350","company_name":"한국종합기술","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"ENGINEERING_SERVICE_POLICY_PROJECT_VOCABULARY_WITHOUT_SIGNED_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EngineeringServicePolicyProjectVocabularyLateSpikeNoOriginalMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_policy_project_vocabulary_late_spike_not_original_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_engineering_policy_project_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Engineering-service / policy-project vocabulary had weak original bridge and a later December spike. Without signed project scope, schedule, margin and working-capital bridge at entry, it remains 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 011930 신성이엔지 — cleanroom / industrial EPC order-conversion margin bridge positive-watch

Entry row: `2024-01-29 c=1948`.
Observed path: low `2024-01-30 l=1914`, peak `2024-03-29 h=2545`, and later full-window drawdown to `2024-12-09 l=1030`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L92_C05_011930_20240129_STAGE2_CLEANROOM_EPC_ORDER_MARGIN","case_id":"C05_R11L92_011930_SHINSUNG_CLEANROOM_EPC","symbol":"011930","company_name":"신성이엔지","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CLEANROOM_EPC_ORDER_CONVERSION_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CleanroomEPCOrderMarginBridge-PositiveWatch","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1948.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cleanroom_industrial_EPC_order_conversion_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cleanroom/EPC order conversion, delivery schedule, cost pass-through, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cleanroom_EPC_order_proxy","industrial_capex_customer_proxy","delivery_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_signed_order_source_pending","project_scope_source_pending","cost_pass_through_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["MFE90_ge30_watch","late_drawdown_watch","Green_strict_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011930/2024.csv","profile_path":"atlas/symbol_profiles/011/011930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.37,"MFE_90D_pct":30.65,"MFE_180D_pct":30.65,"MAE_30D_pct":-1.75,"MAE_90D_pct":-1.75,"MAE_180D_pct":-26.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":2545.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1030.0,"drawdown_after_peak_pct":-59.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.40,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_signed_order_delivery_cost_pass_through_margin_cash_evidence","four_b_evidence_type":["MFE90_ge30_watch","late_drawdown_watch","Green_strict_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_watch_MFE90_ge30_low_entry_MAE_but_late_drawdown_EPC_margin_bridge","current_profile_verdict":"current_profile_correct_if_signed_order_delivery_cost_pass_through_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"011930_2024-01-29_1948","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 can allow Yellow/positive-watch when EPC strength is tied to signed order, customer scope, delivery schedule, cost pass-through, margin and cash conversion. Late drawdown and proxy-only evidence block Green."}
```

### 6.2 023960 에쓰씨엔지니어링 — small plant EPC vocabulary / late spike not original-entry validation

Entry row: `2024-01-29 c=1700`.
Observed path: original 90D path did not produce strong order-margin validation; later Q3/Q4 price spike to `2024-09-30 h=2450` and `2024-12-11 h=7510` needs a fresh trigger and fresh evidence.

```jsonl
{"row_type":"trigger","trigger_id":"R11L92_C05_023960_20240129_STAGE2_FALSE_POSITIVE_SMALL_EPC_LATE_SPIKE","case_id":"C05_R11L92_023960_SCENG_SMALL_PLANT_EPC_LATE_SPIKE","symbol":"023960","company_name":"에쓰씨엔지니어링","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SMALL_PLANT_EPC_VOCABULARY_LATE_SPIKE_WITHOUT_ORIGINAL_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_spike_not_entry_validation","trigger_type":"Stage2-FalsePositive-SmallPlantEPCVocabularyLateSpikeNoOriginalOrderMarginBridge","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_small_plant_EPC_engineering_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small plant EPC vocabulary treated as insufficient without signed order, credible backlog, delivery schedule, cost pass-through, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["small_plant_EPC_keyword","engineering_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["signed_order_missing","credible_backlog_missing","cost_pass_through_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["weak_original_bridge","late_spike_not_entry_validation","full_window_MAE_expansion"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/023/023960/2024.csv","profile_path":"atlas/symbol_profiles/023/023960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":15.88,"MFE_180D_pct":44.12,"MAE_30D_pct":-9.82,"MAE_90D_pct":-13.76,"MAE_180D_pct":-13.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":2450.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1230.0,"drawdown_after_peak_pct":-49.80,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_EPC_late_spike_requires_fresh_trigger_and_fresh_order_margin_evidence; original_entry_remains_4B_watch","four_b_evidence_type":["weak_original_bridge","late_spike_not_entry_validation","full_window_MAE_expansion"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_late_spike_not_original_entry_validation_deep_full_window_MAE","current_profile_verdict":"current_profile_false_positive_if_late_spike_validates_original_small_EPC_vocabulary_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"023960_2024-01-29_1700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not let a late spike retroactively validate an original EPC entry that lacked signed order, backlog, cost pass-through, margin and cash evidence. A late move requires a fresh trigger date and fresh evidence."}
```

### 6.3 023350 한국종합기술 — engineering-service / policy-project vocabulary late spike non-validation

Entry row: `2024-01-10 c=5840`, on engineering / project-policy vocabulary.
Observed path: same-day high `2024-01-10 h=6790`, then range decay into Q4; a large December spike to `2024-12-13 h=7900` does not validate the original weak entry without fresh evidence.

```jsonl
{"row_type":"trigger","trigger_id":"R11L92_C05_023350_20240110_STAGE2_FALSE_POSITIVE_ENGINEERING_POLICY_PROJECT","case_id":"C05_R11L92_023350_KOREA_ENGINEERING_POLICY_PROJECT","symbol":"023350","company_name":"한국종합기술","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"ENGINEERING_SERVICE_POLICY_PROJECT_VOCABULARY_WITHOUT_SIGNED_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_spike_not_entry_validation","trigger_type":"Stage2-FalsePositive-EngineeringServicePolicyProjectVocabularyLateSpikeNoOriginalMarginBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":5840.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_engineering_service_policy_project_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; engineering-service / policy-project vocabulary treated as insufficient without signed scope, NTP, project schedule, margin and cash bridge","evidence_source_type":"historical_public_policy_project_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["engineering_service_keyword","policy_project_vocabulary","relative_strength_spike"],"stage3_evidence_fields":["signed_project_scope_missing","NTP_or_schedule_missing","cost_pass_through_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["same_day_spike_watch","late_spike_not_entry_validation","order_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/023/023350/2024.csv","profile_path":"atlas/symbol_profiles/023/023350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.27,"MFE_90D_pct":16.27,"MFE_180D_pct":16.27,"MAE_30D_pct":-4.62,"MAE_90D_pct":-7.53,"MAE_180D_pct":-25.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-10","peak_price":6790.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":4205.0,"drawdown_after_peak_pct":-38.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"engineering_policy_project_vocabulary_without_signed_scope_schedule_margin_cash_bridge_should_be_4B_watch; late_December_spike_needs_fresh_trigger","four_b_evidence_type":["same_day_spike_watch","late_spike_not_entry_validation","order_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_policy_project_vocabulary_late_spike_not_original_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_engineering_policy_project_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"023350_2024-01-10_5840","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not count engineering-policy vocabulary or same-day spikes as EPC margin validation. Signed scope, NTP/schedule, cost pass-through, margin and cash bridge are required before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R11L92_011930_SHINSUNG_CLEANROOM_EPC","trigger_id":"R11L92_C05_011930_20240129_STAGE2_CLEANROOM_EPC_ORDER_MARGIN","symbol":"011930","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C05 requires signed order, customer scope, delivery schedule, cost pass-through, working-capital discipline, margin and cash bridge rather than EPC vocabulary alone","raw_component_scores_before":{"signed_order_score":10,"customer_scope_score":9,"delivery_schedule_score":9,"cost_pass_through_score":7,"working_capital_score":7,"margin_bridge_score":8,"cash_conversion_score":6,"relative_strength_score":12,"valuation_repricing_score":6,"execution_risk_score":-6,"theme_spike_risk":-3,"information_confidence":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"signed_order_score":13,"customer_scope_score":12,"delivery_schedule_score":11,"cost_pass_through_score":9,"working_capital_score":9,"margin_bridge_score":10,"cash_conversion_score":8,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Cleanroom EPC order/margin bridge supports Yellow-watch; late drawdown and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R11L92_023960_SCENG_SMALL_PLANT_EPC_LATE_SPIKE","trigger_id":"R11L92_C05_023960_20240129_STAGE2_FALSE_POSITIVE_SMALL_EPC_LATE_SPIKE","symbol":"023960","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"small EPC vocabulary without original signed order and margin bridge should be blocked even if later price spike appears","raw_component_scores_before":{"signed_order_score":0,"customer_scope_score":1,"delivery_schedule_score":0,"cost_pass_through_score":0,"working_capital_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"signed_order_score":0,"customer_scope_score":0,"delivery_schedule_score":0,"cost_pass_through_score":0,"working_capital_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Original bridge missing; late Q3/Q4 spike needs fresh trigger evidence and cannot backfill original entry."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R11L92_023350_KOREA_ENGINEERING_POLICY_PROJECT","trigger_id":"R11L92_C05_023350_20240110_STAGE2_FALSE_POSITIVE_ENGINEERING_POLICY_PROJECT","symbol":"023350","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"engineering-service/policy-project vocabulary without signed scope and margin/cash bridge should remain Watch/4B","raw_component_scores_before":{"signed_order_score":0,"customer_scope_score":1,"delivery_schedule_score":0,"cost_pass_through_score":0,"working_capital_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":6,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"signed_order_score":0,"customer_scope_score":0,"delivery_schedule_score":0,"cost_pass_through_score":0,"working_capital_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Same-day/late price strength is not EPC margin validation without signed scope, schedule, margin and working-capital evidence."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L92_C05_P0_CURRENT","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C05 needs exact signed-order, delivery, cost-pass-through, working-capital, margin/cash and late-spike non-validation taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":20.93,"avg_MAE90_pct":-7.68,"avg_MFE180_pct":30.35,"avg_MAE180_pct":-21.67,"false_positive_rate":0.67,"late_spike_not_validation_count":2,"score_return_alignment_verdict":"mixed_without_C05_signed_order_margin_cash_bridge_and_late_spike_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L92_C05_P1_SECTOR_SPECIFIC","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P1_L1_EPC_order_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 EPC signals need signed order, customer/project scope, delivery schedule, cost pass-through, working-capital discipline, margin or cash conversion before Stage2-Actionable","changed_axes":["signed_order_required","delivery_cost_pass_through_required","late_spike_nonvalidation"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_signed_order_customer_scope_delivery_margin_or_cash_proxy","bad_entry_filter":"bridge_missing_and_late_spike_only"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L92_C05_P2_CANONICAL","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P2_C05_signed_order_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C05 should reward signed-order-to-margin mechanics, not EPC/engineering vocabulary or late price spikes","changed_axes":["C05_signed_order_delivery_margin_cash_bridge_required","C05_small_EPC_engineering_vocabulary_local_4B_guard","C05_late_spike_not_entry_validation_guard","C05_Green_exact_evidence_guard"],"changed_thresholds":{"stage2_yellow_gate":"signed_order_or_customer_scope_plus_delivery_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L92_C05_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P3_C05_bridge_missing_late_spike_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If signed-order/margin bridge is missing, MFE90<20 or late-spike-only behavior blocks Yellow/Green and routes to Watch/4B","changed_axes":["C05_low_MFE_guardrail","C05_late_spike_only_guardrail","C05_working_capital_missing_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_late_spike_only_or_MAE180_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_CLEANROOM_EPC_POSITIVE_VS_SMALL_EPC_ENGINEERING_LATE_SPIKE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"late_spike_not_validation_count":2,"avg_MFE90_pct":20.93,"avg_MAE90_pct":-7.68,"avg_MFE180_pct":30.35,"avg_MAE180_pct":-21.67,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C05 needs bridge discipline. 신성이엔지 shows cleanroom EPC/order-margin bridge can support Yellow/positive-watch, while 에쓰씨엔지니어링 and 한국종합기술 show EPC/engineering vocabulary and late price spikes should not be promoted without signed order, scope, delivery schedule, cost pass-through, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"011930","trigger_type":"Stage2-Actionable-CleanroomEPCOrderMarginBridge-PositiveWatch","entry_date":"2024-01-29","stage2_to_90D_outcome":"positive_watch_MFE90_ge30_low_entry_MAE","stage2_to_180D_outcome":"cleanroom_EPC_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/positive-watch when EPC strength is tied to signed order, delivery, cost-pass-through and margin/cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"023960","trigger_type":"Stage2-FalsePositive-SmallPlantEPCVocabularyLateSpikeNoOriginalOrderMarginBridge","entry_date":"2024-01-29","stage2_to_90D_outcome":"weak_stage2_bridge_missing","stage2_to_180D_outcome":"late_spike_requires_fresh_trigger_not_original_validation","MFE90_ge20":false,"late_spike_not_validation":true,"transition_note":"Small EPC vocabulary without signed order/margin bridge should stay Watch/4B-risk; later spike needs fresh trigger evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"023350","trigger_type":"Stage2-FalsePositive-EngineeringServicePolicyProjectVocabularyLateSpikeNoOriginalMarginBridge","entry_date":"2024-01-10","stage2_to_90D_outcome":"same_day_price_spike_without_signed_scope","stage2_to_180D_outcome":"engineering_policy_vocabulary_4B_watch_late_spike_not_validation","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Engineering/policy-project vocabulary without signed scope, NTP/schedule and margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"small_EPC_engineering_vocabulary_overcredit_and_late_spike_not_entry_validation_without_signed_order_margin_cash_bridge","contribution":"Adds two C05 4B counterexamples against one cleanroom EPC positive-watch, avoiding recent C05 and adjacent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CLEANROOM_EPC_ORDER_MARGIN_BRIDGE_VS_SMALL_EPC_ENGINEERING_LATE_SPIKE_NONVALIDATION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C05 now has non-recent cleanroom EPC positive-watch and two small-EPC/engineering weak-bridge late-spike non-validation counterexamples; next R11/C05 loops should exact-URL repair signed order, customer scope, delivery schedule, cost pass-through, working capital, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_signed_order_delivery_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"011930 supports Yellow-watch when cleanroom EPC order/margin proxy exists; 023960 and 023350 fail when EPC/engineering vocabulary lacks signed order, schedule, margin and cash evidence."}
{"row_type":"shadow_weight","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_small_EPC_engineering_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small EPC and engineering-service rows showed weak original bridge; price movement alone did not prove cost-pass-through or working-capital quality."}
{"row_type":"shadow_weight","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_late_spike_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"023960 and 023350 show late Q3/Q4 price spikes must use fresh trigger-date evidence and cannot backfill original weak entries."}
{"row_type":"shadow_weight","round":"R11","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_Green_exact_evidence_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"011930 is constructive but late drawdown and source-proxy evidence mean Green requires exact signed-order/margin/cash evidence."}
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
  - small_EPC_vocabulary_overcredit
  - engineering_policy_project_vocabulary_overcredit
  - signed_order_bridge_missing
  - cost_pass_through_margin_cash_bridge_missing
  - late_spike_not_entry_validation
new_axis_proposed:
  - C05_signed_order_delivery_margin_cash_bridge_required_shadow_only
  - C05_small_EPC_engineering_vocabulary_local_4B_guard_shadow_only
  - C05_late_spike_not_entry_validation_guard_shadow_only
  - C05_Green_exact_evidence_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`011930` and `023960` have only historical corporate-action/name-transition candidates before the selected 2024 windows.
`023350` has no corporate-action candidate in its profile and the selected 2024 window is clean.
Late Q3/Q4 or December spikes in `023960` and `023350` are not treated as original-entry validation; they require fresh trigger-date evidence.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
late_spike_not_entry_validation = true for 023960 and 023350
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
3. Confirm R11 / L1 / C05 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - previous R11 loop86 C03 symbols
   - previous R11 loop87 C04 symbols
   - previous R11 loop88 C05 symbols
   - previous R11 loop89 C02 symbols
   - previous R11 loop90 C03 symbols
   - previous R11 loop91 C04 symbols
   - previous R1 loop89 C03 symbols
   - previous R1 loop90 C04 symbols
   - previous R1 loop91 C05 symbols
   - previous R1 loop92 C02 symbols
6. Confirm stale R10/C30, R8/C28, R7/C25 and earlier-sector candidate rows are not ingested from this MD.
7. Treat 023960 and 023350 as late-spike non-validation failure-mode rows unless fresh trigger evidence is added later.
8. If aggregate support remains stable after exact evidence URL repair, consider C05-scoped safe patch candidates:
   - C05_signed_order_delivery_margin_cash_bridge_required
   - C05_small_EPC_engineering_vocabulary_local_4B_guard
   - C05_late_spike_not_entry_validation_guard
   - C05_Green_exact_evidence_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 92
next_round = R12
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive-watch, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
```
