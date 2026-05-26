# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 11
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS
loop_objective = residual_missed_structural_mining | counterexample_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R6_loop_11_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop follows the v12 rule that historical calibration research must not become live candidate discovery. The selected cases are historical insurer rerating and failed-event-premium paths. The purpose is to separate the broad financial value-up / ROE-PBR capital-return signal from the more specific insurance reserve-cycle signal.

The working hypothesis is simple:

```text
C21 financial capital-return evidence is not enough for insurers.
For C22, the evidence stack must show:
1. sustainable IFRS17 earnings or CSM quality,
2. K-ICS / solvency headroom,
3. loss-ratio or reserve-risk stability,
4. capital-return or payout visibility,
5. low event-premium contamination.
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

No production scoring change is proposed here. The proposed changes are shadow-only and scoped to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL / C22_INSURANCE_RATE_CYCLE_RESERVE`.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R6 |
| loop | 11 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE |
| fine_archetype_id | KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS |
| sector | Korean non-life insurance |
| primary_archetype | insurance_rate_cycle_reserve_kics_capital_return |

This loop is intentionally adjacent to but not identical with the previous `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` loop. In bank / holding-company value-up cases, ROE/PBR and shareholder return may be sufficient early evidence. In insurance, the same headline can be a mirage if reserve strengthening, auto-loss ratio, K-ICS pressure, or event-premium contamination dominates.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were checked at the summary level only:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
reports/e2r_calibration/calibrated_profile_report.md
```

Key prior coverage summary:

```text
discovered_md_count = 398
discovered_result_md_count = 107
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
loops_covered = 1~9
price_source_usable_rows = 146
large existing global axes already applied:
  stage2_actionable_evidence_bonus
  stage3_yellow_total_min
  stage3_green_total_min
  stage3_green_revision_min
  stage3_cross_evidence_green_buffer
  full_4b_requires_non_price_evidence
  hard_4c_thesis_break_routes_to_4c
```

Duplicate-avoidance interpretation:

```text
- This loop does not re-prove general Stage2 earlyness.
- This loop does not re-prove general Green lateness.
- This loop does not re-prove generic price-only 4B blocking.
- This loop narrows the already-known financial value-up evidence into a C22 insurer-specific residual gate.
```

Case novelty:

| case_id | symbol | company | new independent? | reason |
|---|---:|---|---:|---|
| R6L11_C22_000810 | 000810 | Samsung Fire & Marine | true | insurer-specific reserve/K-ICS/capital-return positive |
| R6L11_C22_005830 | 005830 | DB Insurance | true | insurer-specific reserve/K-ICS/capital-return positive |
| R6L11_C22_001450 | 001450 | Hyundai Marine & Fire | true | C22 counterexample: weaker reserve/loss-ratio quality than price reaction implied |
| R6L11_C22_000400 | 000400 | Lotte Non-Life Insurance | true | C22 false-positive: event/control-premium path not reserve-cycle rerating |

```text
new_independent_case_ratio = 4 / 4 = 1.00
required_new_independent_case_ratio = 0.60
novelty_status = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web atlas input was validated before case work.

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
price_basis = tradable_raw
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
corporate_action_blocking = enabled
```

Price source status:

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative calibration triggers in this loop satisfy the minimum v12 gate:

```text
- trigger_date is historical.
- entry_date exists in stock-web tradable shard.
- entry_date has positive OHLCV.
- at least 180 forward trading days exist before manifest max_date.
- MFE/MAE 30D, 90D, 180D computed from stock-web rows.
- 180D windows are not contaminated by detected corporate-action candidate dates.
```

| symbol | profile_path | last_date | corporate_action_candidate_dates relevant to 2024 window? | 180D status |
|---:|---|---|---|---|
| 000810 | atlas/symbol_profiles/000/000810.json | 2026-02-20 | none after 2000-02-15 | clean_180D_window |
| 005830 | atlas/symbol_profiles/005/005830.json | 2026-02-20 | none after 1999-07-20 | clean_180D_window |
| 001450 | atlas/symbol_profiles/001/001450.json | 2026-02-20 | none after 2004-07-13 | clean_180D_window |
| 000400 | atlas/symbol_profiles/000/000400.json | 2026-02-20 | none after 2019-10-25 | clean_180D_window |

Notes:

```text
MFE_2Y_pct = null for early-2024 triggers because 504 forward trading days are not fully available by stock_web_manifest_max_date.
MFE_1Y_pct is included where estimated from available 252D window; it is not used for the proposed shadow weight.
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | mapping reason |
|---|---|---|
| KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS | C22_INSURANCE_RATE_CYCLE_RESERVE | insurer earnings quality depends on IFRS17/CSM, K-ICS, reserve risk, loss ratio, and capital return |
| INSURANCE_VALUEUP_PAYOUT_WITH_KICS_HEADROOM | C22_INSURANCE_RATE_CYCLE_RESERVE | value-up is accepted only when solvency and reserve quality support payout |
| INSURANCE_CONTROL_PREMIUM_EVENT_FALSE_POSITIVE | C22_INSURANCE_RATE_CYCLE_RESERVE | event premium can move price but should not train positive C22 entry weights |

