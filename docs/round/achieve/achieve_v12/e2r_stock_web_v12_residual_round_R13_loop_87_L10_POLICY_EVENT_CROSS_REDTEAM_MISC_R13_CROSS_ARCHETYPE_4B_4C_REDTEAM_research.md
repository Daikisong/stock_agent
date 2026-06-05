---
schema_family: v12_sector_archetype_residual
selected_round: R13
scheduled_round: R13
selected_loop: 87
scheduled_loop: 87
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM
sector: policy_event_cross_redteam_misc
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
output_file: e2r_stock_web_v12_residual_round_R13_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R13 Loop 87 — Cross-Archetype 4B/4C RedTeam

## 0. Execution Mode

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a standalone R13 red-team checkpoint. It is not a new sector-specific positive research file and it does not propose a production scoring patch.

## 1. Schedule Resolution

Previous completed state observed in this conversation:

```text
completed_round = R12
completed_loop = 87
next_round = R13
next_loop = 87
```

R13 is a cross-archetype checkpoint and must use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`. Selected scope:

```text
scheduled_round = R13
scheduled_loop = 87
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

Output filename follows the hard rule:

```text
e2r_stock_web_v12_residual_round_R13_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

## 2. Price Source Validation

Primary price source is `Songdaiki/stock-web`.

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Manifest values used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
```

Profile and shard paths used or inherited from prior R10/R11/R12 rows:

```text
atlas/symbol_profiles/034/034300.json
atlas/symbol_profiles/005/005960.json
atlas/symbol_profiles/010/010780.json
atlas/symbol_profiles/052/052690.json
atlas/symbol_profiles/051/051600.json
atlas/symbol_profiles/130/130660.json

atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv
atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv
atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv
```

Corporate-action handling:

- `052690`, `051600`, and `130660` have no corporate-action candidate dates in inspected stock-web profiles.
- `034300` has a 2024-02-06 corporate-action candidate, but the R10 entry windows used here begin after that date; the R10 row already marks no overlap for entry-to-D+180.
- `005960` and `010780` have historical corporate-action candidates, but no 2024 candidate overlapping the selected entry-to-D+180 windows in the prior R10 validation rows.

## 3. No-Repeat / R13 Scope Check

No-Repeat Index is used as a duplicate-prevention ledger only.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

R13 review rows are intentionally marked:

```text
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
dedupe_for_aggregate = false
aggregate_group_role = r13_cross_redteam_only
```

This R13 file reuses prior R10/R11/R12 evidence rows as red-team material. It is not counted as new C04/C30/C31 sector evidence and does not add positive coverage to those canonical scopes.

## 4. RedTeam Question

The question for this R13 checkpoint is narrow:

```text
When a policy/PF/project headline produces a fast local peak, should the system treat it as full 4B, hard 4C, or only a local watch?
```

The cross-archetype answer from R10/R11/R12 is:

1. **Price-only local 4B is often real as a local heat signal**, but it is not enough for full 4B unless non-price evidence appears.
2. **Hard 4C should not fire merely because a spike fades.** It needs a thesis break such as legal block, contract cancellation, financing failure, accounting trust break, or persistent cashflow failure.
3. **Earlier thesis-break watch is useful.** C04/C31 legal and contract path risks should live as watch overlays before they become hard 4C.
4. **The same visual price path can mean different things across C04/C30/C31.** A legal-clearance contract bridge can be a valid Stage2 entry; a preferred-bidder-only or macro support-only spike can be a false-positive/high-MAE case.

## 5. Machine-readable R13 review rows

