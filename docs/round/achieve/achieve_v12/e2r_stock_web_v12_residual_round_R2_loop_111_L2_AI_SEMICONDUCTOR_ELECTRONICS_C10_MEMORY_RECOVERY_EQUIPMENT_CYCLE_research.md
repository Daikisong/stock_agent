# E2R Stock-Web V12 Residual Research — R2 Loop 111 — C10 MEMORY RECOVERY EQUIPMENT CYCLE

```text
expected_v12_result_file: true
filename_pattern_pass: true
standard_v12_result_filename: e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
current_stock_discovery_allowed: false
```

## 1. Selection Metadata

```text
selected_round: R2
selected_loop: 111
selected_priority_bucket: Priority 0
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE
deep_sub_archetype_id: C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN
selection_basis: V12_Research_No_Repeat_Index.md says C10 has 13 representative rows and is Priority 0. Same-session C10 loop109 and loop110 were already produced, but local-session adjusted C10 remains below 30-row minimum stability, so C10 is still an under-covered canonical.
loop_basis: previous local C10 standard output was R2 loop110, therefore selected_loop = 111.
loop_objective: coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery
```

## 2. Price Source Validation

```text
price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
upstream_source: FinanceData/marcap
historical_eligibility_gate: pass for all trigger rows; every trigger row has 30D/90D/180D MFE and MAE.
local_runtime_note: OHLC CSV rows were computed from local stock-web CSV copies already present in this execution runtime; manifest and profile metadata were checked through GitHub.
source_proxy_only_count: 5
evidence_url_pending_count: 5
promotion_blocked_until_url_repair: true
```

## 3. Novelty / No-Repeat Check

```text
hard_duplicate_check_key: canonical_archetype_id + symbol + trigger_type + entry_date
same_session_prior_C10_loop109_symbols_excluded: 240810, 095610, 084370, 003160, 108320, 067310
same_session_prior_C10_loop110_symbols_excluded: 031980, 042700, 036810, 036200, 039440, 079370, 101490
new_symbols_this_loop: 319660, 183300, 074600, 089890, 166090
same_entry_duplicate_count: 0
new_trigger_family_count: 5
```

## 4. Human-Readable Case Table

| case_id | symbol | company | trigger_type | entry_date | role | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| C10-R2-L111-319660-20240201-DRY_STRIP_MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_BRIDGE | 319660 | 피에스케이 | Stage2-Actionable | 2024-02-01 @ 19760 | positive | 81.68 | -1.16 | 97.87 | -1.16 | current_profile_missed_structural |
| C10-R2-L111-183300-20240315-SEMI_CLEANING_COATING_SERVICE_RECOVERY_MARGIN_BRIDGE | 183300 | 코미코 | Stage2-Actionable | 2024-03-15 @ 59900 | positive | 64.27 | -3.51 | 64.27 | -47.33 | current_profile_too_late |
| C10-R2-L111-074600-20240502-QUARTZ_CONSUMABLES_LATE_CYCLE_FALSE_YELLOW | 074600 | 원익QnC | Stage3-Yellow | 2024-05-02 @ 33850 | counterexample | 21.12 | -29.99 | 21.12 | -50.72 | current_profile_false_positive |
| C10-R2-L111-089890-20240502-BACKEND_AUTOMATION_LATE_CYCLE_FALSE_YELLOW | 089890 | 코세스 | Stage3-Yellow | 2024-05-02 @ 15730 | counterexample | 26.64 | -45.9 | 26.64 | -63.32 | current_profile_false_positive |
| C10-R2-L111-166090-20240701-PARTS_MATERIALS_PEAK_TO_4B_WATCH | 166090 | 하나머티리얼즈 | Stage4B | 2024-07-01 @ 65700 | counterexample | 5.48 | -62.1 | 5.48 | -66.74 | current_profile_4B_too_late |

## 5. Case Synthesis

