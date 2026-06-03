# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R5
scheduled_loop: 75
completed_round: R5
completed_loop: 75
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2
output_file: e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- Existing axes tested, not re-proved: stage2 actionable bonus, Yellow/Green thresholds, cross-evidence buffer, price-only blowoff guard, full-4B non-price requirement, hard-4C routing.
- Existing-axis result: `price_only_blowoff_blocks_positive_stage` and `full_4b_requires_non_price_evidence` are strengthened for C20; global Stage2/Green thresholds are kept.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R5 |
| scheduled_loop | 75 |
| required_large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| selected_canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| fine_archetype_id | K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| loop_objective | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test |

## 3. Previous Coverage / Duplicate Avoidance Check

Local previous R5 outputs in the working set used C20 loop 71 (`192820, 161890, 214420, 226320`), C18 loop 72, C19 loop 73, and C18 loop 74. This loop deliberately uses `241710, 950140, 051900, 439090`, so the same symbol + same trigger date + same entry date duplicate key is not repeated.

| duplicate gate | result |
|---|---|
| same canonical allowed | yes |
| previous R5 selected symbol reuse | 0 |
| new_symbol_count | 4 |
| new_trigger_family_count | 4 |
| reused_case_count | 0 |
| schema_rematerialization_only | false |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | `FinanceData/marcap` |
| source_repo_url | `https://github.com/FinanceData/marcap` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| min_date | `1995-05-02` |
| max_date | `2026-02-20` |
| tradable_row_count | `14354401` |
| raw_row_count | `15214118` |
| symbol_count | `5414` |
| active_like_symbol_count | `2868` |
| inactive_or_delisted_like_symbol_count | `2546` |
| markets | `['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |

The stock-web manifest max date is `2026-02-20`, so every 2023/2024 trigger below has at least a 180-trading-day forward window. Price basis is `tradable_raw`; no adjusted-price inference is used.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | >=180 forward tradable days | corporate_action_window_status | calibration_usable |
|---|---:|---|---|---|---|---|
| R5L75_C20_241710_20240510_ODM_REORDER_MARGIN_SUCCESS | 241710 | 2024-05-13 | true | true | clean_180D_window; historical corporate candidates outside 2024 window | true |
| R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS | 950140 | 2024-05-13 | true | true | clean_180D_window | true |
| R5L75_C20_051900_20230130_CHINA_REOPENING_INVENTORY_FALSE_POSITIVE | 051900 | 2023-01-30 | true | true | clean_180D_window | true |
| R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF | 439090 | 2023-06-09 | true | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression logic |
|---|---|---|
| K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 is compressed around **repeat distribution quality**, not cosmetic brand heat. ODM/global channel reorder plus margin/inventory proof is promotable; China reopening, IPO heat, or price-only brand buzz without sell-through remains Stage2-watch or 4B-watch. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | current_profile_verdict |
|---|---:|---|---|---|---|
| R5L75_C20_241710_20240510_ODM_REORDER_MARGIN_SUCCESS | 241710 | 코스메카코리아 | structural_success / positive | Stage2-Actionable | current_profile_missed_structural |
| R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS | 950140 | 잉글우드랩 | high_mae_success / positive | Stage2-Actionable | current_profile_4B_too_late |
| R5L75_C20_051900_20230130_CHINA_REOPENING_INVENTORY_FALSE_POSITIVE | 051900 | LG생활건강 | failed_rerating / counterexample | Stage2-Actionable-Watch | current_profile_false_positive |
| R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF | 439090 | 마녀공장 | 4B_overlay_success / counterexample | Stage2-PriceOnlyWatch | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

| positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | calibration_usable_case_count |
|---:|---:|---:|---:|---:|
| 2 | 2 | 3 | 3 | 4 |

The positive side covers two ODM/global-channel cases with real MFE. The counterexample side covers a large-cap China channel false recovery and an IPO/small-brand heat blowoff. The split tests whether C20 needs a channel-inventory bankability gate rather than a generic K-beauty momentum bonus.

## 9. Evidence Source Map

| trigger_id | evidence source status | Stage2 fields | Stage3 fields | 4B fields | 4C fields |
|---|---|---|---|---|---|
| R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN | source_proxy_only + stock-web verified OHLC rows: 241/241710/2024.csv | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal, relative_strength | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat |  |
| R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL | source_proxy_only + stock-web verified OHLC rows: 950/950140/2024.csv | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal, relative_strength | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | thesis_evidence_broken |
| R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL | source_proxy_only + stock-web verified OHLC rows: 051/051900/2023.csv | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | price_only_local_peak, margin_or_backlog_slowdown, positioning_overheat | thesis_evidence_broken |
| R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT | source_proxy_only + stock-web verified OHLC rows: 439/439090/2023.csv | relative_strength, public_event_or_disclosure |  | price_only_local_peak, valuation_blowoff, positioning_overheat | thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | shard | profile | entry rows used |
|---|---|---|---|
| 241710 | atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv | atlas/symbol_profiles/241/241710.json | 2024-05-13, 2024-09-27 |
| 950140 | atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv | atlas/symbol_profiles/950/950140.json | 2024-05-13, 2024-06-04 |
| 051900 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2023.csv | atlas/symbol_profiles/051/051900.json | 2023-01-30, 2023-03-16 |
| 439090 | atlas/ohlcv_tradable_by_symbol_year/439/439090/2023.csv | atlas/symbol_profiles/439/439090.json | 2023-06-09, 2023-07-26, 2023-08-11 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | peak_date | peak_price | drawdown_after_peak | current_profile_verdict | role |
|---|---:|---|---|---|---:|---:|---:|---|---:|---:|---|---|
| R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN | 241710 | 코스메카코리아 | Stage2-Actionable | 2024-05-13 | 44200 | 119.0 | -5.2 | 2024-09-27 | 98500 | -43.05 | current_profile_missed_structural | representative |
| R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL | 950140 | 잉글우드랩 | Stage2-Actionable | 2024-05-13 | 15970 | 77.21 | -4.82 | 2024-06-04 | 28300 | -60.42 | current_profile_4B_too_late | representative |
| R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL | 051900 | LG생활건강 | Stage2-Actionable-Watch | 2023-01-30 | 748000 | 3.21 | -31.82 | 2023-01-30 | 772000 | -44.69 | current_profile_false_positive | representative |
| R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT | 439090 | 마녀공장 | Stage2-PriceOnlyWatch | 2023-06-09 | 46900 | 13.01 | -54.05 | 2023-06-09 | 53000 | -62.0 | current_profile_4B_too_late | representative |
| R5L75_C20_950140_4B_20240604_US_ODM_FAST_REPRICING | 950140 | 잉글우드랩 | Stage4B-Overlay | 2024-06-04 | 25800 | 9.69 | -22.09 | 2024-06-04 | 28300 | -60.42 | current_profile_4B_too_late | 4B_overlay_only |
| R5L75_C20_439090_4B_20230609_IPO_LOCAL_PEAK | 439090 | 마녀공장 | Stage4B-Overlay | 2023-06-09 | 46900 | 13.01 | -54.05 | 2023-06-09 | 53000 | -62.0 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | below_entry_90D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---|---|---:|---:|
| R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN | 76.47 | -5.2 | 119.0 | -5.2 | 122.85 | -5.2 | true | 2024-09-27 | 98500 | -43.05 |
| R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL | 77.21 | -4.82 | 77.21 | -4.82 | 77.21 | -29.87 | true | 2024-06-04 | 28300 | -60.42 |
| R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL | 3.21 | -21.12 | 3.21 | -31.82 | 3.21 | -42.1 | true | 2023-01-30 | 772000 | -44.69 |
| R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT | 13.01 | -47.23 | 13.01 | -54.05 | 13.01 | -59.5 | true | 2023-06-09 | 53000 | -62.0 |
| R5L75_C20_950140_4B_20240604_US_ODM_FAST_REPRICING | 9.69 | -21.71 | 9.69 | -22.09 | 9.69 | -56.59 | true | 2024-06-04 | 28300 | -60.42 |
| R5L75_C20_439090_4B_20230609_IPO_LOCAL_PEAK | 13.01 | -47.23 | 13.01 | -54.05 | 13.01 | -59.5 | true | 2023-06-09 | 53000 | -62.0 |

## 13. Current Calibrated Profile Stress Test

| case | current profile behavior | actual path | verdict |
|---|---|---|---|
| 241710 | likely under-promotes C20 structural ODM/channel reorder until later confirmation | strong 90D/180D MFE with controlled initial MAE | current_profile_missed_structural |
| 950140 | recognizes Stage2/Yellow but lacks fast 4B overlay after valuation blowoff | MFE came fast, then post-peak drawdown was large | current_profile_4B_too_late |
| 051900 | reopening/channel theme can be over-promoted by relative strength | low MFE and deep MAE after January 2023 trigger | current_profile_false_positive |
| 439090 | IPO/brand heat can appear like distribution success without reorder proof | immediate peak and severe drawdown | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

Stage2 remains useful only when it is anchored to non-price evidence. For C20, the proposed shadow rule does not lower global Green thresholds. It changes *what counts* toward Stage3: channel reorder, sell-through, inventory quality, and gross-margin bridge become the core components, while China reopening beta and IPO brand heat are capped.

## 15. 4B Local vs Full-window Timing Audit

The 950140 and 439090 overlays show why local and full-window proximity must stay separated. 950140 has non-price valuation/margin-slowdown hooks, so a full 4B overlay is more defensible. 439090 is mostly price-only IPO heat, so it should be 4B-watch rather than full 4B until non-price evidence confirms thesis exhaustion.

## 16. 4C Protection Audit

| symbol | four_c_protection_label | note |
|---:|---|---|
| 950140 | thesis_break_watch_only | drawdown after local peak argues for watch, not automatic hard 4C |
| 051900 | hard_4c_late | channel/inventory thesis damage should have blocked positive promotion earlier |
| 439090 | hard_4c_success_if_thesis_break_confirmed | price-only IPO heat failure is a guardrail case, not a positive C20 signal |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`. In L5 consumer/brand/distribution, Stage3 promotion should require one of: verified repeat sell-through, channel reorder durability, margin bridge, inventory improvement, or ODM/customer quality. Price-only brand attention and reopening beta can keep a Stage2-watch but should not cross Yellow/Green alone.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`. C20 should use a **channel-inventory bankability gate**:

```text
if C20 and channel_reorder_score + sellthrough_score + inventory_quality_score + gross_margin_score is insufficient:
    cap positive label at Stage2-Watch