```jsonl
{"row_type":"trigger","trigger_id":"R13L87_4B4C_REVIEW_001_C04_052690_20240718","case_id":"R13L87_REVIEW_C04_052690_PREFERRED_BIDDER_SPIKE","source_case_id":"R11L87-C04-052690-CZECH_PREFERRED_BIDDER_SPIKE","source_trigger_id":"R11L87-C04-052690-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE","symbol":"052690","company_name":"한전기술","round":"R13","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","original_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM","sector":"cross_archetype_redteam / nuclear_policy_event","primary_archetype":"preferred_bidder_policy_spike_without_final_contract","loop_objective":"4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | residual_false_positive_mining | holdout_validation","trigger_type":"R13-Review / PriceOnlyLocal4BTooEarly / PreferredBidderNoFinalContract","trigger_date":"2024-07-17","evidence_available_at_that_date":"Czech preferred-bidder event created a one-day policy spike, but final contract and legal clearance were absent at entry.","evidence_source":"R11 generated research row; Reuters 2024-07-17 preferred-bidder event; stock-web 052690 OHLCV","stage2_evidence_fields":"policy_or_regulatory_score=high; contract_score=preferred_bidder_only; legal_or_contract_risk_score=material","stage3_evidence_fields":"missing_final_contract; missing_legal_clearance; missing_margin_or_scope_conversion","stage4b_evidence_fields":"price_gap_and_volume_blowoff_without_non_price_4B_evidence","stage4c_evidence_fields":"later legal-risk watch existed, but not enough for hard 4C at entry","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":95000,"MFE_30D_pct":3.26,"MFE_90D_pct":3.26,"MFE_180D_pct":3.26,"MFE_1Y_pct":28.11,"MFE_2Y_pct":"unavailable_by_manifest","MAE_30D_pct":-35.16,"MAE_90D_pct":-35.16,"MAE_180D_pct":-47.58,"MAE_1Y_pct":-47.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":98100,"drawdown_after_peak_pct":-49.24,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early_not_full_4B","four_b_evidence_type":"price_only | positioning_overheat","four_c_protection_label":"thesis_break_watch_only_not_hard_4C","trigger_outcome_label":"r13_counterexample_price_only_event_spike_high_MAE","current_profile_verdict":"existing price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence should be kept","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_profile_corporate_action_in_entry_to_D180","same_entry_group_id":"R13_052690_2024-07-18_95000","dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","is_new_independent_case":false,"reuse_reason":"R13 cross-review of R11 row; do not count as new C04 evidence","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L87_4B4C_REVIEW_002_C04_130660_20240718","case_id":"R13L87_REVIEW_C04_130660_SMALL_CAP_POLICY_FADE","source_case_id":"R11L87-C04-130660-CZECH_POLICY_THEME_SMALL_CAP_FADE","source_trigger_id":"R11L87-C04-130660-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE","symbol":"130660","company_name":"한전산업","round":"R13","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","original_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM","sector":"cross_archetype_redteam / nuclear_policy_proxy","primary_archetype":"small_cap_policy_theme_without_direct_contract_scope","loop_objective":"4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | residual_false_positive_mining","trigger_type":"R13-Review / HighMAEPolicyProxy / NoDirectCashflowBridge","trigger_date":"2024-07-17","evidence_available_at_that_date":"Small-cap proxy moved on preferred-bidder event, but direct contract scope, final signing, and durable economics were absent.","evidence_source":"R11 generated research row; Reuters 2024-07-17 preferred-bidder event; stock-web 130660 OHLCV","stage2_evidence_fields":"policy_or_regulatory_score=high; direct_contract_score=low; bridge_to_cashflow=missing","stage3_evidence_fields":"not Green; no final contract/direct scope/margin bridge","stage4b_evidence_fields":"price-only local spike; no full 4B non-price confirmation","stage4c_evidence_fields":"high-MAE thesis-break watch, but hard 4C requires more than price fade","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv","profile_path":"atlas/symbol_profiles/130/130660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":19500,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":0.0,"MFE_2Y_pct":"unavailable_by_manifest","MAE_30D_pct":-39.18,"MAE_90D_pct":-43.74,"MAE_180D_pct":-55.28,"MAE_1Y_pct":-55.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":19500,"drawdown_after_peak_pct":-55.28,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early_but_full_4B_requires_non_price","four_b_evidence_type":"price_only | positioning_overheat","four_c_protection_label":"thesis_break_watch_only_not_hard_4C","trigger_outcome_label":"r13_high_MAE_counterexample","current_profile_verdict":"policy proxy should be blocked from positive Stage2/Green; hard 4C needs non-price thesis break","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_profile_corporate_action_in_entry_to_D180","same_entry_group_id":"R13_130660_2024-07-18_19500","dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","is_new_independent_case":false,"reuse_reason":"R13 cross-review of R11 row; do not count as new C04 evidence","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L87_4B4C_REVIEW_003_C31_052690_20250605","case_id":"R13L87_REVIEW_C31_052690_FINAL_CONTRACT_POSITIVE_CONTROL","source_case_id":"R12L87_C31_POS_052690_20250605","source_trigger_id":"R12L87_C31_T01","symbol":"052690","company_name":"한전기술","round":"R13","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM","sector":"cross_archetype_redteam / policy_to_contract_positive_control","primary_archetype":"legal_clearance_and_final_contract_bridge_positive_control","loop_objective":"4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | holdout_validation","trigger_type":"R13-Review / ContractBridgePositiveControl / NotImmediate4B","trigger_date":"2025-06-04","evidence_available_at_that_date":"Court/legal pathway cleared and CEZ/KHNP contract was signed, giving a stronger bridge than 2024 preferred-bidder-only headlines.","evidence_source":"R12 generated research row; AP/Reuters 2025 legal-clearance and signing context; stock-web 052690 OHLCV","stage2_evidence_fields":"contract_signed_or_final_path=true; legal_block_cleared=true; policy_event=true","stage3_evidence_fields":"Green still waits for company-level margin/order conversion","stage4b_evidence_fields":"later peak requires valuation/revision/legal non-price evidence; price alone not full 4B","stage4c_evidence_fields":"not 4C; this is the positive control that prevents overblocking all policy-event rows","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-05","entry_price":67300,"MFE_30D_pct":80.8,"MFE_90D_pct":80.8,"MFE_180D_pct":80.8,"MFE_1Y_pct":"insufficient_forward_window_in_stock_web","MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-4.0,"MAE_90D_pct":-4.0,"MAE_180D_pct":-4.0,"MAE_1Y_pct":"insufficient_forward_window_in_stock_web","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-06-25","peak_price":121700,"drawdown_after_peak_pct":-31.1,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_4B_entry","four_b_full_window_peak_proximity":"not_4B_entry","four_b_timing_verdict":"positive_control_not_4B_at_entry_monitor_later_peak","four_b_evidence_type":"none_at_entry","four_c_protection_label":"not_applicable_positive_control","trigger_outcome_label":"r13_positive_control_contract_bridge_captures_move","current_profile_verdict":"do not hard-block all C31/C04 policy events; distinguish legal/contract bridge from preferred-bidder-only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_profile_corporate_action_in_entry_to_D180","same_entry_group_id":"R13_052690_2025-06-05_67300","dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","is_new_independent_case":false,"reuse_reason":"R13 positive-control review of R12 row; do not count as new C31 evidence","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L87_4B4C_REVIEW_004_C30_034300_20240529","case_id":"R13L87_REVIEW_C30_034300_PRICE_ONLY_LOCAL_4B","source_case_id":"R10L87-C30-034300","source_trigger_id":"R10L87-C30-034300-T2","symbol":"034300","company_name":"신세계건설","round":"R13","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM","sector":"cross_archetype_redteam / PF_balance_sheet_local_4B","primary_archetype":"PF_repair_rally_local_peak_without_non_price_4B_confirmation","loop_objective":"4B_non_price_requirement_stress_test | accounting_trust_price_validation | data_quality_redteam","trigger_type":"R13-Review / PriceOnlyLocal4BWatch / NonPrice4BMissing","trigger_date":"2024-05-29","evidence_available_at_that_date":"Sharp local acceleration after repair/support narrative, but no verified non-price 4B evidence in the run.","evidence_source":"R10 generated research row; stock-web 034300 OHLCV","stage2_evidence_fields":"same case as R10 Stage2 repair bridge proxy","stage3_evidence_fields":"not applicable for R13 review","stage4b_evidence_fields":"price-only local peak; non-price overlay missing","stage4c_evidence_fields":"not hard 4C; drawdown after peak observed but thesis-break evidence pending","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv","profile_path":"atlas/symbol_profiles/034/034300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-29","entry_price":14700,"MFE_30D_pct":26.87,"MFE_90D_pct":26.87,"MFE_180D_pct":26.87,"MFE_1Y_pct":"contaminated_or_unavailable_not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-24.08,"MAE_90D_pct":-24.15,"MAE_180D_pct":-24.15,"MAE_1Y_pct":"contaminated_or_unavailable_not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-30","peak_price":18650,"drawdown_after_peak_pct":-40.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.51,"four_b_full_window_peak_proximity":0.51,"four_b_timing_verdict":"price_only_local_4B_requires_non_price_confirmation","four_b_evidence_type":"price_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"r13_local_4B_watch_not_full_4B","current_profile_verdict":"full_4b_requires_non_price_evidence kept; source_proxy/data-quality blocks promotion","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_has_2024-02-06_candidate_before_entry; no_overlap_entry_to_D180","same_entry_group_id":"R13_034300_2024-05-29_14700","dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","is_new_independent_case":false,"reuse_reason":"R13 cross-review of R10 4B overlay; do not count as new C30 evidence","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L87_4B4C_REVIEW_005_C30_010780_20240327","case_id":"R13L87_REVIEW_C30_010780_MACRO_SUPPORT_HIGH_MAE","source_case_id":"R10L87-C30-010780","source_trigger_id":"R10L87-C30-010780-T1","symbol":"010780","company_name":"아이에스동서","round":"R13","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM","sector":"cross_archetype_redteam / PF_balance_sheet_high_MAE","primary_archetype":"macro_support_without_company_specific_repair_bridge","loop_objective":"4C_thesis_break_timing_test | high_MAE_guardrail | residual_false_positive_mining","trigger_type":"R13-Review / HighMAEGuard / MacroSupportNoRepairBridge","trigger_date":"2024-03-27","evidence_available_at_that_date":"Macro PF/builder support tape existed, but company-specific repair bridge was not verified.","evidence_source":"R10 generated research row; stock-web 010780 OHLCV","stage2_evidence_fields":"macro_support_only; company_specific_repair_bridge_missing","stage3_evidence_fields":"not supported","stage4b_evidence_fields":"not primary","stage4c_evidence_fields":"MAE90/180 high; thesis-break watch useful; hard 4C still needs company-specific thesis break","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv","profile_path":"atlas/symbol_profiles/010/010780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":29250,"MFE_30D_pct":4.10,"MFE_90D_pct":4.10,"MFE_180D_pct":4.10,"MFE_1Y_pct":"not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-16.41,"MAE_90D_pct":-30.43,"MAE_180D_pct":-40.24,"MAE_1Y_pct":"not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":30450,"drawdown_after_peak_pct":-42.59,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B; failed_stage2_high_MAE_guard","four_b_evidence_type":"not_applicable","four_c_protection_label":"thesis_break_watch_only_not_hard_4C","trigger_outcome_label":"r13_high_MAE_counterexample_macro_support_no_bridge","current_profile_verdict":"earlier_thesis_break_watch useful; hard_4C should require company-specific thesis break","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_2024_corporate_action_candidate_in_profile","same_entry_group_id":"R13_010780_2024-03-27_29250","dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","is_new_independent_case":false,"reuse_reason":"R13 cross-review of R10 row; do not count as new C30 evidence","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

## 6. R13 Review Table

| R13 review id | source scope | symbol | entry | MFE90 | MAE90 | MFE180 | MAE180 | R13 verdict |
|---|---|---:|---|---:|---:|---:|---:|---|
| REVIEW_001 | C04 preferred bidder | 052690 | 2024-07-18 @ 95,000 | 3.26 | -35.16 | 3.26 | -47.58 | price-only local 4B; not full 4B; thesis-break watch not hard 4C |
| REVIEW_002 | C04 policy proxy | 130660 | 2024-07-18 @ 19,500 | 0.00 | -43.74 | 0.00 | -55.28 | high-MAE false positive; block positive stage |
| REVIEW_003 | C31 contract bridge positive control | 052690 | 2025-06-05 @ 67,300 | 80.80 | -4.00 | 80.80 | -4.00 | contract/legal bridge can be Stage2; do not overblock all policy events |
| REVIEW_004 | C30 PF local 4B | 034300 | 2024-05-29 @ 14,700 | 26.87 | -24.15 | 26.87 | -24.15 | local 4B watch only; non-price 4B missing |
| REVIEW_005 | C30 macro support high-MAE | 010780 | 2024-03-27 @ 29,250 | 4.10 | -30.43 | 4.10 | -40.24 | high-MAE Stage2 false positive; thesis-break watch useful |

## 7. Cross-Archetype Pattern Diagnosis

### Pattern A — preferred-bidder-only policy spike

Applies to:

```text
R13L87_4B4C_REVIEW_001_C04_052690_20240718
R13L87_4B4C_REVIEW_002_C04_130660_20240718
```

Diagnosis:

- The local peak was immediate.
- MFE after entry was weak or zero.
- MAE was severe.
- Full 4B still should not be inferred from price alone; the right label is `local_4b_watch` plus `Stage2 positive block`.
- Hard 4C requires legal/contract thesis break. A future legal block can upgrade watch, but the original preferred-bidder day is not enough.

### Pattern B — legal/contract bridge positive control

Applies to:

```text
R13L87_4B4C_REVIEW_003_C31_052690_20250605
```

Diagnosis:

- Same policy theme, same broad nuclear umbrella, but different evidence state.
- Legal/contract bridge converted the event from headline optionality into a tradable Stage2-Actionable candidate.
- This row prevents an overly blunt rule that blocks all C04/C31 policy events.

### Pattern C — PF/macro support without company repair bridge

Applies to:

```text
R13L87_4B4C_REVIEW_004_C30_034300_20240529
R13L87_4B4C_REVIEW_005_C30_010780_20240327
```

Diagnosis:

- Macro support without company-level repair creates false positives and high-MAE paths.
- A price-only local peak can be useful as a watch overlay.
- Full 4B requires non-price evidence: refinancing failure, asset-sale failure, dilution/CB/overhang, margin/backlog slowdown, legal block, or accounting trust deterioration.

## 8. Score Simulation Rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_current_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","profile_hypothesis":"Current global guards block price-only blowoff and require non-price evidence for full 4B; hard 4C needs thesis break.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":5,"selected_entry_trigger_per_case":["REVIEW_001","REVIEW_002","REVIEW_003","REVIEW_004","REVIEW_005"],"avg_MFE_90D_pct":23.01,"avg_MAE_90D_pct":-27.50,"avg_MFE_180D_pct":23.01,"avg_MAE_180D_pct":-34.25,"false_positive_rate":0.6,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"mixed: local 4B rows show 0.51~1.0, positive control not 4B","avg_four_b_full_window_peak_proximity":"mixed: preferred-bidder rows low/zero, PF local 4B around 0.51","score_return_alignment_verdict":"guards directionally correct; R13 does not propose new global delta","raw_component_scores_before":{"contract_score":"varies_by_bridge","backlog_visibility_score":"low_to_medium","margin_bridge_score":"low","revision_score":"unknown_or_not_supported","relative_strength_score":"high_for_spikes","customer_quality_score":"not_applicable","policy_or_regulatory_score":"high","valuation_repricing_score":"medium_to_high","execution_risk_score":"high_when_bridge_missing","legal_or_contract_risk_score":"high_before_clearance","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"not_primary"},"weighted_score_before":"research_proxy_mixed","stage_label_before":"mixed Watch/Stage2/local4B","raw_component_scores_after":"same_as_before","weighted_score_after":"no_new_profile_applied","stage_label_after":"unchanged_shadow_only","component_delta_explanation":"No scoring patch. This is cross-case validation of existing 4B/4C guardrails."}
{"row_type":"score_simulation","profile_id":"P3_counterexample_guard_profile","profile_scope":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","profile_hypothesis":"Treat price-only local peaks as 4B-watch, not full 4B; route high-MAE macro/policy false positives to thesis-break watch, not hard 4C unless non-price thesis break appears.","changed_axes":["existing_axis_kept:price_only_blowoff_blocks_positive_stage","existing_axis_kept:full_4b_requires_non_price_evidence","existing_axis_kept:hard_4c_thesis_break_routes_to_4c","existing_axis_strengthened:earlier_thesis_break_watch"],"changed_thresholds":{},"eligible_trigger_count":5,"selected_entry_trigger_per_case":["REVIEW_001","REVIEW_002","REVIEW_003","REVIEW_004","REVIEW_005"],"avg_MFE_90D_pct":23.01,"avg_MAE_90D_pct":-27.50,"avg_MFE_180D_pct":23.01,"avg_MAE_180D_pct":-34.25,"false_positive_rate":0.6,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"price-only local 4B rows valid only as watch overlays","avg_four_b_full_window_peak_proximity":"non-price confirmation missing for full 4B rows","score_return_alignment_verdict":"best R13 interpretation: keep existing guardrails; add no new delta"}
```

