# E2R Stock-Web v12 Residual Research — R11 Loop 89 / L1 / C02

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 89
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_CABLE_EXPORT_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_NUCLEAR_POWER_POLICY_THEME_DECAY
sector: industrials / infra / power grid / datacenter capex / cable / switchgear / power equipment
output_file: e2r_stock_web_v12_residual_round_R11_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 89`.

```text
scheduled_round = R11
scheduled_loop = 89
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

R11 is the L1 policy / infra / defense / grid-link lane.  
C02 is selected because the recent R11 cycle walked through C02 → C03 → C04 → C05, and after R11 loop88 C05 the L1 rotation returns to the power-grid / datacenter CAPEX bucket.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C02_POWER_GRID_DATACENTER_CAPEX
rows = 22
symbols = 12
good/bad Stage2 = 11/4
4B/4C = 2/0
top-covered = 000500, 006340, 033100, 001440, 017040, 189860
```

This loop avoids the C02 top-covered symbols and recent L1 loop symbols:

```text
R11 loop85 C02: 267260, 010120, 103590
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R1 loop88 C02: 298040, 388050, 147830
R1 loop89 C03: 064350, 099320, 214430
```

Candidate hygiene note:

```text
A R10/C30 construction-materials candidate sweep and a R9/C29 auto-parts sweep were accidentally touched during source lookup.
Those candidates are not used in this R11/C02 output.
```

Selected symbols:

```text
229640, 199820, 006910
```

The selected pocket is:

```text
power cable export / grid CAPEX / datacenter power-infra bridge
vs
switchgear theme spike after corporate-action candidates without confirmed datacenter CAPEX order/margin bridge
vs
power/nuclear policy equipment rebound without grid CAPEX backlog and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"229640","company_name":"LS에코에너지","profile_path":"atlas/symbol_profiles/229/229640.json","first_date":"2016-09-22","last_date":"2026-02-20","trading_day_count":2309,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Name changed from LS전선아시아 to LS에코에너지 before selected 2024 window, but 2024 price path is clean.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"199820","company_name":"제일일렉트릭","profile_path":"atlas/symbol_profiles/199/199820.json","first_date":"2020-11-26","last_date":"2026-02-20","trading_day_count":1282,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2024-05-21","2024-06-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024 corporate-action candidates exist before the selected September entry; the row is kept as post-candidate data-quality-watch counterexample.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-06-11_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"006910","company_name":"보성파워텍","profile_path":"atlas/symbol_profiles/006/006910.json","first_date":"1996-07-24","last_date":"2026-02-20","trading_day_count":6673,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1997-05-26","1999-06-24","2000-03-28","2000-07-31","2000-12-22","2009-06-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"229640","trigger_type":"Stage2-Actionable-PowerCableExportGridCapexBridge-Positive","entry_date":"2024-04-22","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered and recent L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"199820","trigger_type":"Stage2-FalsePositive-SwitchgearThemeSpike-NoDatacenterCapexOrderMarginBridge","entry_date":"2024-09-20","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered and recent L1 loop symbols; selected after 2024 corporate-action candidates"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"006910","trigger_type":"Stage2-FalsePositive-PowerNuclearPolicyTheme-NoGridCapexBacklogCashBridge","entry_date":"2024-02-22","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered and recent L1 loop symbols; note symbol is known in C04 but hard duplicate is canonical-specific"}
```

## 4. Research question

C02 is not “전력·전선 테마가 움직였다.”  
The useful grid/datacenter CAPEX signal must prove a chain from macro capex to company economics:

```text
grid orderbook
datacenter or utility customer quality
export cable demand
delivery schedule
capacity expansion
margin mix
working-capital discipline
cash conversion
```

A cable or switchgear theme without that bridge is like current with no closed circuit. The voltage is visible, but no work is being done.

Residual question:

```text
Can C02 distinguish:
1. power cable / grid CAPEX export bridge with very high MFE and tolerable early MAE,
2. switchgear theme spike where post-corporate-action price action lacks datacenter order and margin bridge,
3. power/nuclear policy equipment rebound where local MFE is not a grid CAPEX backlog and cash bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C02_R11L89_229640_LS_ECO_POWER_CABLE_EXPORT_GRID_CAPEX","symbol":"229640","company_name":"LS에코에너지","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_EXPORT_GRID_CAPEX_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PowerCableExportGridCapexBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_orderbook_export_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Power cable / export grid CAPEX proxy produced very high MFE with tolerable early MAE. Green still requires exact customer/orderbook/delivery/margin evidence."}
{"row_type":"case","case_id":"C02_R11L89_199820_CHEIL_SWITCHGEAR_THEME","symbol":"199820","company_name":"제일일렉트릭","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_THEME_SPIKE_WITHOUT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SwitchgearThemeSpike-NoDatacenterCapexOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_local_MFE_post_candidate_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_switchgear_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Post-candidate switchgear theme spike had only local price MFE and later drawdown without exact datacenter/customer order, delivery, margin or cash bridge."}
{"row_type":"case","case_id":"C02_R11L89_006910_BOSUNG_POWER_POLICY_THEME","symbol":"006910","company_name":"보성파워텍","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_NUCLEAR_POLICY_THEME_WITHOUT_GRID_CAPEX_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PowerNuclearPolicyTheme-NoGridCapexBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_MFE_deep_MAE_no_grid_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_power_policy_rebound_counted_as_C02_bridge","price_source":"Songdaiki/stock-web","notes":"Power/nuclear policy equipment rebound generated local MFE but lacked grid CAPEX backlog, customer delivery and margin/cash bridge; later MAE expansion makes it a Watch/4B row."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 229640 LS에코에너지 — power cable export / grid CAPEX bridge positive

Entry row: `2024-04-22 c=19600`.  
Observed path: early low `2024-04-24 l=18680`, high `2024-05-30 h=45300`, and late low `2024-11-15 l=22450`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L89_C02_229640_20240422_STAGE2_POWER_CABLE_EXPORT_GRID","case_id":"C02_R11L89_229640_LS_ECO_POWER_CABLE_EXPORT_GRID_CAPEX","symbol":"229640","company_name":"LS에코에너지","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_EXPORT_GRID_CAPEX_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PowerCableExportGridCapexBridge-Positive","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":19600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_power_cable_export_grid_capex_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; export cable/grid capex, delivery schedule and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["grid_capex_proxy","export_cable_demand_proxy","delivery_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_orderbook_pending","capacity_expansion_pending","margin_mix_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/229/229640/2024.csv","profile_path":"atlas/symbol_profiles/229/229640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":127.04,"MFE_90D_pct":131.12,"MFE_180D_pct":131.12,"MAE_30D_pct":-4.69,"MAE_90D_pct":-4.69,"MAE_180D_pct":-4.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-30","peak_price":45300.0,"max_drawdown_low_date":"2024-04-24","max_drawdown_low":18680.0,"drawdown_after_peak_pct":-50.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_orderbook_delivery_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_orderbook_export_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"229640_2024-04-22_19600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 can allow Stage2/Yellow when grid strength is tied to export cable demand, orderbook, delivery schedule, margin mix and cash conversion. Green requires exact source-grade evidence."}
```

### 6.2 199820 제일일렉트릭 — switchgear theme spike without datacenter CAPEX order/margin bridge

Entry row: `2024-09-20 c=9870`, selected after 2024 corporate-action candidates.  
Observed path: high `2024-09-27 h=11000`, later low `2024-12-09 l=7860`, and separate late spikes that should not validate missing non-price bridge.

```jsonl
{"row_type":"trigger","trigger_id":"R11L89_C02_199820_20240920_STAGE2_FALSE_POSITIVE_SWITCHGEAR_THEME","case_id":"C02_R11L89_199820_CHEIL_SWITCHGEAR_THEME","symbol":"199820","company_name":"제일일렉트릭","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_THEME_SPIKE_WITHOUT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch","trigger_type":"Stage2-FalsePositive-SwitchgearThemeSpike-NoDatacenterCapexOrderMarginBridge","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":9870.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_switchgear_datacenter_power_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; switchgear/datacenter power theme treated as insufficient without confirmed customer order, delivery schedule, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["switchgear_theme","datacenter_power_keyword","relative_strength_spike"],"stage3_evidence_fields":["confirmed_datacenter_order_missing","delivery_schedule_missing","margin_cash_bridge_missing","customer_quality_missing"],"stage4b_evidence_fields":["price_only_local_MFE","data_quality_watch","order_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/199/199820/2024.csv","profile_path":"atlas/symbol_profiles/199/199820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.45,"MFE_90D_pct":20.97,"MFE_180D_pct":20.97,"MAE_30D_pct":-8.51,"MAE_90D_pct":-20.36,"MAE_180D_pct":-20.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-14","peak_price":11940.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":7860.0,"drawdown_after_peak_pct":-34.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"switchgear_theme_without_confirmed_datacenter_order_margin_bridge_should_remain_4B_watch; data_quality_watch_due_to_2024_candidates","four_b_evidence_type":["price_only","data_quality_watch","order_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_post_candidate_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_switchgear_theme_overcredited","calibration_usable":true,"forward_window_trading_days":"partial_post_candidate_2024_window","calibration_block_reasons":["data_quality_watch_due_to_2024-05-21_and_2024-06-11_candidates"],"corporate_action_window_status":"selected_entry_after_2024-06-11_candidate","same_entry_group_id":"199820_2024-09-20_9870","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not promote switchgear theme strength without confirmed datacenter or grid customer order, delivery schedule, margin and cash bridge. Data-quality watch remains before any patch."}
```

### 6.3 006910 보성파워텍 — power/nuclear policy theme without grid CAPEX backlog/cash bridge

Entry row: `2024-02-22 c=3275`.  
Observed path: local high `2024-02-22 h=3430`, later policy high `2024-04-08 h=3285`, and low `2024-12-09 l=2290`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L89_C02_006910_20240222_STAGE2_FALSE_POSITIVE_POWER_POLICY","case_id":"C02_R11L89_006910_BOSUNG_POWER_POLICY_THEME","symbol":"006910","company_name":"보성파워텍","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_NUCLEAR_POLICY_THEME_WITHOUT_GRID_CAPEX_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_policy_spike_stress_test","trigger_type":"Stage2-FalsePositive-PowerNuclearPolicyTheme-NoGridCapexBacklogCashBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":3275.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_power_nuclear_policy_equipment_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; power/nuclear policy equipment rebound treated as insufficient for C02 without grid/datacenter capex backlog, delivery schedule, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["power_policy_theme","nuclear_equipment_keyword","relative_strength_spike"],"stage3_evidence_fields":["grid_capex_orderbook_missing","datacenter_customer_bridge_missing","margin_cash_bridge_missing","delivery_schedule_missing"],"stage4b_evidence_fields":["price_only_local_MFE","policy_theme_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv","profile_path":"atlas/symbol_profiles/006/006910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.73,"MFE_90D_pct":4.73,"MFE_180D_pct":6.72,"MAE_30D_pct":-11.45,"MAE_90D_pct":-12.82,"MAE_180D_pct":-13.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-22","peak_price":3495.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2290.0,"drawdown_after_peak_pct":-34.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"power_policy_theme_without_grid_datacenter_backlog_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","policy_theme_watch","grid_backlog_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_MFE_deep_MAE_no_grid_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_power_policy_rebound_counted_as_C02_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006910_2024-02-22_3275","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not count generic power/nuclear policy MFE as grid/datacenter CAPEX evidence. Orderbook, customer quality, delivery, margin and cash bridge must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R11L89_229640_LS_ECO_POWER_CABLE_EXPORT_GRID_CAPEX","trigger_id":"R11L89_C02_229640_20240422_STAGE2_POWER_CABLE_EXPORT_GRID","symbol":"229640","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C02 requires grid/datacenter orderbook, export cable demand, delivery schedule, margin and cash bridge rather than power-grid theme alone","raw_component_scores_before":{"grid_capex_score":15,"datacenter_customer_score":10,"export_orderbook_score":14,"delivery_schedule_score":12,"capacity_expansion_score":11,"margin_mix_score":10,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"grid_capex_score":18,"datacenter_customer_score":12,"export_orderbook_score":17,"delivery_schedule_score":15,"capacity_expansion_score":13,"margin_mix_score":12,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Power cable/export grid CAPEX bridge plus very high MFE supports Yellow/Green-candidate watch; exact orderbook, delivery, margin and cash evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R11L89_199820_CHEIL_SWITCHGEAR_THEME","trigger_id":"R11L89_C02_199820_20240920_STAGE2_FALSE_POSITIVE_SWITCHGEAR_THEME","symbol":"199820","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"switchgear theme without confirmed datacenter/grid order and margin bridge should be blocked or kept data-quality watch","raw_component_scores_before":{"grid_capex_score":4,"datacenter_customer_score":3,"export_orderbook_score":0,"delivery_schedule_score":0,"capacity_expansion_score":1,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"grid_capex_score":1,"datacenter_customer_score":0,"export_orderbook_score":0,"delivery_schedule_score":0,"capacity_expansion_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Local MFE is not enough when datacenter/grid order, delivery and margin bridge are missing and 2024 candidate watch remains."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R11L89_006910_BOSUNG_POWER_POLICY_THEME","trigger_id":"R11L89_C02_006910_20240222_STAGE2_FALSE_POSITIVE_POWER_POLICY","symbol":"006910","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"power/nuclear policy theme without grid/datacenter backlog and cash bridge should remain Watch/4B","raw_component_scores_before":{"grid_capex_score":2,"datacenter_customer_score":0,"export_orderbook_score":0,"delivery_schedule_score":0,"capacity_expansion_score":1,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":7,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"grid_capex_score":0,"datacenter_customer_score":0,"export_orderbook_score":0,"delivery_schedule_score":0,"capacity_expansion_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Small local MFE and missing orderbook/margin/cash bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L89_C02_P0_CURRENT","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C02 needs explicit grid/datacenter orderbook, export cable demand, delivery, capacity, margin and cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":52.27,"avg_MAE90_pct":-12.62,"avg_MFE180_pct":52.94,"avg_MAE180_pct":-12.78,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":0.67,"score_return_alignment_verdict":"mixed_without_C02_orderbook_delivery_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L89_C02_P1_SECTOR_SPECIFIC","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P1_L1_grid_datacenter_orderbook_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 grid/datacenter signals need utility/datacenter customer quality, export orderbook, delivery schedule, capacity expansion, margin or cash conversion before Stage2-Actionable","changed_axes":["grid_datacenter_customer_required","orderbook_delivery_required","power_policy_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_orderbook_delivery_capacity_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":52.27,"avg_MAE90_pct":-12.62,"avg_MFE180_pct":52.94,"avg_MAE180_pct":-12.78,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L89_C02_P2_CANONICAL","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P2_C02_grid_orderbook_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C02 should reward orderbook-to-margin mechanics, not power/switchgear policy labels","changed_axes":["C02_grid_orderbook_delivery_margin_bridge_required","C02_switchgear_power_policy_local_4B_guard","C02_data_quality_watch_for_2024_candidates"],"changed_thresholds":{"stage2_yellow_gate":"grid_or_datacenter_customer_plus_orderbook_or_delivery_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":52.27,"avg_MAE90_pct":-12.62,"avg_MFE180_pct":52.94,"avg_MAE180_pct":-12.78,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L89_C02_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P3_C02_missing_bridge_policy_theme_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If bridge is missing, policy/switchgear theme MFE cannot validate Stage2/Yellow; if data-quality watch exists, block promotion before exact repair","changed_axes":["C02_price_only_MFE_guardrail","C02_policy_theme_guardrail","C02_data_quality_pre_patch_guard"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_or_data_quality_watch"},"eligible_trigger_count":3,"avg_MFE90_pct":52.27,"avg_MAE90_pct":-12.62,"avg_MFE180_pct":52.94,"avg_MAE180_pct":-12.78,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_POWER_CABLE_EXPORT_POSITIVE_VS_SWITCHGEAR_POLICY_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":52.27,"avg_MAE90_pct":-12.62,"avg_MFE180_pct":52.94,"avg_MAE180_pct":-12.78,"stage2_hit_rate_MFE90_ge_20":2,"stage2_bad_entry_rate_bridge_missing":0.67,"data_quality_watch_count":1,"interpretation":"C02 needs bridge discipline. LS에코에너지 shows export cable/grid CAPEX bridge can produce very high MFE, while 제일일렉트릭 and 보성파워텍 show switchgear/power-policy theme MFE should not be promoted without confirmed customer orderbook, delivery schedule, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"229640","trigger_type":"Stage2-Actionable-PowerCableExportGridCapexBridge-Positive","entry_date":"2024-04-22","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_grid_capex_rerating_with_late_drawdown_watch","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export cable/grid CAPEX is tied to orderbook, delivery, margin and cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"199820","trigger_type":"Stage2-FalsePositive-SwitchgearThemeSpike-NoDatacenterCapexOrderMarginBridge","entry_date":"2024-09-20","stage2_to_90D_outcome":"price_only_local_MFE_data_quality_watch","stage2_to_180D_outcome":"post_candidate_watch_deep_MAE","MFE90_ge_20":true,"MAE90_le_minus_20":true,"transition_note":"Switchgear theme MFE without confirmed datacenter/grid order and margin bridge should remain Watch/4B and data-quality-watch."}
{"row_type":"stage_transition_summary","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"006910","trigger_type":"Stage2-FalsePositive-PowerNuclearPolicyTheme-NoGridCapexBacklogCashBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_power_policy_theme_no_grid_backlog","MFE90_ge_20":false,"MAE180_le_minus_20":false,"transition_note":"Generic power/nuclear policy theme without grid/datacenter backlog and cash bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_type":"switchgear_power_policy_theme_overcredit_without_grid_orderbook_delivery_margin_cash_bridge","contribution":"Adds two C02 local 4B/Watch counterexamples against one power-cable export/grid CAPEX positive, avoiding C02 top-covered and recent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_EXPORT_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_NUCLEAR_POWER_POLICY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C02 now has a non-top-symbol power-cable export/grid CAPEX positive and two switchgear/power-policy weak-bridge counterexamples; next L1 loops should exact-URL repair orderbook, delivery schedule, datacenter/utility customer quality, margin mix and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_grid_orderbook_delivery_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"229640 worked when export cable/grid CAPEX proxy existed; 199820 and 006910 were weak when non-price orderbook/delivery/margin bridge was missing."}
{"row_type":"shadow_weight","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_switchgear_power_policy_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Switchgear and generic power-policy rows showed price-only MFE without sufficient C02 bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_data_quality_watch_for_2024_candidates","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"199820 has 2024 corporate-action candidates before selected entry and should stay data-quality-watch before patch consideration."}
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
  - switchgear_theme_overcredit
  - power_policy_theme_overcredit
  - grid_orderbook_bridge_missing
  - delivery_margin_cash_bridge_missing
new_axis_proposed:
  - C02_grid_orderbook_delivery_margin_bridge_required_shadow_only
  - C02_switchgear_power_policy_local_4B_watch_guard_shadow_only
  - C02_data_quality_watch_for_2024_candidates_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C02
  - full_4b_requires_non_price_evidence within C02
  - hard_4c_thesis_break_routes_to_4c within C02
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
`199820` is selected after 2024 corporate-action candidates and is usable as a weak-bridge / data-quality-watch counterexample, but must be exact-repaired before any production patch.  
The non-price evidence layer remains source-name/proxy level.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 199820
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
3. Confirm R11 / L1 / C02 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C02 top-covered symbols
   - previous R11 loop85 C02 symbols
   - previous R11 loop86 C03 symbols
   - previous R11 loop87 C04 symbols
   - previous R11 loop88 C05 symbols
   - previous R1 loop88 C02 symbols
   - previous R1 loop89 C03 symbols
6. Confirm accidentally touched R10/C30 and R9/C29 candidate rows are not ingested from this MD.
7. Keep 199820 in data-quality watch because of 2024-05-21 and 2024-06-11 candidate dates.
8. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C02-scoped safe patch candidates:
   - C02_grid_orderbook_delivery_margin_bridge_required
   - C02_switchgear_power_policy_local_4B_watch_guard
   - C02_data_quality_watch_for_2024_candidates
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 89
next_round = R12
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
```
