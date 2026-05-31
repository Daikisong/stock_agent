# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative-strength guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TEST_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_hbm_test_deposition_equipment_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH current coverage:
rows=8, symbols=5, date range=2024-01-19~2024-06-13, good/bad S2=2/0, 4B/4C=1/0
top covered symbols: 042700(3), 089030(2), 039030(1), 058470(1), 095340(1)
```

This run avoids the top-covered C07 symbols and adds 232140, 240810, and 036930.  
Each row uses a new `C07 + symbol + trigger_type + entry_date` hard key.

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

Selected profiles:
```text
232140 와이씨: 2024 window clean; corporate-action candidate is 2017-04-05.
240810 원익IPS: corporate_action_candidate_count=0.
036930 주성엔지니어링: 2024 window clean; corporate-action candidate is 2000-06-22.
```

## 3. Research thesis

C07 is not a generic semiconductor equipment bucket. It should test whether HBM/memory equipment attention actually becomes order visibility:

```text
HBM or advanced-memory equipment attention
→ relative strength
→ order/backlog/customer qualification
→ revision bridge
→ rerating
```

The positive rows show that C07 can catch sharp equipment reratings. The counterexample row shows the guard: if relative strength is only equipment beta, the signal should stop at Stage2/Yellow or local 4B watch.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_232140_YC_20240417_HBM_TESTER_ORDER_RELATIVE_STRENGTH | 232140 | positive_structural_success_with_4b_guard | 2024-04-17 | 7280 | 22950 on 2024-06-13 | 6280 on 2024-04-17 | 142.58% | 215.25% | 215.25% | -13.74% | -63.79% |
| C07_240810_WONIKIPS_20240229_MEMORY_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 240810 | positive_high_mae_success | 2024-02-29 | 32800 | 44850 on 2024-04-08 | 27800 on 2024-09-11 | 36.74% | 36.74% | 36.74% | -15.24% | -38.02% |
| C07_036930_JUSUNG_20240228_DEPOSITION_EQUIPMENT_FALSE_GREEN | 036930 | false_green_counterexample | 2024-02-28 | 40000 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 3.62% | 3.62% | 3.62% | -44.88% | -46.8% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- HBM equipment attention and relative strength are valid research triggers.
- 240810 and 232140 show that the market rewarded equipment names before the full earnings bridge was visible.

### Stage3 / Green
- C07 Green should require actual order/backlog, customer qualification, and revision confirmation.
- The row must not inherit C06 customer-capacity credit unless the equipment supplier has its own order evidence.

### 4B
- 232140 is the clearest 4B guard row: a large HBM tester rerating needed local blowoff discipline after June 2024.
- 240810 also shows that a valid Stage2 move can later become high-MAE if the order/revision bridge is incomplete.

### 4C
- 036930 is a false-Green / thesis-gap counterexample.
- The failure mode is order/revision gap, not necessarily hard accounting break.

## 6. Raw component score breakdown

```json
{
  "C07_036930_JUSUNG_20240228_DEPOSITION_EQUIPMENT_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 35,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  },
  "C07_232140_YC_20240417_HBM_TESTER_ORDER_RELATIVE_STRENGTH": {
    "bottleneck_pricing_power": 13,
    "capital_allocation": 2,
    "eps_fcf_explosion": 13,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 67,
    "valuation_rerating_runway": 9,
    "visibility_quality": 14
  },
  "C07_240810_WONIKIPS_20240229_MEMORY_EQUIPMENT_ORDER_RELATIVE_STRENGTH": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 3,
    "market_mispricing": 11,
    "total": 55,
    "valuation_rerating_runway": 9,
    "visibility_quality": 10
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if hbm_equipment_relative_strength and no order_or_customer_qualification_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if equipment_price_run and no new non_price_order_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and revision_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 036930 / 2024-02-28: deposition/equipment beta could be over-promoted if C07 treats relative strength as order visibility.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.74, "MAE_30D_pct": -13.74, "MAE_90D_pct": -13.74, "MFE_180D_pct": 215.25, "MFE_30D_pct": 142.58, "MFE_90D_pct": 215.25, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_232140_YC_20240417_HBM_TESTER_ORDER_RELATIVE_STRENGTH", "case_role": "positive_structural_success_with_4b_guard", "company_name": "와이씨", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "C07 Stage3-Yellow/Green is reasonable only if tester order and customer qualification evidence close; after the blowoff, local 4B discipline is required.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.79, "entry_date": "2024-04-17", "entry_price": 7280, "evidence_family": "hbm_memory_tester_order_relative_strength_with_customer_visibility", "evidence_url_pending": false, "fine_archetype_id": "HBM_TEST_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-04-17", "low_price_180d": 6280, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 13, "capital_allocation": 2, "eps_fcf_explosion": 13, "information_confidence": 4, "market_mispricing": 12, "total": 67, "valuation_rerating_runway": 9, "visibility_quality": 14}, "reuse_reason": null, "same_entry_group_id": "C07_232140_YC_20240417_HBM_TESTER_ORDER_RELATIVE_STRENGTH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_or_memory_equipment_attention", "relative_strength", "order_or_customer_visibility_claim"], "stage3_evidence_fields": ["actual_order_or_backlog_confirmation_required", "customer_qualification_required", "revision_bridge_required"], "stage4b_evidence_fields": ["late_equipment_beta_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "customer_visibility_failure", "equipment_beta_mean_reversion"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-04-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -15.24, "MAE_30D_pct": -2.29, "MAE_90D_pct": -2.29, "MFE_180D_pct": 36.74, "MFE_30D_pct": 36.74, "MFE_90D_pct": 36.74, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_240810_WONIKIPS_20240229_MEMORY_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_role": "positive_high_mae_success", "company_name": "원익IPS", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 worked as early memory/HBM equipment attention, but Green should wait for order/backlog and revision bridge rather than inheriting C06 customer-capacity credit.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.02, "entry_date": "2024-02-29", "entry_price": 32800, "evidence_family": "memory_equipment_hbm_capex_attention_without_full_customer_order_lock", "evidence_url_pending": false, "fine_archetype_id": "HBM_TEST_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-11", "low_price_180d": 27800, "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/240/240810.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 3, "market_mispricing": 11, "total": 55, "valuation_rerating_runway": 9, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C07_240810_WONIKIPS_20240229_MEMORY_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_or_memory_equipment_attention", "relative_strength", "order_or_customer_visibility_claim"], "stage3_evidence_fields": ["actual_order_or_backlog_confirmation_required", "customer_qualification_required", "revision_bridge_required"], "stage4b_evidence_fields": ["late_equipment_beta_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "customer_visibility_failure", "equipment_beta_mean_reversion"], "symbol": "240810", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "trigger_date": "2024-02-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.88, "MAE_30D_pct": -16.37, "MAE_90D_pct": -16.37, "MFE_180D_pct": 3.62, "MFE_30D_pct": 3.62, "MFE_90D_pct": 3.62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_036930_JUSUNG_20240228_DEPOSITION_EQUIPMENT_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "AI/HBM equipment beta should not become C07 Green unless actual order, customer, backlog, and revision evidence arrive.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-02-28", "entry_price": 40000, "evidence_family": "deposition_equipment_ai_memory_beta_without_hbm_order_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_TEST_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 6, "total": 35, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C07_036930_JUSUNG_20240228_DEPOSITION_EQUIPMENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_or_memory_equipment_attention", "relative_strength", "order_or_customer_visibility_claim"], "stage3_evidence_fields": ["actual_order_or_backlog_confirmation_required", "customer_qualification_required", "revision_bridge_required"], "stage4b_evidence_fields": ["late_equipment_beta_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "customer_visibility_failure", "equipment_beta_mean_reversion"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-02-28", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_TEST_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_equipment_new_symbol_and_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM-equipment relative strength should permit Stage2/Yellow on equipment beta, but Stage3 Green requires actual order/backlog/customer-qualification/revision bridge; relative strength alone should route to Yellow or local 4B watch.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C07 + symbol + trigger_type + entry_date.
3. Add C07-specific order/customer/revision bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C07_HBM_EQUIPMENT_GREEN_REQUIRES_ORDER_BACKLOG_CUSTOMER_QUALIFICATION
- C07_EQUIPMENT_RELATIVE_STRENGTH_STAGE2_CAP
- C07_LATE_EQUIPMENT_BETA_LOCAL_4B

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

