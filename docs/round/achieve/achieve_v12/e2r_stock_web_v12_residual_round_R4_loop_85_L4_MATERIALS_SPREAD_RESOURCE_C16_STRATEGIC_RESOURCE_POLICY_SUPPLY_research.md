# E2R Stock-Web v12 Residual Research — R4 Loop 85 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 85
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_ELECTRIFICATION_RESOURCE_SUPPLY_BRIDGE_VS_SMALLCAP_POLICY_THEME_SPIKE
sector: materials / strategic resource / copper / policy supply
output_file: e2r_stock_web_v12_residual_round_R4_loop_85_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 85`.

```text
scheduled_round = R4
scheduled_loop = 85
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

R4 is restricted to L4 materials / spread / resource.  
C16 is selected because it is the strategic resource and policy-supply bucket. The No-Repeat Index shows C16 already has broad rows, but the remaining useful gap is still the distinction between **real resource supply-chain bridge** and **small-cap copper/theme spike**.

The selected symbols avoid the C16 top-covered list:

```text
047400, 005490, 012320, 001570, 081150, 101670
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"006260","company_name":"LS","profile_path":"atlas/symbol_profiles/006/006260.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7765,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-04","1996-12-04","1999-06-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"025820","company_name":"이구산업","profile_path":"atlas/symbol_profiles/025/025820.json","first_date":"1995-09-12","last_date":"2026-02-20","trading_day_count":7558,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-03","2007-04-30","2007-07-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"021050","company_name":"서원","profile_path":"atlas/symbol_profiles/021/021050.json","first_date":"1996-01-30","last_date":"2026-02-20","trading_day_count":7529,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1996-12-24","1997-09-25","2008-04-16","2016-06-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"006260","trigger_type":"Stage2-Actionable-CopperElectrificationSupplyBridge-Positive","entry_date":"2024-04-11","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"025820","trigger_type":"Stage2-FalsePositive-SmallcapCopperPolicyTheme-NoSupplyBridge","entry_date":"2024-05-20","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"021050","trigger_type":"Stage2-FalsePositive-CopperThemeSpike-NoResourceSupplyBridge","entry_date":"2024-05-20","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C16 should not read every copper or resource-price spike as strategic supply power. In this archetype, the real bridge is resource exposure plus downstream demand, supply bottleneck, margin capture, customer quality, balance-sheet capacity, and policy durability. Without that bridge, the copper theme behaves like a flare: bright, fast, and gone.

Residual question:

```text
Can C16 distinguish:
1. strategic resource/electrification supply bridge with high MFE and tolerable early MAE,
2. small-cap copper theme extension with no durable supply/margin bridge,
3. copper-policy theme spike where price goes first and non-price bridge never catches up?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C16_R4L85_006260_LS_COPPER_ELECTRIFICATION_SUPPLY_BRIDGE","symbol":"006260","company_name":"LS","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ELECTRIFICATION_RESOURCE_SUPPLY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CopperElectrificationSupplyBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE_with_later_drawdown","current_profile_verdict":"current_profile_correct_if_supply_bridge_required","price_source":"Songdaiki/stock-web","notes":"Copper/electrification supply-chain bridge produced high MFE. Later drawdown means Green still needs exact margin/cash/customer evidence."}
{"row_type":"case","case_id":"C16_R4L85_025820_LEEGU_SMALLCAP_COPPER_THEME","symbol":"025820","company_name":"이구산업","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"SMALLCAP_COPPER_POLICY_THEME_WITHOUT_SUPPLY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapCopperPolicyTheme-NoSupplyBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_copper_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap copper-policy theme had local peak and severe forward MAE when supply/margin bridge was missing."}
{"row_type":"case","case_id":"C16_R4L85_021050_SEOWON_COPPER_THEME_SPIKE","symbol":"021050","company_name":"서원","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_THEME_SPIKE_WITHOUT_RESOURCE_SUPPLY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CopperThemeSpike-NoResourceSupplyBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_supply_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Copper theme spike had almost no durable MFE after entry and a deep 180D MAE without resource-supply bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 006260 LS — copper/electrification supply bridge positive

Entry row: `2024-04-11 c=114900`.  
Observed path: local peak `2024-05-21 h=194800`, then later drawdown to `2024-11-18 l=84500`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L85_C16_006260_20240411_STAGE2_COPPER_ELECTRIFICATION_SUPPLY_BRIDGE","case_id":"C16_R4L85_006260_LS_COPPER_ELECTRIFICATION_SUPPLY_BRIDGE","symbol":"006260","company_name":"LS","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ELECTRIFICATION_RESOURCE_SUPPLY_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CopperElectrificationSupplyBridge-Positive","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":114900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_electrification_supply_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper/electrification and supply-chain bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["strategic_resource_policy_tailwind","copper_electrification_supply_bridge_proxy","customer_or_downstream_demand_proxy","relative_strength_turn"],"stage3_evidence_fields":["margin_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":69.54,"MFE_90D_pct":69.54,"MFE_180D_pct":69.54,"MAE_30D_pct":-8.01,"MAE_90D_pct":-8.01,"MAE_180D_pct":-26.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":194800.0,"max_drawdown_low_date":"2024-11-18","max_drawdown_low":84500.0,"drawdown_after_peak_pct":-56.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE_with_later_drawdown","current_profile_verdict":"current_profile_correct_if_supply_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006260_2024-04-11_114900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 can allow Stage2/Yellow when resource-policy strength is tied to downstream demand and supply-chain bridge. Green still requires exact margin, customer and cash-conversion evidence."}
```

### 6.2 025820 이구산업 — small-cap copper-policy theme without supply bridge

Entry row: `2024-05-20 c=7880`.  
Observed path: same-day peak `h=8420`, then lows reached `2024-09-24 l=4175` and `2024-12-09 l=3545`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L85_C16_025820_20240520_STAGE2_FALSE_POSITIVE_SMALLCAP_COPPER_THEME","case_id":"C16_R4L85_025820_LEEGU_SMALLCAP_COPPER_THEME","symbol":"025820","company_name":"이구산업","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"SMALLCAP_COPPER_POLICY_THEME_WITHOUT_SUPPLY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallcapCopperPolicyTheme-NoSupplyBridge","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":7880.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap copper policy/theme spike treated as insufficient without supply, customer, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_policy_theme_spike","relative_strength_extension"],"stage3_evidence_fields":["strategic_supply_bridge_missing","customer_quality_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv","profile_path":"atlas/symbol_profiles/025/025820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.85,"MFE_90D_pct":6.85,"MFE_180D_pct":6.85,"MAE_30D_pct":-32.74,"MAE_90D_pct":-47.02,"MAE_180D_pct":-55.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":8420.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3545.0,"drawdown_after_peak_pct":-57.90,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_copper_theme_peak_without_supply_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_copper_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"025820_2024-05-20_7880","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Copper price/theme spike without strategic supply bridge became a high-MAE false positive. C16 needs a local supply/margin bridge guard."}
```

### 6.3 021050 서원 — copper theme spike without resource-supply bridge

Entry row: `2024-05-20 c=1916`.  
Observed path: local high `2024-05-21 h=2005`, then lows reached `2024-10-25 l=1226` and `2024-12-09 l=993`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L85_C16_021050_20240520_STAGE2_FALSE_POSITIVE_COPPER_THEME_SPIKE","case_id":"C16_R4L85_021050_SEOWON_COPPER_THEME_SPIKE","symbol":"021050","company_name":"서원","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_THEME_SPIKE_WITHOUT_RESOURCE_SUPPLY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-CopperThemeSpike-NoResourceSupplyBridge","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":1916.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper theme spike treated as insufficient without strategic resource supply, margin and customer bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_theme_spike","relative_strength_extension"],"stage3_evidence_fields":["resource_supply_bridge_missing","margin_bridge_missing","customer_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv","profile_path":"atlas/symbol_profiles/021/021050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.65,"MFE_90D_pct":4.65,"MFE_180D_pct":4.65,"MAE_30D_pct":-31.11,"MAE_90D_pct":-33.56,"MAE_180D_pct":-48.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2005.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":993.0,"drawdown_after_peak_pct":-50.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"copper_theme_peak_without_supply_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_supply_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"021050_2024-05-20_1916","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not upgrade copper theme spikes without a supply-chain, margin or customer bridge. Low MFE and deep MAE support Watch/4B-risk routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L85_006260_LS_COPPER_ELECTRIFICATION_SUPPLY_BRIDGE","trigger_id":"R4L85_C16_006260_20240411_STAGE2_COPPER_ELECTRIFICATION_SUPPLY_BRIDGE","symbol":"006260","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C16 requires supply-chain and margin bridge rather than copper price alone","raw_component_scores_before":{"strategic_resource_score":16,"policy_supply_score":13,"customer_or_downstream_demand":12,"margin_bridge_score":11,"capacity_or_asset_quality":11,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"strategic_resource_score":18,"policy_supply_score":15,"customer_or_downstream_demand":14,"margin_bridge_score":13,"capacity_or_asset_quality":13,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Resource-supply and downstream-demand bridge support Yellow-watch; exact customer, margin and cash evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L85_025820_LEEGU_SMALLCAP_COPPER_THEME","trigger_id":"R4L85_C16_025820_20240520_STAGE2_FALSE_POSITIVE_SMALLCAP_COPPER_THEME","symbol":"025820","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap copper theme without supply/margin bridge should be blocked","raw_component_scores_before":{"strategic_resource_score":8,"policy_supply_score":8,"customer_or_downstream_demand":2,"margin_bridge_score":1,"capacity_or_asset_quality":2,"relative_strength_score":15,"valuation_repricing_score":7,"execution_risk_score":-13,"theme_spike_risk":-15,"information_confidence":3},"weighted_score_before":28,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"strategic_resource_score":3,"policy_supply_score":4,"customer_or_downstream_demand":0,"margin_bridge_score":0,"capacity_or_asset_quality":1,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-20,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and severe MAE convert copper theme extension into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L85_021050_SEOWON_COPPER_THEME_SPIKE","trigger_id":"R4L85_C16_021050_20240520_STAGE2_FALSE_POSITIVE_COPPER_THEME_SPIKE","symbol":"021050","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"copper theme spike without direct supply/margin bridge should remain Watch/blocked","raw_component_scores_before":{"strategic_resource_score":7,"policy_supply_score":7,"customer_or_downstream_demand":1,"margin_bridge_score":1,"capacity_or_asset_quality":1,"relative_strength_score":14,"valuation_repricing_score":6,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":25,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"strategic_resource_score":2,"policy_supply_score":3,"customer_or_downstream_demand":0,"margin_bridge_score":0,"capacity_or_asset_quality":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Price moved first; the resource-supply bridge never caught up. High MAE blocks Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L85_C16_P0_CURRENT","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C16 needs explicit strategic supply/margin/customer bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":27.01,"avg_MAE90_pct":-29.53,"avg_MFE180_pct":27.01,"avg_MAE180_pct":-43.21,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C16_supply_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L85_C16_P1_SECTOR_SPECIFIC","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P1_L4_resource_supply_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 strategic resource signals need supply-chain, customer/downstream demand, margin or cash bridge before Stage2-Actionable","changed_axes":["strategic_supply_bridge_required","customer_or_downstream_demand_required","margin_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_supply_customer_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":27.01,"avg_MAE90_pct":-29.53,"avg_MFE180_pct":27.01,"avg_MAE180_pct":-43.21,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L85_C16_P2_CANONICAL","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P2_C16_resource_supply_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C16 should reward strategic resource supply bridge, not copper theme spikes","changed_axes":["C16_supply_chain_bridge_required","C16_copper_theme_spike_penalty","C16_smallcap_policy_theme_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"supply_customer_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":27.01,"avg_MAE90_pct":-29.53,"avg_MFE180_pct":27.01,"avg_MAE180_pct":-43.21,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L85_C16_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P3_C16_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-30 while supply/margin bridge is missing, block Yellow/Green","changed_axes":["C16_high_MAE_guardrail","C16_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":27.01,"avg_MAE90_pct":-29.53,"avg_MFE180_pct":27.01,"avg_MAE180_pct":-43.21,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_COPPER_SUPPLY_BRIDGE_VS_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":27.01,"avg_MAE90_pct":-29.53,"avg_MFE180_pct":27.01,"avg_MAE180_pct":-43.21,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_30":0.67,"interpretation":"C16 needs bridge discipline. LS shows a valid copper/electrification supply-chain bridge, while 이구산업 and 서원 show small-cap copper theme spikes that fail without supply, customer and margin conversion."}
{"row_type":"stage_transition_summary","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"006260","trigger_type":"Stage2-Actionable-CopperElectrificationSupplyBridge-Positive","entry_date":"2024-04-11","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_supply_bridge_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when strategic supply and downstream-demand bridge exists; Green requires exact margin/customer/cash evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"025820","trigger_type":"Stage2-FalsePositive-SmallcapCopperPolicyTheme-NoSupplyBridge","entry_date":"2024-05-20","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_copper_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Small-cap copper theme without supply/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"021050","trigger_type":"Stage2-FalsePositive-CopperThemeSpike-NoResourceSupplyBridge","entry_date":"2024-05-20","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_theme_spike_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Copper theme spike without resource-supply bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"strategic_resource_policy_theme_overcredit_without_supply_customer_margin_bridge","contribution":"Adds two C16 local 4B/high-MAE counterexamples against one strategic supply bridge positive, avoiding C16 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ELECTRIFICATION_RESOURCE_SUPPLY_BRIDGE_VS_SMALLCAP_POLICY_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C16 now has non-top-symbol copper-theme counterexamples; next R4 loops should exact-URL repair supply-chain, customer demand, margin and cash conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_supply_customer_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"006260 worked with supply-chain/downstream-demand bridge proxy; 025820 and 021050 failed when copper theme lacked supply, customer and margin conversion."}
{"row_type":"shadow_weight","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_copper_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small-cap copper theme spikes showed low MFE and severe MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"85","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-30 while supply/customer/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - strategic_resource_theme_overcredit
  - smallcap_copper_theme_no_supply_bridge
  - resource_policy_spike_no_margin_customer_bridge
new_axis_proposed:
  - C16_supply_customer_margin_bridge_required_shadow_only
  - C16_copper_theme_local_4B_watch_guard_shadow_only
  - C16_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C16
  - full_4b_requires_non_price_evidence within C16
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
3. Confirm R4 / L4 / C16 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C16 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C16-scoped safe patch candidates:
   - C16_supply_customer_margin_bridge_required
   - C16_copper_theme_local_4B_watch_guard
   - C16_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 85
next_round = R5
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
```
