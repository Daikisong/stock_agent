# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 13
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET
output_file: e2r_stock_web_v12_residual_round_R5_loop_13_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **4** new independent cases, **2** counterexamples, and **3** residual errors for **R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION**.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

Existing applied global axes treated as already active:

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

This file does **not** repeat those global claims. It stress-tests whether C20 needs a narrower rule: global beauty/distribution winners require actual channel reorder and margin bridge evidence, while legacy China/duty-free reopening narratives must be capped or guarded.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R5`
- Loop: `13`
- Required sector: `L5_CONSUMER_BRAND_DISTRIBUTION`
- Canonical archetype: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- Fine archetype: `K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET`
- Scope: historical calibration only.
- Non-scope: no live scan, no stock recommendation, no production patch.

## 3. Previous Coverage / Duplicate Avoidance Check

Repository search for `e2r_stock_web_v12_residual_round_R5_loop_13` and the selected C20 identifier returned no matching existing R5/Loop13 result file in the accessible research artifacts. This loop therefore proceeds as a scheduled R5 fill.

Duplicate-avoidance stance:

```text
same_canonical_archetype_research: allowed
same_symbol_same_trigger_date_research: blocked
new_symbol_count: 4
same_archetype_new_symbol_count: 4
new_trigger_family_count: 6
minimum_new_independent_case_ratio: 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` diagnostics report:

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
```

Default price basis:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Symbol profile validation:

| symbol | company | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D status |
|---|---|---|---:|---:|---|---|
| 257720 | 실리콘투 | atlas/symbol_profiles/257/257720.json | 2021-09-29 | 2026-02-20 | 2022-07-14; 2022-08-02 | clean for 2024 trigger windows |
| 018290 | 브이티 | atlas/symbol_profiles/018/018290.json | 1996-07-03 | 2026-02-20 | old events through 2019-11-08 | clean for 2024 trigger windows |
| 051900 | LG생활건강 | atlas/symbol_profiles/051/051900.json | 2001-04-25 | 2026-02-20 | none | clean for 2022 trigger windows |
| 090430 | 아모레퍼시픽 | atlas/symbol_profiles/090/090430.json | 2006-06-29 | 2026-02-20 | 2015-05-08 | clean for 2023 trigger windows |

## 5. Historical Eligibility Gate

All representative triggers pass:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

1Y and 2Y fields are retained as schema fields. 2Y is not used for weight proposal in this loop because the research purpose is 30D/90D/180D trigger calibration.

## 6. Canonical Archetype Compression Map

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  ├─ K_BEAUTY_GLOBAL_DISTRIBUTOR_REORDER
  │   └─ 실리콘투: channel breadth + operating leverage + reorder visibility
  ├─ K_BEAUTY_BRAND_NON_CHINA_REPEAT_SELLTHROUGH
  │   └─ 브이티: product traction + repeat channel conversion + margin visibility
  └─ LEGACY_CHINA_DUTYFREE_REOPENING_BETA
      ├─ LG생활건강: premium beauty recovery narrative without confirmed China/duty-free repair
      └─ 아모레퍼시픽: reopening headline bounce without durable channel reorder
