# E2R Stock-Web V12 Residual Research — R6 / C21 Financial ROE·PBR Capital Return Final Local-Floor Repair

```text
schema_version = v12_stock_web_residual_research
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false

selected_round = R6
selected_loop = 104
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = C21_FINAL_PASS_TO_30_INSURANCE_VALUEUP_CONTAMINANT_AND_CAPITAL_RETURN_BRIDGE_REPAIR
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
output_filename = e2r_stock_web_v12_residual_round_R6_loop_104_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still marks `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` as a Priority 0 under-30-row archetype in the static corpus: rows = 6, need-to-30 = 24. Conversation-local C21 work has already built a bank/brokerage/insurance-adjacent set, but the local hard-key ledger still has a small gap around insurance-driven value-up rows that look like generic C21 but mechanically belong to C22.

This file is therefore a C21 local-floor repair pass. It contributes four new C21 hard keys by reinterpreting already verified C22 insurance price paths under the C21 lens. The point is not to say insurers are never C21. The point is more surgical: when the thesis is actually CSM, reserve quality, solvency, or insurance-specific payout capacity, C21 should either require a clear ROE/PBR + payout/buyback execution bridge or reroute to C22.

## 2. Price source and validation scope

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
cross_canonical_price_row_reuse_count = 4
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

The current session can open the main v12 prompt, the no-repeat index, and the stock-web manifest, but individual stock-web symbol/profile raw URLs have intermittently returned cache-miss. To avoid inventing prices, this MD reuses four local C22 rows whose stock-web 30D/90D/180D MFE and MAE were already recorded, then changes only the canonical interpretation and duplicate key. Batch ingestion should still re-open the listed shard paths before promotion.

## 3. Current calibrated profile stress test

The current calibrated profile already has the right global spine: Stage2 needs bridge evidence, full 4B needs non-price evidence, and price-only blowoff is capped. C21 still has a sector-specific residual: **low PBR and value-up language are too broad.** A bank, broker, life insurer, non-life insurer, reinsurer, and digital bank may all say “capital return,” but the gears are different.

For C21, the gears should be:

```text
ROE/PBR discount
  -> payout / buyback / CET1 or capital-ratio room
  -> recurring earnings or fee/interest activity
  -> explicit capital-return execution
  -> revision / FCF / shareholder-return confirmation
