# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2
deep_sub_archetype_id: C08_DEEP_TEST_SOCKET_PROBE_CARD_CERAMIC_STF_INSPECTION_QUALITY_REPEAT_DEMAND_VS_LABEL_SPIKE
loop_objective: quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 7 new independent cases, 3 counterexamples, and 6 residual errors for R2/L2/C08.

## 1. Current Calibrated Profile Assumption

Current default proxy is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are kept as baseline assumptions: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, and `hard_4c_thesis_break_routes_to_4c=true`.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R2`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`
- fine_archetype_id: `C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2`
- scope rule: C06~C10 map to R2 / L2, so the round-sector pair is valid.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index says C08 has 50 representative rows, 43 symbols, positives/counter `0/0`, 4B/4C `0/0`, and top covered C08 symbols include `058470`, `067310`, `092870`, `095340`, `131970`, and `232140`. This loop avoids the visible C08 loop110 symbol set and uses seven C08-focused symbols not used in that local loop: `131290`, `098120`, `425420`, `253590`, `252990`, `064290`, `098460`.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_repo_url = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Stock-Web manifest confirms `raw_unadjusted_marcap`, `tradable_raw`, max date `2026-02-20`, and calibration-safe tradable shards. All trigger rows below use 2024 tradable shards and have 180 trading-day windows inside the downloaded year shard.

## 5. Historical Eligibility Gate

- trigger dates are historical and before stock-web max date.
- entry dates exist in the tradable shards.
- each trigger has 30D/90D/180D MFE and MAE.
- forward_window_trading_days = 180 for every trigger.
- corporate_action_window_status = clean_180D_window by profile review; candidate split/discontinuity dates, where present, are outside each row's 180D window.
- evidence rows are source-proxy and therefore promotion-blocked until URL repair, but price-path validation is usable.

## 6. Canonical Archetype Compression Map

| fine/deep route | canonical compression | why |
|---|---|---|
| probe card / test interface / socket repeat demand | C08 | customer quality and repeat test demand decide whether RS converts into rerating |
| ceramic STF / probe-card substrate | C08 | substrate quality is useful only if tied to customer acceptance/repeat demand |
| inspection/metrology label spike | C08 | quality-inspection routes belong here when test/customer-quality is the claimed bridge |
| CXL/SSD tester proxy | C08 boundary with C10 | accepted only as C08 when customer-quality/test demand is the evidence family; otherwise C10 |

## 7. Case Selection Summary

|symbol|company|entry_date|entry_price|trigger_type|role|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|131290|티에스이|2024-02-01|43500|Stage2-Actionable|positive|101.84|-2.53|101.84|-12.53|current_profile_missed_structural|
|253590|네오셈|2024-01-02|9300|Stage2-Actionable|positive|84.41|-17.63|85.7|-20.22|current_profile_correct|
|252990|샘씨엔에스|2024-01-02|5800|Stage2|positive|60.0|-6.9|60.0|-18.1|current_profile_too_late|
|098460|고영|2024-01-02|17370|Stage2|positive|38.46|-12.2|38.46|-45.77|current_profile_4B_too_late|
|098120|마이크로컨텍솔|2024-01-02|14790|Stage4B|counterexample|0.41|-40.16|0.41|-66.43|current_profile_false_positive|
|425420|티에프이|2024-01-02|37100|Stage4B|counterexample|18.46|-23.58|18.46|-60.94|current_profile_false_positive|
|064290|인텍플러스|2024-03-04|40200|Stage4B|counterexample|1.74|-47.76|1.74|-77.06|current_profile_4B_too_late|

## 8. Positive vs Counterexample Balance

- positive_case_count: 4
- counterexample_count: 3
- stage4b_case_count: 3
- stage4c_case_count: 0
- current_profile_error_count: 6

The useful split is not “test socket good / bad” but **verified customer-quality repeat demand vs label-only local overheat**. TSE, Neosem, SamCNS, and Koh Young show positive or high-MFE routes. Micro Contact Solution, TFE, and Intekplus show how the same label can become a high-MAE false positive when the non-price bridge is missing.

## 9. Evidence Source Map

