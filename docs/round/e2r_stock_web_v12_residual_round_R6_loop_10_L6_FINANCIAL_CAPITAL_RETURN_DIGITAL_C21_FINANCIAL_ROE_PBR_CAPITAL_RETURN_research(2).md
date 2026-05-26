# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R6
loop = 10
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME
selection_mode = auto_coverage_gap_fill
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

This file is historical calibration research only. It is not a live scan, not a recommendation, and not a production scoring patch.

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

The loop does not re-argue the global Stage2 bonus or the price-only 4B guard. It stress-tests whether C21 needs a narrower capital-return quality gate inside the financial sector.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME
loop_objective = sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, stage2_actionable_bonus_stress_test, 4B_non_price_requirement_stress_test, green_strictness_stress_test, coverage_gap_fill
```

The selected coverage gap is the 2024 Korea Corporate Value-up financial-sector cycle. This loop compares major financial holding companies where policy optionality met ROE/PBR/capital-return capacity against policy/price-beta names where the same sector story did not close the fundamental bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact accessed:

```text
reports/e2r_calibration/ingest_summary.md
```

Duplicate and novelty check:

```text
existing_ingest_discovered_md_count = 398
existing_unique_document_count = 82
existing_aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
search_for_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = no direct result in allowed artifact search
selected_loop_is_not_previous_C18_food_export_loop = true
new_independent_case_ratio = 1.00
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
```

No `src/e2r` code was opened. No stock_agent code patch was written.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields verified in this run:

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

Schema validation:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All four representative triggers are historical, have a stock-web tradable entry row, have at least 180 forward trading days by manifest max date, have positive OHLCV, and have no 2024 corporate-action candidate in the entry~D+180 window.

2Y windows are marked unavailable because 504 forward trading days from the 2024-02-26 entries are not fully present by the stock-web manifest max date 2026-02-20.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME

compressed evidence bridge:
1. policy/value-up optionality
2. bank/financial ROE and PBR repricing capacity
3. explicit or credible capital-return path
4. relative strength confirming the market can underwrite the bridge
5. guard against policy-only or price-only sector beta
```

