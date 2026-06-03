# E2R Stock-Web v12 Residual Research — R4 Loop 87 / L4 / C15

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 87,
  "computed_next_round": "R5",
  "computed_next_loop": 87,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "materials_spread_supercycle_guardrail",
    "steel_rebar_pipe_spread_to_inventory_margin_bridge_test",
    "late_steel_theme_MFE_vs_product_spread_utilization_margin_bridge_test",
    "local_4B_timing_after_material_spread_MFE",
    "hard_4C_non_price_spread_inventory_or_margin_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "corporate_action_window_caveat_review",
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
scheduled_round = R4
scheduled_loop = 87
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
computed_next_round = R5
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R4 is the materials / spread / resource round. This run selects C15 because loop86 R4 used C16 and loop85 R4 used C17. C15 is the remaining materials-spread route in the current rotation.

The tested mechanism:

```text
steel / rebar / pipe / structural steel spread headline
→ realized product spread
→ inventory valuation and utilization
→ customer demand
→ ASP or cost pass-through
→ gross / OP margin conversion
→ durable rerating or late steel theme fade
```

C15 is the mill spread ledger. A material headline can heat the furnace, but the rerating holds only when spread, inventory, utilization and margin all flow through.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C15 top-covered symbols include `005490`, `004020`, `012800`, `025820`, `001430`, and `018470`. This run avoids that top-covered set and uses:

```text
104700 / 한국철강
306200 / 세아제강
008260 / NI스틸
```

