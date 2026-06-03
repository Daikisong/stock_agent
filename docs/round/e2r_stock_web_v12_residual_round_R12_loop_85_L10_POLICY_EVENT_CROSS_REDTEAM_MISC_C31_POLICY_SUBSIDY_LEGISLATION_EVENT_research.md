# E2R Stock-Web v12 Residual Research — R12 Loop 85 / L10 / C31

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 85,
  "computed_next_round": "R13",
  "computed_next_loop": 85,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE",
  "loop_objective": [
    "under_covered_service_policy_extension",
    "coverage_gap_fill",
    "counterexample_mining",
    "education_policy_private_demand_guardrail",
    "medical_school_quota_policy_event_vs_revenue_bridge_test",
    "education_theme_spike_MFE_vs_enrollment_ARPU_margin_bridge_test",
    "local_4B_timing_after_education_policy_MFE",
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
scheduled_round = R12
scheduled_loop = 85
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R12 is the policy / under-covered service-agri extension slot. This run selects an under-covered education-service fine route under C31, avoiding loop85 R11's resource-policy C31 and loop84 R12's agri-food C31.

The tested mechanism:

```text
medical-school quota / education-policy headline
→ direct beneficiary mapping
→ lead conversion and enrollment visibility
→ ARPU, capacity and instructor supply
→ revenue and gross-margin conversion
→ durable rerating or education-policy theme spike fade
```

C31 here is a classroom roster, not a headline. The thesis only becomes durable when policy noise turns into paid enrollment and margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols include `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top-covered set and uses:

```text
339950 / 아이비김영
053290 / NE능률
133750 / 메가엠디
```

All three are treated as new independent C31 education-policy/private-demand cases for this loop. No hard duplicate is intentionally reused.

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
| 339950 | 아이비김영 | `atlas/symbol_profiles/339/339950.json` | old 2020 SPAC CA candidate; selected 2024 forward window clean |
| 053290 | NE능률 | `atlas/symbol_profiles/053/053290.json` | old CA candidates through 2009; selected 2024 forward window clean |
| 133750 | 메가엠디 | `atlas/symbol_profiles/133/133750.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R12L85-C31-01 | 339950 | 2024-02-06 | 1,750 | 180D | clean | true |
| R12L85-C31-02 | 053290 | 2024-02-06 | 5,240 | 180D | clean | true |
| R12L85-C31-03 | 133750 | 2024-02-06 | 2,995 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | EDUCATION_POLICY_TRANSFER_ADMISSION_DEMAND | keep Stage2 only with direct beneficiary, lead conversion, enrollment, ARPU and margin bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | TEXTBOOK_EDU_POLICY_THEME_SPIKE | reject education-policy theme spike without enrollment/revenue bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | MEDICAL_ADMISSIONS_THEME_HIGH_MAE | reject adult-education/medical admissions theme MFE without conversion and margin evidence |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R12L85-C31-01 | 339950 | 아이비김영 | Stage2-Actionable | 2024-02-06 | 1,750 | 69.43 | -15.43 | current_profile_4B_too_late_after_education_policy_MFE |
| R12L85-C31-02 | 053290 | NE능률 | Stage2-FalsePositive | 2024-02-06 | 5,240 | 20.23 | -47.61 | current_profile_false_positive_high_MAE_theme_spike |
| R12L85-C31-03 | 133750 | 메가엠디 | Stage2-FalsePositive | 2024-02-06 | 2,995 | 22.54 | -45.01 | current_profile_false_positive_high_MAE |

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

This MD creates a source-repair queue and a C31 education-policy shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: policy text, direct beneficiary mapping, lead conversion, enrollment trend, ARPU, course capacity, instructor supply, revenue bridge, margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 339950 | `atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv` | `atlas/symbol_profiles/339/339950.json` |
| 053290 | `atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv` | `atlas/symbol_profiles/053/053290.json` |
| 133750 | `atlas/ohlcv_tradable_by_symbol_year/133/133750/2024.csv` | `atlas/symbol_profiles/133/133750.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 339950 / 아이비김영

C31 education-policy positive with local 4B watch. The entry created a large MFE, but the post-peak drawdown shows that a policy spike should not be allowed into clean Green without lead conversion, enrollment, ARPU and margin evidence.

### Case 2 — 053290 / NE능률

C31 textbook/education-policy theme false positive. The policy headline generated a same-day MFE, but the later MAE was much deeper. This is a theme-spike rejection row.

### Case 3 — 133750 / 메가엠디

C31 medical-admissions/adult-education false positive. The MFE was tradable, but MAE and drawdown were severe. The model should require conversion-to-enrollment and revenue/margin bridge before Stage2 validation.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 339950 | 1,750 | 69.43 | -2.86 | 69.43 | -2.86 | 69.43 | -15.43 | 2024-02-26 / 2,965 | -50.08 |
| 053290 | 5,240 | 20.23 | -13.55 | 20.23 | -25.67 | 20.23 | -47.61 | 2024-02-06 / 6,300 | -56.43 |
| 133750 | 2,995 | 22.54 | -30.55 | 22.54 | -45.01 | 22.54 | -45.01 | 2024-02-06 / 3,670 | -55.12 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R12L85-C31-01 | Stage2-Actionable if enrollment/revenue bridge exists | large MFE and post-peak drawdown | partially correct; local 4B watch needed |
| R12L85-C31-02 | risk of treating education-policy theme as Stage2 | same-day MFE / deep MAE | false positive / theme spike |
| R12L85-C31-03 | risk of treating admissions policy theme as Stage2 | MFE then severe MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C31 education-policy rows, the residual is whether policy-event MFE becomes clean Stage2/Green before direct beneficiary, lead conversion, enrollment and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R12L85-C31-01 | 0.90 | 0.80 | local 4B watch required when private-education MFE outruns enrollment/ARPU/margin bridge |
| R12L85-C31-02 | 0.35 | 0.30 | education-policy theme rejected without direct-beneficiary/enrollment bridge |
| R12L85-C31-03 | 0.35 | 0.30 | admissions-policy theme rejected without lead-conversion/ARPU/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_policy_reversal_or_enrollment_demand_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C31 education-policy hard 4C requires policy reversal, demand/enrollment failure, lead-conversion break, pricing/ARPU compression or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L10/C31 education-policy rows need direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = C31_education_policy_direct_beneficiary_enrollment_revenue_margin_bridge_required
effect = keep education-policy positives with local 4B watch; demote theme-spike false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 37.40 | -24.51 | may over-credit education-policy theme MFE | needs C31 education-demand bridge repair |
| P1 canonical shadow bridge profile | 3 | 69.43 on kept positive | demotes 053290/133750 | blocks clean Green until source repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R12L85-C31-01 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + local 4B/education-demand bridge watch | partially aligned |
| R12L85-C31-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Education-policy theme RiskWatch | improved |
| R12L85-C31-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Education-policy theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - education_policy_theme_false_positive_high_MAE
  - direct_beneficiary_enrollment_ARPU_margin_bridge_required
  - local_4B_late_after_education_policy_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_policy_or_demand_break
new_axis_proposed: false
existing_axis_strengthened:
  - C31_education_policy_direct_beneficiary_enrollment_revenue_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C31_education_policy_direct_beneficiary_enrollment_revenue_margin_bridge_required
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
- official education-policy source
- direct beneficiary and lead-conversion evidence
- enrollment / ARPU / course capacity data
- revenue and gross-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_education_policy_direct_beneficiary_enrollment_revenue_margin_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/margin bridge before clean Stage2/Green","keeps 339950 with local 4B education-demand bridge watch; demotes 053290/133750","R12L85-C31-01-S2A-20240206|R12L85-C31-02-S2FP-20240206|R12L85-C31-03-S2FP-20240206",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L85-C31-01", "symbol": "339950", "company_name": "아이비김영", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "medical_school_quota_transfer_admission_policy_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L85-C31-01-S2A-20240206", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_policy_MFE_but_local_4B_and_revenue_bridge_required", "current_profile_verdict": "current_profile_4B_too_late_after_education_policy_MFE", "price_source": "Songdaiki/stock-web", "notes": "C31 education-policy positives need direct beneficiary mapping, actual enrollment/lead conversion, ARPU, capacity and margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R12L85-C31-01-S2A-20240206", "case_id": "R12L85-C31-01", "symbol": "339950", "company_name": "아이비김영", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "under_covered_service_policy_extension|coverage_gap_fill|counterexample_mining|education_policy_private_demand_guardrail|local_4B_timing_after_education_policy_MFE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "evidence_available_at_that_date": "medical-school quota / transfer-admission / private education demand proxy; primary enrollment, ARPU and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["education_policy_proxy", "direct_beneficiary_proxy", "private_education_demand_proxy"], "stage3_evidence_fields": ["lead_conversion", "enrollment_visibility", "ARPU_or_price", "capacity_or_instructor_supply", "revenue_and_margin_conversion"], "stage4b_evidence_fields": ["education_policy_MFE_without_revenue_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_enrollment_demand_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv", "profile_path": "atlas/symbol_profiles/339/339950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-06", "entry_price": 1750, "MFE_30D_pct": 69.43, "MFE_90D_pct": 69.43, "MFE_180D_pct": 69.43, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.86, "MAE_90D_pct": -2.86, "MAE_180D_pct": -15.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 2965, "drawdown_after_peak_pct": -50.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "local_4B_watch_required_when_private_education_policy_MFE_outruns_enrollment_ARPU_margin_bridge", "four_b_evidence_type": ["education_policy_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_enrollment_demand_break", "trigger_outcome_label": "large_policy_MFE_but_local_4B_and_revenue_bridge_required", "current_profile_verdict": "current_profile_4B_too_late_after_education_policy_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2020_SPAC_CA_candidate", "same_entry_group_id": "R12L85-C31-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L85-C31-01", "trigger_id": "R12L85-C31-01-S2A-20240206", "symbol": "339950", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 55, "direct_beneficiary_mapping_score": 45, "lead_conversion_score": 35, "enrollment_visibility_score": 35, "ARPU_or_price_score": 30, "capacity_or_instructor_supply_score": 30, "revenue_bridge_score": 35, "gross_margin_bridge_score": 30, "event_momentum_score": 75, "theme_blowoff_risk_score": 80, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"policy_specificity_score": 55, "direct_beneficiary_mapping_score": 45, "lead_conversion_score": 35, "enrollment_visibility_score": 35, "ARPU_or_price_score": 30, "capacity_or_instructor_supply_score": 30, "revenue_bridge_score": 35, "gross_margin_bridge_score": 30, "event_momentum_score": 75, "theme_blowoff_risk_score": 90, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 85}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/education-demand bridge watch", "changed_components": ["direct_beneficiary_mapping_score", "lead_conversion_score", "enrollment_visibility_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C31 education-policy rows require direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/margin bridge before clean Stage2/Green; policy-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 69.43, "MAE_90D_pct": -2.86, "score_return_alignment_label": "large_policy_MFE_but_local_4B_and_revenue_bridge_required", "current_profile_verdict": "current_profile_4B_too_late_after_education_policy_MFE"}
{"row_type": "case", "case_id": "R12L85-C31-02", "symbol": "053290", "company_name": "NE능률", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "education_policy_theme_spike_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R12L85-C31-02-S2FP-20240206", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_theme_spike_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_theme_spike", "price_source": "Songdaiki/stock-web", "notes": "Education-policy theme heat should not validate Stage2 unless beneficiary mapping, revenue conversion and margin bridge are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R12L85-C31-02-S2FP-20240206", "case_id": "R12L85-C31-02", "symbol": "053290", "company_name": "NE능률", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "under_covered_service_policy_extension|coverage_gap_fill|counterexample_mining|education_policy_private_demand_guardrail|local_4B_timing_after_education_policy_MFE", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-06", "evidence_available_at_that_date": "education-policy / textbook / private education demand theme proxy without direct enrollment, ARPU and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["education_policy_proxy", "direct_beneficiary_proxy", "private_education_demand_proxy"], "stage3_evidence_fields": ["lead_conversion", "enrollment_visibility", "ARPU_or_price", "capacity_or_instructor_supply", "revenue_and_margin_conversion"], "stage4b_evidence_fields": ["education_policy_MFE_without_revenue_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_enrollment_demand_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-06", "entry_price": 5240, "MFE_30D_pct": 20.23, "MFE_90D_pct": 20.23, "MFE_180D_pct": 20.23, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.55, "MAE_90D_pct": -25.67, "MAE_180D_pct": -47.61, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 6300, "drawdown_after_peak_pct": -56.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "education_policy_theme_MFE_rejected_without_direct_beneficiary_enrollment_margin_bridge", "four_b_evidence_type": ["education_policy_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_enrollment_demand_break", "trigger_outcome_label": "policy_theme_spike_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_theme_spike", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2009_CA_candidates", "same_entry_group_id": "R12L85-C31-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L85-C31-02", "trigger_id": "R12L85-C31-02-S2FP-20240206", "symbol": "053290", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "lead_conversion_score": 5, "enrollment_visibility_score": 5, "ARPU_or_price_score": 5, "capacity_or_instructor_supply_score": 15, "revenue_bridge_score": 5, "gross_margin_bridge_score": 5, "event_momentum_score": 50, "theme_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 5, "lead_conversion_score": 0, "enrollment_visibility_score": 0, "ARPU_or_price_score": 5, "capacity_or_instructor_supply_score": 15, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "event_momentum_score": 50, "theme_blowoff_risk_score": 80, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Education-policy theme RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "lead_conversion_score", "enrollment_visibility_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C31 education-policy rows require direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/margin bridge before clean Stage2/Green; policy-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 20.23, "MAE_90D_pct": -25.67, "score_return_alignment_label": "policy_theme_spike_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_theme_spike"}
{"row_type": "case", "case_id": "R12L85-C31-03", "symbol": "133750", "company_name": "메가엠디", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "medical_admissions_policy_theme_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L85-C31-03-S2FP-20240206", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "admissions_policy_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Medical admissions/private education policy MFE should remain RiskWatch unless lead conversion, enrollment, ARPU and margin conversion are source-repaired."}
{"row_type": "trigger", "trigger_id": "R12L85-C31-03-S2FP-20240206", "case_id": "R12L85-C31-03", "symbol": "133750", "company_name": "메가엠디", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "under_covered_service_policy_extension|coverage_gap_fill|counterexample_mining|education_policy_private_demand_guardrail|local_4B_timing_after_education_policy_MFE", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-06", "evidence_available_at_that_date": "medical admissions / adult education / private education policy theme proxy without confirmed lead conversion, enrollment and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["education_policy_proxy", "direct_beneficiary_proxy", "private_education_demand_proxy"], "stage3_evidence_fields": ["lead_conversion", "enrollment_visibility", "ARPU_or_price", "capacity_or_instructor_supply", "revenue_and_margin_conversion"], "stage4b_evidence_fields": ["education_policy_MFE_without_revenue_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_enrollment_demand_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/133/133750/2024.csv", "profile_path": "atlas/symbol_profiles/133/133750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-06", "entry_price": 2995, "MFE_30D_pct": 22.54, "MFE_90D_pct": 22.54, "MFE_180D_pct": 22.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.55, "MAE_90D_pct": -45.01, "MAE_180D_pct": -45.01, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 3670, "drawdown_after_peak_pct": -55.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "admissions_policy_theme_rejected_without_lead_conversion_enrollment_ARPU_margin_bridge", "four_b_evidence_type": ["education_policy_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_enrollment_demand_break", "trigger_outcome_label": "admissions_policy_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R12L85-C31-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L85-C31-03", "trigger_id": "R12L85-C31-03-S2FP-20240206", "symbol": "133750", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "lead_conversion_score": 5, "enrollment_visibility_score": 5, "ARPU_or_price_score": 5, "capacity_or_instructor_supply_score": 15, "revenue_bridge_score": 5, "gross_margin_bridge_score": 5, "event_momentum_score": 50, "theme_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 5, "lead_conversion_score": 0, "enrollment_visibility_score": 0, "ARPU_or_price_score": 5, "capacity_or_instructor_supply_score": 15, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "event_momentum_score": 50, "theme_blowoff_risk_score": 80, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Education-policy theme RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "lead_conversion_score", "enrollment_visibility_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C31 education-policy rows require direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/margin bridge before clean Stage2/Green; policy-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 22.54, "MAE_90D_pct": -45.01, "score_return_alignment_label": "admissions_policy_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C31_education_policy_direct_beneficiary_enrollment_revenue_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Education-policy rerating requires direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/margin bridge; policy-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 339950 with local 4B education-demand bridge watch; demotes 053290/133750 high-MAE education-policy theme false positives", "trigger_ids": "R12L85-C31-01-S2A-20240206|R12L85-C31-02-S2FP-20240206|R12L85-C31-03-S2FP-20240206", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R12", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["education_policy_theme_false_positive_high_MAE", "direct_beneficiary_enrollment_ARPU_margin_bridge_required", "local_4B_late_after_education_policy_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_policy_or_demand_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C31 education-policy rows, test a canonical-archetype guard requiring direct beneficiary mapping, lead conversion, enrollment visibility, ARPU/capacity and revenue/gross-margin conversion before clean Stage2/Green. Keep hard 4C blocked unless a non-price policy reversal or demand thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 85
next_round = R13
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
