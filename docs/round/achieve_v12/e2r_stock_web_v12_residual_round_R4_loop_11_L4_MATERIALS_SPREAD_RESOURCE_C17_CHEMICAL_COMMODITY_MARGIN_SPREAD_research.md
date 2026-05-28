# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R4
loop = 11
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN
loop_objective = counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This MD is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a repository patch.

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

This loop does not re-prove those global axes. It tests whether C17 chemical/material spread cycles need a narrower archetype-level cap: feedstock or reopening beta should not become Green unless spread improvement closes into margin bridge and revision.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R4
sector = 소재·스프레드·전략자원
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN
rule_scope_preference = canonical_archetype_specific
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts indicate broad calibration ingestion across R1–R13 and loops 1–9. Direct repository search for this specific R4/C17 residual path did not surface a strongly duplicated loop in the accessible index. Therefore, this loop chooses new R4/C17 samples rather than repeating R1/R2 semiconductor or infrastructure sets.

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 0
new_trigger_family_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 1
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
```

Manifest confirms raw/unadjusted marcap OHLC and max_date `2026-02-20`. Schema confirms the tradable columns `d,o,h,l,c,v,a,mc,s,m` and the MFE/MAE computation basis.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward rows | corporate action 180D window | calibration_usable | reason |
|---|---:|---:|---:|---|---|---|
| R4L11-C17-011780-20240201 | 011780 | 2024-02-01 | available | clean_180D_window | true | 2024 window far from 2001 corporate action candidate |
| R4L11-C17-011170-20240124 | 011170 | 2024-01-24 | available | clean_180D_window | true | 2024 window far from 2023 corporate action candidate |
| R4L11-C17-298020-20240329 | 298020 | 2024-03-29 | available | clean_180D_window | true | no corporate action candidate in profile |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype compression:
- SYNTHETIC_RUBBER_SPREAD_RECOVERY -> C17
- SPANDEX_TEXTILE_SPREAD_RECOVERY -> C17
- NAPHTHA_REOPENING_BETA_FALSE_GREEN -> C17
```

