# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_129_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 129
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_CATHODE_UTILIZATION_ASP_DEMAND_SLOWDOWN_HARD_4C
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_timing_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after a duplicate loop128 materialization path was discarded. Loop128 already used `247540`, `066970`, and `373220`; this loop uses new C14 symbol/trigger/date combinations only.

This loop adds 3 new independent C14 rows and moves C14 from static 21 rows to local projected 24 after loop128, then to projected 27 after this loop. It still needs 3 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C14:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C14 -> C14_EV_DEMAND_SLOWDOWN_4B_4C
```

C14 is the EV demand slowdown / 4B / 4C archetype. The mechanism is a tug-of-war: 4B rebounds can lift the tape for weeks, but utilization, call-off, ASP/mix, inventory, margin and FCF decide whether the rope is anchored or fraying.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C14 static rows | 21 |
| C14 need to 30 | 9 |
| C14 need to 50 | 29 |
| C14 investigation point | EV 수요 둔화, utilization, call-off, hard 4C 확인 |
| local C14 loop128 projected rows | 24 |
| this loop projected rows | 27 |

Selected symbols avoid local C14 loop128 symbols `247540`, `066970`, and `373220`.

| symbol | company | status |
|---|---|---|
| 003670 | 포스코퓨처엠 | new local C14 hard 4C cathode case |
| 361610 | SK아이이테크놀로지 | new local C14 hard 4C separator case |
| 006400 | 삼성SDI | new local C14 premature-hard-4C timing counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 003670 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 361610 / 2024-03-06 | true | true | clean_180D_window | true |
| 006400 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |

Corporate-action notes:

- 포스코퓨처엠 has old corporate-action candidates in 2015/2021 only; selected 2024 window is clean.
- SK아이이테크놀로지 has zero corporate-action candidates.
- 삼성SDI has old corporate-action candidates before selected 2024 window; selected 2024 window is clean.
- 천보(278280) was considered but not selected because this loop needed one timing/overblock counterexample in addition to hard 4C protection rows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| EV_CATHODE_UTILIZATION_ASP_DEMAND_SLOWDOWN_HARD_4C | C14 | cathode rebound should be capped when utilization/ASP/call-off pressure persists |
| EV_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C | C14 | separator recovery beta fails when utilization/margin/FCF bridge is absent |
| EV_CELL_PREMATURE_HARD_4C_OVERBLOCK_WITH_4B_TIMING_BOUNCE | C14 | immediate blanket hard 4C can overblock a real large-cap cell 4B timing window |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C14_POSCOFUTUREM_003670_2024_03_06_CATHODE_UTILIZATION_ASP_HARD_4C | 003670 | 포스코퓨처엠 | hard_4c_protection_success | positive_protection | minor 10% bounce followed by large 180D MAE |
| C14_SKIET_361610_2024_03_06_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C | 361610 | SK아이이테크놀로지 | hard_4c_protection_success | positive_protection | separator recovery beta had low MFE and severe MAE |
| C14_SAMSUNGSDI_006400_2024_03_06_CELL_PREMATURE_4C_TIMING_COUNTEREXAMPLE | 006400 | 삼성SDI | timing_overblock_counterexample | counterexample | immediate hard 4C would have missed a 35.67% 4B timing bounce |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_protection_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 2 |
| overblock_or_timing_counterexample_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 003670 | source_proxy_only | cathode utilization / ASP / customer inventory-calloff pressure | required before promotion |
| 361610 | source_proxy_only | separator utilization / EV slowdown / margin-okayness failure | required before promotion |
| 006400 | source_proxy_only | cell-scale/customer mix buffer and 4B timing bounce before later risk | required; useful as timing counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv | atlas/symbol_profiles/003/003670.json |
| 361610 | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | atlas/symbol_profiles/361/361610.json |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | atlas/symbol_profiles/006/006400.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| POSCOFUTUREM_003670_2024_03_06_STAGE4C_CATHODE_UTILIZATION_ASP_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 310000 | cathode utilization/ASP/call-off hard 4C |
| SKIET_361610_2024_03_06_STAGE4C_SEPARATOR_UTILIZATION_SLOWDOWN | Stage4C | 2024-03-06 | 2024-03-06 | 70900 | separator utilization/margin hard 4C |
| SAMSUNGSDI_006400_2024_03_06_STAGE2_4B_TIMING_OVERBLOCK_COUNTEREXAMPLE | Stage2 | 2024-03-06 | 2024-03-06 | 364500 | cell-scale 4B timing counterexample |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 003670 | 2024-03-06 | 310000 | 10.00 | -19.68 | 10.00 | -20.32 | 10.00 | -47.74 | 2024-03-13 | 341000 | -52.49 |
| 361610 | 2024-03-06 | 70900 | 9.59 | -15.66 | 9.59 | -43.30 | 9.59 | -65.66 | 2024-03-26 | 77700 | -68.66 |
| 006400 | 2024-03-06 | 364500 | 35.67 | -0.41 | 35.67 | -3.70 | 35.67 | -35.39 | 2024-03-25 | 494500 | -52.38 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 003670 | Stage2 bounce risk if cathode recovery beta is over-credited | hard 4C protection worked | current_profile_4C_too_late |
| 361610 | Stage2 bounce risk if separator recovery beta is over-credited | hard 4C protection worked | current_profile_4C_too_late |
| 006400 | hard 4C risk if EV slowdown fires immediately without timing gate | premature overblock counterexample | current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C14 interpretation:

- Cathode and separator names should be capped by hard 4C when utilization, ASP/mix, call-off, margin and FCF pressure are visible.
- A 4B bounce does not create Yellow/Green without non-price customer and margin recovery.
- Large cell names can have a real 4B timing window before later 4C risk; immediate blanket hard 4C can be too early.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 003670 | 0.91 | 1.00 | cathode minor rebound / hard 4C | 4B bounce should not override hard 4C |
| 361610 | 0.91 | 1.00 | separator minor rebound / hard 4C | 4B bounce should not override hard 4C |
| 006400 | 0.74 | 1.00 | cell-scale large 4B bounce / delayed 4C watch | immediate blanket 4C overblocks timing window |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 003670 | hard_4c_success | cathode utilization/ASP pressure protected against later drawdown |
| 361610 | hard_4c_success | separator utilization/margin pressure protected against severe drawdown |
| 006400 | timing_overblock_counterexample | hard 4C should require confirmed utilization break, not just broad EV weakness |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, EV demand slowdown should trigger hard 4C when utilization, call-off, ASP/mix, inventory, margin, revision or FCF deterioration is visible. But for large cell makers, immediate hard 4C should wait for confirmed utilization or margin break if customer/scale buffers and a 4B timing window are still present.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
confidence = medium
```

