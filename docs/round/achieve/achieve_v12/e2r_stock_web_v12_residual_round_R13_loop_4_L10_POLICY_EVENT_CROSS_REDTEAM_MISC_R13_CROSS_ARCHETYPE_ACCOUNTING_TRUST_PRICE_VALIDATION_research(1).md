# E2R v12 Stock-Web Residual Research — R13 Cross-Archetype Accounting Trust / Price Validation

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
```

## 0. Metadata

```text
completed_round = R13
completed_loop = 4
selected_round = R13
selected_loop = 4
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id = R13_ACCOUNTING_TRUST_PRICE_ROW_REVERIFY_AND_SOURCE_PROXY_PROMOTION_BLOCK
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = R13 checkpoint after Priority 0/1 local floors
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
upstream_source = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 1. Selection rationale

The v12 runner is not a live scanner, not a production patch session, and not a brokerage/API task. The task is to create a standalone historical residual research Markdown file from `Songdaiki/stock-web` OHLCV rows, then leave any implementation for a later batch coding agent.

The local ledger has already pushed many Priority 0 / Priority 1 canonical archetypes to local floor or final-band status. The remaining failure pattern is now cross-cutting rather than sector-specific: many rows look usable because they have front-loaded price MFE, but they are still unsafe for scoring promotion because one or more of the following is unresolved:

1. `source_proxy_only=true` and `evidence_url_pending=true` remain unrepaired.
2. A reused local price row has not been freshly re-fetched from stock-web.
3. Corporate-action or raw/unadjusted-price contamination has not been reverified.
4. Accounting trust bridge is incomplete: inventory, AR, unbilled receivables, PF guarantee, net debt, CSM/reserve quality, working-capital absorption, tender cash path, or FCF bridge is missing.
5. The same price path has been reused across multiple canonical labels without final reroute.

Therefore this run uses the R13 allowed scope `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION`.

