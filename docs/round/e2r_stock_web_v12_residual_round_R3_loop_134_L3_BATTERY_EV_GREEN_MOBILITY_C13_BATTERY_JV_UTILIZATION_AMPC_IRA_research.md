# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_134_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round: R3
selected_loop: 134
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C_WITH_SHARE_COUNT_DRIFT
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

This is the corrected valid run after a duplicate C12 loop133 materialization path was discarded. C12 reached the local 30-row stability threshold at loop133, so this run moves to the next Priority 0 gap: C13.

This loop adds 3 new independent C13 rows and moves C13 from static 27 rows to projected 30 rows. The 30-row minimum stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C13:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C13 -> C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

C13 is the battery JV utilization / AMPC / IRA archetype. AMPC is not free alpha by itself. It behaves like a credit line: valuable only when utilization, qualified production, margin, working capital, and cash conversion make the credit usable.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C13 static rows | 27 |
| C13 need to 30 | 3 |
| C13 need to 50 | 23 |
| C13 investigation point | JV 가동률, AMPC, utilization, cash conversion |
| local previous C13 rows in this session | 0 |
| this loop projected rows | 30 |

Selected C13 symbols:

| symbol | company | status |
|---|---|---|
| 096770 | SK이노베이션 | new local C13 hard 4C AMPC/JV utilization case |
| 051910 | LG화학 | new local C13 parent look-through hard 4C case |
| 373220 | LG에너지솔루션 | new local C13 AMPC scale-buffer overblock counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate. 373220 appeared in prior C14 research, but the C13 mechanism and canonical key are different; it is reduced-weight to avoid symbol overcount.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 096770 / 2024-03-06 | true | true | forward_window_has_late_2024_corporate_action_candidate | true, weight 0.75 |
| 051910 / 2024-03-06 | true | true | clean_180D_window_zero_corporate_action_candidates | true, weight 1.00 |
| 373220 / 2024-03-06 | true | true | clean_180D_window | true, weight 0.80 |

Corporate-action notes:

- SK이노베이션 has a 2024-11-20 corporate-action candidate and share-count drift in the forward window, so it is retained as a reduced-weight guardrail row.
- LG화학 has zero corporate-action candidates.
- LG에너지솔루션 has zero corporate-action candidates, but the symbol was used in prior C14 overblock research; C13 evidence is reduced to avoid symbol overcount.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C_WITH_SHARE_COUNT_DRIFT | C13 | JV/AMPC narrative should become hard 4C when utilization and cash conversion are absent |
| PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_WITHOUT_MARGIN_FCF_BRIDGE | C13 | parent look-through AMPC/JV optionality needs margin/FCF bridge |
| CELL_SCALE_AMPC_CUSTOMER_BUFFER_OVERBLOCK_EXCEPTION | C13 | blanket AMPC/JV hard 4C can overblock scale leaders without confirmed utilization break |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C13_SKINNOVATION_096770_2024_03_06_SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C | 096770 | SK이노베이션 | hard_4c_protection_success | positive_protection | minor MFE, moderate MAE, and share-count/corporate-action drift |
| C13_LGCHEM_051910_2024_03_06_PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_FAIL | 051910 | LG화학 | hard_4c_protection_success | positive_protection | low MFE and deep 180D MAE without margin/FCF bridge |
| C13_LGES_373220_2024_03_06_CELL_SCALE_AMPC_BUFFER_OVERBLOCK_COUNTEREXAMPLE | 373220 | LG에너지솔루션 | overblock_counterexample | counterexample | scale/AMPC buffer prevents blanket hard 4C |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_protection_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| overblock_counterexample_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 096770 | source_proxy_only | JV/AMPC optionality but utilization/cash conversion and funding risk unresolved | required before promotion |
| 051910 | source_proxy_only | parent-level AMPC/JV look-through but margin/FCF bridge absent | required before promotion |
| 373220 | source_proxy_only | cell-scale AMPC/customer buffer against blanket hard 4C | required; useful as overblock counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 096770 | atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv | atlas/symbol_profiles/096/096770.json |
| 051910 | atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv | atlas/symbol_profiles/051/051910.json |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SKINNOVATION_096770_2024_03_06_STAGE4C_JV_UTILIZATION_AMPC_CASH_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 115700 | SK On/JV utilization and AMPC cash-conversion risk |
| LGCHEM_051910_2024_03_06_STAGE4C_PARENT_AMPC_JV_LOOKTHROUGH_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 441500 | parent AMPC/JV look-through without margin/FCF bridge |
| LGES_373220_2024_03_06_STAGE2_AMPC_SCALE_BUFFER_OVERBLOCK_COUNTEREXAMPLE | Stage2 | 2024-03-06 | 2024-03-06 | 387000 | AMPC scale/customer buffer overblock exception |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 096770 | 2024-03-06 | 115700 | 10.89 | -11.32 | 10.89 | -13.92 | 10.89 | -20.66 | 2024-03-18 | 128300 | -28.45 |
| 051910 | 2024-03-06 | 441500 | 6.68 | -14.95 | 6.68 | -23.78 | 6.68 | -39.41 | 2024-03-13 | 471000 | -43.21 |
| 373220 | 2024-03-06 | 387000 | 9.04 | -7.49 | 9.04 | -16.67 | 14.73 | -16.67 | 2024-10-08 | 444000 | -16.44 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 096770 | Stage2/AMPC optionality risk if JV narrative is over-credited | hard 4C protection needed | current_profile_4C_too_late |
| 051910 | parent AMPC/JV look-through could be over-credited | hard 4C protection worked | current_profile_4C_too_late |
| 373220 | blanket AMPC/JV hard 4C could be too broad | overblock counterexample | current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C13 interpretation:

