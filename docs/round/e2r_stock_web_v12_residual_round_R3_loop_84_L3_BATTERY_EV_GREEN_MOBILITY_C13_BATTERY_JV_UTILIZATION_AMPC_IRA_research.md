# E2R Stock-Web v12 Residual Research — R3 Loop 84 / L3 / C13

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 84,
  "computed_next_round": "R4",
  "computed_next_loop": 84,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "battery_JV_utilization_AMPC_IRA_guardrail",
    "AMPC_policy_benefit_to_volume_margin_bridge_test",
    "local_4B_timing_after_policy_MFE",
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
scheduled_loop = 84
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
computed_next_round = R4
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R3 is the battery / EV / green mobility round. This run selects C13 because R3 loop83 already tested C12 call-off risk, while C13 remains a thinner axis in the No-Repeat ledger.

The tested mechanism:

```text
IRA / AMPC / JV / US-localized capacity headline
→ direct customer and plant mapping
→ customer call-off and volume utilization
→ subsidy capture and cost / ASP pass-through
→ margin conversion
→ durable rerating or local 4B / false-positive fade
```

C13 is not “battery policy beneficiary.” It is the tollbooth where the policy credit must actually turn into shipped volume, utilized capacity, and margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C13 top-covered symbols include `373220`, `006400`, `096770`, `003670`, `020150`, and `051910`. This run avoids that top-covered set and uses:

```text
348370 / 엔켐
005070 / 코스모신소재
025900 / 동화기업
```

All three are treated as new independent C13 battery-JV / utilization / AMPC cases for this loop. No hard duplicate is intentionally reused.

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
| 348370 | 엔켐 | `atlas/symbol_profiles/348/348370.json` | no profile-level CA candidate |
| 005070 | 코스모신소재 | `atlas/symbol_profiles/005/005070.json` | old CA candidates through 2019; selected 2024 forward window clean |
| 025900 | 동화기업 | `atlas/symbol_profiles/025/025900.json` | 2024-05-03 CA candidate; selected entry is after that date |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R3L84-C13-01 | 348370 | 2024-01-15 | 107,000 | 180D | clean | true |
| R3L84-C13-02 | 005070 | 2024-02-13 | 157,100 | 180D | clean | true |
| R3L84-C13-03 | 025900 | 2024-07-16 | 12,470 | 180D | post-CA clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | ELECTROLYTE_US_CAPACITY_AMPC_BLOWOFF | keep Stage2 only with customer call-off/utilization/subsidy capture; add local 4B after extreme MFE |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | CATHODE_LOCALIZATION_CAPACITY_FADE | reject or demote when capacity narrative lacks utilization and margin bridge |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | POST_CA_ELECTROLYTE_DELAYED_SQUEEZE | delayed squeeze after high MAE does not validate original trigger without entry-date bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R3L84-C13-01 | 348370 | 엔켐 | Stage2-Actionable | 2024-01-15 | 107,000 | 268.69 | -6.36 | current_profile_4B_too_late_after_extreme_AMPC_MFE |
| R3L84-C13-02 | 005070 | 코스모신소재 | Stage2-FalsePositive | 2024-02-13 | 157,100 | 23.68 | -38.57 | current_profile_false_positive_high_MAE |
| R3L84-C13-03 | 025900 | 동화기업 | Stage2-FalsePositive | 2024-07-16 | 12,470 | 19.33 | -38.25 | current_profile_false_positive_delayed_squeeze |

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

