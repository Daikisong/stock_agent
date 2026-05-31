# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

- output_file: `e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md`
- scheduled_round: `R1`
- scheduled_loop: `10`
- completed_round: `R1`
- completed_loop: `10`
- next_round: `R2`
- next_loop: `10`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C02_POWER_GRID_DATACENTER_CAPEX`
- fine_archetype_focus: `GRID_TRANSFORMER_EXPORT_BACKLOG_MARGIN_BRIDGE | US_TRANSFORMER_BACKLOG_MARGIN_BRIDGE | GRID_DATACENTER_RELATIVE_STRENGTH_WITH_HIGH_MAE | SMALL_ELECTRICAL_GRID_THEME_PRICE_ONLY`
- loop_objective: `coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test`
- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- previous_baseline_reference: `e2r_2_0_baseline`

This loop adds 4 new independent cases, 2 counterexamples, and 1 current-profile residual error for `R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX`.

## 1. Current Calibrated Profile Assumption

Applied global calibration is treated as already active and is not re-proposed:

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

This MD only tests whether C02 needs a narrower canonical-archetype shadow rule. The proposed rule does not loosen Green. It adds a bridge requirement around `backlog_visibility_score`, `margin_bridge_score`, and `revision_score` for C02 power-grid/data-center capex rerating.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R1 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX |
| allowed sector pair | pass |
| reason for selection | R1 loop 10 is missing in visible v12 filename registry; C02 appears as a canonical archetype but was not visible as a dedicated runtime archetype row in the current v2.2 profile snapshot reviewed earlier. |

## 3. Previous Coverage / Duplicate Avoidance Check

Visible `docs/round` filenames show v12 files beginning at loop 10 for R5~R13, many invalid R13-sector pair files, and later R3-only loop 61~71 files. The corrected scheduler therefore resolves the lowest incomplete loop first.

```text
lowest_visible_incomplete_loop = 10
first_missing_round_in_that_loop = R1
scheduled_round = R1
scheduled_loop = 10
```

Duplicate avoidance policy used here:

```text
same canonical_archetype_id = allowed
same symbol + same trigger_date + same entry_date = avoided
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
```

The HD현대일렉트릭 4B overlay reuses the symbol but tests a different trigger family and is not counted as a new independent case.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| validation_status | usable_for_historical_calibration |

The stock-web manifest reports raw/unadjusted FinanceData/marcap OHLC, excludes zero-volume/invalid OHLC rows from tradable calibration shards, and uses `2026-02-20` as max_date. The schema defines the MFE/MAE formulas used below.

## 5. Historical Eligibility Gate

| symbol | profile_path | first_date | last_date | corporate_action_candidate_dates in tested 180D window | 180D usable |
|---|---|---:|---:|---|---|
| 267260 | atlas/symbol_profiles/267/267260.json | 2017-05-10 | 2026-02-20 | none in 2023-04-25~2024-01 window | true |
| 298040 | atlas/symbol_profiles/298/298040.json | 2018-07-13 | 2026-02-20 | none | true |
| 010120 | atlas/symbol_profiles/010/010120.json | 1995-05-02 | 2026-02-20 | none in 2024 window | true |
| 017040 | atlas/symbol_profiles/017/017040.json | 1995-05-02 | 2026-02-20 | none in 2024 window | true |

Historical eligibility result:

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4 representative + 1 overlay
forward_window_minimum = 180 trading days
price_source_fields_present = true
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| GRID_TRANSFORMER_EXPORT_BACKLOG_MARGIN_BRIDGE | C02_POWER_GRID_DATACENTER_CAPEX | Transformer/grid capex beneficiary with backlog + margin bridge. |
| US_TRANSFORMER_BACKLOG_MARGIN_BRIDGE | C02_POWER_GRID_DATACENTER_CAPEX | U.S. transformer demand and delivery visibility. |
| GRID_DATACENTER_RELATIVE_STRENGTH_WITH_HIGH_MAE | C02_POWER_GRID_DATACENTER_CAPEX | Data-center/grid theme had MFE but also high MAE when bridge evidence lagged. |
| SMALL_ELECTRICAL_GRID_THEME_PRICE_ONLY | C02_POWER_GRID_DATACENTER_CAPEX | Price-only theme participation without durable backlog or margin evidence. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | new independent? | current_profile_verdict |
|---|---:|---|---|---|---|---:|---|---|
| R1L10_C02_HDHE_20230424 | 267260 | HD현대일렉트릭 | structural_success | Stage2-Actionable | 2023-04-25 | 53,000 | true | current_profile_correct |
| R1L10_C02_HYOSUNG_20230728 | 298040 | 효성중공업 | structural_success | Stage2-Actionable | 2023-07-31 | 174,500 | true | current_profile_correct |
| R1L10_C02_LS_20240429 | 010120 | LS ELECTRIC | high_mae_success | Stage2-Actionable | 2024-04-30 | 176,600 | true | current_profile_too_early |
| R1L10_C02_KWANGMYUNG_20240507 | 017040 | 광명전기 | price_moved_without_evidence | price-only | 2024-05-07 | 3,185 | true | current_profile_correct |
| R1L10_C02_HDHE_20240412_4B | 267260 | HD현대일렉트릭 | 4B_too_early | Stage4B overlay | 2024-04-12 | 235,000 | false | current_profile_correct |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | HD현대일렉트릭, 효성중공업 |
| counterexample_or_failed_rerating | 2 | LS ELECTRIC high-MAE path, 광명전기 price-only collapse |
| 4B_or_4C_case | 1 | HD현대일렉트릭 local 4B too early |
| calibration_usable_case_count | 4 | all representative cases |
| new_independent_case_ratio | 1.00 | 4/4 representative cases |

Balance verdict:

```text
positive_case_count = 2
counterexample_count = 2
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

