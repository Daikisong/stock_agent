# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 12
completed_round: R5
completed_loop: 12
next_round: R6
next_loop: 12
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R5_loop_12_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated`.

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

This file does not re-prove those global axes. It stress-tests them in R5/C18, where a consumer brand can look strong on the surface while the actual mechanism depends on whether export/channel reorder turns into margin and revision.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
loop = 12
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`, so the round-sector consistency gate passes. C18 is selected because the prior local R5 loop10/11 files were concentrated in C20 beauty/food global distribution, while C18 still needed a cleaner export-channel reorder vs. brand-headline false-positive split.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 state contained R5 loop10 and loop11 C20 files. The immediately prior generated file was R4 loop12 with `next_round = R5` and `next_loop = 12`, so this file uses R5 loop12.

```text
same_symbol_same_trigger_date_research = avoided
same_canonical_archetype_research = allowed
same_archetype_new_symbol_count = 4
new_trigger_family_count = 4
reused_case_count = 1  # BINGGRAE 4B overlay only
```

Novelty logic: this is not another C20 K-beauty/K-food rerun. It shifts to C18 and asks a narrower question: **is there observable export/channel reorder that becomes margin bridge and revision, or is the signal only brand/geography beta?**

## 4. Stock-Web OHLC Input / Price Source Validation

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
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Stock-Web schema basis: tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE use high/low over forward tradable rows. The basis is raw/unadjusted, so selected 180D windows are blocked if they overlap corporate-action candidate dates.

## 5. Historical Eligibility Gate

|symbol|company|profile|corporate_action_candidate_dates|selected window status|
|---:|---|---|---|---|
|004370|농심|`atlas/symbol_profiles/004/004370.json`|1997-05-08, 1997-07-21, 2000-07-28, 2003-07-18|clean for 2023-05-16|
|005180|빙그레|`atlas/symbol_profiles/005/005180.json`|1995-09-29, 1996-09-25, 1998-12-15|clean for 2024-05-17 and 2024-06-10|
|271560|오리온|`atlas/symbol_profiles/271/271560.json`|none|clean for 2023-04-28|
|097950|CJ제일제당|`atlas/symbol_profiles/097/097950.json`|none|clean for 2023-05-10|

All representative triggers are historical, have stock-web tradable entry rows, have at least 180 forward trading days by manifest max date, and have positive OHLCV rows.

## 6. Canonical Archetype Compression Map

|fine_archetype_id|canonical_archetype_id|include logic|guard / exclude logic|
|---|---|---|---|
|RAMEN_US_EXPORT_REORDER_MARGIN_BRIDGE|C18|export/channel reorder plus margin bridge|domestic defensive brand rerating alone|
|ICECREAM_DAIRY_EXPORT_REORDER_MARGIN_SURGE|C18|export/product mix conversion plus earnings surprise|seasonality-only price spike|
|CHINA_REOPENING_BRAND_BETA_WITHOUT_REORDER|C18 guarded|brand and geography exposure can be watch-only|no positive Stage2 without fresh reorder/margin proof|
|KFOOD_BRAND_EXPORT_HEADLINE_INPUT_COST_MARGIN_TRAP|C18 guarded|large food brand with global narrative|block if input-cost/margin bridge contradicts thesis|

Mechanism analogy: C18 is not the shop sign; it is the repeat purchase order behind the counter. A famous brand can glow in the window, but if reorder and margin do not walk through the door together, the signal should stay in watch mode.

## 7. Case Selection Summary

|case_id|symbol|company|case_type|positive_or_counterexample|best_entry|MFE90|MAE90|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|R5L12-C18-NONGSHIM-20230516-US-CHANNEL-REORDER|004370|농심|structural_success|positive|2023-05-16|11.5|-9.39|current_profile_too_late|
|R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE|005180|빙그레|high_mae_success|positive|2024-05-17|34.09|-9.29|current_profile_correct|
|R5L12-C18-ORION-20230428-CHINA-BRAND-BETA-FAILED|271560|오리온|failed_rerating|counterexample|2023-04-28|2.0|-20.43|current_profile_false_positive|
|R5L12-C18-CJFOOD-20230510-KFOOD-MARGIN-TRAP|097950|CJ제일제당|false_positive_green|counterexample|2023-05-10|3.42|-19.28|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 2
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
representative_trigger_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The useful split is not “food winners vs. food losers.” It is “reorder-to-margin bridge vs. headline without conversion.” `농심` and `빙그레` show the first path. `오리온` and `CJ제일제당` show why the current profile still needs a C18-specific guard.

