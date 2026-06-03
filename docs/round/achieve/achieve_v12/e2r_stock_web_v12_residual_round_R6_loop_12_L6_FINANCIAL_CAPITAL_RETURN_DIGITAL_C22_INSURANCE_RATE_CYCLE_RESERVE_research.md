# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "output_file": "e2r_stock_web_v12_residual_round_R6_loop_12_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md",
  "scheduled_round": "R6",
  "scheduled_loop": 12,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 12,
  "computed_next_round": "R7",
  "computed_next_loop": 12,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN",
  "loop_objective": [
    "coverage_gap_fill",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "stage2_actionable_bonus_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 3,
  "diversity_score_summary": "estimated +53; wrong_round_penalty=0; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0; local R6 loop 10/11 were C21, so C22 fills scheduled-round gap",
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": [
    "C22_verified_CSM_KICS_capital_return_bonus",
    "C22_rate_cycle_beta_cap_without_reserve_quality",
    "C22_reserve_risk_high_MAE_guard",
    "C22_post_rerating_4B_positioning_overlay"
  ],
  "existing_axis_strengthened": [
    "stage2_actionable_evidence_bonus",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "existing_axis_weakened": null
}
```

This loop adds **3** new independent cases, **1** counterexamples, and **3** residual errors for **R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE**.

No current/live candidate scan was performed. No stock_agent production scoring was changed. This is a standalone historical residual calibration file.

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

This loop does **not** re-prove the global Stage2 bonus, Green threshold, or price-only 4B guard. It stress-tests whether the already calibrated profile still lacks an insurance-specific distinction between real CSM/K-ICS/capital-return evidence and generic rate-cycle beta.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 12
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN
round_sector_consistency = pass
```

R6 allows `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. C22 is selected because local R6 loop 10 and loop 11 were both C21 bank/financial-holding capital-return studies, while no local C22 insurance file was found in `/mnt/data`.

## 3. Previous Coverage / Duplicate Avoidance Check

Local duplicate scan:

```text
existing_local_R6_v12:
- e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
- e2r_stock_web_v12_residual_round_R6_loop_11_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

selected_gap:
- C22_INSURANCE_RATE_CYCLE_RESERVE
```

No reused symbol + trigger_date + entry_date + evidence-family row is used. 삼성화재, DB손해보험, 현대해상 are new independent C22 samples for this loop.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest confirms:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
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
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Price basis is `tradable_raw`. These rows are raw/unadjusted and are not corporate-action-adjusted. Corporate action candidate windows are excluded from quantitative calibration when they overlap the entry-to-180D window.

## 5. Historical Eligibility Gate

| symbol | profile_path | profile corporate-action caveat | entry_date | 180D window | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 000810 | atlas/symbol_profiles/000/000810.json | old action candidates only: 1999-02-01, 1999-07-05, 2000-02-15 | 2024-02-02 | available before manifest max_date | true |
| 005830 | atlas/symbol_profiles/005/005830.json | old action candidate only: 1999-07-20 | 2024-02-02 | available before manifest max_date | true |
| 001450 | atlas/symbol_profiles/001/001450.json | old action candidate only: 2004-07-13 | 2024-02-02 | available before manifest max_date | true |

All representative triggers have at least 180 stock-web tradable rows available after entry and no recent profile corporate-action candidate overlapping the 180D calibration window.

## 6. Canonical Archetype Compression Map

```text
fine_archetype:
  NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN
maps_to:
  C22_INSURANCE_RATE_CYCLE_RESERVE
```

C22 is distinct from C21. C21 rewards ROE/PBR and capital return in banks/holding companies. C22 must read insurance through four extra lenses: IFRS17 CSM quality, K-ICS solvency buffer, reserve-risk asymmetry, and shareholder-return visibility.

## 7. Case Selection Summary

| case_id | symbol | name | role | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202 | 000810 | 삼성화재 | positive | Stage2-Actionable | 2024-02-02 | 299000 | 27.09 | -8.86 | 31.61 | -8.86 | current_profile_too_late |
| R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202 | 005830 | DB손해보험 | positive | Stage2-Actionable | 2024-02-02 | 99200 | 16.33 | -13.1 | 21.67 | -13.1 | current_profile_too_late |
| R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202 | 001450 | 현대해상 | counterexample | Stage2-Actionable_false | 2024-02-02 | 35950 | 2.36 | -20.86 | 2.36 | -20.86 | current_profile_false_positive |

Selection rationale:

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1 overlay trigger
minimum_calibration_usable_case_count = 3
new_independent_case_ratio = 3 / 3 = 1.00
```

