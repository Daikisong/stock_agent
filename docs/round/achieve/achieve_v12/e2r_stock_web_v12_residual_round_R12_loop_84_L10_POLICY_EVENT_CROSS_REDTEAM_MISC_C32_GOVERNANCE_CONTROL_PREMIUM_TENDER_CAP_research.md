# E2R Stock-Web v12 Residual Research — R12 Loop 84 / L10 / C32

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 84
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDCO_NAV_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_HOLDCO_THEME_SPIKE
sector: policy/event/cross-redteam/misc / governance / holding-company NAV / control-premium cap
output_file: e2r_stock_web_v12_residual_round_R12_loop_84_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 84`.

```text
scheduled_round = R12
scheduled_loop = 84
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

R12 may use L10 policy/event/cross-redteam/misc.  
This loop selects C32 because the previous R12 loop used C31 policy/subsidy events, while C32 still needs a cleaner separation between true holding-company NAV/shareholder-return bridge and generic value-up/governance theme spikes.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"028260","company_name":"삼성물산","profile_path":"atlas/symbol_profiles/028/028260.json","first_date":"2014-12-18","last_date":"2026-02-20","trading_day_count":2741,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-09-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"004990","company_name":"롯데지주","profile_path":"atlas/symbol_profiles/004/004990.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7661,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2016-05-17","2017-10-30","2018-04-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"000880","company_name":"한화","profile_path":"atlas/symbol_profiles/000/000880.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7763,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-03","1999-01-04","1999-07-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

The No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C32, the top-covered symbols are:

```text
010130, 036560, 000150, 041510, 241560, 000990
```

This loop also avoids the previous C32 loop83 symbols:

```text
402340, 034730, 003550
```

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"028260","trigger_type":"Stage2-Actionable-HoldcoNAVShareholderReturnBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered list and previous C32 loop83 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004990","trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoNAVReturnBridge","entry_date":"2024-02-01","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered list and previous C32 loop83 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000880","trigger_type":"Stage2-FalsePositive-HoldcoDefenseValueupTheme-NoGovernanceBridge","entry_date":"2024-02-01","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered list and previous C32 loop83 symbols"}
```

## 4. Research question

C32 should not read every value-up or holding-company rally as a governance rerating.  
A real governance rerating needs a bridge: NAV discount repair, explicit shareholder return, control-premium mechanics, capital allocation credibility, or a credible tender/ownership route. Without that bridge, a holding-company price spike becomes a short fuse rather than a durable signal.

Residual question:

```text
Can C32 distinguish:
1. holding-company NAV/shareholder-return rerating with strong price confirmation,
2. holding-company value-up theme spike without NAV/capital-return conversion,
3. conglomerate/defense holding-company theme spike without direct governance bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C32_R12L84_028260_SAMSUNGCNT_HOLDCO_NAV_RETURN_BRIDGE","symbol":"028260","company_name":"삼성물산","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_NAV_SHAREHOLDER_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HoldcoNAVShareholderReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_governance_bridge_required","price_source":"Songdaiki/stock-web","notes":"NAV discount repair/shareholder-return proxy aligned with strong MFE and tolerable MAE. Supports C32 Stage2/Yellow, not automatic Green without exact evidence."}
{"row_type":"case","case_id":"C32_R12L84_004990_LOTTE_HOLDCO_VALUEUP_THEME_NO_BRIDGE","symbol":"004990","company_name":"롯데지주","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_VALUEUP_THEME_WITHOUT_NAV_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoValueupTheme-NoNAVReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_valueup_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Initial value-up/holding-company spike faded because NAV discount repair and capital-return bridge were not strong enough."}
{"row_type":"case","case_id":"C32_R12L84_000880_HANWHA_HOLDCO_THEME_NO_GOVERNANCE_BRIDGE","symbol":"000880","company_name":"한화","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONGLOMERATE_HOLDCO_THEME_WITHOUT_DIRECT_GOVERNANCE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoDefenseValueupTheme-NoGovernanceBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_conglomerate_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Conglomerate/defense holding-company theme had only modest MFE and medium MAE when direct NAV, shareholder-return, and control-premium bridge were missing."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 028260 삼성물산 — holdco NAV/shareholder-return bridge positive

Entry row: `2024-01-29 c=127900`.  
Forward path: `2024-02-19 h=171700`; same selected forward-window low was the entry-day low `2024-01-29 l=120400`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L84_C32_028260_20240129_STAGE2_HOLDCO_NAV_RETURN_BRIDGE","case_id":"C32_R12L84_028260_SAMSUNGCNT_HOLDCO_NAV_RETURN_BRIDGE","symbol":"028260","company_name":"삼성물산","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_NAV_SHAREHOLDER_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HoldcoNAVShareholderReturnBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":127900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_valueup_NAV_shareholder_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company NAV discount repair and shareholder-return thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["NAV_discount_repair_proxy","shareholder_return_proxy","governance_policy_tailwind","relative_strength_turn"],"stage3_evidence_fields":["capital_allocation_bridge_pending","multi_source_confirmation_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028260/2024.csv","profile_path":"atlas/symbol_profiles/028/028260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.25,"MFE_90D_pct":34.25,"MFE_180D_pct":34.25,"MAE_30D_pct":-5.86,"MAE_90D_pct":-5.86,"MAE_180D_pct":-5.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":171700.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":120400.0,"drawdown_after_peak_pct":-22.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_governance_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"028260_2024-01-29_127900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 can allow Stage2/Yellow when governance/value-up theme is backed by NAV discount repair and shareholder-return bridge. Green still needs exact source and capital allocation confirmation."}
```

### 6.2 004990 롯데지주 — holdco value-up theme without NAV/return bridge

Entry row: `2024-02-01 c=31250`.  
Forward path: high `2024-02-13 h=33750`, but later lows reached `2024-06-27 l=24300`, `2024-10-22 l=23600`, and `2024-12-09 l=19780`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L84_C32_004990_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME","case_id":"C32_R12L84_004990_LOTTE_HOLDCO_VALUEUP_THEME_NO_BRIDGE","symbol":"004990","company_name":"롯데지주","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_VALUEUP_THEME_WITHOUT_NAV_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoNAVReturnBridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":31250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_valueup_holdco_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company value-up theme treated as insufficient without NAV discount repair, explicit shareholder-return or control-premium route","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["valueup_theme_spike","holdco_NAV_keyword_proxy","relative_strength_spike"],"stage3_evidence_fields":["NAV_discount_repair_missing","shareholder_return_confirmation_missing","capital_allocation_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv","profile_path":"atlas/symbol_profiles/004/004990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.0,"MFE_90D_pct":8.0,"MFE_180D_pct":8.0,"MAE_30D_pct":-11.04,"MAE_90D_pct":-22.24,"MAE_180D_pct":-24.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":33750.0,"max_drawdown_low_date":"2024-10-22","max_drawdown_low":23600.0,"drawdown_after_peak_pct":-30.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_valueup_peak_without_NAV_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_valueup_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004990_2024-02-01_31250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 needs a NAV/shareholder-return bridge guard. Generic holding-company value-up theme had low MFE and high MAE when governance mechanics did not convert."}
```

### 6.3 000880 한화 — conglomerate/defense holdco theme without direct governance bridge

Entry row: `2024-02-01 c=30000`.  
Forward path: high `2024-02-02 h=32200`, but later lows reached `2024-06-27 l=25400` and remained range-bound before a separate late-year rebound.

