# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 14
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_GLOBAL_PLATFORM_REORDER | K_BEAUTY_RIDDLE_SHOT_REPEAT_EXPORT_REORDER | LEGACY_BRAND_CHINA_CHANNEL_REBOUND_FALSE_POSITIVE
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration research artifact, not a live stock recommendation and not an implementation patch.

## 1. Current Calibrated Profile Assumption

Current profile proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes assumed in force:

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

The existing applied-axis source confirms that the calibrated profile already changed production defaults and includes the Stage2, Yellow, stricter Green, and 4B/4C guardrail axes. fileciteturn1222file0L3-L24

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test
```

Reason for auto-selection: R1/R2 representative set repetition is avoided. The ingest summary already covers many rounds and sectors, but this loop adds new C20-specific K-beauty channel-distribution positives and a legacy-brand false positive counterexample, rather than restating global Stage2/Green/4B rules. fileciteturn1221file0L14-L20

## 3. Previous Coverage / Duplicate Avoidance Check

```text
selection_mode = auto_coverage_gap_fill
auto_selected_coverage_gap = C20 needs explicit channel/reorder vs generic K-beauty theme separation
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 1
```

Duplicate gate result:

```text
same_symbol_same_trigger_date_research = false
schema_rematerialization_only = false
duplicate_low_value_loop = false
do_not_propose_new_weight_delta = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```text
source_name = FinanceData/marcap
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
```

The manifest records `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, the tradable/raw row counts, market set, and shard roots. fileciteturn1223file0L4-L60

Schema validation: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`; MFE/MAE formulas and calibration-usable rules are defined in the schema. fileciteturn1224file0L4-L78

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date is historical = true
entry row exists in stock-web tradable shard = true
minimum 180 forward tradable days available by manifest max_date = true
positive OHLCV fields = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

Symbol profile checks:

| symbol | company | first_date | last_date | tradable rows | corporate_action_candidate_dates relevant to 180D window | usable |
|---:|---|---|---|---:|---|---|
| 257720 | 실리콘투 | 2021-09-29 | 2026-02-20 | 1074 | none in 2024/2025 window; historical 2022 only | true |
| 018290 | 브이티 | 1996-07-03 | 2026-02-20 | 6972 | none in 2024/2025 window; old actions only | true |
| 090430 | 아모레퍼시픽 | 2006-06-29 | 2026-02-20 | 4834 | none in 2024/2025 window; historical 2015 only | true |

Profile citations: Silicontwo profile includes the current/latest name, available years, year files, and 2022-only corporate-action candidates. fileciteturn1209file0L3-L96 VT profile includes the current/latest name, long available years, and no 2024/2025 corporate-action candidate in the listed dates. fileciteturn1210file0L3-L136 fileciteturn1211file0L3-L37 Amorepacific profile includes available 2024/2025 files and a historical 2015 corporate-action candidate only. fileciteturn1212file0L3-L152 fileciteturn1213file0L3-L21

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype:
  - K_BEAUTY_US_GLOBAL_PLATFORM_REORDER
  - K_BEAUTY_RIDDLE_SHOT_REPEAT_EXPORT_REORDER
  - LEGACY_BRAND_CHINA_CHANNEL_REBOUND_FALSE_POSITIVE
```

Compression rule candidate:

```text
C20 should not mean "beauty stock moved."
C20 should mean:
  cross-border channel data,
  reorder velocity,
  product-level demand confirmation,
  non-China or diversified global distribution,
  and revision bridge visible near trigger date.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER | 257720 | 실리콘투 | positive / structural_success | 27,000 | 100.74 | -9.26 | 100.74 | -13.7 | current_profile_correct |