- AMPC/JV narratives cannot promote Yellow/Green unless utilization, qualified production, margin, working-capital quality and cash conversion are visible.
- Parent look-through optionality needs a discount unless the cash bridge is direct.
- Cell-scale leaders can deserve an overblock exception when scale/customer/policy buffers are visible and utilization break is not confirmed.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 096770 | 0.90 | 1.00 | minor AMPC/JV bounce / drift watch | 4B should not override hard 4C |
| 051910 | 0.94 | 1.00 | parent AMPC look-through / bridge absent | not Stage3 without cash bridge |
| 373220 | 0.87 | 1.00 | AMPC scale buffer / customer scale | overblock exception, still not Green |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 096770 | hard_4c_success_reduced_weight | utilization/cash-conversion failure plus share-count drift required 4C |
| 051910 | hard_4c_success | parent look-through optionality failed without margin/FCF bridge |
| 373220 | overblock_counterexample | hard 4C should wait for confirmed utilization/cash-conversion break |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, AMPC/IRA/JV language should promote Stage2A only when qualified production, utilization, margin, working-capital quality and cash conversion are visible. If utilization or cash conversion is absent, route to hard 4C. If a cell leader has scale/customer/policy buffer and no confirmed utilization break, keep it as Stage2-watch with an overblock exception.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
confidence = medium
```

Candidate C13 rule:

```text
C13_jv_ampc_utilization_cash_bridge_required =
  battery_JV_or_AMPC_or_IRA_route
  AND (qualified_production OR utilization_recovery OR margin_bridge OR working_capital_quality OR confirmed_revision OR fcf_conversion)

if AMPC_JV_narrative and utilization_cash_bridge_absent:
    cap_stage = Stage4C
    do_not_allow_Stage3_Yellow_or_Green = true

if parent_lookthrough_AMPC and direct_cash_bridge_absent:
    apply_lookthrough_discount = true
    cap_stage = Stage1/Stage2-watch_or_4C

