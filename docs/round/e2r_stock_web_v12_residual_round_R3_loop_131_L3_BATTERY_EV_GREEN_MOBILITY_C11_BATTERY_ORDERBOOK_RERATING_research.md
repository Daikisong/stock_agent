# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_131_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 131
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_FCF_RERATING_4B_WATCH
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

This is the corrected valid run after a duplicate C14 loop130 materialization path was discarded. C14 reached the local 30-row stability threshold at loop130, so this loop moves to the next Priority 0 gap: C11.

This loop adds 3 new independent C11 rows and moves C11 from static 23 rows to projected 26 rows. It still needs 4 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C11:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C11 -> C11_BATTERY_ORDERBOOK_RERATING
```

C11 is the battery orderbook rerating archetype. The mechanism is simple: orderbook is the warehouse receipt, but margin, revision, working capital, and FCF are the cash register. If the receipt never reaches the register, the rerating decays into beta.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C11 static rows | 23 |
| C11 need to 30 | 7 |
| C11 need to 50 | 27 |
| C11 investigation point | 배터리 orderbook이 FCF/마진으로 전환되는지 검증 |
| local previous C11 rows in this session | 0 |
| this loop projected rows | 26 |

Selected symbols avoid local C14 loop128/129/130 symbols and local C06/C07/C08/C09/C10 threshold-completion loops.

| symbol | company | status |
|---|---|---|
| 137400 | 피엔티 | new local C11 positive/4B, reduced weight due to share-count drift |
| 222080 | 씨아이에스 | new local C11 counterexample, reduced weight due to share-count drift |
| 372170 | 윤성에프앤씨 | new local C11 clean counterexample |

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
| 137400 / 2024-03-06 | true | true | old_profile_caveat_but_2024_share_count_drift_watch | true, reduced weight 0.80 |
| 222080 / 2024-03-06 | true | true | old_profile_caveat_but_2024_share_count_drift_watch | true, reduced weight 0.80 |
| 372170 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 피엔티 has old corporate-action candidates before the selected 2024 window, but the 2024 row stream shows share-count drift during the forward window.
- 씨아이에스 has an old SPAC/name-change corporate-action candidate before the selected window, and 2024 share-count drift is visible in the row stream.
- 윤성에프앤씨 has zero corporate-action candidates.
- The drift rows are kept because they are useful for C11 guardrails, but they should not overcount clean independent evidence.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_FCF_RERATING_4B_WATCH | C11 | orderbook rerating can work, but Green requires margin/revision/FCF and share-count quality |
| BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE | C11 | orderbook beta without margin/FCF bridge is false-positive risk |
| MIXING_EQUIPMENT_ORDERBOOK_WITHOUT_MARGIN_FCF_CONVERSION | C11 | mixing-equipment orderbook premium needs margin/revision/FCF conversion before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C11_PNT_137400_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_RERATING_4B | 137400 | 피엔티 | 4B_overlay_success | positive | orderbook rerating produced ~95% MFE but later 4B drawdown |
| C11_CIS_222080_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL | 222080 | 씨아이에스 | failed_rerating | counterexample | orderbook beta had only 13.7% MFE and deep drawdown |
| C11_YUNSUNG_372170_2024_03_06_MIXING_EQUIPMENT_ORDERBOOK_FAIL | 372170 | 윤성에프앤씨 | failed_rerating | counterexample | mixing-equipment orderbook premium had low MFE and severe MAE |

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
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 137400 | source_proxy_only | equipment orderbook / customer capex / backlog-margin expectation | required before promotion |
| 222080 | source_proxy_only | equipment orderbook beta but margin/revision/FCF bridge absent | required; useful as counterexample |
| 372170 | source_proxy_only | mixing-equipment orderbook premium but margin/FCF bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 137400 | atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv | atlas/symbol_profiles/137/137400.json |
| 222080 | atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv | atlas/symbol_profiles/222/222080.json |
| 372170 | atlas/ohlcv_tradable_by_symbol_year/372/372170/2024.csv | atlas/symbol_profiles/372/372170.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 45900 | battery equipment orderbook / backlog-margin expectation |
| CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA | Stage2 | 2024-03-06 | 2024-03-06 | 13290 | orderbook beta without margin/FCF bridge |
| YUNSUNG_372170_2024_03_06_STAGE2_FALSE_POSITIVE_MIXING_EQUIPMENT_ORDERBOOK | Stage2 | 2024-03-06 | 2024-03-06 | 94200 | mixing equipment orderbook without margin/FCF conversion |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 137400 | 2024-03-06 | 45900 | 5.01 | -20.92 | 94.99 | -20.92 | 94.99 | -20.92 | 2024-06-19 | 89500 | -55.59 |
| 222080 | 2024-03-06 | 13290 | 13.70 | -22.27 | 13.70 | -26.86 | 13.70 | -40.41 | 2024-03-11 | 15110 | -47.58 |
| 372170 | 2024-03-06 | 94200 | 6.79 | -26.75 | 6.79 | -35.14 | 6.79 | -59.24 | 2024-03-13 | 100600 | -61.83 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 137400 | Stage2A possible; 4B after orderbook rerating | high MFE but post-peak drawdown and drift watch | current_profile_4B_too_late |
| 222080 | Stage2 risk if orderbook beta is over-credited | short MFE and deep 180D MAE | current_profile_false_positive |
| 372170 | Stage2 risk if equipment orderbook premium is over-credited | low MFE and severe full-window MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C11 interpretation:

- Stage2A can work when battery equipment orderbook is tied to customer capex, margin bridge, revision and FCF conversion.
- Yellow/Green require non-price margin/FCF proof and clean validation quality.
- Orderbook vocabulary by itself should remain Stage1/Stage2-watch when margin, revision and FCF are absent.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 137400 | 0.51 | 1.00 | orderbook rerating / valuation peak | full-window C11 4B audit required |
| 222080 | 0.88 | 1.00 | orderbook beta / bridge absent | not Stage3 without margin/FCF bridge |
| 372170 | 0.94 | 1.00 | mixing equipment premium / bridge absent | not Stage3 without margin/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 137400 | thesis_break_watch_only | not hard 4C, but share-count and 4B audit needed |
| 222080 | hard_4c_late | margin/revision/FCF absence and share-count drift should have capped Stage2 earlier |
| 372170 | hard_4c_late | margin/revision/FCF absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, orderbook rerating should promote Stage2A only when backlog is linked to customer capex, margin bridge, revision, working-capital quality, and FCF conversion. Orderbook beta without margin/FCF bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C11_BATTERY_ORDERBOOK_RERATING
confidence = medium
```