All evidence fields are deliberately marked `source_proxy_only__url_repair_required`. This MD is still useful for price-path and residual-rule mining, but any future promotion should repair evidence URLs before production use.

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|entry_date|forward_window_trading_days|
|---|---|---|---|---|---|
|131290|티에스이|atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv|atlas/symbol_profiles/131/131290.json|2024-02-01|180|
|253590|네오셈|atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv|atlas/symbol_profiles/253/253590.json|2024-01-02|180|
|252990|샘씨엔에스|atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv|atlas/symbol_profiles/252/252990.json|2024-01-02|180|
|098460|고영|atlas/ohlcv_tradable_by_symbol_year/098/098460/2024.csv|atlas/symbol_profiles/098/098460.json|2024-01-02|180|
|098120|마이크로컨텍솔|atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv|atlas/symbol_profiles/098/098120.json|2024-01-02|180|
|425420|티에프이|atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv|atlas/symbol_profiles/425/425420.json|2024-01-02|180|
|064290|인텍플러스|atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv|atlas/symbol_profiles/064/064290.json|2024-03-04|180|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_C08_R2L111_131290_Stage2Actionable_20240201|131290|티에스이|Stage2-Actionable|2024-02-01|43500.0|45.29|101.84|101.84|-2.53|-2.53|-12.53|2024-05-03|87800.0|-56.66|current_profile_missed_structural|
|TRG_C08_R2L111_253590_Stage2Actionable_20240102|253590|네오셈|Stage2-Actionable|2024-01-02|9300.0|61.08|84.41|85.7|-17.63|-17.63|-20.22|2024-07-04|17270.0|-57.04|current_profile_correct|
|TRG_C08_R2L111_252990_Stage2_20240102|252990|샘씨엔에스|Stage2|2024-01-02|5800.0|52.41|60.0|60.0|-6.9|-6.9|-18.1|2024-04-18|9280.0|-48.81|current_profile_too_late|
|TRG_C08_R2L111_098460_Stage2_20240102|098460|고영|Stage2|2024-01-02|17370.0|24.93|38.46|38.46|-12.03|-12.2|-45.77|2024-02-23|24050.0|-60.83|current_profile_4B_too_late|
|TRG_C08_R2L111_098120_Stage4B_20240102|098120|마이크로컨텍솔|Stage4B|2024-01-02|14790.0|0.41|0.41|0.41|-29.61|-40.16|-66.43|2024-01-02|14850.0|-66.57|current_profile_false_positive|
|TRG_C08_R2L111_425420_Stage4B_20240102|425420|티에프이|Stage4B|2024-01-02|37100.0|1.08|18.46|18.46|-23.58|-23.58|-60.94|2024-03-21|43950.0|-67.03|current_profile_false_positive|
|TRG_C08_R2L111_064290_Stage4B_20240304|064290|인텍플러스|Stage4B|2024-03-04|40200.0|1.74|1.74|1.74|-15.67|-47.76|-77.06|2024-03-07|40900.0|-77.46|current_profile_4B_too_late|

## 12. Trigger-Level OHLC Backtest Tables

The 180D path shows why C08 needs a bridge-specific split. Positive routes have high 90D/180D upside, but several still suffer late drawdown. Label-only rows often have nearly no MFE and severe MAE. The proper rule is not to loosen C08 globally, but to require customer-quality / repeat-demand evidence before Yellow or Green.

## 13. Current Calibrated Profile Stress Test

- current_profile_correct: 1 case (`253590`)
- current_profile_missed_structural / too_late: 3 cases (`131290`, `252990`, `098460`)
- current_profile_false_positive / 4B_too_late: 3 cases (`098120`, `425420`, `064290`)

Existing global safeguards help, but C08 still needs a canonical distinction between verified customer-quality repeat demand and socket/test/inspection label spikes.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Green label is introduced in this loop. `green_lateness_ratio` is therefore `not_applicable:no_confirmed_Stage3_Green_trigger` for trigger rows. The stress test is Stage2/Yellow eligibility: C08 should not Yellow on price and label alone, but it should not miss verified repeat-demand/customer-quality bridges.

