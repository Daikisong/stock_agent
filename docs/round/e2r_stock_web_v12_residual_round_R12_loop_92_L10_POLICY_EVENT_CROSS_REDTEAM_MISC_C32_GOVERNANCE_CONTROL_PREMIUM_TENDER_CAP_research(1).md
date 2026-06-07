# E2R Stock-Web v12 Residual Research — R12 Loop 92 / L10 / C32

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 92
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_PREMIUM_TENDER_CASH_PATH_VS_SPILLOVER_AND_HISTORICAL_CONTROL_PREMIUM_THEME_DECAY
sector: policy / event / governance / control premium / tender cap / minority cash path / holding company discount / shareholder action
output_file: e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 92`.

```text
scheduled_round = R12
scheduled_loop = 92
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

R12 is restricted to policy / event / cross-redteam / misc.
C32 is selected because R12 loop91 used C31 policy/subsidy, and the R12 lane now rotates back into governance / control-premium / tender-cap residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows = 55
symbols = 32
good/bad Stage2 = 12/14
4B/4C = 8/5
top-covered = 008930, 028260, 001040, 003240, 004990, 034730
```

This loop avoids the C32 top-covered list and recent R12 loop symbols:

```text
R12 loop85 C31: 055550, 034730, 004020
R12 loop86 C32: 028260, 001040, 004990
R12 loop87 C31: 036460, 004090, 024060
R12 loop88 C32: 000240, 001230, 004800
R12 loop89 C31: 071320, 035250, 039130
R12 loop90 C32: 008930, 006840, 003030
R12 loop91 C31: 086790, 034230, 068290
```

Candidate hygiene note:

```text
During this execution path, stale R11/C05, R10/C30, R8/C28, R7/C25 and earlier-sector candidate rows were touched while checking alternatives.
Those rows are not used in this R12/C32 output.
```

Selected symbols:

```text
010130, 000670, 180640
```

The selected pocket is:

```text
direct control-premium / tender / minority-cash-path positive-control
vs
related-party control-battle spillover price MFE without direct minority tender/cash path
vs
historical control-premium holding-company vocabulary without fresh tender, cap, or minority protection event
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"010130","company_name":"고려아연","profile_path":"atlas/symbol_profiles/010/010130.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7757,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"000670","company_name":"영풍","profile_path":"atlas/symbol_profiles/000/000670.json","first_date":"1995-05-04","last_date":"2026-02-20","trading_day_count":6704,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2025-04-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Future 2025 corporate-action candidate is outside selected 2024 window; selected 2024 control-battle spillover window is usable as price-path stress but not patch-ready evidence.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; future_candidate_watch"}
{"row_type":"price_source_validation","symbol":"180640","company_name":"한진칼","profile_path":"atlas/symbol_profiles/180/180640.json","first_date":"2013-09-16","last_date":"2026-02-20","trading_day_count":3048,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2014-11-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"010130","trigger_type":"Stage2-Actionable-ControlPremiumTenderMinorityCashPath-Positive","entry_date":"2024-09-13","duplicate_status":"new C32 symbol/trigger/date combination outside C32 top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000670","trigger_type":"Stage2-FalsePositive-RelatedPartyControlBattleSpilloverNoDirectMinorityTenderCashPath","entry_date":"2024-09-13","duplicate_status":"new C32 symbol/trigger/date combination outside C32 top-covered and previous R12 loop symbols; future-candidate watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"180640","trigger_type":"Stage2-FalsePositive-HistoricalControlPremiumHoldingVocabularyNoFreshTenderCapMinorityProtection","entry_date":"2024-01-29","duplicate_status":"new C32 symbol/trigger/date combination outside C32 top-covered and previous R12 loop symbols"}
```

## 4. Research question

C32 is not “지배구조 이슈가 있다.”
The useful governance / control-premium signal must prove the minority-holder cash path:

```text
credible acquirer or competing bloc
tender / buyout / share purchase mechanism
offer price or premium cap
minority eligibility
board / court / regulator / shareholder-vote path
financing and settlement visibility
timeline
downside floor if the event fails
post-event liquidity and float risk
```

A control-premium headline without this bridge is a locked gate with a gold sign. The sign says value exists, but E2R needs the key: tender terms, eligibility, settlement, floor, and minority protection.

Residual question:

```text
Can C32 distinguish:
1. direct control-premium / tender contest where minority shares have an observable cash-path and high MFE,
2. related-party spillover where price MFE exists but the stock itself lacks direct tender/cash eligibility,
3. old control-premium / holding-company vocabulary where no fresh tender, cap or minority-protection event exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C32_R12L92_010130_KOREA_ZINC_CONTROL_PREMIUM","symbol":"010130","company_name":"고려아연","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_MINORITY_CASH_PATH","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ControlPremiumTenderMinorityCashPath-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_and_MFE180_low_entry_MAE_direct_tender_cash_path","current_profile_verdict":"current_profile_correct_if_tender_terms_minority_eligibility_financing_settlement_floor_required","price_source":"Songdaiki/stock-web","notes":"Direct control-premium / tender contest produced extreme MFE with shallow entry MAE. Green still requires exact tender terms, minority eligibility, financing, settlement timeline and failed-event floor evidence."}
{"row_type":"case","case_id":"C32_R12L92_000670_YOUNGPOONG_RELATED_PARTY_SPILLOVER","symbol":"000670","company_name":"영풍","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"RELATED_PARTY_CONTROL_BATTLE_SPILLOVER_WITHOUT_DIRECT_MINORITY_TENDER_CASH_PATH","case_type":"failed_entry_price_mfe","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RelatedPartyControlBattleSpilloverNoDirectMinorityTenderCashPath","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_price_MFE_but_spillover_no_direct_minority_cash_path_high_after_peak_drawdown","current_profile_verdict":"current_profile_false_positive_if_spillover_MFE_counted_as_direct_C32_tender_evidence","price_source":"Songdaiki/stock-web","notes":"Related-party control-battle spillover produced price MFE, but without a direct minority tender/settlement path for the stock itself it should remain 4B/watch or cross-label stress, not direct C32 positive."}
{"row_type":"case","case_id":"C32_R12L92_180640_HANJINKAL_HISTORICAL_CONTROL_PREMIUM","symbol":"180640","company_name":"한진칼","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HISTORICAL_CONTROL_PREMIUM_HOLDING_VOCABULARY_WITHOUT_FRESH_TENDER_CAP_MINORITY_PROTECTION","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HistoricalControlPremiumHoldingVocabularyNoFreshTenderCapMinorityProtection","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub20_MFE_deep_MAE_no_fresh_tender_cap","current_profile_verdict":"current_profile_false_positive_if_historical_control_premium_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Historical control-premium / holding-company vocabulary had sub-20 MFE and deep MAE without a fresh tender cap, shareholder-vote path, minority protection or settlement bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 010130 고려아연 — direct control-premium / tender / minority cash-path positive-control

Entry row: `2024-09-13 c=666000`.
Observed path: entry low `2024-09-13 l=655000`, local contest high `2024-10-29 h=1543000`, full-window high `2024-12-06 h=2407000`, and after-peak drawdown to `2024-12-13 l=1222000`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L92_C32_010130_20240913_STAGE2_CONTROL_PREMIUM_TENDER_CASH_PATH","case_id":"C32_R12L92_010130_KOREA_ZINC_CONTROL_PREMIUM","symbol":"010130","company_name":"고려아연","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_MINORITY_CASH_PATH","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ControlPremiumTenderMinorityCashPath-Positive","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_control_premium_tender_contest_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; competing control bloc, tender/buyout mechanism, minority eligibility, financing and settlement bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["control_premium_proxy","tender_or_buyout_mechanism_proxy","minority_cash_path_proxy","relative_strength_event_turn"],"stage3_evidence_fields":["exact_tender_terms_source_pending","minority_eligibility_source_pending","financing_settlement_source_pending","failed_event_floor_pending"],"stage4b_evidence_fields":["price_extension_watch","after_peak_drawdown_watch"],"stage4c_evidence_fields":["event_failure_floor_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.27,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-1.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000.0,"max_drawdown_low_date":"2024-09-13","max_drawdown_low":655000.0,"drawdown_after_peak_pct":-49.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.09,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_tender_terms_minority_eligibility_financing_settlement_and_failed_event_floor_evidence","four_b_evidence_type":["price_extension_watch","after_peak_drawdown_watch"],"four_c_protection_label":"event_failure_floor_watch_only","trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_low_entry_MAE_direct_tender_cash_path","current_profile_verdict":"current_profile_correct_if_tender_terms_minority_eligibility_financing_settlement_floor_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"010130_2024-09-13_666000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 can allow Stage2/Yellow or Green-candidate-watch when governance strength is tied to an observable tender/buyout mechanism, minority cash eligibility, financing, settlement timeline and failed-event floor. Green requires exact source-grade evidence."}
```

### 6.2 000670 영풍 — related-party control-battle spillover without direct minority tender/cash path

Entry row: `2024-09-13 c=386000`.
Observed path: spike high `2024-09-20 h=649000`, then fast drawdown to `2024-10-08 l=335500`. The price moved, but the row is a spillover pathway, not direct tender eligibility for the same security.

```jsonl
{"row_type":"trigger","trigger_id":"R12L92_C32_000670_20240913_STAGE2_FALSE_POSITIVE_SPILLOVER_CONTROL_BATTLE","case_id":"C32_R12L92_000670_YOUNGPOONG_RELATED_PARTY_SPILLOVER","symbol":"000670","company_name":"영풍","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"RELATED_PARTY_CONTROL_BATTLE_SPILLOVER_WITHOUT_DIRECT_MINORITY_TENDER_CASH_PATH","loop_objective":"residual_false_positive_mining;counterexample_mining;price_MFE_not_direct_tender_validation","trigger_type":"Stage2-FalsePositive-RelatedPartyControlBattleSpilloverNoDirectMinorityTenderCashPath","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":386000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_related_party_control_battle_spillover_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; related-party control battle and affiliate ownership exposure treated as insufficient without direct tender/buyout terms, minority eligibility, financing, settlement and floor for the stock itself","evidence_source_type":"historical_public_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["control_battle_spillover_keyword","affiliate_ownership_exposure","price_MFE"],"stage3_evidence_fields":["direct_tender_terms_missing","minority_cash_eligibility_missing","settlement_floor_missing","own_shareholder_protection_missing"],"stage4b_evidence_fields":["price_MFE_without_direct_tender","after_peak_drawdown","future_candidate_watch"],"stage4c_evidence_fields":["event_failure_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000670/2024.csv","profile_path":"atlas/symbol_profiles/000/000670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":68.13,"MFE_90D_pct":68.13,"MFE_180D_pct":68.13,"MAE_30D_pct":-13.08,"MAE_90D_pct":-13.08,"MAE_180D_pct":-13.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-20","peak_price":649000.0,"max_drawdown_low_date":"2024-10-08","max_drawdown_low":335500.0,"drawdown_after_peak_pct":-48.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"related_party_spillover_price_MFE_without_direct_tender_cash_path_should_be_4B_watch_not_positive_C32","four_b_evidence_type":["price_MFE_without_direct_tender","after_peak_drawdown","future_candidate_watch"],"four_c_protection_label":"event_failure_watch_only","trigger_outcome_label":"counterexample_price_MFE_but_spillover_no_direct_minority_cash_path_high_after_peak_drawdown","current_profile_verdict":"current_profile_false_positive_if_spillover_MFE_counted_as_direct_C32_tender_evidence","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["future_2025-04-25_corporate_action_candidate_watch","spillover_not_direct_tender_path"],"corporate_action_window_status":"selected_2024_window_usable; future_candidate_watch","same_entry_group_id":"000670_2024-09-13_386000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not count related-party spillover price MFE as direct control-premium evidence unless the specific security has its own tender/buyout terms, minority eligibility, settlement timeline and floor."}
```

### 6.3 180640 한진칼 — historical control-premium holding vocabulary without fresh tender cap / minority protection

Entry row: `2024-01-29 c=74100`.
Observed path: local high `2024-02-13 h=87400`, then drawdown to `2024-03-07 l=55300`; later Q4 high `2024-10-17 h=94900` did not come with a fresh tender / cap / minority cash path at the original entry.

```jsonl
{"row_type":"trigger","trigger_id":"R12L92_C32_180640_20240129_STAGE2_FALSE_POSITIVE_HISTORICAL_CONTROL_PREMIUM","case_id":"C32_R12L92_180640_HANJINKAL_HISTORICAL_CONTROL_PREMIUM","symbol":"180640","company_name":"한진칼","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HISTORICAL_CONTROL_PREMIUM_HOLDING_VOCABULARY_WITHOUT_FRESH_TENDER_CAP_MINORITY_PROTECTION","loop_objective":"residual_false_positive_mining;counterexample_mining;historical_control_premium_vocabulary_stress_test","trigger_type":"Stage2-FalsePositive-HistoricalControlPremiumHoldingVocabularyNoFreshTenderCapMinorityProtection","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":74100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_holding_company_control_premium_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; historical control-premium / holding-company governance vocabulary treated as insufficient without fresh tender cap, shareholder vote, minority protection, financing and settlement bridge","evidence_source_type":"historical_public_governance_theme_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["historical_control_premium_vocabulary","holding_company_discount_keyword","relative_strength_rebound"],"stage3_evidence_fields":["fresh_tender_cap_missing","minority_protection_missing","shareholder_vote_or_regulatory_path_missing","settlement_cash_bridge_missing"],"stage4b_evidence_fields":["sub20_MFE","deep_MAE","late_high_not_entry_validation"],"stage4c_evidence_fields":["event_failure_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/180/180640/2024.csv","profile_path":"atlas/symbol_profiles/180/180640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.95,"MFE_90D_pct":17.95,"MFE_180D_pct":28.07,"MAE_30D_pct":-25.37,"MAE_90D_pct":-25.37,"MAE_180D_pct":-25.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":94900.0,"max_drawdown_low_date":"2024-03-07","max_drawdown_low":55300.0,"drawdown_after_peak_pct":-36.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.64,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"historical_control_premium_holding_vocabulary_without_fresh_tender_cap_minority_protection_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","deep_MAE","late_high_not_entry_validation"],"four_c_protection_label":"event_failure_watch_only","trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_no_fresh_tender_cap","current_profile_verdict":"current_profile_false_positive_if_historical_control_premium_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"180640_2024-01-29_74100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C32 should not promote historical control-premium or holding-discount vocabulary unless fresh tender/buyout terms, minority protection, shareholder-vote or regulatory path, financing and settlement evidence are repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L92_010130_KOREA_ZINC_CONTROL_PREMIUM","trigger_id":"R12L92_C32_010130_20240913_STAGE2_CONTROL_PREMIUM_TENDER_CASH_PATH","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C32 requires credible acquirer/competing bloc, tender/buyout mechanism, offer premium, minority eligibility, financing, settlement and failed-event floor rather than governance vocabulary alone","raw_component_scores_before":{"acquirer_bloc_score":14,"tender_mechanism_score":15,"offer_premium_score":14,"minority_eligibility_score":13,"financing_settlement_score":11,"regulatory_vote_path_score":9,"failed_event_floor_score":8,"float_liquidity_score":7,"relative_strength_score":16,"valuation_repricing_score":10,"execution_risk_score":-7,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"acquirer_bloc_score":17,"tender_mechanism_score":18,"offer_premium_score":17,"minority_eligibility_score":16,"financing_settlement_score":14,"regulatory_vote_path_score":11,"failed_event_floor_score":10,"float_liquidity_score":8,"relative_strength_score":17,"valuation_repricing_score":11,"execution_risk_score":-6,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":95,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"Direct tender/control-premium cash-path bridge plus extreme MFE supports Green-candidate watch; exact tender/settlement/floor evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L92_000670_YOUNGPOONG_RELATED_PARTY_SPILLOVER","trigger_id":"R12L92_C32_000670_20240913_STAGE2_FALSE_POSITIVE_SPILLOVER_CONTROL_BATTLE","symbol":"000670","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"related-party control-battle spillover MFE without direct tender/cash path should be blocked from positive C32 scoring","raw_component_scores_before":{"acquirer_bloc_score":5,"tender_mechanism_score":0,"offer_premium_score":0,"minority_eligibility_score":0,"financing_settlement_score":0,"regulatory_vote_path_score":1,"failed_event_floor_score":0,"float_liquidity_score":1,"relative_strength_score":15,"valuation_repricing_score":6,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/Spillover","raw_component_scores_after":{"acquirer_bloc_score":2,"tender_mechanism_score":0,"offer_premium_score":0,"minority_eligibility_score":0,"financing_settlement_score":0,"regulatory_vote_path_score":0,"failed_event_floor_score":0,"float_liquidity_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-26,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/Spillover","component_delta_explanation":"Price MFE alone is not C32 validation when the specific security lacks direct tender eligibility and settlement path."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_R12L92_180640_HANJINKAL_HISTORICAL_CONTROL_PREMIUM","trigger_id":"R12L92_C32_180640_20240129_STAGE2_FALSE_POSITIVE_HISTORICAL_CONTROL_PREMIUM","symbol":"180640","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_scope":"current_default_proxy","profile_hypothesis":"historical control-premium / holding-company vocabulary without fresh tender cap and minority protection should remain Watch/4B","raw_component_scores_before":{"acquirer_bloc_score":1,"tender_mechanism_score":0,"offer_premium_score":0,"minority_eligibility_score":0,"financing_settlement_score":0,"regulatory_vote_path_score":0,"failed_event_floor_score":0,"float_liquidity_score":1,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"acquirer_bloc_score":0,"tender_mechanism_score":0,"offer_premium_score":0,"minority_eligibility_score":0,"financing_settlement_score":0,"regulatory_vote_path_score":0,"failed_event_floor_score":0,"float_liquidity_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-20 MFE, deep MAE and missing fresh tender/minority protection bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L92_C32_P0_CURRENT","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C32 needs explicit direct tender/cash-path, minority eligibility, financing, settlement and failed-event floor taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":115.83,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":119.2,"avg_MAE180_pct":-13.37,"false_positive_rate":0.67,"spillover_price_MFE_count":1,"historical_control_vocabulary_count":1,"score_return_alignment_verdict":"mixed_without_C32_direct_tender_cash_path_and_spillover_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L92_C32_P1_SECTOR_SPECIFIC","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P1_L10_governance_control_cash_path_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 governance signals need direct tender/buyout terms, minority eligibility, offer premium, financing, settlement or failed-event floor before Stage2-Actionable","changed_axes":["direct_tender_required","minority_cash_path_required","spillover_price_MFE_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_direct_tender_offer_premium_minority_eligibility_financing_settlement_or_floor_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L92_C32_P2_CANONICAL","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P2_C32_direct_tender_cash_path_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C32 should reward minority-cash-path mechanics, not governance vocabulary or spillover price MFE","changed_axes":["C32_direct_tender_minority_cash_path_required","C32_related_party_spillover_price_MFE_local_4B_guard","C32_historical_control_premium_vocabulary_4B_guard","C32_event_failure_floor_required"],"changed_thresholds":{"stage2_yellow_gate":"direct_tender_or_buyout_plus_minority_eligibility_or_settlement_floor_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L92_C32_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile_id":"P3_C32_spillover_or_no_fresh_event_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If direct tender/cash path is missing, spillover MFE or historical control-premium vocabulary blocks Yellow/Green; MAE30<=-20 also routes to 4B-watch","changed_axes":["C32_spillover_MFE_guardrail","C32_no_fresh_tender_guardrail","C32_deep_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"direct_cash_path_missing_and_(spillover_MFE_or_no_fresh_tender_or_MAE30_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_DIRECT_TENDER_POSITIVE_VS_SPILLOVER_HISTORICAL_CONTROL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":115.83,"avg_MAE90_pct":-13.37,"avg_MFE180_pct":119.2,"avg_MAE180_pct":-13.37,"direct_tender_positive_count":1,"spillover_price_MFE_counterexample_count":1,"historical_control_vocabulary_counterexample_count":1,"interpretation":"C32 needs cash-path discipline. 고려아연 shows direct tender/control-premium mechanics can support Green-candidate-watch, while 영풍 and 한진칼 show spillover MFE or historical control-premium vocabulary should not be promoted without direct tender terms, minority eligibility, settlement timeline and failed-event floor."}
{"row_type":"stage_transition_summary","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"010130","trigger_type":"Stage2-Actionable-ControlPremiumTenderMinorityCashPath-Positive","entry_date":"2024-09-13","stage2_to_90D_outcome":"good_stage2_extreme_MFE_low_MAE","stage2_to_180D_outcome":"direct_tender_cash_path_positive_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow/Green-candidate when the stock itself has direct tender/buyout mechanism, minority eligibility, settlement and failed-event floor; exact evidence is required for Green."}
{"row_type":"stage_transition_summary","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000670","trigger_type":"Stage2-FalsePositive-RelatedPartyControlBattleSpilloverNoDirectMinorityTenderCashPath","entry_date":"2024-09-13","stage2_to_90D_outcome":"price_MFE_but_spillover_not_direct_tender_path","stage2_to_180D_outcome":"spillover_high_MFE_after_peak_drawdown_4B_watch","MFE90_ge20":true,"direct_cash_path_missing":true,"transition_note":"Related-party spillover price MFE should remain Watch/4B unless direct minority tender/cash settlement evidence exists for the stock itself."}
{"row_type":"stage_transition_summary","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"180640","trigger_type":"Stage2-FalsePositive-HistoricalControlPremiumHoldingVocabularyNoFreshTenderCapMinorityProtection","entry_date":"2024-01-29","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_deep_MAE","stage2_to_180D_outcome":"historical_control_premium_vocabulary_no_fresh_event","MFE90_ge20":false,"MAE30_le_minus20":true,"transition_note":"Historical control-premium vocabulary without fresh tender cap, minority protection and settlement path should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"spillover_price_MFE_and_historical_control_premium_vocabulary_overcredit_without_direct_minority_cash_path","contribution":"Adds two C32 4B counterexamples against one direct control-premium/tender positive, avoiding C32 top-covered and previous R12 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_CASH_PATH_VS_SPILLOVER_AND_HISTORICAL_CONTROL_PREMIUM_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C32 now has non-top-symbol direct tender/control-premium positive, related-party spillover MFE counterexample, and historical control-premium vocabulary counterexample; next R12 C32 loops should exact-URL repair tender terms, minority eligibility, settlement/financing, shareholder-vote/regulatory path and failed-event floor evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_direct_tender_minority_cash_path_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"010130 worked when direct control-premium/tender cash-path proxy existed; 000670 and 180640 fail as direct positives without their own minority cash eligibility and settlement bridge."}
{"row_type":"shadow_weight","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_related_party_spillover_price_MFE_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"000670 shows price MFE from a related-party control battle should not validate C32 unless the same security has direct tender/buyout terms."}
{"row_type":"shadow_weight","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_historical_control_premium_vocabulary_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"180640 shows historical control-premium/holding-company vocabulary without fresh tender/cap/minority protection can create sub-20 MFE and deep MAE."}
{"row_type":"shadow_weight","round":"R12","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"C32_event_failure_floor_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"Even direct tender positives need failed-event floor and settlement evidence before Green because after-peak drawdowns can be large."}
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
  - related_party_spillover_price_MFE_overcredit
  - historical_control_premium_vocabulary_overcredit
  - direct_tender_cash_path_missing
  - minority_eligibility_settlement_bridge_missing
  - failed_event_floor_required
new_axis_proposed:
  - C32_direct_tender_minority_cash_path_required_shadow_only
  - C32_related_party_spillover_price_MFE_local_4B_guard_shadow_only
  - C32_historical_control_premium_vocabulary_4B_guard_shadow_only
  - C32_event_failure_floor_required_shadow_only
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
`010130` has no corporate-action candidate in its profile and the selected 2024 window is clean.
`000670` has a future 2025-04-25 corporate-action candidate outside the selected 2024 window, so it remains future-candidate watch before patching.
`180640` has an older 2014 corporate-action candidate before the selected 2024 window; the selected 2024 window is usable.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
future_candidate_watch = true for 000670
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
3. Confirm R12 / L10 / C32 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C32 top-covered symbols
   - previous R12 loop85 C31 symbols
   - previous R12 loop86 C32 symbols
   - previous R12 loop87 C31 symbols
   - previous R12 loop88 C32 symbols
   - previous R12 loop89 C31 symbols
   - previous R12 loop90 C32 symbols
   - previous R12 loop91 C31 symbols
6. Confirm stale R11/C05, R10/C30, R8/C28, R7/C25 and earlier-sector candidate rows are not ingested from this MD.
7. Keep 000670 in future-candidate / spillover-only watch before patch consideration.
8. Treat 180640 as historical-control-premium vocabulary failure-mode stress unless fresh tender/cap evidence is added later.
9. If aggregate support remains stable after exact evidence URL repair, consider C32-scoped safe patch candidates:
   - C32_direct_tender_minority_cash_path_required
   - C32_related_party_spillover_price_MFE_local_4B_guard
   - C32_historical_control_premium_vocabulary_4B_guard
   - C32_event_failure_floor_required
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 92
next_round = R13
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 direct control-premium/tender positive, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```
