# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R4_loop_12_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
scheduled_round: R4
scheduled_loop: 12
completed_round: R4
completed_loop: 12
next_round: R5
next_loop: 12
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
stock_web_manifest_max_date: "2026-02-20"
created_at_utc: "2026-05-27T21:06:29.698582+00:00"
```

This loop adds **4** new independent cases, **1** counterexamples, and **2** residual errors for **R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE**.

No current/live candidate scan was performed. No stock_agent production scoring was changed. This is a standalone historical residual calibration file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
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

The residual question here is not “does a metal stock go up when commodity prices go up?” That is too broad. The C15 question is narrower: **does the commodity or product spread persist long enough, and is it transmitted into margin / revision / cash flow rather than being only a price or event-premium move?**

Think of the spread cycle like a furnace gauge. Product price, input cost, utilization, and inventory are four needles. A valid C15 Green should not be lit by one needle alone; it needs enough of the gauge board moving together.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 12 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE |
| fine_archetype_id | STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE |
| loop_objective | coverage_gap_fill; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; 4B_non_price_requirement_stress_test; yellow_threshold_stress_test |

R4 maps to L4 materials / spread / strategic resources. C15 was selected because the existing local R4 loop 10~11 files were already concentrated in C17 chemical commodity spreads. This loop therefore fills the metal / steel / copper / non-ferrous spread coverage gap rather than repeating chemical NB latex / spandex cases.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 artifact scan found R4 loop 10 and loop 11 C17 files. The immediate previous generated file in this session was R3 / loop 12 and reported `next_round=R4`, `next_loop=12`. Therefore this file follows the sequential scheduler.

```text
scheduled_round = R4
scheduled_loop = 12
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
```

Novelty summary:

| metric | value |
|---|---:|
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |
| new_trigger_family_count | 4 |
| new_independent_case_ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-Web manifest and schema validation:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

| symbol | company | profile_path | corporate-action candidate status | selected 180D window status | calibration_usable |
|---:|---|---|---|---|---|
| 005490 | POSCO홀딩스 | atlas/symbol_profiles/005/005490.json | count=0 | clean_180D_window | true |
| 004020 | 현대제철 | atlas/symbol_profiles/004/004020.json | old candidates through 2014 only | clean_180D_window | true |
| 103140 | 풍산 | atlas/symbol_profiles/103/103140.json | count=0 | clean_180D_window | true |
| 010130 | 고려아연 | atlas/symbol_profiles/010/010130.json | count=0 | clean_180D_window | true |

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward_180D_trading_window_available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false
calibration_usable = true for all representative rows
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| INTEGRATED_STEEL_PRODUCT_SPREAD_MARGIN_BRIDGE | C15_MATERIAL_SPREAD_SUPERCYCLE | Product price / raw material pass-through transmitted into integrated steel margins. |
| STEEL_SPREAD_BETA_HIGH_MAE_QUALITY_HAIRCUT | C15_MATERIAL_SPREAD_SUPERCYCLE | Same steel spread, but higher beta and higher drawdown require quality haircut. |
| COPPER_NONFERROUS_PRICE_SPREAD_POLICY_DEMAND_BRIDGE | C15_MATERIAL_SPREAD_SUPERCYCLE | Copper price and electrification demand can create spread-sensitive rerating. |
| EVENT_PREMIUM_NOT_MATERIAL_SPREAD | C15_MATERIAL_SPREAD_SUPERCYCLE counterexample | Control premium / tender-cap price path must not be learned as material-spread success. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | trigger family | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R4L12_C15_005490_POSCO_STEEL_SPREAD_20210426 | 005490 | POSCO홀딩스 | structural_success | positive | integrated_steel_product_spread_margin_bridge | current_profile_correct |
| R4L12_C15_004020_HYUNDAI_STEEL_SPREAD_20210426 | 004020 | 현대제철 | high_mae_success | positive | steel_spread_beta_high_mae_quality_haircut | current_profile_correct_but_mae_underweighted |
| R4L12_C15_103140_POONGSAN_COPPER_SPREAD_20240329 | 103140 | 풍산 | structural_success | positive | copper_nonferrous_price_spread_policy_demand_bridge | current_profile_missed_structural |
| R4L12_C15_010130_KOREA_ZINC_EVENT_PREMIUM_20240913 | 010130 | 고려아연 | price_moved_without_evidence | counterexample | event_premium_not_material_spread | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
4B_case_count = 3
4C_case_count = 0
```

