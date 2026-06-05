# E2R Stock-Web v12 Residual Research — R9 Loop 83 / L3 / C29

---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 83
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: MOBILITY_VOLUME_MIX_MARGIN_BRIDGE_VS_TIRE_ADAS_PRICE_SPIKE
sector: Mobility / auto parts / tire / ADAS
output_file: e2r_stock_web_v12_residual_round_R9_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---


## 1. Scope lock

This run follows the sequential v12 scheduler after the latest session state `R8 loop 83`.

```text
scheduled_round = R9
scheduled_loop = 83
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is treated as the mobility/transport specialty lane. This MD does not recommend current stocks, does not patch `stock_agent`, and does not change production scoring. It only adds Stock-Web 1D OHLC based historical calibration rows.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"012330","company_name":"현대모비스","profile_path":"atlas/symbol_profiles/012/012330.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7753,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1997-05-27","1999-01-08","1999-04-15","1999-08-16","1999-12-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are historical and do not contaminate the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"002350","company_name":"넥센타이어","profile_path":"atlas/symbol_profiles/002/002350.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7723,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-02-18","1999-06-08","1999-06-10","2008-03-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are historical and do not contaminate the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"204320","company_name":"HL만도","profile_path":"atlas/symbol_profiles/204/204320.json","first_date":"2014-10-06","last_date":"2026-02-20","trading_day_count":2790,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2018-05-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate is historical and does not contaminate the 2024/2025 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_2025_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

The No-Repeat Index is used only as a duplicate ledger. C29 is already well covered, so this run deliberately avoids the high-repeat C29 set such as `011210`, `000270`, `005380`, `005850`, `010690`, and `018880`.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novel keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012330","trigger_type":"Stage2-Actionable-MobilityMixMarginCapitalReturn-Positive","entry_date":"2024-02-01","duplicate_status":"selected as new C29 positive bridge control; exact hard key not reused"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"002350","trigger_type":"Stage2-FalsePositive-TireMarginSpike-NoVolumeBridge","entry_date":"2024-04-11","duplicate_status":"selected as C29 tire-margin high-MAE counterexample; not in top-covered symbol set"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"204320","trigger_type":"Stage2-FalsePositive-ADAS-EVComponentSpike-NoMarginBridge","entry_date":"2024-06-05","duplicate_status":"selected as C29 ADAS/EV component high-MAE counterexample; not in top-covered symbol set"}
```

## 4. Research question

C29 should catch real mobility operating leverage, but it should not turn every auto/tire/ADAS price spike into a Stage2 promotion.

Residual question:

```text
Can the calibrated profile distinguish:
1. mobility mix / parts margin / capital-return bridge with low MAE,
2. tire margin spike with no durable volume bridge,
3. ADAS/EV component momentum spike with no delivery or margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L83_012330_HYUNDAIMOBIS_VALUEUP_MIX_MARGIN_BRIDGE","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_AFTERMARKET_ELECTRIFICATION_MIX_CAPITAL_RETURN_BRIDGE","symbol":"012330","company_name":"현대모비스","case_role":"positive_control","case_summary":"Large-cap auto parts value-up / margin-mix bridge with clean 2024 price window; Stage2/Yellow can be allowed when mobility volume/mix evidence is paired with shareholder-return or margin bridge, but no Green relaxation without exact evidence URLs."}
{"row_type":"case","case_id":"C29_R9L83_002350_NEXENTIRE_MARGIN_SPIKE_ROUNDTRIP","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_MARGIN_OPERATING_LEVERAGE_PRICE_SPIKE_NO_VOLUME_BRIDGE","symbol":"002350","company_name":"넥센타이어","case_role":"counterexample","case_summary":"Tire margin/operating-leverage spike failed after entry: almost no MFE and large 90/180D MAE. C29 should require volume/mix/margin continuity rather than price spike alone."}
{"row_type":"case","case_id":"C29_R9L83_204320_HLMANDO_ADAS_EV_MIX_SPIKE_HIGH_MAE","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_EV_COMPONENT_ORDER_SPIKE_NO_MARGIN_DELIVERY_BRIDGE","symbol":"204320","company_name":"HL만도","case_role":"counterexample","case_summary":"ADAS/EV component excitement after a price spike showed almost no follow-through and deep 90/180D MAE; C29 needs a local bridge requirement before Yellow/Green."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 012330 현대모비스 — positive mobility mix/margin bridge

Entry row: `2024-02-01 c=219500`.
The 30D/90D/180D high is `2024-03-18 h=270000`; the entry-day low is `208000`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L83_C29_012330_20240201_STAGE2_VALUEUP_MIX_MARGIN_BRIDGE_POSITIVE","case_id":"C29_R9L83_012330_HYUNDAIMOBIS_VALUEUP_MIX_MARGIN_BRIDGE","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_AFTERMARKET_ELECTRIFICATION_MIX_CAPITAL_RETURN_BRIDGE","sector":"mobility/auto-parts","primary_archetype":"mobility volume/mix/margin operating leverage","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","symbol":"012330","company_name":"현대모비스","trigger_type":"Stage2-Actionable-MobilityMixMarginCapitalReturn-Positive","trigger_date":"2024-02-01","evidence_available_at_that_date":"historical_public_report_consensus_proxy; value-up/capital-return and mobility mix/margin bridge proxy; exact URL pending","evidence_source":"source-name-level proxy; exact URL pending; used only as non-price bridge proxy","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"non_price_evidence_bridge":true,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv","profile_path":"atlas/symbol_profiles/012/012330.json","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-01","entry_price":219500.0,"entry_price_basis":"close","entry_row_exists":true,"MFE_30D_pct":23.01,"MFE_90D_pct":23.01,"MFE_180D_pct":23.01,"MFE_1Y_pct":"not_calculated","MFE_2Y_pct":"not_calculated","MAE_30D_pct":-5.24,"MAE_90D_pct":-5.24,"MAE_180D_pct":-5.24,"MAE_1Y_pct":"not_calculated","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date_30D":"2024-03-18","peak_price_30D":270000.0,"peak_date_90D":"2024-03-18","peak_price_90D":270000.0,"peak_date_180D":"2024-03-18","peak_price_180D":270000.0,"peak_date":"2024-03-18","peak_price":270000.0,"max_drawdown_low_30D_date":"2024-02-01","max_drawdown_low_30D":208000.0,"max_drawdown_low_90D_date":"2024-02-01","max_drawdown_low_90D":208000.0,"max_drawdown_low_180D_date":"2024-02-01","max_drawdown_low_180D":208000.0,"drawdown_after_peak_pct":-21.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"price_only_local_peak_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_good_stage2_moderate_MFE_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"C29_012330_20240201_219500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","current_profile_residual":"C29 should allow Stage2/Yellow when mobility mix/parts margin and capital-return bridge exist, while still blocking Green relaxation because exact evidence URLs are pending."}
```

### 6.2 002350 넥센타이어 — tire margin spike without durable bridge

