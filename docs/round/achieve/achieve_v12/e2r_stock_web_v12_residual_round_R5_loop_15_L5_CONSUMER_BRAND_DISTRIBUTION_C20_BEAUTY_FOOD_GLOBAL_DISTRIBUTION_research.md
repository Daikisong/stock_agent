# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_STEADY_FOOTPRINT
output_file: e2r_stock_web_v12_residual_round_R5_loop_15_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **3** new independent cases, **1** counterexample, and **2** residual errors for **R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION**.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

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

This file does **not** repeat the global calibration claim. It tests a narrower C20 residual: food/global distribution winners need **incremental country-level sell-through, channel reorder, export/local-plant capacity, and margin bridge**. A globally distributed brand without new reorder/revision torque is a lighthouse, not a motor; it can be visible from far away while the earnings engine stays idle.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R5`
- Loop: `15`
- Required sector: `L5_CONSUMER_BRAND_DISTRIBUTION`
- Canonical archetype: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- Fine archetype: `K_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_STEADY_FOOTPRINT`
- Scope: historical calibration only.
- Non-scope: no live scan, no current candidate discovery, no stock recommendation, no production patch.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 R5 research already covered C20 through `003230`, `192820`, `090430`, `257720`, `018290`, `051900`, plus C18/C19 apparel and retail loops. This loop keeps the same canonical C20 but rotates into **new food/global distribution symbols**: `004370`, `280360`, and `271560`.

```text
scheduled_round = R5
scheduled_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

Duplicate avoidance conclusion: this is **not** a C20 beauty-channel rematerialization loop. It adds K-food direct export/local plant evidence and a steady-global-footprint counterexample.

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest confirms the calibration atlas properties:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
raw_row_count = 15214118
tradable_row_count = 14354401
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The manifest uses raw/unadjusted FinanceData/marcap OHLC, excludes zero-volume and invalid rows from tradable shards, and blocks corporate-action-contaminated windows by default.

Symbol profile validation:

| symbol | company | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D status |
| --- | --- | --- | --- | --- | --- | --- |
| 004370 | 농심 | atlas/symbol_profiles/004/004370.json | 1995-05-02 | 2026-02-20 | 1997-05-08; 1997-07-21; 2000-07-28; 2003-07-18 | clean for 2023 entry |
| 280360 | 롯데웰푸드 | atlas/symbol_profiles/280/280360.json | 2017-10-30 | 2026-02-20 | 2019-01-04; 2022-07-20 | clean for 2024 entry |
| 271560 | 오리온 | atlas/symbol_profiles/271/271560.json | 2017-07-07 | 2026-02-20 | none | clean |

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

Corporate-action note: 004370 and 280360 have old stock-web corporate-action candidate dates, but none overlap the selected 180D windows. 271560 has no corporate-action candidates in the profile.

## 6. Canonical Archetype Compression Map

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  ├─ K_FOOD_RAMEN_US_EXPORT_MARGIN_BRIDGE
  │   └─ 농심: direct overseas ramen mix + margin bridge; positive but not explosive
  ├─ K_FOOD_GLOBAL_CONFECTIONERY_LOCAL_PLANTS_MARGIN_REPRICE
  │   └─ 롯데웰푸드: local plant/global confectionery repricing; high MFE then hard 4B/MAE
  └─ K_FOOD_GLOBAL_STEADY_MARKETS_WITHOUT_INCREMENTAL_REORDER
      └─ 오리온: global footprint without incremental reorder/revision; false positive
