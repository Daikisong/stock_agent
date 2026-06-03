# E2R Stock-Web v12 Residual Research — R4 Loop 84 / L4 / C15

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 84,
  "computed_next_round": "R5",
  "computed_next_loop": 84,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "material_spread_supercycle_guardrail",
    "commodity_price_to_product_spread_margin_bridge_test",
    "local_4B_timing_after_spread_MFE",
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
scheduled_loop = 84
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
computed_next_round = R5
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R4 is the materials / spread / resource round. This run selects C15 because loop83 already tested C16, while C15 remains less crowded than C17 in the No-Repeat ledger.

The tested mechanism:

```text
commodity / material price headline
→ product spread and inventory valuation
→ customer volume and mix
→ cost pass-through
→ gross-margin conversion
→ durable rerating or local 4B / false-positive fade
```

C15 is not “copper or aluminum went up.” It is the furnace test: the raw material heat must become product spread, then margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C15 top-covered symbols include `005490`, `004020`, `012800`, `025820`, `001430`, and `018470`. This run avoids that top-covered set and uses:

```text
103140 / 풍산
004560 / 현대비앤지스틸
008350 / 남선알미늄
```

All three are treated as new independent C15 material-spread cases for this loop. No hard duplicate is intentionally reused.

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
| 103140 | 풍산 | `atlas/symbol_profiles/103/103140.json` | no profile-level CA candidate |
| 004560 | 현대비앤지스틸 | `atlas/symbol_profiles/004/004560.json` | old CA candidates through 2003; selected 2024 forward window clean |
| 008350 | 남선알미늄 | `atlas/symbol_profiles/008/008350.json` | old CA candidates through 2009; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R4L84-C15-01 | 103140 | 2024-03-07 | 46,100 | 180D | clean | true |
| R4L84-C15-02 | 004560 | 2024-03-12 | 20,900 | 180D | clean | true |
| R4L84-C15-03 | 008350 | 2024-02-13 | 2,155 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_PRODUCT_SPREAD_DEFENSE_MIX | keep Stage2 only with product spread, inventory valuation, mix and margin bridge; add local 4B after spread MFE |
| C15_MATERIAL_SPREAD_SUPERCYCLE | STAINLESS_NICKEL_THEME_FADE | reject or demote when nickel/stainless theme lacks realized spread and order/margin bridge |
| C15_MATERIAL_SPREAD_SUPERCYCLE | ALUMINUM_INFRA_MATERIAL_THEME_FADE | reject when aluminum/infrastructure material beta lacks volume and margin conversion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R4L84-C15-01 | 103140 | 풍산 | Stage2-Actionable | 2024-03-07 | 46,100 | 54.23 | -3.9 | current_profile_partially_correct_local_4B_watch_needed |
| R4L84-C15-02 | 004560 | 현대비앤지스틸 | Stage2-FalsePositive | 2024-03-12 | 20,900 | 7.18 | -41.63 | current_profile_false_positive_high_MAE |
| R4L84-C15-03 | 008350 | 남선알미늄 | Stage2-FalsePositive | 2024-02-13 | 2,155 | 1.16 | -41.3 | current_profile_false_positive |

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

This MD therefore creates a source-repair queue and a C15 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: commodity price spread, product spread, inventory valuation, shipment volume, customer mix, cost pass-through, margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 103140 | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv` | `atlas/symbol_profiles/103/103140.json` |
| 004560 | `atlas/ohlcv_tradable_by_symbol_year/004/004560/2024.csv` | `atlas/symbol_profiles/004/004560.json` |
| 008350 | `atlas/ohlcv_tradable_by_symbol_year/008/008350/2024.csv` | `atlas/symbol_profiles/008/008350.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 103140 / 풍산

C15 copper/material positive with local 4B watch. The price path delivered strong MFE with controlled MAE, but the later drawdown shows why product-spread positives should still carry a local 4B watch if the margin bridge stops improving.

### Case 2 — 004560 / 현대비앤지스틸

C15 stainless/nickel false positive. The initial MFE was small and quickly overwhelmed by high MAE. Theme movement without realized product spread and margin pass-through is not Stage2-Actionable.

### Case 3 — 008350 / 남선알미늄

