# E2R Stock-Web v12 Residual Research — R12 Loop 87 / L10 / C31

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 87
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: GAS_EXPLORATION_POLICY_ASSET_OPTIONALITY_BRIDGE_VS_OIL_THEME_BLOWOFF_WITHOUT_MONETIZATION
sector: policy / subsidy / legislation / event / energy exploration / oil-gas policy
output_file: e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 87`.

```text
scheduled_round = R12
scheduled_loop = 87
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

R12 is the policy / event / cross-redteam / miscellaneous lane.  
C31 is selected because the previous R12 loop used C32 governance / control premium, while C31 remains a broad policy-event bucket with substantial false-positive risk.

No-Repeat Index snapshot:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows = 97
symbols = 70
good/bad Stage2 = 35/25
4B/4C = 5/0
top-covered = 013990, 003550, 015760, 032350, 114090, 000270
```

This loop avoids the top-covered set and also avoids the immediately previous R12 loop symbols:

```text
R12 loop85 C31: 055550, 034730, 004020
R12 loop86 C32: 028260, 001040, 004990
```

Selected symbols:

```text
036460, 004090, 024060
```

This loop focuses on the 2024 energy-exploration / oil-gas policy event family.  
The research question is not whether the headline moved price. It is whether a policy event has an asset, monopoly, tariff, fiscal, commercial, or cash-flow bridge. Without that bridge, the event is a match flare: bright first, then oxygen-dependent.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"036460","company_name":"한국가스공사","profile_path":"atlas/symbol_profiles/036/036460.json","first_date":"1999-12-15","last_date":"2026-02-20","trading_day_count":6452,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"004090","company_name":"한국석유","profile_path":"atlas/symbol_profiles/004/004090.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7596,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1997-08-07","2021-04-15","2021-05-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"024060","company_name":"흥구석유","profile_path":"atlas/symbol_profiles/024/024060.json","first_date":"1996-07-30","last_date":"2026-02-20","trading_day_count":6644,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1997-09-11","1998-04-08","1998-08-24","2008-08-26","2008-10-06","2008-10-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"036460","trigger_type":"Stage2-Actionable-GasExplorationPolicyAssetOptionalityBridge-Positive","entry_date":"2024-06-04","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"004090","trigger_type":"Stage2-FalsePositive-OilExplorationPolicyThemeBlowoff-NoAssetCashBridge","entry_date":"2024-06-04","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"024060","trigger_type":"Stage2-FalsePositive-OilDistributorPolicyTheme-NoDirectMonetizationBridge","entry_date":"2024-06-04","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
```

## 4. Research question

C31 is not “a policy headline exists.”  
The useful policy-event signal must pass through an economic bridge: direct beneficiary status, asset ownership or option value, regulated tariff/cost recovery, subsidy receipt, contract award, legal certainty, and cash-flow path. If the bridge is missing, price acts like a crowd running toward a siren.

Residual question:

