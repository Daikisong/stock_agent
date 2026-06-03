# E2R Stock-Web v12 Residual Research — R11 Loop 83 / L10 / C31

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 83,
  "computed_next_round": "R12",
  "computed_next_loop": 83,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_direct_beneficiary_mapping_guardrail",
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
scheduled_round = R11
scheduled_loop = 83
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R11 is a policy / event round. This run stays in L10 rather than L1 because the tested cases are regulated-utility / tariff / rate-policy beneficiaries, not defense-policy backlog cases.

The tested mechanism:

```text
policy / subsidy / tariff / regulated-rate headline
→ direct beneficiary mapping
→ tariff or subsidy pass-through
→ revenue / margin / FCF or balance-sheet bridge
→ durable rerating or policy-theme fade
```

A policy headline is like a law written on paper. The rerating only becomes real when it walks through the company’s income statement: tariff, subsidy, receivable repair, margin and cash flow.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 already has heavy coverage in `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top-covered set and uses:

```text
015760 / 한국전력
017390 / 서울가스
004690 / 삼천리
```

All three are treated as new independent C31 cases for this loop. No hard duplicate is intentionally reused.

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
| 015760 | 한국전력 | `atlas/symbol_profiles/015/015760.json` | no profile-level corporate-action candidate |
| 017390 | 서울가스 | `atlas/symbol_profiles/017/017390.json` | old CA candidates only through 2002; selected 2024 forward window clean |
| 004690 | 삼천리 | `atlas/symbol_profiles/004/004690.json` | old CA candidates only through 2001; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R11L83-C31-01 | 015760 | 2024-01-25 | 19,160 | 180D | clean | true |
| R11L83-C31-02 | 017390 | 2024-02-19 | 62,900 | 180D | clean | true |
| R11L83-C31-03 | 004690 | 2024-02-19 | 107,000 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | UTILITY_TARIFF_DIRECT_BENEFICIARY | keep Stage2 when policy directly improves tariff/revenue/margin/FCF bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | REGULATED_RATE_PASS_THROUGH_GAP | reject or demote when policy headline lacks pass-through and margin evidence |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_THEME_MFE_FADE | local 4B watch after large policy MFE if follow-through stalls |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R11L83-C31-01 | 015760 | 한국전력 | Stage2-Actionable | 2024-01-25 | 19,160 | 32.83 | -4.59 | current_profile_partially_correct_4B_watch_needed |
| R11L83-C31-02 | 017390 | 서울가스 | Stage2-FalsePositive | 2024-02-19 | 62,900 | 0.79 | -18.28 | current_profile_false_positive |
| R11L83-C31-03 | 004690 | 삼천리 | Stage2-FalsePositive | 2024-02-19 | 107,000 | 2.06 | -21.59 | current_profile_false_positive |

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

This MD therefore creates a source-repair queue and a C31 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: tariff decision, regulated-rate pass-through, subsidy mechanism, receivable repair, utility report, company disclosure, or official policy source.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 015760 | `atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv` | `atlas/symbol_profiles/015/015760.json` |
| 017390 | `atlas/ohlcv_tradable_by_symbol_year/017/017390/2024.csv` | `atlas/symbol_profiles/017/017390.json` |
| 004690 | `atlas/ohlcv_tradable_by_symbol_year/004/004690/2024.csv` | `atlas/symbol_profiles/004/004690.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 015760 / 한국전력

C31 policy-positive, but not blindly Green. The entry path captured a large policy/rate normalization MFE. The later drawdown says the policy signal needs a local 4B watch if tariff-to-margin/FCF bridge stalls.

### Case 2 — 017390 / 서울가스

C31 regulated-rate false positive. The stock had almost no upside after entry while MAE widened. A city-gas or regulated-rate policy narrative should be rejected unless volume, pass-through, receivable and margin evidence are explicit.

### Case 3 — 004690 / 삼천리