## 9. Evidence Source Map

This MD uses historical evidence proxies for event timing and uses stock-web only for price path validation.

| case | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| HD현대일렉트릭 2023 | disclosure/research proxy for transformer/export demand, backlog/delivery visibility, margin bridge | revision and margin bridge later confirmed | none in representative trigger | none |
| 효성중공업 2023 | results/research proxy for heavy electrical equipment and transformer demand | later margin/revision confirmation | none in representative trigger | none |
| LS ELECTRIC 2024 | grid/data-center theme + relative strength + policy optionality | partial revision support, but bridge was not strong enough for clean Green | local price overheat | none |
| 광명전기 2024 | relative strength only | none | price-only local peak | none |
| HD현대일렉트릭 2024 4B | none | none | valuation/positioning local peak without non-price slowdown | none |

## 10. Price Data Source Map

| symbol | price_shard_path | cited row windows used |
|---:|---|---|
| 267260 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv; 2024.csv | 2023-04-25 entry, 2023-05~2024-04 highs/lows |
| 298040 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2023.csv; 2024.csv | 2023-07-31 entry, 2023-08~2024-04 highs/lows |
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | 2024-04-30 entry, 2024-05~2024-12 highs/lows |
| 017040 | atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv | 2024-05-07 entry, 2024-05~2024-12 highs/lows |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_type | trigger_date | entry_date | entry_price | evidence_source | representative? |
|---|---|---:|---:|---:|---|---|
| R1L10_C02_HDHE_20230424 | Stage2-Actionable | 2023-04-24 | 2023-04-25 | 53,000 | disclosure/research proxy + stock-web price | yes |
| R1L10_C02_HYOSUNG_20230728 | Stage2-Actionable | 2023-07-28 | 2023-07-31 | 174,500 | disclosure/research proxy + stock-web price | yes |
| R1L10_C02_LS_20240429 | Stage2-Actionable | 2024-04-29 | 2024-04-30 | 176,600 | theme/revision proxy + stock-web price | yes |
| R1L10_C02_KWANGMYUNG_20240507 | price_moved_without_evidence | 2024-05-07 | 2024-05-07 | 3,185 | price-only theme + stock-web price | yes |
| R1L10_C02_HDHE_LOCAL_4B_20240412 | Stage4B | 2024-04-12 | 2024-04-12 | 235,000 | price/valuation local overheat + stock-web price | no, overlay only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger table

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 267260 | 2023-04-25 | 53,000 | 3.77% | -14.91% | 58.49% | -14.91% | 81.89% | -14.91% | 400.94% | -14.91% | 2024-04-12 | 265,500 | -24.67% |
| 298040 | 2023-07-31 | 174,500 | 19.20% | -11.12% | 26.93% | -12.44% | 104.58% | -12.44% | 104.58% | -12.44% | 2024-04-15 | 357,000 | -26.89% |
| 010120 | 2024-04-30 | 176,600 | 38.17% | -9.91% | 55.44% | -19.71% | 55.44% | -28.54% | 55.44% | -28.54% | 2024-07-24 | 274,500 | -54.03% |
| 017040 | 2024-05-07 | 3,185 | 4.24% | -32.03% | 4.24% | -51.33% | 4.24% | -60.75% | 4.24% | -60.75% | 2024-05-08 | 3,320 | -62.35% |

