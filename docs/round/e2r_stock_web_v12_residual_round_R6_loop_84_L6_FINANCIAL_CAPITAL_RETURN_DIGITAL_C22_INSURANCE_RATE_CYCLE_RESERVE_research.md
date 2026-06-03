# E2R Stock-Web v12 Residual Research — R6 Loop 84 / L6 / C22

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 84,
  "computed_next_round": "R7",
  "computed_next_loop": 84,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "insurance_rate_cycle_reserve_guardrail",
    "CSM_reserve_quality_to_capital_return_bridge_test",
    "local_4B_timing_after_insurance_MFE",
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
scheduled_round = R6
scheduled_loop = 84
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R6 is the financial / capital return / digital-finance round. This run selects C22 because loop83 already tested C21 capital-return/PBR rerating, while C22 is the insurance-specific bucket.

The tested mechanism:

```text
rate cycle / IFRS17 / CSM / reserve headline
→ CSM quality and reserve adequacy
→ underwriting ROE and solvency buffer
→ dividend / buyback / capital-return execution
→ durable rerating or local 4B / false-positive fade
```

C22 is not “insurance beta went up.” It is the actuarial bridge: the policy book must convert into reserve quality, capital flexibility, and shareholder return.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C22 top-covered symbols include `000810`, `005830`, `088350`, `001450`, `032830`, and `085620`. This run avoids that top-covered set and uses:

```text
000370 / 한화손해보험
082640 / 동양생명
000540 / 흥국화재
```

All three are treated as new independent C22 insurance-rate / reserve / capital-return cases for this loop. No hard duplicate is intentionally reused.

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
| 000370 | 한화손해보험 | `atlas/symbol_profiles/000/000370.json` | old CA candidates through 2017; selected 2024 forward window clean |
| 082640 | 동양생명 | `atlas/symbol_profiles/082/082640.json` | old 2017 CA candidate; selected 2024 forward window clean |
| 000540 | 흥국화재 | `atlas/symbol_profiles/000/000540.json` | old CA candidates through 2011; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R6L84-C22-01 | 000370 | 2024-01-25 | 3,970 | 180D | clean | true |
| R6L84-C22-02 | 082640 | 2024-06-26 | 7,000 | 180D | clean | true |
| R6L84-C22-03 | 000540 | 2024-02-13 | 5,280 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | P_AND_C_RATE_CYCLE_CAPITAL_RETURN | keep Stage2 only with rate-cycle / reserve-quality / underwriting ROE / capital-return bridge; add local 4B after MFE |
| C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_CSM_HIGH_MAE_RISKWATCH | allow Stage2 only with high-MAE RiskWatch when MFE is real but CSM/reserve evidence is unrepaired |
| C22_INSURANCE_RATE_CYCLE_RESERVE | SMALL_INSURER_VALUEUP_THEME_FADE | reject when the move is theme beta without solvency buffer and capital-return execution |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R6L84-C22-01 | 000370 | 한화손해보험 | Stage2-Actionable | 2024-01-25 | 3,970 | 56.93 | -1.26 | current_profile_partially_correct_local_4B_watch_needed |
| R6L84-C22-02 | 082640 | 동양생명 | Stage2-Actionable | 2024-06-26 | 7,000 | 34.86 | -25.43 | current_profile_4B_too_late_high_MAE |
| R6L84-C22-03 | 000540 | 흥국화재 | Stage2-FalsePositive | 2024-02-13 | 5,280 | 25.0 | -34.47 | current_profile_false_positive_high_MAE |

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