C31 policy-theme/regulated-utility false positive. The policy narrative was too broad; the stock showed small MFE and a persistent drawdown. Direct beneficiary economics were not visible enough in this proxy run.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 015760 | 19,160 | 31.00 | -4.59 | 32.83 | -4.59 | 32.83 | -4.59 | 2024-03-14 / 25,450 | -25.30 |
| 017390 | 62,900 | 0.79 | -9.22 | 0.79 | -9.70 | 0.79 | -18.28 | 2024-02-20 / 63,400 | -18.93 |
| 004690 | 107,000 | 2.06 | -12.80 | 2.06 | -15.98 | 2.06 | -21.59 | 2024-02-20 / 109,200 | -23.17 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R11L83-C31-01 | Stage2-Actionable if tariff policy bridge exists | high MFE, later drawdown | partially correct; local 4B watch needed |
| R11L83-C31-02 | risk of treating regulated-rate theme as Stage2 | tiny MFE / high MAE | false positive |
| R11L83-C31-03 | risk of treating broad utility policy as Stage2 | tiny MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C31, the residual is not Green lateness. The residual is whether policy headline evidence is allowed to become Stage2-Actionable before the actual tariff/subsidy/pass-through/margin bridge is proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R11L83-C31-01 | 0.82 | 0.76 | local 4B watch after policy MFE if tariff-margin bridge stalls |
| R11L83-C31-02 | 0.20 | 0.20 | regulated-rate theme rejected without pass-through bridge |
| R11L83-C31-03 | 0.20 | 0.20 | policy-theme rally rejected without direct-beneficiary margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_policy_reversal_or_regulatory_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = C31 policy rows need direct beneficiary mapping and explicit tariff/subsidy/revenue/margin bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = C31_policy_direct_beneficiary_tariff_margin_bridge_required
effect = keep direct-beneficiary tariff positives with 4B watch; demote utility policy-theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.89 | -10.09 | may over-credit policy/rate headlines | needs C31 bridge repair |
| P1 canonical shadow bridge profile | 3 | 32.83 on kept positive | -4.59 on kept positive | demotes 017390/004690 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R11L83-C31-01 | 78 | Stage2-Actionable | 80 | Stage2-Actionable + local 4B watch | partially aligned |
| R11L83-C31-02 | 57 | Stage2-Watch/FalsePositive | 49 | Rejected-Stage2 / RiskWatch | improved |
| R11L83-C31-03 | 57 | Stage2-Watch/FalsePositive | 49 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - policy_theme_false_positive_low_MFE_high_MAE
  - tariff_subsidy_pass_through_bridge_required
  - direct_beneficiary_mapping_required
  - 4B_needed_after_policy_MFE_if_margin_bridge_stalls
