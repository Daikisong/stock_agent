# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer contract / copper-foil call-off guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: COPPERFOIL_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_copperfoil_customer_calloff_2023_2024_research.md
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

This run avoids those top-covered C12 symbols and adds 011790, 020150, and 336370.  
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
011790 SKC: selected 2023 forward window clean; corporate-action candidates are 1998-01-03 and 2001-12-21, outside selected test window.
020150 롯데에너지머티리얼즈: corporate_action_candidate_count=0.
336370 솔루스첨단소재: selected post-2024-01-30 forward window clean; corporate-action candidates are 2024-01-08 and 2024-01-30, before selected trigger window.
```

## 3. Research thesis

C12 should not treat a battery customer contract or copper-foil rebound as bankable demand. It should test whether the contract converts into customer call-offs and utilization:

```text
battery customer contract / copper-foil rebound attention
→ customer call-off stability and shipment cadence
→ plant utilization and capacity-ramp absorption
→ ASP/mix, copper/input-cost pass-through and working capital
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A battery supply contract is a reservation book. Green should not pay for the reservation alone; it should require the customer to call off volume, the line to run, and the invoice to survive ASP and input-cost pressure.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_011790_SKC_20230726_COPPERFOIL_CUSTOMER_CALLOFF_4B | 011790 | protective_copperfoil_customer_calloff_price_premium_4b_success | 2023-07-26 | 103000 | 111000 on 2023-07-26 | 68000 on 2023-10-23 | 7.77% | 7.77% | 7.77% | -33.98% | -38.74% |
| C12_020150_LOTTEENERGYMATERIALS_20230726_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN | 020150 | copperfoil_customer_contract_false_green_counterexample | 2023-07-26 | 56700 | 59700 on 2023-07-26 | 31000 on 2024-02-01 | 5.29% | 5.29% | 5.29% | -45.33% | -48.07% |
| C12_336370_SOLUS_20240701_COPPERFOIL_REBOUND_PREMIUM_4B | 336370 | copperfoil_rebound_premium_counterexample | 2024-07-01 | 23050 | 23500 on 2024-07-01 | 7650 on 2024-12-09 | 1.95% | 1.95% | 1.95% | -66.81% | -67.45% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C12 Green should require direct customer call-off visibility, utilization/capacity-ramp recovery, ASP/mix, input-cost pass-through, working-capital and margin/revision confirmation.
- 020150 shows the false-Green/Yellow guard: customer-contract recovery and price confirmation did not protect the forward path without call-off and utilization evidence.

### 4B
- 011790 is the protective 4B anchor. The July 2023 copper-foil/customer-contract spike made its high on the trigger day, then drew down as utilization and margin evidence did not refresh.
- 020150 is the customer-contract false-Green counterexample. The trigger had only a small MFE and a large 180D MAE.
- 336370 is the rebound-premium counterexample. After the post-corporate-action window, the July 2024 copper-foil rebound had very little additional upside before a deep 180D drawdown.

