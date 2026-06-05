# E2R Stock-Web v12 Residual Research — R12 Loop 87 — C31 Policy Subsidy / Legislation Event

## Metadata

```json
{
  "schema_family": "v12_sector_archetype_residual",
  "scheduled_round": "R12",
  "scheduled_loop": 87,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD",
  "loop_objective": "coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression",
  "price_data_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false
}
```

## Schedule Resolution


- Previous completed state observed in this conversation: `R11 / Loop 87`.
- Per the v12 round cycle, `R11 -> R12` with the same loop number.
- `R12` allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or relevant under-covered service/agri sector.
- Selected pair: `R12 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.
- Selected canonical: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`.
- Output filename follows the hard rule:
  `e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md`

## Price Source Validation


Primary price source is `Songdaiki/stock-web`, `tradable_raw`, `raw_unadjusted_marcap`.

Manifest fields used:
- `source_name`: FinanceData/marcap
- `price_adjustment_status`: raw_unadjusted_marcap
- `min_date`: 1995-05-02
- `max_date`: 2026-02-20
- `tradable_row_count`: 14,354,401
- `calibration_shard_root`: atlas/ohlcv_tradable_by_symbol_year

Symbol profiles inspected:
- `052690` 한전기술: no corporate action candidate dates; clean 180D window for 2024-07-10 and 2025-06-05 entries.
- `051600` 한전KPS: no corporate action candidate dates; clean 180D window for 2025-06-05 entry.
- `130660` 한전산업: no corporate action candidate dates; clean 180D window for 2024-07-10 entry.

Relevant stock-web paths:
- `atlas/manifest.json`
- `atlas/symbol_profiles/052/052690.json`
- `atlas/symbol_profiles/051/051600.json`
- `atlas/symbol_profiles/130/130660.json`
- `atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv`

## Evidence Sources


External evidence used as historical as-of anchors:
- Reuters, 2024-07-17: Czech government picked South Korea's KHNP over EDF for new nuclear units.
- Reuters, 2024-08-27: EDF and Westinghouse appealed the Czech nuclear tender decision; Westinghouse cited KHNP export/licensing issues.
- Reuters, 2025-05-06 and 2025-05-07: Czech court halted signing; CEZ planned appeal and warned delays could threaten the first unit schedule.
- AP, 2025-06-04: Czech Republic signed the KHNP/CEZ deal after an appeals court cleared the way; contract cost reported at 407bn koruna and trial operation target around 2036.

Interpretation:
- 2024 preferred-bidder events are not enough for Stage3-Green in C31.
- 2025 legal clearance + signed contract is a stronger Stage2-Actionable bridge, but still not automatic Green for each Korean listed beneficiary without company-level order/margin allocation.

## No-Repeat / Novelty Check


No-Repeat Index role: duplication ledger only.

Hard duplicate key:
`canonical_archetype_id + symbol + trigger_type + entry_date`

C31 currently has broad coverage, but the top-covered C31 symbols listed in the No-Repeat Index are:
`013990`, `003550`, `015760`, `032350`, `114090`, `000270`.

This MD intentionally avoids those top repeated C31 clusters and uses:
- `052690`
- `051600`
- `130660`

Novelty caveat:
- `052690` appears twice in this MD, but the 2024 row is a preferred-bidder-only false-positive test, while the 2025 row is a legal-clearance/final-contract bridge test. Same symbol reuse is therefore kept as a different trigger family and market regime, with independent evidence weight capped at `0.75` for the reused-symbol row.

## Case Thesis


C31 is the event-policy archetype. Its failure mode is simple: the market often treats a policy headline as if it were already cashflow. The right state machine should behave more like a customs gate:

1. **Policy headline / preferred bidder**: passport presented, but no entry yet.
2. **Legal clearance / final contract**: gate opens; Stage2-Actionable can be considered.
3. **Company-level order, scope, margin, or recurring revenue bridge**: luggage checked; Stage3-Green can be considered.

The residual error tested here is whether nuclear policy events are being admitted too early when the evidence is still only headline-level.

