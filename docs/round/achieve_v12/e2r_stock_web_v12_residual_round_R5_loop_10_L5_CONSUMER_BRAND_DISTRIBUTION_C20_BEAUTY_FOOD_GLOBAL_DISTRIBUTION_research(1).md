# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R5
loop = 10
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_MULTI_REGION_CHANNEL_REORDER
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research, not live stock discovery and not an implementation patch. The research asks a narrower question: in K-beauty / consumer global distribution, does the current post-calibrated profile still miss early structural channel/reorder signals or over-promote narrative-only distribution stories?

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

The applied global axes are treated as the starting profile. This loop does not re-prove that Stage2 is early or that Green is often late. It searches for a C20-specific residual: the difference between **multi-region channel/reorder quality** and **single-channel reopening/IPO narrative**.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: R5
- loop: 10
- large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
- canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
- fine_archetype_id: K_BEAUTY_MULTI_REGION_CHANNEL_REORDER
- loop_objective: coverage_gap_fill, counterexample_mining, residual_missed_structural_mining, residual_false_positive_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts indicated that R1~R13 and loop 1~9 are present in the prior ingest set, while this loop deliberately avoids the previous R6/C22 insurance work and avoids the highly repeated R1/R2 infrastructure/HBM representative sets.

No duplicate hits were found in the available artifact search for the three selected symbols:

```text
257720 실리콘투
237880 클리오
362320 청담글로벌
```

Novelty interpretation:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = not used
same_archetype_new_symbol_bonus = applied
same_archetype_new_trigger_family_bonus = applied
counterexample_gap_bonus = applied
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields read from `Songdaiki/stock-web`:

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

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Symbol profile checks:

|symbol|company_name|profile_path|first_date|last_date|corporate_action_candidate_count|corporate_action_candidate_dates|180D status|
|---|---|---|---|---:|---:|---|---|
|257720|실리콘투|atlas/symbol_profiles/257/257720.json|2021-09-29|2026-02-20|2|2022-07-14; 2022-08-02|clean for 2023-05-09~D+180|
|237880|클리오|atlas/symbol_profiles/237/237880.json|2016-11-09|2026-02-20|0|[]|clean|
|362320|청담글로벌|atlas/symbol_profiles/362/362320.json|2022-06-03|2026-02-20|0|[]|clean|

## 5. Historical Eligibility Gate

All three representative triggers satisfy the historical eligibility gate:

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
entry_date + 180 trading days exists before manifest max_date = true
high/low/close/volume present = true
MFE/MAE 30D/90D/180D calculated = true
corporate-action-contaminated 180D window = false
calibration_usable = true
```

2Y fields are included for residual context, but quantitative shadow deltas rely on clean representative 30D/90D/180D rows.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = K_BEAUTY_MULTI_REGION_CHANNEL_REORDER
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

compresses:
- multi-brand export/platform reorder
- Japan/US/global channel expansion
- brand distribution operating leverage
- single-channel China/reopening false promotion guard
```

The important distinction is not “beauty stock up” versus “beauty stock down.” It is whether the evidence behaves like a **reorder conveyor belt** or a **showroom mirror**. Reorder quality keeps moving product and eventually earnings; narrative-only channel stories reflect light for a while and then go dark.

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|calibration_usable|current_profile_verdict|
|---|---|---|---|---|---|---|---|
|R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509|257720|실리콘투|structural_success|positive|R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509|True|current_profile_missed_structural|
|R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810|237880|클리오|structural_success|positive|R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810|True|current_profile_too_late|
|R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119|362320|청담글로벌|failed_rerating|counterexample|R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119|True|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

The positive cases test whether the current profile is too slow when a consumer-export channel is already converting into measurable operating leverage. The counterexample tests whether a reopening/IPO/single-channel story can be falsely treated as C20 structural evidence.

## 9. Evidence Source Map

|case_id|evidence family|Stage2 evidence|Stage3 evidence|4B/4C evidence|
|---|---|---|---|---|
|R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509|multi-brand global platform / export distributor|public event/disclosure, relative strength, channel/customer quality, early revision signal|margin bridge, financial visibility, multiple public sources|2024-06-19 valuation/positioning overheat overlay|
|R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810|brand export + multi-region reorder|public event/disclosure, relative strength, customer/channel quality|margin bridge, financial visibility, later Green confirmation|not full 4B at initial trigger|
|R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119|single-channel reopening narrative|price/narrative evidence only; weak customer/reorder evidence|no confirmed margin/revision bridge|4C watch after narrative unwind|

## 10. Price Data Source Map