### 4C
- No hard customer cancellation, covenant breach or plant impairment is asserted.
- The C12 break mode is call-off-to-utilization failure: the contract story remains plausible, but customer shipment cadence, plant utilization, ASP/mix, input-cost and gross-margin revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C12_011790_SKC_20230726_COPPERFOIL_CUSTOMER_CALLOFF_4B": {
    "ASP_mix_input_cost_bridge": 4,
    "calloff_stability": 3,
    "customer_contract_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "total": 27,
    "utilization_capacity_ramp": 4,
    "valuation_rerating_runway": 1
  },
  "C12_020150_LOTTEENERGYMATERIALS_20230726_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN": {
    "ASP_mix_input_cost_bridge": 3,
    "calloff_stability": 3,
    "customer_contract_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 5,
    "total": 26,
    "utilization_capacity_ramp": 3,
    "valuation_rerating_runway": 1
  },
  "C12_336370_SOLUS_20240701_COPPERFOIL_REBOUND_PREMIUM_4B": {
    "ASP_mix_input_cost_bridge": 3,
    "calloff_stability": 3,
    "customer_contract_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 23,
    "utilization_capacity_ramp": 3,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_customer_contract_attention and calloff_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if copperfoil_contract_price_premium and no calloff_utilization_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and contract_to_utilization_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020150 / 2023-07-26: copper-foil customer-contract recovery can be over-promoted if the model treats price confirmation as call-off, utilization and margin proof.
- 336370 / 2024-07-01: copper-foil rebound premium can become price-only when customer call-off and utilization evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -33.98, "MAE_30D_pct": -14.47, "MAE_90D_pct": -33.98, "MFE_180D_pct": 7.77, "MFE_30D_pct": 7.77, "MFE_90D_pct": 7.77, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_011790_SKC_20230726_COPPERFOIL_CUSTOMER_CALLOFF_4B", "case_role": "protective_copperfoil_customer_calloff_price_premium_4b_success", "company_name": "SKC", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 1998-01-03 and 2001-12-21, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when copper-foil/battery materials customer-contract enthusiasm had already been capitalized but call-off stability, plant utilization, ASP/mix, input-cost pass-through and margin/revision evidence did not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.74, "entry_date": "2023-07-26", "entry_price": 103000, "evidence_family": "copperfoil_customer_contract_price_premium_without_calloff_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-23", "low_price_180d": 68000, "peak_date": "2023-07-26", "peak_price": 111000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 4, "calloff_stability": 3, "customer_contract_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 27, "utilization_capacity_ramp": 4, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_011790_SKC_20230726_COPPERFOIL_CUSTOMER_CALLOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_or_supply_agreement_attention", "customer_calloff_stability_visibility", "utilization_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["direct_customer_calloff_and_volume_required", "plant_utilization_and_capacity_ramp_required", "ASP_mix_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_customer_contract_price_premium", "rebound_or_contract_theme_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap_or_volume_delay", "utilization_capacity_ramp_disappointment", "margin_revision_bridge_failure"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.33, "MAE_30D_pct": -16.93, "MAE_90D_pct": -34.66, "MFE_180D_pct": 5.29, "MFE_30D_pct": 5.29, "MFE_90D_pct": 5.29, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_020150_LOTTEENERGYMATERIALS_20230726_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN", "case_role": "copperfoil_customer_contract_false_green_counterexample", "company_name": "롯데에너지머티리얼즈", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Copper-foil customer-contract recovery should stay Yellow or route to 4B when price confirmation is not followed by customer call-off stability, utilization recovery, ASP/mix, input-cost and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.07, "entry_date": "2023-07-26", "entry_price": 56700, "evidence_family": "copperfoil_customer_contract_recovery_price_confirmation_without_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-02-01", "low_price_180d": 31000, "peak_date": "2023-07-26", "peak_price": 59700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020150.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 3, "calloff_stability": 3, "customer_contract_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 5, "total": 26, "utilization_capacity_ramp": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_020150_LOTTEENERGYMATERIALS_20230726_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_or_supply_agreement_attention", "customer_calloff_stability_visibility", "utilization_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["direct_customer_calloff_and_volume_required", "plant_utilization_and_capacity_ramp_required", "ASP_mix_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_customer_contract_price_premium", "rebound_or_contract_theme_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap_or_volume_delay", "utilization_capacity_ramp_disappointment", "margin_revision_bridge_failure"], "symbol": "020150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -66.81, "MAE_30D_pct": -36.05, "MAE_90D_pct": -51.41, "MFE_180D_pct": 1.95, "MFE_30D_pct": 1.95, "MFE_90D_pct": 1.95, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_336370_SOLUS_20240701_COPPERFOIL_REBOUND_PREMIUM_4B", "case_role": "copperfoil_rebound_premium_counterexample", "company_name": "솔루스첨단소재", "corporate_action_window_status": "clean_post_2024_01_30_forward_window; corporate-action candidates are 2024-01-08 and 2024-01-30, both before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Copper-foil rebound premium should route to local 4B or counterexample unless customer call-off recovery, utilization, ASP/mix, input-cost and margin/revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.45, "entry_date": "2024-07-01", "entry_price": 23050, "evidence_family": "copperfoil_rebound_price_premium_without_customer_calloff_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-12-09", "low_price_180d": 7650, "peak_date": "2024-07-01", "peak_price": 23500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336370.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 3, "calloff_stability": 3, "customer_contract_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 23, "utilization_capacity_ramp": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_336370_SOLUS_20240701_COPPERFOIL_REBOUND_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_or_supply_agreement_attention", "customer_calloff_stability_visibility", "utilization_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["direct_customer_calloff_and_volume_required", "plant_utilization_and_capacity_ramp_required", "ASP_mix_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_customer_contract_price_premium", "rebound_or_contract_theme_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap_or_volume_delay", "utilization_capacity_ramp_disappointment", "margin_revision_bridge_failure"], "symbol": "336370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv", "trigger_date": "2024-07-01", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "COPPERFOIL_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_customer_contract_calloff_copperfoil_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery customer-contract/call-off rows should block Stage3 Green when contract or rebound price action lacks direct customer call-off stability, utilization/capacity-ramp recovery, ASP/mix, input-cost and margin/revision bridge; copper-foil customer-contract price premium should route to local 4B or counterexample unless non-price conversion evidence refreshes.",
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
3. Add C12-specific battery customer-contract / call-off / utilization / margin-revision / copper-foil local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_BLOCK_GREEN_WITHOUT_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE
- C12_COPPERFOIL_CONTRACT_PRICE_PREMIUM_LOCAL_4B
- C12_REQUIRE_ASP_MIX_INPUT_COST_WORKING_CAPITAL_REVISION
- C12_CONTRACT_STORY_WITHOUT_SHIPMENT_CADENCE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