The important distinction is not “bank stock went up.” It is whether the policy event found a balance sheet that could answer it with capital return. A policy headline is like rain on a roof: it only becomes useful water if the gutter is actually connected.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | calibration_usable | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS | 105560 | KB금융 | structural_success | positive | R6L10_C21_105560_STAGE2_20240226 | True | current_profile_correct | high_MFE_low_MAE_aligned |
| R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS | 055550 | 신한지주 | structural_success | positive | R6L10_C21_055550_STAGE2_20240226 | True | current_profile_correct | high_MFE_low_MAE_aligned_but_green_late |
| R6L10_C21_323410_POLICY_THEME_COUNTER | 323410 | 카카오뱅크 | failed_rerating | counterexample | R6L10_C21_323410_STAGE2_20240226 | True | current_profile_false_positive | policy_only_false_positive |
| R6L10_C21_006220_PRICE_THEME_COUNTER | 006220 | 제주은행 | price_moved_without_evidence | counterexample | R6L10_C21_006220_STAGE2_20240226 | True | current_profile_false_positive | price_only_mfe_misleading_high_mae_counterexample |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
new_independent_case_count = 4
```

Positive examples:

- KB금융 and 신한지주: sector policy plus capital-return/ROE bridge generated large MFE with low early MAE.
- Both show Stage2 Actionable was valuable before later Green confirmation.

Counterexamples:

- 카카오뱅크: policy tag alone did not create a durable rerating; MFE was tiny and MAE was large.
- 제주은행: price-only bank/value-up theme spike produced attractive local MFE, then a deep drawdown. This is a 4B risk-overlay row, not a positive Stage2/3 row.

## 9. Evidence Source Map

| Evidence family | Source basis | Use in this loop |
| --- | --- | --- |
| Corporate Value-up policy frame | Reuters/FSC-reported February and May 2024 value-up programme coverage | Stage2 policy optionality only |
| Company-specific capital-return quality | Research proxy from public financial-holding capital-return/ROE/PBR frame; not a production parser output | Shadow-only C21 component |
| Price confirmation | Songdaiki/stock-web tradable raw OHLC shard | MFE/MAE, peak, drawdown |
| Counterexample guard | Stock-web price path plus absence of capital-return bridge in the proxy score | Blocks policy-only / price-only promotion |

Validation note: The company-specific capital-return component is intentionally a research proxy. A later coding/import session should replace it with parsed disclosures, IR PDFs, or approved report evidence before any production promotion.

## 10. Price Data Source Map

| symbol | company_name | profile_path | price_shard_path | corporate_action_window_status | entry_date | entry_price | stock_web_manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | clean_180D_window | 2024-02-26 | 62500 | 2026-02-20 |
| 055550 | 신한지주 | atlas/symbol_profiles/055/055550.json | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv | clean_180D_window | 2024-02-26 | 41350 | 2026-02-20 |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | clean_180D_window | 2024-02-26 | 30150 | 2026-02-20 |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | clean_180D_window | 2024-02-26 | 11710 | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L10_C21_105560_STAGE2_20240226 | 105560 | KB금융 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 62500 | 44.0 | -4.48 | 66.24 | -4.48 | current_profile_correct | True | representative |
| R6L10_C21_055550_STAGE2_20240226 | 055550 | 신한지주 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 41350 | 31.08 | -3.63 | 56.23 | -3.63 | current_profile_correct | True | representative |
| R6L10_C21_323410_STAGE2_20240226 | 323410 | 카카오뱅크 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 30150 | 1.66 | -33.5 | 1.66 | -38.67 | current_profile_false_positive | True | representative |
| R6L10_C21_006220_STAGE2_20240226 | 006220 | 제주은행 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 11710 | 44.32 | -7.51 | 44.32 | -33.3 | current_profile_false_positive | True | representative |
| R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240426 | 105560 | KB금융 | Stage3-Green | 2024-04-26 | 2024-04-26 | 76000 | 36.71 | -5.26 | 36.71 | -5.26 | current_profile_correct | False | label_comparison_only |
| R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240726 | 055550 | 신한지주 | Stage3-Green | 2024-07-26 | 2024-07-26 | 58000 | 11.38 | -11.03 | 11.38 | -11.55 | current_profile_too_late | False | label_comparison_only |
| R6L10_C21_006220_4B_PRICE_ONLY_20240419 | 006220 | 제주은행 | Stage4B | 2024-04-19 | 2024-04-19 | 14910 | 13.35 | -34.21 | 13.35 | -47.62 | current_profile_4B_too_late | False | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L10_C21_105560_STAGE2_20240226 | 105560 | 62500 | 25.76 | 44.0 | 66.24 | 66.24 | unavailable_insufficient_504D_window | -4.48 | -4.48 | -4.48 | -4.48 | 2024-10-25 | 103900 | -15.5 | clean_180D_window |
| R6L10_C21_055550_STAGE2_20240226 | 055550 | 41350 | 24.55 | 31.08 | 56.23 | 56.23 | unavailable_insufficient_504D_window | -3.63 | -3.63 | -3.63 | -3.63 | 2024-08-26 | 64600 | -20.59 | clean_180D_window |
| R6L10_C21_323410_STAGE2_20240226 | 323410 | 30150 | 1.66 | 1.66 | 1.66 | 1.66 | unavailable_insufficient_504D_window | -17.74 | -33.5 | -38.67 | -38.67 | 2024-02-27 | 30650 | -39.67 | clean_180D_window |
| R6L10_C21_006220_STAGE2_20240226 | 006220 | 11710 | 29.63 | 44.32 | 44.32 | 44.32 | unavailable_insufficient_504D_window | -7.51 | -7.51 | -33.3 | -42.36 | 2024-04-19 | 16900 | -53.79 | clean_180D_window |
| R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240426 | 105560 | 76000 | 9.61 | 36.71 | 36.71 | 36.71 | unavailable_insufficient_504D_window | -5.39 | -5.26 | -5.26 | -5.26 | 2024-10-25 | 103900 | -15.5 | clean_180D_window |
| R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240726 | 055550 | 58000 | 11.38 | 11.38 | 11.38 | 11.38 | unavailable_insufficient_504D_window | -11.03 | -11.03 | -11.55 | -11.55 | 2024-08-26 | 64600 | -20.59 | clean_180D_window |
| R6L10_C21_006220_4B_PRICE_ONLY_20240419 | 006220 | 14910 | 13.35 | 13.35 | 13.35 | 13.35 | unavailable_insufficient_504D_window | -19.18 | -34.21 | -47.62 | -54.73 | 2024-04-19 | 16900 | -53.79 | clean_180D_window |

Representative aggregate metrics:

```text
positive_avg_MFE_90D_pct = 37.54
positive_avg_MAE_90D_pct = -4.06
positive_avg_MFE_180D_pct = 61.24
positive_avg_MAE_180D_pct = -4.06