## 9. Aggregate / Residual / Shadow Rows

```jsonl
{"row_type":"aggregate_metric","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM","review_trigger_count":5,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"positive_control_count":1,"counterexample_or_high_MAE_count":4,"price_only_local_4B_watch_count":3,"hard_4C_confirmation_count":0,"thesis_break_watch_only_count":4,"do_not_count_as_new_case_count":5,"avg_MFE_90D_pct":23.01,"avg_MAE_90D_pct":-27.50,"avg_MFE_180D_pct":23.01,"avg_MAE_180D_pct":-34.25,"metric_verdict":"Existing full_4b_requires_non_price_evidence and hard_4c_thesis_break_routes_to_4c are directionally correct; R13 adds cross-case validation, not a new patch."}
{"row_type":"residual_contribution","residual_error_type":"price_only_policy_or_macro_spike_misclassified_as_positive_stage_or_full_4B","affected_scope":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","supporting_trigger_ids":["R13L87_4B4C_REVIEW_001_C04_052690_20240718","R13L87_4B4C_REVIEW_002_C04_130660_20240718","R13L87_4B4C_REVIEW_004_C30_034300_20240529","R13L87_4B4C_REVIEW_005_C30_010780_20240327"],"opposing_trigger_ids":["R13L87_4B4C_REVIEW_003_C31_052690_20250605"],"new_axis_proposed":"none","existing_axis_strengthened":"earlier_thesis_break_watch","existing_axis_kept":"price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c","promotion_recommendation":"holdout_validation_passed_no_patch","reason":"The issue is not lack of a new global rule; the correct behavior is already represented by existing guards. R13 confirms separation of local 4B watch, full 4B, and hard 4C."}
{"row_type":"shadow_weight","rule_scope":"R13_cross_archetype_redteam_only","shadow_rule_candidate":"Across C04/C30/C31, price-only local peaks should be recorded as 4B-watch overlays. Full 4B requires non-price evidence. Hard 4C requires thesis break confirmation, not just drawdown after event spike. Legal/contract bridge positives must remain eligible for Stage2 and should not be overblocked.","shadow_delta":0,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"rollback_condition":"If future R13 rows show multiple verified non-price full-4B events missed by current profile, reopen full_4b_overlay calibration. If legal/contract bridge positives fail repeatedly after signing, reopen hard_4c confirmation timing."}
```