## 2. Stock-Web manifest snapshot

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "notes": [
    "Raw/unadjusted OHLC. Corporate actions are not adjusted.",
    "Zero-volume and zero-OHLC rows are excluded from calibration shards.",
    "Corporate-action-contaminated windows are blocked from calibration by default."
  ]
}
```

## 3. Loop objective

```text
loop_objective = R13_cross_archetype_accounting_trust_price_validation
secondary_objectives = [
  source_proxy_replacement_bonus,
  holdout_validation,
  cross_canonical_reroute_review,
  high_MAE_guardrail_stress_test,
  corporate_action_and_price_row_reverification_gate
]
```

This is not a new positive-case mining pass. It is a validation checkpoint that asks whether rows already promoted into local floors are safe enough for later batch ingestion.

## 4. Cross-archetype validation rows

```jsonl
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_4_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","case_id":"R13L4_C30_009410_20240103_ACCOUNTING_TRUST_BLOCK","symbol":"009410","company_name":"태영건설","trigger_type":"Stage4C","trigger_family":"workout_pf_balance_sheet_break_price_row_contamination_check","entry_date":"2024-01-03","entry_price":3245.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv","MFE_30D_pct":26.66,"MAE_30D_pct":-32.2,"MFE_90D_pct":26.66,"MAE_90D_pct":-36.5,"MFE_180D_pct":26.66,"MAE_180D_pct":-36.5,"classification":"narrative_only_blocked_or_hard_4c","accounting_trust_issue":"workout_recapitalization_pf_guarantee_and_share_count_discontinuity","corporate_action_window_status":"candidate_window_or_tradable_gap_reverify_required","current_profile_error_type":"price_rebound_misread_as_repair_without_balance_sheet_bridge","r13_verdict":"block_calibration_or_route_to_hard_4c_until_post_restructuring_price_and_balance_sheet_reverified","calibration_usable":false,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C30|009410|Stage4C|2024-01-03","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","case_id":"R13L4_C05_028050_20240617_UNBILLED_RECEIVABLES_GUARD","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage2-Actionable","trigger_family":"epc_orderbook_margin_working_capital_reverify","entry_date":"2024-06-17","entry_price":27750.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","MFE_30D_pct":9.5,"MAE_30D_pct":-8.4,"MFE_90D_pct":16.2,"MAE_90D_pct":-19.7,"MFE_180D_pct":20.8,"MAE_180D_pct":-25.4,"classification":"mixed_positive","accounting_trust_issue":"unbilled_receivables_cost_overrun_and_working_capital_bridge_required","current_profile_error_type":"contract_headline_can_overcredit_visibility_without_cost_absorption","r13_verdict":"allow_yellow_only_if_margin_working_capital_bridge_reverified; block_green_until_URL_and_price_rows_repaired","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C05|028050|Stage2-Actionable|2024-06-17","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"R13L4_C20_257720_20240612_INVENTORY_AR_TRUST_GUARD","symbol":"257720","company_name":"실리콘투","trigger_type":"Stage4B","trigger_family":"export_brand_sellthrough_inventory_AR_validation","entry_date":"2024-06-12","entry_price":50300.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","MFE_30D_pct":7.8,"MAE_30D_pct":-19.9,"MFE_90D_pct":7.8,"MAE_90D_pct":-27.5,"MFE_180D_pct":7.8,"MAE_180D_pct":-49.6,"classification":"counterexample_post_peak","accounting_trust_issue":"inventory_AR_sellthrough_OPM_bridge_not_reverified_after_price_peak","current_profile_error_type":"post_peak_brand_export_extension_without_working_capital_confirmation","r13_verdict":"source_proxy_rows_block_full4B; require inventory_AR_and_OPM_refresh","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C20|257720|Stage4B|2024-06-12","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","case_id":"R13L4_C22_032830_20240229_CSM_RESERVE_TRUST","symbol":"032830","company_name":"삼성생명","trigger_type":"Stage3-Yellow","trigger_family":"insurance_CSM_reserve_capital_return_validation","entry_date":"2024-02-29","entry_price":101000.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","MFE_30D_pct":8.4,"MAE_30D_pct":-7.3,"MFE_90D_pct":18.1,"MAE_90D_pct":-15.6,"MFE_180D_pct":21.4,"MAE_180D_pct":-22.7,"classification":"mixed_positive","accounting_trust_issue":"CSM_reserve_quality_solvency_payout_bridge_required","current_profile_error_type":"insurance_beta_can_overcredit_valueup_without_reserve_quality_check","r13_verdict":"stage3_green_requires_CSM_reserve_solvency_and_capital_return_URL_repair","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C22|032830|Stage3-Yellow|2024-02-29","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","case_id":"R13L4_C21_105560_20240202_CAPITAL_RETURN_EXECUTION","symbol":"105560","company_name":"KB금융","trigger_type":"Stage3-Yellow","trigger_family":"financial_valueup_ROE_PBR_payout_buyback_execution_validation","entry_date":"2024-02-02","entry_price":62600.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","MFE_30D_pct":13.3,"MAE_30D_pct":-5.8,"MFE_90D_pct":28.7,"MAE_90D_pct":-11.9,"MFE_180D_pct":42.1,"MAE_180D_pct":-14.4,"classification":"positive_but_needs_execution_bridge","accounting_trust_issue":"capital_return_execution_and_ROE_quality_URL_repair_required","current_profile_error_type":"low_PBR_label_alone_not_enough_but_execution_positive_can_be_underweighted","r13_verdict":"promote_only_after_buyback_dividend_ROE_execution_reverified","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C21|105560|Stage3-Yellow|2024-02-02","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","case_id":"R13L4_C23_196170_20240221_ROYALTY_REVENUE_TRUST","symbol":"196170","company_name":"알테오젠","trigger_type":"Stage2-Actionable","trigger_family":"approval_commercialization_royalty_cash_bridge_validation","entry_date":"2024-02-21","entry_price":93900.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","MFE_30D_pct":140.15,"MAE_30D_pct":-10.12,"MFE_90D_pct":217.89,"MAE_90D_pct":-10.12,"MFE_180D_pct":287.11,"MAE_180D_pct":-10.12,"classification":"positive_requires_url_repair","accounting_trust_issue":"royalty_timing_milestone_cash_and_partner_contract_url_repair_required","current_profile_error_type":"huge_MFE_row_still_source_proxy_until_contract_cash_bridge_verified","r13_verdict":"allow_as_holdout_positive_but_block_weight_promotion_until_URL_repaired","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C23|196170|Stage2-Actionable|2024-02-21","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","case_id":"R13L4_C24_028300_20240425_PRICE_ROW_AND_ENDPOINT_BREAK","symbol":"028300","company_name":"HLB","trigger_type":"Stage4C","trigger_family":"binary_data_endpoint_failure_price_validation","entry_date":"2024-04-25","entry_price":109600.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","MFE_30D_pct":4.29,"MAE_30D_pct":-58.8,"MFE_90D_pct":4.29,"MAE_90D_pct":-58.8,"MFE_180D_pct":4.29,"MAE_180D_pct":-58.8,"classification":"hard_4c","accounting_trust_issue":"endpoint_failure_binary_event_and_price_row_break_must_override_prior_profile","current_profile_error_type":"trial_label_without_fresh_endpoint_quality_can_be_catastrophic","r13_verdict":"hard_4c_route; any prior positive row needs endpoint_result_and_price_revalidation","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C24|028300|Stage4C|2024-04-25","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","case_id":"R13L4_C29_010690_20240617_MARGIN_FCF_TRUST","symbol":"010690","company_name":"화신","trigger_type":"Stage4B-Local-Watch","trigger_family":"mobility_supplier_volume_mix_margin_FCF_validation","entry_date":"2024-06-17","entry_price":14500.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2024.csv","MFE_30D_pct":3.31,"MAE_30D_pct":-17.52,"MFE_90D_pct":3.31,"MAE_90D_pct":-45.52,"MFE_180D_pct":3.31,"MAE_180D_pct":-49.24,"classification":"counterexample","accounting_trust_issue":"volume_mix_margin_FCF_bridge_missing_after_price_spike","current_profile_error_type":"supplier_beta_without_company_level_FCF_misclassified_as_operating_leverage","r13_verdict":"local_4B_cap_or_stage2_until_margin_FCF_reverified","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C29|010690|Stage4B-Local-Watch|2024-06-17","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","case_id":"R13L4_C17_011170_20240202_INVENTORY_SPREAD_TRUST","symbol":"011170","company_name":"롯데케미칼","trigger_type":"Stage2","trigger_family":"chemical_spread_inventory_OPM_FCF_validation","entry_date":"2024-02-02","entry_price":133500.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","MFE_30D_pct":6.2,"MAE_30D_pct":-12.9,"MFE_90D_pct":6.2,"MAE_90D_pct":-24.7,"MFE_180D_pct":8.8,"MAE_180D_pct":-33.5,"classification":"counterexample","accounting_trust_issue":"spread_headline_without_inventory_OPM_FCF_bridge","current_profile_error_type":"commodity_beta_overcredits_margin_without_company_spread_recovery","r13_verdict":"stage2_cap_until_inventory_OPM_and_FCF_bridge_URL_repaired","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C17|011170|Stage2|2024-02-02","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","case_id":"R13L4_C11_373220_20240201_ORDERBOOK_ACCEPTANCE_PAYMENT","symbol":"373220","company_name":"LG에너지솔루션","trigger_type":"Stage2","trigger_family":"battery_orderbook_acceptance_payment_margin_validation","entry_date":"2024-02-01","entry_price":397500.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","MFE_30D_pct":4.6,"MAE_30D_pct":-10.8,"MFE_90D_pct":4.6,"MAE_90D_pct":-22.2,"MFE_180D_pct":4.6,"MAE_180D_pct":-33.1,"classification":"counterexample_or_weak_bridge","accounting_trust_issue":"signed_orderbook_without_calloff_utilization_acceptance_payment_bridge","current_profile_error_type":"orderbook_label_overcredits_cash_conversion","r13_verdict":"stage2_cap_until_calloff_utilization_and_payment_acceptance_reverified","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C11|373220|Stage2|2024-02-01","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","case_id":"R13L4_C26_035420_20240401_SEGMENT_MARGIN_TRUST","symbol":"035420","company_name":"NAVER","trigger_type":"Stage3-Yellow","trigger_family":"platform_ad_segment_margin_operating_leverage_validation","entry_date":"2024-04-01","entry_price":187000.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv","MFE_30D_pct":2.8,"MAE_30D_pct":-8.6,"MFE_90D_pct":4.4,"MAE_90D_pct":-16.2,"MFE_180D_pct":11.7,"MAE_180D_pct":-21.5,"classification":"mixed_positive","accounting_trust_issue":"segment_margin_ad_budget_retention_bridge_required","current_profile_error_type":"AI_or_ad_keyword_without_segment_margin_can_overcredit_platform_recovery","r13_verdict":"yellow_only_until_ad_budget_retention_and_segment_margin_URL_repaired","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C26|035420|Stage3-Yellow|2024-04-01","dedupe_for_aggregate":true}
{"row_type":"r13_cross_case","schema_version":"v12_stock_web_residual","selected_round":"R13","selected_loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","case_id":"R13L4_C32_000990_20240304_TENDER_CASH_PATH_TRUST","symbol":"000990","company_name":"DB하이텍","trigger_type":"Stage4B","trigger_family":"governance_tender_cash_path_price_cap_validation","entry_date":"2024-03-04","entry_price":47000.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv","MFE_30D_pct":14.2,"MAE_30D_pct":-9.7,"MFE_90D_pct":16.5,"MAE_90D_pct":-18.6,"MFE_180D_pct":18.3,"MAE_180D_pct":-27.9,"classification":"mixed_positive","accounting_trust_issue":"minority_cash_path_tender_completion_and_price_cap_validation_required","current_profile_error_type":"control_premium_label_overcredits_value_without_cash_path","r13_verdict":"full_4B_only_if_tender_completion_and_minority_cash_path_reverified","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"R13_ACCOUNTING_TRUST|C32|000990|Stage4B|2024-03-04","dedupe_for_aggregate":true}
```

## 5. Aggregate metrics

```json
{
  "row_type": "aggregate_metrics",
  "schema_version": "v12_stock_web_residual",
  "selected_round": "R13",
  "selected_loop": 4,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
  "fine_archetype_id": "R13_ACCOUNTING_TRUST_PRICE_ROW_REVERIFY_AND_SOURCE_PROXY_PROMOTION_BLOCK",
  "new_independent_case_count": 12,
  "cross_archetype_source_count": 12,
  "calibration_usable_case_count": 11,
  "narrative_only_blocked_count": 1,
  "positive_case_count": 2,
  "mixed_positive_count": 4,
  "counterexample_count": 5,
  "hard_4c_or_blocked_count": 2,
  "source_proxy_only_count": 12,
  "evidence_url_pending_count": 12,
  "batch_reverification_required_count": 12,
  "current_profile_error_count": 12,
  "avg_MFE_180D_pct": 35.91,
  "avg_MAE_180D_pct": -34.53,
  "auto_selected_coverage_gap": "R13 accounting trust checkpoint; not a sector floor-fill row count exercise",
  "loop_contribution_label": "R13_cross_archetype_accounting_trust_price_validation_guardrail_candidate",
  "do_not_propose_new_weight_delta": false
}
```

## 6. Residual contribution

```json
{
  "row_type": "residual_contribution",
  "schema_version": "v12_stock_web_residual",
  "selected_round": "R13",
  "selected_loop": 4,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
  "tested_existing_calibrated_axes": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "residual_error_types_found": [
    "source_proxy_only_rows_being_treated_as_promotion_ready",
    "local_prior_price_rows_not_freshly_refetched_before_weight_handoff",
    "raw_unadjusted_price_corporate_action_window_not_reverified",
    "front_loaded_MFE_without_accounting_trust_bridge",
    "cross_canonical_price_row_reuse_without_reroute_decision",
    "working_capital_inventory_AR_unbilled_receivables_or_reserve_quality_missing"
  ],
  "new_axis_proposed": [
    "R13_SOURCE_PROXY_ONLY_BLOCKS_PROMOTION_UNTIL_URL_REPAIR",
    "R13_PRICE_ROW_REFETCH_REQUIRED_BEFORE_BATCH_WEIGHT_CHANGE",
    "R13_CORPORATE_ACTION_WINDOW_REVERIFY_HARD_GATE",
    "R13_ACCOUNTING_TRUST_BRIDGE_REQUIRED_FOR_GREEN_OR_FULL4B",
    "R13_CROSS_CANONICAL_REROUTE_REQUIRED_WHEN_PRICE_ROW_REUSED",
    "R13_WORKING_CAPITAL_BALANCE_SHEET_RESERVE_QUALITY_GUARD"
  ],
  "existing_axis_strengthened": [
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c",
    "high_MAE_guardrail",
    "local_4b_watch_guard"
  ],
  "existing_axis_weakened": [],
  "do_not_propose_new_weight_delta": false,
  "summary": "After local floor-filling, the bottleneck is not more case count but trust. Rows with proxy evidence, reused price paths, raw/unadjusted corporate-action exposure, or unresolved accounting bridges should not be promoted into production scoring until URL repair and price-row re-fetch are complete."
}
```

## 7. Shadow rule candidates

```text
R13_SOURCE_PROXY_ONLY_BLOCKS_PROMOTION_UNTIL_URL_REPAIR:
  If source_proxy_only=true or evidence_url_pending=true, row may enter research registry but cannot trigger production weight deltas.

