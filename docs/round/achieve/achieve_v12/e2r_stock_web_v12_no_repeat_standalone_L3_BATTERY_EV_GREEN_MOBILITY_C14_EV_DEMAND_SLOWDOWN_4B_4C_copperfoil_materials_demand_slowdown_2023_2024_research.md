# E2R V12 No-Repeat Standalone Residual Research
## R9 / L3 / C14 — EV demand slowdown / copper-foil materials 4B·4C guard

metadata:
```text
selected_round: R9
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: COPPERFOIL_MATERIALS_DEMAND_SLOWDOWN_4B_4C_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_demand_slowdown_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_copperfoil_materials_demand_slowdown_2023_2024_research.md
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

This run avoids those top-covered C14 symbols and adds 011790, 020150, and 336370.  
Each row uses a new `C14 + symbol + trigger_type + entry_date` hard key.

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
011790 SKC: selected 2023 forward window clean; corporate-action candidates are 1998-01-03 and 2001-12-21, outside selected test window.
020150 롯데에너지머티리얼즈: corporate_action_candidate_count=0; clean 2023/2024 forward window.
336370 솔루스첨단소재: selected post-2024-01-30 forward window clean; corporate-action candidates are 2024-01-08 and 2024-01-30, before selected trigger window.
```

## 3. Research thesis

C14 should not treat EV-materials rebound price action as proof that EV demand slowdown has ended:

```text
EV demand slowdown / inventory correction
→ customer call-off and shipment cadence
→ copper-foil/materials utilization recovery
→ ASP/mix and input-cost pass-through
→ capex absorption and working-capital quality
→ gross margin and revision bridge
→ local 4B or 4C-watch if unresolved
```

A rebound candle is not a purchase order. Green should require the customer to call off volume, the line to run, and the margin bridge to recover.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C14_011790_SKC_20230726_EV_COPPERFOIL_DEMAND_SLOWDOWN_4B | 011790 | protective_ev_materials_demand_slowdown_4b_success | 2023-07-26 | 103000 | 111000 on 2023-07-26 | 68000 on 2023-10-23 | 7.77% | 7.77% | 7.77% | -33.98% | -38.74% |
| C14_020150_LOTTEENERGYMATERIALS_20230726_EV_COPPERFOIL_FALSE_RECOVERY | 020150 | ev_copperfoil_false_recovery_counterexample | 2023-07-26 | 56700 | 59700 on 2023-07-26 | 31000 on 2024-02-01 | 5.29% | 5.29% | 5.29% | -45.33% | -48.07% |
| C14_336370_SOLUS_20240701_EV_COPPERFOIL_DEMAND_SLOWDOWN_4C_WATCH | 336370 | ev_copperfoil_demand_slowdown_4c_watch_counterexample | 2024-07-01 | 23050 | 23500 on 2024-07-01 | 7650 on 2024-12-09 | 1.95% | 1.95% | 1.95% | -66.81% | -67.45% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C14 Green should require customer call-off recovery, volume recovery, utilization recovery, ASP/mix, input-cost pass-through, capex absorption and margin/revision confirmation.
- 020150 is the false-recovery guard: price confirmation had small residual upside but a much larger forward MAE once demand slowdown and utilization/margin weakness persisted.

### 4B
- 011790 is the protective 4B anchor. The EV materials/copper-foil recovery narrative was already capitalized while non-price demand evidence did not refresh.
- 336370 shows the later rebound-premium version: the trigger had almost no residual upside before a large drawdown.

### 4C
- 336370 is classified as 4C-watch rather than hard 4C because no single cancellation/accounting break is asserted.
- The failure mode is cumulative: EV demand slowdown, weak call-offs, utilization pressure, capex burden and margin-revision failure.
- Hard 4C should require clearer company-level financing, impairment, contract loss or operating break; absent that, 4C-watch / counterexample is the safer label.

## 6. Raw component score breakdown

```json
{
  "C14_011790_SKC_20230726_EV_COPPERFOIL_DEMAND_SLOWDOWN_4B": {
    "ASP_mix_input_cost_pressure": 7,
    "customer_calloff_gap": 8,
    "ev_demand_slowdown_signal": 9,
    "information_confidence": 3,
    "margin_revision_break": 7,
    "market_mispricing": 4,
    "total": 47,
    "utilization_pressure": 8,
    "valuation_rerating_runway": 1
  },
  "C14_020150_LOTTEENERGYMATERIALS_20230726_EV_COPPERFOIL_FALSE_RECOVERY": {
    "ASP_mix_input_cost_pressure": 7,
    "customer_calloff_gap": 8,
    "ev_demand_slowdown_signal": 8,
    "information_confidence": 3,
    "margin_revision_break": 7,
    "market_mispricing": 4,
    "total": 45,
    "utilization_pressure": 7,
    "valuation_rerating_runway": 1
  },
  "C14_336370_SOLUS_20240701_EV_COPPERFOIL_DEMAND_SLOWDOWN_4C_WATCH": {
    "ASP_mix_input_cost_pressure": 7,
    "customer_calloff_gap": 8,
    "ev_demand_slowdown_signal": 9,
    "information_confidence": 3,
    "margin_revision_break": 8,
    "market_mispricing": 3,
    "total": 47,
    "utilization_pressure": 8,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C14 guard:
```text
if EV_materials_rebound and no customer_calloff_utilization_margin_revision_bridge:
    block_stage2_green_positive = true
    route_to_local_4B_or_counterexample = true

if demand_slowdown + capex_utilization_burden + margin_revision_break:
    route_to_4C_watch = true

if rebound_price_confirmation and residual_upside_small_and_forward_MAE_large:
    strengthen_EV_demand_slowdown_guard = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020150 / 2023-07-26: copper-foil recovery can be over-promoted if price confirmation substitutes for customer call-off and utilization proof.
