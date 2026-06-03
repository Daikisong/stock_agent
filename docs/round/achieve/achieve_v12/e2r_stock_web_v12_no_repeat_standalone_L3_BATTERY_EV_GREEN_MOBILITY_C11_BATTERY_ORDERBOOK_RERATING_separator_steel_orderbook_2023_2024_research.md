# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating / separator call-off guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_SEPARATOR_STEEL_CAN_ORDERBOOK_CALL_OFF_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_separator_steel_orderbook_2023_2024_research.md
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

This run avoids those top-covered C11 symbols and adds 002710, 361610, and 393890.  
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
002710 TCC스틸: 2023 forward window clean; corporate-action candidate is 2009-05-08 and outside selected test window.
361610 SK아이이테크놀로지: corporate_action_candidate_count=0.
393890 더블유씨피: corporate_action_candidate_count=0.
```

## 3. Research thesis

C11 should not treat every battery orderbook headline as bankable EPS. It should test whether the orderbook becomes durable utilization and margin:

```text
battery orderbook / supply contract attention
→ signed order duration and customer quality
→ capacity ramp and call-off stability
→ utilization, ASP/mix and input-cost pass-through
→ gross margin and revision bridge
→ rerating
```

An orderbook is a reservation list. Stage2 can follow the first credible reservation, but Green should require the customer to keep the table, the factory to seat them, and the bill to flow through margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C11_002710_TCCSTEEL_20230323_BATTERY_CAN_STEEL_ORDERBOOK_STAGE2 | 002710 | positive_battery_can_steel_orderbook_stage2_success_with_later_4b_refresh | 2023-03-23 | 22750 | 73600 on 2023-10-13 | 19760 on 2023-03-23 | 115.38% | 152.75% | 223.52% | -13.14% | -34.24% |
| C11_361610_SKIET_20240405_SEPARATOR_ORDERBOOK_FALSE_GREEN | 361610 | separator_orderbook_calloff_false_green_counterexample | 2024-04-05 | 66100 | 68700 on 2024-04-09 | 22250 on 2024-12-27 | 3.93% | 3.93% | 3.93% | -66.34% | -67.61% |
| C11_393890_WCP_20240307_SEPARATOR_ORDERBOOK_PRICE_PREMIUM_4B | 393890 | separator_orderbook_price_premium_counterexample | 2024-03-07 | 49500 | 49500 on 2024-03-07 | 10870 on 2024-12-30 | 0.0% | 0.0% | 0.0% | -78.04% | -78.04% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery orderbook rerating can be a valid Stage2 route when signed order duration, customer quality, capacity expansion and margin visibility appear before valuation fully capitalizes the backlog.
- 002710 is the positive anchor. Battery-can steel supply/demand and capacity-expansion visibility produced a large MFE after the March 2023 trigger. It later required 4B discipline after the October 2023 premium because order duration, input-cost pass-through and revision evidence needed to refresh.

### Stage3 / Green
- C11 Green should require signed duration, customer quality, call-off stability, capacity ramp, utilization, ASP/mix, input-cost pass-through, gross margin and revision confirmation.
- 361610 shows why separator orderbook recovery should stay Yellow when call-off/utilization and margin evidence do not close after price confirmation.
- 393890 shows the same separator orderbook failure in a cleaner local 4B form: the price had already peaked when the thesis still needed non-price confirmation.

### 4B
- This MD fills a C11 4B coverage gap. 393890 is a pure local 4B row; 361610 is a false-Green / Yellow-to-4B counterexample; 002710 is a Stage2 success that later matured into a 4B refresh requirement.
- The common guard is simple: after the orderbook premium is paid, price strength cannot substitute for customer call-off stability, utilization and margin revisions.

### 4C
- No hard customer cancellation or factory impairment is asserted.
- The C11 break mode is orderbook-to-utilization failure: the backlog story remains plausible, but call-off, customer mix, capacity ramp, input cost, utilization, gross margin and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C11_002710_TCCSTEEL_20230323_BATTERY_CAN_STEEL_ORDERBOOK_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 54,
    "valuation_rerating_runway": 9,
    "visibility_quality": 10
  },
  "C11_361610_SKIET_20240405_SEPARATOR_ORDERBOOK_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C11_393890_WCP_20240307_SEPARATOR_ORDERBOOK_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 24,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_orderbook_attention and signed_duration_customer_quality_capacity_margin_bridge_visible:
    allow_stage2_actionable = true

if battery_orderbook_price_premium and no calloff_utilization_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and orderbook_to_utilization_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 361610 / 2024-04-05: separator orderbook recovery can be over-promoted if the model treats price confirmation as call-off stability, utilization and margin proof.
- 393890 / 2024-03-07: separator orderbook premium can become price-only when customer call-off, utilization, ASP/mix and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.14, "MAE_30D_pct": -13.14, "MAE_90D_pct": -13.14, "MFE_180D_pct": 223.52, "MFE_30D_pct": 115.38, "MFE_90D_pct": 152.75, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_002710_TCCSTEEL_20230323_BATTERY_CAN_STEEL_ORDERBOOK_STAGE2", "case_role": "positive_battery_can_steel_orderbook_stage2_success_with_later_4b_refresh", "company_name": "TCC스틸", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2009-05-08 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when battery-can steel/orderbook attention attached to visible customer demand, capacity expansion and margin leverage before the full rerating. Green still requires signed order duration, customer concentration quality, input-cost pass-through, capacity execution, working-capital and revision bridge; after the October 2023 premium, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.24, "entry_date": "2023-03-23", "entry_price": 22750, "evidence_family": "battery_can_steel_supply_contract_orderbook_capacity_expansion_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CAN_ORDERBOOK_CALL_OFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-03-23", "low_price_180d": 19760, "peak_date": "2023-10-13", "peak_price": 73600, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/002/002710.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 54, "valuation_rerating_runway": 9, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C11_002710_TCCSTEEL_20230323_BATTERY_CAN_STEEL_ORDERBOOK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_or_supply_contract_attention", "customer_quality_or_capacity_expansion_visibility", "utilization_margin_or_revision_route"], "stage3_evidence_fields": ["signed_order_duration_and_customer_quality_required", "calloff_risk_and_utilization_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_orderbook_conversion_gap", "utilization_capex_or_input_cost_disappointment", "margin_revision_bridge_failure"], "symbol": "002710", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv", "trigger_date": "2023-03-23", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -66.34, "MAE_30D_pct": -18.31, "MAE_90D_pct": -38.43, "MFE_180D_pct": 3.93, "MFE_30D_pct": 3.93, "MFE_90D_pct": 3.93, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_361610_SKIET_20240405_SEPARATOR_ORDERBOOK_FALSE_GREEN", "case_role": "separator_orderbook_calloff_false_green_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Separator orderbook recovery should stay Yellow when customer call-off risk, utilization, pricing/mix, capex burden and margin/revision evidence do not keep improving after price confirmation. The April 2024 route had only small MFE and very large forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.61, "entry_date": "2024-04-05", "entry_price": 66100, "evidence_family": "separator_orderbook_customer_calloff_risk_without_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CAN_ORDERBOOK_CALL_OFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-12-27", "low_price_180d": 22250, "peak_date": "2024-04-09", "peak_price": 68700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C11_361610_SKIET_20240405_SEPARATOR_ORDERBOOK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_or_supply_contract_attention", "customer_quality_or_capacity_expansion_visibility", "utilization_margin_or_revision_route"], "stage3_evidence_fields": ["signed_order_duration_and_customer_quality_required", "calloff_risk_and_utilization_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_orderbook_conversion_gap", "utilization_capex_or_input_cost_disappointment", "margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "trigger_date": "2024-04-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -78.04, "MAE_30D_pct": -39.6, "MAE_90D_pct": -47.47, "MFE_180D_pct": 0.0, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_393890_WCP_20240307_SEPARATOR_ORDERBOOK_PRICE_PREMIUM_4B", "case_role": "separator_orderbook_price_premium_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Separator orderbook price premium should route to local 4B or counterexample unless firm customer call-offs, utilization, ASP/mix, capex absorption, gross margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -78.04, "entry_date": "2024-03-07", "entry_price": 49500, "evidence_family": "separator_orderbook_price_premium_without_customer_calloff_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CAN_ORDERBOOK_CALL_OFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-12-30", "low_price_180d": 10870, "peak_date": "2024-03-07", "peak_price": 49500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 24, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C11_393890_WCP_20240307_SEPARATOR_ORDERBOOK_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_or_supply_contract_attention", "customer_quality_or_capacity_expansion_visibility", "utilization_margin_or_revision_route"], "stage3_evidence_fields": ["signed_order_duration_and_customer_quality_required", "calloff_risk_and_utilization_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_orderbook_conversion_gap", "utilization_capex_or_input_cost_disappointment", "margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "trigger_date": "2024-03-07", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CAN_ORDERBOOK_CALL_OFF_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_orderbook_rerating_separator_steel_can_new_symbols_and_4b_gap",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery orderbook-rerating rows should allow Stage2 when signed order duration, customer quality, capacity execution and margin/revision evidence appear before valuation fully capitalizes the orderbook; separator or battery-can price premium without call-off, utilization and margin proof should route to Yellow/local 4B or counterexample.",
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
3. Add C11-specific battery orderbook / call-off / utilization / margin-revision / 4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_STAGE2_ALLOWED_ON_SIGNED_DURATION_CUSTOMER_QUALITY_CAPACITY_MARGIN_BRIDGE
- C11_GREEN_REQUIRES_CALLOFF_STABILITY_UTILIZATION_ASP_MIX_INPUT_COST_REVISION
- C11_BATTERY_ORDERBOOK_PRICE_PREMIUM_LOCAL_4B
- C11_SEPARATOR_ORDERBOOK_WITHOUT_UTILIZATION_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

