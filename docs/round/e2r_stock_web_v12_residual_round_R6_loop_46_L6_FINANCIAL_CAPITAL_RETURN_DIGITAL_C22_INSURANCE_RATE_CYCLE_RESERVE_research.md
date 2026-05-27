# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

- file_name: `e2r_stock_web_v12_residual_round_R6_loop_46_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md`
- round: `R6`
- loop: `46`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id: `INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY`
- loop_objective: `coverage_gap_fill`, `counterexample_mining`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `4B_non_price_requirement_stress_test`
- price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated_proxy`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`

This file is historical calibration research only. It is not a live watchlist, not a current stock recommendation, not a repository patch, and not a production scoring change.

## 1. Current Calibrated Profile Assumption

The current proxy profile already includes the first Stock-Web calibrated global axes:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove those global axes. It stress-tests them inside insurance/reserve-cycle cases and proposes C22-specific shadow handling where the general value-up logic can be too permissive.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY
sector = financials / insurance / value-up / IFRS17 reserve quality
primary_archetype = Insurance ROE-PBR re-rating with reserve-quality gate
```

C22 is close to C21 but should not be scored as a simple bank/value-up analogue. For banks, capital return and ROE/PBR discount can often close the Stage2 bridge. For insurers, the same bridge is noisier because reported IFRS17 earnings, CSM growth, actuarial assumption changes, loss ratio normalization, K-ICS capital, and reserve adequacy can split a “cheap value-up” candidate into either durable re-rating or fast mean reversion.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were used only for coverage/duplication screening. A direct repository search for the exact C22 insurance archetype plus the selected symbols returned no matching prior research rows:

```text
query = C22_INSURANCE_RATE_CYCLE_RESERVE 삼성화재 DB손해보험 현대해상
result = no direct matches
```

The current calibrated profile report confirms the applied global axes but does not add C22-specific insurance reserve gates. Therefore this loop is not a schema-rematerialization loop and does not reuse the prior R6/C21 bank/value-up cases.

Duplicate avoidance status:

| check | result |
|---|---:|
| same symbol + same trigger_date + same entry_date reused | 0 |
| same canonical_archetype repeated | no; C22 selected after prior C21 bank loop |
| new symbol count | 3 |
| new trigger family count | 4 |
| counterexample included | yes |
| 4B/4C path included | yes, overlay/protection only |

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web atlas manifest was read for this loop.

| field | value |
|---|---|
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
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Price-source rule used in this loop:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

The selected windows are 2024-02 through 2025-04. All profile corporate-action candidate dates for the three selected symbols are historical and outside the tested 2024-2025 windows. Therefore 30D/90D/180D calibration windows are treated as clean.

## 5. Historical Eligibility Gate

| case_id | symbol | company | profile_path | 180D forward window | corporate-action status | calibration_usable |
|---|---:|---|---|---|---|---:|
| R6L46-C22-SFM-000810 | 000810 | 삼성화재 | atlas/symbol_profiles/000/000810.json | available | candidate dates 1999-02-01, 1999-07-05, 2000-02-15; no overlap | true |
| R6L46-C22-DBI-005830 | 005830 | DB손해보험 | atlas/symbol_profiles/005/005830.json | available | candidate date 1999-07-20; no overlap | true |
| R6L46-C22-HIM-001450 | 001450 | 현대해상 | atlas/symbol_profiles/001/001450.json | available | candidate date 2004-07-13; no overlap | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compressed interpretation |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY | Insurance re-rating needs more than policy value-up or low PBR. Durable Stage2/Stage3 requires explicit capital-return path plus IFRS17 earnings/CSM/reserve-quality confirmation. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_VALUEUP_POLICY_ONLY_FALSE_POSITIVE | Policy value-up alone can produce a short MFE but may fail to protect 90D/180D drawdown when reserve quality, loss ratio, or financial visibility is weak. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_PRICE_ONLY_LOCAL_4B | Price peaks in insurance are often local and not sufficient for full 4B unless valuation, capital-return disappointment, loss-ratio deterioration, or reserve evidence appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | entry_date | entry_price | reason selected |
|---|---:|---|---|---|---|---:|---|
| R6L46-C22-SFM-000810 | 000810 | 삼성화재 | structural_success | Stage2-Actionable, 2024-02-26 | 2024-02-26 | 300000 | Value-up optionality plus high-quality non-life insurer balance sheet produced clean 90D/180D upside; Stage3 confirmation later did not fully miss upside. |
| R6L46-C22-DBI-005830 | 005830 | DB손해보험 | structural_success / high_mae_success | Stage2-Actionable, 2024-02-26 | 2024-02-26 | 95000 | Similar insurance value-up route; strong 90D/180D MFE but with wider drawdown and sharper 2025 pullback, useful for reserve/capital-return guard. |
| R6L46-C22-HIM-001450 | 001450 | 현대해상 | failed_rerating / false_positive_green | Stage3-Yellow/false-positive, 2024-05-14 | 2024-05-14 | 34200 | One-day earnings/insurance rerating spike did not create durable 180D trend; later 4C-like protection trigger was needed. |

## 8. Positive vs Counterexample Balance

| count type | value |
|---|---:|
| calibration_usable_case_count | 3 |
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 4 |

The balance is sufficient for a C22-specific low-confidence shadow rule candidate, not for a global production delta.

## 9. Evidence Source Map

| evidence family | evidence date | source description | stage usage |
|---|---|---|---|
| Corporate Value-up Programme | 2024-02-26 | Korea value-up policy package / public market event; voluntary improvement plans, capital efficiency, shareholder return focus | Stage2 policy_or_regulatory_optionality only |
| Additional corporate value-up incentives | 2024-04-02 | Public regulator follow-up on incentives including exchange fee exemptions and dividend-rule reforms | Stage2/Stage3 support, not enough alone |
| Value-up guidelines | 2024-05-02 | Voluntary guidelines for corporate value enhancement; annual plan disclosure framework | Stage2 support; not a Green trigger by itself |
| Insurance quarterly results / IFRS17 confirmation | 2024-05-14 range | Company financial-result event family for insurers; used as confirmed financial-visibility checkpoint | Stage3-Yellow/Green candidate |
| Reserve/loss-ratio/quality deterioration | 2024-Q3 to 2024-Q4 path | Insurance-specific deterioration / market repricing route; inferred from price confirmation and reserve-quality thesis risk, not a positive entry weight | 4C protection/watch only |

Important interpretation: policy value-up is a gate opener, not a standalone Green signal. For C22, Stage3 should require explicit capital-return bridge and reserve-quality/CSM/financial visibility. This is the core residual contribution.

## 10. Price Data Source Map

| symbol | tradable_shard_2024 | tradable_shard_2025 | profile_path |
|---:|---|---|---|
| 000810 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv | atlas/symbol_profiles/000/000810.json |
| 005830 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv | atlas/symbol_profiles/005/005830.json |
| 001450 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv | atlas/symbol_profiles/001/001450.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence_fields | current_profile_verdict | aggregate_role |
|---|---|---|---|---|---:|---|---|---|
| R6L46-T001 | R6L46-C22-SFM-000810 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 300000 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | current_profile_correct | representative |
| R6L46-T002 | R6L46-C22-SFM-000810 | Stage3-Green | 2024-05-14 | 2024-05-14 | 336500 | confirmed_revision, financial_visibility, low_red_team_risk | current_profile_correct | label_comparison_only |
| R6L46-T003 | R6L46-C22-DBI-005830 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 95000 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | current_profile_correct | representative |
| R6L46-T004 | R6L46-C22-DBI-005830 | Stage3-Green | 2024-05-14 | 2024-05-14 | 104100 | confirmed_revision, financial_visibility, capital_return_visibility | current_profile_too_late | label_comparison_only |
| R6L46-T005 | R6L46-C22-HIM-001450 | Stage3-Yellow false-positive | 2024-05-14 | 2024-05-14 | 34200 | confirmed_revision, financial_visibility, reserve_quality_unknown | current_profile_false_positive | representative |
| R6L46-T006 | R6L46-C22-SFM-000810 | 4B overlay | 2024-12-03 | 2024-12-03 | 435000 | price_only_local_peak, valuation_blowoff_watch | current_profile_4B_too_early | 4B_overlay_only |
| R6L46-T007 | R6L46-C22-HIM-001450 | 4C protection | 2024-10-02 | 2024-10-02 | 30950 | thesis_evidence_broken, reserve_quality_watch, forced_derating_path | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | symbol | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | MFE_1Y_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| R6L46-T001 | 000810 | 300000 | 15.33 | -4.83 | 31.17 | -9.17 | 31.17 | -9.17 | 45.00 | -9.17 | 2024-12-03 | 435000 | -17.82 | true |
| R6L46-T003 | 005830 | 95000 | 15.79 | -4.11 | 27.05 | -8.95 | 30.53 | -8.95 | 30.53 | -8.95 | 2024-08-22 | 124000 | -26.21 | true |
| R6L46-T005 | 001450 | 34200 | 2.34 | -9.36 | 7.46 | -9.36 | 7.46 | -29.97 | 7.46 | -41.37 | 2024-07-31 | 36750 | -45.44 | true |

### Label comparison and overlay triggers

| trigger_id | symbol | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | green_lateness_ratio | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R6L46-T002 | 000810 | 336500 | 12.93 | -3.71 | 16.94 | -3.71 | 29.27 | -3.71 | 0.39 | null | null | Green not disastrously late, but not earliest risk/reward point. |
| R6L46-T004 | 005830 | 104100 | 9.70 | -1.92 | 19.12 | -7.68 | 19.12 | -12.10 | 0.31 | null | null | Green captured less upside than Stage2 but remained acceptable. |
| R6L46-T006 | 000810 | 435000 | 0.00 | -16.32 | 0.00 | -21.84 | not_applicable | not_applicable | not_applicable | 1.00 | 1.00 | Price-only local peak: do not train positive entry; full 4B requires non-price evidence. |
| R6L46-T007 | 001450 | 30950 | 3.39 | -11.95 | 3.39 | -20.68 | 3.39 | -34.73 | not_applicable | null | null | 4C protection/watch trigger would have reduced later drawdown, but is not a positive scoring row. |

Notes:

- MFE/MAE values are computed from stock-web tradable raw OHLC rows observed in the cited 2024-2025 shards.
- 1Y values are included for context but the calibration decision uses 30D/90D/180D only.
- 2Y fields are left `null` in machine-readable rows because the loop does not use 2Y training and manifest max_date limits full two-year confirmation for later triggers.

## 13. Current Calibrated Profile Stress Test

### 삼성화재 / 000810

The current calibrated profile would likely admit 2024-02-26 as Stage2-Actionable, not Green, because the policy value-up catalyst was public but company-level confirmed revision and reserve-quality confirmation were not yet fully closed. This was correct: 30D MFE was +15.33% with limited -4.83% MAE; 90D/180D MFE expanded to +31.17%. The 2024-05-14 Green checkpoint was not fatal, with a green_lateness_ratio of 0.39 against the 180D peak route.

Verdict: `current_profile_correct`.

### DB손해보험 / 005830

The current profile would likely admit 2024-02-26 as Stage2-Actionable and 2024-05-14 as Green candidate after financial visibility improved. That was mostly correct but shows a C22-specific nuance: Stage3-Green still entered after a large part of early upside had begun. Stage2 entry produced +30.53% 180D MFE. Green comparison produced +19.12% 90D/180D MFE, but later reserve/capital-return worries pulled the name back. The current profile is not wrong, but C22 should explicitly require reserve-quality and capital-return durability to avoid over-scoring the Green row.

Verdict: `current_profile_too_late` for Green timing, `current_profile_correct` for Stage2.

### 현대해상 / 001450

The current profile could over-score a post-earnings/insurance-value-up bounce if it treats the 2024-05-14 spike as a conventional insurance Green. That would be a residual false positive. The 30D MFE was only +2.34%, 90D MFE +7.46%, and 180D MAE -29.97%. The 4C-like protection trigger around 2024-10-02 would not be a positive signal; it is a risk route that protects from further derating.

Verdict: `current_profile_false_positive` and `current_profile_4C_too_late`.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3 entry | peak basis | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 삼성화재 | 300000 | 336500 | 393500 | 0.39 | Green was somewhat late but still before a meaningful part of the move. |
| DB손해보험 | 95000 | 104100 | 124000 | 0.31 | Green was acceptable but less efficient than Stage2. |
| 현대해상 | not selected as positive Stage2 | 34200 | 36750 | not_valid_for_positive | Stage3-like label was a false positive because reserve/quality bridge did not close. |

C22 lesson: Stage2 should open on policy + insurance value-up sensitivity only when low-PBR/ROE/capital-return bridge is present. Stage3-Green should require reserve-quality/CSM/earnings-visibility confirmation. Without that, a price spike is a trapdoor, not a staircase.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | timing verdict |
|---|---:|---|---:|---:|---|
| R6L46-T006 | 000810 | price_only, valuation_blowoff_watch | 1.00 | 1.00 | Good local price peak, but price-only. Treat as 4B overlay watch, not full 4B unless valuation/capital-return disappointment or reserve data confirms. |
| R6L46-T004 context | 005830 | price_only, positioning_overheat | 0.97 | 0.97 | Local price peak near 2024-08-20/22 was useful as risk overlay, but the later derating shows why it should not train positive or global 4B. |

Existing axis tested: `full_4b_requires_non_price_evidence`.

Result: `existing_axis_strengthened`.

## 16. 4C Protection Audit

| trigger_id | symbol | 4C date | 4C entry | MAE_90D_after_4C | prior peak | max_drawdown_after_peak_from_prior_stage | four_c_protection_label |
|---|---:|---|---:|---:|---:|---:|---|
| R6L46-T007 | 001450 | 2024-10-02 | 30950 | -20.68 | 36750 | -45.44 | hard_4c_success |

The 4C row should not train positive weights. It is a protection row: once a C22 candidate fails to maintain reserve/earnings/capital-return credibility and breaks below the prior value-up entry group, the evidence routes to 4C or thesis-break watch.

## 17. Sector-Specific Rule Candidate

```text
rule_id = L6_C22_INSURANCE_RESERVE_QUALITY_GREEN_GATE
rule_scope = canonical_archetype_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
proposal_type = shadow_only
```

Proposed rule:

```text
For C22 insurance names, policy value-up optionality can create Stage2-Actionable only when at least one of the following non-price anchors is present:
1. explicit capital-return or dividend/buyback path,
2. IFRS17 earnings/CSM/financial visibility confirmation,
3. capital adequacy / K-ICS / reserve-quality confidence,
4. persistent relative strength versus the insurance peer basket.

