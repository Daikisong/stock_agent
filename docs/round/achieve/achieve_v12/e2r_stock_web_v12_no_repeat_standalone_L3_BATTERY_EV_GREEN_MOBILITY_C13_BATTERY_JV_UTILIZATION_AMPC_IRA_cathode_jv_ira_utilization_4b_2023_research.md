# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C13 — Battery JV utilization / AMPC·IRA cathode 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: CATHODE_JV_IRA_UTILIZATION_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|false_green_utilization_subsidy_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_cathode_jv_ira_utilization_4b_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA current coverage:
rows=16, symbols=3, date range=2022-05-25~2025-04-08, good/bad S2=2/9, 4B/4C=1/0
top covered symbols: 006400(7), 373220(7), 096770(2)
```

This run avoids those top-covered C13 symbols and adds 003670, 051910, and 005070.  
Each row uses a new `C13 + symbol + trigger_type + entry_date` hard key:
```text
C13 + 003670 + Stage2-Actionable + 2023-03-31
C13 + 051910 + Stage3-Yellow + 2023-07-26
C13 + 005070 + 4B-local-price-only + 2023-07-26
```

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
003670 포스코퓨처엠: selected 2023 forward window clean; corporate-action candidates are 2015-05-04 and 2021-02-03, outside selected test window.
051910 LG화학: corporate_action_candidate_count=0; clean 2023 forward window.
005070 코스모신소재: selected 2023/2024 forward window clean; historical corporate-action candidates latest 2019-11-13, outside selected test window.
```

## 3. Research thesis

C13 should distinguish **JV/IRA/AMPC optionality that becomes utilization and margin** from **battery-capacity premium already paid in price**:

```text
battery JV / IRA / AMPC / customer contract attention
→ customer call-off and volume conversion
→ JV ramp or plant utilization absorption
→ subsidy economics realization, if applicable
→ ASP/input-cost and working-capital bridge
→ gross margin and revision confirmation
→ Stage2/Green or local 4B cap
```

A JV or subsidy headline is a factory blueprint. Stage2 can buy it when the line starts filling with call-offs and margin revision. Green should require the blueprint to become utilization, not just a higher blueprint multiple.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C13_003670_POSCOFUTUREM_20230331_CATHODE_JV_IRA_STAGE2 | 003670 | positive_cathode_jv_ira_utilization_stage2_success_with_later_4b_refresh | 2023-03-31 | 272500 | 694000 on 2023-07-26 | 232500 on 2023-10-31 | 55.05% | 154.68% | 154.68% | -14.68% | -66.5% |
| C13_051910_LGCHEM_20230726_CATHODE_IRA_FALSE_GREEN | 051910 | cathode_ira_capacity_false_green_counterexample | 2023-07-26 | 728000 | 783000 on 2023-07-26 | 424500 on 2023-10-26 | 7.55% | 7.55% | 7.55% | -41.69% | -45.79% |
| C13_005070_COSMOAMT_20230726_CATHODE_MATERIAL_UTILIZATION_4B | 005070 | cathode_material_utilization_price_premium_counterexample | 2023-07-26 | 190400 | 226000 on 2023-07-26 | 126500 on 2024-01-25 | 18.7% | 18.7% | 18.7% | -33.56% | -44.03% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 003670 is the positive anchor. The March 2023 cathode/JV/IRA-capacity route produced a large 30D/90D/180D MFE before the July premium required 4B refresh discipline.
- Stage2 is allowed only when customer/JV/IRA salience maps to call-off volume, utilization ramp, ASP/input-cost bridge and margin/revision visibility.

### Stage3 / Green
- C13 Green should require customer call-off or volume conversion, JV ramp/utilization absorption, subsidy economics realization where applicable, ASP/input-cost bridge and margin/revision confirmation.
- 051910 is the false-Green/Yellow guard: capacity/IRA price confirmation was visible, but the July 2023 premium did not provide enough incremental call-off/utilization/margin proof to survive the forward path.

### 4B
- 005070 fills the cathode-material capacity price-premium 4B pocket. The July 2023 trigger had limited residual upside and then a much larger forward MAE.
- 051910 shows the same problem in a larger integrated chemical/cathode-capacity name: the market can pay for IRA/JV optionality before utilization and margin evidence arrives.
- 003670 also demonstrates that valid Stage2 can become local 4B after the rerating has capitalized the JV/utilization option.