```text
Can C31 distinguish:
1. policy event with direct asset optionality / regulated beneficiary bridge,
2. oil/gas exploration theme blowoff where no direct asset/cash bridge exists,
3. distributor/oil theme movement that borrows the headline but lacks direct monetization?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C31_R12L87_036460_KOGAS_POLICY_ASSET_OPTIONALITY","symbol":"036460","company_name":"한국가스공사","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"GAS_EXPLORATION_POLICY_ASSET_OPTIONALITY_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-GasExplorationPolicyAssetOptionalityBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_moderate_180D_MAE","current_profile_verdict":"current_profile_correct_if_direct_policy_asset_bridge_required","price_source":"Songdaiki/stock-web","notes":"Direct public-gas utility / exploration-asset optionality proxy produced high MFE. Later 180D drawdown keeps Green strict and makes this a Yellow-watch positive, not a Green loosening case."}
{"row_type":"case","case_id":"C31_R12L87_004090_KOREA_PETROLEUM_POLICY_BLOWOFF","symbol":"004090","company_name":"한국석유","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OIL_EXPLORATION_POLICY_THEME_BLOWOFF_WITHOUT_ASSET_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OilExplorationPolicyThemeBlowoff-NoAssetCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_same_event_MFE_but_high_MAE_price_only_4B","current_profile_verdict":"current_profile_false_positive_if_policy_theme_blowoff_overcredited","price_source":"Songdaiki/stock-web","notes":"Oil-exploration theme had large event MFE but also opened high MAE without a direct asset/cash bridge. It is a price-only 4B-style case, not positive evidence."}
{"row_type":"case","case_id":"C31_R12L87_024060_HEUNGGU_OIL_DISTRIBUTOR_THEME","symbol":"024060","company_name":"흥구석유","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OIL_DISTRIBUTOR_POLICY_THEME_WITHOUT_DIRECT_MONETIZATION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OilDistributorPolicyTheme-NoDirectMonetizationBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_event_spike_deep_MAE_without_monetization_bridge","current_profile_verdict":"current_profile_false_positive_if_oil_distributor_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Oil-distributor theme borrowed the policy headline, showed event MFE, but later sold off without direct monetization, contract, subsidy or cash-flow bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 036460 한국가스공사 — policy asset optionality bridge positive

Entry row: `2024-06-04 c=39400`.  
Observed path: high `2024-06-20 h=64500`, later low `2024-12-06 l=31200`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L87_C31_036460_20240604_STAGE2_GAS_POLICY_ASSET","case_id":"C31_R12L87_036460_KOGAS_POLICY_ASSET_OPTIONALITY","symbol":"036460","company_name":"한국가스공사","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"GAS_EXPLORATION_POLICY_ASSET_OPTIONALITY_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-GasExplorationPolicyAssetOptionalityBridge-Positive","trigger_date":"2024-06-04","entry_date":"2024-06-04","entry_price":39400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_energy_exploration_policy_asset_optionality_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; direct public gas utility, asset optionality and policy beneficiary bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["direct_policy_beneficiary_proxy","asset_optionality_proxy","regulated_utility_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_asset_interest_pending","commerciality_evidence_pending","tariff_or_cost_recovery_pending","cash_flow_bridge_pending"],"stage4b_evidence_fields":["policy_event_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":63.71,"MFE_90D_pct":63.71,"MFE_180D_pct":63.71,"MAE_30D_pct":-5.20,"MAE_90D_pct":-7.36,"MAE_180D_pct":-20.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500.0,"max_drawdown_low_date":"2024-12-06","max_drawdown_low":31200.0,"drawdown_after_peak_pct":-51.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_policy_asset_bridge; Green requires exact commerciality/cash bridge","four_b_evidence_type":["policy_event_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_moderate_180D_MAE","current_profile_verdict":"current_profile_correct_if_direct_policy_asset_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"036460_2024-06-04_39400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 can allow Stage2/Yellow when a policy event maps to a direct beneficiary and asset optionality. Green still requires exact commerciality, legal, tariff and cash-flow evidence."}
```

### 6.2 004090 한국석유 — oil exploration policy theme blowoff without asset/cash bridge

