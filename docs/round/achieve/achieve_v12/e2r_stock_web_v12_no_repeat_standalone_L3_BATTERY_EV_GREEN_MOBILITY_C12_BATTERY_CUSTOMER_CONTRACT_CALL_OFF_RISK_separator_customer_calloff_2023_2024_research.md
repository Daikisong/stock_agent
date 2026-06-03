# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer-contract call-off risk guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_SEPARATOR_STEEL_CUSTOMER_CONTRACT_CALLOFF_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_separator_customer_calloff_2023_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK current coverage:
rows=15, symbols=9, date range=2023-01-31~2024-07-25, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: UNKNOWN_SYMBOL(4), 247540(2), 278280(2), 003670(1), 005070(1)
```

This run avoids those top-covered C12 symbols and adds 002710, 361610, and 393890.  
Each row uses a new `C12 + symbol + trigger_type + entry_date` hard key.

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

C12 should not treat a customer contract or battery orderbook as revenue already earned. It should test whether the contract survives call-off and utilization reality:

```text
battery customer contract / orderbook attention
→ signed duration and customer quality
→ call-off stability
→ capacity ramp and utilization
→ ASP/mix, input-cost pass-through and gross margin
→ revision bridge
→ rerating or break
```

A battery contract is a reservation, not a completed shipment. Stage2 can follow a credible reservation. Green should require the customer to keep taking delivery and the factory to run at margins that actually revise earnings.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_002710_TCCSTEEL_20230405_BATTERY_CAN_CUSTOMER_CONTRACT_STAGE2 | 002710 | positive_battery_can_customer_contract_stage2_success_with_later_4b_refresh | 2023-04-05 | 27800 | 73600 on 2023-10-13 | 23350 on 2023-04-05 | 76.26% | 106.83% | 164.75% | -16.01% | -34.24% |
| C12_361610_SKIET_20240517_SEPARATOR_CALLOFF_MARGIN_BREAK_4C | 361610 | separator_customer_calloff_margin_break_counterexample | 2024-05-17 | 54500 | 57500 on 2024-05-17 | 22250 on 2024-12-27 | 5.5% | 5.5% | 5.5% | -59.17% | -61.3% |
| C12_393890_WCP_20240222_SEPARATOR_CONTRACT_PREMIUM_FALSE_GREEN | 393890 | separator_contract_premium_false_green_counterexample | 2024-02-22 | 47100 | 49500 on 2024-03-07 | 10870 on 2024-12-30 | 5.1% | 5.1% | 5.1% | -76.92% | -78.04% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery customer-contract evidence can be a valid Stage2 route only when signed duration, customer quality, capacity expansion and gross-margin visibility exist before the valuation fully capitalizes the backlog.
- 002710 is the positive anchor. Battery-can steel customer/orderbook evidence produced very large MFE after the April 2023 trigger. It later required 4B refresh discipline once the contract/capacity story was fully priced.

### Stage3 / Green
- C12 Green should require call-off stability, customer concentration quality, order duration, capacity ramp, utilization, ASP/mix, input-cost pass-through, gross margin and revision confirmation.
- 393890 is the false-Green guard: separator contract/orderbook price confirmation was not enough when customer call-off, utilization and margin evidence failed to keep improving.

### 4B
- 393890 also functions as a local 4B watch: the March price peak was close to the selected trigger window, and the subsequent drawdown confirms that price premium needed non-price evidence.
- 002710 shows that a valid Stage2 customer-contract rerating can later migrate into 4B when the market pays upfront for several contract years.

### 4C
- 361610 fills the 4C/call-off break gap. The separator thesis did not need a hard cancellation to fail; weak utilization, capex absorption, call-off uncertainty and margin/revision failure were enough to turn the orderbook story into a break.
- The C12 break mode is orderbook-to-utilization failure: contracts remain narratively plausible, but call-off, utilization, ASP/mix, capex absorption, gross margin and revisions no longer support the price.

## 6. Raw component score breakdown

```json
{
  "C12_002710_TCCSTEEL_20230405_BATTERY_CAN_CUSTOMER_CONTRACT_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 54,
    "valuation_rerating_runway": 9,
    "visibility_quality": 10
  },
  "C12_361610_SKIET_20240517_SEPARATOR_CALLOFF_MARGIN_BREAK_4C": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 20,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C12_393890_WCP_20240222_SEPARATOR_CONTRACT_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_contract_attention and signed_duration_customer_quality_capacity_margin_bridge_visible:
    allow_stage2_actionable = true

if separator_or_battery_contract_price_premium and no calloff_utilization_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if calloff_or_utilization_margin_break:
    route_to_4C_counterexample = true