```

Compression rule: C20 should not score “global distribution” as one flat word. It has three gears: **country-level sell-through**, **channel reorder/capacity**, and **margin/revision bridge**. When all three mesh, the price path can rerate. When only the brand footprint is visible, the case behaves like a decorated storefront with no cash register ringing faster.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5L15_C20_POS_NONGSHIM_202305_Q1_US_RAMEN_MARGIN | 004370 | 농심 | structural_success | positive | T_NONGSHIM_20230516_STAGE2_ACTIONABLE | current_profile_correct | direct_export_capacity_margin_bridge_aligned_with_positive_MFE |
| R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY | 280360 | 롯데웰푸드 | high_mae_success | positive | T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE | current_profile_too_late | high_MFE_but_later_drawdown_requires_4B_overlay |
| R5L15_C20_NEG_ORION_202305_GLOBAL_STEADY_GROWTH_HEADLINE | 271560 | 오리온 | failed_rerating | counterexample | T_ORION_20230516_FALSE_STAGE2 | current_profile_false_positive | global_brand_headline_without_incremental_revision_failed |

## 8. Positive vs Counterexample Balance

| balance_item | count | notes |
| --- | --- | --- |
| positive_structural_success | 2 | 농심, 롯데웰푸드 |
| counterexample_or_failed_rerating | 1 | 오리온 |
| 4B_or_4C_case | 1 | 롯데웰푸드 4B valuation/positioning overlay |
| calibration_usable_case_count | 3 | all representative cases clean |
| calibration_usable_trigger_count | 5 | three representatives + one Stage3 comparison + one 4B overlay |

Because this loop has only one counterexample, the proposal is kept **canonical-archetype shadow-only**, not global.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| 농심 | Q1 result, overseas ramen channel traction, margin bridge, relative strength | margin bridge and financial visibility | none in representative entry | not triggered |
| 롯데웰푸드 | Q1 result, global confectionery/local plant narrative, early revision and relative strength | margin bridge, financial visibility, repeat conversion | valuation/positioning overheat at 2024-06-18 peak | later thesis-break watch only |
| 오리온 | global footprint headline only | absent; no sufficient incremental reorder/revision bridge | margin slowdown watch | thesis evidence broken after large drawdown |

## 10. Price Data Source Map

| symbol | entry shard | profile path | price basis | adjustment |
| --- | --- | --- | --- | --- |
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv; atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv | atlas/symbol_profiles/004/004370.json | tradable_raw | raw_unadjusted_marcap |
| 280360 | atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv; atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv | atlas/symbol_profiles/280/280360.json | tradable_raw | raw_unadjusted_marcap |
| 271560 | atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv; atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | atlas/symbol_profiles/271/271560.json | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict | trigger_outcome_label | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_NONGSHIM_20230516_STAGE2_ACTIONABLE | 004370 | 농심 | Stage2-Actionable | 2023-05-15 | 2023-05-16 | 426000 | 15.02 | -9.39 | 17.37 | -14.08 | current_profile_correct | structural_success | representative |
| T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE | 280360 | 롯데웰푸드 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 142000 | 46.83 | -10.77 | 46.83 | -29.65 | current_profile_too_late | high_mae_success | representative |
| T_LOTTEWELLFOOD_20240610_STAGE3_GREEN_PROXY | 280360 | 롯데웰푸드 | Stage3-Green | 2024-06-10 | 2024-06-10 | 177900 | 17.20 | -28.78 | 17.20 | -43.84 | current_profile_too_late | green_late_high_MAE | label_comparison_only |
| T_LOTTEWELLFOOD_20240618_4B_VALUATION_OVERLAY | 280360 | 롯데웰푸드 | Stage4B-Overlay | 2024-06-18 | 2024-06-18 | 193300 | 7.86 | -34.45 | 7.86 | -48.32 | current_profile_correct | 4B_overlay_success | 4B_overlay_only |
| T_ORION_20230516_FALSE_STAGE2 | 271560 | 오리온 | Stage2-Actionable | 2023-05-15 | 2023-05-16 | 143000 | 0.56 | -22.31 | 0.56 | -37.27 | current_profile_false_positive | false_positive_stage2 | representative |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_NONGSHIM_20230516_STAGE2_ACTIONABLE | 004370 | 2023-05-16 | 426000 | 7.04 | -7.39 | 15.02 | -9.39 | 17.37 | -14.08 | 2023-10-10 | 500000 | -30.50 |
| T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE | 280360 | 2024-05-17 | 142000 | 46.83 | -3.24 | 46.83 | -10.77 | 46.83 | -29.65 | 2024-06-18 | 208500 | -52.09 |
| T_ORION_20230516_FALSE_STAGE2 | 271560 | 2023-05-16 | 143000 | 0.56 | -16.08 | 0.56 | -22.31 | 0.56 | -37.27 | 2023-05-16 | 143800 | -37.62 |

### Overlay / label-comparison triggers

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_c_protection_label | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_LOTTEWELLFOOD_20240610_STAGE3_GREEN_PROXY | 280360 | Stage3-Green | 2024-06-10 | 177900 | 17.20 | -28.78 | null | null | not_applicable | label_comparison_only |
| T_LOTTEWELLFOOD_20240618_4B_VALUATION_OVERLAY | 280360 | Stage4B-Overlay | 2024-06-18 | 193300 | 7.86 | -34.45 | 0.77 | 0.77 | thesis_break_watch_only | 4B_overlay_only |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | verdict |
| --- | --- | --- | --- |
| 농심 | Promote Stage2/Yellow; wait for revision proof before Green | positive MFE with moderate MAE and no immediate false-positive collapse | current_profile_correct |
| 롯데웰푸드 | Could wait too long for Green; Stage2 was the better entry | strong 30D/90D MFE, then major drawdown after blowoff | current_profile_too_late |
| 오리온 | Could over-score generic global footprint as C20 quality | near-zero MFE and severe 180D MAE | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus: useful for direct export/local-capacity plus margin bridge; too permissive for generic global footprint.
yellow_threshold_75: acceptable if country-level sell-through and margin bridge are present; too generous for steady global brands without incremental reorder.
green_threshold_87_revision_55: kept; C20 Green should still need confirmed revision.
price_only_blowoff_guard: kept.
full_4B_non_price_requirement: strengthened; 롯데웰푸드 required valuation/positioning overlay, not price-only peak.
hard_4C_thesis_break_routes_to_4c: kept, but C20 needs earlier proxy-decay watch when distribution evidence does not convert into revision.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green entry proxy | peak after Stage2 | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- | --- |
| R5L15_C20_POS_NONGSHIM_202305_Q1_US_RAMEN_MARGIN | 426000 | approx 459000 after later confirmation | 500000 | 0.45 | Green somewhat late but still usable |
| R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY | 142000 | 177900 | 208500 | 0.54 | Green consumed over half of upside and carried much worse MAE |
| R5L15_C20_NEG_ORION_202305_GLOBAL_STEADY_GROWTH_HEADLINE | 143000 | not_applicable | 143800 | not_applicable | no confirmed Green should be allowed |

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | Stage2 entry price | 4B entry price | local peak | full-window peak | local proximity | full-window proximity | evidence type | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_LOTTEWELLFOOD_20240618_4B_VALUATION_OVERLAY | 142000 | 193300 | 208500 | 208500 | 0.77 | 0.77 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |

Interpretation: the 4B row is not “sell because it went up.” It is “the thesis is still alive, but the re-rating has moved from engine to fireworks.” The later drawdown from 208,500 to 99,900 confirms why C20 needs a valuation/positioning overlay once a defensive food rerating becomes crowded.

## 16. 4C Protection Audit

| case | 4C/protection trigger | label | protection read |
| --- | --- | --- | --- |
| 농심 | none | not_applicable | no hard thesis break in observed window |
| 롯데웰푸드 | not a full 4C in June; 4B overlay was enough | thesis_break_watch_only | 4B protected against large later drawdown before formal 4C evidence |
| 오리온 | watch from missing revision, not after late crash | hard_4c_late_if_waiting_for_accounting_style_break | earlier Stage2 demotion is better than waiting for hard 4C |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_sector_rule
sector_specific_rule_candidate = false
reason = only one large sector is tested and C20 already spans beauty/food; this loop supports canonical C20 compression, not a broad L5 sector-wide rule.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
axis_1 = C20_direct_country_sellthrough_capacity_margin_bridge_bonus
axis_2 = C20_generic_global_footprint_without_incremental_reorder_guard
axis_3 = C20_valuation_positioning_4B_overlay_after_fast_reprice
proposal_type = shadow_only
```

