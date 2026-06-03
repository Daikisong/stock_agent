# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family: v12_sector_archetype_residual
scheduled_round: R9
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_VOLUME_MIX_OPERATING_LEVERAGE_VS_PEAK_REVERSAL_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining
research_date: 2026-05-31
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

This loop adds **3 new independent cases**, **1 counterexample**, and **1 residual profile error** for `R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

## 1. Current Calibrated Profile Assumption

The current calibrated proxy is treated as `e2r_2_1_stock_web_calibrated_proxy`, with `e2r_2_0_baseline_reference` as rollback reference. This MD does not change production scoring. It tests whether C29 mobility/auto-parts cases should require a stricter bridge from volume/mix narrative into margin, EPS/FCF, and non-price 4B timing.

Applied global axes are treated as already present and are not re-proposed: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

## 2. Round / Large Sector / Canonical Archetype Scope

R9 permits L3 mobility work. This run selects the mobility side of L3 rather than L9 construction because R10 is the clean dedicated construction/PF round. The selected canonical archetype is:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

### Canonical compression map

| canonical_archetype_id | fine/deep sub-archetype | evidence bridge being tested |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_VOLUME_MIX_MARGIN_CONVERSION | vehicle production / mix tailwind must become margin and EPS revision |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_PEAK_AFTER_VOLUME_REPRICING | price rerating after volume/mix success needs 4B overlay when revision slows |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | MOBILITY_CAPEX_OR_LOW_MARGIN_COUNTEREXAMPLE | headline mobility exposure without margin/EPS bridge should stay Yellow/Watch |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C29 as already covered but still eligible for new symbol / trigger family expansion. The high-repeat combinations in the index emphasize `UNKNOWN_SYMBOL`, `000270`, `005380`, `204320`, `018880`, and `161390`. This loop deliberately avoids those high-repeat symbols and uses:

| symbol | company_name | duplicate risk | reason allowed |
|---|---|---|---|
| 005850 | 에스엘 | low | not listed among top repeated C29 combinations; new auto-lighting operating leverage case |
| 010690 | 화신 | low | not listed among top repeated C29 combinations; new auto-body parts 4B reversal case |
| 011210 | 현대위아 | low | not listed among top repeated C29 combinations; new mobility-capex / lower-margin counterexample |

Hard duplicate key checked for this MD:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No matching hard duplicate was found through repository search for the selected `C29 + symbol` combinations during this run.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| price_data_repo | https://github.com/Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| OHLC columns | d,o,h,l,c,v,a,mc,s,m |

### Symbol profile validation

| symbol | company | profile_path | profile status | corporate-action caveat in tested window |
|---|---|---|---|---|
| 005850 | 에스엘 | atlas/symbol_profiles/005/005850.json | active_like, 2024 file present | profile has old corporate-action candidates but none in 2024 window tested |
| 010690 | 화신 | atlas/symbol_profiles/010/010690.json | active_like, 2023 file present | profile has old corporate-action candidates but none in 2023 window tested |
| 011210 | 현대위아 | atlas/symbol_profiles/011/011210.json | active_like, 2023 file present | no corporate-action candidates in profile |

## 5. Historical Eligibility Gate

| case_id | entry_date | entry row exists | forward 180 trading days | high/low/close/volume present | corporate action window | calibration_usable |
|---|---:|---|---|---|---|---|
| C29_SL_20240201_STAGE2 | 2024-02-01 | yes | yes | yes | clean_180D_window | true |
| C29_HWASHIN_20230412_STAGE2_4B | 2023-04-12 | yes | yes | yes | clean_180D_window | true |
| C29_WIA_20230412_COUNTEREXAMPLE | 2023-04-12 | yes | yes | yes | clean_180D_window | true |

Evidence-source URL verification is intentionally left as a deferred coding-agent task. Price rows are usable for historical calibration; evidence rows should be treated as **source-verification-pending** before any production promotion.

## 6. Canonical Archetype Compression Map

C29 should not simply mean “auto upcycle”. The tested compression is:

```text
C29 = mobility volume/mix + visible operating leverage + EPS/FCF conversion + 4B reversal guard
```

Mechanically, the archetype behaves like a gearbox. Volume is the engine rev; mix is the gear ratio; margin conversion is the clutch. When the clutch does not bite, headline production growth spins without moving EPS enough to justify Green.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | evidence bridge |
|---|---|---|---|---|---:|---:|---|
| C29_SL_20240201_STAGE2 | 005850 | 에스엘 | structural_success | Stage2-Actionable | 2024-02-01 | 33,750 | auto-lighting mix / customer volume → margin conversion |
| C29_HWASHIN_20230412_STAGE2_4B | 010690 | 화신 | 4B_overlay_success | Stage2-Actionable | 2023-04-12 | 14,600 | body/chassis parts volume and overseas mix → rerating, then sharp peak reversal |
| C29_WIA_20230412_COUNTEREXAMPLE | 011210 | 현대위아 | failed_rerating | Stage2-Actionable | 2023-04-12 | 65,200 | mobility/EV component narrative without enough margin/EPS bridge |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| calibration_usable_case_count | 3 |
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_or_4C_case_count | 2 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |

This is acceptable for a canonical-archetype-specific shadow rule, but not sufficient for a global rule.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | evidence_url_pending | source_proxy_only | non-price evidence quality |
|---|---|---|---|---|---|
| C29_SL_20240201_STAGE2 | 2024 auto parts earnings/margin revision window and stock-web volume reaction | public earnings / IR / consensus proxy to be URL-verified | true | false | medium, needs URL repair before promotion |
| C29_HWASHIN_20230412_STAGE2_4B | 2023 auto body/chassis parts volume and overseas mix rerating window | public earnings / sector report proxy to be URL-verified | true | false | medium, price path strongly supports 4B guard but source URL repair needed |
| C29_WIA_20230412_COUNTEREXAMPLE | 2023 mobility/EV parts narrative without durable margin conversion | public earnings / sector report proxy to be URL-verified | true | false | medium-low, useful as counterexample not as positive promotion |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry row excerpt used |
|---|---|---|---|
| 005850 | atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv | atlas/symbol_profiles/005/005850.json | `2024-02-01,...,c=33750` |
| 010690 | atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv | atlas/symbol_profiles/010/010690.json | `2023-04-12,...,c=14600` |
| 011210 | atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv | atlas/symbol_profiles/011/011210.json | `2023-04-12,...,c=65200` |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_id | trigger_type | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | current_profile_verdict |
|---|---|---|---|---|---|---|---|
| C29_SL_20240201_STAGE2 | C29_SL_S2_20240201 | Stage2-Actionable | volume/mix, relative strength, early margin conversion | later margin / revision confirmation | peak reversal after strong run | none | current_profile_correct |
| C29_HWASHIN_20230412_STAGE2_4B | C29_HWASHIN_S2_20230412 | Stage2-Actionable | overseas parts volume/mix, relative strength | revision and operating leverage confirmation | price and later revision/positioning slowdown | none | current_profile_4B_too_late |
| C29_WIA_20230412_COUNTEREXAMPLE | C29_WIA_S2_20230412 | Stage2-Actionable | mobility narrative, relative strength | weak / not durable | valuation/multiple cap without margin bridge | none | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger table

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C29_SL_S2_20240201 | 005850 | 2024-02-01 | 33750 | 10.96 | -5.48 | 41.19 | -12.74 | 41.19 | -12.74 | 2024-06-17 | 47650 | -35.57 | structural_success_then_4B_watch |
| C29_HWASHIN_S2_20230412 | 010690 | 2023-04-12 | 14600 | 18.22 | -6.64 | 55.48 | -6.64 | 55.48 | -31.92 | 2023-07-06 | 22700 | -56.21 | high_MFE_success_with_late_4B_risk |
| C29_WIA_S2_20230412 | 011210 | 2023-04-12 | 65200 | 2.76 | -14.88 | 8.13 | -14.88 | 8.13 | -20.71 | 2023-07-06 | 70500 | -26.67 | false_positive_or_low_quality_stage2 |

### Notes on calculation

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
```

