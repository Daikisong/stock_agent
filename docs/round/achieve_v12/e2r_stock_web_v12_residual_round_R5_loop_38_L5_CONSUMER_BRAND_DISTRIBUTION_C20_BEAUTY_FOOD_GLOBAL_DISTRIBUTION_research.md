# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 38
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_GLOBAL_REORDER_BULDAK | K_BEAUTY_DISTRIBUTOR_SELL_THROUGH | INCUMBENT_BRAND_MNA_REBOUND_GUARD
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not a current-stock scan, not a recommendation, not an auto-trading artifact, and not a stock_agent implementation patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
```

Current calibrated axes assumed as already applied:

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

This loop does not re-propose those global axes. It stress-tests whether L5/C20 needs a more specific distinction between: (a) distributor-led global reorder with export-margin confirmation, and (b) incumbent brand rebound or M&A consolidation narrative that lacks sell-through/reorder evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R5 |
| loop | 38 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| primary research question | In L5/C20, does global distribution/reorder plus export-margin visibility deserve a canonical shadow bonus, while incumbent brand rebound without sell-through/reorder should be capped below Green? |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were consulted only for coverage and duplicate avoidance. The calibration ingest summary shows broad R1–R13 coverage and 1,376 aggregate representative trigger rows, so this loop intentionally avoids R1/R2 HBM, defense, grid, and the previous R7/C23 bio path. The active calibrated profile report confirms the applied global axes and guardrails, so this loop only proposes L5/C20-scoped shadow rules.

```text
allowed_artifacts_read:
- reports/e2r_calibration/ingest_summary.md
- reports/e2r_calibration/calibrated_profile_report.md

