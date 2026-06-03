# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative-strength guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_DELIVERY_REVISION_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_hbm_tester_packaging_order_2024_research.md
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

This run avoids those top-covered C07 symbols and adds 003160, 031980, and 232140.  
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
003160 디아이: 2024 forward window clean; corporate-action candidates are old, outside the test window.
031980 피에스케이홀딩스: 2024 forward window clean; corporate-action candidates are old or 2019/2020, outside the selected test window.
232140 와이씨: 2024 forward window clean; corporate-action candidate is 2017-04-05, outside the test window.
```

## 3. Research thesis

C07 should not be a generic "HBM equipment is strong" bucket. It should test the order-to-delivery chain:

```text
HBM tester / advanced packaging equipment attention
→ order or customer visibility
→ backlog quality
→ delivery schedule and revenue conversion
→ margin and revision bridge
→ rerating
```

The signal is useful early because relative strength often arrives before every order detail is visible. But the same signal becomes dangerous late. A purchase order is not a perpetual engine; once the market has already priced it, the next question is delivery, margin and revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_003160_DI_20240329_HBM_TESTER_ORDER_RELATIVE_STRENGTH_STAGE2 | 003160 | positive_order_relative_strength_stage2_success_with_later_4b | 2024-03-29 | 12750 | 30800 on 2024-06-27 | 9860 on 2024-12-09 | 98.82% | 141.57% | 141.57% | -22.67% | -67.99% |
| C07_031980_PSKHOLDINGS_20240320_HBM_PACKAGING_EQUIPMENT_STAGE2 | 031980 | positive_hbm_packaging_equipment_order_stage2_success | 2024-03-20 | 45500 | 85300 on 2024-06-19 | 27700 on 2024-12-09 | 18.24% | 87.47% | 87.47% | -39.12% | -67.53% |
| C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_LOCAL_4B | 232140 | late_order_premium_counterexample | 2024-06-13 | 21900 | 22950 on 2024-06-13 | 8290 on 2024-12-09 | 4.79% | 4.79% | 4.79% | -62.15% | -63.88% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- HBM tester, memory-tester, and advanced packaging equipment relative strength are valid Stage2 routes.
- 003160 and 031980 show the useful part of C07: the signal appeared before the whole market had finished capitalizing the order/backlog path.

### Stage3 / Green
- C07 Green should require fresh order or backlog confirmation, delivery schedule, revenue conversion, margin and revision bridge.
- Relative strength is a smoke trail, not the airplane. The model should follow it, but it should not mistake it for company-level revenue conversion.

### 4B
- 232140 is the late premium guard. The order story was already heavily capitalized by the June 2024 peak, so local 4B was more useful than fresh Green.
- 003160 and 031980 also required later 4B discipline after the Stage2 success matured into a priced-in equipment order story.

### 4C
- No hard accounting or order-cancellation break is asserted.
- The C07 break mode is order-to-delivery disappointment or stale evidence: the order headline remains plausible, but delivery, margin and revision do not keep expanding enough to carry valuation.

## 6. Raw component score breakdown

```json
{
  "C07_003160_DI_20240329_HBM_TESTER_ORDER_RELATIVE_STRENGTH_STAGE2": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 2,
    "eps_fcf_explosion": 12,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 63,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  },
  "C07_031980_PSKHOLDINGS_20240320_HBM_PACKAGING_EQUIPMENT_STAGE2": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 60,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  },
  "C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_LOCAL_4B": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 33,
    "valuation_rerating_runway": 2,
    "visibility_quality": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if hbm_equipment_relative_strength and early_order_visibility:
    allow_stage2_actionable = true