C10의 메모리 회복 장비 사이클은 하나의 파도처럼 보이지만, 실제로는 **초기 회복 bridge**와 **후반 price-only beta**가 서로 다른 물살이다. 피에스케이와 코미코는 2024년 초 회복 국면에서 장비·서비스·소모품 route가 실제 매출/마진 회복으로 이어질 가능성을 가격이 빠르게 읽었다. 반면 원익QnC, 코세스, 하나머티리얼즈의 늦은 진입 구간은 MFE가 남아 있어도 MAE가 훨씬 커졌고, 이 구간은 Stage3-Yellow보다는 4B/watch 또는 bridge 재확인 영역에 가깝다.

핵심 잔여오류는 `memory recovery`라는 섹터 label이 너무 넓다는 점이다. C10에서는 초기 장비·서비스 bridge가 확인된 route와, 피크 이후 같은 label을 타고 들어온 late-cycle 상대강도 route를 나눠야 한다. 이번 loop의 평균 `MFE_90D`는 39.84%지만 평균 `MAE_90D`도 -28.53%다. 즉 C10은 upside가 살아 있어도 entry risk가 뒷문처럼 열려 있으므로, Yellow/Green 전에는 order/revenue/margin bridge가 필요하고, 피크 이후에는 local 4B watch를 더 빨리 붙이는 것이 더 안전하다.

## 6. Current Calibrated Profile Stress Test

```text
before_profile_id: e2r_2_1_stock_web_calibrated_proxy
after_profile_id: proposed_C10_canonical_shadow_profile
rollback_reference_profile_id: e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus: tested_not_reapplied_as_global
stage3_yellow_total_min: kept_75_but_C10_requires_bridge_quality
stage3_green_total_min: kept_87
stage3_green_revision_min: kept_55
price_only_blowoff_blocks_positive_stage: strengthened_for_late_cycle_C10_beta
full_4b_requires_non_price_evidence: kept; price-only peak is local 4B/watch unless margin/order deterioration appears
hard_4c_routing: no confirmed hard 4C in this loop
```

Profile verdicts:

- `current_profile_missed_structural`: 피에스케이. Early 2024 memory equipment recovery route had strong price confirmation and low MAE, but a strict order-only bridge could delay Stage2-Actionable.
- `current_profile_too_late`: 코미코. Cleaning/coating service route behaved like a structural recovery winner before late-cycle drawdown.
- `current_profile_false_positive`: 원익QnC, 코세스. Late-cycle Yellow without fresh order/revenue/margin bridge exposed -29.99% to -45.90% 90D MAE.
- `current_profile_4B_too_late`: 하나머티리얼즈. The 2024-07-01 region was close to the full-window peak and the following 90D/180D drawdown was large enough to justify local 4B/watch.

## 7. Profile Simulation Summary

| profile_id | scope | hypothesis | selected_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Global calibrated bridge and price-only guard, no C10 subcycle separation | 5 | 39.84 | -28.53 | 43.08 | -45.85 | 0.40 | 2 | mixed_early_winner_late_cycle_drawdown |
| P0b_e2r_2_0_baseline_reference | rollback | Older profile likely over-promotes late memory beta and under-detects local 4B | 5 | 39.84 | -28.53 | 43.08 | -45.85 | 0.60 | 1 | worse_false_positive_control |
| P1_L2_sector_shadow | sector | L2 semi recovery requires revenue/order/margin bridge before Yellow | 5 | 39.84 | -28.53 | 43.08 | -45.85 | 0.20 | 1 | better_late_cycle_guard |
| P2_C10_canonical_shadow | canonical | C10 splits early bridge winners from late-cycle price beta; peak-period entries go to 4B/watch | 5 | 39.84 | -28.53 | 43.08 | -45.85 | 0.20 | 0 | best_local_fit |
| P3_C10_counterexample_guard_profile | guard | Keep Stage2 for early low-MAE winners but block Yellow if 90D MAE risk is not controlled by bridge evidence | 5 | 39.84 | -28.53 | 43.08 | -45.85 | 0.20 | 0 | best_risk_control |

## 8. Proposed Residual Rule

