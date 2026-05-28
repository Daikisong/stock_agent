# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 15
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE | K_FOOD_RAMEN_US_CHANNEL_REORDER_WITH_REVERSAL_RISK | LEGACY_K_FOOD_BRAND_GLOBAL_DISTRIBUTION_WITH_WEAK_MARGIN_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R5_loop_15_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This is a historical calibration artifact. It is not a live candidate scan, not a recommendation, not a stock-agent code patch, and not a price-route discovery note.

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

The loop does not re-prove these global axes. It stress-tests them inside one consumer export-channel archetype: export reorder that becomes margin bridge versus broad brand/global-distribution stories that do not close into sustained EPS/revision.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
sector = 소비재·유통·브랜드
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test
```

C18 is treated as a different mechanism from C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION. C20 is “global distribution breadth.” C18 is narrower: **repeat export/channel reorder that visibly converts into margin and revision**. In practice, it behaves like a pipe test. Popularity is the water pressure; reorder and margin bridge are whether the pipe is actually connected to cash flow.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifacts were checked only at summary/profile level, not source code.

- `reports/e2r_calibration/ingest_summary.md` indicates broad R1–R13 coverage, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows.
- `reports/e2r_calibration/calibrated_profile_report.md` indicates the current calibrated profile is already applied and lists the global axes now treated as baseline assumptions.
- This loop avoids repeating the already generated R5/C20 beauty/global distribution residual work and moves to C18 K-food export channel reorder.
- Selected symbols are new for this loop: `003230`, `004370`, `097950`.
- No `stock_agent/src/e2r` path was opened.

```text
auto_selected_coverage_gap = R5/C18 consumer export channel reorder:
  distinguish repeat export reorder + margin bridge from generic K-food/global brand rebound
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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
price_basis = tradable_raw
```

Schema fields used:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

|symbol|company|profile_path|profile summary|corporate action window status|calibration usable|
|---|---|---|---|---|---|
|003230|삼양식품|atlas/symbol_profiles/003/003230.json|active-like; available 1995–2026; 7,704 tradable rows; only candidate action 2003-07-25|clean for 2024-05-17 through 180D|true|
|004370|농심|atlas/symbol_profiles/004/004370.json|active-like; available 1995–2026; 7,742 tradable rows; candidate action dates only 1997/2000/2003|clean for 2024-05-17 through 180D|true|
|097950|CJ제일제당|atlas/symbol_profiles/097/097950.json|active-like; available 2007–2026; 4,536 tradable rows; corporate_action_candidate_count=0|clean for 2024-05-17 through 180D|true|

The 2Y window is not used because `manifest_max_date = 2026-02-20` does not provide a full 504-trading-day window for 2024-05 entries.

## 6. Canonical Archetype Compression Map

|fine_archetype_id|canonical_archetype_id|compression note|
|---|---|---|
|K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE|C18_CONSUMER_EXPORT_CHANNEL_REORDER|True reorder: export demand, capacity/volume route, and margin bridge close together.|
|K_FOOD_RAMEN_US_CHANNEL_REORDER_WITH_REVERSAL_RISK|C18_CONSUMER_EXPORT_CHANNEL_REORDER|Reorder success but with high MAE after channel/margin risk appears.|
|LEGACY_K_FOOD_BRAND_GLOBAL_DISTRIBUTION_WITH_WEAK_MARGIN_BRIDGE|C18_CONSUMER_EXPORT_CHANNEL_REORDER|Counterexample: brand/global distribution story exists, but repeat reorder and margin bridge are not strong enough for Green.|

## 7. Case Selection Summary

|case_id|symbol|company|case_type|pos/counter|fine_archetype_id|current_profile_verdict|notes|
|---|---|---|---|---|---|---|---|
|R5L15-C18-003230-SAMYANG-EXPORT-REORDER|003230|삼양식품|structural_success|positive|K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE|current_profile_correct|Buldak/global reorder translated into export-heavy margin bridge; later full-cycle 4B needs non-price evidence, not just local peak.|
|R5L15-C18-004370-NONGSHIM-EXPORT-REORDER|004370|농심|high_mae_success|positive|K_FOOD_RAMEN_US_CHANNEL_REORDER_WITH_REVERSAL_RISK|current_profile_correct|Export/channel reorder was visible and price moved, but drawdown later shows margin durability and channel concentration must cap Green.|
|R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN|097950|CJ제일제당|false_positive_green|counterexample|LEGACY_K_FOOD_BRAND_GLOBAL_DISTRIBUTION_WITH_WEAK_MARGIN_BRIDGE|current_profile_false_positive|Generic K-food/global-distribution narrative gave early MFE, but margin bridge and repeat reorder were insufficient; later price path was dominated by legacy cost/base effects.|

## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 3
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 1
new_independent_case_count = 3
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

The loop clears the minimum balance: at least one positive, one counterexample, and three calibration-usable cases.

## 9. Evidence Source Map

|symbol|trigger family|Stage2 evidence|Stage3 evidence|4B/4C evidence|
|---|---|---|---|---|
|003230|export reorder + margin bridge|1Q24 result shock, export-heavy demand, relative strength, early revision|confirmed revision, margin bridge, repeat global demand|local valuation/positioning overheat later; not full 4B without non-price confirmation|
|004370|export reorder with reversal risk|US/global ramen channel strength and relative strength|partial revision confirmation|later margin/channel slowdown risk; high MAE after positive MFE|
|097950|legacy K-food rebound false positive|generic K-food/global distribution narrative and early result improvement|weak separable reorder evidence|margin/base/legacy execution risk; watch-only thesis break, not hard 4C|

Important limitation: external evidence labels are stored as trigger-family summaries for later source-resolution. The quantitative calibration in this MD is based only on stock-web OHLC rows and clean profile windows.

## 10. Price Data Source Map

|symbol|tradable shard|profile|
|---|---|---|
|003230|atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv; atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv|atlas/symbol_profiles/003/003230.json|
|004370|atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv; atlas/ohlcv_tradable_by_symbol_year/004/004370/2025.csv|atlas/symbol_profiles/004/004370.json|
|097950|atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv; atlas/ohlcv_tradable_by_symbol_year/097/097950/2025.csv|atlas/symbol_profiles/097/097950.json|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak_date|peak_price|current_profile|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L15-C18-003230-T1|003230|삼양식품|Stage2-Actionable|2024-05-16|2024-05-17|446500|60.81|60.81|85.44|0.0|0.0|0.0|2025-05-16|1233000|current_profile_correct|representative|
|R5L15-C18-003230-T2|003230|삼양식품|Stage4B-Overlay|2024-12-16|2024-12-16|729000|9.47|31.41|69.14|-5.9|-6.58|-6.58|2025-05-16|1233000|current_profile_4B_too_early|4B_overlay_only|
|R5L15-C18-004370-T1|004370|농심|Stage2-Actionable|2024-05-16|2024-05-17|399000|50.13|50.13|50.13|-1.75|-9.65|-20.55|2024-06-13|599000|current_profile_correct|representative|
|R5L15-C18-097950-T1|097950|CJ제일제당|Stage3-Yellow|2024-05-16|2024-05-17|333500|22.19|22.19|22.19|-0.3|-10.04|-30.28|2024-06-26|407500|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 003230 삼양식품 — structural export reorder

|field|value|
|---|---|
|entry_date|2024-05-17|
|entry_price|446,500|
|entry row|2024-05-17, close 446,500|
|30D max high|718,000 on 2024-06-19|
|180D max high used for calibration|828,000 on 2025-02-06|
|1Y peak used for lateness audit|1,233,000 on 2025-05-16|
|MFE_30D_pct|60.81|
|MFE_90D_pct|60.81|
|MFE_180D_pct|85.44|
|MFE_1Y_pct|176.15|
|MAE_30D_pct|0.00|
|MAE_90D_pct|0.00|
|MAE_180D_pct|0.00|

Interpretation: this is the clean positive case. The export-reorder signal acted less like a one-day theme and more like a valve opening into a new margin regime.

### 12.2 004370 농심 — positive but high-MAE reorder

|field|value|
|---|---|
|entry_date|2024-05-17|
|entry_price|399,000|
|peak high|599,000 on 2024-06-13|
|deepest low after peak in observed calibration path|317,000 on 2024-11-15|
|MFE_30D_pct|50.13|
|MFE_90D_pct|50.13|
|MFE_180D_pct|50.13|
|MAE_30D_pct|-1.75|
|MAE_90D_pct|-9.65|
|MAE_180D_pct|-20.55|
|drawdown_after_peak_pct|-47.08|

Interpretation: the signal was real enough for Stage2/Yellow but not durable enough for automatic Green. The price path behaves like a strong first shipment that did not become a smooth replenishment cycle.

### 12.3 097950 CJ제일제당 — false-positive legacy/global narrative

|field|value|
|---|---|
|entry_date|2024-05-17|
|entry_price|333,500|
|peak high|407,500 on 2024-06-26|
|deepest low in 1Y path|226,500 on 2025-04-11|
|MFE_30D_pct|22.19|
|MFE_90D_pct|22.19|
|MFE_180D_pct|22.19|
|MAE_30D_pct|-0.30|
|MAE_90D_pct|-10.04|
|MAE_180D_pct|-30.28|
|MAE_1Y_pct|-32.08|
|drawdown_after_peak_pct|-44.42|

Interpretation: the early MFE was not enough. Without separable repeat reorder and margin bridge, the global K-food narrative became a false Green/Yelllow trap.

## 13. Current Calibrated Profile Stress Test

|case|current profile likely label|actual path|verdict|
|---|---|---|---|
|삼양식품|Stage3-Green after revision/margin confirmation|MFE180 85.44, MAE180 0.00|current_profile_correct|
|농심|Stage3-Yellow / capped Green|MFE180 50.13 but MAE180 -20.55|current_profile_correct, but high-MAE guard needed|
|CJ제일제당|Stage3-Yellow risk; could be false positive if generic channel score is too generous|MFE180 22.19 but MAE180 -30.28|current_profile_false_positive|

Axis review:

```text
stage2_actionable_evidence_bonus = kept
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened inside C18
stage3_cross_evidence_green_buffer = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept
```

## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|Stage3/Green proxy|green_lateness_ratio|interpretation|
|---|---:|---:|---:|---|
|삼양식품|446,500|647,000 proxy on 2024-06-14|0.25|Green confirmation was not badly late; export reorder was already visible and then confirmed.|
|농심|399,000|no clean Green|not_applicable|Price MFE was strong, but later MAE argues against forcing Green.|
|CJ제일제당|333,500|no Green under proposed guard|not_applicable|Generic K-food narrative should remain watch/Yellow only.|

## 15. 4B Local vs Full-window Timing Audit

삼양식품 local 4B overlay:

```text
Stage2_Actionable_entry_price = 446500
Stage4B_overlay_entry_price = 729000
local_peak_after_Stage2 = 718000
full_observed_peak_after_Stage2 = 1233000