new_axis_proposed: false
existing_axis_strengthened: C31_policy_direct_beneficiary_tariff_margin_bridge_required
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C31_policy_direct_beneficiary_tariff_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

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
- official tariff/subsidy source
- regulated-rate pass-through detail
- revenue/margin/FCF bridge
- receivable or balance-sheet repair detail
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_policy_direct_beneficiary_tariff_margin_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require direct beneficiary mapping plus tariff/subsidy pass-through and revenue/margin/FCF bridge before Stage2-Actionable","keeps 015760 with 4B watch; demotes 017390/004690","R11L83-C31-01-S2A-20240125|R11L83-C31-02-S2FP-20240219|R11L83-C31-03-S2FP-20240219",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L83-C31-01", "symbol": "015760", "company_name": "한국전력", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE", "case_type": "tariff_normalization_policy_positive_with_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L83-C31-01-S2A-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_direct_beneficiary_positive_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Policy can be Stage2 only if direct beneficiary mapping converts into tariff/revenue/margin/FCF bridge."}
{"row_type": "trigger", "trigger_id": "R11L83-C31-01-S2A-20240125", "case_id": "R11L83-C31-01", "symbol": "015760", "company_name": "한국전력", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_direct_beneficiary_mapping_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "electricity tariff / regulated utility normalization policy proxy; tariff-to-margin/FCF bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_direct_beneficiary_mapping", "tariff_or_subsidy_pass_through_proxy", "revenue_margin_bridge_proxy"], "stage3_evidence_fields": ["confirmed_tariff_or_subsidy_execution", "revision_or_FCF_bridge", "receivable_or_balance_sheet_repair"], "stage4b_evidence_fields": ["policy_theme_overheat", "pass_through_delay", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_policy_reversal_or_regulatory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv", "profile_path": "atlas/symbol_profiles/015/015760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 19160, "MFE_30D_pct": 31.0, "MFE_90D_pct": 32.83, "MFE_180D_pct": 32.83, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.59, "MAE_90D_pct": -4.59, "MAE_180D_pct": -4.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-14", "peak_price": 25450, "drawdown_after_peak_pct": -25.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.76, "four_b_timing_verdict": "local_4B_watch_after_policy_MFE_if_tariff_margin_bridge_stalls", "four_b_evidence_type": ["policy_theme_overheat", "tariff_margin_bridge_delay", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_regulatory_break", "trigger_outcome_label": "policy_direct_beneficiary_positive_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R11L83-C31-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L83-C31-01", "trigger_id": "R11L83-C31-01-S2A-20240125", "symbol": "015760", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"direct_beneficiary_mapping_score": 60, "policy_specificity_score": 55, "tariff_or_subsidy_pass_through_score": 45, "revenue_visibility_score": 45, "margin_bridge_score": 40, "FCF_or_balance_sheet_repair_score": 35, "revision_score": 45, "relative_strength_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "regulatory_reversal_risk_score": 35, "policy_delay_risk_score": 35}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"direct_beneficiary_mapping_score": 60, "policy_specificity_score": 55, "tariff_or_subsidy_pass_through_score": 50, "revenue_visibility_score": 45, "margin_bridge_score": 40, "FCF_or_balance_sheet_repair_score": 35, "revision_score": 45, "relative_strength_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "regulatory_reversal_risk_score": 40, "policy_delay_risk_score": 35}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["direct_beneficiary_mapping_score", "tariff_or_subsidy_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C31 utility-policy rows require direct beneficiary mapping, tariff/subsidy pass-through, revenue/margin and FCF bridge before Stage2-Actionable; policy-theme-only cases are demoted.", "MFE_90D_pct": 32.83, "MAE_90D_pct": -4.59, "score_return_alignment_label": "policy_direct_beneficiary_positive_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_4B_watch_needed"}
{"row_type": "case", "case_id": "R11L83-C31-02", "symbol": "017390", "company_name": "서울가스", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE", "case_type": "regulated_city_gas_rate_policy_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R11L83-C31-02-S2FP-20240219", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_theme_false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Regulated rate headlines should not become Stage2 unless pass-through, volume, receivable, and margin bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R11L83-C31-02-S2FP-20240219", "case_id": "R11L83-C31-02", "symbol": "017390", "company_name": "서울가스", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_direct_beneficiary_mapping_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-19", "evidence_available_at_that_date": "city-gas regulated rate / utility policy proxy without volume/pass-through/margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_direct_beneficiary_mapping", "tariff_or_subsidy_pass_through_proxy", "revenue_margin_bridge_proxy"], "stage3_evidence_fields": ["confirmed_tariff_or_subsidy_execution", "revision_or_FCF_bridge", "receivable_or_balance_sheet_repair"], "stage4b_evidence_fields": ["policy_theme_overheat", "pass_through_delay", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_policy_reversal_or_regulatory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017390/2024.csv", "profile_path": "atlas/symbol_profiles/017/017390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-19", "entry_price": 62900, "MFE_30D_pct": 0.79, "MFE_90D_pct": 0.79, "MFE_180D_pct": 0.79, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.22, "MAE_90D_pct": -9.7, "MAE_180D_pct": -18.28, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 63400, "drawdown_after_peak_pct": -18.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.2, "four_b_full_window_peak_proximity": 0.2, "four_b_timing_verdict": "regulated_rate_theme_rejected_without_pass_through_margin_bridge", "four_b_evidence_type": ["policy_theme_overheat", "tariff_margin_bridge_delay", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_regulatory_break", "trigger_outcome_label": "policy_theme_false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2002_CA_candidates", "same_entry_group_id": "R11L83-C31-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L83-C31-02", "trigger_id": "R11L83-C31-02-S2FP-20240219", "symbol": "017390", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"direct_beneficiary_mapping_score": 20, "policy_specificity_score": 25, "tariff_or_subsidy_pass_through_score": 10, "revenue_visibility_score": 15, "margin_bridge_score": 5, "FCF_or_balance_sheet_repair_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_repricing_score": 25, "execution_risk_score": 65, "regulatory_reversal_risk_score": 60, "policy_delay_risk_score": 55}, "weighted_score_before": 57, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"direct_beneficiary_mapping_score": 10, "policy_specificity_score": 25, "tariff_or_subsidy_pass_through_score": 0, "revenue_visibility_score": 15, "margin_bridge_score": 0, "FCF_or_balance_sheet_repair_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_repricing_score": 25, "execution_risk_score": 80, "regulatory_reversal_risk_score": 60, "policy_delay_risk_score": 55}, "weighted_score_after": 49, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "tariff_or_subsidy_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C31 utility-policy rows require direct beneficiary mapping, tariff/subsidy pass-through, revenue/margin and FCF bridge before Stage2-Actionable; policy-theme-only cases are demoted.", "MFE_90D_pct": 0.79, "MAE_90D_pct": -9.7, "score_return_alignment_label": "policy_theme_false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R11L83-C31-03", "symbol": "004690", "company_name": "삼천리", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE", "case_type": "regulated_utility_policy_valuation_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R11L83-C31-03-S2FP-20240219", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_theme_MFE_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Utility policy narrative must be translated into direct beneficiary economics; otherwise it remains RiskWatch."}
{"row_type": "trigger", "trigger_id": "R11L83-C31-03-S2FP-20240219", "case_id": "R11L83-C31-03", "symbol": "004690", "company_name": "삼천리", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_REGULATED_RATE_POLICY_BENEFICIARY_VS_RATE_PASS_THROUGH_FALSE_POSITIVE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_direct_beneficiary_mapping_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-19", "evidence_available_at_that_date": "utility regulation/rate-policy narrative proxy without direct earnings or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_direct_beneficiary_mapping", "tariff_or_subsidy_pass_through_proxy", "revenue_margin_bridge_proxy"], "stage3_evidence_fields": ["confirmed_tariff_or_subsidy_execution", "revision_or_FCF_bridge", "receivable_or_balance_sheet_repair"], "stage4b_evidence_fields": ["policy_theme_overheat", "pass_through_delay", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_policy_reversal_or_regulatory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004690/2024.csv", "profile_path": "atlas/symbol_profiles/004/004690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-19", "entry_price": 107000, "MFE_30D_pct": 2.06, "MFE_90D_pct": 2.06, "MFE_180D_pct": 2.06, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.8, "MAE_90D_pct": -15.98, "MAE_180D_pct": -21.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 109200, "drawdown_after_peak_pct": -23.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.2, "four_b_full_window_peak_proximity": 0.2, "four_b_timing_verdict": "policy_theme_rally_rejected_without_direct_beneficiary_margin_bridge", "four_b_evidence_type": ["policy_theme_overheat", "tariff_margin_bridge_delay", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_regulatory_break", "trigger_outcome_label": "policy_theme_MFE_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_CA_candidates", "same_entry_group_id": "R11L83-C31-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L83-C31-03", "trigger_id": "R11L83-C31-03-S2FP-20240219", "symbol": "004690", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"direct_beneficiary_mapping_score": 20, "policy_specificity_score": 25, "tariff_or_subsidy_pass_through_score": 10, "revenue_visibility_score": 15, "margin_bridge_score": 5, "FCF_or_balance_sheet_repair_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_repricing_score": 25, "execution_risk_score": 65, "regulatory_reversal_risk_score": 60, "policy_delay_risk_score": 55}, "weighted_score_before": 57, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"direct_beneficiary_mapping_score": 10, "policy_specificity_score": 25, "tariff_or_subsidy_pass_through_score": 0, "revenue_visibility_score": 15, "margin_bridge_score": 0, "FCF_or_balance_sheet_repair_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_repricing_score": 25, "execution_risk_score": 80, "regulatory_reversal_risk_score": 60, "policy_delay_risk_score": 55}, "weighted_score_after": 49, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "tariff_or_subsidy_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C31 utility-policy rows require direct beneficiary mapping, tariff/subsidy pass-through, revenue/margin and FCF bridge before Stage2-Actionable; policy-theme-only cases are demoted.", "MFE_90D_pct": 2.06, "MAE_90D_pct": -15.98, "score_return_alignment_label": "policy_theme_MFE_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C31_policy_direct_beneficiary_tariff_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Policy/subsidy/event rerating requires direct beneficiary mapping plus tariff/subsidy pass-through and revenue/margin/FCF bridge; utility-rate theme alone fades.", "backtest_effect": "keeps 015760 as policy-positive with local 4B watch; demotes 017390/004690 policy-theme false positives", "trigger_ids": "R11L83-C31-01-S2A-20240125|R11L83-C31-02-S2FP-20240219|R11L83-C31-03-S2FP-20240219", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R11", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_theme_false_positive_low_MFE_high_MAE", "tariff_subsidy_pass_through_bridge_required", "direct_beneficiary_mapping_required", "4B_needed_after_policy_MFE_if_margin_bridge_stalls"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C31, test a canonical-archetype guard requiring direct beneficiary mapping plus tariff/subsidy pass-through and revenue/margin/FCF bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 83
next_round = R12
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