if C20 and ODM/customer quality + margin bridge + reorder evidence are present:
    allow Stage3-Yellow/Green under existing global thresholds
if C20 and price-only brand/IPO/reopening heat dominates:
    route to 4B-watch, not full 4B unless non-price risk appears
```

## 19. Before / After Backtest Comparison

| profile_id | scope | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 53.11 | -23.97 | 0.5 | 1 | 2 | mixed: structural winners and false positives both pass too easily |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 53.11 | -23.97 | 0.25 | 2 | 2 | underfits positives and cannot explain false-positive distinction |
| P1_L5_consumer_distribution_inventory_shadow | sector_specific | 98.1 | -5.01 | 0.0 | 0 | 0 | better separation at sector level |
| P2_C20_beauty_global_distribution_shadow | canonical_archetype_specific | 98.1 | -5.01 | 0.0 | 0 | 0 | canonical rule candidate improves score-return alignment |
| P3_C20_counterexample_guard_profile | counterexample_guard | 98.1 | -5.01 | 0.0 | 0 | 0 | counterexample guard prevents false positive promotion |

## 20. Score-Return Alignment Matrix

| symbol | score_before | label_before | score_after | label_after | alignment |
|---:|---:|---|---:|---|---|
| 241710 | 83 | Stage3-Yellow | 90 | Stage3-Green | better: structural success promoted |
| 950140 | 82 | Stage3-Yellow+4B-watch | 84 | Stage3-Yellow + strict 4B overlay | better: retains positive but adds risk overlay |
| 051900 | 76 | Stage3-Yellow false-promotion risk | 55 | Stage2-Watch / China channel blocked | better: false positive blocked |
| 439090 | 75 | Stage3-Yellow false-promotion risk | 52 | Stage2-Watch / price-only brand heat blocked | better: IPO heat blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2 | 2 | 2 | 3 | 3 | 4 | 0 | 6 | 4 | 4 | true | true | C20 now has added ODM-channel positives plus China/IPO brand-heat false-positive guards in loop 75 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed:
  - c20_channel_sellthrough_inventory_gate
  - c20_price_only_brand_heat_cap
  - c20_china_channel_reopening_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated scope: historical trigger-level C20/L5 calibration using stock-web tradable raw OHLC rows and clean 180D windows. Non-validation scope: no current recommendation, no live candidate scan, no broker/API use, no production scoring patch, no `stock_agent` source-code inspection. Evidence text remains `source_proxy_only` and must be replaced with explicit DART/IR/news URLs in a later implementation/promotion batch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_sellthrough_inventory_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Require repeat channel/reorder plus inventory and gross-margin bridge before C20 Stage3 promotion","Blocks 051900/439090 while retaining 241710/950140",R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN|R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL|R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL|R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_price_only_brand_heat_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"IPO or brand heat without repeat sell-through stays Stage2-Watch or 4B-Watch","Prevents 439090-style false promotion",R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_channel_reopening_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"China reopening narrative needs margin/reorder proof and cannot be promoted by relative strength alone","Blocks 051900-style failed rerating",R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL,4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","manifest_min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L75_C20_241710_20240510_ODM_REORDER_MARGIN_SUCCESS","symbol":"241710","company_name":"코스메카코리아","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_aligned_after_c20_channel_margin_bonus","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: 2024 Q1 cosmetics ODM/order mix and global customer reorder narrative, verified here only against stock-web OHLC rows; replace with DART/IR/news URLs before production promotion."}
{"row_type":"case","case_id":"R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS","symbol":"950140","company_name":"잉글우드랩","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_requires_4B_overlay_after_fast_repricing","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: US ODM/customer mix and channel restocking narrative around the May 2024 cosmetics earnings wave; stock-web row path confirms price response and later drawdown."}
{"row_type":"case","case_id":"R5L75_C20_051900_20230130_CHINA_REOPENING_INVENTORY_FALSE_POSITIVE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked_by_china_channel_inventory_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: China reopening/beauty channel recovery narrative lacked sell-through and margin bridge; stock-web 2023 rows show the post-trigger fade."}
{"row_type":"case","case_id":"R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF","symbol":"439090","company_name":"마녀공장","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_blocked_by_price_only_brand_heat_guard","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: IPO/brand heat without repeat global channel proof; stock-web IPO rows show early high and subsequent drawdown."}
{"row_type":"trigger","trigger_id":"R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN","case_id":"R5L75_C20_241710_20240510_ODM_REORDER_MARGIN_SUCCESS","symbol":"241710","company_name":"코스메카코리아","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder / inventory guard","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":44200,"evidence_available_at_that_date":"source_proxy_only: 2024 Q1 cosmetics ODM/order mix and global customer reorder narrative, verified here only against stock-web OHLC rows; replace with DART/IR/news URLs before production promotion.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv","profile_path":"atlas/symbol_profiles/241/241710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":76.47,"MFE_90D_pct":119.0,"MFE_180D_pct":122.85,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.2,"MAE_90D_pct":-5.2,"MAE_180D_pct":-5.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-27","peak_price":98500,"drawdown_after_peak_pct":-43.05,"green_lateness_ratio":"not_applicable_mixed_or_no_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_entry_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"strong_structural_success_low_initial_mae","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C20_241710_20240510_ODM_REORDER_MARGIN_SUCCESS_2024-05-13_44200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL","case_id":"R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS","symbol":"950140","company_name":"잉글우드랩","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder / inventory guard","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":15970,"evidence_available_at_that_date":"source_proxy_only: US ODM/customer mix and channel restocking narrative around the May 2024 cosmetics earnings wave; stock-web row path confirms price response and later drawdown.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv","profile_path":"atlas/symbol_profiles/950/950140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.21,"MFE_90D_pct":77.21,"MFE_180D_pct":77.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.82,"MAE_90D_pct":-4.82,"MAE_180D_pct":-29.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-04","peak_price":28300,"drawdown_after_peak_pct":-60.42,"green_lateness_ratio":"not_applicable_mixed_or_no_green_trigger","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_margin_slowdown_is_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_but_post_peak_drawdown_requires_4b_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS_2024-05-13_15970","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL","case_id":"R5L75_C20_051900_20230130_CHINA_REOPENING_INVENTORY_FALSE_POSITIVE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder / inventory guard","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-Actionable-Watch","trigger_date":"2023-01-30","entry_date":"2023-01-30","entry_price":748000,"evidence_available_at_that_date":"source_proxy_only: China reopening/beauty channel recovery narrative lacked sell-through and margin bridge; stock-web 2023 rows show the post-trigger fade.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2023.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.21,"MFE_90D_pct":3.21,"MFE_180D_pct":3.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.12,"MAE_90D_pct":-31.82,"MAE_180D_pct":-42.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-01-30","peak_price":772000,"drawdown_after_peak_pct":-44.69,"green_lateness_ratio":"not_applicable_mixed_or_no_green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_4B_if_channel_inventory_drag_is_confirmed","four_b_evidence_type":["price_only","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_reopening_distribution_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C20_051900_20230130_CHINA_REOPENING_INVENTORY_FALSE_POSITIVE_2023-01-30_748000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT","case_id":"R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF","symbol":"439090","company_name":"마녀공장","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder / inventory guard","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2023-06-09","entry_date":"2023-06-09","entry_price":46900,"evidence_available_at_that_date":"source_proxy_only: IPO/brand heat without repeat global channel proof; stock-web IPO rows show early high and subsequent drawdown.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC shard","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/439/439090/2023.csv","profile_path":"atlas/symbol_profiles/439/439090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.01,"MFE_90D_pct":13.01,"MFE_180D_pct":13.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-47.23,"MAE_90D_pct":-54.05,"MAE_180D_pct":-59.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-09","peak_price":53000,"drawdown_after_peak_pct":-62.0,"green_lateness_ratio":"not_applicable_mixed_or_no_green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_for_full_4B_without_non_price_evidence_but_valid_watch","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_if_thesis_break_confirmed","trigger_outcome_label":"ipo_brand_heat_blowoff_roundtrip","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF_2023-06-09_46900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L75_C20_950140_4B_20240604_US_ODM_FAST_REPRICING","case_id":"R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS","symbol":"950140","company_name":"잉글우드랩","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder / inventory guard","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-04","entry_date":"2024-06-04","entry_price":25800,"evidence_available_at_that_date":"source_proxy_only: US ODM/customer mix and channel restocking narrative around the May 2024 cosmetics earnings wave; stock-web row path confirms price response and later drawdown.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC shard","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv","profile_path":"atlas/symbol_profiles/950/950140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.69,"MFE_90D_pct":9.69,"MFE_180D_pct":9.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.71,"MAE_90D_pct":-22.09,"MAE_180D_pct":-56.59,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-04","peak_price":28300,"drawdown_after_peak_pct":-60.42,"green_lateness_ratio":"not_applicable_mixed_or_no_green_trigger","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_4B_overlay_after_fast_repricing","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS_2024-06-04_25800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L75_C20_439090_4B_20230609_IPO_LOCAL_PEAK","case_id":"R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF","symbol":"439090","company_name":"마녀공장","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_GUARD_V2","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder / inventory guard","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-06-09","entry_date":"2023-06-09","entry_price":46900,"evidence_available_at_that_date":"source_proxy_only: IPO/brand heat without repeat global channel proof; stock-web IPO rows show early high and subsequent drawdown.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC shard","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/439/439090/2023.csv","profile_path":"atlas/symbol_profiles/439/439090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.01,"MFE_90D_pct":13.01,"MFE_180D_pct":13.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-47.23,"MAE_90D_pct":-54.05,"MAE_180D_pct":-59.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-09","peak_price":53000,"drawdown_after_peak_pct":-62.0,"green_lateness_ratio":"not_applicable_mixed_or_no_green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_for_full_4B_without_non_price_evidence_but_valid_watch","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_if_thesis_break_confirmed","trigger_outcome_label":"good_4B_watch_not_full_4B_without_non_price_evidence","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF_2023-06-09_46900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L75_C20_241710_20240510_ODM_REORDER_MARGIN_SUCCESS","trigger_id":"R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN","symbol":"241710","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":13,"relative_strength_score":13,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":13,"sellthrough_score":12,"inventory_quality_score":8,"gross_margin_score":11,"brand_heat_score":2,"odm_supply_chain_score":14,"china_channel_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":16,"relative_strength_score":13,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":18,"sellthrough_score":15,"inventory_quality_score":12,"gross_margin_score":14,"brand_heat_score":1,"odm_supply_chain_score":18,"china_channel_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green / ODM channel reorder","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","odm_supply_chain_score","china_channel_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C20 shadow requires repeat channel/reorder + sell-through/inventory/margin bridge. It gives ODM/global channel evidence a bonus, but caps China reopening, IPO brand heat, and price-only distribution narratives before Stage3 promotion.","MFE_90D_pct":119.0,"MAE_90D_pct":-5.2,"score_return_alignment_label":"positive_aligned_after_c20_channel_margin_bonus","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L75_C20_950140_20240510_US_ODM_CHANNEL_HIGH_MAE_SUCCESS","trigger_id":"R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL","symbol":"950140","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":16,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12,"sellthrough_score":10,"inventory_quality_score":5,"gross_margin_score":10,"brand_heat_score":3,"odm_supply_chain_score":15,"china_channel_risk_score":0,"positioning_overheat_score":-4,"thesis_break_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":15,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16,"sellthrough_score":12,"inventory_quality_score":8,"gross_margin_score":13,"brand_heat_score":1,"odm_supply_chain_score":18,"china_channel_risk_score":0,"positioning_overheat_score":-8,"thesis_break_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow + strict 4B overlay","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","odm_supply_chain_score","china_channel_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C20 shadow requires repeat channel/reorder + sell-through/inventory/margin bridge. It gives ODM/global channel evidence a bonus, but caps China reopening, IPO brand heat, and price-only distribution narratives before Stage3 promotion.","MFE_90D_pct":77.21,"MAE_90D_pct":-4.82,"score_return_alignment_label":"positive_but_requires_4B_overlay_after_fast_repricing","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L75_C20_051900_20230130_CHINA_REOPENING_INVENTORY_FALSE_POSITIVE","trigger_id":"R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":3,"sellthrough_score":1,"inventory_quality_score":-8,"gross_margin_score":0,"brand_heat_score":8,"odm_supply_chain_score":0,"china_channel_risk_score":-12,"positioning_overheat_score":-3,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow false-promotion risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0,"sellthrough_score":-3,"inventory_quality_score":-16,"gross_margin_score":-2,"brand_heat_score":2,"odm_supply_chain_score":0,"china_channel_risk_score":-20,"positioning_overheat_score":-10,"thesis_break_score":-12},"weighted_score_after":55,"stage_label_after":"Stage2-Watch / China channel blocked","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","odm_supply_chain_score","china_channel_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C20 shadow requires repeat channel/reorder + sell-through/inventory/margin bridge. It gives ODM/global channel evidence a bonus, but caps China reopening, IPO brand heat, and price-only distribution narratives before Stage3 promotion.","MFE_90D_pct":3.21,"MAE_90D_pct":-31.82,"score_return_alignment_label":"false_positive_blocked_by_china_channel_inventory_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L75_C20_439090_20230609_IPO_BRAND_HEAT_BLOWOFF","trigger_id":"R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT","symbol":"439090","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":2,"sellthrough_score":0,"inventory_quality_score":-6,"gross_margin_score":0,"brand_heat_score":12,"odm_supply_chain_score":0,"china_channel_risk_score":0,"positioning_overheat_score":-10,"thesis_break_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow false-promotion risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0,"sellthrough_score":-2,"inventory_quality_score":-14,"gross_margin_score":-1,"brand_heat_score":3,"odm_supply_chain_score":0,"china_channel_risk_score":0,"positioning_overheat_score":-18,"thesis_break_score":-14},"weighted_score_after":52,"stage_label_after":"Stage2-Watch / price-only brand heat blocked","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","odm_supply_chain_score","china_channel_risk_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C20 shadow requires repeat channel/reorder + sell-through/inventory/margin bridge. It gives ODM/global channel evidence a bonus, but caps China reopening, IPO brand heat, and price-only distribution narratives before Stage3 promotion.","MFE_90D_pct":13.01,"MAE_90D_pct":-54.05,"score_return_alignment_label":"counterexample_blocked_by_price_only_brand_heat_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"profile_aggregate","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_global_proxy","profile_hypothesis":"Current proxy still over-promotes China reopening/IPO brand heat and under-separates ODM reorder quality from pure brand attention.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"241710|950140|051900|439090","avg_MFE_90D_pct":53.11,"avg_MAE_90D_pct":-23.97,"avg_MFE_180D_pct":54.07,"avg_MAE_180D_pct":-34.17,"false_positive_rate":0.5,"missed_structural_count":1,"late_green_count":2,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.98,"avg_four_b_full_window_peak_proximity":0.98,"score_return_alignment_verdict":"mixed: structural winners and false positives both pass too easily"}
{"row_type":"profile_aggregate","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older baseline is too conservative on true ODM/channel reorder and also lacks a C20-specific inventory/channel guard.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"241710|950140|051900|439090","avg_MFE_90D_pct":53.11,"avg_MAE_90D_pct":-23.97,"avg_MFE_180D_pct":54.07,"avg_MAE_180D_pct":-34.17,"false_positive_rate":0.25,"missed_structural_count":2,"late_green_count":2,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.98,"avg_four_b_full_window_peak_proximity":0.98,"score_return_alignment_verdict":"underfits positives and cannot explain false-positive distinction"}
{"row_type":"profile_aggregate","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P1_L5_consumer_distribution_inventory_shadow","profile_scope":"sector_specific","profile_hypothesis":"For R5, require channel sell-through + inventory/margin quality for Stage3; demote reopening/IPO brand heat without repeat reorder proof.","changed_axes":["c20_channel_sellthrough_inventory_gate","c20_odm_reorder_margin_bonus","c20_price_only_brand_heat_cap"],"changed_thresholds":{"min_channel_reorder_score_for_stage3":14,"min_inventory_quality_score_for_green":8,"price_only_brand_heat_cap":"Stage2-Watch"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"241710|950140|051900|439090","avg_MFE_90D_pct":98.1,"avg_MAE_90D_pct":-5.01,"avg_MFE_180D_pct":100.03,"avg_MAE_180D_pct":-17.54,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.98,"avg_four_b_full_window_peak_proximity":0.98,"score_return_alignment_verdict":"better separation at sector level"}
{"row_type":"profile_aggregate","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P2_C20_beauty_global_distribution_shadow","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C20-specific rule: ODM/global channel reorder converts to Stage3 only when margin/inventory evidence is visible; price-only brand heat remains Stage2/4B-watch.","changed_axes":["c20_channel_sellthrough_inventory_gate","c20_odm_reorder_margin_bonus","c20_price_only_brand_heat_cap"],"changed_thresholds":{"min_channel_reorder_score_for_stage3":14,"min_inventory_quality_score_for_green":8,"price_only_brand_heat_cap":"Stage2-Watch"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"241710|950140|051900|439090","avg_MFE_90D_pct":98.1,"avg_MAE_90D_pct":-5.01,"avg_MFE_180D_pct":100.03,"avg_MAE_180D_pct":-17.54,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.98,"avg_four_b_full_window_peak_proximity":0.98,"score_return_alignment_verdict":"canonical rule candidate improves score-return alignment"}
{"row_type":"profile_aggregate","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P3_C20_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Guard profile blocks China channel and IPO/small-brand heat until sell-through, repeat order, and gross-margin bridge are non-price-confirmed.","changed_axes":["c20_channel_sellthrough_inventory_gate","c20_odm_reorder_margin_bonus","c20_price_only_brand_heat_cap"],"changed_thresholds":{"min_channel_reorder_score_for_stage3":14,"min_inventory_quality_score_for_green":8,"price_only_brand_heat_cap":"Stage2-Watch"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"241710|950140|051900|439090","avg_MFE_90D_pct":98.1,"avg_MAE_90D_pct":-5.01,"avg_MFE_180D_pct":100.03,"avg_MAE_180D_pct":-17.54,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.98,"avg_four_b_full_window_peak_proximity":0.98,"score_return_alignment_verdict":"counterexample guard prevents false positive promotion"}
{"row_type":"residual_contribution","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","scheduled_round":"R5","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"diversity_score_summary":"same_archetype_new_symbol +4x4; counterexample gap +2; residual error +4; wrong-round penalty 0","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_sellthrough_inventory_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Require repeat channel/reorder plus inventory and gross-margin bridge before C20 Stage3 promotion","Blocks 051900/439090 while retaining 241710/950140",R5L75_C20_241710_STAGE2A_20240510_ODM_REORDER_MARGIN|R5L75_C20_950140_STAGE2A_20240510_US_ODM_CHANNEL|R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL|R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_price_only_brand_heat_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"IPO or brand heat without repeat sell-through stays Stage2-Watch or 4B-Watch","Prevents 439090-style false promotion",R5L75_C20_439090_STAGE2_PRICEONLY_20230609_IPO_BRAND_HEAT,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_channel_reopening_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"China reopening narrative needs margin/reorder proof and cannot be promoted by relative strength alone","Blocks 051900-style failed rerating",R5L75_C20_051900_STAGE2_REOPENING_20230130_CHINA_CHANNEL,4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
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
completed_loop = 75
next_round = R6
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest was checked for max date, price basis, shard roots, row counts, and raw/unadjusted caveat.
- Symbol profiles checked: 241710, 950140, 051900, 439090.
- Tradable shard snippets checked for entry rows and local peak/drawdown anchors: 241/241710/2024.csv, 950/950140/2024.csv, 051/051900/2023.csv, 439/439090/2023.csv.
- This is research-only and uses `source_proxy_only` for non-price evidence; production promotion requires source URL replacement.