```text
rule_scope: canonical_archetype_specific
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
new_axis_proposed: C10_memory_recovery_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_RS_to_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
```

Rule wording:

> In C10, early memory-equipment recovery can remain Stage2-Actionable when relative strength is paired with a plausible order/revenue/margin bridge and controlled 30/90D MAE. However, after the subcycle has already rerated, a Stage3-Yellow/Green label should require fresh order, revenue conversion, margin expansion, or explicit customer/capex confirmation. Late-cycle relative strength without those bridges should be routed to local 4B/watch, not positive rerating.

## 9. 4B / 4C Audit

```text
4B_case_count: 3
4C_case_count: 0
four_b_local_vs_full_split_required: satisfied
local_4B_watch_guard_result: strengthened
hard_4C_confirmation_result: no_new_evidence
```

- 하나머티리얼즈의 Stage4B row uses a 2024-03-15 recovery bridge anchor price of 46500 and a full-window peak of 69300. The 2024-07-01 Stage4B entry price of 65700 gives `four_b_full_window_peak_proximity=0.842`, followed by `MAE_90D=-62.1%` and `MAE_180D=-66.74%`.
- 원익QnC and 코세스 show that even when MFE remains positive, late-cycle memory-equipment entries can carry -30% to -60% drawdown bands without a fresh bridge.

## 10. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE | 2 | 3 | 3 | 0 | 5 | 0 | 5 | 5 | 5 | true | true | base index 13 rows; local session C10 loop109 +6 and loop110 +7, this loop +5 -> local estimate 31/30 minimum, batch ingest still required |

## 11. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 2
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 12. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: missed_structural_for_verified_memory_subcycle_route, false_positive_for_late_cycle_memory_beta_without_bridge, 4B_watch_too_late_after_parts_materials_peak
new_axis_proposed: C10_memory_recovery_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_RS_to_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
promotion_blocked_until_url_repair: true
```

## 13. Shadow Weight Rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_memory_recovery_order_revenue_margin_bridge_required_before_Yellow,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Early winners had controlled MAE and plausible bridge; late-cycle Yellow proxies had large MAE","false positive rate falls from 0.40 to 0.20 in this mini-batch","C10-R2-L111-319660-S2Actionable-20240201|C10-R2-L111-183300-S2Actionable-20240315|C10-R2-L111-074600-S3Yellow-20240502|C10-R2-L111-089890-S3Yellow-20240502",5,5,3,medium,canonical_shadow_only,"not production; source URLs need repair"
shadow_weight,C10_late_cycle_RS_to_local_4B_watch,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"After the memory equipment subcycle peak, price-only RS without fresh order/revenue bridge led to high drawdown","routes 166090 and late-cycle false Yellow cases to watch/4B overlay","C10-R2-L111-166090-S4B-20240701|C10-R2-L111-074600-S3Yellow-20240502|C10-R2-L111-089890-S3Yellow-20240502",5,5,3,medium,canonical_shadow_only,"strengthens existing price-only blowoff and local 4B guard"
```

