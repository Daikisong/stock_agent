# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 13
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD
output_file = e2r_stock_web_v12_residual_round_R6_loop_13_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is historical calibration research only. It is not a current stock screen, not a recommendation list, and not a repository patch. The loop extends R6 financial coverage from C21 bank/capital-return residuals into C22 insurance. The residual question is not whether value-up or low-PBR policy beta moved prices; that is visible in 2024. The question is whether C22 should require insurance-specific evidence: IFRS17/K-ICS capital quality, reserve stability, loss-ratio/CSM quality, and explicit shareholder-return execution.

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

This loop does not re-argue the global Stage2/Green timing result. The residual is narrower: for Korean insurers after IFRS17/K-ICS, a broad value-up policy event can ignite the whole group, but only some names convert that spark into a durable Stage2/Stage3 path. In practical terms, policy beta is the wind; capital-return execution and reserve/capital quality are the sail and hull.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
loop = 13
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD

loop_objective:
- sector_specific_rule_discovery
- canonical_archetype_compression
- counterexample_mining
- 4B_non_price_requirement_stress_test
- green_strictness_stress_test
```

The canonical compression is:

```text
NONLIFE_IFRS17_CAPITAL_RETURN_EXECUTION -> C22_INSURANCE_RATE_CYCLE_RESERVE
LIFE_INSURANCE_POLICY_BETA_RESERVE_GAP -> C22_INSURANCE_RATE_CYCLE_RESERVE
NONLIFE_POLICY_BETA_WITH_CAPITAL_QUALITY_GAP -> C22_INSURANCE_RATE_CYCLE_RESERVE
PRICE_ONLY_INSURANCE_LOCAL_4B -> C22_INSURANCE_RATE_CYCLE_RESERVE
```

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` source code was not opened. This loop follows the previous generated state that pointed the next round to `R6_loop_13_C22_INSURANCE_RATE_CYCLE_RESERVE`. It avoids repeating the C21 bank/capital-return symbols and uses four new C22 insurance symbols.

```text
auto_selected_coverage_gap = R6/L6 C22 insurance-rate-cycle reserve/capital quality residual
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_count = 4
reused_case_count = 0
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

The price atlas manifest used here reports:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

All representative triggers use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`. Raw/unadjusted status matters: this is not split-adjusted chart data. Corporate-action contaminated 180D windows are blocked by default. For the 2024 windows used here, all representative 180D windows are treated as clean; profile-level corporate-action candidates, where present, are historical and outside the tested 2024 windows.

## 5. Historical Eligibility Gate

| Case | Entry in tradable shard | 180D forward window | 30/90/180 MFE/MAE | 2024 180D corporate-action contamination | Calibration usable |
|---|---:|---:|---:|---:|---:|
| 삼성화재 000810 | true | true | true | false | true |
| DB손해보험 005830 | true | true | true | false | true |
| 한화생명 088350 | true | true | true | false | true |
| 현대해상 001450 | true | true | true | false | true |

## 6. Canonical Archetype Compression Map

C22 is not simply “insurance stock rose when rates or policy headlines improved.” It is a balance-sheet rerating archetype:

```text
IFRS17/K-ICS capital visibility
  -> reserve / CSM / loss-ratio confidence
  -> explicit dividend or shareholder-return execution
  -> lower solvency fear and lower book-value discount
  -> positive Stage2/Stage3 insurance rerating
```

Counterexamples occur when the first node is replaced by “low-PBR policy beta only.” The stock can jump, but without capital-return execution and reserve-capital confirmation the path behaves like a paper umbrella in rain: it opens fast, then collapses under MAE.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN | 000810 | 삼성화재 | positive | 2024-02-22 | 2024-02-23 | 308500 | 27.55 | -11.67 | 27.55 | -11.67 | current_profile_correct |
| R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN | 005830 | DB손해보험 | positive | 2024-02-22 | 2024-02-23 | 97800 | 23.42 | -11.55 | 26.79 | -11.55 | current_profile_correct |
| R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP | 088350 | 한화생명 | counterexample | 2024-02-22 | 2024-02-23 | 3385 | 3.84 | -23.78 | 3.84 | -24.52 | current_profile_false_positive |
| R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP | 001450 | 현대해상 | counterexample | 2024-02-22 | 2024-02-23 | 34650 | 3.46 | -17.89 | 6.06 | -21.36 | current_profile_too_early |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_watch_case_count = 2
calibration_usable_case_count = 4
```

The split is clean. Samsung Fire and DB Insurance show positive C22 conversion: policy context plus company-specific capital-return / IFRS17-KICS visibility. Hanwha Life and Hyundai Marine show why broad insurance value-up beta cannot be promoted alone: MFE stayed small while MAE widened.

```text
positive_avg_MFE_90D_pct = 25.48
positive_avg_MAE_90D_pct = -11.61
positive_avg_MFE_180D_pct = 27.17
positive_avg_MAE_180D_pct = -11.61