|symbol|entry_date|price_shard_path|profile_path|price_basis|price_adjustment_status|
|---|---|---|---|---|---|
|257720|2023-05-09|atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv|atlas/symbol_profiles/257/257720.json|tradable_raw|raw_unadjusted_marcap|
|237880|2023-08-10|atlas/ohlcv_tradable_by_symbol_year/237/237880/2023.csv|atlas/symbol_profiles/237/237880.json|tradable_raw|raw_unadjusted_marcap|
|362320|2023-01-19|atlas/ohlcv_tradable_by_symbol_year/362/362320/2023.csv|atlas/symbol_profiles/362/362320.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509|257720|실리콘투|Stage2-Actionable|2023-05-09|2023-05-09|3855.0|95.85|151.62|175.23|-22.05|-22.05|-22.05|2024-06-19|54200.0|current_profile_missed_structural|representative|
|R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810|237880|클리오|Stage2-Actionable|2023-08-10|2023-08-10|23400.0|24.36|43.16|64.74|-21.37|-21.37|-21.37|2024-06-13|45000.0|current_profile_too_late|representative|
|R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119|362320|청담글로벌|Stage2-Guard|2023-01-19|2023-01-19|13100.0|12.75|12.75|12.75|-11.91|-34.73|-52.29|2023-01-26|14770.0|current_profile_false_positive|representative|
|R5L10_C20_257720_T2_4B_OVERHEAT_20240619|257720|실리콘투|4B-overlay|2024-06-19|2024-06-19|50700.0|6.9|6.9|6.9|-20.51|-36.59|-54.04|2024-06-19|54200.0|current_profile_correct|4B_overlay_only|
|R5L10_C20_362320_T2_4C_GUARD_20230726|362320|청담글로벌|4C-watch|2023-07-26|2023-07-26|6600.0|36.36|36.36|36.36|-3.03|-4.7|-10.61|2023-08-14|9000.0|current_profile_4C_too_late|4C_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

|symbol|entry_date|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|MFE_1Y|MFE_2Y|peak_date|peak_price|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
|257720|2023-05-09|3855|95.85|-22.05|151.62|-22.05|175.23|-22.05|663.94|1305.97|2024-06-19|54200|
|237880|2023-08-10|23400|24.36|-21.37|43.16|-21.37|64.74|-21.37|92.31|92.31|2024-06-13|45000|
|362320|2023-01-19|13100|12.75|-11.91|12.75|-34.73|12.75|-52.29|12.75|12.75|2023-01-26|14770|

Aggregate representative metrics:

```text
representative_trigger_count = 3
avg_MFE_90D_pct = 69.18
avg_MAE_90D_pct = -26.05
avg_MFE_180D_pct = 84.24
avg_MAE_180D_pct = -31.9
```

## 13. Current Calibrated Profile Stress Test

|case|current profile verdict|why residual remains|
|---|---|---|
|실리콘투|current_profile_missed_structural|Stage2 evidence existed before strict Green-grade revision. C20 needs a channel/reorder quality lens so the profile does not wait for the whole earnings bridge to be already obvious.|
|클리오|current_profile_too_late|The existing profile recognizes revision later, but does not fully price the mechanism where multi-region reorder quality converts into margin visibility.|
|청담글로벌|current_profile_false_positive|Distribution/reopening narrative can look like C20 demand evidence, but without reorder proof and margin bridge it should be blocked or demoted.|

Applied-axis interpretation:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
stage3_cross_evidence_green_buffer = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened for C20 story-only rows
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

The residual is not that Green is late in general. The residual is that C20 needs to score **channel quality** separately:

|case|Stage2-Actionable behavior|Yellow/Green issue|green_lateness_ratio|
|---|---|---|---|
|실리콘투|Stage2 should promote when platform/export reorder evidence appears|Green revision gate may arrive after a large part of the move|not_applicable; no separate Green row used for aggregate|
|클리오|Stage2 can be promoted if brand reorder and multi-region distribution are visible|Green confirmation is later but useful|not_applicable; no separate Green row used for aggregate|
|청담글로벌|Stage2 should be blocked/guarded|Narrative-only Yellow/Green is false promotion|not_applicable|

## 15. 4B Local vs Full-window Timing Audit

|symbol|4B trigger|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|
|---|---|---:|---:|---|
|257720|2024-06-19 valuation/positioning overheat|1.00|1.00|good_full_window_4B_timing|
|362320|no full 4B promotion; 4C watch after narrative unwind|null|null|do not treat rebound spikes as positive rerating evidence|

C20 4B should be a heat overlay, not a thesis killer by itself. For a true full 4B in this archetype, valuation/positioning heat should be accompanied by non-price signs such as channel saturation, margin fatigue, inventory build, or revision slowdown.

## 16. 4C Protection Audit

|symbol|4C label|interpretation|
|---|---|---|
|362320|hard_4c_success|Once the single-channel/reopening story lacked reorder and margin confirmation, the unwind path became a thesis-break/protection case rather than a positive rerating case.|
|257720|thesis_break_watch_only|Peak/overheat did not equal immediate 4C; the business thesis remained alive, so 4B overlay is more appropriate than hard 4C.|

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_consumer_channel_quality_gate
proposal = add small positive shadow weight only when channel evidence includes repeat reorder, multi-region expansion, and margin/OP bridge.
```

Rationale:

- Consumer distribution reratings are not just order announcements; they are repeat sell-through systems.
- One-off channel expansion, IPO distribution story, or China reopening narrative should not be treated as durable channel evidence.
- Sector-level L5 weighting should prefer reorder quality over headline market size.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

new_axis_proposed:
1. c20_multi_region_channel_reorder_quality_bonus = +2 shadow
2. c20_single_channel_reopening_inventory_guard = -3 shadow
3. c20_margin_bridge_required_for_green = true as C20-specific Green quality condition
```

C20 is a conveyor-belt archetype. If the belt is running across multiple regions and margin improves, Stage2 can be early and valid. If it is just a signboard over one channel, the same narrative should be guarded.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global_current_proxy|3|69.18|-26.05|84.24|-31.9|0.33|2|2|mixed; misses early K-beauty channel/reorder positives and overweights single-channel narrative|
|P0b_e2r_2_0_baseline_reference|rollback_reference|3|69.18|-26.05|84.24|-31.9|0.67|2|2|weaker|
|P1_L5_consumer_channel_shadow|sector_specific|3|69.18|-26.05|84.24|-31.9|0.0|0|1|improved|
|P2_C20_beauty_food_distribution_shadow|canonical_archetype_specific|3|69.18|-26.05|84.24|-31.9|0.0|0|1|best shadow alignment|
|P3_C20_counterexample_guard_profile|canonical_guard|1|12.75|-34.73|12.75|-52.29|0.0|0|0|guard pass|

## 20. Score-Return Alignment Matrix

|case_id|symbol|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509|257720|78.0|Stage3-Yellow|82.0|Stage2-Actionable|151.62|-22.05|aligned|current_profile_missed_structural|
|R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810|237880|76.0|Stage3-Yellow|80.0|Stage2-Actionable|43.16|-21.37|aligned|current_profile_too_late|
|R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119|362320|74.0|Stage3-Yellow|62.0|Watch/Blocked|12.75|-34.73|guard_improved_alignment|current_profile_false_positive|

Component details are in the machine-readable `score_simulation` rows below. Unknown or unsupported components are not used for weight delta.

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L5_CONSUMER_BRAND_DISTRIBUTION|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|K_BEAUTY_MULTI_REGION_CHANNEL_REORDER|2|1|1|1|3|0|5|3|3|True|True|C20 now has positive+counterexample+4B+4C seed coverage; still needs food/brand-export holdout.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - missed_structural_multi_region_channel_reorder
  - false_positive_single_channel_reopening_narrative
  - 4C_too_late_after_narrative_unwind
new_axis_proposed:
  - c20_multi_region_channel_reorder_quality_bonus
  - c20_single_channel_reopening_inventory_guard
  - c20_margin_bridge_required_for_green
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: new_symbol=3; same_archetype_new_symbol=3; new_trigger_family=3; counterexample=1; reused=0; schema_rematerialization_penalty=0
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L5/C20 had fewer dedicated K-beauty global distribution positive/counterexample rows than R1/R2 infrastructure/HBM and prior R6/C22 work.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest, schema, symbol profiles, and selected tradable OHLC rows.
- 30D/90D/180D MFE/MAE for representative triggers.
- C20 positive/counterexample balance.
- 4B local vs full-window distinction on the positive structural winner.
- 4C watch path on the counterexample.
```

Not validated:

```text
- No current/live candidate scan.
- No stock_agent source code opened.
- No production scoring change.
- No broker/API/autotrading work.
- No claim that this shadow delta is globally valid.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes,shadow_weight
shadow_weight,c20_multi_region_channel_reorder_quality_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,2,+2,Silicon2 and Clio show early upside when multi-region reorder/channel evidence appears before full Green-grade revisions.,reduces missed structural positives while keeping Green revision gate intact,R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509|R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810,2,2,1,medium,canonical_shadow_only,not production; post-calibrated residual,2.0
shadow_weight,c20_single_channel_reopening_inventory_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-3,-3,Cheongdam Global shows that China/reopening/IPO-distribution narrative without reorder and margin bridge can be false promotion.,removes one current-profile false positive; improves 90D/180D MAE profile,R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119,1,1,1,medium,canonical_guard_shadow_only,not production; post-calibrated residual,-3.0
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Multi-brand K-beauty export/platform distributor; early global channel acceleration appeared before full Green-grade revision confirmation."}
{"row_type": "case", "case_id": "R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810", "symbol": "237880", "company_name": "클리오", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Brand/export channel broadening with later revision confirmation. Stage2 needed to distinguish channel-quality evidence from generic cosmetic narrative."}
{"row_type": "case", "case_id": "R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119", "symbol": "362320", "company_name": "청담글로벌", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "China/reopening/beauty-distribution story showed price response, but lacked multi-region reorder proof and margin/revision bridge."}
{"row_type": "trigger", "trigger_id": "R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509", "case_id": "R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution channel/reorder quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-09", "entry_date": "2023-05-09", "entry_price": 3855.0, "evidence_available_at_that_date": "Multi-brand K-beauty export/platform distributor; early global channel acceleration appeared before full Green-grade revision confirmation.", "evidence_source": "historical public filing/news evidence map; price rows from stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 95.85, "MFE_90D_pct": 151.62, "MFE_180D_pct": 175.23, "MFE_1Y_pct": 663.94, "MFE_2Y_pct": 1305.97, "MAE_30D_pct": -22.05, "MAE_90D_pct": -22.05, "MAE_180D_pct": -22.05, "MAE_1Y_pct": -22.05, "MAE_2Y_pct": -22.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200.0, "drawdown_after_peak_pct": -57.01, "green_lateness_ratio": "not_applicable_for_representative_stage2_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_4C_trigger", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509:2023-05-09:3855", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810", "case_id": "R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810", "symbol": "237880", "company_name": "클리오", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution channel/reorder quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-10", "entry_date": "2023-08-10", "entry_price": 23400.0, "evidence_available_at_that_date": "Brand/export channel broadening with later revision confirmation. Stage2 needed to distinguish channel-quality evidence from generic cosmetic narrative.", "evidence_source": "historical public filing/news evidence map; price rows from stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2023.csv", "profile_path": "atlas/symbol_profiles/237/237880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.36, "MFE_90D_pct": 43.16, "MFE_180D_pct": 64.74, "MFE_1Y_pct": 92.31, "MFE_2Y_pct": 92.31, "MAE_30D_pct": -21.37, "MAE_90D_pct": -21.37, "MAE_180D_pct": -21.37, "MAE_1Y_pct": -21.37, "MAE_2Y_pct": -21.37, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 45000.0, "drawdown_after_peak_pct": -16.67, "green_lateness_ratio": "not_applicable_for_representative_stage2_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_4C_trigger", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810:2023-08-10:23400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119", "case_id": "R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119", "symbol": "362320", "company_name": "청담글로벌", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution channel/reorder quality", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Guard", "trigger_date": "2023-01-19", "entry_date": "2023-01-19", "entry_price": 13100.0, "evidence_available_at_that_date": "China/reopening/beauty-distribution story showed price response, but lacked multi-region reorder proof and margin/revision bridge.", "evidence_source": "historical public filing/news evidence map; price rows from stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/362/362320/2023.csv", "profile_path": "atlas/symbol_profiles/362/362320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.75, "MFE_90D_pct": 12.75, "MFE_180D_pct": 12.75, "MFE_1Y_pct": 12.75, "MFE_2Y_pct": 12.75, "MAE_30D_pct": -11.91, "MAE_90D_pct": -34.73, "MAE_180D_pct": -52.29, "MAE_1Y_pct": -52.29, "MAE_2Y_pct": -52.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-01-26", "peak_price": 14770.0, "drawdown_after_peak_pct": -57.68, "green_lateness_ratio": "not_applicable_for_representative_stage2_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_4C_trigger", "trigger_outcome_label": "failed_rerating_after_single_channel_narrative", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119:2023-01-19:13100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_257720_T2_4B_OVERHEAT_20240619", "case_id": "R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution channel/reorder quality", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "4B-overlay", "trigger_date": "2024-06-19", "entry_date": "2024-06-19", "entry_price": 50700.0, "evidence_available_at_that_date": "Cycle peak area; valuation and positioning heat overlaid on still-strong structural thesis.", "evidence_source": "stock-web price row plus historical valuation/positioning narrative map", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.9, "MFE_90D_pct": 6.9, "MFE_180D_pct": 6.9, "MFE_1Y_pct": 6.9, "MFE_2Y_pct": null, "MAE_30D_pct": -20.51, "MAE_90D_pct": -36.59, "MAE_180D_pct": -54.04, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200.0, "drawdown_after_peak_pct": -57.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_257720_4B_20240619_50700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_new_4B_timing_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_362320_T2_4C_GUARD_20230726", "case_id": "R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119", "symbol": "362320", "company_name": "청담글로벌", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_MULTI_REGION_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "single-channel reopening narrative guard", "loop_objective": "4C_thesis_break_timing_test", "trigger_type": "4C-watch", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 6600.0, "evidence_available_at_that_date": "Narrative price premium had unwound; no margin/reorder proof appeared to defend the thesis.", "evidence_source": "stock-web price row plus historical evidence map", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/362/362320/2023.csv", "profile_path": "atlas/symbol_profiles/362/362320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.36, "MFE_90D_pct": 36.36, "MFE_180D_pct": 36.36, "MFE_1Y_pct": 36.36, "MFE_2Y_pct": 36.36, "MAE_30D_pct": -3.03, "MAE_90D_pct": -4.7, "MAE_180D_pct": -10.61, "MAE_1Y_pct": -17.27, "MAE_2Y_pct": -30.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-14", "peak_price": 9000.0, "drawdown_after_peak_pct": -53.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_362320_4C_20230726_6600", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_new_4C_timing_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_257720_SILICON2_GLOBAL_PLATFORM_20230509", "trigger_id": "R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 13, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 18, "export_platform_score": 16}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 13, "relative_strength_score": 18, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 22, "export_platform_score": 20}, "weighted_score_after": 82.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["channel_reorder_score", "export_platform_score", "customer_quality_score"], "component_delta_explanation": "C20 shadow adds quality for multi-brand exporter/platform reorder evidence before formal Green revision.", "MFE_90D_pct": 151.62, "MAE_90D_pct": -22.05, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_237880_CLIO_GLOBAL_CHANNEL_20230810", "trigger_id": "R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810", "symbol": "237880", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 12, "relative_strength_score": 12, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "global_distribution_score": 13}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 12, "relative_strength_score": 12, "customer_quality_score": 17, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 20, "global_distribution_score": 17}, "weighted_score_after": 80.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["channel_reorder_score", "global_distribution_score", "customer_quality_score"], "component_delta_explanation": "C20 shadow lets brand reorder quality bridge the gap while Green remains revision-gated.", "MFE_90D_pct": 43.16, "MAE_90D_pct": -21.37, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119", "trigger_id": "R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119", "symbol": "362320", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "execution_risk": 12, "channel_reorder_score": 6, "single_channel_concentration_risk": 15}, "weighted_score_before": 74.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "execution_risk": 18, "channel_reorder_score": 2, "single_channel_concentration_risk": 22}, "weighted_score_after": 62.0, "stage_label_after": "Watch/Blocked", "changed_components": ["relative_strength_score", "channel_reorder_score", "single_channel_concentration_risk", "execution_risk_score"], "component_delta_explanation": "C20 guard demotes single-channel reopening/IPO narrative unless reorder and margin bridge close.", "MFE_90D_pct": 12.75, "MAE_90D_pct": -34.73, "score_return_alignment_label": "guard_improved_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 0, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["missed_structural_multi_region_channel_reorder", "false_positive_single_channel_reopening_narrative", "4C_too_late_after_narrative_unwind"], "diversity_score_summary": "new_symbol=3; same_archetype_new_symbol=3; new_trigger_family=3; counterexample=1; reused=0; schema_rematerialization_penalty=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "L5/C20 had fewer dedicated K-beauty global distribution positive/counterexample rows than R1/R2 infrastructure/HBM and prior R6/C22 work."}
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
next_round = R5_loop_11_C20_food_global_distribution_holdout
alternative_next_round = L7_C23_bio_regulatory_approval_commercialization
carry_forward_gap = C20 still needs food/global-brand distribution cases and non-beauty consumer holdout.
```

## 28. Source Notes

Stock-Web files accessed for this MD:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/257/257720.json
atlas/symbol_profiles/237/237880.json
atlas/symbol_profiles/362/362320.json
atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv
atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/237/237880/2023.csv
atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv
atlas/ohlcv_tradable_by_symbol_year/362/362320/2022.csv
atlas/ohlcv_tradable_by_symbol_year/362/362320/2023.csv
```

Allowed stock_agent artifact files accessed only for coverage / duplicate avoidance:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/calibrated_profile_report.md
data/e2r/calibration/md_registry.jsonl
```

This file contains historical calibration research only. It is not an investment recommendation.