| R5L14_C20_018290_VT_RIDDLE_SHOT_REPEAT_REORDER | 018290 | 브이티 | positive / structural_success | 25,500 | 56.86 | -3.53 | 72.55 | -3.53 | current_profile_correct |
| R5L14_C20_090430_AMOREPACIFIC_LEGACY_CHINA_REBOUND_FALSE_GREEN | 090430 | 아모레퍼시픽 | counterexample / failed_rerating | 169,500 | 18.29 | -13.92 | 18.29 | -41.3 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1
minimum_positive_case_count_met = true
minimum_counterexample_count_met = true
minimum_calibration_usable_case_count_met = true
```

Silicontwo and VT show strong MFE with low early MAE. Amorepacific shows a short-lived rebound followed by a deep 180D drawdown, making it the necessary false-positive counterexample.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B/4C evidence | key distinction |
|---|---|---|---|---|
| R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER | 1Q24 disclosure / cross-border channel / relative strength | revision + global distribution visibility | later price/valuation blowoff | platform reorder, not simple cosmetics theme |
| R5L14_C20_018290_VT_RIDDLE_SHOT_REPEAT_REORDER | 1Q24 disclosure / product-level demand / relative strength | repeat reorder + product/customer confirmation | watch-only | product-specific overseas reorder |
| R5L14_C20_090430_AMOREPACIFIC_LEGACY_CHINA_REBOUND_FALSE_GREEN | 1Q24 rebound / large-brand global narrative | partial revision | thesis evidence broke later | legacy China/duty-free rebound not equal to C20 reorder |

## 10. Price Data Source Map

| symbol | shard | profile |
|---:|---|---|
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json |
| 018290 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv | atlas/symbol_profiles/018/018290.json |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv | atlas/symbol_profiles/090/090430.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown | aggregate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R5L14_C20_257720_T1_STAGE2A_2024-05-14 | Stage2-Actionable | 2024-05-13 | 2024-05-14 | 27,000 | 100.74 | -9.26 | 100.74 | -9.26 | 100.74 | -13.7 | 2024-06-19 / 54,200 | -57.01 | representative |
| R5L14_C20_018290_T1_STAGE2A_2024-05-14 | Stage2-Actionable | 2024-05-13 | 2024-05-14 | 25,500 | 52.94 | -3.53 | 56.86 | -3.53 | 72.55 | -3.53 | 2024-12-16 / 44,000 | -29.32 | representative |
| R5L14_C20_090430_T1_STAGE2Y_2024-04-30 | Stage3-Yellow | 2024-04-30 | 2024-04-30 | 169,500 | 18.29 | -4.84 | 18.29 | -13.92 | 18.29 | -41.3 | 2024-05-31 / 200,500 | -50.37 | representative |
| R5L14_C20_257720_T2_4B_PRICE_ONLY_2024-06-19 | Stage4B-overlay | 2024-06-19 | 2024-06-19 | 50,700 | 6.9 | -20.61 | 6.9 | -23.96 | 6.9 | -54.04 | 2024-06-19 / 54,200 | -57.01 | 4B_overlay_only |

Selected price rows:
- Silicontwo entry row: 2024-05-14 close 27,000, followed by highs through June including 54,200 on 2024-06-19; later 2024 lows are visible in November/December rows. fileciteturn1215file0L21-L50 fileciteturn1216file0L30-L63
- VT entry row: 2024-05-14 close 25,500; 30D/90D peaks include 39,000–40,000 in June; 180D peak area includes 44,000 on 2024-12-16. fileciteturn1217file0L11-L40 fileciteturn1218file0L39-L58
- Amorepacific entry row: 2024-04-30 close 169,500; 30D peak is 200,500 on 2024-05-31; later 180D low area includes 99,500 on 2024-12-09. fileciteturn1219file0L14-L39 fileciteturn1220file0L48-L58

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger backtest

| trigger_id | type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown | aggregate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R5L14_C20_257720_T1_STAGE2A_2024-05-14 | Stage2-Actionable | 2024-05-13 | 2024-05-14 | 27,000 | 100.74 | -9.26 | 100.74 | -9.26 | 100.74 | -13.7 | 2024-06-19 / 54,200 | -57.01 | representative |
| R5L14_C20_018290_T1_STAGE2A_2024-05-14 | Stage2-Actionable | 2024-05-13 | 2024-05-14 | 25,500 | 52.94 | -3.53 | 56.86 | -3.53 | 72.55 | -3.53 | 2024-12-16 / 44,000 | -29.32 | representative |
| R5L14_C20_090430_T1_STAGE2Y_2024-04-30 | Stage3-Yellow | 2024-04-30 | 2024-04-30 | 169,500 | 18.29 | -4.84 | 18.29 | -13.92 | 18.29 | -41.3 | 2024-05-31 / 200,500 | -50.37 | representative |
| R5L14_C20_257720_T2_4B_PRICE_ONLY_2024-06-19 | Stage4B-overlay | 2024-06-19 | 2024-06-19 | 50,700 | 6.9 | -20.61 | 6.9 | -23.96 | 6.9 | -54.04 | 2024-06-19 / 54,200 | -57.01 | 4B_overlay_only |

### 12.2 Metric interpretation

```text
Silicontwo:
  entry = 27,000
  peak = 54,200
  180D MFE = +100.74%
  180D MAE = -13.70%
  implication = strong C20 positive but needs later 4B overlay