Candidate rule wording:

> For C20, Stage2-Actionable can receive a small shadow lift only when global distribution evidence is tied to country-level sell-through/reorder, export or local-plant capacity, and margin/revision bridge. Generic global footprint or steady overseas sales without incremental reorder should be demoted to Stage2-Watch/Yellow-Block. After fast repricing, full 4B requires valuation/positioning or margin-slowdown evidence, not price-only peak.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | selected reps | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 3 | 3 | 20.8 | -14.16 | 21.59 | -27.0 | 0.33 | 1 | mixed; misses C20 directness/proxy distinction |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | 3 | 20.8 | -14.16 | 21.59 | -27.0 | 0.33 | 2 | worse entry timing and no clean guard |
| P1_L5_consumer_sector_shadow | sector_shadow | 3 | 3 | 20.8 | -14.16 | 21.59 | -27.0 | 0.33 | 1 | too broad; sector rule not justified |
| P2_C20_direct_reorder_margin_shadow | canonical_shadow | 2 | 2 | 30.92 | -10.08 | 32.1 | -21.86 | 0.00 | 1 | best alignment; drops Orion false positive |
| P3_C20_counterexample_guard | guard_shadow | 2 | 2 | 30.92 | -10.08 | 32.1 | -21.86 | 0.00 | 1 | same as P2, but explicitly keeps generic-footprint cases watch-only |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5L15_C20_POS_NONGSHIM_202305_Q1_US_RAMEN_MARGIN | 82 | Stage3-Yellow | 86 | Stage3-Yellow | 15.02 | -9.39 | aligned_positive |
| R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY | 78 | Stage3-Yellow | 84 | Stage3-Yellow | 46.83 | -10.77 | aligned_positive_but_4B_needed |
| R5L15_C20_NEG_ORION_202305_GLOBAL_STEADY_GROWTH_HEADLINE | 76 | Stage3-Yellow | 66 | Stage2-Watch | 0.56 | -22.31 | guard_needed_false_positive |