## 9. Evidence Source Map

|case_id|evidence family|Stage2 evidence|Stage3 evidence|4B/4C evidence|
|---|---|---|---|---|
|R5L12-C18-NONGSHIM-20230516-US-CHANNEL-REORDER|US/overseas ramen reorder + margin bridge|public earnings event, relative strength, overseas channel quality|confirmed margin/revision later|late Green shows upside already compressed|
|R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE|export/product mix + margin surprise|earnings shock, channel mix, relative strength|financial visibility|2024-06-10 valuation/positioning 4B overlay|
|R5L12-C18-ORION-20230428-CHINA-BRAND-BETA-FAILED|China/reopening brand beta|brand/geography narrative only|missing reorder acceleration|thesis evidence broke as price failed|
|R5L12-C18-CJFOOD-20230510-KFOOD-MARGIN-TRAP|K-food headline with input-cost drag|large brand/global narrative only|missing margin bridge|input-cost/margin trap blocked positive stage|

Evidence source IDs are deliberately left as research-proxy labels in this v12 MD. Implementation must attach exact DART/KIND/news/report IDs before any promotion batch.

## 10. Price Data Source Map

|symbol|company|tradable shard|profile|
|---:|---|---|---|
|004370|농심|`atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv`|`atlas/symbol_profiles/004/004370.json`|
|005180|빙그레|`atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv`|`atlas/symbol_profiles/005/005180.json`|
|271560|오리온|`atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv`|`atlas/symbol_profiles/271/271560.json`|
|097950|CJ제일제당|`atlas/ohlcv_tradable_by_symbol_year/097/097950/2023.csv`|`atlas/symbol_profiles/097/097950.json`|

## 11. Case-by-Case Trigger Grid

|trigger_id|trigger_type|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak|current_profile_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L12_C18_NONGSHIM_T2A_20230516|Stage2-Actionable|2023-05-16|426,000|7.04|11.5|17.37|-7.39|-9.39|-9.39|2023-10-10 500,000|current_profile_too_late|representative|
|R5L12_C18_NONGSHIM_GREEN_20231113|Stage3-Green|2023-11-13|488,000|0.41|0.41|0.41|-17.01|-17.01|-17.01|2023-11-14 493,000|current_profile_too_late|label_comparison_only|
|R5L12_C18_BINGGRAE_T2A_20240517|Stage2-Actionable|2024-05-17|88,300|34.09|34.09|34.09|-9.29|-9.29|-31.71|2024-06-11 118,400|current_profile_correct|representative|
|R5L12_C18_BINGGRAE_T4B_20240610|Stage4B|2024-06-10|112,100|5.62|5.62|5.62|-27.56|-44.87|-46.21|2024-06-11 118,400|current_profile_correct|4B_overlay_only|
|R5L12_C18_ORION_T2_REJECT_20230428|Stage2-candidate-rejected|2023-04-28|144,900|2.0|2.0|2.0|-15.11|-20.43|-25.74|2023-05-08 147,800|current_profile_false_positive|representative|
|R5L12_C18_CJFOOD_T2_REJECT_20230510|Stage2-candidate-rejected|2023-05-10|321,500|3.42|3.42|3.42|-14.93|-19.28|-19.28|2023-05-10 332,500|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

