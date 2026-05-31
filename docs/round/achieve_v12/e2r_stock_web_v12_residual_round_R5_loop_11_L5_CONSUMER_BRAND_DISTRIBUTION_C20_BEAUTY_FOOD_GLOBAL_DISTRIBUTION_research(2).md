# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R5",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 11,
  "computed_next_round": "R6",
  "computed_next_loop": 11,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
  "fine_archetype_id": "K_BEAUTY_NON_CHINA_GLOBAL_CHANNEL_REORDER_PLATFORM_ODM",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "residual_false_positive_mining",
    "residual_missed_structural_mining",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "4B_non_price_requirement_stress_test",
    "green_strictness_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 3,
  "diversity_score_summary": "estimated +46; wrong_round_penalty=0; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0",
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

This loop adds 3 new independent cases, 1 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

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

No production scoring is changed. This file only proposes shadow-only sector/canonical rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 11
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_NON_CHINA_GLOBAL_CHANNEL_REORDER_PLATFORM_ODM
round_schedule_status = valid
round_sector_consistency = pass
```

This file follows the prior R4 loop 11 next state and advances to R5. It does not jump to R13 or another coverage gap.

## 3. Previous Coverage / Duplicate Avoidance Check

The prior generated MD was R4 / L4 / C17. This loop moves to the scheduled R5 consumer/brand/distribution round and selects C20 rather than repeating materials, battery, or semiconductor cases.

```text
same_canonical_archetype_research = allowed
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | company | profile_path | corporate-action candidates | selected window status |
|---:|---|---|---|---|
| 257720 | 실리콘투 | atlas/symbol_profiles/257/257720.json | 2022-07-14, 2022-08-02 | clean for 2023-2024 selected windows |
| 192820 | 코스맥스 | atlas/symbol_profiles/192/192820.json | none | clean |
| 090430 | 아모레퍼시픽 | atlas/symbol_profiles/090/090430.json | 2015-05-08 | clean for 2023 selected window |
| 161890 | 한국콜마 | atlas/symbol_profiles/161/161890.json | none | narrative holdout only |

## 5. Historical Eligibility Gate

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false
calibration_usable = true for representative rows
```

The 180D representative windows are all before the stock-web manifest max_date and do not overlap the profile corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| K_BEAUTY_NON_CHINA_GLOBAL_PLATFORM_DISTRIBUTION_REORDER | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Cross-border channel/platform reorder signal; not a legacy single-market brand thesis. |
| K_BEAUTY_ODM_GLOBAL_CUSTOMER_REORDER_MARGIN_BRIDGE | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | ODM customer reorder + margin bridge; distribution pull-through rather than pure brand multiple. |
| LEGACY_CHINA_REOPENING_CHANNEL_FALSE_GREEN | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Brand-channel reopening beta without reorder/inventory proof. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R5L11_C20_257720_SILICON2_GLOBAL_PLATFORM_REORDER_20230515 | 257720 | 실리콘투 | positive / missed structural | K-beauty global platform distribution carried reorder quality before classic brand EPS confirmation. |
| R5L11_C20_192820_COSMAX_ODM_GLOBAL_REORDER_20230515 | 192820 | 코스맥스 | positive / structural success | ODM customer reorder and margin bridge created rerating. |
| R5L11_C20_090430_AMORE_CHINA_REOPENING_FALSE_GREEN_20230210 | 090430 | 아모레퍼시픽 | counterexample / false positive | China reopening narrative lacked channel inventory/reorder confirmation. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
4B_case_count = 1
4C_case_count = 0
```

The C20 distinction is not “beauty stock up.” It is the difference between a store shelf that keeps being refilled and a display window that only looks busy. 실리콘투 and 코스맥스 had the refill mechanism: non-China/global channel pull-through, customer quality, and reorder visibility. 아모레퍼시픽 had the display-window narrative: China reopening and legacy brand beta, but no durable reorder/inventory proof.

## 9. Evidence Source Map

