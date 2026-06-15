# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_118_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 118
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TCBONDER_ORDER_RELATIVE_STRENGTH_REVISION_4B_WATCH
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

This is the corrected valid run after an accidental loop117 re-materialization attempt. C08 reached the 30-row stability threshold at local loop117, so this loop moves to C07.

This loop adds 3 new independent C07 rows and moves C07 from static 18 rows to projected 21 rows. It remains below the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C07:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C07 -> C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

C07 is the HBM equipment order/relative-strength archetype. Relative strength is the smoke; actual order conversion, customer capex, revision, margin, and FCF are the fire.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C07 static rows | 18 |
| C07 need to 30 | 12 |
| C07 need to 50 | 32 |
| C07 investigation point | HBM 장비 상대강도와 실제 order/revision 연결 여부 |
| local previous C07 rows in this session | 0 |
| this loop projected rows | 21 |

Selected symbols avoid local C01/C08/C09/C10 symbols where possible. 한미반도체 is an HBM anchor and may overlap static C07 exposure, so it is retained with reduced independent weight and used as the positive reference row. QRT(405100), which was briefly considered during the discarded C08 path, was rejected for C08 because its 2024 row stream had share-count drift inside the candidate window; it is not used here.

| symbol | company | status |
|---|---|---|
| 042700 | 한미반도체 | C07 anchor positive; reduced weight due to possible static overlap |
| 110990 | 디아이티 | new local C07 counterexample |
| 412350 | 레이저쎌 | new local C07 counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is known to be a local hard duplicate. The accidental duplicate loop117 materialization is not counted.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 042700 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.85 |
| 110990 / 2024-03-06 | true | true | clean_180D_window | true |
| 412350 / 2024-03-06 | true | true | clean_180D_window_before_2026_candidate | true, reduced weight 0.95 |

Corporate-action notes:

- 한미반도체 has old corporate-action candidates before the selected 2024 window.
- 디아이티 has zero corporate-action candidates.
- 레이저쎌 has a 2026 corporate-action candidate, outside the selected 2024 window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_TCBONDER_ORDER_RELATIVE_STRENGTH_REVISION_4B_WATCH | C07 | HBM order + relative strength can support Stage2A, but valuation peak audit is mandatory |
| HBM_LASER_INSPECTION_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_ORDER_REVISION_BRIDGE | C07 | HBM equipment RS without order/revision bridge is false-positive risk |
| HBM_LASER_BONDING_EVENT_PREMIUM_WITHOUT_ORDER_MARGIN_BRIDGE | C07 | HBM laser-bonding event premium needs actual order/margin bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C07_HANMI_042700_2024_03_06_HBM_TCBONDER_ORDER_RS_RERATING_4B | 042700 | 한미반도체 | 4B_overlay_success | positive | HBM TC-bonder order/RS route produced 93% MFE, then full-window drawdown |
| C07_DIT_110990_2024_03_06_HBM_LASER_INSPECTION_EQUIPMENT_RS_FALSE_POSITIVE | 110990 | 디아이티 | failed_rerating | counterexample | RS premium had high MFE but high MAE and bridge absence |
| C07_LASERSEL_412350_2024_03_06_HBM_LASER_BONDING_EVENT_PREMIUM_FAIL | 412350 | 레이저쎌 | failed_rerating | counterexample | event premium spiked, then collapsed without order/margin bridge |

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
| 042700 | source_proxy_only | HBM TC-bonder order visibility / customer capex / revision expectation | required before promotion |
| 110990 | source_proxy_only | HBM equipment RS but confirmed order/revision/margin bridge absent | required; useful as counterexample |
| 412350 | source_proxy_only | HBM laser-bonding event premium but order/margin bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json |
| 110990 | atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv | atlas/symbol_profiles/110/110990.json |
| 412350 | atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv | atlas/symbol_profiles/412/412350.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HANMI_042700_2024_03_06_STAGE2A_HBM_TCBONDER_ORDER_RS | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 101400 | HBM TC-bonder order / RS / revision route |
| DIT_110990_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_EQUIPMENT_RS | Stage2 | 2024-03-06 | 2024-03-06 | 22600 | HBM equipment RS without order/revision bridge |
| LASERSEL_412350_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_LASER_BONDING | Stage2 | 2024-03-06 | 2024-03-06 | 9000 | HBM laser-bonding event premium without order/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 042700 | 2024-03-06 | 101400 | 51.08 | -9.27 | 93.49 | -9.27 | 93.49 | -25.84 | 2024-06-14 | 196200 | -61.67 |
| 110990 | 2024-03-06 | 22600 | 36.95 | -25.88 | 43.14 | -25.88 | 43.14 | -42.74 | 2024-04-26 | 32350 | -60.00 |
| 412350 | 2024-03-06 | 9000 | 32.56 | -6.44 | 51.22 | -16.67 | 51.22 | -48.89 | 2024-05-07 | 13610 | -66.20 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 042700 | Stage2A/Yellow possible; 4B after TC-bonder rerating | extreme MFE, later deep drawdown | current_profile_4B_too_late |
| 110990 | Stage2 risk if RS premium is over-credited | tradable MFE but high MAE and bridge absent | current_profile_false_positive |
| 412350 | Stage2 risk if event premium is over-credited | event MFE and severe full-window collapse | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C07 interpretation:

- Stage2A can work when relative strength is tied to HBM equipment order conversion, customer capex, margin, revision, and FCF.
- Yellow/Green require non-price order/revision evidence.
- HBM-equipment labels or event RS alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 042700 | 0.52 | 1.00 | HBM order rerating / valuation | full-window 4B audit required |
| 110990 | 0.70 | 1.00 | RS event premium / high MAE | not Stage3 without order/revision bridge |
| 412350 | 0.66 | 1.00 | laser-bonding event premium / bridge absent | not Stage3 without order/margin bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 042700 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 110990 | hard_4c_late | order/revision/margin bridge absence should have capped Stage2 earlier |
| 412350 | hard_4c_late | order/margin bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM equipment relative strength can support Stage2A only when order conversion, customer capex, margin bridge, revision, or FCF is visible. RS/event premium without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
confidence = medium
```

Candidate C07 rule:

```text
C07_hbm_equipment_order_revision_bridge_required =
  hbm_equipment_relative_strength_route
  AND (confirmed_order OR customer_capex_conversion OR backlog_visibility OR margin_bridge OR confirmed_revision OR fcf_conversion)

if relative_strength_premium and order_revision_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C07_peak_proximity_4B_audit = true

if MFE_90D > 30 and MAE_90D < -15 and bridge_absent:
    classify_as C07_hbm_equipment_rs_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 62.62 | -17.27 | 62.62 | -39.16 | 2 | useful but C07 bridge too loose |