This MD therefore creates a source-repair queue and a C13 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: IRA/AMPC mechanism, US plant/JV location, customer call-off, utilization, subsidy capture, cost pass-through, margin bridge, company disclosure, report, or official policy source.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 348370 | `atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv` | `atlas/symbol_profiles/348/348370.json` |
| 005070 | `atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv` | `atlas/symbol_profiles/005/005070.json` |
| 025900 | `atlas/ohlcv_tradable_by_symbol_year/025/025900/2024.csv` and `2025.csv` | `atlas/symbol_profiles/025/025900.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 348370 / 엔켐

C13 high-MFE positive with mandatory local 4B. The policy/localization MFE was extremely strong, but the post-peak drawdown shows why the model cannot wait for a full-window 4B. It should keep Stage2 only if source repair confirms customer location, call-off, utilization, subsidy capture and margin bridge.

### Case 2 — 005070 / 코스모신소재

C13 capacity-localization false positive. The initial upside was tradable, but the later MAE was too deep. The model should not treat cathode capacity or localization narrative as Stage2-Actionable without utilization, ASP and customer call-off evidence.

### Case 3 — 025900 / 동화기업

C13 post-CA electrolyte false positive / delayed squeeze. The entry is deliberately after the 2024-05-03 CA candidate. Even then, the path shows a delayed spike after a wide drawdown. That late squeeze should not validate the original Stage2 trigger unless customer utilization evidence was already available at entry.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 348370 | 107,000 | 235.05 | -6.36 | 268.69 | -6.36 | 268.69 | -6.36 | 2024-04-08 / 394,500 | -62.23 |
| 005070 | 157,100 | 23.68 | -1.85 | 23.68 | -20.43 | 23.68 | -38.57 | 2024-02-21 / 194,300 | -50.33 |
| 025900 | 12,470 | 10.51 | -8.42 | 15.32 | -16.28 | 19.33 | -38.25 | 2025-02-21 / 14,880 | -48.25 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R3L84-C13-01 | Stage2-Actionable if AMPC/JV bridge exists | extreme MFE, later deep drawdown | 4B too late after extreme AMPC MFE |
| R3L84-C13-02 | risk of treating capacity localization as Stage2 | short MFE / high MAE | false positive |
| R3L84-C13-03 | risk of treating delayed post-CA squeeze as validation | high MAE before delayed MFE | false positive / delayed squeeze |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C13, the residual is not Green lateness. The residual is whether AMPC/JV/localization policy MFE becomes Stage2-Actionable before customer call-off, utilization, subsidy capture and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R3L84-C13-01 | 0.95 | 0.85 | local 4B watch required when AMPC policy MFE outruns volume/margin bridge |
| R3L84-C13-02 | 0.75 | 0.65 | policy/capacity MFE should be local 4B or reject without utilization bridge |
| R3L84-C13-03 | 0.35 | 0.30 | delayed post-CA squeeze not valid Stage2 without customer utilization bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_calloff_or_subsidy_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L3 battery AMPC/JV rows need customer call-off, utilization, subsidy capture and margin bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
candidate_axis = C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required
effect = keep extreme-MFE positive only with local 4B watch; demote policy/localization false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 102.56 | -14.36 | may over-credit AMPC/localization policy MFE | needs C13 bridge repair |
| P1 canonical shadow bridge profile | 3 | 268.69 on kept positive | -6.36 on kept positive | demotes 005070/025900 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R3L84-C13-01 | 82 | Stage2-Actionable | 79 | Stage2-Actionable + local 4B/high-MAE watch | partially aligned |
| R3L84-C13-02 | 60 | Stage2-Watch/FalsePositive | 48 | Rejected-Stage2 / RiskWatch | improved |
| R3L84-C13-03 | 60 | Stage2-Watch/FalsePositive | 48 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 3 | no | yes | source repair needed |

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
  - AMPC_policy_theme_false_positive_high_MAE
  - local_4B_late_after_extreme_policy_MFE
  - customer_calloff_utilization_margin_bridge_required
  - source_proxy_runtime_promotion_risk
  - post_CA_battery_material_squeeze_not_original_stage2_validation
new_axis_proposed: false
existing_axis_strengthened:
  - C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.

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
- official IRA/AMPC subsidy source
- customer call-off and utilization detail
- subsidy capture and cost pass-through bridge
- margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"Require IRA/AMPC/JV capacity to convert into customer call-off, volume utilization, subsidy capture and margin bridge before Stage2-Actionable","keeps 348370 with local 4B watch; demotes 005070/025900","R3L84-C13-01-S2A-20240115|R3L84-C13-02-S2FP-20240213|R3L84-C13-03-S2FP-20240716",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L84-C13-01", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE", "case_type": "electrolyte_US_capacity_AMPC_positive_with_blowoff_4B", "positive_or_counterexample": "positive", "best_trigger": "R3L84-C13-01-S2A-20240115", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_local_4B_required", "current_profile_verdict": "current_profile_4B_too_late_after_extreme_AMPC_MFE", "price_source": "Songdaiki/stock-web", "notes": "C13 can keep Stage2 only when IRA/AMPC/JV capacity translates into customer volume, utilization, subsidy capture and margin bridge."}
{"row_type": "trigger", "trigger_id": "R3L84-C13-01-S2A-20240115", "case_id": "R3L84-C13-01", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_JV_utilization_AMPC_IRA_guardrail|local_4B_timing_after_policy_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-15", "evidence_available_at_that_date": "electrolyte US capacity / IRA-AMPC beneficiary and customer-location bridge proxy; primary evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["AMPC_or_IRA_policy_proxy", "JV_or_US_capacity_proxy", "customer_location_proxy"], "stage3_evidence_fields": ["customer_calloff", "volume_utilization", "subsidy_capture", "ASP_or_cost_pass_through", "margin_conversion"], "stage4b_evidence_fields": ["policy_MFE_without_utilization_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_or_subsidy_reversal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-15", "entry_price": 107000, "MFE_30D_pct": 235.05, "MFE_90D_pct": 268.69, "MFE_180D_pct": 268.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.36, "MAE_90D_pct": -6.36, "MAE_180D_pct": -6.36, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 394500, "drawdown_after_peak_pct": -62.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "local_4B_watch_required_when_AMPC_policy_MFE_outruns_volume_margin_bridge", "four_b_evidence_type": ["policy_MFE_without_utilization_bridge", "valuation_blowoff", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_calloff_or_subsidy_break", "trigger_outcome_label": "large_positive_MFE_but_local_4B_required", "current_profile_verdict": "current_profile_4B_too_late_after_extreme_AMPC_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R3L84-C13-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L84-C13-01", "trigger_id": "R3L84-C13-01-S2A-20240115", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"AMPC_policy_specificity_score": 55, "JV_or_US_capacity_score": 60, "customer_volume_bridge_score": 45, "utilization_score": 40, "margin_bridge_score": 35, "revision_score": 50, "relative_strength_score": 80, "valuation_blowoff_risk_score": 85, "execution_risk_score": 50, "source_quality_score": 20, "calloff_risk_score": 35, "4B_watch_score": 45}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"AMPC_policy_specificity_score": 55, "JV_or_US_capacity_score": 60, "customer_volume_bridge_score": 45, "utilization_score": 40, "margin_bridge_score": 35, "revision_score": 50, "relative_strength_score": 80, "valuation_blowoff_risk_score": 90, "execution_risk_score": 50, "source_quality_score": 10, "calloff_risk_score": 35, "4B_watch_score": 90}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable + local 4B/high-MAE watch", "changed_components": ["customer_volume_bridge_score", "utilization_score", "margin_bridge_score", "source_quality_score", "calloff_risk_score", "4B_watch_score"], "component_delta_explanation": "C13 requires IRA/AMPC/JV capacity to convert into customer call-off, utilization, subsidy capture and margin bridge; policy or localization MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 268.69, "MAE_90D_pct": -6.36, "score_return_alignment_label": "large_positive_MFE_but_local_4B_required", "current_profile_verdict": "current_profile_4B_too_late_after_extreme_AMPC_MFE"}
{"row_type": "case", "case_id": "R3L84-C13-02", "symbol": "005070", "company_name": "코스모신소재", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE", "case_type": "cathode_capacity_AMPC_theme_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R3L84-C13-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_high_MAE_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Cathode localization/AMPC narrative is not enough if utilization, ASP pass-through and customer call-off bridge are absent."}
{"row_type": "trigger", "trigger_id": "R3L84-C13-02-S2FP-20240213", "case_id": "R3L84-C13-02", "symbol": "005070", "company_name": "코스모신소재", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_JV_utilization_AMPC_IRA_guardrail|local_4B_timing_after_policy_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "cathode capacity / customer localization / policy-beneficiary proxy without confirmed utilization and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["AMPC_or_IRA_policy_proxy", "JV_or_US_capacity_proxy", "customer_location_proxy"], "stage3_evidence_fields": ["customer_calloff", "volume_utilization", "subsidy_capture", "ASP_or_cost_pass_through", "margin_conversion"], "stage4b_evidence_fields": ["policy_MFE_without_utilization_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_or_subsidy_reversal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv", "profile_path": "atlas/symbol_profiles/005/005070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 157100, "MFE_30D_pct": 23.68, "MFE_90D_pct": 23.68, "MFE_180D_pct": 23.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.85, "MAE_90D_pct": -20.43, "MAE_180D_pct": -38.57, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 194300, "drawdown_after_peak_pct": -50.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.65, "four_b_timing_verdict": "policy_capacity_MFE_should_be_local_4B_or_reject_without_utilization_margin_bridge", "four_b_evidence_type": ["policy_MFE_without_utilization_bridge", "valuation_blowoff", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_calloff_or_subsidy_break", "trigger_outcome_label": "short_MFE_high_MAE_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2019_CA_candidates", "same_entry_group_id": "R3L84-C13-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L84-C13-02", "trigger_id": "R3L84-C13-02-S2FP-20240213", "symbol": "005070", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"AMPC_policy_specificity_score": 35, "JV_or_US_capacity_score": 35, "customer_volume_bridge_score": 10, "utilization_score": 10, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "calloff_risk_score": 75, "4B_watch_score": 50}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"AMPC_policy_specificity_score": 35, "JV_or_US_capacity_score": 35, "customer_volume_bridge_score": 0, "utilization_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 5, "calloff_risk_score": 85, "4B_watch_score": 80}, "weighted_score_after": 48, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["customer_volume_bridge_score", "utilization_score", "margin_bridge_score", "source_quality_score", "calloff_risk_score", "4B_watch_score"], "component_delta_explanation": "C13 requires IRA/AMPC/JV capacity to convert into customer call-off, utilization, subsidy capture and margin bridge; policy or localization MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 23.68, "MAE_90D_pct": -20.43, "score_return_alignment_label": "short_MFE_high_MAE_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R3L84-C13-03", "symbol": "025900", "company_name": "동화기업", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE", "case_type": "electrolyte_post_CA_utilization_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R3L84-C13-03-S2FP-20240716", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_squeeze_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_delayed_squeeze", "price_source": "Songdaiki/stock-web", "notes": "Post-CA battery electrolyte moves should be blocked from Stage2 unless customer call-off, utilization and margin bridge are proven at entry."}
{"row_type": "trigger", "trigger_id": "R3L84-C13-03-S2FP-20240716", "case_id": "R3L84-C13-03", "symbol": "025900", "company_name": "동화기업", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_CATHODE_US_CAPACITY_AMPC_UTILIZATION_BRIDGE_VS_POLICY_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_JV_utilization_AMPC_IRA_guardrail|local_4B_timing_after_policy_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-16", "evidence_available_at_that_date": "electrolyte/localization and post-CA US capacity utilization proxy without customer volume and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["AMPC_or_IRA_policy_proxy", "JV_or_US_capacity_proxy", "customer_location_proxy"], "stage3_evidence_fields": ["customer_calloff", "volume_utilization", "subsidy_capture", "ASP_or_cost_pass_through", "margin_conversion"], "stage4b_evidence_fields": ["policy_MFE_without_utilization_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_calloff_or_subsidy_reversal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025900/2024.csv", "profile_path": "atlas/symbol_profiles/025/025900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-16", "entry_price": 12470, "MFE_30D_pct": 10.51, "MFE_90D_pct": 15.32, "MFE_180D_pct": 19.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.42, "MAE_90D_pct": -16.28, "MAE_180D_pct": -38.25, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-21", "peak_price": 14880, "drawdown_after_peak_pct": -48.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "delayed_post_CA_squeeze_not_valid_stage2_without_customer_utilization_bridge", "four_b_evidence_type": ["policy_MFE_without_utilization_bridge", "valuation_blowoff", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_calloff_or_subsidy_break", "trigger_outcome_label": "delayed_squeeze_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_delayed_squeeze", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024_05_03_CA_clean_forward_window", "same_entry_group_id": "R3L84-C13-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L84-C13-03", "trigger_id": "R3L84-C13-03-S2FP-20240716", "symbol": "025900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"AMPC_policy_specificity_score": 35, "JV_or_US_capacity_score": 35, "customer_volume_bridge_score": 10, "utilization_score": 10, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "calloff_risk_score": 75, "4B_watch_score": 50}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"AMPC_policy_specificity_score": 35, "JV_or_US_capacity_score": 35, "customer_volume_bridge_score": 0, "utilization_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 5, "calloff_risk_score": 85, "4B_watch_score": 80}, "weighted_score_after": 48, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["customer_volume_bridge_score", "utilization_score", "margin_bridge_score", "source_quality_score", "calloff_risk_score", "4B_watch_score"], "component_delta_explanation": "C13 requires IRA/AMPC/JV capacity to convert into customer call-off, utilization, subsidy capture and margin bridge; policy or localization MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 15.32, "MAE_90D_pct": -16.28, "score_return_alignment_label": "delayed_squeeze_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_delayed_squeeze"}
{"row_type": "shadow_weight", "axis": "C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Battery JV/IRA/AMPC rerating requires customer call-off, volume utilization, subsidy capture and margin bridge; policy-MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 348370 only with local 4B watch; demotes 005070/025900 policy-theme false positives", "trigger_ids": "R3L84-C13-01-S2A-20240115|R3L84-C13-02-S2FP-20240213|R3L84-C13-03-S2FP-20240716", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R3", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["AMPC_policy_theme_false_positive_high_MAE", "local_4B_late_after_extreme_policy_MFE", "customer_calloff_utilization_margin_bridge_required", "source_proxy_runtime_promotion_risk", "post_CA_battery_material_squeeze_not_original_stage2_validation"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C13, test a canonical-archetype guard requiring IRA/AMPC/JV capacity to convert into customer call-off, utilization, subsidy capture and margin bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 84
next_round = R4
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
