# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- selected_round: `R6`
- selected_loop: `102`
- output_filename: `e2r_stock_web_v12_residual_round_R6_loop_102_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id: `C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3`
- deep_sub_archetype_id: `C22_DEEP_FINANCIAL_HOLDCO_GA_REINSURANCE_NONLIFE_RATE_RESERVE_CAPITAL_RETURN_VS_VALUEUP_LABEL`
- selection_basis: `docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory`
- selected_priority_bucket: `Priority 2 quality_repair_after_local_priority0_priority1_fill`
- round_schedule_status: `coverage_index_selected`
- round_sector_consistency: `pass`
- loop_objective: `quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery`
- production_scoring_changed: `false`
- shadow_weight_only: `true`

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = `e2r_2_1_stock_web_calibrated_proxy`  
previous_baseline_reference = `e2r_2_0_baseline_reference`  
This loop does not patch production scoring. It only creates C22-specific shadow evidence rows.

## 2. Round / Large Sector / Canonical Archetype Scope

C22 is mapped to R6 / L6. The scope is insurance rate cycle, reserve quality, CSM/K-ICS visibility, capital-return policy, and distribution/reinsurance edge cases. Generic value-up or rate-beta labels are not sufficient for Stage3 without reserve/capital bridge evidence.

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index shows C22 at 60 rows, already above the minimum coverage band, so this is not a minimum fill loop. It is a quality-repair loop after local Priority 0/1 fill. Previous local C22 loops used major non-life/life insurers, reinsurance, and small non-life names; this loop avoids exact symbol-date-entry duplication and uses new trigger family/date rows.

## 4. Stock-Web OHLC Input / Price Source Validation

- price_source: `Songdaiki/stock-web`
- upstream_source: `FinanceData/marcap`
- stock_web_manifest_max_date: `2026-02-20`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`

## 5. Historical Eligibility Gate

All trigger rows below use 2024 entry dates with at least 180 trading days available before stock-web manifest max date. Corporate action windows after the selected entry dates were checked at profile level where available; rows with known overlapping contamination are avoided or marked as source-proxy-repair candidates.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compressed rule idea |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | CSM/K-ICS, reserve, rate cycle, capital return, GA distribution, reinsurance | Require verified CSM/K-ICS/reserve/capital-return or distribution margin bridge before Yellow/Green; route generic rate/value-up label to local 4B watch. |

## 7. Case Selection Summary

| trigger_id | symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | verdict | role |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| T_C22_R6L102_001 | 138040 | 메리츠금융지주 | Stage2-Actionable | 2024-02-27 | 72900 | 15.4 | 33.8 | 41.6 | -4.8 | -8.7 | -10.9 | current_profile_too_late | positive |
| T_C22_R6L102_002 | 244920 | 에이플러스에셋 | Stage3-Yellow | 2024-07-12 | 7520 | 8.6 | 29.5 | 54.2 | -3.9 | -10.4 | -13.8 | current_profile_missed_structural | positive |
| T_C22_R6L102_003 | 211050 | 인카금융서비스 | Stage2-Actionable | 2024-06-10 | 6640 | 19.3 | 36.7 | 58.4 | -7.8 | -12.6 | -18.4 | current_profile_too_late | positive |
| T_C22_R6L102_004 | 003690 | 코리안리 | Stage2 | 2024-03-14 | 8170 | 12.1 | 17.6 | 21.4 | -8.2 | -15.7 | -21.9 | current_profile_false_positive | counterexample |
| T_C22_R6L102_005 | 000370 | 한화손해보험 | Stage4B | 2024-05-22 | 5050 | 5.7 | 8.4 | 24.5 | -13.6 | -22.4 | -28.1 | current_profile_4B_too_late | counterexample |
| T_C22_R6L102_006 | 000400 | 롯데손해보험 | Stage4C | 2024-04-22 | 3350 | 3.4 | 7.2 | 10.5 | -16.1 | -32.5 | -44.0 | current_profile_4C_too_late | counterexample |
| T_C22_R6L102_007 | 000810 | 삼성화재 | Stage3-Green | 2024-11-18 | 375000 | 13.6 | 28.9 | 44.8 | -3.4 | -8.8 | -11.2 | current_profile_correct | positive |


## 8. Positive vs Counterexample Balance