## 15. 4B Local vs Full-window Timing Audit

The three Stage4B rows use price/label local-overheat evidence. They are not full 4B production exits. They are guardrail samples showing that C08 label spikes should be watch overlays until non-price deterioration confirms a full 4B thesis risk.

## 16. 4C Protection Audit

No trigger row is emitted as Stage4C. Several counterexamples have large post-peak drawdown, but without verified non-price thesis break evidence they should remain local 4B / high-MAE guardrail rows, not hard 4C rows.

## 17. Sector-Specific Rule Candidate

`L2_SEMI_TEST_QUALITY_BRIDGE`: in semiconductor electronics, test/socket/inspection rerating should require customer-quality or repeat-demand bridge evidence before Yellow/Green. This is sector-specific because the same price RS often appears across HBM equipment and memory beta routes, but C08 depends more on customer-quality acceptance and repeatability than on one-off CAPEX labels.

## 18. Canonical-Archetype Rule Candidate

`C08_customer_quality_repeat_demand_bridge_required_before_Yellow_or_Green`: verified customer-quality, repeat purchase, customer qualification, or revenue/margin conversion is required before C08 can promote. `C08_label_spike_to_local_4B_watch`: when only a socket/test/inspection label and price RS exist, route to local 4B watch rather than positive Stage3.

## 19. Before / After Backtest Comparison

|profile_id|hypothesis|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|missed_structural_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current global calibrated profile|7|43.62|-21.54|3/7|3|mixed: C08 still confuses label spike with repeat-demand bridge|
|P0b e2r_2_0_baseline_reference|old broad RS-heavy baseline|7|43.62|-21.54|4/7|2|weaker: more price-label false positives|
|P1 sector_specific_candidate_profile|L2 quality bridge + 4B label guard|7|71.18|-9.81|1/7|1|better for L2 semicap quality|
|P2 canonical_C08_candidate_profile|verified customer-quality/repeat-demand bridge before Yellow; label spikes to local 4B watch|7|71.18|-9.81|0-1/7 after URL repair|1|best canonical fit|
|P3 counterexample_guard_profile|proxy/label rows cannot promote; only risk overlay|3|6.87|-37.17|0/3 for counterexample subset|0|strong guardrail|

## 20. Score-Return Alignment Matrix

