# E2R Stock-Web v12 Residual Research — R12 Loop 84 / L10 / C31

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 84,
  "computed_next_round": "R13",
  "computed_next_loop": 84,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE",
  "loop_objective": [
    "under_covered_service_agri_extension",
    "coverage_gap_fill",
    "counterexample_mining",
    "agri_food_policy_input_cost_guardrail",
    "food_security_grain_sugar_feed_price_theme_vs_margin_bridge_test",
    "local_4B_timing_after_agri_food_MFE",
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
scheduled_round = R12
scheduled_loop = 84
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R12 is the policy / under-covered service-agri extension slot. This run uses an agri-food fine route under C31 rather than repeating utility, tourism or governance event work.

The tested mechanism:

```text
food security / sugar / feed / import-quota / price-policy headline
→ direct beneficiary mapping
→ raw-material or input-cost bridge
→ inventory valuation and ASP pass-through
→ volume / livestock demand
→ gross-margin conversion
→ durable rerating or food-policy theme fade
```

A food-security headline is like a weather alert. It only becomes a company rerating if the alert changes cost, inventory, selling price and margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 is already wide and top-covered in `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top-covered set and uses:

```text
136490 / 선진
001790 / 대한제당
027710 / 팜스토리
```

All three are treated as new independent C31 agri-food policy/input-cost cases for this loop. No hard duplicate is intentionally reused.

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
| 136490 | 선진 | `atlas/symbol_profiles/136/136490.json` | old 2017 CA candidates; selected 2024 forward window clean |
| 001790 | 대한제당 | `atlas/symbol_profiles/001/001790.json` | old CA candidates through 2021; selected 2024 forward window clean |
| 027710 | 팜스토리 | `atlas/symbol_profiles/027/027710.json` | old CA candidates through 2019; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R12L84-C31-01 | 136490 | 2024-01-25 | 6,480 | 180D | clean | true |
| R12L84-C31-02 | 001790 | 2024-01-12 | 3,345 | 180D | clean | true |
| R12L84-C31-03 | 027710 | 2024-01-17 | 1,707 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | FEED_LIVESTOCK_INPUT_COST_MARGIN_BRIDGE | keep Stage2 only with input-cost, inventory, livestock spread and margin bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | SUGAR_IMPORT_QUOTA_PRICE_THEME_FADE | reject sugar/import-quota theme without raw-sugar cost, refining spread and ASP pass-through |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | GRAIN_FEED_FOOD_SECURITY_SPIKE_FADE | reject grain/feed theme spike without feed-cost, inventory, demand and gross-margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R12L84-C31-01 | 136490 | 선진 | Stage2-Actionable | 2024-01-25 | 6,480 | 18.21 | -6.64 | current_profile_partially_correct_margin_bridge_watch_needed |
| R12L84-C31-02 | 001790 | 대한제당 | Stage2-FalsePositive | 2024-01-12 | 3,345 | 6.13 | -22.27 | current_profile_false_positive_high_MAE |
| R12L84-C31-03 | 027710 | 팜스토리 | Stage2-FalsePositive | 2024-01-17 | 1,707 | 12.54 | -25.19 | current_profile_false_positive_theme_spike |

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

This MD therefore creates a source-repair queue and a C31 agri-food shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: import quota, feed-grain policy, sugar price policy, raw-material costs, inventory valuation, ASP pass-through, livestock demand, gross-margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 136490 | `atlas/ohlcv_tradable_by_symbol_year/136/136490/2024.csv` | `atlas/symbol_profiles/136/136490.json` |
| 001790 | `atlas/ohlcv_tradable_by_symbol_year/001/001790/2024.csv` | `atlas/symbol_profiles/001/001790.json` |
| 027710 | `atlas/ohlcv_tradable_by_symbol_year/027/027710/2024.csv` | `atlas/symbol_profiles/027/027710.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 136490 / 선진

C31 agri-food positive with margin-bridge watch. The forward path produced controlled MFE and tolerable MAE. It is not clean Green, though, because feed-cost, livestock spread and margin conversion must be source-repaired.

### Case 2 — 001790 / 대한제당

C31 sugar/import-quota false positive. The initial MFE was small and the later drawdown widened. This is a direct example of why sugar/food-price headlines should not become Stage2-Actionable without raw-material cost, refining spread, ASP pass-through and margin bridge.

### Case 3 — 027710 / 팜스토리

C31 grain/feed theme spike false positive. The MFE came quickly, then faded into a persistent MAE. Food-security and feed-grain headlines are tradable heat, not durable rerating evidence by themselves.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 136490 | 6,480 | 13.89 | -1.39 | 18.21 | -1.39 | 18.21 | -6.64 | 2024-03-27 / 7,660 | -21.02 |
| 001790 | 3,345 | 6.13 | -4.04 | 6.13 | -10.76 | 6.13 | -22.27 | 2024-01-18 / 3,550 | -26.76 |
| 027710 | 1,707 | 12.54 | -7.79 | 12.54 | -11.01 | 12.54 | -25.19 | 2024-01-18 / 1,921 | -33.52 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R12L84-C31-01 | Stage2-Actionable if feed/livestock cost bridge exists | controlled MFE and tolerable MAE | partially correct; margin bridge watch needed |
| R12L84-C31-02 | risk of treating sugar/import-quota theme as Stage2 | low MFE / high MAE | false positive |
| R12L84-C31-03 | risk of treating grain/feed theme spike as Stage2 | short MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C31 agri-food rows, the residual is not Green lateness. The residual is whether food-policy MFE becomes clean Stage2/Green before input-cost, inventory, ASP pass-through and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R12L84-C31-01 | 0.65 | 0.55 | local 4B watch after feed-cost MFE if livestock margin bridge stalls |
| R12L84-C31-02 | 0.35 | 0.30 | sugar-policy theme rejected without import-cost/spread/margin bridge |
| R12L84-C31-03 | 0.35 | 0.30 | grain/feed theme MFE rejected without inventory/cost/livestock margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_import_policy_or_cost_spread_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = C31 agri/food-policy rows need direct beneficiary mapping plus input-cost, inventory, ASP pass-through, demand and gross-margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = C31_agri_food_policy_input_cost_inventory_margin_bridge_required
effect = keep bridge-positive agri rows with margin-watch; demote grain/sugar/feed theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 12.29 | -7.72 | may over-credit food-security / sugar / feed theme MFE | needs C31 agri-food bridge repair |
| P1 canonical shadow bridge profile | 3 | 18.21 on kept positive | -1.39 on kept positive | demotes 001790/027710 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R12L84-C31-01 | 74 | Stage2-Actionable | 72 | Stage2-Actionable + margin-bridge/local 4B watch | partially aligned |
| R12L84-C31-02 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / Food-policy theme RiskWatch | improved |
| R12L84-C31-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / Food-policy theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - agri_food_policy_theme_false_positive_high_MAE
  - input_cost_inventory_ASP_margin_bridge_required
  - local_4B_late_after_food_policy_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_import_policy_or_cost_spread_break_not_price_only
new_axis_proposed: false
existing_axis_strengthened:
  - C31_agri_food_policy_input_cost_inventory_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C31_agri_food_policy_input_cost_inventory_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

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
- import quota or food-price policy source
- grain/feed/sugar raw-material cost detail
- inventory valuation
- ASP pass-through and livestock demand
- gross-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_agri_food_policy_input_cost_inventory_margin_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require direct beneficiary mapping plus raw-material/input-cost bridge, inventory valuation, ASP pass-through, volume/livestock demand and gross-margin conversion before clean Stage2/Green","keeps 136490 with margin-bridge watch; demotes 001790/027710","R12L84-C31-01-S2A-20240125|R12L84-C31-02-S2FP-20240112|R12L84-C31-03-S2FP-20240117",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L84-C31-01", "symbol": "136490", "company_name": "선진", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE", "case_type": "feed_livestock_input_cost_policy_positive_with_margin_bridge_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L84-C31-01-S2A-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "controlled_positive_MFE_but_margin_bridge_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_margin_bridge_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C31 agri/food positives need input-cost pass-through, livestock spread, inventory and gross-margin bridge before clean Stage2/Green."}
{"row_type": "trigger", "trigger_id": "R12L84-C31-01-S2A-20240125", "case_id": "R12L84-C31-01", "symbol": "136490", "company_name": "선진", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE", "loop_objective": "under_covered_service_agri_extension|coverage_gap_fill|counterexample_mining|agri_food_policy_input_cost_guardrail|local_4B_timing_after_agri_food_MFE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "feed/livestock input-cost normalization and food-price policy proxy; primary feed-cost, livestock spread and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["agri_food_policy_proxy", "input_cost_or_import_quota_proxy", "direct_beneficiary_mapping_proxy"], "stage3_evidence_fields": ["raw_material_cost_bridge", "inventory_valuation", "ASP_pass_through", "volume_or_livestock_demand", "gross_margin_conversion"], "stage4b_evidence_fields": ["food_policy_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_import_policy_reversal_or_cost_spread_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136490/2024.csv", "profile_path": "atlas/symbol_profiles/136/136490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 6480, "MFE_30D_pct": 13.89, "MFE_90D_pct": 18.21, "MFE_180D_pct": 18.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.39, "MAE_90D_pct": -1.39, "MAE_180D_pct": -6.64, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-27", "peak_price": 7660, "drawdown_after_peak_pct": -21.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.65, "four_b_full_window_peak_proximity": 0.55, "four_b_timing_verdict": "local_4B_watch_after_feed_cost_MFE_if_livestock_margin_bridge_stalls", "four_b_evidence_type": ["food_policy_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_import_policy_or_cost_spread_break", "trigger_outcome_label": "controlled_positive_MFE_but_margin_bridge_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_margin_bridge_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2017_CA_candidates", "same_entry_group_id": "R12L84-C31-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L84-C31-01", "trigger_id": "R12L84-C31-01-S2A-20240125", "symbol": "136490", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 45, "input_cost_bridge_score": 45, "inventory_valuation_score": 35, "ASP_pass_through_score": 35, "volume_or_livestock_demand_score": 40, "gross_margin_bridge_score": 40, "revision_score": 35, "relative_strength_score": 50, "valuation_blowoff_risk_score": 45, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 40}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 45, "input_cost_bridge_score": 45, "inventory_valuation_score": 35, "ASP_pass_through_score": 35, "volume_or_livestock_demand_score": 40, "gross_margin_bridge_score": 40, "revision_score": 35, "relative_strength_score": 50, "valuation_blowoff_risk_score": 45, "execution_risk_score": 55, "source_quality_score": 10, "4B_watch_score": 70}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + margin-bridge/local 4B watch", "changed_components": ["input_cost_bridge_score", "inventory_valuation_score", "ASP_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C31 agri/food rows require direct beneficiary mapping plus input-cost, inventory, ASP pass-through, volume/livestock demand and gross-margin bridge before clean Stage2/Green; grain/sugar/feed theme MFE alone is demoted.", "MFE_90D_pct": 18.21, "MAE_90D_pct": -1.39, "score_return_alignment_label": "controlled_positive_MFE_but_margin_bridge_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_margin_bridge_watch_needed"}
{"row_type": "case", "case_id": "R12L84-C31-02", "symbol": "001790", "company_name": "대한제당", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE", "case_type": "sugar_import_quota_food_price_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R12L84-C31-02-S2FP-20240112", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_food_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Sugar/import-quota headline should remain RiskWatch unless raw-sugar cost, refining spread, ASP pass-through and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R12L84-C31-02-S2FP-20240112", "case_id": "R12L84-C31-02", "symbol": "001790", "company_name": "대한제당", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE", "loop_objective": "under_covered_service_agri_extension|coverage_gap_fill|counterexample_mining|agri_food_policy_input_cost_guardrail|local_4B_timing_after_agri_food_MFE", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-12", "evidence_available_at_that_date": "sugar price / food inflation / import-quota policy theme proxy without realized refining spread and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["agri_food_policy_proxy", "input_cost_or_import_quota_proxy", "direct_beneficiary_mapping_proxy"], "stage3_evidence_fields": ["raw_material_cost_bridge", "inventory_valuation", "ASP_pass_through", "volume_or_livestock_demand", "gross_margin_conversion"], "stage4b_evidence_fields": ["food_policy_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_import_policy_reversal_or_cost_spread_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001790/2024.csv", "profile_path": "atlas/symbol_profiles/001/001790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-12", "entry_price": 3345, "MFE_30D_pct": 6.13, "MFE_90D_pct": 6.13, "MFE_180D_pct": 6.13, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.04, "MAE_90D_pct": -10.76, "MAE_180D_pct": -22.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 3550, "drawdown_after_peak_pct": -26.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "sugar_policy_theme_rejected_without_import_cost_spread_margin_bridge", "four_b_evidence_type": ["food_policy_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_import_policy_or_cost_spread_break", "trigger_outcome_label": "low_MFE_high_MAE_food_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_2021_CA_candidates", "same_entry_group_id": "R12L84-C31-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L84-C31-02", "trigger_id": "R12L84-C31-02-S2FP-20240112", "symbol": "001790", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 25, "direct_beneficiary_mapping_score": 20, "input_cost_bridge_score": 10, "inventory_valuation_score": 10, "ASP_pass_through_score": 5, "volume_or_livestock_demand_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 65}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 25, "direct_beneficiary_mapping_score": 20, "input_cost_bridge_score": 0, "inventory_valuation_score": 0, "ASP_pass_through_score": 0, "volume_or_livestock_demand_score": 10, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / Food-policy theme RiskWatch", "changed_components": ["input_cost_bridge_score", "inventory_valuation_score", "ASP_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C31 agri/food rows require direct beneficiary mapping plus input-cost, inventory, ASP pass-through, volume/livestock demand and gross-margin bridge before clean Stage2/Green; grain/sugar/feed theme MFE alone is demoted.", "MFE_90D_pct": 6.13, "MAE_90D_pct": -10.76, "score_return_alignment_label": "low_MFE_high_MAE_food_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R12L84-C31-03", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE", "case_type": "grain_feed_food_security_theme_spike_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R12L84-C31-03-S2FP-20240117", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_spike_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_spike", "price_source": "Songdaiki/stock-web", "notes": "Grain/feed theme MFE is not enough; the row needs inventory valuation, feed raw-material cost, livestock demand and margin bridge at entry."}
{"row_type": "trigger", "trigger_id": "R12L84-C31-03-S2FP-20240117", "case_id": "R12L84-C31-03", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_SECURITY_SUGAR_FEED_PRICE_POLICY_INPUT_COST_MARGIN_BRIDGE_VS_GRAIN_THEME_FADE", "loop_objective": "under_covered_service_agri_extension|coverage_gap_fill|counterexample_mining|agri_food_policy_input_cost_guardrail|local_4B_timing_after_agri_food_MFE", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-17", "evidence_available_at_that_date": "grain/feed/food-security policy theme proxy without feed-cost, inventory, livestock demand and gross-margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["agri_food_policy_proxy", "input_cost_or_import_quota_proxy", "direct_beneficiary_mapping_proxy"], "stage3_evidence_fields": ["raw_material_cost_bridge", "inventory_valuation", "ASP_pass_through", "volume_or_livestock_demand", "gross_margin_conversion"], "stage4b_evidence_fields": ["food_policy_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_import_policy_reversal_or_cost_spread_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/027/027710/2024.csv", "profile_path": "atlas/symbol_profiles/027/027710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-17", "entry_price": 1707, "MFE_30D_pct": 12.54, "MFE_90D_pct": 12.54, "MFE_180D_pct": 12.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.79, "MAE_90D_pct": -11.01, "MAE_180D_pct": -25.19, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 1921, "drawdown_after_peak_pct": -33.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "grain_feed_theme_MFE_rejected_without_inventory_cost_livestock_margin_bridge", "four_b_evidence_type": ["food_policy_theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_import_policy_or_cost_spread_break", "trigger_outcome_label": "theme_spike_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_spike", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2019_CA_candidate", "same_entry_group_id": "R12L84-C31-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L84-C31-03", "trigger_id": "R12L84-C31-03-S2FP-20240117", "symbol": "027710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 25, "direct_beneficiary_mapping_score": 20, "input_cost_bridge_score": 10, "inventory_valuation_score": 10, "ASP_pass_through_score": 5, "volume_or_livestock_demand_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 65}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 25, "direct_beneficiary_mapping_score": 20, "input_cost_bridge_score": 0, "inventory_valuation_score": 0, "ASP_pass_through_score": 0, "volume_or_livestock_demand_score": 10, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / Food-policy theme RiskWatch", "changed_components": ["input_cost_bridge_score", "inventory_valuation_score", "ASP_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C31 agri/food rows require direct beneficiary mapping plus input-cost, inventory, ASP pass-through, volume/livestock demand and gross-margin bridge before clean Stage2/Green; grain/sugar/feed theme MFE alone is demoted.", "MFE_90D_pct": 12.54, "MAE_90D_pct": -11.01, "score_return_alignment_label": "theme_spike_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_spike"}
{"row_type": "shadow_weight", "axis": "C31_agri_food_policy_input_cost_inventory_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Agri/food policy rerating requires direct beneficiary mapping plus raw-material/input-cost bridge, inventory valuation, ASP pass-through, volume/livestock demand and gross-margin conversion; food-security or sugar/feed theme MFE alone fades into high MAE.", "backtest_effect": "keeps 136490 with margin-bridge watch; demotes 001790/027710 food-policy theme false positives", "trigger_ids": "R12L84-C31-01-S2A-20240125|R12L84-C31-02-S2FP-20240112|R12L84-C31-03-S2FP-20240117", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R12", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["agri_food_policy_theme_false_positive_high_MAE", "input_cost_inventory_ASP_margin_bridge_required", "local_4B_late_after_food_policy_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_import_policy_or_cost_spread_break_not_price_only"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C31 agri-food rows, test a canonical-archetype guard requiring direct beneficiary mapping plus raw-material/input-cost bridge, inventory valuation, ASP pass-through, volume/livestock demand and gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 84
next_round = R13
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
