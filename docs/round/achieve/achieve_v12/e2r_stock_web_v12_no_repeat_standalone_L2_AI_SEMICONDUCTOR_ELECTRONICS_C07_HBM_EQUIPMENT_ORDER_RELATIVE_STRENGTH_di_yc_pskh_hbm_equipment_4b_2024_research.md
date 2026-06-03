# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative-strength / tester-packaging 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|false_green_order_optional_value_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_di_yc_pskh_hbm_equipment_4b_2024_research.md
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

This run avoids those top-covered C07 symbols and adds 003160, 232140, and 031980.  
Each row uses a new `C07 + symbol + trigger_type + entry_date` hard key.

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
003160 디아이: selected 2024 forward window clean; corporate-action candidates are historical and outside selected test window.
232140 와이씨/와이아이케이: selected 2024 forward window clean; corporate-action candidate is 2017-04-05 and outside selected test window.
031980 피에스케이홀딩스: selected 2024 forward window clean; corporate-action candidates are historical and latest 2020-02-21, outside selected test window.
```

## 3. Research thesis

C07 should split fresh HBM equipment order-relative-strength from already-capitalized order optionality:

```text
HBM tester / packaging equipment relative strength
→ named customer order or allocation visibility
→ delivery schedule, acceptance and revenue-recognition cadence
→ backlog conversion and capacity utilization
→ gross margin and revision bridge
→ rerating or local 4B cap
```

Relative strength is the smoke from a hot equipment cycle. Stage2 can buy it when orders and delivery cadence are visible, but Green should require the purchase order to become accepted equipment, recognized revenue and margin revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_003160_DI_20240305_HBM_TESTER_ORDER_RS_STAGE2 | 003160 | positive_hbm_tester_order_relative_strength_stage2_success_with_later_4b_refresh | 2024-03-05 | 11740 | 30800 on 2024-06-27 | 9860 on 2024-12-09 | 46.51% | 93.78% | 162.35% | -16.01% | -67.99% |
| C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_4B | 232140 | hbm_tester_order_price_premium_counterexample | 2024-06-13 | 21900 | 22950 on 2024-06-13 | 8290 on 2024-12-09 | 4.79% | 4.79% | 4.79% | -62.15% | -63.88% |
| C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B | 031980 | hbm_packaging_equipment_false_green_counterexample | 2024-06-14 | 80000 | 85300 on 2024-06-19 | 27700 on 2024-12-09 | 6.62% | 6.62% | 6.62% | -65.38% | -67.53% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 003160 is the positive anchor. The March 2024 HBM tester/equipment relative-strength route produced large MFE before the June premium required 4B refresh discipline.
- Stage2 is allowed only when price action is backed by customer/order allocation, delivery schedule, acceptance and margin/revision visibility.

### Stage3 / Green
- C07 Green should require named customer order or allocation, delivery schedule, acceptance, revenue recognition, backlog conversion and margin/revision confirmation.
- 031980 is the false-Green guard: packaging-equipment relative strength was real, but the June 2024 price already capitalized much of the order optionality and later required incremental delivery/margin proof.

### 4B
- 232140 fills the tester order price-premium 4B pocket. The June trigger had small residual upside and much larger forward drawdown.
- 031980 fills the packaging-equipment version of the same failure: a strong equipment narrative can turn into price-only if delivery acceptance and margin revisions do not refresh.
- 003160 also shows that valid Stage2 can transition into 4B once the rerating has already paid for the order narrative.

### 4C
- No hard customer cancellation, delivery failure or accounting break is asserted.
- The C07 break mode is order-to-revenue exhaustion: the equipment thesis may remain real, but order optionality, acceptance, revenue recognition and margin evidence no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C07_003160_DI_20240305_HBM_TESTER_ORDER_RS_STAGE2": {
    "customer_allocation_quality": 8,
    "delivery_acceptance_revenue_cadence": 7,
    "hbm_equipment_order_visibility": 10,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 10,
    "relative_strength_confirmation": 10,
    "total": 63,
    "valuation_rerating_runway": 7
  },
  "C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B": {
    "customer_allocation_quality": 4,
    "delivery_acceptance_revenue_cadence": 3,
    "hbm_equipment_order_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_confirmation": 7,
    "total": 30,
    "valuation_rerating_runway": 1
  },
  "C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_4B": {
    "customer_allocation_quality": 5,
    "delivery_acceptance_revenue_cadence": 3,
    "hbm_equipment_order_visibility": 6,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_confirmation": 7,
    "total": 32,
    "valuation_rerating_runway": 1
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
- 232140 / 2024-06-13: HBM tester order premium can be over-promoted if the model treats price strength as fresh customer order and delivery-margin proof.
- 031980 / 2024-06-14: packaging-equipment relative strength can look like Yellow-to-Green, but fails without renewed delivery, acceptance, revenue cadence and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -16.01, "MAE_30D_pct": -21.29, "MAE_90D_pct": -21.29, "MFE_180D_pct": 162.35, "MFE_30D_pct": 46.51, "MFE_90D_pct": 93.78, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_003160_DI_20240305_HBM_TESTER_ORDER_RS_STAGE2", "case_role": "positive_hbm_tester_order_relative_strength_stage2_success_with_later_4b_refresh", "company_name": "디아이", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM tester/equipment relative strength appeared before the order/capacity theme was fully capitalized. Green still requires named customer order or allocation, delivery schedule, acceptance/yield, revenue-recognition cadence, backlog conversion and margin/revision bridge; after the June 2024 premium the same evidence required local 4B refresh discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.99, "entry_date": "2024-03-05", "entry_price": 11740, "evidence_family": "hbm_tester_equipment_order_relative_strength_customer_allocation_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 9860, "peak_date": "2024-06-27", "peak_price": 30800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003160.json", "raw_component_score_breakdown": {"customer_allocation_quality": 8, "delivery_acceptance_revenue_cadence": 7, "hbm_equipment_order_visibility": 10, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 10, "relative_strength_confirmation": 10, "total": 63, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C07_003160_DI_20240305_HBM_TESTER_ORDER_RS_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_or_tester_order_relative_strength", "customer_order_or_allocation_visibility", "delivery_acceptance_revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["named_customer_order_or_allocation_required", "delivery_schedule_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_allocation_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "003160", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "trigger_date": "2024-03-05", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -62.15, "MAE_30D_pct": -35.57, "MAE_90D_pct": -42.24, "MFE_180D_pct": 4.79, "MFE_30D_pct": 4.79, "MFE_90D_pct": 4.79, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_4B", "case_role": "hbm_tester_order_price_premium_counterexample", "company_name": "와이씨", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2017-04-05 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM tester order/equipment price premium should route to local 4B or counterexample when the stock has already capitalized customer/order optionality and incremental delivery acceptance, revenue cadence, backlog conversion and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.88, "entry_date": "2024-06-13", "entry_price": 21900, "evidence_family": "hbm_tester_order_price_premium_without_incremental_delivery_acceptance_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 8290, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"customer_allocation_quality": 5, "delivery_acceptance_revenue_cadence": 3, "hbm_equipment_order_visibility": 6, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_confirmation": 7, "total": 32, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_232140_YC_20240613_HBM_TESTER_ORDER_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_or_tester_order_relative_strength", "customer_order_or_allocation_visibility", "delivery_acceptance_revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["named_customer_order_or_allocation_required", "delivery_schedule_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_allocation_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-06-13", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -65.38, "MAE_30D_pct": -28.75, "MAE_90D_pct": -49.75, "MFE_180D_pct": 6.62, "MFE_30D_pct": 6.62, "MFE_90D_pct": 6.62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B", "case_role": "hbm_packaging_equipment_false_green_counterexample", "company_name": "피에스케이홀딩스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2020-02-21, outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM packaging-equipment relative strength should remain Yellow or local 4B when price confirmation is not followed by incremental customer order, delivery schedule, acceptance, revenue recognition and margin/revision evidence. The late June premium had small residual upside and much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.53, "entry_date": "2024-06-14", "entry_price": 80000, "evidence_family": "hbm_packaging_equipment_relative_strength_price_confirmation_without_incremental_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 27700, "peak_date": "2024-06-19", "peak_price": 85300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/031/031980.json", "raw_component_score_breakdown": {"customer_allocation_quality": 4, "delivery_acceptance_revenue_cadence": 3, "hbm_equipment_order_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_confirmation": 7, "total": 30, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_or_tester_order_relative_strength", "customer_order_or_allocation_visibility", "delivery_acceptance_revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["named_customer_order_or_allocation_required", "delivery_schedule_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_allocation_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "031980", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "trigger_date": "2024-06-14", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_TESTER_PACKAGING_EQUIPMENT_ORDER_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_equipment_order_relative_strength_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM equipment rows should allow Stage2 when relative strength is backed by customer order/allocation, delivery acceptance, revenue cadence and margin-revision bridge, but should route to local 4B/Yellow when price already capitalizes order optionality and incremental delivery or margin evidence has not refreshed.",
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
3. Add C07-specific HBM equipment / tester / packaging order-relative-strength / delivery-acceptance / revenue-cadence / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_CUSTOMER_ORDER_DELIVERY_MARGIN_REVISION_BRIDGE
- C07_GREEN_REQUIRES_ORDER_ALLOCATION_DELIVERY_ACCEPTANCE_REVENUE_CADENCE_REVISION
- C07_HBM_EQUIPMENT_PRICE_PREMIUM_LOCAL_4B
- C07_RELATIVE_STRENGTH_WITHOUT_ORDER_TO_REVENUE_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

