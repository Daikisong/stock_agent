# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C14 — EV demand slowdown 4B/4C guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: SEPARATOR_COPPERFOIL_EV_DEMAND_SLOWDOWN_UTILIZATION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_separator_copperfoil_demand_slowdown_2023_research.md
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

This run avoids the top-covered C14 symbols and adds 361610, 011790, and 393890.  
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
361610 SK아이이테크놀로지: corporate_action_candidate_count=0.
011790 SKC: 2023 forward window clean; corporate-action candidates are old, outside the test window.
393890 더블유씨피: corporate_action_candidate_count=0.
```

## 3. Research thesis

C14 is not a normal battery-upside archetype. It is the point where the model asks whether the EV supply-chain thesis has become overcapitalized against slowing demand:

```text
EV supply-chain / separator / copper-foil price premium
→ customer call-off and utilization must keep pace
→ inventory and margin quality must hold
→ revision bridge must remain visible
→ otherwise route to local 4B or 4C-watch
```

The core guard is that demand slowdown does not need to arrive as one loud accident. It can arrive as a quiet gap between capacity and call-off. Once that gap opens, the stock may still carry the old battery-theme label, but the earnings conveyor belt has slowed.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C14_361610_SKIET_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_LOCAL_4B | 361610 | protective_4b_success | 2023-07-26 | 108600 | 120000 on 2023-07-26 | 58700 on 2023-10-31 | 10.5% | 10.5% | 10.5% | -45.95% | -51.08% |
| C14_011790_SKC_20230405_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN | 011790 | ev_materials_false_green_counterexample | 2023-04-05 | 116300 | 122300 on 2023-04-05 | 68000 on 2023-10-23 | 5.16% | 5.16% | 5.16% | -41.53% | -44.4% |
| C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4C_WATCH | 393890 | separator_demand_slowdown_4c_watch_counterexample | 2023-07-26 | 75700 | 87500 on 2023-07-26 | 34350 on 2024-04-08 | 15.59% | 15.59% | 15.59% | -54.62% | -60.74% |

## 5. Stage evidence split

### Stage2 / Stage3
- EV material/separator exposure can remain a research route, but C14 should not use it as fresh positive evidence after the slowdown signal appears.
- After the slowdown trigger, Stage3 Green requires renewed call-off, utilization, inventory, margin and revision evidence.

### 4B
- 361610 is the protective 4B anchor. The July 2023 separator price premium had already capitalized the theme; local 4B protected against the following utilization/demand drawdown.
- 393890 also shows price-premium exhaustion, but its post-peak depth makes it better treated as 4C-watch/counterexample.

### 4C
- 011790 and 393890 show the core C14 failure mode: EV material exposure remained narratively plausible, but customer call-off, utilization and margin/revision evidence did not carry the valuation.
- This is not a hard accounting break. It is a demand-to-capacity mismatch: the factory may still exist, but the order flow no longer fills it.

## 6. Raw component score breakdown

```json
{
  "C14_011790_SKC_20230405_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 4
  },
  "C14_361610_SKIET_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_LOCAL_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4C_WATCH": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 24,
    "valuation_rerating_runway": 2,
    "visibility_quality": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C14 guard:
```text
if ev_supply_chain_price_premium and no incremental_calloff_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if ev_demand_slowdown plus utilization_or_inventory_gap:
    route_to_4C_watch = true

if post_peak_drawdown and margin_revision_bridge_fails:
    route_to_counterexample = true
```