if cell_scale_customer_buffer and policy_buffer and not confirmed_utilization_break:
    classify_as C13_overblock_counterexample
    cap_stage = Stage2-watch_not_Green
    require delayed_4C_recheck

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 8.87 | -18.12 | 10.77 | -25.58 | 1 overblock | useful but C13 cash-bridge rule needed |
| P0b calibrated rollback | rollback | 3 | 8.87 | -18.12 | 10.77 | -25.58 | 1 overblock | over-credits AMPC/JV language or overblocks scale leader |
| P1 sector_specific_candidate_profile | L3 | 2 hard 4C + 1 overblock exception | 8.79 | -18.85 | 8.79 | -30.03 | 0 | better after utilization/cash bridge gate |
| P2 canonical_archetype_candidate_profile | C13 | 2 hard 4C + 1 overblock exception | 8.79 | -18.85 | 8.79 | -30.03 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C13 guard | 2 hard 4C + 1 overblock exception | 8.79 | -18.85 | 8.79 | -30.03 | 0 | adds AMPC/JV overblock guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 096770 | hard 4C aligned; AMPC/JV narrative lacked cash bridge | current_profile_4C_too_late |
| 051910 | hard 4C aligned; parent optionality lacked direct FCF bridge | current_profile_4C_too_late |
| 373220 | hard 4C overblock if scale AMPC buffer ignored | current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive protection | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | mixed C13 fine ids | 2 | 1 | 2 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 27 -> projected 30; reaches minimum stability threshold |

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
  - current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C
