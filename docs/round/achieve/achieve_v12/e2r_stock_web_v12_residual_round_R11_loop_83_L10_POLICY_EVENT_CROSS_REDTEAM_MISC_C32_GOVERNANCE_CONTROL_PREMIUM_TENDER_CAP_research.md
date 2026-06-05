# E2R Stock-Web v12 Residual Research — R11 Loop 83 / L10 / C32

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 83
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDCO_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_EVENT_PREMIUM_CAP
sector: policy_event_cross_redteam_misc / governance_control_premium_tender_cap
output_file: e2r_stock_web_v12_residual_round_R11_loop_83_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the sequential v12 scheduler after `R10 loop 83`.

```text
scheduled_round = R11
scheduled_loop = 83
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

R11 may use L10 policy/event/governance or L1 policy-defense linkage.  
This execution selects the L10 governance lane because C32 has a specific residual: **holding-company NAV discount and shareholder-return events often create a fast control-premium / event-premium rally, but only some cases convert into durable rerating.**

This is not a current stock recommendation, not a `stock_agent` patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"402340","company_name":"SK스퀘어","profile_path":"atlas/symbol_profiles/402/402340.json","first_date":"2021-11-29","last_date":"2026-02-20","trading_day_count":1034,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"034730","company_name":"SK","profile_path":"atlas/symbol_profiles/034/034730.json","first_date":"2009-11-11","last_date":"2026-02-20","trading_day_count":4007,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-08-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate is outside the 2024 trigger windows used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"003550","company_name":"LG","profile_path":"atlas/symbol_profiles/003/003550.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7689,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1999-04-23","2001-04-25","2001-09-20","2002-01-02","2003-03-11","2004-08-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates are outside the 2024 trigger windows used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

C32 already contains several repeated governance/control-premium symbols, so this run avoids the most repeated C32 cluster (`010130`, `036560`, `000150`, `041510`, `241560`, `000990`) and adds holding-company / NAV-discount / value-up event-premium residual cases.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novel keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"402340","trigger_type":"Stage2-Actionable-HoldCoNAVShareholderReturnBridge-Positive","entry_date":"2024-02-02","duplicate_status":"new C32 symbol/trigger family in this run; not a hard duplicate"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"034730","trigger_type":"Stage2-FalsePositive-HoldCoEventPremiumCap-Roundtrip","entry_date":"2024-05-31","duplicate_status":"new C32 trigger family and event-premium roundtrip residual"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003550","trigger_type":"Stage2-FalsePositive-ValueUpHoldCoDiscount-NoDurableBridge","entry_date":"2024-02-01","duplicate_status":"same symbol has policy/value-up relevance elsewhere but this exact C32 symbol+trigger+entry key is not reused"}
```

## 4. Research question

C32 is not simply “governance good, rerating automatic.”  
It is the place where event premium, shareholder-return credibility, NAV discount, tender/control premium, and overhang all fight.

Residual question:

```text
Can C32 separate:
1. durable holding-company NAV discount rerating with shareholder-return bridge,
2. event-premium rally that fades when the bridge is unclear,
3. value-up holding-company rally that does not convert into durable Stage3 rerating?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C32_R11L83_402340_SKSQUARE_NAV_DISCOUNT_RETURN_BRIDGE","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE","symbol":"402340","company_name":"SK스퀘어","case_role":"structural_success","case_summary":"Clean 2024 path where holding-company discount, shareholder-return proxy, and NAV/rerating bridge aligned with high MFE and controlled MAE."}
{"row_type":"case","case_id":"C32_R11L83_034730_SK_HOLDCO_EVENT_PREMIUM_ROUNDTRIP","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_EVENT_PREMIUM_CAP_WITH_ROUNDTRIP","symbol":"034730","company_name":"SK","case_role":"failed_rerating","case_summary":"Event premium / holding-company rerating spike produced modest upside and then a long roundtrip; C32 needs bridge verification rather than pure event premium credit."}
{"row_type":"case","case_id":"C32_R11L83_003550_LG_VALUEUP_HOLDCO_DISCOUNT_NO_DURABLE_BRIDGE","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"VALUEUP_HOLDCO_DISCOUNT_NO_DURABLE_BRIDGE","symbol":"003550","company_name":"LG","case_role":"failed_rerating","case_summary":"Value-up/holding-company discount rally had limited forward MFE and repeated below-entry closes; event premium alone should remain Watch unless payout/NAV/asset-action bridge confirms."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 402340 SK스퀘어 — positive holdco NAV/shareholder-return bridge

Stock-Web profile is clean with no corporate-action candidate dates.  
Entry uses `2024-02-02 c=59500`. The observed path reached `2024-06-10 h=103800` inside the 90D window and `2024-07-11 h=109000` inside the 180D window.

```jsonl
{"row_type":"trigger","trigger_id":"R11L83_C32_402340_20240202_STAGE2_HOLDCO_NAV_RETURN_BRIDGE_POSITIVE","case_id":"C32_R11L83_402340_SKSQUARE_NAV_DISCOUNT_RETURN_BRIDGE","symbol":"402340","company_name":"SK스퀘어","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-HoldCoNAVShareholderReturnBridge-Positive","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":59500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public report / shareholder-return / NAV-discount proxy available at trigger date; exact URLs pending","evidence_source":"source-name-level proxy; exact URL pending; holding-company NAV discount + shareholder-return bridge treated as non-price proxy only","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","shareholder_return_proxy","nav_discount_bridge"],"stage3_evidence_fields":["confirmed_revision_proxy","financial_visibility_proxy","repeat_public_source_proxy","low_red_team_risk_proxy"],"stage4b_evidence_fields":["valuation_blowoff_watch","positioning_overheat_watch","price_only_local_peak"],"stage4c_evidence_fields":[],"non_price_evidence_bridge":true,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv","profile_path":"atlas/symbol_profiles/402/402340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.55,"MAE_30D_pct":-9.24,"MFE_90D_pct":74.45,"MAE_90D_pct":-9.24,"MFE_180D_pct":83.19,"MAE_180D_pct":-9.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":109000.0,"drawdown_after_peak_pct":-20.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.63,"four_b_timing_verdict":"price_only_local_4B_too_early_if_no_non_price_overheat_evidence","four_b_evidence_type":["price_only","valuation_blowoff_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_controlled_MAE","current_profile_verdict":"current_profile_correct","current_profile_residual":"C32 should allow Stage2/Yellow when governance/NAV/shareholder-return bridge exists, but should not loosen Green because exact evidence URLs are pending.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"C32_402340_20240202_59500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 6.2 034730 SK — holding-company event premium roundtrip

Stock-Web profile has one old corporate-action candidate in 2015, outside the 2024 forward window.  
Entry uses `2024-05-31 c=176200`. The local event peak reached `2024-06-11 h=195700`, but the full 180D observed low fell to `2024-12-09 l=127600`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L83_C32_034730_20240531_STAGE2_EVENT_PREMIUM_ROUNDTRIP","case_id":"C32_R11L83_034730_SK_HOLDCO_EVENT_PREMIUM_ROUNDTRIP","symbol":"034730","company_name":"SK","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_EVENT_PREMIUM_CAP_WITH_ROUNDTRIP","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-HoldCoEventPremiumCap-Roundtrip","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":176200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical public event/governance premium proxy; exact URLs pending","evidence_source":"source-name-level proxy; exact URL pending; holding-company event premium not treated as durable bridge without capital action / NAV realization / payout conversion","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","relative_strength","governance_event_premium_proxy"],"stage3_evidence_fields":["missing_confirmed_revision","missing_durable_capital_action","missing_nav_realization_bridge"],"stage4b_evidence_fields":["event_premium_cap","valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken_watch"],"non_price_evidence_bridge":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv","profile_path":"atlas/symbol_profiles/034/034730.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.07,"MAE_30D_pct":-14.42,"MFE_90D_pct":11.07,"MAE_90D_pct":-17.08,"MFE_180D_pct":11.07,"MAE_180D_pct":-27.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":195700.0,"drawdown_after_peak_pct":-34.80,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"event_premium_local_peak_should_remain_watch_without_non_price_bridge","four_b_evidence_type":["price_only","control_premium_or_event_premium","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_event_premium_roundtrip","current_profile_verdict":"current_profile_false_positive","current_profile_residual":"C32 event-premium rallies can produce a fast local peak with poor 180D MAE. The profile should require capital-action/NAV-realization bridge before Stage3-positive credit.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"C32_034730_20240531_176200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 6.3 003550 LG — value-up holding-company discount with no durable bridge

Stock-Web profile has historical corporate-action candidates only before the selected 2024 window.  
Entry uses `2024-02-01 c=88100`. The rally reached `2024-02-19 h=103600`, but the forward window repeatedly closed below entry and fell to the low-70k range later in the observed cycle.

```jsonl
{"row_type":"trigger","trigger_id":"R11L83_C32_003550_20240201_STAGE2_VALUEUP_HOLDCO_NO_DURABLE_BRIDGE","case_id":"C32_R11L83_003550_LG_VALUEUP_HOLDCO_DISCOUNT_NO_DURABLE_BRIDGE","symbol":"003550","company_name":"LG","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"VALUEUP_HOLDCO_DISCOUNT_NO_DURABLE_BRIDGE","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"residual_false_positive_mining;yellow_threshold_stress_test;counterexample_mining","trigger_type":"Stage2-FalsePositive-ValueUpHoldCoDiscount-NoDurableBridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":88100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical value-up / holding-company discount proxy; exact URLs pending","evidence_source":"source-name-level proxy; exact URL pending; holding-company value-up rally treated as insufficient without payout/NAV/asset-action bridge","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","holding_company_discount_proxy"],"stage3_evidence_fields":["missing_confirmed_revision","missing_durable_shareholder_return_conversion","missing_asset_action_bridge"],"stage4b_evidence_fields":["event_premium_cap","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"non_price_evidence_bridge":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003550/2024.csv","profile_path":"atlas/symbol_profiles/003/003550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.59,"MAE_30D_pct":-7.83,"MFE_90D_pct":17.59,"MAE_90D_pct":-15.10,"MFE_180D_pct":17.59,"MAE_180D_pct":-17.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":103600.0,"drawdown_after_peak_pct":-31.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.00,"four_b_full_window_peak_proximity":1.00,"four_b_timing_verdict":"good_local_peak_but_price_only_should_not_be_full_4B_without_event_cap_evidence","four_b_evidence_type":["price_only","control_premium_or_event_premium"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_limited_MFE_roundtrip","current_profile_verdict":"current_profile_false_positive","current_profile_residual":"Value-up/holding-company discount momentum alone was not enough. C32 needs a stricter bridge: actual payout, cancellation, NAV realization, tender ratio, or asset action before durable Stage3 credit.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"C32_003550_20240201_88100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 7. Score simulation rows

Proxy scoring only. No production scoring changes are made.

```jsonl
{"row_type":"score_simulation","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"402340","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":13,"market_mispricing":16,"valuation_rerating":16,"capital_allocation":5,"information_confidence":5,"raw_total_proxy":91,"weighted_total_proxy":83,"simulated_stage":"Stage2-Actionable/Stage3-Yellow-Watch","simulation_note":"Positive C32 case when NAV discount, shareholder-return proxy, and relative strength align; no Green loosening without URL-grade evidence."}
{"row_type":"score_simulation","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"034730","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":12,"earnings_visibility":11,"bottleneck_pricing":8,"market_mispricing":15,"valuation_rerating":12,"capital_allocation":3,"information_confidence":4,"raw_total_proxy":65,"weighted_total_proxy":68,"simulated_stage":"Stage2-Watch/EventPremiumCap","simulation_note":"Local event spike but poor 180D MAE; do not promote to Yellow/Green without capital-action bridge."}
{"row_type":"score_simulation","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003550","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":13,"earnings_visibility":12,"bottleneck_pricing":7,"market_mispricing":16,"valuation_rerating":13,"capital_allocation":3,"information_confidence":4,"raw_total_proxy":68,"weighted_total_proxy":69,"simulated_stage":"Stage2-Watch/EventPremiumCap","simulation_note":"Value-up / holdco discount event premium is not enough without payout/NAV realization bridge."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L83_C32_P0_BASELINE","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile":"P0_e2r_2_0_baseline","profile_role":"rollback_reference","expected_error":"Would over-credit event-premium and holding-company discount momentum as rerating evidence."}
{"row_type":"profile_comparison","comparison_id":"R11L83_C32_P0B_CURRENT","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile":"P0b_e2r_2_2_rolling_calibrated","profile_role":"current_default_proxy","expected_error":"Global price-only guard helps, but C32 still needs local bridge to distinguish NAV/shareholder-return conversion from one-shot event premium."}
{"row_type":"profile_comparison","comparison_id":"R11L83_C32_P1_BRIDGE_REQUIRED","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile":"P1_shadow_C32_governance_bridge_required","profile_role":"shadow_candidate","expected_effect":"Stage2/Yellow requires at least one non-price bridge: payout/cancellation, tender/control ratio, NAV realization, asset action, or capital-allocation confirmation."}
{"row_type":"profile_comparison","comparison_id":"R11L83_C32_P2_EVENT_PREMIUM_CAP","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","profile":"P2_shadow_C32_event_premium_cap_guard","profile_role":"shadow_candidate","expected_effect":"If event-premium local peak has MFE90<20 and later MAE180<-15, keep as Watch/4B-local rather than durable Stage3."}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDCO_NAV_EVENT_PREMIUM_STRESS","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":34.37,"avg_MAE90_pct":-13.81,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_15":0.67,"interpretation":"C32 needs a local bridge gate: NAV/shareholder-return conversion worked in SK스퀘어, while event-premium/holdco-discount rallies in SK and LG had limited forward MFE and roundtrip risk."}
{"row_type":"stage_transition_summary","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"402340","trigger_type":"Stage2-Actionable-HoldCoNAVShareholderReturnBridge-Positive","entry_date":"2024-02-02","stage2_to_90D_outcome":"good_stage2","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"C32 can promote to Stage2/Yellow watch when NAV discount and shareholder-return bridge exists."}
{"row_type":"stage_transition_summary","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"034730","trigger_type":"Stage2-FalsePositive-HoldCoEventPremiumCap-Roundtrip","entry_date":"2024-05-31","stage2_to_90D_outcome":"bad_stage2_limited_MFE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":false,"MAE180_le_minus_20":true,"transition_note":"Event premium peak faded into a large 180D drawdown; require capital-action bridge before positive stage."}
{"row_type":"stage_transition_summary","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003550","trigger_type":"Stage2-FalsePositive-ValueUpHoldCoDiscount-NoDurableBridge","entry_date":"2024-02-01","stage2_to_90D_outcome":"bad_stage2_limited_MFE","stage2_to_180D_outcome":"event_premium_roundtrip","MFE90_ge_20":false,"MAE90_le_minus_15":true,"transition_note":"Holding-company value-up rally did not convert into durable rerating."}
{"row_type":"residual_contribution","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"C32_event_premium_cap_vs_governance_bridge","contribution":"Adds one positive NAV/shareholder-return bridge case and two event-premium counterexamples; strengthens C32 local bridge requirement and local 4B-watch logic.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_rows":3,"new_symbols":3,"new_positive":1,"new_counterexample":2,"new_4B_watch":2,"new_4C":0,"source_proxy_only":3,"evidence_url_pending":3,"calibration_usable":3,"next_gap":"Exact URL repair for shareholder-return/tender/NAV evidence; test non-holdco tender/control-premium rows separately from value-up holding-company rows."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"governance_bridge_required","scope":"canonical_archetype","candidate_delta":0.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"Only the case with NAV/shareholder-return bridge delivered high MFE with controlled MAE; event-premium-only rows roundtripped."}
{"row_type":"shadow_weight","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"local_4b_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"C32 event premium can peak locally and fade; local 4B watch should activate without treating price-only event peak as full 4B unless non-price overheat/cap evidence exists."}
{"row_type":"shadow_weight","round":"R11","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","axis":"event_premium_cap_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If C32 MFE90<20 and MAE180<-15 after a value-up/control-premium event, require stronger payout/NAV/asset-action evidence before Yellow/Green."}
```

Interpretation:

```text
C32 should not become a generic value-up momentum bucket.
It should ask: what concretely converts governance/event premium into owner return?

Acceptable bridge examples:
- confirmed buyback/cancellation or payout step-up,
- tender/control premium with economically binding terms,
- NAV realization, asset monetization, or capital-allocation proof,
- durable financial visibility rather than one-day policy or event rerating.

Without that bridge, C32 should route to Watch / local 4B guard.
```

## 11. Data-quality caveat

All three selected cases use actual Stock-Web OHLC rows and clean tradable shards for the selected 2024 windows.  
The non-price evidence layer is still source-name/proxy level.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm trigger rows validate with price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Check that C32 rows are not hard duplicates by canonical_archetype_id + symbol + trigger_type + entry_date.
4. If aggregate support remains stable after exact evidence URL repair, consider a C32-scoped safe patch:
   - governance_bridge_required,
   - event_premium_cap_guard,
   - local_4b_watch_guard for price-only control/event premium spikes.
5. Do not loosen Stage3-Green. Do not use future MFE/MAE in runtime scoring. Use this only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R11
completed_loop = 83
next_round = R12
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```