## 8. Positive vs Counterexample Balance

The positive pair is deliberately two non-life insurers with different drawdown profiles. 삼성화재 validates the clean CSM/K-ICS/capital-return rerating path; DB손해보험 validates the same archetype but forces a high-MAE guard. 현대해상 is the counterexample: the same insurer/rate/value-up beta was not enough, because MFE stayed tiny and MAE became large.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence source note |
| --- | --- | --- | --- | --- |
| R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202 | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality, early_revision_signal | confirmed_revision, financial_visibility, multiple_public_sources, low_red_team_risk | valuation_blowoff, positioning_overheat | source_proxy: 2024 low-PBR/value-up policy context + issuer IR/earnings evidence family; exact URL enrichment required before production promotion |
| R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202 | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality, early_revision_signal | confirmed_revision, financial_visibility, multiple_public_sources | valuation_blowoff, positioning_overheat | source_proxy: 2024 insurer value-up/IFRS17 earnings evidence family; exact URL enrichment required before production promotion |
| R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202 | public_event_or_disclosure, relative_strength | none | price_only_local_peak, positioning_overheat, thesis_evidence_broken | source_proxy: same 2024 policy/rate-cycle evidence family; issuer-specific reserve and payout confirmation weaker than positive cases |

No trigger is promoted from price action alone. Price confirms or rejects the evidence score; it does not create Stage2/3 evidence.

## 10. Price Data Source Map

| symbol | company | tradable shard | profile | entry row used |
| --- | --- | --- | --- | --- |
| 000810 | 삼성화재 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json | 2024-02-02 close 299000 |
| 005830 | DB손해보험 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json | 2024-02-02 close 99200 |
| 001450 | 현대해상 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/symbol_profiles/001/001450.json | 2024-02-02 close 35950 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN | 000810 | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 299000 | 15.72 | 27.09 | 31.61 | -4.52 | -8.86 | -8.86 | 2024-12-03 | 435000 | current_profile_too_late | True |
| R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN | 005830 | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 99200 | 10.89 | 16.33 | 21.67 | -8.17 | -13.1 | -13.1 | 2024-07-02 | 120700 | current_profile_too_late | True |
| R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD | 001450 | Stage2-Actionable_false | 2024-02-02 | 2024-02-02 | 35950 | 2.36 | 2.36 | 2.36 | -14.88 | -20.86 | -20.86 | 2024-02-05 | 36800 | current_profile_false_positive | True |
| R6L12_T04_SAMSUNGFIRE_20241203_4B_VALUATION_POSITIONING_OVERHEAT | 000810 | Stage4B-overlay | 2024-12-03 | 2024-12-03 | 435000 | 0.0 | 0.0 | 0.0 | -18.05 | -18.05 | None | 2024-12-03 | 435000 | current_profile_4B_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger rows

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | below_entry_90D | peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000810 | 2024-02-02 | 299000 | 15.72 | -4.52 | 27.09 | -8.86 | 31.61 | -8.86 | True | 2024-12-03 / 435000 |
| 005830 | 2024-02-02 | 99200 | 10.89 | -8.17 | 16.33 | -13.1 | 21.67 | -13.1 | True | 2024-07-02 / 120700 |
| 001450 | 2024-02-02 | 35950 | 2.36 | -14.88 | 2.36 | -20.86 | 2.36 | -20.86 | True | 2024-02-05 / 36800 |

### Observed price row anchors

```text
000810 Samsung Fire:
- 2024-02-02 row: o=292000, h=301000, l=287500, c=299000.
- 2024-06-28 row: h=393500, 180D positive path high candidate.
- 2024-12-03 row: h=435000, full observed 2024 peak / 4B overlay candidate.

005830 DB Insurance:
- 2024-02-02 row: o=93900, h=99700, l=93800, c=99200.
- 2024-07-02 row: h=120700, 180D high candidate.
- 2024-04-19 row: l=86200, adverse excursion anchor.

001450 Hyundai Marine:
- 2024-02-02 row: o=35450, h=36350, l=34550, c=35950.
- 2024-02-05 row: h=36800, small local high candidate.
- 2024-04-15 row: l=28450, adverse excursion anchor.
- 2024-12-09 row: l=24750, 1Y adverse excursion anchor.
```

