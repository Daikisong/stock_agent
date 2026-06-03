# E2R Stock-Web v12 Residual Research — R9 Loop 83 / L3 / C29

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 83,
  "computed_next_round": "R10",
  "computed_next_loop": 83,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_volume_margin_operating_leverage_guardrail",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R9
scheduled_loop = 83
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R9 is routed to C29 because this run is about mobility / transport / logistics operating leverage, not construction or PF balance-sheet stress.

The tested economic mechanism:

```text
traffic / shipment / capacity recovery
→ load factor or volume utilization
→ yield, fuel, FX, lease/debt and cost bridge
→ margin conversion
→ durable operating leverage or 4B/false-positive fade
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 is already thickly covered and top-covered names include `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that top-covered set and uses:

```text
086280 / 현대글로비스
091810 / 티웨이항공
089590 / 제주항공
```

All three are treated as new independent C29 cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 086280 | 현대글로비스 | `atlas/symbol_profiles/086/086280.json` | 2024-07-12 and 2024-08-02 CA candidates; entry selected after these dates |
| 091810 | 티웨이항공 | `atlas/symbol_profiles/091/091810.json` | 2025-09-15 and 2026-01-13 CA candidates are after selected 180D test window |
| 089590 | 제주항공 | `atlas/symbol_profiles/089/089590.json` | profile CA candidates are old 2020~2022 windows; selected 2024 window treated clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R9L83-C29-01 | 086280 | 2024-08-26 | 115,500 | 180D | post-CA clean forward window | true |
| R9L83-C29-02 | 091810 | 2024-07-01 | 2,725 | 180D | clean before 2025 CA candidate | true |
| R9L83-C29-03 | 089590 | 2024-01-09 | 13,070 | 180D | clean after old CA candidates | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | LOGISTICS_VOLUME_CONTRACT_MIX_MARGIN_BRIDGE | keep Stage2 when volume/yield/contract mix converts into margin |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | LCC_CAPACITY_LOAD_FACTOR_HIGH_MAE_RISKWATCH | allow Stage2 only with high-MAE riskwatch and local 4B if cost bridge is weak |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AIR_TRAFFIC_THEME_FALSE_POSITIVE | reject traffic-only rerating if yield/fuel/FX/cost bridge is absent |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R9L83-C29-01 | 086280 | 현대글로비스 | Stage2-Actionable | 2024-08-26 | 115,500 | 30.74 | -9.09 | current_profile_partially_correct_4B_watch_needed |
| R9L83-C29-02 | 091810 | 티웨이항공 | Stage2-Actionable | 2024-07-01 | 2,725 | 65.14 | -22.94 | current_profile_4B_too_late_high_MAE |
| R9L83-C29-03 | 089590 | 제주항공 | Stage2-FalsePositive | 2024-01-09 | 13,070 | 3.98 | -36.5 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C29 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: transport volume, airline traffic, yield, load factor, fuel/FX, lease/debt, logistics contract mix, margin bridge, report or disclosure evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 086280 | `atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv` and `2025.csv` | `atlas/symbol_profiles/086/086280.json` |
| 091810 | `atlas/ohlcv_tradable_by_symbol_year/091/091810/2024.csv` and `2025.csv` | `atlas/symbol_profiles/091/091810.json` |
| 089590 | `atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv` | `atlas/symbol_profiles/089/089590.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 086280 / 현대글로비스

C29 positive after separating the post-2024 corporate-action window. The price path shows controlled upside and later peak formation. The key repair question is whether logistics/shipment volume and contract mix actually converted into margin, not whether the stock moved after a split.

### Case 2 — 091810 / 티웨이항공

C29 positive but high-MAE/high-volatility. Capacity and route expansion can produce strong MFE, but airline operating leverage is a thin bridge. Fuel, FX, lease/debt, load factor and yield must be visible before Stage3. A local 4B watch should appear when the MFE outruns those non-price confirmations.

### Case 3 — 089590 / 제주항공

C29 false-positive traffic recovery case. Passenger traffic and reopening-style narratives do not automatically create margin rerating. The OHLC path shows small MFE and large MAE, which argues for demotion unless a yield/cost bridge is proven.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 086280 | 115,500 | 8.74 | -8.05 | 17.92 | -8.05 | 30.74 | -9.09 | 2025-01-31 / 151,000 | -30.46 |
| 091810 | 2,725 | 10.46 | -15.41 | 22.02 | -15.41 | 65.14 | -22.94 | 2025-01-31 / 4,500 | -56.00 |
| 089590 | 13,070 | 3.98 | -14.92 | 3.98 | -19.05 | 3.98 | -36.50 | 2024-01-18 / 13,590 | -38.93 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R9L83-C29-01 | Stage2-Actionable if volume/margin bridge exists | positive MFE, moderate MAE, later drawdown | partially correct; 4B watch needed |
| R9L83-C29-02 | Stage2-Actionable if capacity/traffic route is over-credited | high MFE but high MAE and later drawdown | 4B too late / high-MAE risk |
| R9L83-C29-03 | risk of treating traffic recovery as Stage2 | low MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C29, the residual is not Green lateness. The residual is whether traffic/volume/capacity headlines are allowed to become Stage2-Actionable before yield, cost and margin bridge is proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R9L83-C29-01 | 0.82 | 0.76 | local 4B watch after volume/margin rerating matures |
| R9L83-C29-02 | 0.82 | 0.76 | local 4B required when capacity-theme MFE outruns yield/cost bridge |
| R9L83-C29-03 | 0.20 | 0.20 | traffic theme rejected without yield/cost/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = mobility/transport rows need yield/cost/load-factor/contract-mix bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
candidate_axis = C29_volume_yield_cost_margin_bridge_required
effect = keep bridge-positive logistics/airline cases, demote traffic-only false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.64 | -14.17 | may over-credit traffic/capacity theme | needs C29 bridge repair |
| P1 canonical shadow bridge profile | 3 | 19.97 on kept positives | -11.73 on kept positives | demotes 089590 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R9L83-C29-01 | 80 | Stage2-Actionable | 82 | Stage2-Actionable + local 4B watch | aligned |
| R9L83-C29-02 | 72 | Stage2-Actionable | 70 | Stage2-Actionable + high-MAE RiskWatch | partially aligned |
| R9L83-C29-03 | 58 | Stage2-Watch/FalsePositive | 51 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE | 2 | 1 | 2 | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - traffic_theme_false_positive_high_MAE
  - 4B_too_late_after_capacity_theme_MFE
  - yield_fuel_FX_cost_margin_bridge_required
new_axis_proposed: false
existing_axis_strengthened: C29_volume_yield_cost_margin_bridge_required
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C29_volume_yield_cost_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- airline traffic source
- load factor / yield / fuel / FX bridge
- lease/debt and refinancing detail
- logistics contract mix and margin bridge
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_volume_yield_cost_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require volume/capacity recovery to convert into yield/cost/load-factor/contract-mix/margin bridge before Stage2-Actionable","keeps 086280; keeps 091810 with 4B/high-MAE riskwatch; demotes 089590","R9L83-C29-01-S2A-20240826|R9L83-C29-02-S2A-20240701|R9L83-C29-03-S2FP-20240109",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R9L83-C29-01", "symbol": "086280", "company_name": "현대글로비스", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE", "case_type": "logistics_volume_margin_positive_post_CA_clean_window", "positive_or_counterexample": "positive", "best_trigger": "R9L83-C29-01-S2A-20240826", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_lifecycle_with_later_4B_watch", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Logistics rerating is valid only when volume, yield, contract mix and margin bridge are visible; post-CA price window is separated."}
{"row_type": "trigger", "trigger_id": "R9L83-C29-01-S2A-20240826", "case_id": "R9L83-C29-01", "symbol": "086280", "company_name": "현대글로비스", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-26", "evidence_available_at_that_date": "logistics/PCC volume and margin leverage proxy after post-split clean entry; contract/yield bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_capacity_recovery", "yield_cost_margin_bridge_proxy"], "stage3_evidence_fields": ["load_factor", "yield", "fuel_FX_cost_bridge", "contract_mix", "debt_lease_risk_control"], "stage4b_evidence_fields": ["valuation_blowoff", "capacity_theme_overheat", "yield_cost_bridge_gap"], "stage4c_evidence_fields": ["hard_safety_or_solvent_thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv", "profile_path": "atlas/symbol_profiles/086/086280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-26", "entry_price": 115500, "MFE_30D_pct": 8.74, "MFE_90D_pct": 17.92, "MFE_180D_pct": 30.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.05, "MAE_90D_pct": -8.05, "MAE_180D_pct": -9.09, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-31", "peak_price": 151000, "drawdown_after_peak_pct": -30.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.76, "four_b_timing_verdict": "local_4B_watch_after_volume_margin_rerating_matures", "four_b_evidence_type": ["valuation_blowoff", "yield_cost_bridge_gap", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_lifecycle_with_later_4B_watch", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024_split_clean_forward_window", "same_entry_group_id": "R9L83-C29-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L83-C29-01", "trigger_id": "R9L83-C29-01-S2A-20240826", "symbol": "086280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_safety_risk_score": 15, "debt_or_lease_risk_score": 20, "volume_yield_bridge_score": 45, "fuel_fx_cost_bridge_score": 35, "operating_leverage_score": 50}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_safety_risk_score": 15, "debt_or_lease_risk_score": 20, "volume_yield_bridge_score": 45, "fuel_fx_cost_bridge_score": 35, "operating_leverage_score": 55}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["volume_yield_bridge_score", "fuel_fx_cost_bridge_score", "execution_risk_score", "operating_leverage_score"], "component_delta_explanation": "C29 requires volume/capacity recovery to convert into yield, cost, load-factor and margin bridge; traffic theme alone is demoted.", "MFE_90D_pct": 17.92, "MAE_90D_pct": -8.05, "score_return_alignment_label": "positive_lifecycle_with_later_4B_watch", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed"}
{"row_type": "case", "case_id": "R9L83-C29-02", "symbol": "091810", "company_name": "티웨이항공", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE", "case_type": "LCC_capacity_volume_positive_but_high_MAE_risk", "positive_or_counterexample": "positive", "best_trigger": "R9L83-C29-02-S2A-20240701", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MFE_high_MAE_positive_requires_4B_and_riskwatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Airline volume is not enough; yield, fuel, FX, lease/debt and load-factor bridge must convert before Green."}
{"row_type": "trigger", "trigger_id": "R9L83-C29-02-S2A-20240701", "case_id": "R9L83-C29-02", "symbol": "091810", "company_name": "티웨이항공", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-01", "evidence_available_at_that_date": "LCC capacity/traffic recovery and medium-haul expansion proxy; yield/fuel/FX/capital structure bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_capacity_recovery", "yield_cost_margin_bridge_proxy"], "stage3_evidence_fields": ["load_factor", "yield", "fuel_FX_cost_bridge", "contract_mix", "debt_lease_risk_control"], "stage4b_evidence_fields": ["valuation_blowoff", "capacity_theme_overheat", "yield_cost_bridge_gap"], "stage4c_evidence_fields": ["hard_safety_or_solvent_thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/091/091810/2024.csv", "profile_path": "atlas/symbol_profiles/091/091810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-01", "entry_price": 2725, "MFE_30D_pct": 10.46, "MFE_90D_pct": 22.02, "MFE_180D_pct": 65.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.41, "MAE_90D_pct": -15.41, "MAE_180D_pct": -22.94, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-31", "peak_price": 4500, "drawdown_after_peak_pct": -56.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.76, "four_b_timing_verdict": "local_4B_required_when_capacity_theme_MFE_outruns_yield_cost_bridge", "four_b_evidence_type": ["valuation_blowoff", "yield_cost_bridge_gap", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_MFE_high_MAE_positive_requires_4B_and_riskwatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2025_CA_candidate", "same_entry_group_id": "R9L83-C29-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L83-C29-02", "trigger_id": "R9L83-C29-02-S2A-20240701", "symbol": "091810", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_safety_risk_score": 35, "debt_or_lease_risk_score": 55, "volume_yield_bridge_score": 35, "fuel_fx_cost_bridge_score": 20, "operating_leverage_score": 40}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_safety_risk_score": 35, "debt_or_lease_risk_score": 55, "volume_yield_bridge_score": 35, "fuel_fx_cost_bridge_score": 20, "operating_leverage_score": 45}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["volume_yield_bridge_score", "fuel_fx_cost_bridge_score", "execution_risk_score", "operating_leverage_score"], "component_delta_explanation": "C29 requires volume/capacity recovery to convert into yield, cost, load-factor and margin bridge; traffic theme alone is demoted.", "MFE_90D_pct": 22.02, "MAE_90D_pct": -15.41, "score_return_alignment_label": "high_MFE_high_MAE_positive_requires_4B_and_riskwatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE"}
{"row_type": "case", "case_id": "R9L83-C29-03", "symbol": "089590", "company_name": "제주항공", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE", "case_type": "traffic_recovery_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R9L83-C29-03-S2FP-20240109", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Traffic recovery headline alone should be RiskWatch unless yield, load factor, fuel/FX and cost bridge are proven."}
{"row_type": "trigger", "trigger_id": "R9L83-C29-03-S2FP-20240109", "case_id": "R9L83-C29-03", "symbol": "089590", "company_name": "제주항공", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MOBILITY_LOGISTICS_AIRLINE_VOLUME_YIELD_COST_BRIDGE_VS_TRAFFIC_THEME_MAE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-09", "evidence_available_at_that_date": "air passenger traffic recovery proxy without durable yield / cost / safety-risk / margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_capacity_recovery", "yield_cost_margin_bridge_proxy"], "stage3_evidence_fields": ["load_factor", "yield", "fuel_FX_cost_bridge", "contract_mix", "debt_lease_risk_control"], "stage4b_evidence_fields": ["valuation_blowoff", "capacity_theme_overheat", "yield_cost_bridge_gap"], "stage4c_evidence_fields": ["hard_safety_or_solvent_thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv", "profile_path": "atlas/symbol_profiles/089/089590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-09", "entry_price": 13070, "MFE_30D_pct": 3.98, "MFE_90D_pct": 3.98, "MFE_180D_pct": 3.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.92, "MAE_90D_pct": -19.05, "MAE_180D_pct": -36.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 13590, "drawdown_after_peak_pct": -38.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.2, "four_b_full_window_peak_proximity": 0.2, "four_b_timing_verdict": "traffic_theme_rejected_without_yield_cost_margin_bridge", "four_b_evidence_type": ["valuation_blowoff", "yield_cost_bridge_gap", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_CA_candidates", "same_entry_group_id": "R9L83-C29-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L83-C29-03", "trigger_id": "R9L83-C29-03-S2FP-20240109", "symbol": "089590", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 75, "legal_or_safety_risk_score": 55, "debt_or_lease_risk_score": 55, "volume_yield_bridge_score": 10, "fuel_fx_cost_bridge_score": 5, "operating_leverage_score": 10}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_safety_risk_score": 55, "debt_or_lease_risk_score": 55, "volume_yield_bridge_score": 0, "fuel_fx_cost_bridge_score": 0, "operating_leverage_score": 10}, "weighted_score_after": 51, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["volume_yield_bridge_score", "fuel_fx_cost_bridge_score", "execution_risk_score", "operating_leverage_score"], "component_delta_explanation": "C29 requires volume/capacity recovery to convert into yield, cost, load-factor and margin bridge; traffic theme alone is demoted.", "MFE_90D_pct": 3.98, "MAE_90D_pct": -19.05, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C29_volume_yield_cost_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Mobility/transport rerating requires volume or capacity recovery to convert into yield, cost, load-factor and margin bridge; traffic-only theme fades.", "backtest_effect": "keeps 086280 as positive, keeps 091810 only with 4B/high-MAE riskwatch, rejects 089590 traffic-theme false positive", "trigger_ids": "R9L83-C29-01-S2A-20240826|R9L83-C29-02-S2A-20240701|R9L83-C29-03-S2FP-20240109", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R9", "loop": 83, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["traffic_theme_false_positive_high_MAE", "4B_too_late_after_capacity_theme_MFE", "yield_fuel_FX_cost_margin_bridge_required"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C29, test a canonical-archetype guard requiring volume/capacity recovery to convert into yield, cost, load-factor, contract-mix and margin bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 83
next_round = R10
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
