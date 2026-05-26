# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 16
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

This file is historical calibration research only. It is not a live watchlist, not an investment recommendation, and not a production scoring patch.

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

This loop does not re-prove the global axes. It tests whether financial ROE/PBR/capital-return cases need a C21-specific positive gate and a C21-specific policy-halo guard.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 16
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN

loop_objective =
- holdout_validation
- residual_false_positive_mining
- residual_missed_structural_mining
- sector_specific_rule_discovery
- canonical_archetype_compression
- 4B_non_price_requirement_stress_test
- coverage_gap_fill
```

The research target is the Korean financial rerating pattern where low PBR, durable ROE, explicit capital return, and accounting-trust quality combine into a structural rerating. The key residual question is whether a generic Stage2/Yellow/Green model sees only the policy wave, while a C21-specific model distinguishes real shareholder-return machinery from policy halo.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts checked:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- repository search for `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`

Observed state:

```text
discovered_result_md_count = 107
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
loops_covered = 1~9
applied global axes already include Stage2 bonus, Yellow/Green threshold changes, price-only 4B guard, hard 4C routing.
direct repository search for C21 canonical id returned no prior direct C21 hit in the checked artifact search surface.
```

Novelty decision:

```text
required_new_independent_case_ratio = 0.60
new_independent_case_count = 5
reused_case_count = 0
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields read from `Songdaiki/stock-web/atlas/manifest.json`:

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
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema validation:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative cases are historical and use stock-web tradable rows with at least 180 forward trading days available as of manifest max date 2026-02-20.

|symbol|company|profile_path|first_date|last_date|trading_days|corp_action_dates|180D_window_status|
|---|---|---|---|---|---|---|---|
|105560|KB금융|atlas/symbol_profiles/105/105560.json|2008-10-10|2026-02-20|4282|none|clean_180D_window|
|005830|DB손해보험|atlas/symbol_profiles/005/005830.json|1995-05-02|2026-02-20|7762|1999-07-20|clean_180D_window|
|000810|삼성화재|atlas/symbol_profiles/000/000810.json|1995-05-02|2026-02-20|7763|1999-02-01,1999-07-05,2000-02-15|clean_180D_window|
|001450|현대해상|atlas/symbol_profiles/001/001450.json|1995-05-02|2026-02-20|7761|2004-07-13|clean_180D_window|
|323410|카카오뱅크|atlas/symbol_profiles/323/323410.json|2021-08-06|2026-02-20|1109|none|clean_180D_window|

Corporate-action candidates exist in some profiles, but none overlap the 2024 entry through 180D validation windows used here.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN
maps_to = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Compressed evidence families:

1. **ROE/PBR bridge**: low valuation only matters when durable ROE is visible.
2. **Capital-return machinery**: explicit buyback, cancellation, dividend policy, or payout improvement is required.
3. **Accounting-trust quality**: for insurers, IFRS17 earnings must be filtered by reserve/loss-ratio/CSM quality.
4. **Policy-halo guard**: a value-up or low-PBR policy theme cannot promote a high-PBR financial name without shareholder-return route.
5. **4B overlay**: when capital-return premium becomes crowded, 4B is an overlay, not a positive-stage reversal.

## 7. Case Selection Summary