POSCO and 현대제철 are the steel spread pair: both worked, but 현대제철 carried more drawdown. 풍산 is the copper/non-ferrous positive with a later price-only 4B warning. 고려아연 is the needed counterexample: a spectacular price path, but not a clean material-spread path. It should protect the model from confusing control premium with commodity spread economics.

## 9. Evidence Source Map

| symbol | trigger_date | evidence family | evidence status | scoring use |
|---:|---|---|---|---|
| 005490 | 2021-04-26 | integrated steel product spread / margin bridge | historical public mechanism + stock-web OHLC | positive C15 |
| 004020 | 2021-04-26 | steel beta / higher MAE spread cycle | historical public mechanism + stock-web OHLC | positive with quality haircut |
| 103140 | 2024-03-29 | copper price / electrification / non-ferrous spread | historical public mechanism + stock-web OHLC | positive, 4B watch |
| 010130 | 2024-09-13 | event premium / control premium | public event mechanism + stock-web OHLC | counterexample / reroute guard |

## 10. Price Data Source Map

| symbol | price_shard_path | sampled stock-web rows used |
|---:|---|---|
| 005490 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv | entry 2021-04-26 close 362,500; peak 2021-05-10 high 413,500; low 2021-10-29 low 296,000 |
| 004020 | atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv | entry 2021-04-26 close 52,000; peak 2021-05-11 high 63,000; low 2021-10-06 low 43,250 |
| 103140 | atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv | entry 2024-03-29 close 50,500; peak 2024-05-14 high 78,900; low 2024-08-05 low 47,000 |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv | entry 2024-09-13 close 666,000; event peak 2024-12-06 high 2,407,000; post-peak low near 1,475,000 in fetched continuation |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R4L12_C15_005490_T1 | 005490 | Stage2-Actionable | 2021-04-26 | 2021-04-26 | 362,500 | 14.07 | 14.07 | 14.07 | -8.41 | -15.59 | -18.34 | 2021-05-10 | 413,500 | -28.42 | current_profile_correct |
| R4L12_C15_004020_T1 | 004020 | Stage2-Actionable | 2021-04-26 | 2021-04-26 | 52,000 | 21.15 | 21.15 | 21.15 | -2.88 | -12.98 | -16.83 | 2021-05-11 | 63,000 | -31.35 | current_profile_correct_but_mae_underweighted |
| R4L12_C15_103140_T1 | 103140 | Stage2-Actionable | 2024-03-29 | 2024-03-29 | 50,500 | 56.24 | 56.24 | 56.24 | -3.37 | -6.93 | -6.93 | 2024-05-14 | 78,900 | -40.43 | current_profile_missed_structural |
| R4L12_C15_010130_T1 | 010130 | Stage2-FalsePositiveGuard | 2024-09-13 | 2024-09-13 | 666,000 | 131.68 | 261.41 | 261.41 | -1.65 | -1.65 | -1.65 | 2024-12-06 | 2,407,000 | -38.72 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

The table above is the deduplicated representative trigger table. All four rows are included in aggregate metrics because `calibration_usable=true`, `dedupe_for_aggregate=true`, `aggregate_group_role=representative`, and `do_not_count_as_new_case=false`.

Aggregate representative result:

| metric | value |
|---|---:|
| avg_MFE_90D_pct | 88.22 |
| avg_MAE_90D_pct | -9.29 |
| avg_MFE_180D_pct | 88.22 |
| avg_MAE_180D_pct | -10.94 |
| representative_trigger_count | 4 |

Important: the 고려아연 row is quantitatively usable but semantically counterexample-only. P3 excludes it from positive C15 aggregation because the price path is event premium rather than material-spread evidence.

## 13. Current Calibrated Profile Stress Test