forbidden_artifacts_read:
- src/e2r/** = not opened
- live runner = not executed
- production scoring code = not inferred
```

Duplicate avoidance result:

```text
auto_selected_coverage_gap = L5/C20 distributor-led K-food/K-beauty global reorder versus incumbent brand rebound counterexample
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 0
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest was checked before case construction.

```text
source = Songdaiki/stock-web
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

Schema basis:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable_rules = entry row exists; >=180 forward tradable days; MFE/MAE 30/90/180 computed; no 180D corporate-action contamination
```

## 5. Historical Eligibility Gate

| Case | Symbol | Entry date | 180D forward window by manifest max_date | Corporate action overlap in 180D | Usable? |
|---|---:|---|---|---|---|
| SAMYANG_2023_EXPORT_REORDER | 003230 | 2023-11-15 | yes | no; only 2003-07-25 profile candidate | true |
| SILICONTU_2023_GLOBAL_DISTRIBUTOR | 257720 | 2023-11-15 | yes | no; profile candidates are 2022-07-14 and 2022-08-02 | true |
| AMORE_2024_BRAND_REBOUND_FALSE_GREEN | 090430 | 2024-05-02 | yes | no; only 2015-05-08 profile candidate | true |

All representative rows use `price_basis = tradable_raw` and `price_adjustment_status = raw_unadjusted_marcap`.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression note |
|---|---|---|
| K_FOOD_GLOBAL_REORDER_BULDAK | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Food-export reorder and channel expansion can be compressed into C20 when export demand is verified by sales/margin revision rather than theme-only price movement. |
| K_BEAUTY_DISTRIBUTOR_SELL_THROUGH | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Asset-light distributor / cross-border beauty platform routes belong in C20 when reorder velocity and export-margin evidence are visible. |
| INCUMBENT_BRAND_MNA_REBOUND_GUARD | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Same C20 universe, but should be guarded when the evidence is brand rebound, China normalization, or acquisition consolidation without sell-through proof. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | best_trigger | why selected |
|---|---:|---|---|---|---|---|
| C20_SAMYANG_2023_EXPORT_REORDER | 003230 | 삼양식품 | structural_success | positive | Stage2-Actionable on 2023-11-15 | K-food export/reorder path later converted into a large 180D move; useful for C20 export-margin bridge. |
| C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR | 257720 | 실리콘투 | structural_success | positive | Stage2-Actionable on 2023-11-15 | K-beauty distributor/sell-through path showed stronger forward returns than conventional brand narratives. |
| C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN | 090430 | 아모레퍼시픽 | failed_rerating / false_positive_green | counterexample | Stage3-Yellow/false Green candidate on 2024-05-02 | Incumbent brand rebound and acquisition narrative had initial MFE but poor 90D/180D risk profile; useful guard example. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 8
representative_trigger_count = 3
```

The loop satisfies the minimum positive/counterexample balance. It is not a positive-only loop and does not propose a global delta.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|---|---|
| C20_SAMYANG_2023_EXPORT_REORDER | 2023-11-14 / entry 2023-11-15 | 3Q23 earnings and export-led margin thesis were public enough for next-trading-day entry. | DART filings / company earnings materials / brokerage reports around 2023-11-14 | public_event_or_disclosure; channel/export reorder; relative_strength; early_revision_signal | confirmed_revision appears later with 2024Q1 acceleration | June 2024 price-only local peak; no full 4B without non-price fatigue evidence |
| C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR | 2023-11-14 / entry 2023-11-15 | 3Q23 earnings and K-beauty cross-border distributor growth were public enough for next-trading-day entry. | DART filings / company earnings materials / brokerage reports around 2023-11-14 | public_event_or_disclosure; customer_or_order_quality; channel_reorder; relative_strength; early_revision_signal | confirmed_revision and financial_visibility strengthen in 2024Q1 | June 2024 price-only local peak; no full 4B without non-price slowdown |
| C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN | 2024-04-30 / entry 2024-05-02 | 1Q24 result / brand rebound / COSRX consolidation narrative was visible, but sell-through/reorder evidence was not comparable to distributor-led positive cases. | company earnings materials / DART filings / public market commentary around 2024-04-30 | public_event_or_disclosure; brand/M&A optionality; relative_strength | weak confirmed_revision; weak distributor sell-through proof | 2024-08-07 drawdown routes to 4C-watch; thesis break was not price-only entry evidence |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | profile caveat | 180D status |
|---:|---|---|---|---|---|
| 003230 | 삼양식품 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv; atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json | raw_unadjusted_marcap; corporate-action windows blocked by default; only 2003 candidate | clean_180D_window |
| 257720 | 실리콘투 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv; atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json | raw_unadjusted_marcap; 2022 corporate-action candidates outside window | clean_180D_window |
| 090430 | 아모레퍼시픽 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv; atlas/ohlcv_tradable_by_symbol_year/090/090430/2025.csv | atlas/symbol_profiles/090/090430.json | raw_unadjusted_marcap; 2015 corporate-action candidate outside window | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | representative? | current_profile_verdict | trigger_outcome_label |
|---|---|---|---|---|---:|---|---|---|
| R5L38_C20_003230_STAGE2A | C20_SAMYANG_2023_EXPORT_REORDER | Stage2-Actionable | 2023-11-14 | 2023-11-15 | 199600 | yes | current_profile_correct | structural_success |
| R5L38_C20_003230_GREEN | C20_SAMYANG_2023_EXPORT_REORDER | Stage3-Green label comparison | 2024-05-16 | 2024-05-17 | 446500 | no | current_profile_too_late_if_waits_for_green | late_green_success |
| R5L38_C20_003230_4B_PRICE | C20_SAMYANG_2023_EXPORT_REORDER | 4B overlay | 2024-06-18 | 2024-06-18 | 712000 | no | current_profile_correct | price_only_local_peak_not_full_4B |
| R5L38_C20_257720_STAGE2A | C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR | Stage2-Actionable | 2023-11-14 | 2023-11-15 | 8670 | yes | current_profile_correct | structural_success |
| R5L38_C20_257720_GREEN | C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR | Stage3-Green label comparison | 2024-05-09 | 2024-05-10 | 26250 | no | current_profile_too_late_if_waits_for_green | late_green_success |
| R5L38_C20_257720_4B_PRICE | C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR | 4B overlay | 2024-06-19 | 2024-06-19 | 50700 | no | current_profile_correct | price_only_local_peak_not_full_4B |
| R5L38_C20_090430_FALSE_GREEN | C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN | Stage3-Yellow / false Green candidate | 2024-04-30 | 2024-05-02 | 173400 | yes | current_profile_false_positive | failed_rerating_high_drawdown |
| R5L38_C20_090430_4C_WATCH | C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN | 4C thesis-break watch | 2024-08-07 | 2024-08-07 | 124500 | no | current_profile_4C_too_late | hard_4c_watch_success |

## 12. Trigger-Level OHLC Backtest Tables

Representative entry rows:

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | below_entry_30D | below_entry_90D | drawdown_after_peak_pct |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|---:|
| R5L38_C20_003230_STAGE2A | 003230 | 2023-11-15 | 199600 | 16.98 | -5.11 | 19.99 | -15.13 | 259.72 | -15.13 | 2024-06-19 | 718000 | true | true | -20.19 |
| R5L38_C20_257720_STAGE2A | 257720 | 2023-11-15 | 8670 | 8.19 | -15.34 | 38.29 | -15.34 | 525.14 | -15.34 | 2024-06-19 | 54200 | true | true | -25.74 |
| R5L38_C20_090430_FALSE_GREEN | 090430 | 2024-05-02 | 173400 | 15.63 | -5.82 | 15.63 | -33.16 | 15.63 | -42.62 | 2024-05-31 | 200500 | true | true | -50.37 |

Label/overlay rows:

| trigger_id | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | role |
|---|---|---:|---:|---:|---|
| R5L38_C20_003230_GREEN | 2024-05-17 | 446500 | 60.81 | -2.58 | label_comparison_only |
| R5L38_C20_003230_4B_PRICE | 2024-06-18 | 712000 | 0.84 | -19.52 | 4B_overlay_only |
| R5L38_C20_257720_GREEN | 2024-05-10 | 26250 | 106.48 | -1.71 | label_comparison_only |
| R5L38_C20_257720_4B_PRICE | 2024-06-19 | 50700 | 6.90 | -20.61 | 4B_overlay_only |
| R5L38_C20_090430_4C_WATCH | 2024-08-07 | 124500 | 21.29 | -20.08 | 4C_overlay_only |

Calculation notes:

```text
003230 representative entry row is 2023-11-15 c=199600. 30D max high observed in the first 30-trading-day window is 233500; 90D max high is 239500; 180D max high is 718000 on 2024-06-19.
257720 representative entry row is 2023-11-15 c=8670. 30D max high is 9380; 90D max high is 11990; 180D max high is 54200 on 2024-06-19.
090430 representative entry row is 2024-05-02 c=173400. 30D/90D/180D max high is 200500 on 2024-05-31; 180D low is 99500 on 2024-12-09.
```

## 13. Current Calibrated Profile Stress Test

| Case | Current proxy likely judgment | Fit to actual path | Verdict |
|---|---|---|---|
| 삼양식품 | Stage2-Actionable accepted before full Green; Green confirmation later | Correct. Stage2 row had large 180D MFE; waiting for May Green still worked but lost ~48% of the Stage2-to-peak path. | current_profile_correct |
| 실리콘투 | Stage2-Actionable accepted if channel/export evidence scored; Green later | Correct direction. The case argues C20 should reward distributor-led reorder more explicitly. | current_profile_correct |
| 아모레퍼시픽 | Could be over-scored as Yellow/Green if brand rebound + M&A optionality is treated like distributor reorder | Incorrect if promoted. Initial 30D MFE was positive, but 90D/180D MAE was severe and peak occurred early. | current_profile_false_positive |

Applied-axis stress-test answers:

```text
stage2_actionable_evidence_bonus: kept. It worked for 003230 and 257720 when non-price export/reorder evidence existed.
stage3_yellow_total_min: kept but guarded. 090430 should be Yellow/watch, not Green, absent sell-through/reorder proof.
stage3_green_total_min / revision_min: kept. L5/C20 Green should require export-margin revision or distributor sell-through, not only brand rebound.
stage3_cross_evidence_green_buffer: kept but not sufficient for 090430 when evidence families are correlated narrative families.
price_only_blowoff_blocks_positive_stage: strengthened by 4B overlay rows.
full_4b_requires_non_price_evidence: strengthened. 003230 and 257720 price peaks were not full 4B without non-price fatigue evidence.
hard_4c_thesis_break_routes_to_4c: strengthened. 090430 drawdown after early peak belongs to guard/protection, not positive entry calibration.
```

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2-Actionable entry | Stage3-Green / comparison entry | Full-window peak after Stage2 | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| 삼양식품 | 199600 | 446500 | 718000 | 0.476 | Green was useful but meaningfully late; C20 export-margin bridge should let Stage2-Actionable carry weight. |
| 실리콘투 | 8670 | 26250 | 54200 | 0.386 | Green was useful but late; distributor-led sell-through should not be treated as a soft brand narrative. |
| 아모레퍼시픽 | 173400 | not accepted as Green under proposed guard | 200500 | not_applicable | A brand/M&A rebound with weak reorder proof should be capped below Green. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | stage2_entry_price | 4B_entry_price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| R5L38_C20_003230_4B_PRICE | 199600 | 712000 | 718000 | 718000 | 0.988 | 0.988 | price_only | do_not_treat_as_full_4B |
| R5L38_C20_257720_4B_PRICE | 8670 | 50700 | 54200 | 54200 | 0.923 | 0.923 | price_only | do_not_treat_as_full_4B |

The two positive cases confirm the existing 4B guardrail: price-only local peaks can mark review zones, but they should not create a full 4B unless accompanied by non-price evidence such as revision slowdown, margin fatigue, channel inventory, or order/reorder deterioration.

## 16. 4C Protection Audit

| trigger_id | prior_peak_price | 4C_watch_entry | low_after_4C_90D | prior_peak_to_low_drawdown_pct | MAE_90D_after_4C_pct | four_c_protection_score | label |
|---|---:|---:|---:|---:|---:|---:|---|
| R5L38_C20_090430_4C_WATCH | 200500 | 124500 | 99500 | -50.37 | -20.08 | 0.60 | hard_4c_watch_success |

The 090430 4C-watch row does not train positive weights. It is useful for C20 guard calibration: once a brand-rebound thesis loses sell-through/reorder support and the price structure breaks, it belongs in protection logic.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
axis = l5_global_distribution_reorder_margin_bridge
baseline_value = 0
shadow_tested_value = +1.0
proposal_type = sector_shadow_only
```

Rule candidate:

> In L5 consumer export/brand/distribution cases, Stage2-Actionable deserves a shadow bonus only when export/channel evidence is tied to reorder velocity, distributor sell-through, or export-margin bridge. Brand heat, acquisition consolidation, or China-normalization narrative alone should not receive the same bonus.

Why:

```text
003230 and 257720 had severe early volatility but very large 180D MFE because the evidence was not only price action; it was export/distribution demand converting into financial visibility.
090430 had an attractive 30D MFE but poor 90D/180D MAE because the evidence did not prove the same reorder/sell-through engine.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
axis_1 = c20_distributor_reorder_export_margin_bridge_bonus
baseline_value = 0
shadow_tested_value = +1.5
axis_2 = c20_incumbent_brand_mna_rebound_green_cap
baseline_value = 0
shadow_tested_value = true
```

Canonical rule candidate:

```text
if C20 and evidence includes distributor-led sell-through OR verified reorder velocity OR export-margin bridge:
    allow Stage2-Actionable shadow bonus +1.5

if C20 and evidence is primarily incumbent-brand rebound, M&A consolidation, China normalization, or one-off channel restocking:
    cap at Stage3-Yellow unless confirmed_revision and sell-through proof both exist
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current proxy | none | 3 | all 3 representative rows | 24.64 | -21.21 | 266.83 | -24.36 | 33.3% | 0 | 2 | mixed: positives captured, but incumbent brand false-positive remains |
| P0b_e2r_2_0_baseline_reference | rollback reference | no Stage2 bonus, looser Green | 3 | likely later/less consistent | 24.64 | -21.21 | 266.83 | -24.36 | 33.3% | 1 | 2 | weaker: misses early distributor cases or admits broad rebound |
| P1_l5_sector_shadow_profile | sector_specific | +l5 reorder/margin bridge; brand rebound guard | 3 | 003230,257720 accepted; 090430 watch-only | 29.14 | -15.24 | 392.43 | -15.24 | 0.0% | 0 | 2 | improved alignment |
| P2_c20_archetype_shadow_profile | canonical_archetype_specific | +c20 distributor reorder bonus; C20 brand/M&A cap | 3 | 003230,257720 accepted; 090430 capped | 29.14 | -15.24 | 392.43 | -15.24 | 0.0% | 0 | 2 | best fit for this loop |
| P3_counterexample_guard_profile | guard profile | blocks C20 Green without sell-through/reorder | 3 | positive cases accepted; 090430 blocked from Green | 29.14 | -15.24 | 392.43 | -15.24 | 0.0% | 0 | 2 | useful as safety guard |

## 20. Score-Return Alignment Matrix

Canonical component keys are preserved in all score simulation rows. These are research proxy scores, not production scores.

| case_id | trigger_id | P0 score / label | P2 score / label | Return alignment |
|---|---|---|---|---|
| C20_SAMYANG_2023_EXPORT_REORDER | R5L38_C20_003230_STAGE2A | 82 / Stage2-Actionable | 84 / Stage2-Actionable+ | strong positive alignment; 180D MFE 259.72 |
| C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR | R5L38_C20_257720_STAGE2A | 80 / Stage2-Actionable | 84 / Stage2-Actionable+ | strong positive alignment; 180D MFE 525.14 |
| C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN | R5L38_C20_090430_FALSE_GREEN | 76 / Stage3-Yellow, risk of false Green via narrative buffer | 66 / Watch / capped below Green | guard improves alignment; 180D MAE -42.62 |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_FOOD_GLOBAL_REORDER_BULDAK; K_BEAUTY_DISTRIBUTOR_SELL_THROUGH; INCUMBENT_BRAND_MNA_REBOUND_GUARD | 2 | 1 | 2 | 1 | 3 | 0 | 8 | 3 | 1 | true | true | More counterexamples needed for food/beauty restocking vs sell-through distinction; add at least one C18/C19 adjacent holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
diversity_score_summary: high; undercovered L5/C20; three new symbols; distributor-led positive plus incumbent-brand false-positive counterexample; 4B/4C overlay coverage added
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: incumbent_brand_rebound_false_green; narrative_buffer_without_sell_through; price_only_4b_review_not_full_4b
new_axis_proposed: c20_distributor_reorder_export_margin_bridge_bonus; c20_incumbent_brand_mna_rebound_green_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema basis checked.
- Symbol profile caveats checked.
- Entry rows are present in tradable shards.
- 30D/90D/180D MFE/MAE computed from tradable OHLC rows.
- 180D windows do not overlap profile corporate-action candidate dates.
- Representative trigger rows are deduped by same_entry_group_id.
```

Not validated:

```text
- No stock_agent production code was opened.
- No live scan was run.
- No brokerage/API execution was attempted.
- No recommendation or current watchlist was produced.
- Evidence dates use public historical event timing; this MD is not a legal audit of disclosure timestamps.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_distributor_reorder_export_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1.5,+1.5,"Distributor-led sell-through/export-margin bridge separated two large positive cases from one incumbent-brand false-positive.","Selected positive cases avg MFE180 392.43% with avg MAE180 -15.24%; false-positive blocked.","R5L38_C20_003230_STAGE2A|R5L38_C20_257720_STAGE2A|R5L38_C20_090430_FALSE_GREEN",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_incumbent_brand_mna_rebound_green_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"Brand rebound/acquisition consolidation without sell-through should cap at Yellow/watch.","090430 had MFE30 15.63% but MAE180 -42.62%; Green would be false positive.","R5L38_C20_090430_FALSE_GREEN|R5L38_C20_090430_4C_WATCH",1,1,1,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,l5_price_only_peak_review_not_full_4b,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,existing_guard,kept,0,"Price-only local peaks in consumer winners did not create full 4B without non-price fatigue evidence.","003230 and 257720 overlay rows remain review-only; positive entry weights not affected.","R5L38_C20_003230_4B_PRICE|R5L38_C20_257720_4B_PRICE",2,2,0,medium,axis_strengthening,"strengthens existing full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C20_SAMYANG_2023_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_REORDER_BULDAK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L38_C20_003230_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Export/reorder plus margin revision path; Stage2 captured earlier than Green."}
{"row_type":"case","case_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L38_C20_257720_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Asset-light distributor/sell-through path; large 180D MFE with early volatility."}
{"row_type":"case","case_id":"C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"INCUMBENT_BRAND_MNA_REBOUND_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L38_C20_090430_FALSE_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Initial rebound MFE was not enough; absent distributor sell-through/reorder proof, 90D/180D MAE was severe."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L38_C20_003230_STAGE2A","case_id":"C20_SAMYANG_2023_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_REORDER_BULDAK","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-14","evidence_available_at_that_date":"3Q23 export-led earnings/reorder and margin bridge evidence available before next-trading-day entry","evidence_source":"DART/company earnings materials/brokerage commentary","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","backlog_or_delivery_visibility","early_revision_signal","channel_reorder_score"],"stage3_evidence_fields":["financial_visibility","margin_bridge","confirmed_revision"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-15","entry_price":199600,"MFE_30D_pct":16.98,"MFE_90D_pct":19.99,"MFE_180D_pct":259.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.11,"MAE_90D_pct":-15.13,"MAE_180D_pct":-15.13,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-20.19,"green_lateness_ratio":0.476,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SAMYANG_2023_EXPORT_REORDER_2023-11-15_199600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_003230_GREEN","case_id":"C20_SAMYANG_2023_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_REORDER_BULDAK","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"2024Q1 confirmed revision/margin bridge visible","evidence_source":"company earnings/DART/brokerage commentary","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":446500,"MFE_30D_pct":60.81,"MFE_90D_pct":60.81,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.58,"MAE_90D_pct":-2.58,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-20.19,"green_lateness_ratio":0.476,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_success","current_profile_verdict":"current_profile_too_late_if_waits_for_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SAMYANG_2023_EXPORT_REORDER_2024-05-17_446500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same_case_label_comparison_green_lateness","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_003230_4B_PRICE","case_id":"C20_SAMYANG_2023_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_REORDER_BULDAK","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B overlay","trigger_date":"2024-06-18","evidence_available_at_that_date":"price-only local peak zone; no non-price slowdown evidence used","evidence_source":"Stock-Web OHLC only for overlay stress test","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-18","entry_price":712000,"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.52,"MAE_90D_pct":-19.52,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-20.19,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.988,"four_b_full_window_peak_proximity":0.988,"four_b_timing_verdict":"price_only_local_peak_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":null,"trigger_outcome_label":"price_only_local_peak_not_full_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SAMYANG_2023_EXPORT_REORDER_2024-06-18_712000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_4b_overlay_new_trigger_family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_257720_STAGE2A","case_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-14","evidence_available_at_that_date":"3Q23 distributor/sell-through growth and early revision evidence available before next-trading-day entry","evidence_source":"DART/company earnings materials/brokerage commentary","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal","channel_reorder_score"],"stage3_evidence_fields":["financial_visibility","confirmed_revision"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-15","entry_price":8670,"MFE_30D_pct":8.19,"MFE_90D_pct":38.29,"MFE_180D_pct":525.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.34,"MAE_90D_pct":-15.34,"MAE_180D_pct":-15.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":0.386,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR_2023-11-15_8670","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_257720_GREEN","case_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-09","evidence_available_at_that_date":"2024Q1 distributor/sell-through and earnings revision confirmation visible","evidence_source":"company earnings/DART/brokerage commentary","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-10","entry_price":26250,"MFE_30D_pct":106.48,"MFE_90D_pct":106.48,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.71,"MAE_90D_pct":-1.71,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":0.386,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_success","current_profile_verdict":"current_profile_too_late_if_waits_for_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR_2024-05-10_26250","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same_case_label_comparison_green_lateness","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_257720_4B_PRICE","case_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B overlay","trigger_date":"2024-06-19","evidence_available_at_that_date":"price-only local peak zone; no non-price slowdown evidence used","evidence_source":"Stock-Web OHLC only for overlay stress test","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":50700,"MFE_30D_pct":6.90,"MFE_90D_pct":6.90,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.61,"MAE_90D_pct":-20.61,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.923,"four_b_full_window_peak_proximity":0.923,"four_b_timing_verdict":"price_only_local_peak_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":null,"trigger_outcome_label":"price_only_local_peak_not_full_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR_2024-06-19_50700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_4b_overlay_new_trigger_family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_090430_FALSE_GREEN","case_id":"C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"INCUMBENT_BRAND_MNA_REBOUND_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"residual_false_positive_mining;counterexample_mining","trigger_type":"Stage3-Yellow / false Green candidate","trigger_date":"2024-04-30","evidence_available_at_that_date":"1Q24 rebound and COSRX consolidation narrative visible; distributor-led sell-through/reorder evidence not comparable to positives","evidence_source":"company earnings/DART/public market commentary","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv|atlas/ohlcv_tradable_by_symbol_year/090/090430/2025.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-02","entry_price":173400,"MFE_30D_pct":15.63,"MFE_90D_pct":15.63,"MFE_180D_pct":15.63,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.82,"MAE_90D_pct":-33.16,"MAE_180D_pct":-42.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500,"drawdown_after_peak_pct":-50.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"false_green_counterexample","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN_2024-05-02_173400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L38_C20_090430_4C_WATCH","case_id":"C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"INCUMBENT_BRAND_MNA_REBOUND_GUARD","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C thesis-break watch","trigger_date":"2024-08-07","evidence_available_at_that_date":"post-peak collapse; rebound thesis should route to protection/watch rather than positive scoring","evidence_source":"Stock-Web OHLC plus public market context","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken","forced_liquidation_or_crash"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-07","entry_price":124500,"MFE_30D_pct":2.01,"MFE_90D_pct":21.29,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.91,"MAE_90D_pct":-20.08,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-25","peak_price":157600,"drawdown_after_peak_pct":-36.87,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_watch_success","trigger_outcome_label":"hard_4c_watch_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN_2024-08-07_124500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_4c_overlay_new_trigger_family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_SAMYANG_2023_EXPORT_REORDER","trigger_id":"R5L38_C20_003230_STAGE2A","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":48,"margin_bridge_score":58,"revision_score":50,"relative_strength_score":61,"customer_quality_score":54,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":63},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":50,"margin_bridge_score":60,"revision_score":52,"relative_strength_score":61,"customer_quality_score":56,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":67},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable+","changed_components":["channel_reorder_score","margin_bridge_score","customer_quality_score"],"component_delta_explanation":"C20 distributor/export reorder bridge adds shadow credit without changing production scoring.","MFE_90D_pct":19.99,"MAE_90D_pct":-15.13,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_SILICONTU_2023_GLOBAL_DISTRIBUTOR","trigger_id":"R5L38_C20_257720_STAGE2A","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":42,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":58,"customer_quality_score":60,"policy_or_regulatory_score":0,"valuation_repricing_score":46,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":66},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":45,"margin_bridge_score":59,"revision_score":53,"relative_strength_score":58,"customer_quality_score":64,"policy_or_regulatory_score":0,"valuation_repricing_score":46,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":70},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable+","changed_components":["channel_reorder_score","customer_quality_score","margin_bridge_score","revision_score"],"component_delta_explanation":"Asset-light distributor sell-through should be recognized as a C20-specific non-price evidence family.","MFE_90D_pct":38.29,"MAE_90D_pct":-15.34,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_AMORE_2024_BRAND_REBOUND_FALSE_GREEN","trigger_id":"R5L38_C20_090430_FALSE_GREEN","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":32,"revision_score":44,"relative_strength_score":62,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":25},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / false Green risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":28,"revision_score":38,"relative_strength_score":62,"customer_quality_score":28,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15},"weighted_score_after":66,"stage_label_after":"Watch / Green-capped","changed_components":["channel_reorder_score","customer_quality_score","execution_risk_score","revision_score"],"component_delta_explanation":"Brand rebound and acquisition consolidation should not substitute for distributor sell-through/reorder evidence.","MFE_90D_pct":15.63,"MAE_90D_pct":-33.16,"score_return_alignment_label":"false_positive_guard_alignment","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_distributor_reorder_export_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1.5,+1.5,"Distributor-led sell-through/export-margin bridge separated positive cases from incumbent-brand false-positive.","Selected positives avg MFE180 392.43% and avg MAE180 -15.24%; false-positive blocked.","R5L38_C20_003230_STAGE2A|R5L38_C20_257720_STAGE2A|R5L38_C20_090430_FALSE_GREEN",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_incumbent_brand_mna_rebound_green_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"Brand rebound/M&A consolidation without sell-through should cap below Green.","090430 MFE30 15.63% but MAE180 -42.62%.","R5L38_C20_090430_FALSE_GREEN|R5L38_C20_090430_4C_WATCH",1,1,1,medium,counterexample_guard,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"38","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["incumbent_brand_rebound_false_green","narrative_buffer_without_sell_through","price_only_4b_review_not_full_4b"],"diversity_score_summary":"high; 3 new symbols, 3 trigger families, undercovered L5/C20, positive plus counterexample balance","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L5/C20 distributor-led global reorder versus incumbent brand rebound guard"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"all selected cases have usable 180D Stock-Web windows; no narrative-only case required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round_candidates:
- R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER: add non-beauty/non-food consumer export channel counterexamples.
- R5 / C19_BRAND_RETAIL_INVENTORY_MARGIN: separate inventory/margin cases from global reorder winners.
- R7 / C24_BIO_TRIAL_DATA_EVENT_RISK: follow the prior R7/C23 output with trial-event risk rows.
```

## 28. Source Notes

```text
Stock-Web source validation:
- atlas/manifest.json: max_date 2026-02-20, price_adjustment_status raw_unadjusted_marcap, calibration_shard_root atlas/ohlcv_tradable_by_symbol_year.
- atlas/schema.json: tradable columns d,o,h,l,c,v,a,mc,s,m and MFE/MAE formula.

Stock-Web profile checks:
- 003230 profile: corporate_action_candidate_dates only 2003-07-25; selected 2023-11-15~D+180 window clean.
- 257720 profile: corporate_action_candidate_dates 2022-07-14 and 2022-08-02; selected 2023-11-15~D+180 window clean.
- 090430 profile: corporate_action_candidate_dates only 2015-05-08; selected 2024-05-02~D+180 window clean.

Price shard rows sampled:
- 003230 2023 row for 2023-11-15 c=199600; 2024 row for 2024-06-19 h=718000.
- 257720 2023 row for 2023-11-15 c=8670; 2024 row for 2024-06-19 h=54200.
- 090430 2024 row for 2024-05-02 c=173400 and 2024-05-31 h=200500; 2024-12-09 low=99500.

Evidence sources are historical public event references summarized for calibration only. This file is not a disclosure timestamp audit and not investment advice.
```
