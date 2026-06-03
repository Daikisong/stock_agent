# E2R Stock-Web v12 Residual Research — R5 Loop 85 / L5 / C20

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 85,
  "computed_next_round": "R6",
  "computed_next_loop": 85,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
  "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "food_global_distribution_guardrail",
    "export_channel_sellthrough_to_margin_bridge_test",
    "global_distribution_theme_vs_reorder_margin_bridge_test",
    "local_4B_timing_after_food_MFE",
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
scheduled_round = R5
scheduled_loop = 85
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
computed_next_round = R6
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R5 is the consumer / brand / distribution round. This run selects C20 because loop83 tested C19 and loop84 tested C18.

The tested mechanism:

```text
K-food / dairy / plant-based / bakery / global-distribution headline
→ channel sell-through
→ reorder cadence and capacity fulfillment
→ ASP / mix and cost pass-through
→ gross-margin conversion
→ durable rerating or food-theme fade
```

C20 is not “food became hot.” It is the shelf test: the product has to leave the shelf, reorder, and carry margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C20 top-covered symbols include `257720`, `090430`, `003230`, `018290`, `051900`, and `192820`. This run avoids that top-covered set and uses:

```text
005180 / 빙그레
017810 / 풀무원
005610 / SPC삼립
```

All three are treated as new independent C20 global food-distribution cases for this loop. No hard duplicate is intentionally reused.

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
| 005180 | 빙그레 | `atlas/symbol_profiles/005/005180.json` | old CA candidates through 1998; selected 2024 forward window clean |
| 017810 | 풀무원 | `atlas/symbol_profiles/017/017810.json` | old 2019 CA candidate; selected 2024 forward window clean |
| 005610 | SPC삼립 | `atlas/symbol_profiles/005/005610.json` | old CA candidates through 2002; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R5L85-C20-01 | 005180 | 2024-04-01 | 58,000 | 180D | clean | true |
| R5L85-C20-02 | 017810 | 2024-04-01 | 11,100 | 180D | clean | true |
| R5L85-C20-03 | 005610 | 2024-04-01 | 58,900 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_FOOD_DAIRY_EXPORT_SELLTHROUGH | keep Stage2 with global sell-through, reorder and margin bridge; local 4B after large MFE |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | PLANT_BASED_GLOBAL_CHANNEL_HIGH_MAE | keep as Stage2 only with high-MAE/reorder-margin RiskWatch |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | BAKERY_DOMESTIC_CHANNEL_THEME_FADE | reject low-MFE distribution theme without export/reorder/margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R5L85-C20-01 | 005180 | 빙그레 | Stage2-Actionable | 2024-04-01 | 58,000 | 104.14 | -5.52 | current_profile_partially_correct_local_4B_watch_needed |
| R5L85-C20-02 | 017810 | 풀무원 | Stage2-Actionable | 2024-04-01 | 11,100 | 65.86 | -17.12 | current_profile_partially_correct_high_MAE_watch_needed |
| R5L85-C20-03 | 005610 | SPC삼립 | Stage2-FalsePositive | 2024-04-01 | 58,900 | 2.55 | -15.96 | current_profile_false_positive_low_MFE |

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