Stage3-Green requires at least two anchors, and one must be confirmed financial visibility or explicit capital-return bridge. Policy-only + price momentum cannot be Green.
```

Backtest support:

- Positive: 삼성화재 and DB손해보험 had clean Stage2 MFE profiles.
- Counterexample: 현대해상 post-earnings spike had poor 180D alignment.
- 4B/4C: price-only peaks were useful as risk overlays but not as full 4B without non-price confirmation.

Confidence: `medium_low` because usable case count is 3. Direction is useful as a shadow rule but not enough for a global delta.

## 18. Canonical-Archetype Rule Candidate

```text
axis = C22_reserve_quality_required_for_green
baseline_value = 0
shadow_tested_value = 1
scope = canonical_archetype_specific
```

Candidate effect:

- Reduces false-positive Green on insurance names whose value-up narrative lacks reserve-quality and capital-return confirmation.
- Preserves Stage2-Actionable entries for high-quality insurers when public policy optionality and relative strength appear early.
- Keeps 4B/4C rows out of positive-entry training.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | 3 | T001, T003, T005 | 21.89 | -9.16 | 23.05 | -16.03 | 0.33 | 1 | acceptable but C22 false-positive remains |
| P0b_e2r_2_0_baseline_reference | baseline rollback | 3 | likely later Green rows | 14.67 | -7.55 | 18.86 | -15.26 | 0.33 | 2 | worse timing, misses early Stage2 capture |
| P1_L6_sector_specific_candidate_profile | L6 sector shadow | 3 | T001, T003, T005 blocked-to-watch | 29.11 | -9.06 | 30.85 | -9.06 | 0.00 | 1 | better false-positive control |
| P2_C22_archetype_candidate_profile | C22 canonical shadow | 3 | T001, T003, HIM narrative-only | 29.11 | -9.06 | 30.85 | -9.06 | 0.00 | 1 | best alignment in this small sample |
| P3_counterexample_guard_profile | C22 guard | 3 | T001, T003; T005 blocked | 29.11 | -9.06 | 30.85 | -9.06 | 0.00 | 1 | keeps protection logic separated from entries |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment label |
|---|---:|---|---:|---|---:|---:|---|
| R6L46-T001 | 76 | Stage2-Actionable | 79 | Stage2-Actionable | 31.17 | -9.17 | aligned_positive_stage2 |
| R6L46-T002 | 88 | Stage3-Green | 89 | Stage3-Green | 16.94 | -3.71 | aligned_but_later_than_stage2 |
| R6L46-T003 | 75 | Stage2-Actionable | 78 | Stage2-Actionable | 27.05 | -8.95 | aligned_positive_stage2 |
| R6L46-T004 | 87 | Stage3-Green | 88 | Stage3-Green | 19.12 | -7.68 | aligned_but_later_than_stage2 |
| R6L46-T005 | 80 | Stage3-Yellow | 64 | Watch / blocked from Green | 7.46 | -9.36 | false_positive_reduced |
| R6L46-T006 | 4B overlay | 4B watch | 4B overlay | 4B watch | 0.00 | -21.84 | risk_overlay_only |
| R6L46-T007 | 4C watch | 4C watch | 4C watch | 4C watch | 3.39 | -20.68 | protection_only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY | 2 | 1 | 2 | 1 | 3 | 0 | 7 | 3 | 2 | true | true | Still needs life-insurer and reinsurance holdout cases; C22 rule direction established but not global. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [insurance_policy_only_false_positive, green_without_reserve_quality_risk, price_only_local_4B_watch_not_full_4B]
new_axis_proposed: C22_reserve_quality_required_for_green; C22_policy_only_valueup_stage2_cap; C22_4C_reserve_quality_break_watch
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c; price_only_blowoff_blocks_positive_stage
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R6/C22 insurance reserve-quality Green gate and policy-only false-positive gap
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and shard roots.
- 2024-2025 tradable OHLC rows for selected symbols.
- Symbol profiles and corporate-action candidate dates.
- 30D/90D/180D MFE/MAE direction and relative profile alignment.
- C22-specific positive/counterexample split.
```