Compression rule:

```text
C22 should not inherit all C21 financial-capital-return promotion power.
C22 needs insurer-specific reserve/capital adequacy gates before Stage3-Green promotion.
```

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | best_trigger | calibration_usable |
|---|---:|---|---|---|---|---:|
| R6L11_C22_000810 | 000810 | Samsung Fire & Marine | structural_success | positive | T1_STAGE2_ACTIONABLE_20240216 | true |
| R6L11_C22_005830 | 005830 | DB Insurance | structural_success | positive | T1_STAGE2_ACTIONABLE_20240216 | true |
| R6L11_C22_001450 | 001450 | Hyundai Marine & Fire | failed_rerating | counterexample | T1_STAGE2_OR_YELLOW_STRESS_20240216 | true |
| R6L11_C22_000400 | 000400 | Lotte Non-Life Insurance | false_positive_green / 4C_success | counterexample | T1_EVENT_PREMIUM_20240213 | true |

Selection balance:

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

## 8. Positive vs Counterexample Balance

Positive cases share this evidence pattern:

```text
- insurer earnings or IFRS17 profitability already visible,
- capital adequacy / K-ICS headroom not obviously impaired,
- payout or capital-return expectation has accounting support,
- stock price rerates without requiring a control-premium event,
- MAE is tolerable relative to 90D/180D MFE.
```

Counterexamples share this warning pattern:

```text
- generic value-up or event-premium headline appears,
- insurer-specific reserve quality / K-ICS / loss-ratio evidence is weaker,
- price response is not matched by durable revision quality,
- later MAE and drawdown overwhelm the early MFE.
```

## 9. Evidence Source Map

This loop uses historical evidence labels as research proxy evidence, not live research output.

| evidence_id | symbol | evidence_available_at_that_date | evidence family | v12 role |
|---|---:|---|---|---|
| EV_C22_000810_20240216_IFRS17_CAPITAL | 000810 | FY2023/early-2024 insurer earnings, capital-return, K-ICS solvency discussion available by the trigger window | financial_actual / research_report / capital_return | Stage2 / Stage3 support |
| EV_C22_005830_20240216_IFRS17_CAPITAL | 005830 | FY2023/early-2024 non-life earnings, payout, solvency, ROE/PBR rerating evidence available by the trigger window | financial_actual / research_report / capital_return | Stage2 / Stage3 support |
| EV_C22_001450_20240216_RESERVE_RISK | 001450 | sector value-up evidence existed, but reserve/loss-ratio risk and weaker relative path limited rerating quality | financial_actual / reserve_risk / relative_strength | counterexample |
| EV_C22_000400_20240213_EVENT_PREMIUM | 000400 | acquisition/control-premium event was visible, but reserve-cycle and payout-quality evidence were not sufficient | event_premium / control_premium / weak_reserve_visibility | false positive / 4B / 4C |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | entry rows checked |
|---:|---|---|---|---|
| 000810 | Samsung Fire & Marine | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json | 2024-02-16 close 304000 |
| 005830 | DB Insurance | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json | 2024-02-16 close 100000 |
| 001450 | Hyundai Marine & Fire | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/symbol_profiles/001/001450.json | 2024-02-16 close 34450 |
| 000400 | Lotte Non-Life Insurance | atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv | atlas/symbol_profiles/000/000400.json | 2024-02-13 close 3370 |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_id | trigger_type | trigger_date | entry_date | entry_price | role | current_profile_verdict |
|---|---|---|---|---|---:|---|---|
| R6L11_C22_000810 | R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216 | Stage2-Actionable | 2024-02-16 | 2024-02-16 | 304000 | representative | current_profile_correct |
| R6L11_C22_000810 | R6L11_C22_000810_T2_STAGE3_GREEN_20240516 | Stage3-Green | 2024-05-16 | 2024-05-16 | 370000 | label_comparison_only | current_profile_too_late |
| R6L11_C22_005830 | R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216 | Stage2-Actionable | 2024-02-16 | 2024-02-16 | 100000 | representative | current_profile_correct |
| R6L11_C22_005830 | R6L11_C22_005830_T2_STAGE3_GREEN_20240516 | Stage3-Green | 2024-05-16 | 2024-05-16 | 111500 | label_comparison_only | current_profile_correct |
| R6L11_C22_001450 | R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216 | Stage2-or-Yellow stress | 2024-02-16 | 2024-02-16 | 34450 | representative | current_profile_false_positive |
| R6L11_C22_000400 | R6L11_C22_000400_T1_EVENT_PREMIUM_20240213 | Stage2 false positive stress | 2024-02-13 | 2024-02-13 | 3370 | representative | current_profile_false_positive |
| R6L11_C22_000400 | R6L11_C22_000400_T2_4B_EVENT_PREMIUM_20240423 | 4B event-premium overlay | 2024-04-23 | 2024-04-23 | 3850 | 4B_overlay_only | current_profile_correct |
| R6L11_C22_000400 | R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628 | 4C thesis-break protection | 2024-06-28 | 2024-06-28 | 2915 | 4C_overlay_only | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216 | 304000 | 13.82 | -6.09 | 29.44 | -10.36 | 29.44 | -10.36 | 2024-06-28 | 393500 | -30.75 |
| R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216 | 100000 | 10.00 | -8.50 | 15.40 | -13.50 | 20.70 | -13.50 | 2024-07-02 | 120700 | -15.82 |
| R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216 | 34450 | 4.06 | -11.90 | 4.06 | -17.42 | 6.68 | -17.42 | 2024-07-31 | 36750 | -17.28 |
| R6L11_C22_000400_T1_EVENT_PREMIUM_20240213 | 3370 | 8.90 | -19.88 | 19.73 | -19.88 | 20.92 | -25.67 | 2024-06-21 | 4075 | -38.53 |

### Label comparison / overlay metrics

| trigger_id | trigger_type | entry_price | MFE_90D_pct | MAE_90D_pct | outcome use |
|---|---|---:|---:|---:|---|
| R6L11_C22_000810_T2_STAGE3_GREEN_20240516 | Stage3-Green | 370000 | 6.35 | -11.08 | Green lateness comparison only |
| R6L11_C22_005830_T2_STAGE3_GREEN_20240516 | Stage3-Green | 111500 | 8.25 | -7.26 | Green lateness comparison only |
| R6L11_C22_000400_T2_4B_EVENT_PREMIUM_20240423 | 4B overlay | 3850 | 5.84 | -34.94 | overlay/risk only |
| R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628 | 4C overlay | 2915 | 1.20 | -14.07 | thesis-break/protection only |

## 13. Current Calibrated Profile Stress Test

### 000810 Samsung Fire & Marine

```text
current calibrated profile expected behavior:
  Stage2-Actionable accepted on early non-price evidence.
  Stage3-Green delayed until confirmed revision / multiple-source evidence.
actual result:
  Stage2 timing was useful: 90D/180D MFE +29.44%, MAE -10.36%.
  Full Green in May was valid but somewhat late versus the first usable entry.
verdict = current_profile_correct
```

Axis answers:

```text
stage2_actionable_evidence_bonus: appropriate
Yellow threshold 75: appropriate
Green 87 / revision 55: slightly late but not false
price-only blowoff guard: not central
full 4B non-price requirement: appropriate
hard 4C routing: not triggered
```

### 005830 DB Insurance

```text
current calibrated profile expected behavior:
  Stage2-Actionable accepted, later Green/4A only with confirmed insurer earnings and payout support.
actual result:
  Stage2 had +20.70% 180D MFE with -13.50% MAE.
  Green comparison entry still had positive but less asymmetric path.
verdict = current_profile_correct
```

Axis answers:

```text
stage2_actionable_evidence_bonus: appropriate
Yellow threshold 75: appropriate
Green 87 / revision 55: appropriate
price-only blowoff guard: not central
full 4B non-price requirement: appropriate
hard 4C routing: not triggered
```

### 001450 Hyundai Marine & Fire

```text
current calibrated profile expected behavior:
  Generic C21 value-up profile could push it into Stage2/Yellow.
actual result:
  180D MFE only +6.68%, while MAE reached -17.42%.
  The sector headline did not translate into a clean C22 rerating path.
verdict = current_profile_false_positive
```

Axis answers:

```text
stage2_actionable_evidence_bonus: too generous if applied without insurer-specific reserve/K-ICS quality
Yellow threshold 75: can be too loose for C22 if reserve risk is unresolved
Green 87 / revision 55: appropriate; should block Green
price-only blowoff guard: not central
full 4B non-price requirement: appropriate
hard 4C routing: not triggered
```

### 000400 Lotte Non-Life Insurance

```text
current calibrated profile expected behavior:
  Event/control-premium price action may appear as Stage2 if not separated.
actual result:
  90D MFE +19.73% existed, but MAE and subsequent drawdown were severe.
  This was not a reserve-cycle rerating; it was an event premium that needed overlay / 4C protection.
verdict = current_profile_false_positive for positive promotion; current_profile_4C_too_late for protection timing
```

Axis answers:

```text
stage2_actionable_evidence_bonus: too generous if event premium is treated as non-price structural evidence
Yellow threshold 75: too loose for event-premium insurers without reserve-quality support
Green 87 / revision 55: appropriate; should block Green
price-only blowoff guard: appropriate but needs event-premium extension
full 4B non-price requirement: appropriate; event premium is non-price but risk overlay, not positive evidence
hard 4C routing: should be faster when event premium breaks and drawdown accelerates
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3 entry | peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R6L11_C22_000810 | 304000 | 370000 | 393500 | 0.738 | Green captured evidence quality but lost much of the 180D upside |
| R6L11_C22_005830 | 100000 | 111500 | 120700 | 0.556 | Green somewhat late but still before most local upside was consumed |
| R6L11_C22_001450 | 34450 | not_applicable | 36750 | not_applicable | no confirmed Green should be granted |
| R6L11_C22_000400 | 3370 | not_applicable | 4075 | not_applicable | event premium should not become Green |

Interpretation:

```text
C22 insurers should keep Green strict.
The useful residual adjustment is not broad Green relaxation.
The useful adjustment is better Stage2/Yellow gating based on insurer-specific reserve/K-ICS/payout-quality evidence.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---|---:|---:|---:|---:|---|
| R6L11_C22_000400_T2_4B_EVENT_PREMIUM_20240423 | control_premium_or_event_premium | 4075 | 4075 | 0.681 | 0.681 | good_event_premium_4B_overlay_not_positive_signal |
| R6L11_C22_000810_T2_STAGE3_GREEN_20240516 | valuation_repricing | 393500 | 435000 | 0.738 | 0.504 | not_full_4B; Green comparison only |
| R6L11_C22_005830_T2_STAGE3_GREEN_20240516 | valuation_repricing | 120700 | 120700 | 0.556 | 0.556 | not_full_4B; rerating still supported |

Conclusion:

```text
full_4b_requires_non_price_evidence remains correct.
However, for C22, event/control-premium evidence should route to 4B/risk overlay, not positive Stage2/3 evidence.
This is an extension of the existing guardrail, not a replacement.
```

## 16. 4C Protection Audit

| trigger_id | prior_peak_price | 4C entry_price | MAE_90D_after_4C | max_drawdown_after_peak_from_prior_stage | four_c_protection_label |
|---|---:|---:|---:|---:|---|
| R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628 | 4075 | 2915 | -14.07 | -38.53 | hard_4c_success_if_triggered_promptly |
| R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216 | 36750 | 34450 | -17.42 | -17.28 | thesis_break_watch_only |

Interpretation:

```text
Lotte Non-Life shows that event-premium insurance moves need faster 4C protection when the event premium breaks.
Hyundai Marine shows weaker quality / loss-ratio risk should be a Yellow/Watch constraint rather than a hard 4C.
```

## 17. Sector-Specific Rule Candidate

### Rule S-C22-01: Reserve/K-ICS/Payout Quality Gate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
axis = c22_reserve_kics_payout_quality_gate
proposal_type = sector_shadow_only
```

Candidate rule:

```text
For insurer C22 Stage2-Actionable or Yellow promotion, require at least two of:
1. sustainable IFRS17 earnings or CSM growth/quality evidence,
2. K-ICS / solvency headroom not impaired,
3. loss-ratio / reserve-risk not deteriorating,
4. explicit payout / shareholder return support,
5. valuation still below sector rerating band.

For Stage3-Green, require at least three of those, including either K-ICS/solvency or reserve/loss-ratio quality.
```

Backtest effect:

```text
- Retains Samsung Fire & Marine and DB Insurance as usable positives.
- Blocks or downgrades Hyundai Marine if reserve/loss-ratio evidence is unresolved.
- Blocks Lotte Non-Life event premium from positive promotion.
```

Confidence:

```text
confidence = medium_low
reason = 4 cases; positive and counterexample both present; needs more C22 holdout rows
```

## 18. Canonical-Archetype Rule Candidate

### Rule A-C22-01: Event Premium Is Risk Overlay, Not Reserve-Cycle Evidence

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
axis = c22_event_premium_guard
proposal_type = archetype_shadow_only
```