All three are treated as new independent C15 material-spread cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 104700 | 한국철강 | `atlas/symbol_profiles/104/104700.json` | old 2018 CA candidate; selected 2024 forward window clean |
| 306200 | 세아제강 | `atlas/symbol_profiles/306/306200.json` | no profile-level CA candidate |
| 008260 | NI스틸 | `atlas/symbol_profiles/008/008260.json` | old CA candidates through 2004; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R4L87-C15-01 | 104700 | 2024-02-13 | 6,890 | 180D | clean | true |
| R4L87-C15-02 | 306200 | 2024-02-13 | 138,200 | 180D | clean | true |
| R4L87-C15-03 | 008260 | 2024-02-13 | 5,370 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C15_MATERIAL_SPREAD_SUPERCYCLE | REBAR_STEEL_SPREAD_INVENTORY_MARGIN | keep Stage2 with product spread, inventory, utilization and margin bridge |
| C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_PIPE_ENERGY_PIPE_SPREAD_FADE | reject low-MFE pipe-spread theme without backlog, ASP/cost and margin bridge |
| C15_MATERIAL_SPREAD_SUPERCYCLE | STRUCTURAL_STEEL_VALUE_TRAP_FADE | reject structural-steel rebound without inventory/product-spread margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R4L87-C15-01 | 104700 | 한국철강 | Stage2-Actionable | 2024-02-13 | 6,890 | 66.04 | -0.73 | current_profile_partially_correct_controlled_MAE_but_margin_bridge_needed |
| R4L87-C15-02 | 306200 | 세아제강 | Stage2-FalsePositive | 2024-02-13 | 138,200 | 4.05 | -21.35 | current_profile_false_positive_low_MFE_high_MAE |
| R4L87-C15-03 | 008260 | NI스틸 | Stage2-FalsePositive | 2024-02-13 | 5,370 | 0.74 | -31.01 | current_profile_false_positive_low_MFE_high_MAE_value_trap |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C15 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: product spread, inventory valuation, utilization, customer demand, ASP/cost pass-through, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 104700 | `atlas/ohlcv_tradable_by_symbol_year/104/104700/2024.csv` | `atlas/symbol_profiles/104/104700.json` |
| 306200 | `atlas/ohlcv_tradable_by_symbol_year/306/306200/2024.csv` | `atlas/symbol_profiles/306/306200.json` |
| 008260 | `atlas/ohlcv_tradable_by_symbol_year/008/008260/2024.csv` | `atlas/symbol_profiles/008/008260.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 104700 / 한국철강

C15 rebar/steel spread positive with controlled MAE. The February entry produced strong MFE into April, while entry-window MAE stayed controlled. It is kept as Stage2-Actionable, but clean Green still requires product-spread, inventory and margin source repair.

### Case 2 — 306200 / 세아제강

C15 steel-pipe spread false positive. The MFE was small, and the later MAE widened. Pipe/export spread language without backlog, ASP/cost pass-through and utilization bridge should not validate Stage2.

### Case 3 — 008260 / NI스틸

C15 structural-steel value-trap false positive. The entry produced almost no MFE, then moved into deep MAE. This rejects structural steel / materials spread rebound language without explicit product-spread, inventory and margin evidence.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 104700 | 6,890 | 41.80 | -0.73 | 66.04 | -0.73 | 66.04 | -0.73 | 2024-04-12 / 11,440 | -33.65 |
| 306200 | 138,200 | 4.05 | -4.70 | 4.05 | -9.19 | 4.05 | -21.35 | 2024-03-22 / 143,800 | -24.41 |
| 008260 | 5,370 | 0.74 | -13.78 | 0.74 | -17.41 | 0.74 | -31.01 | 2024-02-13 / 5,410 | -31.52 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R4L87-C15-01 | Stage2-Actionable if spread/margin bridge exists | strong MFE, controlled MAE | partially correct; margin bridge needed |
| R4L87-C15-02 | risk of treating steel-pipe spread language as Stage2 | low MFE / high MAE | false positive |
| R4L87-C15-03 | risk of treating structural-steel rebound as Stage2 | very low MFE / deep MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C15, the residual is whether materials-spread MFE becomes clean Stage2/Green before realized product spread, inventory, utilization and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R4L87-C15-01 | 0.78 | 0.68 | local 4B watch after rebar/steel spread MFE if inventory/utilization/margin bridge stalls |
| R4L87-C15-02 | 0.35 | 0.30 | steel-pipe spread theme rejected without backlog/ASP/cost/margin bridge |
| R4L87-C15-03 | 0.35 | 0.30 | structural-steel theme rejected without inventory/product-spread/utilization bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_spread_inventory_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C15 hard 4C requires confirmed spread collapse, inventory impairment, utilization break, customer-demand deterioration, ASP/cost pass-through failure or margin thesis break.

## 17. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C15_material_spread_product_inventory_utilization_margin_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 23.61 | -9.11 | may over-credit steel/pipe/structural theme without spread bridge | needs C15 product-spread margin repair |
| P1 canonical shadow bridge profile | 3 | keeps 104700 with watch | demotes 306200/008260 | better alignment, source repair required |

## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | yes |

## 20. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
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
  - material_spread_theme_false_positive_low_MFE_high_MAE
  - product_spread_inventory_utilization_margin_bridge_required
  - controlled_MAE_positive_still_needs_margin_bridge
  - source_proxy_runtime_promotion_risk
  - corporate_action_window_caveat_required_for_raw_unadjusted_prices
  - hard_4C_requires_non_price_spread_inventory_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C15_material_spread_product_inventory_utilization_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 21. Validation Scope / Non-Validation Scope

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
- realized product spread source
- inventory valuation and utilization
- customer demand / ASP / cost pass-through
- gross/OP margin conversion
- production scoring implementation
```

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_material_spread_product_inventory_utilization_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Require realized product spread, inventory valuation, utilization, customer demand, ASP/cost pass-through and gross/OP margin conversion before clean Stage2/Green","keeps 104700 with local 4B/spread-margin watch; demotes 306200/008260","R4L87-C15-01-S2A-20240213|R4L87-C15-02-S2FP-20240213|R4L87-C15-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 23. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L87-C15-01", "symbol": "104700", "company_name": "한국철강", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE", "case_type": "rebar_steel_spread_inventory_margin_positive_with_controlled_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L87-C15-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_steel_spread_MFE_with_controlled_MAE_but_inventory_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_controlled_MAE_but_margin_bridge_needed", "price_source": "Songdaiki/stock-web", "notes": "C15 steel/rebar positives need realized product spread, inventory valuation, utilization, demand and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R4L87-C15-01-S2A-20240213", "case_id": "R4L87-C15-01", "symbol": "104700", "company_name": "한국철강", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|materials_spread_supercycle_guardrail|product_spread_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "rebar/steel spread, inventory normalization and product-margin recovery proxy; primary spread, inventory and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["materials_spread_proxy", "inventory_rebound_proxy", "utilization_or_margin_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "utilization", "customer_demand", "ASP_cost_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["material_spread_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_spread_collapse_inventory_impairment_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/104/104700/2024.csv", "profile_path": "atlas/symbol_profiles/104/104700.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 6890, "MFE_30D_pct": 41.8, "MAE_30D_pct": -0.73, "MFE_90D_pct": 66.04, "MAE_90D_pct": -0.73, "MFE_180D_pct": 66.04, "MAE_180D_pct": -0.73, "peak_date": "2024-04-12", "peak_price": 11440, "drawdown_after_peak_pct": -33.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "local_4B_watch_after_rebar_steel_spread_MFE_if_inventory_utilization_margin_bridge_stalls", "four_b_evidence_type": ["materials_spread_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_inventory_or_margin_break", "trigger_outcome_label": "large_steel_spread_MFE_with_controlled_MAE_but_inventory_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_controlled_MAE_but_margin_bridge_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2018_CA_candidate", "same_entry_group_id": "R4L87-C15-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L87-C15-01", "trigger_id": "R4L87-C15-01-S2A-20240213", "symbol": "104700", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"product_spread_score": 55, "inventory_valuation_score": 45, "utilization_score": 45, "customer_demand_score": 40, "ASP_cost_pass_through_score": 45, "gross_margin_bridge_score": 45, "revision_score": 40, "relative_strength_score": 65, "valuation_blowoff_risk_score": 55, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"product_spread_score": 55, "inventory_valuation_score": 45, "utilization_score": 45, "customer_demand_score": 40, "ASP_cost_pass_through_score": 45, "gross_margin_bridge_score": 45, "revision_score": 40, "relative_strength_score": 65, "valuation_blowoff_risk_score": 65, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/spread-margin watch", "changed_components": ["product_spread_score", "inventory_valuation_score", "utilization_score", "ASP_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C15 requires materials-spread MFE to convert into realized product spread, inventory valuation, utilization, ASP/cost pass-through and gross/OP margin bridge before clean Stage2/Green.", "MFE_90D_pct": 66.04, "MAE_90D_pct": -0.73, "score_return_alignment_label": "large_steel_spread_MFE_with_controlled_MAE_but_inventory_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_controlled_MAE_but_margin_bridge_needed"}
{"row_type": "case", "case_id": "R4L87-C15-02", "symbol": "306200", "company_name": "세아제강", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE", "case_type": "steel_pipe_energy_pipe_spread_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R4L87-C15-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_pipe_spread_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Steel-pipe spread language should remain RiskWatch unless backlog quality, ASP/cost pass-through, utilization and margin conversion are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R4L87-C15-02-S2FP-20240213", "case_id": "R4L87-C15-02", "symbol": "306200", "company_name": "세아제강", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|materials_spread_supercycle_guardrail|product_spread_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "steel pipe / energy pipe / export spread theme proxy without confirmed backlog, ASP/cost spread, utilization or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["materials_spread_proxy", "inventory_rebound_proxy", "utilization_or_margin_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "utilization", "customer_demand", "ASP_cost_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["material_spread_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_spread_collapse_inventory_impairment_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/306/306200/2024.csv", "profile_path": "atlas/symbol_profiles/306/306200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 138200, "MFE_30D_pct": 4.05, "MAE_30D_pct": -4.7, "MFE_90D_pct": 4.05, "MAE_90D_pct": -9.19, "MFE_180D_pct": 4.05, "MAE_180D_pct": -21.35, "peak_date": "2024-03-22", "peak_price": 143800, "drawdown_after_peak_pct": -24.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "steel_pipe_spread_theme_rejected_without_backlog_ASP_cost_spread_utilization_margin_bridge", "four_b_evidence_type": ["materials_spread_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_inventory_or_margin_break", "trigger_outcome_label": "low_MFE_high_MAE_pipe_spread_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R4L87-C15-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L87-C15-02", "trigger_id": "R4L87-C15-02-S2FP-20240213", "symbol": "306200", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"product_spread_score": 10, "inventory_valuation_score": 5, "utilization_score": 10, "customer_demand_score": 15, "ASP_cost_pass_through_score": 5, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"product_spread_score": 0, "inventory_valuation_score": 0, "utilization_score": 0, "customer_demand_score": 15, "ASP_cost_pass_through_score": 0, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 70, "execution_risk_score": 92, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Material-spread theme RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "utilization_score", "ASP_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C15 requires materials-spread MFE to convert into realized product spread, inventory valuation, utilization, ASP/cost pass-through and gross/OP margin bridge before clean Stage2/Green.", "MFE_90D_pct": 4.05, "MAE_90D_pct": -9.19, "score_return_alignment_label": "low_MFE_high_MAE_pipe_spread_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "case", "case_id": "R4L87-C15-03", "symbol": "008260", "company_name": "NI스틸", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE", "case_type": "structural_steel_theme_low_MFE_high_MAE_value_trap", "positive_or_counterexample": "counterexample", "best_trigger": "R4L87-C15-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "very_low_MFE_deep_MAE_structural_steel_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE_value_trap", "price_source": "Songdaiki/stock-web", "notes": "Structural steel/material spread rebound should be rejected unless product spread, inventory turn, utilization and margin bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R4L87-C15-03-S2FP-20240213", "case_id": "R4L87-C15-03", "symbol": "008260", "company_name": "NI스틸", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_REBAR_PIPE_STRUCTURAL_STEEL_PRODUCT_SPREAD_INVENTORY_UTILIZATION_MARGIN_BRIDGE_VS_LATE_STEEL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|materials_spread_supercycle_guardrail|product_spread_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "structural steel / construction steel / materials spread rebound theme proxy without product spread, inventory, utilization or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["materials_spread_proxy", "inventory_rebound_proxy", "utilization_or_margin_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "utilization", "customer_demand", "ASP_cost_pass_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["material_spread_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_spread_collapse_inventory_impairment_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008260/2024.csv", "profile_path": "atlas/symbol_profiles/008/008260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 5370, "MFE_30D_pct": 0.74, "MAE_30D_pct": -13.78, "MFE_90D_pct": 0.74, "MAE_90D_pct": -17.41, "MFE_180D_pct": 0.74, "MAE_180D_pct": -31.01, "peak_date": "2024-02-13", "peak_price": 5410, "drawdown_after_peak_pct": -31.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "structural_steel_theme_rejected_without_inventory_product_spread_utilization_margin_bridge", "four_b_evidence_type": ["materials_spread_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_inventory_or_margin_break", "trigger_outcome_label": "very_low_MFE_deep_MAE_structural_steel_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE_value_trap", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2004_CA_candidates", "same_entry_group_id": "R4L87-C15-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L87-C15-03", "trigger_id": "R4L87-C15-03-S2FP-20240213", "symbol": "008260", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"product_spread_score": 10, "inventory_valuation_score": 5, "utilization_score": 10, "customer_demand_score": 15, "ASP_cost_pass_through_score": 5, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"product_spread_score": 0, "inventory_valuation_score": 0, "utilization_score": 0, "customer_demand_score": 15, "ASP_cost_pass_through_score": 0, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 70, "execution_risk_score": 92, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Material-spread theme RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "utilization_score", "ASP_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C15 requires materials-spread MFE to convert into realized product spread, inventory valuation, utilization, ASP/cost pass-through and gross/OP margin bridge before clean Stage2/Green.", "MFE_90D_pct": 0.74, "MAE_90D_pct": -17.41, "score_return_alignment_label": "very_low_MFE_deep_MAE_structural_steel_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE_value_trap"}
{"row_type": "shadow_weight", "axis": "C15_material_spread_product_inventory_utilization_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Materials spread rerating requires realized product spread, inventory valuation, utilization, customer demand, ASP/cost pass-through and gross/OP margin conversion; steel/pipe/structural-steel theme MFE without bridge fades into high MAE or low-MFE false positive.", "backtest_effect": "keeps 104700 with local 4B/spread-margin watch; demotes 306200/008260 low-MFE high-MAE material-spread false positives", "trigger_ids": "R4L87-C15-01-S2A-20240213|R4L87-C15-02-S2FP-20240213|R4L87-C15-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R4", "loop": 87, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["material_spread_theme_false_positive_low_MFE_high_MAE", "product_spread_inventory_utilization_margin_bridge_required", "controlled_MAE_positive_still_needs_margin_bridge", "source_proxy_runtime_promotion_risk", "corporate_action_window_caveat_required_for_raw_unadjusted_prices", "hard_4C_requires_non_price_spread_inventory_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 24. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C15, test a canonical guard requiring realized product spread, inventory valuation, utilization, customer demand, ASP/cost pass-through and gross/OP margin conversion before clean Stage2/Green.

## 25. Next Round State

```text
completed_round = R4
completed_loop = 87
next_round = R5
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 26. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