| symbol | evidence family | source status | use |
|---:|---|---|---|
| 257720 | non-China/global K-beauty platform distribution, reorder visibility, relative strength | public filing/news/research-summary family; exact URLs require enrichment before production promotion | quantitative |
| 192820 | ODM/global customer reorder, margin bridge, revision path | public filing/news/research-summary family; exact URLs require enrichment before production promotion | quantitative |
| 090430 | China reopening/legacy channel optimism, weak inventory/reorder proof | public filing/news/research-summary family; exact URLs require enrichment before production promotion | quantitative counterexample |
| 161890 | same-family ODM holdout | checked but not aggregated | narrative-only |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv | atlas/symbol_profiles/257/257720.json | 2023-05-15 | usable |
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv | atlas/symbol_profiles/257/257720.json | 2023-10-13 | usable 4B overlay |
| 192820 | atlas/ohlcv_tradable_by_symbol_year/192/192820/2023.csv | atlas/symbol_profiles/192/192820.json | 2023-05-15 | usable |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv | atlas/symbol_profiles/090/090430.json | 2023-02-10 | usable |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 실리콘투 global platform reorder | 257720 | Stage2-Actionable | 2023-05-15 | 4,915 | +49.75% | +97.36% | +115.87% | -7.43% | -7.43% | -7.43% | missed structural / positive |
| 코스맥스 ODM global reorder | 192820 | Stage3-Yellow | 2023-05-15 | 86,000 | +11.63% | +82.79% | +82.79% | -8.02% | -8.02% | -8.02% | structural success |
| 아모레퍼시픽 China reopening false Green | 090430 | false Green | 2023-02-10 | 153,000 | +1.83% | +1.83% | +1.83% | -20.13% | -36.47% | -38.63% | false positive |
| 실리콘투 price-only local 4B | 257720 | 4B price-only local peak | 2023-10-13 | 10,240 | +3.61% | +3.61% | +419.53% | -28.42% | -28.42% | -28.42% | 4B too early |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

| metric | 257720 | 192820 | 090430 |
|---|---:|---:|---:|
| entry_price | 4,915 | 86,000 | 153,000 |
| MFE_30D_pct | +49.75 | +11.63 | +1.83 |
| MFE_90D_pct | +97.36 | +82.79 | +1.83 |
| MFE_180D_pct | +115.87 | +82.79 | +1.83 |
| MAE_30D_pct | -7.43 | -8.02 | -20.13 |
| MAE_90D_pct | -7.43 | -8.02 | -36.47 |
| MAE_180D_pct | -7.43 | -8.02 | -38.63 |

Aggregate interpretation:

```text
positive_structural_avg_MFE_90D_pct = 90.08
positive_structural_avg_MAE_90D_pct = -7.73
counterexample_MFE_90D_pct = 1.83
counterexample_MAE_90D_pct = -36.47
```

## 13. Current Calibrated Profile Stress Test

| case | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| 실리콘투 global platform reorder | likely underweights distribution/platform reorder before conventional revision | +97.36% MFE90 / -7.43% MAE90 | current_profile_missed_structural |
| 코스맥스 ODM reorder | likely waits for stronger reported revision confirmation | +82.79% MFE90 / -8.02% MAE90 | current_profile_too_late |
| 아모레퍼시픽 China reopening | may over-promote legacy brand/reopening beta | +1.83% MFE90 / -36.47% MAE90 | current_profile_false_positive |
| 실리콘투 2023 local peak 4B | price-only peak looks hot locally, but full-window peak came later | local proximity 0.94 / full-window proximity 0.11 | current_profile_4B_too_early |

Axis verdict:

```text
stage2_actionable_evidence_bonus = existing_axis_strengthened for global reorder/platform evidence
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_weakened only for C20 non-China/global reorder + customer quality exception
stage3_green_revision_min = existing_axis_weakened only when reorder/channel evidence is independently strong
stage3_cross_evidence_green_buffer = existing_axis_strengthened
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = not_primary_tested
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2 / Watch:
  brand narrative, China reopening, or cosmetic sector beta without reorder proof

Stage2-Actionable:
  non-China/global channel expansion, platform distribution, early reorder, customer diversification

Stage3-Yellow:
  reorder and margin bridge visible, but reported revision still incomplete

Stage3-Green:
  reorder + channel quality + non-China/global mix + financial visibility or margin bridge

False Green guard:
  legacy China reopening, brand size, or valuation rebound without inventory/reorder quality

4B overlay:
  valuation blowoff or local price peak only becomes full 4B when non-price evidence also shows channel/reorder deterioration
```

