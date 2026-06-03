# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer-contract call-off risk / separator·aluminum-foil guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: SEPARATOR_ALUMINUMFOIL_CALLOFF_UTILIZATION_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_calloff_risk_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_separator_aluminumfoil_calloff_risk_2023_research.md
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

This run avoids those top-covered C12 symbols and adds 393890, 361610, and 006110.  
Each row uses a new `C12 + symbol + trigger_type + entry_date` hard key.

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
393890 더블유씨피: corporate_action_candidate_count=0; clean 2023/2024 forward window.
361610 SK아이이테크놀로지: corporate_action_candidate_count=0; clean 2023/2024 forward window.
006110 삼아알미늄: selected post-2023-02-09 forward window; earlier corporate-action candidates outside selected trigger window.
```

## 3. Research thesis

C12 should not treat a customer contract or capacity option as earnings evidence unless the customer actually calls off volume:

```text
battery customer contract / long-term supply optionality
→ customer call-off cadence and allocation quality
→ utilization and capacity absorption
→ ASP/mix, input-cost pass-through and working-capital quality
→ gross margin and revision bridge
→ Stage2/Green or local 4B/4C-watch
```

A battery contract is a reservation book. Stage2 can buy it when reservations turn into call-offs and running lines. Green should require the booked customer to pull volume, the plant to absorb fixed cost, and margins to revise.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B | 393890 | protective_separator_customer_calloff_risk_4b_success | 2023-07-26 | 75700 | 87700 on 2023-08-01 | 34350 on 2024-04-08 | 15.85% | 15.85% | 15.85% | -54.62% | -60.83% |
| C12_361610_SKIET_20230726_SEPARATOR_FALSE_RECOVERY | 361610 | separator_customer_contract_false_recovery_counterexample | 2023-07-26 | 108600 | 120000 on 2023-07-26 | 58700 on 2023-10-31 | 10.5% | 10.5% | 10.5% | -45.95% | -51.08% |
| C12_006110_SAMAAL_20231012_ALUMINUMFOIL_CALLOFF_LATECYCLE_4C_WATCH | 006110 | aluminum_foil_calloff_late_cycle_4c_watch_counterexample | 2023-10-12 | 152400 | 158900 on 2023-10-17 | 54300 on 2024-07-26 | 4.27% | 4.27% | 4.27% | -64.37% | -75.08% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C12 Green should require customer call-off volume conversion, utilization absorption, ASP/mix, input-cost pass-through and margin/revision confirmation.
- 361610 is the false-recovery guard: separator recovery price confirmation was visible, but customer call-off and utilization/margin evidence did not protect the forward path.

### 4B
- 393890 is the protective 4B anchor. The separator price premium was tradable, but it needed call-off and utilization evidence to remain actionable.
- 361610 shows that a large same-day spike can still be Yellow/4B-watch when the call-off bridge is weak.

### 4C
- 006110 is classified as 4C-watch rather than hard 4C because no single cancellation/accounting break is asserted.
- The failure mode is cumulative: late-cycle battery-foil contract optionality, weak incremental call-off, utilization uncertainty, input-cost/ASP pressure and margin-revision failure.
- Hard 4C should require clearer customer cancellation, impairment, financing break or accounting event; absent that, 4C-watch / counterexample is the safer label.

## 6. Raw component score breakdown

```json
{
  "C12_006110_SAMAAL_20231012_ALUMINUMFOIL_CALLOFF_LATECYCLE_4C_WATCH": {
    "ASP_mix_input_cost_bridge": 2,
    "calloff_cadence_quality": 2,
    "customer_contract_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "total": 21,
    "utilization_absorption": 2,
    "valuation_rerating_runway": 0
  },
  "C12_361610_SKIET_20230726_SEPARATOR_FALSE_RECOVERY": {
    "ASP_mix_input_cost_bridge": 3,
    "calloff_cadence_quality": 3,
    "customer_contract_visibility": 6,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 25,
    "utilization_absorption": 3,
    "valuation_rerating_runway": 1
  },
  "C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B": {
    "ASP_mix_input_cost_bridge": 3,
    "calloff_cadence_quality": 3,
    "customer_contract_visibility": 6,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 25,
    "utilization_absorption": 3,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_customer_contract and customer_calloff_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if contract_price_premium and no calloff_utilization_ASP_mix_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if calloff_gap + utilization_absorption_failure + margin_revision_break:
    route_to_4C_watch_or_counterexample = true
```

Residual errors:
```text
current_profile_error_count = 2
- 361610 / 2023-07-26: separator recovery can be over-promoted if price confirmation substitutes for customer call-off and utilization proof.
- 006110 / 2023-10-12: battery-foil contract optionality can look like actionable strength, but fails without fresh call-off, utilization and margin revisions.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -18.1, "MAE_90D_pct": -47.62, "MFE_180D_pct": 15.85, "MFE_30D_pct": 15.85, "MFE_90D_pct": 15.85, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B", "case_role": "protective_separator_customer_calloff_risk_4b_success", "company_name": "더블유씨피", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when separator capacity/customer-contract optionality was already capitalized but customer call-off cadence, utilization recovery, ASP/mix and margin/revision evidence did not support the price premium.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.83, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_customer_contract_calloff_risk_price_premium_without_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_ALUMINUMFOIL_CALLOFF_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-08-01", "peak_price": 87700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 3, "calloff_cadence_quality": 3, "customer_contract_visibility": 6, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 25, "utilization_absorption": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_visibility", "customer_calloff_cadence_required", "utilization_ASP_mix_inputcost_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_volume_conversion_required", "separator_or_foil_utilization_absorption_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["customer_contract_price_premium", "calloff_risk_not_resolved", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap", "utilization_and_capacity_absorption_failure", "margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.95, "MAE_30D_pct": -26.89, "MAE_90D_pct": -45.95, "MFE_180D_pct": 10.5, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_361610_SKIET_20230726_SEPARATOR_FALSE_RECOVERY", "case_role": "separator_customer_contract_false_recovery_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": true, "current_profile_verdict": "Separator recovery price confirmation should stay Yellow or route to 4B-watch when customer call-off and utilization/margin bridge are weak. Price strength alone did not convert the customer-contract narrative into durable revisions.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.08, "entry_date": "2023-07-26", "entry_price": 108600, "evidence_family": "separator_false_recovery_without_customer_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_ALUMINUMFOIL_CALLOFF_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 58700, "peak_date": "2023-07-26", "peak_price": 120000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 3, "calloff_cadence_quality": 3, "customer_contract_visibility": 6, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 25, "utilization_absorption": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_361610_SKIET_20230726_SEPARATOR_FALSE_RECOVERY", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_visibility", "customer_calloff_cadence_required", "utilization_ASP_mix_inputcost_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_volume_conversion_required", "separator_or_foil_utilization_absorption_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["customer_contract_price_premium", "calloff_risk_not_resolved", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap", "utilization_and_capacity_absorption_failure", "margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -64.37, "MAE_30D_pct": -27.3, "MAE_90D_pct": -47.38, "MFE_180D_pct": 4.27, "MFE_30D_pct": 4.27, "MFE_90D_pct": 4.27, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_006110_SAMAAL_20231012_ALUMINUMFOIL_CALLOFF_LATECYCLE_4C_WATCH", "case_role": "aluminum_foil_calloff_late_cycle_4c_watch_counterexample", "company_name": "삼아알미늄", "corporate_action_window_status": "selected post-2023-02-09 window clean; prior corporate-action candidates are outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Battery aluminum-foil contract optionality should route to 4C-watch/counterexample when late-cycle price confirmation is not followed by customer call-off volume, utilization, input-cost pass-through and margin/revision confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -75.08, "entry_date": "2023-10-12", "entry_price": 152400, "evidence_family": "battery_aluminumfoil_contract_calloff_latecycle_without_incremental_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_ALUMINUMFOIL_CALLOFF_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-07-26", "low_price_180d": 54300, "peak_date": "2023-10-17", "peak_price": 158900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006110.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 2, "calloff_cadence_quality": 2, "customer_contract_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "total": 21, "utilization_absorption": 2, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C12_006110_SAMAAL_20231012_ALUMINUMFOIL_CALLOFF_LATECYCLE_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_visibility", "customer_calloff_cadence_required", "utilization_ASP_mix_inputcost_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_volume_conversion_required", "separator_or_foil_utilization_absorption_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["customer_contract_price_premium", "calloff_risk_not_resolved", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap", "utilization_and_capacity_absorption_failure", "margin_revision_bridge_failure"], "symbol": "006110", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv", "trigger_date": "2023-10-12", "trigger_type": "4C-watch", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_ALUMINUMFOIL_CALLOFF_UTILIZATION_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_customer_contract_calloff_risk_separator_aluminumfoil_new_symbols_4b_4c_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery customer-contract rows should block Stage2/Green when customer contract optionality lacks call-off cadence, utilization absorption, ASP/mix, input-cost pass-through and margin/revision bridge; separator/foil price premiums should route to local 4B or 4C-watch when call-off risk and capacity absorption remain unresolved.",
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
3. Add C12-specific battery customer contract / call-off cadence / utilization absorption / ASP-mix / input-cost / margin-revision / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_BLOCK_GREEN_WITHOUT_CALLOFF_UTILIZATION_MARGIN_REVISION
- C12_CUSTOMER_CONTRACT_PRICE_PREMIUM_LOCAL_4B
- C12_CALLOFF_GAP_UTILIZATION_MARGIN_BREAK_4C_WATCH
- C12_PRICE_CONFIRMATION_WITHOUT_CUSTOMER_VOLUME_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