Entry row: `2024-04-11 c=9500`.
The upside was almost capped at `2024-05-02 h=9600`, while the 180D low fell to `2024-12-30 l=6000`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L83_C29_002350_20240411_STAGE2_FALSE_POSITIVE_TIRE_MARGIN_ROUNDTRIP","case_id":"C29_R9L83_002350_NEXENTIRE_MARGIN_SPIKE_ROUNDTRIP","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_MARGIN_OPERATING_LEVERAGE_PRICE_SPIKE_NO_VOLUME_BRIDGE","sector":"mobility/tire","primary_archetype":"mobility volume/mix/margin operating leverage","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","symbol":"002350","company_name":"넥센타이어","trigger_type":"Stage2-FalsePositive-TireMarginSpike-NoVolumeBridge","trigger_date":"2024-04-11","evidence_available_at_that_date":"historical_public_report_consensus_proxy; tire margin/operating leverage theme proxy; exact URL pending","evidence_source":"source-name-level proxy; exact URL pending; treated as insufficient non-price bridge unless volume/mix/margin continuity is verified","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"non_price_evidence_bridge":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv","profile_path":"atlas/symbol_profiles/002/002350.json","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-11","entry_price":9500.0,"entry_price_basis":"close","entry_row_exists":true,"MFE_30D_pct":1.05,"MFE_90D_pct":1.05,"MFE_180D_pct":1.05,"MFE_1Y_pct":"not_calculated","MFE_2Y_pct":"not_calculated","MAE_30D_pct":-15.47,"MAE_90D_pct":-22.74,"MAE_180D_pct":-36.84,"MAE_1Y_pct":"not_calculated","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date_30D":"2024-05-02","peak_price_30D":9600.0,"peak_date_90D":"2024-05-02","peak_price_90D":9600.0,"peak_date_180D":"2024-05-02","peak_price_180D":9600.0,"peak_date":"2024-05-02","peak_price":9600.0,"max_drawdown_low_30D_date":"2024-05-24","max_drawdown_low_30D":8030.0,"max_drawdown_low_90D_date":"2024-08-05","max_drawdown_low_90D":7340.0,"max_drawdown_low_180D_date":"2024-12-30","max_drawdown_low_180D":6000.0,"drawdown_after_peak_pct":-37.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_price_spike_failed_no_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"C29_002350_20240411_9500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","current_profile_residual":"Tire margin theme produced almost no upside and large 90/180D drawdown. C29 needs volume/mix/margin continuity before Stage2/Yellow promotion."}
```

### 6.3 204320 HL만도 — ADAS/EV component spike without margin bridge

Entry row: `2024-06-05 c=49600`.
The spike peak was the same day at `h=50000`, while the 90D/180D low reached `2024-09-24 l=32750`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L83_C29_204320_20240605_STAGE2_FALSE_POSITIVE_ADAS_EV_SPIKE_HIGH_MAE","case_id":"C29_R9L83_204320_HLMANDO_ADAS_EV_MIX_SPIKE_HIGH_MAE","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_EV_COMPONENT_ORDER_SPIKE_NO_MARGIN_DELIVERY_BRIDGE","sector":"mobility/auto-parts/ADAS","primary_archetype":"mobility volume/mix/margin operating leverage","loop_objective":"residual_false_positive_mining;4B_non_price_requirement_stress_test;counterexample_mining","symbol":"204320","company_name":"HL만도","trigger_type":"Stage2-FalsePositive-ADAS-EVComponentSpike-NoMarginBridge","trigger_date":"2024-06-05","evidence_available_at_that_date":"historical_public_report_consensus_proxy; ADAS/EV component momentum proxy; exact URL pending","evidence_source":"source-name-level proxy; exact URL pending; ADAS/EV order spike treated as insufficient until margin/delivery bridge is visible","evidence_source_type":"historical_public_report_consensus_proxy","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"non_price_evidence_bridge":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/204/204320.json","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-05","entry_price":49600.0,"entry_price_basis":"close","entry_row_exists":true,"MFE_30D_pct":0.81,"MFE_90D_pct":0.81,"MFE_180D_pct":0.81,"MFE_1Y_pct":"not_calculated","MFE_2Y_pct":"not_calculated","MAE_30D_pct":-17.64,"MAE_90D_pct":-33.97,"MAE_180D_pct":-33.97,"MAE_1Y_pct":"not_calculated","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date_30D":"2024-06-05","peak_price_30D":50000.0,"peak_date_90D":"2024-06-05","peak_price_90D":50000.0,"peak_date_180D":"2024-06-05","peak_price_180D":50000.0,"peak_date":"2024-06-05","peak_price":50000.0,"max_drawdown_low_30D_date":"2024-07-08","max_drawdown_low_30D":40850.0,"max_drawdown_low_90D_date":"2024-09-24","max_drawdown_low_90D":32750.0,"max_drawdown_low_180D_date":"2024-09-24","max_drawdown_low_180D":32750.0,"drawdown_after_peak_pct":-34.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_4B_watch_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_2025_window","same_entry_group_id":"C29_204320_20240605_49600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","current_profile_residual":"ADAS/EV component spike had almost no MFE and deep 90D drawdown. C29 should require margin/delivery bridge and route price-only spikes to Watch/local 4B guard."}
```

