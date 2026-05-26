# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 46
selection_mode = auto_coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
created_at = 2026-05-25 Asia/Seoul
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration artifact. It is not a live scan, not a recommendation list, not a code patch, and not a production scoring change.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The goal is not to prove these global axes again. The residual question is narrower: inside C20, when does a K-beauty/K-food global channel story become a true EPS/rerating route, and when is it merely a channel narrative that later becomes high-MAE or 4C?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_ids =
  - K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER
  - K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER
  - K_BEAUTY_ODM_GLOBAL_CUSTOMER_MARGIN_BRIDGE
  - K_BEAUTY_BRAND_CHANNEL_REORDER_MARGIN_GUARD

loop_objective =
  - auto_coverage_gap_fill
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - residual_false_positive_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

The search target was not “new canonical only.” Same canonical archetype research is allowed. The duplicate risk is the repeated use of the same symbol + trigger date + entry date + evidence family.

```text
duplicate_check_scope = stock_agent research artifact search only
stock_agent_code_opened = false
stock_agent_src_e2r_opened = false
candidate_symbol_search = 257720 / 003230 / 192820 / 237880 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
search_result = no direct duplicate hit found
parallel_overlap_policy = keep if new symbol, new trigger family, counterexample, or residual error
```

Diversity governor result:

```text
same_canonical_archetype_research = allowed
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_ratio = 1.00
counterexample_count = 2
positive_case_count = 2
diversity_score_summary = avg≈18; no repeated same symbol/trigger/entry group
```

## 4. Stock-Web OHLC Input / Price Source Validation

|field|value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|

Schema basis:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_rule = block 180D windows overlapping corporate-action candidate dates
```

## 5. Historical Eligibility Gate

|symbol|company|profile_path|price_shard_2024|corporate_action_candidate_dates|window_status|
|---|---|---|---|---|---|
|257720|실리콘투|atlas/symbol_profiles/257/257720.json|atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|['2022-07-14', '2022-08-02']|2024 trigger windows clean; 2022 corporate-action candidates outside window|
|003230|삼양식품|atlas/symbol_profiles/003/003230.json|atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|['2003-07-25']|2024 trigger windows clean; legacy corporate-action candidate outside window|
|192820|코스맥스|atlas/symbol_profiles/192/192820.json|atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv|[]|clean profile; no corporate-action candidates|
|237880|클리오|atlas/symbol_profiles/237/237880.json|atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv|[]|clean profile; no corporate-action candidates|

Eligibility conclusion:

```text
minimum_forward_window = 180 trading days
stock_web_manifest_max_date = 2026-02-20
all_representative_entries_have_180D_window = true
all_representative_180D_windows_clean = true
calibration_usable_case_count = 4
calibration_usable_trigger_count = 10
```

## 6. Canonical Archetype Compression Map

C20 compresses four visually different but economically similar routes:

|fine_archetype_id|canonical mapping|mechanism|risk|
|---|---|---|---|
|K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER|C20|Cross-border wholesale/distribution platform converts overseas demand into operating leverage.|Can become valuation blowoff if price outruns repeat-order proof.|
|K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER|C20|Global food SKU becomes export reorder engine; margin bridge is visible when ASP/mix/export capacity align.|Viral/social heat can create price-only 4B watch without thesis break.|
|K_BEAUTY_ODM_GLOBAL_CUSTOMER_MARGIN_BRIDGE|C20|ODM demand and customer orders can look like global distribution rerating when margin bridge is confirmed.|If sell-through/inventory is not visible, it is high-MAE prone.|
|K_BEAUTY_BRAND_CHANNEL_REORDER_MARGIN_GUARD|C20|Beauty brand channel expansion needs reorder quality and inventory discipline.|Channel story without margin durability becomes false positive.|

## 7. Case Selection Summary

|case_id|symbol|company|role|case_type|best_trigger|current_profile_verdict|novelty|
|---|---|---|---|---|---|---|---|
|R13L46_257720_SILICON2|257720|실리콘투|positive|structural_success|R13L46_257720_STAGE2_20240321|current_profile_correct|new|
|R13L46_003230_SAMYANG|003230|삼양식품|positive|structural_success|R13L46_003230_STAGE2_20240321|current_profile_correct|new|
|R13L46_192820_COSMAX|192820|코스맥스|counterexample|high_mae_success|R13L46_192820_STAGE2_20240516|current_profile_false_positive|new|
|R13L46_237880_CLIO|237880|클리오|counterexample|false_positive_green|R13L46_237880_STAGE2_20240514|current_profile_false_positive|new|

Selection balance:

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 2
4B_case_count = 2
4C_case_count = 1
new_symbol_count = 4
reused_case_count = 0
```

