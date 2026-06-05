# E2R Stock-Web v12 Residual Research — R12 Loop 86 / L10 / C32

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 86
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: GOVERNANCE_CAPITAL_RETURN_CONTROL_PREMIUM_BRIDGE_VS_HOLDCO_VALUEUP_THEME_DECAY
sector: policy / governance / control premium / tender cap / holdco value-up
output_file: e2r_stock_web_v12_residual_round_R12_loop_86_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 86`.

```text
scheduled_round = R12
scheduled_loop = 86
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

R12 is the policy / event / cross-redteam / miscellaneous lane.  
C32 is selected because the previous R12 loop used C31 policy/subsidy/value-up evidence, while C32 is the governance, control-premium, tender-cap, shareholder-return, and holdco discount bucket.

The No-Repeat Index shows C32 as:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows = 41
symbols = 22
good/bad Stage2 = 16/12
4B/4C = 3/0
top-covered = 010130, 036560, 000150, 041510, 241560, 000990
```

This loop avoids those top-covered symbols and also avoids the previous R12 loop85 C31 symbols:

```text
055550, 034730, 004020
```

The selected set is:

```text
028260, 001040, 004990
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"028260","company_name":"삼성물산","profile_path":"atlas/symbol_profiles/028/028260.json","first_date":"2014-12-18","last_date":"2026-02-20","trading_day_count":2741,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-09-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001040","company_name":"CJ","profile_path":"atlas/symbol_profiles/001/001040.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7745,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1998-06-30","1999-01-29","2007-09-28","2008-01-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"004990","company_name":"롯데지주","profile_path":"atlas/symbol_profiles/004/004990.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7661,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2016-05-17","2017-10-30","2018-04-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"028260","trigger_type":"Stage2-Actionable-GovernanceCapitalReturnControlPremiumBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop85 C31 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"001040","trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoDirectControlPremiumBridge","entry_date":"2024-03-29","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop85 C31 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004990","trigger_type":"Stage2-FalsePositive-HoldcoGovernanceRebound-NoTenderCapitalBridge","entry_date":"2024-02-01","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop85 C31 symbols"}
```

## 4. Research question

C32 is not “holding company or governance theme went up.”  
The useful signal needs a hard economic bridge: tender offer, control-premium floor, capital-allocation reset, cancellation or buyback, direct shareholder-return policy, NAV discount repair, or binding governance event. Without that bridge, the market is only admiring a locked door; the premium is not real unless someone has a key.

Residual question:

```text
Can C32 distinguish:
1. governance / capital-return / control-premium bridge with high MFE and shallow MAE,
2. holdco value-up theme extension without a direct control-premium or tender-cap bridge,
3. holdco governance rebound that decays when tender, buyback, cancellation, and capital-allocation evidence do not confirm?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C32_R12L86_028260_SAMSUNGCNT_GOVERNANCE_CAPITAL_RETURN","symbol":"028260","company_name":"삼성물산","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CAPITAL_RETURN_CONTROL_PREMIUM_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-GovernanceCapitalReturnControlPremiumBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_governance_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Governance/value-up/control-premium proxy produced high MFE with shallow initial MAE. Green still requires exact buyback/cancellation, shareholder-return or binding capital-allocation evidence."}
{"row_type":"case","case_id":"C32_R12L86_001040_CJ_HOLDCO_VALUEUP_NO_DIRECT_BRIDGE","symbol":"001040","company_name":"CJ","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_VALUEUP_THEME_WITHOUT_DIRECT_CONTROL_PREMIUM_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoValueupTheme-NoDirectControlPremiumBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_then_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_holdco_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Holdco/value-up theme had an initial tradable extension, but then opened deep 180D MAE without a direct control-premium, tender, cancellation or NAV-conversion bridge."}
{"row_type":"case","case_id":"C32_R12L86_004990_LOTTE_HOLDCO_GOVERNANCE_REBOUND","symbol":"004990","company_name":"롯데지주","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_GOVERNANCE_REBOUND_WITHOUT_TENDER_CAPITAL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoGovernanceRebound-NoTenderCapitalBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_governance_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Governance/holdco rebound had low MFE and high 180D MAE without tender, buyback/cancellation, direct capital allocation or NAV repair bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 028260 삼성물산 — governance / capital-return / control-premium bridge positive

Entry row: `2024-01-29 c=127900`.  
Observed path: same-day low `2024-01-29 l=120400`, then high `2024-02-19 h=171700`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L86_C32_028260_20240129_STAGE2_GOVERNANCE_CAPITAL_RETURN","case_id":"C32_R12L86_028260_SAMSUNGCNT_GOVERNANCE_CAPITAL_RETURN","symbol":"028260","company_name":"삼성물산","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CAPITAL_RETURN_CONTROL_PREMIUM_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-GovernanceCapitalReturnControlPremiumBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":127900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_governance_capital_return_control_premium_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; governance, capital return and control-premium bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_policy_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["governance_event_proxy","capital_return_proxy","NAV_discount_repair_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_buyback_cancellation_pending","binding_control_premium_or_tender_cap_pending","capital_allocation_source_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028260/2024.csv","profile_path":"atlas/symbol_profiles/028/028260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.25,"MFE_90D_pct":34.25,"MFE_180D_pct":34.25,"MAE_30D_pct":-5.86,"MAE_90D_pct":-5.86,"MAE_180D_pct":-5.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":171700.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":120400.0,"drawdown_after_peak_pct":-30.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_governance_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"028260_2024-01-29_127900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 can allow Stage2/Yellow when governance strength is tied to capital return, NAV repair, binding shareholder-return or control-premium bridge. Green still requires exact source-grade evidence."}
```

### 6.2 001040 CJ — holdco value-up theme without direct control-premium bridge

Entry row: `2024-03-29 c=129800`.  
Observed path: high `2024-05-16 h=152900`, then lows `2024-07-04 l=105700` and `2024-11-15 l=89400`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L86_C32_001040_20240329_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP","case_id":"C32_R12L86_001040_CJ_HOLDCO_VALUEUP_NO_DIRECT_BRIDGE","symbol":"001040","company_name":"CJ","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_VALUEUP_THEME_WITHOUT_DIRECT_CONTROL_PREMIUM_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoDirectControlPremiumBridge","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":129800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holdco_valueup_governance_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holdco value-up theme treated as insufficient without direct tender, control premium, buyback/cancellation, NAV conversion or binding capital allocation bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["holdco_valueup_theme","NAV_discount_repair_theme","relative_strength_extension"],"stage3_evidence_fields":["direct_control_premium_bridge_missing","tender_cap_missing","buyback_cancellation_missing","capital_allocation_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_extension","direct_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001040/2024.csv","profile_path":"atlas/symbol_profiles/001/001040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.31,"MFE_90D_pct":17.80,"MFE_180D_pct":17.80,"MAE_30D_pct":-9.32,"MAE_90D_pct":-18.57,"MAE_180D_pct":-31.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":152900.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":89400.0,"drawdown_after_peak_pct":-41.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_theme_without_direct_control_premium_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","direct_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_then_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_holdco_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001040_2024-03-29_129800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not promote holdco value-up theme to Yellow/Green unless direct control-premium, tender, cancellation or capital-allocation bridge is verified. Initial MFE does not override deep 180D MAE."}
```