## 7. Score simulation rows

Proxy-only simulation rows for calibration analysis. They do not change production scoring.

```jsonl
{"row_type":"score_simulation","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012330","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":12,"market_mispricing":14,"valuation_rerating":11,"capital_allocation":6,"information_confidence":5,"raw_total_proxy":84,"weighted_total_proxy":79,"simulated_stage":"Stage2-Actionable/Stage3-Yellow-Watch","simulation_note":"Allow watch-to-Yellow when non-price margin/capital-return bridge exists; no Green loosening without exact evidence URLs."}
{"row_type":"score_simulation","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"002350","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":15,"earnings_visibility":11,"bottleneck_pricing":8,"market_mispricing":13,"valuation_rerating":7,"capital_allocation":3,"information_confidence":3,"raw_total_proxy":60,"weighted_total_proxy":58,"simulated_stage":"Stage2-FalsePositive-Watch","simulation_note":"Price spike and tire margin narrative without volume/mix continuity should remain Watch/local 4B guard."}
{"row_type":"score_simulation","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"204320","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":14,"earnings_visibility":10,"bottleneck_pricing":11,"market_mispricing":14,"valuation_rerating":7,"capital_allocation":3,"information_confidence":3,"raw_total_proxy":62,"weighted_total_proxy":58,"simulated_stage":"Stage2-FalsePositive-Watch","simulation_note":"ADAS/EV component spike lacks delivery/margin confirmation; high-MAE path should block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L83_C29_P0_VS_P3","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile":"P0_e2r_2_0_baseline","profile_role":"rollback_reference","expected_error":"Would over-credit mobility price/momentum and under-detect no-volume/margin-bridge false positives."}
{"row_type":"profile_comparison","comparison_id":"R9L83_C29_P0B_CURRENT","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile":"P0b_e2r_2_2_rolling_calibrated","profile_role":"current_default_proxy","expected_error":"Global price-only guard works, but C29 needs a local rule separating mobility mix/margin bridge from tire/ADAS price spikes."}
{"row_type":"profile_comparison","comparison_id":"R9L83_C29_P1_VOLUME_MIX_MARGIN_BRIDGE","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile":"P1_shadow_C29_volume_mix_margin_bridge_required","profile_role":"shadow_candidate","expected_effect":"Stage2/Yellow requires at least one non-price volume/mix/margin/capital-return bridge; price spike only remains Watch."}
{"row_type":"profile_comparison","comparison_id":"R9L83_C29_P2_LOCAL_4B_GUARD","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile":"P2_shadow_C29_local_4B_watch_guard","profile_role":"shadow_candidate","expected_effect":"If MFE90<5 and MAE90<=-20 in historical calibration, route to local 4B/watch and require stronger bridge before any Yellow/Green."}
{"row_type":"profile_comparison","comparison_id":"R9L83_C29_P3_RECOMMENDED","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile":"P3_recommended_shadow_only","profile_role":"recommended_shadow_rule","expected_effect":"No production change now; record C29-scoped bridge requirement and local 4B/high-MAE guard for later batch planner."}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_MOBILITY_MARGIN_BRIDGE_VS_PRICE_SPIKE_STRESS","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":8.29,"avg_MAE90_pct":-20.65,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C29 positive bridge exists, but two new symbols show low-MFE/high-MAE false positives when volume/mix/margin confirmation is missing."}
{"row_type":"stage_transition_summary","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012330","trigger_type":"Stage2-Actionable-MobilityMixMarginCapitalReturn-Positive","entry_date":"2024-02-01","stage2_to_90D_outcome":"good_stage2","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow watch when non-price volume/mix/margin and capital-return bridge exists; evidence URL still pending."}
{"row_type":"stage_transition_summary","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"002350","trigger_type":"Stage2-FalsePositive-TireMarginSpike-NoVolumeBridge","entry_date":"2024-04-11","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Tire margin spike without volume/mix bridge round-tripped into high-MAE drawdown."}
{"row_type":"stage_transition_summary","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"204320","trigger_type":"Stage2-FalsePositive-ADAS-EVComponentSpike-NoMarginBridge","entry_date":"2024-06-05","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"ADAS/EV component spike had tiny MFE and deep 90D MAE; local C29 bridge guard should block promotion."}
{"row_type":"residual_contribution","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"C29_volume_mix_margin_bridge_vs_price_spike_false_positive","contribution":"Adds two high-MAE C29 counterexamples and one positive mobility mix/margin bridge control, reducing top-covered OEM repetition and strengthening C29-scoped bridge requirements.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_rows":3,"new_symbols":3,"new_positive":1,"new_counterexample":2,"new_4B_watch":2,"new_4C":0,"source_proxy_only":3,"evidence_url_pending":3,"calibration_usable":3,"next_gap":"Replace source-name proxies with exact report/disclosure URLs; test transport/logistics mobility-adjacent C29 cases in future R9 loops."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"volume_mix_margin_bridge_required","scope":"canonical_archetype","candidate_delta":0.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"2/3 selected clean C29 cases were high-MAE false positives; require non-price volume/mix/margin or capital-return bridge for Stage2/Yellow."}
{"row_type":"shadow_weight","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"local_4b_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Tire and ADAS/EV component price spikes showed MFE90 near zero and MAE90 <= -20; price-only mobility spikes should stay Watch/local 4B."}
{"row_type":"shadow_weight","round":"R9","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"high_mae_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"Historical trigger if MFE90<5 and MAE90<=-20: block Yellow/Green and require bridge repair."}
```