The tested windows use stock-web `tradable_raw` rows only. No split-adjustment is applied. No corporate-action candidate appears inside these tested 180D windows based on profile caveats.

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current calibrated profile 판단 | C29 positive Stage2 can be triggered by volume/mix + RS + early margin evidence |
| 실제 MFE/MAE와 맞았는가 | SL and Hwashin support Stage2, WIA shows narrative-only mobility exposure is weak |
| Stage2 bonus 과했는가 | not globally; but C29 needs bridge quality split |
| Yellow threshold 75 | reasonable; WIA should remain Yellow/Watch without EPS/FCF conversion |
| Green 87 / revision 55 | should not be loosened; C29 Green needs margin/revision evidence |
| price-only blowoff guard | appropriate, especially for Hwashin after local peak |
| full 4B non-price requirement | appropriate but C29 needs earlier 4B watch when revision/positioning cools |
| hard 4C routing | not directly tested; no hard 4C here |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 timing | Green timing implication | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| C29_SL_20240201_STAGE2 | useful; entry before major June rerating | Green after full confirmation would catch less upside | 0.30~0.45 proxy | Green somewhat late but acceptable |
| C29_HWASHIN_20230412_STAGE2_4B | useful; entry before peak run | Green near May/June would be late but still profitable | 0.40~0.60 proxy | Green can work only with 4B overlay |
| C29_WIA_20230412_COUNTEREXAMPLE | weak; entry had little MFE and high MAE | Green should not trigger | not_applicable | insufficient Stage3 evidence |

