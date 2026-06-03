# E2R Stock-Web v12 Residual Research — R6 Loop 86 / L6 / C22

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 86,
  "computed_next_round": "R7",
  "computed_next_loop": 86,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "insurance_rate_cycle_reserve_guardrail",
    "insurance_valueup_theme_vs_ROE_reserve_capital_buffer_bridge_test",
    "small_nonlife_policyholder_margin_beta_false_positive_test",
    "local_4B_timing_after_insurance_MFE",
    "hard_4C_non_price_reserve_capital_break_protection",
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
scheduled_loop = 86
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R6 is the financial / capital return / digital finance round. This run selects C22 because loop85 R6 used C21 brokerage ROE/PBR, while C22 remains the insurance reserve/rate-cycle axis for loop86.

The tested mechanism:

```text
insurance / reinsurance / non-life value-up headline
→ reserve adequacy and loss-ratio or combined-ratio discipline
→ capital buffer and solvency
→ payout / dividend execution
→ ROE quality and liquidity control
→ durable rerating or small-insurance value-up beta fade
```

C22 is the reserve vault. A value-up candle can open the door, but underwriting, reserves, solvency and payout decide whether anything is inside.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C22 top-covered symbols include `000810`, `005830`, `088350`, `001450`, `032830`, and `085620`. This run avoids that top-covered set and uses:

```text
003690 / 코리안리
000370 / 한화손해보험
000540 / 흥국화재
```

All three are treated as new independent C22 insurance-rate-cycle / reserve cases for this loop. No hard duplicate is intentionally reused.

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
| 003690 | 코리안리 | `atlas/symbol_profiles/003/003690.json` | old CA candidates through 2004; selected 2024 forward window clean |
| 000370 | 한화손해보험 | `atlas/symbol_profiles/000/000370.json` | old CA candidates through 2017; selected 2024 forward window clean |
| 000540 | 흥국화재 | `atlas/symbol_profiles/000/000540.json` | old CA candidates through 2011; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R6L86-C22-01 | 003690 | 2024-02-13 | 7,910 | 180D | clean | true |
| R6L86-C22-02 | 000370 | 2024-02-13 | 5,520 | 180D | clean | true |
| R6L86-C22-03 | 000540 | 2024-02-13 | 5,280 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | REINSURANCE_RATE_RESERVE_CAPITAL_RETURN | keep Stage2 with reserve adequacy, combined-ratio discipline, capital buffer and payout bridge |
| C22_INSURANCE_RATE_CYCLE_RESERVE | NONLIFE_VALUEUP_BETA_HIGH_MAE | reject or RiskWatch when value-up MFE lacks reserve/capital/payout bridge |
| C22_INSURANCE_RATE_CYCLE_RESERVE | SMALL_NONLIFE_THEME_BLOWOFF | reject small-insurance theme spike without solvency, liquidity and underwriting evidence |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R6L86-C22-01 | 003690 | 코리안리 | Stage2-Actionable | 2024-02-13 | 7,910 | 20.73 | -5.18 | current_profile_partially_correct_reserve_capital_return_bridge_needed |
| R6L86-C22-02 | 000370 | 한화손해보험 | Stage2-FalsePositive | 2024-02-13 | 5,520 | 12.86 | -23.82 | current_profile_false_positive_high_MAE_valueup_beta |
| R6L86-C22-03 | 000540 | 흥국화재 | Stage2-FalsePositive | 2024-02-13 | 5,280 | 25.0 | -39.39 | current_profile_false_positive_theme_blowoff_high_MAE |

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