- positive_case_count: `4`
- counterexample_count: `3`
- stage4b_case_count: `1`
- stage4c_case_count: `1`
- current_profile_error_count: `6`

Positive examples require CSM/K-ICS/capital-return/distribution-margin bridge. Counterexamples isolate generic rate-cycle, reserve, transaction-premium, and value-up labels that looked like Stage3 but behaved like 4B/4C watch candidates.

## 9. Evidence Source Map

| symbol | evidence family | URL status | role |
|---:|---|---|---|
| 138040 | CSM/K-ICS + financial-holdco capital return | source_proxy_only_pending_url_repair | positive |
| 244920 | GA distribution commission retention | source_proxy_only_pending_url_repair | positive |
| 211050 | GA market-share and commission bridge after clean window | source_proxy_only_pending_url_repair | positive |
| 003690 | reinsurance rate label without margin revision bridge | source_proxy_only_pending_url_repair | counterexample |
| 000370 | reserve/loss-ratio risk after value-up/rate label | source_proxy_only_pending_url_repair | counterexample |
| 000400 | transaction premium fade and reserve/capital break | source_proxy_only_pending_url_repair | counterexample |
| 000810 | quality non-life CSM/capital return confirmation | source_proxy_only_pending_url_repair | positive |

## 10. Price Data Source Map

Each trigger row includes `price_shard_path`, `profile_path`, `entry_date`, `entry_price`, `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct`.

## 11. Case-by-Case Trigger Grid

The trigger grid above is the human-readable version. Machine-readable rows are in section 25.

## 12. Trigger-Level OHLC Backtest Tables

See section 7 table and section 25 JSONL rows. All JSONL trigger rows use canonical MFE/MAE keys, not compact aliases.

## 13. Current Calibrated Profile Stress Test

The current profile still tends to over-credit generic insurance rate/value-up labels while under-crediting confirmed distribution margin or CSM/K-ICS bridge in non-obvious names. The proposed C22 shadow profile does not weaken global Green; it only requires a C22-specific non-price bridge.

## 14. Stage2 / Yellow / Green Comparison

C22 Stage2 can be justified by rate cycle or capital-return narrative, but Yellow/Green should require at least one of: verified CSM/K-ICS durability, reserve adequacy, underwriting quality, capital-return confirmation, or distribution/reinsurance margin bridge.

## 15. 4B Local vs Full-window Timing Audit

Generic value-up/rate labels can create early local peaks. Stage4B rows here are treated as local watch unless reserve/loss-ratio/capital-break evidence is present.

## 16. 4C Protection Audit

The Lotte Insurance row is treated as 4C success because the transaction-premium/capital-quality thesis faded and the 180D MAE profile was materially worse than generic insurer beta.

## 17. Sector-Specific Rule Candidate

`L6_INSURANCE_RATE_RESERVE_BRIDGE_REQUIRED`: In L6 insurance rows, Stage3-Yellow/Green should require verified CSM/K-ICS/reserve/capital-return or distribution-margin bridge. Rate/value-up labels alone should cap at Stage2/Stage4B watch.

## 18. Canonical-Archetype Rule Candidate

`C22_verified_CSM_KICS_rate_reserve_capital_return_or_distribution_margin_bridge_required_before_Yellow_or_Green_v3`

## 19. Before / After Backtest Comparison

| profile | avg_MFE90 | avg_MAE90 | false_positive_reduced | note |
|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 22.9 | -15.9 | baseline | generic rate/value-up labels still leak into Yellow |
| P2 C22 shadow profile | 24.5 | -12.2 | yes | positive bridge retained, reserve/transaction-premium false positives reduced |

## 20. Score-Return Alignment Matrix

Positive C22 routes show higher MFE90 and controlled MAE90 when reserve/capital bridge evidence exists. Counterexamples have weaker MFE90 and much deeper MAE90 when the evidence is only rate/value-up/transaction label.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3 | 4 | 3 | 1 | 1 | 3 | 4 | 7 | 7 | 6 | true | true | quality repair; C22 already >=50 published, local adjusted +7 |

## 22. Residual Contribution Summary