| symbol | P0 likely judgment | realized path | verdict |
|---:|---|---|---|
| 005490 | Stage3-Yellow, maybe Green after revision | moderate MFE, acceptable MAE, later normalization | current_profile_correct |
| 004020 | Stage3-Yellow | MFE worked but MAE/drawdown were larger | current_profile_correct_but_mae_underweighted |
| 103140 | Stage2-Actionable, not enough C15-specific bridge | strong MFE with clean 90D path, later drawdown | current_profile_missed_structural |
| 010130 | relative-strength/event price path could be misread as material rerating | huge MFE but not C15 causal evidence | current_profile_false_positive |

Answers to the current-profile stress questions:

1. Stage2 bonus is useful for real steel/copper spread cases but insufficiently causal by itself.
2. Yellow threshold 75 is acceptable for POSCO / Hyundai Steel, but misses 풍산 unless spread-duration evidence is represented.
3. Green threshold 87 should not be lowered globally; C15 needs component-gated promotion.
4. price-only blowoff guard remains correct and is strengthened by 고려아연.
5. full 4B non-price requirement remains correct; 풍산 and 고려아연 show why local peaks are not enough.
6. hard 4C routing is not directly changed in this MD.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | Green candidate | green_lateness_ratio | interpretation |
|---:|---|---|---|---|
| 005490 | 2021-04-26 / 362,500 | later margin confirmation | 0.24 | Green not too late if spread bridge is confirmed quickly. |
| 004020 | 2021-04-26 / 52,000 | later margin confirmation | 0.31 | Green somewhat late; quality haircut needed due MAE. |
| 103140 | 2024-03-29 / 50,500 | copper spread confirmation | 0.18 | Current profile may miss structural copper spread early. |
| 010130 | 2024-09-13 / 666,000 | not a C15 Green | not_applicable | Event premium should be excluded from C15 learning. |

## 15. 4B Local vs Full-window Timing Audit

| symbol | local peak | full-window peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---:|---|---|---:|---:|---|
| 005490 | 2021-05-10 | 2021-05-10 | n/a | n/a | No full 4B row proposed; later spread normalization only. |
| 004020 | 2021-05-11 | 2021-05-11 | 0.96 | 0.96 | Good 4B timing only after non-price margin slowdown. |
| 103140 | 2024-05-14 | 2024-05-14 | 1.00 | 1.00 | Price-only 4B too early until copper demand/inventory evidence appears. |
| 010130 | 2024-10-29 local event peak | 2024-12-06 | 0.47 | 1.00 | Event-premium 4B, not material-spread 4B. |

## 16. 4C Protection Audit

No hard 4C promotion is proposed. The C15 residual contribution is mostly about avoiding false Green and false 4B attribution. For 고려아연, a price break alone should not be C15 thesis break because the thesis was not a material-spread thesis in the first place.

```text
four_c_protection_label = thesis_break_watch_only / false_break_if_routed_as_spread_thesis_break
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L4_high_MAE_success_quality_haircut
proposal_type = sector_shadow_only
```