### 6.3 004990 롯데지주 — holdco governance rebound without tender/capital bridge

Entry row: `2024-02-01 c=31250`.  
Observed path: local high `2024-02-13 h=33750`, then lows `2024-04-08 l=26350` and `2024-12-09 l=19780`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L86_C32_004990_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_GOVERNANCE_REBOUND","case_id":"C32_R12L86_004990_LOTTE_HOLDCO_GOVERNANCE_REBOUND","symbol":"004990","company_name":"롯데지주","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_GOVERNANCE_REBOUND_WITHOUT_TENDER_CAPITAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-HoldcoGovernanceRebound-NoTenderCapitalBridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":31250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holdco_governance_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holdco governance rebound treated as insufficient without tender-cap, buyback/cancellation, direct capital-return and NAV conversion bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["holdco_governance_rebound","lowPBR_valueup_theme"],"stage3_evidence_fields":["tender_cap_bridge_missing","buyback_cancellation_missing","capital_return_confirmation_missing","NAV_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","capital_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv","profile_path":"atlas/symbol_profiles/004/004990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.00,"MFE_90D_pct":8.00,"MFE_180D_pct":8.00,"MAE_30D_pct":-9.76,"MAE_90D_pct":-15.68,"MAE_180D_pct":-36.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":33750.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":19780.0,"drawdown_after_peak_pct":-41.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_governance_rebound_without_tender_capital_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","capital_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_governance_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004990_2024-02-01_31250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should block holdco governance rebound when tender/capital-allocation bridge is missing. Low MFE and high 180D MAE support local 4B guard."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C32_R12L86_028260_SAMSUNGCNT_GOVERNANCE_CAPITAL_RETURN","trigger_id":"R12L86_C32_028260_20240129_STAGE2_GOVERNANCE_CAPITAL_RETURN","symbol":"028260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C32 requires direct governance/capital-return/control-premium bridge rather than holdco theme alone","raw_component_scores_before":{"governance_event_quality":14,"control_premium_or_tender_score":10,"capital_return_score":13,"NAV_discount_repair_score":12,"buyback_cancellation_score":9,"relative_strength_score":12,"valuation_repricing_score":9,"implementation_risk":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"governance_event_quality":17,"control_premium_or_tender_score":13,"capital_return_score":16,"NAV_discount_repair_score":14,"buyback_cancellation_score":11,"relative_strength_score":13,"valuation_repricing_score":10,"implementation_risk":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Governance and capital-return bridge plus high MFE support Yellow-watch; exact tender/control-premium and capital-allocation evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C32_R12L86_001040_CJ_HOLDCO_VALUEUP_NO_DIRECT_BRIDGE","trigger_id":"R12L86_C32_001040_20240329_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP","symbol":"001040","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco value-up extension without direct control-premium bridge should be blocked from Green and kept Watch/4B-risk","raw_component_scores_before":{"governance_event_quality":8,"control_premium_or_tender_score":1,"capital_return_score":3,"NAV_discount_repair_score":7,"buyback_cancellation_score":0,"relative_strength_score":12,"valuation_repricing_score":6,"implementation_risk":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":16,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"governance_event_quality":3,"control_premium_or_tender_score":0,"capital_return_score":0,"NAV_discount_repair_score":2,"buyback_cancellation_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"implementation_risk":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Initial MFE is not enough when direct tender/control-premium bridge is absent and 180D MAE deepens."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C32_R12L86_004990_LOTTE_HOLDCO_GOVERNANCE_REBOUND","trigger_id":"R12L86_C32_004990_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_GOVERNANCE_REBOUND","symbol":"004990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco governance rebound without tender/capital bridge should remain Watch/blocked","raw_component_scores_before":{"governance_event_quality":7,"control_premium_or_tender_score":0,"capital_return_score":2,"NAV_discount_repair_score":5,"buyback_cancellation_score":0,"relative_strength_score":10,"valuation_repricing_score":5,"implementation_risk":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":8,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"governance_event_quality":2,"control_premium_or_tender_score":0,"capital_return_score":0,"NAV_discount_repair_score":1,"buyback_cancellation_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"implementation_risk":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high 180D MAE require tender/capital-return bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L86_C32_P0_CURRENT","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C32 needs explicit control-premium, tender, cancellation, capital-return and NAV conversion bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":20.02,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":20.02,"avg_MAE180_pct":-24.56,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C32_direct_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L86_C32_P1_SECTOR_SPECIFIC","round":"R12","loop":86,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P1_L10_governance_control_premium_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 governance signals need tender/control-premium, buyback/cancellation, direct capital return, binding capital allocation or NAV conversion bridge before Stage2-Actionable","changed_axes":["direct_control_premium_required","tender_or_capital_return_required","holdco_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_tender_control_premium_buyback_cancellation_capital_return_or_NAV_conversion_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":20.02,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":20.02,"avg_MAE180_pct":-24.56,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L86_C32_P2_CANONICAL","round":"R12","loop":86,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P2_C32_direct_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C32 should reward hard governance/control-premium conversion, not holdco value-up theme beta","changed_axes":["C32_direct_tender_control_premium_bridge_required","C32_holdco_theme_local_4B_guard","C32_late_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"direct_governance_capital_return_or_control_premium_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":20.02,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":20.02,"avg_MAE180_pct":-24.56,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L86_C32_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":86,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P3_C32_high_180D_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If direct bridge is missing and MFE90<20 with MAE180<=-30, block Yellow/Green and route to 4B-watch","changed_axes":["C32_high_180D_MAE_guardrail","C32_holdco_theme_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MFE90_lt_20_and_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":20.02,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":20.02,"avg_MAE180_pct":-24.56,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_DIRECT_GOVERNANCE_BRIDGE_VS_HOLDCO_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":20.02,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":20.02,"avg_MAE180_pct":-24.56,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_bridge_missing_MFE90_lt_20_and_MAE180_le_minus30":0.67,"interpretation":"C32 needs bridge discipline. 삼성물산 shows governance/capital-return bridge can rerate with shallow MAE, while CJ and 롯데지주 show holdco/value-up theme strength can fade without direct tender, control premium, cancellation, capital allocation or NAV conversion bridge."}
{"row_type":"stage_transition_summary","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"028260","trigger_type":"Stage2-Actionable-GovernanceCapitalReturnControlPremiumBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_governance_capital_return_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when governance event is tied to capital return, NAV repair or control-premium bridge; Green requires exact tender/cancellation/capital-allocation evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"001040","trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoDirectControlPremiumBridge","entry_date":"2024-03-29","stage2_to_90D_outcome":"mixed_initial_MFE_but_bridge_missing","stage2_to_180D_outcome":"failed_holdco_valueup_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Holdco value-up theme without direct control-premium/tender/capital-allocation bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004990","trigger_type":"Stage2-FalsePositive-HoldcoGovernanceRebound-NoTenderCapitalBridge","entry_date":"2024-02-01","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"failed_holdco_governance_rebound_high_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Holdco governance rebound without tender/capital-return bridge should remain Watch/blocked."}
{"row_type":"residual_contribution","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"holdco_valueup_theme_overcredit_without_direct_governance_control_premium_capital_bridge","contribution":"Adds two C32 local 4B/high-180D-MAE counterexamples against one governance/capital-return bridge positive, avoiding C32 top-covered and previous R12 loop85 C31 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CAPITAL_RETURN_CONTROL_PREMIUM_BRIDGE_VS_HOLDCO_VALUEUP_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C32 now has non-top-symbol holdco/value-up theme counterexamples; next R12 loops should exact-URL repair tender, control premium, buyback/cancellation, capital allocation, NAV conversion and shareholder-return evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_direct_tender_control_premium_capital_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"028260 worked with governance/capital-return proxy; 001040 and 004990 failed when only holdco/value-up/governance rebound theme existed."}
{"row_type":"shadow_weight","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_holdco_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Holdco/value-up theme rows produced deep 180D MAE when tender/control-premium/capital-return bridge was missing."}
{"row_type":"shadow_weight","round":"R12","loop":"86","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_high_180D_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If direct bridge is missing and MFE90<20 with MAE180<=-30, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - holdco_valueup_theme_overcredit
  - direct_control_premium_bridge_missing
  - tender_capital_allocation_bridge_missing
  - high_180D_MAE_without_governance_conversion
new_axis_proposed:
  - C32_direct_tender_control_premium_capital_bridge_required_shadow_only
  - C32_holdco_theme_local_4B_watch_guard_shadow_only
  - C32_high_180D_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C32
  - full_4b_requires_non_price_evidence within C32
  - hard_4c_thesis_break_routes_to_4c within C32
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
3. Confirm R12 / L10 / C32 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C32 top-covered symbols
   - previous R12 loop85 C31 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C32-scoped safe patch candidates:
   - C32_direct_tender_control_premium_capital_bridge_required
   - C32_holdco_theme_local_4B_watch_guard
   - C32_high_180D_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 86
next_round = R13
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```