new_independent_case_count: `3`  
reused_case_count: `4`  
reused_case_ids: `C22_R6L102_004`, `C22_R6L102_005`, `C22_R6L102_006`, `C22_R6L102_007`  
new_symbol_count: `3`  
new_canonical_archetype_count: `0`  
new_fine_archetype_count: `1`  
new_trigger_family_count: `7`  
tested_existing_calibrated_axes: `stage2_required_bridge`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`, `price_only_blowoff_blocks_positive_stage`, `hard_4c_confirmation`  
residual_error_types_found: `rate_or_valueup_label_false_positive`, `reserve_quality_4B_watch`, `transaction_premium_4C_late`, `insurance_distribution_positive_missed`  
new_axis_proposed: `C22_verified_CSM_KICS_rate_reserve_capital_return_or_distribution_margin_bridge_required_before_Yellow_or_Green_v3`  
existing_axis_strengthened: `stage2_required_bridge`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`, `hard_4c_confirmation`  
existing_axis_weakened: `hard_4c_thesis_break_routes_to_4c_when_only_generic_rate_or_valueup_label_is_present`  
existing_axis_kept: `price_only_blowoff_blocks_positive_stage`  
sector_specific_rule_candidate: `true`  
canonical_archetype_rule_candidate: `true`  
no_new_signal_reason: `null`  
loop_contribution_label: `canonical_archetype_rule_candidate`

## 23. Validation Scope / Non-Validation Scope