C15 aluminum/infrastructure-material false positive. The price path barely created MFE and then bled into deep MAE. This is the cleanest rejection row in the loop.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 103140 | 46,100 | 23.64 | -3.90 | 54.23 | -3.90 | 54.23 | -3.90 | 2024-07-10 / 71,100 | -33.90 |
| 004560 | 20,900 | 7.18 | -8.66 | 7.18 | -23.16 | 7.18 | -41.63 | 2024-03-28 / 22,400 | -45.54 |
| 008350 | 2,155 | 1.16 | -11.23 | 1.16 | -18.00 | 1.16 | -41.30 | 2024-02-13 / 2,180 | -41.97 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R4L84-C15-01 | Stage2-Actionable if spread bridge exists | high MFE, later drawdown | partially correct; local 4B watch needed |
| R4L84-C15-02 | risk of treating steel/nickel theme as Stage2 | low MFE / high MAE | false positive |
| R4L84-C15-03 | risk of treating aluminum/infrastructure theme as Stage2 | almost no MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C15, the residual is not Green lateness. The residual is whether commodity/material price movement becomes Stage2-Actionable before realized product spread and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R4L84-C15-01 | 0.82 | 0.72 | local 4B watch after copper spread MFE if margin bridge stalls |
| R4L84-C15-02 | 0.35 | 0.30 | commodity theme MFE rejected without spread/margin bridge |
| R4L84-C15-03 | 0.35 | 0.30 | aluminum theme rejected without product spread/volume bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_spread_or_volume_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L4 material-spread rows need realized product spread, inventory valuation, customer volume and gross-margin bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
candidate_axis = C15_material_price_to_product_spread_margin_bridge_required
effect = keep spread-positive cases with local 4B watch; demote commodity/material theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 20.86 | -15.02 | may over-credit commodity/material theme MFE | needs C15 bridge repair |
| P1 canonical shadow bridge profile | 3 | 54.23 on kept positive | -3.90 on kept positive | demotes 004560/008350 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R4L84-C15-01 | 80 | Stage2-Actionable | 78 | Stage2-Actionable + local 4B watch | partially aligned |
| R4L84-C15-02 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |
| R4L84-C15-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
residual_error_types_found:
  - material_theme_false_positive_high_MAE
  - commodity_price_to_product_spread_margin_bridge_required
  - local_4B_late_after_spread_MFE
  - source_proxy_runtime_promotion_risk
