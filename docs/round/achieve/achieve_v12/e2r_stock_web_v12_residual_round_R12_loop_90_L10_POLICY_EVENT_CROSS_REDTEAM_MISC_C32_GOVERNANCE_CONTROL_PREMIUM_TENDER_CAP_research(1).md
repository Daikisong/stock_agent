# E2R Stock-Web v12 Residual Research — R12 Loop 90 / L10 / C32

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 90
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: BIO_HOLDCO_CONTROL_PREMIUM_EVENT_BRIDGE_VS_HOLDCO_DISCOUNT_VOCABULARY_DECAY
sector: policy / event / governance / control premium / tender cap / holdco discount / shareholder return
output_file: e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 90`.

```text
scheduled_round = R12
scheduled_loop = 90
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

R12 is restricted to policy / event / governance / cross-misc.  
C32 is selected because the immediately previous R12 loop used C31 policy-to-cash, and the R12 alternation returns to governance / control-premium / tender-cap.

No-Repeat Index snapshot:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows = 41
symbols = 22
good/bad Stage2 = 16/12
4B/4C = 3/0
top-covered = 010130, 036560, 000150, 041510, 241560, 000990
```

This loop avoids the C32 top-covered list and recent R12 loop symbols:

```text
R12 loop85 C31: 055550, 034730, 004020
R12 loop86 C32: 028260, 001040, 004990
R12 loop87 C31: 036460, 004090, 024060
R12 loop88 C32: 000240, 001230, 004800
R12 loop89 C31: 071320, 035250, 039130
```

Candidate hygiene note:

```text
During this execution path, R11/C03, R10/C30, R9/C29 and R8/C27 candidate rows were touched or one stale MD path was regenerated in the surrounding tool calls.
Those rows are not used in this R12/C32 output.
```

Selected symbols:

```text
008930, 006840, 003030
```

This loop tests:

```text
bio-holdco control-premium / ownership-event bridge
vs
airline/consumer holding-company discount rebound without tender, buyback or asset-sale bridge
vs
steel-pipe holding-company NAV vocabulary without control-premium or shareholder-return catalyst
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"008930","company_name":"한미사이언스","profile_path":"atlas/symbol_profiles/008/008930.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7726,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-04-19","2010-07-30","2010-10-21","2012-05-14"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"006840","company_name":"AK홀딩스","profile_path":"atlas/symbol_profiles/006/006840.json","first_date":"1999-08-11","last_date":"2026-02-20","trading_day_count":6528,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2011-11-24","2012-09-17","2012-11-05","2012-12-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"003030","company_name":"세아제강지주","profile_path":"atlas/symbol_profiles/003/003030.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7715,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2001-07-30","2018-10-05","2019-01-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"008930","trigger_type":"Stage2-Actionable-BioHoldcoControlPremiumOwnershipEventBridge-Positive","entry_date":"2024-01-12","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"006840","trigger_type":"Stage2-FalsePositive-HoldcoDiscountReboundNoTenderBuybackAssetSaleBridge","entry_date":"2024-01-02","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003030","trigger_type":"Stage2-FalsePositive-SteelPipeHoldcoNAVVocabularyNoControlPremiumReturnBridge","entry_date":"2024-01-02","duplicate_status":"new C32 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
```

## 4. Research question

C32 is not “지배구조나 홀딩스 이름이 붙었다.”  
The useful governance / control-premium signal must prove an event bridge:

```text
credible control-premium event
tender or block-trade probability
ownership contest or voting path
asset-sale / restructuring path
minority-shareholder alignment
buyback or cancellation mechanism
NAV discount closure
legal / board / shareholder-meeting milestone
cash-return visibility
```

A governance headline without this bridge is a key drawn on paper. It looks like access, but until it turns in the lock, the discount stays locked inside the holding-company door.

Residual question:

```text
Can C32 distinguish:
1. explicit control-premium / ownership-event bridge with large MFE and tolerable early MAE,
2. holding-company discount vocabulary where no tender, buyback, asset sale or minority-return mechanism exists,
3. NAV-discount language where no control-premium, legal milestone or shareholder-return catalyst closes the gap?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C32_R12L90_008930_HANMI_SCIENCE_CONTROL_PREMIUM","symbol":"008930","company_name":"한미사이언스","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"BIO_HOLDCO_CONTROL_PREMIUM_OWNERSHIP_EVENT_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BioHoldcoControlPremiumOwnershipEventBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_entry_MAE_but_event_volatility_watch","current_profile_verdict":"current_profile_correct_if_control_premium_ownership_event_bridge_required","price_source":"Songdaiki/stock-web","notes":"Bio-holdco ownership/control-premium event produced a rapid high MFE after the selected entry. It remains Green-strict because governance outcomes can reverse and exact legal/ownership/voting evidence is required."}
{"row_type":"case","case_id":"C32_R12L90_006840_AK_HOLDINGS_DISCOUNT_REBOUND","symbol":"006840","company_name":"AK홀딩스","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_DISCOUNT_REBOUND_WITHOUT_TENDER_BUYBACK_ASSET_SALE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoDiscountReboundNoTenderBuybackAssetSaleBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_control_premium_bridge","current_profile_verdict":"current_profile_false_positive_if_holdco_discount_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Holding-company discount rebound had only low MFE and then deep drawdown without tender, buyback, asset sale, restructuring or cash-return bridge."}
{"row_type":"case","case_id":"C32_R12L90_003030_SEAH_HOLDCO_NAV_VOCABULARY","symbol":"003030","company_name":"세아제강지주","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"STEEL_PIPE_HOLDCO_NAV_VOCABULARY_WITHOUT_CONTROL_PREMIUM_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SteelPipeHoldcoNAVVocabularyNoControlPremiumReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_return_bridge","current_profile_verdict":"current_profile_false_positive_if_NAV_discount_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Holdco/NAV discount vocabulary did not produce durable original-entry validation. Without control-premium event, shareholder-return mechanism or legal milestone, low MFE and deep MAE require 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 008930 한미사이언스 — bio-holdco control-premium / ownership-event bridge

Entry row: `2024-01-12 c=38400`.  
Observed path: entry low `2024-01-12 l=37200`, sharp event high `2024-01-16 h=56200`, and later governance volatility with a full-year low around `2024-12-09 l=28200`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L90_C32_008930_20240112_STAGE2_CONTROL_PREMIUM_EVENT","case_id":"C32_R12L90_008930_HANMI_SCIENCE_CONTROL_PREMIUM","symbol":"008930","company_name":"한미사이언스","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"BIO_HOLDCO_CONTROL_PREMIUM_OWNERSHIP_EVENT_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BioHoldcoControlPremiumOwnershipEventBridge-Positive","trigger_date":"2024-01-12","entry_date":"2024-01-12","entry_price":38400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_control_premium_ownership_event_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ownership event, control-premium probability, board/shareholder vote path and transaction structure treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["control_premium_event_proxy","ownership_contest_proxy","board_or_shareholder_vote_path_proxy","relative_strength_event"],"stage3_evidence_fields":["exact_transaction_structure_pending","voting_path_source_pending","legal_milestone_pending","minority_shareholder_alignment_pending"],"stage4b_evidence_fields":["event_volatility_watch","late_drawdown_watch"],"stage4c_evidence_fields":["event_reversal_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":46.35,"MFE_90D_pct":46.35,"MFE_180D_pct":46.35,"MAE_30D_pct":-3.13,"MAE_90D_pct":-18.62,"MAE_180D_pct":-26.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":56200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":28200.0,"drawdown_after_peak_pct":-49.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_control_premium_event_but_Green_requires_exact_ownership_voting_legal_cash_return_evidence","four_b_evidence_type":["event_volatility_watch","late_drawdown_watch"],"four_c_protection_label":"event_reversal_watch_only","trigger_outcome_label":"positive_high_MFE_low_entry_MAE_but_event_volatility_watch","current_profile_verdict":"current_profile_correct_if_control_premium_ownership_event_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"008930_2024-01-12_38400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 can allow Stage2/Yellow when governance strength is tied to an explicit ownership/control-premium event, voting/legal path and minority-shareholder economics. Green still requires exact source-grade evidence because event reversals can be violent."}
```

### 6.2 006840 AK홀딩스 — holdco discount rebound without tender/buyback/asset-sale bridge

Entry row: `2024-01-02 c=17090`.  
Observed path: high `2024-02-19 h=18030`, then long drawdown to `2024-12-30 l=9630`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L90_C32_006840_20240102_STAGE2_FALSE_POSITIVE_HOLDCO_DISCOUNT","case_id":"C32_R12L90_006840_AK_HOLDINGS_DISCOUNT_REBOUND","symbol":"006840","company_name":"AK홀딩스","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_DISCOUNT_REBOUND_WITHOUT_TENDER_BUYBACK_ASSET_SALE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HoldcoDiscountReboundNoTenderBuybackAssetSaleBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":17090.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holdco_discount_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company discount rebound treated as insufficient without tender, buyback/cancellation, asset sale, restructuring or cash-return bridge","evidence_source_type":"historical_public_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["holdco_discount_keyword","relative_strength_rebound"],"stage3_evidence_fields":["tender_offer_missing","buyback_cancellation_missing","asset_sale_missing","cash_return_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","holdco_discount_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006840/2024.csv","profile_path":"atlas/symbol_profiles/006/006840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.51,"MFE_90D_pct":5.50,"MFE_180D_pct":5.50,"MAE_30D_pct":-9.30,"MAE_90D_pct":-16.33,"MAE_180D_pct":-43.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":18030.0,"max_drawdown_low_date":"2024-12-30","max_drawdown_low":9630.0,"drawdown_after_peak_pct":-46.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_discount_rebound_without_tender_buyback_asset_sale_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","holdco_discount_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_control_premium_bridge","current_profile_verdict":"current_profile_false_positive_if_holdco_discount_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"006840_2024-01-02_17090","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not promote holding-company discount rebound without tender, buyback/cancellation, asset sale, restructuring, legal milestone or cash-return bridge. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 003030 세아제강지주 — holdco/NAV vocabulary without control-premium or shareholder-return bridge

Entry row: `2024-01-02 c=236000`.  
Observed path: high `2024-03-27 h=240500`, then long drawdown to `2024-10-22 l=156500` and `2024-12-09 l=162300`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L90_C32_003030_20240102_STAGE2_FALSE_POSITIVE_STEEL_HOLDCO_NAV","case_id":"C32_R12L90_003030_SEAH_HOLDCO_NAV_VOCABULARY","symbol":"003030","company_name":"세아제강지주","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"STEEL_PIPE_HOLDCO_NAV_VOCABULARY_WITHOUT_CONTROL_PREMIUM_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SteelPipeHoldcoNAVVocabularyNoControlPremiumReturnBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":236000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holdco_NAV_discount_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holdco/NAV discount vocabulary treated as insufficient without control-premium event, tender, buyback/cancellation, asset sale or shareholder-return bridge","evidence_source_type":"historical_public_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["holdco_NAV_discount_keyword","relative_strength_rebound"],"stage3_evidence_fields":["control_premium_event_missing","tender_or_block_trade_missing","shareholder_return_mechanism_missing","legal_milestone_missing"],"stage4b_evidence_fields":["low_MFE_watch","NAV_discount_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003030/2024.csv","profile_path":"atlas/symbol_profiles/003/003030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.12,"MFE_90D_pct":2.12,"MFE_180D_pct":2.12,"MAE_30D_pct":-16.91,"MAE_90D_pct":-17.37,"MAE_180D_pct":-33.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":240500.0,"max_drawdown_low_date":"2024-10-22","max_drawdown_low":156500.0,"drawdown_after_peak_pct":-34.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"holdco_NAV_vocabulary_without_control_premium_or_shareholder_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","NAV_discount_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_return_bridge","current_profile_verdict":"current_profile_false_positive_if_NAV_discount_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"003030_2024-01-02_236000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not promote holdco/NAV discount vocabulary unless there is an explicit control-premium event, tender/block-trade path, legal milestone, buyback/cancellation or cash-return mechanism. Low MFE and deep MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L90_008930_HANMI_SCIENCE_CONTROL_PREMIUM","trigger_id":"R12L90_C32_008930_20240112_STAGE2_CONTROL_PREMIUM_EVENT","symbol":"008930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C32 requires explicit control-premium event, ownership contest, voting/legal path and minority shareholder economics rather than governance vocabulary alone","raw_component_scores_before":{"control_premium_event_score":14,"tender_or_transaction_probability":10,"ownership_contest_score":14,"voting_path_score":12,"legal_milestone_score":10,"minority_alignment_score":8,"cash_return_score":6,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-6,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"control_premium_event_score":17,"tender_or_transaction_probability":12,"ownership_contest_score":17,"voting_path_score":15,"legal_milestone_score":12,"minority_alignment_score":10,"cash_return_score":8,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Control-premium/ownership event bridge plus high MFE supports Yellow/Green-candidate watch; exact legal/voting/transaction evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L90_006840_AK_HOLDINGS_DISCOUNT_REBOUND","trigger_id":"R12L90_C32_006840_20240102_STAGE2_FALSE_POSITIVE_HOLDCO_DISCOUNT","symbol":"006840","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco discount rebound without tender/buyback/asset-sale bridge should be blocked","raw_component_scores_before":{"control_premium_event_score":0,"tender_or_transaction_probability":0,"ownership_contest_score":0,"voting_path_score":0,"legal_milestone_score":0,"minority_alignment_score":1,"cash_return_score":1,"relative_strength_score":4,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"control_premium_event_score":0,"tender_or_transaction_probability":0,"ownership_contest_score":0,"voting_path_score":0,"legal_milestone_score":0,"minority_alignment_score":0,"cash_return_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert holdco-discount vocabulary into missing tender/buyback/cash-return bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L90_003030_SEAH_HOLDCO_NAV_VOCABULARY","trigger_id":"R12L90_C32_003030_20240102_STAGE2_FALSE_POSITIVE_STEEL_HOLDCO_NAV","symbol":"003030","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"holdco/NAV vocabulary without control-premium or shareholder-return bridge should remain Watch/4B","raw_component_scores_before":{"control_premium_event_score":0,"tender_or_transaction_probability":0,"ownership_contest_score":0,"voting_path_score":0,"legal_milestone_score":0,"minority_alignment_score":1,"cash_return_score":1,"relative_strength_score":3,"valuation_repricing_score":4,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"control_premium_event_score":0,"tender_or_transaction_probability":0,"ownership_contest_score":0,"voting_path_score":0,"legal_milestone_score":0,"minority_alignment_score":0,"cash_return_score":0,"relative_strength_score":1,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require control-premium, tender, legal milestone or shareholder-return evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L90_C32_P0_CURRENT","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C32 needs explicit control-premium, tender/block-trade, legal/voting, buyback/cancellation and holdco-discount 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.99,"avg_MAE90_pct":-17.44,"avg_MFE180_pct":17.99,"avg_MAE180_pct":-34.63,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.33,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C32_control_premium_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L90_C32_P1_SECTOR_SPECIFIC","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P1_L10_governance_event_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 governance signals need control-premium event, tender/transaction probability, ownership contest, voting/legal milestone, minority alignment or cash-return mechanism before Stage2-Actionable","changed_axes":["control_premium_required","voting_legal_path_required","holdco_discount_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_control_premium_tender_ownership_vote_legal_or_cash_return_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":17.99,"avg_MAE90_pct":-17.44,"avg_MFE180_pct":17.99,"avg_MAE180_pct":-34.63,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L90_C32_P2_CANONICAL","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P2_C32_control_premium_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C32 should reward executable control-premium/shareholder-return mechanics, not holdco/NAV vocabulary","changed_axes":["C32_control_premium_legal_return_bridge_required","C32_holdco_discount_vocabulary_local_4B_guard","C32_event_reversal_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"control_premium_or_tender_or_voting_path_plus_cash_return_or_legal_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":17.99,"avg_MAE90_pct":-17.44,"avg_MFE180_pct":17.99,"avg_MAE180_pct":-34.63,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L90_C32_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P3_C32_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If governance bridge is missing, MFE90<10 or MAE180<=-30 should block Yellow/Green and route to 4B-watch","changed_axes":["C32_low_MFE_guardrail","C32_deep_MAE_4B_guardrail","C32_holdco_vocabulary_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus_30)"},"eligible_trigger_count":3,"avg_MFE90_pct":17.99,"avg_MAE90_pct":-17.44,"avg_MFE180_pct":17.99,"avg_MAE180_pct":-34.63,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_CONTROL_PREMIUM_POSITIVE_VS_HOLDCO_DISCOUNT_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":17.99,"avg_MAE90_pct":-17.44,"avg_MFE180_pct":17.99,"avg_MAE180_pct":-34.63,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus30":0.67,"interpretation":"C32 needs bridge discipline. 한미사이언스 shows explicit ownership/control-premium events can support Yellow/Green-candidate-watch, while AK홀딩스 and 세아제강지주 show holdco/NAV discount vocabulary should not be promoted without tender, buyback/cancellation, asset-sale, legal/voting milestone and cash-return evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"008930","trigger_type":"Stage2-Actionable-BioHoldcoControlPremiumOwnershipEventBridge-Positive","entry_date":"2024-01-12","stage2_to_90D_outcome":"good_stage2_high_MFE_low_entry_MAE","stage2_to_180D_outcome":"positive_control_premium_event_but_reversal_risk_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when governance strength is tied to explicit control-premium event, ownership contest, voting/legal path and minority-shareholder economics; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"006840","trigger_type":"Stage2-FalsePositive-HoldcoDiscountReboundNoTenderBuybackAssetSaleBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_holdco_discount_rebound_deep_MAE","MFE90_ge20":false,"MAE180_le_minus30":true,"transition_note":"Holdco-discount rebound without tender, buyback/cancellation, asset sale or cash-return bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003030","trigger_type":"Stage2-FalsePositive-SteelPipeHoldcoNAVVocabularyNoControlPremiumReturnBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_NAV_discount_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus30":true,"transition_note":"Holdco/NAV vocabulary without control-premium and shareholder-return bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"holdco_discount_NAV_vocabulary_overcredit_without_control_premium_legal_return_bridge","contribution":"Adds two C32 4B counterexamples against one control-premium/ownership-event positive, avoiding C32 top-covered and previous R12 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"BIO_HOLDCO_CONTROL_PREMIUM_EVENT_BRIDGE_VS_HOLDCO_DISCOUNT_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C32 now has non-top-symbol control-premium/ownership-event positive and two holdco/NAV weak-bridge counterexamples; next R12 C32 loops should exact-URL repair tender/block-trade, voting/legal path, asset-sale, buyback/cancellation, minority alignment and cash-return evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_control_premium_legal_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"008930 worked when an explicit ownership/control-premium event proxy existed; 006840 and 003030 failed when the only evidence was holdco/NAV discount vocabulary."}
{"row_type":"shadow_weight","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_holdco_discount_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Holdco-discount and NAV-discount rows showed low MFE and deep MAE without tender, buyback, asset-sale, legal/voting or cash-return bridge."}
{"row_type":"shadow_weight","round":"R12","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_event_reversal_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"008930 shows control-premium events can create large MFE but also violent reversal risk; Green requires exact transaction, legal and voting evidence."}
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
  - holdco_discount_vocabulary_overcredit
  - NAV_discount_vocabulary_overcredit
  - control_premium_bridge_missing
  - shareholder_return_cash_bridge_missing
new_axis_proposed:
  - C32_control_premium_legal_return_bridge_required_shadow_only
  - C32_holdco_discount_vocabulary_local_4B_guard_shadow_only
  - C32_event_reversal_Green_strict_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
All three symbols have older corporate-action or name-transition candidates before 2024, but the selected 2024 windows are usable for this residual price-path analysis.  
The non-price evidence layer remains source-name/proxy level for all three rows.

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
   - previous R12 loop85 C31 symbols
   - previous R12 loop86 C32 symbols
   - previous R12 loop87 C31 symbols
   - previous R12 loop88 C32 symbols
   - previous R12 loop89 C31 symbols
6. Confirm accidentally touched R11/C03, R10/C30, R9/C29 and R8/C27 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C32-scoped safe patch candidates:
   - C32_control_premium_legal_return_bridge_required
   - C32_holdco_discount_vocabulary_local_4B_guard
   - C32_event_reversal_Green_strict_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 90
next_round = R13
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```
