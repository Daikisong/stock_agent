# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 11
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION
output_file = e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

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

The purpose is not to re-prove the global Stage2/Green/4B axes. This R5 loop tests whether C20 needs a more precise distinction between **global channel reorder/export distribution** and **legacy China reopening or duty-free price-only optimism**.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 11
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION
```

R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`, so the round-sector pair passes the hard gate. C20 is selected because the prior R5 aggregate has enough broad representation, but the residual split between global K-beauty export/distribution winners and legacy China-channel false positives still needs tighter guardrails.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check:

```text
reports/e2r_calibration/by_round/R5.md
representative_triggers = 112
unique_cases = 26
Stage2/Stage2-Actionable/Stage3/4B/4C rows already exist
```

Selection therefore avoids a low-value repetition of generic consumer brand rerating. The selected cases emphasize new symbols and a specific residual path:

```text
positive side:
- global K-beauty distribution / reorder path
- ODM/export channel earnings acceleration

counterexample side:
- legacy China/duty-free price-only recovery narratives
- reopening optimism without reorder/margin bridge confirmation
```

Duplicate search status:

```text
same_symbol_same_trigger_date_research = avoided
same_canonical_archetype_research = allowed
same_archetype_new_symbol_count = 5
new_trigger_family_count = 5
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest and schema context:

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

Profile validation highlights:

```text
257720 실리콘투:
- first_date = 2021-09-29
- last_date = 2026-02-20
- corporate_action_candidate_dates = 2022-07-14, 2022-08-02
- selected 2024 window = clean_180D_window

241710 코스메카코리아:
- first_date = 2016-10-28
- last_date = 2026-02-20
- corporate_action_candidate_dates = 2018-04-25, 2018-05-18
- selected 2024 window = clean_180D_window

192820 코스맥스:
- first_date = 2014-04-07
- last_date = 2026-02-20
- corporate_action_candidate_dates = []
- selected 2024 window = clean_180D_window

051900 LG생활건강:
- first_date = 2001-04-25
- last_date = 2026-02-20
- corporate_action_candidate_dates = []
- selected 2022 window = clean_180D_window

090430 아모레퍼시픽:
- first_date = 2006-06-29
- last_date = 2026-02-20
- selected 2023 window = clean_180D_window
```

## 5. Historical Eligibility Gate

All representative triggers satisfy the eligibility gate:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available_by_stock_web_manifest = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

The fundamental evidence source is recorded as a research proxy and must be reattached with DART/KIND/news IDs during implementation. The price rows themselves are Stock-Web tradable OHLC rows.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

fine_archetype compression:
- K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION
- K_BEAUTY_ODM_EXPORT_REORDER_MARGIN_BRIDGE
- LEGACY_CHINA_DUTYFREE_PRICE_ONLY_FALSE_POSITIVE
- CHINA_REOPENING_RALLY_WITHOUT_REORDER_CONFIRMATION
```

The compression rule is simple: **C20 should not treat every “beauty China/reopening” story as equivalent to global distribution reorder evidence.** The former is a narrative tide; the latter is a purchase-order current.

## 7. Case Selection Summary

|case_id|company|symbol|case_type|pos_or_counter|entry_date|MFE_90D|MAE_90D|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|R5L11-C20-SILICON2-202405|실리콘투|257720|structural_success|positive|2024-05-13|103.4|-8.1|current_profile_correct|
|R5L11-C20-COSMECCA-202405|코스메카코리아|241710|structural_success|positive|2024-05-10|99.8|-9.5|current_profile_correct|
|R5L11-C20-COSMAX-202405|코스맥스|192820|high_mae_success|positive|2024-05-14|29.6|-27.7|current_profile_too_early|
|R5L11-C20-LGHNH-202201|LG생활건강|051900|false_positive_green|counterexample|2022-01-28|7.2|-31.2|current_profile_false_positive|
|R5L11-C20-AMORE-202302|아모레퍼시픽|090430|price_moved_without_evidence|counterexample|2023-02-02|3.2|-28.5|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 5
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive/counterexample split is intentionally not symmetric by market capitalization. It is symmetric by mechanism: channel reorder/export durability on one side, price-only China recovery optimism on the other.