Not validated:

```text
- No stock_agent src/e2r code was opened.
- No production scoring code was modified.
- No live 2026 candidate scan was performed.
- No brokerage or auto-trading integration was touched.
- Company-level accounting details are not used as production-grade fundamentals; they are trigger-family labels for historical calibration.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_reserve_quality_required_for_green,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 Green should require reserve-quality/financial-visibility bridge, not policy-only value-up.","Blocks Hyundai false-positive while preserving Samsung Fire/DB Stage2 positives.","R6L46-T001|R6L46-T003|R6L46-T005",3,3,1,medium_low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_policy_only_valueup_stage2_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Policy value-up can open Stage2 but should cap before Green without explicit capital return or IFRS17 financial confirmation.","Reduces policy-only false Green risk.","R6L46-T005",1,1,1,low,canonical_shadow_only,"watch/blocked route"
shadow_weight,C22_4C_reserve_quality_break_watch,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Reserve-quality/loss-ratio thesis break should route to protection/watch, not positive entry training.","Protects from Hyundai drawdown path after 2024-10 break.","R6L46-T007",1,1,1,low,canonical_shadow_only,"4C only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L46-C22-SFM-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L46-T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive Stage2 aligned with 30D/90D/180D MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"High-quality insurance value-up case; Green not earliest but acceptable."}
{"row_type":"case","case_id":"R6L46-C22-DBI-005830","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R6L46-T003","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 captured 90D/180D upside but later pullback supports reserve-quality gate","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive but with guardrail value."}
{"row_type":"case","case_id":"R6L46-C22-HIM-001450","symbol":"001450","company_name":"현대해상","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_POLICY_ONLY_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L46-T005","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Weak MFE and large 180D MAE; Green should be blocked without reserve-quality bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C22 counterexample for policy/earnings-spike overpromotion."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L46-T001","case_id":"R6L46-C22-SFM-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"insurance","primary_archetype":"Insurance ROE/PBR capital return with reserve-quality gate","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate value-up policy optionality plus insurance relative strength; company-level Green confirmation not yet complete.","evidence_source":"Korea corporate value-up public event; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":300000,"MFE_30D_pct":15.33,"MFE_90D_pct":31.17,"MFE_180D_pct":31.17,"MFE_1Y_pct":45.0,"MFE_2Y_pct":null,"MAE_30D_pct":-4.83,"MAE_90D_pct":-9.17,"MAE_180D_pct":-9.17,"MAE_1Y_pct":-9.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-17.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L46-EG-000810-20240226-300000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L46-T002","case_id":"R6L46-C22-SFM-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"insurance","primary_archetype":"Insurance ROE/PBR capital return with reserve-quality gate","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-14","evidence_available_at_that_date":"Insurance earnings/financial visibility confirmation event family; still must be checked against Stage2 earlier entry.","evidence_source":"company quarterly result event family; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":336500,"MFE_30D_pct":12.93,"MFE_90D_pct":16.94,"MFE_180D_pct":29.27,"MFE_1Y_pct":27.04,"MFE_2Y_pct":null,"MAE_30D_pct":-3.71,"MAE_90D_pct":-3.71,"MAE_180D_pct":-3.71,"MAE_1Y_pct":-3.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-17.82,"green_lateness_ratio":0.39,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_acceptable_but_later_than_stage2","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L46-EG-000810-20240514-336500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L46-T003","case_id":"R6L46-C22-DBI-005830","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"insurance","primary_archetype":"Insurance ROE/PBR capital return with reserve-quality gate","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate value-up policy optionality and insurance relative strength; company-specific Green not yet confirmed.","evidence_source":"Korea corporate value-up public event; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":95000,"MFE_30D_pct":15.79,"MFE_90D_pct":27.05,"MFE_180D_pct":30.53,"MFE_1Y_pct":30.53,"MFE_2Y_pct":null,"MAE_30D_pct":-4.11,"MAE_90D_pct":-8.95,"MAE_180D_pct":-8.95,"MAE_1Y_pct":-8.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-26.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L46-EG-005830-20240226-95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L46-T004","case_id":"R6L46-C22-DBI-005830","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"insurance","primary_archetype":"Insurance ROE/PBR capital return with reserve-quality gate","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-14","evidence_available_at_that_date":"Company result/financial visibility event family; used as Green comparison against earlier Stage2.","evidence_source":"company quarterly result event family; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","capital_return_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":104100,"MFE_30D_pct":9.70,"MFE_90D_pct":19.12,"MFE_180D_pct":19.12,"MFE_1Y_pct":19.12,"MFE_2Y_pct":null,"MAE_30D_pct":-1.92,"MAE_90D_pct":-7.68,"MAE_180D_pct":-12.10,"MAE_1Y_pct":-22.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-26.21,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_acceptable_but_later_than_stage2","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L46-EG-005830-20240514-104100","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L46-T005","case_id":"R6L46-C22-HIM-001450","symbol":"001450","company_name":"현대해상","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_POLICY_ONLY_FALSE_POSITIVE","sector":"insurance","primary_archetype":"Insurance policy-only false-positive guard","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage3-Yellow false-positive","trigger_date":"2024-05-14","evidence_available_at_that_date":"Post-earnings insurance rerating spike; reserve-quality and durable capital-return bridge not sufficiently confirmed.","evidence_source":"company quarterly result event family; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":34200,"MFE_30D_pct":2.34,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MFE_1Y_pct":7.46,"MFE_2Y_pct":null,"MAE_30D_pct":-9.36,"MAE_90D_pct":-9.36,"MAE_180D_pct":-29.97,"MAE_1Y_pct":-41.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-45.44,"green_lateness_ratio":"not_valid_for_positive","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L46-EG-001450-20240514-34200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L46-T006","case_id":"R6L46-C22-SFM-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_PRICE_ONLY_LOCAL_4B","sector":"insurance","primary_archetype":"Insurance price-only 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B overlay","trigger_date":"2024-12-03","evidence_available_at_that_date":"Observed local/full window price peak; no standalone non-price 4B evidence used in this loop.","evidence_source":"stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-03","entry_price":435000,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.32,"MAE_90D_pct":-21.84,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-17.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success_watch_only","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_90D_window","same_entry_group_id":"R6L46-EG-000810-20241203-435000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_timing_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L46-T007","case_id":"R6L46-C22-HIM-001450","symbol":"001450","company_name":"현대해상","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_4C_RESERVE_QUALITY_BREAK","sector":"insurance","primary_archetype":"Insurance reserve-quality 4C protection","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C protection","trigger_date":"2024-10-02","evidence_available_at_that_date":"Break below prior value-up/earnings entry group with reserve-quality/loss-ratio thesis risk; protection row only.","evidence_source":"stock-web OHLC plus insurance reserve-quality thesis-break path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-02","entry_price":30950,"MFE_30D_pct":3.39,"MFE_90D_pct":3.39,"MFE_180D_pct":3.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.95,"MAE_90D_pct":-20.68,"MAE_180D_pct":-34.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-14","peak_price":32000,"drawdown_after_peak_pct":-37.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success_protection_only","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L46-EG-001450-20241002-30950","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4C_timing_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L46-C22-SFM-000810","trigger_id":"R6L46-T001","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":42,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":68,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"roe_pbr_capital_return_score":70,"reserve_quality_score":"unknown_or_not_supported"},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":42,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":68,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"roe_pbr_capital_return_score":74,"reserve_quality_score":55},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["roe_pbr_capital_return_score","reserve_quality_score"],"component_delta_explanation":"C22 Stage2 accepts policy plus relative strength, but reserve quality is still not a Green gate until confirmed.","MFE_90D_pct":31.17,"MAE_90D_pct":-9.17,"score_return_alignment_label":"aligned_positive_stage2","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L46-C22-DBI-005830","trigger_id":"R6L46-T003","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":40,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":70,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12,"roe_pbr_capital_return_score":72,"reserve_quality_score":"unknown_or_not_supported"},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":40,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":70,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12,"roe_pbr_capital_return_score":75,"reserve_quality_score":52},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["roe_pbr_capital_return_score","reserve_quality_score"],"component_delta_explanation":"Positive Stage2, but later drawdown means reserve quality should gate Green rather than Stage2.","MFE_90D_pct":27.05,"MAE_90D_pct":-8.95,"score_return_alignment_label":"aligned_positive_stage2","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L46-C22-HIM-001450","trigger_id":"R6L46-T005","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":46,"relative_strength_score":40,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":62,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":35,"roe_pbr_capital_return_score":50,"reserve_quality_score":"unknown_or_not_supported"},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":38,"relative_strength_score":35,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":52,"execution_risk_score":68,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":50,"roe_pbr_capital_return_score":38,"reserve_quality_score":25},"weighted_score_after":64,"stage_label_after":"Watch / blocked_from_Green","changed_components":["revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score","roe_pbr_capital_return_score","reserve_quality_score"],"component_delta_explanation":"C22 Green blocked because reserve-quality and capital-return bridge did not close; 180D MAE dominates MFE.","MFE_90D_pct":7.46,"MAE_90D_pct":-9.36,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"46","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["insurance_policy_only_false_positive","green_without_reserve_quality_risk","price_only_local_4B_watch_not_full_4B"],"diversity_score_summary":"high: 3 new symbols, new C22 canonical coverage, one counterexample, one 4C path","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R6/C22 insurance reserve-quality Green gate and policy-only false-positive gap"}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L46-C22-LIFE-HOLDOUT","symbol":"088350","company_name":"한화생명","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"life-insurer holdout needed; not included in this quantitative loop to avoid mixing CSM/reserve route with non-life cases before separate validation","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

Recommended next loops:

```text
next_round_candidate_1 = R6 / C22 / life-insurer holdout / 한화생명, 삼성생명, 미래에셋생명
next_round_candidate_2 = R6 / C21-C22 cross validation / bank vs insurer value-up gate contrast
next_round_candidate_3 = R10 / C30 / PF balance-sheet break holdout if sector balance is needed
```

The best continuation is C22 life-insurer holdout because this loop intentionally focused on non-life insurers and reserve-quality/IFRS17 bridge. Life insurers may need a separate interest-rate sensitivity and CSM-duration rule.

## 28. Source Notes

Stock-Web files inspected:

```text
atlas/manifest.json
atlas/symbol_profiles/000/000810.json
atlas/symbol_profiles/005/005830.json
atlas/symbol_profiles/001/001450.json
atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv
atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv
atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv
```

stock_agent research artifacts inspected only for coverage/duplication:

```text
reports/e2r_calibration/calibrated_profile_report.md
data/e2r/calibration/md_registry.jsonl
repository search query: C22_INSURANCE_RATE_CYCLE_RESERVE 삼성화재 DB손해보험 현대해상
```

Public event sources used as trigger-family context:

```text
2024-02-26 Korea Corporate Value-up Programme public announcement / market event
2024-04-02 follow-up incentive framework
2024-05-02 voluntary value-up guidelines
2024-05-14 insurance quarterly earnings event family
```
