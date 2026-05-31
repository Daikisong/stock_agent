# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative-strength / second-wave tester-packaging 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TESTER_PACKAGING_SECOND_WAVE_ORDER_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_refresh_after_stage2_success|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_yc_exicon_pskh_second_wave_4b_2024_research.md
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

This run avoids those top-covered C07 symbols and uses new hard keys:
```text
C07 + 232140 + Stage2-Actionable + 2024-04-18
C07 + 092870 + 4B-local-price-only + 2024-07-01
C07 + 031980 + Stage3-Yellow + 2024-10-17
```

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
232140 와이씨/와이아이케이: selected 2024 forward window clean; corporate-action candidate is 2017-04-05 and outside selected test window.
092870 엑시콘: has 2024-07-31 corporate-action candidate; immediate 4B proximity row is usable narratively, but full-window calibration is caveated.
031980 피에스케이홀딩스: selected 2024 forward window clean; corporate-action candidates are historical and latest 2020-02-21, outside selected test window.
```

## 3. Research thesis

C07 should distinguish fresh HBM equipment order-relative-strength from second-wave order optionality that has already been capitalized:

```text
HBM tester / packaging equipment relative strength
→ named customer order or allocation visibility
→ delivery schedule, acceptance and revenue-recognition cadence
→ backlog conversion and capacity utilization
→ gross margin and revision bridge
→ rerating or local 4B cap
```

Relative strength is smoke from a hot equipment cycle. Stage2 can buy it when orders become deliverable revenue; Green should require the equipment to be accepted, recognized and revised into margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_232140_YC_20240418_HBM_TESTER_ORDER_STAGE2 | 232140 | positive_hbm_tester_order_stage2_success_with_later_4b_refresh | 2024-04-18 | 9460 | 22950 on 2024-06-13 | 8290 on 2024-12-09 | 98.31% | 142.6% | 142.6% | -12.37% | -63.88% |
| C07_092870_EXICON_20240701_HBM_TESTER_PRICE_PREMIUM_4B | 092870 | hbm_tester_price_premium_counterexample | 2024-07-01 | 21650 | 25150 on 2024-07-08 | 8410 on 2024-12-09 | 16.17% | 16.17% | 16.17% | -61.15% | -66.56% |
| C07_031980_PSKH_20241017_HBM_PACKAGING_EQUIPMENT_FALSE_GREEN | 031980 | hbm_packaging_equipment_second_wave_false_green_counterexample | 2024-10-17 | 54500 | 54500 on 2024-10-17 | 27700 on 2024-12-09 | 0.0% | 0.0% | 0.0% | -49.17% | -49.17% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 232140 is the positive anchor. The April 2024 HBM tester route captured a large move before the June premium became a 4B refresh problem.
- Stage2 is allowed only when price relative strength is backed by customer allocation/order visibility, delivery schedule, acceptance and margin/revision visibility.

### Stage3 / Green
- C07 Green should require named customer order or allocation, delivery schedule, acceptance, revenue recognition, backlog conversion and margin/revision confirmation.
- 031980 is the second-wave false-Green guard: price confirmation was present in October, but the forward drawdown showed that delivery/margin evidence had not refreshed enough for Green.

### 4B
- 092870 fills a tester price-premium pocket. Because the symbol has a 2024-07-31 corporate-action candidate, it is caveated for full-window aggregation, but it still helps define local 4B proximity behavior.
- 031980 is a clean second-wave packaging-equipment counterexample: order optionality remained plausible, but price had already paid for too much without fresh delivery and revision evidence.
- 232140 also demonstrates that valid Stage2 can turn into local 4B after the order narrative is capitalized.

### 4C
- No hard customer cancellation, delivery failure or accounting break is asserted.
- The break mode is order-to-revenue exhaustion: the HBM equipment thesis may remain real while order optionality, acceptance, revenue recognition and margin evidence no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C07_031980_PSKH_20241017_HBM_PACKAGING_EQUIPMENT_FALSE_GREEN": {
    "customer_allocation_quality": 4,
    "delivery_acceptance_revenue_cadence": 3,
    "hbm_equipment_order_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_confirmation": 6,
    "total": 29,
    "valuation_rerating_runway": 1
  },
  "C07_092870_EXICON_20240701_HBM_TESTER_PRICE_PREMIUM_4B": {
    "customer_allocation_quality": 4,
    "delivery_acceptance_revenue_cadence": 3,
    "hbm_equipment_order_visibility": 6,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_confirmation": 6,
    "total": 30,
    "valuation_rerating_runway": 1
  },
  "C07_232140_YC_20240418_HBM_TESTER_ORDER_STAGE2": {
    "customer_allocation_quality": 8,
    "delivery_acceptance_revenue_cadence": 7,
    "hbm_equipment_order_visibility": 10,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 10,
    "relative_strength_confirmation": 10,
    "total": 64,
    "valuation_rerating_runway": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if HBM_equipment_relative_strength and customer_order_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if HBM_equipment_price_premium and no incremental_order_delivery_acceptance_revenue_margin_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_to_revenue_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 092870 / 2024-07-01: tester price premium can be over-promoted if price strength substitutes for fresh order, delivery and margin proof.
- 031980 / 2024-10-17: second-wave packaging-equipment confirmation can look like Yellow-to-Green, but fails without renewed delivery, revenue cadence and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.37, "MAE_30D_pct": -6.66, "MAE_90D_pct": -6.66, "MFE_180D_pct": 142.6, "MFE_30D_pct": 98.31, "MFE_90D_pct": 142.6, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_232140_YC_20240418_HBM_TESTER_ORDER_STAGE2", "case_role": "positive_hbm_tester_order_stage2_success_with_later_4b_refresh", "company_name": "와이씨", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2017-04-05 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM tester/order relative strength began before the full tester-order premium was capitalized. Green still requires named customer allocation, delivery schedule, acceptance, revenue-recognition cadence and margin/revision bridge; after the June premium the same evidence required 4B refresh discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.88, "entry_date": "2024-04-18", "entry_price": 9460, "evidence_family": "hbm_tester_equipment_order_customer_allocation_delivery_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_SECOND_WAVE_ORDER_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 8290, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"customer_allocation_quality": 8, "delivery_acceptance_revenue_cadence": 7, "hbm_equipment_order_visibility": 10, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 10, "relative_strength_confirmation": 10, "total": 64, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C07_232140_YC_20240418_HBM_TESTER_ORDER_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_or_tester_order_relative_strength", "customer_order_or_allocation_visibility", "delivery_acceptance_revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["named_customer_order_or_allocation_required", "delivery_schedule_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_allocation_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-04-18", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -61.15, "MAE_30D_pct": -17.92, "MAE_90D_pct": -49.98, "MFE_180D_pct": 16.17, "MFE_30D_pct": 16.17, "MFE_90D_pct": 16.17, "calibration_caveat": "post-candidate full-window caveated because selected symbol has 2024-07-31 corporate-action candidate", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": false, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_092870_EXICON_20240701_HBM_TESTER_PRICE_PREMIUM_4B", "case_role": "hbm_tester_price_premium_counterexample", "company_name": "엑시콘", "corporate_action_window_status": "clean_pre_2024_07_31_window for immediate 4B proximity; profile has a 2024-07-31 corporate-action candidate, so post-candidate full-window interpretation is marked caveated", "current_profile_error": true, "current_profile_verdict": "HBM tester price premium should route to local 4B or counterexample when price already capitalizes the order optionality and incremental delivery acceptance, revenue cadence, backlog conversion and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.56, "entry_date": "2024-07-01", "entry_price": 21650, "evidence_family": "hbm_tester_price_premium_without_incremental_order_delivery_acceptance_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_SECOND_WAVE_ORDER_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 8410, "peak_date": "2024-07-08", "peak_price": 25150, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/092/092870.json", "raw_component_score_breakdown": {"customer_allocation_quality": 4, "delivery_acceptance_revenue_cadence": 3, "hbm_equipment_order_visibility": 6, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_confirmation": 6, "total": 30, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_092870_EXICON_20240701_HBM_TESTER_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_or_tester_order_relative_strength", "customer_order_or_allocation_visibility", "delivery_acceptance_revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["named_customer_order_or_allocation_required", "delivery_schedule_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_allocation_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "092870", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv", "trigger_date": "2024-07-01", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.17, "MAE_30D_pct": -23.67, "MAE_90D_pct": -49.17, "MFE_180D_pct": 0.0, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_031980_PSKH_20241017_HBM_PACKAGING_EQUIPMENT_FALSE_GREEN", "case_role": "hbm_packaging_equipment_second_wave_false_green_counterexample", "company_name": "피에스케이홀딩스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2020-02-21, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Second-wave HBM packaging-equipment relative strength should stay Yellow or route to local 4B when price confirmation is not followed by incremental customer order, delivery schedule, acceptance, revenue recognition and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.17, "entry_date": "2024-10-17", "entry_price": 54500, "evidence_family": "hbm_packaging_equipment_second_wave_relative_strength_without_incremental_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_SECOND_WAVE_ORDER_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 27700, "peak_date": "2024-10-17", "peak_price": 54500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/031/031980.json", "raw_component_score_breakdown": {"customer_allocation_quality": 4, "delivery_acceptance_revenue_cadence": 3, "hbm_equipment_order_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_confirmation": 6, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_031980_PSKH_20241017_HBM_PACKAGING_EQUIPMENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_or_tester_order_relative_strength", "customer_order_or_allocation_visibility", "delivery_acceptance_revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["named_customer_order_or_allocation_required", "delivery_schedule_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_allocation_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "031980", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "trigger_date": "2024-10-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 2,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "caveated_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_TESTER_PACKAGING_SECOND_WAVE_ORDER_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_equipment_order_relative_strength_second_wave_4b_new_dates",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM equipment rows should allow Stage2 only when relative strength is backed by customer order/allocation, delivery acceptance, revenue cadence and margin-revision bridge; second-wave tester/packaging price premiums should route to local 4B/Yellow when incremental delivery or margin evidence has not refreshed.",
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
3. Treat 092870 as caveated for full-window aggregation because the post-trigger path crosses a 2024-07-31 corporate-action candidate.
4. Add C07-specific HBM equipment / tester / packaging order-relative-strength / delivery-acceptance / revenue-cadence / margin-revision / local-4B refresh guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_CUSTOMER_ORDER_DELIVERY_MARGIN_REVISION_BRIDGE
- C07_GREEN_REQUIRES_ORDER_ALLOCATION_DELIVERY_ACCEPTANCE_REVENUE_CADENCE_REVISION
- C07_SECOND_WAVE_HBM_EQUIPMENT_PRICE_PREMIUM_LOCAL_4B
- C07_RELATIVE_STRENGTH_WITHOUT_ORDER_TO_REVENUE_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

