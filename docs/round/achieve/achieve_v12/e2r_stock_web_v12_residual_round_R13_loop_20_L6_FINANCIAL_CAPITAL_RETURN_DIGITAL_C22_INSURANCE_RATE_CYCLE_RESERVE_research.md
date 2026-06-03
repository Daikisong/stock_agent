# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 20
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_RESERVE_QUALITY_CAPITAL_RETURN_HOLDOUT
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This is not live candidate research and not a repository patch. It is a historical residual calibration file using stock-web OHLC rows only for price validation.

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

The loop does not re-propose the global calibrated axes. It stress-tests them inside the insurance reserve/rate-cycle archetype and proposes only C22/L6 shadow candidates.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 20
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetypes =
  - P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY
  - P_AND_C_RESERVE_RISK_COUNTEREXAMPLE
  - LIFE_INSURER_RATE_BETA_WITH_CAPITAL_QUALITY_GAP
loop_objective =
  - holdout_validation
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - coverage_gap_fill
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

The previous generated L6 residual file covered C21 brokerage/capital-return behavior. This loop moves to C22 insurance rate/reserve/capital-return behavior and uses four new symbols:

```text
new_symbols = 000810, 005830, 001450, 088350
reused_case_count = 0
new_independent_case_ratio = 1.00
required_new_independent_case_ratio = 0.60
loop_contribution_label = canonical_archetype_rule_candidate
```

No stock_agent `src/e2r` files were opened. The only repository inspected for price was `Songdaiki/stock-web`.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest used in this loop declares:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

The manifest notes that the data is raw/unadjusted OHLC, zero-volume and invalid OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows should be blocked by default.

### Symbol profile validation

| symbol | company | profile_path | first_date | last_date | trading_days | CA candidates | CA dates | 2024 180D window |
|---:|---|---|---|---|---:|---:|---|---|
| 000810 | 삼성화재 | atlas/symbol_profiles/000/000810.json | 1995-05-02 | 2026-02-20 | 7763 | 3 | 1999-02-01, 1999-07-05, 2000-02-15 | clean; no overlap with 2024 entry→D+180 |
| 005830 | DB손해보험 | atlas/symbol_profiles/005/005830.json | 1995-05-02 | 2026-02-20 | 7762 | 1 | 1999-07-20 | clean; no overlap with 2024 entry→D+180 |
| 001450 | 현대해상 | atlas/symbol_profiles/001/001450.json | 1995-05-02 | 2026-02-20 | 7761 | 1 | 2004-07-13 | clean; no overlap with 2024 entry→D+180 |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | 2010-03-17 | 2026-02-20 | 3922 | 0 | none | clean; no overlap with 2024 entry→D+180 |

## 5. Historical Eligibility Gate

All representative Stage2-Actionable triggers satisfy:

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
entry_date + 180 trading days exists by stock-web manifest/profile max_date = true
high / low / close / volume available = true
MFE_30D / 90D / 180D and MAE_30D / 90D / 180D calculated = true
corporate_action_contaminated_180D_window = false
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