|case|entry|entry_price|90D MFE/MAE|180D MFE/MAE|interpretation|
|---|---|---|---|---|---|
|농심|2023-05-16|426,000|11.5 / -9.39|17.37 / -9.39|moderate_structural_success|
|빙그레|2024-05-17|88,300|34.09 / -9.29|34.09 / -31.71|high_mae_success|
|오리온|2023-04-28|144,900|2.0 / -20.43|2.0 / -25.74|failed_rerating|
|CJ제일제당|2023-05-10|321,500|3.42 / -19.28|3.42 / -19.28|false_positive_green_blocked_by_C18_guard|

### Stock-Web row anchors used

```text
004370 농심: 2023-05-16 close 426,000; observed representative peak 2023-10-10 high 500,000; 180D low anchor 386,000 near 2023-06-30 window.
005180 빙그레: 2024-05-17 close 88,300; observed peak 2024-06-11 high 118,400; post-peak low anchor 60,300 on 2024-11-13.
271560 오리온: 2023-04-28 close 144,900; observed forward peak 147,800 on 2023-05-08; 180D low anchor 107,600 on 2023-12-19.
097950 CJ제일제당: 2023-05-10 close 321,500; observed forward high 332,500 on entry date; 90D/180D low anchor 259,500 on 2023-07-07.
```

## 13. Current Calibrated Profile Stress Test

|case|current profile decision|actual price alignment|verdict|
|---|---|---|---|
|농심|likely waits for stronger Green confirmation despite Stage2-Actionable signal|Stage2 worked moderately; Green near 2023-11 sat close to high and had poor forward MFE|current_profile_too_late|
|빙그레|promotes Stage2-Actionable with non-price earnings/channel evidence|large short-run MFE, then severe drawdown requiring 4B overlay|current_profile_correct|
|오리온|could over-promote brand/geography quality as Stage2/Yellow|MFE capped near +2%, MAE deepened below -20%|current_profile_false_positive|
|CJ제일제당|could over-promote K-food/global brand headline|MFE capped near +3%, MAE near -19%|current_profile_false_positive|

Current calibrated profile answers:

```text
stage2_actionable_evidence_bonus = useful for true reorder cases, too generous for brand/geography headlines
Yellow threshold 75 = acceptable only after C18 reorder-to-margin gate
Green threshold 87 / revision 55 = too late for Nongshim if used as the first actionable signal
price_only_blowoff guard = kept
full 4B non-price requirement = strengthened by Binggrae 2024-06-10
hard 4C routing = kept for ORION/CJFOOD thesis-break protection
```

## 14. Stage2 / Yellow / Green Comparison

`농심` provides the cleanest Green lateness audit. Stage2-Actionable on 2023-05-16 entered at 426,000. The observed full-window peak was 500,000. A later Green-style confirmation around 2023-11-13 entered near 488,000.

```text
green_lateness_ratio = (488000 - 426000) / (500000 - 426000) = 0.84
interpretation = Green captured the label but missed most of the actionable C18 upside.
```

`빙그레` also shows why Stage2 and 4B must be separated. The Stage2 entry worked; the later 2024-06-10/11 zone was not a new entry proof but a 4B overlay zone.

## 15. 4B Local vs Full-window Timing Audit

|case|Stage2 entry|4B entry|local peak|full-window peak|local proximity|full-window proximity|verdict|
|---|---:|---:|---:|---:|---:|---:|---|
|빙그레 2024|88,300|112,100|118,400|118,400|0.79|0.79|good_full_window_4B_timing_when_non_price_evidence_attached|

The 4B row is not a chart-only call. The price had become vertical, but the valid 4B evidence type is `valuation_blowoff + positioning_overheat`, and the row is explicitly `4B_overlay_only`.

## 16. 4C Protection Audit

