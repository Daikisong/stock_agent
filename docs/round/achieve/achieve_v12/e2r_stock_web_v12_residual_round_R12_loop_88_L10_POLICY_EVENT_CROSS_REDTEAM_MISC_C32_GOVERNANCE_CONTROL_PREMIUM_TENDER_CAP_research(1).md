# E2R Stock-Web v12 Residual Research — R12 Loop 88 / L10 / C32

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 88
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_PREMIUM_HOLDCO_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_RESTRUCTURING_THEME_DECAY
sector: governance / control premium / tender cap / holding company / capital return
output_file: e2r_stock_web_v12_residual_round_R12_loop_88_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 88`.

```text
scheduled_round = R12
scheduled_loop = 88
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

R12 is the policy / event / governance / cross-misc lane.  
C32 is selected because the immediately previous R12 loop used C31 policy/subsidy/legislation event, while C32 still has large false-positive risk around governance headlines, tender-offer vocabulary, holding-company discount repair, split/restructuring events, and control-premium expectation.

No-Repeat Index snapshot:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows = 41
symbols = 22
good/bad Stage2 = 16/12
4B/4C = 3/0
top-covered = 010130, 036560, 000150, 041510, 241560, 000990
```

This loop avoids the C32 top-covered symbols and also avoids recent R12 loop symbols:

```text
R12 loop85 C31: 055550, 034730, 004020
R12 loop86 C32: 028260, 001040, 004990
R12 loop87 C31: 036460, 004090, 024060
```

Candidate notes:

```text
005810 / 풍산홀딩스 was checked but rejected as representative because the 2024 path has a large raw discontinuity / share-count change around March and would require data repair first.
```

Selected symbols:

```text
000240, 001230, 004800
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"000240","company_name":"한국앤컴퍼니","profile_path":"atlas/symbol_profiles/000/000240.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7738,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1997-01-03","1998-08-03","1999-05-21","1999-06-25","2012-10-04","2013-07-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001230","company_name":"동국홀딩스","profile_path":"atlas/symbol_profiles/001/001230.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7751,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1999-01-27","1999-07-13","1999-09-21","2004-05-20","2017-05-08","2023-06-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"2023 spin-off / name-change candidate exists before the selected 2024 forward window. 2024 path is usable but holding-company split background should remain evidence-quality watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"004800","company_name":"효성","profile_path":"atlas/symbol_profiles/004/004800.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7711,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1998-12-14","1999-12-20","2018-07-13","2019-01-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the selected 2024 forward window. Late 2024 share-count drift is marked data-quality watch before any patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; late_2024_share_count_drift_watch"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000240","trigger_type":"Stage2-Actionable-ControlPremiumHoldcoCapitalReturnBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"001230","trigger_type":"Stage2-FalsePositive-HoldcoSplitThemeSpike-NoTenderCapitalReturnBridge","entry_date":"2024-02-02","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004800","trigger_type":"Stage2-FalsePositive-HoldcoRestructuringTheme-NoMinorityReturnBridge","entry_date":"2024-02-01","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
```

## 4. Research question

C32 is not “지배구조 뉴스가 있다.”  
The useful governance signal must prove a bridge from governance event to investable economics: tender certainty, control premium visibility, shareholder-return mechanism, minority-holder protection, buyback/cancellation, capital-allocation clarity, holding-company discount repair, legal certainty, and valuation cap. Without that bridge, a governance headline is a locked door with a shiny handle; it may invite the market closer, but it does not open value by itself.

Residual question:

```text
Can C32 distinguish:
1. control-premium / holdco capital-return bridge with good MFE and shallow MAE,
2. holdco split or restructuring theme spike that has no tender, cancellation, minority-return or valuation-cap bridge,
3. holding-company restructuring theme where later bursts should not validate the original weak entry without fresh shareholder-return mechanics?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C32_R12L88_000240_HANKOOK_CONTROL_PREMIUM_HOLDCO_BRIDGE","symbol":"000240","company_name":"한국앤컴퍼니","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_HOLDCO_CAPITAL_RETURN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ControlPremiumHoldcoCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_shallow_MAE","current_profile_verdict":"current_profile_correct_if_control_premium_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Control-premium / holding-company capital-return proxy produced MFE above 20% with shallow drawdown. Green still requires exact tender/capital-return/minority-protection evidence."}
{"row_type":"case","case_id":"C32_R12L88_001230_DONGKUK_HOLDCO_SPLIT_THEME_SPIKE","symbol":"001230","company_name":"동국홀딩스","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_SPLIT_THEME_SPIKE_WITHOUT_TENDER_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoSplitThemeSpike-NoTenderCapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_local_MFE_but_high_MAE_no_bridge","current_profile_verdict":"current_profile_false_positive_if_split_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Holding-company split theme had local MFE after the spike, but then large MAE opened without tender certainty, buyback/cancellation, capital-return or minority-protection bridge."}
{"row_type":"case","case_id":"C32_R12L88_004800_HYOSUNG_HOLDCO_RESTRUCTURING_THEME","symbol":"004800","company_name":"효성","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_RESTRUCTURING_THEME_WITHOUT_MINORITY_RETURN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoRestructuringTheme-NoMinorityReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_low_MFE_high_180D_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_holdco_restructuring_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Holding-company restructuring theme had low initial MFE and meaningful later MAE without minority-return or cancellation bridge. Q4 price bursts should not validate the original weak entry. Data-quality watch is retained for late-2024 share-count drift."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 000240 한국앤컴퍼니 — control-premium / holdco capital-return bridge positive

Entry row: `2024-01-29 c=15810`.  
Observed path: high `2024-02-08 h=19460`, low `2024-01-31 l=15340`, and later Q4 control-premium-like spike `2024-12-17 h=21900`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L88_C32_000240_20240129_STAGE2_CONTROL_PREMIUM_HOLDCO","case_id":"C32_R12L88_000240_HANKOOK_CONTROL_PREMIUM_HOLDCO_BRIDGE","symbol":"000240","company_name":"한국앤컴퍼니","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_HOLDCO_CAPITAL_RETURN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ControlPremiumHoldcoCapitalReturnBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":15810.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_control_premium_holdco_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; control-premium, holding-company discount repair and capital-return bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["control_premium_proxy","holdco_discount_repair_proxy","capital_return_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_tender_or_control_premium_source_pending","minority_holder_protection_pending","buyback_cancellation_pending","valuation_cap_pending"],"stage4b_evidence_fields":["price_extension_watch","late_event_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000240/2024.csv","profile_path":"atlas/symbol_profiles/000/000240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.09,"MFE_90D_pct":23.09,"MFE_180D_pct":23.09,"MAE_30D_pct":-2.97,"MAE_90D_pct":-3.04,"MAE_180D_pct":-3.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-08","peak_price":19460.0,"max_drawdown_low_date":"2024-04-02","max_drawdown_low":15330.0,"drawdown_after_peak_pct":-21.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_tender_capital_return_and_minority_protection_evidence","four_b_evidence_type":["price_extension_watch","late_event_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_shallow_MAE","current_profile_verdict":"current_profile_correct_if_control_premium_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000240_2024-01-29_15810","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 can allow Stage2/Yellow when governance strength is tied to control-premium visibility, capital-return mechanics, minority protection and valuation-cap evidence. Green still requires exact source-grade evidence."}
```

### 6.2 001230 동국홀딩스 — holdco split theme spike without tender/capital-return bridge

Entry row: `2024-02-02 c=10250`, after the split-theme spike began.  
Observed path: high `2024-02-05 h=11350`, then the move faded with lows around the 7,800~8,000 zone.

```jsonl
{"row_type":"trigger","trigger_id":"R12L88_C32_001230_20240202_STAGE2_FALSE_POSITIVE_HOLDCO_SPLIT_THEME","case_id":"C32_R12L88_001230_DONGKUK_HOLDCO_SPLIT_THEME_SPIKE","symbol":"001230","company_name":"동국홀딩스","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_SPLIT_THEME_SPIKE_WITHOUT_TENDER_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HoldcoSplitThemeSpike-NoTenderCapitalReturnBridge","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":10250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holdco_split_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company split theme treated as insufficient without tender, cancellation, capital-return, minority-protection or valuation-cap bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["holdco_split_theme","relative_strength_spike"],"stage3_evidence_fields":["tender_certainty_missing","capital_return_bridge_missing","minority_protection_missing","valuation_cap_missing"],"stage4b_evidence_fields":["price_only_local_peak","capital_return_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001230/2024.csv","profile_path":"atlas/symbol_profiles/001/001230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.73,"MFE_90D_pct":10.73,"MFE_180D_pct":10.73,"MAE_30D_pct":-23.51,"MAE_90D_pct":-23.51,"MAE_180D_pct":-23.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":11350.0,"max_drawdown_low_date":"2024-04-08","max_drawdown_low":7850.0,"drawdown_after_peak_pct":-30.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_split_theme_without_tender_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","capital_return_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_but_high_MAE_no_bridge","current_profile_verdict":"current_profile_false_positive_if_split_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"2024_window_after_2023_split_candidate","same_entry_group_id":"001230_2024-02-02_10250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not promote a holdco split theme spike unless tender certainty, buyback/cancellation, minority-holder protection and capital-return bridge are exact-evidence repaired."}
```

### 6.3 004800 효성 — holdco restructuring theme without minority-return bridge

Entry row: `2024-02-01 c=65100`.  
Observed path: local high `2024-02-02 h=65900`, then drawdown through spring and late-year share-count/data-quality watch around the Q4 path.

```jsonl
{"row_type":"trigger","trigger_id":"R12L88_C32_004800_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_RESTRUCTURING","case_id":"C32_R12L88_004800_HYOSUNG_HOLDCO_RESTRUCTURING_THEME","symbol":"004800","company_name":"효성","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_RESTRUCTURING_THEME_WITHOUT_MINORITY_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-HoldcoRestructuringTheme-NoMinorityReturnBridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":65100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holdco_restructuring_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company restructuring theme treated as insufficient without minority-return bridge, buyback/cancellation, tender or valuation-cap clarity","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["holdco_restructuring_theme","relative_strength_rebound"],"stage3_evidence_fields":["minority_return_bridge_missing","buyback_cancellation_missing","tender_certainty_missing","valuation_cap_missing"],"stage4b_evidence_fields":["price_only_local_extension","late_rebound_not_entry_validation","data_quality_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004800/2024.csv","profile_path":"atlas/symbol_profiles/004/004800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.23,"MFE_90D_pct":3.53,"MFE_180D_pct":3.53,"MAE_30D_pct":-9.37,"MAE_90D_pct":-12.90,"MAE_180D_pct":-24.50,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":67400.0,"max_drawdown_low_date":"2024-11-25","max_drawdown_low":43550.0,"drawdown_after_peak_pct":-35.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_restructuring_theme_without_minority_return_bridge_should_remain_watch; late_spike_not_entry_validation","four_b_evidence_type":["price_only","late_rebound_not_entry_validation","data_quality_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_180D_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_holdco_restructuring_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["late_2024_share_count_drift_watch_before_patch"],"corporate_action_window_status":"2024_entry_clean; late_2024_share_count_drift_watch","same_entry_group_id":"004800_2024-02-01_65100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not treat generic holding-company restructuring strength as tender/control-premium evidence. Without minority-return, buyback/cancellation or valuation-cap bridge, low MFE and later drawdown require Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C32_R12L88_000240_HANKOOK_CONTROL_PREMIUM_HOLDCO_BRIDGE","trigger_id":"R12L88_C32_000240_20240129_STAGE2_CONTROL_PREMIUM_HOLDCO","symbol":"000240","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C32 requires control-premium and capital-return mechanics rather than governance theme alone","raw_component_scores_before":{"control_premium_score":13,"tender_certainty_score":10,"capital_return_score":11,"minority_protection_score":9,"buyback_cancellation_score":8,"valuation_cap_score":8,"relative_strength_score":12,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"control_premium_score":16,"tender_certainty_score":12,"capital_return_score":14,"minority_protection_score":12,"buyback_cancellation_score":10,"valuation_cap_score":10,"relative_strength_score":13,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Control-premium / capital-return bridge and shallow MAE support Yellow-watch; exact tender/cancellation/minority evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C32_R12L88_001230_DONGKUK_HOLDCO_SPLIT_THEME_SPIKE","trigger_id":"R12L88_C32_001230_20240202_STAGE2_FALSE_POSITIVE_HOLDCO_SPLIT_THEME","symbol":"001230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco split theme without tender/capital-return bridge should be blocked","raw_component_scores_before":{"control_premium_score":3,"tender_certainty_score":0,"capital_return_score":1,"minority_protection_score":0,"buyback_cancellation_score":0,"valuation_cap_score":1,"relative_strength_score":11,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"control_premium_score":0,"tender_certainty_score":0,"capital_return_score":0,"minority_protection_score":0,"buyback_cancellation_score":0,"valuation_cap_score":0,"relative_strength_score":3,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is outweighed by high MAE and missing tender/capital-return bridge."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C32_R12L88_004800_HYOSUNG_HOLDCO_RESTRUCTURING_THEME","trigger_id":"R12L88_C32_004800_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_RESTRUCTURING","symbol":"004800","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco restructuring theme without minority-return bridge should remain Watch/blocked","raw_component_scores_before":{"control_premium_score":2,"tender_certainty_score":0,"capital_return_score":1,"minority_protection_score":0,"buyback_cancellation_score":0,"valuation_cap_score":1,"relative_strength_score":6,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"control_premium_score":0,"tender_certainty_score":0,"capital_return_score":0,"minority_protection_score":0,"buyback_cancellation_score":0,"valuation_cap_score":0,"relative_strength_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Low MFE and missing minority-return/cancellation bridge keep the original row Watch/4B. Late price bursts are not entry validation."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L88_C32_P0_CURRENT","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C32 needs explicit tender/control-premium/capital-return/minority-protection taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":12.45,"avg_MAE90_pct":-13.15,"avg_MFE180_pct":12.45,"avg_MAE180_pct":-17.02,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C32_control_premium_capital_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L88_C32_P1_SECTOR_SPECIFIC","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P1_L10_governance_control_premium_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 governance signals need tender certainty, control premium, capital return, minority protection, buyback/cancellation or valuation cap before Stage2-Actionable","changed_axes":["control_premium_required","capital_return_required","governance_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_tender_control_premium_capital_return_minority_buyback_or_valuation_cap_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":12.45,"avg_MAE90_pct":-13.15,"avg_MFE180_pct":12.45,"avg_MAE180_pct":-17.02,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L88_C32_P2_CANONICAL","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P2_C32_tender_capital_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C32 should reward control-premium/capital-return mechanics, not holding-company theme labels","changed_axes":["C32_control_premium_capital_return_bridge_required","C32_holdco_theme_local_4B_guard","C32_late_rebound_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"control_premium_or_tender_plus_capital_return_or_minority_protection_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":12.45,"avg_MAE90_pct":-13.15,"avg_MFE180_pct":12.45,"avg_MAE180_pct":-17.02,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L88_C32_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P3_C32_missing_bridge_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If tender/capital-return bridge is missing and MAE90<=-12, block Yellow/Green even when local MFE exists; late price spikes do not validate the original weak row","changed_axes":["C32_missing_bridge_guardrail","C32_late_rebound_not_validation"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE90_le_minus_12"},"eligible_trigger_count":3,"avg_MFE90_pct":12.45,"avg_MAE90_pct":-13.15,"avg_MFE180_pct":12.45,"avg_MAE180_pct":-17.02,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_CONTROL_PREMIUM_BRIDGE_VS_HOLDCO_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":12.45,"avg_MAE90_pct":-13.15,"avg_MFE180_pct":12.45,"avg_MAE180_pct":-17.02,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_bridge_missing_MAE90_le_minus12":0.67,"interpretation":"C32 needs bridge discipline. 한국앤컴퍼니 shows control-premium/holdco capital-return bridge can support Yellow-watch, while 동국홀딩스 and 효성 show holdco split/restructuring themes should not be promoted without tender certainty, capital-return mechanics, minority protection, cancellation or valuation-cap evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000240","trigger_type":"Stage2-Actionable-ControlPremiumHoldcoCapitalReturnBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_shallow_MAE","stage2_to_180D_outcome":"positive_control_premium_holdco_bridge","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when control premium and capital-return bridge exists; Green requires exact tender/cancellation/minority-protection evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"001230","trigger_type":"Stage2-FalsePositive-HoldcoSplitThemeSpike-NoTenderCapitalReturnBridge","entry_date":"2024-02-02","stage2_to_90D_outcome":"price_only_local_MFE_high_MAE","stage2_to_180D_outcome":"failed_holdco_split_theme_no_capital_return_bridge","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Holdco split theme without tender/capital-return bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004800","trigger_type":"Stage2-FalsePositive-HoldcoRestructuringTheme-NoMinorityReturnBridge","entry_date":"2024-02-01","stage2_to_90D_outcome":"weak_stage2_low_MFE_moderate_MAE","stage2_to_180D_outcome":"weak_original_entry_late_spike_not_validation","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Holdco restructuring theme without minority-return/cancellation bridge should remain Watch; late Q4 spike is not original-entry validation."}
{"row_type":"residual_contribution","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"governance_holdco_theme_overcredit_without_control_premium_capital_return_minority_bridge","contribution":"Adds two C32 local 4B/Watch counterexamples against one control-premium holdco positive, avoiding C32 top-covered and previous R12 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_HOLDCO_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_RESTRUCTURING_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C32 now has non-top-symbol control-premium holdco positive and two holdco split/restructuring weak-bridge counterexamples; next R12 loops should exact-URL repair tender certainty, buyback/cancellation, minority protection, capital allocation and valuation-cap evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_control_premium_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"000240 worked when control-premium/capital-return proxy was present; 001230 and 004800 were weak or failed when only split/restructuring theme existed."}
{"row_type":"shadow_weight","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_holdco_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Holding-company split/restructuring rows showed missing tender/capital-return/minority bridge and drawdown risk even when local MFE existed."}
{"row_type":"shadow_weight","round":"R12","loop":"88","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_late_rebound_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"004800 shows late price bursts should not retroactively validate the original weak governance-theme entry unless fresh tender/capital-return/minority-protection evidence is repaired."}
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
  - holdco_split_theme_overcredit
  - holdco_restructuring_theme_overcredit
  - tender_certainty_bridge_missing
  - capital_return_minority_protection_bridge_missing
new_axis_proposed:
  - C32_control_premium_capital_return_bridge_required_shadow_only
  - C32_holdco_theme_local_4B_watch_guard_shadow_only
  - C32_late_rebound_not_entry_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.  
`004800` has late-2024 share-count drift watch in the selected price path, so the original 90D weak-entry finding is usable, but any future production patch should exact-repair the price path and evidence URLs.  
`005810` was not used as representative because March 2024 raw discontinuity / share-count movement would require data repair first.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 004800 before patch
excluded_candidate = 005810 due to raw discontinuity / share-count watch
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
   - previous R12 loop85 C31 symbols
   - previous R12 loop86 C32 symbols
   - previous R12 loop87 C31 symbols
6. Confirm 005810 was excluded from representative use due to raw discontinuity/share-count repair requirement.
7. Keep 004800 in data-quality watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C32-scoped safe patch candidates:
   - C32_control_premium_capital_return_bridge_required
   - C32_holdco_theme_local_4B_watch_guard
   - C32_late_rebound_not_entry_validation_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 88
next_round = R13
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```