## 13. Current Calibrated Profile Stress Test

| case | current profile expected behavior | actual OHLC verdict | profile verdict | residual error |
| --- | --- | --- | --- | --- |
| 삼성화재 | Would likely wait for stronger revision/financial visibility before full Green. | High 180D MFE with controlled 90D MAE; clean positive. | current_profile_too_late | C22 verified CSM/K-ICS/capital-return proof should promote earlier. |
| DB손해보험 | Would treat as insurance/rate/value-up positive but with generic thresholds. | Positive, but 90D/180D MAE is materially larger than 삼성화재. | current_profile_too_late | Needs promotion plus high-MAE reserve-risk guard. |
| 현대해상 | Could be over-promoted if rate/value-up beta substitutes for CSM/reserve proof. | MFE_180D only 2.36%, MAE_180D -20.86%. | current_profile_false_positive | Rate-cycle beta without reserve/capital-return confirmation must be capped. |

Applied-axis stress test:

```text
stage2_actionable_evidence_bonus:
  kept but must be conditioned by C22-specific evidence quality.

stage3_yellow_total_min / green thresholds:
  kept globally; C22 needs a pre-threshold component cap when reserve risk is high.

price_only_blowoff_blocks_positive_stage:
  strengthened. Hyundai's price pop cannot create Stage3 evidence.

full_4b_requires_non_price_evidence:
  strengthened. Samsung Fire's 2024-12-03 peak is overlay only unless non-price valuation/positioning evidence is logged.

hard_4c_thesis_break_routes_to_4c:
  kept. Hyundai becomes 4C only if reserve/payout thesis evidence breaks, not merely because price falls.
```

## 14. Stage2 / Yellow / Green Comparison

Green lateness is meaningful only for the positive cases:

```text
삼성화재:
  Stage2 entry = 299000
  later Green proxy price ≈ 339000~345000
  full observed 2024 peak = 435000
  green_lateness_ratio = 0.42

DB손해보험:
  Stage2 entry = 99200
  later Green proxy price ≈ 110000
  full observed 2024 peak = 120700
  green_lateness_ratio = 0.50

현대해상:
  no confirmed Green trigger
  green_lateness_ratio = not_applicable
```

Interpretation: current Green strictness is reasonable globally, but C22 needs a verified evidence route that lets 삼성화재-like cases promote earlier while blocking 현대해상-like rate beta.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
| --- | --- | --- | --- | --- |
| R6L12_T01 삼성화재 Stage2 | 1.44 | 1.0 | valuation_blowoff|positioning_overheat | positive entry, later 4B overlay needed |
| R6L12_T02 DB손해보험 Stage2 | 0.88 | 1.0 | valuation_blowoff|positioning_overheat | watch after full-window peak |
| R6L12_T03 현대해상 false Stage2 | 1.0 | 1.0 | price_only|positioning_overheat | price-only local peak cannot promote positive stage |
| R6L12_T04 삼성화재 4B overlay | 1.44 | 1.0 | valuation_blowoff|positioning_overheat | 4B overlay only; not representative aggregate |

## 16. 4C Protection Audit