```jsonl
{"row_type":"trigger","trigger_id":"R12L84_C32_000880_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_DEFENSE_THEME","case_id":"C32_R12L84_000880_HANWHA_HOLDCO_THEME_NO_GOVERNANCE_BRIDGE","symbol":"000880","company_name":"한화","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONGLOMERATE_HOLDCO_THEME_WITHOUT_DIRECT_GOVERNANCE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-HoldcoDefenseValueupTheme-NoGovernanceBridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":30000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_conglomerate_valueup_defense_holdco_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; conglomerate/defense holdco value-up theme treated as insufficient without direct NAV, shareholder-return or control-premium mechanics","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["conglomerate_valueup_theme","defense_affiliate_readthrough","relative_strength_spike"],"stage3_evidence_fields":["direct_governance_bridge_missing","NAV_discount_repair_missing","shareholder_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000880/2024.csv","profile_path":"atlas/symbol_profiles/000/000880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.33,"MFE_90D_pct":7.33,"MFE_180D_pct":7.33,"MAE_30D_pct":-8.67,"MAE_90D_pct":-15.33,"MAE_180D_pct":-15.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":32200.0,"max_drawdown_low_date":"2024-06-27","max_drawdown_low":25400.0,"drawdown_after_peak_pct":-21.12,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_defense_readthrough_without_governance_bridge_should_remain_watch","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_low_MFE_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_conglomerate_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000880_2024-02-01_30000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Conglomerate/defense read-through alone is not a C32 governance bridge. Without direct NAV/shareholder-return/control-premium mechanics, the signal should stay Watch or blocked from Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L84_028260_SAMSUNGCNT_HOLDCO_NAV_RETURN_BRIDGE","trigger_id":"R12L84_C32_028260_20240129_STAGE2_HOLDCO_NAV_RETURN_BRIDGE","symbol":"028260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C32 requires NAV/shareholder-return bridge rather than value-up headline alone","raw_component_scores_before":{"NAV_discount_repair":15,"shareholder_return_score":14,"control_premium_mechanics":5,"capital_allocation_credibility":13,"governance_policy_tailwind":12,"relative_strength_score":14,"valuation_repricing_score":12,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"NAV_discount_repair":18,"shareholder_return_score":17,"control_premium_mechanics":5,"capital_allocation_credibility":15,"governance_policy_tailwind":13,"relative_strength_score":15,"valuation_repricing_score":13,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"NAV/shareholder-return bridge and high MFE support Yellow-watch; exact source and capital-allocation confirmation still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L84_004990_LOTTE_HOLDCO_VALUEUP_THEME_NO_BRIDGE","trigger_id":"R12L84_C32_004990_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME","symbol":"004990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco value-up headline without NAV/capital-return bridge should be blocked","raw_component_scores_before":{"NAV_discount_repair":4,"shareholder_return_score":3,"control_premium_mechanics":1,"capital_allocation_credibility":3,"governance_policy_tailwind":10,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":32,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"NAV_discount_repair":1,"shareholder_return_score":0,"control_premium_mechanics":0,"capital_allocation_credibility":1,"governance_policy_tailwind":6,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high MAE convert generic value-up/holdco theme into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L84_000880_HANWHA_HOLDCO_THEME_NO_GOVERNANCE_BRIDGE","trigger_id":"R12L84_C32_000880_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_DEFENSE_THEME","symbol":"000880","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"conglomerate/defense read-through without direct governance bridge should remain Watch/blocked","raw_component_scores_before":{"NAV_discount_repair":3,"shareholder_return_score":3,"control_premium_mechanics":0,"capital_allocation_credibility":4,"governance_policy_tailwind":8,"relative_strength_score":11,"valuation_repricing_score":6,"execution_risk_score":-8,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":31,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"NAV_discount_repair":1,"shareholder_return_score":1,"control_premium_mechanics":0,"capital_allocation_credibility":2,"governance_policy_tailwind":5,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"A defensive affiliate read-through is not a governance bridge. Missing NAV/shareholder-return mechanics and low MFE should block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L84_C32_P0_CURRENT","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C32 needs explicit NAV/shareholder-return/control-premium bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":16.53,"avg_MAE_90D_pct":-14.48,"avg_MFE_180D_pct":16.53,"avg_MAE_180D_pct":-15.22,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C32_governance_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L84_C32_P1_SECTOR_SPECIFIC","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P1_L10_governance_valueup_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 governance signals need NAV repair, shareholder return, capital-allocation or control-premium bridge before Stage2-Actionable","changed_axes":["NAV_discount_repair_required","shareholder_return_bridge_required","control_premium_route_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_NAV_shareholder_return_or_control_premium_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":16.53,"avg_MAE_90D_pct":-14.48,"avg_MFE_180D_pct":16.53,"avg_MAE_180D_pct":-15.22,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L84_C32_P2_CANONICAL","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P2_C32_NAV_return_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C32 should reward governance mechanics, not generic value-up or conglomerate read-through themes","changed_axes":["C32_NAV_shareholder_return_bridge_required","C32_holdco_theme_spike_penalty","C32_direct_control_premium_or_capital_allocation_gate"],"changed_thresholds":{"stage2_yellow_gate":"NAV_shareholder_return_or_control_premium_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":16.53,"avg_MAE_90D_pct":-14.48,"avg_MFE_180D_pct":16.53,"avg_MAE_180D_pct":-15.22,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L84_C32_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P3_C32_low_MFE_no_bridge_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and NAV/shareholder-return/control-premium bridge is missing, block Yellow/Green even if value-up policy theme is strong","changed_axes":["C32_low_MFE_guardrail","C32_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_bridge_missing"},"eligible_trigger_count":3,"avg_MFE_90D_pct":16.53,"avg_MAE_90D_pct":-14.48,"avg_MFE_180D_pct":16.53,"avg_MAE_180D_pct":-15.22,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_HOLDCO_NAV_RETURN_BRIDGE_VS_VALUEUP_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":16.53,"avg_MAE90_pct":-14.48,"avg_MFE180_pct":16.53,"avg_MAE180_pct":-15.22,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.33,"interpretation":"C32 needs bridge discipline. 028260 shows true NAV/shareholder-return bridge, while 004990 and 000880 show value-up/holding-company read-through themes that fail or stagnate without direct governance mechanics."}
{"row_type":"stage_transition_summary","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"028260","trigger_type":"Stage2-Actionable-HoldcoNAVShareholderReturnBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_governance_rerating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when NAV/shareholder-return bridge exists; Green requires exact evidence and capital allocation confirmation."}
{"row_type":"stage_transition_summary","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004990","trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoNAVReturnBridge","entry_date":"2024-02-01","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_valueup_holdco_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Value-up/holdco headline without NAV/return bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000880","trigger_type":"Stage2-FalsePositive-HoldcoDefenseValueupTheme-NoGovernanceBridge","entry_date":"2024-02-01","stage2_to_90D_outcome":"weak_stage2_low_MFE_medium_MAE","stage2_to_180D_outcome":"failed_or_stagnant_holdco_theme","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Defense-affiliate read-through without direct governance mechanics should remain Watch/blocked from Yellow/Green."}
{"row_type":"residual_contribution","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"governance_valueup_theme_overcredit_without_NAV_shareholder_return_control_premium_bridge","contribution":"Adds two C32 low-MFE false positives against one NAV/shareholder-return bridge positive, avoiding C32 top-covered and previous loop83 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_NAV_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_HOLDCO_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C32 now has non-top-symbol value-up/holdco theme counterexamples; next R12 loops should exact-URL repair shareholder return, capital allocation, tender/control-premium and NAV-discount evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_NAV_shareholder_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"028260 worked with NAV/shareholder-return bridge proxy; 004990 and 000880 failed or stagnated when direct governance bridge was missing."}
{"row_type":"shadow_weight","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_valueup_holdco_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Holding-company value-up and conglomerate read-through themes showed low MFE without direct NAV/shareholder-return/control-premium mechanics."}
{"row_type":"shadow_weight","round":"R12","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_low_MFE_no_bridge_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and direct governance bridge is missing, block Stage2-Actionable/Yellow even when policy/value-up narrative is active."}
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
  - governance_valueup_theme_overcredit
  - holdco_NAV_return_bridge_missing
  - conglomerate_readthrough_not_direct_governance_bridge
new_axis_proposed:
  - C32_NAV_shareholder_return_bridge_required_shadow_only
  - C32_valueup_holdco_theme_local_4B_watch_guard_shadow_only
  - C32_low_MFE_no_bridge_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C32
  - full_4b_requires_non_price_evidence within C32
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
3. Confirm R12 / L10 / C32 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C32 top-covered symbols and previous loop83 C32 symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C32-scoped safe patch candidates:
   - C32_NAV_shareholder_return_bridge_required
   - C32_valueup_holdco_theme_local_4B_watch_guard
   - C32_low_MFE_no_bridge_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 84
next_round = R13
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```