```

Residual errors:
```text
current_profile_error_count = 2
- 361610 / 2024-05-17: separator customer-contract attention can be over-promoted if the model ignores call-off, utilization and capex absorption failure.
- 393890 / 2024-02-22: separator contract premium can look like Green, but the forward path argues for Yellow/local 4B unless utilization, ASP/mix and margin revisions close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -16.01, "MAE_30D_pct": -16.01, "MAE_90D_pct": -16.01, "MFE_180D_pct": 164.75, "MFE_30D_pct": 76.26, "MFE_90D_pct": 106.83, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_002710_TCCSTEEL_20230405_BATTERY_CAN_CUSTOMER_CONTRACT_STAGE2", "case_role": "positive_battery_can_customer_contract_stage2_success_with_later_4b_refresh", "company_name": "TCC스틸", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2009-05-08 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when battery-can steel customer-contract/orderbook attention attached to capacity expansion and an input-cost/margin bridge before the full rerating. Green still requires signed duration, customer concentration quality, call-off stability, input-cost pass-through, capacity execution, working-capital and revision confirmation; after the October 2023 premium, the same evidence required local 4B refresh discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.24, "entry_date": "2023-04-05", "entry_day_high": 28700, "entry_day_low": 23350, "entry_price": 27800, "evidence_family": "battery_can_steel_customer_contract_capacity_expansion_orderbook_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CUSTOMER_CONTRACT_CALLOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-04-05", "low_price_180d": 23350, "peak_date": "2023-10-13", "peak_price": 73600, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/002/002710.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 54, "valuation_rerating_runway": 9, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C12_002710_TCCSTEEL_20230405_BATTERY_CAN_CUSTOMER_CONTRACT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_line_basis": ["atlas/symbol_profiles/002/002710.json lines 4-16, 135-137, 214-224", "atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv around 2023-04-05 and 2023-10-13"], "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_or_orderbook_attention", "signed_duration_customer_quality_or_capacity_expansion_signal", "utilization_margin_or_revision_route"], "stage3_evidence_fields": ["calloff_stability_required", "customer_concentration_and_order_duration_required", "capacity_ramp_utilization_ASP_mix_margin_revision_required"], "stage4b_evidence_fields": ["battery_contract_or_separator_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_break", "utilization_or_capex_absorption_failure", "gross_margin_revision_bridge_failure"], "symbol": "002710", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv", "trigger_date": "2023-04-05", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -59.17, "MAE_30D_pct": -21.1, "MAE_90D_pct": -39.08, "MFE_180D_pct": 5.5, "MFE_30D_pct": 5.5, "MFE_90D_pct": 5.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_361610_SKIET_20240517_SEPARATOR_CALLOFF_MARGIN_BREAK_4C", "case_role": "separator_customer_calloff_margin_break_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Separator customer-contract attention should route to 4C/counterexample when call-off risk, utilization, capex absorption, ASP/mix and margin revisions break after the contract/orderbook premium. Price stabilization did not repair the non-price evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.3, "entry_date": "2024-05-17", "entry_day_high": 57500, "entry_day_low": 54000, "entry_price": 54500, "evidence_family": "separator_customer_contract_calloff_utilization_margin_break_without_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CUSTOMER_CONTRACT_CALLOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-12-27", "low_price_180d": 22250, "peak_date": "2024-05-17", "peak_price": 57500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 3, "market_mispricing": 4, "total": 20, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C12_361610_SKIET_20240517_SEPARATOR_CALLOFF_MARGIN_BREAK_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_line_basis": ["atlas/symbol_profiles/361/361610.json lines 4-10, 45-50, 75-93", "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv around 2024-05-17 and 2024-12-27"], "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_or_orderbook_attention", "signed_duration_customer_quality_or_capacity_expansion_signal", "utilization_margin_or_revision_route"], "stage3_evidence_fields": ["calloff_stability_required", "customer_concentration_and_order_duration_required", "capacity_ramp_utilization_ASP_mix_margin_revision_required"], "stage4b_evidence_fields": ["battery_contract_or_separator_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_break", "utilization_or_capex_absorption_failure", "gross_margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "trigger_date": "2024-05-17", "trigger_type": "4C-calloff-margin-break", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -76.92, "MAE_30D_pct": -21.66, "MAE_90D_pct": -42.68, "MFE_180D_pct": 5.1, "MFE_30D_pct": 5.1, "MFE_90D_pct": 5.1, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20240222_SEPARATOR_CONTRACT_PREMIUM_FALSE_GREEN", "case_role": "separator_contract_premium_false_green_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Separator contract/orderbook premium should stay Yellow or local 4B when the stock has only price confirmation and lacks call-off stability, utilization, customer mix, ASP/mix, capex absorption, gross margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -78.04, "entry_date": "2024-02-22", "entry_day_high": 49400, "entry_day_low": 44250, "entry_price": 47100, "evidence_family": "separator_contract_orderbook_premium_without_calloff_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CUSTOMER_CONTRACT_CALLOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-12-30", "low_price_180d": 10870, "peak_date": "2024-03-07", "peak_price": 49500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20240222_SEPARATOR_CONTRACT_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_line_basis": ["atlas/symbol_profiles/393/393890.json lines 4-10, 49-53, 76-94", "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv around 2024-02-22, 2024-03-07 and 2024-12-30"], "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_or_orderbook_attention", "signed_duration_customer_quality_or_capacity_expansion_signal", "utilization_margin_or_revision_route"], "stage3_evidence_fields": ["calloff_stability_required", "customer_concentration_and_order_duration_required", "capacity_ramp_utilization_ASP_mix_margin_revision_required"], "stage4b_evidence_fields": ["battery_contract_or_separator_orderbook_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_break", "utilization_or_capex_absorption_failure", "gross_margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "trigger_date": "2024-02-22", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "BATTERY_SEPARATOR_STEEL_CUSTOMER_CONTRACT_CALLOFF_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_customer_contract_calloff_separator_steel_new_symbols_4b_4c_gap",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery customer-contract/call-off rows should allow Stage2 only when signed duration, customer quality, capacity execution and margin/revision evidence are visible; separator or battery-contract price premium without call-off stability, utilization and margin proof should route to Yellow/local 4B or 4C counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C12 + symbol + trigger_type + entry_date.
3. Add C12-specific customer-contract / call-off / utilization / margin-revision / 4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_STAGE2_ALLOWED_ON_SIGNED_DURATION_CUSTOMER_QUALITY_CAPACITY_MARGIN_BRIDGE
- C12_GREEN_REQUIRES_CALLOFF_STABILITY_UTILIZATION_ASP_MIX_INPUT_COST_REVISION
- C12_BATTERY_CONTRACT_PRICE_PREMIUM_LOCAL_4B
- C12_CALLOFF_UTILIZATION_MARGIN_BREAK_4C_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

