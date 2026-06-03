# E2R Stock-Web v12 Residual Research — R4 Loop 85 / L4 / C17

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 85,
  "computed_next_round": "R5",
  "computed_next_loop": 85,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "chemical_commodity_margin_spread_guardrail",
    "chemical_rebound_theme_vs_product_spread_margin_bridge_test",
    "inventory_cost_ASP_margin_bridge_test",
    "local_4B_timing_after_chemical_MFE",
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
scheduled_round = R4
scheduled_loop = 85
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
computed_next_round = R5
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R4 is the materials / spread / resource round. This run selects C17 because loop83 already tested C16 and loop84 tested C15.

The tested mechanism:

```text
chemical / commodity-spread / specialty-material rebound headline
→ realized product spread
→ inventory valuation and ASP pass-through
→ utilization and customer demand
→ gross / OP margin conversion
→ durable rerating or chemical-theme fade
```

C17 is not “chemical stocks bounced.” It is the distillation column: only real product spread and margin conversion survive the heat.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C17 top-covered symbols include `298020`, `011780`, `006650`, `011170`, `014830`, and `010950`. This run avoids that top-covered set and uses:

```text
014680 / 한솔케미칼
005950 / 이수화학
069260 / TKG휴켐스
```

All three are treated as new independent C17 chemical/commodity margin-spread cases for this loop. No hard duplicate is intentionally reused.

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
| 014680 | 한솔케미칼 | `atlas/symbol_profiles/014/014680.json` | old CA candidates through 1999; selected 2024 forward window clean |
| 005950 | 이수화학 | `atlas/symbol_profiles/005/005950.json` | old 2020 CA candidate; selected 2024 forward window clean |
| 069260 | TKG휴켐스 | `atlas/symbol_profiles/069/069260.json` | old 2010 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R4L85-C17-01 | 014680 | 2024-03-20 | 200,000 | 180D | clean | true |
| R4L85-C17-02 | 005950 | 2024-02-26 | 14,210 | 180D | clean | true |
| R4L85-C17-03 | 069260 | 2024-01-25 | 20,650 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SPECIALTY_CHEMICAL_REBOUND_FADE | reject rebound when product spread, customer demand and margin bridge are absent |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SULFUR_SPECIALTY_THEME_SPIKE_HIGH_MAE | reject chemical-theme spike unless raw-material spread and utilization bridge are visible |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | NITRIC_ACID_SPREAD_VALUE_TRAP | reject low-MFE chemical-spread value trap without revision and margin expansion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R4L85-C17-01 | 014680 | 한솔케미칼 | Stage2-FalsePositive | 2024-03-20 | 200,000 | 7.0 | -41.9 | current_profile_false_positive_rebound_MFE_fade |
| R4L85-C17-02 | 005950 | 이수화학 | Stage2-FalsePositive | 2024-02-26 | 14,210 | 10.91 | -49.82 | current_profile_false_positive_high_MAE |
| R4L85-C17-03 | 069260 | TKG휴켐스 | Stage2-FalsePositive | 2024-01-25 | 20,650 | 2.66 | -15.74 | current_profile_false_positive_low_MFE_value_trap |

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