```text
현대해상:
  label = hard_4c_success_if_reserve_quality_break_logged
  reason = high MAE / tiny MFE path supports a reserve-risk guard, but hard 4C still requires thesis evidence broken.

삼성화재 and DB손해보험:
  label = thesis_break_watch_only
  reason = drawdowns after peak are overlays, not thesis breaks.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
candidate = L6 insurance-specific reserve-risk high-MAE guard

If an insurance row has rate-cycle / low-PBR / policy beta but lacks at least two of:
- verified IFRS17 CSM quality,
- K-ICS solvency buffer,
- explicit or highly visible capital return,
- low reserve-risk / claim-loss risk,
then Stage3-Yellow/Green promotion should be capped even if relative strength is strong.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE

Proposed C22 axes:
1. C22_verified_CSM_KICS_capital_return_bonus
2. C22_rate_cycle_beta_cap_without_reserve_quality
3. C22_reserve_risk_high_MAE_guard
4. C22_post_rerating_4B_positioning_overlay
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural | late_green | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 3 | 15.26 | -14.27 | 18.55 | -14.27 | 1/3 | 2 | 2 | mixed; positive cases too late and Hyundai false positive risk remains |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback | 3 | 15.26 | -14.27 | 18.55 | -14.27 | 1/3+ | 1 | 1 | worse false-positive control |
| P1_L6_insurance_sector_shadow_profile | sector_specific | C22_verified_CSM_KICS_capital_return_bonus; C22_reserve_risk_guard | 3 | 15.26 | -14.27 | 18.55 | -14.27 | 0/3 after guard | 0 | 0 | best alignment in this loop |
| P2_C22_archetype_shadow_profile | canonical_archetype_specific | C22_rate_cycle_not_enough; C22_verified_CSM_KICS_green_gate | 3 | 15.26 | -14.27 | 18.55 | -14.27 | 0/3 after guard | 0 | 0 | good; preferred coding scope |
| P3_C22_counterexample_guard_profile | counterexample_guard | reserve_quality_guard; price_only_4B_kept | 3 | 15.26 | -14.27 | 18.55 | -14.27 | 0/3 | 1 | 1 | safe but may under-promote DB-like cases |

## 20. Score-Return Alignment Matrix

| case | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202 | 81 | Stage3-Yellow | 88 | Stage3-Green-shadow | 27.09 | -8.86 | insurance_CSM_KICS_capital_return_rerating_captured_but_late |
| R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202 | 78 | Stage3-Yellow-low | 85 | Stage3-Yellow-high | 16.33 | -13.1 | insurance_capital_return_positive_but_needs_MAE_guard |
| R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202 | 76 | Stage3-Yellow_false | 58 | Stage2-Watch_or_blocked | 2.36 | -20.86 | rate_beta_false_positive_blocked_by_reserve_quality_guard |

Component mechanism:

```text
Positive C22:
  CSM/K-ICS quality + payout visibility acts like a bridge.
  It turns rate-cycle wind into durable equity rerating.

Counterexample C22:
  rate beta without reserve/payout proof is like a sail without a keel.
  It can move fast at first, but the first adverse wave creates high MAE.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN | 2 | 1 | 1 | 1 | 3 | 0 | 3 | 3 | 3 | True | True | C22 initial coverage filled; still needs life-insurer / reinsurance / reserve shock holdouts |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - insurance_verified_CSM_KICS_capital_return_too_late
  - rate_beta_false_positive_high_MAE
  - 4B_price_peak_needs_non_price_positioning_context