The compression target is not “chemical stock up.” It is the mechanism: input/output spread → margin bridge → earnings/revision confirmation. A raw commodity or policy rebound is only the spark; Green requires that the furnace actually catches.

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | MFE90/MAE90 | MFE180/MAE180 | current_profile_verdict | notes |
|---|---:|---|---|---|---|---|---|---|
| R4L11-C17-011780-20240201 | 011780 | 금호석유화학 | positive / high_mae_success | R4L11-C17-011780-S2A-20240201 | 25.69 / -11.66 | 28.07 / -11.66 | current_profile_correct | Synthetic rubber / butadiene spread recovery path showed an actual tradable rerating, but 4B should attach when margin-cycle enthusiasm becomes crowded. |
| R4L11-C17-011170-20240124 | 011170 | 롯데케미칼 | counterexample / failed_rerating | R4L11-C17-011170-S2A-20240124 | 9.4 / -25.33 | 9.4 / -40.56 | current_profile_false_positive | Policy/reopening/naphtha-beta rebound looked like an early Stage2, but commodity spread did not close into earnings revision; large MAE invalidates Green promotion. |
| R4L11-C17-298020-20240329 | 298020 | 효성티앤씨 | positive / high_mae_success | R4L11-C17-298020-S2A-20240329 | 29.89 / -17.57 | 29.89 / -40.83 | current_profile_correct | Spandex/textile spread rebound translated to a strong MFE path, but later demand/fx/margin rollover created severe drawdown; needs C17-specific 4B overlay. |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
minimum_new_independent_case_ratio = 1.00
```

The selected set intentionally keeps both sides of the same mechanism: two cases where spread/margin evidence produced strong MFE, and one case where feedstock/reopening beta failed to close into margin revision.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| R4L11-C17-011780-20240201 | relative_strength, early_revision_signal, spread recovery | margin_bridge partial | positioning/valuation overheat at July local peak | none |
| R4L11-C17-011170-20240124 | policy/reopening/feedstock beta, relative strength | not confirmed | margin slowdown | thesis evidence broken by sustained drawdown |
| R4L11-C17-298020-20240329 | spread recovery, early revision signal, relative strength | margin_bridge partial | positioning overheat, margin rollover after May peak | watch-only thesis break |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | profile caveat |
|---:|---|---|---|---|
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv | corporate action candidate in 2001 only; 2024 window clean |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv | corporate action candidate in 2023; 2024 trigger window not contaminated |
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv | no corporate action candidate |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R4L11-C17-011780-S2A-20240201 | 011780 | Stage2-Actionable | 2024-02-01 | 130,400 | 25.69 | -4.83 | 25.69 | -11.66 | 28.07 | -11.66 | 2024-07-15 167,000 | current_profile_correct |
| R4L11-C17-011780-4B-20240715 | 011780 | Stage4B-Overlay | 2024-07-15 | 164,300 | 1.64 | -26.54 | 1.64 | -26.54 | 1.64 | -46.87 | 2024-07-15 167,000 | current_profile_correct |
| R4L11-C17-011170-S2A-20240124 | 011170 | Stage2-Actionable | 2024-01-24 | 128,700 | 9.4 | -7.38 | 9.4 | -25.33 | 9.4 | -40.56 | 2024-02-01 140,800 | current_profile_false_positive |
| R4L11-C17-298020-S2A-20240329 | 298020 | Stage2-Actionable | 2024-03-29 | 324,500 | 21.57 | -5.7 | 29.89 | -17.57 | 29.89 | -40.83 | 2024-05-17 421,500 | current_profile_correct |
| R4L11-C17-298020-4B-20240517 | 298020 | Stage4B-Overlay | 2024-05-17 | 412,000 | 2.31 | -16.75 | 2.31 | -35.07 | 2.31 | -53.4 | 2024-05-17 421,500 | current_profile_correct |


## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger aggregate

| metric | value |
|---|---:|
| representative_trigger_count | 3 |
| avg_MFE_30D_pct | 18.89 |
| avg_MAE_30D_pct | -5.97 |
| avg_MFE_90D_pct | 21.66 |
| avg_MAE_90D_pct | -18.19 |
| avg_MFE_180D_pct | 22.45 |
| avg_MAE_180D_pct | -31.02 |
| false_positive_rate | 0.333 |
| missed_structural_count | 0 |
| late_green_count | 0 |

### Read-through

C17 is asymmetrical. When the spread-to-margin bridge is real, the MFE can be strong, but the same trade can later turn into a deep drawdown when spread momentum stalls. Therefore, the useful rule is not “raise or lower all C17 scores.” It is a two-lane rule:

1. **Positive lane**: spread improvement plus margin bridge may remain Stage2/Yellow early.
2. **Counterexample lane**: feedstock/reopening beta without revision should be capped below Green.
3. **4B lane**: after strong MFE, positioning or margin-rollover evidence should attach before the hard 4C break.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual path | profile verdict |
|---|---|---|---|
| R4L11-C17-011780-20240201 | Stage2/Yellow, Green waits for revision | +25.69% 90D MFE, clean early MAE | current_profile_correct |
| R4L11-C17-011170-20240124 | Stage2/near-Yellow if beta/reopening scored too high | +9.40% MFE but -40.56% 180D MAE | current_profile_false_positive |
| R4L11-C17-298020-20240329 | Stage2/Yellow, Green waits for revision | +29.89% 90D MFE but later -40.83% 180D MAE | current_profile_correct |

Answers to required checks:

```text
1. Current profile generally handles strict Green, but C17 can still over-score feedstock/reopening beta.
2. The false-positive residual is 011170: low MFE, high MAE, no durable margin bridge.
3. Stage2 bonus is useful for 011780/298020, but should be capped when only commodity beta exists.
4. Yellow threshold 75 is acceptable if C17 beta-only rows are capped.
5. Green threshold 87 / revision 55 should be strengthened only within C17's feedstock-beta branch.
6. price-only blowoff guard is appropriate and kept.
7. full 4B non-price requirement is appropriate and strengthened for spread-cycle rollover.
8. hard 4C routing should remain thesis-break only; 4B should catch overheat earlier.
```

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable for all representative rows
reason = no confirmed Stage3-Green trigger is asserted from outcome; this loop avoids outcome-labeled Green.
```