## 9. Evidence Source Map

|case_id|evidence family|evidence source status|validation note|
|---|---|---|---|
|R5L11-C20-SILICON2-202405|global distribution/reorder + earnings acceleration|public quarterly disclosure proxy|DART/KIND filing ID should be attached later|
|R5L11-C20-COSMECCA-202405|ODM/export reorder + earnings acceleration|public quarterly disclosure proxy|DART/KIND filing ID should be attached later|
|R5L11-C20-COSMAX-202405|ODM revision + margin bridge, but high-MAE follow-through|public quarterly disclosure proxy|use as guarded positive, not clean Green proof|
|R5L11-C20-LGHNH-202201|legacy China/duty-free recovery narrative|public earnings/news proxy|counterexample: weak reorder/margin durability|
|R5L11-C20-AMORE-202302|China reopening price optimism|public reopening/news proxy|counterexample: price moved before evidence durability|

## 10. Price Data Source Map

|symbol|company|tradable shard|profile|clean 180D?|
|---|---|---|---|---|
|257720|실리콘투|atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/symbol_profiles/257/257720.json|yes|
|241710|코스메카코리아|atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv|atlas/symbol_profiles/241/241710.json|yes|
|192820|코스맥스|atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv|atlas/symbol_profiles/192/192820.json|yes|
|051900|LG생활건강|atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv|atlas/symbol_profiles/051/051900.json|yes|
|090430|아모레퍼시픽|atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv|atlas/symbol_profiles/090/090430.json|yes|

## 11. Case-by-Case Trigger Grid

|trigger_id|company|symbol|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak_date|peak_price|outcome|current_profile|dedupe|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L11-C20-SILICON2-STAGE2A-20240513|실리콘투|257720|Stage2-Actionable|2024-05-10|2024-05-13|26650|103.4|103.4|103.4|-8.1|-8.1|-8.1|2024-06-19|54200|strong_structural_success|current_profile_correct|True|
|R5L11-C20-SILICON2-4B-20240619|실리콘투|257720|Stage4B|2024-06-19|2024-06-19|50700|6.9|6.9|6.9|-20.6|-28.1|-46.7|2024-06-19|54200|4B_overlay_success|current_profile_correct|False|
|R5L11-C20-COSMECCA-STAGE2A-20240510|코스메카코리아|241710|Stage2-Actionable|2024-05-09|2024-05-10|46300|68.5|99.8|99.8|-9.5|-9.5|-9.5|2024-07-24|92500|strong_structural_success|current_profile_correct|True|
|R5L11-C20-COSMECCA-4B-20240724|코스메카코리아|241710|Stage4B|2024-07-24|2024-07-24|88800|4.2|4.2|14.2|-29.2|-32.0|-32.0|2024-07-24|92500|4B_overlay_success|current_profile_correct|False|
|R5L11-C20-COSMAX-STAGE2A-20240514|코스맥스|192820|Stage2-Actionable|2024-05-13|2024-05-14|160500|29.6|29.6|29.6|-3.9|-27.7|-27.7|2024-06-14|208000|high_mae_success|current_profile_too_early|True|
|R5L11-C20-LGHNH-STAGE2A-20220128|LG생활건강|051900|Stage2-Actionable|2022-01-27|2022-01-28|975000|7.2|7.2|7.2|-13.7|-31.2|-36.8|2022-02-18|1045000|false_positive_green|current_profile_false_positive|True|
|R5L11-C20-LGHNH-4C-20220314|LG생활건강|051900|Stage4C|2022-03-14|2022-03-14|841000|9.5|9.5|-5.8|-2.0|-25.6|-39.1|2022-04-05|921000|4C_late|current_profile_4C_too_late|False|
|R5L11-C20-AMORE-STAGE2-20230202|아모레퍼시픽|090430|Stage2|2023-02-02|2023-02-02|151000|3.2|3.2|3.2|-19.1|-28.5|-28.5|2023-02-10|155800|price_moved_without_evidence|current_profile_false_positive|True|

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

|case|symbol|entry|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|실리콘투|257720|2024-05-13|26650|103.4|-8.1|103.4|-8.1|103.4|-8.1|2024-06-19 / 54200|strong structural success|
|코스메카코리아|241710|2024-05-10|46300|68.5|-9.5|99.8|-9.5|99.8|-9.5|2024-07-24 / 92500|strong structural success|
|코스맥스|192820|2024-05-14|160500|29.6|-3.9|29.6|-27.7|29.6|-27.7|2024-06-14 / 208000|high-MAE success|
|LG생활건강|051900|2022-01-28|975000|7.2|-13.7|7.2|-31.2|7.2|-36.8|2022-02-18 / 1045000|false positive|
|아모레퍼시픽|090430|2023-02-02|151000|3.2|-19.1|3.2|-28.5|3.2|-28.5|2023-02-10 / 155800|price-only false positive|

Calculation note:

```text
MFE_N_pct = (max(high over observed N trading-day window) / entry_price - 1) * 100
MAE_N_pct = (min(low over observed N trading-day window) / entry_price - 1) * 100
values rounded to 0.1 percentage point
```

## 13. Current Calibrated Profile Stress Test

### Verdict summary

|case|current profile expected behavior|actual price result|verdict|
|---|---|---|---|
|실리콘투|Stage2/Yellow should pass; Green only with earnings/channel confirmation|MFE +103.4%, MAE -8.1%|current_profile_correct|
|코스메카코리아|Stage2/Yellow should pass; Green plausible with channel/revision evidence|MFE +99.8%, MAE -9.5%|current_profile_correct|
|코스맥스|Stage2/Yellow should pass; Green should be guarded|MFE +29.6%, MAE -27.7%|current_profile_too_early if promoted unguarded|
|LG생활건강|legacy China recovery should be blocked without reorder bridge|MFE +7.2%, MAE -36.8%|current_profile_false_positive|
|아모레퍼시픽|price-only reopening rally should not promote Stage2/3|MFE +3.2%, MAE -28.5%|current_profile_false_positive|

Answers to required stress-test questions:

```text
1. current calibrated profile would correctly block price-only 4B as positive evidence, but may still over-credit legacy China/reopening narratives if they are fed as public_event + relative_strength.
2. Actual MFE/MAE supports a C20-specific guard: global reorder/export distribution works; reopening price optimism does not.
3. Stage2 actionable bonus is not globally wrong, but C20 needs channel durability qualification.
4. Yellow threshold 75 is acceptable when channel_reorder_score exists; too permissive when only China reopening narrative exists.
5. Green threshold 87 / revision 55 is acceptable, but C20 ODM names with high MAE need repeat-order confirmation.
6. price-only blowoff guard is appropriate and strengthened.
7. full 4B non-price requirement is appropriate and strengthened.
8. hard 4C routing is too late for legacy China-channel breakdowns; a watch-only 4C precursor should be logged earlier.
```

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable for this MD
reason = no clean separate Stage3-Green public trigger rows were attached with independent disclosure timestamps
```

Interpretation:

```text
- This loop is not another proof that Stage2 is earlier than Green.
- The residual question is what C20 evidence should be allowed to reach Yellow/Green.
- Proposed answer: global channel reorder/export diversification can raise C20 confidence; legacy China/duty-free price optimism should remain watch-only until margin/reorder evidence appears.
```

## 15. 4B Local vs Full-window Timing Audit

|trigger|stage2_entry|4B_entry|local_peak|full_window_peak|local_proximity|full_window_proximity|verdict|
|---|---:|---:|---:|---:|---:|---:|---|
|R5L11-C20-SILICON2-4B-20240619|26650|50700|54200|54200|0.87|0.87|good_full_window_4B_timing|
|R5L11-C20-COSMECCA-4B-20240724|46300|88800|92500|92500|0.92|0.92|good_full_window_4B_timing|
|R5L11-C20-AMORE-STAGE2-20230202|151000|151000|155800|155800|1.00|1.00|price_only_local_peak_not_full_4B|

4B conclusion:

```text
existing_axis_tested = full_4b_requires_non_price_evidence
existing_axis_strengthened = true
new_axis_proposed = null
```

A price peak is a smoke alarm, not the fire report. For C20, 4B becomes useful only when valuation/positioning/revision slowdown evidence is attached; price-only peaks block promotion but do not by themselves define the thesis break.

## 16. 4C Protection Audit

|case|4C/watch candidate|label|protection interpretation|
|---|---|---|---|
|LG생활건강|2022-03-14 break below 841000 after failed bounce|hard_4c_late|current hard 4C catches damage after MAE already widened|
|아모레퍼시픽|post-Feb 2023 reopening rally fade|thesis_break_watch_only|should remain watch-only until reorder/margin evidence fails formally|
|코스맥스|post-June 2024 high-MAE drawdown|thesis_break_watch_only|not hard 4C, but ODM Green should be guarded|

C20-specific 4C note:

```text
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c, only for legacy China-channel watch timing
```

This does not propose a global rollback. It proposes that C20 legacy China/duty-free cases need an earlier **thesis-break watch** state before hard 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
candidate = L5_channel_reorder_export_durability_gate
```

Rule candidate:

```text
In L5 consumer/beauty names, promote Stage2-Actionable confidence only when at least one non-price distribution signal exists:
- channel reorder / sell-through evidence
- export-region diversification
- repeat order / ODM customer durability
- margin bridge from channel mix or operating leverage

If the only evidence is China reopening, duty-free rebound, or price relative strength, cap at Stage2-watch / Yellow-watch unless margin/reorder evidence appears.
```

Backtest effect:

```text
positive cases retained = 실리콘투, 코스메카코리아, guarded 코스맥스
false positives blocked = LG생활건강, 아모레퍼시픽
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
candidate = C20_global_channel_reorder_bonus_and_legacy_china_guard
```

Rule candidate:

```text
C20 positive bonus:
+1 shadow point when earnings/revision evidence is accompanied by global channel reorder or export diversification.

C20 guard:
-1 shadow point when the setup is primarily legacy China/duty-free/reopening optimism without channel reorder and margin bridge.

C20 high-MAE ODM guard:
-0.5 shadow point or Green-watch cap when 90D/180D MAE exceeds -25% despite positive MFE, unless repeat-order evidence is attached.
```

## 19. Before / After Backtest Comparison

|profile|id|hypothesis|changed_axes|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|avg_green_lateness|avg_4B_local|avg_4B_full|alignment|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current calibrated proxy|none|5|48.6|-21.0|48.6|-22.1|40%|0|1|n/a|0.895|0.895|mixed: positive works, legacy China false positives remain|
|P0b|e2r_2_0_baseline_reference|rollback reference|pre-calibrated thresholds|5|48.6|-21.0|48.6|-22.1|40%|0|2|n/a|0.895|0.895|worse false-positive separation|
|P1|L5_C20_sector_specific_candidate|add global channel reorder bonus and legacy China guard|+channel_reorder; -legacy_china_concentration|5|77.6|-15.1|77.6|-15.1|0%|0|1|n/a|0.895|0.895|better score-return alignment for R5 C20|
|P2|C20_archetype_candidate_profile|same as P1 but scoped to C20 only|+C20_channel_reorder; +repeat_order_guard|5|77.6|-15.1|77.6|-15.1|0%|0|0|n/a|0.895|0.895|preferred scope|
|P3|C20_counterexample_guard_profile|block price-only China reopening/duty-free narratives|-legacy_china_price_only|2|5.2|-23.9|5.2|-32.7|0%|n/a|n/a|n/a|||blocks false positives|

## 20. Score-Return Alignment Matrix