Interpretation:

```text
C29 can keep mobility operating leverage credit, but the bridge must have teeth:
- volume / mix / margin continuity,
- delivery or customer conversion,
- capital-return or clear financial visibility where relevant,
- shallow MAE and no corporate-action contamination.

If the case is mostly tire/ADAS/EV price momentum without a non-price bridge, it should route to Watch / local 4B guard rather than Stage3-Yellow or Green.
```

## 11. Current calibrated profile stress test

```text
1. current calibrated profile would likely allow 012330 as Stage2/Yellow-watch because non-price bridge proxy exists.
2. This matches MFE/MAE: MFE180 +23.01%, MAE180 -5.24%.
3. The same profile would be too generous if it treated 002350 or 204320 price spikes as actionable Stage2.
4. 002350: MFE90 +1.05%, MAE90 -22.74%, MAE180 -36.84%.
5. 204320: MFE90 +0.81%, MAE90 -33.97%.
6. price-only blowoff guard is strengthened, but C29 needs an archetype-specific bridge test.
7. full 4B non-price requirement remains correct: these are local 4B/watch rows, not full 4B confirmations.
8. hard 4C routing is not directly changed; both counterexamples are thesis-break watch rows, not hard 4C rows.
```

## 12. Data-quality caveat

All selected trigger rows use actual Stock-Web tradable OHLC rows and clean 180D calibration windows.
However, non-price evidence remains source-name/proxy level.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. One-line contribution summary

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```

## 14. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Check that C29 rows are representative and not hard duplicates by canonical_archetype_id + symbol + trigger_type + entry_date.
4. If aggregate support remains stable after exact evidence URL repair, consider a C29-scoped safe patch:
   - volume_mix_margin_bridge_required,
   - local_4b_watch_guard for tire/ADAS/EV price spikes,
   - high_mae_guardrail when MFE90 < 5 and MAE90 <= -20.
5. Do not loosen Stage3-Green. Do not use future MFE/MAE in runtime scoring. Use this only for calibration profile planning.
```

## 15. Round state

```text
completed_round = R9
completed_loop = 83
next_round = R10
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass

scheduled_round = R9
scheduled_loop = 83
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
diversity_score_summary = Avoided top-covered C29 OEM set and added 012330/002350/204320 as new symbol/failure-mode mix.
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
production_scoring_changed = false
shadow_weight_only = true
```
