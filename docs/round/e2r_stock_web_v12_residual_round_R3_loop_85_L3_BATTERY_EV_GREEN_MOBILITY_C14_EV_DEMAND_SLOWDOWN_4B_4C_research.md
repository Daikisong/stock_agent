# E2R Stock-Web v12 Residual Research — R3 Loop 85 / L3 / C14

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 85,
  "computed_next_round": "R4",
  "computed_next_loop": 85,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "EV_demand_slowdown_4B_4C_guardrail",
    "battery_material_rebound_theme_vs_inventory_margin_bridge_test",
    "local_4B_timing_after_material_rebound_MFE",
    "hard_4C_non_price_thesis_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
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
scheduled_round = R3
scheduled_loop = 85
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
computed_next_round = R4
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R3 is the battery / EV / green mobility round. This run selects C14 because loop83 tested C12 and loop84 tested C13. C14 is the demand-slowdown / 4B / 4C guardrail bucket.

The tested mechanism:

```text
battery-material rebound / EV recovery headline
→ customer call-off and inventory normalization
→ utilization and ASP/cost pass-through
→ gross / OP margin recovery
→ true recovery or 4B/4C riskwatch
```

C14 is the brake pedal. A rebound candle is not the same as repaired EV demand.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C14 top-covered symbols include `247540`, `003670`, `066970`, `361610`, `373220`, and `393890`. This run avoids that top-covered set and uses:

```text
121600 / 나노신소재
278280 / 천보
020150 / 롯데에너지머티리얼즈
```

All three are treated as new independent C14 EV-demand slowdown / 4B-4C cases for this loop. No hard duplicate is intentionally reused.

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
| 121600 | 나노신소재 | `atlas/symbol_profiles/121/121600.json` | old 2015 CA candidate; selected 2024 forward window clean |
| 278280 | 천보 | `atlas/symbol_profiles/278/278280.json` | no profile-level CA candidate |
| 020150 | 롯데에너지머티리얼즈 | `atlas/symbol_profiles/020/020150.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R3L85-C14-01 | 121600 | 2024-02-21 | 134,000 | 180D | clean | true |
| R3L85-C14-02 | 278280 | 2024-02-08 | 95,000 | 180D | clean | true |
| R3L85-C14-03 | 020150 | 2024-03-21 | 47,050 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | CNT_REBOUND_MFE_INVENTORY_BRIDGE_FAIL | reject recovery label when CNT material rebound lacks demand/inventory/margin bridge |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | ELECTROLYTE_ADDITIVE_DEMAND_SLOWDOWN | reject electrolyte/additive rebound without call-off, inventory and utilization bridge |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | COPPERFOIL_MARGIN_BRIDGE_BREAK | reject copper-foil recovery without ASP, utilization and OP-margin repair |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R3L85-C14-01 | 121600 | 나노신소재 | Stage2-FalsePositive | 2024-02-21 | 134,000 | 17.76 | -48.88 | current_profile_false_positive_4B_too_late |
| R3L85-C14-02 | 278280 | 천보 | Stage2-FalsePositive | 2024-02-08 | 95,000 | 5.05 | -48.42 | current_profile_false_positive_high_MAE |
| R3L85-C14-03 | 020150 | 롯데에너지머티리얼즈 | Stage2-FalsePositive | 2024-03-21 | 47,050 | 17.53 | -35.18 | current_profile_false_positive_inventory_margin_bridge_break |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 0
counterexample_count = 3
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C14 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: EV demand data, customer call-off, inventory normalization, utilization, ASP/cost pass-through, margin conversion, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 121600 | `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv` | `atlas/symbol_profiles/121/121600.json` |
| 278280 | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv` | `atlas/symbol_profiles/278/278280.json` |
| 020150 | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv` | `atlas/symbol_profiles/020/020150.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 121600 / 나노신소재

C14 battery-material rebound false positive. The February rebound created immediate MFE, but it failed to become durable recovery. The later 180D MAE shows why recovery labels should be blocked unless inventory normalization, customer call-off and margin bridge are repaired.

### Case 2 — 278280 / 천보

C14 electrolyte/additive demand-slowdown false positive. The rebound MFE was small, while the later low printed a large drawdown. This is a clean demotion row for C14.

### Case 3 — 020150 / 롯데에너지머티리얼즈

C14 copper-foil margin-bridge break. The rebound looked better than the other two, but the later margin/demand fade still turned it into a 4B/RiskWatch case rather than clean recovery.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 121600 | 134,000 | 17.76 | -9.48 | 17.76 | -17.09 | 17.76 | -48.88 | 2024-02-22 / 157,800 | -56.59 |
| 278280 | 95,000 | 5.05 | -9.26 | 5.05 | -23.79 | 5.05 | -48.42 | 2024-02-21 / 99,800 | -50.90 |
| 020150 | 47,050 | 11.37 | -5.42 | 17.53 | -21.99 | 17.53 | -35.18 | 2024-07-02 / 55,300 | -44.85 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R3L85-C14-01 | risk of treating battery-material rebound as recovery | MFE then deep MAE | false positive / 4B too late |
| R3L85-C14-02 | risk of treating electrolyte/additive rebound as Stage2 | small MFE / deep MAE | false positive |
| R3L85-C14-03 | risk of treating copper-foil rebound as recovered demand | MFE then margin-bridge fade | false positive / 4B-watch |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = C14 is a 4B/4C demand-slowdown guardrail run, not a Green recovery run
```

For C14, the residual is whether a rebound signal is incorrectly allowed back into Stage2/Green before demand, inventory and margin evidence are repaired.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R3L85-C14-01 | 0.35 | 0.30 | local 4B watch or reject when rebound MFE lacks inventory/margin bridge |
| R3L85-C14-02 | 0.35 | 0.30 | EV additive rebound rejected without call-off/utilization bridge |
| R3L85-C14-03 | 0.35 | 0.30 | copper-foil MFE rejected without ASP/inventory/utilization bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_calloff_inventory_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is insufficient for hard 4C. C14 hard 4C requires confirmed customer call-off collapse, inventory impairment, utilization break, policy/subsidy reversal, or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L3/C14 EV-demand-slowdown rows need customer call-off, inventory normalization, utilization and margin bridge before any recovery label
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
candidate_axis = C14_EV_demand_calloff_inventory_margin_bridge_required_for_recovery
effect = demote rebound-theme false positives; keep hard 4C non-price requirement
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 13.45 | -20.96 | may over-credit EV/battery-material rebound MFE | needs C14 demand/inventory bridge |
| P1 canonical shadow bridge profile | 3 | no kept positives | demotes all three | blocks recovery labels until demand/inventory/margin repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R3L85-C14-01 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / 4B-watch | improved |
| R3L85-C14-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / 4B-watch | improved |
| R3L85-C14-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / 4B-watch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE | 0 | 3 | 3-watch | 0-hard | 3 | 0 | 3 | 3 | no | yes | source repair needed |

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
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - battery_material_rebound_theme_false_positive_high_MAE
  - EV_demand_calloff_inventory_margin_bridge_required
  - local_4B_late_after_rebound_MFE
  - hard_4C_requires_non_price_calloff_inventory_margin_break
  - source_proxy_runtime_promotion_risk
new_axis_proposed: false
existing_axis_strengthened:
  - C14_EV_demand_calloff_inventory_margin_bridge_required_for_recovery
  - source_proxy_only_blocks_runtime_promotion
  - hard_4C_requires_non_price_thesis_break
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C14_EV_demand_calloff_inventory_margin_bridge_required_for_recovery
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent counterexamples for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- EV demand or customer call-off data
- inventory normalization data
- utilization / ASP / cost pass-through
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_EV_demand_calloff_inventory_margin_bridge_required_for_recovery,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Require EV demand, customer call-off, inventory normalization, utilization, ASP/cost pass-through and margin recovery before any recovery label","demotes 121600/278280/020150 rebound-theme false positives; keeps hard 4C non-price requirement","R3L85-C14-01-S2FP-20240221|R3L85-C14-02-S2FP-20240208|R3L85-C14-03-S2FP-20240321",3,3,3,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L85-C14-01", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "case_type": "CNT_battery_material_rebound_theme_4B_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R3L85-C14-01-S2FP-20240221", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "initial_MFE_then_EV_demand_slowdown_high_MAE_4B_watch", "current_profile_verdict": "current_profile_false_positive_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "C14 should demote battery-material rebound MFE unless EV demand, customer call-off, inventory burn and margin bridge are repaired."}
{"row_type": "trigger", "trigger_id": "R3L85-C14-01-S2FP-20240221", "case_id": "R3L85-C14-01", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EV_demand_slowdown_4B_4C_guardrail|battery_material_rebound_theme_vs_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-21", "evidence_available_at_that_date": "CNT/battery-material rebound and EV supply-chain recovery proxy without repaired demand, inventory and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["battery_material_rebound_proxy", "EV_demand_recovery_proxy"], "stage3_evidence_fields": ["customer_calloff", "inventory_normalization", "utilization", "ASP_or_price_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["rebound_MFE_without_demand_bridge", "inventory_margin_bridge_stalls", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_or_inventory_impairment_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-21", "entry_price": 134000, "MFE_30D_pct": 17.76, "MFE_90D_pct": 17.76, "MFE_180D_pct": 17.76, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.48, "MAE_90D_pct": -17.09, "MAE_180D_pct": -48.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 157800, "drawdown_after_peak_pct": -56.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "local_4B_watch_or_reject_when_battery_material_rebound_MFE_lacks_inventory_margin_bridge", "four_b_evidence_type": ["EV_rebound_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_calloff_inventory_or_margin_break", "trigger_outcome_label": "initial_MFE_then_EV_demand_slowdown_high_MAE_4B_watch", "current_profile_verdict": "current_profile_false_positive_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2015_CA_candidate", "same_entry_group_id": "R3L85-C14-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L85-C14-01", "trigger_id": "R3L85-C14-01-S2FP-20240221", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"EV_demand_visibility_score": 20, "customer_calloff_score": 5, "inventory_normalization_score": 5, "utilization_score": 10, "ASP_or_price_pass_through_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 40, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"EV_demand_visibility_score": 0, "customer_calloff_score": 0, "inventory_normalization_score": 0, "utilization_score": 0, "ASP_or_price_pass_through_score": 10, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 40, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 70}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / 4B-watch; 4C-watch only after non-price break", "changed_components": ["EV_demand_visibility_score", "customer_calloff_score", "inventory_normalization_score", "utilization_score", "margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C14 requires EV demand, customer call-off, inventory normalization, utilization and margin bridge before any recovery label; price rebound alone is demoted to 4B/RiskWatch, and hard 4C still requires non-price thesis break.", "MFE_90D_pct": 17.76, "MAE_90D_pct": -17.09, "score_return_alignment_label": "initial_MFE_then_EV_demand_slowdown_high_MAE_4B_watch", "current_profile_verdict": "current_profile_false_positive_4B_too_late"}
{"row_type": "case", "case_id": "R3L85-C14-02", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "case_type": "electrolyte_additive_rebound_theme_demand_slowdown_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R3L85-C14-02-S2FP-20240208", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "small_MFE_then_large_MAE_EV_slowdown_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Electrolyte/additive rebound theme should stay RiskWatch unless customer demand, inventory normalization, utilization and gross-margin bridge are visible."}
{"row_type": "trigger", "trigger_id": "R3L85-C14-02-S2FP-20240208", "case_id": "R3L85-C14-02", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EV_demand_slowdown_4B_4C_guardrail|battery_material_rebound_theme_vs_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-08", "evidence_available_at_that_date": "electrolyte/additive demand recovery and customer restocking proxy without confirmed inventory normalization and utilization bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["battery_material_rebound_proxy", "EV_demand_recovery_proxy"], "stage3_evidence_fields": ["customer_calloff", "inventory_normalization", "utilization", "ASP_or_price_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["rebound_MFE_without_demand_bridge", "inventory_margin_bridge_stalls", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_or_inventory_impairment_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 95000, "MFE_30D_pct": 5.05, "MFE_90D_pct": 5.05, "MFE_180D_pct": 5.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.26, "MAE_90D_pct": -23.79, "MAE_180D_pct": -48.42, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 99800, "drawdown_after_peak_pct": -50.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "EV_additive_rebound_rejected_without_customer_inventory_utilization_margin_bridge", "four_b_evidence_type": ["EV_rebound_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_calloff_inventory_or_margin_break", "trigger_outcome_label": "small_MFE_then_large_MAE_EV_slowdown_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R3L85-C14-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L85-C14-02", "trigger_id": "R3L85-C14-02-S2FP-20240208", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"EV_demand_visibility_score": 10, "customer_calloff_score": 5, "inventory_normalization_score": 5, "utilization_score": 10, "ASP_or_price_pass_through_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"EV_demand_visibility_score": 0, "customer_calloff_score": 0, "inventory_normalization_score": 0, "utilization_score": 0, "ASP_or_price_pass_through_score": 10, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 70}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / 4B-watch; 4C-watch only after non-price break", "changed_components": ["EV_demand_visibility_score", "customer_calloff_score", "inventory_normalization_score", "utilization_score", "margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C14 requires EV demand, customer call-off, inventory normalization, utilization and margin bridge before any recovery label; price rebound alone is demoted to 4B/RiskWatch, and hard 4C still requires non-price thesis break.", "MFE_90D_pct": 5.05, "MAE_90D_pct": -23.79, "score_return_alignment_label": "small_MFE_then_large_MAE_EV_slowdown_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R3L85-C14-03", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "case_type": "copperfoil_EV_material_margin_bridge_break", "positive_or_counterexample": "counterexample", "best_trigger": "R3L85-C14-03-S2FP-20240321", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "rebound_MFE_then_demand_slowdown_margin_bridge_break", "current_profile_verdict": "current_profile_false_positive_inventory_margin_bridge_break", "price_source": "Songdaiki/stock-web", "notes": "Copper-foil rebound is not C14 recovery evidence unless ASP, inventory, utilization, customer call-off and OP-margin bridge repair."}
{"row_type": "trigger", "trigger_id": "R3L85-C14-03-S2FP-20240321", "case_id": "R3L85-C14-03", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EV_demand_slowdown_4B_4C_guardrail|battery_material_rebound_theme_vs_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-21", "evidence_available_at_that_date": "copper foil / battery material rebound and utilization recovery proxy without confirmed ASP, inventory and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["battery_material_rebound_proxy", "EV_demand_recovery_proxy"], "stage3_evidence_fields": ["customer_calloff", "inventory_normalization", "utilization", "ASP_or_price_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["rebound_MFE_without_demand_bridge", "inventory_margin_bridge_stalls", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_or_inventory_impairment_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-21", "entry_price": 47050, "MFE_30D_pct": 11.37, "MFE_90D_pct": 17.53, "MFE_180D_pct": 17.53, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.42, "MAE_90D_pct": -21.99, "MAE_180D_pct": -35.18, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-02", "peak_price": 55300, "drawdown_after_peak_pct": -44.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "copperfoil_material_MFE_rejected_without_ASP_inventory_utilization_margin_bridge", "four_b_evidence_type": ["EV_rebound_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_calloff_inventory_or_margin_break", "trigger_outcome_label": "rebound_MFE_then_demand_slowdown_margin_bridge_break", "current_profile_verdict": "current_profile_false_positive_inventory_margin_bridge_break", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R3L85-C14-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L85-C14-03", "trigger_id": "R3L85-C14-03-S2FP-20240321", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"EV_demand_visibility_score": 10, "customer_calloff_score": 5, "inventory_normalization_score": 5, "utilization_score": 10, "ASP_or_price_pass_through_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"EV_demand_visibility_score": 0, "customer_calloff_score": 0, "inventory_normalization_score": 0, "utilization_score": 0, "ASP_or_price_pass_through_score": 10, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 70}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / 4B-watch; 4C-watch only after non-price break", "changed_components": ["EV_demand_visibility_score", "customer_calloff_score", "inventory_normalization_score", "utilization_score", "margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C14 requires EV demand, customer call-off, inventory normalization, utilization and margin bridge before any recovery label; price rebound alone is demoted to 4B/RiskWatch, and hard 4C still requires non-price thesis break.", "MFE_90D_pct": 17.53, "MAE_90D_pct": -21.99, "score_return_alignment_label": "rebound_MFE_then_demand_slowdown_margin_bridge_break", "current_profile_verdict": "current_profile_false_positive_inventory_margin_bridge_break"}
{"row_type": "shadow_weight", "axis": "C14_EV_demand_calloff_inventory_margin_bridge_required_for_recovery", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "EV/battery-material rebound requires customer call-off, inventory normalization, utilization, ASP/cost pass-through and margin recovery; rebound MFE without bridge should route to 4B-watch or rejected Stage2, while hard 4C requires non-price break.", "backtest_effect": "demotes 121600/278280/020150 rebound-theme false positives and reinforces local 4B plus hard-4C non-price guard", "trigger_ids": "R3L85-C14-01-S2FP-20240221|R3L85-C14-02-S2FP-20240208|R3L85-C14-03-S2FP-20240321", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 3, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R3", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["battery_material_rebound_theme_false_positive_high_MAE", "EV_demand_calloff_inventory_margin_bridge_required", "local_4B_late_after_rebound_MFE", "hard_4C_requires_non_price_calloff_inventory_margin_break", "source_proxy_runtime_promotion_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C14, test a canonical-archetype guard requiring EV demand, customer call-off, inventory normalization, utilization and margin bridge before any recovery label. Keep hard 4C blocked unless a non-price thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 85
next_round = R4
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