## Machine-readable trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R12L87_C31_T01","case_id":"R12L87_C31_POS_052690_20250605","symbol":"052690","company_name":"한전기술","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc / nuclear_policy","primary_archetype":"policy contract signing converted to visible project cashflow path","loop_objective":"coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable / PolicyEventContractBridge","trigger_date":"2025-06-04","evidence_available_at_that_date":"Czech Supreme Administrative Court cleared the way and CEZ/KHNP signed the Dukovany contract on 2025-06-04; this is stronger than 2024 preferred-bidder-only policy news because it converts policy option into contract path.","evidence_source":"AP 2025-06-04 Czech-KHNP contract signing after court cleared way; Reuters 2025-05-06/05-07 court halt and appeal context.","stage2_evidence_fields":"contract_signed_or_final_path=true; policy_event=true; legal_block_cleared=true; project_cashflow_path=partial; source_proxy_only=false","stage3_evidence_fields":"final company-level backlog/margin split still not fully visible; Green should wait for order allocation/margin/procurement conversion","stage4b_evidence_fields":"none at entry; later price acceleration requires non-price 4B confirmation","stage4c_evidence_fields":"not applicable at entry","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-05","entry_price":67300,"MFE_30D_pct":80.8,"MFE_90D_pct":80.8,"MFE_180D_pct":80.8,"MFE_1Y_pct":"insufficient_forward_window_in_stock_web","MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-4.0,"MAE_90D_pct":-4.0,"MAE_180D_pct":-4.0,"MAE_1Y_pct":"insufficient_forward_window_in_stock_web","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-06-25","peak_price":121700,"drawdown_after_peak_pct":-31.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_but_requires_contract_to_company_conversion","current_profile_verdict":"Stage2-Actionable correct; Green must remain restricted until company-level margin/order visibility","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"052690_20250605_67300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L87_C31_T02","case_id":"R12L87_C31_POS_051600_20250605","symbol":"051600","company_name":"한전KPS","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc / nuclear_policy_maintenance","primary_archetype":"policy event with service/maintenance cashflow optionality","loop_objective":"coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable / PolicyServiceCashflowBridge","trigger_date":"2025-06-04","evidence_available_at_that_date":"Same Czech-KHNP contract signing event; service/maintenance names participated in policy rerating but direct revenue path is less immediate than EPC/design names.","evidence_source":"AP 2025-06-04; Reuters 2025-05-06/05-07","stage2_evidence_fields":"policy_event=true; maintenance_service_optional_cashflow=true; direct_contract_allocation=uncertain","stage3_evidence_fields":"Green should require service scope, margin or recurring maintenance revenue evidence","stage4b_evidence_fields":"later price spike can be local 4B only without direct non-price evidence","stage4c_evidence_fields":"not applicable at entry","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv","profile_path":"atlas/symbol_profiles/051/051600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-05","entry_price":44850,"MFE_30D_pct":45.8,"MFE_90D_pct":45.8,"MFE_180D_pct":45.8,"MFE_1Y_pct":"insufficient_forward_window_in_stock_web","MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-4.1,"MAE_90D_pct":-4.1,"MAE_180D_pct":-14.8,"MAE_1Y_pct":"insufficient_forward_window_in_stock_web","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":65400,"drawdown_after_peak_pct":-33.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_price_peak_needs_non_price_4B_confirmation","four_b_evidence_type":"price_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_but_lower_quality_than_direct_design_contract_exposure","current_profile_verdict":"Stage2-Actionable acceptable; do not Green without service revenue bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"051600_20250605_44850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L87_C31_T03","case_id":"R12L87_C31_FAIL_130660_20240710","symbol":"130660","company_name":"한전산업","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc / nuclear_policy_theme","primary_archetype":"event-only policy beta without direct contract economics","loop_objective":"coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-FalsePositive-Candidate / PolicyThemeNoCashflowBridge","trigger_date":"2024-07-10","evidence_available_at_that_date":"Nuclear-policy/preferred-bidder anticipation created policy beta, but not yet final contract, legal clearance, company-level scope or margin bridge.","evidence_source":"Reuters 2024-07-17 preferred bidder; Reuters 2024-08-27 appeal/legal risk","stage2_evidence_fields":"policy_event=true; company_scope=weak; margin_bridge=absent; final_contract=false","stage3_evidence_fields":"not enough for Green","stage4b_evidence_fields":"local price blowoff appears before non-price confirmation","stage4c_evidence_fields":"fade route after policy event exhausted","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv","profile_path":"atlas/symbol_profiles/130/130660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-10","entry_price":15890,"MFE_30D_pct":22.7,"MFE_90D_pct":22.7,"MFE_180D_pct":22.7,"MFE_1Y_pct":"not_calculated","MFE_2Y_pct":"not_calculated","MAE_30D_pct":-25.0,"MAE_90D_pct":-25.4,"MAE_180D_pct":-44.1,"MAE_1Y_pct":"not_calculated","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":19500,"drawdown_after_peak_pct":-54.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_good_for_watch_not_full_4B","four_b_evidence_type":"price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_policy_theme_without_cashflow_bridge","current_profile_verdict":"If Stage2-Actionable was triggered, it was false positive; should remain Watch until contract/cashflow bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"130660_20240710_15890","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L87_C31_T04","case_id":"R12L87_C31_FAIL_052690_20240710","symbol":"052690","company_name":"한전기술","round":"R12","loop":87,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc / nuclear_policy","primary_archetype":"preferred-bidder-only policy event before legal clearance","loop_objective":"coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-FalsePositive-Candidate / PreferredBidderOnlyLegalOverhang","trigger_date":"2024-07-10","evidence_available_at_that_date":"Preferred-bidder expectation/policy momentum arrived before final contract and before EDF/Westinghouse legal overhang was resolved.","evidence_source":"Reuters 2024-07-17 preferred bidder; Reuters 2024-08-27 appeals; Reuters/AP 2025 legal clearance context","stage2_evidence_fields":"policy_event=true; preferred_bidder_only=true; legal_clearance=false; final_contract=false","stage3_evidence_fields":"not enough for Green; should wait for legal clearance/final contract","stage4b_evidence_fields":"price-only local spike without full non-price 4B evidence","stage4c_evidence_fields":"legal-overhang fade risk","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-10","entry_price":75000,"MFE_30D_pct":30.8,"MFE_90D_pct":30.8,"MFE_180D_pct":30.8,"MFE_1Y_pct":"not_calculated","MFE_2Y_pct":"not_calculated","MAE_30D_pct":-17.9,"MAE_90D_pct":-17.9,"MAE_180D_pct":-33.5,"MAE_1Y_pct":"not_calculated","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":98100,"drawdown_after_peak_pct":-49.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_window_without_non_price_evidence","four_b_evidence_type":"price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_preferred_bidder_only_spike_reversed_before_contract","current_profile_verdict":"Stage2 may be watch/actionable only; Green should be blocked until legal/final contract bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"052690_20240710_75000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol as T01 but different trigger family and different market regime; counted as independent C31 residual false-positive test","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
```

## Score Simulation Rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"baseline_current_proxy","profile_hypothesis":"Existing policy-event guard mostly blocks price-only blowoff but can still allow Stage2-Actionable too early when legal/final-contract bridge is missing.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["R12L87_C31_T01","R12L87_C31_T02","R12L87_C31_T03","R12L87_C31_T04"],"avg_MFE_90D_pct":45.0,"avg_MAE_90D_pct":-12.9,"avg_MFE_180D_pct":45.0,"avg_MAE_180D_pct":-24.1,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed: contract-signed route works; preferred-bidder-only route has high-MAE false positive risk","raw_component_scores_before":{"contract_score":"varies_by_trigger","backlog_visibility_score":"low_to_medium","margin_bridge_score":"low","revision_score":"unknown_or_not_supported","relative_strength_score":"high_in_theme_spikes","customer_quality_score":"not_applicable","policy_or_regulatory_score":"high","valuation_repricing_score":"medium","execution_risk_score":"high_before_final_contract","legal_or_contract_risk_score":"high_before_court_clearance","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"not_primary"},"weighted_score_before":"research_proxy_mixed_61_78","stage_label_before":"Watch_to_Stage2_Actionable","raw_component_scores_after":"same_as_before","weighted_score_after":"no_new_profile_applied","stage_label_after":"no_new_profile_applied","component_delta_explanation":"No production/scoring patch proposed; row is a residual/error and holdout test for C31 event-to-cashflow bridge."}
{"row_type":"score_simulation","profile_id":"P1_policy_event_contract_bridge_guard_shadow","profile_scope":"canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_hypothesis":"Stage2-Actionable requires at least one of final_contract_signed, legal_clearance, or company-specific order/margin bridge; preferred-bidder-only remains Watch.","changed_axes":["stage2_required_bridge_tested"],"changed_thresholds":{"preferred_bidder_only_to_stage2":"blocked_without_legal_clearance_or_final_contract"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["T01","T02","T03_as_blocked_watch","T04_as_blocked_watch"],"avg_MFE_90D_pct":63.3,"avg_MAE_90D_pct":-4.1,"avg_MFE_180D_pct":63.3,"avg_MAE_180D_pct":-9.4,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best alignment in this sample but requires verified non-proxy evidence before promotion"}
{"row_type":"score_simulation","profile_id":"P2_no_new_weight_delta","profile_scope":"no_new_rule","profile_hypothesis":"Do not propose a new global delta because C31 already carries event-only-until-cashflow-conversion logic; add counterexamples and evidence requirements only.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["all_representative_rows"],"avg_MFE_90D_pct":45.0,"avg_MAE_90D_pct":-12.9,"avg_MFE_180D_pct":45.0,"avg_MAE_180D_pct":-24.1,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"hold for evidence normalization"}
{"row_type":"score_simulation","profile_id":"P3_counterexample_guard_profile","profile_scope":"canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_hypothesis":"Price-only policy theme spikes with no legal/contract/cashflow bridge should be Watch or local 4B watch, not positive Stage2/Green.","changed_axes":["existing_axis_kept:price_only_blowoff_blocks_positive_stage","existing_axis_kept:full_4b_requires_non_price_evidence"],"changed_thresholds":{},"eligible_trigger_count":2,"selected_entry_trigger_per_case":["R12L87_C31_T03","R12L87_C31_T04"],"avg_MFE_90D_pct":26.75,"avg_MAE_90D_pct":-21.65,"avg_MFE_180D_pct":26.75,"avg_MAE_180D_pct":-38.8,"false_positive_rate":1.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"guard confirmed"}
```

