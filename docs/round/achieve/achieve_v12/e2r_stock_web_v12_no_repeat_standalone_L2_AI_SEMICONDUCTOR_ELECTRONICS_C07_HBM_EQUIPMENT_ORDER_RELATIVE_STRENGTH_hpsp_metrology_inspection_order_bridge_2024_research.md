# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative-strength guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_EQUIPMENT_CUSTOMER_ORDER_RELATIVE_STRENGTH_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_hpsp_metrology_inspection_order_bridge_2024_research.md
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

This run avoids those top-covered C07 symbols and adds 403870, 348210, and 322310.  
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
403870 HPSP: selected 2024 forward window clean; corporate-action candidates are 2023-03-16 and 2023-04-11, outside selected test window.
348210 넥스틴: selected 2024 forward window clean; corporate-action candidates are 2021-01-13 and 2021-01-27, outside selected test window.
322310 오로스테크놀로지: corporate_action_candidate_count=0.
```

## 3. Research thesis

C07 should not treat equipment relative strength itself as the orderbook. It should test whether the price strength is backed by a customer-order bridge:

```text
HBM / advanced equipment relative strength
→ customer or process qualification
→ signed order or allocation visibility
→ delivery schedule and utilization
→ ASP/mix, gross margin and revision bridge
→ rerating or local 4B cap
```

Equipment relative strength is the machine humming in the next room. Green should not buy the sound alone; it should require the purchase order, delivery date, utilization and margin invoice.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_403870_HPSP_20240119_HIGH_PRESSURE_EQUIPMENT_RS_STAGE2 | 403870 | positive_high_pressure_anneal_equipment_relative_strength_stage2_success_with_later_4b | 2024-01-19 | 47800 | 63900 on 2024-02-15 | 22650 on 2024-08-05 | 33.68% | 33.68% | 33.68% | -52.62% | -64.55% |
| C07_348210_NEXTIN_20240405_INSPECTION_EQUIPMENT_RS_FALSE_GREEN | 348210 | inspection_equipment_relative_strength_false_green_counterexample | 2024-04-05 | 66300 | 77500 on 2024-06-21 | 40350 on 2024-09-09 | 7.24% | 16.89% | 16.89% | -39.14% | -47.94% |
| C07_322310_AUROS_20240704_OVERLAY_METROLOGY_ORDER_PREMIUM_4B | 322310 | overlay_metrology_equipment_order_price_premium_counterexample | 2024-07-04 | 26600 | 27050 on 2024-07-04 | 15130 on 2024-09-09 | 1.69% | 1.69% | 1.69% | -43.12% | -44.07% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Equipment relative strength can be a valid Stage2 route when customer/process qualification and order/delivery visibility arrive before the valuation fully capitalizes the equipment cycle.
- 403870 is the positive anchor. The January 2024 HPSP route produced a large 30D/90D MFE with tolerable early MAE. It then became a later 4B discipline problem because the February premium needed incremental order and revision evidence to stay Green.

### Stage3 / Green
- C07 Green should require signed order or customer allocation, delivery schedule, utilization, ASP/mix, gross margin and revision confirmation.
- 348210 shows why inspection/metrology equipment price confirmation should stay Yellow if fresh order, delivery and margin evidence do not keep expanding after the price move.

### 4B
- 322310 fills the local 4B pocket: the July 2024 overlay/metrology spike had almost no forward upside from the trigger price and then drew down sharply as customer-allocation and delivery evidence did not refresh.
- 348210 is a false-Green/Yellow-to-4B counterexample. The stock had some MFE, but the later MAE and post-peak drawdown show that relative strength alone was not an orderbook bridge.
- 403870 also required 4B discipline after the initial Stage2 success matured into a fully capitalized equipment premium.

### 4C
- No hard customer cancellation, order cancellation, or accounting break is asserted.
- The C07 break mode is evidence exhaustion: equipment demand remains plausible, but customer allocation, signed order, delivery, utilization, ASP/mix, gross margin and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C07_322310_AUROS_20240704_OVERLAY_METROLOGY_ORDER_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C07_348210_NEXTIN_20240405_INSPECTION_EQUIPMENT_RS_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C07_403870_HPSP_20240119_HIGH_PRESSURE_EQUIPMENT_RS_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if equipment_relative_strength and customer_process_qualification_order_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if equipment_relative_strength_price_premium and no incremental_order_customer_allocation_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_to_delivery_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 348210 / 2024-04-05: inspection equipment relative strength can be over-promoted if the model treats price confirmation as fresh order and delivery-margin proof.
- 322310 / 2024-07-04: overlay/metrology equipment spike can become price-only when customer allocation, utilization and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -52.62, "MAE_30D_pct": -8.37, "MAE_90D_pct": -18.2, "MFE_180D_pct": 33.68, "MFE_30D_pct": 33.68, "MFE_90D_pct": 33.68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_403870_HPSP_20240119_HIGH_PRESSURE_EQUIPMENT_RS_STAGE2", "case_role": "positive_high_pressure_anneal_equipment_relative_strength_stage2_success_with_later_4b", "company_name": "HPSP", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2023-03-16 and 2023-04-11, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when advanced equipment relative strength attached to customer/process qualification, scarce equipment positioning and a plausible order/revision route. Green still requires incremental order visibility, customer allocation, delivery schedule, utilization, ASP/mix, gross margin and revision bridge; after the February 2024 premium, the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -64.55, "entry_date": "2024-01-19", "entry_price": 47800, "evidence_family": "advanced_semiconductor_high_pressure_equipment_customer_order_relative_strength_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "HBM_EQUIPMENT_CUSTOMER_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-08-05", "low_price_180d": 22650, "peak_date": "2024-02-15", "peak_price": 63900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/403/403870.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C07_403870_HPSP_20240119_HIGH_PRESSURE_EQUIPMENT_RS_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["equipment_relative_strength_attention", "customer_or_process_qualification_visibility", "order_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_order_or_customer_allocation_required", "delivery_schedule_and_utilization_required", "ASP_mix_gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["equipment_relative_strength_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_to_delivery_gap", "customer_allocation_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "403870", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv", "trigger_date": "2024-01-19", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.14, "MAE_30D_pct": -16.29, "MAE_90D_pct": -32.28, "MFE_180D_pct": 16.89, "MFE_30D_pct": 7.24, "MFE_90D_pct": 16.89, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_348210_NEXTIN_20240405_INSPECTION_EQUIPMENT_RS_FALSE_GREEN", "case_role": "inspection_equipment_relative_strength_false_green_counterexample", "company_name": "넥스틴", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2021-01-13 and 2021-01-27, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Inspection/metrology equipment relative strength should stay Yellow if price confirmation is not followed by fresh customer order, delivery schedule, utilization, margin and revision evidence. The later drawdown shows the error of treating equipment beta as customer-order proof.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.94, "entry_date": "2024-04-05", "entry_price": 66300, "evidence_family": "inspection_metrology_equipment_price_confirmation_without_incremental_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_EQUIPMENT_CUSTOMER_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 40350, "peak_date": "2024-06-21", "peak_price": 77500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/348/348210.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C07_348210_NEXTIN_20240405_INSPECTION_EQUIPMENT_RS_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["equipment_relative_strength_attention", "customer_or_process_qualification_visibility", "order_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_order_or_customer_allocation_required", "delivery_schedule_and_utilization_required", "ASP_mix_gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["equipment_relative_strength_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_to_delivery_gap", "customer_allocation_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "348210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv", "trigger_date": "2024-04-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -43.12, "MAE_30D_pct": -38.72, "MAE_90D_pct": -43.12, "MFE_180D_pct": 1.69, "MFE_30D_pct": 1.69, "MFE_90D_pct": 1.69, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_322310_AUROS_20240704_OVERLAY_METROLOGY_ORDER_PREMIUM_4B", "case_role": "overlay_metrology_equipment_order_price_premium_counterexample", "company_name": "오로스테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Overlay/metrology equipment price premium should route to local 4B or counterexample unless customer allocation, signed order, delivery schedule, utilization, ASP/mix and margin/revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.07, "entry_date": "2024-07-04", "entry_price": 26600, "evidence_family": "overlay_metrology_equipment_order_premium_without_customer_allocation_utilization_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_EQUIPMENT_CUSTOMER_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 15130, "peak_date": "2024-07-04", "peak_price": 27050, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/322/322310.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C07_322310_AUROS_20240704_OVERLAY_METROLOGY_ORDER_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["equipment_relative_strength_attention", "customer_or_process_qualification_visibility", "order_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_order_or_customer_allocation_required", "delivery_schedule_and_utilization_required", "ASP_mix_gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["equipment_relative_strength_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_to_delivery_gap", "customer_allocation_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "322310", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv", "trigger_date": "2024-07-04", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_EQUIPMENT_CUSTOMER_ORDER_RELATIVE_STRENGTH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_equipment_order_relative_strength_new_symbols_customer_order_margin_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 equipment relative-strength rows should allow Stage2 when equipment RS is backed by customer/process qualification, signed order visibility, delivery schedule and margin/revision route, but Stage3 Green requires incremental order, customer allocation, utilization, ASP/mix, gross margin and revision bridge; equipment RS price premium without order-to-delivery proof should route to Yellow/local 4B or counterexample.",
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
3. Add C07-specific HBM/advanced equipment relative-strength / customer-order / delivery-margin guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_CUSTOMER_QUALIFICATION_ORDER_DELIVERY_MARGIN_BRIDGE
- C07_GREEN_REQUIRES_SIGNED_ORDER_CUSTOMER_ALLOCATION_UTILIZATION_ASP_MIX_REVISION
- C07_EQUIPMENT_RS_PRICE_PREMIUM_LOCAL_4B
- C07_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_ORDER_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

