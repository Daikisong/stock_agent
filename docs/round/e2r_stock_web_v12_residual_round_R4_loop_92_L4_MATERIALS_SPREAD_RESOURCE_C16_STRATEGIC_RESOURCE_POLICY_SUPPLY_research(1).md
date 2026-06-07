# E2R Stock-Web v12 Residual Research — R4 Loop 92 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 92
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RESOURCE_TRADING_SUPPLY_CHAIN_CASH_BRIDGE_VS_RARE_EARTH_FERTILIZER_POLICY_VOCABULARY_DECAY
sector: materials / strategic resource / resource trading / rare earth / fertilizer / supply policy / cash bridge
output_file: e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 92`.

```text
scheduled_round = R4
scheduled_loop = 92
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

R4 is restricted to materials / spread / resource.
C16 is selected because R4 loop91 used C15 material-spread, while the recent R4 sequence is:

```text
R4 loop86 C17
R4 loop87 C16
R4 loop88 C15
R4 loop89 C17
R4 loop90 C16
R4 loop91 C15
```

So loop92 returns to strategic resource / policy-supply residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rows = 36
symbols = 23
good/bad Stage2 = 14/9
4B/4C = 2/0
top-covered = 047400, 005490, 012320, 001570, 081150, 101670
```

This loop avoids the C16 top-covered list and recent R4 loop symbols:

```text
R4 loop86 C17: 120110, 010060, 009830
R4 loop87 C16: 006260, 073570, 131400
R4 loop88 C15: 024840, 006110, 004430
R4 loop89 C17: 001340, 298000, 161000
R4 loop90 C16: 128660, 009520, 018470
R4 loop91 C15: 006340, 005810, 008350
```

Candidate hygiene note:

```text
During this execution path, stale R3/C14 and R2/C08 candidate rows were touched or generated while checking alternatives.
Those rows are not used in this R4/C16 output.
```

Selected symbols:

```text
001120, 000910, 001550
```

The selected pocket is:

```text
resource trading / strategic supply-chain cash bridge positive-watch
vs
rare-earth policy vocabulary without direct resource offtake / margin / cash bridge
vs
fertilizer / food-security policy vocabulary without subsidy-to-volume / margin / cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"001120","company_name":"LX인터내셔널","profile_path":"atlas/symbol_profiles/001/001120.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7741,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1997-05-20","2021-07-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"000910","company_name":"유니온","profile_path":"atlas/symbol_profiles/000/000910.json","first_date":"1996-07-09","last_date":"2026-02-20","trading_day_count":7329,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1997-05-20","1999-10-20","2001-10-25","2007-07-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical name-transition/corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001550","company_name":"조비","profile_path":"atlas/symbol_profiles/001/001550.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7744,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["1997-05-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical name-transition candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"001120","trigger_type":"Stage2-Actionable-ResourceTradingSupplyChainCashBridge-PositiveWatch","entry_date":"2024-01-29","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered and previous R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"000910","trigger_type":"Stage2-FalsePositive-RareEarthPolicyVocabularyNoDirectResourceOfftakeMarginCashBridge","entry_date":"2024-01-10","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered and previous R4 loop symbols; related to top-covered 047400 family but new symbol and failure mode"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"001550","trigger_type":"Stage2-FalsePositive-FertilizerFoodSecurityPolicyVocabularyNoSubsidyVolumeCashBridge","entry_date":"2024-01-02","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered and previous R4 loop symbols"}
```

## 4. Research question

C16 is not “전략자원·공급망 단어가 있다.”
The useful strategic-resource signal must prove a policy-to-supply-to-cash chain:

```text
resource exposure or trading channel
named policy / supply-security context
customer or offtake visibility
inventory or supply availability
pricing / spread / logistics edge
margin bridge
working-capital discipline
cash conversion
```

A strategic-resource headline without this bridge is a map with a mine circled in red. The circle is not the ore. E2R needs the mine, offtake, logistics route, margin ledger, and cash collection.

Residual question:

```text
Can C16 distinguish:
1. resource trading / supply-chain cash bridge that deserves only positive-watch, not Green,
2. rare-earth policy vocabulary where price action does not prove direct resource offtake or margin bridge,
3. fertilizer / food-security vocabulary where no subsidy-to-volume, procurement, margin or cash bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C16_R4L92_001120_LX_RESOURCE_TRADING_CASH","symbol":"001120","company_name":"LX인터내셔널","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_TRADING_SUPPLY_CHAIN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ResourceTradingSupplyChainCashBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_moderate_MFE_low_MAE_resource_trading_cash_bridge","current_profile_verdict":"current_profile_correct_if_resource_channel_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Resource trading/supply-chain cash proxy produced moderate but clean positive path with low MAE. Because MFE is not explosive, this is Yellow/positive-watch only unless exact offtake/logistics/margin evidence is repaired."}
{"row_type":"case","case_id":"C16_R4L92_000910_UNION_RARE_EARTH_POLICY","symbol":"000910","company_name":"유니온","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_VOCABULARY_WITHOUT_DIRECT_OFFTAKE_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RareEarthPolicyVocabularyNoDirectResourceOfftakeMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub20_MFE_deep_MAE_policy_vocabulary_no_offtake_bridge","current_profile_verdict":"current_profile_false_positive_if_rare_earth_policy_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Rare-earth policy vocabulary had sub-20 MFE and later deep drawdown without direct resource offtake, pricing, margin or cash evidence."}
{"row_type":"case","case_id":"C16_R4L92_001550_CHOBI_FERTILIZER_POLICY","symbol":"001550","company_name":"조비","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"FERTILIZER_FOOD_SECURITY_POLICY_VOCABULARY_WITHOUT_SUBSIDY_VOLUME_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-FertilizerFoodSecurityPolicyVocabularyNoSubsidyVolumeCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_subsidy_volume_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_fertilizer_policy_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Fertilizer/food-security policy vocabulary had very low MFE and persistent drawdown without subsidy implementation, procurement volume, margin or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 001120 LX인터내셔널 — resource trading / supply-chain cash bridge positive-watch

Entry row: `2024-01-29 c=27650`.
Observed path: entry-area low `2024-03-19 l=25800`, full-window peak around `2024-09-25 h=31500`, and controlled later drawdown.

```jsonl
{"row_type":"trigger","trigger_id":"R4L92_C16_001120_20240129_STAGE2_RESOURCE_TRADING_CASH","case_id":"C16_R4L92_001120_LX_RESOURCE_TRADING_CASH","symbol":"001120","company_name":"LX인터내셔널","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_TRADING_SUPPLY_CHAIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ResourceTradingSupplyChainCashBridge-PositiveWatch","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":27650.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_resource_trading_supply_chain_cash_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; resource trading, logistics channel, offtake and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["resource_trading_channel_proxy","supply_chain_cash_flow_proxy","logistics_or_offtake_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_resource_offtake_source_pending","logistics_margin_source_pending","inventory_or_supply_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","Green_strict_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv","profile_path":"atlas/symbol_profiles/001/001120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.33,"MFE_90D_pct":6.33,"MFE_180D_pct":13.92,"MAE_30D_pct":-3.44,"MAE_90D_pct":-6.51,"MAE_180D_pct":-6.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-25","peak_price":31500.0,"max_drawdown_low_date":"2024-03-19","max_drawdown_low":25800.0,"drawdown_after_peak_pct":-14.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.45,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_only; moderate MFE requires exact resource/offtake/logistics/margin/cash evidence before any Green consideration","four_b_evidence_type":["moderate_MFE_watch","Green_strict_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_watch_moderate_MFE_low_MAE_resource_trading_cash_bridge","current_profile_verdict":"current_profile_correct_if_resource_channel_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_name_transition_pre_2024; selected_window_clean","same_entry_group_id":"001120_2024-01-29_27650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 can allow Yellow/positive-watch when strategic-resource exposure is tied to actual trading channel, offtake/logistics, margin and cash conversion. Moderate MFE blocks Green until exact evidence is repaired."}
```

### 6.2 000910 유니온 — rare-earth policy vocabulary without direct offtake / margin bridge

Entry row: `2024-01-10 c=5840`, on rare-earth / supply-security vocabulary.
Observed path: local high `2024-01-10 h=6580`, but later drawdown to `2024-10-08 l=4035`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L92_C16_000910_20240110_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY","case_id":"C16_R4L92_000910_UNION_RARE_EARTH_POLICY","symbol":"000910","company_name":"유니온","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_VOCABULARY_WITHOUT_DIRECT_OFFTAKE_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-RareEarthPolicyVocabularyNoDirectResourceOfftakeMarginCashBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":5840.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_rare_earth_supply_security_policy_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; rare-earth policy vocabulary treated as insufficient without direct resource offtake, pricing/spread, inventory, margin and cash bridge","evidence_source_type":"historical_public_policy_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["rare_earth_policy_keyword","supply_security_vocabulary","relative_strength_spike"],"stage3_evidence_fields":["direct_resource_offtake_missing","pricing_or_spread_bridge_missing","inventory_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["sub20_MFE","policy_vocabulary_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv","profile_path":"atlas/symbol_profiles/000/000910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.67,"MFE_90D_pct":12.67,"MFE_180D_pct":12.67,"MAE_30D_pct":-6.34,"MAE_90D_pct":-12.50,"MAE_180D_pct":-30.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-10","peak_price":6580.0,"max_drawdown_low_date":"2024-10-08","max_drawdown_low":4035.0,"drawdown_after_peak_pct":-38.68,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"rare_earth_policy_vocabulary_without_direct_offtake_pricing_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","policy_vocabulary_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_policy_vocabulary_no_offtake_bridge","current_profile_verdict":"current_profile_false_positive_if_rare_earth_policy_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"000910_2024-01-10_5840","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not promote rare-earth policy vocabulary unless resource offtake, pricing/spread, inventory, margin and cash evidence are exact-repaired. Sub-20 MFE and deep drawdown force Watch/4B routing."}
```

### 6.3 001550 조비 — fertilizer / food-security policy vocabulary without subsidy-volume-cash bridge

Entry row: `2024-01-02 c=14280`.
Observed path: local high `2024-01-25 h=15000`, then persistent decline to `2024-11-14 l=9570`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L92_C16_001550_20240102_STAGE2_FALSE_POSITIVE_FERTILIZER_POLICY","case_id":"C16_R4L92_001550_CHOBI_FERTILIZER_POLICY","symbol":"001550","company_name":"조비","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"FERTILIZER_FOOD_SECURITY_POLICY_VOCABULARY_WITHOUT_SUBSIDY_VOLUME_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;policy_to_volume_cash_stress_test","trigger_type":"Stage2-FalsePositive-FertilizerFoodSecurityPolicyVocabularyNoSubsidyVolumeCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":14280.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_fertilizer_food_security_policy_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; fertilizer/food-security policy vocabulary treated as insufficient without subsidy implementation, procurement/volume channel, margin and cash bridge","evidence_source_type":"historical_public_policy_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["fertilizer_policy_keyword","food_security_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["subsidy_implementation_missing","procurement_volume_missing","input_cost_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_MFE","policy_to_volume_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001550/2024.csv","profile_path":"atlas/symbol_profiles/001/001550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.04,"MFE_90D_pct":5.04,"MFE_180D_pct":5.04,"MAE_30D_pct":-8.12,"MAE_90D_pct":-10.08,"MAE_180D_pct":-32.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-25","peak_price":15000.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":9570.0,"drawdown_after_peak_pct":-36.20,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fertilizer_food_security_policy_vocabulary_without_subsidy_volume_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","policy_to_volume_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_subsidy_volume_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_fertilizer_policy_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"001550_2024-01-02_14280","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not count fertilizer/food-security vocabulary as strategic supply evidence unless subsidy implementation, procurement volume, margin and cash bridge are repaired. Low MFE and deep MAE require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L92_001120_LX_RESOURCE_TRADING_CASH","trigger_id":"R4L92_C16_001120_20240129_STAGE2_RESOURCE_TRADING_CASH","symbol":"001120","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C16 requires resource exposure, offtake/logistics, pricing or margin and cash conversion rather than policy vocabulary alone","raw_component_scores_before":{"resource_exposure_score":10,"policy_supply_context_score":8,"offtake_visibility_score":8,"logistics_channel_score":10,"inventory_supply_score":7,"pricing_spread_score":7,"margin_bridge_score":8,"cash_conversion_score":8,"relative_strength_score":6,"valuation_repricing_score":5,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"resource_exposure_score":13,"policy_supply_context_score":10,"offtake_visibility_score":10,"logistics_channel_score":12,"inventory_supply_score":9,"pricing_spread_score":9,"margin_bridge_score":10,"cash_conversion_score":10,"relative_strength_score":7,"valuation_repricing_score":6,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Resource trading/cash bridge supports Yellow-watch only; moderate MFE and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L92_000910_UNION_RARE_EARTH_POLICY","trigger_id":"R4L92_C16_000910_20240110_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY","symbol":"000910","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"rare-earth policy vocabulary without direct resource bridge should be blocked","raw_component_scores_before":{"resource_exposure_score":2,"policy_supply_context_score":5,"offtake_visibility_score":0,"logistics_channel_score":0,"inventory_supply_score":0,"pricing_spread_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"resource_exposure_score":1,"policy_supply_context_score":2,"offtake_visibility_score":0,"logistics_channel_score":0,"inventory_supply_score":0,"pricing_spread_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-20 MFE and deep MAE convert rare-earth vocabulary into missing offtake/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L92_001550_CHOBI_FERTILIZER_POLICY","trigger_id":"R4L92_C16_001550_20240102_STAGE2_FALSE_POSITIVE_FERTILIZER_POLICY","symbol":"001550","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"fertilizer/food-security policy vocabulary without subsidy volume and margin/cash bridge should remain Watch/4B","raw_component_scores_before":{"resource_exposure_score":1,"policy_supply_context_score":4,"offtake_visibility_score":0,"logistics_channel_score":0,"inventory_supply_score":1,"pricing_spread_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"resource_exposure_score":0,"policy_supply_context_score":1,"offtake_visibility_score":0,"logistics_channel_score":0,"inventory_supply_score":0,"pricing_spread_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require subsidy implementation, procurement volume, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L92_C16_P0_CURRENT","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C16 needs explicit offtake/logistics/inventory/pricing/margin/cash bridge and policy-vocabulary 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":8.01,"avg_MAE90_pct":-9.70,"avg_MFE180_pct":10.54,"avg_MAE180_pct":-23.53,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.82,"avg_four_b_full_window_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C16_policy_to_supply_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L92_C16_P1_SECTOR_SPECIFIC","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P1_L4_strategic_resource_policy_supply_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 strategic-resource signals need actual resource channel, offtake, logistics, inventory, pricing/spread, margin or cash before Stage2-Actionable","changed_axes":["offtake_required","policy_to_supply_required","policy_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_offtake_logistics_inventory_pricing_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":8.01,"avg_MAE90_pct":-9.70,"avg_MFE180_pct":10.54,"avg_MAE180_pct":-23.53,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L92_C16_P2_CANONICAL","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P2_C16_resource_policy_to_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C16 should reward supply-to-cash mechanics, not rare-earth/fertilizer policy vocabulary","changed_axes":["C16_offtake_logistics_margin_cash_bridge_required","C16_rare_earth_fertilizer_vocabulary_local_4B_guard","C16_moderate_MFE_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"resource_or_policy_context_plus_offtake_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":8.01,"avg_MAE90_pct":-9.70,"avg_MFE180_pct":10.54,"avg_MAE180_pct":-23.53,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L92_C16_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P3_C16_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If policy-to-supply/cash bridge is missing, MFE90<15 or MAE180<=-25 should block Yellow/Green and route to Watch/4B","changed_axes":["C16_sub15_MFE_guardrail","C16_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_15_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":8.01,"avg_MAE90_pct":-9.70,"avg_MFE180_pct":10.54,"avg_MAE180_pct":-23.53,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_RESOURCE_TRADING_POSITIVE_VS_RAREEARTH_FERTILIZER_POLICY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":8.01,"avg_MAE90_pct":-9.70,"avg_MFE180_pct":10.54,"avg_MAE180_pct":-23.53,"stage2_hit_rate_MFE90_ge15":0.0,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C16 needs bridge discipline. LX인터내셔널 shows only a resource-trading positive-watch when cash/logistics bridge exists, while 유니온 and 조비 show rare-earth/fertilizer policy vocabulary should not be promoted without direct offtake, subsidy-to-volume, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"001120","trigger_type":"Stage2-Actionable-ResourceTradingSupplyChainCashBridge-PositiveWatch","entry_date":"2024-01-29","stage2_to_90D_outcome":"positive_watch_moderate_MFE_low_MAE","stage2_to_180D_outcome":"resource_trading_bridge_but_Green_strict","MFE90_ge15":false,"MAE90_le_minus20":false,"transition_note":"Allow only Yellow/positive-watch when resource trading is tied to logistics/offtake/margin/cash bridge; moderate MFE blocks Green."}
{"row_type":"stage_transition_summary","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"000910","trigger_type":"Stage2-FalsePositive-RareEarthPolicyVocabularyNoDirectResourceOfftakeMarginCashBridge","entry_date":"2024-01-10","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_bridge_missing","stage2_to_180D_outcome":"failed_rare_earth_policy_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Rare-earth policy vocabulary without direct offtake/pricing/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"001550","trigger_type":"Stage2-FalsePositive-FertilizerFoodSecurityPolicyVocabularyNoSubsidyVolumeCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_policy_to_volume_bridge_missing","stage2_to_180D_outcome":"failed_fertilizer_policy_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Fertilizer/food-security policy vocabulary without subsidy implementation, procurement volume and margin/cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"rare_earth_fertilizer_policy_vocabulary_overcredit_without_policy_to_supply_cash_bridge","contribution":"Adds two C16 4B counterexamples against one resource-trading positive-watch, avoiding C16 top-covered and recent R4 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_TRADING_SUPPLY_CHAIN_CASH_BRIDGE_VS_RARE_EARTH_FERTILIZER_POLICY_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C16 now has non-top-symbol resource-trading positive-watch and two rare-earth/fertilizer weak-bridge counterexamples; next R4 C16 loops should exact-URL repair policy implementation, resource offtake, logistics, inventory, pricing/spread, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_offtake_logistics_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"001120 only supports Yellow-watch when resource trading/cash proxy exists; 000910 and 001550 fail when policy vocabulary lacks offtake/subsidy-to-volume/margin evidence."}
{"row_type":"shadow_weight","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_rare_earth_fertilizer_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Rare-earth and fertilizer policy rows showed sub-15 MFE and deep MAE when non-price policy-to-supply/cash evidence was missing."}
{"row_type":"shadow_weight","round":"R4","loop":"92","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_moderate_MFE_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"001120 is a positive-watch but MFE is moderate, so Green requires exact source-grade offtake/logistics/margin/cash bridge."}
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
  - rare_earth_policy_vocabulary_overcredit
  - fertilizer_food_security_policy_vocabulary_overcredit
  - policy_to_supply_bridge_missing
  - offtake_logistics_margin_cash_bridge_missing
  - moderate_MFE_Green_strict_watch
new_axis_proposed:
  - C16_offtake_logistics_margin_cash_bridge_required_shadow_only
  - C16_rare_earth_fertilizer_vocabulary_local_4B_guard_shadow_only
  - C16_moderate_MFE_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C16
  - full_4b_requires_non_price_evidence within C16
  - hard_4c_thesis_break_routes_to_4c within C16
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
All three selected symbols have only older name-transition or corporate-action candidates before 2024.
Those candidates are outside the selected 2024 windows and do not contaminate this residual price-path analysis.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
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
3. Confirm R4 / L4 / C16 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C16 top-covered symbols
   - previous R4 loop86 C17 symbols
   - previous R4 loop87 C16 symbols
   - previous R4 loop88 C15 symbols
   - previous R4 loop89 C17 symbols
   - previous R4 loop90 C16 symbols
   - previous R4 loop91 C15 symbols
6. Confirm stale R3/C14 and R2/C08 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C16-scoped safe patch candidates:
   - C16_offtake_logistics_margin_cash_bridge_required
   - C16_rare_earth_fertilizer_vocabulary_local_4B_guard
   - C16_moderate_MFE_Green_strict_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 92
next_round = R5
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive-watch, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
```
