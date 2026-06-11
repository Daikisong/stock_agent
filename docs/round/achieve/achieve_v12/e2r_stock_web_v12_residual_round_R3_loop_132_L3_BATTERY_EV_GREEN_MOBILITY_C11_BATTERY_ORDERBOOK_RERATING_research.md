# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_132_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 132
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE
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

This is the corrected valid run after loop131 already used `137400`, `222080`, and `372170`. This loop uses new C11 symbol/trigger/date combinations only.

This loop intentionally uses 4 cases, not 3, because C11 moved from static 23 rows to projected 26 after loop131 and needed 4 more rows to reach the 30-row minimum stability threshold. With this loop, C11 moves to projected 30 rows.

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

C11 is the battery orderbook rerating archetype. Orderbook is the promise; margin, revision, working capital and FCF are the settlement. A promise can move the tape, but without settlement it should not become Green.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C11 static rows | 23 |
| C11 need to 30 | 7 |
| C11 local loop131 projected rows | 26 |
| this loop projected rows | 30 |

Selected symbols avoid local C11 loop131 symbols `137400`, `222080`, and `372170`.

| symbol | company | status |
|---|---|---|
| 299030 | 하나기술 | new local C11 counterexample |
| 382840 | 원준 | new local C11 counterexample |
| 382480 | 지아이텍 | new local C11 counterexample |
| 104460 | 디와이피엔에프 | new local C11 boundary 4B row |

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
| 299030 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 382840 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 382480 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 104460 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, boundary weight 0.75 |

Corporate-action notes:

- 하나기술 has old corporate-action candidates in 2021 only.
- 원준 has old corporate-action candidates in 2022 only.
- 지아이텍 has an old corporate-action candidate in 2022 only.
- 디와이피엔에프 has an old corporate-action candidate in 2011 only.
- All selected 2024 forward windows are usable; 104460 is reduced-weight because it is a C11/C01 boundary row.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE | C11 | equipment orderbook vocabulary without margin/FCF bridge is false-positive risk |
| BATTERY_PROCESS_EQUIPMENT_ORDERBOOK_WITHOUT_MARGIN_REVISION_FCF | C11 | process equipment orderbook needs margin/revision/FCF conversion |
| SLOT_DIE_EQUIPMENT_ORDERBOOK_WITHOUT_CUSTOMER_MARGIN_FCF_BRIDGE | C11 | slot-die orderbook needs customer conversion and FCF |
| BATTERY_MATERIAL_POWDER_HANDLING_ORDERBOOK_BOUNDARY_4B_WATCH | C11 | boundary orderbook rerating can be 4B but not Green without direct bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C11_HANATECH_299030_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL | 299030 | 하나기술 | failed_rerating | counterexample | 19% MFE followed by severe 90D/180D MAE |
| C11_WONJUN_382840_2024_03_06_PROCESS_EQUIPMENT_ORDERBOOK_FAIL | 382840 | 원준 | failed_rerating | counterexample | low-teens MFE and persistent MAE |
| C11_GITECH_382480_2024_03_06_SLOT_DIE_ORDERBOOK_FAIL | 382480 | 지아이텍 | failed_rerating | counterexample | short event MFE without customer/margin/FCF bridge |
| C11_DYPNF_104460_2024_03_06_POWDER_HANDLING_BATTERY_MATERIAL_EQUIPMENT_4B | 104460 | 디와이피엔에프 | 4B_overlay_boundary_success | positive_boundary | 27.54% MFE but later MAE; 4B only |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_boundary_case_count | 1 |
| counterexample_count | 3 |
| 4B_case_count | 1 |
| 4C_case_count | 3 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 1 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 299030 | source_proxy_only | equipment orderbook beta but margin/revision/FCF absent | required; useful as counterexample |
| 382840 | source_proxy_only | process-equipment orderbook but margin/revision/FCF absent | required; useful as counterexample |
| 382480 | source_proxy_only | slot-die orderbook but customer/margin/FCF absent | required; useful as counterexample |
| 104460 | source_proxy_only | powder-handling / battery-material equipment boundary route | required before promotion |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 299030 | atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv | atlas/symbol_profiles/299/299030.json |
| 382840 | atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv | atlas/symbol_profiles/382/382840.json |
| 382480 | atlas/ohlcv_tradable_by_symbol_year/382/382480/2024.csv | atlas/symbol_profiles/382/382480.json |
| 104460 | atlas/ohlcv_tradable_by_symbol_year/104/104460/2024.csv | atlas/symbol_profiles/104/104460.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA | Stage2 | 2024-03-06 | 2024-03-06 | 61400 | orderbook beta without margin/FCF |
| WONJUN_382840_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_ORDERBOOK | Stage2 | 2024-03-06 | 2024-03-06 | 18170 | process equipment orderbook without margin/FCF |
| GITECH_382480_2024_03_06_STAGE2_FALSE_POSITIVE_SLOT_DIE_ORDERBOOK | Stage2 | 2024-03-06 | 2024-03-06 | 3015 | slot-die orderbook without customer bridge |
| DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 19720 | boundary orderbook 4B watch |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 299030 | 2024-03-06 | 61400 | 19.06 | -19.14 | 19.06 | -39.33 | 19.06 | -70.20 | 2024-03-08 | 73100 | -74.97 |
| 382840 | 2024-03-06 | 18170 | 13.65 | -17.39 | 13.65 | -24.16 | 13.65 | -47.06 | 2024-03-12 | 20650 | -53.41 |
| 382480 | 2024-03-06 | 3015 | 18.24 | -8.46 | 18.24 | -19.07 | 18.24 | -24.05 | 2024-03-12 | 3565 | -35.76 |
| 104460 | 2024-03-06 | 19720 | 27.54 | -4.36 | 27.54 | -28.35 | 27.54 | -51.77 | 2024-04-12 | 25150 | -62.19 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 299030 | Stage2 risk if equipment orderbook beta is over-credited | false positive | current_profile_false_positive |
| 382840 | Stage2 risk if process-equipment orderbook is over-credited | false positive | current_profile_false_positive |
| 382480 | Stage2 risk if slot-die orderbook vocabulary is over-credited | false positive | current_profile_false_positive |
| 104460 | Stage2A boundary possible; 4B audit needed | boundary 4B only | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C11 interpretation:

- Orderbook vocabulary can start Stage2-watch.
- Stage2A requires backlog-to-customer-capex, margin, revision, working-capital quality, and FCF bridge.
- Yellow/Green should not be allowed when orderbook beta is disconnected from margin/FCF.
- Boundary rows can support a 4B audit but should not inflate pure C11 positive counts.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 299030 | 0.84 | 1.00 | event spike / bridge absent | not Stage3 without margin/FCF bridge |
| 382840 | 0.88 | 1.00 | weak follow-through / bridge absent | not Stage3 |
| 382480 | 0.85 | 1.00 | slot-die event spike / bridge absent | not Stage3 |
| 104460 | 0.78 | 1.00 | boundary rerating / cycle peak | 4B audit required |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 299030 | hard_4c_late | margin/revision/FCF absence should have capped Stage2 earlier |
| 382840 | hard_4c_late | orderbook without conversion should have capped Stage2 earlier |
| 382480 | stage2_watch_not_green | bridge absence blocks Yellow/Green |
| 104460 | thesis_break_watch_only | boundary 4B, not hard 4C at trigger |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, orderbook rerating should promote Stage2A only when the backlog is tied to customer capex, margin bridge, revision, working-capital quality, and FCF conversion. Equipment vocabulary alone should remain Stage1/Stage2-watch.

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

if equipment_orderbook_beta and margin_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 20 and drawdown_after_peak < -35:
    add C11_orderbook_4B_audit = true

if MFE_90D < 20 and MAE_90D < -15 and bridge_absent:
    classify_as C11_orderbook_false_positive_guardrail