|case_id|symbol|company|case_type|positive/counterexample|best_trigger|current_profile_verdict|calibration_usable|
|---|---|---|---|---|---|---|---|
|C21_KB_2024_VALUEUP_CAPRETURN|105560|KB금융|structural_success|positive|C21-KB-S2A-20240201|current_profile_too_late|true|
|C21_DB_2024_IFRS17_CAPRETURN|005830|DB손해보험|structural_success|positive|C21-DB-S2A-20240201|current_profile_too_late|true|
|C21_SAM_2024_IFRS17_CAPRETURN|000810|삼성화재|structural_success|positive|C21-SAM-S2A-20240201|current_profile_too_late|true|
|C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS|001450|현대해상|false_positive_green|counterexample|C21-HYUN-S2A-20240201|current_profile_false_positive|true|
|C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS|323410|카카오뱅크|false_positive_green|counterexample|C21-KAKAO-S2A-20240201|current_profile_false_positive|true|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 3
counterexample_or_failed_rerating = 2
4B_or_4C_case = 1
minimum_calibration_usable_case_count = 5
counterexample_search_incomplete = false
positive_case_missing = false
```

Positive cases: KB금융, DB손해보험, 삼성화재.
Counterexamples: 현대해상, 카카오뱅크.
4B overlay: KB금융 2024-10-25 capital-return premium / full-window proximity overlay.

## 9. Evidence Source Map

| case_id | trigger evidence | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| C21_KB_2024_VALUEUP_CAPRETURN | Korea value-up / low-PBR rerating + bank capital-return path | policy, public event, relative strength, capital return route | shareholder-return and financial visibility confirmation | 2024-10-25 4B overlay after full-window capital-return premium |
| C21_DB_2024_IFRS17_CAPRETURN | IFRS17 insurer ROE/PBR rerating + capital-return optionality | policy, public event, ROE/PBR bridge | confirmed earnings/ROE visibility and accounting-trust pass | not observed as full 4B inside representative trigger |
| C21_SAM_2024_IFRS17_CAPRETURN | High-quality P&C insurer ROE/PBR rerating | policy, public event, ROE/PBR bridge, trust quality | confirmed revision + solvency/trust quality | December blowoff noted but not used for positive entry |
| C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS | Insurance value-up halo without durable reserve-quality bridge | policy halo, relative strength | weak/insufficient confirmation | false-positive protection |
| C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS | Financial-sector policy halo in high-PBR bank | public event, relative strength only | no low-PBR/capital-return confirmation | false-positive protection |

## 10. Price Data Source Map

|symbol|company|entry_year_shard|profile_path|price_basis|adjustment_status|
|---|---|---|---|---|---|
|105560|KB금융|atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv|atlas/symbol_profiles/105/105560.json|tradable_raw|raw_unadjusted_marcap|
|005830|DB손해보험|atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv|atlas/symbol_profiles/005/005830.json|tradable_raw|raw_unadjusted_marcap|
|000810|삼성화재|atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv|atlas/symbol_profiles/000/000810.json|tradable_raw|raw_unadjusted_marcap|
|001450|현대해상|atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv|atlas/symbol_profiles/001/001450.json|tradable_raw|raw_unadjusted_marcap|
|323410|카카오뱅크|atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv|atlas/symbol_profiles/323/323410.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|outcome|current_verdict|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C21-KB-S2A-20240201|105560|Stage2-Actionable|2024-02-01|2024-02-02|66300|25.79|-9.95|56.71|-9.95|positive_structural_success|current_profile_too_late|representative|
|C21-KB-S3Y-20240426|105560|Stage3-Yellow|2024-04-26|2024-04-26|76000|21.58|-5.39|36.71|-5.39|positive_structural_success|current_profile_too_late|label_comparison_only|
|C21-KB-4B-20241025|105560|Stage4B|2024-10-25|2024-10-25|101000|0.0|-19.21|0.0|-19.21|good_full_window_4B_timing|current_profile_4B_too_late|4B_overlay_only|
|C21-DB-S2A-20240201|005830|Stage2-Actionable|2024-02-01|2024-02-02|99200|15.12|-8.17|25.0|-8.17|positive_structural_success|current_profile_too_late|representative|
|C21-DB-S3G-20240516|005830|Stage3-Green|2024-05-16|2024-05-16|111500|11.21|-15.61|11.21|-15.61|positive_structural_success|current_profile_too_late|label_comparison_only|
|C21-SAM-S2A-20240201|000810|Stage2-Actionable|2024-02-01|2024-02-02|299000|27.09|-8.03|31.61|-8.03|positive_structural_success|current_profile_too_late|representative|
|C21-SAM-S3G-20240516|000810|Stage3-Green|2024-05-16|2024-05-16|370000|6.35|-12.43|17.57|-12.43|positive_structural_success|current_profile_too_late|label_comparison_only|
|C21-HYUN-S2A-20240201|001450|Stage2-Actionable|2024-02-01|2024-02-02|35950|2.36|-20.17|2.36|-20.17|failed_rerating_or_false_positive|current_profile_false_positive|representative|
|C21-KAKAO-S2A-20240201|323410|Stage2-Actionable|2024-02-01|2024-02-02|29300|6.48|-28.67|6.48|-36.89|failed_rerating_or_false_positive|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows:

|case|symbol|entry|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C21_KB_2024_VALUEUP_CAPRETURN|105560|2024-02-02|66300|18.55|-9.95|25.79|-9.95|56.71|-9.95|2024-10-25|103900|-21.46|
|C21_DB_2024_IFRS17_CAPRETURN|005830|2024-02-02|99200|10.89|-8.17|15.12|-8.17|25.0|-8.17|2024-08-22|124000|-24.11|
|C21_SAM_2024_IFRS17_CAPRETURN|000810|2024-02-02|299000|13.71|-4.52|27.09|-8.03|31.61|-8.03|2024-06-28|393500|-25.52|
|C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS|001450|2024-02-02|35950|2.36|-14.19|2.36|-20.17|2.36|-20.17|2024-02-05|36800|-34.92|
|C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS|323410|2024-02-02|29300|6.48|-6.83|6.48|-28.67|6.48|-36.89|2024-02-15|31200|-40.74|

Aggregate representative metrics:

```text
eligible_representative_trigger_count = 5
avg_MFE_90D_pct = 15.37
avg_MAE_90D_pct = -15.0
avg_MFE_180D_pct = 24.43
avg_MAE_180D_pct = -16.64