The 1Y/2Y columns are retained in machine-readable rows as `null` because this loop calibrates only 30D/90D/180D and 4B/4C overlays. This avoids mixing partial 2025/2026 windows into the core 180D residual calibration.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | scoring interpretation |
|---|---|---|
| P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY | C22_INSURANCE_RATE_CYCLE_RESERVE | P&C insurers where reserve quality, ROE, and shareholder-return visibility make low-PBR/value-up rerating durable. |
| P_AND_C_RESERVE_RISK_COUNTEREXAMPLE | C22_INSURANCE_RATE_CYCLE_RESERVE | P&C insurer with same policy/rerating beta but insufficient reserve/loss-ratio quality, causing false positive risk. |
| LIFE_INSURER_RATE_BETA_WITH_CAPITAL_QUALITY_GAP | C22_INSURANCE_RATE_CYCLE_RESERVE | Life insurer where rate/value-up beta is visible but capital-return and durable revision evidence are insufficient. |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| R13L20_C22_000810 | 000810 | 삼성화재 | structural_success / positive | 308,500 | 27.55 | -11.67 | 27.55 | -11.67 | current_profile_too_late |
| R13L20_C22_005830 | 005830 | DB손해보험 | structural_success / positive | 97,800 | 23.42 | -11.55 | 26.79 | -11.55 | current_profile_too_late |
| R13L20_C22_001450 | 001450 | 현대해상 | failed_rerating / counterexample | 34,650 | 3.46 | -17.17 | 6.06 | -21.36 | current_profile_false_positive |
| R13L20_C22_088350 | 088350 | 한화생명 | false_positive_green / counterexample | 3,385 | 3.84 | -23.63 | 3.84 | -24.52 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 4
minimum_calibration_usable_case_count = 4
calibration_usable_representative_trigger_count = 4
calibration_usable_total_trigger_count = 6
```

Interpretation: C22 cannot be scored as a plain “financial low-PBR + ROE” bucket. In insurance, the same policy wind can lift the whole sea, but only vessels with reserve quality and shareholder-return ballast keep sailing. The counterexamples show the hull cracking once reserve/loss-ratio or capital-return visibility is missing.

## 9. Evidence Source Map

| symbol | evidence route at trigger | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---:|---|---|---|---|
| 000810 | FY2023/early-2024 P&C earnings visibility + value-up/low-PBR backdrop + capital-return expectation | policy/regulatory optionality, early revision, relative strength | financial visibility, low red-team risk | local price blowoff stress-tested but not full 4B without non-price evidence |
| 005830 | FY2023/early-2024 P&C earnings visibility + value-up/low-PBR backdrop + capital-return expectation | policy/regulatory optionality, early revision, relative strength | financial visibility, low red-team risk | local price blowoff stress-tested but not full 4B without non-price evidence |
| 001450 | same policy/value-up window but weaker durable repricing | policy beta, relative strength | weak/insufficient | later reserve/loss-ratio pressure; hard 4C route useful |
| 088350 | value-up/rate-sensitive life-insurer beta without capital-return proof | policy beta, relative strength | absent/insufficient | value-up beta faded; hard 4C late but protective |

Evidence timing rule: exact intraday versus after-close disclosure timestamps were not guaranteed by this loop, so representative entries use next-trading-day close after the 2024-02-22 trigger date.

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | stock_web_manifest_max_date | basis | adjustment |
|---:|---|---|---|---|---|
| 000810 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 005830 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 001450 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/symbol_profiles/001/001450.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 088350 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak | group_role |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R13L20_C22_000810_S2A_20240222 | Stage2-Actionable | 000810 | 2024-02-23 | 308,500 | 12.16 | -7.46 | 27.55 | -11.67 | 27.55 | -11.67 | 2024-06-28 | 393,500 | representative |
| R13L20_C22_005830_S2A_20240222 | Stage2-Actionable | 005830 | 2024-02-23 | 97,800 | 12.47 | -6.85 | 23.42 | -11.55 | 26.79 | -11.55 | 2024-08-22 | 124,000 | representative |
| R13L20_C22_001450_S2A_20240222 | Stage2-Actionable | 001450 | 2024-02-23 | 34,650 | 3.46 | -12.41 | 3.46 | -17.17 | 6.06 | -21.36 | 2024-07-31 | 36,750 | representative |
| R13L20_C22_088350_S2A_20240222 | Stage2-Actionable | 088350 | 2024-02-23 | 3,385 | 3.84 | -17.13 | 3.84 | -23.63 | 3.84 | -24.52 | 2024-02-23 | 3,515 | representative |
| R13L20_C22_000810_4B_LOCAL_20240321 | 4B-local-price-only | 000810 | 2024-03-21 | 343,000 | 0.87 | -12.97 | 14.72 | -20.55 | 26.82 | -20.55 | 2024-12-03 | 435,000 | 4B_overlay_only |
| R13L20_C22_005830_4B_LOCAL_20240314 | 4B-local-price-only | 005830 | 2024-03-14 | 106,200 | 3.58 | -11.02 | 13.65 | -18.55 | 16.76 | -18.55 | 2024-08-22 | 124,000 | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers only

| symbol | entry | peak in 180D/observed | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 000810 | 308,500 | 393,500 | 12.16 | -7.46 | 27.55 | -11.67 | 27.55 | -11.67 | structural_success_with_high_MAE |
| 005830 | 97,800 | 124,000 | 12.47 | -6.85 | 23.42 | -11.55 | 26.79 | -11.55 | structural_success_with_high_MAE |
| 001450 | 34,650 | 36,750 | 3.46 | -12.41 | 3.46 | -17.17 | 6.06 | -21.36 | failed_rerating_high_MAE |
| 088350 | 3,385 | 3,515 | 3.84 | -17.13 | 3.84 | -23.63 | 3.84 | -24.52 | false_positive_valueup_beta |

### Read-through

The positive cases had high drawdowns but also much higher MFE. The failed cases never generated enough MFE to justify the early risk: their drawdowns were larger than their upside from the Stage2 entry. That means C22 needs a **quality gate**, not a mere sector beta gate.

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would the current profile judge positives? | It likely sees Stage2/Yellow but waits for stronger confirmation; this is too late for 000810 and partly for 005830. |
| Did that match MFE/MAE? | No. The positives had 23%~28% 90D/180D upside, but Green confirmation would arrive after a large portion of upside had already occurred. |
| Was Stage2 bonus excessive? | Not for P&C quality positives; yes for policy-beta-only counterexamples if used without reserve/capital-return gates. |
| Was Yellow 75 too high or low? | Too loose for value-up beta without reserve quality; too strict for confirmed P&C reserve/capital-return quality. |
| Was Green 87 / revision 55 too high or low? | Too high when C22 reserve quality + shareholder return are both visible; correctly high for life/rate beta and weak-reserve cases. |
| Was price-only blowoff guard appropriate? | Yes. Local 4B signals were early in 000810/005830. |
| Was full 4B non-price requirement appropriate? | Yes. Price-only local peaks missed the full observed window. |
| Was hard 4C routing late or excessive? | Useful for 001450 and 088350, but should be triggered by reserve/loss-ratio/capital-return evidence deterioration rather than price alone. |

Case-level verdicts:

```text
000810 = current_profile_too_late
005830 = current_profile_too_late
001450 = current_profile_false_positive
088350 = current_profile_false_positive
current_profile_error_count = 4
```

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | plausible Green entry proxy | peak after Stage2 | green_lateness_ratio | verdict |
|---:|---:|---:|---:|---:|---|
| 000810 | 308,500 | 370,000 on 2024-05-16 | 393,500 in 180D | 0.72 | Green captures too much of move late. |
| 005830 | 97,800 | 111,500 on 2024-05-16 | 124,000 in 180D | 0.52 | Green somewhat late, but less severe than 000810. |
| 001450 | 34,650 | no confirmed Green | 36,750 | n/a | No Green should be emitted. |
| 088350 | 3,385 | no confirmed Green | 3,515 | n/a | No Green should be emitted. |

Formula used:

```text
green_lateness_ratio =
(Stage3_Green_entry_price - Stage2_Actionable_entry_price)
/
(peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B trigger | local proximity | full-window proximity | verdict |
|---:|---|---:|---:|---|
| 000810 | 2024-03-21 price-only local peak | 0.92 | 0.27 | price_only_local_4B_too_early |
| 005830 | 2024-03-14 price-only local spike | 0.69 | 0.32 | borderline_price_only_local_4B_too_early |

Conclusion:

```text
existing_axis_tested = full_4b_requires_non_price_evidence
existing_axis_strengthened = true
do_not_treat_as_full_4B = true for both local price-only rows
```

The local peak looked like a red traffic light, but it was only a bend in the road. Without non-price evidence, it would have forced exit before the real observed-cycle peak.

## 16. 4C Protection Audit

| symbol | prior peak | 4C watch trigger proxy | entry | later low | MAE after 4C | protection label |
|---:|---:|---|---:|---:|---:|---|
| 001450 | 36,750 | 2024-10-02 reserve/loss-ratio deterioration proxy | 30,950 | 23,950 | -22.62 | hard_4c_success |
| 088350 | 3,515 | 2024-10-02 policy-beta fade proxy | 2,795 | 2,440 | -12.70 | hard_4c_late |

Approximate protection scores:

```text
001450 four_c_protection_score ≈ 0.35
088350 four_c_protection_score ≈ 0.58
```

The 4C route helps more when thesis deterioration is recognized before the late-year drawdown. It is less useful when the price already gave back most of the speculative beta.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
candidate_axis = L6_insurance_reserve_quality_capital_return_split
```

Rule candidate:

```text
For insurance cases inside L6, do not treat policy/value-up/low-PBR beta as sufficient Stage3 evidence.
Promote earlier only when all three are present:
1. reserve quality / loss-ratio risk is not deteriorating,
2. ROE or revision quality is visible,
3. shareholder-return visibility is explicit or strongly inferable.

If any of the three is missing, cap at Stage2/Yellow unless later evidence confirms.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
candidate_axis = C22_p_and_c_quality_vs_life_rate_beta_guard
```

Rule candidate:

```text
C22 should split P&C quality rerating from life/rate beta.

Positive promotion:
- P&C + reserve quality + shareholder return + revision/ROE visibility = eligible for earlier Stage3-Green shadow.

Counterexample guard:
- life/rate beta or policy/value-up beta without reserve/capital-return proof = do not promote above Stage2/Yellow.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | missed structural | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 14.57 | -15.99 | 16.06 | -17.28 | 0.5 | 2 | mixed; high residual error |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 14.57 | -15.99 | 16.06 | -17.28 | 0.5 | 2 | worse timing; no sector specificity |
| P1_L6_insurance_sector_shadow_profile | sector_specific | 4 | 25.49 | -11.61 | 27.17 | -11.61 | 0.0 | 0 | improved positive/counterexample separation |
| P2_C22_canonical_archetype_shadow_profile | canonical_archetype_specific | 4 | 25.49 | -11.61 | 27.17 | -11.61 | 0.0 | 0 | best explanatory fit |
| P3_C22_counterexample_guard_profile | counterexample_guard | 2 | 3.65 | -20.4 | 4.95 | -22.94 | 0.0 | 0 | guard effective |

## 20. Score-Return Alignment Matrix

| symbol | before score/label | after score/label | MFE_180D | MAE_180D | alignment |
|---:|---|---|---:|---:|---|
| 000810 | 82.0 / Stage3-Yellow | 89.0 / Stage3-Green-shadow | 27.55 | -11.67 | after aligns better |
| 005830 | 79.0 / Stage3-Yellow | 87.5 / Stage3-Green-shadow | 26.79 | -11.55 | after aligns better |
| 001450 | 76.0 / Stage3-Yellow false positive | 66.0 / Stage2-watch guarded | 6.06 | -21.36 | after blocks false positive |
| 088350 | 75.0 / Stage3-Yellow false positive | 61.0 / Stage2-watch guarded | 3.84 | -24.52 | after blocks false positive |

Component-level interpretation:

```text
component_delta_explanation:
- Add reserve_quality_score and shareholder_return_visibility_score for P&C positives.
- Penalize loss_ratio_or_claims_risk_score when capital-return visibility is absent.
- Reduce valuation_repricing_score impact when the evidence is only policy/value-up beta.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | mixed: P&C quality / reserve risk / life rate beta | 2 | 2 | 2 | 2 | 4 | 0 | 6 | 4 | 4 | true | true | Need C22 insurance holdout with 2025 rate-cut and reserve-review cycle; need C21/C22 merge later. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - positive_too_late_without_C22_reserve_quality_gate
  - false_positive_policy_beta_without_capital_return_visibility
  - price_only_local_4B_too_early
new_axis_proposed:
  - c22_p_and_c_reserve_quality_capital_return_bonus
  - c22_policy_beta_without_reserve_quality_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
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
- stock-web manifest max_date and price basis.
- symbol profile paths and 2024 tradable shard existence.
- entry_date / entry_price from stock-web 2024 tradable rows.
- MFE/MAE 30D/90D/180D estimates from fetched stock-web rows.
- corporate-action candidate dates do not overlap 2024 representative entry→D+180 windows.
- same_entry_group_id and aggregate dedupe.
```

Not validated in this loop:

```text
- exact intraday timestamp of each earnings/shareholder-return disclosure.
- full DART/IR text extraction.
- stock_agent source code.
- production scoring implementation.
- live candidate state.
- 1Y/2Y full-window metrics.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_p_and_c_reserve_quality_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,2,+2,P&C insurers with reserve quality and shareholder-return visibility showed avg MFE_180D 27.17% with manageable MAE vs guarded counterexamples.,Promotes 000810/005830 earlier; blocks 001450/088350,R13L20_C22_000810_S2A_20240222|R13L20_C22_005830_S2A_20240222,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c22_policy_beta_without_reserve_quality_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1 guard,Low-PBR/value-up beta without reserve/capital-return proof produced weak MFE and high MAE in 001450/088350.,Reduces false positives,R13L20_C22_001450_S2A_20240222|R13L20_C22_088350_S2A_20240222,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,price_only_local_4B_too_early_C22_keep_non_price_requirement,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,True,True,0,Local peak timing in 000810/005830 was early relative to full observed window; non-price 4B requirement should stay.,"Keeps existing axis strengthened, no new positive-stage delta",R13L20_C22_000810_4B_LOCAL_20240321|R13L20_C22_005830_4B_LOCAL_20240314,2,2,0,medium,axis_strengthening_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L20_C22_000810","symbol":"000810","company_name":"삼성화재","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L20_C22_000810_S2A_20240222","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C22 positive: P&C reserve/capital-return quality produced sustained MFE despite high MAE."}
{"row_type":"case","case_id":"R13L20_C22_005830","symbol":"005830","company_name":"DB손해보험","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L20_C22_005830_S2A_20240222","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C22 positive: P&C ROE/capital-return quality produced structural repricing with high drawdown risk."}
{"row_type":"case","case_id":"R13L20_C22_001450","symbol":"001450","company_name":"현대해상","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_RESERVE_RISK_COUNTEREXAMPLE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L20_C22_001450_S2A_20240222","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment_for_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C22 counterexample: same value-up window did not convert into durable repricing; reserve/loss-ratio risk mattered."}
{"row_type":"case","case_id":"R13L20_C22_088350","symbol":"088350","company_name":"한화생명","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURER_RATE_BETA_WITH_CAPITAL_QUALITY_GAP","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L20_C22_088350_S2A_20240222","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment_for_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C22 counterexample: rate/value-up beta without visible capital return/revision quality reverted."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R13L20_C22_000810_S2A_20240222","case_id":"R13L20_C22_000810","symbol":"000810","company_name":"삼성화재","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"Insurance / P&C","primary_archetype":"insurance_roe_capital_return_with_reserve_quality","loop_objective":"holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":308500,"evidence_available_at_that_date":"FY2023/early-2024 insurance rerating window: strong P&C earnings visibility, capital-return expectation, K-Value-up/low-PBR backdrop; exact filing timestamp treated as unclear, so next-trading-day close used.","evidence_source":"public FY2023 earnings / shareholder-return expectation route; stock-web price rows verified in atlas","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.16,"MFE_90D_pct":27.55,"MFE_180D_pct":27.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.46,"MAE_90D_pct":-11.67,"MAE_180D_pct":-11.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-30.75,"green_lateness_ratio":0.72,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_with_high_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L20_C22_000810_20240223_308500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L20_C22_005830_S2A_20240222","case_id":"R13L20_C22_005830","symbol":"005830","company_name":"DB손해보험","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"Insurance / P&C","primary_archetype":"insurance_roe_capital_return_with_reserve_quality","loop_objective":"holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":97800,"evidence_available_at_that_date":"FY2023/early-2024 insurance rerating window: high ROE P&C insurer with low-PBR policy optionality and visible capital-return setup; exact filing timestamp treated as unclear, so next-trading-day close used.","evidence_source":"public FY2023 earnings / shareholder-return expectation route; stock-web price rows verified in atlas","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.47,"MFE_90D_pct":23.42,"MFE_180D_pct":26.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.85,"MAE_90D_pct":-11.55,"MAE_180D_pct":-11.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-30.24,"green_lateness_ratio":0.52,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_with_high_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L20_C22_005830_20240223_97800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L20_C22_001450_S2A_20240222","case_id":"R13L20_C22_001450","symbol":"001450","company_name":"현대해상","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_RESERVE_RISK_COUNTEREXAMPLE","sector":"Insurance / P&C","primary_archetype":"insurance_valueup_price_beta_without_reserve_quality","loop_objective":"residual_false_positive_mining|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":34650,"evidence_available_at_that_date":"Same early-2024 low-PBR/insurance rerating window, but forward path shows weaker durable repricing and later reserve/loss-ratio risk pressure. Exact filing timestamp treated as unclear, so next-trading-day close used.","evidence_source":"public FY2023/2024 insurance rerating route; stock-web price rows verified in atlas","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.46,"MFE_90D_pct":3.46,"MFE_180D_pct":6.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.41,"MAE_90D_pct":-17.17,"MAE_180D_pct":-21.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-34.83,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L20_C22_001450_20240223_34650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L20_C22_088350_S2A_20240222","case_id":"R13L20_C22_088350","symbol":"088350","company_name":"한화생명","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURER_RATE_BETA_WITH_CAPITAL_QUALITY_GAP","sector":"Insurance / Life","primary_archetype":"life_insurer_rate_beta_without_shareholder_return_visibility","loop_objective":"residual_false_positive_mining|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":3385,"evidence_available_at_that_date":"Low-PBR/value-up and rate-sensitive life-insurer beta was visible, but capital-return/revision quality was not strong enough; exact filing timestamp treated as unclear, so next-trading-day close used.","evidence_source":"public value-up/insurance rerating route; stock-web price rows verified in atlas","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.84,"MFE_90D_pct":3.84,"MFE_180D_pct":3.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.13,"MAE_90D_pct":-23.63,"MAE_180D_pct":-24.52,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":3515,"drawdown_after_peak_pct":-30.58,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_green_or_valueup_beta","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L20_C22_088350_20240223_3385","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L20_C22_000810_4B_LOCAL_20240321","case_id":"R13L20_C22_000810","symbol":"000810","company_name":"삼성화재","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"Insurance / P&C","primary_archetype":"insurance_roe_capital_return_with_reserve_quality","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-local-price-only","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":343000,"evidence_available_at_that_date":"Local price blowoff near March rally; no independently confirmed non-price thesis break on that date.","evidence_source":"price-only local peak audit using stock-web rows","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.87,"MFE_90D_pct":14.72,"MFE_180D_pct":26.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.97,"MAE_90D_pct":-20.55,"MAE_180D_pct":-20.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-17.47,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.27,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L20_C22_000810_20240321_343000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_different_trigger_family_for_4B_timing_audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L20_C22_005830_4B_LOCAL_20240314","case_id":"R13L20_C22_005830","symbol":"005830","company_name":"DB손해보험","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_ROE_CAPITAL_RETURN_RESERVE_QUALITY","sector":"Insurance / P&C","primary_archetype":"insurance_roe_capital_return_with_reserve_quality","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-local-price-only","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":106200,"evidence_available_at_that_date":"Local March price spike; no independently confirmed non-price thesis break on that date.","evidence_source":"price-only local peak audit using stock-web rows","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.58,"MFE_90D_pct":13.65,"MFE_180D_pct":16.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.02,"MAE_90D_pct":-18.55,"MAE_180D_pct":-18.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-30.24,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":0.32,"four_b_timing_verdict":"borderline_price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L20_C22_005830_20240314_106200","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_different_trigger_family_for_4B_timing_audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L20_C22_000810","trigger_id":"R13L20_C22_000810_S2A_20240222","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":15,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":18,"roe_capital_return_score":18,"asset_liability_rate_sensitivity_score":6,"loss_ratio_or_claims_risk_score":3,"shareholder_return_visibility_score":14},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":16,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":12,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":22,"roe_capital_return_score":22,"asset_liability_rate_sensitivity_score":6,"loss_ratio_or_claims_risk_score":2,"shareholder_return_visibility_score":18},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green-shadow","changed_components":["reserve_quality_score","roe_capital_return_score","loss_ratio_or_claims_risk_score","shareholder_return_visibility_score","valuation_repricing_score"],"component_delta_explanation":"C22 shadow adds explicit reserve-quality and shareholder-return visibility; generic financial profile was too slow.","MFE_90D_pct":27.55,"MAE_90D_pct":-11.67,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L20_C22_005830","trigger_id":"R13L20_C22_005830_S2A_20240222","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":14,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":17,"roe_capital_return_score":17,"asset_liability_rate_sensitivity_score":5,"loss_ratio_or_claims_risk_score":3,"shareholder_return_visibility_score":13},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":15,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":21,"roe_capital_return_score":21,"asset_liability_rate_sensitivity_score":5,"loss_ratio_or_claims_risk_score":2,"shareholder_return_visibility_score":17},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green-shadow","changed_components":["reserve_quality_score","roe_capital_return_score","loss_ratio_or_claims_risk_score","shareholder_return_visibility_score","valuation_repricing_score"],"component_delta_explanation":"P&C ROE/capital-return quality should qualify earlier than generic L6 financial threshold.","MFE_90D_pct":23.42,"MAE_90D_pct":-11.55,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L20_C22_001450","trigger_id":"R13L20_C22_001450_S2A_20240222","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":8,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":8,"roe_capital_return_score":8,"asset_liability_rate_sensitivity_score":4,"loss_ratio_or_claims_risk_score":13,"shareholder_return_visibility_score":7},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":7,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":5,"roe_capital_return_score":6,"asset_liability_rate_sensitivity_score":4,"loss_ratio_or_claims_risk_score":18,"shareholder_return_visibility_score":5},"weighted_score_after":66.0,"stage_label_after":"Stage2-watch_or_guarded","changed_components":["reserve_quality_score","roe_capital_return_score","loss_ratio_or_claims_risk_score","shareholder_return_visibility_score","valuation_repricing_score"],"component_delta_explanation":"Reserve/loss-ratio risk guard prevents policy-beta price move from becoming Stage3.","MFE_90D_pct":3.46,"MAE_90D_pct":-17.17,"score_return_alignment_label":"aligned_guard_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L20_C22_088350","trigger_id":"R13L20_C22_088350_S2A_20240222","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":6,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":12,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":5,"roe_capital_return_score":5,"asset_liability_rate_sensitivity_score":12,"loss_ratio_or_claims_risk_score":7,"shareholder_return_visibility_score":3},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":5,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":11,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"reserve_quality_score":4,"roe_capital_return_score":4,"asset_liability_rate_sensitivity_score":9,"loss_ratio_or_claims_risk_score":8,"shareholder_return_visibility_score":2},"weighted_score_after":61.0,"stage_label_after":"Stage2-watch_or_guarded","changed_components":["reserve_quality_score","roe_capital_return_score","loss_ratio_or_claims_risk_score","shareholder_return_visibility_score","valuation_repricing_score"],"component_delta_explanation":"Life-insurer rate beta alone is not enough without capital-return/revision confirmation.","MFE_90D_pct":3.84,"MAE_90D_pct":-23.63,"score_return_alignment_label":"aligned_guard_counterexample","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_p_and_c_reserve_quality_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,2,+2,P&C insurers with reserve quality and shareholder-return visibility showed avg MFE_180D 27.17% with manageable MAE vs guarded counterexamples.,Promotes 000810/005830 earlier; blocks 001450/088350,R13L20_C22_000810_S2A_20240222|R13L20_C22_005830_S2A_20240222,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c22_policy_beta_without_reserve_quality_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1 guard,Low-PBR/value-up beta without reserve/capital-return proof produced weak MFE and high MAE in 001450/088350.,Reduces false positives,R13L20_C22_001450_S2A_20240222|R13L20_C22_088350_S2A_20240222,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,price_only_local_4B_too_early_C22_keep_non_price_requirement,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,True,True,0,Local peak timing in 000810/005830 was early relative to full observed window; non-price 4B requirement should stay.,"Keeps existing axis strengthened, no new positive-stage delta",R13L20_C22_000810_4B_LOCAL_20240321|R13L20_C22_005830_4B_LOCAL_20240314,2,2,0,medium,axis_strengthening_shadow_only,not production; post-calibrated residual
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"20","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["positive_too_late_without_C22_reserve_quality_gate","false_positive_policy_beta_without_capital_return_visibility","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R13L20_C22_1Y_2Y_EXTENSION","symbol":"MULTI","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"1Y_2Y_fields_retained_but_not_used_for_weight_calibration_in_this_loop","price_source":"Songdaiki/stock-web","usage":"future_validation_needed"}
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
next_round = R13_loop_21_L6_C22_2025_rate_cut_reserve_review_holdout
recommended_next_scope:
  - extend C22 into 2025 rate-cut / reserve-review cases
  - add at least one reinsurer / financial holding insurance-adjacent case if stock-web shard coverage is clean
  - merge with C21 only after separate C22 ledger has >= 8 unique cases
```

## 28. Source Notes

Stock-web files accessed for this loop:

```text
atlas/manifest.json
atlas/symbol_profiles/000/000810.json
atlas/symbol_profiles/005/005830.json
atlas/symbol_profiles/001/001450.json
atlas/symbol_profiles/088/088350.json
atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv
atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv
```

Caveat:

```text
The price path is validated against stock-web rows. Evidence labels are research-proxy classifications based on the historical public event route and should be reconciled against exact DART/IR timestamps before production promotion.
```