## Aggregate / Residual / Shadow Rows

```jsonl
{"row_type":"aggregate_metric","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD","positive_case_count":2,"counterexample_count":2,"calibration_usable_case_count":4,"new_independent_case_count":4,"new_symbol_count":3,"new_trigger_family_count":3,"avg_MFE_90D_pct":45.0,"avg_MAE_90D_pct":-12.9,"avg_MFE_180D_pct":45.0,"avg_MAE_180D_pct":-24.1,"source_proxy_only_count":0,"evidence_url_pending_count":0,"current_profile_error_count":2,"metric_verdict":"C31 needs event-to-contract-to-cashflow sequencing; preferred-bidder-only price spikes are high-MAE counterexamples."}
{"row_type":"residual_contribution","residual_error_type":"policy_event_preferred_bidder_only_false_positive","affected_scope":"canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT","supporting_trigger_ids":["R12L87_C31_T03","R12L87_C31_T04"],"opposing_trigger_ids":["R12L87_C31_T01","R12L87_C31_T02"],"new_axis_proposed":"none","existing_axis_strengthened":"stage2_required_bridge / price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence","promotion_recommendation":"hold_for_more_evidence_not_apply_patch","reason":"Enough to add counterexamples, not enough to propose new global or canonical weight delta; C31 existing green_policy already says event-only until cashflow conversion."}
{"row_type":"shadow_weight","rule_scope":"no_new_rule","shadow_rule_candidate":"Do not elevate C31 policy event to Stage2-Actionable unless at least one bridge exists: final_contract_signed, legal_clearance, explicit company-level order/backlog allocation, or subsidy-to-cashflow conversion.","shadow_delta":0,"do_not_propose_new_weight_delta":true,"rollback_condition":"If future C31 examples show preferred-bidder-only events with MFE90>=40 and MAE90>-10 across multiple symbols without legal/cashflow bridge, revisit."}
```