counterexample_avg_MFE_90D_pct = 3.65
counterexample_avg_MAE_90D_pct = -20.84
counterexample_avg_MFE_180D_pct = 4.95
counterexample_avg_MAE_180D_pct = -22.94
```

## 9. Evidence Source Map

| Evidence family | Used for | Interpretation |
|---|---|---|
| Company FY2023 result / dividend / capital-return disclosure cluster | 삼성화재, DB손해보험 | Non-price evidence that the insurance rerating had capital-return and financial visibility support. Exact intraday disclosure timestamps were not normalized; next-tradable-close entry is used. |
| Korea Corporate Value-up programme context | All four cases | Sector-wide policy beta; useful but insufficient by itself. Public reports note that the programme was first proposed in February 2024 and that later guidelines were voluntary rather than mandatory. |
| IFRS17/K-ICS capital quality / reserve visibility proxy | All four cases | Insurance-specific conversion gate. Strong enough in positive cases, insufficient in counterexamples. |
| Price-only local peak / positioning overheat | DB overlay, Hanwha Life | 4B watch signal only. It cannot promote or exit full thesis without non-price deterioration. |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile 2024 window status |
|---:|---|---|---|---|
| 000810 | 삼성화재 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json | old corporate-action candidates only; 2024 tested window clean |
| 005830 | DB손해보험 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json | old corporate-action candidate only; 2024 tested window clean |
| 088350 | 한화생명 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json | no profile corporate-action candidates |
| 001450 | 현대해상 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/symbol_profiles/001/001450.json | old corporate-action candidate only; 2024 tested window clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | aggregate_role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_T1 | 000810 | Stage2-Actionable | 2024-02-23 | 308500 | 12.16 | 27.55 | 27.55 | -7.46 | -11.67 | -11.67 | 2024-06-28 | 393500 | current_profile_correct | representative |
| R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_T1 | 005830 | Stage2-Actionable | 2024-02-23 | 97800 | 12.47 | 23.42 | 26.79 | -6.85 | -11.55 | -11.55 | 2024-08-22 | 124000 | current_profile_correct | representative |
| R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1 | 088350 | Stage2-Actionable(false) | 2024-02-23 | 3385 | 3.84 | 3.84 | 3.84 | -17.13 | -23.78 | -24.52 | 2024-02-23 | 3515 | current_profile_false_positive | representative |
| R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1 | 001450 | Stage2-Actionable(false) | 2024-02-23 | 34650 | 3.46 | 3.46 | 6.06 | -12.55 | -17.89 | -21.36 | 2024-07-31 | 36750 | current_profile_too_early | representative |
| R6L13_C22_DBI_20240822_PRICE_ONLY_LOCAL_4B_T2 | 005830 | Stage4B-Local-PriceOnly | 2024-08-22 | 120600 | 2.82 | 2.82 | None | -11.19 | -17.5 | None | 2024-08-22 | 124000 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| Symbol | Entry | Entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Peak | Drawdown after peak | Verdict |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 000810 | 2024-02-23 | 308500 | +12.16 / -7.46 | +27.55 / -11.67 | +27.55 / -11.67 | 2024-06-28 @ 393500 | -17.66 | positive structural |
| 005830 | 2024-02-23 | 97800 | +12.47 / -6.85 | +23.42 / -11.55 | +26.79 / -11.55 | 2024-08-22 @ 124000 | -19.76 | positive structural |
| 088350 | 2024-02-23 | 3385 | +3.84 / -17.13 | +3.84 / -23.78 | +3.84 / -24.52 | 2024-02-23 @ 3515 | -27.31 | failed rerating |
| 001450 | 2024-02-23 | 34650 | +3.46 / -12.55 | +3.46 / -17.89 | +6.06 / -21.36 | 2024-07-31 @ 36750 | -25.85 | failed rerating |

### Price row anchors

```text
000810 entry row: 2024-02-23, o=304500, h=321500, l=304500, c=308500
000810 180D peak anchor: 2024-06-28, h=393500
000810 180D trough anchor after peak: 2024-08-05, l=324000

005830 entry row: 2024-02-23, o=94100, h=97800, l=93000, c=97800
005830 180D peak anchor: 2024-08-22, h=124000
005830 180D trough anchor after peak: 2024-11-18, l=99500

088350 entry row: 2024-02-23, o=3405, h=3515, l=3355, c=3385
088350 180D peak anchor: 2024-02-23, h=3515
088350 180D trough anchor after peak: 2024-11-15, l=2555

001450 entry row: 2024-02-23, o=33850, h=35100, l=33850, c=34650
001450 180D peak anchor: 2024-07-31, h=36750
001450 180D trough anchor after peak: 2024-11-15, l=27250
```

## 13. Current Calibrated Profile Stress Test

| Question | C22 finding |
|---|---|
| How would current calibrated profile judge the case? | It correctly rewards 삼성화재/DB손보 where policy beta is tied to company-specific capital-return and capital-quality visibility. It can still be too generous when policy beta and relative strength are present without the insurance-specific conversion evidence. |
| Was Stage2 bonus too high or too low? | Correct for positive C22 cases; too high for policy-only C22 counterexamples. |
| Was Yellow threshold 75 too high or too low? | Threshold itself is reasonable, but C22 component composition needs a guard so policy beta cannot fill missing reserve/capital quality. |
| Was Green threshold 87 / revision 55 too strict? | Not too strict. Green should remain hard for C22 unless capital-return execution and reserve/K-ICS visibility are both present. |
| Was price-only blowoff guard appropriate? | Strengthened. Hanwha Life and the DB overlay show that price-only peak behavior can be useful as watch evidence but cannot create positive stage evidence. |
| Was full 4B non-price requirement appropriate? | Strengthened. DB's 2024-08-22 overlay was close to full-window peak, but absent non-price deterioration it remains a 4B watch row, not full exit evidence. |
| Was hard 4C routing too late or too early? | Keep as watch for this loop; hard 4C needs explicit reserve/capital/disclosure deterioration. |

## 14. Stage2 / Yellow / Green Comparison

There is no separate confirmed Stage3-Green trigger in this MD because the evidence timestamps are normalized at the FY2023 result/disclosure cluster level, not at analyst-revision timestamp level.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger_normalized_in_this_loop
```

Interpretation:

```text
- Positive cases: current profile can remain Yellow or move to Green only when C22 execution evidence is high.
- Counterexamples: proposed shadow profile blocks false Yellow by capping policy beta without capital-return/reserve quality.
```

## 15. 4B Local vs Full-window Timing Audit

DB Insurance provides a 4B timing stress test:

```text
Stage2_Actionable_entry_price = 97800
Stage4B_watch_entry_price = 120600
local_peak_price_after_Stage2 = 124000
full_180D_window_peak_price_after_Stage2 = 124000

four_b_local_peak_proximity = (120600 - 97800) / (124000 - 97800) = 0.87
four_b_full_window_peak_proximity = 0.87
four_b_timing_verdict = price_only_local_4B_watch_not_full_4B
```

This is the knife-edge case. The price-only overlay was actually close to the full observed peak, but the rule should not convert that into full 4B without non-price evidence. It should raise risk, tighten review cadence, and wait for revision slowdown, reserve/capital deterioration, regulatory block, dilution, or explicit shareholder-return disappointment.

## 16. 4C Protection Audit

No hard 4C row is used for weight calibration. Hanwha Life and Hyundai Marine are `thesis_break_watch_only` rows because the price path punished policy-beta over-scoring, but this MD does not normalize an explicit reserve/capital disclosure break date.

```text
four_c_protection_label:
- 088350 = thesis_break_watch_only
- 001450 = thesis_break_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
axis = C22_policy_beta_without_capital_return_block
proposal_type = sector_shadow_only
```

Rule candidate:

```text
If canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE
and policy_or_regulatory_score is high
and relative_strength_score is high
but capital_return_execution_score < 20
and reserve_capital_quality_score < 40,
then cap positive Stage2/Yellow promotion and route to Watch/4B-risk rather than Stage2-Actionable.
```

Mechanism: in insurance, the low-PBR/value-up headline can move the group like a tide. But the rerating only holds when the insurer proves it can return capital without damaging solvency and without reserve uncertainty swallowing the accounting profit.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
axis = C22_IFRS17_KICS_execution_gate
proposal_type = archetype_shadow_only
```

Rule candidate:

```text
For C22, Stage3-Yellow requires at least one of:
- capital_return_execution_score >= 55
- reserve_capital_quality_score >= 60
- ifrs17_kics_visibility_score >= 60

Stage3-Green requires:
- capital_return_execution_score >= 65
- reserve_capital_quality_score >= 65
- revision_score >= current Green revision threshold
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current_proxy | 4 | 14.57 | -16.22 | 16.06 | -17.27 | 0.5 | mixed; two false positives remain in insurance policy beta |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 14.57 | -16.22 | 16.06 | -17.27 | 0.5 | weaker; policy beta too easily becomes positive stage |
| P1_L6_insurance_sector_shadow_profile | sector_specific | 4 | 25.48 | -11.61 | 27.17 | -11.61 | 0.0 | improved; filters reserve/capital-quality false positives |
| P2_C22_archetype_shadow_profile | canonical_archetype_specific | 4 | 25.48 | -11.61 | 27.17 | -11.61 | 0.0 | best explanatory compression for C22 |
| P3_counterexample_guard_profile | counterexample_guard | 2 | 3.65 | -20.84 | 4.95 | -22.94 | 0.0 | guard works; counterexamples blocked |

## 20. Score-Return Alignment Matrix

| Case group | Avg MFE 90D | Avg MAE 90D | Avg MFE 180D | Avg MAE 180D | Alignment |
|---|---:|---:|---:|---:|---|
| Positive C22 execution cases | 25.48 | -11.61 | 27.17 | -11.61 | strong enough for Stage2/Yellow, selective Green |
| Policy/reserve-gap counterexamples | 3.65 | -20.84 | 4.95 | -22.94 | block promotion; watch/4B-risk only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD | 2 | 2 | 1 | 2 | 4 | 0 | 5 | 4 | 2 | true | true | C22 now has positive/counterexample balance; next gap is C22 life-insurer 4C hard thesis-break timing and C23/C24 bio coverage. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

residual_error_types_found:
- insurance_policy_beta_false_positive
- reserve_capital_quality_gap
- price_only_local_4B_without_non_price_evidence

new_axis_proposed:
- C22_IFRS17_KICS_execution_gate
- C22_policy_beta_without_capital_return_block
- C22_reserve_capital_quality_guard

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_weakened: null
existing_axis_kept:
- stage3_green_revision_min
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
- Stock-Web manifest and schema fields
- 2024 tradable OHLC rows for 000810, 005830, 088350, 001450
- 2024 entry_date / entry_price
- 30D / 90D / 180D MFE and MAE
- profile-level corporate-action candidate status
- positive/counterexample balance
- C22-specific residual rule proposal
```

Not validated in this MD:

```text
- Intraday disclosure timestamps
- Exact EPS/CSM/K-ICS numerical parsing from company IR PDFs
- Full production scoring code
- Live watchlist or current candidate discovery
- Brokerage or auto-trading integration
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_IFRS17_KICS_execution_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Positive C22 insurance rerating required both shareholder-return execution and reserve/capital quality visibility; policy beta alone produced high-MAE false positives.","Positive cases avg 90D MFE 25.49 vs counterexamples avg 90D MFE 3.65; counterexamples avg 90D MAE -20.84.","R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_T1|R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_T1|R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1|R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_policy_beta_without_capital_return_block,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Korea Value-up / low-PBR insurance beta should not promote Stage2/3 without capital-return execution or reserve-capital confirmation.","Filters Hanwha Life and Hyundai Marine false positives while keeping Samsung Fire and DB Insurance positive cases.",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_local_4B_watch_not_full_exit,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"DB Insurance price-only 4B timing was near peak, but lack of non-price deterioration means watch overlay, not full 4B exit.","Strengthens full_4b_requires_non_price_evidence while retaining useful local risk overlay.","R6L13_C22_DBI_20240822_PRICE_ONLY_LOCAL_4B_T2",1,0,0,low,4B_overlay_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"structural_rerating_with_high_but_tolerable_MAE"}
{"row_type":"case","case_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"structural_rerating_with_capital_return_execution"}
{"row_type":"case","case_id":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP","symbol":"088350","company_name":"한화생명","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"blocked_counterexample_after_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"policy_beta_false_positive_high_MAE"}
{"row_type":"case","case_id":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP","symbol":"001450","company_name":"현대해상","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"blocked_counterexample_after_guard","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"policy_beta_failed_rerating_high_MAE"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_T1","case_id":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","sector":"financials/insurance","primary_archetype":"IFRS17/K-ICS insurance rerating vs policy beta/reserve-capital guard","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"FY2023 result/dividend/capital-return disclosure cluster plus non-life underwriting quality under IFRS17/K-ICS. Entry uses next tradable close because the exact public timing is not normalized in this MD.","evidence_source":"company FY2023 result/dividend disclosure cluster; public Korea Value-up policy context","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":308500,"MFE_30D_pct":12.16,"MFE_90D_pct":27.55,"MFE_180D_pct":27.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.46,"MAE_90D_pct":-11.67,"MAE_180D_pct":-11.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-17.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_rerating_with_high_but_tolerable_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"old_corporate_action_candidates_outside_test_window_clean_180D","same_entry_group_id":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_2024-02-23_308500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_T1","case_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","sector":"financials/insurance","primary_archetype":"IFRS17/K-ICS insurance rerating vs policy beta/reserve-capital guard","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"FY2023 result/dividend/capital-return disclosure cluster with non-life loss-ratio/reserve quality and IFRS17/K-ICS capital visibility. Entry uses next tradable close because exact public timing is not normalized in this MD.","evidence_source":"company FY2023 result/dividend disclosure cluster; public Korea Value-up policy context","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":97800,"MFE_30D_pct":12.47,"MFE_90D_pct":23.42,"MFE_180D_pct":26.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.85,"MAE_90D_pct":-11.55,"MAE_180D_pct":-11.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-19.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_rerating_with_capital_return_execution","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"old_corporate_action_candidate_outside_test_window_clean_180D","same_entry_group_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_2024-02-23_97800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1","case_id":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP","symbol":"088350","company_name":"한화생명","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","sector":"financials/insurance","primary_archetype":"IFRS17/K-ICS insurance rerating vs policy beta/reserve-capital guard","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;green_strictness_stress_test","trigger_type":"Stage2-Actionable(false)","trigger_date":"2024-02-22","evidence_available_at_that_date":"Low-PBR / insurance policy beta existed, but durable capital-return execution and reserve/capital quality confirmation were not strong enough to justify positive Stage3. The price path peaked locally almost immediately.","evidence_source":"public Korea Value-up policy context plus company FY2023 result/disclosure cluster","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":3385,"MFE_30D_pct":3.84,"MFE_90D_pct":3.84,"MFE_180D_pct":3.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.13,"MAE_90D_pct":-23.78,"MAE_180D_pct":-24.52,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":3515,"drawdown_after_peak_pct":-27.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_was_near_full_window_peak_but_needs_non_price_guard","four_b_evidence_type":["price_only","positioning_overheat","reserve_capital_quality_gap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_beta_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_profile_corporate_action_candidates","same_entry_group_id":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_2024-02-23_3385","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1","case_id":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP","symbol":"001450","company_name":"현대해상","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","sector":"financials/insurance","primary_archetype":"IFRS17/K-ICS insurance rerating vs policy beta/reserve-capital guard","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;green_strictness_stress_test","trigger_type":"Stage2-Actionable(false)","trigger_date":"2024-02-22","evidence_available_at_that_date":"Non-life insurance policy/value-up beta existed, but the disclosure cluster did not close the capital-return/reserve-quality gap strongly enough. MFE remained small while 180D MAE expanded.","evidence_source":"public Korea Value-up policy context plus company FY2023 result/disclosure cluster","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":34650,"MFE_30D_pct":3.46,"MFE_90D_pct":3.46,"MFE_180D_pct":6.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.55,"MAE_90D_pct":-17.89,"MAE_180D_pct":-21.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-25.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_beta_failed_rerating_high_MAE","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"old_corporate_action_candidate_outside_test_window_clean_180D","same_entry_group_id":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_2024-02-23_34650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C22_DBI_20240822_PRICE_ONLY_LOCAL_4B_T2","case_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_KICS_SHAREHOLDER_RETURN_EXECUTION_VS_POLICY_BETA_RESERVE_GUARD","sector":"financials/insurance","primary_archetype":"IFRS17/K-ICS insurance rerating vs policy beta/reserve-capital guard","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;green_strictness_stress_test","trigger_type":"Stage4B-Local-PriceOnly","trigger_date":"2024-08-22","evidence_available_at_that_date":"Price had moved close to the local/full 180D window peak after the February capital-return trigger. No fresh non-price 4B evidence is normalized here, so this remains 4B watch/overlay rather than full thesis exit.","evidence_source":"stock-web price path + absence of normalized non-price 4B evidence in this MD","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-22","entry_price":120600,"MFE_30D_pct":2.82,"MFE_90D_pct":2.82,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.19,"MAE_90D_pct":-17.5,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-19.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":0.87,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"price_only_peak_watch_good_timing_but_no_non_price_evidence","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"old_corporate_action_candidate_outside_test_window_clean_180D","same_entry_group_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_2024-08-22_120600","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN","trigger_id":"R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_T1","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":46,"revision_score":58,"relative_strength_score":62,"customer_quality_score":55,"policy_or_regulatory_score":70,"valuation_repricing_score":64,"execution_risk_score":14,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"reserve_capital_quality_score":72,"capital_return_execution_score":68,"ifrs17_kics_visibility_score":70,"policy_beta_without_execution_risk_score":20,"positioning_overheat_score":25},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":46,"revision_score":58,"relative_strength_score":62,"customer_quality_score":55,"policy_or_regulatory_score":70,"valuation_repricing_score":68,"execution_risk_score":12,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"reserve_capital_quality_score":78,"capital_return_execution_score":76,"ifrs17_kics_visibility_score":76,"policy_beta_without_execution_risk_score":20,"positioning_overheat_score":25},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["reserve_capital_quality_score","capital_return_execution_score","ifrs17_kics_visibility_score","policy_beta_without_execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C22 shadow profile separates actual IFRS17/K-ICS capital quality and shareholder-return execution from broad policy/value-up beta or price-only insurance rallies.","MFE_90D_pct":27.55,"MAE_90D_pct":-11.67,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN","trigger_id":"R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_T1","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":46,"revision_score":58,"relative_strength_score":62,"customer_quality_score":55,"policy_or_regulatory_score":70,"valuation_repricing_score":64,"execution_risk_score":14,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"reserve_capital_quality_score":72,"capital_return_execution_score":68,"ifrs17_kics_visibility_score":70,"policy_beta_without_execution_risk_score":20,"positioning_overheat_score":25},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":46,"revision_score":58,"relative_strength_score":62,"customer_quality_score":55,"policy_or_regulatory_score":70,"valuation_repricing_score":68,"execution_risk_score":12,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"reserve_capital_quality_score":78,"capital_return_execution_score":76,"ifrs17_kics_visibility_score":76,"policy_beta_without_execution_risk_score":20,"positioning_overheat_score":25},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["reserve_capital_quality_score","capital_return_execution_score","ifrs17_kics_visibility_score","policy_beta_without_execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C22 shadow profile separates actual IFRS17/K-ICS capital quality and shareholder-return execution from broad policy/value-up beta or price-only insurance rallies.","MFE_90D_pct":23.42,"MAE_90D_pct":-11.55,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP","trigger_id":"R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":28,"revision_score":30,"relative_strength_score":68,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":48,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":12,"reserve_capital_quality_score":30,"capital_return_execution_score":10,"ifrs17_kics_visibility_score":35,"policy_beta_without_execution_risk_score":82,"positioning_overheat_score":65},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow(false)","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":28,"revision_score":30,"relative_strength_score":25,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":35,"valuation_repricing_score":28,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":12,"reserve_capital_quality_score":22,"capital_return_execution_score":0,"ifrs17_kics_visibility_score":25,"policy_beta_without_execution_risk_score":90,"positioning_overheat_score":75},"weighted_score_after":59,"stage_label_after":"Watch/Blocked","changed_components":["reserve_capital_quality_score","capital_return_execution_score","ifrs17_kics_visibility_score","policy_beta_without_execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C22 shadow profile separates actual IFRS17/K-ICS capital quality and shareholder-return execution from broad policy/value-up beta or price-only insurance rallies.","MFE_90D_pct":3.84,"MAE_90D_pct":-23.78,"score_return_alignment_label":"blocked_counterexample_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP","trigger_id":"R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":28,"revision_score":30,"relative_strength_score":68,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":48,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":12,"reserve_capital_quality_score":30,"capital_return_execution_score":10,"ifrs17_kics_visibility_score":35,"policy_beta_without_execution_risk_score":82,"positioning_overheat_score":65},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow(false)","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":28,"revision_score":30,"relative_strength_score":25,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":35,"valuation_repricing_score":28,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":12,"reserve_capital_quality_score":22,"capital_return_execution_score":0,"ifrs17_kics_visibility_score":25,"policy_beta_without_execution_risk_score":90,"positioning_overheat_score":75},"weighted_score_after":60,"stage_label_after":"Watch/Blocked","changed_components":["reserve_capital_quality_score","capital_return_execution_score","ifrs17_kics_visibility_score","policy_beta_without_execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C22 shadow profile separates actual IFRS17/K-ICS capital quality and shareholder-return execution from broad policy/value-up beta or price-only insurance rallies.","MFE_90D_pct":3.46,"MAE_90D_pct":-17.89,"score_return_alignment_label":"blocked_counterexample_after_guard","current_profile_verdict":"current_profile_too_early"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_IFRS17_KICS_execution_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Positive C22 insurance rerating required both shareholder-return execution and reserve/capital quality visibility; policy beta alone produced high-MAE false positives.","Positive cases avg 90D MFE 25.49 vs counterexamples avg 90D MFE 3.65; counterexamples avg 90D MAE -20.84.","R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN_T1|R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN_T1|R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1|R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_policy_beta_without_capital_return_block,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Korea Value-up / low-PBR insurance beta should not promote Stage2/3 without capital-return execution or reserve-capital confirmation.","Filters Hanwha Life and Hyundai Marine false positives while keeping Samsung Fire and DB Insurance positive cases.",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_local_4B_watch_not_full_exit,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"DB Insurance price-only 4B timing was near peak, but lack of non-price deterioration means watch overlay, not full 4B exit.","Strengthens full_4b_requires_non_price_evidence while retaining useful local risk overlay.","R6L13_C22_DBI_20240822_PRICE_ONLY_LOCAL_4B_T2",1,0,0,low,4B_overlay_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["insurance_policy_beta_false_positive","reserve_capital_quality_gap","price_only_local_4B_without_non_price_evidence"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R6/L6 C22 insurance-rate-cycle reserve/capital quality residual"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L13_C22_HARD_4C_NOT_NORMALIZED","symbol":"088350|001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"explicit_hard_4c_reserve_or_capital_thesis_break_date_not_normalized_in_this_loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R7_loop_14_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
next_objective = coverage_gap_fill + counterexample_mining
carry_forward_guard = C22 policy beta cannot promote positive Stage2/3 without capital-return execution or reserve/K-ICS capital-quality confirmation
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_web_price_basis = tradable_raw
stock_web_price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

price_files_used:
- atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv

profile_files_used:
- atlas/symbol_profiles/000/000810.json
- atlas/symbol_profiles/005/005830.json
- atlas/symbol_profiles/088/088350.json
- atlas/symbol_profiles/001/001450.json

external_context:
- Korea Corporate Value-up programme first proposed in February 2024.
- Later guidelines were voluntary and did not impose mandatory dividend/payout action.
```

The external policy context is used only to classify policy beta. It is not used as a stand-alone positive Stage2/Stage3 evidence source for C22.