counterexample_avg_MFE_90D_pct = 22.99
counterexample_avg_MAE_90D_pct = -20.51
counterexample_avg_MFE_180D_pct = 22.99
counterexample_avg_MAE_180D_pct = -35.99
```

This is the residual insight: counterexamples can show superficially high MFE, but their MAE and post-peak drawdown expose that the move is not a durable capital-return rerating.

## 13. Current Calibrated Profile Stress Test

| Case | P0 likely judgement | Actual MFE/MAE alignment | Verdict |
| --- | --- | --- | --- |
| KB금융 | Stage2-Actionable/Yellow allowed by policy + relative strength | Correct; 180D MFE +66.24%, MAE -4.48% | current_profile_correct |
| 신한지주 | Stage2-Actionable/Yellow allowed; Green confirmation later | Mostly correct; Green later but not harmful to Stage2 | current_profile_correct |
| 카카오뱅크 | Broad financial policy could over-promote without capital-return bridge | Wrong; 180D MFE +1.66%, MAE -38.67% | current_profile_false_positive |
| 제주은행 | Broad bank/value-up beta and price spike could look attractive | Wrong if promoted; correct only if treated as price-only overlay | current_profile_false_positive / 4B_too_late |

Axis stress test:

```text
stage2_actionable_evidence_bonus = kept, but C21 needs capital-return quality gate
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept
```

## 14. Stage2 / Yellow / Green Comparison

| Symbol | Stage2 entry | Stage2 price | Green entry | Green price | Peak after Stage2 | green_lateness_ratio | Verdict |
| --- | --- | ---: | --- | ---: | ---: | ---: | --- |
| 105560 | 2024-02-26 | 62,500 | 2024-04-26 | 76,000 | 103,900 | 0.326 | Green somewhat late but still usable |
| 055550 | 2024-02-26 | 41,350 | 2024-07-26 | 58,000 | 64,600 | 0.716 | Green misses most upside; Stage2 retention matters |
| 323410 | 2024-02-26 | 30,150 | none | n/a | 30,650 | n/a | No confirmed Green |
| 006220 | 2024-02-26 | 11,710 | none | n/a | 16,900 | n/a | No confirmed Green; price spike only |

C21 conclusion: Green should stay strict, but Stage2 Actionable should not be demoted for major financial holding companies with a clean capital-return bridge. The guard should operate against policy-only/price-only names, not against the bank capital-return leaders.

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | Stage2 price | 4B entry price | local peak | full window peak | local proximity | full-window proximity | Evidence type | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| R6L10_C21_006220_4B_PRICE_ONLY_20240419 | 11,710 | 14,910 | 16,900 | 16,900 | 0.617 | 0.617 | price_only, positioning_overheat | valid risk overlay; not full 4B because no non-price evidence |

The 4B insight is not “sell every local peak.” It is that price-only spikes in C21 should become an overlay/watch row, while full 4B still requires non-price fatigue, capital-return disappointment, valuation blowoff, or explicit thesis cap.

## 16. 4C Protection Audit

A precise 4C protection score was not promoted because no hard cancellation/default/balance-sheet break event was validated from source documents. Counterexamples are therefore labelled:

```text
카카오뱅크 = thesis_break_watch_only
제주은행 = hard_4c_late / thesis_break_watch_only
```

The loop contributes primarily to Stage2/4B guard calibration, not hard 4C routing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L6_value_up_policy_requires_capital_return_quality
candidate_delta = +1 shadow guard
```

Rule candidate:

```text
For L6 financial value-up cases, policy_or_regulatory_score may not promote a trigger above Stage2-Watch unless at least one of the following is present:
- credible ROE/PBR capital-return bridge,
- explicit shareholder-return plan or recurring buyback/dividend path,
- CET1/capital adequacy room for returns,
- confirmed revision/financial visibility.
```

