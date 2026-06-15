# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_130_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 130
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_ELECTROLYTE_ADDITIVE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C
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

This is the corrected valid run after a duplicate loop129 materialization path was discarded. Loop129 already used `003670`, `361610`, and `006400`; this loop uses new C14 symbol/trigger/date combinations only.

This loop adds 3 new independent C14 rows and moves C14 from static 21 rows to local projected 27 after loops 128/129, then to projected 30 after this loop. The 30-row stability threshold is reached.

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

C14 is the EV demand slowdown / 4B / 4C archetype. It is a timing switchboard: utilization and ASP pressure can demand hard 4C, but some copper-foil names can still run a 4B timing rally before the delayed 4C audit takes over.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C14 static rows | 21 |
| C14 need to 30 | 9 |
| C14 need to 50 | 29 |
| C14 investigation point | EV 수요 둔화, utilization, call-off, hard 4C 확인 |
| local C14 loop128 projected rows | 24 |
| local C14 loop129 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid local C14 loop128 symbols `247540`, `066970`, `373220` and loop129 symbols `003670`, `361610`, `006400`.

| symbol | company | status |
|---|---|---|
| 278280 | 천보 | new local C14 hard 4C additive/utilization case |
| 020150 | 롯데에너지머티리얼즈 | new local C14 4B timing overblock counterexample |
| 011790 | SKC | new local C14 extreme 4B timing overblock counterexample |

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
| 278280 / 2024-03-06 | true | true | clean_180D_window_zero_corporate_action_candidates | true, reduced weight 0.95 |
| 020150 / 2024-03-06 | true | true | clean_180D_window | true |
| 011790 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |

Corporate-action notes:

- 천보 has zero corporate-action candidates; the 2024 KOSDAQ GLOBAL label ending is treated as market-label only.
- 롯데에너지머티리얼즈 has zero corporate-action candidates.
- SKC has old corporate-action candidates before the selected 2024 window only.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| EV_ELECTROLYTE_ADDITIVE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C | C14 | additive/electrolyte rebound should be capped when utilization/ASP pressure persists |
| EV_COPPER_FOIL_PREMATURE_HARD_4C_WITH_LARGE_4B_BOUNCE | C14 | immediate hard 4C can overblock a large copper-foil 4B timing window |
| EV_COPPER_FOIL_EXTREME_4B_BLOWOFF_WITH_DELAYED_4C_WATCH | C14 | extreme 4B rally needs blowoff audit and delayed 4C, not immediate Green |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C14_CHUNBO_278280_2024_03_06_ELECTROLYTE_ADDITIVE_UTILIZATION_HARD_4C | 278280 | 천보 | hard_4c_protection_success | positive_protection | 3.93% MFE followed by -60.11% 180D MAE |
| C14_LOTTEENERGYMATERIALS_020150_2024_03_06_COPPER_FOIL_4B_TIMING_OVERBLOCK | 020150 | 롯데에너지머티리얼즈 | timing_overblock_counterexample | counterexample | 64.22% MFE before later drawdown |
| C14_SKC_011790_2024_03_06_COPPER_FOIL_EXTREME_4B_TIMING_OVERBLOCK | 011790 | SKC | timing_overblock_counterexample | counterexample | 107.68% MFE before major peak drawdown |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_protection_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| overblock_or_timing_counterexample_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 278280 | source_proxy_only | electrolyte/additive utilization and ASP pressure | required before promotion |
| 020150 | source_proxy_only | copper-foil 4B timing bounce with later utilization/margin audit | required; useful as timing counterexample |
| 011790 | source_proxy_only | copper-foil extreme 4B blowoff with delayed 4C watch | required; useful as timing counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | atlas/symbol_profiles/278/278280.json |
| 020150 | atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv | atlas/symbol_profiles/020/020150.json |
| 011790 | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | atlas/symbol_profiles/011/011790.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| CHUNBO_278280_2024_03_06_STAGE4C_ELECTROLYTE_UTILIZATION_SLOWDOWN | Stage4C | 2024-03-06 | 2024-03-06 | 89000 | electrolyte/additive utilization hard 4C |
| LOTTEENERGYMATERIALS_020150_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE | Stage2 | 2024-03-06 | 2024-03-06 | 36050 | copper-foil large 4B timing window |
| SKC_011790_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE | Stage2 | 2024-03-06 | 2024-03-06 | 96300 | copper-foil extreme 4B blowoff timing |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 278280 | 2024-03-06 | 89000 | 3.93 | -19.55 | 3.93 | -26.18 | 3.93 | -60.11 | 2024-03-18 | 92500 | -61.62 |
| 020150 | 2024-03-06 | 36050 | 45.35 | -1.66 | 64.22 | -1.66 | 64.22 | -33.84 | 2024-06-18 | 59200 | -59.71 |
| 011790 | 2024-03-06 | 96300 | 55.45 | -4.88 | 107.68 | -4.88 | 107.68 | -4.88 | 2024-06-18 | 200000 | -53.30 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 278280 | Stage2 bounce risk if additive recovery beta is over-credited | hard 4C protection worked | current_profile_4C_too_late |
| 020150 | hard 4C risk if EV material slowdown fires immediately | premature overblock counterexample | current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion |
| 011790 | hard 4C risk if all EV material slowdown is treated equally | extreme timing overblock counterexample | current_profile_overblocks_if_all_EV_material_slowdown_equal |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C14 interpretation:

