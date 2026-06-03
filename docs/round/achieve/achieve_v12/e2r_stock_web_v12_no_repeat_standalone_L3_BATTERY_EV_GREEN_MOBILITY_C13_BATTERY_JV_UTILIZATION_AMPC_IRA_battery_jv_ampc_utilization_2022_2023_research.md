# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C13 — Battery JV / utilization / AMPC / IRA guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_AMPC_UTILIZATION_MARGIN_REVISION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_4C_guard_validation
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_battery_jv_ampc_utilization_2022_2023_research.md
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

C13 has a narrow real-world symbol universe, so this run does not pretend to add a new symbol. It avoids hard duplicates by selecting new `symbol + trigger_type + entry_date` combinations and adds a sharper failure-mode split:
```text
positive: IRA/AMPC/JV capacity visibility can work when utilization and margin/revision bridge later close.
counterexample: AMPC/JV headline credit fails when utilization, call-off, funding burden, and revision evidence do not close.
```

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
373220 LG에너지솔루션: corporate_action_candidate_count=0.
006400 삼성SDI: 2023 forward window clean; corporate-action candidates are old, outside the test window.
096770 SK이노베이션: 2023 forward window clean; corporate-action candidate is 2024-11-20, outside the test window.
```

## 3. Research thesis

C13 is not just "battery policy good." It is a conversion test:

```text
IRA / AMPC / JV announcement
→ capacity and subsidy option value
→ utilization and customer call-off
→ AMPC-to-cash and margin bridge
→ EPS/FCF revision
→ rerating
```

The trap is that AMPC credit can look like earnings before it becomes cash. If the plant is under-utilized, the customer call-off is soft, or funding burden dominates, the subsidy headline becomes a painted door: it looks like an exit, but does not open into FCF.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C13_373220_LGES_20220812_IRA_AMPC_JV_STAGE2_SUCCESS | 373220 | positive_ampc_jv_stage2_success | 2022-08-12 | 460500 | 629000 on 2022-11-11 | 420000 on 2022-09-30 | 11.4% | 36.59% | 36.59% | -8.79% | -29.01% |
| C13_006400_SDI_20230307_AMPC_JV_UTILIZATION_FALSE_GREEN | 006400 | false_green_counterexample | 2023-03-07 | 793000 | 801000 on 2023-03-07 | 417000 on 2023-11-13 | 1.01% | 1.01% | 1.01% | -47.41% | -47.94% |
| C13_096770_SKINNO_20230330_SKON_AMPC_UTILIZATION_COUNTEREXAMPLE | 096770 | ampc_jv_utilization_4c_watch_counterexample | 2023-03-30 | 187200 | 209000 on 2023-04-11 | 120100 on 2023-11-01 | 11.65% | 11.65% | 11.65% | -35.84% | -42.54% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- IRA/AMPC/JV attention is enough to route a Stage2 research row.
- 373220 shows the cleanest positive path: policy plus capacity visibility produced a strong rerating window before the market later demanded utilization and margin proof.

### Stage3 / Green
- C13 Green should require utilization, customer call-off/volume, AMPC-to-cash conversion, margin and revision confirmation.
- 006400 and 096770 show why policy/JV optionality should not be promoted to Green when the bridge is still open.

### 4B
- A battery policy premium can become local 4B when valuation prices the subsidy before the plant-level evidence catches up.
- 373220 after the 2022 rerating still required 4B discipline; a true policy-positive case can mature into a risk-control case.

### 4C
- 096770 is closer to a 4C-watch counterexample: when AMPC headline credit coexists with funding burden and utilization uncertainty, the model should not treat the headline as EPS bodyweight.
- 006400 is a softer false-Green: the company was high quality, but the stock path shows that JV/AMPC optionality alone was not enough.

## 6. Raw component score breakdown

```json
{
  "C13_006400_SDI_20230307_AMPC_JV_UTILIZATION_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C13_096770_SKINNO_20230330_SKON_AMPC_UTILIZATION_COUNTEREXAMPLE": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C13_373220_LGES_20220812_IRA_AMPC_JV_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 12,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 63,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C13 guard:
```text
if ira_ampc_jv_attention and no utilization_calloff_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if ampc_policy_premium and plant_utilization_or_cash_conversion_uncertain:
    route_to_local_4B_or_4C_watch = true

if funding_burden plus utilization_shortfall dominates subsidy_credit:
    route_to_counterexample = true
```

Residual errors:
```text
current_profile_error_count = 2
- 006400 / 2023-03-07: high-quality battery JV optionality can look like Green, but the later path demands utilization/revision proof.
- 096770 / 2023-03-30: AMPC/JV headline credit can be outweighed by cash burn, utilization uncertainty, and funding burden.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -8.79, "MAE_30D_pct": -5.54, "MAE_90D_pct": -8.79, "MFE_180D_pct": 36.59, "MFE_30D_pct": 11.4, "MFE_90D_pct": 36.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_373220_LGES_20220812_IRA_AMPC_JV_STAGE2_SUCCESS", "case_role": "positive_ampc_jv_stage2_success", "company_name": "LG에너지솔루션", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was valid because IRA/AMPC and JV capacity visibility created a real rerating route, but Green still requires utilization, customer call-off, margin, and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.01, "entry_date": "2022-08-12", "entry_price": 460500, "evidence_family": "ira_ampc_jv_capacity_visibility_to_rerating", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2022-09-30", "low_price_180d": 420000, "peak_date": "2022-11-11", "peak_price": 629000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/373/373220.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 12, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 63, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C13_373220_LGES_20220812_IRA_AMPC_JV_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["ira_ampc_or_jv_policy_attention", "capacity_or_customer_visibility_claim", "relative_strength_or_policy_premium"], "stage3_evidence_fields": ["utilization_confirmation_required", "customer_calloff_or_volume_confirmation_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_premium_or_battery_cell_rerating_matured", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["utilization_shortfall", "ampc_credit_without_cashflow_conversion", "funding_burden_or_revision_break"], "symbol": "373220", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv", "trigger_date": "2022-08-12", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -47.41, "MAE_30D_pct": -11.1, "MAE_90D_pct": -15.89, "MFE_180D_pct": 1.01, "MFE_30D_pct": 1.01, "MFE_90D_pct": 1.01, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_006400_SDI_20230307_AMPC_JV_UTILIZATION_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "삼성SDI", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "JV/AMPC optionality should not become Green if utilization, customer call-off and margin/revision evidence are still unresolved.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.94, "entry_date": "2023-03-07", "entry_price": 793000, "evidence_family": "battery_jv_ampc_optionality_without_utilization_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-13", "low_price_180d": 417000, "peak_date": "2023-03-07", "peak_price": 801000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006400.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C13_006400_SDI_20230307_AMPC_JV_UTILIZATION_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["ira_ampc_or_jv_policy_attention", "capacity_or_customer_visibility_claim", "relative_strength_or_policy_premium"], "stage3_evidence_fields": ["utilization_confirmation_required", "customer_calloff_or_volume_confirmation_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_premium_or_battery_cell_rerating_matured", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["utilization_shortfall", "ampc_credit_without_cashflow_conversion", "funding_burden_or_revision_break"], "symbol": "006400", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv", "trigger_date": "2023-03-07", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.84, "MAE_30D_pct": -8.55, "MAE_90D_pct": -35.84, "MFE_180D_pct": 11.65, "MFE_30D_pct": 11.65, "MFE_90D_pct": 11.65, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_096770_SKINNO_20230330_SKON_AMPC_UTILIZATION_COUNTEREXAMPLE", "case_role": "ampc_jv_utilization_4c_watch_counterexample", "company_name": "SK이노베이션", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "AMPC headline credit should stay Yellow/4C-watch when cash burn, utilization, funding burden and revision bridge are not closed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.54, "entry_date": "2023-03-30", "entry_price": 187200, "evidence_family": "skon_jv_ampc_credit_without_cashflow_utilization_closure", "evidence_url_pending": false, "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-01", "low_price_180d": 120100, "peak_date": "2023-04-11", "peak_price": 209000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/096/096770.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C13_096770_SKINNO_20230330_SKON_AMPC_UTILIZATION_COUNTEREXAMPLE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["ira_ampc_or_jv_policy_attention", "capacity_or_customer_visibility_claim", "relative_strength_or_policy_premium"], "stage3_evidence_fields": ["utilization_confirmation_required", "customer_calloff_or_volume_confirmation_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_premium_or_battery_cell_rerating_matured", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["utilization_shortfall", "ampc_credit_without_cashflow_conversion", "funding_burden_or_revision_break"], "symbol": "096770", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_MARGIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_jv_ampc_utilization_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C13 battery JV/AMPC/IRA rows should cap at Stage2/Yellow unless utilization, customer call-off/volume, AMPC-to-cash conversion, funding burden, margin and revision bridge close; policy premium alone should route to local 4B or 4C-watch.",
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
3. Because C13 has a narrow symbol universe, accept same-symbol soft duplicates only when date, trigger family, Stage transition, or failure mode differs.
4. Add C13-specific utilization/AMPC-to-cash/funding-burden guard only as a shadow candidate until more rows exist.

Candidate rule:
- C13_GREEN_REQUIRES_UTILIZATION_CALLOFF_AMPC_CASH_MARGIN_REVISION
- C13_AMPC_POLICY_PREMIUM_LOCAL_4B_OR_4C_WATCH
- C13_JV_OPTIONALITY_WITHOUT_UTILIZATION_STAGE2_CAP

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.