new_axis_proposed: C13_jv_ampc_utilization_cash_bridge_required|C13_parent_lookthrough_discount|C13_cell_scale_ampc_overblock_exception|share_count_drift_independent_weight_reduction
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
- Uses C13 Priority 0 coverage gap.
- Avoids local C12/C11 threshold-completion repetition.
- Keeps 096770 with reduced weight because of 2024-11-20 corporate-action/share-count drift watch.
- Keeps 373220 with reduced weight because same symbol appeared in prior local C14, though C13 mechanism is different.
- Treats 373220 as overblock counterexample, not a Green promotion.
- Discards the accidental duplicate C12 loop133 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated C12 loop133 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C13_jv_ampc_utilization_cash_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"096770/051910 show AMPC/JV optionality can fail without utilization and cash-conversion bridge","caps Stage2/Yellow when AMPC/JV narrative lacks qualified production, margin and FCF","SKINNOVATION_096770_2024_03_06_STAGE4C_JV_UTILIZATION_AMPC_CASH_RISK|LGCHEM_051910_2024_03_06_STAGE4C_PARENT_AMPC_JV_LOOKTHROUGH_RISK",2,2,0,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C13_parent_lookthrough_discount,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"051910 parent look-through AMPC/JV optionality did not translate into direct margin/FCF proof","discounts parent-level optionality unless cash bridge is direct","LGCHEM_051910_2024_03_06_STAGE4C_PARENT_AMPC_JV_LOOKTHROUGH_RISK",1,1,0,medium,canonical_shadow_only,"parent look-through guardrail"
shadow_weight,C13_cell_scale_ampc_overblock_exception,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"373220 shows blanket AMPC/JV hard 4C can overblock a cell-scale leader with policy/customer buffer","keeps 373220 as Stage2-watch with delayed 4C recheck rather than immediate hard 4C","LGES_373220_2024_03_06_STAGE2_AMPC_SCALE_BUFFER_OVERBLOCK_COUNTEREXAMPLE",1,1,1,medium,canonical_shadow_only,"overblock guardrail"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"096770 has 2024 share-count/corporate-action drift during the validation window","keeps row usable but lowers independent evidence weight","SKINNOVATION_096770_2024_03_06_STAGE4C_JV_UTILIZATION_AMPC_CASH_RISK",1,1,0,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C13_SKINNOVATION_096770_2024_03_06_SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C","symbol":"096770","company_name":"SK이노베이션","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C_WITH_SHARE_COUNT_DRIFT","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"SKINNOVATION_096770_2024_03_06_STAGE4C_JV_UTILIZATION_AMPC_CASH_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2024-11-20 corporate-action candidate and share-count drift in forward window; retained as reduced-weight guardrail","independent_evidence_weight":0.75,"score_price_alignment":"SK On/JV/AMPC narrative produced only 10.89% MFE before roughly -20.66% forward MAE and share-count drift, so AMPC/JV language needed hard utilization/cash-conversion gating","current_profile_verdict":"current_profile_4C_too_late_if_AMPC_JV_narrative_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C13 symbol; reduced weight due to 2024-11-20 corporate-action/share-count drift watch"}
{"row_type":"case","case_id":"C13_LGCHEM_051910_2024_03_06_PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_FAIL","symbol":"051910","company_name":"LG화학","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_WITHOUT_MARGIN_FCF_BRIDGE","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"LGCHEM_051910_2024_03_06_STAGE4C_PARENT_AMPC_JV_LOOKTHROUGH_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"battery/JV/AMPC look-through narrative produced only 6.68% MFE and then about -39.41% 180D MAE, validating hard 4C when utilization and FCF conversion are absent","current_profile_verdict":"current_profile_4C_too_late_if_parent_AMPC_optional_value_overcredited","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; parent look-through false-positive guard"}
{"row_type":"case","case_id":"C13_LGES_373220_2024_03_06_CELL_SCALE_AMPC_BUFFER_OVERBLOCK_COUNTEREXAMPLE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_SCALE_AMPC_CUSTOMER_BUFFER_OVERBLOCK_EXCEPTION","case_type":"overblock_counterexample","positive_or_counterexample":"counterexample","best_trigger":"LGES_373220_2024_03_06_STAGE2_AMPC_SCALE_BUFFER_OVERBLOCK_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol used earlier for C14, but C13 mechanism is AMPC/JV scale buffer; independent weight reduced to avoid overcount","independent_evidence_weight":0.8,"score_price_alignment":"cell-scale/AMPC buffer had limited 180D MAE around -16.67% and later +14.73% MFE, so blanket C13 hard 4C would overblock without confirmed utilization/cash-conversion break","current_profile_verdict":"current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C","price_source":"Songdaiki/stock-web","notes":"clean price profile; reduced weight only because symbol appeared in prior local C14 overblock work"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SKINNOVATION_096770_2024_03_06_STAGE4C_JV_UTILIZATION_AMPC_CASH_RISK","case_id":"C13_SKINNOVATION_096770_2024_03_06_SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C","symbol":"096770","company_name":"SK이노베이션","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C_WITH_SHARE_COUNT_DRIFT","sector":"battery / EV / green mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":115700.0,"evidence_available_at_that_date":"source_proxy_only: SK On/JV utilization, IRA/AMPC narrative, cash-conversion pressure and parent funding/dilution risk visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["SK_On_JV_AMPC_narrative","battery_turnaround_optionality","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["minor_bounce","valuation_peak_watch","share_count_drift_watch"],"stage4c_evidence_fields":["JV_utilization_pressure","cash_conversion_absent","funding_risk","share_count_drift_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.89,"MFE_90D_pct":10.89,"MFE_180D_pct":10.89,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.32,"MAE_90D_pct":-13.92,"MAE_180D_pct":-20.66,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-18","peak_price":128300.0,"drawdown_after_peak_pct":-28.45,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"minor AMPC/JV bounce should not override utilization/cash-conversion hard 4C, especially with share-count drift","four_b_evidence_type":["minor_rebound","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success_reduced_weight","trigger_outcome_label":"positive_protection_low_mfe_moderate_mae_share_count_drift","current_profile_verdict":"current_profile_4C_too_late_if_AMPC_JV_narrative_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024_11_20_corporate_action_candidate_share_count_drift_reduced_weight"],"corporate_action_window_status":"forward_window_has_late_2024_corporate_action_candidate","same_entry_group_id":"C13_096770_2024_03_06_115700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"2024-11-20 corporate-action/share-count drift watch","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LGCHEM_051910_2024_03_06_STAGE4C_PARENT_AMPC_JV_LOOKTHROUGH_RISK","case_id":"C13_LGCHEM_051910_2024_03_06_PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_FAIL","symbol":"051910","company_name":"LG화학","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_WITHOUT_MARGIN_FCF_BRIDGE","sector":"battery / EV / green mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":441500.0,"evidence_available_at_that_date":"source_proxy_only: parent-level battery/JV/AMPC look-through narrative visible, but utilization, margin, FCF and parent cash-conversion bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_JV_AMPC_lookthrough","cell_material_parent_optionality","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["minor_rebound","valuation_peak_watch"],"stage4c_evidence_fields":["utilization_pressure","parent_cash_conversion_absent","margin_fcf_bridge_absent","lookthrough_discount"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.68,"MFE_90D_pct":6.68,"MFE_180D_pct":6.68,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-14.95,"MAE_90D_pct":-23.78,"MAE_180D_pct":-39.41,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":471000.0,"drawdown_after_peak_pct":-43.21,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"parent AMPC/JV look-through bounce should not override absent utilization/margin/FCF bridge","four_b_evidence_type":["minor_rebound","lookthrough_discount"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protection_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late_if_parent_AMPC_optional_value_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_zero_corporate_action_candidates","same_entry_group_id":"C13_051910_2024_03_06_441500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LGES_373220_2024_03_06_STAGE2_AMPC_SCALE_BUFFER_OVERBLOCK_COUNTEREXAMPLE","case_id":"C13_LGES_373220_2024_03_06_CELL_SCALE_AMPC_BUFFER_OVERBLOCK_COUNTEREXAMPLE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_SCALE_AMPC_CUSTOMER_BUFFER_OVERBLOCK_EXCEPTION","sector":"battery / EV / green mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":387000.0,"evidence_available_at_that_date":"source_proxy_only: cell-scale AMPC buffer, customer diversification, US policy/IRA optionality and scale advantage visible; confirmed utilization break not yet hard 4C; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cell_scale_buffer","AMPC_policy_buffer","customer_diversification","relative_strength_partial"],"stage3_evidence_fields":["customer_scale_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["AMPC_scale_buffer","valuation_peak_watch"],"stage4c_evidence_fields":["utilization_pressure_watch","cash_conversion_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.04,"MFE_90D_pct":9.04,"MFE_180D_pct":14.73,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.49,"MAE_90D_pct":-16.67,"MAE_180D_pct":-16.67,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"drawdown_after_peak_pct":-16.44,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"blanket C13 hard 4C would overblock cell-scale AMPC buffer without confirmed utilization/cash-conversion break","four_b_evidence_type":["AMPC_scale_buffer","customer_scale_buffer"],"four_c_protection_label":"overblock_counterexample","trigger_outcome_label":"counterexample_overbroad_AMPC_JV_4C","current_profile_verdict":"current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["prior_local_C14_symbol_overlap_reduced_weight"],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_373220_2024_03_06_387000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol used in prior C14 but different C13 AMPC/JV mechanism","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C13_SKINNOVATION_096770_2024_03_06_SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C","trigger_id":"SKINNOVATION_096770_2024_03_06_STAGE4C_JV_UTILIZATION_AMPC_CASH_RISK","symbol":"096770","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2/AMPC optionality risk, late 4C","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":3,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage4C utilization/cash-conversion protection","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"AMPC/JV optionality lacked confirmed utilization and cash conversion; share-count drift adds validation-quality risk.","MFE_90D_pct":10.89,"MAE_90D_pct":-13.92,"score_return_alignment_label":"hard_4c_protection_success_reduced_weight","current_profile_verdict":"current_profile_4C_too_late_if_AMPC_JV_narrative_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C13_LGCHEM_051910_2024_03_06_PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_FAIL","trigger_id":"LGCHEM_051910_2024_03_06_STAGE4C_PARENT_AMPC_JV_LOOKTHROUGH_RISK","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 parent AMPC/JV look-through risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":43,"stage_label_after":"Stage4C parent look-through discount / cash-conversion protection","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Parent-level AMPC/JV optional value did not translate into utilization/margin/FCF proof.","MFE_90D_pct":6.68,"MAE_90D_pct":-23.78,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_4C_too_late_if_parent_AMPC_optional_value_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C13_LGES_373220_2024_03_06_CELL_SCALE_AMPC_BUFFER_OVERBLOCK_COUNTEREXAMPLE","trigger_id":"LGES_373220_2024_03_06_STAGE2_AMPC_SCALE_BUFFER_OVERBLOCK_COUNTEREXAMPLE","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-watch / AMPC scale buffer","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch with C13 overblock exception","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"AMPC scale/customer buffer prevents blanket hard 4C without confirmed utilization/cash-conversion break.","MFE_90D_pct":9.04,"MAE_90D_pct":-16.67,"score_return_alignment_label":"overblock_counterexample","current_profile_verdict":"current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"134","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overblocks_if_all_AMPC_JV_risk_treated_as_hard_4C"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 134
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```

If this loop is accepted, C13 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C13 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/096/096770.json
  - atlas/symbol_profiles/051/051910.json
  - atlas/symbol_profiles/373/373220.json
- Rejected duplicate materialization path:
  - e2r_stock_web_v12_residual_round_R3_loop_133_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
