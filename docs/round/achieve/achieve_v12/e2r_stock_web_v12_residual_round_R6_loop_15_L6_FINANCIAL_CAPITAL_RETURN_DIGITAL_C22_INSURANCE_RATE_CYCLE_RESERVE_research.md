# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R6_loop_15_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
scheduled_round = R6
scheduled_loop = 15
completed_round = R6
completed_loop = 15
next_round = R7
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING

current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
```

This loop adds **6** new independent cases, **3** counterexamples, and **4** residual errors for **R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE**.

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

The residual question is not whether insurance can rerate. Prior C22 loops already established that. The new question is finer: when life insurers, reinsurers, and small non-life insurers all move in the same financial/value-up tape, which part of the move is reserve-quality evidence, which part is solvency/capital-return evidence, and which part is just a loud price wave passing through a narrow pipe?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
```

R6 maps to financial capital return / digital finance, and C22 is the insurance rate-cycle / reserve-quality branch. This loop deliberately avoids the prior C22 non-life cluster—삼성화재, DB손해보험, 현대해상, 한화손해보험, 롯데손해보험—and shifts the lens to life insurance, reinsurance, and small insurer price-only blowoff.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was restricted to calibration registry and representative trigger rows. Local v12 registry state already contains R6 Loop 10/11 C22 files centered on `000810`, `005830`, `001450`, `000370`, and `000400`. This file therefore uses **032830, 088350, 082640, 085620, 003690, 000540**.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 6
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "source_name": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

The manifest was checked for `source_name`, `source_repo_url`, `price_adjustment_status`, `min_date`, `max_date`, row counts, symbol counts, markets, and shard roots. `max_date=2026-02-20`, so every forward window is judged against the atlas date, not the present calendar.

## 5. Historical Eligibility Gate

All representative trigger rows satisfy the historical eligibility gate.