four_b_local_peak_proximity = 1.04
four_b_full_window_peak_proximity = 0.36
four_b_timing_verdict = price_only_local_4B_too_early
```

Conclusion: in C18 export-reorder winners, a local price peak can look like a full 4B, but the cycle may still have reorder and revision legs left. This strengthens the existing rule that full 4B requires non-price evidence.

## 16. 4C Protection Audit

No hard 4C case is used for weight calibration in this loop. CJ is labeled `thesis_break_watch_only`, not hard 4C, because the evidence is a failed positive/re-rating structure rather than a discrete cancellation, regulatory rejection, forced liquidation, or accounting break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_price_only_local_4B_guard_for_export_winners
proposal = keep price-only local peak as overlay-only unless valuation blowoff is joined by revision slowdown, margin deterioration, channel slowdown, or explicit capacity/order cap.
evidence = Samyang local 4B proximity 1.04 but full-window proximity 0.36.
proposal_type = sector_shadow_only
production_scoring_changed = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER

positive gate:
  repeat_export_reorder + margin_bridge + revision_score >= Green-level confirmation

counterexample guard:
  generic K-food/global brand narrative without separable repeat reorder and segment margin bridge caps at Stage2-watch/Stage3-Yellow, not Green

risk overlay:
  high-MAE-success cases require execution/channel concentration risk component even when MFE is strong
```