positive_only_avg_MFE_90D_pct = 22.67
positive_only_avg_MAE_90D_pct = -8.72
positive_only_avg_MFE_180D_pct = 37.77
positive_only_avg_MAE_180D_pct = -8.72
```

## 13. Current Calibrated Profile Stress Test

1. **KB금융**: current profile would likely reach Stage3-Yellow/late Green using generic policy and relative-strength evidence. Actual 180D MFE of 56.71% supports earlier C21 promotion. Verdict: `current_profile_too_late`.
2. **DB손해보험**: current profile sees insurer rerating but lacks explicit IFRS17/capital-return component. Later Green missed nearly half of the move. Verdict: `current_profile_too_late`.
3. **삼성화재**: same broad profile eventually catches quality, but Green after confirmation is late. Verdict: `current_profile_too_late`.
4. **현대해상**: generic policy + relative strength over-promotes; 180D MFE is only 2.36% and MAE is -20.17%. Verdict: `current_profile_false_positive`.
5. **카카오뱅크**: broad financial-sector policy halo is a false positive because C21 needs low-PBR/capital-return route. Verdict: `current_profile_false_positive`.

Existing axes tested:

```text
stage2_actionable_evidence_bonus = kept, but C21-specific gate needed
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened for C21 via capital-return/revision quality
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/Yellow entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KB금융 | 66,300 | 76,000 | 103,900 | 0.258 | Green not too late, but Stage2 was materially better |
| DB손해보험 | 99,200 | 111,500 | 124,000 | 0.496 | Green captured only late middle of the move |
| 삼성화재 | 299,000 | 370,000 | 435,000 | 0.522 | Green missed more than half of the full observed upside |

For C21, the right interpretation is not simply “lower Green threshold.” The stronger rule is: when capital return is explicit and accounting trust is clean, Stage2-Actionable deserves a C21-specific evidence bonus; when the signal is only policy halo, Stage2 should not promote.

## 15. 4B Local vs Full-window Timing Audit

KB금융 2024-10-25 is treated as the 4B overlay case.

```text
Stage2_Actionable_entry_price = 66,300
Stage4B_entry_price = 101,000
full_window_peak_price_after_Stage2 = 103,900
four_b_full_window_peak_proximity = 0.923
four_b_local_peak_proximity = 0.923
four_b_timing_verdict = good_full_window_4B_timing
four_b_evidence_type = valuation_blowoff | positioning_overheat | control_premium_or_event_premium
drawdown_after_peak_pct = -21.46
```

The overlay is not a sell rule by itself. It says that when a capital-return rerating is near full-window peak and the narrative is saturated, 4B should attach as risk state rather than remain Stage3-Green by inertia.

## 16. 4C Protection Audit

No hard 4C thesis break was used for quantitative weight calibration in this loop.