Entry row: `2024-06-04 c=23300`.  
Observed path: high `2024-06-05 h=28100`, then low `2024-07-16 l=16620`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L87_C31_004090_20240604_STAGE2_FALSE_POSITIVE_OIL_POLICY_BLOWOFF","case_id":"C31_R12L87_004090_KOREA_PETROLEUM_POLICY_BLOWOFF","symbol":"004090","company_name":"한국석유","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OIL_EXPLORATION_POLICY_THEME_BLOWOFF_WITHOUT_ASSET_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-OilExplorationPolicyThemeBlowoff-NoAssetCashBridge","trigger_date":"2024-06-04","entry_date":"2024-06-04","entry_price":23300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_oil_exploration_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; oil/gas exploration policy theme treated as insufficient without direct asset interest, contract, subsidy, legal entitlement or cash-flow bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["oil_exploration_policy_theme","relative_strength_blowoff"],"stage3_evidence_fields":["direct_asset_interest_missing","commerciality_bridge_missing","contract_or_subsidy_missing","cash_flow_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","asset_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv","profile_path":"atlas/symbol_profiles/004/004090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.60,"MFE_90D_pct":20.60,"MFE_180D_pct":20.60,"MAE_30D_pct":-26.87,"MAE_90D_pct":-28.67,"MAE_180D_pct":-28.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":28100.0,"max_drawdown_low_date":"2024-07-16","max_drawdown_low":16620.0,"drawdown_after_peak_pct":-40.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"policy_theme_price_blowoff_without_direct_asset_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","asset_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_same_event_MFE_but_high_MAE_price_only_4B","current_profile_verdict":"current_profile_false_positive_if_policy_theme_blowoff_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004090_2024-06-04_23300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should not promote policy-event blowoff when direct asset/cash-flow bridge is missing. High MFE does not override deep MAE and bridge absence."}
```

### 6.3 024060 흥구석유 — distributor/oil policy theme without direct monetization bridge

Entry row: `2024-06-04 c=19240`.  
Observed path: same-day high `20950`, then lows around `2024-06-17 l=13800` and `2024-07-17 l=13690`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L87_C31_024060_20240604_STAGE2_FALSE_POSITIVE_DISTRIBUTOR_THEME","case_id":"C31_R12L87_024060_HEUNGGU_OIL_DISTRIBUTOR_THEME","symbol":"024060","company_name":"흥구석유","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OIL_DISTRIBUTOR_POLICY_THEME_WITHOUT_DIRECT_MONETIZATION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-OilDistributorPolicyTheme-NoDirectMonetizationBridge","trigger_date":"2024-06-04","entry_date":"2024-06-04","entry_price":19240.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_oil_distributor_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; oil distributor theme treated as insufficient without direct monetization, asset, contract or subsidy bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["oil_distributor_theme","policy_event_beta"],"stage3_evidence_fields":["direct_monetization_missing","asset_bridge_missing","contract_subsidy_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","monetization_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv","profile_path":"atlas/symbol_profiles/024/024060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.89,"MFE_90D_pct":8.89,"MFE_180D_pct":8.89,"MAE_30D_pct":-28.27,"MAE_90D_pct":-28.85,"MAE_180D_pct":-28.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-04","peak_price":20950.0,"max_drawdown_low_date":"2024-07-17","max_drawdown_low":13690.0,"drawdown_after_peak_pct":-34.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"oil_distributor_policy_theme_without_direct_monetization_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","monetization_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_event_spike_deep_MAE_without_monetization_bridge","current_profile_verdict":"current_profile_false_positive_if_oil_distributor_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"024060_2024-06-04_19240","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should not treat distributor beta as policy-event beneficiary evidence. Direct monetization, contract/subsidy, margin and cash bridge are required before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C31_R12L87_036460_KOGAS_POLICY_ASSET_OPTIONALITY","trigger_id":"R12L87_C31_036460_20240604_STAGE2_GAS_POLICY_ASSET","symbol":"036460","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C31 requires direct policy-beneficiary and asset/cash-flow bridge rather than policy headline alone","raw_component_scores_before":{"direct_beneficiary_score":13,"policy_event_quality_score":12,"asset_optionality_score":12,"legal_certainty_score":8,"cash_flow_bridge_score":6,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-6,"theme_spike_risk":-4,"information_confidence":5},"weighted_score_before":67,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"direct_beneficiary_score":16,"policy_event_quality_score":15,"asset_optionality_score":15,"legal_certainty_score":10,"cash_flow_bridge_score":8,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":6},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Direct beneficiary and asset optionality bridge plus high MFE support Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C31_R12L87_004090_KOREA_PETROLEUM_POLICY_BLOWOFF","trigger_id":"R12L87_C31_004090_20240604_STAGE2_FALSE_POSITIVE_OIL_POLICY_BLOWOFF","symbol":"004090","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"oil policy blowoff without asset/cash bridge should be 4B-watch","raw_component_scores_before":{"direct_beneficiary_score":2,"policy_event_quality_score":8,"asset_optionality_score":0,"legal_certainty_score":1,"cash_flow_bridge_score":0,"relative_strength_score":15,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"direct_beneficiary_score":0,"policy_event_quality_score":2,"asset_optionality_score":0,"legal_certainty_score":0,"cash_flow_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"High same-event MFE is outweighed by missing direct asset/cash bridge and high MAE."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C31_R12L87_024060_HEUNGGU_OIL_DISTRIBUTOR_THEME","trigger_id":"R12L87_C31_024060_20240604_STAGE2_FALSE_POSITIVE_DISTRIBUTOR_THEME","symbol":"024060","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"oil distributor theme without direct monetization bridge should remain Watch/blocked","raw_component_scores_before":{"direct_beneficiary_score":1,"policy_event_quality_score":5,"asset_optionality_score":0,"legal_certainty_score":0,"cash_flow_bridge_score":0,"relative_strength_score":12,"valuation_repricing_score":4,"execution_risk_score":-15,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"direct_beneficiary_score":0,"policy_event_quality_score":1,"asset_optionality_score":0,"legal_certainty_score":0,"cash_flow_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require direct monetization, contract/subsidy and cash bridge before any promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L87_C31_P0_CURRENT","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C31 needs explicit direct-beneficiary, legal/cash-flow and monetization bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":31.07,"avg_MAE90_pct":-21.63,"avg_MFE180_pct":31.07,"avg_MAE180_pct":-26.11,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C31_direct_beneficiary_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L87_C31_P1_SECTOR_SPECIFIC","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P1_L10_policy_direct_beneficiary_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 policy/event signals need direct beneficiary, asset optionality, legal certainty, contract/subsidy, tariff/cost recovery or cash-flow bridge before Stage2-Actionable","changed_axes":["direct_beneficiary_required","asset_cash_flow_bridge_required","policy_theme_blowoff_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_direct_beneficiary_asset_contract_subsidy_tariff_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":31.07,"avg_MAE90_pct":-21.63,"avg_MFE180_pct":31.07,"avg_MAE180_pct":-26.11,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L87_C31_P2_CANONICAL","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P2_C31_direct_policy_cash_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C31 should reward policy-to-cash mechanics, not headline beta or distributor/oil theme labels","changed_axes":["C31_direct_beneficiary_cash_bridge_required","C31_policy_theme_local_4B_guard","C31_high_MAE_price_only_guard"],"changed_thresholds":{"stage2_yellow_gate":"direct_beneficiary_plus_asset_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":31.07,"avg_MAE90_pct":-21.63,"avg_MFE180_pct":31.07,"avg_MAE180_pct":-26.11,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L87_C31_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P3_C31_price_only_policy_blowoff_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If direct beneficiary/cash bridge is missing and MAE90<=-25, route to 4B-watch even when MFE exists","changed_axes":["C31_high_MAE_guardrail","C31_price_only_policy_blowoff_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":31.07,"avg_MAE90_pct":-21.63,"avg_MFE180_pct":31.07,"avg_MAE180_pct":-26.11,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_GAS_POLICY_ASSET_BRIDGE_VS_OIL_THEME_BLOWOFF","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":31.07,"avg_MAE90_pct":-21.63,"avg_MFE180_pct":31.07,"avg_MAE180_pct":-26.11,"stage2_hit_rate_MFE90_ge_20":0.67,"stage2_bad_entry_rate_bridge_missing_MAE90_le_minus25":0.67,"interpretation":"C31 needs bridge discipline. 한국가스공사 shows direct policy beneficiary/asset optionality can support Yellow-watch, while 한국석유 and 흥구석유 show oil/gas policy headline beta should not become Yellow/Green without direct asset, contract, subsidy, monetization or cash-flow bridge."}
{"row_type":"stage_transition_summary","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"036460","trigger_type":"Stage2-Actionable-GasExplorationPolicyAssetOptionalityBridge-Positive","entry_date":"2024-06-04","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_90D_MAE","stage2_to_180D_outcome":"watch_positive_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when policy event is tied to direct beneficiary and asset/cash optionality; Green requires exact commerciality and cash-flow evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"004090","trigger_type":"Stage2-FalsePositive-OilExplorationPolicyThemeBlowoff-NoAssetCashBridge","entry_date":"2024-06-04","stage2_to_90D_outcome":"price_only_policy_blowoff_MFE_with_high_MAE","stage2_to_180D_outcome":"failed_policy_theme_no_direct_asset_bridge","MFE90_ge_20":true,"MAE90_le_minus_20":true,"transition_note":"High event MFE should not validate the row when direct asset/cash bridge is missing and MAE opens deeply."}
{"row_type":"stage_transition_summary","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"024060","trigger_type":"Stage2-FalsePositive-OilDistributorPolicyTheme-NoDirectMonetizationBridge","entry_date":"2024-06-04","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_distributor_policy_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Distributor beta without direct monetization bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"policy_event_headline_overcredit_without_direct_beneficiary_asset_cash_bridge","contribution":"Adds two C31 4B/high-MAE policy-theme counterexamples against one direct-beneficiary gas policy positive, avoiding C31 top-covered and previous R12 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"87","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"GAS_EXPLORATION_POLICY_ASSET_OPTIONALITY_BRIDGE_VS_OIL_THEME_BLOWOFF_WITHOUT_MONETIZATION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C31 now has non-top-symbol energy-policy positive and oil-theme blowoff counterexamples; next R12 loops should exact-URL repair direct beneficiary, legal certainty, asset ownership, contract/subsidy, tariff/cost recovery and cash-flow evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_direct_beneficiary_asset_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"036460 worked when direct beneficiary/asset optionality proxy existed; 004090 and 024060 were 4B/high-MAE rows when only policy headline beta existed."}
{"row_type":"shadow_weight","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_policy_theme_price_only_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Oil/gas policy-theme rows showed local MFE but high MAE without non-price monetization bridge."}
{"row_type":"shadow_weight","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_high_MAE_missing_bridge_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If direct beneficiary/cash bridge is missing and MAE90<=-25, block Stage2-Actionable/Yellow and route to Watch/4B-risk even when MFE exists."}
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
  - policy_event_headline_overcredit
  - direct_beneficiary_bridge_missing
  - asset_cash_flow_bridge_missing
  - oil_distributor_policy_beta_no_direct_monetization
new_axis_proposed:
  - C31_direct_beneficiary_asset_cash_bridge_required_shadow_only
  - C31_policy_theme_price_only_local_4B_guard_shadow_only
  - C31_high_MAE_missing_bridge_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C31
  - full_4b_requires_non_price_evidence within C31
  - hard_4c_thesis_break_routes_to_4c within C31
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
3. Confirm R12 / L10 / C31 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C31 top-covered symbols
   - previous R12 loop85 C31 symbols
   - previous R12 loop86 C32 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C31-scoped safe patch candidates:
   - C31_direct_beneficiary_asset_cash_bridge_required
   - C31_policy_theme_price_only_local_4B_guard
   - C31_high_MAE_missing_bridge_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 87
next_round = R13
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
```