## Trigger Table

| trigger_id | symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| R12L87_C31_T01 | 052690 | 2025-06-05 | 67300 | 80.8 | -4.0 | 80.8 | -4.0 | 80.8 | -4.0 | positive_structural_success_but_requires_contract_to_company_conversion |
| R12L87_C31_T02 | 051600 | 2025-06-05 | 44850 | 45.8 | -4.1 | 45.8 | -4.1 | 45.8 | -14.8 | positive_but_lower_quality_than_direct_design_contract_exposure |
| R12L87_C31_T03 | 130660 | 2024-07-10 | 15890 | 22.7 | -25.0 | 22.7 | -25.4 | 22.7 | -44.1 | counterexample_high_MAE_policy_theme_without_cashflow_bridge |
| R12L87_C31_T04 | 052690 | 2024-07-10 | 75000 | 30.8 | -17.9 | 30.8 | -17.9 | 30.8 | -33.5 | counterexample_preferred_bidder_only_spike_reversed_before_contract |

## 4B / 4C Audit


- `130660 / 2024-07-10` and `052690 / 2024-07-10` show local policy-theme blowoff followed by heavy drawdown. These are not full 4B confirmations by themselves because `four_b_evidence_type=price_only`.
- `052690 / 2025-06-05` and `051600 / 2025-06-05` show contract-bridge rallies. Their local peaks are useful for 4B timing audit, but full 4B still requires non-price evidence such as valuation blowoff, revision slowdown, delayed allocation, or legal/contract setback.
- No hard 4C row is proposed in this MD. The counterexamples are `thesis_break_watch_only`, not final hard-4C confirmations.