```text
four_c_protection_label = not_observed
hard_4c_success = not_applicable
hard_4c_late = not_applicable
false_break = not_applicable
thesis_break_watch_only = relevant for future insurer reserve deterioration loops
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
candidate = l6_financial_capital_return_requires_explicit_distribution_or_roe_bridge
```

Rule:

> In L6, low-PBR or value-up policy evidence can promote only when it is paired with either explicit shareholder-return machinery or a durable ROE/PBR bridge. Relative strength plus policy alone remains Stage2-Watch, not Stage2-Actionable.

Backtest explanation:

- Positive cases with explicit route averaged 90D MFE 22.67% and 90D MAE -8.72%.
- Counterexamples had 90D MFE 4.42% average and 90D MAE -24.42% average.
- The split is explained by evidence quality, not by price action alone.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate = c21_roe_pbr_capital_return_gate
```

Canonical C21 compression:

```text
positive C21 gate =
    low PBR / valuation rerating evidence
    + durable ROE or IFRS17 ROE bridge
    + explicit payout / buyback / cancellation / capital return route
    + low accounting-trust risk

counterexample C21 guard =
    high PBR financial
    OR no capital-return route
    OR insurance reserve/loss-ratio quality unresolved
    OR policy halo only
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|eligible_triggers|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural_count|avg_green_lateness_ratio|alignment|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|global current proxy|Uses generic Stage2 bonus, Yellow/Green thresholds, price-only guard, non-price 4B guard; no explicit C21 capital-return gate.|none|5|15.37|-15.0|24.43|-16.64|2/5|3|0.425|mixed; positive cases late, 2 false positives|
|P0b|e2r_2_0_baseline_reference|rollback reference|No Stage2 actionable bonus, looser Green revision, weaker 4B thesis break routing.|none|5|15.37|-15.0|24.43|-16.64|2/5|4|0.50|worse; late positive capture and more false positive risk|
|P1|l6_sector_specific_candidate_profile|financial capital-return sector overlay|Add ROE/PBR capital-return score; block high-PBR/no-return policy halo.|+roe_pbr_capital_return_score; +high_pbr_guard|3|22.67|-8.72|37.77|-8.72|0/3|0|0.425|aligned; filters weak C21 impostors|
|P2|c21_canonical_archetype_candidate_profile|C21-specific compression|Require explicit payout/buyback/cancellation or IFRS17 solvency/ROE bridge; Green only if accounting-trust risk low.|+capital_return_quality_gate; +insurance_reserve_quality_gate|3|22.67|-8.72|37.77|-8.72|0/3|0|0.425|best explanatory fit|
|P3|c21_counterexample_guard_profile|guard profile|Reject price-only value-up halo and high-PBR financials; downgrade insurers without reserve/loss-ratio bridge.|+policy_halo_block; +reserve_quality_penalty|3|22.67|-8.72|37.77|-8.72|0/3|0|0.425|best protection against false positives|

## 20. Score-Return Alignment Matrix

|case|before_score|before_stage|after_score|after_stage|90D_MFE|90D_MAE|alignment|
|---|---|---|---|---|---|---|---|
|C21_KB_2024_VALUEUP_CAPRETURN|76|Stage3-Yellow|88|Stage3-Green|25.79|-9.95|aligned_positive|
|C21_DB_2024_IFRS17_CAPRETURN|75|Stage3-Yellow|87|Stage3-Green|15.12|-8.17|aligned_positive|
|C21_SAM_2024_IFRS17_CAPRETURN|77|Stage3-Yellow|90|Stage3-Green|27.09|-8.03|aligned_positive|
|C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS|75|Stage3-Yellow|64|Stage2-Watch|2.36|-20.17|aligned_counterexample|
|C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS|74|Stage2-Actionable|58|Rejected-Halo|6.48|-28.67|aligned_counterexample|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN|3|2|1|0|5|0|9|5|5|True|True|C21 still needs more non-bank financial holding and life-insurance holdouts; this loop fills direct C21 gap.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late_for_explicit_capital_return_positive
  - current_profile_false_positive_for_valueup_policy_halo
  - current_profile_4B_too_late_when_capital_return_premium_overheats