new_axis_proposed:
  - C22_verified_CSM_KICS_capital_return_bonus
  - C22_rate_cycle_beta_cap_without_reserve_quality
  - C22_reserve_risk_high_MAE_guard
  - C22_post_rerating_4B_positioning_overlay
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price-basis fields
- symbol profile availability and corporate-action window caveats
- representative entry rows in 2024 tradable shards
- 30D / 90D / 180D MFE and MAE approximated from actual stock-web OHLC rows
- same_entry_group dedupe
- C22 novelty versus local R6 loop 10/11 C21 files
```

Not validated:

```text
- production stock_agent scoring code
- live/current candidate ranking
- exact official disclosure URL enrichment for every evidence item
- adjusted-price comparison
- brokerage or order execution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_verified_CSM_KICS_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"삼성화재/DB손보 positive에서 CSM/K-ICS/자본환원 evidence가 price path와 정렬","positive cases promoted earlier; Hyundai guard unchanged","R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN|R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN",3,3,1,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_rate_cycle_beta_cap_without_reserve_quality,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"rate/value-up beta alone caused Hyundai false-positive high-MAE path","false positive blocked; avg MAE improves by excluding low-quality trigger","R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD",3,3,1,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C22_reserve_risk_high_MAE_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"reserve-risk and weak payout visibility explain high MAE differential inside same sector","protects against broad insurer beta over-promotion","R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD",3,3,1,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_post_rerating_4B_positioning_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"after strong CSM/capital-return rerating, full-window peak needs valuation/positioning overlay","4B overlay separated from positive entry; no price-only promotion","R6L12_T04_SAMSUNGFIRE_20241203_4B_VALUATION_POSITIONING_OVERHEAT",3,3,1,low,overlay_only,"not production; 4B overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"insurance_CSM_KICS_capital_return_rerating_captured_but_late","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Representative positive: clean 180D window; max 180D high approximated from stock-web 2024 rows at 393,500 and full observed 2024 peak at 435,000."}
{"row_type":"case","case_id":"R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"insurance_capital_return_positive_but_needs_MAE_guard","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Representative positive with higher drawdown: useful for reserve/MAE guard, not only promotion."}
{"row_type":"case","case_id":"R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202","symbol":"001450","company_name":"현대해상","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"rate_beta_false_positive_blocked_by_reserve_quality_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: insurer beta alone should not promote to C22 Green. Same entry group would have been over-scored if rate/value-up beta substituted for reserve/capital-return proof."}
{"row_type":"trigger","trigger_id":"R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN","case_id":"R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17 CSM K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":299000,"evidence_available_at_that_date":"IFRS17-era non-life insurer rerating where CSM/K-ICS quality, capital-return visibility and relative strength moved together rather than simple rate beta.","evidence_source":"source_proxy: 2024 low-PBR/value-up policy context + issuer IR/earnings evidence family; exact URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.72,"MFE_90D_pct":27.09,"MFE_180D_pct":31.61,"MFE_1Y_pct":45.48,"MFE_2Y_pct":null,"MAE_30D_pct":-4.52,"MAE_90D_pct":-8.86,"MAE_180D_pct":-8.86,"MAE_1Y_pct":-8.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-18.05,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":1.44,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_positioning_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_MFE_with_late_overheat","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202|2024-02-02|299000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN","case_id":"R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17 CSM K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":99200,"evidence_available_at_that_date":"Non-life insurer rerating with CSM/earnings visibility and shareholder-return optionality; upside persisted, but MAE was materially higher than 삼성화재.","evidence_source":"source_proxy: 2024 insurer value-up/IFRS17 earnings evidence family; exact URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.89,"MFE_90D_pct":16.33,"MFE_180D_pct":21.67,"MFE_1Y_pct":21.67,"MFE_2Y_pct":null,"MAE_30D_pct":-8.17,"MAE_90D_pct":-13.1,"MAE_180D_pct":-13.1,"MAE_1Y_pct":-13.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":120700,"drawdown_after_peak_pct":-17.73,"green_lateness_ratio":0.5,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positioning_4B_watch_after_full_window_peak","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_moderate_MFE_high_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202|2024-02-02|99200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD","case_id":"R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202","symbol":"001450","company_name":"현대해상","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17 CSM K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable_false","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":35950,"evidence_available_at_that_date":"Same insurer/value-up/rate-cycle beta produced an early price pop, but without enough reserve-quality / capital-return / CSM confirmation the path delivered tiny MFE and large MAE.","evidence_source":"source_proxy: same 2024 policy/rate-cycle evidence family; issuer-specific reserve and payout confirmation weaker than positive cases","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.36,"MFE_90D_pct":2.36,"MFE_180D_pct":2.36,"MFE_1Y_pct":2.36,"MFE_2Y_pct":null,"MAE_30D_pct":-14.88,"MAE_90D_pct":-20.86,"MAE_180D_pct":-20.86,"MAE_1Y_pct":-31.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":36800,"drawdown_after_peak_pct":-32.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_but_no_positive_stage","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_success_if_reserve_quality_break_logged","trigger_outcome_label":"false_positive_green_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202|2024-02-02|35950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_T04_SAMSUNGFIRE_20241203_4B_VALUATION_POSITIONING_OVERHEAT","case_id":"R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_KICS_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17 CSM K-ICS rate-cycle reserve/capital-return","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2024-12-03","entry_date":"2024-12-03","entry_price":435000,"evidence_available_at_that_date":"Full-window peak / valuation-positioning overlay after the earlier CSM/K-ICS capital-return rerating; this is risk overlay only, not a new positive entry.","evidence_source":"stock-web observed price peak + non-price valuation/positioning evidence should be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.05,"MAE_90D_pct":-18.05,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-18.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.44,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_positioning_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":false,"forward_window_trading_days":60,"calibration_block_reasons":["overlay_not_representative_entry","not_used_for_positive_weight_calibration"],"corporate_action_window_status":"clean_observed_window_no_recent_profile_action","same_entry_group_id":"R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202|2024-12-03|435000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_different_trigger_family_4B_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C22_000810_SAMSUNGFIRE_IFRS17_CSM_KICS_CAPITAL_RETURN_20240202","trigger_id":"R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":58,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":74,"valuation_repricing_score":78,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"ifrs17_csm_quality_score":76,"kics_capital_buffer_score":76,"reserve_risk_score":22,"shareholder_return_visibility_score":72,"rate_cycle_tailwind_score":62},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":66,"relative_strength_score":84,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":84,"execution_risk_score":24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6,"ifrs17_csm_quality_score":88,"kics_capital_buffer_score":86,"reserve_risk_score":18,"shareholder_return_visibility_score":84,"rate_cycle_tailwind_score":66},"weighted_score_after":88,"stage_label_after":"Stage3-Green-shadow","changed_components":["ifrs17_csm_quality_score","kics_capital_buffer_score","shareholder_return_visibility_score","reserve_risk_score"],"component_delta_explanation":"C22 shadow profile separates verified IFRS17/CSM/K-ICS/capital-return proof from generic rate-cycle or low-PBR beta.","MFE_90D_pct":27.09,"MAE_90D_pct":-8.86,"score_return_alignment_label":"insurance_CSM_KICS_capital_return_rerating_captured_but_late","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C22_005830_DBINSURANCE_IFRS17_CSM_CAPITALRETURN_20240202","trigger_id":"R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":54,"relative_strength_score":78,"customer_quality_score":0,"policy_or_regulatory_score":72,"valuation_repricing_score":74,"execution_risk_score":34,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"ifrs17_csm_quality_score":72,"kics_capital_buffer_score":72,"reserve_risk_score":34,"shareholder_return_visibility_score":68,"rate_cycle_tailwind_score":62},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow-low","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":62,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":76,"valuation_repricing_score":80,"execution_risk_score":32,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"ifrs17_csm_quality_score":82,"kics_capital_buffer_score":80,"reserve_risk_score":32,"shareholder_return_visibility_score":80,"rate_cycle_tailwind_score":66},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-high","changed_components":["ifrs17_csm_quality_score","kics_capital_buffer_score","shareholder_return_visibility_score","reserve_risk_score"],"component_delta_explanation":"C22 shadow profile separates verified IFRS17/CSM/K-ICS/capital-return proof from generic rate-cycle or low-PBR beta.","MFE_90D_pct":16.33,"MAE_90D_pct":-13.1,"score_return_alignment_label":"insurance_capital_return_positive_but_needs_MAE_guard","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C22_001450_HYUNDAIMARINE_RATE_BETA_RESERVE_RISK_FALSEPOSITIVE_20240202","trigger_id":"R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":74,"customer_quality_score":0,"policy_or_regulatory_score":72,"valuation_repricing_score":70,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20,"ifrs17_csm_quality_score":44,"kics_capital_buffer_score":52,"reserve_risk_score":64,"shareholder_return_visibility_score":36,"rate_cycle_tailwind_score":78},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":34,"relative_strength_score":42,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":44,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":24,"ifrs17_csm_quality_score":32,"kics_capital_buffer_score":44,"reserve_risk_score":78,"shareholder_return_visibility_score":24,"rate_cycle_tailwind_score":64},"weighted_score_after":58,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["rate_cycle_tailwind_score","reserve_risk_score","shareholder_return_visibility_score","ifrs17_csm_quality_score"],"component_delta_explanation":"C22 shadow profile separates verified IFRS17/CSM/K-ICS/capital-return proof from generic rate-cycle or low-PBR beta.","MFE_90D_pct":2.36,"MAE_90D_pct":-20.86,"score_return_alignment_label":"rate_beta_false_positive_blocked_by_reserve_quality_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["insurance_verified_CSM_KICS_capital_return_too_late","rate_beta_false_positive_high_MAE","4B_price_peak_needs_non_price_positioning_context"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R6
completed_loop = 12
next_round = R7
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv

Key stock-web files inspected:
- atlas/manifest.json
- atlas/symbol_profiles/000/000810.json
- atlas/symbol_profiles/005/005830.json
- atlas/symbol_profiles/001/001450.json
- atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv

Research-artifact duplicate check:
- local /mnt/data R6 loop 10 and loop 11 are C21, not C22.
```