### 12.2 Aggregate representative path

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 36.27
avg_MAE_90D_pct = -24.6
avg_MFE_180D_pct = 61.54
avg_MAE_180D_pct = -29.16
false_positive_rate = 0.25
current_profile_error_count = 1
```

## 13. Current Calibrated Profile Stress Test

| case | current calibrated profile judgment | path result | verdict |
|---|---|---|---|
| HD현대일렉트릭 | Stage2-Actionable/Yellow acceptable; Green should wait for stronger revision | strong MFE and controlled MAE after early drawdown | current_profile_correct |
| 효성중공업 | Stage2-Actionable acceptable; Green after margin/revision confirmation | strong 180D path | current_profile_correct |
| LS ELECTRIC | likely Yellow/Actionable too quickly from relative strength + theme | high MFE but MAE90 -19.71 and MAE180 -28.54 | current_profile_too_early |
| 광명전기 | price-only guard should block positive stage | MFE90 4.24 vs MAE90 -51.33 | current_profile_correct |
| HD현대일렉트릭 4B overlay | full 4B should not trigger from price-only local peak | later full-window extension invalidates full 4B | current_profile_correct |

Answers to required stress-test questions:

```text
1. current profile: mostly correct, but LS ELECTRIC shows a high-MAE residual when C02 relative strength runs ahead of bridge evidence.
2. actual MFE/MAE: positives had MFE180 above 80%; price-only counterexample had MAE180 below -60%.
3. Stage2 bonus: useful only with non-price backlog/margin bridge; too generous if applied to relative-strength-only grid themes.
4. Yellow 75: too early for LS-like cases when bridge evidence is thin.
5. Green 87 / revision 55: kept; do not loosen.
6. price-only blowoff guard: kept and strengthened in C02 language.
7. full 4B non-price requirement: kept; C02 needs explicit slowdown before full 4B.
8. hard 4C routing: not directly tested in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

C02 behaves like a long transformer being loaded onto a ship: early evidence matters, but the heavy object is not truly moving until backlog, delivery, and margin bridge all line up.

| comparison | finding |
|---|---|
| Stage2-Actionable vs Green | Stage2-Actionable can be early and useful for HD현대일렉트릭/효성중공업. |
| Yellow threshold | Yellow is acceptable only when non-price bridge exists. |
| Green threshold | Green should remain strict; this loop does not support lower Green thresholds. |
| residual issue | LS ELECTRIC shows relative-strength and policy/theme evidence can arrive before a clean backlog/margin bridge, causing high MAE. |

```text
green_lateness_ratio = not_applicable for representative Stage2 triggers
reason = no separate confirmed Stage3-Green trigger row selected for this loop
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R1L10_C02_HDHE_LOCAL_4B_20240412 | 0.86 | 0.19 | valuation_blowoff / price_only_local_peak / positioning_overheat | price_only_local_4B_too_early |

Interpretation:

```text
if local proximity is high but full-window proximity is low:
    four_b_timing_verdict = price_only_local_4B_too_early

if price-only local peak has no non-price slowdown evidence:
    do_not_treat_as_full_4B = true
```

The C02-specific 4B rule should keep local price-only overheat as watch-only until revision slowdown, order slowdown, margin/backlog deterioration, or non-price overhang appears.

## 16. 4C Protection Audit

No hard 4C trigger is selected as a representative row in this loop.

```text
four_c_protection_label = not_tested
reason = C02 loop focused on Stage2 bridge, price-only false positives, and 4B local-vs-full-window timing.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate_axis = L1_power_grid_non_price_bridge_required
proposal_type = shadow_only
```

Candidate rule:

```text
For L1 power-grid/data-center capex beneficiaries, Stage2-Actionable evidence may receive credit only when at least two non-price families are present:
- backlog_or_delivery_visibility
- margin_bridge
- early_revision_signal
- customer_or_order_quality
- capacity_or_volume_route
- policy_or_regulatory_optionality connected to actual capex/order conversion

Relative strength alone cannot promote Stage2/Stage3.
```

Backtest rationale:

```text
positive cases: HD현대일렉트릭, 효성중공업
counterexamples: LS ELECTRIC high-MAE path, 광명전기 price-only collapse
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
candidate_axis = c02_non_price_backlog_margin_bridge_required
proposal_type = shadow_only
confidence = medium
```

Candidate rule:

```text
if canonical_archetype_id == C02_POWER_GRID_DATACENTER_CAPEX:
    if relative_strength_score >= 75
       and backlog_visibility_score < 60
       and margin_bridge_score < 55
       and revision_score < 55:
           cap stage at Stage2-watch or Stage2, not Stage3-Yellow/Green

    if price_only_local_peak and no non_price_slowdown:
           four_b_timing_verdict = price_only_local_4B_too_early
           do_not_treat_as_full_4B = true