new_axis_proposed: false
existing_axis_strengthened:
  - C15_material_price_to_product_spread_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C15_material_price_to_product_spread_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

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
- commodity spread source
- realized product spread
- inventory valuation
- customer volume and mix
- gross-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_material_price_to_product_spread_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Require realized product spread, inventory valuation, customer volume and gross-margin bridge before Stage2-Actionable","keeps 103140 with local 4B watch; demotes 004560/008350","R4L84-C15-01-S2A-20240307|R4L84-C15-02-S2FP-20240312|R4L84-C15-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L84-C15-01", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE", "case_type": "copper_spread_defense_material_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L84-C15-01-S2A-20240307", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "spread_positive_MFE_with_later_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C15 can keep Stage2 only if copper/material price tailwind converts into product spread, inventory valuation, mix and margin bridge."}
{"row_type": "trigger", "trigger_id": "R4L84-C15-01-S2A-20240307", "case_id": "R4L84-C15-01", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|material_spread_supercycle_guardrail|local_4B_timing_after_spread_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-07", "evidence_available_at_that_date": "copper price / product spread / defense-material mix proxy; primary spread and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["commodity_price_or_material_spread_proxy", "product_spread_proxy", "volume_or_mix_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "customer_volume", "cost_pass_through", "gross_margin_conversion"], "stage4b_evidence_fields": ["spread_theme_MFE_without_margin_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_spread_collapse_or_customer_volume_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-07", "entry_price": 46100, "MFE_30D_pct": 23.64, "MFE_90D_pct": 54.23, "MFE_180D_pct": 54.23, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.9, "MAE_90D_pct": -3.9, "MAE_180D_pct": -3.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-10", "peak_price": 71100, "drawdown_after_peak_pct": -33.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_copper_spread_MFE_if_margin_bridge_stalls", "four_b_evidence_type": ["spread_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_or_volume_break", "trigger_outcome_label": "spread_positive_MFE_with_later_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R4L84-C15-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L84-C15-01", "trigger_id": "R4L84-C15-01-S2A-20240307", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_price_score": 60, "product_spread_score": 45, "inventory_valuation_score": 40, "order_volume_score": 35, "margin_bridge_score": 40, "revision_score": 50, "relative_strength_score": 70, "valuation_blowoff_risk_score": 55, "execution_risk_score": 35, "source_quality_score": 20, "cost_pass_through_score": 40, "4B_watch_score": 45}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"commodity_price_score": 60, "product_spread_score": 45, "inventory_valuation_score": 40, "order_volume_score": 35, "margin_bridge_score": 40, "revision_score": 50, "relative_strength_score": 70, "valuation_blowoff_risk_score": 65, "execution_risk_score": 35, "source_quality_score": 10, "cost_pass_through_score": 40, "4B_watch_score": 75}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["product_spread_score", "inventory_valuation_score", "order_volume_score", "margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C15 requires commodity/material price to convert into realized product spread, inventory valuation, customer volume and margin bridge; material theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 54.23, "MAE_90D_pct": -3.9, "score_return_alignment_label": "spread_positive_MFE_with_later_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R4L84-C15-02", "symbol": "004560", "company_name": "현대비앤지스틸", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE", "case_type": "stainless_nickel_material_theme_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R4L84-C15-02-S2FP-20240312", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_high_MAE_material_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "A nickel/stainless theme should not become Stage2 unless product spread, orderbook, inventory valuation and margin bridge are visible."}
{"row_type": "trigger", "trigger_id": "R4L84-C15-02-S2FP-20240312", "case_id": "R4L84-C15-02", "symbol": "004560", "company_name": "현대비앤지스틸", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|material_spread_supercycle_guardrail|local_4B_timing_after_spread_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-12", "evidence_available_at_that_date": "stainless / nickel / specialty-steel spread theme proxy without realized product-spread and order/margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["commodity_price_or_material_spread_proxy", "product_spread_proxy", "volume_or_mix_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "customer_volume", "cost_pass_through", "gross_margin_conversion"], "stage4b_evidence_fields": ["spread_theme_MFE_without_margin_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_spread_collapse_or_customer_volume_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004560/2024.csv", "profile_path": "atlas/symbol_profiles/004/004560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-12", "entry_price": 20900, "MFE_30D_pct": 7.18, "MFE_90D_pct": 7.18, "MFE_180D_pct": 7.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.66, "MAE_90D_pct": -23.16, "MAE_180D_pct": -41.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 22400, "drawdown_after_peak_pct": -45.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "commodity_theme_MFE_rejected_without_realized_spread_margin_bridge", "four_b_evidence_type": ["spread_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_or_volume_break", "trigger_outcome_label": "short_MFE_high_MAE_material_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2003_CA_candidates", "same_entry_group_id": "R4L84-C15-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L84-C15-02", "trigger_id": "R4L84-C15-02-S2FP-20240312", "symbol": "004560", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_price_score": 45, "product_spread_score": 10, "inventory_valuation_score": 10, "order_volume_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "cost_pass_through_score": 5, "4B_watch_score": 55}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"commodity_price_score": 45, "product_spread_score": 0, "inventory_valuation_score": 0, "order_volume_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "cost_pass_through_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "order_volume_score", "margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C15 requires commodity/material price to convert into realized product spread, inventory valuation, customer volume and margin bridge; material theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 7.18, "MAE_90D_pct": -23.16, "score_return_alignment_label": "short_MFE_high_MAE_material_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R4L84-C15-03", "symbol": "008350", "company_name": "남선알미늄", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE", "case_type": "aluminum_material_policy_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R4L84-C15-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_material_theme_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Aluminum material beta is rejected unless volume, product spread, customer mix and gross-margin conversion are proven at entry."}
{"row_type": "trigger", "trigger_id": "R4L84-C15-03-S2FP-20240213", "case_id": "R4L84-C15-03", "symbol": "008350", "company_name": "남선알미늄", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_STEEL_ALUMINUM_SPREAD_REPRICING_BRIDGE_VS_COMMODITY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|material_spread_supercycle_guardrail|local_4B_timing_after_spread_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "aluminum / infrastructure-material theme proxy without product spread, volume or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["commodity_price_or_material_spread_proxy", "product_spread_proxy", "volume_or_mix_proxy"], "stage3_evidence_fields": ["realized_product_spread", "inventory_valuation", "customer_volume", "cost_pass_through", "gross_margin_conversion"], "stage4b_evidence_fields": ["spread_theme_MFE_without_margin_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_spread_collapse_or_customer_volume_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008350/2024.csv", "profile_path": "atlas/symbol_profiles/008/008350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 2155, "MFE_30D_pct": 1.16, "MFE_90D_pct": 1.16, "MFE_180D_pct": 1.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.23, "MAE_90D_pct": -18.0, "MAE_180D_pct": -41.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-13", "peak_price": 2180, "drawdown_after_peak_pct": -41.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "aluminum_theme_rejected_without_product_spread_volume_margin_bridge", "four_b_evidence_type": ["spread_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_spread_or_volume_break", "trigger_outcome_label": "low_MFE_high_MAE_material_theme_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2009_CA_candidates", "same_entry_group_id": "R4L84-C15-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L84-C15-03", "trigger_id": "R4L84-C15-03-S2FP-20240213", "symbol": "008350", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_price_score": 45, "product_spread_score": 10, "inventory_valuation_score": 10, "order_volume_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "cost_pass_through_score": 5, "4B_watch_score": 55}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"commodity_price_score": 45, "product_spread_score": 0, "inventory_valuation_score": 0, "order_volume_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "cost_pass_through_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["product_spread_score", "inventory_valuation_score", "order_volume_score", "margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C15 requires commodity/material price to convert into realized product spread, inventory valuation, customer volume and margin bridge; material theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 1.16, "MAE_90D_pct": -18.0, "score_return_alignment_label": "low_MFE_high_MAE_material_theme_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C15_material_price_to_product_spread_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Material spread rerating requires realized product spread, inventory valuation, customer volume and gross-margin bridge; commodity or infrastructure-material theme MFE alone fades into high MAE.", "backtest_effect": "keeps 103140 with local 4B watch; demotes 004560/008350 material-theme false positives", "trigger_ids": "R4L84-C15-01-S2A-20240307|R4L84-C15-02-S2FP-20240312|R4L84-C15-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R4", "loop": 84, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["material_theme_false_positive_high_MAE", "commodity_price_to_product_spread_margin_bridge_required", "local_4B_late_after_spread_MFE", "source_proxy_runtime_promotion_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C15, test a canonical-archetype guard requiring realized product spread, inventory valuation, customer volume and margin bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 84
next_round = R5
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
