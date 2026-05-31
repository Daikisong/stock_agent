# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C14 — EV demand slowdown 4B/4C component guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: ELECTROLYTE_SEPARATOR_DEMAND_CALLOFF_UTILIZATION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_electrolyte_separator_demand_slowdown_2023_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C14_EV_DEMAND_SLOWDOWN_4B_4C current coverage:
rows=23, symbols=5, date range=2023-07-26~2024-12-20, good/bad S2=0/0, 4B/4C=3/5
top covered symbols: 066970(6), 247540(6), 003670(5), 373220(4), 006400(2)
```

This run avoids those top-covered C14 symbols and adds 348370, 393890, and 361610.  
Each row uses a new `C14 + symbol + trigger_type + entry_date` hard key.

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

C14 should not wait for a headline that literally says "EV demand slowdown." It should detect when a battery-component stock has already priced capacity/customer optionality while the evidence bridge moves the other way:

```text
battery component price premium
→ customer call-off cadence weakens
→ utilization or delivery schedule loses visibility
→ ASP/mix and margin pressure appears
→ revisions stop carrying valuation
→ 4B or 4C
```

The factory can be built before demand arrives. Stage 4 begins when the market has paid for a full factory, but the customer's order cadence leaves machines waiting.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C14_348370_ENCHEM_20240408_ELECTROLYTE_EV_DEMAND_VALUATION_4B | 348370 | protective_4b_success_electrolyte_demand_slowdown | 2024-04-08 | 358000 | 394500 on 2024-04-08 | 108000 on 2024-11-15 | 10.2% | 10.2% | 10.2% | -69.83% | -72.62% |
| C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_CALLOFF_4C | 393890 | separator_demand_slowdown_4c_counterexample | 2023-07-26 | 75700 | 87500 on 2023-07-26 | 34350 on 2024-04-08 | 15.59% | 15.59% | 15.59% | -54.62% | -60.74% |
| C14_361610_SKIET_20230726_SEPARATOR_UTILIZATION_DEMAND_4C | 361610 | separator_utilization_4c_counterexample | 2023-07-26 | 108600 | 120000 on 2023-07-26 | 58700 on 2023-10-31 | 10.5% | 10.5% | 10.5% | -45.95% | -51.08% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as Stage2/Green positive research.
- The research target is post-premium risk routing: when battery component valuation already embeds contract/capacity optionality, the model should require fresh demand recovery, call-off, utilization, margin and revision evidence before allowing any Green.

### 4B
- 348370 is the local 4B protective anchor. The electrolyte stock had already capitalized a large customer/capacity narrative by April 2024, and the forward path shows why price premium itself should trigger risk discipline.
- This is a local 4B rather than automatic hard 4C because the first signal is valuation/proximity: the chart is telling the model that the evidence must be refreshed.

### 4C
- 393890 and 361610 are hard 4C/counterexample rows. Separator names had already priced customer/capacity optionality, then followed a deep drawdown path as call-off, utilization, margin and revision evidence failed to support valuation.
- The lesson is not just "battery fell." It is that the customer contract/capacity story did not convert into enough utilization bodyweight.

## 6. Raw component score breakdown

```json
{
  "C14_348370_ENCHEM_20240408_ELECTROLYTE_EV_DEMAND_VALUATION_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 25,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  },
  "C14_361610_SKIET_20230726_SEPARATOR_UTILIZATION_DEMAND_4C": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_CALLOFF_4C": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C14 guard:
```text
if battery_component_price_premium and no fresh_calloff_utilization_margin_revision_bridge:
    route_to_local_4B_watch = true
    block_stage3_green = true

if EV_demand_slowdown and customer_calloff_or_utilization_bridge_fails:
    route_to_4C_hard = true
    block_stage2_green = true

if separator_or_electrolyte_capacity_story and post_peak_drawdown_confirms:
    require_non_price_recovery_evidence_before_reentry = true
```

Residual errors:
```text
current_profile_error_count = 2
- 393890 / 2023-07-26: separator customer/capacity premium can be over-promoted if the model treats contract language as durable demand despite weakening call-off/utilization evidence.
- 361610 / 2023-07-26: separator utilization slowdown can become a hard 4C path when the stock has already priced capacity but margin/revision support fails.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -69.83, "MAE_30D_pct": -29.75, "MAE_90D_pct": -58.38, "MFE_180D_pct": 10.2, "MFE_30D_pct": 10.2, "MFE_90D_pct": 10.2, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_348370_ENCHEM_20240408_ELECTROLYTE_EV_DEMAND_VALUATION_4B", "case_role": "protective_4b_success_electrolyte_demand_slowdown", "company_name": "엔켐", "corporate_action_window_status": "clean_forward_window; corporate_action_candidate_count=0 for all selected symbols", "current_profile_error": false, "current_profile_verdict": "Local 4B was the useful signal once electrolyte capacity/customer optionality had been capitalized and EV demand/call-off risk began to dominate; fresh Green should require utilization, delivery call-off, margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -72.62, "entry_date": "2024-04-08", "entry_price": 358000, "evidence_family": "electrolyte_price_premium_before_ev_demand_calloff_utilization_slowdown", "evidence_url_pending": false, "fine_archetype_id": "ELECTROLYTE_SEPARATOR_DEMAND_CALLOFF_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-11-15", "low_price_180d": 108000, "peak_date": "2024-04-08", "peak_price": 394500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/348/348370.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 25, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C14_348370_ENCHEM_20240408_ELECTROLYTE_EV_DEMAND_VALUATION_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_component_customer_or_capacity_attention", "EV_demand_slowdown_watch", "customer_calloff_or_utilization_claim"], "stage3_evidence_fields": ["fresh_demand_recovery_evidence_required", "customer_calloff_and_utilization_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["battery_component_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["EV_demand_slowdown", "customer_calloff_delay_or_volume_gap", "utilization_margin_revision_bridge_failure"], "symbol": "348370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -17.57, "MAE_90D_pct": -33.29, "MFE_180D_pct": 15.59, "MFE_30D_pct": 15.59, "MFE_90D_pct": 15.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_CALLOFF_4C", "case_role": "separator_demand_slowdown_4c_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "clean_forward_window; corporate_action_candidate_count=0 for all selected symbols", "current_profile_error": true, "current_profile_verdict": "Separator demand-slowdown rows should hard-route to 4C or counterexample when customer call-off, utilization, ASP/mix and revision evidence deteriorate after the stock already priced contract/capacity optionality.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.74, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_customer_calloff_utilization_slowdown_after_battery_premium", "evidence_url_pending": false, "fine_archetype_id": "ELECTROLYTE_SEPARATOR_DEMAND_CALLOFF_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-07-26", "peak_price": 87500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 4, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_CALLOFF_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_component_customer_or_capacity_attention", "EV_demand_slowdown_watch", "customer_calloff_or_utilization_claim"], "stage3_evidence_fields": ["fresh_demand_recovery_evidence_required", "customer_calloff_and_utilization_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["battery_component_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["EV_demand_slowdown", "customer_calloff_delay_or_volume_gap", "utilization_margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.95, "MAE_30D_pct": -24.68, "MAE_90D_pct": -45.95, "MFE_180D_pct": 10.5, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_361610_SKIET_20230726_SEPARATOR_UTILIZATION_DEMAND_4C", "case_role": "separator_utilization_4c_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "clean_forward_window; corporate_action_candidate_count=0 for all selected symbols", "current_profile_error": true, "current_profile_verdict": "Separator utilization/call-off slowdown should cap any Stage3 thesis and route to 4C when price already embeds capacity value but demand, utilization, margin and revision evidence fail.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.08, "entry_date": "2023-07-26", "entry_price": 108600, "evidence_family": "separator_capacity_utilization_calloff_slowdown_without_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "ELECTROLYTE_SEPARATOR_DEMAND_CALLOFF_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 58700, "peak_date": "2023-07-26", "peak_price": 120000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 4, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C14_361610_SKIET_20230726_SEPARATOR_UTILIZATION_DEMAND_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_component_customer_or_capacity_attention", "EV_demand_slowdown_watch", "customer_calloff_or_utilization_claim"], "stage3_evidence_fields": ["fresh_demand_recovery_evidence_required", "customer_calloff_and_utilization_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["battery_component_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["EV_demand_slowdown", "customer_calloff_delay_or_volume_gap", "utilization_margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ELECTROLYTE_SEPARATOR_DEMAND_CALLOFF_UTILIZATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "ev_demand_slowdown_component_4b_4c_new_symbols_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C14 EV demand-slowdown rows should route battery-component price premiums to local 4B when valuation runs ahead of call-off/utilization evidence, and to 4C when EV demand, customer call-off, utilization, margin and revision bridges deteriorate after the stock already priced capacity/customer optionality.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C14 + symbol + trigger_type + entry_date.
3. Add C14-specific EV demand slowdown / call-off / utilization / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C14_PRICE_PREMIUM_WITHOUT_CALLOFF_UTILIZATION_LOCAL_4B
- C14_SEPARATOR_ELECTROLYTE_DEMAND_SLOWDOWN_HARD_4C
- C14_GREEN_BLOCK_REQUIRES_FRESH_DEMAND_RECOVERY_MARGIN_REVISION
- C14_POST_PEAK_DRAWDOWN_REQUIRES_NON_PRICE_RECOVERY_EVIDENCE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

