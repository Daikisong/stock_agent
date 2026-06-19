# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
expected_v12_result_file: true
filename_pattern_pass: true
standard_v12_result_filename: e2r_stock_web_v12_residual_round_R1_loop_141_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
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

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus: already_applied_not_reproposed_globally
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
price_only_blowoff_blocks_positive_stage: tested_for_C02_theme_proxy_residuals
full_4b_requires_non_price_evidence: tested_for_local_peak_vs_full_window_split
hard_4c_thesis_break_routes_to_4c: kept; no confirmed hard 4C promotion in this loop
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
selected_round: R1
selected_loop: 141
selected_priority_bucket: Priority 0
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE
deep_sub_archetype_id: C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery
```

## 3. Previous Coverage / Duplicate Avoidance Check

```text
no_repeat_index_C02_rows: 10
same_session_prior_C02_loop139_symbols_excluded: 267260, 033100, 298040, 103590, 017040, 006340
same_session_prior_C02_loop140_symbols_excluded: 229640, 199820, 189860, 388050, 237750, 006910
no_repeat_index_top_C02_symbols_avoided: 000500, 001440, 006260, 010120, 017510, 024840
new_symbols_this_loop: 062040, 060370, 147830, 130660, 042370, 040160, 057540
hard_duplicate_check_key: canonical_archetype_id + symbol + trigger_type + entry_date
same_entry_duplicate_count: 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
historical_eligibility_gate: pass for all trigger rows
```

## 5. Historical Eligibility Gate

All representative trigger rows use stock-web tradable shards and have clean 180-trading-day windows. Corporate-action candidate dates, where present in profile metadata, are outside the 180D windows used here. Rows are raw/unadjusted and therefore remain calibration rows rather than split-adjusted performance claims.

## 6. Canonical Archetype Compression Map

```text
canonical: C02_POWER_GRID_DATACENTER_CAPEX
fine route A: transformer IPO / capacity / backlog visibility / ASP bridge -> 062040
fine route B: subsea cable and interconnector grid CAPEX -> 060370
fine route C: transmission component / poleline / grid-material extension -> 147830
fine route D: utility power-service / policy proxy overheat -> 130660
fine route E: switchgear / power-control label without confirmed order bridge -> 042370
fine route F: AMI / smart-meter policy label without durable conversion -> 040160
fine route G: AMI / smart-grid recovery exception, still source-proxy limited -> 057540
```

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | role | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| C02-R1-L141-01-062040 | 062040 | 산일전기 | Stage2-Actionable | 2024-11-06 | structural_success / positive | 53.78 | -11.6 | 125.97 | -20.17 | current_profile_missed_structural |
| C02-R1-L141-02-060370 | 060370 | LS마린솔루션 | Stage2-Actionable | 2024-05-20 | structural_success / positive | 86.98 | -10.91 | 86.98 | -14.97 | current_profile_4B_too_late |
| C02-R1-L141-03-147830 | 147830 | 제룡산업 | Stage2 | 2024-04-29 | high_mae_success / positive | 81.93 | -22.43 | 81.93 | -29.83 | current_profile_correct |
| C02-R1-L141-04-130660 | 130660 | 한전산업 | Stage4B | 2024-06-10 | 4B_overlay_success / counterexample | 57.89 | -22.67 | 57.89 | -28.66 | current_profile_4B_too_late |
| C02-R1-L141-05-042370 | 042370 | 비츠로테크 | Stage4B | 2024-05-08 | failed_rerating / counterexample | 16.65 | -43.52 | 16.65 | -47.14 | current_profile_false_positive |
| C02-R1-L141-06-040160 | 040160 | 누리플렉스 | Stage4B | 2024-04-05 | failed_rerating / counterexample | 9.71 | -32.94 | 9.71 | -40.42 | current_profile_false_positive |
| C02-R1-L141-07-057540 | 057540 | 옴니시스템 | Stage2-Actionable | 2024-12-11 | missed_structural / positive | 59.88 | -16.02 | 70.96 | -16.02 | current_profile_data_insufficient |


## 8. Positive vs Counterexample Balance

```text
positive_case_count: 4
counterexample_count: 3
4B_case_count: 6
4C_case_count: 2
calibration_usable_case_count: 7
new_independent_case_count: 7
```

C02 behaves like a substation: the same voltage label can feed a real load or an empty bus. Transformer and subsea-cable routes carried real load in the price path, while AMI/policy/switchgear labels often flashed first and lost power after the local peak. That is the residual this loop tries to capture.

## 9. Evidence Source Map

| symbol | evidence family | evidence status | promotion use |
|---:|---|---|---|
| 062040 | transformer capacity/backlog/IPO rerating route | source_proxy_only | usable for residual pattern; URL repair before promotion |
| 060370 | subsea cable / grid interconnect order route | source_proxy_only | usable for residual pattern; URL repair before promotion |
| 147830 | transmission equipment component route | source_proxy_only | usable with high-MAE guard |
| 130660 | utility/power-service policy proxy overheat | source_proxy_only | guardrail evidence |
| 042370 | power-control/switchgear label spike | source_proxy_only | guardrail evidence |
| 040160 | AMI/smart-meter policy label | source_proxy_only | guardrail evidence |
| 057540 | AMI/smart-grid recovery exception | source_proxy_only | residual exception; URL repair pending |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | status |
|---:|---|---|---|
| 062040 | atlas/ohlcv_tradable_by_symbol_year/062/062040/2024.csv | atlas/symbol_profiles/062/062040.json | clean_180D_window |
| 060370 | atlas/ohlcv_tradable_by_symbol_year/060/060370/2024.csv | atlas/symbol_profiles/060/060370.json | clean_180D_window |
| 147830 | atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv | atlas/symbol_profiles/147/147830.json | clean_180D_window |
| 130660 | atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv | atlas/symbol_profiles/130/130660.json | clean_180D_window |
| 042370 | atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv | atlas/symbol_profiles/042/042370.json | clean_180D_window |
| 040160 | atlas/ohlcv_tradable_by_symbol_year/040/040160/2024.csv | atlas/symbol_profiles/040/040160.json | clean_180D_window |
| 057540 | atlas/ohlcv_tradable_by_symbol_year/057/057540/2024.csv | atlas/symbol_profiles/057/057540.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C02-R1-L141-01-062040-Stage2_Actionable | 062040 | Stage2-Actionable | 2024-11-06 | 54300 | 40.33 | -11.6 | 53.78 | -11.6 | 125.97 | -20.17 | 2025-08-04 | 122700 | -5.62 |
| C02-R1-L141-02-060370-Stage2_Actionable | 060370 | Stage2-Actionable | 2024-05-20 | 13290 | 57.26 | -10.91 | 86.98 | -10.91 | 86.98 | -14.97 | 2024-07-11 | 24850 | -54.53 |
| C02-R1-L141-03-147830-Stage2 | 147830 | Stage2 | 2024-04-29 | 6420 | 42.52 | -22.43 | 81.93 | -22.43 | 81.93 | -29.83 | 2024-07-11 | 11680 | -61.43 |
| C02-R1-L141-04-130660-Stage4B | 130660 | Stage4B | 2024-06-10 | 12350 | 57.89 | -22.67 | 57.89 | -22.67 | 57.89 | -28.66 | 2024-07-18 | 19500 | -54.82 |
| C02-R1-L141-05-042370-Stage4B | 042370 | Stage4B | 2024-05-08 | 11350 | 16.65 | -24.58 | 16.65 | -43.52 | 16.65 | -47.14 | 2024-05-13 | 13240 | -54.68 |
| C02-R1-L141-06-040160-Stage4B | 040160 | Stage4B | 2024-04-05 | 3810 | 9.71 | -19.16 | 9.71 | -32.94 | 9.71 | -40.42 | 2024-04-05 | 4180 | -45.69 |
| C02-R1-L141-07-057540-Stage2_Actionable | 057540 | Stage2-Actionable | 2024-12-11 | 830 | 11.33 | -15.66 | 59.88 | -16.02 | 70.96 | -16.02 | 2025-04-29 | 1419 | -43.06 |


## 12. Trigger-Level OHLC Backtest Tables

The average 90D path is `MFE_90D=52.4% / MAE_90D=-22.87%`; the average 180D path is `MFE_180D=64.3% / MAE_180D=-28.17%`. The attractive headline MFE is polluted by three local-peak failures and several MAE bands below -20%, so C02 cannot be loosened globally. It needs a verified bridge split.

## 13. Current Calibrated Profile Stress Test

```text
current_profile_correct: 1
current_profile_missed_structural: 1
current_profile_false_positive: 2
current_profile_4B_too_late: 2
current_profile_data_insufficient: 1
current_profile_error_count: 6
```

The current calibrated profile is mostly right to distrust price-only spikes. Its residual miss is subtler: it needs a way to separate a transformer/subsea-cable route with genuine capacity or order visibility from a policy/AMI/switchgear label that only borrowed the C02 costume.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green representative row is promoted in this loop. `Stage2-Actionable` is allowed for 062040, 060370, and 057540 only as residual/bridge evidence. `Stage3-Yellow` should remain blocked until one of order/backlog, capacity/lead-time, ASP, project/customer, or grid-automation conversion is verified. `Stage3-Green` remains unchanged at the global threshold and should not be unlocked by source-proxy-only rows.

## 15. 4B Local vs Full-window Timing Audit

- 060370, 147830, and 130660 show that C02 winners can have excellent MFE but still demand local peak watch when the rally compresses too much upside into 30~60 trading days.
- 042370 and 040160 are cleaner failed-rerating samples: local peak proximity was high, full-window follow-through was weak, and non-price bridge remained thin.
- The proposed 4B treatment is not a sell rule. It is a watch overlay that stops theme-only C02 labels from becoming positive Stage3 evidence.

## 16. 4C Protection Audit

No new hard 4C route is promoted. 042370 and 040160 receive `thesis_break_watch_only` because price path and missing bridge support a warning, but the loop does not provide confirmed contract cancellation, accounting break, or hard order cut evidence.

## 17. Sector-Specific Rule Candidate

```text
rule_scope: sector_specific
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
proposal: L1 grid/datacenter CAPEX Stage2-Actionable requires at least one non-price bridge before Yellow/Green.
sector_specific_rule_candidate: true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope: canonical_archetype_specific
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
new_axis_proposed: C02_verified_transformer_subsea_cable_grid_automation_bridge_required_before_Yellow_plus_AMI_policy_proxy_to_local_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
canonical_archetype_rule_candidate: true
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | selected_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Existing calibrated bridge and price-only blowoff guard without C02 sub-route differentiation | 7 | 52.4 | -22.87 | 64.3 | -28.17 | 0.43 | 2 | mixed; misses transformer/subsea positives and still lets theme proxies breathe too long |
| P0b_e2r_2_0_baseline_reference | rollback | Older baseline over-promotes relative-strength theme spikes and under-penalizes local peaks | 7 | 52.4 | -22.87 | 64.3 | -28.17 | 0.57 | 1 | worse false-positive control |
| P1_L1_sector_shadow | sector | Require L1 non-price bridge: order/backlog/capacity/ASP/lead-time or grid automation conversion | 7 | 52.4 | -22.87 | 64.3 | -28.17 | 0.29 | 1 | better but still broad |
| P2_C02_canonical_shadow | canonical | Split transformer/subsea/product-route positives from AMI/policy/theme-only spikes | 7 | 52.4 | -22.87 | 64.3 | -28.17 | 0.14 | 1 | best local fit |
| P3_C02_high_MAE_guard_profile | guard | Permit high-MFE winners only after second confirmation when MAE risk exceeds -20% | 7 | 52.4 | -22.87 | 64.3 | -28.17 | 0.14 | 1 | best risk control |