VT:
  entry = 25,500
  peak = 44,000
  180D MFE = +72.55%
  180D MAE = -3.53%
  implication = cleaner structural C20 positive

Amorepacific:
  entry = 169,500
  peak = 200,500
  180D MFE = +18.29%
  180D MAE = -41.30%
  implication = false positive / failed rerating when legacy rebound is scored like channel reorder
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected label | actual path | verdict |
|---|---|---|---|
| Silicontwo | Stage3-Yellow/Green once revision and channel evidence appear | +100.74% 180D MFE | current_profile_correct |
| VT | Stage3-Yellow/Green once product-specific reorder appears | +72.55% 180D MFE, only -3.53% MAE | current_profile_correct |
| Amorepacific | likely Stage3-Yellow or false Green if legacy rebound gets C20 channel credit | +18.29% MFE but -41.30% MAE | current_profile_false_positive |

Answers to required stress questions:

```text
1. current calibrated profile judgment:
   - correct for Silicontwo and VT
   - too generous for Amorepacific if C20 channel/reorder evidence is inferred from legacy-brand rebound
2. actual MFE/MAE alignment:
   - positives aligned
   - Amore misaligned due deep 180D MAE
3. Stage2 bonus:
   - sufficient for true channel-reorder names
   - too generous when applied to generic K-beauty/legacy China rebound
4. Yellow threshold 75:
   - acceptable; not the main issue
5. Green threshold 87 / revision 55:
   - should stay strict; Amore supports not relaxing Green
6. price-only blowoff guard:
   - strengthened by Silicontwo 4B overlay: price peak needs non-price confirmation
7. full 4B non-price requirement:
   - kept/strengthened
8. hard 4C routing:
   - Amore should route to watch/4C-late when thesis evidence breaks
```

## 14. Stage2 / Yellow / Green Comparison

```text
Silicontwo:
  Stage2-Actionable entry = 27,000
  inferred Stage3-Green confirmation zone ≈ 36,400~39,200
  full observed peak after Stage2 = 54,200
  green_lateness_ratio ≈ 0.36
  verdict = Green somewhat late but still tradable

VT:
  Stage2-Actionable entry = 25,500
  inferred Stage3-Green confirmation zone ≈ 31,500~33,900
  full observed peak after Stage2 = 44,000
  green_lateness_ratio ≈ 0.42
  verdict = Green somewhat late but still acceptable

Amorepacific:
  no confirmed C20 Stage3-Green should be assigned under proposed guard
```

## 15. 4B Local vs Full-window Timing Audit

Silicontwo 4B overlay:

```text
Stage2_Actionable_entry_price = 27,000
Stage4B_overlay_entry_price = 50,700
local_peak_price_after_Stage2 = 54,200
full_window_peak_price_after_Stage2 = 54,200

four_b_local_peak_proximity = 0.87
four_b_full_window_peak_proximity = 0.87
four_b_evidence_type = price_only | valuation_blowoff | positioning_overheat
four_b_timing_verdict = price_only_local_peak_needs_non_price_confirmation
```