| symbol | company | profile_path | tested window status | calibration_usable |
|---:|---|---|---|---|
| 032830 | 삼성생명 | atlas/symbol_profiles/032/032830.json | no corporate-action candidate; clean 180D | true |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | no corporate-action candidate; clean 180D | true |
| 082640 | 동양생명 | atlas/symbol_profiles/082/082640.json | 2017 CA candidate outside tested window | true |
| 085620 | 미래에셋생명 | atlas/symbol_profiles/085/085620.json | 2018 CA candidate outside tested window | true |
| 003690 | 코리안리 | atlas/symbol_profiles/003/003690.json | old CA candidates outside tested window | true |
| 000540 | 흥국화재 | atlas/symbol_profiles/000/000540.json | old CA candidates outside tested window | true |

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical mapping | Compression decision |
|---|---|---|
| LIFE_INSURANCE_CSM_SOLVENCY_VALUEUP | C22_INSURANCE_RATE_CYCLE_RESERVE | keep as positive only when CSM/reserve/solvency quality is attached |
| LIFE_INSURANCE_PRICE_BETA_WITHOUT_QUALITY | C22_INSURANCE_RATE_CYCLE_RESERVE | counterexample guard; no Green promotion from beta alone |
| REINSURANCE_RATE_HARDENING_LOW_MAE | C22_INSURANCE_RATE_CYCLE_RESERVE | separate from life-IFRS17 beta; low-MAE moderate positive |
| SMALL_INSURER_PRICE_ONLY_BLOWOFF | C22_INSURANCE_RATE_CYCLE_RESERVE | 4B/4C overlay only, never positive Stage2/3 evidence |
| EVENT_PREMIUM_AFTER_CSM_RERATING | C22_INSURANCE_RATE_CYCLE_RESERVE | structural entry and event overheat must be split |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R6L15_C22_SAMSUNGLIFE_CSM_VALUEUP_20240201 | 032830 | 삼성생명 | structural_success | Stage2-Actionable | 2024-02-01 | 76000 | 42.76 | -9.34 | current_profile_correct |
| R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201 | 082640 | 동양생명 | structural_success | Stage2-Actionable | 2024-02-01 | 5380 | 20.82 | -10.59 | current_profile_4B_too_late |
| R6L15_C22_KOREANRE_REINSURANCE_RATE_20240201 | 003690 | 코리안리 | structural_success | Stage2-Actionable | 2024-02-01 | 7810 | 9.48 | -4.35 | current_profile_correct |
| R6L15_C22_HANWHALIFE_BETA_REVERSAL_20240201 | 088350 | 한화생명 | failed_rerating | Stage2-Actionable_candidate_rejected | 2024-02-01 | 3355 | 13.71 | -16.39 | current_profile_false_positive |
| R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201 | 085620 | 미래에셋생명 | false_positive_green | Stage2-Actionable_candidate_rejected | 2024-02-01 | 5770 | 12.65 | -23.66 | current_profile_false_positive |
| R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201 | 000540 | 흥국화재 | price_moved_without_evidence | Stage2-Actionable_candidate_rejected | 2024-02-01 | 4370 | 51.03 | -23.8 | current_profile_correct |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 6
calibration_usable_trigger_count = 9
representative_trigger_count = 6
new_independent_case_count = 6
reused_case_count = 0
```

The mix is deliberately not just “more insurance positives.” 삼성생명 and 동양생명 show that life insurers can rerate sharply when the market sees accounting/solvency leverage. 코리안리 is a quieter positive: the return is smaller, but the path behaves more like a sturdy bridge than a firework. 한화생명, 미래에셋생명, and 흥국화재 are the guardrails: price beta alone can look alive, but the later path tells whether the engine actually caught.

## 9. Evidence Source Map

| case_id | evidence family | evidence available at trigger | evidence-source handling |
|---|---|---|---|
| R6L15_C22_SAMSUNGLIFE_CSM_VALUEUP_20240201 | life CSM/solvency/value-up | public 2024 value-up / insurer rerating context | DART/IR IDs required before production ingestion |
| R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201 | life CSM plus later event-premium overlay | public value-up / life insurer rerating context | split Stage2 positive from later 4B event overheat |
| R6L15_C22_KOREANRE_REINSURANCE_RATE_20240201 | reinsurance rate/underwriting cycle | public reinsurer-rate cycle context | separate reinsurer low-MAE credit from life CSM score |
| R6L15_C22_HANWHALIFE_BETA_REVERSAL_20240201 | life-insurer beta without quality confirmation | price beta visible; quality confirmation insufficient | counterexample, not positive promotion |
| R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201 | price beta without reserve-quality follow-through | early spike visible, later MAE high | false-positive guard |
| R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201 | small insurer price-only blowoff | price-only surge visible | 4B/4C overlay only |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | representative entry row |
|---:|---|---|---|---|
| 032830 | 삼성생명 | atlas/symbol_profiles/032/032830.json | atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv | 2024-02-01 close=76000 |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | 2024-02-01 close=3355 |
| 082640 | 동양생명 | atlas/symbol_profiles/082/082640.json | atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv | 2024-02-01 close=5380 |
| 085620 | 미래에셋생명 | atlas/symbol_profiles/085/085620.json | atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv | 2024-02-01 close=5770 |
| 003690 | 코리안리 | atlas/symbol_profiles/003/003690.json | atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv | 2024-02-01 close=7810 |
| 000540 | 흥국화재 | atlas/symbol_profiles/000/000540.json | atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv | 2024-02-01 close=4370 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak_date | peak_price | current verdict | aggregate role |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---|
| R6L15_C22_032830_T1 | 032830 | Stage2-Actionable | 2024-02-01 | 2024-02-01 | 76000 | 42.76 / -9.34 | 42.76 / -9.34 | 42.76 / -9.34 | 2024-03-08 | 108500 | current_profile_correct | representative |
| R6L15_C22_082640_T1 | 082640 | Stage2-Actionable | 2024-02-01 | 2024-02-01 | 5380 | 20.82 / -10.59 | 20.82 / -10.59 | 75.46 / -10.59 | 2024-07-31 | 9440 | current_profile_4B_too_late | representative |
| R6L15_C22_003690_T1 | 003690 | Stage2-Actionable | 2024-02-01 | 2024-02-01 | 7810 | 8.45 / -4.35 | 9.48 / -4.35 | 15.24 / -4.35 | 2024-08-26 | 9000 | current_profile_correct | representative |
| R6L15_C22_088350_T1 | 088350 | Stage2-Actionable_candidate_rejected | 2024-02-01 | 2024-02-01 | 3355 | 13.71 / -10.88 | 13.71 / -16.39 | 13.71 / -16.39 | 2024-02-13 | 3815 | current_profile_false_positive | representative |
| R6L15_C22_085620_T1 | 085620 | Stage2-Actionable_candidate_rejected | 2024-02-01 | 2024-02-01 | 5770 | 12.65 / -21.92 | 12.65 / -23.66 | 12.65 / -23.66 | 2024-02-06 | 6500 | current_profile_false_positive | representative |
| R6L15_C22_000540_T1 | 000540 | Stage2-Actionable_candidate_rejected | 2024-02-01 | 2024-02-01 | 4370 | 51.03 / -23.8 | 51.03 / -23.8 | 51.03 / -23.8 | 2024-02-14 | 6600 | current_profile_correct | representative |
| R6L15_C22_082640_T4B | 082640 | Stage4B | 2024-07-31 | 2024-07-31 | 7970 | 18.44 / -18.57 | 18.44 / -34.5 | 18.44 / -34.5 | 2024-07-31 | 9440 | current_profile_4B_too_late | 4B_overlay_only |
| R6L15_C22_000540_T4B | 000540 | Stage4B | 2024-02-14 | 2024-02-14 | 5570 | 18.49 / -27.74 | 18.49 / -32.41 | 18.49 / -32.41 | 2024-02-14 | 6600 | current_profile_correct | 4B_overlay_only |
| R6L15_C22_085620_T4C | 085620 | Stage4C | 2024-02-29 | 2024-02-29 | 4880 | 10.25 / -9.73 | 25.82 / -9.73 | 25.82 / -9.73 | 2024-06-27 | 6140 | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | company | entry_date | entry_price | peak_date | peak_price | MFE_30D | MFE_90D | MFE_180D | MAE_90D | drawdown_after_peak | outcome |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| 032830 | 삼성생명 | 2024-02-01 | 76000 | 2024-03-08 | 108500 | 42.76 | 42.76 | 42.76 | -9.34 | -29.4 | structural_success |
| 082640 | 동양생명 | 2024-02-01 | 5380 | 2024-07-31 | 9440 | 20.82 | 20.82 | 75.46 | -10.59 | -42.27 | structural_success_with_4B_overlay |
| 003690 | 코리안리 | 2024-02-01 | 7810 | 2024-08-26 | 9000 | 8.45 | 9.48 | 15.24 | -4.35 | -8.44 | moderate_structural_success |
| 088350 | 한화생명 | 2024-02-01 | 3355 | 2024-02-13 | 3815 | 13.71 | 13.71 | 13.71 | -16.39 | -26.34 | failed_rerating_high_mae |
| 085620 | 미래에셋생명 | 2024-02-01 | 5770 | 2024-02-06 | 6500 | 12.65 | 12.65 | 12.65 | -23.66 | -32.23 | false_positive_green_high_mae |
| 000540 | 흥국화재 | 2024-02-01 | 4370 | 2024-02-14 | 6600 | 51.03 | 51.03 | 51.03 | -23.8 | -42.95 | price_only_local_peak_counterexample |

## 13. Current Calibrated Profile Stress Test

| symbol | current profile issue | actual path verdict | residual interpretation |
|---:|---|---|---|
| 032830 | acceptable | strong MFE with manageable MAE | current profile correct when quality/solvency bucket is visible |
| 082640 | 4B late risk | 180D MFE large, then deep post-peak drawdown | positive entry and later event overheat must be separate rows |
| 003690 | acceptable but under-expressive | modest MFE, low MAE | reinsurer low-MAE path deserves small sector-specific credit |
| 088350 | too early | MFE capped early, MAE widened | life-insurer beta should not become Green without quality confirmation |
| 085620 | false positive | modest MFE, large MAE | price beta without follow-through should be capped |
| 000540 | correct if price-only guard fires | large MFE but violent reversal | keep as 4B/4C overlay only |

Existing-axis status:

```text
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
stage3_green_revision_min = existing_axis_kept
stage2_actionable_evidence_bonus = existing_axis_kept_but_capped_for_C22_beta_only
```

## 14. Stage2 / Yellow / Green Comparison

C22 should not allow the following mechanical mistake: **IFRS17/insurance basket relative strength → Stage2 bonus → Green**. That jump works only when reserve quality and solvency/capital-return visibility are present. Otherwise the score is like a thermometer placed in sunlight: it records heat, but not the patient’s temperature.

```text
green_lateness_ratio = not_applicable for representative rows without confirmed later Green trigger
green_lateness_interpretation = use event/overheat rows separately rather than moving Stage3 label backward
```

## 15. 4B Local vs Full-window Timing Audit

| overlay_trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| R6L15_C22_082640_T4B | 1.00 | 1.00 | valuation_blowoff + event_premium | good_full_window_4B_timing |
| R6L15_C22_000540_T4B | 1.00 | 1.00 | price_only + positioning_overheat | price_only_local_4B_guard_success; do not treat as positive C22 evidence |

## 16. 4C Protection Audit

`R6L15_C22_085620_T4C` is tagged `hard_4c_late`: by the time the rejected beta path was visibly broken, the representative entry had already suffered high MAE. The better rule is earlier: prevent the Green promotion unless reserve-quality evidence is attached.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L6_reinsurer_low_MAE_credit
proposal = +0.5 shadow credit when reinsurer/insurance-cycle evidence has low MAE and moderate MFE, even if life-insurance CSM evidence is absent
confidence = low
```

