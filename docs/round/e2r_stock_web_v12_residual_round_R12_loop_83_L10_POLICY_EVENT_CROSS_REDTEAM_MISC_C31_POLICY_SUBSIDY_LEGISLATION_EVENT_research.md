# E2R Stock-Web v12 Residual Research — R12 Loop 83 / L10 / C31

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 83,
  "computed_next_round": "R13",
  "computed_next_loop": 83,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE",
  "loop_objective": [
    "under_covered_service_tourism_policy_extension",
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_direct_beneficiary_mapping_guardrail",
    "tourism_visitor_drop_revenue_margin_bridge",
    "4B_non_price_requirement_stress_test",
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
scheduled_loop = 83
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R12 is the policy / under-covered service extension slot. This run uses a tourism / visa / casino fine route under C31 rather than another utility tariff route.

The tested mechanism:

```text
tourism / visa / reopening / casino-regulation policy headline
→ direct beneficiary mapping
→ visitors / casino drop / hotel occupancy / sales bridge
→ margin and FCF conversion
→ durable rerating or reopening-theme fade
```

A tourism headline is the airport gate opening. The model should not mark the trip as successful until passengers actually board, spend, and the spend survives the cost line.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 is already wide and top-covered in `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top-covered set and uses:

```text
035250 / 강원랜드
114090 / GKL
032350 / 롯데관광개발
```

All three are treated as new independent C31 tourism/service-policy cases for this loop. No hard duplicate is intentionally reused.

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
| 035250 | 강원랜드 | `atlas/symbol_profiles/035/035250.json` | old 2003 CA candidate; selected 2024/2025 forward window clean |
| 114090 | GKL | `atlas/symbol_profiles/114/114090.json` | no profile-level corporate-action candidate |
| 032350 | 롯데관광개발 | `atlas/symbol_profiles/032/032350.json` | old CA candidates through 2018; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R12L83-C31-01 | 035250 | 2024-07-12 | 14,250 | 180D | clean | true |
| R12L83-C31-02 | 114090 | 2024-02-19 | 13,660 | 180D | clean | true |
| R12L83-C31-03 | 032350 | 2024-03-27 | 9,990 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | DOMESTIC_CASINO_POLICY_DIRECT_BENEFICIARY | keep Stage2 when visitor/drop/revenue/margin bridge is visible |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | FOREIGNER_CASINO_VISA_REOPENING_GAP | reject or demote when visa/inbound headline lacks visitor-mix/drop/hold-rate bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | INTEGRATED_RESORT_REOPENING_BETA_FADE | local 4B/reject when tourism beta MFE fades without occupancy/debt/cost bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R12L83-C31-01 | 035250 | 강원랜드 | Stage2-Actionable | 2024-07-12 | 14,250 | 30.6 | -6.46 | current_profile_partially_correct_4B_watch_needed |
| R12L83-C31-02 | 114090 | GKL | Stage2-FalsePositive | 2024-02-19 | 13,660 | 3.15 | -22.04 | current_profile_false_positive |
| R12L83-C31-03 | 032350 | 롯데관광개발 | Stage2-FalsePositive | 2024-03-27 | 9,990 | 7.31 | -19.02 | current_profile_false_positive_4B_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C31 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: visa policy, foreign tourist data, casino monthly drop/sales, hotel occupancy, regulatory decision, company disclosure, report, or official tourism statistics.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 035250 | `atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv` and `2025.csv` | `atlas/symbol_profiles/035/035250.json` |
| 114090 | `atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv` | `atlas/symbol_profiles/114/114090.json` |
| 032350 | `atlas/ohlcv_tradable_by_symbol_year/032/032350/2024.csv` | `atlas/symbol_profiles/032/032350.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 035250 / 강원랜드

C31 tourism-policy positive, but not automatically Stage3. The stock had a strong MFE after the July entry and a later peak around the tourism/casino beneficiary window. The model should keep Stage2-Actionable only if visitor volume, casino drop, revenue and margin bridge survive source repair.

### Case 2 — 114090 / GKL

C31 false positive for foreigner-casino reopening. The price path showed little MFE and wide MAE. The case shows why inbound/visa policy should not be credited unless the evidence reaches visitor mix, drop/hold-rate and margin bridge.

### Case 3 — 032350 / 롯데관광개발

C31 integrated-resort reopening beta fade. It had a short MFE, then a deeper drawdown. The model should not treat Jeju tourism/inbound headlines as Stage2-Actionable unless occupancy, casino drop, debt/cost and margin conversion are visible.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 035250 | 14,250 | 7.44 | -6.46 | 30.60 | -6.46 | 30.60 | -6.46 | 2024-09-05 / 18,610 | -21.12 |
| 114090 | 13,660 | 0.66 | -12.30 | 3.15 | -12.30 | 3.15 | -22.04 | 2024-04-05 / 14,090 | -24.41 |
| 032350 | 9,990 | 7.31 | -3.70 | 7.31 | -19.02 | 7.31 | -19.02 | 2024-04-01 / 10,720 | -24.53 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R12L83-C31-01 | Stage2-Actionable if tourism policy bridge exists | high MFE, later drawdown | partially correct; local 4B watch needed |
| R12L83-C31-02 | risk of treating inbound/casino reopening as Stage2 | tiny MFE / high MAE | false positive |
| R12L83-C31-03 | risk of treating resort reopening beta as Stage2 | short MFE / high MAE | false positive / 4B late |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For this C31 tourism-policy route, the residual is not Green lateness. The residual is whether a policy/reopening headline becomes Stage2-Actionable before the visitor/drop/revenue/margin bridge is proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R12L83-C31-01 | 0.82 | 0.76 | local 4B watch after tourism policy MFE if drop/margin bridge stalls |
| R12L83-C31-02 | 0.25 | 0.25 | reopening theme rejected without drop/hold-rate/margin bridge |
| R12L83-C31-03 | 0.25 | 0.25 | local 4B or reject after reopening MFE without occupancy/drop bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_policy_or_demand_mix_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = C31 tourism/service-policy rows need visitor/drop/sales/occupancy/margin bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = C31_tourism_policy_visitor_drop_margin_bridge_required
effect = keep direct-beneficiary tourism positives with 4B watch; demote reopening-theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 13.69 | -12.59 | may over-credit tourism/reopening headlines | needs C31 tourism bridge repair |
| P1 canonical shadow bridge profile | 3 | 30.60 on kept positive | -6.46 on kept positive | demotes 114090/032350 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R12L83-C31-01 | 78 | Stage2-Actionable | 81 | Stage2-Actionable + local 4B watch | partially aligned |
| R12L83-C31-02 | 58 | Stage2-Watch/FalsePositive | 49 | Rejected-Stage2 / RiskWatch | improved |
| R12L83-C31-03 | 58 | Stage2-Watch/FalsePositive | 49 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
residual_error_types_found:
  - tourism_policy_theme_false_positive_low_MFE_high_MAE
  - visitor_drop_sales_margin_bridge_required
  - direct_beneficiary_mapping_required
  - 4B_needed_after_policy_MFE_if_drop_margin_bridge_stalls
new_axis_proposed: false
existing_axis_strengthened: C31_tourism_policy_visitor_drop_margin_bridge_required
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C31_tourism_policy_visitor_drop_margin_bridge_required
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
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- official visa/tourism-policy source
- visitor count and nationality mix
- casino drop/hold-rate and hotel occupancy detail
- revenue/margin/FCF bridge
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_tourism_policy_visitor_drop_margin_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require direct beneficiary mapping plus visitor/drop/sales/occupancy and margin bridge before Stage2-Actionable","keeps 035250 with 4B watch; demotes 114090/032350","R12L83-C31-01-S2A-20240712|R12L83-C31-02-S2FP-20240219|R12L83-C31-03-S2FP-20240327",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L83-C31-01", "symbol": "035250", "company_name": "강원랜드", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE", "case_type": "tourism_policy_domestic_casino_volume_positive_with_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L83-C31-01-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_direct_beneficiary_positive_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Tourism policy can be Stage2 only if direct beneficiary mapping converts into visitors, drop/revenue and margin bridge."}
{"row_type": "trigger", "trigger_id": "R12L83-C31-01-S2A-20240712", "case_id": "R12L83-C31-01", "symbol": "035250", "company_name": "강원랜드", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE", "loop_objective": "under_covered_service_tourism_policy_extension|coverage_gap_fill|counterexample_mining|policy_direct_beneficiary_mapping_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "tourism / casino regulation and domestic visitor recovery policy proxy; visitor-to-drop-to-margin bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_direct_beneficiary_mapping", "tourism_or_visa_policy_proxy", "visitor_volume_bridge_proxy"], "stage3_evidence_fields": ["drop_or_sales_bridge", "occupancy_or_visit_mix", "hold_rate_or_take_rate", "margin_conversion"], "stage4b_evidence_fields": ["reopening_theme_overheat", "drop_margin_bridge_delay", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_policy_reversal_or_demand_mix_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv", "profile_path": "atlas/symbol_profiles/035/035250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 14250, "MFE_30D_pct": 7.44, "MFE_90D_pct": 30.6, "MFE_180D_pct": 30.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.46, "MAE_90D_pct": -6.46, "MAE_180D_pct": -6.46, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-05", "peak_price": 18610, "drawdown_after_peak_pct": -21.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.76, "four_b_timing_verdict": "local_4B_watch_after_tourism_policy_MFE_if_drop_margin_bridge_stalls", "four_b_evidence_type": ["tourism_policy_theme_overheat", "visitor_drop_margin_bridge_delay", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_policy_or_demand_mix_break", "trigger_outcome_label": "policy_direct_beneficiary_positive_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2003_CA_candidate", "same_entry_group_id": "R12L83-C31-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L83-C31-01", "trigger_id": "R12L83-C31-01-S2A-20240712", "symbol": "035250", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"direct_beneficiary_mapping_score": 55, "policy_specificity_score": 45, "visitor_volume_bridge_score": 45, "casino_drop_or_sales_bridge_score": 40, "margin_bridge_score": 40, "FCF_or_balance_sheet_repair_score": 35, "revision_score": 40, "relative_strength_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "policy_delay_risk_score": 35, "demand_mix_risk_score": 40}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"direct_beneficiary_mapping_score": 55, "policy_specificity_score": 45, "visitor_volume_bridge_score": 50, "casino_drop_or_sales_bridge_score": 45, "margin_bridge_score": 40, "FCF_or_balance_sheet_repair_score": 35, "revision_score": 40, "relative_strength_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "policy_delay_risk_score": 35, "demand_mix_risk_score": 40}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["direct_beneficiary_mapping_score", "visitor_volume_bridge_score", "casino_drop_or_sales_bridge_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C31 tourism-policy rows require direct beneficiary mapping plus visitor/drop/sales/occupancy/margin bridge before Stage2-Actionable; reopening-theme-only cases are demoted.", "MFE_90D_pct": 30.6, "MAE_90D_pct": -6.46, "score_return_alignment_label": "policy_direct_beneficiary_positive_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed"}
{"row_type": "case", "case_id": "R12L83-C31-02", "symbol": "114090", "company_name": "GKL", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE", "case_type": "foreigner_casino_visa_reopening_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R12L83-C31-02-S2FP-20240219", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "tourism_policy_theme_false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Foreign casino policy/inbound narrative should not become Stage2 unless visitor mix, drop, hold rate and cost bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R12L83-C31-02-S2FP-20240219", "case_id": "R12L83-C31-02", "symbol": "114090", "company_name": "GKL", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE", "loop_objective": "under_covered_service_tourism_policy_extension|coverage_gap_fill|counterexample_mining|policy_direct_beneficiary_mapping_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-19", "evidence_available_at_that_date": "visa / inbound tourism / foreigner casino recovery proxy without drop, hold-rate, Chinese/Japanese VIP and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_direct_beneficiary_mapping", "tourism_or_visa_policy_proxy", "visitor_volume_bridge_proxy"], "stage3_evidence_fields": ["drop_or_sales_bridge", "occupancy_or_visit_mix", "hold_rate_or_take_rate", "margin_conversion"], "stage4b_evidence_fields": ["reopening_theme_overheat", "drop_margin_bridge_delay", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_policy_reversal_or_demand_mix_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv", "profile_path": "atlas/symbol_profiles/114/114090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-19", "entry_price": 13660, "MFE_30D_pct": 0.66, "MFE_90D_pct": 3.15, "MFE_180D_pct": 3.15, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.3, "MAE_90D_pct": -12.3, "MAE_180D_pct": -22.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-05", "peak_price": 14090, "drawdown_after_peak_pct": -24.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.25, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "tourism_reopening_theme_rejected_without_drop_hold_rate_margin_bridge", "four_b_evidence_type": ["tourism_policy_theme_overheat", "visitor_drop_margin_bridge_delay", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_policy_or_demand_mix_break", "trigger_outcome_label": "tourism_policy_theme_false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R12L83-C31-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L83-C31-02", "trigger_id": "R12L83-C31-02-S2FP-20240219", "symbol": "114090", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"direct_beneficiary_mapping_score": 25, "policy_specificity_score": 30, "visitor_volume_bridge_score": 20, "casino_drop_or_sales_bridge_score": 10, "margin_bridge_score": 5, "FCF_or_balance_sheet_repair_score": 10, "revision_score": 20, "relative_strength_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 65, "policy_delay_risk_score": 55, "demand_mix_risk_score": 65}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"direct_beneficiary_mapping_score": 15, "policy_specificity_score": 30, "visitor_volume_bridge_score": 5, "casino_drop_or_sales_bridge_score": 0, "margin_bridge_score": 0, "FCF_or_balance_sheet_repair_score": 10, "revision_score": 20, "relative_strength_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 80, "policy_delay_risk_score": 55, "demand_mix_risk_score": 65}, "weighted_score_after": 49, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "visitor_volume_bridge_score", "casino_drop_or_sales_bridge_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C31 tourism-policy rows require direct beneficiary mapping plus visitor/drop/sales/occupancy/margin bridge before Stage2-Actionable; reopening-theme-only cases are demoted.", "MFE_90D_pct": 3.15, "MAE_90D_pct": -12.3, "score_return_alignment_label": "tourism_policy_theme_false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R12L83-C31-03", "symbol": "032350", "company_name": "롯데관광개발", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE", "case_type": "integrated_resort_visa_reopening_theme_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R12L83-C31-03-S2FP-20240327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "tourism_policy_theme_MFE_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive_4B_late", "price_source": "Songdaiki/stock-web", "notes": "Integrated resort policy narrative must be translated into occupancy/drop/revenue and debt-cost bridge; otherwise it is a reopening beta trade."}
{"row_type": "trigger", "trigger_id": "R12L83-C31-03-S2FP-20240327", "case_id": "R12L83-C31-03", "symbol": "032350", "company_name": "롯데관광개발", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TOURISM_VISA_CASINO_TRAFFIC_DROP_REVENUE_MARGIN_BRIDGE_VS_REOPENING_THEME_FADE", "loop_objective": "under_covered_service_tourism_policy_extension|coverage_gap_fill|counterexample_mining|policy_direct_beneficiary_mapping_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Jeju tourism / visa / integrated resort recovery proxy without occupancy, casino drop, debt/cost and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_direct_beneficiary_mapping", "tourism_or_visa_policy_proxy", "visitor_volume_bridge_proxy"], "stage3_evidence_fields": ["drop_or_sales_bridge", "occupancy_or_visit_mix", "hold_rate_or_take_rate", "margin_conversion"], "stage4b_evidence_fields": ["reopening_theme_overheat", "drop_margin_bridge_delay", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_policy_reversal_or_demand_mix_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032350/2024.csv", "profile_path": "atlas/symbol_profiles/032/032350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 9990, "MFE_30D_pct": 7.31, "MFE_90D_pct": 7.31, "MFE_180D_pct": 7.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.7, "MAE_90D_pct": -19.02, "MAE_180D_pct": -19.02, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 10720, "drawdown_after_peak_pct": -24.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.25, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "local_4B_or_reject_after_reopening_MFE_without_occupancy_drop_margin_bridge", "four_b_evidence_type": ["tourism_policy_theme_overheat", "visitor_drop_margin_bridge_delay", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_policy_or_demand_mix_break", "trigger_outcome_label": "tourism_policy_theme_MFE_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive_4B_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2018_CA_candidates", "same_entry_group_id": "R12L83-C31-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L83-C31-03", "trigger_id": "R12L83-C31-03-S2FP-20240327", "symbol": "032350", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"direct_beneficiary_mapping_score": 25, "policy_specificity_score": 30, "visitor_volume_bridge_score": 20, "casino_drop_or_sales_bridge_score": 10, "margin_bridge_score": 5, "FCF_or_balance_sheet_repair_score": 10, "revision_score": 20, "relative_strength_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 65, "policy_delay_risk_score": 55, "demand_mix_risk_score": 65}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"direct_beneficiary_mapping_score": 15, "policy_specificity_score": 30, "visitor_volume_bridge_score": 5, "casino_drop_or_sales_bridge_score": 0, "margin_bridge_score": 0, "FCF_or_balance_sheet_repair_score": 10, "revision_score": 20, "relative_strength_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 80, "policy_delay_risk_score": 55, "demand_mix_risk_score": 65}, "weighted_score_after": 49, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "visitor_volume_bridge_score", "casino_drop_or_sales_bridge_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C31 tourism-policy rows require direct beneficiary mapping plus visitor/drop/sales/occupancy/margin bridge before Stage2-Actionable; reopening-theme-only cases are demoted.", "MFE_90D_pct": 7.31, "MAE_90D_pct": -19.02, "score_return_alignment_label": "tourism_policy_theme_MFE_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive_4B_late"}
{"row_type": "shadow_weight", "axis": "C31_tourism_policy_visitor_drop_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Tourism/visa/policy rerating requires direct beneficiary mapping plus visitor/drop/sales/occupancy and margin bridge; reopening headline alone fades.", "backtest_effect": "keeps 035250 as policy-positive with local 4B watch; demotes 114090/032350 reopening-theme false positives", "trigger_ids": "R12L83-C31-01-S2A-20240712|R12L83-C31-02-S2FP-20240219|R12L83-C31-03-S2FP-20240327", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R12", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["tourism_policy_theme_false_positive_low_MFE_high_MAE", "visitor_drop_sales_margin_bridge_required", "direct_beneficiary_mapping_required", "4B_needed_after_policy_MFE_if_drop_margin_bridge_stalls"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C31 tourism/service-policy rows, test a canonical-archetype guard requiring direct beneficiary mapping plus visitor/drop/sales/occupancy and margin bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 83
next_round = R13
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