This MD therefore creates a source-repair queue and a C22 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: IFRS17/CSM detail, reserve adequacy, solvency/K-ICS or RBC buffer, underwriting ROE, capital-return announcement, company disclosure, or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 000370 | `atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv` | `atlas/symbol_profiles/000/000370.json` |
| 082640 | `atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv` | `atlas/symbol_profiles/082/082640.json` |
| 000540 | `atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv` | `atlas/symbol_profiles/000/000540.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 000370 / 한화손해보험

C22 P&C insurance positive with local 4B watch. The price path delivered strong MFE with small initial MAE. The model should keep Stage2 only if CSM/reserve quality, underwriting ROE and shareholder-return bridge survive source repair.

### Case 2 — 082640 / 동양생명

C22 life-insurance positive but high-MAE. The path produced meaningful MFE, but later drawdown was too large for clean Green. It should stay Stage2-Actionable with high-MAE RiskWatch until reserve quality and capital-return execution are confirmed.

### Case 3 — 000540 / 흥국화재

C22 small-insurer value-up false positive. The MFE came fast, but the drawdown afterward was too deep. This is the rejection row: insurance beta and value-up excitement alone are not reserve-quality or capital-return evidence.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 000370 | 3,970 | 55.42 | -1.26 | 55.42 | -1.26 | 56.93 | -1.26 | 2024-08-20 / 6,230 | -21.91 |
| 082640 | 7,000 | 34.86 | -5.29 | 34.86 | -25.43 | 34.86 | -25.43 | 2024-07-31 / 9,440 | -44.70 |
| 000540 | 5,280 | 25.00 | -23.01 | 25.00 | -28.13 | 25.00 | -34.47 | 2024-02-14 / 6,600 | -47.58 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R6L84-C22-01 | Stage2-Actionable if CSM/reserve/capital-return bridge exists | strong MFE, controlled MAE, later drawdown | partially correct; local 4B watch needed |
| R6L84-C22-02 | Stage2-Actionable if life-insurance rate cycle is over-credited | good MFE but high MAE and drawdown | high-MAE RiskWatch needed |
| R6L84-C22-03 | risk of treating small-insurer value-up theme as Stage2 | quick MFE / deep MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C22, the residual is not Green lateness. The residual is whether insurance MFE becomes clean Stage2/Green before CSM quality, reserve adequacy, solvency buffer and capital-return execution are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R6L84-C22-01 | 0.82 | 0.72 | local 4B watch after insurance MFE if CSM/capital-return bridge stalls |
| R6L84-C22-02 | 0.82 | 0.72 | local 4B and high-MAE RiskWatch when life-insurance MFE outruns evidence |
| R6L84-C22-03 | 0.30 | 0.25 | insurance theme overheat rejected without reserve/capital-return bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_reserve_or_solvency_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L6 insurance rows need CSM quality, reserve adequacy, solvency buffer and capital-return execution before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
candidate_axis = C22_rate_cycle_CSM_reserve_capital_return_bridge_required
effect = keep insurance positives with local 4B/high-MAE watch; demote small-insurer theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 38.43 | -18.27 | may over-credit insurance value-up/rate-cycle theme MFE | needs C22 bridge repair |
| P1 canonical shadow bridge profile | 3 | 45.14 on kept positives | -13.35 on kept positives | demotes 000540 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R6L84-C22-01 | 80 | Stage2-Actionable | 78 | Stage2-Actionable + local 4B watch | partially aligned |
| R6L84-C22-02 | 74 | Stage2-Actionable | 71 | Stage2-Actionable + high-MAE RiskWatch/local 4B watch | partially aligned |
| R6L84-C22-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - insurance_theme_false_positive_high_MAE
  - rate_cycle_CSM_reserve_capital_return_bridge_required
  - local_4B_late_after_insurance_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C22_rate_cycle_CSM_reserve_capital_return_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C22_rate_cycle_CSM_reserve_capital_return_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.

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
- CSM quality and reserve detail
- solvency buffer / K-ICS or RBC detail
- underwriting ROE bridge
- capital-return execution
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_rate_cycle_CSM_reserve_capital_return_bridge_required,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Require rate cycle, CSM quality, reserve adequacy, solvency buffer and capital-return execution before clean Stage2/Green","keeps 000370/082640 with local 4B or high-MAE RiskWatch; demotes 000540","R6L84-C22-01-S2A-20240125|R6L84-C22-02-S2A-20240626|R6L84-C22-03-S2FP-20240213",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L84-C22-01", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE", "case_type": "P_and_C_insurance_rate_cycle_capital_return_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L84-C22-01-S2A-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_rate_cycle_MFE_with_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C22 can keep Stage2 only when rate-cycle/CSM/reserve quality converts into underwriting ROE and capital-return bridge."}
{"row_type": "trigger", "trigger_id": "R6L84-C22-01-S2A-20240125", "case_id": "R6L84-C22-01", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail|local_4B_timing_after_insurance_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "P&C insurance rate-cycle / reserve-quality / value-up capital-return proxy; primary CSM/underwriting evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["rate_cycle_proxy", "CSM_or_reserve_quality_proxy", "capital_return_proxy"], "stage3_evidence_fields": ["confirmed_CSM_quality", "reserve_adequacy", "underwriting_ROE", "solvency_buffer", "capital_return_execution"], "stage4b_evidence_fields": ["insurance_MFE_without_reserve_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reserve_or_solvency_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv", "profile_path": "atlas/symbol_profiles/000/000370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 3970, "MFE_30D_pct": 55.42, "MFE_90D_pct": 55.42, "MFE_180D_pct": 56.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.26, "MAE_90D_pct": -1.26, "MAE_180D_pct": -1.26, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-20", "peak_price": 6230, "drawdown_after_peak_pct": -21.91, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_insurance_MFE_if_CSM_capital_return_bridge_stalls", "four_b_evidence_type": ["insurance_MFE_without_reserve_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reserve_or_solvency_break", "trigger_outcome_label": "positive_rate_cycle_MFE_with_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_CA_candidates", "same_entry_group_id": "R6L84-C22-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L84-C22-01", "trigger_id": "R6L84-C22-01-S2A-20240125", "symbol": "000370", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 55, "CSM_quality_score": 40, "reserve_adequacy_score": 40, "underwriting_ROE_score": 45, "capital_return_execution_score": 35, "solvency_buffer_score": 40, "revision_score": 50, "relative_strength_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 40, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"rate_cycle_score": 55, "CSM_quality_score": 40, "reserve_adequacy_score": 40, "underwriting_ROE_score": 45, "capital_return_execution_score": 35, "solvency_buffer_score": 40, "revision_score": 50, "relative_strength_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 40, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["CSM_quality_score", "reserve_adequacy_score", "capital_return_execution_score", "solvency_buffer_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C22 requires rate-cycle/CSM/reserve quality to convert into underwriting ROE, solvency buffer and capital-return execution before clean Stage2/Green; insurance-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 55.42, "MAE_90D_pct": -1.26, "score_return_alignment_label": "positive_rate_cycle_MFE_with_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R6L84-C22-02", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE", "case_type": "life_insurance_rate_cycle_positive_but_high_MAE_risk", "positive_or_counterexample": "positive", "best_trigger": "R6L84-C22-02-S2A-20240626", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MFE_high_MAE_positive_requires_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Life-insurance rerating can be real, but CSM quality, reserve adequacy and shareholder-return execution must be repaired before clean Green."}
{"row_type": "trigger", "trigger_id": "R6L84-C22-02-S2A-20240626", "case_id": "R6L84-C22-02", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail|local_4B_timing_after_insurance_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "evidence_available_at_that_date": "life-insurance rate-cycle / CSM / reserve-quality and capital-return proxy; primary CSM movement and reserve evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["rate_cycle_proxy", "CSM_or_reserve_quality_proxy", "capital_return_proxy"], "stage3_evidence_fields": ["confirmed_CSM_quality", "reserve_adequacy", "underwriting_ROE", "solvency_buffer", "capital_return_execution"], "stage4b_evidence_fields": ["insurance_MFE_without_reserve_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reserve_or_solvency_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "profile_path": "atlas/symbol_profiles/082/082640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-26", "entry_price": 7000, "MFE_30D_pct": 34.86, "MFE_90D_pct": 34.86, "MFE_180D_pct": 34.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.29, "MAE_90D_pct": -25.43, "MAE_180D_pct": -25.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 9440, "drawdown_after_peak_pct": -44.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_and_high_MAE_RiskWatch_needed_when_life_insurance_MFE_outruns_reserve_quality_evidence", "four_b_evidence_type": ["insurance_MFE_without_reserve_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reserve_or_solvency_break", "trigger_outcome_label": "high_MFE_high_MAE_positive_requires_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_CA_candidate", "same_entry_group_id": "R6L84-C22-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L84-C22-02", "trigger_id": "R6L84-C22-02-S2A-20240626", "symbol": "082640", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 55, "CSM_quality_score": 40, "reserve_adequacy_score": 40, "underwriting_ROE_score": 45, "capital_return_execution_score": 35, "solvency_buffer_score": 40, "revision_score": 50, "relative_strength_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"rate_cycle_score": 55, "CSM_quality_score": 40, "reserve_adequacy_score": 40, "underwriting_ROE_score": 45, "capital_return_execution_score": 35, "solvency_buffer_score": 40, "revision_score": 50, "relative_strength_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 75, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable + high-MAE RiskWatch/local 4B watch", "changed_components": ["CSM_quality_score", "reserve_adequacy_score", "capital_return_execution_score", "solvency_buffer_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C22 requires rate-cycle/CSM/reserve quality to convert into underwriting ROE, solvency buffer and capital-return execution before clean Stage2/Green; insurance-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 34.86, "MAE_90D_pct": -25.43, "score_return_alignment_label": "high_MFE_high_MAE_positive_requires_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE"}
{"row_type": "case", "case_id": "R6L84-C22-03", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE", "case_type": "small_insurer_valueup_rate_cycle_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R6L84-C22-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_overheat_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Small-insurer value-up/rate-cycle moves should stay RiskWatch unless reserve quality, solvency buffer and capital-return execution are explicit."}
{"row_type": "trigger", "trigger_id": "R6L84-C22-03-S2FP-20240213", "case_id": "R6L84-C22-03", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_THEME_OVERHEAT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail|local_4B_timing_after_insurance_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "small-insurer value-up / rate-cycle theme proxy without enough capital buffer, reserve quality and capital-return bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["rate_cycle_proxy", "CSM_or_reserve_quality_proxy", "capital_return_proxy"], "stage3_evidence_fields": ["confirmed_CSM_quality", "reserve_adequacy", "underwriting_ROE", "solvency_buffer", "capital_return_execution"], "stage4b_evidence_fields": ["insurance_MFE_without_reserve_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reserve_or_solvency_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv", "profile_path": "atlas/symbol_profiles/000/000540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 5280, "MFE_30D_pct": 25.0, "MFE_90D_pct": 25.0, "MFE_180D_pct": 25.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.01, "MAE_90D_pct": -28.13, "MAE_180D_pct": -34.47, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-14", "peak_price": 6600, "drawdown_after_peak_pct": -47.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "insurance_theme_overheat_rejected_without_reserve_capital_return_bridge", "four_b_evidence_type": ["insurance_MFE_without_reserve_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reserve_or_solvency_break", "trigger_outcome_label": "theme_overheat_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_CA_candidates", "same_entry_group_id": "R6L84-C22-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L84-C22-03", "trigger_id": "R6L84-C22-03-S2FP-20240213", "symbol": "000540", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 35, "CSM_quality_score": 10, "reserve_adequacy_score": 10, "underwriting_ROE_score": 15, "capital_return_execution_score": 5, "solvency_buffer_score": 15, "revision_score": 20, "relative_strength_score": 40, "valuation_repricing_score": 35, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"rate_cycle_score": 35, "CSM_quality_score": 0, "reserve_adequacy_score": 0, "underwriting_ROE_score": 15, "capital_return_execution_score": 0, "solvency_buffer_score": 5, "revision_score": 20, "relative_strength_score": 40, "valuation_repricing_score": 35, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["CSM_quality_score", "reserve_adequacy_score", "capital_return_execution_score", "solvency_buffer_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C22 requires rate-cycle/CSM/reserve quality to convert into underwriting ROE, solvency buffer and capital-return execution before clean Stage2/Green; insurance-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 25.0, "MAE_90D_pct": -28.13, "score_return_alignment_label": "theme_overheat_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C22_rate_cycle_CSM_reserve_capital_return_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Insurance rerating requires rate cycle, CSM quality, reserve adequacy, solvency buffer and capital-return execution; insurance-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 000370/082640 with local 4B or high-MAE RiskWatch; demotes 000540 theme false positive", "trigger_ids": "R6L84-C22-01-S2A-20240125|R6L84-C22-02-S2A-20240626|R6L84-C22-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R6", "loop": 84, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["insurance_theme_false_positive_high_MAE", "rate_cycle_CSM_reserve_capital_return_bridge_required", "local_4B_late_after_insurance_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C22, test a canonical-archetype guard requiring CSM quality, reserve adequacy, solvency buffer, underwriting ROE and capital-return execution before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 84
next_round = R7
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