This MD creates a source-repair queue and a C17 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: product-spread data, raw-material cost, inventory valuation, ASP pass-through, utilization, customer demand, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 014680 | `atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv` | `atlas/symbol_profiles/014/014680.json` |
| 005950 | `atlas/ohlcv_tradable_by_symbol_year/005/005950/2024.csv` | `atlas/symbol_profiles/005/005950.json` |
| 069260 | `atlas/ohlcv_tradable_by_symbol_year/069/069260/2024.csv` | `atlas/symbol_profiles/069/069260.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 014680 / 한솔케미칼

C17 specialty-chemical rebound false positive. The entry created a short MFE, but the later drawdown was much larger. Without source-repaired product-spread and margin evidence, the rebound is not a clean Stage2 recovery.

### Case 2 — 005950 / 이수화학

C17 sulfur/specialty-chemical theme spike false positive. The initial spike was tradable, but it faded into a deep MAE. This is the clean high-MAE rejection row.

### Case 3 — 069260 / TKG휴켐스

C17 low-MFE chemical-spread value trap. The drawdown was less dramatic than the first two, but the MFE was too small to justify Stage2. Stable spread/value language is not an E2R trigger without positive revision and margin expansion.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 014680 | 200,000 | 7.00 | -9.90 | 7.00 | -13.45 | 7.00 | -41.90 | 2024-03-21 / 214,000 | -45.70 |
| 005950 | 14,210 | 10.91 | -15.41 | 10.91 | -30.96 | 10.91 | -49.82 | 2024-02-26 / 15,760 | -54.76 |
| 069260 | 20,650 | 2.66 | -4.41 | 2.66 | -7.07 | 2.66 | -15.74 | 2024-02-02 / 21,200 | -17.92 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R4L85-C17-01 | risk of treating specialty chemical rebound as Stage2 | small MFE / large MAE | false positive |
| R4L85-C17-02 | risk of treating sulfur/specialty theme spike as Stage2 | short MFE / deep MAE | false positive / high-MAE guardrail |
| R4L85-C17-03 | risk of treating chemical spread value as Stage2 | very low MFE / slow MAE | false positive / low-MFE value trap |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C17, the residual is whether chemical rebound or spread language becomes Stage2 before product spread, inventory valuation and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R4L85-C17-01 | 0.35 | 0.30 | chemical rebound MFE rejected without product-spread/inventory/margin bridge |
| R4L85-C17-02 | 0.35 | 0.30 | sulfur/specialty theme rejected without spread/utilization/margin bridge |
| R4L85-C17-03 | 0.35 | 0.30 | chemical-spread value rebound rejected without positive revision/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_spread_or_margin_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L4/C17 chemical rows need realized product spread, inventory valuation, ASP pass-through, utilization and gross/OP margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
candidate_axis = C17_chemical_product_spread_inventory_margin_bridge_required
effect = demote chemical rebound/theme false positives and low-MFE spread value traps
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 6.86 | -17.16 | may over-credit chemical rebound/spread theme | needs C17 bridge repair |
| P1 canonical shadow bridge profile | 3 | no kept positives | demotes all three | blocks recovery labels until product-spread/margin repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R4L85-C17-01 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Chemical-spread RiskWatch | improved |
| R4L85-C17-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Chemical-spread RiskWatch | improved |
| R4L85-C17-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / Chemical-spread RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE | 0 | 3 | 3-watch | 0-hard | 3 | 0 | 3 | 3 | no | yes | source repair needed |

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
  - chemical_rebound_theme_false_positive_high_MAE
  - product_spread_inventory_margin_bridge_required
  - low_MFE_chemical_spread_value_trap
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C17_chemical_product_spread_inventory_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C17_chemical_product_spread_inventory_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent counterexamples for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

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
- product-spread data source
- raw-material cost and ASP pass-through
- inventory valuation
- utilization and customer demand
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_chemical_product_spread_inventory_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Require realized product spread, inventory valuation, ASP pass-through, utilization and gross/OP margin conversion before clean Stage2/Green","demotes 014680/005950/069260 chemical-rebound or spread-theme false positives","R4L85-C17-01-S2FP-20240320|R4L85-C17-02-S2FP-20240226|R4L85-C17-03-S2FP-20240125",3,3,3,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L85-C17-01", "symbol": "014680", "company_name": "한솔케미칼", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "case_type": "specialty_chemical_semiconductor_material_rebound_margin_bridge_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R4L85-C17-01-S2FP-20240320", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "small_MFE_then_large_MAE_chemical_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_rebound_MFE_fade", "price_source": "Songdaiki/stock-web", "notes": "C17 specialty chemical rebound should be demoted unless product spread, inventory valuation, customer demand and gross/OP margin bridge are confirmed."}
{"row_type": "trigger", "trigger_id": "R4L85-C17-01-S2FP-20240320", "case_id": "R4L85-C17-01", "symbol": "014680", "company_name": "한솔케미칼", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail|chemical_rebound_theme_vs_product_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-20", "evidence_available_at_that_date": "specialty chemical / semiconductor material demand rebound proxy without confirmed product-spread, inventory and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["chemical_rebound_or_spread_proxy", "commodity_cost_proxy", "ASP_or_demand_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "ASP_pass_through", "utilization", "gross_or_OP_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["chemical_MFE_without_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_spread_collapse_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv", "profile_path": "atlas/symbol_profiles/014/014680.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-20", "entry_price": 200000, "MFE_30D_pct": 7.0, "MFE_90D_pct": 7.0, "MFE_180D_pct": 7.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.9, "MAE_90D_pct": -13.45, "MAE_180D_pct": -41.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-21", "peak_price": 214000, "drawdown_after_peak_pct": -45.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "chemical_rebound_MFE_rejected_without_product_spread_inventory_margin_bridge", "four_b_evidence_type": ["chemical_MFE_without_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_or_margin_break", "trigger_outcome_label": "small_MFE_then_large_MAE_chemical_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_rebound_MFE_fade", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_1999_CA_candidates", "same_entry_group_id": "R4L85-C17-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L85-C17-01", "trigger_id": "R4L85-C17-01-S2FP-20240320", "symbol": "014680", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"commodity_price_score": 25, "product_spread_score": 10, "inventory_valuation_score": 10, "ASP_pass_through_score": 5, "utilization_score": 10, "customer_demand_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"commodity_price_score": 25, "product_spread_score": 0, "inventory_valuation_score": 0, "ASP_pass_through_score": 0, "utilization_score": 0, "customer_demand_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Chemical-spread RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "ASP_pass_through_score", "utilization_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C17 requires commodity/chemical rebound to convert into realized product spread, inventory valuation, ASP pass-through, utilization and margin conversion before clean Stage2/Green; rebound MFE alone is demoted.", "MFE_90D_pct": 7.0, "MAE_90D_pct": -13.45, "score_return_alignment_label": "small_MFE_then_large_MAE_chemical_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_rebound_MFE_fade"}
{"row_type": "case", "case_id": "R4L85-C17-02", "symbol": "005950", "company_name": "이수화학", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "case_type": "sulfur_specialty_chemical_theme_spike_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L85-C17-02-S2FP-20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_spike_high_MAE_chemical_margin_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Chemical theme spike should remain RiskWatch unless raw-material cost spread, ASP pass-through, utilization and margin bridge are visible at entry."}
{"row_type": "trigger", "trigger_id": "R4L85-C17-02-S2FP-20240226", "case_id": "R4L85-C17-02", "symbol": "005950", "company_name": "이수화학", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail|chemical_rebound_theme_vs_product_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "sulfur / specialty chemical / battery-material adjacent theme proxy without realized spread, utilization or margin conversion", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["chemical_rebound_or_spread_proxy", "commodity_cost_proxy", "ASP_or_demand_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "ASP_pass_through", "utilization", "gross_or_OP_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["chemical_MFE_without_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_spread_collapse_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005950/2024.csv", "profile_path": "atlas/symbol_profiles/005/005950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 14210, "MFE_30D_pct": 10.91, "MFE_90D_pct": 10.91, "MFE_180D_pct": 10.91, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.41, "MAE_90D_pct": -30.96, "MAE_180D_pct": -49.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 15760, "drawdown_after_peak_pct": -54.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "sulfur_specialty_chemical_theme_rejected_without_spread_utilization_margin_bridge", "four_b_evidence_type": ["chemical_MFE_without_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_or_margin_break", "trigger_outcome_label": "theme_spike_high_MAE_chemical_margin_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2020_CA_candidate", "same_entry_group_id": "R4L85-C17-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L85-C17-02", "trigger_id": "R4L85-C17-02-S2FP-20240226", "symbol": "005950", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"commodity_price_score": 35, "product_spread_score": 10, "inventory_valuation_score": 10, "ASP_pass_through_score": 5, "utilization_score": 10, "customer_demand_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"commodity_price_score": 35, "product_spread_score": 0, "inventory_valuation_score": 0, "ASP_pass_through_score": 0, "utilization_score": 0, "customer_demand_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Chemical-spread RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "ASP_pass_through_score", "utilization_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C17 requires commodity/chemical rebound to convert into realized product spread, inventory valuation, ASP pass-through, utilization and margin conversion before clean Stage2/Green; rebound MFE alone is demoted.", "MFE_90D_pct": 10.91, "MAE_90D_pct": -30.96, "score_return_alignment_label": "theme_spike_high_MAE_chemical_margin_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R4L85-C17-03", "symbol": "069260", "company_name": "TKG휴켐스", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "case_type": "nitric_acid_chemical_spread_low_MFE_value_trap_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L85-C17-03-S2FP-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_slow_MAE_chemical_spread_value_trap", "current_profile_verdict": "current_profile_false_positive_low_MFE_value_trap", "price_source": "Songdaiki/stock-web", "notes": "Commodity chemical spread/value cases should not be Stage2 without product-spread improvement, utilization, ASP pass-through and revision evidence."}
{"row_type": "trigger", "trigger_id": "R4L85-C17-03-S2FP-20240125", "case_id": "R4L85-C17-03", "symbol": "069260", "company_name": "TKG휴켐스", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail|chemical_rebound_theme_vs_product_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "nitric acid / commodity chemical spread and dividend/value proxy without positive product-spread revision or margin expansion bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["chemical_rebound_or_spread_proxy", "commodity_cost_proxy", "ASP_or_demand_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "ASP_pass_through", "utilization", "gross_or_OP_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["chemical_MFE_without_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_spread_collapse_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/069/069260/2024.csv", "profile_path": "atlas/symbol_profiles/069/069260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 20650, "MFE_30D_pct": 2.66, "MFE_90D_pct": 2.66, "MFE_180D_pct": 2.66, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.41, "MAE_90D_pct": -7.07, "MAE_180D_pct": -15.74, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 21200, "drawdown_after_peak_pct": -17.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "chemical_spread_value_rebound_rejected_without_positive_revision_margin_bridge", "four_b_evidence_type": ["chemical_MFE_without_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_or_margin_break", "trigger_outcome_label": "low_MFE_slow_MAE_chemical_spread_value_trap", "current_profile_verdict": "current_profile_false_positive_low_MFE_value_trap", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2010_CA_candidate", "same_entry_group_id": "R4L85-C17-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L85-C17-03", "trigger_id": "R4L85-C17-03-S2FP-20240125", "symbol": "069260", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"commodity_price_score": 35, "product_spread_score": 10, "inventory_valuation_score": 10, "ASP_pass_through_score": 5, "utilization_score": 10, "customer_demand_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 20, "valuation_blowoff_risk_score": 45, "execution_risk_score": 65, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"commodity_price_score": 35, "product_spread_score": 0, "inventory_valuation_score": 0, "ASP_pass_through_score": 0, "utilization_score": 0, "customer_demand_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 20, "valuation_blowoff_risk_score": 45, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / Chemical-spread RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "ASP_pass_through_score", "utilization_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C17 requires commodity/chemical rebound to convert into realized product spread, inventory valuation, ASP pass-through, utilization and margin conversion before clean Stage2/Green; rebound MFE alone is demoted.", "MFE_90D_pct": 2.66, "MAE_90D_pct": -7.07, "score_return_alignment_label": "low_MFE_slow_MAE_chemical_spread_value_trap", "current_profile_verdict": "current_profile_false_positive_low_MFE_value_trap"}
{"row_type": "shadow_weight", "axis": "C17_chemical_product_spread_inventory_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Chemical/commodity-spread rerating requires realized product spread, inventory valuation, ASP pass-through, utilization and gross/OP margin conversion; chemical rebound theme MFE without bridge fades into high MAE or low-MFE value trap.", "backtest_effect": "demotes 014680/005950/069260 chemical-rebound or spread-theme false positives", "trigger_ids": "R4L85-C17-01-S2FP-20240320|R4L85-C17-02-S2FP-20240226|R4L85-C17-03-S2FP-20240125", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 3, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R4", "loop": 85, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["chemical_rebound_theme_false_positive_high_MAE", "product_spread_inventory_margin_bridge_required", "low_MFE_chemical_spread_value_trap", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C17, test a canonical-archetype guard requiring realized product spread, inventory valuation, ASP pass-through, utilization and gross/OP margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 85
next_round = R5
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
