# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating / equipment delivery-margin guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_battery_equipment_orderbook_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C11_BATTERY_ORDERBOOK_RERATING current coverage:
rows=14, symbols=6, date range=2023-01-31~2024-06-24, good/bad S2=6/2, 4B/4C=0/1
top covered symbols: 247540(6), 003670(3), 348370(2), 066970(1), 373220(1)
```

This run avoids those top-covered C11 symbols and adds 137400, 222080, and 382840.  
Each row uses a new `C11 + symbol + trigger_type + entry_date` hard key.

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
137400 피엔티: 2023 forward window clean; corporate-action candidates are old, outside the test window.
222080 씨아이에스: 2023 forward window clean; corporate-action candidate is 2017-01-20.
382840 원준: 2023 forward window clean; corporate-action candidates are in 2022, outside the test window.
```

## 3. Research thesis

C11 should not treat “orderbook” as a magic word. It should test whether a backlog becomes deliverable EPS:

```text
battery orderbook / equipment backlog attention
→ backlog quality and customer capex visibility
→ delivery schedule and revenue conversion
→ margin bridge
→ revision confirmation
→ rerating
```

The key distinction is backlog as a loaded conveyor belt versus backlog as a warehouse label. The first can become earnings. The second can sit in the corner while valuation has already moved.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C11_137400_PNT_20230403_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2_SUCCESS | 137400 | positive_orderbook_stage2_success_with_later_4b | 2023-04-03 | 51900 | 86100 on 2023-07-26 | 47950 on 2023-11-01 | 32.37% | 65.9% | 65.9% | -7.61% | -44.31% |
| C11_222080_CIS_20230329_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN | 222080 | orderbook_visibility_false_green_counterexample | 2023-03-29 | 13920 | 16440 on 2023-03-30 | 8970 on 2023-10-31 | 18.1% | 18.1% | 18.1% | -35.56% | -45.44% |
| C11_382840_WONJUN_20230323_CATHODE_EQUIPMENT_ORDERBOOK_BLOWOFF | 382840 | battery_equipment_blowoff_counterexample | 2023-03-23 | 27950 | 33250 on 2023-04-10 | 15060 on 2023-10-31 | 18.96% | 18.96% | 18.96% | -46.12% | -54.71% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery-equipment orderbook and customer capex attention are valid routing signals.
- 137400 is the positive anchor: orderbook/delivery visibility produced a low-MAE Stage2 route and a large forward MFE before the later drawdown.

### Stage3 / Green
- C11 Green should require backlog quality, delivery schedule, revenue conversion, margin and revision evidence.
- 222080 and 382840 show why orderbook or equipment-capex language should not be promoted if the non-price bridge is weak.

### 4B
- 382840 is the local 4B guard: the price premium arrived quickly, but the equipment orderbook story did not keep enough evidence-weighted runway.
- 137400 also required later 4B discipline after the orderbook rerating matured.

### 4C
- No hard accounting break is asserted.
- The C11 break mode is backlog-quality failure: the orderbook headline remains plausible, but delivery, margin and revision do not carry the stock already priced in.

## 6. Raw component score breakdown