Mechanism: a consumer export reorder is not “people like the brand.” It is a restocking machine. The signal is strong only when the shelf is emptied, the distributor reorders, the factory/shipments can meet it, and the incremental unit carries better margin.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|global current|No C18-specific channel reorder guard.|4|003230 T1 / 004370 T1 / 097950 T1|44.38|-6.56|52.59|-16.94|1/3|0|0.25|n/a|n/a|1.04 / 0.36|correct on two positives, false-positive risk on CJ|
|P0b|e2r_2_0_baseline_reference|rollback reference|Higher Yellow min, looser Green revision.|4|Same|44.38|-6.56|52.59|-16.94|1/3|1|0.25|n/a|n/a|not split|worse stage separation; likely late/unstable|
|P1|sector_specific_candidate_profile|L5 sector shadow|Add L5 price-only local-4B guard.|4|Same|44.38|-6.56|52.59|-16.94|1/3|0|0.25|n/a|n/a|1.04 / 0.36|improves 4B handling only|
|P2|canonical_archetype_candidate_profile|C18 canonical shadow|Promote repeat reorder + margin bridge; cap legacy/global narrative.|4|003230 T1 / 004370 T1; 097950 watch-only|55.47|-4.83|67.79|-10.28|0/2 selected|0|0.25|n/a|n/a|1.04 / 0.36|best score-return alignment|
|P3|counterexample_guard_profile|C18 guard profile|CJ-like legacy food global story cannot pass Green without segment margin bridge.|4|Block 097950 from positive promotion|55.47|-4.83|67.79|-10.28|0/2 selected|0|0.25|n/a|n/a|1.04 / 0.36|strong false-positive reduction|