Interpretation: price-only 4B would have been directionally useful near the peak, but it should stay overlay-only and never train positive entry weights. This strengthens the existing full-4B non-price guardrail rather than proposing a global rollback.

## 16. 4C Protection Audit

```text
Silicontwo = thesis_break_watch_only after deep drawdown, not a 4C entry-weight row
VT = not_applicable
Amorepacific = hard_4c_late / thesis_evidence_broken after legacy rebound failed to sustain
```

Amorepacific is useful as a C20 guard case: once the old China/duty-free channel weakness reasserted, the positive C20 thesis should be demoted rather than treated as delayed Green.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
axis = l5_consumer_export_channel_reorder_visibility
proposal = +1 shadow credit when repeat cross-border channel/order evidence is explicit
```

Do not apply this globally. It belongs to consumer/brand/distribution where the stock path often hinges on whether sell-through/reorder is real, not merely whether a brand has a popular narrative.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
new_axis_proposed:
  - c20_channel_reorder_score
  - c20_legacy_brand_rebound_guard
```

Mechanism:

```text
if channel_reorder_score and global_distribution_score are both explicit:
    allow C20 Stage2-Actionable / Yellow-to-Green bridge
else if evidence is only legacy-brand rebound, China recovery, or generic K-beauty theme:
    cap at Stage2-Watch or Stage3-Yellow, block Green
```

## 19. Before / After Backtest Comparison

| profile | selected trigger count | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | missed structural | late green | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 58.63 | -8.90 | 63.86 | -19.51 | 0.33 | 0 | 1 | correct positives but one C20 false positive remains |
| P0b e2r_2_0_baseline_reference | 3 | 58.63 | -8.90 | 63.86 | -19.51 | 0.33 | 1 | 0 | looser Green risks Amore false positive; misses early C20 channel specificity |
| P1 sector_specific_candidate_profile | 3 | 58.63 | -8.90 | 63.86 | -19.51 | 0.00 | 0 | 1 | better L5 separation of reorder/export vs legacy rebound |
| P2 canonical_archetype_candidate_profile | 3 | 58.63 | -8.90 | 63.86 | -19.51 | 0.00 | 0 | 1 | best fit: add C20 channel_reorder and global_distribution components |
| P3 counterexample_guard_profile | 3 | 58.63 | -8.90 | 63.86 | -19.51 | 0.00 | 0 | 2 | safer but may delay strong positives if too strict |

## 20. Score-Return Alignment Matrix

| case_id | before score | before label | after score | after label | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| Silicontwo | 78 | Stage3-Yellow | 90 | Stage3-Green | 100.74 | -9.26 | improved positive capture |
| VT | 76 | Stage3-Yellow | 87 | Stage3-Green | 56.86 | -3.53 | improved positive capture |
| Amorepacific | 78 | Stage3-Yellow | 64 | Stage2-Watch | 18.29 | -13.92 | false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_US_GLOBAL_PLATFORM_REORDER / K_BEAUTY_RIDDLE_SHOT_REPEAT_EXPORT_REORDER / LEGACY_BRAND_CHINA_CHANNEL_REBOUND_FALSE_POSITIVE | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 1 | true | true | still needs food/export and channel-inventory counterexamples |


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
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - legacy_brand_rebound_false_positive
  - channel_reorder_vs_theme_confusion