```

The compression principle is simple: in C20, “global” does not mean any overseas exposure. It must behave like a conveyor belt: reorder → shipment/channel breadth → margin bridge → revision. If the belt is missing and only the shop sign says “China reopening,” the model should not give the same Stage2/3 credit.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5L13_C20_POS_SILICON2_202405_Q1_EXPORT_CHANNEL | 257720 | 실리콘투 | structural_success | positive | T_SILICON2_20240517_STAGE2_ACTIONABLE | current_profile_correct | strong_positive_alignment |
| R5L13_C20_POS_VT_202405_Q1_RIDLESHOT_JAPAN | 018290 | 브이티 | structural_success | positive | T_VT_20240517_STAGE2_ACTIONABLE | current_profile_4B_too_late | positive_but_green_late |
| R5L13_C20_NEG_LGHNH_202201_CHINA_DUTYFREE_RESET | 051900 | LG생활건강 | failed_rerating | counterexample | T_LGHNH_20220128_FALSE_STAGE2 | current_profile_false_positive | negative_alignment |
| R5L13_C20_NEG_AMORE_202302_REOPENING_HEADLINE | 090430 | 아모레퍼시픽 | failed_rerating | counterexample | T_AMORE_20230201_FALSE_STAGE2 | current_profile_false_positive | weak_or_negative_alignment |

## 8. Positive vs Counterexample Balance

| balance_item | count | notes |
|---|---:|---|
| positive_structural_success | 2 | 실리콘투, 브이티 |
| counterexample_or_failed_rerating | 2 | LG생활건강, 아모레퍼시픽 |
| 4B_or_4C_case | 2 | 실리콘투 4B overlay, LG생활건강 4C |
| calibration_usable_case_count | 4 | all representative cases clean |
| calibration_usable_trigger_count | 7 | includes representative, Stage3 comparison, 4B/4C overlays |

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 실리콘투 | Q1 result shock, channel breadth, export distributor model | margin bridge, financial visibility | valuation/positioning overheat after parabolic move | not triggered in representative window |
| 브이티 | Q1 result shock, Japan/non-China channel traction, product repeat | repeat order/conversion, margin bridge | later valuation/positioning monitor | not triggered in representative window |
| LG생활건강 | weak public recovery narrative only | absent at trigger | margin/channel slowdown | thesis evidence broken after China/duty-free shock |
| 아모레퍼시픽 | China reopening headline | absent at trigger | margin/channel slowdown | thesis evidence broken by lack of durable channel repair |

## 10. Price Data Source Map

| symbol | entry shard | profile path | price basis | adjustment |
|---|---|---|---|---|
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json | tradable_raw | raw_unadjusted_marcap |
| 018290 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv | atlas/symbol_profiles/018/018290.json | tradable_raw | raw_unadjusted_marcap |
| 051900 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv | atlas/symbol_profiles/051/051900.json | tradable_raw | raw_unadjusted_marcap |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv | atlas/symbol_profiles/090/090430.json | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict | trigger_outcome_label | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_SILICON2_20240517_STAGE2_ACTIONABLE | 257720 | 실리콘투 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 29550 | 83.42 | -6.77 | 83.42 | -21.15 | current_profile_correct | structural_success_high_MFE_high_late_drawdown | representative |
| T_SILICON2_20240621_4B_OVERLAY | 257720 | 실리콘투 | Stage4B-Overlay | 2024-06-21 | 2024-06-21 | 52800 | 2.65 | -30.97 | 2.65 | -55.87 | current_profile_correct | 4B_overlay_success | 4B_overlay_only |
| T_VT_20240517_STAGE2_ACTIONABLE | 018290 | 브이티 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 26600 | 50.38 | -4.14 | 65.41 | -4.14 | current_profile_correct | structural_success_high_MFE_low_MAE | representative |
| T_VT_20240920_STAGE3_GREEN_LATE | 018290 | 브이티 | Stage3-Green | 2024-09-20 | 2024-09-20 | 38000 | 15.79 | -28.42 | 15.79 | -19.61 | current_profile_too_late | green_late_but_not_invalid | label_comparison_only |
| T_LGHNH_20220128_FALSE_STAGE2 | 051900 | LG생활건강 | Stage2-Actionable | 2022-01-28 | 2022-01-28 | 975000 | 7.18 | -38.87 | 7.18 | -38.87 | current_profile_false_positive | false_positive_stage2 | representative |
| T_LGHNH_20220512_4C_THESIS_BREAK | 051900 | LG생활건강 | Stage4C | 2022-05-12 | 2022-05-12 | 691000 | 14.62 | -13.75 | 14.62 | -13.75 | current_profile_4C_too_late | 4C_success | 4C_overlay_only |
| T_AMORE_20230201_FALSE_STAGE2 | 090430 | 아모레퍼시픽 | Stage2-Actionable | 2023-02-01 | 2023-02-01 | 141400 | 10.18 | -28.64 | 10.18 | -33.59 | current_profile_false_positive | false_positive_stage2 | representative |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_SILICON2_20240517_STAGE2_ACTIONABLE | 257720 | 2024-05-17 | 29550 | 83.42 | -6.77 | 83.42 | -6.77 | 83.42 | -21.15 | 2024-06-19 | 54200 | -57.01 |
| T_VT_20240517_STAGE2_ACTIONABLE | 018290 | 2024-05-17 | 26600 | 50.38 | -4.14 | 50.38 | -4.14 | 65.41 | -4.14 | 2024-12-16 | 44000 | -30.57 |
| T_LGHNH_20220128_FALSE_STAGE2 | 051900 | 2022-01-28 | 975000 | 7.18 | -15.38 | 7.18 | -38.87 | 7.18 | -38.87 | 2022-02-18 | 1045000 | -42.97 |
| T_AMORE_20230201_FALSE_STAGE2 | 090430 | 2023-02-01 | 141400 | 10.18 | -13.58 | 10.18 | -28.64 | 10.18 | -33.59 | 2023-02-10 | 155800 | -39.73 |

### Overlay / label-comparison triggers

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | four_b_local_peak_proximity | four_b_full_window_peak_proximity | green_lateness_ratio | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_SILICON2_20240621_4B_OVERLAY | 257720 | Stage4B-Overlay | 2024-06-21 | 52800 | 2.65 | -30.97 | 0.94 | 0.94 | not_applicable | 4B_overlay_only |
| T_VT_20240920_STAGE3_GREEN_LATE | 018290 | Stage3-Green | 2024-09-20 | 38000 | 15.79 | -28.42 | None | None | 0.66 | label_comparison_only |
| T_LGHNH_20220512_4C_THESIS_BREAK | 051900 | Stage4C | 2022-05-12 | 691000 | 14.62 | -13.75 | None | None | not_applicable | 4C_overlay_only |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | verdict |
|---|---|---|---|
| 실리콘투 | Promote to Stage2/Yellow and later Green | high 90D/180D MFE, but later 4B needed | current_profile_correct |
| 브이티 | Promote, but strict Green may wait for repeat confirmation | strong MFE with low MAE; Green comparison is late | current_profile_too_late |
| LG생활건강 | Could be over-promoted if reopening/premium brand narrative is credited | low MFE, severe MAE, 4C after thesis break | current_profile_false_positive |
| 아모레퍼시픽 | Could be over-promoted if China reopening beta is credited | tactical MFE but large 180D MAE | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus: correct for SILICON2/VT, too permissive for LGHNH/AMORE unless C20 guard exists
yellow_threshold_75: acceptable only when channel quality is supported
green_threshold_87_revision_55: good as global rule, but C20 Green should require repeat-order/channel evidence
price_only_blowoff_guard: kept
full_4B_non_price_requirement: strengthened
hard_4C_routing: kept; LGHNH/AMORE support thesis-break routing
```