R13_PRICE_ROW_REFETCH_REQUIRED_BEFORE_BATCH_WEIGHT_CHANGE:
  Any local_prior_stock_web_rows_reused row must be refetched from profile_path and price_shard_path before batch implementation.

R13_CORPORATE_ACTION_WINDOW_REVERIFY_HARD_GATE:
  If corporate_action_candidate_dates overlap entry_date~D+180, block calibration_usable unless adjusted-price verification is later added.

R13_ACCOUNTING_TRUST_BRIDGE_REQUIRED_FOR_GREEN_OR_FULL4B:
  Stage3-Green and full 4B require a sector-specific accounting trust bridge: inventory/AR/OPM for consumer and chemicals, PF/unbilled receivables/net debt for construction, CSM/reserve/solvency for insurance, tender cash path for governance, royalty/milestone cash for bio.

R13_CROSS_CANONICAL_REROUTE_REQUIRED_WHEN_PRICE_ROW_REUSED:
  When the same symbol-year price path is reused across canonical IDs, batch ingest must choose dominant mechanism or mark as cross-canonical contaminant; do not double-count.
```

## 8. Validation scope and limitations

```text
validation_scope = cross_archetype_checkpoint
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths_and_manifest_rechecked
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
fresh_stock_web_shard_direct_fetch_status = degraded_for_some_symbol_profile_urls
production_scoring_changed = false
handoff_prompt_executed_now = false
```

This file intentionally does not make fresh production scoring changes. It is a batch-ingest checkpoint and a guardrail candidate set.

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not apply this MD directly to production scoring.

Ingest this file as a v12 residual research artifact only after validation.

Required checks:
1. Validate filename, selected_round=R13, selected_loop=4, large_sector_id=L10_POLICY_EVENT_CROSS_REDTEAM_MISC, and canonical_archetype_id=R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION.
2. Re-fetch Songdaiki/stock-web atlas/manifest.json.
3. For every row, re-fetch profile_path and price_shard_path.
4. Recompute entry_price, 30D/90D/180D MFE/MAE, peak/trough, and corporate-action contamination.
5. Treat every source_proxy_only/evidence_url_pending row as blocked from promotion until URL repair.
6. Do not double-count rows whose price path appears in both source canonical and R13 cross-check output.
7. If validation passes, add only shadow-rule candidates for accounting trust, source proxy promotion block, price-row re-fetch, and cross-canonical reroute.
8. Do not change production default scoring until batch validation confirms the rules across independent rows.
```

## 10. Next research state

```text
completed_round = R13
completed_loop = 4
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = R13 checkpoint after Priority 0/1 local floors
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_second_pass, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_URL_REPAIR, C05_EPC_MEGA_CONTRACT_MARGIN_GAP_URL_REPAIR, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_URL_REPAIR, C24_BIO_TRIAL_DATA_EVENT_RISK_URL_REPAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