```json
{
  "C11_137400_PNT_20230403_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 59,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  },
  "C11_222080_CIS_20230329_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C11_382840_WONJUN_20230323_CATHODE_EQUIPMENT_ORDERBOOK_BLOWOFF": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_orderbook_attention and no delivery_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if equipment_orderbook_price_premium and no incremental_backlog_quality_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and delivery_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 222080 / 2023-03-29: equipment orderbook price spike could be over-promoted if the model does not require delivery and margin evidence.
- 382840 / 2023-03-23: cathode-equipment orderbook premium became a local blowoff; fresh Green should be blocked without revision duration.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -7.61, "MAE_30D_pct": -6.36, "MAE_90D_pct": -6.36, "MFE_180D_pct": 65.9, "MFE_30D_pct": 32.37, "MFE_90D_pct": 65.9, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_137400_PNT_20230403_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2_SUCCESS", "case_role": "positive_orderbook_stage2_success_with_later_4b", "company_name": "피엔티", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when battery-equipment orderbook and delivery visibility were plausible; Green still requires backlog quality, delivery schedule, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.31, "entry_date": "2023-04-03", "entry_price": 51900, "evidence_family": "battery_electrode_equipment_orderbook_delivery_margin_rerating", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-01", "low_price_180d": 47950, "peak_date": "2023-07-26", "peak_price": 86100, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/137/137400.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 59, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C11_137400_PNT_20230403_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_equipment_or_material_orderbook_attention", "backlog_or_capacity_visibility_claim", "delivery_schedule_or_customer_capex_signal"], "stage3_evidence_fields": ["backlog_quality_confirmation_required", "delivery_schedule_and_revenue_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["delivery_delay_or_backlog_quality_gap", "margin_or_revision_duration_failure", "orderbook_story_mean_reversion"], "symbol": "137400", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/137/137400/2023.csv", "trigger_date": "2023-04-03", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.56, "MAE_30D_pct": -13.43, "MAE_90D_pct": -24.07, "MFE_180D_pct": 18.1, "MFE_30D_pct": 18.1, "MFE_90D_pct": 18.1, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_222080_CIS_20230329_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN", "case_role": "orderbook_visibility_false_green_counterexample", "company_name": "씨아이에스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Battery-equipment orderbook language should stay Yellow if delivery, backlog quality, margin and revision durability are not visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.44, "entry_date": "2023-03-29", "entry_price": 13920, "evidence_family": "battery_equipment_orderbook_price_spike_without_margin_delivery_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 8970, "peak_date": "2023-03-30", "peak_price": 16440, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/222/222080.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C11_222080_CIS_20230329_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_equipment_or_material_orderbook_attention", "backlog_or_capacity_visibility_claim", "delivery_schedule_or_customer_capex_signal"], "stage3_evidence_fields": ["backlog_quality_confirmation_required", "delivery_schedule_and_revenue_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["delivery_delay_or_backlog_quality_gap", "margin_or_revision_duration_failure", "orderbook_story_mean_reversion"], "symbol": "222080", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222080/2023.csv", "trigger_date": "2023-03-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -46.12, "MAE_30D_pct": -15.56, "MAE_90D_pct": -26.65, "MFE_180D_pct": 18.96, "MFE_30D_pct": 18.96, "MFE_90D_pct": 18.96, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_382840_WONJUN_20230323_CATHODE_EQUIPMENT_ORDERBOOK_BLOWOFF", "case_role": "battery_equipment_blowoff_counterexample", "company_name": "원준", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "After the battery-equipment orderbook premium expanded, local 4B was more useful than fresh Green unless incremental delivery and revision evidence arrived.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.71, "entry_date": "2023-03-23", "entry_price": 27950, "evidence_family": "cathode_heat_treatment_equipment_orderbook_price_premium_without_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 15060, "peak_date": "2023-04-10", "peak_price": 33250, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/382/382840.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C11_382840_WONJUN_20230323_CATHODE_EQUIPMENT_ORDERBOOK_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_equipment_or_material_orderbook_attention", "backlog_or_capacity_visibility_claim", "delivery_schedule_or_customer_capex_signal"], "stage3_evidence_fields": ["backlog_quality_confirmation_required", "delivery_schedule_and_revenue_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["delivery_delay_or_backlog_quality_gap", "margin_or_revision_duration_failure", "orderbook_story_mean_reversion"], "symbol": "382840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382840/2023.csv", "trigger_date": "2023-03-23", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_orderbook_equipment_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery orderbook rows should allow Stage2 on early backlog/orderbook attention, but Stage3 Green requires backlog quality, delivery schedule, revenue conversion, margin and revision bridge; late equipment orderbook price premium should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C11 + symbol + trigger_type + entry_date.
3. Add C11-specific backlog-quality / delivery-schedule / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_GREEN_REQUIRES_BACKLOG_QUALITY_DELIVERY_MARGIN_REVISION
- C11_BATTERY_ORDERBOOK_STAGE2_ALLOWED
- C11_EQUIPMENT_ORDERBOOK_PRICE_PREMIUM_LOCAL_4B
- C11_BACKLOG_WITHOUT_DELIVERY_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