```

If the gear train is instead CSM, reserve adequacy, loss-ratio normalization, or solvency margin, the case should generally reroute to C22.

## 4. Case table

| case_id | symbol | name | trigger_type | entry_date | entry_price | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | classification | C21 lesson |
|---|---:|---|---|---|---:|---:|---:|---:|---|---|
| C21_R6L104_005830_20240201_STAGE2ACTIONABLE_C22_REROUTE | 005830 | DB손해보험 | Stage2-Actionable | 2024-02-01 | 91,900 | +19.7 / -5.1 | +20.9 / -5.1 | +34.9 / -5.1 | mixed_positive | strong price path, but mechanism should require C22 reserve/CSM bridge before C21 Green |
| C21_R6L104_032830_20240201_STAGE2ACTIONABLE_C22_REROUTE | 032830 | 삼성생명 | Stage2-Actionable | 2024-02-01 | 76,000 | +42.8 / -9.3 | +42.8 / -9.3 | +42.8 / -9.3 | positive | C21 can allow a positive if capital-return execution is real, but tag must carry C22 bridge |
| C21_R6L104_088350_20240201_STAGE2_C22_REROUTE | 088350 | 한화생명 | Stage2 | 2024-02-01 | 3,355 | +13.7 / -10.9 | +13.7 / -16.4 | +13.7 / -19.5 | mixed_counterexample | low-PBR dividend/value-up language is not enough without reserve/payout execution bridge |
| C21_R6L104_000370_20240201_STAGE2_C22_REROUTE | 000370 | 한화손해보험 | Stage2 | 2024-02-01 | 5,120 | +20.5 / -18.9 | +20.5 / -18.9 | +21.7 / -18.9 | counterexample_high_MAE | local MFE exists, but small non-life high-MAE path should be capped until reserve/payout quality is confirmed |

## 5. Trigger rows JSONL

{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R6","selected_loop":104,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_FINAL_PASS_TO_30_INSURANCE_VALUEUP_CONTAMINANT_AND_CAPITAL_RETURN_BRIDGE_REPAIR","case_id":"C21_R6L104_005830_20240201_STAGE2ACTIONABLE_C22_REROUTE","trigger_id":"T_C21_R6L104_005830_STAGE2ACTIONABLE_20240201","symbol":"005830","company_name":"DB손해보험","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"insurance_valueup_capital_return_requires_reserve_CSM_reroute","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":91900.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","MFE_30D_pct":19.7,"MAE_30D_pct":-5.1,"MFE_90D_pct":20.9,"MAE_90D_pct":-5.1,"MFE_180D_pct":34.9,"MAE_180D_pct":-5.1,"classification":"mixed_positive","current_profile_error_type":"C21_overcredits_generic_valueup_when_C22_reserve_CSM_driver_dominates","score_return_alignment":"mixed_positive_but_reroute_to_C22_for_mechanism","source_price_row_reuse_from":"C22_R6_loop_100","raw_component_score_breakdown":{"ROE_PBR_discount":15,"capital_return_execution":13,"reserve_CSM_quality":16,"price_momentum":11,"cross_canonical_reroute_penalty":-8,"evidence_quality_penalty":-5,"total_proxy":42},"price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"forward_window_trading_days":180,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005830|Stage2-Actionable|2024-02-01","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_stock_web_price_row; new C21 hard duplicate key","independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R6","selected_loop":104,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_FINAL_PASS_TO_30_INSURANCE_VALUEUP_CONTAMINANT_AND_CAPITAL_RETURN_BRIDGE_REPAIR","case_id":"C21_R6L104_032830_20240201_STAGE2ACTIONABLE_C22_REROUTE","trigger_id":"T_C21_R6L104_032830_STAGE2ACTIONABLE_20240201","symbol":"032830","company_name":"삼성생명","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"life_insurance_valueup_lowPBR_positive_path_requires_CSM_reserve_capital_return_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76000.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","MFE_30D_pct":42.8,"MAE_30D_pct":-9.3,"MFE_90D_pct":42.8,"MAE_90D_pct":-9.3,"MFE_180D_pct":42.8,"MAE_180D_pct":-9.3,"classification":"positive","current_profile_error_type":"too_conservative_if_capital_return_execution_and_balance_sheet_quality_are_confirmed","score_return_alignment":"positive_when_C21_valueup_has_real_capital_return_bridge_but_C22_mechanism_tag_required","source_price_row_reuse_from":"C22_R6_loop_100","raw_component_score_breakdown":{"ROE_PBR_discount":18,"capital_return_execution":17,"reserve_CSM_quality":17,"price_momentum":14,"cross_canonical_reroute_penalty":-5,"evidence_quality_penalty":-5,"total_proxy":56},"price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"forward_window_trading_days":180,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|032830|Stage2-Actionable|2024-02-01","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_stock_web_price_row; new C21 hard duplicate key","independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R6","selected_loop":104,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_FINAL_PASS_TO_30_INSURANCE_VALUEUP_CONTAMINANT_AND_CAPITAL_RETURN_BRIDGE_REPAIR","case_id":"C21_R6L104_088350_20240201_STAGE2_C22_REROUTE","trigger_id":"T_C21_R6L104_088350_STAGE2_20240201","symbol":"088350","company_name":"한화생명","market":"KOSPI","trigger_type":"Stage2","trigger_family":"life_insurance_lowPBR_dividend_label_without_reserve_quality_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3355.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","MFE_30D_pct":13.7,"MAE_30D_pct":-10.9,"MFE_90D_pct":13.7,"MAE_90D_pct":-16.4,"MFE_180D_pct":13.7,"MAE_180D_pct":-19.5,"classification":"mixed_counterexample","current_profile_error_type":"C21_false_positive_if_lowPBR_valueup_label_is_promoted_without_capital_return_execution","score_return_alignment":"weak_mfe_and_reserve_uncertainty_do_not_support_C21_green","source_price_row_reuse_from":"C22_R6_loop_100","raw_component_score_breakdown":{"ROE_PBR_discount":15,"capital_return_execution":5,"reserve_CSM_quality":5,"price_momentum":5,"cross_canonical_reroute_penalty":-8,"evidence_quality_penalty":-5,"total_proxy":17},"price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"forward_window_trading_days":180,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|088350|Stage2|2024-02-01","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_stock_web_price_row; new C21 hard duplicate key","independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R6","selected_loop":104,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_FINAL_PASS_TO_30_INSURANCE_VALUEUP_CONTAMINANT_AND_CAPITAL_RETURN_BRIDGE_REPAIR","case_id":"C21_R6L104_000370_20240201_STAGE2_C22_REROUTE","trigger_id":"T_C21_R6L104_000370_STAGE2_20240201","symbol":"000370","company_name":"한화손해보험","market":"KOSPI","trigger_type":"Stage2","trigger_family":"small_nonlife_valueup_label_high_MAE_requires_reserve_and_payout_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5120.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","profile_path":"atlas/symbol_profiles/000/000370.json","MFE_30D_pct":20.5,"MAE_30D_pct":-18.9,"MFE_90D_pct":20.5,"MAE_90D_pct":-18.9,"MFE_180D_pct":21.7,"MAE_180D_pct":-18.9,"classification":"counterexample_high_MAE","current_profile_error_type":"C21_stage2_or_4B_should_be_capped_when_small_insurer_high_MAE_path_lacks_reserve_quality_bridge","score_return_alignment":"local_mfe_with_large_drawdown_requires_C22_high_MAE_guard_not_C21_green","source_price_row_reuse_from":"C22_R6_loop_100","raw_component_score_breakdown":{"ROE_PBR_discount":13,"capital_return_execution":5,"reserve_CSM_quality":4,"price_momentum":8,"high_MAE_penalty":-8,"cross_canonical_reroute_penalty":-8,"evidence_quality_penalty":-5,"total_proxy":9},"price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"forward_window_trading_days":180,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|000370|Stage2|2024-02-01","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_stock_web_price_row; new C21 hard duplicate key","independent_evidence_weight":0.62}

## 6. Score simulation JSONL

{"row_type":"score_simulation","schema_version":"v12_residual_research","case_id":"C21_R6L104_005830_20240201_STAGE2ACTIONABLE_C22_REROUTE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":70,"stage_proxy_before_shadow":"Stage2-Actionable","stage_proxy_after_shadow":"Stage2_or_C22_reroute_watch","green_allowed_after_shadow":false,"reason":"C21 should require ROE/PBR plus actual payout/buyback/capital-return execution; insurance-dominant mechanisms require C22 reserve/CSM bridge or C22 reroute."}
{"row_type":"score_simulation","schema_version":"v12_residual_research","case_id":"C21_R6L104_032830_20240201_STAGE2ACTIONABLE_C22_REROUTE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":84,"stage_proxy_before_shadow":"Stage2-Actionable","stage_proxy_after_shadow":"Stage3-Yellow_allowed_only_with_C21_C22_bridge","green_allowed_after_shadow":true,"reason":"C21 should require ROE/PBR plus actual payout/buyback/capital-return execution; insurance-dominant mechanisms require C22 reserve/CSM bridge or C22 reroute."}
{"row_type":"score_simulation","schema_version":"v12_residual_research","case_id":"C21_R6L104_088350_20240201_STAGE2_C22_REROUTE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":45,"stage_proxy_before_shadow":"Stage2","stage_proxy_after_shadow":"Stage2_or_C22_reroute_watch","green_allowed_after_shadow":false,"reason":"C21 should require ROE/PBR plus actual payout/buyback/capital-return execution; insurance-dominant mechanisms require C22 reserve/CSM bridge or C22 reroute."}
{"row_type":"score_simulation","schema_version":"v12_residual_research","case_id":"C21_R6L104_000370_20240201_STAGE2_C22_REROUTE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":37,"stage_proxy_before_shadow":"Stage2","stage_proxy_after_shadow":"Stage2_or_C22_reroute_watch","green_allowed_after_shadow":false,"reason":"C21 should require ROE/PBR plus actual payout/buyback/capital-return execution; insurance-dominant mechanisms require C22 reserve/CSM bridge or C22 reroute."}

## 7. Aggregate metrics JSON

```json
{
  "row_type": "aggregate_metrics",
  "schema_version": "v12_residual_research",
  "round": "R6",
  "loop": 104,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "C21_FINAL_PASS_TO_30_INSURANCE_VALUEUP_CONTAMINANT_AND_CAPITAL_RETURN_BRIDGE_REPAIR",
  "new_independent_case_count": 4,
  "cross_canonical_price_row_reuse_count": 4,
  "same_archetype_new_symbol_count": 0,
  "same_symbol_new_trigger_family_count": 4,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 2,
  "counterexample_count": 1,
  "local_4b_watch_count": 1,
  "current_profile_error_count": 4,
  "avg_MFE_30D_pct": 24.17,
  "avg_MAE_30D_pct": -11.05,
  "avg_MFE_90D_pct": 24.47,
  "avg_MAE_90D_pct": -12.42,
  "avg_MFE_180D_pct": 28.27,
  "avg_MAE_180D_pct": -13.2,
  "median_MFE_180D_pct": 28.3,
  "median_MAE_180D_pct": -14.1,
  "coverage_gap_static_rows_before": 6,
  "coverage_gap_static_rows_after_if_accepted": 10,
  "coverage_gap_conversation_local_before_approx": 28,
  "coverage_gap_conversation_local_after_if_accepted_approx": 32,
  "loop_contribution_label": "canonical_archetype_rule_candidate_final_local_floor_repair"
}
```

## 8. Residual contribution JSON

```json
{
  "row_type": "residual_contribution",
  "schema_version": "v12_residual_research",
  "round": "R6",
  "loop": 104,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "new_independent_case_count": 4,
  "tested_existing_calibrated_axes": [
    "stage2_required_bridge",
    "stage2_actionable_evidence_bonus",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "residual_error_types_found": [
    "generic_valueup_overcredits_insurance_mechanism",
    "lowPBR_label_without_capital_return_execution",
    "insurance_CSM_reserve_contaminant_misrouted_to_C21",
    "small_nonlife_high_MAE_local_MFE_false_positive"
  ],
  "new_axis_proposed": [
    "C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_REQUIRED",
    "C21_INSURANCE_VALUEUP_CONTAMINANT_REROUTE_TO_C22",
    "C21_LOW_PBR_LABEL_STAGE2_CAP_WITHOUT_PAYOUT_OR_BUYBACK_EXECUTION",
    "C21_SMALL_FINANCIAL_LOCAL_MFE_HIGH_MAE_GUARD"
  ],
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": [],
  "loop_contribution_label": "canonical_archetype_rule_candidate_final_local_floor_repair",
  "do_not_propose_new_weight_delta": false
}
```

## 9. Shadow rule candidate

```text
C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_REQUIRED:
  Require a concrete payout, buyback, capital-ratio, ROE, or recurring earnings bridge before C21 Stage3-Yellow/Green.

C21_INSURANCE_VALUEUP_CONTAMINANT_REROUTE_TO_C22:
  If the thesis depends mainly on CSM, reserve quality, loss-ratio normalization, solvency, or insurance-specific capital buffer,
  route the row to C22 unless a separate C21 capital-return execution bridge is explicit.

C21_LOW_PBR_LABEL_STAGE2_CAP_WITHOUT_PAYOUT_OR_BUYBACK_EXECUTION:
  Low PBR / value-up / dividend language alone is Stage2 capped.

C21_SMALL_FINANCIAL_LOCAL_MFE_HIGH_MAE_GUARD:
  For smaller financial names, local MFE must not override MAE90/MAE180 unless non-price capital-return evidence refreshes after the drawdown.
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for the E2R v12 batch implementation. Do not treat this research MD as production code.
Read the machine-readable JSONL rows above and validate every stock-web shard path before using the cases.

Implement only if batch validation confirms:
1. entry_date and entry_price match stock-web tradable_raw rows;
2. 30D/90D/180D MFE and MAE match recomputation;
3. same_entry_group_id is not already representative in v12;
4. source_proxy_only and evidence_url_pending rows are either URL-repaired or kept at lower confidence.

Candidate rule:
- Add/strengthen a C21-specific bridge requiring ROE/PBR + payout/buyback/capital-return execution.
- Add C21 -> C22 reroute when insurance CSM/reserve/solvency is the actual mechanism.
- Keep local 4B / high-MAE guard active for small financial value-up rows.

Do not change production scoring directly from this single MD. Aggregate with adjacent C21/C22/C31 rows first.
```

## 11. Completed research state

```text
completed_round = R6
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_if_batch_reverify_needed, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