Positive rows align when `customer_quality_score` and `margin_bridge_score` are supported. Counterexamples align when `valuation_repricing_score` and `execution_risk_score` dominate while customer-quality evidence is only proxy/label-level.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2 | 4 | 3 | 3 | 0 | 7 | 0 | 7 | 7 | 6 | true | true | C08 published index 50 + local loop110 7 + loop111 7 = local-session adjusted about 64; quality repair / positive-balance / 4B audit rather than minimum coverage fill |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: missed_customer_quality_positive, source_proxy_label_false_positive, local_4B_watch_needed_after_test_socket_label_spike
new_axis_proposed: C08_customer_quality_repeat_demand_bridge_required_before_Yellow_or_Green + C08_label_spike_to_local_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: stock-web OHLC path, 30/90/180D MFE/MAE, clean 180D window, canonical/round consistency, novelty against local loop memory. Non-validation scope: live candidate discovery, investment recommendation, production scoring change, repository code patch, current watchlist creation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_repeat_demand_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,Require verified repeat-demand/customer-quality bridge before Yellow or Green,positives retain high MFE while label spikes route to watch,TRG_C08_R2L111_131290_Stage2Actionable_20240201|TRG_C08_R2L111_253590_Stage2Actionable_20240102|TRG_C08_R2L111_252990_Stage2_20240102|TRG_C08_R2L111_098460_Stage2_20240102,7,7,3,medium,canonical_shadow_only,not production; source_proxy rows require URL repair
shadow_weight,C08_label_spike_to_local_4B_watch,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,Price-only socket/test/inspection labels should remain local 4B watch,prevents Microcontactsol/TFE/Intekplus-style high MAE false positives,TRG_C08_R2L111_098120_Stage4B_20240102|TRG_C08_R2L111_425420_Stage4B_20240102|TRG_C08_R2L111_064290_Stage4B_20240304,7,7,3,medium,canonical_shadow_only,not production
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C08_R2L111_131290_20240201","symbol":"131290","company_name":"티에스이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"probe-card/test interface direct positive"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_131290_Stage2Actionable_20240201","case_id":"C08_R2L111_131290_20240201","symbol":"131290","company_name":"티에스이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":43500.0,"evidence_available_at_that_date":"source_proxy: probe-card/test-interface quality bridge; URL repair required before promotion","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","customer_quality_proxy","repeat_demand_bridge_proxy"],"stage3_evidence_fields":["margin_bridge_pending","revision_pending","multiple_public_sources_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.29,"MFE_90D_pct":101.84,"MFE_180D_pct":101.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.53,"MAE_90D_pct":-2.53,"MAE_180D_pct":-12.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-05-03","peak_price":87800.0,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"customer_quality_repeat_demand_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|131290|Stage2-Actionable|2024-02-01|43500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_131290_20240201","trigger_id":"TRG_C08_R2L111_131290_Stage2Actionable_20240201","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":16,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":6,"relative_strength_score":16,"customer_quality_score":23,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":101.84,"MAE_90D_pct":-2.53,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C08_R2L111_253590_20240102","symbol":"253590","company_name":"네오셈","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"tester quality positive"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_253590_Stage2Actionable_20240102","case_id":"C08_R2L111_253590_20240102","symbol":"253590","company_name":"네오셈","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":9300.0,"evidence_available_at_that_date":"source_proxy: enterprise storage/CXL test demand proxy; URL repair required before promotion","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","customer_quality_proxy","repeat_demand_bridge_proxy"],"stage3_evidence_fields":["margin_bridge_pending","revision_pending","multiple_public_sources_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":61.08,"MFE_90D_pct":84.41,"MFE_180D_pct":85.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.63,"MAE_90D_pct":-17.63,"MAE_180D_pct":-20.22,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":17270.0,"drawdown_after_peak_pct":-57.04,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"tester_customer_quality_high_mfe_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|253590|Stage2-Actionable|2024-01-02|9300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_253590_20240102","trigger_id":"TRG_C08_R2L111_253590_Stage2Actionable_20240102","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":16,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":6,"relative_strength_score":16,"customer_quality_score":23,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":84.41,"MAE_90D_pct":-17.63,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C08_R2L111_252990_20240102","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"ceramic substrate positive"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_252990_Stage2_20240102","case_id":"C08_R2L111_252990_20240102","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":5800.0,"evidence_available_at_that_date":"source_proxy: probe-card ceramic STF repeat-demand proxy; URL repair required before promotion","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","customer_quality_proxy","repeat_demand_bridge_proxy"],"stage3_evidence_fields":["margin_bridge_pending","revision_pending","multiple_public_sources_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv","profile_path":"atlas/symbol_profiles/252/252990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":52.41,"MFE_90D_pct":60.0,"MFE_180D_pct":60.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.9,"MAE_90D_pct":-6.9,"MAE_180D_pct":-18.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-18","peak_price":9280.0,"drawdown_after_peak_pct":-48.81,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ceramic_stf_probe_substrate_positive_with_later_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|252990|Stage2|2024-01-02|5800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_252990_20240102","trigger_id":"TRG_C08_R2L111_252990_Stage2_20240102","symbol":"252990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":16,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":6,"relative_strength_score":16,"customer_quality_score":23,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":60.0,"MAE_90D_pct":-6.9,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C08_R2L111_098460_20240102","symbol":"098460","company_name":"고영","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"inspection positive with 4B watch"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_098460_Stage2_20240102","case_id":"C08_R2L111_098460_20240102","symbol":"098460","company_name":"고영","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":17370.0,"evidence_available_at_that_date":"source_proxy: SMT/inspection quality and AI inspection label; URL repair required before promotion","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","customer_quality_proxy","repeat_demand_bridge_proxy"],"stage3_evidence_fields":["margin_bridge_pending","revision_pending","multiple_public_sources_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098460/2024.csv","profile_path":"atlas/symbol_profiles/098/098460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.93,"MFE_90D_pct":38.46,"MFE_180D_pct":38.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.03,"MAE_90D_pct":-12.2,"MAE_180D_pct":-45.77,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":24050.0,"drawdown_after_peak_pct":-60.83,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"inspection_quality_positive_but_needs_4B_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|098460|Stage2|2024-01-02|17370","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_098460_20240102","trigger_id":"TRG_C08_R2L111_098460_Stage2_20240102","symbol":"098460","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":16,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":6,"relative_strength_score":16,"customer_quality_score":23,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":38.46,"MAE_90D_pct":-12.2,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C08_R2L111_098120_20240102","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"socket label counterexample"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_098120_Stage4B_20240102","case_id":"C08_R2L111_098120_20240102","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":14790.0,"evidence_available_at_that_date":"source_proxy: test-socket label spike without visible customer/revision bridge; URL repair required","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","theme_label_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","missing_customer_quality_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv","profile_path":"atlas/symbol_profiles/098/098120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.41,"MFE_90D_pct":0.41,"MFE_180D_pct":0.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-29.61,"MAE_90D_pct":-40.16,"MAE_180D_pct":-66.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":14850.0,"drawdown_after_peak_pct":-66.57,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_or_label_peak_should_remain_local_4B_watch","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"socket_label_price_only_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|098120|Stage4B|2024-01-02|14790","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_098120_20240102","trigger_id":"TRG_C08_R2L111_098120_Stage4B_20240102","symbol":"098120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":18,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":23,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":0.41,"MAE_90D_pct":-40.16,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C08_R2L111_425420_20240102","symbol":"425420","company_name":"티에프이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"newly listed socket counterexample"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_425420_Stage4B_20240102","case_id":"C08_R2L111_425420_20240102","symbol":"425420","company_name":"티에프이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":37100.0,"evidence_available_at_that_date":"source_proxy: socket/test fixture label spike without confirmed repeat demand bridge; URL repair required","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","theme_label_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","missing_customer_quality_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.08,"MFE_90D_pct":18.46,"MFE_180D_pct":18.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.58,"MAE_90D_pct":-23.58,"MAE_180D_pct":-60.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43950.0,"drawdown_after_peak_pct":-67.03,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.35,"four_b_timing_verdict":"price_only_or_label_peak_should_remain_local_4B_watch","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"newly_listed_socket_label_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|425420|Stage4B|2024-01-02|37100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_425420_20240102","trigger_id":"TRG_C08_R2L111_425420_Stage4B_20240102","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":18,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":23,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":18.46,"MAE_90D_pct":-23.58,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C08_R2L111_064290_20240304","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"inspection/metrology 4B counterexample"}
{"row_type":"trigger","trigger_id":"TRG_C08_R2L111_064290_Stage4B_20240304","case_id":"C08_R2L111_064290_20240304","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_PROBE_CARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V2","sector":"semiconductor_test_socket_quality","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":40200.0,"evidence_available_at_that_date":"source_proxy: inspection/metrology label local peak without order/revenue bridge; URL repair required","evidence_source":"source_proxy_only__url_repair_required","stage2_evidence_fields":["relative_strength","theme_label_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","missing_customer_quality_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.74,"MFE_90D_pct":1.74,"MFE_180D_pct":1.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.67,"MAE_90D_pct":-47.76,"MAE_180D_pct":-77.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":40900.0,"drawdown_after_peak_pct":-77.46,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_or_label_peak_should_remain_local_4B_watch","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"inspection_label_local_peak_4B_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08|064290|Stage4B|2024-03-04|40200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L111_064290_20240304","trigger_id":"TRG_C08_R2L111_064290_Stage4B_20240304","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":18,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":23,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile raises verified customer-quality/repeat-demand bridge for positives and routes source-proxy label spikes to local 4B watch.","MFE_90D_pct":1.74,"MAE_90D_pct":-47.76,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["missed_customer_quality_positive","source_proxy_label_false_positive","local_4B_watch_needed_after_test_socket_label_spike"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C22_INSURANCE_RATE_CYCLE_RESERVE, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web raw price shards: `atlas/ohlcv_tradable_by_symbol_year/*/*/2024.csv`

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