| P0b calibrated rollback | rollback | 3 | 62.62 | -17.27 | 62.62 | -39.16 | 2 | over-credits RS/event premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 93.49 | -9.27 | 93.49 | -25.84 | 0 | better after order/revision bridge gate |
| P2 canonical_archetype_candidate_profile | C07 | 1 promoted + 2 guard | 93.49 | -9.27 | 93.49 | -25.84 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C07 guard | 1 promoted + 2 guard | 93.49 | -9.27 | 93.49 | -25.84 | 0 | adds HBM equipment RS false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 042700 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 110990 | Stage2 false positive if order/revision bridge not enforced | current_profile_false_positive |
| 412350 | Stage2 false positive if event premium not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | mixed C07 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 18 -> projected 21; still need 9 to reach 30 |

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
new_axis_proposed: C07_hbm_equipment_order_revision_bridge_required|C07_peak_proximity_4B_audit|C07_hbm_equipment_rs_false_positive_guardrail
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
- Uses C07 Priority 0 coverage gap.
- Avoids local C08/C09/C01/C10 stabilized archetype repetition.
- Treats C08 loop117 and C09 loop114 as already accepted local stability thresholds.
- Corrects the accidental duplicate loop117 materialization by making this the valid loop118 C07 artifact.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count the accidental duplicated C08 loop117 file as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_hbm_equipment_order_revision_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"110990/412350 show HBM equipment RS premiums can fail without order/revision/margin bridge while 042700 works only as Stage2A with 4B audit","blocks two false positives while preserving 042700 Stage2A","HANMI_042700_2024_03_06_STAGE2A_HBM_TCBONDER_ORDER_RS|DIT_110990_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_EQUIPMENT_RS|LASERSEL_412350_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_LASER_BONDING",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C07_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"042700 HBM TC-bonder order rerating needed full-window 4B audit after extreme MFE and drawdown","adds 4B audit after large C07 MFE without converting price-only peaks into Green","HANMI_042700_2024_03_06_STAGE2A_HBM_TCBONDER_ORDER_RS",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C07_hbm_equipment_rs_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"110990/412350 had high MFE but high MAE or severe drawdown after HBM equipment RS/event premiums","requires confirmed order/customer capex/margin/revision/FCF bridge before Stage2/Yellow promotion","DIT_110990_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_EQUIPMENT_RS|LASERSEL_412350_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_LASER_BONDING",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C07_HANMI_042700_2024_03_06_HBM_TCBONDER_ORDER_RS_RERATING_4B","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_ORDER_RELATIVE_STRENGTH_REVISION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HANMI_042700_2024_03_06_STAGE2A_HBM_TCBONDER_ORDER_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; possible C07 anchor overlap, counted with reduced weight","independent_evidence_weight":0.85,"score_price_alignment":"HBM TC-bonder order/relative-strength route captured 90%+ MFE, but the later full-window drawdown required C07 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"C07 anchor positive; reduced weight because large HBM anchor may already be represented in static corpus even though the local loop memory has no C07 rows"}
{"row_type":"case","case_id":"C07_DIT_110990_2024_03_06_HBM_LASER_INSPECTION_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"110990","company_name":"디아이티","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_INSPECTION_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_ORDER_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DIT_110990_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_EQUIPMENT_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM/advanced-equipment relative-strength premium produced a tradable MFE but large early MAE and later drawdown without durable order/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; useful C07 counterexample for RS without order/revision conversion"}
{"row_type":"case","case_id":"C07_LASERSEL_412350_2024_03_06_HBM_LASER_BONDING_EVENT_PREMIUM_FAIL","symbol":"412350","company_name":"레이저쎌","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_BONDING_EVENT_PREMIUM_WITHOUT_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LASERSEL_412350_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_LASER_BONDING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2026 corporate-action candidate is outside selected 2024 window","independent_evidence_weight":0.95,"score_price_alignment":"HBM/laser-bonding event premium produced a spike but then a deep full-window drawdown without order, margin, or revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"clean 2024 calibration window; 2026 corporate-action candidate outside window"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HANMI_042700_2024_03_06_STAGE2A_HBM_TCBONDER_ORDER_RS","case_id":"C07_HANMI_042700_2024_03_06_HBM_TCBONDER_ORDER_RS_RERATING_4B","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_ORDER_RELATIVE_STRENGTH_REVISION_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":101400.0,"evidence_available_at_that_date":"source_proxy_only: HBM TC-bonder order visibility, customer capex route, revision/relative-strength setup, and HBM equipment leadership visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_tcbonder_order_visibility","customer_capex_route","relative_strength_leadership","revision_expectation"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":51.08,"MFE_90D_pct":93.49,"MFE_180D_pct":93.49,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.27,"MAE_90D_pct":-9.27,"MAE_180D_pct":-25.84,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200.0,"drawdown_after_peak_pct":-61.67,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.52,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_tcbonder_order_rs_worked_but_full_window_peak_requires_C07_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["possible_static_C07_anchor_overlap_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C07_042700_2024_03_06_101400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window; possible C07 anchor overlap","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DIT_110990_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_EQUIPMENT_RS","case_id":"C07_DIT_110990_2024_03_06_HBM_LASER_INSPECTION_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"110990","company_name":"디아이티","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_INSPECTION_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_ORDER_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":22600.0,"evidence_available_at_that_date":"source_proxy_only: HBM/advanced equipment relative strength and laser/inspection route visible, but confirmed order, margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_equipment_relative_strength","laser_inspection_theme","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","high_mae","bridge_absent"],"stage4c_evidence_fields":["order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","profile_path":"atlas/symbol_profiles/110/110990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.95,"MFE_90D_pct":43.14,"MFE_180D_pct":43.14,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-25.88,"MAE_90D_pct":-25.88,"MAE_180D_pct":-42.74,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-26","peak_price":32350.0,"drawdown_after_peak_pct":-60.0,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_equipment_rs_not_C07_stage3_without_order_revision_margin_bridge","four_b_evidence_type":["event_premium","high_mae"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_high_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_110990_2024_03_06_22600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LASERSEL_412350_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_LASER_BONDING","case_id":"C07_LASERSEL_412350_2024_03_06_HBM_LASER_BONDING_EVENT_PREMIUM_FAIL","symbol":"412350","company_name":"레이저쎌","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_BONDING_EVENT_PREMIUM_WITHOUT_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":9000.0,"evidence_available_at_that_date":"source_proxy_only: HBM/laser bonding event premium and relative strength visible, but order conversion, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_laser_bonding_event_premium","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","bridge_absent","drawdown"],"stage4c_evidence_fields":["order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv","profile_path":"atlas/symbol_profiles/412/412350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.56,"MFE_90D_pct":51.22,"MFE_180D_pct":51.22,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.44,"MAE_90D_pct":-16.67,"MAE_180D_pct":-48.89,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":13610.0,"drawdown_after_peak_pct":-66.2,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.66,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"laser_bonding_event_premium_not_C07_stage3_without_order_margin_revision_bridge","four_b_evidence_type":["event_spike","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_high_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_before_2026_candidate","same_entry_group_id":"C07_412350_2024_03_06_9000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"2026 corporate-action candidate outside selected 2024 window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_HANMI_042700_2024_03_06_HBM_TCBONDER_ORDER_RS_RERATING_4B","trigger_id":"HANMI_042700_2024_03_06_STAGE2A_HBM_TCBONDER_ORDER_RS","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable with mandatory C07 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM TC-bonder order route worked, but Green requires order/revision/margin/FCF conversion and valuation peak audit.","MFE_90D_pct":93.49,"MAE_90D_pct":-9.27,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_DIT_110990_2024_03_06_HBM_LASER_INSPECTION_EQUIPMENT_RS_FALSE_POSITIVE","trigger_id":"DIT_110990_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_EQUIPMENT_RS","symbol":"110990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive / RS premium risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Relative strength alone produced a tradable spike but high MAE and later drawdown without order/revision bridge.","MFE_90D_pct":43.14,"MAE_90D_pct":-25.88,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_LASERSEL_412350_2024_03_06_HBM_LASER_BONDING_EVENT_PREMIUM_FAIL","trigger_id":"LASERSEL_412350_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_LASER_BONDING","symbol":"412350","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive / event premium risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM laser-bonding event premium without order/margin/revision bridge produced high MFE but severe full-window MAE.","MFE_90D_pct":51.22,"MAE_90D_pct":-16.67,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 118
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C02_POWER_GRID_DATACENTER_CAPEX, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING
```

If this loop is accepted, C07 moves to projected 21 rows and still needs 9 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C07 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/042/042700.json
  - atlas/symbol_profiles/110/110990.json
  - atlas/symbol_profiles/412/412350.json
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_117_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