## Raw Component Score Breakdown — Research Proxy


| component | 2025 contract-signed route | 2024 preferred-bidder-only route |
|---|---|---|
| contract_score | high | low |
| backlog_visibility_score | medium | low |
| margin_bridge_score | low-to-medium | low |
| revision_score | unknown_or_not_supported | unknown_or_not_supported |
| relative_strength_score | high | high but price-only |
| customer_quality_score | not_applicable | not_applicable |
| policy_or_regulatory_score | high | high |
| valuation_repricing_score | medium | medium/high but unstable |
| execution_risk_score | medium | high |
| legal_or_contract_risk_score | lower after court clearance | high before appeals/clearance |
| dilution_cb_risk_score | unknown_or_not_supported | unknown_or_not_supported |
| accounting_trust_risk_score | not_primary | not_primary |

## Coverage Matrix


| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | calibration_usable_case_count | new_symbol_count | 4B_or_4C_case_count |
|---|---|---|---:|---:|---:|---:|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | NUCLEAR_POLICY_LEGISLATION_TO_CONTRACT_CASHFLOW_CONVERSION_GUARD | 2 | 2 | 4 | 3 | 2 local 4B watch / 0 hard 4C |

## Residual Contribution Summary


new_independent_case_count: 4
reused_case_count: 1 same-symbol reuse within MD (`052690`) but different trigger family/regime
reused_case_ids: [`R12L87_C31_FAIL_052690_20240710` as same-symbol cross-regime comparison]
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- event_only_until_cashflow_conversion

residual_error_types_found:
- policy_event_preferred_bidder_only_false_positive
- price_only_local_4B_without_non_price_confirmation
- legal_overhang_not_resolved_at_initial_policy_spike

new_axis_proposed: none
existing_axis_strengthened: C31 event-to-cashflow conversion bridge
existing_axis_weakened: none
existing_axis_kept:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: C31 already contains event-only-until-cashflow-conversion logic; this MD adds counterexamples and holdout validation rather than new scoring delta.

loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true

## Deferred Coding Agent Handoff Prompt


Do not execute this handoff in the research session.

When batch-applying v12 research MDs later, ingest this file as R12/Loop87 C31 residual research. Parse the JSONL trigger rows and aggregate rows. Do not create a new global axis. Treat the main contribution as:
1. C31 policy/preferred-bidder-only false-positive counterexample rows.
2. C31 legal-clearance/final-contract bridge positive rows.
3. Reinforcement of existing event-to-cashflow conversion guard.
4. No production default scoring change.

Recommended application:
- If canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT and trigger evidence is only preferred_bidder/policy_headline/theme, block Stage3-Green and keep at Watch unless legal clearance/final contract/company-level cashflow bridge is present.
- Keep price-only local peaks as 4B watch only unless non-price 4B evidence appears.
- Do not use future MFE/MAE as runtime input; they are only calibration support.

## Final Round State

```text
completed_round = R12
completed_loop = 87
next_round = R13
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```