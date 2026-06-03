# E2R Stock-Web v12 Residual Research — R12 Loop 86 / L10 / C31

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 86,
  "computed_next_round": "R13",
  "computed_next_loop": 86,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE",
  "loop_objective": [
    "under_covered_agri_food_policy_extension",
    "coverage_gap_fill",
    "counterexample_mining",
    "agri_food_grain_input_cost_guardrail",
    "grain_supply_policy_theme_vs_input_cost_margin_bridge_test",
    "feed_grain_theme_MFE_vs_inventory_pass_through_margin_bridge_test",
    "local_4B_timing_after_agri_food_MFE",
    "hard_4C_non_price_supply_or_margin_break_protection",
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
scheduled_loop = 86
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R12 is the policy / under-covered service-agri extension slot. This run selects an under-covered agri-food fine route under C31, avoiding loop86 R11's C32 tender-control-premium route and loop85 R12's education-policy C31 route.

The tested mechanism:

```text
agri-food / grain supply / input-cost policy headline
→ direct beneficiary mapping
→ input-cost trend and inventory valuation
→ pricing pass-through and channel demand
→ gross / OP margin conversion
→ durable rerating or feed/grain theme spike fade
```

C31 here is the pantry and the grain silo. A grain headline can move the price, but the rerating only holds when inventory, pass-through and margin move through the income statement.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols include `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top-covered set and uses:

```text
097950 / CJ제일제당
002140 / 고려산업
027710 / 팜스토리
```

All three are treated as new independent C31 agri-food / grain input-cost cases for this loop. No hard duplicate is intentionally reused.

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
| 097950 | CJ제일제당 | `atlas/symbol_profiles/097/097950.json` | no profile-level CA candidate |
| 002140 | 고려산업 | `atlas/symbol_profiles/002/002140.json` | old CA candidates through 2013; selected 2024 forward window clean |
| 027710 | 팜스토리 | `atlas/symbol_profiles/027/027710.json` | old CA candidates through 2019; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R12L86-C31-01 | 097950 | 2024-02-13 | 298,000 | 180D | clean | true |
| R12L86-C31-02 | 002140 | 2024-01-17 | 3,495 | 180D | clean | true |
| R12L86-C31-03 | 027710 | 2024-01-17 | 1,707 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | FOOD_INPUT_COST_MARGIN_RECOVERY | keep Stage2 with input-cost trend, inventory valuation, pricing pass-through and margin bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | FEED_GRAIN_SUPPLY_THEME_SPIKE | reject same-week feed/grain MFE without inventory/pass-through/margin bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | FEED_LIVESTOCK_POLICY_THEME_FADE | reject feed/livestock theme MFE without cost spread and sell-through evidence |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R12L86-C31-01 | 097950 | CJ제일제당 | Stage2-Actionable | 2024-02-13 | 298,000 | 36.74 | -5.54 | current_profile_partially_correct_food_margin_bridge_watch_needed |
| R12L86-C31-02 | 002140 | 고려산업 | Stage2-FalsePositive | 2024-01-17 | 3,495 | 17.31 | -32.05 | current_profile_false_positive_high_MAE_theme_spike |
| R12L86-C31-03 | 027710 | 팜스토리 | Stage2-FalsePositive | 2024-01-17 | 1,707 | 12.54 | -25.19 | current_profile_false_positive_high_MAE_feed_theme |

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

This MD creates a source-repair queue and a C31 agri-food shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: food-input-cost trend, grain-price or supply policy source, inventory valuation, pricing pass-through, channel demand, gross/OP margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 097950 | `atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv` | `atlas/symbol_profiles/097/097950.json` |
| 002140 | `atlas/ohlcv_tradable_by_symbol_year/002/002140/2024.csv` | `atlas/symbol_profiles/002/002140.json` |
| 027710 | `atlas/ohlcv_tradable_by_symbol_year/027/027710/2024.csv` | `atlas/symbol_profiles/027/027710.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 097950 / CJ제일제당

C31 agri-food input-cost / margin recovery positive with local 4B watch. The February entry produced a later MFE into June as food margin conditions improved. This is a positive row, but clean Green requires input-cost, inventory and pricing-pass-through source repair.

### Case 2 — 002140 / 고려산업

C31 feed/grain supply-policy theme false positive. The January spike produced an immediate MFE, but the later MAE was much deeper. Feed/grain policy heat without inventory and pass-through bridge should not validate Stage2.

### Case 3 — 027710 / 팜스토리

C31 feed/livestock grain-policy theme false positive. Similar to 002140, the same-week MFE faded into a deeper drawdown. This strengthens the high-MAE guardrail for agri-food theme rows.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 097950 | 298,000 | 4.19 | -5.54 | 9.73 | -5.54 | 36.74 | -5.54 | 2024-06-26 / 407,500 | -28.83 |
| 002140 | 3,495 | 17.31 | -10.30 | 17.31 | -13.73 | 17.31 | -32.05 | 2024-01-18 / 4,100 | -42.07 |
| 027710 | 1,707 | 12.54 | -7.79 | 12.54 | -11.01 | 12.54 | -25.19 | 2024-01-18 / 1,921 | -33.52 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R12L86-C31-01 | Stage2-Actionable if input-cost/margin bridge exists | delayed MFE, controlled early MAE | partially correct; source repair needed |
| R12L86-C31-02 | risk of treating feed/grain spike as Stage2 | MFE then deep MAE | false positive |
| R12L86-C31-03 | risk of treating feed/livestock spike as Stage2 | MFE then high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C31 agri-food, the residual is whether food/grain MFE becomes clean Stage2/Green before input-cost trend, inventory valuation, pass-through pricing and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R12L86-C31-01 | 0.70 | 0.60 | local 4B watch after food-margin MFE if input-cost/inventory/pricing bridge stalls |
| R12L86-C31-02 | 0.35 | 0.30 | feed/grain policy theme rejected without inventory/pass-through/margin bridge |
| R12L86-C31-03 | 0.35 | 0.30 | feed/livestock theme rejected without inventory/cost/pass-through bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_supply_inventory_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C31 agri-food hard 4C requires confirmed supply-policy reversal, input-cost shock, inventory impairment, pass-through failure, channel demand break or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L10/C31 agri-food rows need input-cost trend, inventory valuation, pricing pass-through, channel demand and gross/OP margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = C31_agri_food_input_cost_inventory_pass_through_margin_bridge_required
effect = keep food-margin positive with local 4B watch; demote feed/grain policy theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 13.19 | -10.09 | may over-credit feed/grain policy spike without margin bridge | needs C31 agri-food bridge repair |
| P1 canonical shadow bridge profile | 3 | 9.73 on kept positive at 90D / 36.74 at 180D | demotes 002140/027710 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R12L86-C31-01 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + local 4B/input-cost-margin watch | partially aligned |
| R12L86-C31-02 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Feed-grain theme RiskWatch | improved |
| R12L86-C31-03 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Feed-grain theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - feed_grain_theme_false_positive_high_MAE
  - input_cost_inventory_pass_through_margin_bridge_required
  - agri_policy_theme_spike_without_margin_bridge
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_supply_inventory_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C31_agri_food_input_cost_inventory_pass_through_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C31_agri_food_input_cost_inventory_pass_through_margin_bridge_required
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
- official agri-food supply or grain policy source
- input-cost trend and inventory-valuation evidence
- pricing pass-through and channel demand
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_agri_food_input_cost_inventory_pass_through_margin_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require input-cost trend, inventory valuation, pricing pass-through, channel demand and gross/OP margin bridge before clean Stage2/Green","keeps 097950 with local 4B/input-cost-margin watch; demotes 002140/027710","R12L86-C31-01-S2A-20240213|R12L86-C31-02-S2FP-20240117|R12L86-C31-03-S2FP-20240117",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L86-C31-01", "symbol": "097950", "company_name": "CJ제일제당", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "case_type": "food_input_cost_margin_recovery_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L86-C31-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "food_margin_MFE_positive_but_input_cost_inventory_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_food_margin_bridge_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C31 agri/food positives need input-cost trend, inventory valuation, pricing/pass-through, channel demand and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R12L86-C31-01-S2A-20240213", "case_id": "R12L86-C31-01", "symbol": "097950", "company_name": "CJ제일제당", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "loop_objective": "under_covered_agri_food_policy_extension|coverage_gap_fill|counterexample_mining|agri_food_input_cost_margin_guardrail|feed_grain_theme_false_positive_review", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "food ingredient / grain-input-cost normalization / processed-food margin recovery and policy-supply proxy; primary input-cost, inventory and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["agri_food_policy_or_supply_proxy", "input_cost_or_grain_price_proxy", "beneficiary_proxy"], "stage3_evidence_fields": ["input_cost_trend", "inventory_valuation", "pricing_pass_through", "channel_demand", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["agri_food_MFE_without_margin_bridge", "grain_theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_supply_reversal_inventory_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "profile_path": "atlas/symbol_profiles/097/097950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 298000, "MFE_30D_pct": 4.19, "MFE_90D_pct": 9.73, "MFE_180D_pct": 36.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.54, "MAE_90D_pct": -5.54, "MAE_180D_pct": -5.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 407500, "drawdown_after_peak_pct": -28.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "local_4B_watch_after_food_margin_MFE_if_input_cost_inventory_pricing_margin_bridge_stalls", "four_b_evidence_type": ["agri_food_MFE_without_input_cost_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_supply_inventory_or_margin_break", "trigger_outcome_label": "food_margin_MFE_positive_but_input_cost_inventory_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_food_margin_bridge_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R12L86-C31-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L86-C31-01", "trigger_id": "R12L86-C31-01-S2A-20240213", "symbol": "097950", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_supply_specificity_score": 45, "direct_beneficiary_mapping_score": 45, "input_cost_trend_score": 55, "inventory_valuation_score": 45, "pricing_pass_through_score": 45, "channel_demand_score": 40, "gross_margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 55, "theme_blowoff_risk_score": 50, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"policy_or_supply_specificity_score": 45, "direct_beneficiary_mapping_score": 45, "input_cost_trend_score": 55, "inventory_valuation_score": 45, "pricing_pass_through_score": 45, "channel_demand_score": 40, "gross_margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 55, "theme_blowoff_risk_score": 50, "execution_risk_score": 55, "source_quality_score": 10, "4B_watch_score": 80, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/input-cost-margin watch", "changed_components": ["input_cost_trend_score", "inventory_valuation_score", "pricing_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C31 agri/food rows require policy/supply or grain-input-cost MFE to convert into input-cost trend, inventory valuation, pricing pass-through, channel demand and margin conversion before clean Stage2/Green; feed/grain theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 9.73, "MAE_90D_pct": -5.54, "score_return_alignment_label": "food_margin_MFE_positive_but_input_cost_inventory_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_food_margin_bridge_watch_needed"}
{"row_type": "case", "case_id": "R12L86-C31-02", "symbol": "002140", "company_name": "고려산업", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "case_type": "feed_grain_supply_policy_theme_spike_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R12L86-C31-02-S2FP-20240117", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "same_week_grain_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_theme_spike", "price_source": "Songdaiki/stock-web", "notes": "Feed/grain policy theme heat should not validate Stage2 unless inventory position, input-cost spread, pass-through pricing and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R12L86-C31-02-S2FP-20240117", "case_id": "R12L86-C31-02", "symbol": "002140", "company_name": "고려산업", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "loop_objective": "under_covered_agri_food_policy_extension|coverage_gap_fill|counterexample_mining|agri_food_input_cost_margin_guardrail|feed_grain_theme_false_positive_review", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-17", "evidence_available_at_that_date": "feed/grain supply policy and global grain-price shock theme proxy without confirmed inventory, pass-through or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["agri_food_policy_or_supply_proxy", "input_cost_or_grain_price_proxy", "beneficiary_proxy"], "stage3_evidence_fields": ["input_cost_trend", "inventory_valuation", "pricing_pass_through", "channel_demand", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["agri_food_MFE_without_margin_bridge", "grain_theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_supply_reversal_inventory_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002140/2024.csv", "profile_path": "atlas/symbol_profiles/002/002140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-17", "entry_price": 3495, "MFE_30D_pct": 17.31, "MFE_90D_pct": 17.31, "MFE_180D_pct": 17.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.3, "MAE_90D_pct": -13.73, "MAE_180D_pct": -32.05, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 4100, "drawdown_after_peak_pct": -42.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "feed_grain_policy_theme_MFE_rejected_without_inventory_pass_through_margin_bridge", "four_b_evidence_type": ["agri_food_MFE_without_input_cost_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_supply_inventory_or_margin_break", "trigger_outcome_label": "same_week_grain_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_theme_spike", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2013_CA_candidate", "same_entry_group_id": "R12L86-C31-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L86-C31-02", "trigger_id": "R12L86-C31-02-S2FP-20240117", "symbol": "002140", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_supply_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "input_cost_trend_score": 15, "inventory_valuation_score": 5, "pricing_pass_through_score": 5, "channel_demand_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_or_supply_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "input_cost_trend_score": 0, "inventory_valuation_score": 0, "pricing_pass_through_score": 0, "channel_demand_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Feed-grain theme RiskWatch", "changed_components": ["input_cost_trend_score", "inventory_valuation_score", "pricing_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C31 agri/food rows require policy/supply or grain-input-cost MFE to convert into input-cost trend, inventory valuation, pricing pass-through, channel demand and margin conversion before clean Stage2/Green; feed/grain theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 17.31, "MAE_90D_pct": -13.73, "score_return_alignment_label": "same_week_grain_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_theme_spike"}
{"row_type": "case", "case_id": "R12L86-C31-03", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "case_type": "feed_livestock_grain_policy_theme_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L86-C31-03-S2FP-20240117", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "feed_livestock_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_feed_theme", "price_source": "Songdaiki/stock-web", "notes": "Feed/livestock agri-policy MFE should remain RiskWatch unless inventory cost, feed spread, selling-price pass-through and margin bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R12L86-C31-03-S2FP-20240117", "case_id": "R12L86-C31-03", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "loop_objective": "under_covered_agri_food_policy_extension|coverage_gap_fill|counterexample_mining|agri_food_input_cost_margin_guardrail|feed_grain_theme_false_positive_review", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-17", "evidence_available_at_that_date": "feed/livestock grain policy and food-supply theme proxy without confirmed inventory benefit, price pass-through, demand or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["agri_food_policy_or_supply_proxy", "input_cost_or_grain_price_proxy", "beneficiary_proxy"], "stage3_evidence_fields": ["input_cost_trend", "inventory_valuation", "pricing_pass_through", "channel_demand", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["agri_food_MFE_without_margin_bridge", "grain_theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_supply_reversal_inventory_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/027/027710/2024.csv", "profile_path": "atlas/symbol_profiles/027/027710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-17", "entry_price": 1707, "MFE_30D_pct": 12.54, "MFE_90D_pct": 12.54, "MFE_180D_pct": 12.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.79, "MAE_90D_pct": -11.01, "MAE_180D_pct": -25.19, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 1921, "drawdown_after_peak_pct": -33.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "feed_livestock_theme_MFE_rejected_without_inventory_cost_pass_through_margin_bridge", "four_b_evidence_type": ["agri_food_MFE_without_input_cost_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_supply_inventory_or_margin_break", "trigger_outcome_label": "feed_livestock_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_feed_theme", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2019_CA_candidate", "same_entry_group_id": "R12L86-C31-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L86-C31-03", "trigger_id": "R12L86-C31-03-S2FP-20240117", "symbol": "027710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_supply_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "input_cost_trend_score": 15, "inventory_valuation_score": 5, "pricing_pass_through_score": 5, "channel_demand_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_or_supply_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "input_cost_trend_score": 0, "inventory_valuation_score": 0, "pricing_pass_through_score": 0, "channel_demand_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Feed-grain theme RiskWatch", "changed_components": ["input_cost_trend_score", "inventory_valuation_score", "pricing_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C31 agri/food rows require policy/supply or grain-input-cost MFE to convert into input-cost trend, inventory valuation, pricing pass-through, channel demand and margin conversion before clean Stage2/Green; feed/grain theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 12.54, "MAE_90D_pct": -11.01, "score_return_alignment_label": "feed_livestock_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_feed_theme"}
{"row_type": "shadow_weight", "axis": "C31_agri_food_input_cost_inventory_pass_through_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Agri/food policy-supply rerating requires input-cost trend, inventory valuation, pricing pass-through, channel demand and gross/OP margin conversion; feed/grain theme MFE without bridge fades into high MAE.", "backtest_effect": "keeps 097950 with local 4B/input-cost-margin watch; demotes 002140/027710 feed-grain theme false positives", "trigger_ids": "R12L86-C31-01-S2A-20240213|R12L86-C31-02-S2FP-20240117|R12L86-C31-03-S2FP-20240117", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R12", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["feed_grain_theme_false_positive_high_MAE", "input_cost_inventory_pass_through_margin_bridge_required", "agri_policy_theme_spike_without_margin_bridge", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_supply_inventory_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C31 agri-food rows, test a canonical-archetype guard requiring input-cost trend, inventory valuation, pricing pass-through, channel demand and gross/OP margin conversion before clean Stage2/Green. Keep hard 4C blocked unless a non-price supply, inventory or margin thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 86
next_round = R13
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