if hbm_order_story_price_premium and no fresh_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and delivery_or_revision_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 232140 / 2024-06-13: HBM tester order premium can be over-promoted if the model does not require incremental order/backlog and delivery evidence after the price run.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -22.67, "MAE_30D_pct": -14.2, "MAE_90D_pct": -14.2, "MFE_180D_pct": 141.57, "MFE_30D_pct": 98.82, "MFE_90D_pct": 141.57, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_003160_DI_20240329_HBM_TESTER_ORDER_RELATIVE_STRENGTH_STAGE2", "case_role": "positive_order_relative_strength_stage2_success_with_later_4b", "company_name": "디아이", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM tester/order relative strength began to separate from generic semiconductor beta; later local 4B discipline was required once the order story was capitalized.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.99, "entry_date": "2024-03-29", "entry_price": 12750, "evidence_family": "hbm_tester_order_relative_strength_to_equipment_rerating", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_DELIVERY_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 9860, "peak_date": "2024-06-27", "peak_price": 30800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003160.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 2, "eps_fcf_explosion": 12, "information_confidence": 4, "market_mispricing": 12, "total": 63, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C07_003160_DI_20240329_HBM_TESTER_ORDER_RELATIVE_STRENGTH_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_equipment_order_attention", "tester_or_advanced_packaging_relative_strength", "customer_or_backlog_visibility_claim"], "stage3_evidence_fields": ["fresh_order_or_backlog_confirmation_required", "delivery_schedule_and_revenue_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["order_story_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "delivery_delay_or_backlog_quality_gap", "equipment_theme_mean_reversion"], "symbol": "003160", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "trigger_date": "2024-03-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.12, "MAE_30D_pct": -13.96, "MAE_90D_pct": -13.96, "MFE_180D_pct": 87.47, "MFE_30D_pct": 18.24, "MFE_90D_pct": 87.47, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_031980_PSKHOLDINGS_20240320_HBM_PACKAGING_EQUIPMENT_STAGE2", "case_role": "positive_hbm_packaging_equipment_order_stage2_success", "company_name": "피에스케이홀딩스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful where advanced packaging / HBM equipment relative strength connected to order and delivery optionality, but Green still required backlog quality, delivery timing and margin/revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.53, "entry_date": "2024-03-20", "entry_price": 45500, "evidence_family": "hbm_advanced_packaging_equipment_relative_strength_order_visibility", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_DELIVERY_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 27700, "peak_date": "2024-06-19", "peak_price": 85300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/031/031980.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 60, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C07_031980_PSKHOLDINGS_20240320_HBM_PACKAGING_EQUIPMENT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_equipment_order_attention", "tester_or_advanced_packaging_relative_strength", "customer_or_backlog_visibility_claim"], "stage3_evidence_fields": ["fresh_order_or_backlog_confirmation_required", "delivery_schedule_and_revenue_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["order_story_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "delivery_delay_or_backlog_quality_gap", "equipment_theme_mean_reversion"], "symbol": "031980", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "trigger_date": "2024-03-20", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -62.15, "MAE_30D_pct": -36.99, "MAE_90D_pct": -51.42, "MFE_180D_pct": 4.79, "MFE_30D_pct": 4.79, "MFE_90D_pct": 4.79, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_LOCAL_4B", "case_role": "late_order_premium_counterexample", "company_name": "와이씨", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late HBM tester/order premium should route to local 4B or Yellow unless incremental backlog, delivery and revision evidence keep expanding; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.88, "entry_date": "2024-06-13", "entry_price": 21900, "evidence_family": "hbm_tester_order_theme_price_premium_without_incremental_backlog_delivery_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_DELIVERY_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 8290, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 4, "total": 33, "valuation_rerating_runway": 2, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_equipment_order_attention", "tester_or_advanced_packaging_relative_strength", "customer_or_backlog_visibility_claim"], "stage3_evidence_fields": ["fresh_order_or_backlog_confirmation_required", "delivery_schedule_and_revenue_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["order_story_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "delivery_delay_or_backlog_quality_gap", "equipment_theme_mean_reversion"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-06-13", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_DELIVERY_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_equipment_order_relative_strength_new_symbols_and_late_premium_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM equipment-order relative-strength rows should allow Stage2 when tester/advanced-packaging equipment relative strength precedes backlog and delivery confirmation, but Stage3 Green requires fresh order/backlog, delivery schedule, revenue conversion, margin and revision bridge; late order-story price premium should route to local 4B.",
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
3. Add C07-specific HBM equipment order/backlog/delivery-margin guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_EARLY_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
- C07_GREEN_REQUIRES_FRESH_ORDER_BACKLOG_DELIVERY_MARGIN_REVISION
- C07_LATE_HBM_ORDER_PREMIUM_LOCAL_4B
- C07_ORDER_STORY_WITHOUT_INCREMENTAL_DELIVERY_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