### 4C
- No hard JV cancellation, subsidy denial, plant failure or accounting break is asserted.
- The failure mode is utilization/subsidy realization gap: the JV/IRA thesis may remain real while customer call-off, utilization, ASP/input-cost and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C13_003670_POSCOFUTUREM_20230331_CATHODE_JV_IRA_STAGE2": {
    "ASP_input_cost_bridge": 7,
    "IRA_AMPC_economics_visibility": 6,
    "JV_or_customer_contract_visibility": 10,
    "capacity_absorption_working_capital": 7,
    "information_confidence": 4,
    "margin_revision_bridge": 8,
    "market_mispricing": 9,
    "total": 67,
    "utilization_ramp_quality": 8,
    "valuation_rerating_runway": 8
  },
  "C13_005070_COSMOAMT_20230726_CATHODE_MATERIAL_UTILIZATION_4B": {
    "ASP_input_cost_bridge": 3,
    "IRA_AMPC_economics_visibility": 3,
    "JV_or_customer_contract_visibility": 5,
    "capacity_absorption_working_capital": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 27,
    "utilization_ramp_quality": 3,
    "valuation_rerating_runway": 1
  },
  "C13_051910_LGCHEM_20230726_CATHODE_IRA_FALSE_GREEN": {
    "ASP_input_cost_bridge": 3,
    "IRA_AMPC_economics_visibility": 4,
    "JV_or_customer_contract_visibility": 6,
    "capacity_absorption_working_capital": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 29,
    "utilization_ramp_quality": 3,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C13 guard:
```text
if battery_JV_IRA and calloff_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if battery_JV_IRA_capacity_price_premium and no incremental_calloff_utilization_ASP_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and utilization_subsidy_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 051910 / 2023-07-26: cathode/IRA capacity confirmation can be over-promoted if price heat substitutes for utilization and margin proof.
- 005070 / 2023-07-26: cathode-material capacity premium can look actionable, but fails without renewed call-off, utilization and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -14.68, "MAE_30D_pct": -6.42, "MAE_90D_pct": -6.42, "MFE_180D_pct": 154.68, "MFE_30D_pct": 55.05, "MFE_90D_pct": 154.68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_003670_POSCOFUTUREM_20230331_CATHODE_JV_IRA_STAGE2", "case_role": "positive_cathode_jv_ira_utilization_stage2_success_with_later_4b_refresh", "company_name": "포스코퓨처엠", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 2015-05-04 and 2021-02-03, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when cathode JV/IRA customer contract optionality, capacity expansion and utilization leverage were visible before the rerating was fully capitalized. Green still requires customer call-off, JV ramp timing, plant utilization, AMPC or IRA economics where applicable, ASP/input-cost pass-through and margin/revision confirmation; after the July 2023 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.5, "entry_date": "2023-03-31", "entry_price": 272500, "evidence_family": "cathode_jv_ira_customer_contract_capacity_utilization_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CATHODE_JV_IRA_UTILIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 232500, "peak_date": "2023-07-26", "peak_price": 694000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003670.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 7, "IRA_AMPC_economics_visibility": 6, "JV_or_customer_contract_visibility": 10, "capacity_absorption_working_capital": 7, "information_confidence": 4, "margin_revision_bridge": 8, "market_mispricing": 9, "total": 67, "utilization_ramp_quality": 8, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C13_003670_POSCOFUTUREM_20230331_CATHODE_JV_IRA_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_JV_or_customer_contract_visibility", "IRA_AMPC_or_subsidy_economics_visibility", "utilization_calloff_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_or_volume_conversion_required", "JV_ramp_or_utilization_absorption_required", "IRA_AMPC_ASP_inputcost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_JV_IRA_capacity_price_premium", "utilization_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_or_utilization_gap", "AMPC_IRA_realization_or_project_timetable_gap", "margin_revision_bridge_failure"], "symbol": "003670", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "trigger_date": "2023-03-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.69, "MAE_30D_pct": -24.73, "MAE_90D_pct": -41.69, "MFE_180D_pct": 7.55, "MFE_30D_pct": 7.55, "MFE_90D_pct": 7.55, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_051910_LGCHEM_20230726_CATHODE_IRA_FALSE_GREEN", "case_role": "cathode_ira_capacity_false_green_counterexample", "company_name": "LG화학", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_forward_window", "current_profile_error": true, "current_profile_verdict": "Cathode/IRA capacity price confirmation should remain Yellow or route to local 4B when customer call-off, utilization ramp, ASP/input-cost bridge and margin/revision evidence are not refreshing. The July 2023 price premium had limited residual upside and much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.79, "entry_date": "2023-07-26", "entry_price": 728000, "evidence_family": "cathode_ira_capacity_price_confirmation_without_customer_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CATHODE_JV_IRA_UTILIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-26", "low_price_180d": 424500, "peak_date": "2023-07-26", "peak_price": 783000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/051/051910.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "IRA_AMPC_economics_visibility": 4, "JV_or_customer_contract_visibility": 6, "capacity_absorption_working_capital": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 29, "utilization_ramp_quality": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C13_051910_LGCHEM_20230726_CATHODE_IRA_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_JV_or_customer_contract_visibility", "IRA_AMPC_or_subsidy_economics_visibility", "utilization_calloff_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_or_volume_conversion_required", "JV_ramp_or_utilization_absorption_required", "IRA_AMPC_ASP_inputcost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_JV_IRA_capacity_price_premium", "utilization_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_or_utilization_gap", "AMPC_IRA_realization_or_project_timetable_gap", "margin_revision_bridge_failure"], "symbol": "051910", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -33.56, "MAE_30D_pct": -21.43, "MAE_90D_pct": -27.63, "MFE_180D_pct": 18.7, "MFE_30D_pct": 18.7, "MFE_90D_pct": 18.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_005070_COSMOAMT_20230726_CATHODE_MATERIAL_UTILIZATION_4B", "case_role": "cathode_material_utilization_price_premium_counterexample", "company_name": "코스모신소재", "corporate_action_window_status": "clean_2023_2024_forward_window; historical corporate-action candidates latest 2019-11-13, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Cathode-material capacity/utilization price premium should route to local 4B or counterexample unless customer call-off, utilization, ASP/input-cost pass-through, inventory and margin/revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.03, "entry_date": "2023-07-26", "entry_price": 190400, "evidence_family": "cathode_material_capacity_price_premium_without_incremental_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CATHODE_JV_IRA_UTILIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-01-25", "low_price_180d": 126500, "peak_date": "2023-07-26", "peak_price": 226000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005070.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "IRA_AMPC_economics_visibility": 3, "JV_or_customer_contract_visibility": 5, "capacity_absorption_working_capital": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 27, "utilization_ramp_quality": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C13_005070_COSMOAMT_20230726_CATHODE_MATERIAL_UTILIZATION_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_JV_or_customer_contract_visibility", "IRA_AMPC_or_subsidy_economics_visibility", "utilization_calloff_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_or_volume_conversion_required", "JV_ramp_or_utilization_absorption_required", "IRA_AMPC_ASP_inputcost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_JV_IRA_capacity_price_premium", "utilization_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_or_utilization_gap", "AMPC_IRA_realization_or_project_timetable_gap", "margin_revision_bridge_failure"], "symbol": "005070", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CATHODE_JV_IRA_UTILIZATION_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_jv_utilization_ampc_ira_cathode_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C13 battery JV/IRA/AMPC rows should allow Stage2 when JV/customer-contract evidence is backed by call-off volume, utilization ramp, subsidy economics realization, ASP/input-cost bridge and margin-revision evidence, but should route to local 4B/Yellow when price already capitalizes IRA/JV optionality and incremental utilization/margin evidence has not refreshed.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C13 + symbol + trigger_type + entry_date.
3. Add C13-specific battery JV/IRA/AMPC / customer call-off / utilization ramp / ASP-input-cost / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C13_STAGE2_ALLOWED_ON_CALLOFF_UTILIZATION_MARGIN_REVISION_BRIDGE
- C13_GREEN_REQUIRES_JV_RAMP_SUBSIDY_REALIZATION_ASP_INPUT_COST_REVISION
- C13_JV_IRA_CAPACITY_PRICE_PREMIUM_LOCAL_4B
- C13_PRICE_CONFIRMATION_WITHOUT_UTILIZATION_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.

