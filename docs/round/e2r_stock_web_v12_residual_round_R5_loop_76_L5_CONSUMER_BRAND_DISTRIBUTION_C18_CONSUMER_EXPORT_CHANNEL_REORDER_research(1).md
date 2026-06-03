# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R5
scheduled_loop = 76
completed_round = R5
completed_loop = 76
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C
output_file = e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **4** new independent cases, **2** counterexamples, and **4** current-profile residual errors for **R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER**.

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

This file does **not** re-prove the global Stage2 bonus or Green lateness. The residual question is narrower: in C18 consumer export/channel reorder cycles, when does a K-food or processed-food export headline become a company-level reorder/margin bridge, and when is it only a sector beta that should be capped or routed to 4B/4C watch?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R5 |
| scheduled_loop | 76 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| fine_archetype_id | K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C |
| loop_objective | sector_specific_rule_discovery \| canonical_archetype_compression \| counterexample_mining \| 4B_non_price_requirement_stress_test \| coverage_gap_fill |

R5 maps to L5 consumer/brand/distribution. C18 was selected because the immediately preceding R5 set has already covered C20 beauty/food global distribution repeatedly and C19 apparel/brand inventory once. This run fills a different C18 branch: **K-food/process-food export reorder versus sector-theme beta / post-spike 4B/4C**.

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent` source code was opened. Local residual MDs show recent R5 coverage:

```text
R5 Loop 71: C20, symbols 192820, 161890, 214420, 226320
R5 Loop 72: C18, symbols 003230, 005180, 383220, 081660
R5 Loop 73: C19, symbols 036620, 337930, 298540, 031430
R5 Loop 74: C18, symbols 011150, 017810, 103840, 271560
R5 Loop 75: C20, symbols 241710, 950140, 051900, 439090
Previous completed round from current session: R4 / Loop 76
Scheduled next slot: R5 / Loop 76
```

Selected symbols for this file are **004370, 280360, 001680, 049770**. None repeats the recent R5 symbol set. All four are treated as same-archetype new-symbol cases.

```text
minimum_new_independent_case_ratio = 1.00
minimum_new_symbol_count = 4
minimum_counterexample_count = 2
minimum_positive_case_count = 2
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
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

The stock-web manifest max date is **2026-02-20**. No price after this date is inferred. All quantitative windows below use `tradable_raw` OHLC rows under `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | profile status |
|---|---|---|---|
| 004370 | 농심 | atlas/symbol_profiles/004/004370.json | corporate_action_candidate_dates=[1997-05-08,1997-07-21,2000-07-28,2003-07-18]; no overlap with 2024-05-17~D+180; clean_180D_window |
| 280360 | 롯데웰푸드 | atlas/symbol_profiles/280/280360.json | corporate_action_candidate_dates=[2019-01-04,2022-07-20]; no overlap with 2024-05-17~D+180; clean_180D_window |
| 001680 | 대상 | atlas/symbol_profiles/001/001680.json | corporate_action_candidate_dates=[1996-01-03,1997-11-25,1998-08-31,1999-04-29,2001-05-07,2005-08-05]; no overlap; clean_180D_window |
| 049770 | 동원F&B | atlas/symbol_profiles/049/049770.json | corporate_action_candidate_dates=[2010-10-25,2023-04-19]; profile last_date=2025-07-09 so 180D window is available; clean_180D_window |

All four representative Stage2 rows pass the 180D forward-window gate. No corporate-action candidate overlaps the entry date through D+180 window.

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C
```

Fine-archetype compression:

| fine route | canonical mapping | treatment |
|---|---|---|
| ramen / processed-food export reorder | C18_CONSUMER_EXPORT_CHANNEL_REORDER | promote only with company-level export reorder + margin bridge |
| confectionery / snack export and gross-margin recovery | C18_CONSUMER_EXPORT_CHANNEL_REORDER | positive if sell-through and margin conversion visible; attach 4B if spike compresses |
| K-food theme beta / peer sympathy | C18_CONSUMER_EXPORT_CHANNEL_REORDER | cap at Stage2-Watch until repeat reorder and inventory quality are confirmed |
| staple-food distribution beta | C18_CONSUMER_EXPORT_CHANNEL_REORDER | cap at Stage2-Watch or 4B-watch if no durable channel proof |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | entry_date | entry_price | current_profile_verdict |
|---|---|---|---|---|---:|---:|---|
| R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS | 004370 | 농심 | high_mae_success | positive | 2024-05-17 | 399000 | current_profile_4B_too_late |
| R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS | 280360 | 롯데웰푸드 | high_mae_success | positive | 2024-05-17 | 142000 | current_profile_4B_too_late |
| R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE | 001680 | 대상 | failed_rerating | counterexample | 2024-05-17 | 22400 | current_profile_false_positive |
| R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE | 049770 | 동원F&B | failed_rerating | counterexample | 2024-05-17 | 39500 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 2
calibration_usable_case_count = 4
```

The two positives support the C18 promotion path only when export reorder and margin conversion are company-level. The two counterexamples show that K-food/processed-food sector heat can generate MFE but still fail score-return alignment if sell-through, inventory quality, and repeat-order proof are weak.

## 9. Evidence Source Map

| symbol | evidence_available_at_that_date | evidence_source | evidence caveat |
|---|---|---|---|
| 004370 | Q1/early-summer food export and ramen channel momentum was visible around the trigger period. | source_proxy_only_research_note | Replace with DART/KIND/IR/news URL before production promotion. |
| 280360 | Processed-food export and margin recovery narrative was tradable around the trigger period. | source_proxy_only_research_note | Replace with DART/KIND/IR/news URL before production promotion. |
| 001680 | K-food/kimchi/sauce export and peer sympathy narrative was visible but company-level reorder proof was weaker. | source_proxy_only_research_note | Used as counterexample; no production promotion without hard evidence URL. |
| 049770 | Staple-food / processed-food export sympathy was visible but not enough for durable Stage3. | source_proxy_only_research_note | Used as counterexample; no production promotion without hard evidence URL. |

## 10. Price Data Source Map

| symbol | shard | profile | entry rows used |
|---|---|---|---|
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv | atlas/symbol_profiles/004/004370.json | 2024-05-17 row: o=404000, h=415500, l=392000, c=399000, v=94916 |
| 280360 | atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv | atlas/symbol_profiles/280/280360.json | 2024-05-17 row: o=138700, h=147300, l=138700, c=142000, v=70879 |
| 001680 | atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv | atlas/symbol_profiles/001/001680.json | 2024-05-17 row: o=22150, h=23050, l=21700, c=22400, v=900106 |
| 049770 | atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv | atlas/symbol_profiles/049/049770.json | 2024-05-17 row: o=38300, h=41600, l=37700, c=39500, v=286823 |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|---|---|
| 004370 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation | valuation_blowoff, positioning_overheat, price_only_local_peak | none |
| 280360 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat, price_only_local_peak | thesis_evidence_broken |
| 001680 | Stage2-Watch | 2024-05-16 | 2024-05-17 | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | unknown_or_not_supported | price_only_local_peak, positioning_overheat | thesis_evidence_broken |
| 049770 | Stage2-Watch | 2024-05-16 | 2024-05-17 | public_event_or_disclosure, relative_strength, capacity_or_volume_route | unknown_or_not_supported | price_only_local_peak, positioning_overheat | thesis_evidence_broken |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger metrics are deduplicated by `same_entry_group_id`. The 4B overlay rows are not aggregate representatives.

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 004370 | 2024-05-17 | 399000 | 50.13 | -1.75 | 50.13 | -9.65 | 50.13 | -20.55 | 2024-06-13 | 599000 | -47.08 |
| 280360 | 2024-05-17 | 142000 | 46.83 | -2.32 | 46.83 | -10.77 | 46.83 | -29.65 | 2024-06-18 | 208500 | -52.09 |
| 001680 | 2024-05-17 | 22400 | 37.95 | -3.12 | 37.95 | -12.19 | 37.95 | -18.35 | 2024-06-17 | 30900 | -40.81 |
| 049770 | 2024-05-17 | 39500 | 23.8 | -4.56 | 23.8 | -21.65 | 23.8 | -26.2 | 2024-06-17 | 48900 | -40.39 |

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | actual path | residual |
|---|---|---|---|
| 004370 | current_profile_4B_too_late | +50.13% MFE then -47.08% post-peak drawdown | Strong positive, but 4B watch should attach around the June local peak. |
| 280360 | current_profile_4B_too_late | +46.83% MFE then -52.09% post-peak drawdown | Strong positive, but the current proxy would understate post-spike risk. |
| 001680 | current_profile_false_positive | +37.95% MFE but -40.81% post-peak drawdown | K-food beta moved, but repeat-order/margin bridge was too weak for Stage3. |
| 049770 | current_profile_false_positive | +23.80% MFE but -40.39% post-peak drawdown | Staple-food beta failed to hold as a durable rerating. |

Stress-test answers:

```text
1. current calibrated profile likely promotes all four to Stage2/Yellow because price/evidence heat is visible.
2. That is only partly aligned: 004370 and 280360 were real positives but needed 4B overlay; 001680 and 049770 were false promotions.
3. Stage2 bonus is useful for true export reorder, but too generous for theme beta without sell-through proof.
4. Yellow threshold 75 is too permissive for K-food sympathy names.
5. Green threshold/revision gate should stay strict; no weakening is supported.
6. price-only blowoff guard is strengthened, not weakened.
7. full 4B non-price requirement remains correct, but C18 needs an earlier 4B-watch overlay when proximity > 0.70.
8. hard 4C routing should remain reserved for thesis break; counterexamples support 4C-watch after reorder failure.
```

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | proxy Yellow/Green issue | green_lateness_ratio |
|---|---|---|---|
| 004370 | 2024-05-17 / 399000 | Green would not be late, but it must carry 4B-watch after June spike. | not_applicable_source_proxy_green_trigger_not_verified |
| 280360 | 2024-05-17 / 142000 | Green would catch upside but expose to severe retracement. | not_applicable_source_proxy_green_trigger_not_verified |
| 001680 | 2024-05-17 / 22400 | Yellow/Green should be blocked unless repeat reorder and margin bridge are verified. | not_applicable_no_confirmed_green_trigger |
| 049770 | 2024-05-17 / 39500 | Yellow/Green should be blocked; price beta is not a channel-reorder proof. | not_applicable_no_confirmed_green_trigger |

## 15. 4B Local vs Full-window Timing Audit

| symbol | Stage2 entry | 4B watch row | full peak | local proximity | full-window proximity | verdict |
|---|---|---|---|---:|---:|---|
| 004370 | 2024-05-17 399000 | 2024-06-13 547000 | 2024-06-13 599000 | 0.74 | 0.74 | good_full_window_4B_watch_timing |
| 280360 | 2024-05-17 142000 | 2024-06-18 193300 | 2024-06-18 208500 | 0.77 | 0.77 | good_full_window_4B_watch_timing |
| 001680 | 2024-05-17 22400 | 2024-06-17 30200 | 2024-06-17 30900 | 0.92 | 0.92 | late_price_only_4B_watch_after_failed_promotion |
| 049770 | 2024-05-17 39500 | 2024-06-17 46700 | 2024-06-17 48900 | 0.77 | 0.77 | late_price_only_4B_watch_after_failed_promotion |

The four local and full-window peaks are the same observed cycle peaks for this 180D window. That makes the 4B watch useful: the spike was not just noise, but the overlay should be **risk marking**, not a standalone sell rule and not a Stage3 promotion rule.

## 16. 4C Protection Audit

| symbol | 4C label | interpretation |
|---|---|---|
| 004370 | thesis_break_watch_only | Positive structural case; the later drawdown is 4B/valuation compression, not hard 4C. |
| 280360 | thesis_break_watch_only | Positive but high-MAE; 4C should wait for actual margin/reorder evidence break. |
| 001680 | hard_4c_late | The route should move from Stage2-Watch to thesis-break watch when repeat reorder fails. |
| 049770 | hard_4c_late | The route should not be promoted after the export beta fades without sell-through proof. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c18_export_reorder_margin_gate
candidate = If L5 food/export/brand distribution case lacks company-level export reorder, sell-through, inventory quality, and margin bridge, cap at Stage2-Watch even if relative strength is high.
```