## 8. Positive vs Counterexample Balance

The positive cases had both customer/channel pull and visible margin/revision bridge. The counterexamples had channel expansion language, but the stock path showed that channel narrative without inventory/reorder durability became either high-MAE or outright thesis-break.

```text
positive_cases = 257720, 003230
counterexamples = 192820, 237880
main_residual_error = C20 channel story can pass global Stage2/Yellow filters but fail unless sell-through/inventory/margin durability is visible.
```

## 9. Evidence Source Map

|case|trigger family|evidence before/at trigger|stage separation|
|---|---|---|---|
|257720 실리콘투|cross-border K-beauty reorder platform|Stage2 route visible before Q1 surprise; Stage3 confirmed by May earnings; 4B overlay after parabolic valuation.|Stage2: channel/order + relative strength; Stage3: confirmed revision; 4B: valuation/positioning.|
|003230 삼양식품|Buldak export reorder engine|Stage2 route visible before Q1 surprise; Stage3 confirmed by export-led earnings; local 4B price-only peak was too early as thesis stayed intact.|Stage2: export/customer pull; Stage3: margin/revision; 4B: price-only/positioning watch.|
|192820 코스맥스|beauty ODM global customer margin bridge|Q1 looked strong, but no durable sell-through/inventory proof; post-rerating drawdown made Green/Yellow risky.|Stage2/Yellow: earnings; Guard: inventory/channel absence.|
|237880 클리오|beauty brand channel reorder guard|Q1 channel narrative had MFE but later collapsed; Q3-style disappointment became late 4C route.|Stage2: channel narrative; 4C: thesis evidence broken, but late.|

## 10. Price Data Source Map

|symbol|tradable shard(s) used|profile|entry rows verified|180D window|
|---|---|---|---|---|
|257720|atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/symbol_profiles/257/257720.json|2024-03-21 / 2024-05-10 / 2024-06-21|clean|
|003230|atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/symbol_profiles/003/003230.json|2024-03-21 / 2024-05-17 / 2024-06-18|clean|
|192820|atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv|atlas/symbol_profiles/192/192820.json|2024-05-16 / 2024-06-14|clean|
|237880|atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv and 2025.csv|atlas/symbol_profiles/237/237880.json|2024-05-14 / 2024-11-11|clean|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D|MFE_90D|MFE_180D|MAE_30D|MAE_90D|MAE_180D|current_profile_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L46_257720_STAGE2_20240321|257720|Stage2-Actionable|2024-03-21|10820|43.3|400.9|400.9|-7.5|-7.5|-7.5|current_profile_correct|representative|
|R13L46_257720_GREEN_20240510|257720|Stage3-Green|2024-05-10|26250|106.5|106.5|106.5|-17.9|-17.9|-17.9|current_profile_too_late|label_comparison_only|
|R13L46_257720_4B_20240621|257720|Stage4B|2024-06-21|52800|1.9|2.7|2.7|-23.8|-39.1|-55.9|current_profile_correct|4B_overlay_only|
|R13L46_003230_STAGE2_20240321|003230|Stage2-Actionable|2024-03-21|188800|64.5|280.3|280.3|-1.3|-1.3|-1.3|current_profile_correct|representative|
|R13L46_003230_GREEN_20240517|003230|Stage3-Green|2024-05-17|446500|60.8|60.8|79.2|0.0|0.0|0.0|current_profile_too_late|label_comparison_only|
|R13L46_003230_4B_20240618|003230|Stage4B|2024-06-18|712000|0.8|0.8|12.4|-18.4|-36.0|-36.0|current_profile_4B_too_early|4B_overlay_only|
|R13L46_192820_STAGE2_20240516|192820|Stage2-Actionable|2024-05-16|161400|28.9|28.9|28.9|-4.4|-28.1|-28.1|current_profile_false_positive|representative|
|R13L46_192820_YELLOW_20240614|192820|Stage3-Yellow|2024-06-14|184900|12.5|12.5|12.5|-20.4|-37.3|-37.3|current_profile_false_positive|label_comparison_only|
|R13L46_237880_STAGE2_20240514|237880|Stage2-Actionable|2024-05-14|36850|22.1|22.1|22.1|-4.9|-19.4|-57.2|current_profile_false_positive|representative|
|R13L46_237880_4C_20241111|237880|Stage4C|2024-11-11|18070|5.0|26.5|26.5|-12.6|-12.6|-21.3|current_profile_4C_too_late|4C_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger aggregate

|metric|value|
|---|---|
|representative_trigger_count|4|
|avg_MFE_90D_pct|183.1|
|avg_MAE_90D_pct|-14.1|
|avg_MFE_180D_pct|183.1|
|avg_MAE_180D_pct|-23.5|
|false_positive_representatives|2 / 4|
|positive_representatives|2 / 4|

### 12.2 Interpretation

Silicon2 and Samyang are classic C20 positives: early channel/reorder evidence was later confirmed by financial visibility. Cosmax and Clio show the residual trap: a beauty/global channel story can produce a tradable 30D MFE, but if reorder durability and inventory/margin bridge are not proven, the same pattern becomes a high-MAE false positive.

## 13. Current Calibrated Profile Stress Test

|case|P0 likely behavior|actual path|verdict|residual|
|---|---|---|---|---|
|257720 실리콘투|Stage2 acceptable; Green on earnings confirmation|Stage2 already captured most signal; Green still worked but was later|current_profile_correct / Green somewhat late|No global change; C20 bridge bonus helps earlier confidence.|
|003230 삼양식품|Stage2 acceptable; Green on Q1 confirmation; local 4B watch|Stage2 and Green both worked; price-only June 4B would be early versus December full-window high|current_profile_correct; current_profile_4B_too_early if price-only|Strengthen non-price 4B rule.|
|192820 코스맥스|Might pass Yellow/near-Green on Q1 and relative strength|MFE existed, but MAE/drawdown severe after June|current_profile_false_positive|Add C20 inventory/channel absence guard.|
|237880 클리오|Might pass Yellow on channel expansion|Initial MFE existed, then 180D MAE -57.2%; 4C arrived late|current_profile_false_positive / current_profile_4C_too_late|Do not promote channel story without reorder/margin proof.|

Current calibrated axis test:

```text
stage2_actionable_evidence_bonus = kept, but C20 requires channel evidence quality
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept, with note that C20 4C may be late if inventory/reorder failure is not tracked earlier
```

## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|Stage3/Yellow entry|green_lateness_ratio|verdict|
|---|---|---|---|---|
|257720|10820 on 2024-03-21|26250 on 2024-05-10|0.4|Green valid but Stage2 captured more upside.|
|003230|188800 on 2024-03-21|446500 on 2024-05-17|0.5|Green valid but late relative to export-route Stage2.|
|192820|161400 on 2024-05-16|184900 on 2024-06-14|0.5|Late Yellow/Green chase worsened drawdown risk.|
|237880|36850 on 2024-05-14|no valid Green|not_applicable|No confirmed Green; channel evidence alone failed.|

## 15. 4B Local vs Full-window Timing Audit

|case|4B trigger|local proximity|full-window proximity|evidence type|verdict|
|---|---|---|---|---|---|
|257720|2024-06-21|1.0|1.0|valuation_blowoff / positioning_overheat|Good 4B overlay timing; later drawdown validates risk overlay.|
|003230|2024-06-18|1.0|0.9|price_only / positioning_overheat|Price-only local 4B was too early as full-window high came later and thesis was intact.|

C20-specific reading: viral/social consumer momentum can look like a peak before the thesis breaks. Therefore price-only 4B should stay a watch overlay unless valuation blowoff is accompanied by revision slowdown, inventory risk, regulatory block, or channel deterioration.

## 16. 4C Protection Audit

|case|4C trigger|entry|MFE_90D|MAE_90D|protection label|
|---|---|---|---|---|---|
|237880 클리오|2024-11-11|18070|26.5|-12.6|hard_4c_late_partial_protection_score_0.81|

The 4C route helped avoid some further loss, but it was late relative to the prior peak-to-trough damage. In C20, inventory/reorder deterioration needs earlier watch logic before the formal thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_id = L5_price_only_social_heat_4B_watch
rule_scope = sector_specific
condition =
  consumer brand/food/beauty stock has local blowoff driven by viral/social heat or momentum
  AND no non-price evidence of revision slowdown / inventory stress / regulatory block / order deterioration exists
effect =
  route to 4B-watch overlay
  do_not_treat_as_full_4B = true
supporting_triggers =
  - R13L46_003230_4B_20240618
  - R13L46_257720_4B_20240621
proposal_type = sector_shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C20_channel_reorder_margin_bridge_bonus
rule_scope = canonical_archetype_specific
positive condition =
  global beauty/food channel evidence includes repeat-order or customer-pull signal
  AND margin bridge or revision path is visible
  AND evidence is non-price
effect =
  +1 C20 shadow bonus to Stage2-Actionable confidence
  no automatic Green without confirmed revision

rule_id = C20_inventory_channel_absence_guard
negative condition =
  global channel narrative exists
  BUT sell-through/inventory/reorder durability is unknown or deteriorating
  OR margin bridge is not confirmed
effect =
  -1.5 C20 shadow guard
  block Stage3-Green; downgrade to Stage2-Watch or Yellow-Watch
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|eligible_triggers|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|stress result|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|current calibrated proxy|Existing global calibrated profile|None|4|183.1|-14.1|183.1|-23.5|50.0%|2 false positive / 1 4C late|kept but needs C20 guard|
|P0b|rollback reference|E2R 2.0 baseline reference|No stock-web calibrated axes|4|183.1|-14.1|183.1|-23.5|50.0%+|would over-promote channel stories|inferior|
|P1|sector-specific candidate|L5 price-only viral/social heat is 4B-watch unless non-price risk appears|4B watch guard|4|183.1|-14.1|183.1|-23.5|50.0%|prevents Samyang premature full-4B|better risk overlay|
|P2|canonical-archetype candidate|C20 needs reorder + margin bridge; blocks channel-story-only Green|C20 bridge bonus and absence guard|4|340.6|-4.4|340.6|-4.4|0.0%|selects Silicon2/Samyang only|best alignment|
|P3|counterexample guard|Down-weight no inventory/sell-through proof|inventory/channel absence guard|4|183.1|-14.1|183.1|-23.5|25.0%|Cosmax downgraded to watch; Clio blocked|good guard|

## 20. Score-Return Alignment Matrix

|trigger_id|before_score|before_label|after_score|after_label|MFE_90D|MAE_90D|alignment|
|---|---|---|---|---|---|---|---|
|R13L46_257720_STAGE2_20240321|78|Stage2-Actionable|83|Stage2-Actionable+|400.9|-7.5|aligned|
|R13L46_257720_GREEN_20240510|91|Stage3-Green|94|Stage3-Green|106.5|-17.9|aligned|
|R13L46_257720_4B_20240621|88|4B-Overlay|88|4B-Overlay|2.7|-39.1|aligned|
|R13L46_003230_STAGE2_20240321|80|Stage2-Actionable|85|Stage2-Actionable+|280.3|-1.3|aligned|
|R13L46_003230_GREEN_20240517|94|Stage3-Green|96|Stage3-Green|60.8|0.0|aligned|
|R13L46_003230_4B_20240618|88|4B-Watch|88|4B-Watch|0.8|-36.0|misaligned_or_guard_needed|
|R13L46_192820_STAGE2_20240516|76|Stage3-Yellow|70|Stage2-Watch|28.9|-28.1|misaligned_or_guard_needed|
|R13L46_192820_YELLOW_20240614|79|Stage3-Yellow|70|Stage2/4B-Watch|12.5|-37.3|misaligned_or_guard_needed|
|R13L46_237880_STAGE2_20240514|75|Stage3-Yellow|66|Stage2-Watch|22.1|-19.4|misaligned_or_guard_needed|
|R13L46_237880_4C_20241111|42|4C-Watch|35|4C|26.5|-12.6|aligned|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L5_CONSUMER_BRAND_DISTRIBUTION|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER / K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER / K_BEAUTY_ODM_GLOBAL_CUSTOMER_MARGIN_BRIDGE / K_BEAUTY_BRAND_CHANNEL_REORDER_MARGIN_GUARD|2|2|2|1|4|0|10|4|3|True|True|C20 now has positive+counterexample+4B/4C coverage; needs additional holdout in C20 food ex-Buldak and beauty brand ex-Clio|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C20 channel-story false positive
  - consumer viral/social heat price-only local 4B too early
  - C20 4C late after inventory/reorder thesis damage