|case|4C label|reason|
|---|---|---|
|오리온|hard_4c_success|brand/geography beta did not convert to C18 reorder acceleration; blocking protected against -20% to -25% MAE path|
|CJ제일제당|hard_4c_success|input-cost/margin trap invalidated the K-food headline before price-only thesis promotion|
|빙그레|thesis_break_watch_only|4B was enough during this window; later 4C requires explicit export/margin deterioration evidence|

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = only one large sector, and C18 is narrower than all R5 consumer cases
```

No broad R5 sector rule is proposed. Beauty, food, apparel, distribution, and retail inventory behave differently enough that a sector-wide promotion would blur the mechanism.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

Proposed C18 shadow rule:

```text
C18_positive_stage_requires = export/channel reorder evidence + margin bridge or revision confirmation
C18_brand_beta_guard = brand/geography/reopening headline alone cannot exceed Stage2-Watch
C18_input_cost_margin_blocker = if input cost or margin bridge contradicts reorder thesis, block Stage2-Actionable and Green
C18_fast_4B_after_vertical_reorder = after vertical C18 rerating, full 4B needs valuation/positioning or evidence-exhaustion signal, not price-only local peak
```

## 19. Before / After Backtest Comparison

|profile|profile_id|hypothesis|changed_axes|eligible_triggers|selected_entries|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|avg_green_lateness|avg_4B_local|avg_4B_full|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current global calibrated proxy|none|4|NONGSHIM|BINGGRAE|ORION|CJFOOD|12.74|-14.60|14.21|-21.22|50%|0|1|0.84|0.79|0.79|mixed: positive C18 works but two false positives remain|
|P0b|e2r_2_0_baseline_reference|old baseline reference|looser Stage2/Green|4|all four|12.74|-14.60|14.21|-21.22|50%+|0|1|0.84|0.79|0.79|worse because brand beta is over-promoted|
|P1|sector_specific_candidate_profile|R5 sector: require channel reorder plus margin bridge|consumer_export_reorder_gate + margin_bridge_min|2|NONGSHIM|BINGGRAE|22.80|-9.34|25.73|-20.55|0%|0|1|0.84|0.79|0.79|better precision, no missed structural among this sample|
|P2|canonical_archetype_candidate_profile|C18: export reorder must convert to margin/revision|C18_reorder_to_margin_bridge_gate|2|NONGSHIM|BINGGRAE|22.80|-9.34|25.73|-20.55|0%|0|1|0.84|0.79|0.79|best balance for this loop|
|P3|counterexample_guard_profile|block brand beta and cost-inflation margin traps|brand_beta_guard + input_cost_margin_blocker|2|NONGSHIM|BINGGRAE|22.80|-9.34|25.73|-20.55|0%|0|1|0.84|0.79|0.79|guard profile keeps positives and rejects ORION/CJFOOD|

## 20. Score-Return Alignment Matrix

|case|before score/stage|after score/stage|90D MFE/MAE|alignment|
|---|---|---|---|---|
|농심|72 / Stage2-Actionable|78 / Stage3-Yellow|+11.50 / -9.39|after score modestly improves without pretending it was a clean Green|
|빙그레|76 / Stage2-Actionable|84 / Stage3-Yellow|+34.09 / -9.29|strong positive, but 4B overlay required after vertical move|
|오리온|75 / false-positive Yellow risk|63 / Stage2-Watch-Rejected|+2.00 / -20.43|guard improves alignment|
|CJ제일제당|74 / false-positive Stage2 risk|58 / Stage2-Watch-Rejected|+3.42 / -19.28|input-cost/margin blocker improves alignment|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L5_CONSUMER_BRAND_DISTRIBUTION|C18_CONSUMER_EXPORT_CHANNEL_REORDER|FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE|2|2|1|2|4|1|6|4|3|false|true|C18 now has positive/counterexample split, but more apparel/brand-retail C18 holdouts remain|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE as 4B overlay only
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: brand/geography beta without reorder, input-cost margin trap, Green confirmation too late after reorder move
new_axis_proposed: C18_reorder_to_margin_bridge_gate, C18_brand_beta_guard, C18_input_cost_margin_blocker, C18_fast_4B_after_vertical_reorder
existing_axis_strengthened: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- symbol profile availability and corporate-action window status
- actual stock-web 1D OHLC entry and forward-window anchor rows
- MFE/MAE proxy calculations from tradable_raw OHLC
- C18 positive/counterexample balance
- same-entry dedupe and 4B overlay-only separation
```