|profile|trigger|symbol|score_before|stage_before|score_after|stage_after|changed_components|alignment|
|---|---|---|---|---|---|---|---|---|
|e2r_2_1_stock_web_calibrated_proxy|R5L11-C20-SILICON2-STAGE2A-20240513|257720|82|Stage3-Yellow|94|Stage3-Green-shadow|channel_reorder_score,export_diversification_score|aligned|
|e2r_2_1_stock_web_calibrated_proxy|R5L11-C20-COSMECCA-STAGE2A-20240510|241710|82|Stage3-Yellow|94|Stage3-Green-shadow|channel_reorder_score,export_diversification_score|aligned|
|e2r_2_1_stock_web_calibrated_proxy|R5L11-C20-COSMAX-STAGE2A-20240514|192820|86|Stage3-Yellow-high-MAE-watch|83|Stage3-Yellow-guarded|execution_risk_score,channel_reorder_score|aligned|
|e2r_2_1_stock_web_calibrated_proxy|R5L11-C20-LGHNH-STAGE2A-20220128|051900|76|Stage3-Yellow-false-positive-risk|58|Stage2-watch-or-reject|legacy_china_concentration_risk,execution_risk_score|misaligned|
|e2r_2_1_stock_web_calibrated_proxy|R5L11-C20-AMORE-STAGE2-20230202|090430|76|Stage3-Yellow-false-positive-risk|58|Stage2-watch-or-reject|legacy_china_concentration_risk,execution_risk_score|misaligned|

Raw component interpretation:

```text
- channel_reorder_score and export_diversification_score separate true C20 winners from old China-channel narratives.
- legacy_china_concentration_risk is a counterexample guard, not a global anti-China rule.
- execution_risk_score is used for high-MAE ODM names where the thesis worked but the path was unstable.
```

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L5_CONSUMER_BRAND_DISTRIBUTION|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION|3|2|2|1|5|0|8|5|3|True|True|C20 still needs more non-K-beauty food/global distribution counterexamples, but beauty export/distribution coverage improves.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- legacy_china_price_only_false_positive
- high_MAE_ODM_success_needs_repeat_order_guard
- 4C_late_on_legacy_channel_break

new_axis_proposed: null
existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_weakened:
- hard_4c_thesis_break_routes_to_4c, only as earlier C20 thesis-break-watch routing

existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical OHLC backtest using Songdaiki/stock-web tradable_raw rows.
- 30D/90D/180D MFE and MAE proxy validation.
- C20 residual false-positive and high-MAE guard discovery.
- Shadow-only sector/canonical rule candidates.
```

Non-validation scope:

```text
- No current stock recommendation.
- No live candidate scan.
- No broker/API/trading integration.
- No stock_agent code access or patch.
- No production scoring change.
- No claim that DART/KIND filing IDs are already attached.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_global_channel_reorder_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"Reward global distribution/reorder evidence only when earnings revision and export/channel evidence are both present","Improves separation of Silicon2/Cosmecca from legacy China price-only rallies","R5L11-C20-SILICON2-STAGE2A-20240513|R5L11-C20-COSMECCA-STAGE2A-20240510",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_legacy_china_concentration_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-1,-1,"Penalize China/duty-free reopening narratives without channel reorder/margin bridge","Blocks Amore/LG H&H false positives","R5L11-C20-LGHNH-STAGE2A-20220128|R5L11-C20-AMORE-STAGE2-20230202",5,5,2,medium,counterexample_guard_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_high_MAE_ODM_repeat_order_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-0.5,-0.5,"ODM positive MFE with >25% 90D/180D MAE requires repeat-order confirmation before Green","Downgrades Cosmax high-MAE success from unguarded Green to guarded Yellow/Green-watch","R5L11-C20-COSMAX-STAGE2A-20240514",5,5,2,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L11-C20-SILICON2-202405", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L11-C20-SILICON2-STAGE2A-20240513", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Global K-beauty distribution/channel reorder case: export-distribution evidence plus price confirmation. Clean 180D window; corporate-action candidates are 2022 only, outside the 2024 window."}
{"row_type": "case", "case_id": "R5L11-C20-COSMECCA-202405", "symbol": "241710", "company_name": "코스메카코리아", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L11-C20-COSMECCA-STAGE2A-20240510", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "ODM/export-channel acceleration case with strong 30D/90D MFE; old 2018 corporate-action candidates do not contaminate the 2024 window."}
{"row_type": "case", "case_id": "R5L11-C20-COSMAX-202405", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R5L11-C20-COSMAX-STAGE2A-20240514", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "High-MAE success: clean near-term MFE, but the 180D drawdown shows ODM names need repeat-order/export-region durability before Green promotion."}
{"row_type": "case", "case_id": "R5L11-C20-LGHNH-202201", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R5L11-C20-LGHNH-STAGE2A-20220128", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "negative_or_false_positive_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "China/duty-free concentration counterexample: price bounce did not carry structural channel reorder evidence."}
{"row_type": "case", "case_id": "R5L11-C20-AMORE-202302", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R5L11-C20-AMORE-STAGE2-20230202", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "negative_or_false_positive_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "China reopening price optimism without durable reorder/margin evidence: MFE was shallow and MAE expanded."}
{"trigger_id": "R5L11-C20-SILICON2-STAGE2A-20240513", "case_id": "R5L11-C20-SILICON2-202405", "symbol": "257720", "company_name": "실리콘투", "sector": "consumer_beauty_distribution", "primary_archetype": "K-beauty global distribution reorder", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 26650, "evidence_available_at_that_date": "1Q24 earnings/revenue acceleration and global K-beauty distribution demand were publicly visible; timing treated as next-trading-day close because exact disclosure time is not attached in this standalone MD.", "evidence_source": "company quarterly earnings/public disclosure; later implementation should attach DART/KIND filing ID", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "MFE_30D_pct": 103.4, "MFE_90D_pct": 103.4, "MFE_180D_pct": 103.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.1, "MAE_90D_pct": -8.1, "MAE_180D_pct": -8.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -50.2, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "strong_structural_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R5L11-C20-SILICON2-202405-20240513-26650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-SILICON2-4B-20240619", "case_id": "R5L11-C20-SILICON2-202405", "symbol": "257720", "company_name": "실리콘투", "sector": "consumer_beauty_distribution", "primary_archetype": "K-beauty global distribution reorder", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-06-19", "entry_date": "2024-06-19", "entry_price": 50700, "evidence_available_at_that_date": "Price had travelled into a local/full-window blowoff zone after a rapid earnings rerating; 4B is treated as overlay only, not thesis break.", "evidence_source": "stock-web price path + valuation/positioning review proxy; later implementation should attach report/news evidence", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "MFE_30D_pct": 6.9, "MFE_90D_pct": 6.9, "MFE_180D_pct": 6.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.6, "MAE_90D_pct": -28.1, "MAE_180D_pct": -46.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -50.2, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R5L11-C20-SILICON2-202405-4B-20240619-50700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used for 4B timing overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-COSMECCA-STAGE2A-20240510", "case_id": "R5L11-C20-COSMECCA-202405", "symbol": "241710", "company_name": "코스메카코리아", "sector": "consumer_beauty_odm", "primary_archetype": "K-beauty ODM global reorder", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-09", "entry_date": "2024-05-10", "entry_price": 46300, "evidence_available_at_that_date": "Export/ODM demand and 1Q24 earnings acceleration were visible; next-trading-day close used because exact disclosure time is not attached.", "evidence_source": "company quarterly earnings/public disclosure; later implementation should attach DART/KIND filing ID", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv", "profile_path": "atlas/symbol_profiles/241/241710.json", "MFE_30D_pct": 68.5, "MFE_90D_pct": 99.8, "MFE_180D_pct": 99.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.5, "MAE_90D_pct": -9.5, "MAE_180D_pct": -9.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 92500, "drawdown_after_peak_pct": -32.0, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "strong_structural_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R5L11-C20-COSMECCA-202405-20240510-46300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-COSMECCA-4B-20240724", "case_id": "R5L11-C20-COSMECCA-202405", "symbol": "241710", "company_name": "코스메카코리아", "sector": "consumer_beauty_odm", "primary_archetype": "K-beauty ODM global reorder", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-07-24", "entry_date": "2024-07-24", "entry_price": 88800, "evidence_available_at_that_date": "Rerating had moved close to the observed full-window high; used as 4B overlay, not as positive-stage promotion evidence.", "evidence_source": "stock-web price path + valuation/positioning review proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv", "profile_path": "atlas/symbol_profiles/241/241710.json", "MFE_30D_pct": 4.2, "MFE_90D_pct": 4.2, "MFE_180D_pct": 14.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -29.2, "MAE_90D_pct": -32.0, "MAE_180D_pct": -32.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 92500, "drawdown_after_peak_pct": -32.0, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R5L11-C20-COSMECCA-202405-4B-20240724-88800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used for 4B timing overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-COSMAX-STAGE2A-20240514", "case_id": "R5L11-C20-COSMAX-202405", "symbol": "192820", "company_name": "코스맥스", "sector": "consumer_beauty_odm", "primary_archetype": "K-beauty ODM global reorder", "loop_objective": "yellow_threshold_stress_test|green_strictness_stress_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-13", "entry_date": "2024-05-14", "entry_price": 160500, "evidence_available_at_that_date": "1Q24 earnings/revision evidence existed, but 180D path later exposed high-MAE sensitivity; treat as positive with guard, not clean Green promotion.", "evidence_source": "company quarterly earnings/public disclosure; later implementation should attach DART/KIND filing ID", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "MFE_30D_pct": 29.6, "MFE_90D_pct": 29.6, "MFE_180D_pct": 29.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.9, "MAE_90D_pct": -27.7, "MAE_180D_pct": -27.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 208000, "drawdown_after_peak_pct": -44.2, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "same_entry_group_id": "R5L11-C20-COSMAX-202405-20240514-160500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-LGHNH-STAGE2A-20220128", "case_id": "R5L11-C20-LGHNH-202201", "symbol": "051900", "company_name": "LG생활건강", "sector": "consumer_beauty_brand_dutyfree", "primary_archetype": "legacy China luxury/duty-free channel", "loop_objective": "residual_false_positive_mining|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-01-27", "entry_date": "2022-01-28", "entry_price": 975000, "evidence_available_at_that_date": "Legacy China/duty-free recovery narrative existed, but durable reorder/margin evidence was weak; price bounce did not become structural rerating.", "evidence_source": "company earnings/public news; later implementation should attach source ID", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "MFE_30D_pct": 7.2, "MFE_90D_pct": 7.2, "MFE_180D_pct": 7.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.7, "MAE_90D_pct": -31.2, "MAE_180D_pct": -36.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-02-18", "peak_price": 1045000, "drawdown_after_peak_pct": -41.1, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R5L11-C20-LGHNH-202201-20220128-975000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-LGHNH-4C-20220314", "case_id": "R5L11-C20-LGHNH-202201", "symbol": "051900", "company_name": "LG생활건강", "sector": "consumer_beauty_brand_dutyfree", "primary_archetype": "legacy China luxury/duty-free channel", "loop_objective": "4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2022-03-14", "entry_date": "2022-03-14", "entry_price": 841000, "evidence_available_at_that_date": "The price path had already broken below the post-trigger setup; used as proxy 4C/watch row for thesis-break timing.", "evidence_source": "stock-web price path + later source attachment required", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "forced_liquidation_or_crash"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "MFE_30D_pct": 9.5, "MFE_90D_pct": 9.5, "MFE_180D_pct": -5.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.0, "MAE_90D_pct": -25.6, "MAE_180D_pct": -39.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-05", "peak_price": 921000, "drawdown_after_peak_pct": -33.1, "green_lateness_ratio": "not_applicable:4C_overlay", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4C_late", "current_profile_verdict": "current_profile_4C_too_late", "same_entry_group_id": "R5L11-C20-LGHNH-202201-4C-20220314-841000", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used for 4C timing overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R5L11-C20-AMORE-STAGE2-20230202", "case_id": "R5L11-C20-AMORE-202302", "symbol": "090430", "company_name": "아모레퍼시픽", "sector": "consumer_beauty_legacy_china", "primary_archetype": "China reopening price-only beauty rally", "loop_objective": "residual_false_positive_mining|counterexample_mining", "trigger_type": "Stage2", "trigger_date": "2023-02-02", "entry_date": "2023-02-02", "entry_price": 151000, "evidence_available_at_that_date": "China reopening optimism and price momentum existed, but durable reorder/margin confirmation was not yet visible.", "evidence_source": "public reopening/news narrative + stock-web price path; later implementation should attach source ID", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "MFE_30D_pct": 3.2, "MFE_90D_pct": 3.2, "MFE_180D_pct": 3.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.1, "MAE_90D_pct": -28.5, "MAE_180D_pct": -28.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-10", "peak_price": 155800, "drawdown_after_peak_pct": -30.7, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_peak_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R5L11-C20-AMORE-202302-20230202-151000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "row_type": "trigger", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_EXPORT_DISTRIBUTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11-C20-SILICON2-202405", "trigger_id": "R5L11-C20-SILICON2-STAGE2A-20240513", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 18, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 18, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12, "export_diversification_score": 8, "legacy_china_concentration_risk": 0}, "weighted_score_after": 94, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["channel_reorder_score", "export_diversification_score"], "component_delta_explanation": "C20 global channel reorder/export diversification is rewarded only when earnings and stock-web MFE align.", "MFE_90D_pct": 103.4, "MAE_90D_pct": -8.1, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11-C20-COSMECCA-202405", "trigger_id": "R5L11-C20-COSMECCA-STAGE2A-20240510", "symbol": "241710", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 18, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 18, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12, "export_diversification_score": 8, "legacy_china_concentration_risk": 0}, "weighted_score_after": 94, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["channel_reorder_score", "export_diversification_score"], "component_delta_explanation": "C20 global channel reorder/export diversification is rewarded only when earnings and stock-web MFE align.", "MFE_90D_pct": 99.8, "MAE_90D_pct": -9.5, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11-C20-COSMAX-202405", "trigger_id": "R5L11-C20-COSMAX-STAGE2A-20240514", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 20, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow-high-MAE-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 20, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 7, "export_diversification_score": 5, "legacy_china_concentration_risk": 0}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow-guarded", "changed_components": ["execution_risk_score", "channel_reorder_score"], "component_delta_explanation": "MFE was positive but 180D MAE argues against unguarded Green without repeat-order durability.", "MFE_90D_pct": 29.6, "MAE_90D_pct": -27.7, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11-C20-LGHNH-202201", "trigger_id": "R5L11-C20-LGHNH-STAGE2A-20220128", "symbol": "051900", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow-false-positive-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": -18}, "weighted_score_after": 58, "stage_label_after": "Stage2-watch-or-reject", "changed_components": ["legacy_china_concentration_risk", "execution_risk_score"], "component_delta_explanation": "Legacy China/duty-free price optimism is penalized when channel reorder and margin bridge are unsupported.", "MFE_90D_pct": 7.2, "MAE_90D_pct": -31.2, "score_return_alignment_label": "misaligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L11-C20-AMORE-202302", "trigger_id": "R5L11-C20-AMORE-STAGE2-20230202", "symbol": "090430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow-false-positive-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_diversification_score": 0, "legacy_china_concentration_risk": -18}, "weighted_score_after": 58, "stage_label_after": "Stage2-watch-or-reject", "changed_components": ["legacy_china_concentration_risk", "execution_risk_score"], "component_delta_explanation": "Legacy China/duty-free price optimism is penalized when channel reorder and margin bridge are unsupported.", "MFE_90D_pct": 3.2, "MAE_90D_pct": -28.5, "score_return_alignment_label": "misaligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "scheduled_round": "R5", "scheduled_loop": 11, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["legacy_china_price_only_false_positive", "high_MAE_ODM_success_needs_repeat_order_guard", "4C_late_on_legacy_channel_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 11
next_round = R6
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Primary price atlas:
- Songdaiki/stock-web
- manifest = atlas/manifest.json
- schema = atlas/schema.json
- universe = atlas/universe/all_symbols.csv

Fetched price/profile paths used:
- atlas/symbol_profiles/257/257720.json
- atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv
- atlas/symbol_profiles/241/241710.json
- atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv
- atlas/symbol_profiles/192/192820.json
- atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv
- atlas/symbol_profiles/051/051900.json
- atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv
- atlas/symbol_profiles/090/090430.json
- atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv

Important caveat:
- Fundamental evidence source IDs are represented as research proxies in this MD.
- The implementation agent should attach exact DART/KIND/news/report identifiers before treating those evidence labels as production-grade source evidence.
```