new_axis_proposed:
  - c20_channel_reorder_score
  - c20_legacy_brand_rebound_guard
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high; same-archetype new symbols 3, new trigger families 3, positive/counterexample balance met
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C20 channel/reorder vs generic beauty/legacy rebound
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema
- symbol profile availability and corporate-action window caveats
- representative entry rows
- 30D/90D/180D MFE/MAE
- current calibrated profile stress test
- C20-specific positive/counterexample balance
```

Not validated:

```text
- live candidate suitability
- current 2026 watchlist
- broker execution
- production scoring patch
- actual code behavior under stock_agent src/e2r
- exact sell-side consensus history
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_reorder_score,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"reward explicit cross-border channel reorder / global distribution evidence","positive cases keep high MFE while counterexample is downgraded","R5L14_C20_257720_T1_STAGE2A_2024-05-14|R5L14_C20_018290_T1_STAGE2A_2024-05-14|R5L14_C20_090430_T1_STAGE2Y_2024-04-30",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_legacy_brand_rebound_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"legacy China/duty-free rebound is not the same as global channel reorder","reduces Amore false positive while preserving Silicontwo/VT positives","R5L14_C20_090430_T1_STAGE2Y_2024-04-30",3,3,1,medium,canonical_shadow_only,"guardrail, not global"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_GLOBAL_PLATFORM_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L14_C20_257720_T1_STAGE2A_2024-05-14","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"High 30D/90D/180D MFE with later drawdown. C20 needs channel/reorder evidence to distinguish durable export distribution from one-off beauty theme."}
{"row_type":"case","case_id":"R5L14_C20_018290_VT_RIDDLE_SHOT_REPEAT_REORDER","symbol":"018290","company_name":"브이티","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_RIDDLE_SHOT_REPEAT_EXPORT_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L14_C20_018290_T1_STAGE2A_2024-05-14","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Lower MAE than Silicontwo and cleaner sustained path; confirms that product-specific reorder evidence deserves more weight than generic K-beauty theme."}
{"row_type":"case","case_id":"R5L14_C20_090430_AMOREPACIFIC_LEGACY_CHINA_REBOUND_FALSE_GREEN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BRAND_CHINA_CHANNEL_REBOUND_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L14_C20_090430_T1_STAGE2Y_2024-04-30","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The price path says the mechanism did not behave like C20 reorder compounding. Legacy brand rebound should not receive the same channel-reorder score without hard reorder evidence."}
{"row_type":"trigger","trigger_id":"R5L14_C20_257720_T1_STAGE2A_2024-05-14","case_id":"R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_GLOBAL_PLATFORM_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / channel reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","evidence_available_at_that_date":"1Q24 earnings/reorder signal translated into the next tradable-date close; cross-border K-beauty distribution platform evidence, not simple price momentum.","evidence_source":"historical earnings disclosure/IR/news family; exact price validation from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":27000,"MFE_30D_pct":100.74,"MFE_90D_pct":100.74,"MFE_180D_pct":100.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.26,"MAE_90D_pct":-9.26,"MAE_180D_pct":-13.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_mfe_then_4B_overlay_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER__2024-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L14_C20_018290_T1_STAGE2A_2024-05-14","case_id":"R5L14_C20_018290_VT_RIDDLE_SHOT_REPEAT_REORDER","symbol":"018290","company_name":"브이티","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_RIDDLE_SHOT_REPEAT_EXPORT_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / channel reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","evidence_available_at_that_date":"1Q24 earnings/reorder signal with product-specific global demand confirmation; next-trading-date close used.","evidence_source":"historical earnings disclosure/IR/news family; exact price validation from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":25500,"MFE_30D_pct":52.94,"MFE_90D_pct":56.86,"MFE_180D_pct":72.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.53,"MAE_90D_pct":-3.53,"MAE_180D_pct":-3.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-16","peak_price":44000,"drawdown_after_peak_pct":-29.32,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_reorder_compounder","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L14_C20_018290_VT_RIDDLE_SHOT_REPEAT_REORDER__2024-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L14_C20_090430_T1_STAGE2Y_2024-04-30","case_id":"R5L14_C20_090430_AMOREPACIFIC_LEGACY_CHINA_REBOUND_FALSE_GREEN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BRAND_CHINA_CHANNEL_REBOUND_FALSE_POSITIVE","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / channel reorder","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-30","evidence_available_at_that_date":"1Q24 rebound and large-brand global expansion narrative; treated as counterexample because channel evidence was not the same as cross-border indie reorder velocity.","evidence_source":"historical earnings disclosure/IR/news family; exact price validation from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-30","entry_price":169500,"MFE_30D_pct":18.29,"MFE_90D_pct":18.29,"MFE_180D_pct":18.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.84,"MAE_90D_pct":-13.92,"MAE_180D_pct":-41.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500,"drawdown_after_peak_pct":-50.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating_high_MAE_false_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L14_C20_090430_AMOREPACIFIC_LEGACY_CHINA_REBOUND_FALSE_GREEN__2024-04-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L14_C20_257720_T2_4B_PRICE_ONLY_2024-06-19","case_id":"R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_GLOBAL_PLATFORM_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"K-beauty global distribution / channel reorder","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2024-06-19","evidence_available_at_that_date":"Price/valuation blowoff around local peak but no clean non-price 4B evidence at that date.","evidence_source":"price-only overlay stress test; exact price from Songdaiki/stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":50700,"MFE_30D_pct":6.9,"MFE_90D_pct":6.9,"MFE_180D_pct":6.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.61,"MAE_90D_pct":-23.96,"MAE_180D_pct":-54.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":0.87,"four_b_timing_verdict":"price_only_local_peak_needs_non_price_confirmation","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_but_not_positive_weight","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L14_C20_257720_4B_2024-06-19","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_new_4B_overlay_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C20_257720_SILICONTWO_Q1_EXPORT_PLATFORM_REORDER","trigger_id":"R5L14_C20_257720_T1_STAGE2A_2024-05-14","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":18,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":10,"global_distribution_score":8},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":18,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":18,"global_distribution_score":14},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["channel_reorder_score","global_distribution_score","customer_quality_score"],"component_delta_explanation":"C20-specific shadow adds weight only when export distribution and repeat reorder are explicit, not just beauty theme.","MFE_90D_pct":100.74,"MAE_90D_pct":-9.26,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C20_018290_VT_RIDDLE_SHOT_REPEAT_REORDER","trigger_id":"R5L14_C20_018290_T1_STAGE2A_2024-05-14","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":17,"relative_strength_score":12,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":9,"global_distribution_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":17,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":17,"global_distribution_score":13},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["channel_reorder_score","global_distribution_score","customer_quality_score"],"component_delta_explanation":"Product-specific overseas reorder evidence closes the gap to Green without relaxing global Green threshold.","MFE_90D_pct":56.86,"MAE_90D_pct":-3.53,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C20_090430_AMOREPACIFIC_LEGACY_CHINA_REBOUND_FALSE_GREEN","trigger_id":"R5L14_C20_090430_T1_STAGE2Y_2024-04-30","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":18,"relative_strength_score":10,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8,"global_distribution_score":6},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":18,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":1,"global_distribution_score":3},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["channel_reorder_score","global_distribution_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"Legacy China rebound/global brand narrative is not equivalent to cross-border channel reorder; C20 guard downgrades false Green.","MFE_90D_pct":18.29,"MAE_90D_pct":-13.92,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["legacy_brand_rebound_false_positive","channel_reorder_vs_theme_confusion"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R5 / C18 or C20 holdout
recommended_next_gap:
  - food/global distribution C20 analog
  - C18 export-channel reorder where sell-through data is present
  - additional C20 counterexample: influencer/viral beauty theme without reorder conversion
```

## 28. Source Notes

Price-source notes:
- Stock-Web manifest and schema were read directly from Songdaiki/stock-web. fileciteturn1223file0L4-L60 fileciteturn1224file0L4-L78
- Silicontwo, VT, and Amorepacific profile checks used stock-web symbol profiles. fileciteturn1209file0L3-L96 fileciteturn1210file0L3-L136 fileciteturn1211file0L3-L37 fileciteturn1212file0L3-L152
- The OHLC trigger/peak/drawdown rows used actual tradable shard rows from stock-web. fileciteturn1215file0L21-L50 fileciteturn1216file0L30-L63 fileciteturn1217file0L11-L40 fileciteturn1218file0L39-L58 fileciteturn1219file0L14-L39 fileciteturn1220file0L48-L58

Non-source disclaimer:
- This is historical calibration research only.
- This is not investment advice.
- No production scoring was changed.