new_axis_proposed:
  - C20_channel_reorder_margin_bridge_bonus
  - C20_inventory_channel_absence_guard
  - L5_price_only_social_heat_4B_watch
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L5/C20 positive/counterexample/4B-4C balance was underfilled versus adjacent C18/C19 coverage.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest and schema
- Symbol profiles for 257720 / 003230 / 192820 / 237880
- Entry date and entry close from tradable shards
- 30D / 90D / 180D MFE and MAE using fetched stock-web rows
- Corporate-action window status via profile dates
- Positive/counterexample balance
- Stage2/Green lateness logic
- 4B local-vs-full timing split
- 4C late protection label for Clio
```

Not validated:

```text
- No live scan
- No current candidate discovery
- No brokerage/API trading action
- No stock_agent source code access
- No production scoring change
- No claim that the shadow weights should be applied without batch review
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"repeat-order/channel evidence plus margin bridge separates Silicon2/Samyang from generic channel stories","improves early Stage2 capture without promoting price-only narratives","R13L46_257720_STAGE2_20240321|R13L46_003230_STAGE2_20240321",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_inventory_channel_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-1.5,-1.5,"Clio/Cosmax show global channel narrative can become high-MAE false positive without inventory/sell-through/margin durability","reduces false positive Green/Yellow in counterexamples","R13L46_192820_STAGE2_20240516|R13L46_237880_STAGE2_20240514",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L5_price_only_social_heat_4B_watch,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"consumer viral/social heat often creates local blowoff but may not equal thesis break","keeps Samyang price-only local peak as 4B-watch rather than full 4B","R13L46_003230_4B_20240618|R13L46_257720_4B_20240621",4,4,2,low,sector_shadow_only,"not production; strengthens full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L46_257720_SILICON2","symbol":"257720","company_name":"실리콘투","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L46_257720_STAGE2_20240321","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024 trigger windows clean; 2022 corporate-action candidates outside window"}
{"row_type":"case","case_id":"R13L46_003230_SAMYANG","symbol":"003230","company_name":"삼양식품","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L46_003230_STAGE2_20240321","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024 trigger windows clean; legacy corporate-action candidate outside window"}
{"row_type":"case","case_id":"R13L46_192820_COSMAX","symbol":"192820","company_name":"코스맥스","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R13L46_192820_STAGE2_20240516","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"clean profile; no corporate-action candidates"}
{"row_type":"case","case_id":"R13L46_237880_CLIO","symbol":"237880","company_name":"클리오","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_CHANNEL_REORDER_MARGIN_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L46_237880_STAGE2_20240514","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"clean profile; no corporate-action candidates"}
{"trigger_id":"R13L46_257720_STAGE2_20240321","case_id":"R13L46_257720_SILICON2","symbol":"257720","company_name":"실리콘투","case_role":"structural_success","positive_or_counterexample":"positive","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":10820,"evidence_available_at_that_date":"K-beauty cross-border distribution/reorder route was visible before the 1Q24 earnings explosion; evidence was channel/order-quality plus relative strength, not price-only.","evidence_source":"historical public filing/earnings coverage; DART/KIND style public evidence family","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","MFE_30D_pct":43.3,"MFE_90D_pct":400.9,"MFE_180D_pct":400.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.5,"MAE_90D_pct":-7.5,"MAE_180D_pct":-7.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"explosive_repricing_after_channel_reorder_route","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R13L46_257720_20240321_10820","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"R13L46_257720_GREEN_20240510","case_id":"R13L46_257720_SILICON2","symbol":"257720","company_name":"실리콘투","case_role":"structural_success","positive_or_counterexample":"positive","trigger_type":"Stage3-Green","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":26250,"evidence_available_at_that_date":"1Q24 operating leverage/revenue surprise confirmed that the earlier channel route had translated into financial visibility.","evidence_source":"historical public filing/earnings coverage; DART/KIND style public evidence family","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","MFE_30D_pct":106.5,"MFE_90D_pct":106.5,"MFE_180D_pct":106.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.9,"MAE_90D_pct":-17.9,"MAE_180D_pct":-17.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.0,"green_lateness_ratio":0.4,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_valid_but_after_large_stage2_move","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"R13L46_257720_20240510_26250","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"trigger_id":"R13L46_257720_4B_20240621","case_id":"R13L46_257720_SILICON2","symbol":"257720","company_name":"실리콘투","case_role":"4B_overlay_success","positive_or_counterexample":"positive","trigger_type":"Stage4B","trigger_date":"2024-06-21","entry_date":"2024-06-21","entry_price":52800,"evidence_available_at_that_date":"Post-Green parabolic repricing created valuation/positioning overheat. It is a risk overlay, not a thesis break.","evidence_source":"historical public market/valuation coverage; price row confirms local blowoff but promotion uses non-price risk overlay","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","MFE_30D_pct":1.9,"MFE_90D_pct":2.7,"MFE_180D_pct":2.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.8,"MAE_90D_pct":-39.1,"MAE_180D_pct":-55.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":53800,"drawdown_after_peak_pct":-56.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_protected_against_later_drawdown","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R13L46_257720_20240621_52800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CROSS_BORDER_PLATFORM_REORDER","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"trigger_id":"R13L46_003230_STAGE2_20240321","case_id":"R13L46_003230_SAMYANG","symbol":"003230","company_name":"삼양식품","case_role":"structural_success","positive_or_counterexample":"positive","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":188800,"evidence_available_at_that_date":"Buldak export mix and overseas demand route were already visible before the Q1 earnings shock; evidence was global sell-through/customer pull plus early revision path.","evidence_source":"historical public filing/earnings coverage; export-demand evidence family","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","MFE_30D_pct":64.5,"MFE_90D_pct":280.3,"MFE_180D_pct":280.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.3,"MAE_90D_pct":-1.3,"MAE_180D_pct":-1.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-36.6,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"explosive_food_export_rerating","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R13L46_003230_20240321_188800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"R13L46_003230_GREEN_20240517","case_id":"R13L46_003230_SAMYANG","symbol":"003230","company_name":"삼양식품","case_role":"structural_success","positive_or_counterexample":"positive","trigger_type":"Stage3-Green","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":446500,"evidence_available_at_that_date":"1Q24 export-led earnings surprise confirmed margin bridge and financial visibility.","evidence_source":"historical public filing/earnings coverage; DART/KIND style public evidence family","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","MFE_30D_pct":60.8,"MFE_90D_pct":60.8,"MFE_180D_pct":79.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-26","peak_price":800000,"drawdown_after_peak_pct":-6.1,"green_lateness_ratio":0.5,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_valid_but_stage2_captured_more_upside","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"R13L46_003230_20240517_446500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"trigger_id":"R13L46_003230_4B_20240618","case_id":"R13L46_003230_SAMYANG","symbol":"003230","company_name":"삼양식품","case_role":"4B_too_early","positive_or_counterexample":"positive","trigger_type":"Stage4B","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":712000,"evidence_available_at_that_date":"Sharp post-earnings overheat was visible, but no hard non-price thesis break was available at that date.","evidence_source":"historical public market/valuation coverage; price-only local blowoff separated from full 4B","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","MFE_30D_pct":0.8,"MFE_90D_pct":0.8,"MFE_180D_pct":12.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.4,"MAE_90D_pct":-36.0,"MAE_180D_pct":-36.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-26","peak_price":800000,"drawdown_after_peak_pct":-6.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"price_only_4B_would_have_cut_structural_winner_too_early","current_profile_verdict":"current_profile_4B_too_early","same_entry_group_id":"R13L46_003230_20240618_712000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_EXPORT_REORDER","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"trigger_id":"R13L46_192820_STAGE2_20240516","case_id":"R13L46_192820_COSMAX","symbol":"192820","company_name":"코스맥스","case_role":"high_mae_success","positive_or_counterexample":"counterexample","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":161400,"evidence_available_at_that_date":"1Q24 beauty ODM demand and margin bridge appeared strong, but channel/inventory durability was not proven enough for Green.","evidence_source":"historical public filing/earnings coverage; DART/KIND style public evidence family","stage2_evidence_fields":["customer_or_order_quality","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","MFE_30D_pct":28.9,"MFE_90D_pct":28.9,"MFE_180D_pct":28.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.4,"MAE_90D_pct":-28.1,"MAE_180D_pct":-28.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"positive_initial_MFE_but_high_MAE_and_roundtrip","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R13L46_192820_20240516_161400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"R13L46_192820_YELLOW_20240614","case_id":"R13L46_192820_COSMAX","symbol":"192820","company_name":"코스맥스","case_role":"false_positive_green","positive_or_counterexample":"counterexample","trigger_type":"Stage3-Yellow","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":184900,"evidence_available_at_that_date":"Price/revision chase after the initial Q1 rerating, without a fresh durable customer confirmation.","evidence_source":"historical public earnings/market coverage; negative control for Green strictness","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","MFE_30D_pct":12.5,"MFE_90D_pct":12.5,"MFE_180D_pct":12.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.4,"MAE_90D_pct":-37.3,"MAE_180D_pct":-37.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.2,"green_lateness_ratio":0.5,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_watch_only","four_b_evidence_type":["price_only"],"four_c_protection_label":null,"trigger_outcome_label":"late_yellow_failed_to_compensate_for_high_MAE","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R13L46_192820_20240614_184900","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"trigger_id":"R13L46_237880_STAGE2_20240514","case_id":"R13L46_237880_CLIO","symbol":"237880","company_name":"클리오","case_role":"false_positive_green","positive_or_counterexample":"counterexample","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":36850,"evidence_available_at_that_date":"Global channel expansion narrative existed, but inventory/reorder durability and margin bridge were not strong enough.","evidence_source":"historical public filing/earnings coverage; DART/KIND style public evidence family","stage2_evidence_fields":["customer_or_order_quality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv","profile_path":"atlas/symbol_profiles/237/237880.json","MFE_30D_pct":22.1,"MFE_90D_pct":22.1,"MFE_180D_pct":22.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.9,"MAE_90D_pct":-19.4,"MAE_180D_pct":-57.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":45000,"drawdown_after_peak_pct":-64.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"channel_story_without_inventory_margin_bridge_became_false_positive","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R13L46_237880_20240514_36850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_CHANNEL_REORDER_MARGIN_GUARD","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"R13L46_237880_4C_20241111","case_id":"R13L46_237880_CLIO","symbol":"237880","company_name":"클리오","case_role":"4C_late","positive_or_counterexample":"counterexample","trigger_type":"Stage4C","trigger_date":"2024-11-11","entry_date":"2024-11-11","entry_price":18070,"evidence_available_at_that_date":"Q3-style margin/channel disappointment turned the earlier channel thesis into a thesis-break watch/4C route, but most drawdown had already happened.","evidence_source":"historical public filing/earnings coverage; DART/KIND style public evidence family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv|atlas/ohlcv_tradable_by_symbol_year/237/237880/2025.csv","profile_path":"atlas/symbol_profiles/237/237880.json","MFE_30D_pct":5.0,"MFE_90D_pct":26.5,"MFE_180D_pct":26.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.6,"MAE_90D_pct":-12.6,"MAE_180D_pct":-21.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-14","peak_price":22850,"drawdown_after_peak_pct":-37.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_partial_protection_score_0.81","trigger_outcome_label":"4C_late_after_prior_drawdown","current_profile_verdict":"current_profile_4C_too_late","same_entry_group_id":"R13L46_237880_20241111_18070","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","row_type":"trigger","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_CHANNEL_REORDER_MARGIN_GUARD","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_257720_SILICON2","trigger_id":"R13L46_257720_STAGE2_20240321","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage2-Actionable+","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"C20 channel/reorder bonus adds confidence but does not force Green before confirmed revision.","MFE_90D_pct":400.9,"MAE_90D_pct":-7.5,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_257720_SILICON2","trigger_id":"R13L46_257720_GREEN_20240510","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":91,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":9,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":94,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score"],"component_delta_explanation":"Confirmed 1Q visibility validates earlier Stage2; no threshold change required.","MFE_90D_pct":106.5,"MAE_90D_pct":-17.9,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_257720_SILICON2","trigger_id":"R13L46_257720_4B_20240621","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"4B-Overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"4B-Overlay","changed_components":["execution_risk_score"],"component_delta_explanation":"C20 risk overlay: valuation/positioning only, not 4C.","MFE_90D_pct":2.7,"MAE_90D_pct":-39.1,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_003230_SAMYANG","trigger_id":"R13L46_003230_STAGE2_20240321","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":7,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":7,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85,"stage_label_after":"Stage2-Actionable+","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"Export reorder/customer pull bonus supports earlier Stage2.","MFE_90D_pct":280.3,"MAE_90D_pct":-1.3,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_003230_SAMYANG","trigger_id":"R13L46_003230_GREEN_20240517","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":94,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":96,"stage_label_after":"Stage3-Green","changed_components":[],"component_delta_explanation":"Confirmed export/margin bridge keeps Green.","MFE_90D_pct":60.8,"MAE_90D_pct":0.0,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_003230_SAMYANG","trigger_id":"R13L46_003230_4B_20240618","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"4B-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"4B-Watch","changed_components":[],"component_delta_explanation":"Price-only local peak is not full 4B without non-price thesis damage.","MFE_90D_pct":0.8,"MAE_90D_pct":-36.0,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_192820_COSMAX","trigger_id":"R13L46_192820_STAGE2_20240516","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"Inventory/channel durability guard prevents over-promotion.","MFE_90D_pct":28.9,"MAE_90D_pct":-28.1,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_192820_COSMAX","trigger_id":"R13L46_192820_YELLOW_20240614","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2/4B-Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"Late price/revision chase is guarded.","MFE_90D_pct":12.5,"MAE_90D_pct":-37.3,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_237880_CLIO","trigger_id":"R13L46_237880_STAGE2_20240514","symbol":"237880","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"No inventory/reorder durability; channel story alone is discounted.","MFE_90D_pct":22.1,"MAE_90D_pct":-19.4,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L46_237880_CLIO","trigger_id":"R13L46_237880_4C_20241111","symbol":"237880","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":42,"stage_label_before":"4C-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_after":35,"stage_label_after":"4C","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Thesis-break evidence routes to 4C but was late relative to drawdown.","MFE_90D_pct":26.5,"MAE_90D_pct":-12.6,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R13","loop":"46","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["consumer_channel_story_false_positive","price_only_local_4B_too_early","late_4C_after_prior_drawdown"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"avg≈18; four new symbols inside same canonical archetype; positive=2, counterexample=2, 4B=2, 4C=1","auto_selected_coverage_gap":"L5/C20 had underfilled positive/counterexample/4B-4C coverage relative to C18/C19"}
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
next_round = R13_loop_47
recommended_scope = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
reason = L5 now has C19 and C20 residual coverage; rotate to undercovered capital-return/financial rerating residuals.
```

## 28. Source Notes

Stock-Web files directly checked in this session:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/257/257720.json
atlas/symbol_profiles/003/003230.json
atlas/symbol_profiles/192/192820.json
atlas/symbol_profiles/237/237880.json
atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv
atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv
atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv
atlas/ohlcv_tradable_by_symbol_year/237/237880/2025.csv
```

Evidence labels are historical trigger-date evidence families, not new live discovery. The research uses them only for calibration row construction and residual error analysis.