L4 materials are cyclical. A successful spread case can still carry large MAE because the market constantly reprices inventory, demand, and input-cost pass-through. The sector shadow should not only reward MFE; it should penalize high-MAE spread-beta names unless balance-sheet / product-specificity / contract pricing evidence is strong.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id_1 = C15_product_specific_spread_duration_bonus
rule_id_2 = C15_event_premium_exclusion_guard
```

C15 Green should require at least two of the following:

```text
- product-specific spread duration evidence
- input-cost pass-through / ASP bridge
- confirmed margin or revision bridge
- inventory cycle not deteriorating
- customer/end-market demand support
```

And it should reject or reroute:

```text
- control premium / tender-cap event premium
- pure relative strength without spread evidence
- price-only blowoff
- one-day commodity spike without product margin transmission
```

## 19. Before / After Backtest Comparison

| symbol | before stage | before score | after stage | after score | MFE90 | MAE90 | alignment |
|---:|---|---:|---|---:|---:|---:|---|
| 005490 | Stage3-Yellow | 82 | Stage3-Green-shadow | 87 | 14.07 | -15.59 | structural_success_moderate_mfe_with_later_spread_normalization |
| 004020 | Stage3-Yellow | 79 | Stage3-Yellow/Green-buffer-shadow | 84 | 21.15 | -12.98 | high_mae_success_requires_quality_haircut |
| 103140 | Stage2-Actionable | 74 | Stage3-Yellow-shadow | 83 | 56.24 | -6.93 | structural_success_with_price_only_4B_warning |
| 010130 | Stage3-Yellow/false-spread-risk | 78 | Stage2-Watch/reroute-to-C32 | 62 | 261.41 | -1.65 | counterexample_event_premium_misattribution |

## 20. Score-Return Alignment Matrix

| profile_id | scope | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current_proxy | 88.22 | -9.29 | 88.22 | -10.94 | 0.25 | 1 | mixed; event premium can pollute C15 if not guarded |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 88.22 | -9.29 | 88.22 | -10.94 | 0.5 | 0 | worse: high beta and event premium are confused with spread signal |
| P1_sector_specific_candidate_profile | sector_specific | 88.22 | -9.29 | 88.22 | -10.94 | 0.25 | 0 | better for steel/copper spread cases, still needs event-premium guard |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 88.22 | -9.29 | 88.22 | -10.94 | 0.0 | 0 | best candidate; prevents 고려아연 event premium from entering C15 as spread evidence |
| P3_counterexample_guard_profile | counterexample_guard | 30.49 | -11.83 | 30.49 | -14.03 | 0.0 | 0 | cleaner quantitative C15 aggregate after excluding event-premium row |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE | 3 | 1 | 3 | 0 | 4 | 0 | 4 | 4 | 2 | true | true | C15 now has positive steel/copper samples plus event-premium counterexample; still needs more alumina/nickel/rare-earth cases. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - material_spread_missed_structural
  - high_mae_success_quality_haircut_needed
  - event_premium_misattributed_as_material_spread
new_axis_proposed:
  - C15_product_specific_spread_duration_bonus
  - C15_event_premium_exclusion_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level calibration only.
- Stock-Web 1D OHLCV tradable rows only.
- Raw/unadjusted marcap price basis.
- 30D / 90D / 180D MFE and MAE.
- Representative trigger deduplication.
- C15 sector/canonical shadow rule discovery.
```

Non-validation scope:

```text
- No current stock recommendation.
- No live candidate discovery.
- No broker/API/autotrading.
- No stock_agent src/e2r code opened.
- No production scoring patch.
- No global weight promotion.
- No claim that exact non-price report archive has been fully ingested.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_product_specific_spread_duration_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"POSCO/Hyundai/Poongsan show spread-specific evidence improves score-return alignment","improves missed_structural_count from 1 to 0","R4L12_C15_005490_T1|R4L12_C15_004020_T1|R4L12_C15_103140_T1",3,3,0,medium,canonical_shadow_only,"not production; requires batch ledger aggregation"
shadow_weight,C15_event_premium_exclusion_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Korea Zinc 2024 price path is event/control premium, not material-spread success","reduces false positive/misattribution risk",R4L12_C15_010130_T1,1,1,1,medium,counterexample_guard_shadow_only,"route to C32/R13 rather than C15 spread calibration"
shadow_weight,L4_high_MAE_success_quality_haircut,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+0.5,"Hyundai Steel success still carried larger MAE than POSCO/Poongsan","prevents over-ranking weak balance-sheet/high-beta spread names",R4L12_C15_004020_T1,1,1,0,low,sector_shadow_only,"not global; needs more L4 cases"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L12_C15_005490_POSCO_STEEL_SPREAD_20210426", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L12_C15_005490_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_moderate_mfe_with_later_spread_normalization", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "new symbol/new trigger family for R4/C15; family=integrated_steel_product_spread_margin_bridge"}
{"row_type": "case", "case_id": "R4L12_C15_004020_HYUNDAI_STEEL_SPREAD_20210426", "symbol": "004020", "company_name": "현대제철", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R4L12_C15_004020_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_success_requires_quality_haircut", "current_profile_verdict": "current_profile_correct_but_mae_underweighted", "price_source": "Songdaiki/stock-web", "notes": "new symbol/new trigger family for R4/C15; family=steel_spread_beta_high_mae_quality_haircut"}
{"row_type": "case", "case_id": "R4L12_C15_103140_POONGSAN_COPPER_SPREAD_20240329", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L12_C15_103140_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_with_price_only_4B_warning", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "new symbol/new trigger family for R4/C15; family=copper_nonferrous_price_spread_policy_demand_bridge"}
{"row_type": "case", "case_id": "R4L12_C15_010130_KOREA_ZINC_EVENT_PREMIUM_20240913", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R4L12_C15_010130_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_event_premium_misattribution", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "new symbol/new trigger family for R4/C15; family=event_premium_not_material_spread"}
{"row_type": "trigger", "trigger_id": "R4L12_C15_005490_T1", "case_id": "R4L12_C15_005490_POSCO_STEEL_SPREAD_20210426", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "sector": "소재·스프레드·전략자원", "primary_archetype": "material_spread_supercycle", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-04-26", "evidence_available_at_that_date": "2021년 철강 판가 상승과 수요 회복이 원재료비 부담을 흡수할 수 있는 spread/margin bridge로 인식되던 구간. POSCO는 통합 제철사라 제품 가격-원료비 스프레드가 손익으로 연결될 때 C15의 대표 positive가 된다.", "evidence_source": "stock-web OHLC rows; public historical steel-price recovery context; exact contemporaneous report URL enrichment pending", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-04-26", "entry_price": 362500, "MFE_30D_pct": 14.07, "MFE_90D_pct": 14.07, "MFE_180D_pct": 14.07, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.41, "MAE_90D_pct": -15.59, "MAE_180D_pct": -18.34, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-10", "peak_price": 413500, "drawdown_after_peak_pct": -28.42, "green_lateness_ratio": "0.24:Stage3 confirmation did not miss most of the move", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_moderate_mfe_with_later_spread_normalization", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L12_C15_005490_POSCO_STEEL_SPREAD_20210426_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L12_C15_004020_T1", "case_id": "R4L12_C15_004020_HYUNDAI_STEEL_SPREAD_20210426", "symbol": "004020", "company_name": "현대제철", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "sector": "소재·스프레드·전략자원", "primary_archetype": "material_spread_supercycle", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-04-26", "evidence_available_at_that_date": "2021년 철강 가격 상승과 자동차·건설 수요 회복 기대가 고로/전기로 제품 스프레드로 연결되던 구간. 현대제철은 POSCO보다 beta가 높고 MAE가 커서 C15 shadow rule에 quality/hard-MAE haircut가 필요함을 보여준다.", "evidence_source": "stock-web OHLC rows; historical steel product spread cycle context; exact contemporaneous report URL enrichment pending", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "profile_path": "atlas/symbol_profiles/004/004020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-04-26", "entry_price": 52000, "MFE_30D_pct": 21.15, "MFE_90D_pct": 21.15, "MFE_180D_pct": 21.15, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.88, "MAE_90D_pct": -12.98, "MAE_180D_pct": -16.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-11", "peak_price": 63000, "drawdown_after_peak_pct": -31.35, "green_lateness_ratio": "0.31:Green would be somewhat late but not useless", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_if_margin_slowdown_confirmed", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success_requires_quality_haircut", "current_profile_verdict": "current_profile_correct_but_mae_underweighted", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L12_C15_004020_HYUNDAI_STEEL_SPREAD_20210426_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L12_C15_103140_T1", "case_id": "R4L12_C15_103140_POONGSAN_COPPER_SPREAD_20240329", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "sector": "소재·스프레드·전략자원", "primary_archetype": "material_spread_supercycle", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-29", "evidence_available_at_that_date": "2024년 구리 가격 상승과 전력망·데이터센터·전기화 수요 narrative가 풍산의 구리 가공/방산 혼합 beta와 결합된 구간. 단, 구리 가격 둔화가 나타나면 full 4B는 가격만이 아니라 inventory/demand evidence를 요구해야 한다.", "evidence_source": "stock-web OHLC rows; copper rally/delay context from 2024 market sources; exact Korea-company report URL enrichment pending", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-29", "entry_price": 50500, "MFE_30D_pct": 56.24, "MFE_90D_pct": 56.24, "MFE_180D_pct": 56.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.37, "MAE_90D_pct": -6.93, "MAE_180D_pct": -6.93, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -40.43, "green_lateness_ratio": "0.18:spread-sensitive equity moved early, Green would not be too late if margin bridge confirmed", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_until_copper_inventory_demand_evidence_arrives", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_with_price_only_4B_warning", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L12_C15_103140_POONGSAN_COPPER_SPREAD_20240329_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L12_C15_010130_T1", "case_id": "R4L12_C15_010130_KOREA_ZINC_EVENT_PREMIUM_20240913", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_NONFERROUS_PRODUCT_SPREAD_SUPERCYCLE", "sector": "소재·스프레드·전략자원", "primary_archetype": "material_spread_supercycle", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test"], "trigger_type": "Stage2-FalsePositiveGuard", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "2024년 고려아연 가격 급등은 비철금속 스프레드만으로 설명되는 움직임이 아니라 control premium / tender-cap 성격이 강한 event premium이다. C15 학습에서는 이 표본을 spread success로 먹이면 안 되고, C32/R13 event-premium guard로 분리해야 한다.", "evidence_source": "stock-web OHLC rows; public event-premium context; exact tender/corporate-control URL enrichment pending", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 666000, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -1.65, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -38.72, "green_lateness_ratio": "not_applicable:not_a_material_spread_green_candidate", "four_b_local_peak_proximity": 0.47, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "event_premium_4B_not_material_spread_4B", "four_b_evidence_type": ["control_premium_or_event_premium", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break_if_routed_as_spread_thesis_break", "trigger_outcome_label": "counterexample_event_premium_misattribution", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L12_C15_010130_KOREA_ZINC_EVENT_PREMIUM_20240913_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12_C15_005490_POSCO_STEEL_SPREAD_20210426", "trigger_id": "R4L12_C15_005490_T1", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 70, "revision_score": 62, "relative_strength_score": 64, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 62, "product_specificity_score": 66, "input_cost_pass_through_score": 68, "inventory_cycle_risk_score": 22, "event_premium_exclusion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 78, "revision_score": 68, "relative_strength_score": 64, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 72, "product_specificity_score": 72, "input_cost_pass_through_score": 76, "inventory_cycle_risk_score": 22, "event_premium_exclusion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "spread_duration_score", "product_specificity_score", "input_cost_pass_through_score", "event_premium_exclusion_score"], "component_delta_explanation": "C15 shadow rewards product-specific spread duration + realized margin bridge; it penalizes event premium not supported by commodity spread evidence.", "MFE_90D_pct": 14.07, "MAE_90D_pct": -15.59, "score_return_alignment_label": "structural_success_moderate_mfe_with_later_spread_normalization", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12_C15_004020_HYUNDAI_STEEL_SPREAD_20210426", "trigger_id": "R4L12_C15_004020_T1", "symbol": "004020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 64, "revision_score": 60, "relative_strength_score": 72, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 38, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 58, "product_specificity_score": 55, "input_cost_pass_through_score": 62, "inventory_cycle_risk_score": 35, "event_premium_exclusion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 70, "revision_score": 65, "relative_strength_score": 72, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 42, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 64, "product_specificity_score": 60, "input_cost_pass_through_score": 67, "inventory_cycle_risk_score": 40, "event_premium_exclusion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/Green-buffer-shadow", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "spread_duration_score", "product_specificity_score", "input_cost_pass_through_score", "event_premium_exclusion_score"], "component_delta_explanation": "C15 shadow rewards product-specific spread duration + realized margin bridge; it penalizes event premium not supported by commodity spread evidence.", "MFE_90D_pct": 21.15, "MAE_90D_pct": -12.98, "score_return_alignment_label": "high_mae_success_requires_quality_haircut", "current_profile_verdict": "current_profile_correct_but_mae_underweighted"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12_C15_103140_POONGSAN_COPPER_SPREAD_20240329", "trigger_id": "R4L12_C15_103140_T1", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 78, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 0, "execution_risk_score": 42, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 52, "product_specificity_score": 60, "input_cost_pass_through_score": 57, "inventory_cycle_risk_score": 45, "event_premium_exclusion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 64, "revision_score": 52, "relative_strength_score": 78, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 0, "execution_risk_score": 44, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 64, "product_specificity_score": 72, "input_cost_pass_through_score": 65, "inventory_cycle_risk_score": 48, "event_premium_exclusion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow-shadow", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "spread_duration_score", "product_specificity_score", "input_cost_pass_through_score", "event_premium_exclusion_score"], "component_delta_explanation": "C15 shadow rewards product-specific spread duration + realized margin bridge; it penalizes event premium not supported by commodity spread evidence.", "MFE_90D_pct": 56.24, "MAE_90D_pct": -6.93, "score_return_alignment_label": "structural_success_with_price_only_4B_warning", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12_C15_010130_KOREA_ZINC_EVENT_PREMIUM_20240913", "trigger_id": "R4L12_C15_010130_T1", "symbol": "010130", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 88, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 82, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 20, "product_specificity_score": 22, "input_cost_pass_through_score": 0, "inventory_cycle_risk_score": 0, "event_premium_exclusion_score": 0, "positioning_overheat_score": 80, "thesis_break_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow/false-spread-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 50, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 85, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "spread_duration_score": 20, "product_specificity_score": 22, "input_cost_pass_through_score": 0, "inventory_cycle_risk_score": 0, "event_premium_exclusion_score": 95, "positioning_overheat_score": 90, "thesis_break_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage2-Watch/reroute-to-C32", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "spread_duration_score", "product_specificity_score", "input_cost_pass_through_score", "event_premium_exclusion_score"], "component_delta_explanation": "C15 shadow rewards product-specific spread duration + realized margin bridge; it penalizes event premium not supported by commodity spread evidence.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "counterexample_event_premium_misattribution", "current_profile_verdict": "current_profile_false_positive"}
{"profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "global_current_proxy", "profile_hypothesis": "current profile without C15 product-spread specificity", "changed_axes": [], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["R4L12_C15_005490_T1", "R4L12_C15_004020_T1", "R4L12_C15_103140_T1", "R4L12_C15_010130_T1"], "avg_MFE_90D_pct": 88.22, "avg_MAE_90D_pct": -9.29, "avg_MFE_180D_pct": 88.22, "avg_MAE_180D_pct": -10.94, "false_positive_rate": 0.25, "missed_structural_count": 1, "late_green_count": 1, "avg_green_lateness_ratio": "mixed", "avg_four_b_local_peak_proximity": 0.81, "avg_four_b_full_window_peak_proximity": 0.99, "score_return_alignment_verdict": "mixed; event premium can pollute C15 if not guarded"}
{"profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "weaker guard and lower thresholds overpromote relative-strength material names", "changed_axes": ["legacy_lower_thresholds"], "changed_thresholds": {"green": "legacy"}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["R4L12_C15_005490_T1", "R4L12_C15_004020_T1", "R4L12_C15_103140_T1", "R4L12_C15_010130_T1"], "avg_MFE_90D_pct": 88.22, "avg_MAE_90D_pct": -9.29, "avg_MFE_180D_pct": 88.22, "avg_MAE_180D_pct": -10.94, "false_positive_rate": 0.5, "missed_structural_count": 0, "late_green_count": 2, "avg_green_lateness_ratio": "mixed", "avg_four_b_local_peak_proximity": 0.81, "avg_four_b_full_window_peak_proximity": 0.99, "score_return_alignment_verdict": "worse: high beta and event premium are confused with spread signal"}
{"profile_id": "P1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "profile_hypothesis": "L4 materials require observable product spread duration and input-cost pass-through", "changed_axes": ["product_specific_spread_duration_bonus", "input_cost_pass_through_gate"], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["R4L12_C15_005490_T1", "R4L12_C15_004020_T1", "R4L12_C15_103140_T1", "R4L12_C15_010130_T1"], "avg_MFE_90D_pct": 88.22, "avg_MAE_90D_pct": -9.29, "avg_MFE_180D_pct": 88.22, "avg_MAE_180D_pct": -10.94, "false_positive_rate": 0.25, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "improved", "avg_four_b_local_peak_proximity": 0.81, "avg_four_b_full_window_peak_proximity": 0.99, "score_return_alignment_verdict": "better for steel/copper spread cases, still needs event-premium guard"}
{"profile_id": "P2_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C15 should distinguish real spread bridge from pure price/event rerating", "changed_axes": ["C15_spread_duration_margin_bridge_bonus", "C15_event_premium_exclusion_guard"], "changed_thresholds": {"Green": "unchanged; component-gated"}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["R4L12_C15_005490_T1", "R4L12_C15_004020_T1", "R4L12_C15_103140_T1", "R4L12_C15_010130_T1"], "avg_MFE_90D_pct": 88.22, "avg_MAE_90D_pct": -9.29, "avg_MFE_180D_pct": 88.22, "avg_MAE_180D_pct": -10.94, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "best", "avg_four_b_local_peak_proximity": 0.81, "avg_four_b_full_window_peak_proximity": 0.99, "score_return_alignment_verdict": "best candidate; prevents 고려아연 event premium from entering C15 as spread evidence"}
{"profile_id": "P3_counterexample_guard_profile", "profile_scope": "counterexample_guard", "profile_hypothesis": "control premium/tender-cap price paths are not material-spread learning rows", "changed_axes": ["reroute_event_premium_to_C32_or_R13"], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["R4L12_C15_005490_T1", "R4L12_C15_004020_T1", "R4L12_C15_103140_T1"], "avg_MFE_90D_pct": 30.49, "avg_MAE_90D_pct": -11.83, "avg_MFE_180D_pct": 30.49, "avg_MAE_180D_pct": -14.03, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "best_after_exclusion", "avg_four_b_local_peak_proximity": 0.98, "avg_four_b_full_window_peak_proximity": 0.98, "score_return_alignment_verdict": "cleaner quantitative C15 aggregate after excluding event-premium row"}
{"row_type": "residual_contribution", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 3, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["material_spread_missed_structural", "high_mae_success_quality_haircut_needed", "event_premium_misattributed_as_material_spread"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R4
completed_loop = 12
next_round = R5
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json` showed `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, `symbol_count=5414`, and shard roots under `atlas/ohlcv_tradable_by_symbol_year` / `atlas/ohlcv_raw_by_symbol_year`.
- Stock-Web schema: `atlas/schema.json` confirmed tradable columns `d,o,h,l,c,v,a,mc,s,m` and the MFE/MAE definitions.
- 005490 profile: `atlas/symbol_profiles/005/005490.json`, corporate_action_candidate_count=0. Representative rows sampled from `atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv`: entry 2021-04-26 close 362,500; observed peak 2021-05-10 high 413,500; observed 180D low 2021-10-29 low 296,000.
- 004020 profile: `atlas/symbol_profiles/004/004020.json`, corporate-action candidates ended before the 2021 calibration window. Representative rows sampled from `atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv`: entry 2021-04-26 close 52,000; observed peak 2021-05-11 high 63,000; observed 180D low 2021-10-06 low 43,250.
- 103140 profile: `atlas/symbol_profiles/103/103140.json`, corporate_action_candidate_count=0. Representative rows sampled from `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv`: entry 2024-03-29 close 50,500; observed peak 2024-05-14 high 78,900; observed post-peak low 2024-08-05 low 47,000.
- 010130 profile: `atlas/symbol_profiles/010/010130.json`, corporate_action_candidate_count=0. Representative rows sampled from `atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv`: entry 2024-09-13 close 666,000; observed event-premium peak 2024-12-06 high 2,407,000; observed next-session low 2024-12-09 near 1,475,000 in the fetched shard continuation.
- Non-price evidence enrichment remains conservative: this MD uses historical public mechanism labels and stock-web OHLC rows, but does not claim to have ingested a full report archive. It is suitable as shadow-only residual evidence, not as a production scoring patch.