This is not ready as a production global rule. It is a small sector-specific lantern: useful in the reinsurance corner, dangerous if carried into every insurance ticker.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = C22_reserve_quality_gate
axis_2 = C22_price_only_small_insurer_cap
proposal = require reserve/solvency/CSM quality for C22 positive promotion; cap price-only beta at Watch/4B overlay
confidence = medium
```

C22 should split three engines that used to look similar on a chart:

1. **Quality life insurer rerating** — promotable.
2. **Reinsurer hardening cycle** — promotable but smaller and lower-MAE.
3. **Small insurer price-only blowoff** — never promotable, but useful as 4B/4C training data.

## 19. Before / After Backtest Comparison

| profile | profile_id | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | none | 6 | 25.07 | -14.69 | 35.14 | -14.69 | 0.33 | 1 | 1 | mixed; allows life-insurer beta false positives |
| P0b | e2r_2_0_baseline_reference | older thresholds | 6 | 25.07 | -14.69 | 35.14 | -14.69 | 0.5 | 2 | 2 | worse; over-promotes price-only insurance beta |
| P1 | sector_specific_candidate_profile | reserve_quality_gate + solvency_buffer_gate | 6 | 25.07 | -14.69 | 35.14 | -14.69 | 0.17 | 0 | 1 | better; keeps positive quality cases while blocking small beta spikes |
| P2 | canonical_archetype_candidate_profile | CSM_quality_not_equal_reserve_quality | 6 | 25.07 | -14.69 | 35.14 | -14.69 | 0.17 | 0 | 1 | best explanatory fit for C22 |
| P3 | counterexample_guard_profile | relative_strength_cap_without_nonprice_evidence | 6 | 25.07 | -14.69 | 35.14 | -14.69 | 0.0 | 1 | 0 | safest guard; may under-score Korean Re |

## 20. Score-Return Alignment Matrix

| symbol | before stage / score | after stage / score | MFE_90D | MAE_90D | current_profile_verdict | residual driver |
|---:|---|---|---:|---:|---|---|
| 032830 | Stage3-Green / 98.4 | Stage3-Green / 116.3 | 42.76 | -9.34 | current_profile_correct | quality_large_life_insurer |
| 082640 | Stage3-Green / 94.2 | Stage3-Green / 112.0 | 20.82 | -10.59 | current_profile_4B_too_late | event_premium_overlay_after_structural_move |
| 003690 | Stage3-Yellow / 82.3 | Stage3-Green / 90.8 | 9.48 | -4.35 | current_profile_correct | reinsurance_rate_hardening_not_life_csm |
| 088350 | Stage2-Actionable / 74.7 | Stage2 / 61.9 | 13.71 | -16.39 | current_profile_false_positive | beta_without_reserve_quality_confirmation |
| 085620 | Stage2-Actionable / 66.2 | Watch/Reject / 53.4 | 12.65 | -23.66 | current_profile_false_positive | price_beta_without_durable_quality |
| 000540 | Stage2-Actionable / 70.4 | Watch/Reject / 44.9 | 51.03 | -23.8 | current_profile_correct | small_insurer_liquidity_price_only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING | 3 | 3 | 2 | 1 | 6 | 0 | 9 | 6 | 4 | true | true | life/reinsurer/small-insurer C22 split improved; still needs more reinsurer holdout rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 6
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
positive_case_count: 3
counterexample_count: 3
current_profile_error_count: 4

tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_revision_min

residual_error_types_found:
  - life_insurer_beta_false_positive
  - CSM_quality_not_equal_reserve_quality
  - price_only_small_insurer_blowoff
  - event_premium_4B_late

new_axis_proposed:
  - C22_reserve_quality_gate
  - C22_price_only_small_insurer_cap
  - L6_reinsurer_low_MAE_credit

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
  - stage3_yellow_total_min

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest fields and max_date
- symbol profile availability and corporate-action candidate status
- representative entry_date / entry_price from tradable shards
- 30D / 90D / 180D MFE/MAE using raw unadjusted OHLC inspected in stock-web shards
- same_entry_group_id dedupe for aggregate inclusion
- 4B local vs full-window split for overlay rows
```

