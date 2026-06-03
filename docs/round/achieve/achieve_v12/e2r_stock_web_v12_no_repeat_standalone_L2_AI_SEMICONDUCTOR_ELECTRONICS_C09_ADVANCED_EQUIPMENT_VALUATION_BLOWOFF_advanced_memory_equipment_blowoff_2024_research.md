# E2R V12 No-Repeat Standalone Residual Research
## L2 / C09 Advanced Equipment Valuation Blowoff — 2024 memory equipment beta

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_MEMORY_EQUIPMENT_VALUATION_BETA_4B_COUNTEREXAMPLE
loop_objective: counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|holdout_validation
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_advanced_memory_equipment_blowoff_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt and duplicate-avoidance basis

This standalone MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` with the user-specified scheduler override.  
`V12_Research_No_Repeat_Index.md` was used only for duplicate avoidance and coverage-gap selection.

No-Repeat observations:
- C09 already has coverage, but its top-covered symbols are concentrated in Hanmi/Eotech/ISC-style advanced packaging and socket/probe names.
- This run adds a different C09 fine path: memory-equipment valuation beta around broad 2024 memory recovery.
- The selected hard keys are new: `C09 + 240810 + Stage4B-Overlay + 2024-02-29`, `C09 + 095610 + Stage3-Yellow + 2024-04-02`, `C09 + 036930 + Stage3-Yellow + 2024-02-28`.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected 2024 windows use calibration-safe tradable shards:
```text
240810 profile: corporate_action_candidate_count=0, 2024 window clean.
095610 profile: old corporate-action dates in 2011/2016 only, 2024 window clean.
036930 profile: old corporate-action date in 2000 only, 2024 window clean.
```

## 3. Research thesis

C09 should not be a free Green pass for every advanced-equipment label. The archetype captures a distinct behavior:

```text
advanced equipment theme / memory recovery beta
→ sharp valuation rerating attempt
→ local 4B or Yellow if non-price evidence is not yet closed
→ Green only if order, customer, backlog, or revision evidence catches up
```

This run therefore stress-tests whether broad memory-equipment beta in 2024 should be promoted or capped.

## 4. Historical trigger-level backtest table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C09_240810_WONIKIPS_20240229_ADVANCED_MEMORY_EQUIPMENT_BLOWOFF_4B | 240810 | 4B_overlay_success | 2024-02-29 | 32800 | 44850 on 2024-04-08 | 27800 on 2024-09-11 | 36.74% | -15.24% | -38.02% |
| C09_095610_TES_20240402_VALUATION_BETA_FALSE_GREEN_COUNTER | 095610 | false_positive_green | 2024-04-02 | 25150 | 26400 on 2024-04-02 | 15880 on 2024-09-09 | 4.97% | -36.86% | -39.85% |
| C09_036930_JUSUNG_20240228_ADVANCED_ALD_BETA_HIGH_MAE_COUNTER | 036930 | high_mae_false_green | 2024-02-28 | 40000 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 3.62% | -44.88% | -46.8% |


## 5. Stage evidence split

### Stage2 / Stage2-Actionable evidence
- Advanced-equipment theme and memory-recovery relative strength were visible.
- That is enough for attention and Stage2/Yellow review.
- It is not enough by itself for Stage3-Green.

### Stage3 evidence
- Required bridge: customer/order/backlog or revision visibility.
- The 240810 case earns 4B-overlay support because price path rerated strongly, but it remains a watch/overlay unless fundamental order evidence is verified.
- The 095610 and 036930 cases show that equipment label plus beta can fail after the initial excitement.

### 4B evidence
- 240810 reached a 36.74% MFE from the trigger entry and then drew down 38.02% from peak.
- C09 therefore needs a local 4B watch guard around valuation beta, not only full-window non-price confirmation.

### 4C evidence
- 095610 and 036930 show slow thesis fade / revision-gap behavior rather than immediate hard 4C.
- The guard should not automatically route all drawdowns to hard 4C; it should first check whether the original order/revision bridge never closed.

## 6. Current calibrated profile stress test

Current calibrated profile assumptions already block price-only positive promotion and require non-price evidence for full 4B. C09 adds a narrower rule:

```text
If advanced-equipment valuation beta lacks explicit order/backlog/customer/revision evidence,
cap positive promotion at Stage3-Yellow or local 4B-watch.
Do not let advanced-equipment label substitute for visibility score.
```

Residual errors:
```text
current_profile_error_count = 2
- 095610: false-Green risk if generic memory beta is treated as visibility.
- 036930: false-Green/high-MAE risk if advanced deposition label is treated as backlog/revision evidence.
```

## 7. Machine-readable rows

```jsonl
{"MAE_180D_pct": -15.24, "MAE_30D_pct": -2.29, "MAE_90D_pct": -2.29, "MFE_180D_pct": 36.74, "MFE_30D_pct": 36.74, "MFE_90D_pct": 36.74, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_240810_WONIKIPS_20240229_ADVANCED_MEMORY_EQUIPMENT_BLOWOFF_4B", "case_role": "4B_overlay_success", "company_name": "원익IPS", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": false, "current_profile_verdict": "current_profile_should_route_to_local_4b_watch_not_new_green", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.02, "entry_date": "2024-02-29", "entry_price": 32800, "evidence_family": "advanced_memory_equipment_rerating_without_full_hbm_order_but_price_path_reached_4b_watch", "evidence_url_pending": false, "fine_archetype_id": "ADVANCED_MEMORY_EQUIPMENT_VALUATION_BETA_4B_COUNTEREXAMPLE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reuse_reason": null, "same_entry_group_id": "C09_240810_WONIKIPS_20240229_ADVANCED_MEMORY_EQUIPMENT_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_theme", "relative_strength", "memory_cycle_recovery"], "stage3_evidence_fields": ["order_backlog_required", "confirmed_revision_required", "customer_visibility_required"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["revision_gap", "customer_order_absence", "capex_delay_or_cycle_fade"], "symbol": "240810", "trigger_date": "2024-02-29", "trigger_type": "Stage4B-Overlay", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.86, "MAE_30D_pct": -23.86, "MAE_90D_pct": -23.86, "MFE_180D_pct": 4.97, "MFE_30D_pct": 4.97, "MFE_90D_pct": 4.97, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_095610_TES_20240402_VALUATION_BETA_FALSE_GREEN_COUNTER", "case_role": "false_positive_green", "company_name": "테스", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "current_profile_error_if_price_spike_or_memory_beta_is_counted_as_order_visibility", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.85, "entry_date": "2024-04-02", "entry_price": 25150, "evidence_family": "generic_memory_equipment_valuation_beta_without_customer_order_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "ADVANCED_MEMORY_EQUIPMENT_VALUATION_BETA_4B_COUNTEREXAMPLE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_date": "2024-04-02", "peak_price": 26400, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reuse_reason": null, "same_entry_group_id": "C09_095610_TES_20240402_VALUATION_BETA_FALSE_GREEN_COUNTER", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_theme", "relative_strength", "memory_cycle_recovery"], "stage3_evidence_fields": ["order_backlog_required", "confirmed_revision_required", "customer_visibility_required"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["revision_gap", "customer_order_absence", "capex_delay_or_cycle_fade"], "symbol": "095610", "trigger_date": "2024-04-02", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.88, "MAE_30D_pct": -16.37, "MAE_90D_pct": -16.37, "MFE_180D_pct": 3.62, "MFE_30D_pct": 3.62, "MFE_90D_pct": 3.62, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_036930_JUSUNG_20240228_ADVANCED_ALD_BETA_HIGH_MAE_COUNTER", "case_role": "high_mae_false_green", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "current_profile_error_if_advanced_equipment_label_is_allowed_to_substitute_for_order_backlog", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-02-28", "entry_price": 40000, "evidence_family": "advanced_deposition_equipment_beta_without_durable_hbm_customer_or_backlog_visibility", "evidence_url_pending": false, "fine_archetype_id": "ADVANCED_MEMORY_EQUIPMENT_VALUATION_BETA_4B_COUNTEREXAMPLE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reuse_reason": null, "same_entry_group_id": "C09_036930_JUSUNG_20240228_ADVANCED_ALD_BETA_HIGH_MAE_COUNTER", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_theme", "relative_strength", "memory_cycle_recovery"], "stage3_evidence_fields": ["order_backlog_required", "confirmed_revision_required", "customer_visibility_required"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["revision_gap", "customer_order_absence", "capex_delay_or_cycle_fade"], "symbol": "036930", "trigger_date": "2024-02-28", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 8. Aggregate / residual contribution

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ADVANCED_MEMORY_EQUIPMENT_VALUATION_BETA_4B_COUNTEREXAMPLE",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment valuation beta should route to 4B watch or Yellow unless explicit order/backlog/revision/customer evidence closes the bridge.",
  "source_proxy_only_count": 0
}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session.

```text
Read this standalone v12 residual research MD.
Add the machine-readable rows to the next v12 calibration candidate set only if:
1. the hard duplicate key canonical_archetype_id + symbol + trigger_type + entry_date is still absent;
2. 240810, 095610, and 036930 2024 tradable OHLC rows are re-verified from Songdaiki/stock-web;
3. C09 logic remains a guard/overlay, not a global Green threshold relaxation.

Suggested shadow axis:
- local_4b_watch_guard for advanced-equipment valuation beta without order/revision evidence
- stage2_required_bridge for C09 Green promotion when order/backlog/customer evidence is missing

Do not change production scoring directly from this single MD.
Batch with more C09 holdout cases before applying runtime weight.
```

## 10. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