This MD creates a source-repair queue and a C22 insurance shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: reserve adequacy, loss-ratio/combined-ratio path, capital buffer, solvency/liquidity, payout/dividend execution, ROE quality, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 003690 | `atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv` | `atlas/symbol_profiles/003/003690.json` |
| 000370 | `atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv` | `atlas/symbol_profiles/000/000370.json` |
| 000540 | `atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv` | `atlas/symbol_profiles/000/000540.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 003690 / 코리안리

C22 reinsurance rate-cycle positive with local 4B watch. The February trigger had controlled MAE and later MFE into the autumn insurance rerating path. It is kept positive, but still requires reserve, combined-ratio and payout source repair before clean Green.

### Case 2 — 000370 / 한화손해보험

C22 non-life value-up beta false positive. The same-day MFE was tradable, and another MFE later appeared, but the early MAE was deep. This is not clean Stage2 unless reserve quality, capital buffer and payout execution are visible at entry.

### Case 3 — 000540 / 흥국화재

C22 small non-life blowoff counterexample. The entry produced a large same-week MFE, but later collapsed deeply. Small-insurance value-up beta should not validate C22 without solvency, reserve and liquidity bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 003690 | 7,910 | 8.09 | -1.64 | 8.09 | -5.18 | 20.73 | -5.18 | 2024-11-05 / 9,550 | -19.37 |
| 000370 | 5,520 | 11.78 | -20.92 | 11.78 | -23.82 | 12.86 | -23.82 | 2024-08-20 / 6,230 | -21.03 |
| 000540 | 5,280 | 25.00 | -23.01 | 25.00 | -28.69 | 25.00 | -39.39 | 2024-02-14 / 6,600 | -51.52 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R6L86-C22-01 | Stage2-Actionable if reserve/capital bridge exists | controlled MAE, later MFE | partially correct; reserve-capital bridge needed |
| R6L86-C22-02 | risk of treating non-life value-up beta as Stage2 | MFE but deep MAE | false positive / high-MAE guardrail |
| R6L86-C22-03 | risk of treating small-insurance spike as Stage2 | large MFE then severe collapse | false positive / theme blowoff |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C22, the residual is whether insurance/value-up MFE becomes clean Stage2/Green before reserve adequacy, combined-ratio discipline, capital buffer and payout execution are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R6L86-C22-01 | 0.70 | 0.60 | local 4B watch after reinsurance MFE if rate/reserve/capital-return bridge stalls |
| R6L86-C22-02 | 0.35 | 0.30 | non-life insurance value-up MFE rejected without reserve/capital/payout bridge |
| R6L86-C22-03 | 0.35 | 0.30 | small non-life theme MFE rejected without reserve/solvency/payout bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_reserve_loss_or_capital_buffer_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C22 hard 4C requires confirmed reserve loss, adverse loss-ratio/combined-ratio deterioration, capital buffer break, solvency/liquidity shock, payout reversal or regulatory-capital thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L6/C22 insurance rows need reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
candidate_axis = C22_insurance_reserve_capital_buffer_payout_bridge_required
effect = keep reinsurance positives with local 4B/reserve-capital watch; demote high-MAE value-up beta false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.96 | -19.23 | may over-credit insurance value-up beta without reserve/capital bridge | needs C22 reserve/payout bridge repair |
| P1 canonical shadow bridge profile | 3 | 8.09 on kept positive at 90D / 20.73 at 180D | demotes 000370/000540 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R6L86-C22-01 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/reserve-capital watch | partially aligned |
| R6L86-C22-02 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Insurance value-up beta RiskWatch | improved |
| R6L86-C22-03 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Insurance value-up beta RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - insurance_valueup_beta_false_positive_high_MAE
  - reserve_capital_buffer_payout_bridge_required
  - small_nonlife_theme_blowoff
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_reserve_or_capital_break
new_axis_proposed: false
existing_axis_strengthened:
  - C22_insurance_reserve_capital_buffer_payout_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C22_insurance_reserve_capital_buffer_payout_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.

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
- reserve adequacy source
- loss-ratio / combined-ratio evidence
- capital buffer / solvency evidence
- payout/dividend execution
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_insurance_reserve_capital_buffer_payout_bridge_required,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Require reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control before clean Stage2/Green","keeps 003690 with reserve/capital-return watch; demotes 000370/000540","R6L86-C22-01-S2A-20240213|R6L86-C22-02-S2FP-20240213|R6L86-C22-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L86-C22-01", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "case_type": "reinsurance_rate_cycle_reserve_capital_buffer_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L86-C22-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "controlled_MAE_positive_MFE_but_reserve_ROE_payout_bridge_required", "current_profile_verdict": "current_profile_partially_correct_reserve_capital_return_bridge_needed", "price_source": "Songdaiki/stock-web", "notes": "C22 reinsurance positives need rate-cycle evidence, reserve adequacy, combined-ratio discipline, capital buffer and payout visibility before clean Green."}
{"row_type": "trigger", "trigger_id": "R6L86-C22-01-S2A-20240213", "case_id": "R6L86-C22-01", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail|reserve_capital_payout_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "reinsurance rate cycle, underwriting margin, reserve adequacy and capital-return proxy; primary combined-ratio/reserve/capital evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["insurance_rate_cycle_proxy", "reserve_or_capital_buffer_proxy", "valueup_or_payout_proxy"], "stage3_evidence_fields": ["confirmed_reserve_adequacy", "loss_ratio_or_combined_ratio", "capital_buffer", "payout_execution", "ROE_quality", "liquidity_control"], "stage4b_evidence_fields": ["insurance_MFE_without_reserve_bridge", "valueup_beta_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reserve_loss_or_capital_buffer_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv", "profile_path": "atlas/symbol_profiles/003/003690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 7910, "MFE_30D_pct": 8.09, "MFE_90D_pct": 8.09, "MFE_180D_pct": 20.73, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.64, "MAE_90D_pct": -5.18, "MAE_180D_pct": -5.18, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-05", "peak_price": 9550, "drawdown_after_peak_pct": -19.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "local_4B_watch_after_reinsurance_MFE_if_rate_reserve_capital_return_bridge_stalls", "four_b_evidence_type": ["insurance_MFE_without_reserve_capital_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reserve_loss_or_capital_buffer_break", "trigger_outcome_label": "controlled_MAE_positive_MFE_but_reserve_ROE_payout_bridge_required", "current_profile_verdict": "current_profile_partially_correct_reserve_capital_return_bridge_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2004_CA_candidate", "same_entry_group_id": "R6L86-C22-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L86-C22-01", "trigger_id": "R6L86-C22-01-S2A-20240213", "symbol": "003690", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 50, "reserve_adequacy_score": 45, "loss_ratio_or_combined_ratio_score": 45, "capital_buffer_score": 45, "payout_execution_score": 40, "ROE_quality_score": 45, "liquidity_risk_score": 30, "valuation_repricing_score": 45, "relative_strength_score": 55, "theme_blowoff_risk_score": 45, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"rate_cycle_score": 50, "reserve_adequacy_score": 45, "loss_ratio_or_combined_ratio_score": 45, "capital_buffer_score": 45, "payout_execution_score": 40, "ROE_quality_score": 45, "liquidity_risk_score": 30, "valuation_repricing_score": 45, "relative_strength_score": 55, "theme_blowoff_risk_score": 60, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/reserve-capital watch", "changed_components": ["reserve_adequacy_score", "loss_ratio_or_combined_ratio_score", "capital_buffer_score", "payout_execution_score", "ROE_quality_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C22 requires insurance/rate-cycle MFE to convert into reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control before clean Stage2/Green; small-insurance value-up beta MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 8.09, "MAE_90D_pct": -5.18, "score_return_alignment_label": "controlled_MAE_positive_MFE_but_reserve_ROE_payout_bridge_required", "current_profile_verdict": "current_profile_partially_correct_reserve_capital_return_bridge_needed"}
{"row_type": "case", "case_id": "R6L86-C22-02", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "case_type": "nonlife_insurance_valueup_beta_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R6L86-C22-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_MFE_with_deep_MAE_insurance_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_valueup_beta", "price_source": "Songdaiki/stock-web", "notes": "Non-life value-up beta should not validate C22 unless reserve quality, loss-ratio trend, capital buffer and payout execution are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R6L86-C22-02-S2FP-20240213", "case_id": "R6L86-C22-02", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail|reserve_capital_payout_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "non-life insurance value-up, reserve release and rate-cycle proxy without confirmed reserve adequacy, payout execution and capital buffer bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["insurance_rate_cycle_proxy", "reserve_or_capital_buffer_proxy", "valueup_or_payout_proxy"], "stage3_evidence_fields": ["confirmed_reserve_adequacy", "loss_ratio_or_combined_ratio", "capital_buffer", "payout_execution", "ROE_quality", "liquidity_control"], "stage4b_evidence_fields": ["insurance_MFE_without_reserve_bridge", "valueup_beta_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reserve_loss_or_capital_buffer_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv", "profile_path": "atlas/symbol_profiles/000/000370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 5520, "MFE_30D_pct": 11.78, "MFE_90D_pct": 11.78, "MFE_180D_pct": 12.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.92, "MAE_90D_pct": -23.82, "MAE_180D_pct": -23.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-20", "peak_price": 6230, "drawdown_after_peak_pct": -21.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "nonlife_insurance_valueup_MFE_rejected_without_reserve_capital_payout_bridge", "four_b_evidence_type": ["insurance_MFE_without_reserve_capital_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reserve_loss_or_capital_buffer_break", "trigger_outcome_label": "theme_MFE_with_deep_MAE_insurance_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_valueup_beta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2017_CA_candidate", "same_entry_group_id": "R6L86-C22-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L86-C22-02", "trigger_id": "R6L86-C22-02-S2FP-20240213", "symbol": "000370", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 35, "reserve_adequacy_score": 10, "loss_ratio_or_combined_ratio_score": 10, "capital_buffer_score": 15, "payout_execution_score": 5, "ROE_quality_score": 15, "liquidity_risk_score": 75, "valuation_repricing_score": 40, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"rate_cycle_score": 35, "reserve_adequacy_score": 0, "loss_ratio_or_combined_ratio_score": 0, "capital_buffer_score": 5, "payout_execution_score": 0, "ROE_quality_score": 5, "liquidity_risk_score": 75, "valuation_repricing_score": 40, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Insurance value-up beta RiskWatch", "changed_components": ["reserve_adequacy_score", "loss_ratio_or_combined_ratio_score", "capital_buffer_score", "payout_execution_score", "ROE_quality_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C22 requires insurance/rate-cycle MFE to convert into reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control before clean Stage2/Green; small-insurance value-up beta MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 11.78, "MAE_90D_pct": -23.82, "score_return_alignment_label": "theme_MFE_with_deep_MAE_insurance_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_valueup_beta"}
{"row_type": "case", "case_id": "R6L86-C22-03", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "case_type": "small_nonlife_insurance_rate_cycle_theme_blowoff_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L86-C22-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_same_week_MFE_then_deep_MAE_small_insurance_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Small non-life insurance theme spikes should remain RiskWatch unless reserve adequacy, solvency buffer, loss-ratio trend, liquidity and payout bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R6L86-C22-03-S2FP-20240213", "case_id": "R6L86-C22-03", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail|reserve_capital_payout_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "small non-life insurance, value-up and rate-cycle theme proxy without durable reserve, solvency, liquidity or payout bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["insurance_rate_cycle_proxy", "reserve_or_capital_buffer_proxy", "valueup_or_payout_proxy"], "stage3_evidence_fields": ["confirmed_reserve_adequacy", "loss_ratio_or_combined_ratio", "capital_buffer", "payout_execution", "ROE_quality", "liquidity_control"], "stage4b_evidence_fields": ["insurance_MFE_without_reserve_bridge", "valueup_beta_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reserve_loss_or_capital_buffer_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv", "profile_path": "atlas/symbol_profiles/000/000540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 5280, "MFE_30D_pct": 25.0, "MFE_90D_pct": 25.0, "MFE_180D_pct": 25.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.01, "MAE_90D_pct": -28.69, "MAE_180D_pct": -39.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-14", "peak_price": 6600, "drawdown_after_peak_pct": -51.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "small_nonlife_theme_MFE_rejected_without_reserve_solvency_payout_bridge", "four_b_evidence_type": ["insurance_MFE_without_reserve_capital_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reserve_loss_or_capital_buffer_break", "trigger_outcome_label": "large_same_week_MFE_then_deep_MAE_small_insurance_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2011_CA_candidate", "same_entry_group_id": "R6L86-C22-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L86-C22-03", "trigger_id": "R6L86-C22-03-S2FP-20240213", "symbol": "000540", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 35, "reserve_adequacy_score": 10, "loss_ratio_or_combined_ratio_score": 10, "capital_buffer_score": 15, "payout_execution_score": 5, "ROE_quality_score": 15, "liquidity_risk_score": 75, "valuation_repricing_score": 40, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"rate_cycle_score": 35, "reserve_adequacy_score": 0, "loss_ratio_or_combined_ratio_score": 0, "capital_buffer_score": 5, "payout_execution_score": 0, "ROE_quality_score": 5, "liquidity_risk_score": 75, "valuation_repricing_score": 40, "relative_strength_score": 45, "theme_blowoff_risk_score": 80, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Insurance value-up beta RiskWatch", "changed_components": ["reserve_adequacy_score", "loss_ratio_or_combined_ratio_score", "capital_buffer_score", "payout_execution_score", "ROE_quality_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C22 requires insurance/rate-cycle MFE to convert into reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control before clean Stage2/Green; small-insurance value-up beta MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 25.0, "MAE_90D_pct": -28.69, "score_return_alignment_label": "large_same_week_MFE_then_deep_MAE_small_insurance_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_high_MAE"}
{"row_type": "shadow_weight", "axis": "C22_insurance_reserve_capital_buffer_payout_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Insurance/rate-cycle rerating requires reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control; value-up beta MFE without bridge fades into high MAE or small-insurance blowoff.", "backtest_effect": "keeps 003690 with reserve/capital-return watch; demotes 000370/000540 insurance value-up beta false positives", "trigger_ids": "R6L86-C22-01-S2A-20240213|R6L86-C22-02-S2FP-20240213|R6L86-C22-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R6", "loop": 86, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["insurance_valueup_beta_false_positive_high_MAE", "reserve_capital_buffer_payout_bridge_required", "small_nonlife_theme_blowoff", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_reserve_or_capital_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C22, test a canonical-archetype guard requiring reserve adequacy, loss/combined-ratio discipline, capital buffer, payout execution, ROE quality and liquidity control before clean Stage2/Green. Keep hard 4C blocked unless a non-price reserve/capital/payout thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 86
next_round = R7
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
