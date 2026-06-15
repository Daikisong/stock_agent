---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 103
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R3/L3/C12 Battery Customer Contract Call-off Risk Third Pass to 30

```text
output_file = e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round = R3
selected_loop = 103
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` keeps `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` in Priority 0 with 16 static representative rows and a need-to-30 gap. Conversation-local C12 work already added two four-row passes: the earlier C12 loop used 348370/247540/361610/278280, and the immediately prior C12 loop used 373220/096770/011790/051910. This third pass deliberately avoids those exact C12 symbol/entry combinations and adds six new symbols: 066970, 005070, 020150, 121600, 222080, and 299030. If accepted, C12 reaches the 30-row floor.

```text
selection_reason = C12 remains under-covered after second pass; use six new symbols to finish 30-row floor.
selected_priority_bucket = Priority 0
static_index_rows = 16
conversation_local_prior_c12_rows = 24
conversation_local_after_this_loop = 30
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
same_canonical_archetype_research = allowed
same_symbol_same_trigger_family_reuse = avoided
```

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"}
{"row_type":"price_source_validation","symbol":"066970","name":"엘앤에프","profile":"atlas/symbol_profiles/066/066970.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2016-02-19","2021-08-11"],"calibration_caveat":"historic corporate-action candidates only; no overlap with 2024 180D windows","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"005070","name":"코스모신소재","profile":"atlas/symbol_profiles/005/005070.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","corporate_action_candidate_count":8,"corporate_action_candidate_dates_last":"2019-11-13","calibration_caveat":"historic corporate-action candidates only; no overlap with 2024 180D windows","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"020150","name":"롯데에너지머티리얼즈","profile":"atlas/symbol_profiles/020/020150.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"calibration_caveat":"","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"121600","name":"나노신소재","profile":"atlas/symbol_profiles/121/121600.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv","corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-12-17"],"calibration_caveat":"historic corporate-action candidate only; no overlap with 2024 180D windows","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"222080","name":"씨아이에스","profile":"atlas/symbol_profiles/222/222080.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv","corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2017-01-20"],"calibration_caveat":"historic SPAC-transition candidate only; no overlap with 2024 180D windows","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"299030","name":"하나기술","profile":"atlas/symbol_profiles/299/299030.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv","corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-03-22","2021-04-13"],"calibration_caveat":"historic corporate-action candidates only; no overlap with 2024 180D windows","calibration_usable":true}
```

## 3. Case rows

```jsonl
{"row_type":"case","case_id":"C12_R3_L103_CASE_001","symbol":"066970","name":"엘앤에프","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"counterexample_high_mae_after_cathode_contract_label","trigger_family":"cathode_customer_contract_without_calloff_volume","entry_date":"2024-03-22","entry_price":186100.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L103_CASE_002","symbol":"005070","name":"코스모신소재","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"mixed_positive_restocking_then_mae","trigger_family":"cathode_material_restocking_vs_customer_calloff_cash_bridge","entry_date":"2024-02-16","entry_price":175800.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L103_CASE_003","symbol":"020150","name":"롯데에너지머티리얼즈","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"positive_local_restocking_with_180d_guard","trigger_family":"copper_foil_customer_reorder_and_utilization_watch","entry_date":"2024-03-21","entry_price":47050.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L103_CASE_004","symbol":"121600","name":"나노신소재","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"mixed_positive_binary_customer_capacity_spike","trigger_family":"cnt_conductive_additive_customer_capacity_vs_actual_calloff","entry_date":"2024-02-21","entry_price":134000.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L103_CASE_005","symbol":"222080","name":"씨아이에스","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"counterexample_equipment_customer_order_delay","trigger_family":"battery_equipment_customer_order_contract_calloff_delay","entry_date":"2024-03-12","entry_price":14840.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L103_CASE_006","symbol":"299030","name":"하나기술","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"counterexample_equipment_orderbook_to_cash_failure","trigger_family":"battery_equipment_orderbook_customer_acceptance_payment_delay","entry_date":"2024-03-08","entry_price":67200.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 4. Trigger-level backtest rows: 30D / 90D / 180D MFE-MAE

All entries are present in the tradable shard. Metrics are calculated on stock-web raw/unadjusted OHLC and are intentionally rounded because this MD is a research artifact, not a production scoring update.

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L103_CASE_001","same_entry_group_id":"C12_066970_2024-03-22_Stage2-Actionable","dedupe_for_aggregate":true,"selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE","symbol":"066970","name":"엘앤에프","trigger_type":"Stage2-Actionable","trigger_family":"cathode_customer_contract_without_calloff_volume","entry_date":"2024-03-22","entry_price":186100.0,"price_basis":"tradable_raw","calibration_usable":true,"peak_30d_date":"2024-03-25","peak_30d_high":199000.0,"mfe_30d_pct":6.93,"trough_30d_date":"2024-04-17","trough_30d_low":140600.0,"mae_30d_pct":-24.45,"peak_90d_date":"2024-03-25","peak_90d_high":199000.0,"mfe_90d_pct":6.93,"trough_90d_date":"2024-06-28","trough_90d_low":134100.0,"mae_90d_pct":-27.94,"peak_180d_date":"2024-03-25","peak_180d_high":199000.0,"mfe_180d_pct":6.93,"trough_180d_date":"2024-09-10","trough_180d_low":82900.0,"mae_180d_pct":-55.45,"score_return_alignment":"aligned_counterexample","current_profile_error":"A cathode customer-contract label produced only a small local MFE before a severe 180D drawdown; Stage3 needs actual call-off/utilization evidence.","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L103_CASE_002","same_entry_group_id":"C12_005070_2024-02-16_Stage4B","dedupe_for_aggregate":true,"selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE","symbol":"005070","name":"코스모신소재","trigger_type":"Stage4B","trigger_family":"cathode_material_restocking_vs_customer_calloff_cash_bridge","entry_date":"2024-02-16","entry_price":175800.0,"price_basis":"tradable_raw","calibration_usable":true,"peak_30d_date":"2024-02-21","peak_30d_high":194300.0,"mfe_30d_pct":10.52,"trough_30d_date":"2024-03-29","trough_30d_low":159500.0,"mae_30d_pct":-9.27,"peak_90d_date":"2024-02-21","peak_90d_high":194300.0,"mfe_90d_pct":10.52,"trough_90d_date":"2024-05-24","trough_90d_low":136800.0,"mae_90d_pct":-22.18,"peak_180d_date":"2024-02-21","peak_180d_high":194300.0,"mfe_180d_pct":10.52,"trough_180d_date":"2024-07-18","trough_180d_low":131500.0,"mae_180d_pct":-25.20,"score_return_alignment":"mixed_positive_high_mae","current_profile_error":"Initial restocking MFE should be preserved as a local watch, but the later MAE means no durable Stage3 without call-off and margin conversion.","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L103_CASE_003","same_entry_group_id":"C12_020150_2024-03-21_Stage2-Actionable","dedupe_for_aggregate":true,"selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"Stage2-Actionable","trigger_family":"copper_foil_customer_reorder_and_utilization_watch","entry_date":"2024-03-21","entry_price":47050.0,"price_basis":"tradable_raw","calibration_usable":true,"peak_30d_date":"2024-03-25","peak_30d_high":51500.0,"mfe_30d_pct":9.46,"trough_30d_date":"2024-04-18","trough_30d_low":40400.0,"mae_30d_pct":-14.13,"peak_90d_date":"2024-06-18","peak_90d_high":59200.0,"mfe_90d_pct":25.82,"trough_90d_date":"2024-04-18","trough_90d_low":40400.0,"mae_90d_pct":-14.13,"peak_180d_date":"2024-06-18","peak_180d_high":59200.0,"mfe_180d_pct":25.82,"trough_180d_date":"2024-08-08","trough_180d_low":30850.0,"mae_180d_pct":-34.43,"score_return_alignment":"positive_local_4b_watch","current_profile_error":"Copper-foil restocking can generate usable MFE, but without customer reorder cadence and utilization recovery it should stay local 4B/watch rather than Green.","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L103_CASE_004","same_entry_group_id":"C12_121600_2024-02-21_Stage2-Actionable","dedupe_for_aggregate":true,"selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE","symbol":"121600","name":"나노신소재","trigger_type":"Stage2-Actionable","trigger_family":"cnt_conductive_additive_customer_capacity_vs_actual_calloff","entry_date":"2024-02-21","entry_price":134000.0,"price_basis":"tradable_raw","calibration_usable":true,"peak_30d_date":"2024-02-22","peak_30d_high":157800.0,"mfe_30d_pct":17.76,"trough_30d_date":"2024-04-04","trough_30d_low":121700.0,"mae_30d_pct":-9.18,"peak_90d_date":"2024-02-22","peak_90d_high":157800.0,"mfe_90d_pct":17.76,"trough_90d_date":"2024-05-27","trough_90d_low":100200.0,"mae_90d_pct":-25.22,"peak_180d_date":"2024-02-22","peak_180d_high":157800.0,"mfe_180d_pct":17.76,"trough_180d_date":"2024-07-18","trough_180d_low":101000.0,"mae_180d_pct":-24.63,"score_return_alignment":"mixed_positive_high_mae","current_profile_error":"CNT/customer-capacity spike needs an explicit customer shipment and inventory absorption bridge before durable Stage3.","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L103_CASE_005","same_entry_group_id":"C12_222080_2024-03-12_Stage4B","dedupe_for_aggregate":true,"selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE","symbol":"222080","name":"씨아이에스","trigger_type":"Stage4B","trigger_family":"battery_equipment_customer_order_contract_calloff_delay","entry_date":"2024-03-12","entry_price":14840.0,"price_basis":"tradable_raw","calibration_usable":true,"peak_30d_date":"2024-03-12","peak_30d_high":15100.0,"mfe_30d_pct":1.75,"trough_30d_date":"2024-04-11","trough_30d_low":11110.0,"mae_30d_pct":-25.13,"peak_90d_date":"2024-03-12","peak_90d_high":15100.0,"mfe_90d_pct":1.75,"trough_90d_date":"2024-05-30","trough_90d_low":10520.0,"mae_90d_pct":-29.11,"peak_180d_date":"2024-03-12","peak_180d_high":15100.0,"mfe_180d_pct":1.75,"trough_180d_date":"2024-07-23","trough_180d_low":9160.0,"mae_180d_pct":-38.27,"score_return_alignment":"aligned_counterexample","current_profile_error":"Battery-equipment order language failed to convert into customer acceptance/payment cadence; the score should cap at 4B/4C until cash bridge appears.","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L103_CASE_006","same_entry_group_id":"C12_299030_2024-03-08_Stage4B","dedupe_for_aggregate":true,"selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_THIRD_PASS_TO_30_MATERIALS_AND_EQUIPMENT_UTILIZATION_BRIDGE","symbol":"299030","name":"하나기술","trigger_type":"Stage4B","trigger_family":"battery_equipment_orderbook_customer_acceptance_payment_delay","entry_date":"2024-03-08","entry_price":67200.0,"price_basis":"tradable_raw","calibration_usable":true,"peak_30d_date":"2024-03-08","peak_30d_high":73100.0,"mfe_30d_pct":8.78,"trough_30d_date":"2024-04-16","trough_30d_low":50000.0,"mae_30d_pct":-25.60,"peak_90d_date":"2024-03-08","peak_90d_high":73100.0,"mfe_90d_pct":8.78,"trough_90d_date":"2024-05-31","trough_90d_low":52700.0,"mae_90d_pct":-21.58,"peak_180d_date":"2024-03-08","peak_180d_high":73100.0,"mfe_180d_pct":8.78,"trough_180d_date":"2024-07-23","trough_180d_low":28950.0,"mae_180d_pct":-56.92,"score_return_alignment":"aligned_counterexample","current_profile_error":"A battery-equipment orderbook label without customer acceptance/payment evidence is a high-MAE false positive and should be capped well below Stage3.","evidence_url_pending":true,"source_proxy_only":true}
```

## 5. Human-readable path notes

### C12_R3_L103_CASE_001 — 066970 엘앤에프
- Entry: 2024-03-22 close 186,100.
- 30D path: MFE +6.93% at 2024-03-25 / MAE -24.45% at 2024-04-17.
- 90D path: MFE +6.93% / MAE -27.94% at 2024-06-28.
- 180D path: MFE +6.93% / MAE -55.45% at 2024-09-10.
- Residual thesis: A cathode customer-contract label without call-off volume and margin evidence is not a Stage3 setup. It is a textbook C12 high-MAE guard candidate.

### C12_R3_L103_CASE_002 — 005070 코스모신소재
- Entry: 2024-02-16 close 175,800.
- 30D path: MFE +10.52% / MAE -9.27%.
- 90D path: MFE +10.52% / MAE -22.18%.
- 180D path: MFE +10.52% / MAE -25.20%.
- Residual thesis: This is a mixed case. The model should preserve local restocking MFE, but Green requires customer demand visibility and working-capital absorption.

### C12_R3_L103_CASE_003 — 020150 롯데에너지머티리얼즈
- Entry: 2024-03-21 close 47,050.
- 30D path: MFE +9.46% / MAE -14.13%.
- 90D path: MFE +25.82% / MAE -14.13%.
- 180D path: MFE +25.82% / MAE -34.43%.
- Residual thesis: Copper foil can produce real local upside when the market anticipates customer restocking. It still needs a utilization/call-off bridge before durable Stage3.

### C12_R3_L103_CASE_004 — 121600 나노신소재
- Entry: 2024-02-21 close 134,000.
- 30D path: MFE +17.76% / MAE -9.18%.
- 90D path: MFE +17.76% / MAE -25.22%.
- 180D path: MFE +17.76% / MAE -24.63%.
- Residual thesis: Customer-capacity or CNT additive excitement creates a sharp local rally, but persistent MAE says call-off and actual shipments must gate Stage3.

### C12_R3_L103_CASE_005 — 222080 씨아이에스
- Entry: 2024-03-12 close 14,840.
- 30D path: MFE +1.75% / MAE -25.13%.
- 90D path: MFE +1.75% / MAE -29.11%.
- 180D path: MFE +1.75% / MAE -38.27%.
- Residual thesis: Equipment contract/orderbook language did not convert into customer acceptance or cash collection. This should be an explicit C12/C11 boundary guard.

### C12_R3_L103_CASE_006 — 299030 하나기술
- Entry: 2024-03-08 close 67,200.
- 30D path: MFE +8.78% / MAE -25.60%.
- 90D path: MFE +8.78% / MAE -21.58%.
- 180D path: MFE +8.78% / MAE -56.92%.
- Residual thesis: Battery-equipment orderbook without customer acceptance/payment cadence is a high-MAE false positive.

## 6. Current calibrated profile stress test

The existing profile already blocks pure price-only blowoff and requires non-price evidence for full 4B. C12 still benefits from a more surgical bridge: customer-contract language is one layer upstream of realized call-off, utilization, working-capital absorption, and cash conversion. Like a factory receiving a signed purchase order but no release schedule, the headline can look firm while the line sits idle. The rule should preserve local restocking MFE when price confirms it, but deny durable Stage3 until the physical release cadence appears.

```jsonl
{"row_type":"score_simulation","axis":"C12_calloff_release_schedule_bridge","before_profile":"e2r_2_1_stock_web_calibrated","candidate_shadow_rule":"C12 Stage3 requires customer call-off/release schedule, utilization stabilization, or shipment revenue cadence evidence, not just contract/framework language.","expected_effect":"reduce 066970/222080/299030 style high-MAE false positives while preserving 020150 local restocking watch cases"}
{"row_type":"score_simulation","axis":"C12_equipment_acceptance_payment_guard","before_profile":"e2r_2_1_stock_web_calibrated","candidate_shadow_rule":"Battery-equipment orderbook cases cannot exceed Stage2 unless acceptance, delivery, payment, or working-capital conversion evidence exists.","expected_effect":"cleanly separates C12 customer call-off risk from C11 pure orderbook rerating"}
{"row_type":"score_simulation","axis":"C12_material_inventory_absorption_guard","before_profile":"e2r_2_1_stock_web_calibrated","candidate_shadow_rule":"Cathode/copper-foil/CNT material suppliers need inventory absorption and customer reorder confirmation before durable Stage3-Green.","expected_effect":"prevents cathode/material label reratings when customer inventory is still being digested"}
```

## 7. Aggregate / residual contribution

```jsonl
{"row_type":"aggregate","selected_round":"R3","selected_loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":6,"reused_case_count":0,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":3,"local_4b_watch_count":4,"current_profile_error_count":6,"median_mfe_180d_pct":9.65,"median_mae_180d_pct":-35.79,"auto_selected_coverage_gap_static_index":"C12 rows 16 -> 22 if accepted","auto_selected_coverage_gap_conversation_local":"C12 rows 24 -> 30 if accepted; C12 30-row Priority 0 floor reached","residual_contribution_label":"canonical_archetype_rule_candidate"}
{"row_type":"shadow_weight","production_scoring_changed":false,"do_not_propose_new_weight_delta":false,"new_axis_proposed":["C12_calloff_release_schedule_bridge_required","C12_equipment_acceptance_payment_guard","C12_material_inventory_absorption_guard","C12_local_mfe_vs_durable_stage3_split","C12_high_MAE_customer_contract_label_guard"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":null}
{"row_type":"residual_contribution","new_failure_mode":"customer contract or orderbook language can be several quarters upstream of actual call-off, acceptance, and payment conversion","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"why_global_rule_insufficient":"global price-only and non-price 4B rules do not distinguish framework contract, release schedule, utilization, delivery acceptance, and working-capital conversion","batch_implementation_hint":"implement as C12-specific shadow guard; do not apply as broad battery-sector penalty to C11/C13/C14"}
```

## 8. Proposed C12-specific shadow rule

```text
C12_calloff_release_schedule_bridge_required:
  For battery customer-contract cases, Stage3-Yellow requires at least one concrete downstream bridge: release schedule/call-off volume, shipment cadence, utilization stabilization, inventory absorption, or working-capital/cash conversion. Signed framework, customer name, or capacity expansion language alone remains Stage2/4B.

C12_equipment_acceptance_payment_guard:
  Battery-equipment suppliers with orderbook headlines require delivery acceptance, customer payment, or backlog-to-revenue evidence before durable Stage3. Otherwise, classify as local 4B/watch or high-MAE counterexample.

C12_local_mfe_vs_durable_stage3_split:
  If 30~90D MFE is strong but 90~180D MAE exceeds -25%, preserve local tradeability but block Green unless call-off/utilization evidence confirms that the demand bridge has become cash.
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent. Do not rerun research. Ingest this MD as a v12 residual research artifact only after batch review. Extract JSONL rows with row_type in [case, trigger, score_simulation, aggregate, shadow_weight, residual_contribution]. Do not modify production scoring directly. If accepted, map proposed axes to C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK shadow rules and test against existing v12 validation rows. Preserve stock-web price_basis=tradable_raw and block corporate-action contaminated windows by default.
```

## 10. Next research state

```text
completed_round = R3
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
