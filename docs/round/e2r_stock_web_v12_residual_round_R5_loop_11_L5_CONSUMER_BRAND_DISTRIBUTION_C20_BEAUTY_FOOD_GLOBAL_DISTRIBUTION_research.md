# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R5
loop = 11
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_REOPENING_BETA_FALSE_GREEN
output_file = e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This is not live candidate research and not a repository patch. It is a historical calibration MD using the Songdaiki/stock-web OHLC atlas.

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

This loop does not re-prove those global axes. It tests a C20-specific residual: in consumer export/channel stories, true reorder/distribution evidence behaves differently from reopening beta and brand-recovery narratives.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
sector = 소비재·유통·브랜드
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_REOPENING_BETA_FALSE_GREEN

loop_objective =
  counterexample_mining
  green_strictness_stress_test
  4B_non_price_requirement_stress_test
  sector_specific_rule_discovery
  canonical_archetype_compression
  coverage_gap_fill
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check shows historical calibration already spans R1-R13 and loops 1-9, with 1,940 validated trigger rows and 1,376 aggregate representative rows. This loop therefore avoids R1/R2 representative repetition and adds a C20 holdout set.

Searches for the exact C20/R5 symbol set in accessible research artifacts returned no direct duplicate hit for this `삼양식품 + 실리콘투 + LG생활건강` C20 combination. Treat this as new independent evidence with implementation-time dedupe required.

Novelty fields:

```text
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

```text
source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
min_date = 1995-05-02
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The schema defines tradable shard columns `d,o,h,l,c,v,a,mc,s,m` and requires positive OHLCV, 180 forward tradable days, computed 30/90/180D MFE/MAE, and a clean 180D corporate-action window.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | 180D forward window | corporate-action 180D window | calibration_usable |
|---|---:|---:|---:|---:|---|---|
| R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517 | 003230 | 2024-05-17 | 446500 | available by manifest max_date | clean; profile action only 2003-07-25 | true |
| R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516 | 257720 | 2024-05-16 | 28900 | available by manifest max_date | clean; profile action only 2022 window | true |
| R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510 | 051900 | 2024-05-10 | 466000 | available by manifest max_date | clean; no profile corporate-action candidates | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| K_FOOD_US_EXPORT_REORDER_MARGIN_BRIDGE | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Food export reorder, capacity, and margin bridge are a distribution-driven consumer rerating path. |
| K_BEAUTY_US_AMAZON_CHANNEL_REORDER_HIGH_MAE | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K-beauty cross-border channel reorder and distribution operating leverage fit C20, even when post-peak MAE is high. |
| CHINA_REOPENING_BEAUTY_FALSE_REORDER_MARGIN | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Reopening/brand recovery belongs in the same canonical bucket as a counterexample when repeat-order/margin bridge is missing. |

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|current_profile_verdict|calibration_usable|independent_evidence_weight|
|---|---|---|---|---|---|---|---|
|R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517|003230|삼양식품|structural_success|positive|current_profile_correct|True|1.0|
|R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516|257720|실리콘투|high_mae_success|positive|current_profile_correct|True|1.0|
|R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510|051900|LG생활건강|failed_rerating|counterexample|current_profile_false_positive|True|1.0|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
representative_trigger_count = 3
```

This meets the minimum C20 loop requirements. The loop is not a pure positive success sweep: LG생활건강 is retained as a false Yellow/false Green guardrail case.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 삼양식품 | export channel acceleration, relative strength, capacity/export route, early revision | confirmed revision, margin bridge, multiple public sources, repeat-order visibility | valuation/positioning overheat, price-only local peak risk | none |
| 실리콘투 | global K-beauty channel reorder, relative strength, cross-border distribution | confirmed revision, margin bridge, repeat order/conversion | valuation/positioning overheat, later margin/backlog slowdown risk | none |
| LG생활건강 | reopening beta and relative strength | weak multi-source recovery narrative without durable reorder/margin bridge | margin slowdown / brand recovery fatigue | thesis evidence broken/watch-only |

## 10. Price Data Source Map

| symbol | profile_path | 2024 shard | 2025 shard |
|---:|---|---|---|
| 003230 | atlas/symbol_profiles/003/003230.json | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv |
| 257720 | atlas/symbol_profiles/257/257720.json | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv |
| 051900 | atlas/symbol_profiles/051/051900.json | atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv | atlas/ohlcv_tradable_by_symbol_year/051/051900/2025.csv |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|trigger_outcome_label|current_profile_verdict|dedupe_for_aggregate|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517_Stage2_Actionable|003230|삼양식품|Stage2-Actionable|2024-05-16|2024-05-17|446500|structural_success|current_profile_correct|True|representative|
|TRG_R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516_Stage2_Actionable|257720|실리콘투|Stage2-Actionable|2024-05-16|2024-05-16|28900|high_mae_success|current_profile_correct|True|representative|
|TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow|051900|LG생활건강|Stage3-Yellow|2024-05-10|2024-05-10|466000|failed_rerating|current_profile_false_positive|True|representative|
|TRG_R5L11_C20_003230_STAGE3_GREEN_20240603|003230|삼양식품|Stage3-Green|2024-06-03|2024-06-03|587000|label_comparison_only|current_profile_correct|False|label_comparison_only|
|TRG_R5L11_C20_257720_STAGE3_GREEN_20240603|257720|실리콘투|Stage3-Green|2024-06-03|2024-06-03|43100|label_comparison_only|current_profile_correct|False|label_comparison_only|

## 12. Trigger-Level OHLC Backtest Tables

Representative triggers:

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 003230 | 2024-05-17 | 446500 | 60.81 | 0.0 | 60.81 | 0.0 | 106.05 | 0.0 | 176.15 | 0.0 | 2025-05-16 | 1233000 | -12.25 |
| 257720 | 2024-05-16 | 28900 | 87.54 | -10.38 | 87.54 | -10.38 | 87.54 | -16.26 | 87.54 | -18.34 | 2024-06-19 | 54200 | -57.01 |
| 051900 | 2024-05-10 | 466000 | 3.0 | -23.18 | 3.0 | -31.12 | 3.0 | -34.55 | 3.0 | -37.77 | 2024-05-23 | 480000 | -39.58 |

Aggregate representative stats:

```text
avg_MFE_90D_pct = 50.45
avg_MAE_90D_pct = -13.83
avg_MFE_180D_pct = 65.53
avg_MAE_180D_pct = -16.94
false_positive_rate_before_guard = 0.333
```

## 13. Current Calibrated Profile Stress Test

| case | current profile expected action | outcome | verdict |
|---|---|---|---|
| 삼양식품 | Stage2-Actionable rapidly upgrades to Green after revision/margin confirmation | MFE90 +60.8%, MFE180 +106.0% | current_profile_correct |
| 실리콘투 | Stage2/Green valid, but needs 4B-watch due valuation/positioning and high MAE path | MFE90 +87.5%, but post-peak drawdown -57.0% | current_profile_correct with risk overlay |
| LG생활건강 | Could be mistakenly lifted to Yellow/weak Green from reopening beta and RS | MFE90 +3.0%, MAE90 -31.1% | current_profile_false_positive |

Answers to required stress-test questions:

```text
Stage2 bonus: kept. It helps true C20 export/channel winners but should not override missing channel reorder.
Yellow threshold 75: too permissive for reopening-beta cases without repeat-order/margin evidence.
Green threshold 87 / revision 55: kept globally; strengthened only inside C20 if revision is not tied to channel reorder.
price_only_blowoff guard: strengthened. C20 often has price-led local peaks.
full 4B non-price requirement: kept. Samyang's Dec local peak was not full 4B without non-price deterioration.
hard 4C routing: kept. LG생활건강 is a thesis-break/watch counterexample, not positive-entry evidence.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green comparison entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 삼양식품 | 446500 | 587000 | 0.179 | Green not too late; still captured much of 1Y upside. |
| 실리콘투 | 28900 | 43100 | 0.561 | Green somewhat late; captured less of the first peak and carried higher MAE. |
| LG생활건강 | 466000 | no confirmed Green | not_applicable | A Green label would be false because the channel/margin bridge never closed. |

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B cue | four_b_local_peak_proximity | four_b_full_window_peak_proximity | timing verdict |
|---|---|---:|---:|---|
| 삼양식품 | Dec-2024 price-only local peak near 800k before 2025 re-acceleration | 0.95 | 0.43 | price_only_local_4B_too_early |
| 실리콘투 | Jun-2024 first peak, later deep drawdown and position fatigue | 0.86 | 0.86 | good_full_window_4B_timing_but_high_mae |
| LG생활건강 | May-2024 reopening peak failed quickly | n/a | n/a | false positive / 4C watch rather than 4B graduation |