new_axis_proposed:
  - c21_roe_pbr_capital_return_score
  - c21_high_pbr_no_capital_return_guard
  - c21_insurance_reserve_quality_guard
  - c21_full_4b_capital_return_premium_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_revision_min
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and schema fields
- tradable_raw 2024 OHLC rows for 105560, 005830, 000810, 001450, 323410
- profile corporate-action windows
- entry_date / entry_price from stock-web c column
- MFE/MAE 30D/90D/180D research metrics
- C21 positive/counterexample split
- 4B local/full-window separation for KB금융
```

Not validated:

```text
- production stock_agent code
- broker API data
- live candidates
- 2026 current-stage status
- investment attractiveness
- exact official filing text quotations
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_roe_pbr_capital_return_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+3,+3,"Positive cases with explicit shareholder-return/ROE-PBR bridge showed avg 90D MFE 22.67% vs avg 90D MAE -8.72%.","promotes KB/DB/Samsung without using price-only signal","C21-KB-S2A-20240201|C21-DB-S2A-20240201|C21-SAM-S2A-20240201",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_high_pbr_no_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-5,-5,"KakaoBank showed policy/relative-strength halo but high PBR/no capital-return route; 180D MAE -36.89%.","blocks false positive policy halo","C21-KAKAO-S2A-20240201",1,1,1,medium,counterexample_guard_only,"not production"
shadow_weight,c21_insurance_reserve_quality_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-3,-3,"Hyundai Marine showed insurance halo but weak reserve/loss-ratio quality; 90D MAE -20.17%, 180D MFE only 2.36%.","downgrades weak IFRS17 accounting-quality cases","C21-HYUN-S2A-20240201",1,1,1,low,sector_shadow_only,"needs more insurance counterexamples"
shadow_weight,c21_full_4b_capital_return_premium_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"KB 2024-10-25 had full-window peak proximity 0.923 and subsequent observed drawdown around -21.46%.","adds 4B overlay only, not positive-entry weight","C21-KB-4B-20241025",1,1,0,low,4B_overlay_only,"not production; requires non-price overheat/capital-return premium evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "C21_KB_2024_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C21-KB-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Bank holding company with explicit capital-return route; broad value-up policy plus bank payout/buyback quality made C21 evidence direct rather than price-only."}
{"row_type": "case", "case_id": "C21_DB_2024_IFRS17_CAPRETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C21-DB-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "P&C insurer with IFRS17 ROE/PBR bridge and capital-return optionality. Early entry captured more upside than later Green confirmation."}
{"row_type": "case", "case_id": "C21_SAM_2024_IFRS17_CAPRETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C21-SAM-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Large P&C insurer with capital return and solvency credibility. Still showed material Green lateness after late confirmed-revision entry."}
{"row_type": "case", "case_id": "C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS", "symbol": "001450", "company_name": "현대해상", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C21-HYUN-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Broad insurance/value-up halo did not overcome reserve/loss-ratio quality and weaker sustained capital-return evidence."}
{"row_type": "case", "case_id": "C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS", "symbol": "323410", "company_name": "카카오뱅크", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C21-KAKAO-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Financial-sector label without low-PBR/capital-return evidence; high PBR growth-bank exposure turned value-up policy halo into a false positive."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C21-KB-S2A-20240201", "case_id": "C21_KB_2024_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 66300, "MFE_30D_pct": 18.55, "MFE_90D_pct": 25.79, "MFE_180D_pct": 56.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.95, "MAE_90D_pct": -9.95, "MAE_180D_pct": -9.95, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_KB_2024_VALUEUP_CAPRETURN:2024-02-02:66300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-KB-S3Y-20240426", "case_id": "C21_KB_2024_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-04-26", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-26", "entry_price": 76000, "MFE_30D_pct": 9.74, "MFE_90D_pct": 21.58, "MFE_180D_pct": 36.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.39, "MAE_90D_pct": -5.39, "MAE_180D_pct": -5.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": 0.258, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_KB_2024_VALUEUP_CAPRETURN:2024-04-26:76000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-KB-4B-20241025", "case_id": "C21_KB_2024_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2024-10-25", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-25", "entry_price": 101000, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.58, "MAE_90D_pct": -19.21, "MAE_180D_pct": -19.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.923, "four_b_full_window_peak_proximity": 0.923, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "not_observed", "trigger_outcome_label": "good_full_window_4B_timing", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_KB_2024_VALUEUP_CAPRETURN:4B:2024-10-25:101000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-DB-S2A-20240201", "case_id": "C21_DB_2024_IFRS17_CAPRETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality", "financial_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 99200, "MFE_30D_pct": 10.89, "MFE_90D_pct": 15.12, "MFE_180D_pct": 25.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.17, "MAE_90D_pct": -8.17, "MAE_180D_pct": -8.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -24.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_DB_2024_IFRS17_CAPRETURN:2024-02-02:99200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-DB-S3G-20240516", "case_id": "C21_DB_2024_IFRS17_CAPRETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality", "financial_visibility"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "margin_bridge", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 111500, "MFE_30D_pct": 3.5, "MFE_90D_pct": 11.21, "MFE_180D_pct": 11.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.04, "MAE_90D_pct": -15.61, "MAE_180D_pct": -15.61, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -24.11, "green_lateness_ratio": 0.496, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_DB_2024_IFRS17_CAPRETURN:2024-05-16:111500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-SAM-S2A-20240201", "case_id": "C21_SAM_2024_IFRS17_CAPRETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality", "financial_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 299000, "MFE_30D_pct": 13.71, "MFE_90D_pct": 27.09, "MFE_180D_pct": 31.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.52, "MAE_90D_pct": -8.03, "MAE_180D_pct": -8.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -25.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_SAM_2024_IFRS17_CAPRETURN:2024-02-02:299000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-SAM-S3G-20240516", "case_id": "C21_SAM_2024_IFRS17_CAPRETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality", "financial_visibility"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "margin_bridge", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 370000, "MFE_30D_pct": 6.35, "MFE_90D_pct": 6.35, "MFE_180D_pct": 17.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.43, "MAE_90D_pct": -12.43, "MAE_180D_pct": -12.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 435000, "drawdown_after_peak_pct": -25.52, "green_lateness_ratio": 0.522, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_SAM_2024_IFRS17_CAPRETURN:2024-05-16:370000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-HYUN-S2A-20240201", "case_id": "C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS", "symbol": "001450", "company_name": "현대해상", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "financial_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 35950, "MFE_30D_pct": 2.36, "MFE_90D_pct": 2.36, "MFE_180D_pct": 2.36, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.19, "MAE_90D_pct": -20.17, "MAE_180D_pct": -20.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 36800, "drawdown_after_peak_pct": -34.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "failed_rerating_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS:2024-02-02:35950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-KAKAO-S2A-20240201", "case_id": "C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS", "symbol": "323410", "company_name": "카카오뱅크", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_IFRS17_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital-return rerating after Korea value-up and IFRS17 transition", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up / low-PBR capital-return policy context plus company-level shareholder-return or IFRS17/ROE visibility. Evidence timing is treated as public by trigger date; row is not a live scan.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 29300, "MFE_30D_pct": 6.48, "MFE_90D_pct": 6.48, "MFE_180D_pct": 6.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.83, "MAE_90D_pct": -28.67, "MAE_180D_pct": -36.89, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200, "drawdown_after_peak_pct": -40.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "failed_rerating_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS:2024-02-02:29300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c21_shadow", "case_id": "C21_KB_2024_VALUEUP_CAPRETURN", "trigger_id": "C21-KB-S2A-20240201", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "+capital_return_quality", "+low_pbr_repricing_gate"], "component_delta_explanation": "C21 adds explicit capital-return and low-PBR ROE repricing evidence; current profile recognizes the signal late because it lacks a dedicated capital-return component.", "MFE_90D_pct": 25.79, "MAE_90D_pct": -9.95, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c21_shadow", "case_id": "C21_DB_2024_IFRS17_CAPRETURN", "trigger_id": "C21-DB-S2A-20240201", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["ifrs17_roe_bridge", "+capital_return_quality", "+reserve_quality_pass"], "component_delta_explanation": "The price path validates an insurance-specific ROE/PBR bridge; after-profile treats solvency/reserve quality as a positive gate rather than generic financial revision only.", "MFE_90D_pct": 15.12, "MAE_90D_pct": -8.17, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c21_shadow", "case_id": "C21_SAM_2024_IFRS17_CAPRETURN", "trigger_id": "C21-SAM-S2A-20240201", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": ["ifrs17_roe_bridge", "+capital_return_quality", "+solvency_quality"], "component_delta_explanation": "C21 rewards durable ROE/PBR rerating only when capital return and accounting trust are both clean; this prevented price-only interpretation while allowing earlier positive staging.", "MFE_90D_pct": 27.09, "MAE_90D_pct": -8.03, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c21_shadow", "case_id": "C21_HYUNDAI_2024_RESERVE_RISK_FALSEPOS", "trigger_id": "C21-HYUN-S2A-20240201", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch", "changed_components": ["reserve_quality_guard", "-capital_return_quality", "-green_without_reserve_bridge"], "component_delta_explanation": "Broad value-up halo and relative strength would over-score the case; reserve/loss-ratio uncertainty and weaker durable capital-return evidence explain the weak 180D path.", "MFE_90D_pct": 2.36, "MAE_90D_pct": -20.17, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c21_shadow", "case_id": "C21_KAKAOBANK_2024_HIGH_PBR_FALSEPOS", "trigger_id": "C21-KAKAO-S2A-20240201", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 7, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 58, "stage_label_after": "Rejected-Halo", "changed_components": ["high_pbr_no_capital_return_guard", "-policy_halo", "-valuation_repricing_score"], "component_delta_explanation": "Financial-sector label is not enough; high PBR plus absent shareholder-return route turns the value-up catalyst into a false positive.", "MFE_90D_pct": 6.48, "MAE_90D_pct": -28.67, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_roe_pbr_capital_return_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+3,+3,"Positive cases with explicit shareholder-return/ROE-PBR bridge showed avg 90D MFE 22.67% vs avg 90D MAE -8.72%.","promotes KB/DB/Samsung without using price-only signal","C21-KB-S2A-20240201|C21-DB-S2A-20240201|C21-SAM-S2A-20240201",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_high_pbr_no_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-5,-5,"KakaoBank showed policy/relative-strength halo but high PBR/no capital-return route; 180D MAE -36.89%.","blocks false positive policy halo","C21-KAKAO-S2A-20240201",1,1,1,medium,counterexample_guard_only,"not production"
shadow_weight,c21_insurance_reserve_quality_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-3,-3,"Hyundai Marine showed insurance halo but weak reserve/loss-ratio quality; 90D MAE -20.17%, 180D MFE only 2.36%.","downgrades weak IFRS17 accounting-quality cases","C21-HYUN-S2A-20240201",1,1,1,low,sector_shadow_only,"needs more insurance counterexamples"
shadow_weight,c21_full_4b_capital_return_premium_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"KB 2024-10-25 had full-window peak proximity 0.923 and subsequent observed drawdown around -21.46%.","adds 4B overlay only, not positive-entry weight","C21-KB-4B-20241025",1,1,0,low,4B_overlay_only,"not production; requires non-price overheat/capital-return premium evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "16", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late_for_explicit_capital_return_positive", "current_profile_false_positive_for_valueup_policy_halo", "current_profile_4B_too_late_when_capital_return_premium_overheats"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C21_LIFE_INSURER_RESERVE_QUALITY_FUTURE","symbol":"000000","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"life-insurer C21/C22 boundary requires a separate loop with clean evidence and price windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_17_or_batch_implementation
suggested_next_scope =
  - C22_INSURANCE_RATE_CYCLE_RESERVE to separate reserve/loss-ratio cycle from C21 capital-return rerating
  - C21 additional life-insurer / securities holdout
  - C32 governance tender/capital event cross-check if capital return becomes control-premium event
```

## 28. Source Notes

Stock-Web files read in this run:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/105/105560.json`
- `atlas/symbol_profiles/005/005830.json`
- `atlas/symbol_profiles/000/000810.json`
- `atlas/symbol_profiles/001/001450.json`
- `atlas/symbol_profiles/323/323410.json`
- `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`

Allowed stock_agent research artifacts read:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`

No `stock_agent/src/e2r` code was opened. No production patch was written.