Not validated in this MD:

```text
- exact DART/KIND filing IDs for every evidence event
- live/current stock candidate status
- production code behavior
- brokerage execution
- global scoring changes outside C18 shadow rows
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_reorder_to_margin_bridge_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,Require export/channel reorder plus margin/revision conversion before positive Stage2 promotion,Rejected ORION/CJFOOD while retaining NONGSHIM/BINGGRAE,R5L12_C18_NONGSHIM_T2A_20230516|R5L12_C18_BINGGRAE_T2A_20240517|R5L12_C18_ORION_T2_REJECT_20230428|R5L12_C18_CJFOOD_T2_REJECT_20230510,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C18_input_cost_margin_blocker,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,Block K-food/brand headline when input cost or margin bridge contradicts reorder thesis,Reduced false positive labels for CJFOOD and similar brand narratives,R5L12_C18_CJFOOD_T2_REJECT_20230510,1,1,1,low,canonical_shadow_only,requires more R5 cases before promotion
shadow_weight,C18_fast_4B_after_vertical_reorder,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,After vertical C18 move, require non-price valuation/positioning evidence for full 4B,Correctly marks BINGGRAE 2024-06-10 as overlay rather than new positive entry,R5L12_C18_BINGGRAE_T4B_20240610,1,0,0,low,overlay_shadow_only,4B only; not entry calibration
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L12-C18-NONGSHIM-20230516-US-CHANNEL-REORDER", "symbol": "004370", "company_name": "농심", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L12_C18_NONGSHIM_T2A_20230516", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2-Actionable captured a moderate, real export/channel rerating; waiting for Green left much of the move already priced.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "US/overseas ramen channel reorder plus margin improvement beat simple domestic brand beta."}
{"row_type": "case", "case_id": "R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R5L12_C18_BINGGRAE_T2A_20240517", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2-Actionable was useful, but the move required a fast 4B overlay once valuation/positioning outran incremental evidence.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Export/seasonal product channel expansion converted into earnings surprise, then quickly became an overheat case."}
{"row_type": "case", "case_id": "R5L12-C18-ORION-20230428-CHINA-BRAND-BETA-FAILED", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R5L12_C18_ORION_T2_REJECT_20230428", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Brand/geography beta without fresh reorder acceleration produced poor 90D/180D alignment.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "China/reopening defensive brand narrative was not enough without reorder acceleration or margin revision."}
{"row_type": "case", "case_id": "R5L12-C18-CJFOOD-20230510-KFOOD-MARGIN-TRAP", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R5L12_C18_CJFOOD_T2_REJECT_20230510", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-food export/brand headline was overwhelmed by cost, margin, and non-reorder evidence weakness.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The brand was real, but the channel reorder signal was too mixed for positive Stage2 promotion."}
{"row_type": "trigger", "trigger_id": "R5L12_C18_NONGSHIM_T2A_20230516", "case_id": "R5L12-C18-NONGSHIM-20230516-US-CHANNEL-REORDER", "symbol": "004370", "company_name": "농심", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_US_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "food_export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "evidence_available_at_that_date": "Q1/early-2023 earnings and channel commentary indicated overseas ramen demand, U.S. subsidiary contribution, price/mix and margin bridge rather than only domestic defensive demand.", "evidence_source": "public quarterly disclosure / earnings-call proxy; attach DART-KIND-news IDs during implementation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-16", "entry_price": 426000, "MFE_30D_pct": 7.04, "MFE_90D_pct": 11.5, "MFE_180D_pct": 17.37, "MFE_1Y_pct": 17.37, "MFE_2Y_pct": null, "MAE_30D_pct": -7.39, "MAE_90D_pct": -9.39, "MAE_180D_pct": -9.39, "MAE_1Y_pct": -9.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-10", "peak_price": 500000, "drawdown_after_peak_pct": -18.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "moderate_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L12_C18_NONGSHIM_20230516", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L12_C18_NONGSHIM_GREEN_20231113", "case_id": "R5L12-C18-NONGSHIM-20230516-US-CHANNEL-REORDER", "symbol": "004370", "company_name": "농심", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_US_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "food_export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2023-11-13", "evidence_available_at_that_date": "By Q3 confirmation, more of the export/margin bridge was visible, but the entry sat close to the observed cycle high.", "evidence_source": "public quarterly disclosure / earnings-call proxy; attach IDs later", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-13", "entry_price": 488000, "MFE_30D_pct": 0.41, "MFE_90D_pct": 0.41, "MFE_180D_pct": 0.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.01, "MAE_90D_pct": -17.01, "MAE_180D_pct": -17.01, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-14", "peak_price": 493000, "drawdown_after_peak_pct": -18.9, "green_lateness_ratio": 0.84, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "green_after_most_upside", "four_b_evidence_type": ["valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "late_green_label_comparison", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L12_C18_NONGSHIM_20231113", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case as Stage2 row; used only for Green lateness audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L12_C18_BINGGRAE_T2A_20240517", "case_id": "R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ICECREAM_DAIRY_EXPORT_REORDER_MARGIN_SURGE", "sector": "food_export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "Q1/early-2024 earnings surprise and export/seasonal channel mix showed non-price evidence, not just summer-seasonality price action.", "evidence_source": "public quarterly disclosure / earnings-news proxy; attach DART-KIND-news IDs during implementation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 88300, "MFE_30D_pct": 34.09, "MFE_90D_pct": 34.09, "MFE_180D_pct": 34.09, "MFE_1Y_pct": 34.09, "MFE_2Y_pct": null, "MAE_30D_pct": -9.29, "MAE_90D_pct": -9.29, "MAE_180D_pct": -31.71, "MAE_1Y_pct": -31.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -49.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "needs_fast_4B_overlay_after_vertical_move", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L12_C18_BINGGRAE_20240517", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L12_C18_BINGGRAE_T4B_20240610", "case_id": "R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ICECREAM_DAIRY_EXPORT_REORDER_MARGIN_SURGE", "sector": "food_export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-06-10", "evidence_available_at_that_date": "After a near-vertical move, valuation/positioning risk existed; full 4B is valid only because the risk overlay is non-price and tied to evidence exhaustion/positioning, not because the chart had a local peak.", "evidence_source": "price + valuation/positioning overlay research proxy; attach exact valuation/research evidence later", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-10", "entry_price": 112100, "MFE_30D_pct": 5.62, "MFE_90D_pct": 5.62, "MFE_180D_pct": 5.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.56, "MAE_90D_pct": -44.87, "MAE_180D_pct": -46.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -49.07, "green_lateness_ratio": 0.79, "four_b_local_peak_proximity": 0.79, "four_b_full_window_peak_proximity": 0.79, "four_b_timing_verdict": "good_full_window_4B_timing_when_non_price_evidence_attached", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success_if_export_margin_reversal_confirmed_later", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L12_C18_BINGGRAE_20240610", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same symbol but different trigger family: Stage4B overlay timing, not a second entry case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L12_C18_ORION_T2_REJECT_20230428", "case_id": "R5L12-C18-ORION-20230428-CHINA-BRAND-BETA-FAILED", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "CHINA_REOPENING_BRAND_BETA_WITHOUT_REORDER", "sector": "food_brand", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "counterexample_mining|residual_false_positive_mining", "trigger_type": "Stage2-candidate-rejected", "trigger_date": "2023-04-27", "evidence_available_at_that_date": "China/reopening and brand quality narrative existed, but fresh channel reorder acceleration and margin revision were not strong enough at the trigger date.", "evidence_source": "public narrative/news + monthly sales proxy; exact links deferred", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-28", "entry_price": 144900, "MFE_30D_pct": 2.0, "MFE_90D_pct": 2.0, "MFE_180D_pct": 2.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.11, "MAE_90D_pct": -20.43, "MAE_180D_pct": -25.74, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-08", "peak_price": 147800, "drawdown_after_peak_pct": -25.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "candidate_blocked_before_full_4B", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L12_C18_ORION_20230428", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L12_C18_CJFOOD_T2_REJECT_20230510", "case_id": "R5L12-C18-CJFOOD-20230510-KFOOD-MARGIN-TRAP", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_BRAND_EXPORT_HEADLINE_INPUT_COST_MARGIN_TRAP", "sector": "food_brand", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "counterexample_mining|residual_false_positive_mining", "trigger_type": "Stage2-candidate-rejected", "trigger_date": "2023-05-10", "evidence_available_at_that_date": "K-food/global brand narrative existed, but input cost and margin pressure prevented a clean reorder-to-margin bridge.", "evidence_source": "public quarterly disclosure / earnings-news proxy; exact IDs deferred", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2023.csv", "profile_path": "atlas/symbol_profiles/097/097950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-10", "entry_price": 321500, "MFE_30D_pct": 3.42, "MFE_90D_pct": 3.42, "MFE_180D_pct": 3.42, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.93, "MAE_90D_pct": -19.28, "MAE_180D_pct": -19.28, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-10", "peak_price": 332500, "drawdown_after_peak_pct": -19.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "candidate_blocked_before_full_4B", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green_blocked_by_C18_guard", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L12_C18_CJFOOD_20230510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L12-C18-NONGSHIM-20230516-US-CHANNEL-REORDER", "trigger_id": "R5L12_C18_NONGSHIM_T2A_20230516", "symbol": "004370", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 14, "relative_strength_score": 12, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 15, "relative_strength_score": 12, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["channel_reorder_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow profile promotes only export/channel reorder that converts into margin/revision; it demotes brand narrative when input-cost or channel-sell-through evidence is missing.", "MFE_90D_pct": 11.5, "MAE_90D_pct": -9.39, "score_return_alignment_label": "moderate_structural_success", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L12-C18-BINGGRAE-20240517-EXPORT-MARGIN-SURGE", "trigger_id": "R5L12_C18_BINGGRAE_T2A_20240517", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 15, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 17, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["channel_reorder_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow profile promotes only export/channel reorder that converts into margin/revision; it demotes brand narrative when input-cost or channel-sell-through evidence is missing.", "MFE_90D_pct": 34.09, "MAE_90D_pct": -9.29, "score_return_alignment_label": "high_mae_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L12-C18-ORION-20230428-CHINA-BRAND-BETA-FAILED", "trigger_id": "R5L12_C18_ORION_T2_REJECT_20230428", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 5, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch-Rejected", "changed_components": ["channel_reorder_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow profile promotes only export/channel reorder that converts into margin/revision; it demotes brand narrative when input-cost or channel-sell-through evidence is missing.", "MFE_90D_pct": 2.0, "MAE_90D_pct": -20.43, "score_return_alignment_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L12-C18-CJFOOD-20230510-KFOOD-MARGIN-TRAP", "trigger_id": "R5L12_C18_CJFOOD_T2_REJECT_20230510", "symbol": "097950", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch-Rejected", "changed_components": ["channel_reorder_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow profile promotes only export/channel reorder that converts into margin/revision; it demotes brand narrative when input-cost or channel-sell-through evidence is missing.", "MFE_90D_pct": 3.42, "MAE_90D_pct": -19.28, "score_return_alignment_label": "false_positive_green_blocked_by_C18_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "scheduled_round": "R5", "scheduled_loop": "12", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "new symbols 4, new trigger families 4, counterexample gap filled for R5/C18", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["brand_or_geography_beta_without_channel_reorder", "input_cost_margin_trap", "green_confirmation_too_late_after_reorder_move"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R5
completed_loop = 12
next_round = R6
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source files inspected during this run:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/004/004370.json
atlas/symbol_profiles/005/005180.json
atlas/symbol_profiles/271/271560.json
atlas/symbol_profiles/097/097950.json
atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv
atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv
atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv
atlas/ohlcv_tradable_by_symbol_year/097/097950/2023.csv
```

Evidence-source hardening is deferred. This MD is a historical calibration artifact and contains no current-stock recommendation or live watchlist.