Sector rule candidate is supported because the file includes four L5 cases, two positive and two counterexamples, with clean 180D windows and a visible MFE/MAE separation.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
new_axis_proposed = c18_export_reorder_margin_gate; c18_kfood_theme_beta_cap; c18_fast_spike_4b_overlay
```

C18 should distinguish three signals:

```text
1. real export reorder + sell-through + margin conversion = Stage2-Actionable / Stage3 candidate
2. K-food or peer sympathy beta without company proof = Stage2-Watch cap
3. fast post-Stage2 rerating with local/full proximity > 0.70 = 4B-watch overlay, not full 4B unless non-price risk confirms
```

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 004370\|280360\|001680\|049770 | 39.18 | -13.57 | 39.18 | -23.69 | 0.50 | mixed: all four moved, but two should not be promoted and two require 4B overlay |
| P0b_e2r_2_0_baseline_reference | 4 | 004370\|280360\|001680\|049770 | 39.18 | -13.57 | 39.18 | -23.69 | 0.25 | underfits true positives and cannot explain false-positive distinction |
| P1_L5_food_export_reorder_shadow | 4 | 004370\|280360 only promoted | 48.48 | -10.21 | 48.48 | -25.10 | 0.00 | better separation at sector level |
| P2_C18_export_channel_reorder_shadow | 4 | 004370\|280360 only promoted | 48.48 | -10.21 | 48.48 | -25.10 | 0.00 | canonical rule candidate improves score-return alignment |
| P3_C18_counterexample_guard_profile | 4 | 001680\|049770 blocked | 48.48 | -10.21 | 48.48 | -25.10 | 0.00 | counterexample guard prevents false promotion |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | current_profile_verdict |
|---|---:|---|---:|---|---:|---:|---|
| 004370 | 84 | Stage3-Yellow risk | 88 | Stage3-Green+4B-Watch | 50.13 | -9.65 | current_profile_4B_too_late |
| 280360 | 81 | Stage3-Yellow risk | 86 | Stage3-Yellow/Green+4B-Watch | 46.83 | -10.77 | current_profile_4B_too_late |
| 001680 | 76 | Stage3-Yellow risk | 55 | Stage2-Watch / no promotion | 37.95 | -12.19 | current_profile_false_positive |
| 049770 | 74 | Stage3-Yellow risk | 52 | Stage2-Watch / no promotion | 23.8 | -21.65 | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C | 2 | 2 | 4 | 2 | 4 | 0 | 8 | 4 | 4 | true | true | C18 now has additional K-food/processed-food export reorder vs beta split; still needs external evidence URL enrichment before production promotion. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_4B_too_late, current_profile_false_positive
new_axis_proposed: c18_export_reorder_margin_gate; c18_kfood_theme_beta_cap; c18_fast_spike_4b_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web manifest max_date and price basis checked
- symbol profiles checked for all four cases
- actual tradable_raw OHLC rows used for entry/peak/min windows
- 30D/90D/180D MFE/MAE calculated from stock-web row values
- 4B local vs full-window proximity separated
- same_entry_group_id dedupe applied
- no production score changed
```

Non-validation scope:

```text
- External DART/KIND/news/IR URLs are not fully attached in this standalone file.
- Evidence rows use source_proxy_only and must be URL-enriched before any production promotion.
- No stock_agent source code was opened.
- No live candidate scan or current recommendation was performed.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_export_reorder_margin_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Require company-level export reorder + sell-through + gross-margin bridge before Stage3 promotion","Blocks two false promotions and keeps two positives with explicit 4B watch","R5L76_C18_004370_STAGE2A_20240517_RAMEN_EXPORT_REORDER_MARGIN|R5L76_C18_280360_STAGE2A_20240517_CONFECTIONERY_EXPORT_MARGIN_REORDER|R5L76_C18_001680_STAGE2_20240517_KFOOD_EXPORT_THEME_FALSE_PROMOTION|R5L76_C18_049770_STAGE2_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_fast_spike_4b_overlay,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"If post-Stage2 local rerating proximity exceeds ~0.70 and non-price confirmation is incomplete, attach 4B watch rather than Green promotion","All four cases reached local/full-window peak proximity 0.74~0.92 before large drawdown",4,4,2,medium,sector_shadow_only,"overlay only; not sell recommendation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS","symbol":"004370","company_name":"농심","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L76_C18_004370_STAGE2A_20240517_RAMEN_EXPORT_REORDER_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_aligned_but_high_mae","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Q1/early-summer food export and ramen channel momentum was visible, but later rows show the move needed a 4B overheat overlay once the local rerating compressed into June."}
{"row_type":"trigger","trigger_id":"R5L76_C18_004370_STAGE2A_20240517_RAMEN_EXPORT_REORDER_MARGIN","case_id":"R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS","symbol":"004370","company_name":"농심","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","evidence_available_at_that_date":"Q1/early-summer food export and ramen channel momentum was visible, but later rows show the move needed a 4B overheat overlay once the local rerating compressed into June.","evidence_source":"source_proxy_only_research_note; replace with DART/KIND/IR/news URL before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":399000,"MFE_30D_pct":50.13,"MFE_90D_pct":50.13,"MFE_180D_pct":50.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.75,"MAE_90D_pct":-9.65,"MAE_180D_pct":-20.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":"not_applicable_source_proxy_green_trigger_not_separately_verified","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"good_full_window_4B_watch_timing","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mae_export_reorder_with_late_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L76_C18_004370_STAGE4B_20240517_RAMEN_EXPORT_REORDER_MARGIN_OVERLAY","case_id":"R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS","symbol":"004370","company_name":"농심","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":547000,"evidence_available_at_that_date":"local rerating compression and positioning/valuation overheat after export-theme spike; overlay only, not independent entry","evidence_source":"stock_web_price_path_and_source_proxy_only_risk_note","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"good_full_window_4B_watch_timing","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS_2024-05-17","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay, not a new independent case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS","trigger_id":"R5L76_C18_004370_STAGE2A_20240517_RAMEN_EXPORT_REORDER_MARGIN","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":12,"relative_strength_score":15,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":13,"sellthrough_score":9,"inventory_quality_score":4,"gross_margin_score":11,"brand_heat_score":6,"export_reorder_score":14,"positioning_overheat_score":-3,"thesis_break_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":13,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16,"sellthrough_score":12,"inventory_quality_score":7,"gross_margin_score":14,"brand_heat_score":5,"export_reorder_score":17,"positioning_overheat_score":-12,"thesis_break_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green+4B-Watch","changed_components":["export_reorder_score","channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified export reorder + sell-through + margin bridge, but caps K-food/processed-food theme beta unless repeat-order and inventory quality are visible. Local spike compression is 4B overlay only.","MFE_90D_pct":50.13,"MAE_90D_pct":-9.65,"score_return_alignment_label":"strong_positive_aligned_but_4B_overlay_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L76_C18_280360_STAGE2A_20240517_CONFECTIONERY_EXPORT_MARGIN_REORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_aligned_but_high_mae","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Processed-food export and margin recovery narrative became tradable, but the full path behaved like a June rerating followed by inventory/multiple compression rather than a straight Green hold."}
{"row_type":"trigger","trigger_id":"R5L76_C18_280360_STAGE2A_20240517_CONFECTIONERY_EXPORT_MARGIN_REORDER","case_id":"R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","evidence_available_at_that_date":"Processed-food export and margin recovery narrative became tradable, but the full path behaved like a June rerating followed by inventory/multiple compression rather than a straight Green hold.","evidence_source":"source_proxy_only_research_note; replace with DART/KIND/IR/news URL before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv","profile_path":"atlas/symbol_profiles/280/280360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":142000,"MFE_30D_pct":46.83,"MFE_90D_pct":46.83,"MFE_180D_pct":46.83,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.32,"MAE_90D_pct":-10.77,"MAE_180D_pct":-29.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":208500,"drawdown_after_peak_pct":-52.09,"green_lateness_ratio":"not_applicable_source_proxy_green_trigger_not_separately_verified","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"good_full_window_4B_watch_timing","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_but_severe_post_peak_drawdown_requires_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L76_C18_280360_STAGE4B_20240517_CONFECTIONERY_EXPORT_MARGIN_REORDER_OVERLAY","case_id":"R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":193300,"evidence_available_at_that_date":"local rerating compression and positioning/valuation overheat after export-theme spike; overlay only, not independent entry","evidence_source":"stock_web_price_path_and_source_proxy_only_risk_note","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv","profile_path":"atlas/symbol_profiles/280/280360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"peak_date":"2024-06-18","peak_price":208500,"drawdown_after_peak_pct":-52.09,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"good_full_window_4B_watch_timing","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS_2024-05-17","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay, not a new independent case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS","trigger_id":"R5L76_C18_280360_STAGE2A_20240517_CONFECTIONERY_EXPORT_MARGIN_REORDER","symbol":"280360","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":11,"revision_score":10,"relative_strength_score":15,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12,"sellthrough_score":8,"inventory_quality_score":3,"gross_margin_score":11,"brand_heat_score":5,"export_reorder_score":13,"positioning_overheat_score":-3,"thesis_break_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":15,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":15,"sellthrough_score":11,"inventory_quality_score":6,"gross_margin_score":14,"brand_heat_score":4,"export_reorder_score":16,"positioning_overheat_score":-13,"thesis_break_score":-2},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green+4B-Watch","changed_components":["export_reorder_score","channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified export reorder + sell-through + margin bridge, but caps K-food/processed-food theme beta unless repeat-order and inventory quality are visible. Local spike compression is 4B overlay only.","MFE_90D_pct":46.83,"MAE_90D_pct":-10.77,"score_return_alignment_label":"strong_positive_aligned_but_4B_overlay_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE","symbol":"001680","company_name":"대상","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L76_C18_001680_STAGE2_20240517_KFOOD_EXPORT_THEME_FALSE_PROMOTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_failed_rerating_blocked_by_C18_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"K-food/kimchi/sauce export narrative and peer sympathy created a tradable spike, but company-level repeat reorder and margin bridge were not strong enough to sustain Stage3."}
{"row_type":"trigger","trigger_id":"R5L76_C18_001680_STAGE2_20240517_KFOOD_EXPORT_THEME_FALSE_PROMOTION","case_id":"R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE","symbol":"001680","company_name":"대상","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Watch","trigger_date":"2024-05-16","evidence_available_at_that_date":"K-food/kimchi/sauce export narrative and peer sympathy created a tradable spike, but company-level repeat reorder and margin bridge were not strong enough to sustain Stage3.","evidence_source":"source_proxy_only_research_note; replace with DART/KIND/IR/news URL before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv","profile_path":"atlas/symbol_profiles/001/001680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":22400,"MFE_30D_pct":37.95,"MFE_90D_pct":37.95,"MFE_180D_pct":37.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.12,"MAE_90D_pct":-12.19,"MAE_180D_pct":-18.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":30900,"drawdown_after_peak_pct":-40.81,"green_lateness_ratio":"not_applicable_source_proxy_green_trigger_not_separately_verified","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"price_only_local_4B_too_late_if_promoted","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"theme_spike_failed_rerating_after_peak","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L76_C18_001680_STAGE4B_20240517_KFOOD_EXPORT_THEME_FALSE_PROMOTION_OVERLAY","case_id":"R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE","symbol":"001680","company_name":"대상","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":30200,"evidence_available_at_that_date":"local rerating compression and positioning/valuation overheat after export-theme spike; overlay only, not independent entry","evidence_source":"stock_web_price_path_and_source_proxy_only_risk_note","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv","profile_path":"atlas/symbol_profiles/001/001680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"peak_date":"2024-06-17","peak_price":30900,"drawdown_after_peak_pct":-40.81,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"late_price_only_4B_watch_after_failed_promotion","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE_2024-05-17","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay, not a new independent case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE","trigger_id":"R5L76_C18_001680_STAGE2_20240517_KFOOD_EXPORT_THEME_FALSE_PROMOTION","symbol":"001680","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":5,"relative_strength_score":14,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8,"sellthrough_score":4,"inventory_quality_score":0,"gross_margin_score":5,"brand_heat_score":9,"export_reorder_score":8,"positioning_overheat_score":-2,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":-9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":2,"sellthrough_score":1,"inventory_quality_score":-8,"gross_margin_score":2,"brand_heat_score":3,"export_reorder_score":2,"positioning_overheat_score":-13,"thesis_break_score":-10},"weighted_score_after":55,"stage_label_after":"Stage2-Watch / no promotion","changed_components":["export_reorder_score","channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified export reorder + sell-through + margin bridge, but caps K-food/processed-food theme beta unless repeat-order and inventory quality are visible. Local spike compression is 4B overlay only.","MFE_90D_pct":37.95,"MAE_90D_pct":-12.19,"score_return_alignment_label":"false_positive_blocked_by_export_reorder_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","symbol":"049770","company_name":"동원F&B","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L76_C18_049770_STAGE2_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_failed_rerating_blocked_by_C18_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Staple food / processed-food export sympathy produced a short rerating, but sell-through, repeat-order, and margin confirmation were not enough for durable Stage3."}
{"row_type":"trigger","trigger_id":"R5L76_C18_049770_STAGE2_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","case_id":"R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","symbol":"049770","company_name":"동원F&B","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Watch","trigger_date":"2024-05-16","evidence_available_at_that_date":"Staple food / processed-food export sympathy produced a short rerating, but sell-through, repeat-order, and margin confirmation were not enough for durable Stage3.","evidence_source":"source_proxy_only_research_note; replace with DART/KIND/IR/news URL before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv","profile_path":"atlas/symbol_profiles/049/049770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":39500,"MFE_30D_pct":23.8,"MFE_90D_pct":23.8,"MFE_180D_pct":23.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.56,"MAE_90D_pct":-21.65,"MAE_180D_pct":-26.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":48900,"drawdown_after_peak_pct":-40.39,"green_lateness_ratio":"not_applicable_source_proxy_green_trigger_not_separately_verified","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"price_only_local_4B_too_late_if_promoted","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"staple_food_export_beta_failed_to_hold","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L76_C18_049770_STAGE4B_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE_OVERLAY","case_id":"R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","symbol":"049770","company_name":"동원F&B","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_STABLE_BRAND_VS_THEME_BETA_4B_4C","sector":"consumer_food_export_distribution","primary_archetype":"K-food export reorder / channel sell-through","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":46700,"evidence_available_at_that_date":"local rerating compression and positioning/valuation overheat after export-theme spike; overlay only, not independent entry","evidence_source":"stock_web_price_path_and_source_proxy_only_risk_note","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv","profile_path":"atlas/symbol_profiles/049/049770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"peak_date":"2024-06-17","peak_price":48900,"drawdown_after_peak_pct":-40.39,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"late_price_only_4B_watch_after_failed_promotion","four_b_evidence_type":["price_only","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE_2024-05-17","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay, not a new independent case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","trigger_id":"R5L76_C18_049770_STAGE2_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE","symbol":"049770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7,"sellthrough_score":3,"inventory_quality_score":1,"gross_margin_score":4,"brand_heat_score":7,"export_reorder_score":6,"positioning_overheat_score":-2,"thesis_break_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":1,"sellthrough_score":0,"inventory_quality_score":-9,"gross_margin_score":1,"brand_heat_score":2,"export_reorder_score":1,"positioning_overheat_score":-12,"thesis_break_score":-11},"weighted_score_after":52,"stage_label_after":"Stage2-Watch / no promotion","changed_components":["export_reorder_score","channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified export reorder + sell-through + margin bridge, but caps K-food/processed-food theme beta unless repeat-order and inventory quality are visible. Local spike compression is 4B overlay only.","MFE_90D_pct":23.8,"MAE_90D_pct":-21.65,"score_return_alignment_label":"false_positive_blocked_by_export_reorder_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"profile_aggregate","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_global_proxy","profile_hypothesis":"Current proxy over-promotes K-food theme beta and under-times 4B overlays after fast export-channel spikes.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"004370|280360|001680|049770","avg_MFE_90D_pct":39.18,"avg_MAE_90D_pct":-13.57,"avg_MFE_180D_pct":39.18,"avg_MAE_180D_pct":-23.69,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable_source_proxy_green_trigger_not_verified","avg_four_b_local_peak_proximity":0.8,"avg_four_b_full_window_peak_proximity":0.8,"score_return_alignment_verdict":"mixed: all four moved, but two should not be promoted and two require 4B overlay"}
{"row_type":"profile_aggregate","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older baseline is too conservative on real export reorder but still lacks a K-food beta false-promotion guard.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"004370|280360|001680|049770","avg_MFE_90D_pct":39.18,"avg_MAE_90D_pct":-13.57,"avg_MFE_180D_pct":39.18,"avg_MAE_180D_pct":-23.69,"false_positive_rate":0.25,"missed_structural_count":2,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.8,"avg_four_b_full_window_peak_proximity":0.8,"score_return_alignment_verdict":"underfits true positives and cannot explain false-positive distinction"}
{"row_type":"profile_aggregate","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P1_L5_food_export_reorder_shadow","profile_scope":"sector_specific","profile_hypothesis":"Within L5, promote only when export reorder, sell-through, and margin bridge are company-level; cap sympathy/theme beta and add 4B overlay after fast local rerating.","changed_axes":["c18_export_reorder_margin_gate","c18_kfood_theme_beta_cap","c18_fast_spike_4b_overlay"],"changed_thresholds":{"min_export_reorder_score_for_stage3":14,"min_sellthrough_inventory_for_green":8,"theme_beta_cap":"Stage2-Watch","post_spike_4b_proximity_watch":0.7},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"004370|280360|001680|049770","avg_MFE_90D_pct":48.48,"avg_MAE_90D_pct":-10.21,"avg_MFE_180D_pct":48.48,"avg_MAE_180D_pct":-25.1,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.8,"avg_four_b_full_window_peak_proximity":0.8,"score_return_alignment_verdict":"better separation at sector level"}
{"row_type":"profile_aggregate","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P2_C18_export_channel_reorder_shadow","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C18-specific rule: export reorder must be supported by sell-through and margin conversion. Price/peer sympathy alone is Stage2-Watch or 4B-watch, not Green.","changed_axes":["c18_export_reorder_margin_gate","c18_kfood_theme_beta_cap","c18_fast_spike_4b_overlay"],"changed_thresholds":{"min_export_reorder_score_for_stage3":14,"min_sellthrough_inventory_for_green":8,"theme_beta_cap":"Stage2-Watch","post_spike_4b_proximity_watch":0.7},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"004370|280360|001680|049770","avg_MFE_90D_pct":48.48,"avg_MAE_90D_pct":-10.21,"avg_MFE_180D_pct":48.48,"avg_MAE_180D_pct":-25.1,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.8,"avg_four_b_full_window_peak_proximity":0.8,"score_return_alignment_verdict":"canonical rule candidate improves score-return alignment"}
{"row_type":"profile_aggregate","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P3_C18_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Guard blocks K-food theme beta, staple-food sympathy, and one-off price spikes unless repeat-order and gross-margin evidence are confirmed.","changed_axes":["c18_theme_beta_cap","c18_sellthrough_inventory_guard","c18_hard_4c_thesis_break_watch"],"changed_thresholds":{"theme_beta_cap":"Stage2-Watch","hard_4c_watch_after_failed_reorder":"enabled"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"004370|280360|001680|049770","avg_MFE_90D_pct":48.48,"avg_MAE_90D_pct":-10.21,"avg_MFE_180D_pct":48.48,"avg_MAE_180D_pct":-25.1,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.8,"avg_four_b_full_window_peak_proximity":0.8,"score_return_alignment_verdict":"counterexample guard prevents false promotion"}
{"row_type":"residual_contribution","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","scheduled_round":"R5","scheduled_loop":"76","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"diversity_score_summary":"same_archetype_new_symbol +4x4; counterexample gap +2; residual error +4; wrong-round penalty 0; schema rematerialization penalty 0","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":null,"symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"none; all four representative cases have usable stock-web 180D windows; exact external evidence URLs remain source_proxy_only before production promotion","price_source":"Songdaiki/stock-web","usage":"research_note"}
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
completed_round = R5
completed_loop = 76
next_round = R6
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
primary_price_source = Songdaiki/stock-web
primary_price_source_url = https://github.com/Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
stock_agent_code_accessed = false
stock_agent_code_patched = false
production_scoring_changed = false
external_evidence_url_status = source_proxy_only; needs URL enrichment before production promotion
```