Candidate C11 rule:

```text
C11_orderbook_margin_fcf_bridge_required =
  battery_orderbook_or_equipment_backlog_route
  AND (customer_capex_conversion OR backlog_visibility OR margin_bridge OR confirmed_revision OR working_capital_quality OR fcf_conversion)

if orderbook_beta and margin_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 40 and drawdown_after_peak < -35:
    add C11_orderbook_4B_audit = true

if MFE_90D < 15 and MAE_90D < -20 and bridge_absent:
    classify_as C11_orderbook_false_positive_guardrail

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 38.49 | -27.64 | 38.49 | -40.19 | 2 | useful but C11 bridge too loose |
| P0b calibrated rollback | rollback | 3 | 38.49 | -27.64 | 38.49 | -40.19 | 2 | over-credits orderbook vocabulary |
| P1 sector_specific_candidate_profile | L3 | 1 promoted + 2 guard | 94.99 | -20.92 | 94.99 | -20.92 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C11 | 1 promoted + 2 guard | 94.99 | -20.92 | 94.99 | -20.92 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C11 guard | 1 promoted + 2 guard | 94.99 | -20.92 | 94.99 | -20.92 | 0 | adds orderbook false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 137400 | Stage2A aligned; 4B/share-count audit needed | current_profile_4B_too_late |
| 222080 | Stage2 false positive if margin/FCF bridge not enforced | current_profile_false_positive |
| 372170 | Stage2 false positive if orderbook-to-margin bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed C11 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 23 -> projected 26; still need 4 to reach 30 |

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
new_axis_proposed: C11_orderbook_margin_fcf_bridge_required|C11_orderbook_4B_audit|C11_orderbook_false_positive_guardrail|share_count_drift_independent_weight_reduction
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
- Uses C11 Priority 0 coverage gap.
- Avoids local C14 loop130 repetition after C14 threshold completion.
- Keeps 137400/222080 with reduced independent weights because 2024 share-count drift is visible.
- Keeps 372170 as clean-window orderbook counterexample.
- Discards the accidental duplicate C14 loop130 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop130 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_margin_fcf_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"222080/372170 show orderbook beta can fail without margin/revision/FCF bridge while 137400 works only as Stage2A with 4B/share-count audit","blocks two false positives while preserving 137400 Stage2A","PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK|CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA|YUNSUNG_372170_2024_03_06_STAGE2_FALSE_POSITIVE_MIXING_EQUIPMENT_ORDERBOOK",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C11_orderbook_4B_audit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"137400 battery equipment orderbook rerating needed full-window 4B audit after extreme MFE and drawdown","adds 4B audit after C11 MFE without converting price-only peaks into Green","PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C11_orderbook_false_positive_guardrail,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"222080/372170 had low-to-short MFE and high MAE after orderbook vocabulary without margin/FCF bridge","requires confirmed margin/revision/working-capital/FCF bridge before Stage2/Yellow promotion","CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA|YUNSUNG_372170_2024_03_06_STAGE2_FALSE_POSITIVE_MIXING_EQUIPMENT_ORDERBOOK",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"137400/222080 have 2024 share-count drift during the validation window","keeps rows usable but lowers independent evidence weight","PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK|CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA",2,2,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C11_PNT_137400_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_RERATING_4B","symbol":"137400","company_name":"피엔티","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_FCF_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; 2024 share-count drift visible, independent weight reduced","independent_evidence_weight":0.8,"score_price_alignment":"battery equipment orderbook/rerating route captured ~95% MFE, but full-window drawdown and share-count drift required C11 4B audit","current_profile_verdict":"current_profile_4B_too_late_if_orderbook_rerating_overpromoted_to_green","price_source":"Songdaiki/stock-web","notes":"new local C11 symbol after C14 threshold completion; strong positive with validation-quality caveat"}
{"row_type":"case","case_id":"C11_CIS_222080_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old SPAC/name-change corporate-action candidate before selected window; 2024 share-count drift visible, independent weight reduced","independent_evidence_weight":0.8,"score_price_alignment":"orderbook/equipment beta produced only a short MFE and then deep 180D MAE without margin, revision or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C11 symbol; share-count drift means guardrail row, not clean positive evidence"}
{"row_type":"case","case_id":"C11_YUNSUNG_372170_2024_03_06_MIXING_EQUIPMENT_ORDERBOOK_FAIL","symbol":"372170","company_name":"윤성에프앤씨","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"MIXING_EQUIPMENT_ORDERBOOK_WITHOUT_MARGIN_FCF_CONVERSION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"YUNSUNG_372170_2024_03_06_STAGE2_FALSE_POSITIVE_MIXING_EQUIPMENT_ORDERBOOK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixing-equipment orderbook premium produced only single-digit MFE and then severe full-window MAE without margin/revision/FCF conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; useful C11 counterexample"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK","case_id":"C11_PNT_137400_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_RERATING_4B","symbol":"137400","company_name":"피엔티","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_FCF_RERATING_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":45900.0,"evidence_available_at_that_date":"source_proxy_only: battery equipment orderbook, customer capex route, backlog-to-margin expectation and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_equipment_orderbook","customer_capex_route","relative_strength","backlog_margin_expectation"],"stage3_evidence_fields":["orderbook_visibility_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["orderbook_rerating","valuation_peak_watch","share_count_drift_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.01,"MFE_90D_pct":94.99,"MFE_180D_pct":94.99,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-20.92,"MAE_90D_pct":-20.92,"MAE_180D_pct":-20.92,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":89500.0,"drawdown_after_peak_pct":-55.59,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.51,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook rerating worked as Stage2A but share-count drift and post-peak drawdown require C11 4B audit","four_b_evidence_type":["orderbook_rerating","valuation_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch_reduced_weight","current_profile_verdict":"current_profile_4B_too_late_if_orderbook_rerating_overpromoted_to_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C11_137400_2024_03_06_45900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; 2024 share-count drift","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA","case_id":"C11_CIS_222080_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":13290.0,"evidence_available_at_that_date":"source_proxy_only: battery equipment orderbook and capex beta visible, but confirmed margin, revision and FCF conversion absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_equipment_orderbook_beta","capex_theme_beta","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","share_count_drift_watch","bridge_absent"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent","share_count_drift_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv","profile_path":"atlas/symbol_profiles/222/222080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.7,"MFE_90D_pct":13.7,"MFE_180D_pct":13.7,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-22.27,"MAE_90D_pct":-26.86,"MAE_180D_pct":-40.41,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":15110.0,"drawdown_after_peak_pct":-47.58,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook beta not C11 Stage3 without margin/revision/FCF bridge and share-count quality check","four_b_evidence_type":["event_spike","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_short_mfe_high_mae_bridge_absent_reduced_weight","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C11_222080_2024_03_06_13290","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old SPAC/name-change candidate before selected window; 2024 share-count drift","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"YUNSUNG_372170_2024_03_06_STAGE2_FALSE_POSITIVE_MIXING_EQUIPMENT_ORDERBOOK","case_id":"C11_YUNSUNG_372170_2024_03_06_MIXING_EQUIPMENT_ORDERBOOK_FAIL","symbol":"372170","company_name":"윤성에프앤씨","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"MIXING_EQUIPMENT_ORDERBOOK_WITHOUT_MARGIN_FCF_CONVERSION","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":94200.0,"evidence_available_at_that_date":"source_proxy_only: mixing equipment orderbook premium visible, but confirmed margin, revision and FCF conversion absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["mixing_equipment_orderbook","battery_capex_premium","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/372/372170/2024.csv","profile_path":"atlas/symbol_profiles/372/372170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.79,"MFE_90D_pct":6.79,"MFE_180D_pct":6.79,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-26.75,"MAE_90D_pct":-35.14,"MAE_180D_pct":-59.24,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":100600.0,"drawdown_after_peak_pct":-61.83,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"mixing-equipment orderbook premium not C11 Stage3 without margin/revision/FCF conversion","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_372170_2024_03_06_94200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_PNT_137400_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_RERATING_4B","trigger_id":"PNT_137400_2024_03_06_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":3,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-watch with C11 4B/share-count audit","changed_components":["valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Orderbook rerating worked, but Green needs realized margin/revision/FCF and share-count quality confirmation.","MFE_90D_pct":94.99,"MAE_90D_pct":-20.92,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_orderbook_rerating_overpromoted_to_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_CIS_222080_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL","trigger_id":"CIS_222080_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_BETA","symbol":"222080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / orderbook beta risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":3,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage1/4C-watch, not C11 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Orderbook beta without margin/revision/FCF and share-count quality bridge produced only short MFE and high MAE.","MFE_90D_pct":13.7,"MAE_90D_pct":-26.86,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_YUNSUNG_372170_2024_03_06_MIXING_EQUIPMENT_ORDERBOOK_FAIL","trigger_id":"YUNSUNG_372170_2024_03_06_STAGE2_FALSE_POSITIVE_MIXING_EQUIPMENT_ORDERBOOK","symbol":"372170","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / mixing equipment orderbook risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage1/4C-watch, not C11 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Mixing-equipment orderbook premium without margin/revision/FCF bridge produced low MFE and severe MAE.","MFE_90D_pct":6.79,"MAE_90D_pct":-35.14,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"131","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 131
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C02_POWER_GRID_DATACENTER_CAPEX, C11_BATTERY_ORDERBOOK_RERATING_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted, C11 moves to projected 26 rows and still needs 4 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C11 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/372/372170/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/137/137400.json
  - atlas/symbol_profiles/222/222080.json
  - atlas/symbol_profiles/372/372170.json
- Rejected local threshold-completed archetype repetition:
  - C14 loop130 materialization path
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