The key C20 residual is that full 4B should not trigger on price-only food/beauty momentum if channel reorder and earnings still accelerate; but when distribution momentum breaks or a recovery narrative lacks margin/reorder support, the risk overlay should cap positive stage promotion.

## 16. 4C Protection Audit

| case | 4C label | protection note |
|---|---|---|
| 삼양식품 | not_applicable | No hard thesis break in observed window. |
| 실리콘투 | thesis_break_watch_only | Deep drawdown after first peak argues for watch, not immediate hard 4C, because positive channel evidence remained partly intact. |
| LG생활건강 | hard_4c_late | Reopening/brand recovery thesis failed after peak; C20 guard should have capped Stage before the 180D drawdown widened. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c20_reopening_beta_cap_without_repeat_order
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

Rule:
In L5 consumer export/reopening stories, do not allow reopening beta, brand sentiment, or relative strength alone to lift a case above Stage2-Watch/Stage3-Red unless repeat-order/channel reorder and margin/revision bridge are both visible.

Backtest effect:
- LG생활건강 false positive would be capped.
- 삼양식품 and 실리콘투 remain positive because actual channel/reorder evidence and margin bridge are present.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c20_green_requires_realized_channel_reorder_and_margin_revision

C20 Green requirements:
1. channel_reorder_score >= 7,
2. margin_bridge_score >= 7,
3. revision_score >= 7,
4. customer/channel quality evidence cannot be price-only,
5. if valuation/positioning overheat is high, attach 4B-watch rather than demote a true positive entry.
```

## 19. Before / After Backtest Comparison

| profile | selected entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 50.45 | -13.83 | 65.53 | -16.94 | 33.3% | mixed: LG false positive |
| P0b e2r_2_0_baseline_reference | 3 | 50.45 | -13.83 | 65.53 | -16.94 | 33.3% | worse: less C20-specific filtering |
| P1 sector_specific_candidate_profile | 2 | 74.18 | -5.19 | 96.8 | -8.13 | 0.0% | improved |
| P2 canonical_archetype_candidate_profile | 2 | 74.18 | -5.19 | 96.8 | -8.13 | 0.0% | improved |
| P3 counterexample_guard_profile | 2 + LG watch only | same as P2 | same as P2 | same as P2 | same as P2 | 0.0% | best small-sample guard |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 삼양식품 | 88 | Stage3-Green | 91 | Stage3-Green | 60.81 | 0.0 | aligned |
| 실리콘투 | 86 | Stage3-Green | 84 | Stage3-Yellow/4B-watch | 87.54 | -10.38 | aligned with risk overlay |
| LG생활건강 | 76 | Stage3-Yellow | 65 | Stage2-Watch | 3.0 | -31.12 | misaligned before guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_FOOD_K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_REOPENING_BETA_FALSE_GREEN | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 1 | true | true | Need more C18/C19/C20 consumer holdout, especially failed channel claims and post-peak 4B/4C examples. |

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

tested_existing_calibrated_axes:
- stage3_green_revision_min
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage

residual_error_types_found:
- current_profile_false_positive
- high_mae_success
- price_only_local_4B_too_early

new_axis_proposed:
- c20_green_requires_realized_channel_reorder_and_margin_revision
- c20_reopening_beta_cap_without_repeat_order
- c20_high_mae_success_4b_watch_if_positioning_overheat

existing_axis_strengthened:
- stage3_green_revision_min in C20 only
- full_4b_requires_non_price_evidence in C20 only

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-web manifest/schema fields.
- Symbol profiles for 003230, 257720, 051900.
- Actual 2024/2025 tradable_raw OHLC windows.
- 30/90/180D MFE/MAE, 1Y where available in fetched windows.
- Clean 180D corporate-action window based on profile dates.

Not validated:
- This MD does not patch stock_agent.
- This MD does not change production scoring.
- This MD is not a current/live stock screen.
- Exact DART/news URLs should be attached by the later implementation ledger if production-grade evidence traceability is required.
- No brokerage, auto-trading, or live watchlist action is implied.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_green_requires_realized_channel_reorder_and_margin_revision,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Green in C20 should require realized repeat-order/channel reorder plus margin/revision bridge, not reopening beta alone.","False positive LG생활건강 capped while 삼양식품/실리콘투 remain positive.","TRG_R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517_Stage2_Actionable|TRG_R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516_Stage2_Actionable|TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_reopening_beta_cap_without_repeat_order,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Consumer/beauty reopening policy beta is not enough when channel reorder/margin bridge is missing.","Reduces current_profile_false_positive count from 1 to 0 in this small holdout.","TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow",1,1,1,low,sector_shadow_only,"requires more R5/C18/C19/C20 holdout cases"
shadow_weight,c20_high_mae_success_4b_watch_if_positioning_overheat,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Even true C20 winners can have deep post-peak drawdowns; position/valuation overlay should activate watch rather than negate positive entry.","Silicon2 remains positive but receives 4B-watch after full-window peak proximity and later drawdown.","TRG_R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516_Stage2_Actionable",1,1,0,low,canonical_shadow_only,"risk overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_US_EXPORT_REORDER_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "C20 holdout: channel/export distribution evidence separated from reopening beta and price-only momentum."}
{"row_type": "case", "case_id": "R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_AMAZON_CHANNEL_REORDER_HIGH_MAE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "C20 holdout: channel/export distribution evidence separated from reopening beta and price-only momentum."}
{"row_type": "case", "case_id": "R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "CHINA_REOPENING_BEAUTY_FALSE_REORDER_MARGIN", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C20 holdout: channel/export distribution evidence separated from reopening beta and price-only momentum."}
{"row_type": "trigger", "trigger_id": "TRG_R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517_Stage2_Actionable", "case_id": "R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_US_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "public earnings/revision/channel evidence available by trigger date; exact DART/news URL should be attached in implementation ledger", "evidence_source": "public earnings/disclosure/news proxy; stock-web price rows verified in this MD", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 446500, "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 106.05, "MFE_1Y_pct": 176.15, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": 0.0, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2025-05-16", "peak_price": 1233000, "drawdown_after_peak_pct": -12.25, "green_lateness_ratio": 0.179, "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.43, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L11_C20_003230_20240517_446500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516_Stage2_Actionable", "case_id": "R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_AMAZON_CHANNEL_REORDER_HIGH_MAE", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "public earnings/revision/channel evidence available by trigger date; exact DART/news URL should be attached in implementation ledger", "evidence_source": "public earnings/disclosure/news proxy; stock-web price rows verified in this MD", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 28900, "MFE_30D_pct": 87.54, "MFE_90D_pct": 87.54, "MFE_180D_pct": 87.54, "MFE_1Y_pct": 87.54, "MFE_2Y_pct": null, "MAE_30D_pct": -10.38, "MAE_90D_pct": -10.38, "MAE_180D_pct": -16.26, "MAE_1Y_pct": -18.34, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -57.01, "green_lateness_ratio": 0.561, "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing_but_high_mae", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L11_C20_257720_20240516_28900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow", "case_id": "R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "CHINA_REOPENING_BEAUTY_FALSE_REORDER_MARGIN", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-05-10", "evidence_available_at_that_date": "public earnings/revision/channel evidence available by trigger date; exact DART/news URL should be attached in implementation ledger", "evidence_source": "public earnings/disclosure/news proxy; stock-web price rows verified in this MD", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 466000, "MFE_30D_pct": 3.0, "MFE_90D_pct": 3.0, "MFE_180D_pct": 3.0, "MFE_1Y_pct": 3.0, "MFE_2Y_pct": null, "MAE_30D_pct": -23.18, "MAE_90D_pct": -31.12, "MAE_180D_pct": -34.55, "MAE_1Y_pct": -37.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-23", "peak_price": 480000, "drawdown_after_peak_pct": -39.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L11_C20_051900_20240510_466000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R5L11_C20_003230_STAGE3_GREEN_20240603", "case_id": "R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_K_BEAUTY_STAGE3_GREEN_LABEL_COMPARISON", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "green_strictness_stress_test|canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "later confirmed revision / market recognition trigger", "evidence_source": "stock-web entry row plus public earnings/revision proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 587000, "MFE_30D_pct": 22.32, "MFE_90D_pct": 22.32, "MFE_180D_pct": 56.73, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.39, "MAE_90D_pct": -22.4, "MAE_180D_pct": -22.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-16", "peak_price": 1233000, "drawdown_after_peak_pct": -12.25, "green_lateness_ratio": 0.179, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "label_comparison_only", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L11_C20_003230_20240603_587000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same_case_green_label_comparison", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L11_C20_257720_STAGE3_GREEN_20240603", "case_id": "R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_K_BEAUTY_STAGE3_GREEN_LABEL_COMPARISON", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "green_strictness_stress_test|canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "later confirmed revision / market recognition trigger", "evidence_source": "stock-web entry row plus public earnings/revision proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 43100, "MFE_30D_pct": 25.75, "MFE_90D_pct": 25.75, "MFE_180D_pct": 25.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.44, "MAE_90D_pct": -25.41, "MAE_180D_pct": -43.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -57.01, "green_lateness_ratio": 0.561, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "label_comparison_only", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L11_C20_257720_20240603_43100", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same_case_green_label_comparison", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517", "trigger_id": "TRG_R5L11_C20_003230_SAMYANG_EXPORT_RAMEN_20240517_Stage2_Actionable", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 7, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_mix_score": 10}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 7, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_mix_score": 10}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "export_mix_score"], "component_delta_explanation": "C20 positive: export/channel reorder and margin bridge support Green; no global axis change.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516", "trigger_id": "TRG_R5L11_C20_257720_SILICON2_GLOBAL_KBEAUTY_20240516_Stage2_Actionable", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 7, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_mix_score": 9}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 7, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_mix_score": 9}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/4B-watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C20 high-MAE success: strong channel evidence remains positive but positioning/valuation overlay should keep 4B-watch active.", "MFE_90D_pct": 87.54, "MAE_90D_pct": -10.38, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510", "trigger_id": "TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow", "symbol": "051900", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "export_mix_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "export_mix_score": 1}, "weighted_score_after": 65, "stage_label_after": "Stage2-Watch", "changed_components": ["channel_reorder_score", "export_mix_score", "revision_score", "margin_bridge_score"], "component_delta_explanation": "C20 counterexample: reopening beta/relative strength without realized repeat order and margin revision should be capped below Yellow/Green.", "MFE_90D_pct": 3.0, "MAE_90D_pct": -31.12, "score_return_alignment_label": "misaligned_before_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 0, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["current_profile_false_positive", "high_mae_success", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R5/C20 undercovered holdout after R13; positive K-food/K-beauty distribution vs reopening-beta counterexample."}
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
next_round = R5_holdout_or_R1_loop11_restart
recommended_next_objective = C18/C19/C20 additional counterexample mining, or batch promotion review after loop_11 consumer holdout
```

## 28. Source Notes

Stock-web files checked in this research session:
- reports/e2r_calibration/ingest_summary.md and applied_scoring_diff.md for coverage/applied-axis avoidance.
- atlas/manifest.json and atlas/schema.json for price-source validation.
- atlas/symbol_profiles/003/003230.json, atlas/symbol_profiles/257/257720.json, atlas/symbol_profiles/051/051900.json.
- atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv and 2025.csv.
- atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv and 2025.csv.
- atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv and 2025.csv.