```

Existing global axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_tested / existing_axis_strengthened_for_C02_bridge_only
stage3_yellow_total_min = existing_axis_tested / existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_strengthened_for_C02_local_peak
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | 4 | 36.27% | -24.6% | 61.54% | -29.16% | 25% | good but high-MAE residual remains |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | 36.27% | -24.6% | 61.54% | -29.16% | 25% | weaker Stage2 bridge distinction |
| P1 sector_specific_candidate_profile | L1 non-price bridge | 4 | 36.27% | -24.6% | 61.54% | -29.16% | lower expected | improves interpretability |
| P2 canonical_archetype_candidate_profile | C02 backlog/margin bridge required | 4 | 36.27% | -24.6% | 61.54% | -29.16% | lower expected | best candidate |
| P3 counterexample_guard_profile | price-only/high-MAE guard | 2 counterexamples | 29.84% | -35.52% | 29.84% | -44.65% | lower expected | useful as guard overlay |

## 20. Score-Return Alignment Matrix

| case | weighted_before | stage_before | weighted_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| HD현대일렉트릭 | 76 | Stage2-Actionable | 82 | Stage3-Yellow | 58.49 | -14.91 | aligned positive |
| 효성중공업 | 74 | Stage2-Actionable | 80 | Stage3-Yellow | 26.93 | -12.44 | aligned positive |
| LS ELECTRIC | 75 | Stage3-Yellow | 69 | Stage2-watch | 55.44 | -19.71 | high-MAE residual reduced |
| 광명전기 | 54 | Stage1/weak-watch | 42 | Stage1/weak-watch | 4.24 | -51.33 | price-only false positive blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed | 2 | 2 | 1 | 0 | 4 | 1 | 5 | 4 | 1 | true | true | C02 now has positive/counterexample balance; 4C still untested |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R1L10_C02_HDHE_20240412_4B
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - high_MAE_relative_strength_without_backlog_bridge
  - price_only_grid_theme_false_positive
  - price_only_local_4B_too_early
new_axis_proposed: null
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus strengthened only when C02 backlog/margin bridge exists
  - full_4b_requires_non_price_evidence strengthened for C02 local peak
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema/profile/shard path existence
- entry rows visible in tradable shards
- 30D/90D/180D MFE/MAE for representative triggers
- 4B local-vs-full-window concept on HD현대일렉트릭 overlay
- positive/counterexample balance
```

Not validated:

```text
- production scoring code
- live current candidates
- brokerage/API execution
- exact analyst report text parsing
- global rule promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c02_non_price_backlog_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,not_explicit,require_backlog_or_margin_bridge_for_stage2_bonus,+guardrail,"Positive cases had backlog/margin bridge; counterexamples had relative strength without durable bridge and showed high MAE or collapse.","representative avg MFE90 36.27 / avg MAE90 -24.6; price-only counterexample MAE180 -60.75","R1L10_C02_HDHE_STAGE2A_20230424|R1L10_C02_HYOSUNG_STAGE2A_20230728|R1L10_C02_LS_HIGH_MAE_20240429|R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507",4,4,2,medium,canonical_archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c02_price_only_local_4b_watch_only,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,full_4b_requires_non_price_evidence=true,keep_price_only_local_peak_as_watch_only_even_when_local_proximity_high,+specificity,"local price-only 4B can be too early in full-window terms","local proximity 0.86 vs full-window proximity 0.19","R1L10_C02_HDHE_LOCAL_4B_20240412",1,0,1,low_medium,canonical_archetype_shadow_only,"4B overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L10_C02_HDHE_20230424", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_EXPORT_BACKLOG_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L10_C02_HDHE_STAGE2A_20230424", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_rerating_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2023-04 results/backlog/revision proxy: transformer/export demand and margin bridge became visible before the full 2024 rerating."}
{"row_type": "case", "case_id": "R1L10_C02_HYOSUNG_20230728", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_TRANSFORMER_BACKLOG_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_rerating_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2023-07 results/research proxy: heavy electrical equipment demand and transformer backlog translated into price-confirmed rerating."}
{"row_type": "case", "case_id": "R1L10_C02_LS_20240429", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_DATACENTER_RELATIVE_STRENGTH_WITH_HIGH_MAE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R1L10_C02_LS_HIGH_MAE_20240429", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "2024-04 power-grid/data-center theme and relative strength were visible, but the later path showed high MAE before durable confirmation."}
{"row_type": "case", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "SMALL_ELECTRICAL_GRID_THEME_PRICE_ONLY", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024-05 grid/electrical equipment theme price spike without sufficient backlog, margin bridge, or durable customer confirmation for C02 promotion."}
{"row_type": "case", "case_id": "R1L10_C02_HDHE_20240412_4B", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_PRICE_ONLY_LOCAL_BLOWOFF", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "R1L10_C02_HDHE_LOCAL_4B_20240412", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "same symbol reused for different trigger family: 4B local-vs-full-window timing audit", "independent_evidence_weight": 0.25, "score_price_alignment": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024-04 local valuation/positioning overheat before later full-cycle extension; no confirmed non-price slowdown on trigger date."}
{"row_type": "trigger", "trigger_id": "R1L10_C02_HDHE_STAGE2A_20230424", "case_id": "R1L10_C02_HDHE_20230424", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_EXPORT_BACKLOG_MARGIN_BRIDGE", "sector": "산업재·수주·인프라", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-24", "evidence_available_at_that_date": "2023-04 results/backlog/revision proxy: transformer/export demand and margin bridge became visible before the full 2024 rerating.", "evidence_source": "historical company disclosure / research-report proxy; not live discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv", "profile_path": "atlas/symbol_profiles/267/267260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-25", "entry_price": 53000.0, "MFE_30D_pct": 3.77, "MFE_90D_pct": 58.49, "MFE_180D_pct": 81.89, "MFE_1Y_pct": 400.94, "MFE_2Y_pct": "available_not_used_for_weight_delta", "MAE_30D_pct": -14.91, "MAE_90D_pct": -14.91, "MAE_180D_pct": -14.91, "MAE_1Y_pct": -14.91, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 265500, "drawdown_after_peak_pct": -24.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L10_C02_HDHE_20230424::2023-04-25::53000.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "case_id": "R1L10_C02_HYOSUNG_20230728", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_TRANSFORMER_BACKLOG_MARGIN_BRIDGE", "sector": "산업재·수주·인프라", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-07-28", "evidence_available_at_that_date": "2023-07 results/research proxy: heavy electrical equipment demand and transformer backlog translated into price-confirmed rerating.", "evidence_source": "historical company disclosure / research-report proxy; not live discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298040/2023.csv", "profile_path": "atlas/symbol_profiles/298/298040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-31", "entry_price": 174500.0, "MFE_30D_pct": 19.2, "MFE_90D_pct": 26.93, "MFE_180D_pct": 104.58, "MFE_1Y_pct": 104.58, "MFE_2Y_pct": "available_not_used_for_weight_delta", "MAE_30D_pct": -11.12, "MAE_90D_pct": -12.44, "MAE_180D_pct": -12.44, "MAE_1Y_pct": -12.44, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-15", "peak_price": 357000, "drawdown_after_peak_pct": -26.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L10_C02_HYOSUNG_20230728::2023-07-31::174500.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "case_id": "R1L10_C02_LS_20240429", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_DATACENTER_RELATIVE_STRENGTH_WITH_HIGH_MAE", "sector": "산업재·수주·인프라", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-29", "evidence_available_at_that_date": "2024-04 power-grid/data-center theme and relative strength were visible, but the later path showed high MAE before durable confirmation.", "evidence_source": "historical company disclosure / research-report proxy; not live discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-30", "entry_price": 176600.0, "MFE_30D_pct": 38.17, "MFE_90D_pct": 55.44, "MFE_180D_pct": 55.44, "MFE_1Y_pct": 55.44, "MFE_2Y_pct": "available_not_used_for_weight_delta", "MAE_30D_pct": -9.91, "MAE_90D_pct": -19.71, "MAE_180D_pct": -28.54, "MAE_1Y_pct": -28.54, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 274500, "drawdown_after_peak_pct": -54.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": "price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L10_C02_LS_20240429::2024-04-30::176600.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "SMALL_ELECTRICAL_GRID_THEME_PRICE_ONLY", "sector": "산업재·수주·인프라", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "price_moved_without_evidence", "trigger_date": "2024-05-07", "evidence_available_at_that_date": "2024-05 grid/electrical equipment theme price spike without sufficient backlog, margin bridge, or durable customer confirmation for C02 promotion.", "evidence_source": "historical company disclosure / research-report proxy; not live discovery", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv", "profile_path": "atlas/symbol_profiles/017/017040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-07", "entry_price": 3185.0, "MFE_30D_pct": 4.24, "MFE_90D_pct": 4.24, "MFE_180D_pct": 4.24, "MFE_1Y_pct": 4.24, "MFE_2Y_pct": "available_not_used_for_weight_delta", "MAE_30D_pct": -32.03, "MAE_90D_pct": -51.33, "MAE_180D_pct": -60.75, "MAE_1Y_pct": -60.75, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-08", "peak_price": 3320, "drawdown_after_peak_pct": -62.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": "price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L10_C02_KWANGMYUNG_20240507::2024-05-07::3185.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L10_C02_HDHE_LOCAL_4B_20240412", "case_id": "R1L10_C02_HDHE_20240412_4B", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_PRICE_ONLY_LOCAL_BLOWOFF", "sector": "산업재·수주·인프라", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-04-12", "evidence_available_at_that_date": "2024-04 local valuation/positioning overheat before later full-cycle extension; no confirmed non-price slowdown on trigger date.", "evidence_source": "historical company disclosure / research-report proxy; not live discovery", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "profile_path": "atlas/symbol_profiles/267/267260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-12", "entry_price": 235000.0, "MFE_30D_pct": 33.62, "MFE_90D_pct": 33.62, "MFE_180D_pct": 80.0, "MFE_1Y_pct": 180.0, "MFE_2Y_pct": "available_not_used_for_weight_delta", "MAE_30D_pct": -14.89, "MAE_90D_pct": -14.89, "MAE_180D_pct": -14.89, "MAE_1Y_pct": -14.89, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-27", "peak_price": 314000, "drawdown_after_peak_pct": -18.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.19, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": "valuation_blowoff|price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L10_C02_HDHE_20240412_4B::2024-04-12::235000.0", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same symbol reused for different trigger family: 4B local-vs-full-window timing audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "baseline_current", "case_id": "R1L10_C02_HDHE_20230424", "trigger_id": "R1L10_C02_HDHE_STAGE2A_20230424", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 rewards backlog + margin bridge without loosening Green; Green waits for stronger revision.", "MFE_90D_pct": 58.49, "MAE_90D_pct": -14.91, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "case_id": "R1L10_C02_HDHE_20230424", "trigger_id": "R1L10_C02_HDHE_STAGE2A_20230424", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 rewards backlog + margin bridge without loosening Green; Green waits for stronger revision.", "MFE_90D_pct": 58.49, "MAE_90D_pct": -14.91, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "R1_L1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "case_id": "R1L10_C02_HDHE_20230424", "trigger_id": "R1L10_C02_HDHE_STAGE2A_20230424", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 82, "margin_bridge_score": 68, "revision_score": 70, "relative_strength_score": 65, "customer_quality_score": 68, "policy_or_regulatory_score": 50, "valuation_repricing_score": 52, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 rewards backlog + margin bridge without loosening Green; Green waits for stronger revision.", "MFE_90D_pct": 58.49, "MAE_90D_pct": -14.91, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_power_grid_datacenter_capex_candidate_profile", "profile_scope": "canonical_archetype_specific", "case_id": "R1L10_C02_HDHE_20230424", "trigger_id": "R1L10_C02_HDHE_STAGE2A_20230424", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 82, "margin_bridge_score": 68, "revision_score": 70, "relative_strength_score": 65, "customer_quality_score": 68, "policy_or_regulatory_score": 50, "valuation_repricing_score": 52, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 rewards backlog + margin bridge without loosening Green; Green waits for stronger revision.", "MFE_90D_pct": 58.49, "MAE_90D_pct": -14.91, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_counterexample_guard_profile", "profile_scope": "counterexample_guard", "case_id": "R1L10_C02_HDHE_20230424", "trigger_id": "R1L10_C02_HDHE_STAGE2A_20230424", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 60, "relative_strength_score": 65, "customer_quality_score": 62, "policy_or_regulatory_score": 45, "valuation_repricing_score": 48, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 82, "margin_bridge_score": 68, "revision_score": 70, "relative_strength_score": 65, "customer_quality_score": 68, "policy_or_regulatory_score": 50, "valuation_repricing_score": 52, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 rewards backlog + margin bridge without loosening Green; Green waits for stronger revision.", "MFE_90D_pct": 58.49, "MAE_90D_pct": -14.91, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "baseline_current", "case_id": "R1L10_C02_HYOSUNG_20230728", "trigger_id": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Same C02 rule confirms structural positives when backlog and margin evidence move together.", "MFE_90D_pct": 26.93, "MAE_90D_pct": -12.44, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "case_id": "R1L10_C02_HYOSUNG_20230728", "trigger_id": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Same C02 rule confirms structural positives when backlog and margin evidence move together.", "MFE_90D_pct": 26.93, "MAE_90D_pct": -12.44, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "R1_L1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "case_id": "R1L10_C02_HYOSUNG_20230728", "trigger_id": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 78, "margin_bridge_score": 66, "revision_score": 66, "relative_strength_score": 70, "customer_quality_score": 65, "policy_or_regulatory_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 22, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Same C02 rule confirms structural positives when backlog and margin evidence move together.", "MFE_90D_pct": 26.93, "MAE_90D_pct": -12.44, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_power_grid_datacenter_capex_candidate_profile", "profile_scope": "canonical_archetype_specific", "case_id": "R1L10_C02_HYOSUNG_20230728", "trigger_id": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 78, "margin_bridge_score": 66, "revision_score": 66, "relative_strength_score": 70, "customer_quality_score": 65, "policy_or_regulatory_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 22, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Same C02 rule confirms structural positives when backlog and margin evidence move together.", "MFE_90D_pct": 26.93, "MAE_90D_pct": -12.44, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_counterexample_guard_profile", "profile_scope": "counterexample_guard", "case_id": "R1L10_C02_HYOSUNG_20230728", "trigger_id": "R1L10_C02_HYOSUNG_STAGE2A_20230728", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 58, "policy_or_regulatory_score": 42, "valuation_repricing_score": 45, "execution_risk_score": 28, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 78, "margin_bridge_score": 66, "revision_score": 66, "relative_strength_score": 70, "customer_quality_score": 65, "policy_or_regulatory_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 22, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Same C02 rule confirms structural positives when backlog and margin evidence move together.", "MFE_90D_pct": 26.93, "MAE_90D_pct": -12.44, "score_return_alignment_label": "structural_rerating_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "baseline_current", "case_id": "R1L10_C02_LS_20240429", "trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 guard caps relative-strength-only grid enthusiasm until backlog/margin bridge is above threshold.", "MFE_90D_pct": 55.44, "MAE_90D_pct": -19.71, "score_return_alignment_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "case_id": "R1L10_C02_LS_20240429", "trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 guard caps relative-strength-only grid enthusiasm until backlog/margin bridge is above threshold.", "MFE_90D_pct": 55.44, "MAE_90D_pct": -19.71, "score_return_alignment_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "R1_L1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "case_id": "R1L10_C02_LS_20240429", "trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 78, "customer_quality_score": 48, "policy_or_regulatory_score": 65, "valuation_repricing_score": 40, "execution_risk_score": 58, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 guard caps relative-strength-only grid enthusiasm until backlog/margin bridge is above threshold.", "MFE_90D_pct": 55.44, "MAE_90D_pct": -19.71, "score_return_alignment_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "C02_power_grid_datacenter_capex_candidate_profile", "profile_scope": "canonical_archetype_specific", "case_id": "R1L10_C02_LS_20240429", "trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 78, "customer_quality_score": 48, "policy_or_regulatory_score": 65, "valuation_repricing_score": 40, "execution_risk_score": 58, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 guard caps relative-strength-only grid enthusiasm until backlog/margin bridge is above threshold.", "MFE_90D_pct": 55.44, "MAE_90D_pct": -19.71, "score_return_alignment_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "C02_counterexample_guard_profile", "profile_scope": "counterexample_guard", "case_id": "R1L10_C02_LS_20240429", "trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 88, "customer_quality_score": 48, "policy_or_regulatory_score": 70, "valuation_repricing_score": 44, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 42, "margin_bridge_score": 38, "revision_score": 52, "relative_strength_score": 78, "customer_quality_score": 48, "policy_or_regulatory_score": 65, "valuation_repricing_score": 40, "execution_risk_score": 58, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C02 guard caps relative-strength-only grid enthusiasm until backlog/margin bridge is above threshold.", "MFE_90D_pct": 55.44, "MAE_90D_pct": -19.71, "score_return_alignment_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "baseline_current", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "trigger_id": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 54, "stage_label_before": "Stage1/weak-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/weak-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "No positive promotion; retained as counterexample supporting C02 non-price bridge.", "MFE_90D_pct": 4.24, "MAE_90D_pct": -51.33, "score_return_alignment_label": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "trigger_id": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 54, "stage_label_before": "Stage1/weak-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/weak-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "No positive promotion; retained as counterexample supporting C02 non-price bridge.", "MFE_90D_pct": 4.24, "MAE_90D_pct": -51.33, "score_return_alignment_label": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "R1_L1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "trigger_id": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 54, "stage_label_before": "Stage1/weak-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 15, "execution_risk_score": 85, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage1/weak-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "No positive promotion; retained as counterexample supporting C02 non-price bridge.", "MFE_90D_pct": 4.24, "MAE_90D_pct": -51.33, "score_return_alignment_label": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_power_grid_datacenter_capex_candidate_profile", "profile_scope": "canonical_archetype_specific", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "trigger_id": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 54, "stage_label_before": "Stage1/weak-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 15, "execution_risk_score": 85, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage1/weak-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "No positive promotion; retained as counterexample supporting C02 non-price bridge.", "MFE_90D_pct": 4.24, "MAE_90D_pct": -51.33, "score_return_alignment_label": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_counterexample_guard_profile", "profile_scope": "counterexample_guard", "case_id": "R1L10_C02_KWANGMYUNG_20240507", "trigger_id": "R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 54, "stage_label_before": "Stage1/weak-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 15, "execution_risk_score": 85, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage1/weak-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "No positive promotion; retained as counterexample supporting C02 non-price bridge.", "MFE_90D_pct": 4.24, "MAE_90D_pct": -51.33, "score_return_alignment_label": "price_only_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "aggregate_metric", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "representative_trigger_count": 4, "avg_MFE_90D_pct": 36.27, "avg_MAE_90D_pct": -24.6, "avg_MFE_180D_pct": 61.54, "avg_MAE_180D_pct": -29.16, "false_positive_rate": 0.25, "current_profile_error_count": 1}
{"row_type": "shadow_weight", "axis": "c02_non_price_backlog_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "baseline_value": "not_explicit", "tested_value": "require_backlog_or_margin_bridge_for_stage2_bonus", "delta": "+guardrail", "reason": "Positive cases had backlog/margin bridge; counterexamples had relative strength without durable bridge and showed high MAE or collapse.", "backtest_effect": "representative avg MFE90 36.27 / avg MAE90 -24.6; price-only counterexample MAE180 -60.75", "trigger_ids": "R1L10_C02_HDHE_STAGE2A_20230424|R1L10_C02_HYOSUNG_STAGE2A_20230728|R1L10_C02_LS_HIGH_MAE_20240429|R1L10_C02_KWANGMYUNG_PRICE_ONLY_20240507", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 2, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "shadow_weight", "axis": "c02_price_only_local_4b_watch_only", "scope": "canonical_archetype_specific", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "baseline_value": "full_4b_requires_non_price_evidence=true", "tested_value": "keep_price_only_local_peak_as_watch_only_even_when_local_proximity_high", "delta": "+specificity", "reason": "HD Hyundai Electric local 4B near Apr-2024 looked close to a local peak but full-window extension was still large; full 4B should wait for non-price slowdown.", "backtest_effect": "local proximity 0.86 vs full-window proximity 0.19", "trigger_ids": "R1L10_C02_HDHE_LOCAL_4B_20240412", "calibration_usable_count": 1, "new_independent_case_count": 0, "counterexample_count": 1, "confidence": "low_medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "4B overlay only"}
{"row_type": "residual_contribution", "round": "R1", "loop": "10", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["high_MAE_relative_strength_without_backlog_bridge", "price_only_grid_theme_false_positive", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R1
completed_loop = 10
next_round = R2
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files read or validated:

```text
Songdaiki/stock-web atlas/manifest.json
Songdaiki/stock-web atlas/schema.json
Songdaiki/stock-web atlas/symbol_profiles/267/267260.json
Songdaiki/stock-web atlas/symbol_profiles/298/298040.json
Songdaiki/stock-web atlas/symbol_profiles/010/010120.json
Songdaiki/stock-web atlas/symbol_profiles/017/017040.json
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/298/298040/2023.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv
```

Research-artifact context used only for schedule and coverage/duplicate avoidance:

```text
stock_agent reports/e2r_calibration/ingest_summary.md
stock_agent reports/e2r_calibration/applied_scoring_diff.md
stock_agent reports/e2r_calibration/calibrated_profile_report.md
stock_agent reports/e2r_calibration/by_round/R1.md
stock_agent docs/round filename listing for visible v12 schedule state
```