## 14. Machine-Readable JSONL Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","local_runtime_note":"OHLC CSV rows used from local stock-web copies downloaded in this session runtime; manifest/profile metadata verified via GitHub."}
{"row_type":"case","case_id":"C10-R2-L111-319660-20240201-DRY_STRIP_MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_BRIDGE","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C10-R2-L111-319660-S2Actionable-20240201","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"dry_strip_memory_capex_recovery_order_revenue_bridge"}
{"row_type":"trigger","trigger_id":"C10-R2-L111-319660-S2Actionable-20240201","case_id":"C10-R2-L111-319660-20240201-DRY_STRIP_MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_BRIDGE","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","sector":"AI_semiconductor_electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","evidence_available_at_that_date":"source-proxy memory recovery regime / company exposure known by trigger date; URL repair required before promotion","evidence_source":"source_proxy_only; batch URL repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-01","entry_price":19760.0,"MFE_30D_pct":41.19,"MFE_90D_pct":81.68,"MFE_180D_pct":97.87,"MFE_1Y_pct":97.87,"MFE_2Y_pct":null,"MAE_30D_pct":-1.16,"MAE_90D_pct":-1.16,"MAE_180D_pct":-1.16,"MAE_1Y_pct":-21.31,"MAE_2Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":39100.0,"drawdown_after_peak_pct":-48.87,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_dry_strip_memory_recovery_bridge","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_corporate_action_overlap","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|319660|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10-R2-L111-319660-20240201-DRY_STRIP_MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_BRIDGE","trigger_id":"C10-R2-L111-319660-S2Actionable-20240201","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":44,"margin_bridge_score":42,"revision_score":46,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":35,"valuation_repricing_score":58,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":42,"backlog_visibility_score":44,"margin_bridge_score":50,"revision_score":52,"relative_strength_score":78,"customer_quality_score":58,"policy_or_regulatory_score":35,"valuation_repricing_score":58,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 shadow separates verified order/revenue/margin bridge from late-cycle price-only memory equipment beta; positives gain bridge/revision weight, late-cycle proxies are cut or moved to 4B watch.","MFE_90D_pct":81.68,"MAE_90D_pct":-1.16,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C10-R2-L111-183300-20240315-SEMI_CLEANING_COATING_SERVICE_RECOVERY_MARGIN_BRIDGE","symbol":"183300","company_name":"코미코","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C10-R2-L111-183300-S2Actionable-20240315","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"semi_cleaning_coating_service_recovery_margin_bridge"}
{"row_type":"trigger","trigger_id":"C10-R2-L111-183300-S2Actionable-20240315","case_id":"C10-R2-L111-183300-20240315-SEMI_CLEANING_COATING_SERVICE_RECOVERY_MARGIN_BRIDGE","symbol":"183300","company_name":"코미코","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","sector":"AI_semiconductor_electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-15","evidence_available_at_that_date":"source-proxy memory recovery regime / company exposure known by trigger date; URL repair required before promotion","evidence_source":"source_proxy_only; batch URL repair required","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/183/183300/2024.csv","profile_path":"atlas/symbol_profiles/183/183300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-15","entry_price":59900.0,"MFE_30D_pct":52.25,"MFE_90D_pct":64.27,"MFE_180D_pct":64.27,"MFE_1Y_pct":64.27,"MFE_2Y_pct":null,"MAE_30D_pct":-3.51,"MAE_90D_pct":-3.51,"MAE_180D_pct":-47.33,"MAE_1Y_pct":-47.33,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":98400.0,"drawdown_after_peak_pct":-67.94,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_cleaning_service_recovery_margin_bridge","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_corporate_action_overlap","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|183300|Stage2-Actionable|2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10-R2-L111-183300-20240315-SEMI_CLEANING_COATING_SERVICE_RECOVERY_MARGIN_BRIDGE","trigger_id":"C10-R2-L111-183300-S2Actionable-20240315","symbol":"183300","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":44,"margin_bridge_score":48,"revision_score":46,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":35,"valuation_repricing_score":58,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":73,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":42,"backlog_visibility_score":44,"margin_bridge_score":56,"revision_score":52,"relative_strength_score":78,"customer_quality_score":58,"policy_or_regulatory_score":35,"valuation_repricing_score":58,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 shadow separates verified order/revenue/margin bridge from late-cycle price-only memory equipment beta; positives gain bridge/revision weight, late-cycle proxies are cut or moved to 4B watch.","MFE_90D_pct":64.27,"MAE_90D_pct":-3.51,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C10-R2-L111-074600-20240502-QUARTZ_CONSUMABLES_LATE_CYCLE_FALSE_YELLOW","symbol":"074600","company_name":"원익QnC","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10-R2-L111-074600-S3Yellow-20240502","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"quartz_consumables_late_cycle_false_yellow"}
{"row_type":"trigger","trigger_id":"C10-R2-L111-074600-S3Yellow-20240502","case_id":"C10-R2-L111-074600-20240502-QUARTZ_CONSUMABLES_LATE_CYCLE_FALSE_YELLOW","symbol":"074600","company_name":"원익QnC","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","sector":"AI_semiconductor_electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","evidence_available_at_that_date":"source-proxy memory recovery regime / company exposure known by trigger date; URL repair required before promotion","evidence_source":"source_proxy_only; batch URL repair required","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","profile_path":"atlas/symbol_profiles/074/074600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-02","entry_price":33850.0,"MFE_30D_pct":21.12,"MFE_90D_pct":21.12,"MFE_180D_pct":21.12,"MFE_1Y_pct":21.12,"MFE_2Y_pct":null,"MAE_30D_pct":-7.09,"MAE_90D_pct":-29.99,"MAE_180D_pct":-50.72,"MAE_1Y_pct":-54.95,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":41000.0,"drawdown_after_peak_pct":-59.32,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_cycle_false_yellow_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_corporate_action_overlap","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|074600|Stage3-Yellow|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10-R2-L111-074600-20240502-QUARTZ_CONSUMABLES_LATE_CYCLE_FALSE_YELLOW","trigger_id":"C10-R2-L111-074600-S3Yellow-20240502","symbol":"074600","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":32,"margin_bridge_score":28,"revision_score":34,"relative_strength_score":82,"customer_quality_score":34,"policy_or_regulatory_score":28,"valuation_repricing_score":76,"execution_risk_score":55,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":28,"backlog_visibility_score":32,"margin_bridge_score":20,"revision_score":28,"relative_strength_score":82,"customer_quality_score":34,"policy_or_regulatory_score":28,"valuation_repricing_score":66,"execution_risk_score":63,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 shadow separates verified order/revenue/margin bridge from late-cycle price-only memory equipment beta; positives gain bridge/revision weight, late-cycle proxies are cut or moved to 4B watch.","MFE_90D_pct":21.12,"MAE_90D_pct":-29.99,"score_return_alignment_label":"guardrail_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10-R2-L111-089890-20240502-BACKEND_AUTOMATION_LATE_CYCLE_FALSE_YELLOW","symbol":"089890","company_name":"코세스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10-R2-L111-089890-S3Yellow-20240502","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"backend_automation_late_cycle_false_yellow"}
{"row_type":"trigger","trigger_id":"C10-R2-L111-089890-S3Yellow-20240502","case_id":"C10-R2-L111-089890-20240502-BACKEND_AUTOMATION_LATE_CYCLE_FALSE_YELLOW","symbol":"089890","company_name":"코세스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","sector":"AI_semiconductor_electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","evidence_available_at_that_date":"source-proxy memory recovery regime / company exposure known by trigger date; URL repair required before promotion","evidence_source":"source_proxy_only; batch URL repair required","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv","profile_path":"atlas/symbol_profiles/089/089890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-02","entry_price":15730.0,"MFE_30D_pct":17.48,"MFE_90D_pct":26.64,"MFE_180D_pct":26.64,"MFE_1Y_pct":26.64,"MFE_2Y_pct":null,"MAE_30D_pct":-13.22,"MAE_90D_pct":-45.9,"MAE_180D_pct":-63.32,"MAE_1Y_pct":-63.32,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":19920.0,"drawdown_after_peak_pct":-71.03,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"backend_automation_late_cycle_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_corporate_action_overlap","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|089890|Stage3-Yellow|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10-R2-L111-089890-20240502-BACKEND_AUTOMATION_LATE_CYCLE_FALSE_YELLOW","trigger_id":"C10-R2-L111-089890-S3Yellow-20240502","symbol":"089890","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":32,"margin_bridge_score":28,"revision_score":34,"relative_strength_score":82,"customer_quality_score":34,"policy_or_regulatory_score":28,"valuation_repricing_score":76,"execution_risk_score":55,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":28,"backlog_visibility_score":32,"margin_bridge_score":20,"revision_score":28,"relative_strength_score":82,"customer_quality_score":34,"policy_or_regulatory_score":28,"valuation_repricing_score":66,"execution_risk_score":63,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 shadow separates verified order/revenue/margin bridge from late-cycle price-only memory equipment beta; positives gain bridge/revision weight, late-cycle proxies are cut or moved to 4B watch.","MFE_90D_pct":26.64,"MAE_90D_pct":-45.9,"score_return_alignment_label":"guardrail_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10-R2-L111-166090-20240701-PARTS_MATERIALS_PEAK_TO_4B_WATCH","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"C10-R2-L111-166090-S4B-20240701","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_counterexample","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"parts_materials_peak_to_4B_watch"}
{"row_type":"trigger","trigger_id":"C10-R2-L111-166090-S4B-20240701","case_id":"C10-R2-L111-166090-20240701-PARTS_MATERIALS_PEAK_TO_4B_WATCH","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_CONSUMABLES_SERVICE_DRY_STRIP_BACKEND_TEST_RECOVERY_VS_LATE_CYCLE_DRAWDOWN","sector":"AI_semiconductor_electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-07-01","evidence_available_at_that_date":"source-proxy memory recovery regime / company exposure known by trigger date; URL repair required before promotion","evidence_source":"source_proxy_only; batch URL repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-01","entry_price":65700.0,"MFE_30D_pct":5.48,"MFE_90D_pct":5.48,"MFE_180D_pct":5.48,"MFE_1Y_pct":5.48,"MFE_2Y_pct":null,"MAE_30D_pct":-42.92,"MAE_90D_pct":-62.1,"MAE_180D_pct":-66.74,"MAE_1Y_pct":-66.74,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300.0,"drawdown_after_peak_pct":-68.47,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.842,"four_b_full_window_peak_proximity":0.842,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat|price_only_local_peak","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_4b_watch_after_memory_parts_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_corporate_action_overlap","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|166090|Stage4B|2024-07-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10-R2-L111-166090-20240701-PARTS_MATERIALS_PEAK_TO_4B_WATCH","trigger_id":"C10-R2-L111-166090-S4B-20240701","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":40,"revision_score":42,"relative_strength_score":83,"customer_quality_score":38,"policy_or_regulatory_score":30,"valuation_repricing_score":80,"execution_risk_score":62,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":40,"revision_score":42,"relative_strength_score":83,"customer_quality_score":38,"policy_or_regulatory_score":30,"valuation_repricing_score":88,"execution_risk_score":72,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":69,"stage_label_after":"Stage4B-Watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 shadow separates verified order/revenue/margin bridge from late-cycle price-only memory equipment beta; positives gain bridge/revision weight, late-cycle proxies are cut or moved to 4B watch.","MFE_90D_pct":5.48,"MAE_90D_pct":-62.1,"score_return_alignment_label":"guardrail_counterexample","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"aggregate","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SEMI_CONSUMABLES_SERVICE_MEMORY_RECOVERY_EQUIPMENT_CYCLE_BRIDGE","calibration_usable_trigger_count":5,"representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"stage4b_case_count":3,"stage4c_case_count":0,"avg_MFE_90D_pct":39.84,"avg_MAE_90D_pct":-28.53,"avg_MFE_180D_pct":43.08,"avg_MAE_180D_pct":-45.85,"current_profile_error_count":5}
{"row_type":"residual_contribution","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["missed_structural_for_verified_memory_subcycle_route","late_cycle_false_yellow_without_order_revenue_bridge","4B_watch_too_late_after_memory_parts_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"evidence_url_pending_count":5,"promotion_blocked_until_url_repair":true}
```

## 15. Deferred Coding Agent Handoff Prompt

```text
Do not run now. Later batch implementation agent should ingest this MD together with other V12 research outputs, validate the JSONL rows, verify/repair source URLs for all source_proxy_only evidence rows, and only then consider the C10 canonical shadow rule:
- C10_memory_recovery_order_revenue_margin_bridge_required_before_Yellow
- C10_late_cycle_RS_to_local_4B_watch
No production scoring change is requested by this research file alone.
```

## 16. Next Research State

```text
completed_round: R2
completed_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
next_recommended_archetypes: C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
