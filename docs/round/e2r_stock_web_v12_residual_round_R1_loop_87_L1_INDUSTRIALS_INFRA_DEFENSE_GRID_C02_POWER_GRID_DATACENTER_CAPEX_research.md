# E2R Stock-Web v12 Residual Research — R1 Loop 87 / L1 / C02

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 87,
  "computed_next_round": "R2",
  "computed_next_loop": 87,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "power_grid_datacenter_capex_guardrail",
    "transformer_cable_switchgear_backlog_margin_bridge_test",
    "late_grid_theme_MFE_vs_named_order_capacity_margin_bridge_test",
    "local_4B_timing_after_grid_equipment_MFE",
    "hard_4C_non_price_order_loss_or_margin_break_protection",
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
scheduled_round = R1
scheduled_loop = 87
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
computed_next_round = R2
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R1 restarts loop87 after loop86 R13 completed. This run selects C02 because loop86 R1 used C04, loop85 R1 used C01, and loop84 R1 used C05. The selected route is power-grid / transformer / cable / switchgear, avoiding top-covered C02 symbols.

The tested mechanism:

```text
power-grid / datacenter capex / electrification headline
→ named order or customer
→ backlog quality and delivery schedule
→ capacity expansion
→ ASP or cost pass-through
→ gross / OP margin conversion
→ durable rerating or late theme fade
```

C02 is the substation yard. Demand lights the grid, but the rerating holds only when order, capacity, delivery and margin all carry current.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C02 top-covered symbols include `010120`, `267260`, `298040`, `006340`, `103590`, and `017040`. This run avoids that top-covered set and uses:

```text
033100 / 제룡전기
000500 / 가온전선
189860 / 서전기전
```

All three are treated as new independent C02 power-grid / datacenter capex cases for this loop. No hard duplicate is intentionally reused.

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
| 033100 | 제룡전기 | `atlas/symbol_profiles/033/033100.json` | old CA candidates through 2014; selected 2024 forward window clean |
| 000500 | 가온전선 | `atlas/symbol_profiles/000/000500.json` | selected 2024-01-25 180D window before 2024-11-11 CA candidate; raw CA caveat retained |
| 189860 | 서전기전 | `atlas/symbol_profiles/189/189860.json` | old 2018 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R1L87-C02-01 | 033100 | 2024-02-13 | 20,800 | 180D | clean | true |
| R1L87-C02-02 | 000500 | 2024-01-25 | 26,250 | 180D | clean before 2024-11-11 CA candidate | true |
| R1L87-C02-03 | 189860 | 2024-07-09 | 7,130 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C02_POWER_GRID_DATACENTER_CAPEX | TRANSFORMER_BACKLOG_DELIVERY_MARGIN | keep Stage2 with named order, backlog quality, capacity/delivery and margin bridge; add local 4B after MFE |
| C02_POWER_GRID_DATACENTER_CAPEX | POWER_CABLE_GRID_CAPEX_HIGH_MAE_CA_WATCH | keep Stage2 with high-MAE and raw-CA-window watch until source repair |
| C02_POWER_GRID_DATACENTER_CAPEX | SWITCHGEAR_LATE_THEME_HIGH_MAE_FADE | reject late grid/switchgear theme MFE without named backlog and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R1L87-C02-01 | 033100 | 제룡전기 | Stage2-Actionable | 2024-02-13 | 20,800 | 384.13 | -2.88 | current_profile_partially_correct_local_4B_watch_needed |
| R1L87-C02-02 | 000500 | 가온전선 | Stage2-Actionable | 2024-01-25 | 26,250 | 183.81 | -17.33 | current_profile_partially_correct_high_MAE_CA_window_watch_needed |
| R1L87-C02-03 | 189860 | 서전기전 | Stage2-FalsePositive | 2024-07-09 | 7,130 | 15.99 | -42.99 | current_profile_false_positive_high_MAE_late_theme |

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