if boundary_orderbook_row:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 4 | 19.62 | -27.73 | 19.62 | -48.27 | 3 | useful but C11 bridge too loose |
| P0b calibrated rollback | rollback | 4 | 19.62 | -27.73 | 19.62 | -48.27 | 3 | over-credits orderbook vocabulary |
| P1 sector_specific_candidate_profile | L3 | 1 boundary 4B + 3 guard | 27.54 | -28.35 | 27.54 | -51.77 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C11 | 1 boundary 4B + 3 guard | 27.54 | -28.35 | 27.54 | -51.77 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C11 guard | 1 boundary 4B + 3 guard | 27.54 | -28.35 | 27.54 | -51.77 | 0 | adds orderbook false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 299030 | Stage2 false positive if margin/FCF bridge not enforced | current_profile_false_positive |
| 382840 | Stage2 false positive if orderbook-to-margin bridge not enforced | current_profile_false_positive |
| 382480 | Stage2 false positive if customer/margin bridge not enforced | current_profile_false_positive |
| 104460 | boundary Stage2A with 4B audit, not Green | current_profile_4B_too_late |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive boundary | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed C11 fine ids | 1 | 3 | 1 | 3 | 4 | 0 | 4 | 4 | 4 | true | true | static 23 -> local 26 -> projected 30; reaches minimum stability threshold |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C11_orderbook_margin_fcf_bridge_required|C11_orderbook_4B_audit|C11_orderbook_false_positive_guardrail|C11_boundary_orderbook_weight_reduction
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
- Avoids local C11 loop131 symbols.
- Uses 4 cases to bring projected C11 coverage to 30 rows.
- Keeps 104460 with reduced independent weight because it is a boundary row.
- Does not count repeated loop131 materialization as new evidence.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_margin_fcf_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"299030/382840/382480 show orderbook/equipment vocabulary can fail without margin/revision/FCF bridge while 104460 only works as boundary 4B","blocks three false positives while preserving 104460 as reduced-weight boundary 4B","HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA|WONJUN_382840_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_ORDERBOOK|GITECH_382480_2024_03_06_STAGE2_FALSE_POSITIVE_SLOT_DIE_ORDERBOOK|DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY",4,4,3,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C11_orderbook_4B_audit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"104460 boundary rerating and 299030 event spike show MFE without Green-quality margin/FCF proof","adds 4B audit after C11 MFE without converting price-only peaks into Green","HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA|DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY",2,2,1,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C11_orderbook_false_positive_guardrail,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"299030/382840/382480 had low-to-mid MFE and high MAE after orderbook vocabulary without margin/FCF bridge","requires confirmed margin/revision/working-capital/FCF bridge before Stage2/Yellow promotion","HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA|WONJUN_382840_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_ORDERBOOK|GITECH_382480_2024_03_06_STAGE2_FALSE_POSITIVE_SLOT_DIE_ORDERBOOK",3,3,3,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C11_boundary_orderbook_weight_reduction,archetype_specific_quality_flag,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"104460 is a C11/C01 boundary row and should not overcount pure C11 positive evidence","keeps row usable but lowers independent evidence weight","DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY",1,1,0,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C11_HANATECH_299030_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL","symbol":"299030","company_name":"하나기술","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2021; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"battery-equipment orderbook beta produced an early 19% MFE but then severe 90D/180D MAE without margin, revision or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C11 symbol versus loop131; clean 2024 validation window"}
{"row_type":"case","case_id":"C11_WONJUN_382840_2024_03_06_PROCESS_EQUIPMENT_ORDERBOOK_FAIL","symbol":"382840","company_name":"원준","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_PROCESS_EQUIPMENT_ORDERBOOK_WITHOUT_MARGIN_REVISION_FCF","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"WONJUN_382840_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_ORDERBOOK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2022; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"process-equipment orderbook premium produced only low-teens MFE and then persistent MAE without margin/revision/FCF conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C11 symbol; clean 2024 validation window"}
{"row_type":"case","case_id":"C11_GITECH_382480_2024_03_06_SLOT_DIE_ORDERBOOK_FAIL","symbol":"382480","company_name":"지아이텍","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SLOT_DIE_EQUIPMENT_ORDERBOOK_WITHOUT_CUSTOMER_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"GITECH_382480_2024_03_06_STAGE2_FALSE_POSITIVE_SLOT_DIE_ORDERBOOK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate only in 2022; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"slot-die/orderbook vocabulary produced a short 18% MFE, then decayed without customer, margin, revision or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C11 symbol; small-cap equipment beta guardrail"}
{"row_type":"case","case_id":"C11_DYPNF_104460_2024_03_06_POWDER_HANDLING_BATTERY_MATERIAL_EQUIPMENT_4B","symbol":"104460","company_name":"디와이피엔에프","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MATERIAL_POWDER_HANDLING_ORDERBOOK_BOUNDARY_4B_WATCH","case_type":"4B_overlay_boundary_success","positive_or_counterexample":"positive_boundary","best_trigger":"DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate only in 2011; selected 2024 window is clean; boundary row so independent weight reduced","independent_evidence_weight":0.75,"score_price_alignment":"powder-handling/battery-material equipment rerating produced a 27.54% MFE but later deep full-window MAE, so it is 4B boundary evidence only","current_profile_verdict":"current_profile_4B_too_late_if_boundary_orderbook_overpromoted_to_green","price_source":"Songdaiki/stock-web","notes":"boundary C11/C01 row; useful for 4B audit rather than clean positive scoring"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA","case_id":"C11_HANATECH_299030_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL","symbol":"299030","company_name":"하나기술","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_BETA_WITHOUT_MARGIN_FCF_BRIDGE","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":61400.0,"evidence_available_at_that_date":"source_proxy_only: battery equipment orderbook/capex beta and relative strength visible, but confirmed margin, revision, working-capital and FCF conversion absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_equipment_orderbook_beta","capex_theme_beta","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","working_capital_quality_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv","profile_path":"atlas/symbol_profiles/299/299030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.06,"MFE_90D_pct":19.06,"MFE_180D_pct":19.06,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.14,"MAE_90D_pct":-39.33,"MAE_180D_pct":-70.2,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":73100.0,"drawdown_after_peak_pct":-74.97,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook/equipment beta not C11 Stage3 without margin/revision/FCF bridge","four_b_evidence_type":["event_spike","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_severe_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C11_299030_2024_03_06_61400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"WONJUN_382840_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_ORDERBOOK","case_id":"C11_WONJUN_382840_2024_03_06_PROCESS_EQUIPMENT_ORDERBOOK_FAIL","symbol":"382840","company_name":"원준","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_PROCESS_EQUIPMENT_ORDERBOOK_WITHOUT_MARGIN_REVISION_FCF","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":18170.0,"evidence_available_at_that_date":"source_proxy_only: battery process equipment orderbook premium visible, but confirmed margin, revision and FCF conversion absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["process_equipment_orderbook","battery_capex_beta","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv","profile_path":"atlas/symbol_profiles/382/382840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.65,"MFE_90D_pct":13.65,"MFE_180D_pct":13.65,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-17.39,"MAE_90D_pct":-24.16,"MAE_180D_pct":-47.06,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":20650.0,"drawdown_after_peak_pct":-53.41,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"process-equipment orderbook premium not C11 Stage3 without margin/revision/FCF bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C11_382840_2024_03_06_18170","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"GITECH_382480_2024_03_06_STAGE2_FALSE_POSITIVE_SLOT_DIE_ORDERBOOK","case_id":"C11_GITECH_382480_2024_03_06_SLOT_DIE_ORDERBOOK_FAIL","symbol":"382480","company_name":"지아이텍","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SLOT_DIE_EQUIPMENT_ORDERBOOK_WITHOUT_CUSTOMER_MARGIN_FCF_BRIDGE","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":3015.0,"evidence_available_at_that_date":"source_proxy_only: slot-die/equipment orderbook vocabulary visible, but customer conversion, margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["slot_die_orderbook_beta","battery_capex_beta","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","bridge_absent"],"stage4c_evidence_fields":["customer_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/382/382480/2024.csv","profile_path":"atlas/symbol_profiles/382/382480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.24,"MFE_90D_pct":18.24,"MFE_180D_pct":18.24,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.46,"MAE_90D_pct":-19.07,"MAE_180D_pct":-24.05,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":3565.0,"drawdown_after_peak_pct":-35.76,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"slot-die orderbook vocabulary not C11 Stage3 without customer/margin/FCF bridge","four_b_evidence_type":["event_spike","bridge_absent"],"four_c_protection_label":"stage2_watch_not_green","trigger_outcome_label":"counterexample_mid_mfe_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C11_382480_2024_03_06_3015","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY","case_id":"C11_DYPNF_104460_2024_03_06_POWDER_HANDLING_BATTERY_MATERIAL_EQUIPMENT_4B","symbol":"104460","company_name":"디와이피엔에프","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MATERIAL_POWDER_HANDLING_ORDERBOOK_BOUNDARY_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":19720.0,"evidence_available_at_that_date":"source_proxy_only: powder-handling / battery material process equipment orderbook boundary and capex route visible, but direct battery customer margin/FCF bridge incomplete; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["powder_handling_equipment_orderbook_boundary","battery_material_process_capex_route","relative_strength_partial"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["boundary_rerating","cycle_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/104/104460/2024.csv","profile_path":"atlas/symbol_profiles/104/104460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.54,"MFE_90D_pct":27.54,"MFE_180D_pct":27.54,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.36,"MAE_90D_pct":-28.35,"MAE_180D_pct":-51.77,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":25150.0,"drawdown_after_peak_pct":-62.19,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"boundary orderbook rerating worked only as 4B; not Green without direct margin/FCF proof","four_b_evidence_type":["boundary_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_boundary_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late_if_boundary_orderbook_overpromoted_to_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["C11_C01_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C11_104460_2024_03_06_19720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window; boundary row","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_HANATECH_299030_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL","trigger_id":"HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_ORDERBOOK_EQUIPMENT_BETA","symbol":"299030","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / equipment-orderbook beta risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage1/4C-watch, not C11 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Orderbook beta without margin/revision/FCF produced early MFE but severe MAE.","MFE_90D_pct":19.06,"MAE_90D_pct":-39.33,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_WONJUN_382840_2024_03_06_PROCESS_EQUIPMENT_ORDERBOOK_FAIL","trigger_id":"WONJUN_382840_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_ORDERBOOK","symbol":"382840","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":59,"stage_label_before":"Stage2 false-positive / process-equipment orderbook risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage1/4C-watch, not C11 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Process equipment orderbook premium lacked margin/revision/FCF conversion.","MFE_90D_pct":13.65,"MAE_90D_pct":-24.16,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_GITECH_382480_2024_03_06_SLOT_DIE_ORDERBOOK_FAIL","trigger_id":"GITECH_382480_2024_03_06_STAGE2_FALSE_POSITIVE_SLOT_DIE_ORDERBOOK","symbol":"382480","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / slot-die orderbook risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/Stage2-watch, not C11 Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Slot-die orderbook vocabulary lacked customer/margin/FCF bridge.","MFE_90D_pct":18.24,"MAE_90D_pct":-19.07,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C11_DYPNF_104460_2024_03_06_POWDER_HANDLING_BATTERY_MATERIAL_EQUIPMENT_4B","trigger_id":"DYPNF_104460_2024_03_06_STAGE2A_POWDER_HANDLING_ORDERBOOK_BOUNDARY","symbol":"104460","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable boundary / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage2-watch with C11 boundary 4B audit","changed_components":["backlog_visibility_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Boundary rerating produced MFE, but direct battery customer/margin/FCF proof was incomplete.","MFE_90D_pct":27.54,"MAE_90D_pct":-28.35,"score_return_alignment_label":"positive_boundary_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_boundary_orderbook_overpromoted_to_green"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"132","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 132
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C02_POWER_GRID_DATACENTER_CAPEX, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

If this loop is accepted together with local C11 loop131, C11 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C11 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/382/382480/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/104/104460/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/299/299030.json
  - atlas/symbol_profiles/382/382840.json
  - atlas/symbol_profiles/382/382480.json
  - atlas/symbol_profiles/104/104460.json
- Rejected local duplicate C11 symbols:
  - 137400, 222080, 372170
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