- Additive/electrolyte weakness should be capped by hard 4C when utilization, ASP and inventory pressure are visible.
- Copper-foil names can still produce a major 4B timing rally.
- A 4B rally still cannot become Yellow/Green without non-price margin, utilization, customer, and FCF proof.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 278280 | 0.96 | 1.00 | additive utilization hard 4C | minor bounce should not override hard 4C |
| 020150 | 0.61 | 1.00 | copper-foil 4B rebound | immediate hard 4C overblocks, delayed 4C audit needed |
| 011790 | 0.48 | 1.00 | copper-foil extreme 4B blowoff | price-only blowoff cannot become Green |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 278280 | hard_4c_success | additive utilization/ASP pressure protected against later collapse |
| 020150 | timing_overblock_counterexample | hard 4C should be delayed until 4B exhaustion or utilization break |
| 011790 | timing_overblock_counterexample_then_delayed_4c_watch | immediate hard 4C was too early, but blowoff audit was mandatory |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, EV demand slowdown should trigger hard 4C when utilization, call-off, ASP/mix, inventory, margin, revision or FCF deterioration is visible. But copper-foil/material names can have a large 4B timing window; immediate hard 4C should not overblock that window unless confirmed utilization or margin break is already present.

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

if additive_or_separator_recovery_beta and C14_ev_demand_slowdown_hard_4c:
    cap_stage = Stage4C
    do_not_allow_Stage3_Yellow_or_Green = true

if copper_foil_material_name and large_4b_rebound_window and not confirmed_utilization_break:
    classify_as C14_premature_hard_4c_timing_counterexample
    cap_stage = Stage2-watch_not_Green
    require delayed_4C_recheck

if MFE_90D < 10 and MAE_180D < -40 and hard_4c_evidence:
    strengthen C14_hard_4c_protection

if MFE_90D > 50 and MAE_90D > -10 and copper_foil_material_name:
    add C14_4B_timing_exception

if MFE_90D > 50 and drawdown_after_peak < -35:
    add C14_price_only_blowoff_delayed_4C_audit
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 58.61 | -10.91 | 58.61 | -32.94 | 2 timing overblock | useful but timing rule needed |
| P0b calibrated rollback | rollback | 3 | 58.61 | -10.91 | 58.61 | -32.94 | 2 timing overblock | over-credits additive bounce or overblocks copper-foil rebound |
| P1 sector_specific_candidate_profile | L3 | 1 hard 4C + 2 timing exceptions | 3.93 | -26.18 | 3.93 | -60.11 | 0 | better with hard 4C plus copper-foil timing exception |
| P2 canonical_archetype_candidate_profile | C14 | 1 hard 4C + 2 timing exceptions | 3.93 | -26.18 | 3.93 | -60.11 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C14 guard | 1 hard 4C + 2 timing exceptions | 3.93 | -26.18 | 3.93 | -60.11 | 0 | adds premature-hard-4C timing guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 278280 | hard 4C aligned; additive rebound failed | current_profile_4C_too_late |
| 020150 | hard 4C overblock if fired before 4B exhaustion | current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion |
| 011790 | hard 4C overblock if all EV material slowdown treated equally | current_profile_overblocks_if_all_EV_material_slowdown_equal |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive protection | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed C14 fine ids | 1 | 2 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 27 -> projected 30; reaches minimum stability threshold |

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
  - current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion
new_axis_proposed: C14_ev_demand_slowdown_hard_4c|C14_additive_hard_4c_guard|C14_copper_foil_premature_4c_timing_exception|C14_price_only_blowoff_delayed_4c_audit
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
- Avoids local C14 loop128 and loop129 symbols.
- Keeps 278280 with reduced weight because market-label switch is treated as non-price-adjustment contamination.
- Keeps 011790 with reduced weight because it is a copper-foil/chemical boundary with old profile caveats.
- Treats 020150 and 011790 as timing overblock counterexamples, not Green promotions.
- Discards the accidental duplicate loop129 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop129 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_ev_demand_slowdown_hard_4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"278280 shows additive/electrolyte recovery beta can fail when utilization/ASP pressure persists","caps Stage2/Yellow after weak additive bounce and preserves hard 4C protection","CHUNBO_278280_2024_03_06_STAGE4C_ELECTROLYTE_UTILIZATION_SLOWDOWN",1,1,0,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C14_additive_hard_4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"278280 had only 3.93% MFE and -60.11% 180D MAE after additive utilization pressure","requires utilization/ASP/margin/FCF recovery before Stage2/Yellow promotion","CHUNBO_278280_2024_03_06_STAGE4C_ELECTROLYTE_UTILIZATION_SLOWDOWN",1,1,0,medium,canonical_shadow_only,"hard 4C protection guardrail"
shadow_weight,C14_copper_foil_premature_4c_timing_exception,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"020150/011790 show immediate hard 4C can miss large copper-foil 4B timing rallies before confirmed utilization break","keeps copper-foil names as Stage2-watch with delayed 4C recheck rather than immediate hard 4C","LOTTEENERGYMATERIALS_020150_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE|SKC_011790_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE",2,2,2,medium,canonical_shadow_only,"timing overblock guardrail"
shadow_weight,C14_price_only_blowoff_delayed_4c_audit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"020150/011790 had large MFE and later deep post-peak drawdown, so price-only 4B cannot become Green","requires non-price utilization/margin/FCF proof after rebound or routes to delayed 4C audit","LOTTEENERGYMATERIALS_020150_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE|SKC_011790_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE",2,2,2,medium,canonical_shadow_only,"4B/4C timing calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C14_CHUNBO_278280_2024_03_06_ELECTROLYTE_ADDITIVE_UTILIZATION_HARD_4C","symbol":"278280","company_name":"천보","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_ELECTROLYTE_ADDITIVE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"CHUNBO_278280_2024_03_06_STAGE4C_ELECTROLYTE_UTILIZATION_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"zero corporate-action candidates; 2024 KOSDAQ GLOBAL label ends during forward window but treated as market-label only, independent weight reduced","independent_evidence_weight":0.95,"score_price_alignment":"electrolyte/additive utilization pressure allowed only a 3.93% bounce before roughly -60.11% 180D MAE, validating hard 4C protection","current_profile_verdict":"current_profile_4C_too_late_if_additive_recovery_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol versus loops 128/129; considered in loop129 but not selected"}
{"row_type":"case","case_id":"C14_LOTTEENERGYMATERIALS_020150_2024_03_06_COPPER_FOIL_4B_TIMING_OVERBLOCK","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_COPPER_FOIL_PREMATURE_HARD_4C_WITH_LARGE_4B_BOUNCE","case_type":"timing_overblock_counterexample","positive_or_counterexample":"counterexample","best_trigger":"LOTTEENERGYMATERIALS_020150_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"copper foil name had a 64% MFE before later -33.84% 180D MAE, so immediate hard 4C would overblock the 4B timing window while delayed 4C audit was still needed","current_profile_verdict":"current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; clean profile with zero corporate-action candidates"}
{"row_type":"case","case_id":"C14_SKC_011790_2024_03_06_COPPER_FOIL_EXTREME_4B_TIMING_OVERBLOCK","symbol":"011790","company_name":"SKC","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_COPPER_FOIL_EXTREME_4B_BLOWOFF_WITH_DELAYED_4C_WATCH","case_type":"timing_overblock_counterexample","positive_or_counterexample":"counterexample","best_trigger":"SKC_011790_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; copper-foil/chemical boundary, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"copper foil/EV material name had a 107.68% MFE before a -53.30% post-peak drawdown, so immediate 4C would overblock but 4B peak audit was mandatory","current_profile_verdict":"current_profile_overblocks_if_all_EV_material_slowdown_equal","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; old profile caveat only"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"CHUNBO_278280_2024_03_06_STAGE4C_ELECTROLYTE_UTILIZATION_SLOWDOWN","case_id":"C14_CHUNBO_278280_2024_03_06_ELECTROLYTE_ADDITIVE_UTILIZATION_HARD_4C","symbol":"278280","company_name":"천보","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_ELECTROLYTE_ADDITIVE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":89000.0,"evidence_available_at_that_date":"source_proxy_only: EV electrolyte/additive demand slowdown, utilization pressure, ASP/mix pressure and customer inventory stress visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["electrolyte_additive_recovery_beta","short_rebound_attempt"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["minor_bounce","valuation_peak_watch"],"stage4c_evidence_fields":["utilization_pressure","ev_demand_slowdown","asp_mix_pressure","customer_inventory_overhang"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.93,"MFE_90D_pct":3.93,"MFE_180D_pct":3.93,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.55,"MAE_90D_pct":-26.18,"MAE_180D_pct":-60.11,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-18","peak_price":92500.0,"drawdown_after_peak_pct":-61.62,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"minor additive rebound should not override C14 utilization hard 4C","four_b_evidence_type":["minor_rebound","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protection_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late_if_additive_recovery_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_label_switch_not_price_adjustment_contamination"],"corporate_action_window_status":"clean_180D_window_zero_corporate_action_candidates","same_entry_group_id":"C14_278280_2024_03_06_89000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"zero corporate-action candidates; market-label switch only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LOTTEENERGYMATERIALS_020150_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE","case_id":"C14_LOTTEENERGYMATERIALS_020150_2024_03_06_COPPER_FOIL_4B_TIMING_OVERBLOCK","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_COPPER_FOIL_PREMATURE_HARD_4C_WITH_LARGE_4B_BOUNCE","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":36050.0,"evidence_available_at_that_date":"source_proxy_only: EV copper-foil demand slowdown risk visible, but a sizable 4B timing rebound and customer/material optionality remained; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["copper_foil_4b_rebound_window","customer_optional_recovery","relative_strength_reversal"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["large_4b_timing_bounce","cycle_peak_watch"],"stage4c_evidence_fields":["ev_demand_slowdown_watch","utilization_pressure_watch","margin_fcf_pressure_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.35,"MFE_90D_pct":64.22,"MFE_180D_pct":64.22,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-1.66,"MAE_90D_pct":-1.66,"MAE_180D_pct":-33.84,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":59200.0,"drawdown_after_peak_pct":-59.71,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.61,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"immediate hard 4C would overblock the large copper-foil 4B timing window; delayed 4C audit still needed after peak","four_b_evidence_type":["large_4b_rebound","cycle_peak_watch"],"four_c_protection_label":"timing_overblock_counterexample","trigger_outcome_label":"counterexample_premature_4c_large_4b_bounce_then_drawdown","current_profile_verdict":"current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_020150_2024_03_06_36050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SKC_011790_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE","case_id":"C14_SKC_011790_2024_03_06_COPPER_FOIL_EXTREME_4B_TIMING_OVERBLOCK","symbol":"011790","company_name":"SKC","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_COPPER_FOIL_EXTREME_4B_BLOWOFF_WITH_DELAYED_4C_WATCH","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":96300.0,"evidence_available_at_that_date":"source_proxy_only: EV copper-foil slowdown risk visible, but extreme 4B rebound window and optionality remained before later utilization/margin proof; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["copper_foil_extreme_4b_rebound","relative_strength_reversal","optionality_buffer"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["extreme_4b_blowoff","valuation_peak_watch"],"stage4c_evidence_fields":["ev_demand_slowdown_watch","utilization_pressure_watch","margin_fcf_pressure_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.45,"MFE_90D_pct":107.68,"MFE_180D_pct":107.68,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.88,"MAE_90D_pct":-4.88,"MAE_180D_pct":-4.88,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":200000.0,"drawdown_after_peak_pct":-53.3,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.48,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"blanket hard 4C would overblock a massive 4B timing rally; price-only blowoff still cannot become Green without non-price recovery","four_b_evidence_type":["extreme_4b_rebound","valuation_peak_watch"],"four_c_protection_label":"timing_overblock_counterexample_then_delayed_4c_watch","trigger_outcome_label":"counterexample_premature_4c_extreme_4b_blowoff","current_profile_verdict":"current_profile_overblocks_if_all_EV_material_slowdown_equal","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["old_profile_caveat_and_copper_foil_chemical_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C14_011790_2024_03_06_96300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window; copper-foil boundary","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_CHUNBO_278280_2024_03_06_ELECTROLYTE_ADDITIVE_UTILIZATION_HARD_4C","trigger_id":"CHUNBO_278280_2024_03_06_STAGE4C_ELECTROLYTE_UTILIZATION_SLOWDOWN","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":54,"stage_label_before":"Stage2 false bounce risk / late 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":39,"stage_label_after":"Stage4C hard utilization/ASP protection","changed_components":["backlog_visibility_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Electrolyte/additive recovery beta lacked customer/margin/FCF bridge and later collapsed.","MFE_90D_pct":3.93,"MAE_90D_pct":-26.18,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_4C_too_late_if_additive_recovery_beta_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_LOTTEENERGYMATERIALS_020150_2024_03_06_COPPER_FOIL_4B_TIMING_OVERBLOCK","trigger_id":"LOTTEENERGYMATERIALS_020150_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2-watch / 4B timing window","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch with delayed C14 4C recheck","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Immediate hard 4C would have overblocked a large 4B bounce; post-peak drawdown still blocks Green without margin/FCF proof.","MFE_90D_pct":64.22,"MAE_90D_pct":-1.66,"score_return_alignment_label":"timing_overblock_counterexample","current_profile_verdict":"current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_SKC_011790_2024_03_06_COPPER_FOIL_EXTREME_4B_TIMING_OVERBLOCK","trigger_id":"SKC_011790_2024_03_06_STAGE2_4B_TIMING_COUNTEREXAMPLE","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-watch / extreme 4B timing window","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch with extreme 4B blowoff audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"The 4B rally was real but price-only blowoff cannot become Green without utilization/margin/FCF confirmation.","MFE_90D_pct":107.68,"MAE_90D_pct":-4.88,"score_return_alignment_label":"timing_overblock_counterexample_then_4b_audit","current_profile_verdict":"current_profile_overblocks_if_all_EV_material_slowdown_equal"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"130","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overblocks_if_hard_4c_fires_before_4b_exhaustion"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 130
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C02_POWER_GRID_DATACENTER_CAPEX, C14_EV_DEMAND_SLOWDOWN_4B_4C_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local C14 loops 128 and 129, C14 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C14 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/278/278280.json
  - atlas/symbol_profiles/020/020150.json
  - atlas/symbol_profiles/011/011790.json
- Rejected local duplicate C14 symbols:
  - 247540, 066970, 373220
  - 003670, 361610, 006400
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R3_loop_129_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