Green lateness:

| case | early actionable entry | later Green/proxy | full observed peak | green_lateness_ratio | read |
|---|---:|---:|---:|---:|---|
| 257720 | 4,915 | 8,080 proxy after August confirmation | 54,200 full observed peak | 0.20 | current profile too late/missed structural |
| 192820 | 86,000 | 133,100 proxy after August confirmation | 157,200 near-term peak | 0.35 | Green somewhat late |
| 090430 | not_applicable | false Green | 155,800 local high | not_applicable | false positive |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R5L11_T01B_SILICON2_20231013_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 0.94 | 0.11 | price_only_local_4B_too_early |

For a platform-style K-beauty winner, the first local chart peak can be like a crowded checkout line, not a closed store. Unless channel/reorder deterioration is visible, price-only local 4B can eject the system too early.

## 16. 4C Protection Audit

```text
hard_4c_success = not_primary_tested
hard_4c_late = not_primary_tested
false_break = not_primary_tested
thesis_break_watch_only = Amore false-positive guard and Silicon2 price-only 4B overlay
```

This is a C20 positive-stage and 4B-guard loop, not a hard-4C thesis-break loop.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
candidate_axis = consumer_global_reorder_quality_vs_reopening_beta
```

Candidate rule:

```text
In L5 consumer/brand/distribution names, positive-stage promotion should distinguish repeatable channel reorder and customer quality from one-off reopening or brand-size beta.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
new_axis_proposed:
  - c20_non_china_global_reorder_quality_boost
  - c20_legacy_china_reopening_false_green_guard
  - c20_price_only_local_4b_too_early_guard
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | current representative | +60.66 | -17.31 | +66.83 | -18.03 | 0.33 | 1 | 1 | 0.28 | mixed; one missed structural, one false positive |
| P0b e2r_2_0_baseline_reference | 3 | baseline representative | +60.66 | -17.31 | +66.83 | -18.03 | 0.33 | 1 | 1 | 0.28 | too much brand/reopening beta |
| P1 sector_specific_candidate_profile | 3 | reorder quality guard | +90.08 positive / +1.83 blocked | -7.73 positive / -36.47 blocked | +99.33 positive / +1.83 blocked | -7.73 positive / -38.63 blocked | 0.00 | 0 | 0 | 0.28 | better positive/counterexample separation |
| P2 canonical_archetype_candidate_profile | 3 | C20 global reorder + China false-Green guard | +90.08 positive / +1.83 blocked | -7.73 positive / -36.47 blocked | +99.33 positive / +1.83 blocked | -7.73 positive / -38.63 blocked | 0.00 | 0 | 0 | 0.28 | best explanatory fit |
| P3 counterexample_guard_profile | 3 | China-reopening guard only | +60.66 | -17.31 | +66.83 | -18.03 | 0.00 false-Green | 1 | 1 | 0.28 | safer, but still misses platform reorder upside |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90/MAE90 | alignment |
|---|---:|---|---:|---|---|---|
| 257720 | 74.0 | Stage2-Actionable_high | 88.5 | Stage3-Green | +97.36 / -7.43 | missed structural corrected |
| 192820 | 82.0 | Stage3-Yellow | 88.0 | Stage3-Green | +82.79 / -8.02 | Green exception aligned |
| 090430 | 77.0 | Stage3-Yellow_or_false_Green | 59.0 | Stage2-Watch_or_false_positive_blocked | +1.83 / -36.47 | false positive avoided |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_NON_CHINA_GLOBAL_CHANNEL_REORDER_PLATFORM_ODM | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | C20 now has non-China/global reorder positives, a China reopening false-Green guard, and a price-only local 4B too-early overlay. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - non_china_global_reorder_missed_structural
  - ODM_global_customer_reorder_green_too_late
  - legacy_china_reopening_false_green
  - price_only_local_4B_too_early
