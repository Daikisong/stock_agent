# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
selected_round: R2
selected_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: GLASS_SUBSTRATE_ADVANCED_PACKAGING_EQUIPMENT_VALUATION_BLOWOFF_4B
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

This is the corrected valid run after the accidental duplicate loop110 materialization attempt. Loop110 already existed; this loop is loop111 and uses new C09 symbols only.

This loop adds 3 new independent C09 rows and moves C09 from static 15 rows to local projected 18 after loop110, then to projected 21 after this loop.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C09:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C09 -> C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

C09 is the advanced-equipment valuation blowoff archetype. The market can briefly treat a new equipment label like a rocket engine, but the calibration asks whether order conversion, margin, revision, and FCF are actually bolted to the frame.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C09 static rows | 15 |
| C09 static symbols | 11 |
| C09 good/bad Stage2 | 6 / 3 |
| C09 4B/4C | 1 / 2 |
| C09 URL pending/proxy | 15 / 9 |
| static top covered symbols | 039030(2), 084370(2), 140860(2), 240810(2), 036810(1), 036930(1) |
| local C09 loop110 projected rows | 18 |
| this loop projected rows | 21 |

Selected symbols avoid static C09 top-covered symbols and local C09 loop110 symbols `031980`, `348210`, and `101490`.

| symbol | company | status |
|---|---|---|
| 161580 | 필옵틱스 | new local C09 symbol; reduced weight due to share-count drift watch |
| 089970 | 브이엠 / 에이피티씨 | new local C09 symbol |
| 064290 | 인텍플러스 | new local C09 symbol |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C09 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 161580 / 2024-03-06 | true | true | profile_clean_but_share_count_drift_watch | true, reduced weight |
| 089970 / 2024-03-06 | true | true | clean_180D_window | true |
| 064290 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 필옵틱스 profile corporate-action candidates are old, but the 2024 row stream shows share-count drift; this row is retained with reduced independent evidence weight 0.80 and explicit caveat.
- 브이엠/에이피티씨 has zero corporate-action candidates.
- 인텍플러스 has zero corporate-action candidates.
- GST(083450) was rejected because its profile has 2024-06-26 and 2024-07-24 corporate-action candidates inside the candidate forward window.
- The accidental loop110 duplicate materialization is not counted as a new run.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GLASS_SUBSTRATE_ADVANCED_PACKAGING_EQUIPMENT_VALUATION_BLOWOFF_4B | C09 | glass-substrate/advanced packaging equipment can blow off violently and needs 4B audit |
| ADVANCED_ETCH_EQUIPMENT_MEMORY_CAPEX_PREMIUM_4B_WATCH | C09 | etch equipment capex rerating can work but full-window drawdown requires 4B |
| ADVANCED_INSPECTION_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE | C09 | inspection premium without order/margin/revision bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C09_PHILOPTICS_161580_2024_03_06_GLASS_SUBSTRATE_ADVANCED_PACKAGING_BLOWOFF | 161580 | 필옵틱스 | 4B_overlay_success | positive | advanced packaging/glass substrate event captured 189% MFE and then large drawdown |
| C09_VM_APTC_089970_2024_03_06_ADVANCED_ETCH_EQUIPMENT_RERATING_4B | 089970 | 브이엠/에이피티씨 | 4B_overlay_success | positive | advanced etch route captured 48% MFE and later collapsed below entry |
| C09_INTEKPLUS_064290_2024_03_06_ADVANCED_INSPECTION_PREMIUM_FAIL | 064290 | 인텍플러스 | failed_rerating | counterexample | inspection premium had ~1% MFE and severe MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 1 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 161580 | source_proxy_only | glass substrate / advanced packaging equipment event premium | required before promotion |
| 089970 | source_proxy_only | advanced etch equipment / memory capex route | required before promotion |
| 064290 | source_proxy_only | advanced inspection premium but bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 161580 | atlas/ohlcv_tradable_by_symbol_year/161/161580/2024.csv | atlas/symbol_profiles/161/161580.json |
| 089970 | atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv | atlas/symbol_profiles/089/089970.json |
| 064290 | atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv | atlas/symbol_profiles/064/064290.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 13040 | glass substrate / advanced packaging equipment blowoff |
| VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 14100 | advanced etch equipment / memory capex route |
| INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION | Stage2 | 2024-03-06 | 2024-03-06 | 40450 | advanced inspection premium without order/margin/revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 161580 | 2024-03-06 | 13040 | 189.49 | -4.91 | 189.49 | -4.91 | 189.49 | -4.91 | 2024-04-05 | 37750 | -64.95 |
| 089970 | 2024-03-06 | 14100 | 20.57 | -12.06 | 48.58 | -12.06 | 48.58 | -41.70 | 2024-06-13 | 20950 | -60.76 |
| 064290 | 2024-03-06 | 40450 | 1.11 | -16.93 | 1.11 | -48.08 | 1.11 | -68.60 | 2024-03-07 | 40900 | -68.95 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 161580 | Stage2A/Yellow possible; 4B after event blowoff | extreme MFE and extreme post-peak drawdown | current_profile_4B_too_late |
| 089970 | Stage2A possible; 4B after etch equipment rerating | useful MFE and full-window collapse | current_profile_4B_too_late |
| 064290 | Stage2 risk if inspection premium is over-credited | almost no MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C09 interpretation:

- Stage2A can work when advanced equipment exposure is tied to actual order conversion and margin/revision bridge.
- Yellow/Green require order, customer, margin, revision, and FCF confirmation.
- Advanced-equipment label and valuation premium alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 161580 | 1.00 | 1.00 | valuation blowoff / event crowding | 4B audit required immediately after blowoff |
| 089970 | 0.67 | 1.00 | valuation rerating / cycle peak | full-window 4B audit required |
| 064290 | 1.00 | 1.00 | premium with weak follow-through | not Stage3 without bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 161580 | thesis_break_watch_only | not hard 4C, but 4B cap needed after blowoff |
| 089970 | thesis_break_watch_only | not hard 4C, but full-window cycle drawdown requires audit |
| 064290 | hard_4c_late | order/margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, advanced equipment exposure can support Stage2A only when order conversion, customer confirmation, margin bridge, revision, or FCF is visible. Valuation blowoff or event-crowded advanced-equipment labeling without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
confidence = medium
```

Candidate C09 rule:

```text
C09_advanced_equipment_conversion_bridge_required =
  advanced_equipment_or_advanced_materials_route
  AND (order_conversion OR customer_confirmation OR margin_bridge OR confirmed_revision OR fcf_conversion)

if valuation_premium and conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C09_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -20:
    classify_as C09_advanced_equipment_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 79.73 | -21.68 | 79.73 | -38.4 | 1 | useful but C09 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 79.73 | -21.68 | 79.73 | -38.4 | 1 | over-credits advanced-equipment premiums |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 119.03 | -8.48 | 119.03 | -23.3 | 0 | better after conversion bridge gate |
| P2 canonical_archetype_candidate_profile | C09 | 2 promoted + 1 guard | 119.03 | -8.48 | 119.03 | -23.3 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C09 guard | 2 promoted + 1 guard | 119.03 | -8.48 | 119.03 | -23.3 | 0 | adds advanced-equipment false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 161580 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 089970 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 064290 | Stage2 false positive if order/margin bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | mixed C09 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 15 -> local 18 -> projected 21; still need 9 to reach 30 |

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
new_axis_proposed: C09_advanced_equipment_conversion_bridge_required|C09_peak_proximity_4B_audit|C09_advanced_equipment_false_positive_guardrail
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
- Uses C09 Priority 0 coverage gap.
- Avoids static C09 top-covered symbols and local loop110 C09 symbols.
- Keeps 161580 with reduced weight due to 2024 share-count drift watch.
- Rejects GST(083450) due to 2024 corporate-action candidates in the forward window.
- Does not count the accidental duplicate loop110 materialization as a valid new run.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_advanced_equipment_conversion_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"064290 shows advanced-inspection premium can fail without order/margin/revision bridge while 161580/089970 work only as Stage2A with 4B audit","blocks 064290 false positive while preserving 161580/089970 Stage2A","PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT|VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT|INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C09_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"161580/089970 advanced-equipment reratings needed 4B audit after large MFE and drawdown","adds 4B audit after large C09 MFE without converting price-only peaks into Green","PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT|VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C09_advanced_equipment_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"064290 had near-zero MFE and severe MAE after advanced-inspection premium","requires order/customer/margin/revision/FCF bridge before Stage2/Yellow promotion","INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C09_PHILOPTICS_161580_2024_03_06_GLASS_SUBSTRATE_ADVANCED_PACKAGING_BLOWOFF","symbol":"161580","company_name":"필옵틱스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"GLASS_SUBSTRATE_ADVANCED_PACKAGING_EQUIPMENT_VALUATION_BLOWOFF_4B","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"profile corporate-action candidates are old, but 2024 share-count drift is flagged; independent weight reduced","independent_evidence_weight":0.8,"score_price_alignment":"advanced packaging/glass-substrate equipment narrative captured nearly 190% MFE, but violent post-peak drawdown required a C09 valuation blowoff audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C09 symbol; source_proxy_only evidence; share-count drift watch in 2024 row stream"}
{"row_type":"case","case_id":"C09_VM_APTC_089970_2024_03_06_ADVANCED_ETCH_EQUIPMENT_RERATING_4B","symbol":"089970","company_name":"브이엠","alias_at_trigger":"에이피티씨","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_ETCH_EQUIPMENT_MEMORY_CAPEX_PREMIUM_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"advanced etch equipment / memory capex rerating captured 48% MFE, but full-window post-peak drawdown required C09 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C09 symbol; zero corporate-action candidates in profile; name changed after trigger"}
{"row_type":"case","case_id":"C09_INTEKPLUS_064290_2024_03_06_ADVANCED_INSPECTION_PREMIUM_FAIL","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_INSPECTION_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"advanced inspection equipment premium produced only ~1% MFE and then severe MAE without order/margin/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C09 symbol; zero corporate-action candidates in profile"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT","case_id":"C09_PHILOPTICS_161580_2024_03_06_GLASS_SUBSTRATE_ADVANCED_PACKAGING_BLOWOFF","symbol":"161580","company_name":"필옵틱스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"GLASS_SUBSTRATE_ADVANCED_PACKAGING_EQUIPMENT_VALUATION_BLOWOFF_4B","sector":"AI / semiconductor / electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":13040.0,"evidence_available_at_that_date":"source_proxy_only: glass-substrate / advanced packaging equipment premium, event-crowding, order-cycle expectation, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["glass_substrate_equipment_route","advanced_packaging_equipment_route","event_crowding","relative_strength"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_blowoff","event_crowding","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161580/2024.csv","profile_path":"atlas/symbol_profiles/161/161580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":189.49,"MFE_90D_pct":189.49,"MFE_180D_pct":189.49,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.91,"MAE_90D_pct":-4.91,"MAE_180D_pct":-4.91,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":37750.0,"drawdown_after_peak_pct":-64.95,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_packaging_glass_substrate_blowoff_worked_but_requires_4B_audit","four_b_evidence_type":["valuation_blowoff","event_crowding"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"profile_clean_but_share_count_drift_watch","same_entry_group_id":"C09_161580_2024_03_06_13040","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"profile corporate-action candidates are old, but 2024 share-count drift is flagged","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT","case_id":"C09_VM_APTC_089970_2024_03_06_ADVANCED_ETCH_EQUIPMENT_RERATING_4B","symbol":"089970","company_name":"브이엠","alias_at_trigger":"에이피티씨","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_ETCH_EQUIPMENT_MEMORY_CAPEX_PREMIUM_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":14100.0,"evidence_available_at_that_date":"source_proxy_only: advanced etch equipment premium, memory capex route, relative strength and order-cycle expectation visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_etch_equipment_route","memory_capex_route","relative_strength","order_cycle_expectation"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv","profile_path":"atlas/symbol_profiles/089/089970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.57,"MFE_90D_pct":48.58,"MFE_180D_pct":48.58,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-12.06,"MAE_90D_pct":-12.06,"MAE_180D_pct":-41.7,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":20950.0,"drawdown_after_peak_pct":-60.76,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.67,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_etch_equipment_rerating_worked_but_full_window_peak_requires_C09_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_089970_2024_03_06_14100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION","case_id":"C09_INTEKPLUS_064290_2024_03_06_ADVANCED_INSPECTION_PREMIUM_FAIL","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_INSPECTION_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":40450.0,"evidence_available_at_that_date":"source_proxy_only: advanced inspection equipment premium visible, but order conversion, margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_inspection_premium","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_premium","bridge_absent"],"stage4c_evidence_fields":["order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.11,"MFE_90D_pct":1.11,"MFE_180D_pct":1.11,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.93,"MAE_90D_pct":-48.08,"MAE_180D_pct":-68.6,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":40900.0,"drawdown_after_peak_pct":-68.95,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_inspection_premium_not_C09_stage3_without_order_margin_revision_bridge","four_b_evidence_type":["valuation_premium","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_064290_2024_03_06_40450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_PHILOPTICS_161580_2024_03_06_GLASS_SUBSTRATE_ADVANCED_PACKAGING_BLOWOFF","trigger_id":"PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT","symbol":"161580","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-blowoff risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable with mandatory C09 4B audit","changed_components":["valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Extreme glass-substrate rerating worked, but C09 cannot convert event crowding into Green without order/margin/FCF bridge.","MFE_90D_pct":189.49,"MAE_90D_pct":-4.91,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_VM_APTC_089970_2024_03_06_ADVANCED_ETCH_EQUIPMENT_RERATING_4B","trigger_id":"VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT","symbol":"089970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-watch with C09 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Advanced etch rerating produced MFE, but full-window drawdown says Stage3 needs order/margin/revision conversion.","MFE_90D_pct":48.58,"MAE_90D_pct":-12.06,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_INTEKPLUS_064290_2024_03_06_ADVANCED_INSPECTION_PREMIUM_FAIL","trigger_id":"INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"Stage1/4C-watch, not C09 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Inspection premium without order/margin/revision bridge produced almost no upside and severe MAE.","MFE_90D_pct":1.11,"MAE_90D_pct":-48.08,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R2
completed_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted together with loop110, C09 moves to projected 21 rows and still needs 9 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C09 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/161/161580/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/161/161580.json
  - atlas/symbol_profiles/089/089970.json
  - atlas/symbol_profiles/064/064290.json
- Rejected local duplicate C09 symbols:
  - 031980, 348210, 101490
- Rejected due to candidate forward-window contamination risk:
  - atlas/symbol_profiles/083/083450.json
- Avoided static C09 top-covered symbols:
  - 039030, 084370, 140860, 240810, 036810, 036930
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