Backtest effect:

```text
keeps = KB금융, 신한지주
filters = 카카오뱅크, 제주은행
positive_avg_MFE_180D = +61.24%
counterexample_avg_MAE_180D = -35.99%
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C21_policy_price_beta_guard
candidate_delta = +1 shadow guard
```

Canonical C21 should distinguish three states:

```text
C21_positive = policy + ROE/PBR + capital-return bridge
C21_watch = policy but no capital-return bridge
C21_4B_overlay = price-only bank/value-up spike or overheat
```

This prevents a price-only bank theme from wearing the mask of a structural capital-return rerating.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | global_proxy | 4 | Stage2-Actionable representative | 30.27 | -12.28 | 42.11 | -20.02 | 0.5 | 0 | 1 | 0.521 | 0.617 | 0.617 | mixed_due_policy_theme_false_positives |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | later/uncertain | 14.0 | -12.0 | 20.0 | -20.0 | 0.25 | 2 | 2 | 0.521 | 0.617 | 0.617 | too_late_for_major_bank_positive_cases |
| P1_L6_sector_specific_candidate_profile | sector_specific | 4 | KB/Shinhan selected; KakaoBank/Jeju blocked | 37.54 | -4.05 | 61.23 | -4.05 | 0.0 | 0 | 1 | 0.521 | 0.617 | 0.617 | improved |
| P2_C21_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | capital-return bridge selected | 37.54 | -4.06 | 61.24 | -4.06 | 0.0 | 0 | 1 | 0.521 | 0.617 | 0.617 | best_explainability |
| P3_counterexample_guard_profile | counterexample_guard | 2 | counterexample guard | 22.99 | -20.5 | 22.99 | -35.98 | 0.0 | 0 | 0 | not_applicable | 0.617 | 0.617 | guard_reduces_high_MAE_false_promotions |

## 20. Score-Return Alignment Matrix

| Case | weighted before | label before | weighted after | label after | 90D MFE/MAE | 180D MFE/MAE | Alignment |
| --- | ---: | --- | ---: | --- | --- | --- | --- |
| KB금융 | 78.0 | Stage3-Yellow | 82.0 | Stage3-Yellow | 44.0 / -4.48 | 66.24 / -4.48 | high_MFE_low_MAE_aligned |
| 신한지주 | 75.5 | Stage3-Yellow | 79.0 | Stage3-Yellow | 31.08 / -3.63 | 56.23 / -3.63 | high_MFE_low_MAE_aligned_but_green_late |
| 카카오뱅크 | 73.0 | Stage2-Actionable | 60.0 | Stage2-Watch | 1.66 / -33.5 | 1.66 / -38.67 | policy_only_false_positive |
| 제주은행 | 74.0 | Stage2-Actionable | 54.0 | Blocked-PriceTheme | 44.32 / -7.51 | 44.32 / -33.3 | price_only_mfe_misleading_high_mae_counterexample |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME | 2 | 2 | 1 | 0 | 4 | 0 | 7 | 4 | 3 | True | True | C21 now has policy+capital-return positives and policy/price-only counterexamples; still needs insurance/brokerage holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - policy_only_false_positive
  - price_only_theme_spike_high_MFE_high_MAE
  - green_late_in_bank_capital_return_cycle