new_axis_proposed:
  - c20_non_china_global_reorder_quality_boost
  - c20_legacy_china_reopening_false_green_guard
  - c20_price_only_local_4b_too_early_guard
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened:
  - stage3_green_total_min, only under C20 reorder/channel-quality exception
  - stage3_green_revision_min, only when reorder/channel evidence is independently strong
existing_axis_kept:
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted price basis
- profile availability and corporate-action caveats for 257720, 192820, 161890, 090430
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE calculations from visible stock-web OHLC rows
- clean 180D corporate-action windows for selected quantitative rows
- R5/L5/C20 schedule consistency
```

Not validated:

```text
- production stock_agent source code
- live watchlist or current candidates
- brokerage execution
- exact original disclosure/report URLs for evidence text
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_non_china_global_reorder_quality_boost,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"Non-China/global channel reorder and platform/ODM customer quality explained positive MFE better than legacy brand size","257720 MFE90 +97.36 and 192820 MFE90 +82.79 with controlled MAE","R5L11_T01_SILICON2_20230515_STAGE2_ACTIONABLE_PLATFORM_REORDER|R5L11_T02_COSMAX_20230515_STAGE3_YELLOW_ODM_REORDER",3,3,1,medium,canonical_shadow_only,"not production; exact evidence URLs need enrichment"
shadow_weight,c20_legacy_china_reopening_false_green_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"China reopening/legacy channel beta without reorder and inventory-quality proof created false Green risk","090430 MFE90 +1.83 and MAE90 -36.47","R5L11_T03_AMORE_20230210_FALSE_GREEN_CHINA_REOPENING",3,3,1,medium,guardrail_shadow_only,"cap Green unless channel reorder/inventory quality confirms thesis"
shadow_weight,c20_price_only_local_4b_too_early_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+0.5,+0.5,"K-beauty platform winners can make local price peaks before structural thesis is exhausted; price-only 4B is too early","257720 local 4B proximity 0.94 but full-window proximity 0.11","R5L11_T01B_SILICON2_20231013_PRICE_ONLY_LOCAL_4B_TOO_EARLY",3,3,1,low,overlay_guard_shadow_only,"strengthens existing price-only blowoff guard; not standalone demotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L11_C20_257720_SILICON2_GLOBAL_PLATFORM_REORDER_20230515","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_NON_CHINA_GLOBAL_PLATFORM_DISTRIBUTION_REORDER","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"R5L11_T01_SILICON2_20230515_STAGE2_ACTIONABLE_PLATFORM_REORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Non-China platform distribution/reorder signal produced high MFE before conventional brand-revision confirmation.","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Positive C20 case: global K-beauty distribution platform was a stronger signal than legacy China beauty beta."}
{"row_type":"case","case_id":"R5L11_C20_192820_COSMAX_ODM_GLOBAL_REORDER_20230515","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_REORDER_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L11_T02_COSMAX_20230515_STAGE3_YELLOW_ODM_REORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ODM/global customer reorder and margin bridge produced strong 90D rerating after May 2023 entry.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive C20 case: ODM reorder quality mattered more than simple cosmetics-sector beta."}
{"row_type":"case","case_id":"R5L11_C20_090430_AMORE_CHINA_REOPENING_FALSE_GREEN_20230210","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_CHINA_REOPENING_CHANNEL_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R5L11_T03_AMORE_20230210_FALSE_GREEN_CHINA_REOPENING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"China reopening/legacy channel optimism produced weak MFE and large MAE; no durable reorder or margin bridge.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample C20 case: brand size and reopening narrative were not enough without channel inventory/reorder confirmation."}
{"row_type":"trigger","trigger_id":"R5L11_T01_SILICON2_20230515_STAGE2_ACTIONABLE_PLATFORM_REORDER","case_id":"R5L11_C20_257720_SILICON2_GLOBAL_PLATFORM_REORDER_20230515","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_NON_CHINA_GLOBAL_PLATFORM_DISTRIBUTION_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"BEAUTY_FOOD_GLOBAL_DISTRIBUTION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","evidence_available_at_that_date":"Non-China/global K-beauty platform distribution and reorder visibility became investable; price row confirmed actual entry close at 4,915.","evidence_source":"public filings/news/research-summary evidence family; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":4915,"MFE_30D_pct":49.75,"MFE_90D_pct":97.36,"MFE_180D_pct":115.87,"MFE_1Y_pct":499.19,"MFE_2Y_pct":null,"MAE_30D_pct":-7.43,"MAE_90D_pct":-7.43,"MAE_180D_pct":-7.43,"MAE_1Y_pct":-7.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":0.2,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11_257720_20230515_4915","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11_T01B_SILICON2_20231013_PRICE_ONLY_LOCAL_4B_TOO_EARLY","case_id":"R5L11_C20_257720_SILICON2_GLOBAL_PLATFORM_REORDER_20230515","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_NON_CHINA_GLOBAL_PLATFORM_DISTRIBUTION_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"BEAUTY_FOOD_GLOBAL_DISTRIBUTION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"4B-PriceOnlyLocalPeak","trigger_date":"2023-10-13","evidence_available_at_that_date":"A local price blowoff around 10,610 high existed, but non-price deterioration was not established and the full observed window later reached a much higher 2024 peak.","evidence_source":"public filings/news/research-summary evidence family; exact original URLs must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-13","entry_price":10240,"MFE_30D_pct":3.61,"MFE_90D_pct":3.61,"MFE_180D_pct":419.53,"MFE_1Y_pct":499.19,"MFE_2Y_pct":null,"MAE_30D_pct":-28.42,"MAE_90D_pct":-28.42,"MAE_180D_pct":-28.42,"MAE_1Y_pct":-7.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.11,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11_257720_20231013_10240","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same Silicon2 case, different 4B timing family; not representative for aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L11_T02_COSMAX_20230515_STAGE3_YELLOW_ODM_REORDER","case_id":"R5L11_C20_192820_COSMAX_ODM_GLOBAL_REORDER_20230515","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_REORDER_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"BEAUTY_FOOD_GLOBAL_DISTRIBUTION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"Stage3-Yellow","trigger_date":"2023-05-15","evidence_available_at_that_date":"ODM/global customer reorder and margin bridge were emerging, but later confirmation created a conventional Green label too late.","evidence_source":"public filings/news/research-summary evidence family; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2023.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":86000,"MFE_30D_pct":11.63,"MFE_90D_pct":82.79,"MFE_180D_pct":82.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.02,"MAE_90D_pct":-8.02,"MAE_180D_pct":-8.02,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-01","peak_price":157200,"drawdown_after_peak_pct":-29.58,"green_lateness_ratio":0.35,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11_192820_20230515_86000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11_T03_AMORE_20230210_FALSE_GREEN_CHINA_REOPENING","case_id":"R5L11_C20_090430_AMORE_CHINA_REOPENING_FALSE_GREEN_20230210","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_CHINA_REOPENING_CHANNEL_FALSE_GREEN","sector":"소비재·유통·브랜드","primary_archetype":"BEAUTY_FOOD_GLOBAL_DISTRIBUTION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"Stage3-Green-FalsePositive","trigger_date":"2023-02-10","evidence_available_at_that_date":"China reopening and legacy brand-channel optimism were visible, but channel inventory/reorder and margin bridge were not durable enough.","evidence_source":"public filings/news/research-summary evidence family; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":153000,"MFE_30D_pct":1.83,"MFE_90D_pct":1.83,"MFE_180D_pct":1.83,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.13,"MAE_90D_pct":-36.47,"MAE_180D_pct":-38.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-10","peak_price":155800,"drawdown_after_peak_pct":-39.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"false_positive_green_guard_needed","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11_090430_20230210_153000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11_C20_257720_SILICON2_GLOBAL_PLATFORM_REORDER_20230515","trigger_id":"R5L11_T01_SILICON2_20230515_STAGE2_ACTIONABLE_PLATFORM_REORDER","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":48,"relative_strength_score":76,"customer_quality_score":54,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":58,"global_distribution_score":64,"non_china_mix_score":62,"inventory_quality_score":0,"platform_take_rate_score":66,"brand_customer_diversification_score":70,"china_reopening_dependency_score":0,"positioning_overheat_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable_high","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":58,"relative_strength_score":84,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":64,"execution_risk_score":38,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":88,"global_distribution_score":92,"non_china_mix_score":86,"inventory_quality_score":0,"platform_take_rate_score":90,"brand_customer_diversification_score":84,"china_reopening_dependency_score":0,"positioning_overheat_score":0},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green","changed_components":["channel_reorder_score","global_distribution_score","non_china_mix_score","platform_take_rate_score","customer_quality_score"],"component_delta_explanation":"Non-China/global distribution platform and repeat-order quality should promote earlier than classic brand EPS confirmation.","MFE_90D_pct":97.36,"MAE_90D_pct":-7.43,"score_return_alignment_label":"missed structural signal corrected","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11_C20_192820_COSMAX_ODM_GLOBAL_REORDER_20230515","trigger_id":"R5L11_T02_COSMAX_20230515_STAGE3_YELLOW_ODM_REORDER","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":64,"customer_quality_score":64,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":40,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":64,"global_distribution_score":68,"non_china_mix_score":66,"inventory_quality_score":0,"platform_take_rate_score":0,"brand_customer_diversification_score":74,"china_reopening_dependency_score":0,"positioning_overheat_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":76,"revision_score":68,"relative_strength_score":70,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":82,"global_distribution_score":84,"non_china_mix_score":78,"inventory_quality_score":0,"platform_take_rate_score":0,"brand_customer_diversification_score":84,"china_reopening_dependency_score":0,"positioning_overheat_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","channel_reorder_score","global_distribution_score","customer_quality_score"],"component_delta_explanation":"ODM customer-reorder and margin bridge justified earlier Green than classic reported-revision-only confirmation.","MFE_90D_pct":82.79,"MAE_90D_pct":-8.02,"score_return_alignment_label":"Green threshold exception aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11_C20_090430_AMORE_CHINA_REOPENING_FALSE_GREEN_20230210","trigger_id":"R5L11_T03_AMORE_20230210_FALSE_GREEN_CHINA_REOPENING","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":44,"relative_strength_score":62,"customer_quality_score":46,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":46,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":38,"global_distribution_score":40,"non_china_mix_score":28,"inventory_quality_score":34,"platform_take_rate_score":0,"brand_customer_diversification_score":0,"china_reopening_dependency_score":82,"positioning_overheat_score":0},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow_or_false_Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":36,"relative_strength_score":42,"customer_quality_score":34,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":66,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":24,"global_distribution_score":30,"non_china_mix_score":20,"inventory_quality_score":24,"platform_take_rate_score":0,"brand_customer_diversification_score":0,"china_reopening_dependency_score":88,"positioning_overheat_score":0},"weighted_score_after":59.0,"stage_label_after":"Stage2-Watch_or_false_positive_blocked","changed_components":["china_reopening_dependency_score","channel_reorder_score","inventory_quality_score","execution_risk_score"],"component_delta_explanation":"Legacy China reopening narrative without reorder/inventory quality should be blocked from Green.","MFE_90D_pct":1.83,"MAE_90D_pct":-36.47,"score_return_alignment_label":"false positive avoided","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["non_china_global_reorder_missed_structural","ODM_global_customer_reorder_green_too_late","legacy_china_reopening_false_green","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R5L11_C20_161890_KOLMAR_ODM_HOLDOUT_NOT_AGGREGATED","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"한국콜마 profile and price rows were checked as a same-canonical holdout candidate, but this MD keeps aggregate count to Silicon2/Cosmax/Amore to avoid over-weighting the same ODM family.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 11
next_round = R6
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json.
- 257720 profile: atlas/symbol_profiles/257/257720.json.
- 192820 profile: atlas/symbol_profiles/192/192820.json.
- 161890 profile: atlas/symbol_profiles/161/161890.json.
- 090430 profile: atlas/symbol_profiles/090/090430.json.
- 257720 OHLC: atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv and 2024.csv.
- 192820 OHLC: atlas/ohlcv_tradable_by_symbol_year/192/192820/2023.csv.
- 090430 OHLC: atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv.
- Evidence-source URLs require enrichment before production promotion.
- No live candidate scan, no production patch, no brokerage action.
