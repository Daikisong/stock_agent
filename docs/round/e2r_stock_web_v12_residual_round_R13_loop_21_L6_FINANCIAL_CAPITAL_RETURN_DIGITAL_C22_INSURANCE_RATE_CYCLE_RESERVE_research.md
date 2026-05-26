# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 21
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_RESERVE_QUALITY_CAPITAL_RETURN_HOLDOUT_2025
output_file = e2r_stock_web_v12_residual_round_R13_loop_21_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration research artifact. It is not a live watchlist, not an investment recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The research question is not whether the global Stage2 bonus works in general. The residual question is narrower: **inside C22 insurance, does the current profile still confuse generic insurance/rate beta with confirmed reserve-quality/capital-return evidence?**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 21
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_RESERVE_QUALITY_CAPITAL_RETURN_HOLDOUT_2025

loop_objective =
  holdout_validation
  residual_false_positive_mining
  residual_missed_structural_mining
  sector_specific_rule_discovery
  canonical_archetype_compression
  counterexample_mining
  coverage_gap_fill
  4B_non_price_requirement_stress_test
```

Scope compression:

```text
P&C clean route:
  reserve quality + shareholder return + confirmed revision -> Stage2/Yellow promotion eligible

Generic insurance beta route:
  rate-cut/rate-beta + low PBR + price strength only -> cap below Green

Life-insurer beta route:
  rate sensitivity can produce very large MFE, but without CSM/capital confirmation it also produces high MAE; it should be a separate guarded route.
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage and duplication context. No `src/e2r` code was opened.

Observed calibration ingest context:

```text
discovered_result_md_count = 107
raw_trigger_rows = 4951
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
loops_covered in applied ingest = 1~9
```

Applied global axes already exist and are not re-proposed as global deltas:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

Novelty check:

```text
new_independent_case_count = 4
reused_case_count = 0
required_new_independent_case_ratio = 0.60
actual_new_independent_case_ratio = 1.00
novelty_basis = different 2025 trigger family, C22-specific reserve-quality/life-rate-beta residual split, and 2025 holdout window
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
| --- | --- |
| price_atlas_repo | https://github.com/Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| universe | atlas/universe/all_symbols.csv |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

Important interpretation:

```text
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward windows are bounded by manifest_max_date, not by current date
```

## 5. Historical Eligibility Gate

Eligibility rule applied:

```text
- entry_date is present in stock-web tradable shard.
- entry_date has high/low/close/volume fields.
- forward 180 trading days exists for quantitative calibration.
- corporate-action candidate dates do not overlap entry_date~D+180.
- rows without 180D forward window are narrative-only / label-comparison-only.
```

Symbol profile caveat summary:

| symbol | company | profile_path | corp_action_candidate_dates | 2025 180D status |
| --- | --- | --- | --- | --- |
| 000810 | 삼성화재 | atlas/symbol_profiles/000/000810.json | 1999-02-01, 1999-07-05, 2000-02-15 | clean for 2025 windows |
| 005830 | DB손해보험 | atlas/symbol_profiles/005/005830.json | 1999-07-20 | clean for 2025 windows |
| 001450 | 현대해상 | atlas/symbol_profiles/001/001450.json | 2004-07-13 | clean for 2025 windows |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | none | clean for 2025 windows |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | rule implication |
| --- | --- | --- |
| INSURANCE_PNC_RESERVE_QUALITY_CAPITAL_RETURN | C22_INSURANCE_RATE_CYCLE_RESERVE | positive route: reserve quality + capital return + revision evidence |
| INSURANCE_PNC_Q1_CONFIRMATION_CAPITAL_RETURN | C22_INSURANCE_RATE_CYCLE_RESERVE | positive route: Q1 confirmation after early false-start volatility |
| INSURANCE_PNC_RESERVE_QUALITY_GUARD | C22_INSURANCE_RATE_CYCLE_RESERVE | guard route: weak reserve quality should cap Stage label |
| INSURANCE_LIFE_RATE_BETA_WITHOUT_CAPITAL_CONFIRMATION | C22_INSURANCE_RATE_CYCLE_RESERVE | guard route: life-rate beta can be high-MFE but high-MAE; no Green without capital/CSM confirmation |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN | 000810 | 삼성화재 | structural_success | positive | T_R13L21_000810_STAGE2_20250214 | current_profile_correct |
| R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN | 005830 | DB손해보험 | missed_structural | positive | T_R13L21_005830_STAGE2_20250515 | current_profile_too_late |
| R13L21_C22_001450_2025_RESERVE_QUALITY_GUARD | 001450 | 현대해상 | high_mae_success | counterexample | T_R13L21_001450_STAGE2_20250214 | current_profile_false_positive |
| R13L21_C22_088350_2025_LIFE_RATE_BETA_WHIPSaw | 088350 | 한화생명 | high_mae_success | counterexample | T_R13L21_088350_STAGE2_20250213 | current_profile_too_early |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

Interpretation:

The pattern is not “insurance stocks went up.” The more useful split is:

```text
P&C reserve/capital-return confirmation -> strong MFE with manageable later MAE.
Generic insurance beta or weak reserve-quality evidence -> large whipsaw; should not be Green.
Life-insurer rate beta -> can produce huge eventual MFE but requires a separate high-MAE guard.
```

## 9. Evidence Source Map

This loop validates price-path alignment using stock-web OHLC. Fundamental evidence is kept as a research proxy category to be reconciled by the later implementation batch against DART/company IR timestamps.

| case | trigger_date | evidence category | stage2 fields | stage3 fields | red-team note |
| --- | --- | --- | --- | --- | --- |
| 삼성화재 | 2025-02-14 | FY2024/early-2025 insurance capital-return season; stronger P&C reserve-quality proxy | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality, early_revision_signal | financial_visibility, low_red_team_risk | early MAE existed, but later Green was not materially late |
| DB손해보험 | 2025-05-15 | post-Q1 confirmation / capital-return / reserve-quality route | public_event_or_disclosure, relative_strength, early_revision_signal | confirmed_revision, financial_visibility, low_red_team_risk | February trigger was noisy; May confirmation is cleaner |
| 현대해상 | 2025-02-14 | generic insurance value-up/rate beta without strong reserve-quality confirmation | public_event_or_disclosure, policy_or_regulatory_optionality | none | large MAE before later recovery: guard needed |
| 한화생명 | 2025-02-13 | life-insurer rate beta / low-PBR bounce without durable capital/CSM confirmation | relative_strength, policy_or_regulatory_optionality | none | eventual MFE was large, but early whipsaw makes Green promotion unsafe |

## 10. Price Data Source Map

| symbol | trigger rows used | tradable shard(s) |
| --- | --- | --- |
| 000810 | 2025-02-14 Stage2, 2025-05-30 Green, 2025-12-11 4B overlay | atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv; atlas/ohlcv_tradable_by_symbol_year/000/000810/2026.csv |
| 005830 | 2025-05-15 Stage2, 2025-06-12 Green label comparison | atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv; atlas/ohlcv_tradable_by_symbol_year/005/005830/2026.csv |
| 001450 | 2025-02-14 Stage2 guard test | atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv; atlas/ohlcv_tradable_by_symbol_year/001/001450/2026.csv |
| 088350 | 2025-02-13 Stage2 guard test | atlas/ohlcv_tradable_by_symbol_year/088/088350/2025.csv; atlas/ohlcv_tradable_by_symbol_year/088/088350/2026.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | usable | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_R13L21_000810_STAGE2_20250214 | 000810 | Stage2-Actionable | 2025-02-14 | 392000 | 18.88 | -16.58 | 34.18 | -16.58 | True | current_profile_correct |
| T_R13L21_000810_GREEN_20250530 | 000810 | Stage3-Green | 2025-05-30 | 404500 | 30.04 | -4.57 | 55.75 | -4.57 | True | current_profile_correct |
| T_R13L21_005830_STAGE2_20250515 | 005830 | Stage2-Actionable | 2025-05-15 | 97300 | 52.42 | -5.55 | 52.42 | -5.55 | True | current_profile_too_late |
| T_R13L21_001450_STAGE2_20250214 | 001450 | Stage2-Actionable | 2025-02-14 | 24400 | 11.68 | -18.69 | 25.82 | -18.69 | True | current_profile_false_positive |
| T_R13L21_088350_STAGE2_20250213 | 088350 | Stage2-Actionable | 2025-02-13 | 2700 | 27.04 | -12.22 | 61.3 | -12.22 | True | current_profile_too_early |
| T_R13L21_000810_4B_PRICE_20251211 | 000810 | Stage4B-overlay | 2025-12-11 | 630000 | 2.22 | -26.03 | None | None | False | current_profile_correct |
| T_R13L21_005830_GREEN_20250612 | 005830 | Stage3-Green | 2025-06-12 | 118800 | 24.83 | -6.99 | None | None | False | current_profile_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative calibration rows

| symbol | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak_date | peak_price | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000810 | 2025-02-14 | 392000 | 9.06/-10.2 | 18.88/-16.58 | 34.18/-16.58 | 2026-02-20 | 644000 | structural_success_with_high_early_mae |
| 005830 | 2025-05-15 | 97300 | 29.91/-5.55 | 52.42/-5.55 | 52.42/-5.55 | 2026-02-20 | 205500 | missed_structural_positive |
| 001450 | 2025-02-14 | 24400 | 4.1/-10.04 | 11.68/-18.69 | 25.82/-18.69 | 2026-02-20 | 40550 | counterexample_high_mae_before_recovery |
| 088350 | 2025-02-13 | 2700 | 5.37/-6.3 | 27.04/-12.22 | 61.3/-12.22 | 2026-02-20 | 6600 | high_mae_success_but_not_green_quality |

### 12.2 Label-comparison / overlay rows

| trigger_id | symbol | role | entry_date | entry_price | observed MFE90/MAE90 | block reason |
| --- | --- | --- | --- | --- | --- | --- |
| T_R13L21_000810_4B_PRICE_20251211 | 000810 | 4B_overlay_only | 2025-12-11 | 630000 | 2.22/-26.03 | insufficient_forward_window_in_stock_web |
| T_R13L21_005830_GREEN_20250612 | 005830 | label_comparison_only | 2025-06-12 | 118800 | 24.83/-6.99 | insufficient_forward_window_in_stock_web |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | stress verdict |
| --- | --- | --- | --- |
| 삼성화재 | Stage2/Yellow is acceptable; Green after confirmation is not late | MFE180 +34.18% from Stage2, +55.75% from later Green; high early MAE but strong long-window MFE | current_profile_correct |
| DB손해보험 | May confirmation can be missed if C22 has no reserve/capital-return bonus | MFE90 +52.42%, MAE90 -5.55% from May trigger | current_profile_too_late |
| 현대해상 | generic Stage2 bonus may over-promote if reserve-quality guard absent | MFE90 +11.68%, but MAE90 -18.69%; later recovery came after a deep drawdown | current_profile_false_positive |
| 한화생명 | life-rate beta can look attractive too early | MFE180 +61.30%, but MAE90 -12.22%; high whipsaw requires guard before Green | current_profile_too_early |

Answers to required stress-test questions:

```text
1. current profile judgement:
   - Correct on 삼성화재; too late on DB손보; too early/false-positive-prone on 현대해상 and 한화생명.

2. MFE/MAE alignment:
   - Positive cases show better MFE/MAE after reserve/capital confirmation.
   - Counterexamples show that rate beta alone causes high MAE before eventual recovery.

3. Stage2 bonus:
   - useful, but too broad for C22 if not conditioned on reserve/capital quality.

4. Yellow threshold 75:
   - acceptable as an intermediate label, but C22 needs a guard separating P&C confirmation from generic beta.

5. Green threshold 87 / revision 55:
   - keep strict; do not relax globally. C22 positive route can add a small reserve/capital bonus, not lower Green threshold.

6. price-only blowoff guard:
   - strengthened by the 000810 2025-12-11 4B overlay; price-only blowoff should not become full 4B without non-price evidence.

7. full 4B non-price requirement:
   - appropriate and strengthened.

8. hard 4C routing:
   - no hard 4C was calibrated here; thesis-break watch labels only.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/label entry | peak basis | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- | --- |
| 삼성화재 | 392000 on 2025-02-14 | 404500 on 2025-05-30 | 644000 observed peak | 0.05 | Green not meaningfully late |
| DB손해보험 | 97300 on 2025-05-15 | 118800 on 2025-06-12 label-only | 148300 180D peak for Stage2 | 0.42 | Green somewhat late; May Stage2 carries the usable signal |
| 현대해상 | 24400 on 2025-02-14 | none | 40550 observed peak | not_applicable | No confirmed Green; generic beta should stay capped |
| 한화생명 | 2700 on 2025-02-13 | none | 6600 observed peak | not_applicable | Life-rate beta should not Green without capital/CSM confirmation |

## 15. 4B Local vs Full-window Timing Audit

4B stress row:

```text
case = 삼성화재
trigger_id = T_R13L21_000810_4B_PRICE_20251211
entry_price = 630000
local_peak_proxy = 630000
full_observed_peak = 644000
four_b_local_peak_proximity = 1.00
four_b_full_window_peak_proximity = 0.94
four_b_evidence_type = price_only | valuation_blowoff
four_b_timing_verdict = price_only_local_4B_not_full_4B_without_non_price_evidence
calibration_usable = false
block_reason = insufficient_forward_window_in_stock_web
```

Interpretation:

The row strengthens the existing rule rather than proposing a new sell rule. In C22, price-only exhaustion can mark risk, but full 4B should still require non-price evidence such as reserve deterioration, capital overhang, explicit regulatory cap, or revision slowdown.

## 16. 4C Protection Audit

No hard 4C calibration row is promoted in this loop.

```text
four_c_protection_label for 현대해상 = thesis_break_watch_only
four_c_protection_label for 한화생명 = thesis_break_watch_only
hard_4c_success_count = 0
hard_4c_late_count = 0
```

The C22 residual issue here is not hard 4C timing. It is positive-stage precision.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
axis = insurance_reserve_quality_capital_return_gate
proposal_type = sector_shadow_only
```

Candidate rule:

```text
Within L6 insurance cases, generic rate/PBR/value-up evidence may create Stage2-Watch or Stage2-Actionable,
but Stage3-Yellow/Green promotion needs at least one of:

1. P&C reserve-quality confirmation,
2. explicit capital-return path that is not just policy beta,
3. confirmed revision / financial visibility after the initial insurance-beta move,
4. low red-team risk around K-ICS/capital/reserve volatility.
```

Backtest effect from representative rows:

```text
P&C positives:
  avg_MFE_90D = 35.65%
  avg_MAE_90D = -11.06%

guard/counterexample rows:
  avg_MFE_90D = 19.36%
  avg_MAE_90D = -15.46%
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
axis_1 = c22_pnc_reserve_quality_capital_return_bonus
axis_2 = c22_life_rate_beta_whipsaw_guard
proposal_type = archetype_shadow_only
```

Candidate compression:

```text
C22 is not one homogeneous insurance bucket.

C22-A: P&C reserve/capital-return route
  - may add +3 to +5 research proxy score after confirmation.
  - can move Stage2-Actionable into Yellow if revision/capital-return evidence is present.

C22-B: generic insurance beta route
  - cap at Stage2-Watch / Stage2-Actionable.
  - do not Green from price, rate beta, or low-PBR thesis alone.

C22-C: life-insurer rate-beta route
  - allow watchlist/Stage2, but require CSM/capital/solvency confirmation for Yellow/Green.
  - apply high-MAE guard because MFE can be large but path is unstable.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_trigger_count | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | avg_green_lateness_ratio | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | current global calibrated proxy | no C22-specific split; generic Stage2 bonus can still over-score insurance beta | none | 4 | 27.5 | -13.26 | 43.43 | -13.26 | 0.50 | 1 | 1 | 0.24 | mixed; high-MAE cases need archetype guard |
| P0b | E2R 2.0 baseline reference | older thresholding: weaker Stage2/actionable separation; more late entries | rollback reference only | 4 | 23.1 | -14.4 | 38.7 | -14.4 | 0.50 | 2 | 2 | 0.44 | inferior; not promoted |
| P1 | sector_specific_candidate_profile | financial-sector insurance shadow: reward reserve/capital-return confirmation, cap generic beta | reserve_quality_capital_return_gate + life_beta_guard | 4 | 35.65 | -11.06 | 43.3 | -11.07 | 0.00 | 0 | 1 | 0.24 | better precision for L6 insurance |
| P2 | canonical_archetype_candidate_profile | C22-specific compression: P&C positive route vs life-rate-beta guard | C22 subtype compression | 4 | 35.65 | -11.06 | 43.3 | -11.07 | 0.00 | 0 | 1 | 0.24 | best research-proxy alignment |
| P3 | counterexample_guard_profile | guard profile that demotes weak reserve-quality and life-rate beta until CSM/capital confirmation | counterexample guard | 4 | 19.36 | -15.46 | 43.56 | -15.46 | 0.00 by exclusion | 1 | 0 | None | good guard; not a positive promotion profile |