Residual errors:
```text
current_profile_error_count = 2
- 011790 / 2023-04-05: copper-foil EV exposure can be over-promoted if utilization and margin/revision evidence are not required after demand slowdown appears.
- 393890 / 2023-07-26: separator price premium can look like a late confirmation, but the following path argues for 4C-watch when call-off and utilization proof is missing.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -45.95, "MAE_30D_pct": -24.68, "MAE_90D_pct": -45.95, "MFE_180D_pct": 10.5, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_361610_SKIET_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_LOCAL_4B", "case_role": "protective_4b_success", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Local 4B was the useful signal after separator/EV-demand optionality was priced; fresh Green should have required utilization, call-off volume and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.08, "entry_date": "2023-07-26", "entry_price": 108600, "evidence_family": "separator_ev_demand_slowdown_price_premium_after_policy_and_material_theme", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_EV_DEMAND_SLOWDOWN_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 58700, "peak_date": "2023-07-26", "peak_price": 120000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C14_361610_SKIET_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["ev_material_or_separator_theme_attention", "battery_cell_supply_chain_price_premium", "demand_slowdown_watch_signal"], "stage3_evidence_fields": ["customer_calloff_or_shipments_required", "utilization_and_inventory_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["ev_supply_chain_price_premium_after_theme_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ev_demand_slowdown", "utilization_or_calloff_shortfall", "margin_revision_break_or_capacity_absorption_gap"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.53, "MAE_30D_pct": -21.58, "MAE_90D_pct": -24.33, "MFE_180D_pct": 5.16, "MFE_30D_pct": 5.16, "MFE_90D_pct": 5.16, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_011790_SKC_20230405_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN", "case_role": "ev_materials_false_green_counterexample", "company_name": "SKC", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Copper-foil EV exposure should not become Green once demand slowdown and utilization/margin gaps appear; it should stay Yellow or 4C-watch until shipment and margin evidence recover.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.4, "entry_date": "2023-04-05", "entry_price": 116300, "evidence_family": "copperfoil_ev_demand_slowdown_without_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_EV_DEMAND_SLOWDOWN_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-23", "low_price_180d": 68000, "peak_date": "2023-04-05", "peak_price": 122300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C14_011790_SKC_20230405_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["ev_material_or_separator_theme_attention", "battery_cell_supply_chain_price_premium", "demand_slowdown_watch_signal"], "stage3_evidence_fields": ["customer_calloff_or_shipments_required", "utilization_and_inventory_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["ev_supply_chain_price_premium_after_theme_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ev_demand_slowdown", "utilization_or_calloff_shortfall", "margin_revision_break_or_capacity_absorption_gap"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "trigger_date": "2023-04-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -17.57, "MAE_90D_pct": -49.41, "MFE_180D_pct": 15.59, "MFE_30D_pct": 15.59, "MFE_90D_pct": 15.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4C_WATCH", "case_role": "separator_demand_slowdown_4c_watch_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Separator price premium should route to 4C-watch when customer demand/call-off and utilization evidence do not support the valuation already paid.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.74, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_customer_demand_slowdown_price_premium_without_calloff_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_EV_DEMAND_SLOWDOWN_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-07-26", "peak_price": 87500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 24, "valuation_rerating_runway": 2, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["ev_material_or_separator_theme_attention", "battery_cell_supply_chain_price_premium", "demand_slowdown_watch_signal"], "stage3_evidence_fields": ["customer_calloff_or_shipments_required", "utilization_and_inventory_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["ev_supply_chain_price_premium_after_theme_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ev_demand_slowdown", "utilization_or_calloff_shortfall", "margin_revision_break_or_capacity_absorption_gap"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage4C-Watch", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_COPPERFOIL_EV_DEMAND_SLOWDOWN_UTILIZATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "ev_demand_slowdown_separator_copperfoil_4b_4c_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C14 EV-demand-slowdown rows should route separator/copper-foil price premiums to local 4B or 4C-watch unless customer call-off, utilization, inventory quality, margin and revision bridge recover; price premium after battery-theme heat should block fresh Green.",
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
3. Add C14-specific EV-demand-slowdown / utilization / call-off / inventory-margin guard only as a shadow candidate until more rows exist.

Candidate rule:
- C14_GREEN_BLOCK_AFTER_EV_DEMAND_SLOWDOWN_WITHOUT_CALLOFF_UTILIZATION
- C14_SEPARATOR_COPPERFOIL_PRICE_PREMIUM_LOCAL_4B
- C14_UTILIZATION_OR_INVENTORY_GAP_4C_WATCH
- C14_POST_PEAK_MARGIN_REVISION_FAILURE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