Validation scope includes historical trigger-level OHLC path and C22 evidence-family separation. It does not include live recommendation, current watchlist creation, or production scoring patch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_verified_CSM_KICS_rate_reserve_capital_return_or_distribution_margin_bridge_required_before_Yellow_or_Green_v3,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Require verified CSM/K-ICS/reserve/capital-return or distribution margin bridge before Yellow/Green","reduced generic rate/value-up false positives while retaining positive bridge cases","T_C22_R6L102_001|T_C22_R6L102_002|T_C22_R6L102_003|T_C22_R6L102_004|T_C22_R6L102_005|T_C22_R6L102_006|T_C22_R6L102_007",7,3,3,low,canonical_shadow_only,"not production; source_proxy repair still needed"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C22_R6L102_001","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"holdco_capital_return_CSM_KICS_bridge_positive"}
{"row_type":"case","case_id":"C22_R6L102_002","symbol":"244920","company_name":"에이플러스에셋","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"insurance_distribution_commission_margin_bridge_positive"}
{"row_type":"case","case_id":"C22_R6L102_003","symbol":"211050","company_name":"인카금융서비스","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"GA_market_share_retention_bridge_positive_after_corporate_action_window"}
{"row_type":"case","case_id":"C22_R6L102_004","symbol":"003690","company_name":"코리안리","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_reinsurance_rate_label_trigger_after_loop101","independent_evidence_weight":0.5,"score_price_alignment":"residual_guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"reinsurance_rate_label_without_margin_revision_bridge"}
{"row_type":"case","case_id":"C22_R6L102_005","symbol":"000370","company_name":"한화손해보험","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_reserve_risk_trigger_after_loop101","independent_evidence_weight":0.5,"score_price_alignment":"residual_guardrail_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"loss_ratio_reserve_break_4B_watch"}
{"row_type":"case","case_id":"C22_R6L102_006","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_transaction_premium_to_4C_trigger_after_loop100","independent_evidence_weight":0.5,"score_price_alignment":"residual_guardrail_needed","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"transaction_premium_fade_reserve_capital_4C"}
{"row_type":"case","case_id":"C22_R6L102_007","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Green","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_green_confirmation_trigger_after_loop100","independent_evidence_weight":0.5,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"quality_nonlife_CSM_capital_return_green_confirmed"}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_001","case_id":"C22_R6L102_001","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":72900,"evidence_available_at_that_date":"capital_return_policy; CSM/K-ICS visibility; rate-cycle ROE bridge","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":["capital_return_policy","CSM/K-ICS visibility","rate-cycle ROE bridge"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv","profile_path":"atlas/symbol_profiles/138/138040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.4,"MFE_90D_pct":33.8,"MFE_180D_pct":41.6,"MAE_30D_pct":-4.8,"MAE_90D_pct":-8.7,"MAE_180D_pct":-10.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":103200,"drawdown_after_peak_pct":-52.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"holdco_capital_return_CSM_KICS_bridge_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|138040|Stage2-Actionable|2024-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_002","case_id":"C22_R6L102_002","symbol":"244920","company_name":"에이플러스에셋","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":7520,"evidence_available_at_that_date":"GA commission retention; margin bridge; repeat-policy sales","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":["GA commission retention"],"stage3_evidence_fields":["GA commission retention","margin bridge","repeat-policy sales"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/244/244920/2024.csv","profile_path":"atlas/symbol_profiles/244/244920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.6,"MFE_90D_pct":29.5,"MFE_180D_pct":54.2,"MAE_30D_pct":-3.9,"MAE_90D_pct":-10.4,"MAE_180D_pct":-13.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-08","peak_price":11590,"drawdown_after_peak_pct":-68.0,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"insurance_distribution_commission_margin_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|244920|Stage3-Yellow|2024-07-12","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_003","case_id":"C22_R6L102_003","symbol":"211050","company_name":"인카금융서비스","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-07","entry_date":"2024-06-10","entry_price":6640,"evidence_available_at_that_date":"post-corporate-action clean window; distribution margin bridge; retention growth","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":["post-corporate-action clean window","distribution margin bridge","retention growth"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/211/211050/2024.csv","profile_path":"atlas/symbol_profiles/211/211050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.3,"MFE_90D_pct":36.7,"MFE_180D_pct":58.4,"MAE_30D_pct":-7.8,"MAE_90D_pct":-12.6,"MAE_180D_pct":-18.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-13","peak_price":10520,"drawdown_after_peak_pct":-76.8,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"GA_market_share_retention_bridge_positive_after_corporate_action_window","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|211050|Stage2-Actionable|2024-06-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_004","case_id":"C22_R6L102_004","symbol":"003690","company_name":"코리안리","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-03-13","entry_date":"2024-03-14","entry_price":8170,"evidence_available_at_that_date":"reinsurance rate label; weak revision bridge; large-catastrophe reserve uncertainty","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":["reinsurance rate label","weak revision bridge","large-catastrophe reserve uncertainty"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv","profile_path":"atlas/symbol_profiles/003/003690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.1,"MFE_90D_pct":17.6,"MFE_180D_pct":21.4,"MAE_30D_pct":-8.2,"MAE_90D_pct":-15.7,"MAE_180D_pct":-21.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":9920,"drawdown_after_peak_pct":-43.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"reinsurance_rate_label_without_margin_revision_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|003690|Stage2|2024-03-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_reinsurance_rate_label_trigger_after_loop101","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_005","case_id":"C22_R6L102_005","symbol":"000370","company_name":"한화손해보험","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-05-21","entry_date":"2024-05-22","entry_price":5050,"evidence_available_at_that_date":"loss-ratio volatility; reserve risk; capital-return label overheat","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["loss-ratio volatility","reserve risk","capital-return label overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","profile_path":"atlas/symbol_profiles/000/000370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.7,"MFE_90D_pct":8.4,"MFE_180D_pct":24.5,"MAE_30D_pct":-13.6,"MAE_90D_pct":-22.4,"MAE_180D_pct":-28.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":6290,"drawdown_after_peak_pct":-52.6,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.64,"four_b_timing_verdict":"good_local_4B_watch_not_full_4B","four_b_evidence_type":["reserve_risk","capital_return_label_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"loss_ratio_reserve_break_4B_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000370|Stage4B|2024-05-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_reserve_risk_trigger_after_loop101","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_006","case_id":"C22_R6L102_006","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-04-19","entry_date":"2024-04-22","entry_price":3350,"evidence_available_at_that_date":"transaction premium faded; capital adequacy uncertainty; reserve/capital break","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["transaction premium faded","capital adequacy uncertainty","reserve/capital break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.4,"MFE_90D_pct":7.2,"MFE_180D_pct":10.5,"MAE_30D_pct":-16.1,"MAE_90D_pct":-32.5,"MAE_180D_pct":-44.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":3700,"drawdown_after_peak_pct":-54.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"transaction_premium_fade_reserve_capital_4C","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000400|Stage4C|2024-04-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_transaction_premium_to_4C_trigger_after_loop100","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C22_R6L102_007","case_id":"C22_R6L102_007","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_DISTRIBUTION_REINSURANCE_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE_V3","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Green","trigger_date":"2024-11-15","entry_date":"2024-11-18","entry_price":375000,"evidence_available_at_that_date":"underwriting quality; CSM/K-ICS visibility; capital return confirmation","evidence_source":"source_proxy_only_pending_url_repair","stage2_evidence_fields":["underwriting quality"],"stage3_evidence_fields":["underwriting quality","CSM/K-ICS visibility","capital return confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.6,"MFE_90D_pct":28.9,"MFE_180D_pct":44.8,"MAE_30D_pct":-3.4,"MAE_90D_pct":-8.8,"MAE_180D_pct":-11.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-14","peak_price":543000,"drawdown_after_peak_pct":-56.0,"green_lateness_ratio":0.28,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"quality_nonlife_CSM_capital_return_green_confirmed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage3-Green|2024-11-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_green_confirmation_trigger_after_loop100","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_001","trigger_id":"T_C22_R6L102_001","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":8,"reserve_quality_score":7},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":33.8,"MAE_90D_pct":-8.7,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_002","trigger_id":"T_C22_R6L102_002","symbol":"244920","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":8,"reserve_quality_score":7},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":29.5,"MAE_90D_pct":-10.4,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_003","trigger_id":"T_C22_R6L102_003","symbol":"211050","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":8,"reserve_quality_score":7},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":36.7,"MAE_90D_pct":-12.6,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_004","trigger_id":"T_C22_R6L102_004","symbol":"003690","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":7,"CSM_KICS_capital_return_score":3,"reserve_quality_score":2},"weighted_score_after":66,"stage_label_after":"Stage4B_watch","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":17.6,"MAE_90D_pct":-15.7,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_005","trigger_id":"T_C22_R6L102_005","symbol":"000370","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":7,"CSM_KICS_capital_return_score":3,"reserve_quality_score":2},"weighted_score_after":66,"stage_label_after":"Stage4B_watch","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":8.4,"MAE_90D_pct":-22.4,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_006","trigger_id":"T_C22_R6L102_006","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":7,"CSM_KICS_capital_return_score":3,"reserve_quality_score":2},"weighted_score_after":66,"stage_label_after":"Stage4B_watch","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":7.2,"MAE_90D_pct":-32.5,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"C22_canonical_shadow_profile_v3","case_id":"C22_R6L102_007","trigger_id":"T_C22_R6L102_007","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":6,"reserve_quality_score":5},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":4,"CSM_KICS_capital_return_score":8,"reserve_quality_score":7},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["CSM_KICS_capital_return_score","reserve_quality_score","margin_bridge_score"],"component_delta_explanation":"C22 shadow gate separates verified CSM/K-ICS/reserve/capital-return bridge from generic rate/value-up label.","MFE_90D_pct":28.9,"MAE_90D_pct":-8.8,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R6","loop":"102","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":4,"new_symbol_count":3,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage","hard_4c_confirmation"],"residual_error_types_found":["rate_or_valueup_label_false_positive","reserve_quality_4B_watch","transaction_premium_4C_late","insurance_distribution_positive_missed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

expected_v12_result_file: `true`  
filename_pattern_pass: `true`  
metadata_filename_consistency: `pass`  
jsonl_trigger_row_count: `7`  
calibration_usable_trigger_count: `7`  
representative_trigger_count: `7`  
new_weight_evidence_candidate_count: `3`  
guardrail_candidate_count: `5`  
narrative_only_or_rejected_count: `0`  
rows_missing_required_mfe_mae: `0`  
rows_missing_entry_price_or_date: `0`  
rows_with_noncanonical_trigger_type: `0`  
rows_with_compact_mfe_mae_alias_only: `0`  
ready_for_batch_ingest: `true`

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

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

## 27. Next Round State

completed_round = `R6`  
completed_loop = `102`  
selection_basis = `docs/core/V12_Research_No_Repeat_Index.md`  
selected_priority_bucket = `Priority 2 quality_repair_after_local_priority0_priority1_fill`  
next_recommended_archetypes = `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`, `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`, `C19_BRAND_RETAIL_INVENTORY_MARGIN`, `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT`, `C22_INSURANCE_RATE_CYCLE_RESERVE`, `C24_BIO_TRIAL_DATA_EVENT_RISK`  
round_schedule_status = `coverage_index_selected`  
round_sector_consistency = `pass`

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` used as execution prompt.
- `docs/core/V12_Research_No_Repeat_Index.md` used only as duplicate/coverage ledger.
- `Songdaiki/stock-web` manifest max date: `2026-02-20`.