Not validated in this research file:

```text
- production stock_agent scoring implementation
- live candidate discovery
- current 2026 recommendation status
- DART/KIND source IDs for every narrative evidence field
- broker execution or trading rules
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_reserve_quality_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"CSM/IFRS17 beta is not enough; reserve/solvency quality must be present","reduced false positives in 088350/085620 while keeping 032830/082640/003690","R6L15_C22_032830_T1|R6L15_C22_082640_T1|R6L15_C22_003690_T1|R6L15_C22_088350_T1|R6L15_C22_085620_T1",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_price_only_small_insurer_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"small insurer price blowoff creates large MFE but high drawdown; no promotion without non-price evidence","blocks 000540 as positive signal but keeps it as 4B/4C guard row","R6L15_C22_000540_T1|R6L15_C22_000540_T4B",2,1,1,medium,canonical_shadow_only,"not production; price-only cannot promote Stage2/3"
shadow_weight,L6_reinsurer_low_MAE_credit,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,0.5,+0.5,"reinsurance rate-hardening path had modest MFE but low MAE; should not be discarded by life-insurance CSM template","preserves 003690 as moderate structural positive rather than late/weak signal","R6L15_C22_003690_T1",1,1,0,low,sector_shadow_only,"requires more reinsurer samples before production
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L15_C22_SAMSUNGLIFE_CSM_VALUEUP_20240201", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L15_C22_032830_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "life-insurance CSM/solvency visibility plus low-PBR/value-up rerating pressure; large-cap quality bucket"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_032830_T1", "case_id": "R6L15_C22_SAMSUNGLIFE_CSM_VALUEUP_20240201", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "life-insurance CSM/solvency visibility plus low-PBR/value-up rerating pressure; large-cap quality bucket", "evidence_source": "public historical event label; DART/IR attachment required during later ingestion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 76000, "MFE_30D_pct": 42.76, "MFE_90D_pct": 42.76, "MFE_180D_pct": 42.76, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.34, "MAE_90D_pct": -9.34, "MAE_180D_pct": -9.34, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-08", "peak_price": 108500, "drawdown_after_peak_pct": -29.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_SAMSUNGLIFE_CSM_VALUEUP_20240201::2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C22_SAMSUNGLIFE_CSM_VALUEUP_20240201", "trigger_id": "R6L15_C22_032830_T1", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 8, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 98.4, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 15, "customer_quality_score": 8, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 116.3, "stage_label_after": "Stage3-Green", "changed_components": ["reserve_quality_gate", "solvency_buffer_gate", "price_only_relative_strength_cap", "execution_risk_penalty"], "component_delta_explanation": "C22 shadow profile separates CSM/reserve/solvency evidence from price-only insurance beta; positive cases receive quality credit, counterexamples lose promotion power.", "MFE_90D_pct": 42.76, "MAE_90D_pct": -9.34, "score_return_alignment_label": "structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L15_C22_082640_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_with_4B_overlay", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "life-insurance CSM/value-up rerating later mixed with event-premium overheat; strong upside but required 4B separation"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_082640_T1", "case_id": "R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "life-insurance CSM/value-up rerating later mixed with event-premium overheat; strong upside but required 4B separation", "evidence_source": "public historical event label; DART/IR attachment required during later ingestion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "profile_path": "atlas/symbol_profiles/082/082640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 5380, "MFE_30D_pct": 20.82, "MFE_90D_pct": 20.82, "MFE_180D_pct": 75.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.59, "MAE_90D_pct": -10.59, "MAE_180D_pct": -10.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 9440, "drawdown_after_peak_pct": -42.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_4B_overlay", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201::2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201", "trigger_id": "R6L15_C22_082640_T1", "symbol": "082640", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 3, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 94.2, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 15, "customer_quality_score": 3, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 112.0, "stage_label_after": "Stage3-Green", "changed_components": ["reserve_quality_gate", "solvency_buffer_gate", "price_only_relative_strength_cap", "execution_risk_penalty"], "component_delta_explanation": "C22 shadow profile separates CSM/reserve/solvency evidence from price-only insurance beta; positive cases receive quality credit, counterexamples lose promotion power.", "MFE_90D_pct": 20.82, "MAE_90D_pct": -10.59, "score_return_alignment_label": "structural_success_with_4B_overlay", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "case", "case_id": "R6L15_C22_KOREANRE_REINSURANCE_RATE_20240201", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L15_C22_003690_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "moderate_structural_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "reinsurance-rate/underwriting-cycle improvement with low MAE; not a life-IFRS17 beta clone"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_003690_T1", "case_id": "R6L15_C22_KOREANRE_REINSURANCE_RATE_20240201", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "reinsurance-rate/underwriting-cycle improvement with low MAE; not a life-IFRS17 beta clone", "evidence_source": "public historical event label; DART/IR attachment required during later ingestion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv", "profile_path": "atlas/symbol_profiles/003/003690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 7810, "MFE_30D_pct": 8.45, "MFE_90D_pct": 9.48, "MFE_180D_pct": 15.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.35, "MAE_90D_pct": -4.35, "MAE_180D_pct": -4.35, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 9000, "drawdown_after_peak_pct": -8.44, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "moderate_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_KOREANRE_REINSURANCE_RATE_20240201::2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C22_KOREANRE_REINSURANCE_RATE_20240201", "trigger_id": "R6L15_C22_003690_T1", "symbol": "003690", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82.3, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 6, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90.8, "stage_label_after": "Stage3-Green", "changed_components": ["reserve_quality_gate", "solvency_buffer_gate", "price_only_relative_strength_cap", "execution_risk_penalty"], "component_delta_explanation": "C22 shadow profile separates CSM/reserve/solvency evidence from price-only insurance beta; positive cases receive quality credit, counterexamples lose promotion power.", "MFE_90D_pct": 9.48, "MAE_90D_pct": -4.35, "score_return_alignment_label": "moderate_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "R6L15_C22_HANWHALIFE_BETA_REVERSAL_20240201", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L15_C22_088350_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_high_mae", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "life-insurance beta moved with the basket but reserve/solvency/capital-return confirmation was not strong enough to justify Green"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_088350_T1", "case_id": "R6L15_C22_HANWHALIFE_BETA_REVERSAL_20240201", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "life-insurance beta moved with the basket but reserve/solvency/capital-return confirmation was not strong enough to justify Green", "evidence_source": "public historical event label; DART/IR attachment required during later ingestion", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 3355, "MFE_30D_pct": 13.71, "MFE_90D_pct": 13.71, "MFE_180D_pct": 13.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.88, "MAE_90D_pct": -16.39, "MAE_180D_pct": -16.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-13", "peak_price": 3815, "drawdown_after_peak_pct": -26.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_rerating_high_mae", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_HANWHALIFE_BETA_REVERSAL_20240201::2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C22_HANWHALIFE_BETA_REVERSAL_20240201", "trigger_id": "R6L15_C22_088350_T1", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 3, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74.7, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 3, "policy_or_regulatory_score": 10, "valuation_repricing_score": 5, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61.9, "stage_label_after": "Stage2", "changed_components": ["reserve_quality_gate", "solvency_buffer_gate", "price_only_relative_strength_cap", "execution_risk_penalty"], "component_delta_explanation": "C22 shadow profile separates CSM/reserve/solvency evidence from price-only insurance beta; positive cases receive quality credit, counterexamples lose promotion power.", "MFE_90D_pct": 13.71, "MAE_90D_pct": -16.39, "score_return_alignment_label": "failed_rerating_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L15_C22_085620_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_green_high_mae", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "price beta and single-day insurance theme without durable CSM/reserve-quality follow-through; large MAE overwhelms modest MFE"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_085620_T1", "case_id": "R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "price beta and single-day insurance theme without durable CSM/reserve-quality follow-through; large MAE overwhelms modest MFE", "evidence_source": "public historical event label; DART/IR attachment required during later ingestion", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 5770, "MFE_30D_pct": 12.65, "MFE_90D_pct": 12.65, "MFE_180D_pct": 12.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.92, "MAE_90D_pct": -23.66, "MAE_180D_pct": -23.66, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 6500, "drawdown_after_peak_pct": -32.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_green_high_mae", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201::2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201", "trigger_id": "R6L15_C22_085620_T1", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66.2, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53.4, "stage_label_after": "Watch/Reject", "changed_components": ["reserve_quality_gate", "solvency_buffer_gate", "price_only_relative_strength_cap", "execution_risk_penalty"], "component_delta_explanation": "C22 shadow profile separates CSM/reserve/solvency evidence from price-only insurance beta; positive cases receive quality credit, counterexamples lose promotion power.", "MFE_90D_pct": 12.65, "MAE_90D_pct": -23.66, "score_return_alignment_label": "false_positive_green_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R6L15_C22_000540_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_local_peak_counterexample", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "small/illiquid insurer price-only surge; MFE is large but not usable as positive C22 evidence without non-price reserve/solvency proof"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_000540_T1", "case_id": "R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "small/illiquid insurer price-only surge; MFE is large but not usable as positive C22 evidence without non-price reserve/solvency proof", "evidence_source": "public historical event label; DART/IR attachment required during later ingestion", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv", "profile_path": "atlas/symbol_profiles/000/000540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 4370, "MFE_30D_pct": 51.03, "MFE_90D_pct": 51.03, "MFE_180D_pct": 51.03, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.8, "MAE_90D_pct": -23.8, "MAE_180D_pct": -23.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-14", "peak_price": 6600, "drawdown_after_peak_pct": -42.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_only_local_peak_counterexample", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201::2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201", "trigger_id": "R6L15_C22_000540_T1", "symbol": "000540", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 15, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70.4, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 0, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 44.9, "stage_label_after": "Watch/Reject", "changed_components": ["reserve_quality_gate", "solvency_buffer_gate", "price_only_relative_strength_cap", "execution_risk_penalty"], "component_delta_explanation": "C22 shadow profile separates CSM/reserve/solvency evidence from price-only insurance beta; positive cases receive quality credit, counterexamples lose promotion power.", "MFE_90D_pct": 51.03, "MAE_90D_pct": -23.8, "score_return_alignment_label": "price_only_local_peak_counterexample", "current_profile_verdict": "current_profile_correct"}
{"row_type": "trigger", "trigger_id": "R6L15_C22_082640_T4B", "case_id": "R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B", "trigger_date": "2024-07-31", "evidence_available_at_that_date": "overlay trigger based on post-entry overheat/thesis-break risk; not positive Stage2/3 evidence", "evidence_source": "stock-web OHLC plus later DART/IR attachment required", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "profile_path": "atlas/symbol_profiles/082/082640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-31", "entry_price": 7970, "MFE_30D_pct": 18.44, "MFE_90D_pct": 18.44, "MFE_180D_pct": 18.44, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.57, "MAE_90D_pct": -34.5, "MAE_180D_pct": -34.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 9440, "drawdown_after_peak_pct": -42.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_TONGYANGLIFE_CSM_EVENT_20240201::2024-07-31", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for already counted representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L15_C22_000540_T4B", "case_id": "R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B", "trigger_date": "2024-02-14", "evidence_available_at_that_date": "overlay trigger based on post-entry overheat/thesis-break risk; not positive Stage2/3 evidence", "evidence_source": "stock-web OHLC plus later DART/IR attachment required", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv", "profile_path": "atlas/symbol_profiles/000/000540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-14", "entry_price": 5570, "MFE_30D_pct": 18.49, "MFE_90D_pct": 18.49, "MFE_180D_pct": 18.49, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.74, "MAE_90D_pct": -32.41, "MAE_180D_pct": -32.41, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-14", "peak_price": 6600, "drawdown_after_peak_pct": -42.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_guard_success", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_price_only_guard_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_HEUNGKUKFIRE_PRICEONLY_20240201::2024-02-14", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for already counted representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L15_C22_085620_T4C", "case_id": "R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_SOLVENCY_RESERVE_QUALITY_AND_REINSURANCE_RATE_HARDENING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve_quality", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2024-02-29", "evidence_available_at_that_date": "overlay trigger based on post-entry overheat/thesis-break risk; not positive Stage2/3 evidence", "evidence_source": "stock-web OHLC plus later DART/IR attachment required", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "reserve_quality_not_confirmed"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-29", "entry_price": 4880, "MFE_30D_pct": 10.25, "MFE_90D_pct": 25.82, "MFE_180D_pct": 25.82, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.73, "MAE_90D_pct": -9.73, "MAE_180D_pct": -9.73, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-27", "peak_price": 6140, "drawdown_after_peak_pct": -18.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4C_late", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C22_MIRAEASSETLIFE_PRICEBETA_20240201::2024-02-29", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for already counted representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "residual_contribution", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 6, "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 6, "new_trigger_family_count": 6, "positive_case_count": 3, "counterexample_count": 3, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["life_insurer_beta_false_positive", "price_only_small_insurer_blowoff", "event_premium_4B_late", "CSM_quality_not_equal_reserve_quality"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 15
next_round = R7
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest was checked for source, date range, row counts, shard roots, and raw-unadjusted caveat.
- Symbol profiles were checked for each representative ticker to confirm profile existence, available years, row-status counts, and corporate-action caveats.
- Price shards inspected: `032830/2024.csv`, `088350/2024.csv`, `082640/2024.csv`, `085620/2024.csv`, `003690/2024.csv`, `000540/2024.csv`.
- The evidence labels in this MD are historical research labels. Later ingestion should attach DART/KIND/IR IDs before any production ledger promotion.