Candidate rule:

```text
If an insurer price move is primarily driven by sale, control premium, M&A rumor, or tender/event premium,
do not count the event premium as revision_score, reserve_quality_score, or capital_return_quality_score.
Route it to 4B/event overlay or C32 governance/event-premium mapping unless reserve-cycle evidence independently exists.
```

Backtest effect:

```text
- Lotte Non-Life remains eligible for narrative/event analysis.
- It cannot train positive C22 promotion weights.
- Its 4B/4C rows can still train event-premium risk/protection logic.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy | 4 | 000810_T1,005830_T1,001450_T1,000400_T1 | 17.16 | -15.29 | 19.44 | -16.74 | 0.50 | 0 | 1 | mixed; too permissive for C22 event/weak-reserve names |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | 000810_T2,005830_T2,001450_T1,000400_T1 | 14.11 | -14.61 | 15.02 | -16.30 | 0.50 | 1 | 2 | late positives; still misses insurer-specific counterexample quality |
| P1_sector_specific_candidate_profile | L6 sector shadow | 3 | 000810_T1,005830_T1,001450_watch | 16.30 | -13.76 | 18.94 | -13.76 | 0.33 | 0 | 1 | improved; blocks event premium but needs more holdout |
| P2_canonical_archetype_candidate_profile | C22 archetype shadow | 2 | 000810_T1,005830_T1 | 22.42 | -11.93 | 25.07 | -11.93 | 0.00 | 0 | 1 | best alignment in small sample; may be too strict without holdout |
| P3_counterexample_guard_profile | C22 event/reserve guard | 4 | 000810_T1,005830_T1,001450_watch,000400_4B/4C_only | 22.42 positive-only | -11.93 positive-only | 25.07 positive-only | -11.93 positive-only | 0.00 positive-promotion | 0 | 1 | best risk separation; 4B/4C rows kept out of positive weights |

## 20. Score-Return Alignment Matrix

| case_id | current score-return alignment | proposed alignment | explanation |
|---|---|---|---|
| R6L11_C22_000810 | aligned | aligned | early C22 evidence had strong MFE/MAE asymmetry |
| R6L11_C22_005830 | aligned | aligned | Stage2 path worked; Green still acceptable |
| R6L11_C22_001450 | misaligned | improved by reserve-quality gate | generic value-up was not enough to overcome MAE and weak MFE |
| R6L11_C22_000400 | misaligned | improved by event-premium guard | event premium had local MFE but severe drawdown; should not train positive C22 weights |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS | 2 | 2 | 1 | 1 | 4 | 0 | 8 | 4 | 2 | true | true | needs life insurers, reinsurers, rate-cut holdout, and 2025 reserve-strengthening cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [generic_financial_valueup_false_positive_for_insurers, event_premium_misclassified_as_structural_insurance_evidence, reserve_loss_ratio_quality_gap]
new_axis_proposed: [c22_reserve_kics_payout_quality_gate, c22_event_premium_guard]
existing_axis_strengthened: [full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Korean non-life insurer historical trigger rows.
- Stock-Web tradable_raw OHLC backtest from 2024 entry dates.
- 30D/90D/180D MFE and MAE.
- C22-specific residual classification against current calibrated proxy.
- Sector/canonical-archetype shadow rule proposal only.
```

Non-validation scope:

```text
- No live 2026 candidate scan.
- No current recommendation.
- No stock_agent code read or patch.
- No broker API, no auto-trading, no production scoring change.
- No paid consensus history validation.
- No precise intraday trigger timestamp audit.
- No 504D full 2Y metric where stock-web forward window is insufficient.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_kics_payout_quality_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"require insurer-specific reserve/K-ICS/payout-quality evidence before C22 Stage2/Yellow/Green promotion","retains Samsung Fire and DB Insurance while downgrading Hyundai Marine and Lotte event-premium false positive","R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216|R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216|R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216|R6L11_C22_000400_T1_EVENT_PREMIUM_20240213",4,4,2,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_event_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"sale/control-premium event is risk overlay and cannot train positive reserve-cycle weights","blocks Lotte Non-Life positive promotion; preserves its 4B/4C risk rows","R6L11_C22_000400_T1_EVENT_PREMIUM_20240213|R6L11_C22_000400_T2_4B_EVENT_PREMIUM_20240423|R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628",3,1,1,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L11_C22_000810","symbol":"000810","company_name":"Samsung Fire & Marine","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"insurer-specific capital quality and payout evidence supported rerating"}
{"row_type":"case","case_id":"R6L11_C22_005830","symbol":"005830","company_name":"DB Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment_with_moderate_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C22 signal supported by earnings quality plus capital-return visibility"}
{"row_type":"case","case_id":"R6L11_C22_001450","symbol":"001450","company_name":"Hyundai Marine & Fire","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_mfe_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"generic value-up sector evidence was not enough without strong reserve/K-ICS quality"}
{"row_type":"case","case_id":"R6L11_C22_000400","symbol":"000400","company_name":"Lotte Non-Life Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CONTROL_PREMIUM_EVENT_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L11_C22_000400_T1_EVENT_PREMIUM_20240213","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_premium_mfe_but_large_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"sale/control premium should be 4B/C32-style overlay, not C22 structural promotion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216","case_id":"R6L11_C22_000810","symbol":"000810","company_name":"Samsung Fire & Marine","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_kics_capital_return","loop_objective":"sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-16","evidence_available_at_that_date":"FY2023/early-2024 insurer earnings, K-ICS/capital-return discussion, and sector value-up evidence were available by the trigger window","evidence_source":"research_proxy_company_results_and_broker_review","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-16","entry_price":304000,"MFE_30D_pct":13.82,"MFE_90D_pct":29.44,"MFE_180D_pct":29.44,"MFE_1Y_pct":43.09,"MFE_2Y_pct":null,"MAE_30D_pct":-6.09,"MAE_90D_pct":-10.36,"MAE_180D_pct":-10.36,"MAE_1Y_pct":-10.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-30.75,"green_lateness_ratio":0.738,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_000810_20240216_304000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_C22_000810_T2_STAGE3_GREEN_20240516","case_id":"R6L11_C22_000810","symbol":"000810","company_name":"Samsung Fire & Marine","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_kics_capital_return","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"confirmed earnings/revision evidence after early rerating","evidence_source":"research_proxy_company_results_and_broker_review","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":370000,"MFE_30D_pct":6.35,"MFE_90D_pct":6.35,"MFE_180D_pct":17.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.95,"MAE_90D_pct":-11.08,"MAE_180D_pct":-11.08,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-17.82,"green_lateness_ratio":0.738,"four_b_local_peak_proximity":0.738,"four_b_full_window_peak_proximity":0.504,"four_b_timing_verdict":"not_full_4B_green_comparison_only","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_but_valid_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_000810_20240516_370000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216","case_id":"R6L11_C22_005830","symbol":"005830","company_name":"DB Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_kics_capital_return","loop_objective":"sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-16","evidence_available_at_that_date":"insurer earnings/payout/solvency evidence and value-up rerating evidence were available by the trigger window","evidence_source":"research_proxy_company_results_and_broker_review","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-16","entry_price":100000,"MFE_30D_pct":10.0,"MFE_90D_pct":15.4,"MFE_180D_pct":20.7,"MFE_1Y_pct":20.7,"MFE_2Y_pct":null,"MAE_30D_pct":-8.5,"MAE_90D_pct":-13.5,"MAE_180D_pct":-13.5,"MAE_1Y_pct":-13.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":120700,"drawdown_after_peak_pct":-15.82,"green_lateness_ratio":0.556,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_005830_20240216_100000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_C22_005830_T2_STAGE3_GREEN_20240516","case_id":"R6L11_C22_005830","symbol":"005830","company_name":"DB Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_kics_capital_return","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"confirmed earnings/revision evidence after the early value-up rerating window","evidence_source":"research_proxy_company_results_and_broker_review","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":111500,"MFE_30D_pct":3.5,"MFE_90D_pct":8.25,"MFE_180D_pct":8.25,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.67,"MAE_90D_pct":-7.26,"MAE_180D_pct":-8.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":120700,"drawdown_after_peak_pct":-15.82,"green_lateness_ratio":0.556,"four_b_local_peak_proximity":0.556,"four_b_full_window_peak_proximity":0.556,"four_b_timing_verdict":"not_full_4B_green_comparison_only","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"valid_green_moderate_upside","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_005830_20240516_111500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216","case_id":"R6L11_C22_001450","symbol":"001450","company_name":"Hyundai Marine & Fire","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"KOREA_INSURANCE_IFRS17_RATE_CYCLE_RESERVE_KICS","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_kics_capital_return","loop_objective":"counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-or-Yellow stress","trigger_date":"2024-02-16","evidence_available_at_that_date":"generic value-up and insurer sector evidence existed, but reserve/loss-ratio quality evidence was weaker","evidence_source":"research_proxy_company_results_and_broker_review","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-16","entry_price":34450,"MFE_30D_pct":4.06,"MFE_90D_pct":4.06,"MFE_180D_pct":6.68,"MFE_1Y_pct":12.63,"MFE_2Y_pct":null,"MAE_30D_pct":-11.9,"MAE_90D_pct":-17.42,"MAE_180D_pct":-17.42,"MAE_1Y_pct":-17.42,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-17.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_weak_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_001450_20240216_34450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_C22_000400_T1_EVENT_PREMIUM_20240213","case_id":"R6L11_C22_000400","symbol":"000400","company_name":"Lotte Non-Life Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CONTROL_PREMIUM_EVENT_FALSE_POSITIVE","sector":"insurance","primary_archetype":"insurance_event_premium_false_positive","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2 false positive stress","trigger_date":"2024-02-13","evidence_available_at_that_date":"control-premium / sale-event premium was visible; reserve-cycle evidence not sufficient","evidence_source":"research_proxy_event_premium_news_and_price_path","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-13","entry_price":3370,"MFE_30D_pct":8.9,"MFE_90D_pct":19.73,"MFE_180D_pct":20.92,"MFE_1Y_pct":20.92,"MFE_2Y_pct":null,"MAE_30D_pct":-19.88,"MAE_90D_pct":-19.88,"MAE_180D_pct":-25.67,"MAE_1Y_pct":-25.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":4075,"drawdown_after_peak_pct":-38.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.681,"four_b_full_window_peak_proximity":0.681,"four_b_timing_verdict":"good_event_premium_4B_overlay_not_positive_signal","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat"],"four_c_protection_label":"hard_4c_success_if_triggered_promptly","trigger_outcome_label":"false_positive_event_premium","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_000400_20240213_3370","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_C22_000400_T2_4B_EVENT_PREMIUM_20240423","case_id":"R6L11_C22_000400","symbol":"000400","company_name":"Lotte Non-Life Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CONTROL_PREMIUM_EVENT_FALSE_POSITIVE","sector":"insurance","primary_archetype":"insurance_event_premium_false_positive","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B event-premium overlay","trigger_date":"2024-04-23","evidence_available_at_that_date":"event/control-premium repricing reached late local stage without reserve-cycle confirmation","evidence_source":"research_proxy_event_premium_news_and_price_path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-23","entry_price":3850,"MFE_30D_pct":5.84,"MFE_90D_pct":5.84,"MFE_180D_pct":5.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.08,"MAE_90D_pct":-34.94,"MAE_180D_pct":-34.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":4075,"drawdown_after_peak_pct":-38.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.681,"four_b_full_window_peak_proximity":0.681,"four_b_timing_verdict":"good_event_premium_4B_overlay_not_positive_signal","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_000400_20240423_3850","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628","case_id":"R6L11_C22_000400","symbol":"000400","company_name":"Lotte Non-Life Insurance","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CONTROL_PREMIUM_EVENT_FALSE_POSITIVE","sector":"insurance","primary_archetype":"insurance_event_premium_false_positive","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C event-break protection","trigger_date":"2024-06-28","evidence_available_at_that_date":"event premium broke; sharp drawdown from prior event peak","evidence_source":"research_proxy_event_premium_news_and_price_path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["control_premium_or_event_premium"],"stage4c_evidence_fields":["thesis_evidence_broken","forced_liquidation_or_crash"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-28","entry_price":2915,"MFE_30D_pct":1.20,"MFE_90D_pct":1.20,"MFE_180D_pct":18.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.07,"MAE_90D_pct":-14.07,"MAE_180D_pct":-14.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":4075,"drawdown_after_peak_pct":-38.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":["control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_success_if_triggered_promptly","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_000400_20240628_2915","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_000810","trigger_id":"R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":72,"revision_score":58,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":68,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"reserve_quality_score":78,"kics_solvency_score":75,"capital_return_quality_score":72},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":72,"revision_score":58,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":68,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"reserve_quality_score":82,"kics_solvency_score":80,"capital_return_quality_score":76},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable / C22-qualified Yellow","changed_components":["reserve_quality_score","kics_solvency_score","capital_return_quality_score","execution_risk_score"],"component_delta_explanation":"C22-specific reserve/K-ICS/payout quality confirms generic financial value-up evidence.","MFE_90D_pct":29.44,"MAE_90D_pct":-10.36,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_005830","trigger_id":"R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":56,"relative_strength_score":65,"customer_quality_score":0,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"reserve_quality_score":76,"kics_solvency_score":72,"capital_return_quality_score":70},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":56,"relative_strength_score":65,"customer_quality_score":0,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"reserve_quality_score":80,"kics_solvency_score":76,"capital_return_quality_score":74},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable / C22-qualified Yellow","changed_components":["reserve_quality_score","kics_solvency_score","capital_return_quality_score","execution_risk_score"],"component_delta_explanation":"C22 gate improves confidence without broad Green relaxation.","MFE_90D_pct":15.40,"MAE_90D_pct":-13.50,"score_return_alignment_label":"aligned_moderate_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_001450","trigger_id":"R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":48,"revision_score":42,"relative_strength_score":52,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":62,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"reserve_quality_score":42,"kics_solvency_score":48,"capital_return_quality_score":50},"weighted_score_before":67,"stage_label_before":"Stage2 / possible Yellow under generic L6 value-up","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":48,"revision_score":42,"relative_strength_score":52,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":62,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"reserve_quality_score":38,"kics_solvency_score":42,"capital_return_quality_score":42},"weighted_score_after":58,"stage_label_after":"Watch / Stage1-2, not Yellow","changed_components":["reserve_quality_score","kics_solvency_score","capital_return_quality_score","execution_risk_score"],"component_delta_explanation":"Generic value-up evidence is penalized because C22 reserve/K-ICS quality is not confirmed.","MFE_90D_pct":4.06,"MAE_90D_pct":-17.42,"score_return_alignment_label":"counterexample_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_000400","trigger_id":"R6L11_C22_000400_T1_EVENT_PREMIUM_20240213","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":25,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":40,"execution_risk_score":62,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":18,"reserve_quality_score":30,"kics_solvency_score":35,"capital_return_quality_score":20,"event_premium_score":88},"weighted_score_before":70,"stage_label_before":"Stage2 false-positive risk if event premium is misread","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":25,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":40,"execution_risk_score":78,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":18,"reserve_quality_score":20,"kics_solvency_score":25,"capital_return_quality_score":15,"event_premium_score":88},"weighted_score_after":49,"stage_label_after":"4B/event overlay or C32 mapping; not positive C22","changed_components":["reserve_quality_score","kics_solvency_score","capital_return_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Event premium is separated from reserve-cycle evidence; it remains a risk overlay only.","MFE_90D_pct":19.73,"MAE_90D_pct":-19.88,"score_return_alignment_label":"counterexample_after_event_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_kics_payout_quality_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 requires reserve/K-ICS/payout-quality evidence beyond generic value-up","improves alignment by keeping positives and downgrading weak-reserve/event names","R6L11_C22_000810_T1_STAGE2_ACTIONABLE_20240216|R6L11_C22_005830_T1_STAGE2_ACTIONABLE_20240216|R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216|R6L11_C22_000400_T1_EVENT_PREMIUM_20240213",4,4,2,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_event_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"control-premium or sale event cannot count as reserve-cycle promotion evidence","prevents Lotte Non-Life false positive; keeps 4B/4C overlays","R6L11_C22_000400_T1_EVENT_PREMIUM_20240213|R6L11_C22_000400_T2_4B_EVENT_PREMIUM_20240423|R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628",3,1,1,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_financial_valueup_false_positive_for_insurers","event_premium_misclassified_as_structural_insurance_evidence","reserve_loss_ratio_quality_gap"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L11_C22_LIFE_INSURER_HOLDOUT_NEEDED","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"life_insurer_interest_rate_duration_and_csm_sensitivity_not_yet_covered_in_this_loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

### C22-specific expected implementation treatment

- Add only a shadow ledger row for `c22_reserve_kics_payout_quality_gate`.
- Add only a shadow ledger row for `c22_event_premium_guard`.
- Do not merge these into the global C21 financial value-up profile.
- Treat event/control-premium rows as overlay/risk rows, not positive C22 entries.
- Keep `full_4b_requires_non_price_evidence` intact.
- Keep `hard_4c_thesis_break_routes_to_4c` intact.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R6_loop_12_C22_holdout_or_L7_C23_bio_regulatory_approval
recommended_next_focus = C22 life insurer / rate-cut duration sensitivity holdout, or C23 bio approval-to-commercialization residual
why = this loop covers non-life insurers only; life insurer CSM/rate-duration behavior may differ
```

## 28. Source Notes

Stock-Web files checked:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000810.json
atlas/symbol_profiles/005/005830.json
atlas/symbol_profiles/001/001450.json
atlas/symbol_profiles/000/000400.json
atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv
```

Allowed stock_agent research artifacts checked:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```

Important caveat:

```text
All OHLC values are raw/unadjusted FinanceData/marcap values transformed into stock-web tradable shards.
This loop uses only clean 180D windows for weight-calibration rows.
```