- 336370 / 2024-07-01: EV materials rebound can become price-only when demand slowdown, utilization and margin evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -33.98, "MAE_30D_pct": -14.47, "MAE_90D_pct": -33.98, "MFE_180D_pct": 7.77, "MFE_30D_pct": 7.77, "MFE_90D_pct": 7.77, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_011790_SKC_20230726_EV_COPPERFOIL_DEMAND_SLOWDOWN_4B", "case_role": "protective_ev_materials_demand_slowdown_4b_success", "company_name": "SKC", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 1998-01-03 and 2001-12-21, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when copper-foil/EV-materials rebound price action had already capitalized recovery expectations while non-price evidence still showed demand slowdown risk: weak customer call-off cadence, utilization uncertainty, ASP/input-cost pressure and insufficient margin/revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.74, "entry_date": "2023-07-26", "entry_price": 103000, "evidence_family": "ev_copperfoil_demand_slowdown_price_premium_without_customer_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_MATERIALS_DEMAND_SLOWDOWN_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-23", "low_price_180d": 68000, "peak_date": "2023-07-26", "peak_price": 111000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_pressure": 7, "customer_calloff_gap": 8, "ev_demand_slowdown_signal": 9, "information_confidence": 3, "margin_revision_break": 7, "market_mispricing": 4, "total": 47, "utilization_pressure": 8, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C14_011790_SKC_20230726_EV_COPPERFOIL_DEMAND_SLOWDOWN_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_recovery_not_sufficient_without_calloff", "customer_calloff_utilization_required", "ASP_mix_input_cost_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_volume_recovery_required", "plant_utilization_capacity_absorption_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["EV_materials_recovery_price_premium", "demand_slowdown_not_resolved", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap", "utilization_and_capex_absorption_failure", "margin_revision_break"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.33, "MAE_30D_pct": -16.93, "MAE_90D_pct": -34.66, "MFE_180D_pct": 5.29, "MFE_30D_pct": 5.29, "MFE_90D_pct": 5.29, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_020150_LOTTEENERGYMATERIALS_20230726_EV_COPPERFOIL_FALSE_RECOVERY", "case_role": "ev_copperfoil_false_recovery_counterexample", "company_name": "롯데에너지머티리얼즈", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "EV-materials recovery price confirmation should remain Yellow or local 4B when the customer call-off/utilization bridge is weak. The small residual MFE and large MAE show that price confirmation was not enough to offset EV demand slowdown and margin pressure.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.07, "entry_date": "2023-07-26", "entry_price": 56700, "evidence_family": "ev_materials_false_recovery_without_order_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_MATERIALS_DEMAND_SLOWDOWN_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-02-01", "low_price_180d": 31000, "peak_date": "2023-07-26", "peak_price": 59700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020150.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_pressure": 7, "customer_calloff_gap": 8, "ev_demand_slowdown_signal": 8, "information_confidence": 3, "margin_revision_break": 7, "market_mispricing": 4, "total": 45, "utilization_pressure": 7, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C14_020150_LOTTEENERGYMATERIALS_20230726_EV_COPPERFOIL_FALSE_RECOVERY", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_recovery_not_sufficient_without_calloff", "customer_calloff_utilization_required", "ASP_mix_input_cost_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_volume_recovery_required", "plant_utilization_capacity_absorption_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["EV_materials_recovery_price_premium", "demand_slowdown_not_resolved", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap", "utilization_and_capex_absorption_failure", "margin_revision_break"], "symbol": "020150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -66.81, "MAE_30D_pct": -36.05, "MAE_90D_pct": -51.41, "MFE_180D_pct": 1.95, "MFE_30D_pct": 1.95, "MFE_90D_pct": 1.95, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_336370_SOLUS_20240701_EV_COPPERFOIL_DEMAND_SLOWDOWN_4C_WATCH", "case_role": "ev_copperfoil_demand_slowdown_4c_watch_counterexample", "company_name": "솔루스첨단소재", "corporate_action_window_status": "clean_post_2024_01_30_forward_window; corporate-action candidates are 2024-01-08 and 2024-01-30, before selected trigger window", "current_profile_error": true, "current_profile_verdict": "EV/copper-foil rebound should route to 4C-watch or counterexample when demand slowdown, utilization pressure, financing/capex burden and margin/revision weakness dominate. Price-only rebound after a prior drawdown should not be treated as Stage2 or Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.45, "entry_date": "2024-07-01", "entry_price": 23050, "evidence_family": "ev_copperfoil_rebound_price_premium_with_demand_slowdown_utilization_margin_break", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_MATERIALS_DEMAND_SLOWDOWN_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-12-09", "low_price_180d": 7650, "peak_date": "2024-07-01", "peak_price": 23500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336370.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_pressure": 7, "customer_calloff_gap": 8, "ev_demand_slowdown_signal": 9, "information_confidence": 3, "margin_revision_break": 8, "market_mispricing": 3, "total": 47, "utilization_pressure": 8, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C14_336370_SOLUS_20240701_EV_COPPERFOIL_DEMAND_SLOWDOWN_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_recovery_not_sufficient_without_calloff", "customer_calloff_utilization_required", "ASP_mix_input_cost_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_volume_recovery_required", "plant_utilization_capacity_absorption_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["EV_materials_recovery_price_premium", "demand_slowdown_not_resolved", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_gap", "utilization_and_capex_absorption_failure", "margin_revision_break"], "symbol": "336370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv", "trigger_date": "2024-07-01", "trigger_type": "4C-watch", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "COPPERFOIL_MATERIALS_DEMAND_SLOWDOWN_4B_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "ev_demand_slowdown_copperfoil_materials_new_symbols_4b_4c_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R9",
  "shadow_rule_candidate": "C14 EV-demand slowdown rows should block Stage2/Green when EV materials/copper-foil rebound lacks customer call-off recovery, utilization recovery, ASP/mix and margin-revision bridge; price recovery should route to 4B or 4C-watch when demand slowdown and capex/utilization burden remain unresolved.",
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
3. Add C14-specific EV demand slowdown / customer call-off / utilization / capex absorption / margin-revision / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C14_BLOCK_GREEN_WITHOUT_CALLOFF_UTILIZATION_MARGIN_RECOVERY
- C14_EV_MATERIALS_REBOUND_PRICE_PREMIUM_LOCAL_4B
- C14_DEMAND_SLOWDOWN_CAPEX_UTILIZATION_MARGIN_BREAK_4C_WATCH
- C14_PRICE_RECOVERY_WITHOUT_CUSTOMER_VOLUME_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