## 20. Score-Return Alignment Matrix

|case|weighted_before|label_before|weighted_after|label_after|return alignment|
|---|---:|---|---:|---|---|
|삼양식품|88.0|Stage3-Green|92.0|Stage3-Green|strong positive alignment|
|농심|78.0|Stage3-Yellow|77.0|Stage3-Yellow-capped|positive but high-MAE; cap Green|
|CJ제일제당|76.0|Stage3-Yellow|68.0|Stage2-watch-only|counterexample corrected|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L5_CONSUMER_BRAND_DISTRIBUTION|C18_CONSUMER_EXPORT_CHANNEL_REORDER|K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE / K_FOOD_RAMEN_US_CHANNEL_REORDER_WITH_REVERSAL_RISK / LEGACY_K_FOOD_BRAND_GLOBAL_DISTRIBUTION_WITH_WEAK_MARGIN_BRIDGE|2|1|1|0|3|0|4|3|1|true|true|C18 now has positive + counterexample + 4B overlay, but needs one more non-ramen consumer export holdout.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - legacy_brand_global_distribution_false_positive
  - high_mae_after_export_reorder_success
  - price_only_local_4B_too_early
new_axis_proposed:
  - c18_repeat_export_reorder_margin_bridge
  - c18_legacy_brand_rebound_guard
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_cross_evidence_green_buffer
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
- stock-web manifest and schema fields
- three symbol profiles
- entry_date / entry_price from tradable shards
- MFE / MAE / peak / drawdown from stock-web tradable_raw rows
- positive and counterexample balance
- same_entry_group_id dedupe
- 4B local vs full-window split
```

Not validated:

```text
- live/current stock discovery
- 2026 watchlist
- broker/API execution
- stock_agent source code
- production scoring patch
- external source URL resolution for every historical evidence item
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_repeat_export_reorder_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+2,"Promote export-channel reorder only when repeat demand, capacity/volume route, and margin bridge close together.","Improves Samyang/Nongshim alignment while not promoting CJ legacy narrative.","R5L15-C18-003230-T1|R5L15-C18-004370-T1",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_legacy_brand_rebound_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,-3,"Generic K-food/global brand rebound without separable reorder and margin bridge should cap Stage3-Green.","Blocks CJ false positive without weakening true reorder positives.","R5L15-C18-097950-T1",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_price_only_local_peak_4b_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"In export winners, price-only local peak can arrive far before full window peak; require non-price 4B evidence.","Samyang local 4B proximity 1.04 but full-window proximity 0.36, so overlay-only.","R5L15-C18-003230-T2",1,0,0,low,sector_shadow_only,"4B overlay; not positive entry weight"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L15-C18-003230-SAMYANG-EXPORT-REORDER", "symbol": "003230", "company_name": "삼양식품", "case_type": "structural_success", "positive_or_counterexample": "positive", "fine_archetype_id": "K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE", "best_trigger": "R5L15-C18-003230-T1", "current_profile_verdict": "current_profile_correct", "score_price_alignment": "strong_positive_alignment", "notes": "Buldak/global reorder translated into export-heavy margin bridge; later full-cycle 4B needs non-price evidence, not just local peak.", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R5L15-C18-004370-NONGSHIM-EXPORT-REORDER", "symbol": "004370", "company_name": "농심", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "fine_archetype_id": "K_FOOD_RAMEN_US_CHANNEL_REORDER_WITH_REVERSAL_RISK", "best_trigger": "R5L15-C18-004370-T1", "current_profile_verdict": "current_profile_correct", "score_price_alignment": "positive_but_high_mae", "notes": "Export/channel reorder was visible and price moved, but drawdown later shows margin durability and channel concentration must cap Green.", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN", "symbol": "097950", "company_name": "CJ제일제당", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "fine_archetype_id": "LEGACY_K_FOOD_BRAND_GLOBAL_DISTRIBUTION_WITH_WEAK_MARGIN_BRIDGE", "best_trigger": "R5L15-C18-097950-T1", "current_profile_verdict": "current_profile_false_positive", "score_price_alignment": "poor_alignment_after_initial_mfe", "notes": "Generic K-food/global-distribution narrative gave early MFE, but margin bridge and repeat reorder were insufficient; later price path was dominated by legacy cost/base effects.", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "trigger_id": "R5L15-C18-003230-T1", "case_id": "R5L15-C18-003230-SAMYANG-EXPORT-REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "1Q24 result shock; export-led Buldak reorder, overseas demand, and margin bridge visible by market open/next-trading-day reaction.", "evidence_source": "historical public quarterly result / disclosure-family evidence; stock-web price row confirmed in atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 446500, "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 85.44, "MFE_1Y_pct": 176.15, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": 0.0, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2025-05-16", "peak_price": 1233000, "drawdown_after_peak_pct": -12.25, "green_lateness_ratio": 0.25, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003230-2024-05-17-446500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L15-C18-003230-T2", "case_id": "R5L15-C18-003230-SAMYANG-EXPORT-REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-12-16", "evidence_available_at_that_date": "Local peak/valuation pressure was visible after multi-month rerating; however non-price 4B confirmation was incomplete, so this remains overlay-only.", "evidence_source": "stock-web price row plus valuation/positioning risk proxy; not used as positive entry evidence.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-16", "entry_price": 729000, "MFE_30D_pct": 9.47, "MFE_90D_pct": 31.41, "MFE_180D_pct": 69.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.9, "MAE_90D_pct": -6.58, "MAE_180D_pct": -6.58, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-16", "peak_price": 1233000, "drawdown_after_peak_pct": -12.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.04, "four_b_full_window_peak_proximity": 0.36, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003230-2024-12-16-729000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_new_4B_overlay_timing", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L15-C18-004370-T1", "case_id": "R5L15-C18-004370-NONGSHIM-EXPORT-REORDER", "symbol": "004370", "company_name": "농심", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_RAMEN_US_CHANNEL_REORDER_WITH_REVERSAL_RISK", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "Export/US-channel growth and ramen category reorder narrative visible around 1Q24 result window; margin durability less clear than Samyang.", "evidence_source": "historical public quarterly result / disclosure-family evidence; stock-web price row confirmed in atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 399000, "MFE_30D_pct": 50.13, "MFE_90D_pct": 50.13, "MFE_180D_pct": 50.13, "MFE_1Y_pct": 50.13, "MFE_2Y_pct": null, "MAE_30D_pct": -1.75, "MAE_90D_pct": -9.65, "MAE_180D_pct": -20.55, "MAE_1Y_pct": -20.55, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 599000, "drawdown_after_peak_pct": -47.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "004370-2024-05-17-399000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L15-C18-097950-T1", "case_id": "R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "LEGACY_K_FOOD_BRAND_GLOBAL_DISTRIBUTION_WITH_WEAK_MARGIN_BRIDGE", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "K-food/global brand distribution narrative and early result improvement visible, but channel reorder was not cleanly separable from legacy food, commodity, and base effects.", "evidence_source": "historical public quarterly result / disclosure-family evidence; stock-web price row confirmed in atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "execution_risk_score"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "profile_path": "atlas/symbol_profiles/097/097950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 333500, "MFE_30D_pct": 22.19, "MFE_90D_pct": 22.19, "MFE_180D_pct": 22.19, "MFE_1Y_pct": 22.19, "MFE_2Y_pct": null, "MAE_30D_pct": -0.3, "MAE_90D_pct": -10.04, "MAE_180D_pct": -30.28, "MAE_1Y_pct": -32.08, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 407500, "drawdown_after_peak_pct": -44.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown", "execution_risk_score"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "097950-2024-05-17-333500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L15-C18-003230-SAMYANG-EXPORT-REORDER", "trigger_id": "R5L15-C18-003230-T1", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 19, "revision_score": 58, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 58, "relative_strength_score": 14, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 19}, "weighted_score_after": 92.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 shadow profile promotes repeat export-channel reorder only when margin bridge and revision close; legacy/global narrative without separable reorder is capped.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L15-C18-003230-SAMYANG-EXPORT-REORDER", "trigger_id": "R5L15-C18-003230-T2", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 58, "relative_strength_score": 14, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 19}, "weighted_score_before": null, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 58, "relative_strength_score": 14, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 26, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 19}, "weighted_score_after": null, "stage_label_after": "4B-overlay-only", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 shadow profile promotes repeat export-channel reorder only when margin bridge and revision close; legacy/global narrative without separable reorder is capped.", "MFE_90D_pct": 31.41, "MAE_90D_pct": -6.58, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L15-C18-004370-NONGSHIM-EXPORT-REORDER", "trigger_id": "R5L15-C18-004370-T1", "symbol": "004370", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 44, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 44, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 11, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 14}, "weighted_score_after": 77.0, "stage_label_after": "Stage3-Yellow-capped", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 shadow profile promotes repeat export-channel reorder only when margin bridge and revision close; legacy/global narrative without separable reorder is capped.", "MFE_90D_pct": 50.13, "MAE_90D_pct": -9.65, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN", "trigger_id": "R5L15-C18-097950-T1", "symbol": "097950", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 39, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 37, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 17, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 7}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-watch-only", "changed_components": ["channel_reorder_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 shadow profile promotes repeat export-channel reorder only when margin bridge and revision close; legacy/global narrative without separable reorder is capped.", "MFE_90D_pct": 22.19, "MAE_90D_pct": -10.04, "score_return_alignment_label": "misaligned_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["legacy_brand_global_distribution_false_positive", "high_mae_after_export_reorder_success", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R5/C18 consumer export channel reorder: K-food reorder versus generic legacy K-food narrative"}
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
recommended_next_round = R5
recommended_next_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
next_loop_objective = holdout_validation
suggested_holdout = non-ramen consumer export channel reorder, or C19 brand retail inventory margin counterexample
```

## 28. Source Notes

Stock-web / calibration artifact observations used in this MD:

```text
- Stock-web manifest max_date = 2026-02-20.
- Stock-web basis = tradable_raw / raw_unadjusted_marcap.
- Stock-web schema defines tradable columns d,o,h,l,c,v,a,mc,s,m and MFE/MAE formulas.
- Current calibrated profile is assumed applied; global axes are not re-proposed.
- stock_agent source code was not opened.
```

This file intentionally does not contain investment recommendation language.