new_axis_proposed:
  - C21_policy_requires_capital_return_quality
  - C21_policy_price_beta_guard
  - C21_green_lateness_softener
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L6/C21 policy value-up financials lacked balanced positive/counterexample coverage
diversity_score_summary: new_symbol=4, new_trigger_family=4, counterexample=2, repeated_same_symbol_penalty=0, schema_rematerialization_penalty=0
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date = 2026-02-20
- raw_unadjusted_marcap / tradable_raw basis
- actual stock-web OHLC rows for 105560, 055550, 323410, 006220
- 30D / 90D / 180D MFE and MAE
- representative trigger dedupe
- positive/counterexample balance
- 4B local vs full-window split
- C21-specific residual guard proposal
```

Not validated:

```text
- live/current candidate quality
- production stock_agent scoring code
- exact original company disclosure parsing for capital-return plan
- broker/exchange API state
- adjusted-price backtest
- 504D full 2Y windows from 2024-02-26
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_policy_requires_capital_return_quality,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy/value-up score can promote only when ROE/PBR capital-return bridge is visible","Filters KakaoBank/JejuBank false positives while keeping KB/Shinhan positives","R6L10_C21_105560_STAGE2_20240226|R6L10_C21_055550_STAGE2_20240226|R6L10_C21_323410_STAGE2_20240226|R6L10_C21_006220_STAGE2_20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_price_only_theme_block,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Bank/value-up price spikes without capital return are 4B overlay only","Prevents high MFE/high drawdown spikes from positive promotion","R6L10_C21_006220_STAGE2_20240226|R6L10_C21_006220_4B_PRICE_ONLY_20240419",2,1,1,medium,canonical_shadow_only,"strengthens existing price-only blowoff guard"
shadow_weight,C21_green_lateness_softener,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"For banks, Stage3 Green confirmation often arrives after large part of upside; Stage2 Actionable may deserve retention if capital-return bridge is clean","Improves Stage2/Green alignment without lowering global Green threshold","R6L10_C21_105560_STAGE2_20240226|R6L10_C21_055550_STAGE2_20240226",2,2,0,low,canonical_shadow_only,"do not apply globally"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS","symbol":"105560","company_name":"KB금융","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L10_C21_105560_STAGE2_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_low_MAE_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"stock-web profile has no 2024 corporate-action candidate; stock-web 2024 shard shows entry close 62,500 on 2024-02-26 and high 103,900 on 2024-10-25."}
{"row_type":"case","case_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS","symbol":"055550","company_name":"신한지주","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L10_C21_055550_STAGE2_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_low_MAE_aligned_but_green_late","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"stock-web profile has no corporate-action candidates; stock-web 2024 shard shows entry close 41,350 on 2024-02-26 and high 64,600 on 2024-08-26."}
{"row_type":"case","case_id":"R6L10_C21_323410_POLICY_THEME_COUNTER","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L10_C21_323410_STAGE2_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_only_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"stock-web profile has no corporate-action candidates; stock-web 2024 shard shows entry close 30,150 and 180D low 18,490."}
{"row_type":"case","case_id":"R6L10_C21_006220_PRICE_THEME_COUNTER","symbol":"006220","company_name":"제주은행","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L10_C21_006220_STAGE2_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_mfe_misleading_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"stock-web profile has old corporate-action candidates only before 2019; no 2024 180D contamination. 2024 shard shows high 16,900 and later 180D low 7,810."}
{"row_type":"trigger","trigger_id":"R6L10_C21_105560_STAGE2_20240226","case_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS","symbol":"105560","company_name":"KB금융","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|green_strictness_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate Value-up policy shock created the sector option; KB-style high-ROE/low-PBR bank with credible capital-return capacity converted the policy option into a durable rerating path.","evidence_source":"FSC/Reuters Corporate Value-up policy frame + stock-web OHLC validation; company-specific capital-return quality treated as research proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":62500,"MFE_30D_pct":25.76,"MFE_90D_pct":44.0,"MFE_180D_pct":66.24,"MFE_1Y_pct":66.24,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-4.48,"MAE_90D_pct":-4.48,"MAE_180D_pct":-4.48,"MAE_1Y_pct":-4.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-15.5,"green_lateness_ratio":0.326,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_policy_plus_capital_return","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS_2024-02-26_62500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C21_055550_STAGE2_20240226","case_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS","symbol":"055550","company_name":"신한지주","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|green_strictness_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"The sector-wide value-up policy became investable because the name retained bank-like ROE/capital-return credibility; Stage3 confirmation was later than the first Stage2 signal.","evidence_source":"FSC/Reuters Corporate Value-up policy frame + stock-web OHLC validation; company-specific capital-return quality treated as research proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":41350,"MFE_30D_pct":24.55,"MFE_90D_pct":31.08,"MFE_180D_pct":56.23,"MFE_1Y_pct":56.23,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-3.63,"MAE_90D_pct":-3.63,"MAE_180D_pct":-3.63,"MAE_1Y_pct":-3.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":64600,"drawdown_after_peak_pct":-20.59,"green_lateness_ratio":0.716,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_policy_plus_capital_return","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS_2024-02-26_41350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C21_323410_STAGE2_20240226","case_id":"R6L10_C21_323410_POLICY_THEME_COUNTER","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|green_strictness_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"A broad financial-sector value-up policy tag without low-PBR/capital-return conversion did not produce a durable rerating; the stock had almost no upside and large MAE.","evidence_source":"FSC/Reuters Corporate Value-up policy frame + stock-web OHLC validation; company-specific capital-return quality treated as research proxy","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":30150,"MFE_30D_pct":1.66,"MFE_90D_pct":1.66,"MFE_180D_pct":1.66,"MFE_1Y_pct":1.66,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-17.74,"MAE_90D_pct":-33.5,"MAE_180D_pct":-38.67,"MAE_1Y_pct":-38.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_323410_POLICY_THEME_COUNTER_2024-02-26_30150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C21_006220_STAGE2_20240226","case_id":"R6L10_C21_006220_PRICE_THEME_COUNTER","symbol":"006220","company_name":"제주은행","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|green_strictness_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"The stock had bank/value-up beta and sharp price spikes, but no high-quality capital-return bridge comparable to major financial holding companies; the move behaves like a price-only theme spike.","evidence_source":"FSC/Reuters Corporate Value-up policy frame + stock-web OHLC validation; company-specific capital-return quality treated as research proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":11710,"MFE_30D_pct":29.63,"MFE_90D_pct":44.32,"MFE_180D_pct":44.32,"MFE_1Y_pct":44.32,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-7.51,"MAE_90D_pct":-7.51,"MAE_180D_pct":-33.3,"MAE_1Y_pct":-42.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-53.79,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_theme_spike_then_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_006220_PRICE_THEME_COUNTER_2024-02-26_11710","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240426","case_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS","symbol":"105560","company_name":"KB금융","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-04-26","evidence_available_at_that_date":"Quarterly result/capital-return confirmation proxy used only for Green lateness comparison; not used as representative aggregate trigger.","evidence_source":"stock-web OHLC validation + quarterly capital-return confirmation proxy","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":76000,"MFE_30D_pct":9.61,"MFE_90D_pct":36.71,"MFE_180D_pct":36.71,"MFE_1Y_pct":36.71,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-5.39,"MAE_90D_pct":-5.26,"MAE_180D_pct":-5.26,"MAE_1Y_pct":-5.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-15.5,"green_lateness_ratio":0.326,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_label_comparison_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS_2024-04-26_76000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240726","case_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS","symbol":"055550","company_name":"신한지주","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-07-26","evidence_available_at_that_date":"Quarterly result/capital-return confirmation proxy used only for Green lateness comparison; not used as representative aggregate trigger.","evidence_source":"stock-web OHLC validation + quarterly capital-return confirmation proxy","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":58000,"MFE_30D_pct":11.38,"MFE_90D_pct":11.38,"MFE_180D_pct":11.38,"MFE_1Y_pct":11.38,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-11.03,"MAE_90D_pct":-11.03,"MAE_180D_pct":-11.55,"MAE_1Y_pct":-11.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":64600,"drawdown_after_peak_pct":-20.59,"green_lateness_ratio":0.716,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_label_comparison_only","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS_2024-07-26_58000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L10_C21_006220_4B_PRICE_ONLY_20240419","case_id":"R6L10_C21_006220_PRICE_THEME_COUNTER","symbol":"006220","company_name":"제주은행","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_VS_POLICY_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR 자본환원 밸류업","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-04-19","evidence_available_at_that_date":"Price-only local peak / positioning overheat; no capital-return non-price evidence, so full 4B is blocked but risk overlay is retained.","evidence_source":"stock-web OHLC validation","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-19","entry_price":14910,"MFE_30D_pct":13.35,"MFE_90D_pct":13.35,"MFE_180D_pct":13.35,"MFE_1Y_pct":13.35,"MFE_2Y_pct":"unavailable_insufficient_504D_window","MAE_30D_pct":-19.18,"MAE_90D_pct":-34.21,"MAE_180D_pct":-47.62,"MAE_1Y_pct":-54.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-53.79,"green_lateness_ratio":"not_applicable:not_stage3_green","four_b_local_peak_proximity":0.617,"four_b_full_window_peak_proximity":0.617,"four_b_timing_verdict":"price_only_local_4B_blocked_as_full_4B_but_valid_risk_overlay","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4B_overlay_success_but_not_full_4B","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C21_006220_PRICE_THEME_COUNTER_2024-04-19_14910","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C21_105560_VALUEUP_CAPITAL_RETURN_POS","trigger_id":"R6L10_C21_105560_STAGE2_20240226","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":48,"revision_score":54,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":76,"execution_risk_score":18,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"roe_pbr_capital_return_score":82},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":48,"revision_score":54,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":84,"valuation_repricing_score":76,"execution_risk_score":18,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"roe_pbr_capital_return_score":87},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow","changed_components":["roe_pbr_capital_return_score","policy_or_regulatory_score"],"component_delta_explanation":"C21 shadow profile rewards policy only when ROE/PBR capital-return bridge is visible.","MFE_90D_pct":44.0,"MAE_90D_pct":-4.48,"score_return_alignment_label":"high_MFE_low_MAE_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS","trigger_id":"R6L10_C21_055550_STAGE2_20240226","symbol":"055550","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":50,"relative_strength_score":66,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":72,"execution_risk_score":20,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"roe_pbr_capital_return_score":76},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":50,"relative_strength_score":66,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":72,"execution_risk_score":20,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"roe_pbr_capital_return_score":81},"weighted_score_after":79.0,"stage_label_after":"Stage3-Yellow","changed_components":["roe_pbr_capital_return_score","policy_or_regulatory_score"],"component_delta_explanation":"C21 shadow profile rewards policy only when ROE/PBR capital-return bridge is visible.","MFE_90D_pct":31.08,"MAE_90D_pct":-3.63,"score_return_alignment_label":"high_MFE_low_MAE_aligned_but_green_late","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C21_323410_POLICY_THEME_COUNTER","trigger_id":"R6L10_C21_323410_STAGE2_20240226","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":25,"customer_quality_score":0,"policy_or_regulatory_score":58,"valuation_repricing_score":35,"execution_risk_score":42,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"roe_pbr_capital_return_score":24},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":25,"customer_quality_score":0,"policy_or_regulatory_score":48,"valuation_repricing_score":27,"execution_risk_score":52,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"roe_pbr_capital_return_score":24},"weighted_score_after":60.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21 guard prevents broad policy/price beta from becoming positive Stage2/3 without capital-return quality.","MFE_90D_pct":1.66,"MAE_90D_pct":-33.5,"score_return_alignment_label":"policy_only_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C21_006220_PRICE_THEME_COUNTER","trigger_id":"R6L10_C21_006220_STAGE2_20240226","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":30,"execution_risk_score":55,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":25,"roe_pbr_capital_return_score":18},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":22,"execution_risk_score":65,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":25,"roe_pbr_capital_return_score":18},"weighted_score_after":54.0,"stage_label_after":"Blocked-PriceTheme","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21 guard prevents broad policy/price beta from becoming positive Stage2/3 without capital-return quality.","MFE_90D_pct":44.32,"MAE_90D_pct":-7.51,"score_return_alignment_label":"price_only_mfe_misleading_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_only_false_positive","price_only_theme_spike_high_MFE_high_MAE","green_late_in_bank_capital_return_cycle"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R6_loop_11_or_C21_holdout
recommended_next_scope:
  - insurance rate cycle / C22 holdout
  - brokerage capital-return beta counterexamples
  - non-bank financial false-positive mining
reason:
  - This loop covers bank holding positives and bank/fintech/theme counterexamples.
  - It still needs financial-sector holdout beyond banks.
```

## 28. Source Notes

Stock-web source files accessed in this run:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/105/105560.json
atlas/symbol_profiles/055/055550.json
atlas/symbol_profiles/323/323410.json
atlas/symbol_profiles/006/006220.json
atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv
atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv
```

External policy evidence basis:

```text
- Reuters / Financial Times reporting on Korea Corporate Value-up Programme around 2024-02-26.
- Reuters 2024-05-02 reporting on voluntary Corporate Value-up guidelines.
```

Important source limitation:

```text
Company-level capital-return quality is represented here as a research proxy component.
Before any production promotion, a coding/research ingest pass should replace that proxy with parsed DART, KIND, company IR, or approved analyst-report evidence.
```
