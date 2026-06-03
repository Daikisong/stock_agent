# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating / delivery-margin guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_equipment_orderbook_delivery_margin_2023_2024_research.md
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

This run avoids those top-covered C11 symbols and adds 222080, 299030, and 382840.  
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
222080 씨아이에스: 2023 forward window clean; corporate-action candidate is 2017-01-20, outside the selected test window.
299030 하나기술: 2023/2024 forward window clean; corporate-action candidates are 2021-03-22 and 2021-04-13, outside the selected test window.
382840 원준: 2023/2024 forward window clean; corporate-action candidates are 2022-07-12 and 2022-07-29, outside the selected test window.
```

## 3. Research thesis

C11 should not treat orderbook as already-earned EPS. It should test whether the backlog converts into delivery, revenue, margin and revision:

```text
battery orderbook / backlog / equipment contract attention
→ fresh backlog quality
→ delivery schedule and customer order quality
→ revenue conversion
→ margin and revision bridge
→ rerating
```

Orderbook is a warehouse door, not the shipment itself. Stage2 can follow the door opening early, but Green should require trucks leaving the yard at a margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C11_222080_CIS_20230228_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2 | 222080 | positive_equipment_orderbook_stage2_success_with_later_4b | 2023-02-28 | 10290 | 16440 on 2023-03-30 | 8970 on 2023-10-31 | 59.77% | 59.77% | 59.77% | -12.83% | -45.44% |
| C11_299030_HANATECH_20230724_BATTERY_EQUIPMENT_ORDERBOOK_PREMIUM_4B | 299030 | late_orderbook_rerating_price_premium_counterexample | 2023-07-24 | 137900 | 147000 on 2023-07-24 | 49000 on 2024-01-26 | 6.6% | 6.6% | 6.6% | -64.47% | -66.67% |
| C11_382840_WONJOON_20230726_BATTERY_FURNACE_ORDERBOOK_4B | 382840 | furnace_orderbook_delivery_margin_counterexample | 2023-07-26 | 25800 | 30300 on 2023-07-26 | 15920 on 2024-04-12 | 17.44% | 17.44% | 17.44% | -38.29% | -47.46% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery equipment orderbook, backlog visibility, and delivery schedule attention can be valid Stage2 routes.
- 222080 is the positive anchor: early 2023 equipment orderbook momentum produced a large forward MFE before the evidence aged into a late-cycle risk-control problem.

### Stage3 / Green
- C11 Green should require fresh backlog quality, delivery schedule, customer order quality, revenue conversion, margin and revision confirmation.
- A backlog headline without delivery quality is not enough. The model should demand evidence that backlog is moving through the income statement.

### 4B
- 299030 and 382840 fill the missing local 4B pocket. Both battery equipment/furnace rows had already priced orderbook optionality by the July 2023 spike, then rolled over as delivery, margin and revision evidence failed to carry the premium.
- 222080 also required later 4B discipline after the March 2023 Stage2 success matured into a price-premium state.

### 4C
- No hard accounting or order-cancellation break is asserted.
- The C11 break mode is orderbook-to-delivery failure: orders remain plausible, but delivery schedule, customer quality, margin and revisions stop widening enough to support valuation.

## 6. Raw component score breakdown

```json
{
  "C11_222080_CIS_20230228_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C11_299030_HANATECH_20230724_BATTERY_EQUIPMENT_ORDERBOOK_PREMIUM_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C11_382840_WONJOON_20230726_BATTERY_FURNACE_ORDERBOOK_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_orderbook_attention and early_delivery_revenue_visibility:
    allow_stage2_actionable = true

if battery_orderbook_price_premium and no incremental_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and orderbook_to_delivery_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 299030 / 2023-07-24: late battery equipment orderbook premium can be over-promoted if the model treats price confirmation as fresh backlog/delivery evidence.
- 382840 / 2023-07-26: furnace equipment orderbook premium can become price-only when delivery, margin and revision proof do not arrive.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.83, "MAE_30D_pct": -3.4, "MAE_90D_pct": -3.4, "MFE_180D_pct": 59.77, "MFE_30D_pct": 59.77, "MFE_90D_pct": 59.77, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_222080_CIS_20230228_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2", "case_role": "positive_equipment_orderbook_stage2_success_with_later_4b", "company_name": "씨아이에스", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old/outside selected test window where present", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when battery equipment orderbook and delivery visibility created a rerating route, but Green still requires backlog quality, delivery schedule, revenue conversion, margin and revision bridge; after the March 2023 run, the same evidence needed 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.44, "entry_date": "2023-02-28", "entry_price": 10290, "evidence_family": "battery_equipment_orderbook_delivery_backlog_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 8970, "peak_date": "2023-03-30", "peak_price": 16440, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/222/222080.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C11_222080_CIS_20230228_BATTERY_EQUIPMENT_ORDERBOOK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_equipment_or_material_orderbook_attention", "backlog_or_contract_visibility_claim", "delivery_schedule_or_revenue_conversion_signal"], "stage3_evidence_fields": ["fresh_backlog_quality_required", "delivery_schedule_and_customer_order_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "margin_or_revenue_conversion_failure", "revision_bridge_failure"], "symbol": "222080", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222080/2023.csv", "trigger_date": "2023-02-28", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -64.47, "MAE_30D_pct": -27.56, "MAE_90D_pct": -53.59, "MFE_180D_pct": 6.6, "MFE_30D_pct": 6.6, "MFE_90D_pct": 6.6, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_299030_HANATECH_20230724_BATTERY_EQUIPMENT_ORDERBOOK_PREMIUM_4B", "case_role": "late_orderbook_rerating_price_premium_counterexample", "company_name": "하나기술", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old/outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Late equipment orderbook premium should route to local 4B or counterexample unless incremental backlog, delivery cadence, margin capture and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.67, "entry_date": "2023-07-24", "entry_price": 137900, "evidence_family": "battery_equipment_orderbook_price_premium_without_incremental_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-01-26", "low_price_180d": 49000, "peak_date": "2023-07-24", "peak_price": 147000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/299/299030.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C11_299030_HANATECH_20230724_BATTERY_EQUIPMENT_ORDERBOOK_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_equipment_or_material_orderbook_attention", "backlog_or_contract_visibility_claim", "delivery_schedule_or_revenue_conversion_signal"], "stage3_evidence_fields": ["fresh_backlog_quality_required", "delivery_schedule_and_customer_order_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "margin_or_revenue_conversion_failure", "revision_bridge_failure"], "symbol": "299030", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/299/299030/2023.csv", "trigger_date": "2023-07-24", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.29, "MAE_30D_pct": -18.02, "MAE_90D_pct": -36.98, "MFE_180D_pct": 17.44, "MFE_30D_pct": 17.44, "MFE_90D_pct": 17.44, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_382840_WONJOON_20230726_BATTERY_FURNACE_ORDERBOOK_4B", "case_role": "furnace_orderbook_delivery_margin_counterexample", "company_name": "원준", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old/outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Battery furnace/equipment orderbook premium should be capped at local 4B when delivery schedule, customer order quality, margin and revision bridge do not support the valuation already paid.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.46, "entry_date": "2023-07-26", "entry_price": 25800, "evidence_family": "battery_furnace_equipment_orderbook_premium_without_delivery_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-12", "low_price_180d": 15920, "peak_date": "2023-07-26", "peak_price": 30300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/382/382840.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C11_382840_WONJOON_20230726_BATTERY_FURNACE_ORDERBOOK_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_equipment_or_material_orderbook_attention", "backlog_or_contract_visibility_claim", "delivery_schedule_or_revenue_conversion_signal"], "stage3_evidence_fields": ["fresh_backlog_quality_required", "delivery_schedule_and_customer_order_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "margin_or_revenue_conversion_failure", "revision_bridge_failure"], "symbol": "382840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382840/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
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
  "loop_contribution_label": "battery_orderbook_rerating_equipment_delivery_margin_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery orderbook rerating rows should allow Stage2 when early orderbook/backlog visibility is tied to delivery and revenue conversion, but Stage3 Green requires fresh backlog quality, delivery schedule, customer order quality, margin and revision bridge; late equipment orderbook price premium should route to local 4B or counterexample.",
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
3. Add C11-specific battery orderbook / delivery / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_STAGE2_ALLOWED_ON_EARLY_ORDERBOOK_DELIVERY_VISIBILITY
- C11_GREEN_REQUIRES_FRESH_BACKLOG_DELIVERY_CUSTOMER_QUALITY_MARGIN_REVISION
- C11_ORDERBOOK_PRICE_PREMIUM_LOCAL_4B
- C11_ORDERBOOK_WITHOUT_DELIVERY_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