This MD therefore creates a source-repair queue and a C20 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: export channel data, distributor sell-through, reorder cadence, capacity utilization, ASP/mix, cost pass-through, gross-margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 005180 | `atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv` | `atlas/symbol_profiles/005/005180.json` |
| 017810 | `atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv` | `atlas/symbol_profiles/017/017810.json` |
| 005610 | `atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv` | `atlas/symbol_profiles/005/005610.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 005180 / 빙그레

C20 K-food / dairy global distribution positive with local 4B watch. The price path generated a large MFE after the April entry. The model should keep the positive but not turn it into clean Green unless sell-through, reorder and gross-margin bridge are source-repaired.

### Case 2 — 017810 / 풀무원

C20 plant-based/global food distribution positive with high-MAE watch. The MFE was strong, but the later drawdown means clean Green is unsafe without repaired channel and margin evidence.

### Case 3 — 005610 / SPC삼립

C20 domestic bakery/food distribution false positive. The MFE was very small and the 180D MAE widened. Food-distribution language without export sell-through and reorder bridge should stay RiskWatch.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 005180 | 58,000 | 33.28 | -5.52 | 104.14 | -5.52 | 104.14 | -5.52 | 2024-06-11 / 118,400 | -31.42 |
| 017810 | 11,100 | 36.40 | -6.76 | 65.86 | -6.76 | 65.86 | -17.12 | 2024-06-14 / 18,410 | -23.46 |
| 005610 | 58,900 | 2.55 | -4.58 | 2.55 | -7.81 | 2.55 | -15.96 | 2024-04-02 / 60,400 | -18.05 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R5L85-C20-01 | Stage2-Actionable if sell-through/reorder bridge exists | large MFE, later drawdown | partially correct; local 4B watch needed |
| R5L85-C20-02 | Stage2-Actionable if global-channel story is over-credited | high MFE and later MAE | high-MAE/reorder-margin RiskWatch needed |
| R5L85-C20-03 | risk of treating domestic food distribution as Stage2 | tiny MFE / MAE widening | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C20, the residual is whether global distribution MFE becomes clean Stage2/Green before sell-through, reorder cadence, ASP/mix and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R5L85-C20-01 | 0.85 | 0.75 | local 4B watch after K-food distribution MFE if sell-through margin bridge stalls |
| R5L85-C20-02 | 0.85 | 0.75 | local 4B and high-MAE RiskWatch when global food MFE outruns reorder bridge |
| R5L85-C20-03 | 0.35 | 0.30 | food distribution theme rejected without sell-through/reorder/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_channel_reorder_or_margin_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L5/C20 global food rows need channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
candidate_axis = C20_global_distribution_sellthrough_reorder_margin_bridge_required
effect = keep global-distribution positives with local 4B/high-MAE watch; demote low-MFE domestic food distribution false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 57.52 | -6.70 | may over-credit food/global distribution theme MFE | needs C20 bridge repair |
| P1 canonical shadow bridge profile | 3 | 85.00 on kept positives | -6.14 on kept positives, with high-MAE watch | demotes 005610 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R5L85-C20-01 | 82 | Stage2-Actionable | 79 | Stage2-Actionable + local 4B/global distribution watch | partially aligned |
| R5L85-C20-02 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + high-MAE/reorder-margin RiskWatch | partially aligned |
| R5L85-C20-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / Food-distribution RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - food_distribution_theme_false_positive_low_MFE
  - global_distribution_sellthrough_reorder_margin_bridge_required
  - local_4B_late_after_food_distribution_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C20_global_distribution_sellthrough_reorder_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C20_global_distribution_sellthrough_reorder_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

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
- export-channel or distributor sell-through source
- reorder cadence
- capacity utilization / ASP / mix
- gross-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_global_distribution_sellthrough_reorder_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Require global distribution to convert into export/channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin conversion before clean Stage2/Green","keeps 005180/017810 with local 4B or high-MAE RiskWatch; demotes 005610","R5L85-C20-01-S2A-20240401|R5L85-C20-02-S2A-20240401|R5L85-C20-03-S2FP-20240401",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L85-C20-01", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "case_type": "K_food_dairy_export_distribution_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L85-C20-01-S2A-20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_local_4B_required_after_distribution_MFE", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C20 can keep Stage2 only when global distribution evidence converts into sell-through, reorder cadence, export ASP and gross-margin bridge."}
{"row_type": "trigger", "trigger_id": "R5L85-C20-01-S2A-20240401", "case_id": "R5L85-C20-01", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|food_global_distribution_guardrail|sellthrough_to_reorder_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "K-food / dairy / processed-food global distribution and export sell-through proxy; primary export-channel and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["global_distribution_proxy", "export_channel_proxy", "sellthrough_or_reorder_proxy"], "stage3_evidence_fields": ["confirmed_export_sellthrough", "reorder_cadence", "capacity_fulfillment", "ASP_or_mix", "gross_margin_conversion"], "stage4b_evidence_fields": ["food_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_channel_reorder_break_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 58000, "MFE_30D_pct": 33.28, "MFE_90D_pct": 104.14, "MFE_180D_pct": 104.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.52, "MAE_90D_pct": -5.52, "MAE_180D_pct": -5.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -31.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_after_K_food_distribution_MFE_if_sellthrough_margin_bridge_stalls", "four_b_evidence_type": ["food_distribution_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_channel_reorder_or_margin_break", "trigger_outcome_label": "large_positive_MFE_but_local_4B_required_after_distribution_MFE", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_1998_CA_candidates", "same_entry_group_id": "R5L85-C20-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L85-C20-01", "trigger_id": "R5L85-C20-01-S2A-20240401", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"global_distribution_score": 55, "export_channel_score": 45, "sell_through_score": 40, "reorder_visibility_score": 40, "capacity_fulfillment_score": 35, "ASP_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 70, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"global_distribution_score": 55, "export_channel_score": 45, "sell_through_score": 40, "reorder_visibility_score": 40, "capacity_fulfillment_score": 35, "ASP_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 70, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable + local 4B/global distribution watch", "changed_components": ["global_distribution_score", "export_channel_score", "sell_through_score", "reorder_visibility_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C20 requires global distribution to convert into export/channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin bridge before clean Stage2/Green; food-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 104.14, "MAE_90D_pct": -5.52, "score_return_alignment_label": "large_positive_MFE_but_local_4B_required_after_distribution_MFE", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R5L85-C20-02", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "case_type": "plant_based_global_food_distribution_positive_with_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L85-C20-02-S2A-20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MFE_but_high_MAE_distribution_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Global food-distribution positives need sell-through, reorder, capacity fulfillment and margin conversion before clean Green."}
{"row_type": "trigger", "trigger_id": "R5L85-C20-02-S2A-20240401", "case_id": "R5L85-C20-02", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|food_global_distribution_guardrail|sellthrough_to_reorder_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "plant-based / tofu / global food distribution and US-channel sell-through proxy; primary reorder and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["global_distribution_proxy", "export_channel_proxy", "sellthrough_or_reorder_proxy"], "stage3_evidence_fields": ["confirmed_export_sellthrough", "reorder_cadence", "capacity_fulfillment", "ASP_or_mix", "gross_margin_conversion"], "stage4b_evidence_fields": ["food_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_channel_reorder_break_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv", "profile_path": "atlas/symbol_profiles/017/017810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 11100, "MFE_30D_pct": 36.4, "MFE_90D_pct": 65.86, "MFE_180D_pct": 65.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.76, "MAE_90D_pct": -6.76, "MAE_180D_pct": -17.12, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 18410, "drawdown_after_peak_pct": -23.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_and_high_MAE_RiskWatch_when_global_food_MFE_outruns_reorder_margin_bridge", "four_b_evidence_type": ["food_distribution_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_channel_reorder_or_margin_break", "trigger_outcome_label": "high_MFE_but_high_MAE_distribution_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2019_CA_candidate", "same_entry_group_id": "R5L85-C20-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L85-C20-02", "trigger_id": "R5L85-C20-02-S2A-20240401", "symbol": "017810", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"global_distribution_score": 55, "export_channel_score": 45, "sell_through_score": 40, "reorder_visibility_score": 40, "capacity_fulfillment_score": 35, "ASP_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 60, "valuation_blowoff_risk_score": 70, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"global_distribution_score": 55, "export_channel_score": 45, "sell_through_score": 40, "reorder_visibility_score": 40, "capacity_fulfillment_score": 35, "ASP_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 60, "valuation_blowoff_risk_score": 70, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + high-MAE/reorder-margin RiskWatch", "changed_components": ["global_distribution_score", "export_channel_score", "sell_through_score", "reorder_visibility_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C20 requires global distribution to convert into export/channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin bridge before clean Stage2/Green; food-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 65.86, "MAE_90D_pct": -6.76, "score_return_alignment_label": "high_MFE_but_high_MAE_distribution_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R5L85-C20-03", "symbol": "005610", "company_name": "SPC삼립", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "case_type": "bakery_food_distribution_theme_low_MFE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R5L85-C20-03-S2FP-20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_food_distribution_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE", "price_source": "Songdaiki/stock-web", "notes": "Domestic food distribution/bakery theme is rejected unless channel sell-through, reorder cadence, cost pass-through and gross-margin bridge are proven at entry."}
{"row_type": "trigger", "trigger_id": "R5L85-C20-03-S2FP-20240401", "case_id": "R5L85-C20-03", "symbol": "005610", "company_name": "SPC삼립", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|food_global_distribution_guardrail|sellthrough_to_reorder_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "bakery / food distribution / domestic-channel margin recovery proxy without export sell-through and reorder margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["global_distribution_proxy", "export_channel_proxy", "sellthrough_or_reorder_proxy"], "stage3_evidence_fields": ["confirmed_export_sellthrough", "reorder_cadence", "capacity_fulfillment", "ASP_or_mix", "gross_margin_conversion"], "stage4b_evidence_fields": ["food_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_channel_reorder_break_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv", "profile_path": "atlas/symbol_profiles/005/005610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 58900, "MFE_30D_pct": 2.55, "MFE_90D_pct": 2.55, "MFE_180D_pct": 2.55, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.58, "MAE_90D_pct": -7.81, "MAE_180D_pct": -15.96, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-02", "peak_price": 60400, "drawdown_after_peak_pct": -18.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "food_distribution_theme_rejected_without_sellthrough_reorder_margin_bridge", "four_b_evidence_type": ["food_distribution_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_channel_reorder_or_margin_break", "trigger_outcome_label": "low_MFE_high_MAE_food_distribution_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2002_CA_candidates", "same_entry_group_id": "R5L85-C20-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L85-C20-03", "trigger_id": "R5L85-C20-03-S2FP-20240401", "symbol": "005610", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"global_distribution_score": 20, "export_channel_score": 10, "sell_through_score": 10, "reorder_visibility_score": 5, "capacity_fulfillment_score": 20, "ASP_or_mix_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 45, "execution_risk_score": 70, "source_quality_score": 15, "4B_watch_score": 65}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"global_distribution_score": 10, "export_channel_score": 0, "sell_through_score": 0, "reorder_visibility_score": 0, "capacity_fulfillment_score": 20, "ASP_or_mix_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 45, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / Food-distribution RiskWatch", "changed_components": ["global_distribution_score", "export_channel_score", "sell_through_score", "reorder_visibility_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C20 requires global distribution to convert into export/channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin bridge before clean Stage2/Green; food-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 2.55, "MAE_90D_pct": -7.81, "score_return_alignment_label": "low_MFE_high_MAE_food_distribution_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE"}
{"row_type": "shadow_weight", "axis": "C20_global_distribution_sellthrough_reorder_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Beauty/food global distribution rerating requires export/channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin conversion; food distribution theme MFE without bridge fades or needs local 4B/high-MAE watch.", "backtest_effect": "keeps 005180/017810 with local 4B or high-MAE RiskWatch; demotes 005610 low-MFE distribution false positive", "trigger_ids": "R5L85-C20-01-S2A-20240401|R5L85-C20-02-S2A-20240401|R5L85-C20-03-S2FP-20240401", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R5", "loop": 85, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["food_distribution_theme_false_positive_low_MFE", "global_distribution_sellthrough_reorder_margin_bridge_required", "local_4B_late_after_food_distribution_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C20, test a canonical-archetype guard requiring export/channel sell-through, reorder cadence, capacity fulfillment, ASP/mix and gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 85
next_round = R6
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