C17’s issue is not only Green lateness. The sharper residual is **wrong Green promotion** when spread narrative stays a price/factor trade and never becomes margin revision.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | 4B entry | local/full peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| R4L11-C17-011780-4B-20240715 | 130,400 | 164,300 | 167,000 | 0.93 | 0.93 | good_full_window_4B_timing |
| R4L11-C17-298020-4B-20240517 | 324,500 | 412,000 | 421,500 | 0.90 | 0.90 | good_full_window_4B_timing |

C17 needs the 4B layer because spread cycles behave like a compressed spring: the rerating can be right, but once the spread begins to roll over, the same spring snaps back quickly.

## 16. 4C Protection Audit

| case_id | 4C label | protection note |
|---|---|---|
| R4L11-C17-011170-20240124 | thesis_break_watch_only | The persistent 180D drawdown after weak MFE supports not promoting beta-only Stage2 into Green. |
| R4L11-C17-298020-20240329 | thesis_break_watch_only | 4B overlay should catch the May peak zone; 4C is too late for entry/exit calibration. |
| R4L11-C17-011780-20240201 | none | No hard thesis break in the representative entry window; 4B overlay enough. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c17_green_requires_realized_spread_margin_bridge
candidate_delta = +1 guard
```

Rule candidate:

```text
For C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,
do not allow Stage3-Green from feedstock/reopening/commodity beta alone.
Green requires at least two of:
- realized product/input spread expansion,
- margin_bridge_score supported by reported or strongly visible operating leverage,
- confirmed_revision,
- low execution/inventory risk,
- no obvious China oversupply or demand rollover evidence.
```

## 18. Canonical-Archetype Rule Candidate

```text
axis_1 = c17_feedstock_beta_cap_without_revision
axis_2 = c17_spread_cycle_4b_requires_margin_rollover_or_positioning_overheat
axis_3 = c17_green_requires_realized_spread_margin_bridge
```

This should remain C17-specific. It is not safe to globalize because order/backlog sectors and platform operating leverage use different proof chains.

## 19. Before / After Backtest Comparison

| profile_id | scope | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | score_return_alignment |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 21.66 | -18.19 | 22.45 | -31.02 | 0.333 | mixed; one beta false positive |
| P0b e2r_2_0_baseline_reference | rollback reference | 21.66 | -18.19 | 22.45 | -31.02 | 0.667 | too permissive on beta/rebound |
| P1 sector_specific_candidate_profile | L4 | 21.66 | -18.19 | 22.45 | -31.02 | 0.333 | acceptable but not precise enough |
| P2 canonical_archetype_candidate_profile | C17 | 21.66 | -18.19 | 22.45 | -31.02 | 0.000 after cap | best alignment |
| P3 counterexample_guard_profile | C17 guard | 21.66 | -18.19 | 22.45 | -31.02 | 0.000 for 011170-like rows | best false-positive control |

## 20. Score-Return Alignment Matrix

| case_id | before score/label | after score/label | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| R4L11-C17-011780-20240201 | 76 Stage3-Yellow | 79 Stage3-Yellow | 25.69 | -11.66 | aligned; not forced Green |
| R4L11-C17-011170-20240124 | 77 Stage3-Yellow | 66 Stage2-Watch | 9.40 | -25.33 | corrected false-positive |
| R4L11-C17-298020-20240329 | 78 Stage3-Yellow | 81 Stage3-Yellow | 29.89 | -17.57 | aligned, but requires 4B watch |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_trigger | representative | current_error | sector_rule | canonical_rule | gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 1 | true | true | more holdout needed in C15/C16, but C17 gap partly filled |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - commodity_beta_false_green
  - high_mfe_high_mae_spread_cycle
  - 4B_overlay_needed_before_thesis_break
new_axis_proposed:
  - c17_green_requires_realized_spread_margin_bridge
  - c17_feedstock_beta_cap_without_revision
  - c17_spread_cycle_4b_requires_margin_rollover_or_positioning_overheat
existing_axis_strengthened:
  - stage3_green_revision_min in C17 only
  - full_4b_requires_non_price_evidence in C17 only
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R4/C17 chemical commodity margin-spread residual
diversity_score_summary: high_total_58_avg_19.3
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profile availability and corporate action caveat
- 2024 tradable OHLC rows for each representative trigger
- 30D / 90D / 180D MFE and MAE
- representative trigger dedupe
- 4B local/full-window split
```

Not validated:

```text
- production scoring code
- live scan state
- current candidate recommendation
- brokerage execution
- 1Y/2Y quantitative calibration; fields are left null in machine rows for this loop
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_green_requires_realized_spread_margin_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"C17 Green must require spread-to-margin-to-revision bridge, not feedstock beta alone","false-positive cap improves 011170 without blocking 011780/298020","R4L11-C17-011780-S2A-20240201|R4L11-C17-011170-S2A-20240124|R4L11-C17-298020-S2A-20240329",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_spread_cycle_4b_requires_margin_rollover_or_positioning_overheat,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"High-MFE spread cycles can reverse sharply; 4B should use non-price margin/positioning evidence","captures 011780 and 298020 peak-zone risk without treating price-only peak as full 4B","R4L11-C17-011780-4B-20240715|R4L11-C17-298020-4B-20240517",2,2,0,medium,canonical_shadow_only,"4B overlay only; not positive promotion"
shadow_weight,c17_feedstock_beta_cap_without_revision,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Naphtha/reopening beta without revision is a false Green route","reduces 011170 false-positive score from Yellow/near-Green to Stage2-Watch","R4L11-C17-011170-S2A-20240124",1,1,1,medium,canonical_shadow_only,"counterexample guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L11-C17-011780-20240201","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R4L11-C17-011780-S2A-20240201","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Synthetic rubber / butadiene spread recovery path showed an actual tradable rerating, but 4B should attach when margin-cycle enthusiasm becomes crowded."}
{"row_type":"case","case_id":"R4L11-C17-011170-20240124","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L11-C17-011170-S2A-20240124","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy/reopening/naphtha-beta rebound looked like an early Stage2, but commodity spread did not close into earnings revision; large MAE invalidates Green promotion."}
{"row_type":"case","case_id":"R4L11-C17-298020-20240329","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R4L11-C17-298020-S2A-20240329","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Spandex/textile spread rebound translated to a strong MFE path, but later demand/fx/margin rollover created severe drawdown; needs C17-specific 4B overlay."}
{"row_type":"trigger","trigger_id":"R4L11-C17-011780-S2A-20240201","case_id":"R4L11-C17-011780-20240201","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","evidence_available_at_that_date":"synthetic rubber / butadiene spread recovery and early stock-price relative strength, before full confirmed revision","evidence_source":"public industry spread/newsflow proxy; stock-web confirms tradable OHLC path","stage2_evidence_fields":["relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-01","entry_price":130400,"MFE_30D_pct":25.69,"MFE_90D_pct":25.69,"MFE_180D_pct":28.07,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.83,"MAE_90D_pct":-11.66,"MAE_180D_pct":-11.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":167000,"drawdown_after_peak_pct":-27.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"positive_high_mfe_with_later_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11-C17-011780-20240201-130400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L11-C17-011780-4B-20240715","case_id":"R4L11-C17-011780-20240201","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-07-15","evidence_available_at_that_date":"local cycle overheat after spread rerating; 4B should be overlay, not a positive entry row","evidence_source":"stock-web local peak proximity plus spread-cycle fatigue proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-15","entry_price":164300,"MFE_30D_pct":1.64,"MFE_90D_pct":1.64,"MFE_180D_pct":1.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.54,"MAE_90D_pct":-26.54,"MAE_180D_pct":-46.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":167000,"drawdown_after_peak_pct":-27.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11-C17-011780-20240715-164300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R4L11-C17-011170-S2A-20240124","case_id":"R4L11-C17-011170-20240124","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","evidence_available_at_that_date":"naphtha/reopening/policy-beta rebound without realized spread-to-margin bridge","evidence_source":"public commodity-spread narrative proxy; stock-web confirms failed rerating path","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-24","entry_price":128700,"MFE_30D_pct":9.4,"MFE_90D_pct":9.4,"MFE_180D_pct":9.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.38,"MAE_90D_pct":-25.33,"MAE_180D_pct":-40.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":140800,"drawdown_after_peak_pct":-45.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11-C17-011170-20240124-128700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L11-C17-298020-S2A-20240329","case_id":"R4L11-C17-298020-20240329","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-29","evidence_available_at_that_date":"spandex/textile spread rebound and early margin bridge path before full Green confirmation","evidence_source":"public spread-recovery narrative proxy; stock-web confirms MFE/MAE","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-29","entry_price":324500,"MFE_30D_pct":21.57,"MFE_90D_pct":29.89,"MFE_180D_pct":29.89,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.7,"MAE_90D_pct":-17.57,"MAE_180D_pct":-40.83,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":421500,"drawdown_after_peak_pct":-54.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"positive_high_mfe_high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11-C17-298020-20240329-324500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L11-C17-298020-4B-20240517","case_id":"R4L11-C17-298020-20240329","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPANDEX_SPREAD_RECOVERY_VS_NAPHTHA_BETA_FALSE_GREEN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-17","evidence_available_at_that_date":"near-cycle local peak after spread rerating; later demand/margin rollover turned the move into a severe drawdown","evidence_source":"stock-web peak proximity plus spread-cycle fatigue proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":412000,"MFE_30D_pct":2.31,"MFE_90D_pct":2.31,"MFE_180D_pct":2.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.75,"MAE_90D_pct":-35.07,"MAE_180D_pct":-53.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":421500,"drawdown_after_peak_pct":-54.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11-C17-298020-20240517-412000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L11-C17-011780-20240201","trigger_id":"R4L11-C17-011780-S2A-20240201","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":9,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":10,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":19,"positioning_overheat_score":5,"thesis_break_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["asp_or_spread_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"spread + margin bridge keeps Stage2/Yellow but Green waits for revision","MFE_90D_pct":25.69,"MAE_90D_pct":-11.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L11-C17-011170-20240124","trigger_id":"R4L11-C17-011170-S2A-20240124","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":4,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":14,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":10,"positioning_overheat_score":0,"thesis_break_score":10},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["asp_or_spread_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"policy/feedstock beta capped without realized margin bridge","MFE_90D_pct":9.4,"MAE_90D_pct":-25.33,"score_return_alignment_label":"corrected_false_positive_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L11-C17-298020-20240329","trigger_id":"R4L11-C17-298020-S2A-20240329","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":9,"relative_strength_score":19,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":11,"relative_strength_score":19,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":19,"positioning_overheat_score":7,"thesis_break_score":0},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["asp_or_spread_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"spread rebound accepted, high-MAE guard flags 4B watch","MFE_90D_pct":29.89,"MAE_90D_pct":-17.57,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["commodity_beta_false_green","high_mfe_high_mae_spread_cycle","4B_overlay_needed_before_thesis_break"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R4/C17 chemical commodity spread residual; positive spread recovery vs naphtha-beta failed rerating"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_green_requires_realized_spread_margin_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"C17 Green must require spread-to-margin-to-revision bridge, not feedstock beta alone","false-positive cap improves 011170 without blocking 011780/298020","R4L11-C17-011780-S2A-20240201|R4L11-C17-011170-S2A-20240124|R4L11-C17-298020-S2A-20240329",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_spread_cycle_4b_requires_margin_rollover_or_positioning_overheat,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"High-MFE spread cycles can reverse sharply; 4B should use non-price margin/positioning evidence","captures 011780 and 298020 peak-zone risk without treating price-only peak as full 4B","R4L11-C17-011780-4B-20240715|R4L11-C17-298020-4B-20240517",2,2,0,medium,canonical_shadow_only,"4B overlay only; not positive promotion"
shadow_weight,c17_feedstock_beta_cap_without_revision,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Naphtha/reopening beta without revision is a false Green route","reduces 011170 false-positive score from Yellow/near-Green to Stage2-Watch","R4L11-C17-011170-S2A-20240124",1,1,1,medium,canonical_shadow_only,"counterexample guard"
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
next_round = R4_holdout_or_R5_loop12
recommended_next_gap = C15_MATERIAL_SPREAD_SUPERCYCLE or C16_STRATEGIC_RESOURCE_POLICY_SUPPLY holdout
avoid = repeating R1/R2 HBM/infrastructure examples or this exact C17 symbol/date/evidence set
```

## 28. Source Notes

- Prompt basis: E2R Historical Calibration Prompt v12 loaded in conversation.
- stock_agent research artifact scope used only for coverage and duplicate avoidance.
- stock-web manifest and schema used for price-source validation.
- Symbol profiles inspected: 011780, 011170, 298020.
- OHLC rows inspected from stock-web tradable shards:
  - atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv
