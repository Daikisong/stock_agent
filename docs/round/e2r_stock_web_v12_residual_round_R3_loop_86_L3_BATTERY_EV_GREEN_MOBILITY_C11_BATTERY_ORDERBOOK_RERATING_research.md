# E2R Stock-Web v12 Residual Research — R3 Loop 86 / L3 / C11

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 86,
  "computed_next_round": "R4",
  "computed_next_loop": 86,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "battery_orderbook_rerating_guardrail",
    "cell_cathode_orderbook_to_customer_calloff_margin_bridge_test",
    "speculative_battery_theme_blowoff_vs_orderbook_economics_bridge_test",
    "local_4B_timing_after_battery_orderbook_MFE",
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
scheduled_loop = 86
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
computed_next_round = R4
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R3 is the battery / EV / green mobility round. This run selects C11 because loop83 tested C12, loop84 tested C13, and loop85 tested C14. C11 is the remaining battery orderbook rerating axis for this rotation.

The tested mechanism:

```text
battery cell / cathode / speculative orderbook headline
→ confirmed customer orderbook
→ customer call-off cadence
→ capacity utilization
→ ASP or raw-material cost spread
→ revenue and gross/OP margin bridge
→ durable rerating or speculative battery theme fade
```

C11 is not the press release. It is the loading dock: the model needs orderbook, call-off, utilization and margin moving together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C11 top-covered symbols include `247540`, `003670`, `393890`, `222080`, `348370`, and `066970`. This run avoids that top-covered set and uses:

```text
006400 / 삼성SDI
005070 / 코스모신소재
001570 / 금양
```

All three are treated as new independent C11 battery-orderbook rerating cases for this loop. No hard duplicate is intentionally reused.

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
| 006400 | 삼성SDI | `atlas/symbol_profiles/006/006400.json` | old 2014 CA candidate; selected 2024 forward window clean |
| 005070 | 코스모신소재 | `atlas/symbol_profiles/005/005070.json` | old 2019 CA candidate; selected 2024 forward window clean |
| 001570 | 금양 | `atlas/symbol_profiles/001/001570.json` | old 2007 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R3L86-C11-01 | 006400 | 2024-02-13 | 391,000 | 180D | clean | true |
| R3L86-C11-02 | 005070 | 2024-02-13 | 157,100 | 180D | clean | true |
| R3L86-C11-03 | 001570 | 2024-02-13 | 82,900 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C11_BATTERY_ORDERBOOK_RERATING | CELL_ORDERBOOK_CUSTOMER_CALLOFF_MARGIN | keep Stage2 with customer orderbook, call-off, utilization and margin bridge; local 4B after MFE |
| C11_BATTERY_ORDERBOOK_RERATING | CATHODE_CUSTOMER_ORDERBOOK_HIGH_MAE_WATCH | keep Stage2 only with high-MAE/orderbook-calloff RiskWatch until source repair |
| C11_BATTERY_ORDERBOOK_RERATING | SPECULATIVE_BATTERY_THEME_BLOWOFF | reject speculative battery optionality without customer call-off, revenue and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R3L86-C11-01 | 006400 | 삼성SDI | Stage2-Actionable | 2024-02-13 | 391,000 | 26.47 | -24.68 | current_profile_partially_correct_local_4B_high_MAE_watch_needed |
| R3L86-C11-02 | 005070 | 코스모신소재 | Stage2-Actionable | 2024-02-13 | 157,100 | 23.68 | -38.57 | current_profile_partially_correct_high_MAE_watch_needed |
| R3L86-C11-03 | 001570 | 금양 | Stage2-FalsePositive | 2024-02-13 | 82,900 | 61.76 | -51.57 | current_profile_false_positive_theme_blowoff_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C11 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: customer orderbook, customer call-off schedule, supply agreement, capacity utilization, ASP/raw-material spread, revenue conversion, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 006400 | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` | `atlas/symbol_profiles/006/006400.json` |
| 005070 | `atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv` | `atlas/symbol_profiles/005/005070.json` |
| 001570 | `atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv` | `atlas/symbol_profiles/001/001570.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 006400 / 삼성SDI

C11 battery cell orderbook recovery positive with local 4B watch. The February entry produced a strong MFE into late March, but the later 180D drawdown shows that clean Green requires customer call-off, utilization and margin evidence.

### Case 2 — 005070 / 코스모신소재

C11 cathode material orderbook positive with high-MAE watch. The MFE arrived quickly, but the later MAE was deep. This should stay Stage2-Actionable only with source-repaired customer orderbook and margin bridge.

### Case 3 — 001570 / 금양

C11 speculative battery theme blowoff counterexample. The MFE was very large, but this is precisely the trap: without customer call-off, revenue and margin bridge, speculative orderbook optionality should not be validated as clean Stage2.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 006400 | 391,000 | 26.47 | -7.16 | 26.47 | -7.16 | 26.47 | -24.68 | 2024-03-25 / 494,500 | -40.44 |
| 005070 | 157,100 | 23.68 | -1.85 | 23.68 | -9.10 | 23.68 | -38.57 | 2024-02-21 / 194,300 | -50.33 |
| 001570 | 82,900 | 61.76 | -4.70 | 61.76 | -4.70 | 61.76 | -51.57 | 2024-03-06 / 134,100 | -70.06 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R3L86-C11-01 | Stage2-Actionable if customer/orderbook bridge exists | strong MFE, later drawdown | partially correct; local 4B/orderbook-calloff watch needed |
| R3L86-C11-02 | Stage2-Actionable if cathode orderbook is over-credited | fast MFE, later deep MAE | high-MAE watch needed |
| R3L86-C11-03 | risk of treating speculative battery optionality as Stage2 | large MFE then severe collapse | false positive / theme blowoff |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C11, the residual is whether battery-orderbook MFE becomes clean Stage2/Green before customer call-off, utilization, ASP/cost spread and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R3L86-C11-01 | 0.78 | 0.68 | local 4B watch after cell-orderbook MFE if call-off/utilization/margin bridge stalls |
| R3L86-C11-02 | 0.78 | 0.68 | local 4B and high-MAE watch when cathode MFE outruns orderbook/margin bridge |
| R3L86-C11-03 | 0.90 | 0.80 | speculative battery MFE rejected or local-4B-watch without orderbook/revenue bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_customer_calloff_or_orderbook_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C11 hard 4C requires confirmed customer call-off loss, order cancellation, utilization collapse, ASP/cost-spread break, or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L3/C11 rows need customer orderbook, call-off cadence, capacity utilization, ASP/raw-material spread and revenue/margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
candidate_axis = C11_battery_orderbook_customer_calloff_utilization_margin_bridge_required
effect = keep orderbook positives with local 4B/high-MAE watch; demote speculative theme blowoffs
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 37.30 | -6.99 | may over-credit battery orderbook/speculative MFE | needs C11 call-off/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 25.08 on kept positives | -8.13 on kept positives, but high-MAE watch at 180D | demotes 001570 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R3L86-C11-01 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + local 4B/orderbook-calloff watch | partially aligned |
| R3L86-C11-02 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + local 4B/orderbook-calloff watch | partially aligned |
| R3L86-C11-03 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Speculative battery theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - speculative_battery_theme_false_positive_high_MAE
  - battery_orderbook_customer_calloff_utilization_margin_bridge_required
  - local_4B_late_after_battery_orderbook_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C11_battery_orderbook_customer_calloff_utilization_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C11_battery_orderbook_customer_calloff_utilization_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

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
- customer orderbook or call-off data
- capacity utilization and shipment conversion
- ASP / raw-material cost spread
- revenue and gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_battery_orderbook_customer_calloff_utilization_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Require confirmed customer orderbook, customer call-off, capacity utilization, ASP/cost spread and revenue/margin conversion before clean Stage2/Green","keeps 006400/005070 with local 4B or high-MAE watch; demotes 001570","R3L86-C11-01-S2A-20240213|R3L86-C11-02-S2A-20240213|R3L86-C11-03-S2FP-20240213",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L86-C11-01", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "case_type": "battery_cell_orderbook_recovery_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L86-C11-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "battery_cell_MFE_positive_but_orderbook_calloff_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C11 cell-orderbook positives need customer call-off, capacity utilization, ASP/cost spread and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R3L86-C11-01-S2A-20240213", "case_id": "R3L86-C11-01", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_rerating_guardrail|orderbook_to_calloff_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "battery cell orderbook / EV demand stabilization / premium-cell capacity and margin recovery proxy; primary call-off and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["battery_orderbook_proxy", "customer_demand_proxy", "capacity_or_margin_recovery_proxy"], "stage3_evidence_fields": ["confirmed_customer_orderbook", "customer_calloff", "capacity_utilization", "ASP_or_cost_spread", "revenue_and_margin_conversion"], "stage4b_evidence_fields": ["battery_orderbook_MFE_without_calloff_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_loss_or_order_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 391000, "MFE_30D_pct": 26.47, "MFE_90D_pct": 26.47, "MFE_180D_pct": 26.47, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.16, "MAE_90D_pct": -7.16, "MAE_180D_pct": -24.68, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 494500, "drawdown_after_peak_pct": -40.44, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "local_4B_watch_after_cell_orderbook_MFE_if_calloff_utilization_margin_bridge_stalls", "four_b_evidence_type": ["battery_orderbook_MFE_without_calloff_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_customer_calloff_or_orderbook_break", "trigger_outcome_label": "battery_cell_MFE_positive_but_orderbook_calloff_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2014_CA_candidate", "same_entry_group_id": "R3L86-C11-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L86-C11-01", "trigger_id": "R3L86-C11-01-S2A-20240213", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"orderbook_visibility_score": 50, "customer_calloff_score": 40, "capacity_utilization_score": 40, "ASP_or_cost_spread_score": 35, "revenue_bridge_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 65, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"orderbook_visibility_score": 50, "customer_calloff_score": 40, "capacity_utilization_score": 40, "ASP_or_cost_spread_score": 35, "revenue_bridge_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 75, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/orderbook-calloff watch", "changed_components": ["orderbook_visibility_score", "customer_calloff_score", "capacity_utilization_score", "ASP_or_cost_spread_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C11 requires battery orderbook signal to convert into customer call-off, utilization, ASP/cost spread, revenue and margin bridge before clean Stage2/Green; speculative battery MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 26.47, "MAE_90D_pct": -7.16, "score_return_alignment_label": "battery_cell_MFE_positive_but_orderbook_calloff_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R3L86-C11-02", "symbol": "005070", "company_name": "코스모신소재", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "case_type": "cathode_material_orderbook_recovery_positive_with_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L86-C11-02-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "cathode_MFE_positive_but_later_high_MAE_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C11 cathode-material positives need customer orderbook, call-off cadence, utilization and ASP/raw-material spread margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R3L86-C11-02-S2A-20240213", "case_id": "R3L86-C11-02", "symbol": "005070", "company_name": "코스모신소재", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_rerating_guardrail|orderbook_to_calloff_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "cathode material orderbook / customer demand recovery / precursor spread and margin recovery proxy; primary contract and utilization evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["battery_orderbook_proxy", "customer_demand_proxy", "capacity_or_margin_recovery_proxy"], "stage3_evidence_fields": ["confirmed_customer_orderbook", "customer_calloff", "capacity_utilization", "ASP_or_cost_spread", "revenue_and_margin_conversion"], "stage4b_evidence_fields": ["battery_orderbook_MFE_without_calloff_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_loss_or_order_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv", "profile_path": "atlas/symbol_profiles/005/005070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 157100, "MFE_30D_pct": 23.68, "MFE_90D_pct": 23.68, "MFE_180D_pct": 23.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.85, "MAE_90D_pct": -9.1, "MAE_180D_pct": -38.57, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 194300, "drawdown_after_peak_pct": -50.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "local_4B_and_high_MAE_watch_when_cathode_MFE_outruns_contract_utilization_margin_bridge", "four_b_evidence_type": ["battery_orderbook_MFE_without_calloff_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_customer_calloff_or_orderbook_break", "trigger_outcome_label": "cathode_MFE_positive_but_later_high_MAE_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2019_CA_candidate", "same_entry_group_id": "R3L86-C11-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L86-C11-02", "trigger_id": "R3L86-C11-02-S2A-20240213", "symbol": "005070", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"orderbook_visibility_score": 50, "customer_calloff_score": 40, "capacity_utilization_score": 40, "ASP_or_cost_spread_score": 35, "revenue_bridge_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 65, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"orderbook_visibility_score": 50, "customer_calloff_score": 40, "capacity_utilization_score": 40, "ASP_or_cost_spread_score": 35, "revenue_bridge_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 75, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/orderbook-calloff watch", "changed_components": ["orderbook_visibility_score", "customer_calloff_score", "capacity_utilization_score", "ASP_or_cost_spread_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C11 requires battery orderbook signal to convert into customer call-off, utilization, ASP/cost spread, revenue and margin bridge before clean Stage2/Green; speculative battery MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 23.68, "MAE_90D_pct": -9.1, "score_return_alignment_label": "cathode_MFE_positive_but_later_high_MAE_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R3L86-C11-03", "symbol": "001570", "company_name": "금양", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "case_type": "speculative_battery_theme_blowoff_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L86-C11-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_theme_MFE_then_deep_MAE_speculative_battery_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Speculative battery optionality should not validate C11 unless customer orderbook, shipment/call-off, revenue and margin conversion are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R3L86-C11-03-S2FP-20240213", "case_id": "R3L86-C11-03", "symbol": "001570", "company_name": "금양", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_rerating_guardrail|orderbook_to_calloff_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "speculative battery-cell / lithium / orderbook optionality theme proxy without confirmed customer call-off, revenue and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["battery_orderbook_proxy", "customer_demand_proxy", "capacity_or_margin_recovery_proxy"], "stage3_evidence_fields": ["confirmed_customer_orderbook", "customer_calloff", "capacity_utilization", "ASP_or_cost_spread", "revenue_and_margin_conversion"], "stage4b_evidence_fields": ["battery_orderbook_MFE_without_calloff_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_loss_or_order_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv", "profile_path": "atlas/symbol_profiles/001/001570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 82900, "MFE_30D_pct": 61.76, "MFE_90D_pct": 61.76, "MFE_180D_pct": 61.76, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.7, "MAE_90D_pct": -4.7, "MAE_180D_pct": -51.57, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 134100, "drawdown_after_peak_pct": -70.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "speculative_battery_theme_MFE_rejected_or_local_4B_watch_without_customer_orderbook_revenue_margin_bridge", "four_b_evidence_type": ["battery_orderbook_MFE_without_calloff_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_customer_calloff_or_orderbook_break", "trigger_outcome_label": "large_theme_MFE_then_deep_MAE_speculative_battery_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2007_CA_candidate", "same_entry_group_id": "R3L86-C11-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L86-C11-03", "trigger_id": "R3L86-C11-03-S2FP-20240213", "symbol": "001570", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"orderbook_visibility_score": 15, "customer_calloff_score": 5, "capacity_utilization_score": 5, "ASP_or_cost_spread_score": 5, "revenue_bridge_score": 5, "gross_margin_bridge_score": 5, "customer_quality_score": 10, "revision_score": 15, "relative_strength_score": 65, "valuation_blowoff_risk_score": 90, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"orderbook_visibility_score": 0, "customer_calloff_score": 0, "capacity_utilization_score": 0, "ASP_or_cost_spread_score": 0, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "customer_quality_score": 10, "revision_score": 15, "relative_strength_score": 65, "valuation_blowoff_risk_score": 90, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 95}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Speculative battery theme RiskWatch", "changed_components": ["orderbook_visibility_score", "customer_calloff_score", "capacity_utilization_score", "ASP_or_cost_spread_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C11 requires battery orderbook signal to convert into customer call-off, utilization, ASP/cost spread, revenue and margin bridge before clean Stage2/Green; speculative battery MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 61.76, "MAE_90D_pct": -4.7, "score_return_alignment_label": "large_theme_MFE_then_deep_MAE_speculative_battery_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_4B_too_late"}
{"row_type": "shadow_weight", "axis": "C11_battery_orderbook_customer_calloff_utilization_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Battery orderbook rerating requires confirmed customer orderbook, customer call-off, capacity utilization, ASP/cost spread and revenue/margin conversion; speculative battery MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 006400/005070 with local 4B or high-MAE orderbook-calloff watch; demotes 001570 speculative battery theme blowoff", "trigger_ids": "R3L86-C11-01-S2A-20240213|R3L86-C11-02-S2A-20240213|R3L86-C11-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R3", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["speculative_battery_theme_false_positive_high_MAE", "battery_orderbook_customer_calloff_utilization_margin_bridge_required", "local_4B_late_after_battery_orderbook_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C11, test a canonical-archetype guard requiring customer orderbook, customer call-off, capacity utilization, ASP/cost spread and revenue/gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 86
next_round = R4
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