Candidate C14 rule:

```text
C14_ev_demand_slowdown_hard_4c =
  ev_demand_slowdown
  AND (utilization_pressure OR customer_call_off OR asp_mix_pressure OR inventory_overhang OR margin_revision_down OR fcf_deterioration)

if cathode_or_separator_recovery_beta and C14_ev_demand_slowdown_hard_4c:
    cap_stage = Stage4C
    do_not_allow_Stage3_Yellow_or_Green = true

if large_cell_maker and customer_scale_buffer and 4b_rebound_window and not confirmed_utilization_break:
    classify_as C14_premature_hard_4c_timing_counterexample
    cap_stage = Stage2-watch_not_Green
    require delayed_4C_recheck

if MFE_90D < 12 and MAE_90D < -20 and hard_4c_evidence:
    strengthen C14_hard_4c_protection

if MFE_30D > 30 and MAE_90D > -5 and large_cell_maker:
    add C14_4B_timing_exception
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 18.42 | -22.44 | 18.42 | -49.6 | 1 timing overblock | useful but timing rule needed |
| P0b calibrated rollback | rollback | 3 | 18.42 | -22.44 | 18.42 | -49.6 | 1 timing overblock | over-credits cathode/separator rebound or overblocks cell timing |
| P1 sector_specific_candidate_profile | L3 | 2 hard 4C + 1 timing exception | 9.79 | -31.81 | 9.79 | -56.7 | 0 | better with hard 4C and delayed cell exception |
| P2 canonical_archetype_candidate_profile | C14 | 2 hard 4C + 1 timing exception | 9.79 | -31.81 | 9.79 | -56.7 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C14 guard | 2 hard 4C + 1 timing exception | 9.79 | -31.81 | 9.79 | -56.7 | 0 | adds premature-hard-4C timing guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 003670 | hard 4C aligned; rebound was too small to override | current_profile_4C_too_late |
| 361610 | hard 4C aligned; separator recovery beta failed | current_profile_4C_too_late |
| 006400 | hard 4C overblock if applied before utilization break | current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive protection | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed C14 fine ids | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> projected 27; still need 3 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4C_too_late
  - current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break
new_axis_proposed: C14_ev_demand_slowdown_hard_4c|C14_cathode_separator_hard_4c_guard|C14_large_cell_premature_4c_timing_exception|C14_4B_timing_exception
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
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
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses C14 Priority 0 coverage gap.
- Avoids local C14 loop128 symbols.
- Keeps 003670 and 006400 with reduced weights because old corporate-action candidates are outside selected windows or because large-cell anchor timing rows should not overcount pure hard 4C evidence.
- Treats 006400 as a timing overblock counterexample, not a Green promotion.
- Discards the accidental duplicate loop128 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop128 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_ev_demand_slowdown_hard_4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"003670/361610 show cathode/separator recovery beta can fail when utilization/ASP/margin pressure persists","caps Stage2/Yellow after weak bounce and preserves hard 4C protection","POSCOFUTUREM_003670_2024_03_06_STAGE4C_CATHODE_UTILIZATION_ASP_RISK|SKIET_361610_2024_03_06_STAGE4C_SEPARATOR_UTILIZATION_SLOWDOWN",2,2,0,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C14_cathode_separator_hard_4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"003670/361610 had low MFE and high MAE after EV demand slowdown pressure","requires utilization/ASP/margin/FCF recovery before Stage2/Yellow promotion","POSCOFUTUREM_003670_2024_03_06_STAGE4C_CATHODE_UTILIZATION_ASP_RISK|SKIET_361610_2024_03_06_STAGE4C_SEPARATOR_UTILIZATION_SLOWDOWN",2,2,0,medium,canonical_shadow_only,"hard 4C protection guardrail"
shadow_weight,C14_large_cell_premature_4c_timing_exception,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"006400 shows immediate blanket hard 4C can miss a large 4B timing bounce before confirmed utilization break","keeps large-cell anchor as Stage2-watch with delayed 4C recheck rather than immediate hard 4C","SAMSUNGSDI_006400_2024_03_06_STAGE2_4B_TIMING_OVERBLOCK_COUNTEREXAMPLE",1,1,1,medium,canonical_shadow_only,"timing overblock guardrail"
shadow_weight,C14_4B_timing_exception,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"006400 had 35.67% MFE and only -3.70% 90D MAE before later drawdown","separates immediate hard 4C from delayed hard 4C after utilization/margin confirmation","SAMSUNGSDI_006400_2024_03_06_STAGE2_4B_TIMING_OVERBLOCK_COUNTEREXAMPLE",1,1,1,medium,canonical_shadow_only,"4B/4C timing calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C14_POSCOFUTUREM_003670_2024_03_06_CATHODE_UTILIZATION_ASP_HARD_4C","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CATHODE_UTILIZATION_ASP_DEMAND_SLOWDOWN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"POSCOFUTUREM_003670_2024_03_06_STAGE4C_CATHODE_UTILIZATION_ASP_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates in 2015/2021 only; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"cathode/utilization and ASP pressure allowed only a 10% bounce before roughly -47.74% 180D MAE, so hard 4C protection was directionally correct","current_profile_verdict":"current_profile_4C_too_late_if_cathode_recovery_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol versus loop128; cathode demand/utilization hard 4C"}
{"row_type":"case","case_id":"C14_SKIET_361610_2024_03_06_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"SKIET_361610_2024_03_06_STAGE4C_SEPARATOR_UTILIZATION_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"separator utilization/demand slowdown had only a 9.59% MFE and then roughly -65.66% 180D MAE, validating hard 4C protection","current_profile_verdict":"current_profile_4C_too_late_if_separator_recovery_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; clean profile with zero corporate-action candidates"}
{"row_type":"case","case_id":"C14_SAMSUNGSDI_006400_2024_03_06_CELL_PREMATURE_4C_TIMING_COUNTEREXAMPLE","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CELL_PREMATURE_HARD_4C_OVERBLOCK_WITH_4B_TIMING_BOUNCE","case_type":"timing_overblock_counterexample","positive_or_counterexample":"counterexample","best_trigger":"SAMSUNGSDI_006400_2024_03_06_STAGE2_4B_TIMING_OVERBLOCK_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; large-cell anchor, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"cell large-cap had a 35.67% 30D MFE and only mild 90D MAE before later drawdown, so immediate blanket hard 4C would have overblocked the 4B timing window","current_profile_verdict":"current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; timing counterexample, not a Green promotion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"POSCOFUTUREM_003670_2024_03_06_STAGE4C_CATHODE_UTILIZATION_ASP_RISK","case_id":"C14_POSCOFUTUREM_003670_2024_03_06_CATHODE_UTILIZATION_ASP_HARD_4C","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CATHODE_UTILIZATION_ASP_DEMAND_SLOWDOWN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":310000.0,"evidence_available_at_that_date":"source_proxy_only: EV cathode demand slowdown, utilization pressure, ASP/mix risk and customer inventory/call-off risk visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_recovery_beta","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["short_rebound_after_bad_news","valuation_peak_watch"],"stage4c_evidence_fields":["ev_demand_slowdown","cathode_utilization_pressure","asp_mix_pressure","customer_inventory_call_off_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.0,"MFE_90D_pct":10.0,"MFE_180D_pct":10.0,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.68,"MAE_90D_pct":-20.32,"MAE_180D_pct":-47.74,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":341000.0,"drawdown_after_peak_pct":-52.49,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small 4B bounce existed but should not override C14 cathode hard 4C","four_b_evidence_type":["minor_rebound","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protection_high_mae_after_minor_bounce","current_profile_verdict":"current_profile_4C_too_late_if_cathode_recovery_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C14_003670_2024_03_06_310000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SKIET_361610_2024_03_06_STAGE4C_SEPARATOR_UTILIZATION_SLOWDOWN","case_id":"C14_SKIET_361610_2024_03_06_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":70900.0,"evidence_available_at_that_date":"source_proxy_only: separator utilization pressure, EV demand slowdown, inventory pressure and margin/FCF deterioration risk visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["separator_recovery_beta","short_rebound_attempt"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["minor_bounce","valuation_peak_watch"],"stage4c_evidence_fields":["separator_utilization_pressure","ev_demand_slowdown","inventory_overhang","margin_fcf_pressure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.59,"MFE_90D_pct":9.59,"MFE_180D_pct":9.59,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.66,"MAE_90D_pct":-43.3,"MAE_180D_pct":-65.66,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":77700.0,"drawdown_after_peak_pct":-68.66,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"minor bounce should not override separator utilization hard 4C","four_b_evidence_type":["minor_rebound","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protection_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late_if_separator_recovery_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_361610_2024_03_06_70900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SAMSUNGSDI_006400_2024_03_06_STAGE2_4B_TIMING_OVERBLOCK_COUNTEREXAMPLE","case_id":"C14_SAMSUNGSDI_006400_2024_03_06_CELL_PREMATURE_4C_TIMING_COUNTEREXAMPLE","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CELL_PREMATURE_HARD_4C_OVERBLOCK_WITH_4B_TIMING_BOUNCE","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":364500.0,"evidence_available_at_that_date":"source_proxy_only: EV cell demand slowdown risk visible, but cell-scale/customer mix and short 4B rebound window were also visible; immediate blanket hard 4C would be premature; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cell_scale_buffer","customer_mix_buffer","4b_rebound_window","relative_strength_reversal"],"stage3_evidence_fields":["customer_scale_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["large_4b_timing_bounce","valuation_peak_watch"],"stage4c_evidence_fields":["ev_demand_slowdown_watch","utilization_pressure_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.67,"MFE_90D_pct":35.67,"MFE_180D_pct":35.67,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-0.41,"MAE_90D_pct":-3.7,"MAE_180D_pct":-35.39,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":494500.0,"drawdown_after_peak_pct":-52.38,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"immediate blanket hard 4C would overblock a real 4B timing window; later 4C watch still needed","four_b_evidence_type":["large_4b_rebound","cell_scale_buffer"],"four_c_protection_label":"timing_overblock_counterexample","trigger_outcome_label":"counterexample_premature_4c_after_large_4b_bounce","current_profile_verdict":"current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["large_cell_anchor_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C14_006400_2024_03_06_364500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window; cell anchor timing exception","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_POSCOFUTUREM_003670_2024_03_06_CATHODE_UTILIZATION_ASP_HARD_4C","trigger_id":"POSCOFUTUREM_003670_2024_03_06_STAGE4C_CATHODE_UTILIZATION_ASP_RISK","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2 bounce risk / late 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":42,"stage_label_after":"Stage4C hard cathode demand-slowdown protection","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Cathode utilization/ASP pressure should dominate a minor recovery bounce.","MFE_90D_pct":10.0,"MAE_90D_pct":-20.32,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_4C_too_late_if_cathode_recovery_beta_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_SKIET_361610_2024_03_06_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","trigger_id":"SKIET_361610_2024_03_06_STAGE4C_SEPARATOR_UTILIZATION_SLOWDOWN","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":55,"stage_label_before":"Stage2 false bounce risk / late 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":40,"stage_label_after":"Stage4C hard separator utilization protection","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Separator utilization and margin/FCF pressure left no durable Stage2A bridge.","MFE_90D_pct":9.59,"MAE_90D_pct":-43.3,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_4C_too_late_if_separator_recovery_beta_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_SAMSUNGSDI_006400_2024_03_06_CELL_PREMATURE_4C_TIMING_COUNTEREXAMPLE","trigger_id":"SAMSUNGSDI_006400_2024_03_06_STAGE2_4B_TIMING_OVERBLOCK_COUNTEREXAMPLE","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-watch / 4B timing window","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with C14 delayed-4C timing guard","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Immediate hard 4C would have overblocked a real 4B timing window; later drawdown still blocks Green without margin/FCF confirmation.","MFE_90D_pct":35.67,"MAE_90D_pct":-3.7,"score_return_alignment_label":"timing_overblock_counterexample","current_profile_verdict":"current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"129","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overblocks_if_hard_4c_fires_before_confirmed_utilization_break"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

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
completed_round = R3
completed_loop = 129
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted together with local C14 loop128, C14 moves to projected 27 rows and still needs 3 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C14 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/003/003670.json
  - atlas/symbol_profiles/361/361610.json
  - atlas/symbol_profiles/006/006400.json
- Rejected local duplicate C14 symbols:
  - 247540, 066970, 373220
- Considered but not selected:
  - atlas/symbol_profiles/278/278280.json
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R3_loop_128_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
