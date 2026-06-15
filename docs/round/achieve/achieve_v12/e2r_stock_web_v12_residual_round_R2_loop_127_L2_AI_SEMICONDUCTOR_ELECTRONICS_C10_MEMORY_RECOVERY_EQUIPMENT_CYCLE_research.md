# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_127_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 127
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_ORDER_CYCLE_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after an accidental duplicate loop126 materialization path was discarded. Loop126 already used `319660`, `039440`, and `005290`; this loop uses new C10 symbol/trigger/date combinations only.

This loop adds 3 new independent C10 rows and moves C10 from static 21 rows to local projected 27 after loops 125/126, then to projected 30 after this loop. The 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C10:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C10 -> C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

C10 is the memory recovery equipment-cycle archetype. The bridge is not “memory looks better”; it is actual equipment/consumable order conversion, utilization, margin, revision and FCF. Without that bridge, recovery beta is a bright sign but not a load-bearing beam.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C10 static rows | 21 |
| C10 static symbols | 18 |
| C10 good/bad Stage2 | 6 / 6 |
| C10 4B/4C | 3 / 3 |
| C10 URL pending/proxy | 18 / 12 |
| C10 top covered symbols | 036930(3), 074600(2), 003160(1), 031980(1), 036540(1), 039030(1) |
| local C10 loop125 projected rows | 24 |
| local C10 loop126 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid local C10 loop125 symbols `166090`, `064760`, `014680` and loop126 symbols `319660`, `039440`, `005290`.

| symbol | company | status |
|---|---|---|
| 144960 | 뉴파워프라즈마 | new local C10 symbol |
| 083310 | 엘오티베큠 | new local C10 symbol |
| 067310 | 하나마이크론 | new local C10 symbol; C08 boundary/share-count drift watch |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate. The duplicate loop126 materialization created during this execution is explicitly rejected.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 144960 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 083310 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 067310 / 2024-03-06 | true | true | old_profile_caveat_but_2024_share_count_drift_watch | true, reduced weight 0.75 |

Corporate-action notes:

- 뉴파워프라즈마 has an old corporate-action candidate in 2019 only; selected 2024 window is clean.
- 엘오티베큠 has old corporate-action candidates in 2007 only; selected 2024 window is clean.
- 하나마이크론 has old corporate-action candidates outside the selected entry but visible 2024 share-count drift and C08 boundary contamination, so it is retained only as a reduced-weight guardrail row.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_ORDER_CYCLE_4B_WATCH | C10 | plasma/equipment recovery can support Stage2A, but memory-cycle 4B audit is mandatory |
| VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_WITHOUT_ORDER_MARGIN_BRIDGE | C10 | vacuum-equipment beta without order/margin bridge is false-positive risk |
| OSAT_MEMORY_RECOVERY_EVENT_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE | C10 | OSAT/memory event premium needs clean order/margin/revision bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C10_NPP_144960_2024_03_06_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_4B | 144960 | 뉴파워프라즈마 | 4B_overlay_success | positive | plasma/equipment recovery produced 46.02% MFE |
| C10_LOTVACUUM_083310_2024_03_06_VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_FAIL | 083310 | 엘오티베큠 | failed_rerating | counterexample | vacuum-equipment beta had only 6.18% MFE and deep MAE |
| C10_HANAMICRON_067310_2024_03_06_OSAT_MEMORY_RECOVERY_EVENT_FAIL | 067310 | 하나마이크론 | failed_rerating | counterexample | OSAT/memory event had MFE but severe full-window collapse and share-count drift |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 3 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 144960 | source_proxy_only | plasma/equipment utilization recovery and order-cycle expectation | required before promotion |
| 083310 | source_proxy_only | vacuum-equipment beta but order/margin bridge absent | required; useful as counterexample |
| 067310 | source_proxy_only | OSAT/memory event premium but clean order/margin bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 144960 | atlas/ohlcv_tradable_by_symbol_year/144/144960/2024.csv | atlas/symbol_profiles/144/144960.json |
| 083310 | atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv | atlas/symbol_profiles/083/083310.json |
| 067310 | atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv | atlas/symbol_profiles/067/067310.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 4965 | plasma/equipment recovery order-cycle |
| LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA | Stage2 | 2024-03-06 | 2024-03-06 | 22650 | vacuum-equipment beta without order/margin bridge |
| HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY | Stage2 | 2024-03-06 | 2024-03-06 | 27050 | OSAT/memory event without clean order/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 144960 | 2024-03-06 | 4965 | 28.50 | -4.43 | 46.02 | -4.43 | 46.02 | -11.68 | 2024-06-10 | 7250 | -39.52 |
| 083310 | 2024-03-06 | 22650 | 6.18 | -11.70 | 6.18 | -40.09 | 6.18 | -63.89 | 2024-03-08 | 24050 | -65.99 |
| 067310 | 2024-03-06 | 27050 | 27.54 | -6.28 | 27.54 | -28.84 | 27.54 | -65.90 | 2024-04-04 | 34500 | -73.57 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 144960 | Stage2A possible; 4B after equipment recovery rerating | high MFE but cycle drawdown | current_profile_4B_too_late |
| 083310 | Stage2 risk if vacuum-equipment beta is over-credited | low MFE and high 90D/180D MAE | current_profile_false_positive |
| 067310 | Stage2 risk if OSAT memory event is over-credited | MFE but full-window collapse and share-count drift | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C10 interpretation:

- Stage2A can work when recovery beta is tied to equipment order conversion, utilization, margin, revision, and FCF.
- Yellow/Green require non-price order or margin evidence.
- Vacuum-equipment beta and OSAT memory event premium without clean bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 144960 | 0.68 | 1.00 | plasma/equipment recovery / valuation rerating | full-window C10 4B audit required |
| 083310 | 1.00 | 1.00 | vacuum-equipment beta / bridge absent | not Stage3 without order/margin/revision bridge |
| 067310 | 0.78 | 1.00 | OSAT memory event / bridge absent / drift watch | not Stage3 without clean order/margin/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 144960 | thesis_break_watch_only | not hard 4C, but cycle 4B cap needed after rerating |
| 083310 | hard_4c_late | order/margin/revision bridge absence should have capped Stage2 earlier |
| 067310 | hard_4c_late | bridge absence plus share-count drift should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, memory recovery should promote Stage2A only when equipment order conversion, utilization recovery, margin bridge, revision or FCF is visible. Vacuum-equipment beta or OSAT memory event premium without clean bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
confidence = medium
```

Candidate C10 rule:

```text
C10_memory_recovery_order_margin_bridge_required =
  memory_recovery_equipment_or_consumable_route
  AND (order_conversion OR utilization_recovery OR consumable_repeat_demand OR margin_bridge OR confirmed_revision OR fcf_conversion)

if vacuum_equipment_beta and order_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if osat_memory_event and clean_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C10_memory_cycle_4B_audit = true

if MFE_90D < 10 and MAE_90D < -25 and bridge_absent:
    classify_as C10_equipment_beta_false_positive_guardrail

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 26.58 | -24.45 | 26.58 | -47.16 | 2 | useful but C10 beta bridge still loose |
| P0b calibrated rollback | rollback | 3 | 26.58 | -24.45 | 26.58 | -47.16 | 2 | over-credits equipment/OSAT beta |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 46.02 | -4.43 | 46.02 | -11.68 | 0 | better after order/margin bridge gate |
| P2 canonical_archetype_candidate_profile | C10 | 1 promoted + 2 guard | 46.02 | -4.43 | 46.02 | -11.68 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C10 guard | 1 promoted + 2 guard | 46.02 | -4.43 | 46.02 | -11.68 | 0 | adds equipment/OSAT beta false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 144960 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 083310 | Stage2 false positive if order/margin bridge not enforced | current_profile_false_positive |
| 067310 | Stage2 false positive if clean bridge/drift guard not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed C10 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 27 -> projected 30; reaches minimum stability threshold |

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
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C10_memory_recovery_order_margin_bridge_required|C10_memory_cycle_4B_audit|C10_equipment_beta_false_positive_guardrail|C10_osat_event_false_positive_guardrail|share_count_drift_independent_weight_reduction
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
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
- Uses C10 Priority 0 coverage gap.
- Avoids local C10 loop125 and loop126 symbols.
- Keeps 067310 with reduced weight because of C08 boundary and 2024 share-count drift watch.
- Discards the accidental duplicate loop126 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop126 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_memory_recovery_order_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"083310/067310 show equipment or OSAT beta can fail without order/margin/revision bridge while 144960 works only as Stage2A with 4B audit","blocks two false positives while preserving 144960 Stage2A","NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY|LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA|HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C10_memory_cycle_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"144960 memory/plasma equipment recovery needed full-window 4B audit after high MFE and drawdown","adds 4B audit after C10 memory-cycle MFE without converting price-only peaks into Green","NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C10_equipment_beta_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"083310 had low MFE and high MAE after vacuum-equipment beta without order/margin bridge","requires confirmed order/utilization/margin/revision/FCF bridge before Stage2/Yellow promotion","LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C10_osat_event_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"067310 had MFE but severe full-window drawdown after OSAT memory event without clean order/margin/revision bridge","requires confirmed order/utilization/margin/revision/FCF bridge before Stage2/Yellow promotion","HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY",1,1,1,medium,canonical_shadow_only,"OSAT/event false-positive guardrail"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"067310 has 2024 share-count drift and C08 boundary contamination, so it should not overcount independent C10 evidence","keeps row usable but lowers independent evidence weight","HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY",1,1,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C10_NPP_144960_2024_03_06_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_4B","symbol":"144960","company_name":"뉴파워프라즈마","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_ORDER_CYCLE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate only in 2019; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"plasma power / memory equipment recovery route captured 46% MFE, but later drawdown required C10 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C10 symbol versus loops 125/126; clean 2024 window with old profile caveat only"}
{"row_type":"case","case_id":"C10_LOTVACUUM_083310_2024_03_06_VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_FAIL","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_WITHOUT_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2007; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"vacuum-equipment memory recovery beta produced only 6% MFE and then deep 90D/180D MAE without order, margin, revision or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C10 symbol; clear recovery-beta failure guard"}
{"row_type":"case","case_id":"C10_HANAMICRON_067310_2024_03_06_OSAT_MEMORY_RECOVERY_EVENT_FAIL","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"OSAT_MEMORY_RECOVERY_EVENT_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"C08 static boundary and 2024 share-count drift; usable for C10 guard only with reduced weight","independent_evidence_weight":0.75,"score_price_alignment":"OSAT/memory recovery event premium produced 27% MFE but then severe full-window drawdown without clean order/margin/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C10 symbol; C08 boundary and share-count drift require reduced independent weight"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY","case_id":"C10_NPP_144960_2024_03_06_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_4B","symbol":"144960","company_name":"뉴파워프라즈마","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_ORDER_CYCLE_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":4965.0,"evidence_available_at_that_date":"source_proxy_only: memory recovery, plasma power/equipment utilization recovery, order-cycle expectation and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_recovery_cycle","plasma_power_equipment_route","utilization_recovery","relative_strength"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["cycle_peak_watch","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/144/144960/2024.csv","profile_path":"atlas/symbol_profiles/144/144960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.5,"MFE_90D_pct":46.02,"MFE_180D_pct":46.02,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.43,"MAE_90D_pct":-4.43,"MAE_180D_pct":-11.68,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-10","peak_price":7250.0,"drawdown_after_peak_pct":-39.52,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.68,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"plasma_power_memory_equipment_recovery_worked_as_stage2a_but_full_window_peak_requires_C10_4B_cycle_audit","four_b_evidence_type":["valuation_rerating","memory_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C10_144960_2024_03_06_4965","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA","case_id":"C10_LOTVACUUM_083310_2024_03_06_VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_FAIL","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_WITHOUT_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":22650.0,"evidence_available_at_that_date":"source_proxy_only: vacuum-equipment memory recovery beta visible, but confirmed order conversion, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["vacuum_equipment_beta","memory_recovery_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["equipment_order_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","profile_path":"atlas/symbol_profiles/083/083310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.18,"MFE_90D_pct":6.18,"MFE_180D_pct":6.18,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.7,"MAE_90D_pct":-40.09,"MAE_180D_pct":-63.89,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":24050.0,"drawdown_after_peak_pct":-65.99,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"vacuum_equipment_beta_not_C10_stage3_without_order_margin_revision_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C10_083310_2024_03_06_22650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY","case_id":"C10_HANAMICRON_067310_2024_03_06_OSAT_MEMORY_RECOVERY_EVENT_FAIL","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"OSAT_MEMORY_RECOVERY_EVENT_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":27050.0,"evidence_available_at_that_date":"source_proxy_only: OSAT/memory recovery event premium and relative strength visible, but clean order/margin/revision/FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["osat_memory_recovery_event","semiconductor_cycle_narrative","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","share_count_drift_watch","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["order_bridge_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv","profile_path":"atlas/symbol_profiles/067/067310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.54,"MFE_90D_pct":27.54,"MFE_180D_pct":27.54,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.28,"MAE_90D_pct":-28.84,"MAE_180D_pct":-65.9,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":34500.0,"drawdown_after_peak_pct":-73.57,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"osat_memory_recovery_event_not_C10_stage3_without_clean_order_margin_revision_bridge","four_b_evidence_type":["event_premium","bridge_absent","share_count_drift_watch"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mfe_then_high_mae_bridge_absent_reduced_weight","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["C08_C10_boundary_and_share_count_drift_reduced_weight"],"corporate_action_window_status":"old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C10_067310_2024_03_06_27050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C08 static boundary and 2024 share-count drift; guardrail use only","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_NPP_144960_2024_03_06_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY_4B","trigger_id":"NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY","symbol":"144960","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-watch with C10 4B cycle audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Plasma/equipment recovery worked, but Green needs realized order, utilization, margin, revision and FCF conversion.","MFE_90D_pct":46.02,"MAE_90D_pct":-4.43,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_LOTVACUUM_083310_2024_03_06_VACUUM_EQUIPMENT_MEMORY_RECOVERY_BETA_FAIL","trigger_id":"LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA","symbol":"083310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2 false-positive / vacuum-equipment beta risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage1/4C-watch, not C10 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Vacuum-equipment beta without order/margin bridge produced low MFE and deep drawdown.","MFE_90D_pct":6.18,"MAE_90D_pct":-40.09,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_HANAMICRON_067310_2024_03_06_OSAT_MEMORY_RECOVERY_EVENT_FAIL","trigger_id":"HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY","symbol":"067310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / OSAT memory recovery risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage1/4C-watch, not C10 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"OSAT/memory recovery event without clean bridge produced MFE but severe full-window collapse and share-count drift watch.","MFE_90D_pct":27.54,"MAE_90D_pct":-28.84,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R2
completed_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local C10 loops 125 and 126, C10 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C10 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/144/144960/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/144/144960.json
  - atlas/symbol_profiles/083/083310.json
  - atlas/symbol_profiles/067/067310.json
- Rejected local duplicate C10 symbols:
  - 166090, 064760, 014680
  - 319660, 039440, 005290
- Avoided static C10 top-covered symbols where possible:
  - 036930, 074600, 003160, 031980, 036540, 039030
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_126_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
