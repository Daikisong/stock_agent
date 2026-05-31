# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer contract / call-off risk guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CUSTOMER_CONTRACT_CALLOFF_REVENUE_CONVERSION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_customer_contract_calloff_revenue_2023_2024_research.md
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

This run avoids those top-covered C12 symbols and adds 348370, 393890, and 361610.  
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
348370 엔켐: corporate_action_candidate_count=0.
393890 더블유씨피: corporate_action_candidate_count=0.
361610 SK아이이테크놀로지: corporate_action_candidate_count=0.
```

## 3. Research thesis

C12 should not treat a battery customer contract as immediate EPS. It should test whether the contract becomes call-off, shipment, utilization and margin:

```text
customer contract / supply agreement attention
→ customer call-off cadence
→ delivery schedule and utilization
→ revenue conversion
→ margin and revision bridge
→ rerating
```

The contract is a reservation, not a paid meal. Stage2 can follow the reservation early, but Green should require the customer to sit down, order repeatedly, and let the kitchen run at profitable utilization.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_348370_ENCHEM_20240115_CUSTOMER_CONTRACT_CALLOFF_STAGE2 | 348370 | positive_customer_contract_calloff_stage2_success_with_later_4b | 2024-01-15 | 107000 | 394500 on 2024-04-08 | 100200 on 2024-01-22 | 235.05% | 268.69% | 268.69% | -6.36% | -62.23% |
| C12_393890_WCP_20230726_SEPARATOR_CUSTOMER_CALLOFF_4B | 393890 | separator_customer_calloff_price_premium_counterexample | 2023-07-26 | 75700 | 87500 on 2023-07-26 | 34350 on 2024-04-08 | 15.59% | 15.59% | 15.59% | -54.62% | -60.74% |
| C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_PREMIUM_4B | 361610 | separator_calloff_utilization_counterexample | 2023-07-26 | 108600 | 120000 on 2023-07-26 | 58700 on 2023-10-31 | 10.5% | 10.5% | 10.5% | -45.95% | -51.08% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery customer contract, delivery schedule and call-off visibility can be valid Stage2 routes.
- 348370 is the positive anchor: early 2024 electrolyte/customer-contract attention produced a very large MFE with limited initial MAE before the later price premium demanded risk control.

### Stage3 / Green
- C12 Green should require contracted volume, customer call-off cadence, delivery schedule, utilization, revenue conversion, margin and revision confirmation.
- A contract headline without repeated call-off is not enough. The model should demand evidence that the customer is pulling volume through the factory.

### 4B
- 393890 and 361610 fill the missing C12 4B pocket. Both separator names had customer/capacity narratives that were already priced by the July 2023 event spike, then rolled over as call-off/utilization evidence failed to carry the premium.
- 348370 also required later 4B discipline after the early Stage2 win matured into a high valuation state.

### 4C
- No hard accounting or contract-cancellation break is asserted.
- The C12 break mode is call-off conversion failure: the contract or customer route may remain real, but delivery, utilization, margin and revision do not support the stock already priced in.

## 6. Raw component score breakdown

```json
{
  "C12_348370_ENCHEM_20240115_CUSTOMER_CONTRACT_CALLOFF_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 59,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  },
  "C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C12_393890_WCP_20230726_SEPARATOR_CUSTOMER_CALLOFF_4B": {
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

Suggested C12 guard:
```text
if battery_customer_contract_attention and early_calloff_delivery_visibility:
    allow_stage2_actionable = true

if customer_contract_price_premium and no incremental_calloff_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and calloff_or_revenue_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 393890 / 2023-07-26: separator customer-contract premium can be over-promoted if the model treats contract/capacity language as call-off proof.
- 361610 / 2023-07-26: separator call-off/utilization gap can become a large drawdown when price has already capitalized the customer story.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.36, "MAE_30D_pct": -6.36, "MAE_90D_pct": -6.36, "MFE_180D_pct": 268.69, "MFE_30D_pct": 235.05, "MFE_90D_pct": 268.69, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_348370_ENCHEM_20240115_CUSTOMER_CONTRACT_CALLOFF_STAGE2", "case_role": "positive_customer_contract_calloff_stage2_success_with_later_4b", "company_name": "엔켐", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none for selected symbols", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when electrolyte/customer contract and call-off visibility could plausibly convert into revenue and margin, but Green still requires contracted volume, customer call-off cadence, delivery schedule, utilization, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -62.23, "entry_date": "2024-01-15", "entry_price": 107000, "evidence_family": "electrolyte_customer_contract_calloff_revenue_conversion_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CUSTOMER_CONTRACT_CALLOFF_REVENUE_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-01-22", "low_price_180d": 100200, "peak_date": "2024-04-08", "peak_price": 394500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/348/348370.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 59, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C12_348370_ENCHEM_20240115_CUSTOMER_CONTRACT_CALLOFF_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_attention", "calloff_or_delivery_schedule_claim", "revenue_conversion_or_utilization_visibility_signal"], "stage3_evidence_fields": ["contracted_volume_and_customer_calloff_required", "delivery_schedule_and_utilization_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["customer_contract_calloff_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_delay_or_volume_gap", "utilization_or_revenue_conversion_failure", "margin_revision_bridge_failure"], "symbol": "348370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "trigger_date": "2024-01-15", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -17.57, "MAE_90D_pct": -33.29, "MFE_180D_pct": 15.59, "MFE_30D_pct": 15.59, "MFE_90D_pct": 15.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20230726_SEPARATOR_CUSTOMER_CALLOFF_4B", "case_role": "separator_customer_calloff_price_premium_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none for selected symbols", "current_profile_error": true, "current_profile_verdict": "Separator customer-contract premium should route to local 4B or counterexample unless customer call-off, utilization, delivery schedule, margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.74, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_customer_contract_price_premium_without_calloff_utilization_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "CUSTOMER_CONTRACT_CALLOFF_REVENUE_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-07-26", "peak_price": 87500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20230726_SEPARATOR_CUSTOMER_CALLOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_attention", "calloff_or_delivery_schedule_claim", "revenue_conversion_or_utilization_visibility_signal"], "stage3_evidence_fields": ["contracted_volume_and_customer_calloff_required", "delivery_schedule_and_utilization_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["customer_contract_calloff_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_delay_or_volume_gap", "utilization_or_revenue_conversion_failure", "margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.95, "MAE_30D_pct": -24.68, "MAE_90D_pct": -45.95, "MFE_180D_pct": 10.5, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_PREMIUM_4B", "case_role": "separator_calloff_utilization_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none for selected symbols", "current_profile_error": true, "current_profile_verdict": "Separator/call-off premium should be capped at Yellow or local 4B when utilization, customer call-off, revenue conversion, margin and revision bridge do not support the valuation already paid.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.08, "entry_date": "2023-07-26", "entry_price": 108600, "evidence_family": "separator_capacity_customer_calloff_price_premium_without_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CUSTOMER_CONTRACT_CALLOFF_REVENUE_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 58700, "peak_date": "2023-07-26", "peak_price": 120000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_attention", "calloff_or_delivery_schedule_claim", "revenue_conversion_or_utilization_visibility_signal"], "stage3_evidence_fields": ["contracted_volume_and_customer_calloff_required", "delivery_schedule_and_utilization_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["customer_contract_calloff_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_delay_or_volume_gap", "utilization_or_revenue_conversion_failure", "margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CUSTOMER_CONTRACT_CALLOFF_REVENUE_CONVERSION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_customer_contract_calloff_4b_gap_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery customer-contract/call-off rows should allow Stage2 on early contract plus delivery/call-off visibility, but Stage3 Green requires contracted volume, customer call-off cadence, delivery schedule, utilization, margin and revision bridge; late separator/electrolyte contract price premium without call-off proof should route to local 4B or counterexample.",
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
3. Add C12-specific customer contract / call-off / utilization / revenue-conversion guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_STAGE2_ALLOWED_ON_EARLY_CONTRACT_CALLOFF_DELIVERY_VISIBILITY
- C12_GREEN_REQUIRES_CONTRACTED_VOLUME_CALLOFF_UTILIZATION_MARGIN_REVISION
- C12_CUSTOMER_CONTRACT_PRICE_PREMIUM_LOCAL_4B
- C12_CONTRACT_WITHOUT_CALLOFF_REVENUE_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