## 14. Stage2 / Yellow / Green Comparison

The key residual error is not “Stage2 is better than Green.” The issue is **which Stage2 deserves to exist**.

| symbol | Stage2 entry | Stage3/Green comparison | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 257720 | 29,550 | not used as separate Green row | n/a | Stage2 was already evidence-rich enough |
| 018290 | 26,600 | 38,000 | 0.66 | Green captured quality but entered after most upside was consumed |
| 051900 | 975,000 | no valid Green | n/a | Stage2 should have been blocked |
| 090430 | 141,400 | no valid Green | n/a | Stage2 should have been capped as narrative-only |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| T_SILICON2_20240621_4B_OVERLAY | 0.94 | 0.94 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| T_LGHNH_20220128_FALSE_STAGE2 | 0.12 | 0.12 | margin/channel slowdown | not a price-only 4B; it was a weak Stage2 false positive |
| T_VT_20240920_STAGE3_GREEN_LATE | n/a | n/a | n/a | lateness audit, not 4B |

C20-specific 4B should not be a naked local-peak detector. It should fire when the success thesis itself is intact but valuation/positioning has outrun channel evidence.

## 16. 4C Protection Audit

| case | 4C trigger | prior peak | 4C entry | post-4C MAE proxy | protection label |
|---|---|---:|---:|---:|---|
| LG생활건강 | 2022-05-12 | 1,045,000 | 691,000 | -13.75% | hard_4c_success |
| 아모레퍼시픽 | implicit thesis-break watch after reopening failure | 155,800 | n/a | n/a | thesis_break_watch_only |