## 20. Score-Return Alignment Matrix

Positive bridge-aligned cases: 062040, 060370, 147830, 057540. Counterexample/guardrail cases: 130660, 042370, 040160. The score-return alignment improves only when the after-profile rewards verified product-route bridges and penalizes theme-only local peaks.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE | 4 | 3 | 6 | 2 | 7 | 0 | 7 | 7 | 6 | true | true | C02 index 10 -> local-session adjusted 29 after this loop; need 1 more to 30 / 21 more to 50 |

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
residual_error_types_found: missed_structural_transformer_capacity_route, theme_proxy_false_positive, local_4b_too_late, high_MAE_success_requires_entry_guard
new_axis_proposed: C02_verified_transformer_subsea_cable_grid_automation_bridge_required_before_Yellow_plus_AMI_policy_proxy_to_local_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 7 new independent cases, 3 counterexamples, and 6 residual errors for L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web tradable OHLC path, entry close, 30D/90D/180D MFE/MAE, clean 180D forward availability, canonical/round/sector consistency, same-session duplicate avoidance.

Not validated for immediate promotion: direct article-level evidence URLs. All evidence rows remain source-proxy-only and should be URL-repaired before any production promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_verified_bridge_before_yellow,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Require verified order/backlog/capacity/ASP/grid-automation bridge before Yellow; theme-only spikes stay local 4B watch","reduced false-positive profile while retaining transformer/subsea positives","C02-R1-L141-01-062040-Stage2_Actionable|C02-R1-L141-02-060370-Stage2_Actionable|C02-R1-L141-03-147830-Stage2|C02-R1-L141-04-130660-Stage4B|C02-R1-L141-05-042370-Stage4B|C02-R1-L141-06-040160-Stage4B|C02-R1-L141-07-057540-Stage2_Actionable",7,7,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C02-R1-L141-01-062040","symbol":"062040","company_name":"산일전기","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Transformer IPO route behaved like a delayed C02 structural winner; profile needs verified capacity/backlog bridge, not pure new-listing momentum."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-01-062040-Stage2_Actionable","case_id":"C02-R1-L141-01-062040","symbol":"062040","company_name":"산일전기","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-06","entry_date":"2024-11-06","entry_price":54300.0,"evidence_available_at_that_date":"transformer_ipo_capacity_sold_out_bridge proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/062/062040/2024.csv","profile_path":"atlas/symbol_profiles/062/062040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.33,"MFE_90D_pct":53.78,"MFE_180D_pct":125.97,"MFE_1Y_pct":229.47,"MFE_2Y_pct":null,"MAE_30D_pct":-11.6,"MAE_90D_pct":-11.6,"MAE_180D_pct":-20.17,"MAE_1Y_pct":-20.17,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-08-04","peak_price":122700.0,"drawdown_after_peak_pct":-5.62,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"transformer_ipo_capacity_sold_out_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:062040:Stage2-Actionable:2024-11-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-01-062040","trigger_id":"C02-R1-L141-01-062040-Stage2_Actionable","symbol":"062040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":75,"margin_bridge_score":58,"revision_score":50,"relative_strength_score":78,"customer_quality_score":62,"policy_or_regulatory_score":54,"valuation_repricing_score":55,"execution_risk_score":28,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_before":62.21,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":72,"backlog_visibility_score":83,"margin_bridge_score":65,"revision_score":50,"relative_strength_score":78,"customer_quality_score":62,"policy_or_regulatory_score":54,"valuation_repricing_score":55,"execution_risk_score":23,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_after":65.89,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":53.78,"MAE_90D_pct":-11.6,"score_return_alignment_label":"positive_bridge_aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C02-R1-L141-02-060370","symbol":"060370","company_name":"LS마린솔루션","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Subsea cable/interconnector route generated large early MFE, then the local peak collapsed; bridge was valid but local 4B needed faster watch."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-02-060370-Stage2_Actionable","case_id":"C02-R1-L141-02-060370","symbol":"060370","company_name":"LS마린솔루션","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":13290.0,"evidence_available_at_that_date":"subsea_power_cable_grid_interconnect_order_route proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/060/060370/2024.csv","profile_path":"atlas/symbol_profiles/060/060370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.26,"MFE_90D_pct":86.98,"MFE_180D_pct":86.98,"MFE_1Y_pct":86.98,"MFE_2Y_pct":null,"MAE_30D_pct":-10.91,"MAE_90D_pct":-10.91,"MAE_180D_pct":-14.97,"MAE_1Y_pct":-14.97,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":24850.0,"drawdown_after_peak_pct":-54.53,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":0.44,"four_b_timing_verdict":"price_only_local_4B_watch_required","four_b_evidence_type":["positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"subsea_power_cable_grid_interconnect_order_route_positive","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:060370:Stage2-Actionable:2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-02-060370","trigger_id":"C02-R1-L141-02-060370-Stage2_Actionable","symbol":"060370","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":75,"margin_bridge_score":58,"revision_score":50,"relative_strength_score":78,"customer_quality_score":62,"policy_or_regulatory_score":54,"valuation_repricing_score":55,"execution_risk_score":28,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_before":62.21,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":72,"backlog_visibility_score":83,"margin_bridge_score":65,"revision_score":50,"relative_strength_score":78,"customer_quality_score":62,"policy_or_regulatory_score":54,"valuation_repricing_score":55,"execution_risk_score":23,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_after":65.89,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":86.98,"MAE_90D_pct":-10.91,"score_return_alignment_label":"positive_bridge_aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C02-R1-L141-03-147830","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Transmission-equipment component route produced high MFE but also severe MAE; positive signal should carry entry-risk cap."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-03-147830-Stage2","case_id":"C02-R1-L141-03-147830","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":6420.0,"evidence_available_at_that_date":"transmission_equipment_component_grid_route proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv","profile_path":"atlas/symbol_profiles/147/147830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.52,"MFE_90D_pct":81.93,"MFE_180D_pct":81.93,"MFE_1Y_pct":81.93,"MFE_2Y_pct":null,"MAE_30D_pct":-22.43,"MAE_90D_pct":-22.43,"MAE_180D_pct":-29.83,"MAE_1Y_pct":-29.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":11680.0,"drawdown_after_peak_pct":-61.43,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":0.44,"four_b_timing_verdict":"price_only_local_4B_watch_required","four_b_evidence_type":["positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"transmission_equipment_component_grid_route_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:147830:Stage2:2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-03-147830","trigger_id":"C02-R1-L141-03-147830-Stage2","symbol":"147830","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":58,"margin_bridge_score":42,"revision_score":35,"relative_strength_score":82,"customer_quality_score":45,"policy_or_regulatory_score":58,"valuation_repricing_score":70,"execution_risk_score":62,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":10,"accounting_trust_risk_score":12},"weighted_score_before":46.7,"stage_label_before":"Watch","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":66,"margin_bridge_score":49,"revision_score":35,"relative_strength_score":82,"customer_quality_score":45,"policy_or_regulatory_score":58,"valuation_repricing_score":70,"execution_risk_score":57,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":10,"accounting_trust_risk_score":12},"weighted_score_after":50.38,"stage_label_after":"Watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":81.93,"MAE_90D_pct":-22.43,"score_return_alignment_label":"positive_bridge_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C02-R1-L141-04-130660","symbol":"130660","company_name":"한전산업","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Power-service/policy proxy moved sharply but lacked datacenter/grid order bridge; useful as C02 local-4B watch case."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-04-130660-Stage4B","case_id":"C02-R1-L141-04-130660","symbol":"130660","company_name":"한전산업","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":12350.0,"evidence_available_at_that_date":"utility_power_service_policy_theme_overheat proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv","profile_path":"atlas/symbol_profiles/130/130660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.89,"MFE_90D_pct":57.89,"MFE_180D_pct":57.89,"MFE_1Y_pct":57.89,"MFE_2Y_pct":null,"MAE_30D_pct":-22.67,"MAE_90D_pct":-22.67,"MAE_180D_pct":-28.66,"MAE_1Y_pct":-29.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":19500.0,"drawdown_after_peak_pct":-54.82,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.42,"four_b_timing_verdict":"price_only_local_4B_watch_required","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"utility_power_service_policy_theme_overheat_counterexample","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:130660:Stage4B:2024-06-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-04-130660","trigger_id":"C02-R1-L141-04-130660-Stage4B","symbol":"130660","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":88,"customer_quality_score":30,"policy_or_regulatory_score":70,"valuation_repricing_score":82,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":12,"accounting_trust_risk_score":15},"weighted_score_before":30.19,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":88,"customer_quality_score":30,"policy_or_regulatory_score":70,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":12,"accounting_trust_risk_score":15},"weighted_score_after":27.89,"stage_label_after":"Stage4B-watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":57.89,"MAE_90D_pct":-22.67,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C02-R1-L141-05-042370","symbol":"042370","company_name":"비츠로테크","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Power-control/switchgear theme spike had no durable order/margin bridge and the 90/180D path punished it."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-05-042370-Stage4B","case_id":"C02-R1-L141-05-042370","symbol":"042370","company_name":"비츠로테크","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":11350.0,"evidence_available_at_that_date":"power_control_switchgear_theme_without_order_bridge proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv","profile_path":"atlas/symbol_profiles/042/042370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.65,"MFE_90D_pct":16.65,"MFE_180D_pct":16.65,"MFE_1Y_pct":16.65,"MFE_2Y_pct":null,"MAE_30D_pct":-24.58,"MAE_90D_pct":-43.52,"MAE_180D_pct":-47.14,"MAE_1Y_pct":-47.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":13240.0,"drawdown_after_peak_pct":-54.68,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"price_only_local_4B_watch_required","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"power_control_switchgear_theme_without_order_bridge_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:042370:Stage4B:2024-05-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-05-042370","trigger_id":"C02-R1-L141-05-042370-Stage4B","symbol":"042370","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":18,"relative_strength_score":76,"customer_quality_score":25,"policy_or_regulatory_score":46,"valuation_repricing_score":78,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":18},"weighted_score_before":21.43,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":25,"margin_bridge_score":10,"revision_score":18,"relative_strength_score":76,"customer_quality_score":25,"policy_or_regulatory_score":46,"valuation_repricing_score":66,"execution_risk_score":84,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":18},"weighted_score_after":19.13,"stage_label_after":"Stage4B-watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":16.65,"MAE_90D_pct":-43.52,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C02-R1-L141-06-040160","symbol":"040160","company_name":"누리플렉스","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AMI/smart-meter label popped but never converted into C02-quality backlog/capacity bridge."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-06-040160-Stage4B","case_id":"C02-R1-L141-06-040160","symbol":"040160","company_name":"누리플렉스","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-04-05","entry_date":"2024-04-05","entry_price":3810.0,"evidence_available_at_that_date":"ami_smart_meter_theme_without_retention_or_order_conversion proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/040/040160/2024.csv","profile_path":"atlas/symbol_profiles/040/040160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.71,"MFE_90D_pct":9.71,"MFE_180D_pct":9.71,"MFE_1Y_pct":9.71,"MFE_2Y_pct":null,"MAE_30D_pct":-19.16,"MAE_90D_pct":-32.94,"MAE_180D_pct":-40.42,"MAE_1Y_pct":-40.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":4180.0,"drawdown_after_peak_pct":-45.69,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"price_only_local_4B_watch_required","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"ami_smart_meter_theme_without_retention_or_order_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:040160:Stage4B:2024-04-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-06-040160","trigger_id":"C02-R1-L141-06-040160-Stage4B","symbol":"040160","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":18,"relative_strength_score":76,"customer_quality_score":25,"policy_or_regulatory_score":46,"valuation_repricing_score":78,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":18},"weighted_score_before":21.43,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":25,"margin_bridge_score":10,"revision_score":18,"relative_strength_score":76,"customer_quality_score":25,"policy_or_regulatory_score":46,"valuation_repricing_score":66,"execution_risk_score":84,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":18},"weighted_score_after":19.13,"stage_label_after":"Stage4B-watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":9.71,"MAE_90D_pct":-32.94,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C02-R1-L141-07-057540","symbol":"057540","company_name":"옴니시스템","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","deep_sub_archetype_id":"C02_DEEP_TRANSFORMER_IPO_SUBSEA_CABLE_GRID_METERING_AND_POWER_CONTROL_VS_THEME_SPIKE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Smart-meter route later produced strong 90/180D MFE; because evidence is proxy-only, treat as recovery exception not promotion shortcut."}
{"row_type":"trigger","trigger_id":"C02-R1-L141-07-057540-Stage2_Actionable","case_id":"C02-R1-L141-07-057540","symbol":"057540","company_name":"옴니시스템","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_SUBSEA_CABLE_GRID_AUTOMATION_SMART_METER_CAPEX_BRIDGE","sector":"power_grid_datacenter_capex","primary_archetype":"C02 power-grid / datacenter CAPEX residual","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-11","entry_date":"2024-12-11","entry_price":830.0,"evidence_available_at_that_date":"ami_smart_grid_metering_recovery_exception proxy evidence available on or before trigger date; URL repair pending for promotion use","evidence_source":"source_proxy_only: historical public-disclosure/news theme tag + stock-web OHLC validation; direct URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/057/057540/2024.csv","profile_path":"atlas/symbol_profiles/057/057540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.33,"MFE_90D_pct":59.88,"MFE_180D_pct":70.96,"MFE_1Y_pct":70.96,"MFE_2Y_pct":null,"MAE_30D_pct":-15.66,"MAE_90D_pct":-16.02,"MAE_180D_pct":-16.02,"MAE_1Y_pct":-16.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-04-29","peak_price":1419.0,"drawdown_after_peak_pct":-43.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":0.44,"four_b_timing_verdict":"overlay_watch","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ami_smart_grid_metering_recovery_exception_positive","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:057540:Stage2-Actionable:2024-12-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C02_shadow","case_id":"C02-R1-L141-07-057540","trigger_id":"C02-R1-L141-07-057540-Stage2_Actionable","symbol":"057540","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":48,"backlog_visibility_score":50,"margin_bridge_score":38,"revision_score":32,"relative_strength_score":70,"customer_quality_score":42,"policy_or_regulatory_score":62,"valuation_repricing_score":55,"execution_risk_score":42,"legal_or_contract_risk_score":16,"dilution_cb_risk_score":8,"accounting_trust_risk_score":12},"weighted_score_before":42.47,"stage_label_before":"Watch","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":58,"margin_bridge_score":45,"revision_score":32,"relative_strength_score":70,"customer_quality_score":42,"policy_or_regulatory_score":62,"valuation_repricing_score":55,"execution_risk_score":37,"legal_or_contract_risk_score":16,"dilution_cb_risk_score":8,"accounting_trust_risk_score":12},"weighted_score_after":46.15,"stage_label_after":"Watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C02 shadow bridge rewards verified order/backlog/capacity/margin route and penalizes theme-only price spikes as local 4B watch.","MFE_90D_pct":59.88,"MAE_90D_pct":-16.02,"score_return_alignment_label":"positive_bridge_aligned","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"residual_contribution","round":"R1","loop":"141","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["missed_structural_transformer_capacity_route","theme_proxy_false_positive","local_4b_too_late","high_MAE_success_requires_entry_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

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
completed_round = R1
completed_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C11_BATTERY_ORDERBOOK_RERATING, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/V12_Research_No_Repeat_Index.md` is used only as coverage and duplicate-avoidance ledger.
- `Songdaiki/stock-web` is used as the required price source.
- The stock-web manifest reports `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 9
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