## 15. 4B Local vs Full-window Timing Audit

| case_id | local_peak_date | local_peak_price | four_b_evidence_type | four_b_timing_verdict |
|---|---:|---:|---|---|
| C29_SL_20240201_STAGE2 | 2024-06-17 | 47,650 | valuation_blowoff, positioning_overheat, revision_slowdown proxy | good_local_4B_watch_needed |
| C29_HWASHIN_20230412_STAGE2_4B | 2023-07-06 | 22,700 | valuation_blowoff, positioning_overheat, margin/revision slowdown proxy | good_full_window_4B_timing_needed |
| C29_WIA_20230412_COUNTEREXAMPLE | 2023-07-06 | 70,500 | weak_margin_bridge, capex/low-margin overhang | not_full_4B; mostly failed Stage2 |

C29 behaves as a high-torque but low-forgiveness archetype. When operating leverage appears, the stock can sprint quickly. When revision momentum stalls, the same gearing works in reverse.

## 16. 4C Protection Audit

No hard 4C case is claimed. WIA is treated as a Stage2/Green false-positive counterexample rather than a hard 4C thesis break. Hwashin and SL are 4B watch cases: the problem was not thesis destruction, but peak/revision risk after the market had already paid for the volume/mix bridge.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_candidate = C29_volume_mix_requires_margin_revision_bridge
```

Candidate rule:

```text
For C29, Stage2 can be allowed on volume/mix + customer production + relative strength, but Stage3-Green requires at least two of:
1. explicit margin conversion,
2. EPS/OP revision or consensus upgrade,
3. FCF/cash conversion improvement,
4. non-price customer/order visibility.
If only volume/mix/RS exists, cap at Stage2 or Yellow and add 4B watch after fast MFE > 40%.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
confidence: low_to_medium
promotion_type: shadow_only_until_evidence_urls_verified
```

The evidence is directionally useful but should not be promoted until the evidence URL fields are repaired. The price path is clean; the evidence map is still proxy-based.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | late_4B_count | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | C29 Stage2/Green from broad volume/mix | 3 | 34.93 | -11.42 | 33.3% | 1 | acceptable Stage2, too loose for Green |
| P1_sector_specific_candidate_profile | L3 mobility | raise bridge quality for Green | 3 | 34.93 | -11.42 | 0.0% if WIA stays Yellow | 1 | improves score-return alignment |
| P2_canonical_archetype_candidate_profile | C29 | add margin/revision bridge and fast-MFE 4B watch | 3 | 34.93 | -11.42 | 0.0% if WIA blocked | 0~1 | best shadow profile |
| P3_counterexample_guard_profile | C29 guard | block narrative-only mobility exposure | 1 counterexample | 8.13 | -14.88 | 0.0% | n/a | useful as guard, not standalone rule |

## 20. Score-Return Alignment Matrix

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | alignment |
|---|---|---:|---|---|---:|---|---|
| C29_SL_20240201_STAGE2 | contract=2, backlog=2, margin=7, revision=6, RS=8, customer=6, valuation=4, risk=3 | 79 | Stage3-Yellow | margin=8, revision=7, RS=8, customer=6, valuation=4, risk=4 | 83 | Stage3-Yellow/near-Green | good but 4B watch needed |
| C29_HWASHIN_20230412_STAGE2_4B | contract=2, backlog=2, margin=7, revision=6, RS=9, customer=6, valuation=5, risk=4 | 81 | Stage3-Yellow | margin=8, revision=7, RS=9, customer=6, valuation=6, risk=6 | 84 | Stage3-Yellow + 4B watch | good Stage2, fast 4B watch |
| C29_WIA_20230412_COUNTEREXAMPLE | contract=1, backlog=1, margin=3, revision=3, RS=5, customer=4, valuation=3, risk=5 | 67 | Stage2-Watch | margin=2, revision=2, RS=5, customer=4, valuation=3, risk=6 | 61 | Watch / no Green | corrected false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_VOLUME_MIX_OPERATING_LEVERAGE_VS_PEAK_REVERSAL_GUARD | 2 | 1 | 2 | 0 | 3 | 0 | 3 | 3 | 1 | false | true | need evidence URL repair and more C29 counterexamples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_total_min, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage]
residual_error_types_found: [current_profile_false_positive, current_profile_4B_too_late]
new_axis_proposed: null
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
counterexample_search_incomplete: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- round/sector consistency for R9/L3/C29,
- stock-web profile existence,
- tradable OHLC rows around entry and forward windows,
- clean price-basis fields,
- trigger-level MFE/MAE and peak/drawdown estimates from stock-web rows.

Not validated:

- direct evidence URLs for each company event,
- exact consensus revision archive,
- production scoring implementation,
- investment suitability.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,green_margin_revision_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 Green should require margin/EPS bridge, not volume narrative only","blocks WIA false positive while keeping SL/Hwashin Stage2",C29_SL_S2_20240201|C29_HWASHIN_S2_20230412|C29_WIA_S2_20230412,3,3,1,low_to_medium,canonical_shadow_only,"evidence URL repair required before promotion"
shadow_weight,fast_mfe_4b_watch,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 runs can reverse sharply after MFE>40% if revisions cool","flags SL/Hwashin 4B watch before full thesis break",C29_SL_S2_20240201|C29_HWASHIN_S2_20230412,2,2,0,low_to_medium,canonical_shadow_only,"not a sell rule; overlay risk only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C29_SL_20240201_STAGE2","symbol":"005850","company_name":"에스엘","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MIX_MARGIN_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C29_SL_S2_20240201","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_high_mfe_with_4b_watch","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Evidence URL repair needed before promotion."}
{"row_type":"case","case_id":"C29_HWASHIN_20230412_STAGE2_4B","symbol":"010690","company_name":"화신","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_PEAK_AFTER_VOLUME_REPRICING","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"C29_HWASHIN_S2_20230412","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mfe_then_large_drawdown_after_peak","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Good for 4B watch calibration, not for global positive delta."}
{"row_type":"case","case_id":"C29_WIA_20230412_COUNTEREXAMPLE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_CAPEX_OR_LOW_MARGIN_COUNTEREXAMPLE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C29_WIA_S2_20230412","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"low_mfe_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Narrative mobility exposure did not convert into strong price path."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C29_SL_S2_20240201","case_id":"C29_SL_20240201_STAGE2","symbol":"005850","company_name":"에스엘","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MIX_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":33750,"evidence_available_at_that_date":"2024 auto-parts earnings/margin revision window","evidence_source":"public earnings/IR proxy; URL repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv","profile_path":"atlas/symbol_profiles/005/005850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.96,"MFE_90D_pct":41.19,"MFE_180D_pct":41.19,"MAE_30D_pct":-5.48,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"peak_date":"2024-06-17","peak_price":47650,"drawdown_after_peak_pct":-35.57,"green_lateness_ratio":"0.30_to_0.45_proxy","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_4B_watch_needed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"005850_2024-02-01_33750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_HWASHIN_S2_20230412","case_id":"C29_HWASHIN_20230412_STAGE2_4B","symbol":"010690","company_name":"화신","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_PEAK_AFTER_VOLUME_REPRICING","loop_objective":"coverage_gap_fill|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-12","entry_date":"2023-04-12","entry_price":14600,"evidence_available_at_that_date":"2023 auto body/chassis volume and overseas mix rerating window","evidence_source":"public earnings/sector report proxy; URL repair required","stage2_evidence_fields":["relative_strength","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv","profile_path":"atlas/symbol_profiles/010/010690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.22,"MFE_90D_pct":55.48,"MFE_180D_pct":55.48,"MAE_30D_pct":-6.64,"MAE_90D_pct":-6.64,"MAE_180D_pct":-31.92,"peak_date":"2023-07-06","peak_price":22700,"drawdown_after_peak_pct":-56.21,"green_lateness_ratio":"0.40_to_0.60_proxy","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_needed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"trigger_outcome_label":"high_MFE_success_with_late_4B_risk","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"010690_2023-04-12_14600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_WIA_S2_20230412","case_id":"C29_WIA_20230412_COUNTEREXAMPLE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_CAPEX_OR_LOW_MARGIN_COUNTEREXAMPLE","loop_objective":"counterexample_mining|residual_false_positive_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-12","entry_date":"2023-04-12","entry_price":65200,"evidence_available_at_that_date":"2023 mobility/EV component narrative without durable margin conversion","evidence_source":"public earnings/sector report proxy; URL repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.76,"MFE_90D_pct":8.13,"MFE_180D_pct":8.13,"MAE_30D_pct":-14.88,"MAE_90D_pct":-14.88,"MAE_180D_pct":-20.71,"peak_date":"2023-07-06","peak_price":70500,"drawdown_after_peak_pct":-26.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"failed_stage2_not_full_4B","four_b_evidence_type":["execution_risk"],"trigger_outcome_label":"failed_rerating_or_false_positive_stage2","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"011210_2023-04-12_65200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_SL_20240201_STAGE2","trigger_id":"C29_SL_S2_20240201","symbol":"005850","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow_with_4B_watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C29 positive remains valid but fast MFE requires overlay watch.","MFE_90D_pct":41.19,"MAE_90D_pct":-12.74,"score_return_alignment_label":"good"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"C29_HWASHIN_20230412_STAGE2_4B","trigger_id":"C29_HWASHIN_S2_20230412","symbol":"010690","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow_with_4B_watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Fast MFE followed by drawdown argues for earlier 4B watch rather than Green loosening.","MFE_90D_pct":55.48,"MAE_90D_pct":-6.64,"score_return_alignment_label":"good_but_4B_timing_sensitive"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"C29_WIA_20230412_COUNTEREXAMPLE","trigger_id":"C29_WIA_S2_20230412","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Watch_no_positive_stage","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Mobility narrative without margin bridge fails the return alignment test.","MFE_90D_pct":8.13,"MAE_90D_pct":-14.88,"score_return_alignment_label":"counterexample"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"evidence_url_pending_count":3,"source_proxy_only_count":0}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas.

This MD is not live candidate research. It is historical calibration research designed to extend the post-calibrated E2R profile with a C29 mobility/auto-parts operating-leverage residual test.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not apply global deltas from this single C29 MD.
- Evidence URLs are pending; verify source URLs before promotion.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- price-only rows cannot promote Stage2/Stage3.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R9/L3/C29 round-sector consistency.
4. Validate novelty against `canonical_archetype_id + symbol + trigger_type + entry_date`.
5. Repair evidence URLs for SL, Hwashin, and Hyundai Wia before promotion.
6. Add C29-specific guard: Green needs margin/EPS bridge; volume/mix-only stays Stage2/Yellow.
7. Add C29 fast-MFE 4B watch: MFE above roughly 40% plus revision/positioning risk should create overlay watch.

## 27. Next Round State

```text
current_round: R9
current_loop: 71
next_round: R10
next_loop: 71
next_large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status: valid
round_sector_consistency: pass
```

## 28. Source Notes

Price rows were read from `Songdaiki/stock-web` symbol-year shards:

- `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv`

Symbol profiles were read from:

- `atlas/symbol_profiles/005/005850.json`
- `atlas/symbol_profiles/010/010690.json`
- `atlas/symbol_profiles/011/011210.json`

The No-Repeat Index was used only as a duplicate-avoidance ledger.