This MD creates a source-repair queue and a C02 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: customer order, backlog quality, capacity expansion, delivery schedule, ASP/cost pass-through, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 033100 | `atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv` | `atlas/symbol_profiles/033/033100.json` |
| 000500 | `atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv` | `atlas/symbol_profiles/000/000500.json` |
| 189860 | `atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv` | `atlas/symbol_profiles/189/189860.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 033100 / 제룡전기

C02 transformer/grid-capex positive with local 4B watch. The February trigger produced an extreme MFE into July. It is a strong positive, but the later post-peak drawdown shows why clean Green requires named order, delivery and margin evidence.

### Case 2 — 000500 / 가온전선

C02 power-cable positive with high-MAE and CA-window watch. The January trigger produced a major MFE into May, but the early MAE and raw corporate-action caveat mean it should remain Stage2-Actionable plus RiskWatch until backlog and margin source repair is done.

### Case 3 — 189860 / 서전기전

C02 switchgear late-entry false positive. The July grid-equipment theme MFE was small relative to the later MAE. This rejects late switchgear/power-grid theme heat without named orders, backlog and margin bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 033100 | 20,800 | 88.94 | -2.88 | 300.00 | -2.88 | 384.13 | -2.88 | 2024-07-11 / 100,700 | -57.10 |
| 000500 | 26,250 | 12.19 | -17.33 | 183.81 | -17.33 | 183.81 | -17.33 | 2024-05-13 / 74,500 | -61.61 |
| 189860 | 7,130 | 15.99 | -36.75 | 15.99 | -42.99 | 15.99 | -42.99 | 2024-07-18 / 8,270 | -50.85 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R1L87-C02-01 | Stage2-Actionable if transformer backlog bridge exists | huge MFE, later drawdown | partially correct; local 4B/backlog-margin watch needed |
| R1L87-C02-02 | Stage2-Actionable if cable orderbook bridge exists | huge MFE but high early MAE | partially correct; high-MAE and CA-window watch needed |
| R1L87-C02-03 | risk of treating late grid theme as Stage2 | limited MFE / deep MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C02, the residual is whether power-grid/datacenter capex MFE becomes clean Stage2/Green before named order, backlog quality, delivery and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R1L87-C02-01 | 0.82 | 0.72 | local 4B watch after transformer MFE if named-order/delivery/margin bridge stalls |
| R1L87-C02-02 | 0.82 | 0.72 | local 4B watch after power-cable MFE if backlog/ASP/cost-spread bridge stalls |
| R1L87-C02-03 | 0.35 | 0.30 | late switchgear theme rejected without named order/backlog/delivery margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_order_loss_delivery_failure_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C02 hard 4C requires confirmed order loss, customer cancellation, delivery failure, margin compression, capacity execution failure, or ASP/cost-pass-through thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L1/C02 rows need named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and gross/OP margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
candidate_axis = C02_power_grid_named_order_backlog_delivery_ASP_margin_bridge_required
effect = keep transformer/cable positives with local 4B/backlog-margin watch; demote late switchgear/grid theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 166.60 | -21.07 | may over-credit late grid-equipment theme without backlog/margin bridge | needs C02 order/backlog/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 241.91 on kept positives | demotes 189860 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R1L87-C02-01 | 78 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/backlog-margin watch | partially aligned |
| R1L87-C02-02 | 78 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/backlog-margin watch | partially aligned |
| R1L87-C02-03 | 58 | Stage2-Watch/FalsePositive | 42 | Rejected-Stage2 / Late grid-theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 1 | no | yes | source repair needed |

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
  - late_power_grid_theme_false_positive_high_MAE
  - named_order_backlog_delivery_margin_bridge_required
  - local_4B_late_after_grid_equipment_MFE
  - source_proxy_runtime_promotion_risk
  - corporate_action_window_caveat_required_for_raw_unadjusted_prices
  - hard_4C_requires_non_price_order_delivery_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C02_power_grid_named_order_backlog_delivery_ASP_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C02_power_grid_named_order_backlog_delivery_ASP_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 1 residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

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
- named order or customer source
- backlog quality and delivery schedule
- capacity expansion source
- ASP/cost pass-through and margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_power_grid_named_order_backlog_delivery_ASP_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Require named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and gross/OP margin bridge before clean Stage2/Green","keeps 033100/000500 with local 4B/backlog-margin watch; demotes 189860","R1L87-C02-01-S2A-20240213|R1L87-C02-02-S2A-20240125|R1L87-C02-03-S2FP-20240709",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L87-C02-01", "symbol": "033100", "company_name": "제룡전기", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE", "case_type": "transformer_grid_capex_backlog_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L87-C02-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_transformer_MFE_but_local_4B_and_backlog_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C02 transformer positives need named orders, backlog quality, capacity expansion, delivery schedule, ASP/cost spread and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R1L87-C02-01-S2A-20240213", "case_id": "R1L87-C02-01", "symbol": "033100", "company_name": "제룡전기", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail|backlog_delivery_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "transformer / power-grid capex / datacenter-electrification backlog and capacity proxy; primary named order, delivery and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["grid_capex_proxy", "power_equipment_theme_proxy", "backlog_or_margin_proxy"], "stage3_evidence_fields": ["named_order", "backlog_quality", "delivery_schedule", "capacity_expansion", "ASP_or_cost_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["grid_equipment_MFE_without_margin_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv", "profile_path": "atlas/symbol_profiles/033/033100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 20800, "MFE_30D_pct": 88.94, "MFE_90D_pct": 300.0, "MFE_180D_pct": 384.13, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.88, "MAE_90D_pct": -2.88, "MAE_180D_pct": -2.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 100700, "drawdown_after_peak_pct": -57.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_transformer_MFE_if_named_order_delivery_margin_bridge_stalls", "four_b_evidence_type": ["power_grid_MFE_without_order_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_delivery_failure_or_margin_break", "trigger_outcome_label": "large_transformer_MFE_but_local_4B_and_backlog_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2014_CA_candidate", "same_entry_group_id": "R1L87-C02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L87-C02-01", "trigger_id": "R1L87-C02-01-S2A-20240213", "symbol": "033100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_specificity_score": 55, "named_order_score": 45, "backlog_quality_score": 45, "capacity_expansion_score": 40, "delivery_schedule_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "relative_strength_score": 75, "valuation_blowoff_risk_score": 80, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"grid_capex_specificity_score": 55, "named_order_score": 45, "backlog_quality_score": 45, "capacity_expansion_score": 40, "delivery_schedule_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "relative_strength_score": 75, "valuation_blowoff_risk_score": 90, "execution_risk_score": 60, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/backlog-margin watch", "changed_components": ["named_order_score", "backlog_quality_score", "delivery_schedule_score", "ASP_or_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C02 requires grid/datacenter capex MFE to convert into named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and margin bridge before clean Stage2/Green; late power-grid theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 300.0, "MAE_90D_pct": -2.88, "score_return_alignment_label": "large_transformer_MFE_but_local_4B_and_backlog_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R1L87-C02-02", "symbol": "000500", "company_name": "가온전선", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE", "case_type": "power_cable_grid_capex_positive_with_high_MAE_and_CA_window_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L87-C02-02-S2A-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_power_cable_MFE_but_high_MAE_CA_window_and_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_CA_window_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C02 cable positives can be very strong, but clean Green needs cable orderbook, delivery schedule, ASP/copper cost pass-through and margin bridge; raw CA windows must be checked."}
{"row_type": "trigger", "trigger_id": "R1L87-C02-02-S2A-20240125", "case_id": "R1L87-C02-02", "symbol": "000500", "company_name": "가온전선", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail|backlog_delivery_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "power cable / grid reinforcement / datacenter capex and copper-cable spread proxy; primary cable backlog, ASP and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["grid_capex_proxy", "power_equipment_theme_proxy", "backlog_or_margin_proxy"], "stage3_evidence_fields": ["named_order", "backlog_quality", "delivery_schedule", "capacity_expansion", "ASP_or_cost_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["grid_equipment_MFE_without_margin_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv", "profile_path": "atlas/symbol_profiles/000/000500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 26250, "MFE_30D_pct": 12.19, "MFE_90D_pct": 183.81, "MFE_180D_pct": 183.81, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.33, "MAE_90D_pct": -17.33, "MAE_180D_pct": -17.33, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 74500, "drawdown_after_peak_pct": -61.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_power_cable_MFE_if_backlog_ASP_cost_spread_margin_bridge_stalls", "four_b_evidence_type": ["power_grid_MFE_without_order_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_delivery_failure_or_margin_break", "trigger_outcome_label": "large_power_cable_MFE_but_high_MAE_CA_window_and_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_CA_window_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "selected_2024_01_25_forward_window_clean_before_2024_11_11_CA_candidate", "same_entry_group_id": "R1L87-C02-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L87-C02-02", "trigger_id": "R1L87-C02-02-S2A-20240125", "symbol": "000500", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_specificity_score": 55, "named_order_score": 45, "backlog_quality_score": 45, "capacity_expansion_score": 40, "delivery_schedule_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 80, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"grid_capex_specificity_score": 55, "named_order_score": 45, "backlog_quality_score": 45, "capacity_expansion_score": 40, "delivery_schedule_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 90, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/backlog-margin watch", "changed_components": ["named_order_score", "backlog_quality_score", "delivery_schedule_score", "ASP_or_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C02 requires grid/datacenter capex MFE to convert into named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and margin bridge before clean Stage2/Green; late power-grid theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 183.81, "MAE_90D_pct": -17.33, "score_return_alignment_label": "large_power_cable_MFE_but_high_MAE_CA_window_and_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_CA_window_watch_needed"}
{"row_type": "case", "case_id": "R1L87-C02-03", "symbol": "189860", "company_name": "서전기전", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE", "case_type": "switchgear_grid_theme_late_entry_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R1L87-C02-03-S2FP-20240709", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "late_grid_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_late_theme", "price_source": "Songdaiki/stock-web", "notes": "Late switchgear/grid theme MFE should be rejected unless named order, backlog quality, delivery schedule and margin conversion are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R1L87-C02-03-S2FP-20240709", "case_id": "R1L87-C02-03", "symbol": "189860", "company_name": "서전기전", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_SWITCHGEAR_POWER_GRID_DATACENTER_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_LATE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail|backlog_delivery_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-09", "evidence_available_at_that_date": "switchgear / grid equipment / power-infra policy theme proxy without confirmed named backlog, delivery visibility or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["grid_capex_proxy", "power_equipment_theme_proxy", "backlog_or_margin_proxy"], "stage3_evidence_fields": ["named_order", "backlog_quality", "delivery_schedule", "capacity_expansion", "ASP_or_cost_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["grid_equipment_MFE_without_margin_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv", "profile_path": "atlas/symbol_profiles/189/189860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-09", "entry_price": 7130, "MFE_30D_pct": 15.99, "MFE_90D_pct": 15.99, "MFE_180D_pct": 15.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -36.75, "MAE_90D_pct": -42.99, "MAE_180D_pct": -42.99, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 8270, "drawdown_after_peak_pct": -50.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "late_switchgear_theme_MFE_rejected_without_named_order_backlog_delivery_margin_bridge", "four_b_evidence_type": ["power_grid_MFE_without_order_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_delivery_failure_or_margin_break", "trigger_outcome_label": "late_grid_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_late_theme", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2018_CA_candidate", "same_entry_group_id": "R1L87-C02-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L87-C02-03", "trigger_id": "R1L87-C02-03-S2FP-20240709", "symbol": "189860", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_specificity_score": 35, "named_order_score": 5, "backlog_quality_score": 10, "capacity_expansion_score": 10, "delivery_schedule_score": 5, "ASP_or_cost_pass_through_score": 5, "gross_margin_bridge_score": 5, "customer_quality_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"grid_capex_specificity_score": 35, "named_order_score": 0, "backlog_quality_score": 0, "capacity_expansion_score": 10, "delivery_schedule_score": 0, "ASP_or_cost_pass_through_score": 0, "gross_margin_bridge_score": 0, "customer_quality_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 95, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Late grid-theme RiskWatch", "changed_components": ["named_order_score", "backlog_quality_score", "delivery_schedule_score", "ASP_or_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C02 requires grid/datacenter capex MFE to convert into named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and margin bridge before clean Stage2/Green; late power-grid theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 15.99, "MAE_90D_pct": -42.99, "score_return_alignment_label": "late_grid_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_late_theme"}
{"row_type": "shadow_weight", "axis": "C02_power_grid_named_order_backlog_delivery_ASP_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Power-grid/datacenter capex rerating requires named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and gross/OP margin conversion; late grid-equipment theme MFE without bridge fades into high MAE or 4B watch.", "backtest_effect": "keeps 033100/000500 with local 4B/backlog-margin watch; demotes 189860 late switchgear/grid theme false positive", "trigger_ids": "R1L87-C02-01-S2A-20240213|R1L87-C02-02-S2A-20240125|R1L87-C02-03-S2FP-20240709", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R1", "loop": 87, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["late_power_grid_theme_false_positive_high_MAE", "named_order_backlog_delivery_margin_bridge_required", "local_4B_late_after_grid_equipment_MFE", "source_proxy_runtime_promotion_risk", "corporate_action_window_caveat_required_for_raw_unadjusted_prices", "hard_4C_requires_non_price_order_delivery_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C02, test a canonical-archetype guard requiring named order, backlog quality, delivery schedule, capacity expansion, ASP/cost pass-through and gross/OP margin conversion before clean Stage2/Green. Keep hard 4C blocked unless a non-price order/delivery/margin thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 87
next_round = R2
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