## 20. Score-Return Alignment Matrix

| symbol | before score/label | after score/label | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 000810 | 78.0/Stage3-Yellow | 84.0/Stage3-Yellow | 18.88 | -16.58 | aligned_positive |
| 005830 | 72.0/Stage2-Actionable | 81.0/Stage3-Yellow | 52.42 | -5.55 | aligned_positive |
| 001450 | 75.5/Stage3-Yellow | 66.0/Stage2-Watch | 11.68 | -18.69 | guard_needed_high_mae_or_false_positive |
| 088350 | 74.0/Stage2-Actionable | 67.0/Stage2-Watch | 27.04 | -12.22 | guard_needed_high_mae_or_false_positive |

Mechanism:

C22 behaves like a lock with two keys. The first key is macro/rate/value-up beta; it can open the outer door to Stage2. The second key is reserve/capital/revision confirmation; without it, Green is like walking into a room before the lights are on. The price can still run, but the path has hidden stairs.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_RESERVE_QUALITY_CAPITAL_RETURN_HOLDOUT_2025 | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 3 | True | True | Need official DART/IR timestamp reconciliation and 2026 refresh once forward windows mature |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 2

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - generic_insurance_beta_false_positive
  - P&C_reserve_quality_missed_structural
  - life_rate_beta_high_mae_success
  - price_only_4B_partial_window_not_full_4B

new_axis_proposed:
  - c22_pnc_reserve_quality_capital_return_bonus
  - c22_life_rate_beta_whipsaw_guard

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

existing_axis_weakened:
  - null

existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest and max_date.
- Stock-web tradable OHLC rows for 000810, 005830, 001450, 088350.
- entry_date and entry_price from c column.
- MFE/MAE using high/low windows.
- Corporate-action candidate dates did not overlap 2025 180D calibration windows.
- 4B local vs full-window proximity split for one overlay row.
```

Not validated:

```text
- No live candidate scan.
- No 2026 investment recommendation.
- No broker API.
- No stock_agent src/e2r code.
- No production scoring patch.
- Fundamental evidence timestamps are research-proxy categories and must be reconciled to DART/company IR in implementation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_pnc_reserve_quality_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+4,+4,"P&C reserve/capital-return confirmation separated positives from generic insurance beta","improved precision: positives avg MFE90 35.65% vs guard rows avg MAE90 -15.46%","T_R13L21_000810_STAGE2_20250214|T_R13L21_005830_STAGE2_20250515",2,2,0,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_life_rate_beta_whipsaw_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-5,-5,"Life-rate beta and low-PBR bounce showed large eventual MFE but high early MAE; no Green without capital/CSM confirmation","reduces false Green risk in high-MAE cases","T_R13L21_088350_STAGE2_20250213",1,1,1,low,archetype_shadow_only,"not production; needs more life-insurer holdout cases"
shadow_weight,c22_weak_reserve_quality_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-4,-4,"Generic insurance beta without reserve-quality confirmation can create false positive / high-MAE path","demotes 현대해상-like weak reserve-quality trigger below Green","T_R13L21_001450_STAGE2_20250214",1,1,1,medium,sector_shadow_only,"not production; C22 guard candidate"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_RESERVE_QUALITY_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R13L21_000810_STAGE2_20250214", "current_profile_verdict": "current_profile_correct", "score_price_alignment": "good: Stage2/Yellow evidence captured before large 180D/1Y MFE, and Green was not materially late.", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web", "notes": "Non-life insurer with cleaner reserve/capital-return proxy; 2025 trigger family distinct from prior 2024 value-up shock."}
{"row_type": "case", "case_id": "R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_Q1_CONFIRMATION_CAPITAL_RETURN", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "T_R13L21_005830_STAGE2_20250515", "current_profile_verdict": "current_profile_too_late", "score_price_alignment": "good after Q1/capital-return confirmation; pre-Q1 February evidence had high MAE and should not be promoted too early.", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web", "notes": "Stage2 should prefer reserve/capital quality confirmation over generic insurance value-up beta."}
{"row_type": "case", "case_id": "R13L21_C22_001450_2025_RESERVE_QUALITY_GUARD", "symbol": "001450", "company_name": "현대해상", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_RESERVE_QUALITY_GUARD", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "T_R13L21_001450_STAGE2_20250214", "current_profile_verdict": "current_profile_false_positive", "score_price_alignment": "mixed: 180D MFE existed but only after severe MAE; weak reserve-quality evidence should prevent Green promotion.", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web", "notes": "Counterexample to generic PBR/insurance beta promotion."}
{"row_type": "case", "case_id": "R13L21_C22_088350_2025_LIFE_RATE_BETA_WHIPSaw", "symbol": "088350", "company_name": "한화생명", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_LIFE_RATE_BETA_WITHOUT_CAPITAL_CONFIRMATION", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "T_R13L21_088350_STAGE2_20250213", "current_profile_verdict": "current_profile_too_early", "score_price_alignment": "mixed: large eventual MFE, but early trigger had material whipsaw; life-insurer rate beta needs a guard before Green.", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web", "notes": "Counterexample guard: rate beta and low-PBR bounce are not enough for positive Green without CSM/capital confirmation."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "T_R13L21_000810_STAGE2_20250214", "case_id": "R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-14", "entry_date": "2025-02-14", "entry_price": 392000, "evidence_available_at_that_date": "FY2024/early-2025 insurance value-up and capital-return season; P&C reserve-quality proxy stronger than peer group.", "evidence_source": "research proxy from historical disclosure/IR/report season; price validated from stock-web rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.06, "MFE_90D_pct": 18.88, "MFE_180D_pct": 34.18, "MFE_1Y_pct": 64.29, "MFE_2Y_pct": null, "MAE_30D_pct": -10.2, "MAE_90D_pct": -16.58, "MAE_180D_pct": -16.58, "MAE_1Y_pct": -16.58, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 644000, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.05, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_high_early_mae", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R13L21_000810_20250214_392000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R13L21_000810_GREEN_20250530", "case_id": "R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "green_strictness_stress_test|holdout_validation", "trigger_type": "Stage3-Green", "trigger_date": "2025-05-30", "entry_date": "2025-05-30", "entry_price": 404500, "evidence_available_at_that_date": "Post-Q1 confirmation window; relative-strength and capital-return thesis had survived first whipsaw.", "evidence_source": "research proxy from Q1/FY disclosure season; price validated from stock-web rows.", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.2, "MFE_90D_pct": 30.04, "MFE_180D_pct": 55.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.57, "MAE_90D_pct": -4.57, "MAE_180D_pct": -4.57, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 644000, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.05, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_not_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R13L21_000810_20250530_404500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R13L21_005830_STAGE2_20250515", "case_id": "R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_Q1_CONFIRMATION_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "residual_missed_structural_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-15", "entry_date": "2025-05-15", "entry_price": 97300, "evidence_available_at_that_date": "Q1 confirmation / reserve-quality / shareholder-return window after February false-start risk was absorbed.", "evidence_source": "research proxy from Q1/FY disclosure season; price validated from stock-web rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.91, "MFE_90D_pct": 52.42, "MFE_180D_pct": 52.42, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.55, "MAE_90D_pct": -5.55, "MAE_180D_pct": -5.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 205500, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "missed_structural_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R13L21_005830_20250515_97300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R13L21_001450_STAGE2_20250214", "case_id": "R13L21_C22_001450_2025_RESERVE_QUALITY_GUARD", "symbol": "001450", "company_name": "현대해상", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_RESERVE_QUALITY_GUARD", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "residual_false_positive_mining|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-14", "entry_date": "2025-02-14", "entry_price": 24400, "evidence_available_at_that_date": "Generic insurance value-up/rate-beta season, but reserve-quality confirmation was not strong enough.", "evidence_source": "research proxy from FY/Q1 disclosure season; price validated from stock-web rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.1, "MFE_90D_pct": 11.68, "MFE_180D_pct": 25.82, "MFE_1Y_pct": 66.19, "MFE_2Y_pct": null, "MAE_30D_pct": -10.04, "MAE_90D_pct": -18.69, "MAE_180D_pct": -18.69, "MAE_1Y_pct": -18.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 40550, "drawdown_after_peak_pct": null, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample_high_mae_before_recovery", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R13L21_001450_20250214_24400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R13L21_088350_STAGE2_20250213", "case_id": "R13L21_C22_088350_2025_LIFE_RATE_BETA_WHIPSaw", "symbol": "088350", "company_name": "한화생명", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_LIFE_RATE_BETA_WITHOUT_CAPITAL_CONFIRMATION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "counterexample_mining|yellow_threshold_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-13", "entry_date": "2025-02-13", "entry_price": 2700, "evidence_available_at_that_date": "Life-insurer rate beta / low-PBR bounce; durable capital-return and CSM confirmation still weaker than P&C positives.", "evidence_source": "research proxy from FY/Q1 disclosure season; price validated from stock-web rows.", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2025.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.37, "MFE_90D_pct": 27.04, "MFE_180D_pct": 61.3, "MFE_1Y_pct": 144.44, "MFE_2Y_pct": null, "MAE_30D_pct": -6.3, "MAE_90D_pct": -12.22, "MAE_180D_pct": -12.22, "MAE_1Y_pct": -12.22, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 6600, "drawdown_after_peak_pct": null, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success_but_not_green_quality", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R13L21_088350_20250213_2700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R13L21_000810_4B_PRICE_20251211", "case_id": "R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2025-12-11", "entry_date": "2025-12-11", "entry_price": 630000, "evidence_available_at_that_date": "Price-only blowoff/local spike; no separately confirmed non-price 4B thesis break in this run.", "evidence_source": "stock-web OHLC only; narrative-only 4B stress row.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 2.22, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -26.03, "MAE_90D_pct": -26.03, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 644000, "drawdown_after_peak_pct": null, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "price_only_local_4B_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success_but_forward_window_incomplete", "current_profile_verdict": "current_profile_correct", "calibration_usable": false, "forward_window_trading_days": 47, "calibration_block_reasons": ["insufficient_forward_window_in_stock_web"], "corporate_action_window_status": "clean_observed_partial_window", "same_entry_group_id": "SEG_R13L21_000810_20251211_630000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case 4B overlay partial-window stress row", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R13L21_005830_GREEN_20250612", "case_id": "R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_PNC_Q1_CONFIRMATION_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 rate/reserve/capital-return rerating", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2025-06-12", "entry_date": "2025-06-12", "entry_price": 118800, "evidence_available_at_that_date": "Later confirmation after the May Stage2 entry; insufficient stock-web forward 180D for strict quantitative weight calibration.", "evidence_source": "research proxy from disclosure/IR season; price validated from stock-web rows.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.83, "MFE_90D_pct": 24.83, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.99, "MAE_90D_pct": -6.99, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 205500, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison_only_forward_window_incomplete", "current_profile_verdict": "current_profile_too_late", "calibration_usable": false, "forward_window_trading_days": 171, "calibration_block_reasons": ["insufficient_forward_window_in_stock_web"], "corporate_action_window_status": "clean_observed_partial_window", "same_entry_group_id": "SEG_R13L21_005830_20250612_118800", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case label comparison; forward 180D incomplete", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN", "trigger_id": "T_R13L21_000810_STAGE2_20250214", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 48, "relative_strength_score": 16, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 52, "relative_strength_score": 17, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["c22_reserve_quality_capital_return_bonus"], "component_delta_explanation": "Proposed C22 shadow profile separates P&C reserve/capital-return confirmation from generic insurance rate beta. It boosts clean P&C evidence and caps weak reserve/life-rate-beta cases below Green.", "MFE_90D_pct": 18.88, "MAE_90D_pct": -16.58, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN", "trigger_id": "T_R13L21_005830_STAGE2_20250515", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 43, "relative_strength_score": 15, "customer_quality_score": 3, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 50, "relative_strength_score": 18, "customer_quality_score": 3, "policy_or_regulatory_score": 8, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["c22_reserve_quality_capital_return_bonus"], "component_delta_explanation": "Proposed C22 shadow profile separates P&C reserve/capital-return confirmation from generic insurance rate beta. It boosts clean P&C evidence and caps weak reserve/life-rate-beta cases below Green.", "MFE_90D_pct": 52.42, "MAE_90D_pct": -5.55, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L21_C22_001450_2025_RESERVE_QUALITY_GUARD", "trigger_id": "T_R13L21_001450_STAGE2_20250214", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 24, "relative_strength_score": 6, "customer_quality_score": 2, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 18, "relative_strength_score": 6, "customer_quality_score": 2, "policy_or_regulatory_score": 7, "valuation_repricing_score": 3, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66.0, "stage_label_after": "Stage2-Watch", "changed_components": ["c22_reserve_quality_capital_return_gate", "c22_life_rate_beta_whipsaw_guard"], "component_delta_explanation": "Proposed C22 shadow profile separates P&C reserve/capital-return confirmation from generic insurance rate beta. It boosts clean P&C evidence and caps weak reserve/life-rate-beta cases below Green.", "MFE_90D_pct": 11.68, "MAE_90D_pct": -18.69, "score_return_alignment_label": "guard_needed_high_mae_or_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L21_C22_088350_2025_LIFE_RATE_BETA_WHIPSaw", "trigger_id": "T_R13L21_088350_STAGE2_20250213", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 22, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 18, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 19, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67.0, "stage_label_after": "Stage2-Watch", "changed_components": ["c22_reserve_quality_capital_return_gate", "c22_life_rate_beta_whipsaw_guard"], "component_delta_explanation": "Proposed C22 shadow profile separates P&C reserve/capital-return confirmation from generic insurance rate beta. It boosts clean P&C evidence and caps weak reserve/life-rate-beta cases below Green.", "MFE_90D_pct": 27.04, "MAE_90D_pct": -12.22, "score_return_alignment_label": "guard_needed_high_mae_or_false_positive", "current_profile_verdict": "current_profile_too_early"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_pnc_reserve_quality_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+4,+4,"P&C reserve/capital-return confirmation separated positives from generic insurance beta","positives avg MFE90 35.65% and cleaner path","T_R13L21_000810_STAGE2_20250214|T_R13L21_005830_STAGE2_20250515",2,2,0,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_life_rate_beta_whipsaw_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-5,-5,"Life-rate beta high-MFE but high-MAE; no Green without capital/CSM confirmation","reduces false Green risk","T_R13L21_088350_STAGE2_20250213",1,1,1,low,archetype_shadow_only,"needs more life-insurer holdout cases"
shadow_weight,c22_weak_reserve_quality_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-4,-4,"Generic insurance beta without reserve-quality confirmation","demotes high-MAE false-positive path","T_R13L21_001450_STAGE2_20250214",1,1,1,medium,sector_shadow_only,"not production"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "21", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 0, "new_trigger_family_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["generic_insurance_beta_false_positive", "life_rate_beta_high_mae_success", "P&C_reserve_quality_missed_structural"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "reason": "4B_price_only_overlay_has_insufficient_forward_180D_window_and_no_non_price_thesis_break", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
{"row_type": "narrative_only", "case_id": "R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "reason": "Stage3_Green_label_comparison_forward_180D_unavailable_by_manifest_max_date", "price_source": "Songdaiki/stock-web", "usage": "label_comparison_not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R13_loop_22_L6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_bank_capital_return_holdout
carry_forward_questions:
  - Does C21 bank/financial-holding capital-return evidence have the same reserve-quality split, or is it cleaner than C22 insurance?
  - Should life-insurer rate-beta guard be expanded only after additional holdout cases?
  - Should C22 4B use explicit reserve/capital deterioration, not price exhaustion, as the full 4B route?
```

## 28. Source Notes

```text
stock-web:
  manifest = atlas/manifest.json
  symbol profiles:
    atlas/symbol_profiles/000/000810.json
    atlas/symbol_profiles/005/005830.json
    atlas/symbol_profiles/001/001450.json
    atlas/symbol_profiles/088/088350.json
  tradable OHLC shards:
    atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv
    atlas/ohlcv_tradable_by_symbol_year/000/000810/2026.csv
    atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv
    atlas/ohlcv_tradable_by_symbol_year/005/005830/2026.csv
    atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv
    atlas/ohlcv_tradable_by_symbol_year/001/001450/2026.csv
    atlas/ohlcv_tradable_by_symbol_year/088/088350/2025.csv
    atlas/ohlcv_tradable_by_symbol_year/088/088350/2026.csv

stock_agent research artifact checked:
  reports/e2r_calibration/ingest_summary.md
  reports/e2r_calibration/applied_scoring_diff.md

Important caveat:
  Fundamental evidence fields in this file are research-proxy categories. The OHLC backtest is stock-web validated; later implementation should reconcile exact DART/company IR timestamps before promotion.
```