## 10. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | review rows | reviewed original canonicals | positive controls | counterexamples/high-MAE | local 4B watch | hard 4C confirmations |
|---|---|---|---:|---:|---:|---:|---:|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | R13_POLICY_EVENT_AND_PF_PRICE_ONLY_LOCAL_4B_VS_HARD_4C_TIMING_REDTEAM | 5 | 3 | 1 | 4 | 3 | 0 |

## 11. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 5
reused_case_ids:
  - R11L87-C04-052690-CZECH_PREFERRED_BIDDER_SPIKE
  - R11L87-C04-130660-CZECH_POLICY_THEME_SMALL_CAP_FADE
  - R12L87_C31_POS_052690_20250605
  - R10L87-C30-034300
  - R10L87-C30-010780
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 0

tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - earlier_thesis_break_watch

residual_error_types_found:
  - price_only_policy_spike_as_false_positive
  - price_only_local_4B_without_non_price_confirmation
  - high_MAE_macro_support_without_company_bridge
  - legal_contract_bridge_positive_control_prevents_overblocking

new_axis_proposed: none
existing_axis_strengthened: earlier_thesis_break_watch
existing_axis_weakened: none
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: R13 is cross-redteam only; all rows are do_not_count_as_new_case=true.

loop_contribution_label: holdout_validation_passed
do_not_propose_new_weight_delta: true
```

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session.

When batch-applying v12 MDs later, ingest this file as `R13 / Loop 87 / R13_CROSS_ARCHETYPE_4B_4C_REDTEAM`.

Implementation notes:

1. Treat all `row_type=trigger` rows in this file as R13 review rows only.
2. Preserve `do_not_count_as_new_case=true` and `independent_evidence_weight=0.0`.
3. Do not add C04/C30/C31 positive/counterexample coverage from this R13 file.
4. Use this file only to validate existing guardrails:
   - `price_only_blowoff_blocks_positive_stage`
   - `full_4b_requires_non_price_evidence`
   - `hard_4c_thesis_break_routes_to_4c`
   - `earlier_thesis_break_watch`
5. Do not write a production patch from this MD alone.
6. If a future R13 batch aggregates enough verified non-price full-4B examples, reopen only the `full_4b_overlay_candidate` axis.

## 13. Round State

```text
completed_round = R13
completed_loop = 87
next_round = R1
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