Raw component interpretation:

```text
농심: margin_bridge + customer/channel quality + early revision are supported; Green remains below 87 until stronger revision confirmation.
롯데웰푸드: direct global/local plant setup is valid, but 4B overlay must activate after fast repricing.
오리온: customer/global footprint score exists, but no incremental reorder/revision. Execution-risk and valuation guard should cut the label.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_FOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_STEADY_FOOTPRINT | 2 | 1 | 1 | 0 | 3 | 0 | 5 | 3 | 2 | false | true | still needs more non-beauty food counterexamples and 4C cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - generic_global_food_footprint_false_positive
  - stage3_green_lateness_in_direct_export_reprice
  - post_blowoff_high_MAE_after_success
new_axis_proposed:
  - C20_direct_country_sellthrough_capacity_margin_bridge_bonus
  - C20_generic_global_footprint_without_incremental_reorder_guard
  - C20_valuation_positioning_4B_overlay_after_fast_reprice
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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
- Stock-Web manifest max_date and price basis.
- Symbol profile windows and corporate-action candidate dates.
- Entry-date close values from tradable shards.
- Trigger-level 30D/90D/180D MFE/MAE using tradable OHLC rows.
- same_entry_group_id dedupe rules.
- R5/L5 round-sector consistency.
- C20 canonical-archetype mapping.
```

Not validated:

```text
- No live 2026 candidate scan.
- No production scoring code inspection.
- No stock_agent src/e2r patch.
- No brokerage or auto-trading logic.
- Evidence-source timestamps are summarized from historical public-event context; exact filing timestamp should be rechecked before any future promotion batch.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_direct_country_sellthrough_capacity_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Direct country/channel reorder + capacity/local plant + margin bridge separated 농심/롯데웰푸드 from generic footprint.","Dropped false positive while preserving two positives",T_NONGSHIM_20230516_STAGE2_ACTIONABLE|T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_generic_global_footprint_without_incremental_reorder_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-1.5,-1.5,"오리온 shows global footprint alone can generate false Stage2/Yellow.","False positive demoted to watch",T_ORION_20230516_FALSE_STAGE2,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_valuation_positioning_4B_overlay_after_fast_reprice,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"롯데웰푸드 4B overlay at 0.77 peak proximity preceded large later drawdown.","Improved 4B timing without price-only exit",T_LOTTEWELLFOOD_20240618_4B_VALUATION_OVERLAY,1,1,0,low,canonical_shadow_only,"overlay only; not entry promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L15_C20_POS_NONGSHIM_202305_Q1_US_RAMEN_MARGIN","symbol":"004370","company_name":"농심","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_RAMEN_US_EXPORT_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_NONGSHIM_20230516_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"direct_export_capacity_margin_bridge_aligned_with_positive_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Direct ramen export/channel and margin bridge produced positive but not blowoff-level MFE; Green should wait for revision confirmation."}
{"row_type":"case","case_id":"R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_CONFECTIONERY_LOCAL_PLANTS_MARGIN_REPRICE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_but_later_drawdown_requires_4B_overlay","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Direct global confectionery/local plant exposure was rewarded quickly; later drawdown shows 4B overlay is required once valuation/positioning overheats."}
{"row_type":"case","case_id":"R5L15_C20_NEG_ORION_202305_GLOBAL_STEADY_GROWTH_HEADLINE","symbol":"271560","company_name":"오리온","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_STEADY_MARKETS_WITHOUT_INCREMENTAL_REORDER","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_ORION_20230516_FALSE_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global_brand_headline_without_incremental_revision_failed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Global footprint alone did not create rerating; country-level incremental sell-through/revision was missing and the 180D path broke hard."}
{"row_type":"trigger","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"trigger_id":"T_NONGSHIM_20230516_STAGE2_ACTIONABLE","case_id":"R5L15_C20_POS_NONGSHIM_202305_Q1_US_RAMEN_MARGIN","symbol":"004370","company_name":"농심","fine_archetype_id":"K_FOOD_RAMEN_US_EXPORT_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":426000,"evidence_available_at_that_date":"Q1 earnings shock, overseas ramen channel traction, and margin bridge were visible by the next tradable session; next-day close is used because exact disclosure time is treated as non-intraday-safe.","evidence_source":"public quarterly result/news summary; stock-web row confirms 2023-05-16 close/high/low; FT later confirmed 2023 Shin Ramyun overseas mix and U.S. expansion direction.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv","profile_path":"atlas/symbol_profiles/004/004370.json","MFE_30D_pct":7.04,"MFE_90D_pct":15.02,"MFE_180D_pct":17.37,"MFE_1Y_pct":17.37,"MFE_2Y_pct":null,"MAE_30D_pct":-7.39,"MAE_90D_pct":-9.39,"MAE_180D_pct":-14.08,"MAE_1Y_pct":-18.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-10","peak_price":500000,"drawdown_after_peak_pct":-30.5,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"004370_20230516_426000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"trigger_id":"T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE","case_id":"R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY","symbol":"280360","company_name":"롯데웰푸드","fine_archetype_id":"K_FOOD_GLOBAL_CONFECTIONERY_LOCAL_PLANTS_MARGIN_REPRICE","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":142000,"evidence_available_at_that_date":"Q1 result/revision context plus direct overseas confectionery/local plant narrative; price reacted before the strongest later Green-style confirmation.","evidence_source":"public quarterly result/news summary; stock-web confirms 2024-05-17 close 142000 and subsequent 2024-06-18 high 208500.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv; atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv","profile_path":"atlas/symbol_profiles/280/280360.json","MFE_30D_pct":46.83,"MFE_90D_pct":46.83,"MFE_180D_pct":46.83,"MFE_1Y_pct":46.83,"MFE_2Y_pct":null,"MAE_30D_pct":-3.24,"MAE_90D_pct":-10.77,"MAE_180D_pct":-29.65,"MAE_1Y_pct":-29.65,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":208500,"drawdown_after_peak_pct":-52.09,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"280360_20240517_142000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"trigger_id":"T_LOTTEWELLFOOD_20240610_STAGE3_GREEN_PROXY","case_id":"R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY","symbol":"280360","company_name":"롯데웰푸드","fine_archetype_id":"K_FOOD_GLOBAL_CONFECTIONERY_LOCAL_PLANTS_MARGIN_REPRICE","trigger_type":"Stage3-Green","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":177900,"evidence_available_at_that_date":"By this date the price already reflected much of the revision/positioning move; used only for Stage3 lateness audit.","evidence_source":"stock-web price row and post-Q1 revision path; label-comparison only.","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv; atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv","profile_path":"atlas/symbol_profiles/280/280360.json","MFE_30D_pct":17.2,"MFE_90D_pct":17.2,"MFE_180D_pct":17.2,"MFE_1Y_pct":17.2,"MFE_2Y_pct":null,"MAE_30D_pct":-5.56,"MAE_90D_pct":-28.78,"MAE_180D_pct":-43.84,"MAE_1Y_pct":-43.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":208500,"drawdown_after_peak_pct":-52.09,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_late_high_MAE","current_profile_verdict":"current_profile_too_late","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"280360_20240610_177900","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case but distinct Stage3 lateness audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"trigger_id":"T_LOTTEWELLFOOD_20240618_4B_VALUATION_OVERLAY","case_id":"R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY","symbol":"280360","company_name":"롯데웰푸드","fine_archetype_id":"K_FOOD_GLOBAL_CONFECTIONERY_LOCAL_PLANTS_MARGIN_REPRICE","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":193300,"evidence_available_at_that_date":"After the rapid repricing, valuation/positioning overheat and local peak proximity became meaningful non-price-aware 4B overlay evidence; not a price-only exit.","evidence_source":"stock-web peak row plus contemporaneous valuation/positioning-risk narrative; overlay only.","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv; atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv","profile_path":"atlas/symbol_profiles/280/280360.json","MFE_30D_pct":7.86,"MFE_90D_pct":7.86,"MFE_180D_pct":7.86,"MFE_1Y_pct":7.86,"MFE_2Y_pct":null,"MAE_30D_pct":-14.12,"MAE_90D_pct":-34.45,"MAE_180D_pct":-48.32,"MAE_1Y_pct":-48.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":208500,"drawdown_after_peak_pct":-52.09,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"280360_20240618_193300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case but distinct 4B overlay path","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"consumer_brand_distribution","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"trigger_id":"T_ORION_20230516_FALSE_STAGE2","case_id":"R5L15_C20_NEG_ORION_202305_GLOBAL_STEADY_GROWTH_HEADLINE","symbol":"271560","company_name":"오리온","fine_archetype_id":"K_FOOD_GLOBAL_STEADY_MARKETS_WITHOUT_INCREMENTAL_REORDER","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":143000,"evidence_available_at_that_date":"Global-market/steady confectionery footprint was visible, but incremental country-level sell-through, fresh capacity shock, or revision acceleration was not strong enough.","evidence_source":"public quarterly result/news summary; stock-web confirms immediate post-trigger drawdown and later 2024 gap-down path.","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv; atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","profile_path":"atlas/symbol_profiles/271/271560.json","MFE_30D_pct":0.56,"MFE_90D_pct":0.56,"MFE_180D_pct":0.56,"MFE_1Y_pct":0.56,"MFE_2Y_pct":null,"MAE_30D_pct":-16.08,"MAE_90D_pct":-22.31,"MAE_180D_pct":-37.27,"MAE_1Y_pct":-37.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-16","peak_price":143800,"drawdown_after_peak_pct":-37.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.01,"four_b_full_window_peak_proximity":0.01,"four_b_timing_verdict":"not_full_4B_because_no_prior_upside","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_if_waiting_for_accounting_style_break","trigger_outcome_label":"false_positive_stage2","current_profile_verdict":"current_profile_false_positive","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"271560_20230516_143000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L15_C20_POS_NONGSHIM_202305_Q1_US_RAMEN_MARGIN","trigger_id":"T_NONGSHIM_20230516_STAGE2_ACTIONABLE","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":13,"relative_strength_score":12,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":15,"relative_strength_score":12,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates direct export/channel+margin bridge from generic global footprint. Direct rerating signals get modest support; generic footprint without incremental country sell-through is guarded.","MFE_90D_pct":15.02,"MAE_90D_pct":-9.39,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L15_C20_POS_LOTTEWELLFOOD_202405_Q1_GLOBAL_CONFECTIONERY","trigger_id":"T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE","symbol":"280360","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":12,"relative_strength_score":13,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":19,"revision_score":15,"relative_strength_score":13,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates direct export/channel+margin bridge from generic global footprint. Direct rerating signals get modest support; generic footprint without incremental country sell-through is guarded.","MFE_90D_pct":46.83,"MAE_90D_pct":-10.77,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L15_C20_NEG_ORION_202305_GLOBAL_STEADY_GROWTH_HEADLINE","trigger_id":"T_ORION_20230516_FALSE_STAGE2","symbol":"271560","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":5,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":4,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C20 shadow separates direct export/channel+margin bridge from generic global footprint. Direct rerating signals get modest support; generic footprint without incremental country sell-through is guarded.","MFE_90D_pct":0.56,"MAE_90D_pct":-22.31,"score_return_alignment_label":"guard_needed_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"15","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_global_food_footprint_false_positive","stage3_green_lateness_in_direct_export_reprice","post_blowoff_high_MAE_after_success"],"diversity_score_summary":"new symbols 004370/280360/271560; new trigger families ramen US export, confectionery local-plant repricing, steady global footprint false positive; estimated score +50","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 15
next_round = R6
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest fields are from `atlas/manifest.json`, max_date `2026-02-20`, raw/unadjusted price basis, and tradable shard roots.
- 004370 profile confirms name, long trading history, and old corporate-action candidates outside the selected 2023 window.
- 280360 profile confirms the 롯데웰푸드 name period from 2023-04-14 and corporate-action candidates before the selected 2024 window.
- 271560 profile confirms no corporate-action candidates and a clean 2017-2026 trading profile.
- 004370 selected rows: 2023-05-16 close 426,000, later 2023-10-10 high 500,000, and 2024 early lows were read from stock-web tradable shards.
- 280360 selected rows: 2024-05-17 close 142,000, 2024-06-18 high 208,500/close 193,300, and 2025-01-23 low 99,900 were read from stock-web tradable shards.
- 271560 selected rows: 2023-05-16 close 143,000, 2023-05-16 high 143,800, and 2024-01-17 low 89,700 were read from stock-web tradable shards.
- Non-price evidence is intentionally marked shadow-only. Exact filing/news timestamps should be revalidated before future implementation promotion.