LG생활건강 shows why hard 4C should route on thesis evidence, not simply on price. By the time the break is explicit, the model should stop treating rebound attempts as Stage2.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The evidence is concentrated in one canonical archetype inside L5. It should not yet become an L5-wide consumer rule because apparel, food, retail inventory, and brand wholesale cycles can have different evidence routes.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

Proposed C20 shadow rule:

```text
C20 promotion requires at least one of:
  1. distributor/channel breadth evidence,
  2. repeat sell-through/reorder evidence,
  3. margin bridge already visible in filed/reported numbers.

C20 promotion is capped when:
  - evidence is only China/duty-free reopening beta,
  - evidence is only legacy brand valuation rebound,
  - evidence lacks channel reorder and margin bridge.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 37.79 | -19.61 | 41.55 | -24.44 | 0.5 | 1 | mixed: positives are caught but China/duty-free headline rebounds remain false-positive prone |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 37.79 | -19.61 | 41.55 | -24.44 | 0.75 | 1 | weaker than P0 due to headline beta promotion |
| P1_sector_specific_candidate_profile | sector_specific_shadow | 4 | 66.9 | -5.46 | 74.41 | -12.64 | 0.0 | 1 | improves C20 selection by excluding China/duty-free narrative-only rebounds |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific_shadow | 4 | 66.9 | -5.46 | 74.42 | -12.65 | 0.0 | 1 | best profile for this loop; explains both success and failure paths |
| P3_counterexample_guard_profile | canonical_archetype_specific_guard | 4 | 66.9 | -5.46 | 74.42 | -12.65 | 0.0 | 1 | strong guard; may be too restrictive if future C20 has early wholesale evidence before filings |

## 20. Score-Return Alignment Matrix

| profile | positive capture | false-positive block | residual risk |
|---|---|---|---|
| P0 current | catches SILICON2/VT | may over-credit LGHNH/AMORE if narrative evidence is scored too high | C20 channel quality under-specified |
| P0b baseline | catches positives | weaker false-positive control | too much headline beta |
| P1 sector shadow | catches positives | blocks legacy channel false positives | too broad for all L5 |
| P2 canonical shadow | catches positives | blocks LGHNH/AMORE | best fit |
| P3 guard | strongest false-positive block | could miss very early channel turns | keep as guard, not default promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET | 2 | 2 | 1 | 1 | 4 | 0 | 7 | 4 | 3 | False | True | C20 now has distributor-positive, brand-positive, legacy-China false-positive, and 4C thesis-break coverage; food/global distribution still under-covered. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C20_legacy_channel_false_positive
  - C20_green_lateness_after_channel_proof
  - C20_4B_overheat_requires_non_price_evidence
new_axis_proposed:
  - C20_channel_reorder_quality_gate
  - C20_legacy_china_dutyfree_reopening_penalty
  - C20_non_price_4B_overheat_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- R5 scheduled round consistency
- L5 sector consistency
- C20 canonical archetype mapping
- 4 new symbols
- clean 180D stock-web windows
- representative trigger dedupe
- Stage2 vs Stage3/Green comparison
- 4B local vs full-window split
- 4C thesis-break protection audit
```

Not validated:

```text
- live candidate discovery
- broker/trading behavior
- production scoring implementation
- current 2026 recommendation
- non-C20 consumer sectors
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_quality_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Require reorder/channel breadth before Stage2/3 promotion","Blocks LGHNH/AMORE false positives while retaining SILICON2/VT","T_SILICON2_20240517_STAGE2_ACTIONABLE|T_VT_20240517_STAGE2_ACTIONABLE|T_LGHNH_20220128_FALSE_STAGE2|T_AMORE_20230201_FALSE_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_legacy_china_dutyfree_reopening_penalty,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-3,-3,"China/duty-free reopening headline without margin bridge is a false-positive cluster","Reduces current_profile_false_positive_count from 2 to 0 in this loop","T_LGHNH_20220128_FALSE_STAGE2|T_AMORE_20230201_FALSE_STAGE2",2,2,2,medium,canonical_shadow_only,"guard only; do not apply globally"
shadow_weight,C20_non_price_4B_overheat_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"When channel success produces parabolic valuation/positioning, 4B needs valuation/positioning evidence not price-only","Captures Silicon2 post-peak drawdown without treating all local peaks as full 4B","T_SILICON2_20240621_4B_OVERLAY",1,1,0,low,canonical_shadow_only,"4B overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L13_C20_POS_SILICON2_202405_Q1_EXPORT_CHANNEL","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_SILICON2_20240517_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"K-beauty multi-brand distribution/fulfillment case. The important distinction is not merely 'K-beauty theme' but channel reorder breadth and visible operating leverage."}
{"row_type":"case","case_id":"R5L13_C20_POS_VT_202405_Q1_RIDLESHOT_JAPAN","symbol":"018290","company_name":"브이티","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_VT_20240517_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_green_late","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"K-beauty brand case where non-China channel traction and repeat sell-through converted into margin and revision visibility."}
{"row_type":"case","case_id":"R5L13_C20_NEG_LGHNH_202201_CHINA_DUTYFREE_RESET","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_LGHNH_20220128_FALSE_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Premium beauty recovery narrative failed because China/duty-free demand and channel quality were already deteriorating."}
{"row_type":"case","case_id":"R5L13_C20_NEG_AMORE_202302_REOPENING_HEADLINE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_AMORE_20230201_FALSE_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_or_negative_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Reopening headline could produce a tactical bounce, but it lacked durable channel reorder and margin bridge."}
{"trigger_id":"T_SILICON2_20240517_STAGE2_ACTIONABLE","case_id":"R5L13_C20_POS_SILICON2_202405_Q1_EXPORT_CHANNEL","symbol":"257720","company_name":"실리콘투","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":29550,"evidence_available_at_that_date":"2024Q1 result shock + export/channel reorder narrative already public; next-trading-day close used.","evidence_source":"Company filings/news summary; stock-web shard confirms tradable close.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":83.42,"MFE_90D_pct":83.42,"MFE_180D_pct":83.42,"MFE_1Y_pct":83.42,"MFE_2Y_pct":null,"MAE_30D_pct":-6.77,"MAE_90D_pct":-6.77,"MAE_180D_pct":-21.15,"MAE_1Y_pct":-21.15,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_high_late_drawdown","current_profile_verdict":"current_profile_correct","same_entry_group_id":"257720_20240517_29550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json"}
{"trigger_id":"T_SILICON2_20240621_4B_OVERLAY","case_id":"R5L13_C20_POS_SILICON2_202405_Q1_EXPORT_CHANNEL","symbol":"257720","company_name":"실리콘투","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-21","entry_date":"2024-06-21","entry_price":52800,"evidence_available_at_that_date":"Rapid valuation/positioning blowoff after Q1 channel evidence; not a price-only 4B because the thesis had already been confirmed, but overheat became visible.","evidence_source":"Stock-web local/full-window peak audit plus contemporaneous valuation-risk narrative.","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":2.65,"MFE_90D_pct":2.65,"MFE_180D_pct":2.65,"MFE_1Y_pct":2.65,"MFE_2Y_pct":null,"MAE_30D_pct":-23.67,"MAE_90D_pct":-30.97,"MAE_180D_pct":-55.87,"MAE_1Y_pct":-55.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":53800,"drawdown_after_peak_pct":-56.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","same_entry_group_id":"257720_20240621_52800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case but distinct 4B overlay path","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json"}
{"trigger_id":"T_VT_20240517_STAGE2_ACTIONABLE","case_id":"R5L13_C20_POS_VT_202405_Q1_RIDLESHOT_JAPAN","symbol":"018290","company_name":"브이티","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":26600,"evidence_available_at_that_date":"Q1 beat and non-China/Japan channel traction were available; next-trading-day close used.","evidence_source":"Company filings/news summary; stock-web shard confirms tradable close.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":50.38,"MFE_90D_pct":50.38,"MFE_180D_pct":65.41,"MFE_1Y_pct":65.41,"MFE_2Y_pct":null,"MAE_30D_pct":-4.14,"MAE_90D_pct":-4.14,"MAE_180D_pct":-4.14,"MAE_1Y_pct":-4.14,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-16","peak_price":44000,"drawdown_after_peak_pct":-30.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","same_entry_group_id":"018290_20240517_26600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json"}
{"trigger_id":"T_VT_20240920_STAGE3_GREEN_LATE","case_id":"R5L13_C20_POS_VT_202405_Q1_RIDLESHOT_JAPAN","symbol":"018290","company_name":"브이티","trigger_type":"Stage3-Green","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":38000,"evidence_available_at_that_date":"By this point repeat evidence was stronger, but the entry consumed most of the easy upside from the May Stage2 base.","evidence_source":"Stock-web lateness audit.","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":5.26,"MFE_90D_pct":15.79,"MFE_180D_pct":15.79,"MFE_1Y_pct":15.79,"MFE_2Y_pct":null,"MAE_30D_pct":-20.13,"MAE_90D_pct":-28.42,"MAE_180D_pct":-19.61,"MAE_1Y_pct":-19.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-16","peak_price":44000,"drawdown_after_peak_pct":-30.57,"green_lateness_ratio":0.66,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_late_but_not_invalid","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"018290_20240920_38000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case but distinct Stage3 lateness audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json"}
{"trigger_id":"T_LGHNH_20220128_FALSE_STAGE2","case_id":"R5L13_C20_NEG_LGHNH_202201_CHINA_DUTYFREE_RESET","symbol":"051900","company_name":"LG생활건강","trigger_type":"Stage2-Actionable","trigger_date":"2022-01-28","entry_date":"2022-01-28","entry_price":975000,"evidence_available_at_that_date":"Post-drawdown premium beauty recovery narrative existed, but China/duty-free channel quality and earnings visibility were not confirmed.","evidence_source":"Historical filing/news narrative; stock-web shard confirms price path.","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":7.18,"MFE_90D_pct":7.18,"MFE_180D_pct":7.18,"MFE_1Y_pct":7.18,"MFE_2Y_pct":null,"MAE_30D_pct":-15.38,"MAE_90D_pct":-38.87,"MAE_180D_pct":-38.87,"MAE_1Y_pct":-38.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-02-18","peak_price":1045000,"drawdown_after_peak_pct":-42.97,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.12,"four_b_full_window_peak_proximity":0.12,"four_b_timing_verdict":"price_only_local_4B_too_early_if_no_channel_evidence","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_stage2","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"051900_20220128_975000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv","profile_path":"atlas/symbol_profiles/051/051900.json"}
{"trigger_id":"T_LGHNH_20220512_4C_THESIS_BREAK","case_id":"R5L13_C20_NEG_LGHNH_202201_CHINA_DUTYFREE_RESET","symbol":"051900","company_name":"LG생활건강","trigger_type":"Stage4C","trigger_date":"2022-05-12","entry_date":"2022-05-12","entry_price":691000,"evidence_available_at_that_date":"China lockdown/duty-free cosmetics shock and earnings disappointment made thesis break explicit.","evidence_source":"Historical filing/news narrative; stock-web price reaction confirms break.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken","forced_liquidation_or_crash"],"MFE_30D_pct":7.09,"MFE_90D_pct":14.62,"MFE_180D_pct":14.62,"MFE_1Y_pct":14.62,"MFE_2Y_pct":null,"MAE_30D_pct":-13.75,"MAE_90D_pct":-13.75,"MAE_180D_pct":-13.75,"MAE_1Y_pct":-13.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-01","peak_price":792000,"drawdown_after_peak_pct":-20.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","same_entry_group_id":"051900_20220512_691000","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same case but distinct 4C protection audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv","profile_path":"atlas/symbol_profiles/051/051900.json"}
{"trigger_id":"T_AMORE_20230201_FALSE_STAGE2","case_id":"R5L13_C20_NEG_AMORE_202302_REOPENING_HEADLINE","symbol":"090430","company_name":"아모레퍼시픽","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-01","entry_date":"2023-02-01","entry_price":141400,"evidence_available_at_that_date":"China reopening beauty rebound narrative existed, but durable reorder and margin bridge were not yet visible.","evidence_source":"Historical filing/news narrative; stock-web shard confirms price path.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":10.18,"MFE_90D_pct":10.18,"MFE_180D_pct":10.18,"MFE_1Y_pct":10.18,"MFE_2Y_pct":null,"MAE_30D_pct":-13.58,"MAE_90D_pct":-28.64,"MAE_180D_pct":-33.59,"MAE_1Y_pct":-33.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-10","peak_price":155800,"drawdown_after_peak_pct":-39.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_stage2","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"090430_20230201_141400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_JAPAN_CHANNEL_REORDER_VS_CHINA_DUTYFREE_RESET","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv","profile_path":"atlas/symbol_profiles/090/090430.json"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_vs_C20_shadow","case_id":"R5L13_C20_POS_SILICON2_202405_Q1_EXPORT_CHANNEL","trigger_id":"T_SILICON2_20240517_STAGE2_ACTIONABLE","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":16,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":16,"relative_strength_score":13,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 channel breadth and reorder evidence add customer_quality and margin_bridge points.","MFE_90D_pct":83.42,"MAE_90D_pct":-6.77,"score_return_alignment_label":"score_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_vs_C20_shadow","case_id":"R5L13_C20_POS_VT_202405_Q1_RIDLESHOT_JAPAN","trigger_id":"T_VT_20240517_STAGE2_ACTIONABLE","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":16,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":16,"relative_strength_score":13,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 channel breadth and reorder evidence add customer_quality and margin_bridge points.","MFE_90D_pct":50.38,"MAE_90D_pct":-4.14,"score_return_alignment_label":"score_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_vs_C20_shadow","case_id":"R5L13_C20_NEG_LGHNH_202201_CHINA_DUTYFREE_RESET","trigger_id":"T_LGHNH_20220128_FALSE_STAGE2","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-5,"revision_score":0,"relative_strength_score":2,"customer_quality_score":-6,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch_or_Red","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 guard removes reopening/duty-free headline beta when reorder and margin bridge are not proven.","MFE_90D_pct":7.18,"MAE_90D_pct":-38.87,"score_return_alignment_label":"guard_blocks_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_vs_C20_shadow","case_id":"R5L13_C20_NEG_AMORE_202302_REOPENING_HEADLINE","trigger_id":"T_AMORE_20230201_FALSE_STAGE2","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-5,"revision_score":0,"relative_strength_score":2,"customer_quality_score":-6,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch_or_Red","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C20 guard removes reopening/duty-free headline beta when reorder and margin bridge are not proven.","MFE_90D_pct":10.18,"MAE_90D_pct":-28.64,"score_return_alignment_label":"guard_blocks_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"13","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C20_legacy_channel_false_positive","C20_green_lateness_after_channel_proof","C20_4B_overheat_requires_non_price_evidence"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 13
next_round = R6
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web source files inspected during this loop:

```text
diagnostics/chatgpt_bundle.txt
atlas/symbol_profiles/257/257720.json
atlas/symbol_profiles/018/018290.json
atlas/symbol_profiles/051/051900.json
atlas/symbol_profiles/090/090430.json
atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv
atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv
atlas/ohlcv_tradable_by_symbol_year/018/018290/2025.csv
atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv
atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv
```

The OHLC numbers are raw/unadjusted FinanceData/marcap-derived rows exposed through the stock-web atlas. No production code was opened or patched.
