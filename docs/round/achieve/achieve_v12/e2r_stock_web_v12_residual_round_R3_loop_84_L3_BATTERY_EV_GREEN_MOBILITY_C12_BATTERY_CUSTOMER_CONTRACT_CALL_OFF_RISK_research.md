# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_84_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round: R3
selected_loop: 84
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: ELECTROLYTE_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_protection_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 independent cases, 2 protective C12 call-off successes, and 1 customer-ramp false-positive counterexample for R3/L3/C12.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C12:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C12 -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

C12 separates a customer/contract narrative from actual order pull. The contract is the valve; the key question is whether customers keep drawing volume through it or quietly turn it down through call-off, utilization delay, ASP pressure, or demand slowdown.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C12 current rows | 27 |
| C12 current symbols | 21 |
| C12 good/bad Stage2 | 9 / 4 |
| C12 4B/4C | 3 / 3 |
| C12 URL pending/proxy | 24 / 18 |
| top covered symbols | 066970, 361610, 011790, 078600, 002710, 003670 |

Selected symbols avoid the C12 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 278280 | 천보 | new C12 symbol versus top-covered C12 list |
| 393890 | 더블유씨피 | new C12 symbol versus top-covered C12 list |
| 121600 | 나노신소재 | new C12 symbol versus top-covered C12 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 278280 / 2024-02-21 | true | true | clean_180D_window | true |
| 393890 / 2024-02-21 | true | true | clean_180D_window | true |
| 121600 / 2024-02-21 | true | true | clean_180D_window | true |

Corporate-action notes:

- 천보 has zero corporate-action candidates.
- 더블유씨피 has zero corporate-action candidates.
- 나노신소재 has a corporate-action candidate only in 2015; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ELECTROLYTE_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C | C12 | electrolyte customer demand / ASP / call-off risk routes to protective 4C |
| SEPARATOR_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C | C12 | separator contract route fails if utilization/call-off risk dominates |
| CNT_SILICON_ANODE_CUSTOMER_RAMP_CALL_OFF_LAG_FALSE_POSITIVE | C12 | customer-ramp narrative without volume conversion creates Stage2 false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C12_CHUNBO_278280_2024_02_21_ELECTROLYTE_CUSTOMER_CALL_OFF_RISK | 278280 | 천보 | hard_4c_protection_success | positive | weak MFE and deep 180D drawdown validated call-off/demand risk protection |
| C12_WCP_393890_2024_02_21_SEPARATOR_CUSTOMER_CALL_OFF_RISK | 393890 | 더블유씨피 | hard_4c_protection_success | positive | separator customer route failed without call-off/utilization resolution |
| C12_NANOMATERIALS_121600_2024_02_21_CNT_CUSTOMER_RAMP_STAGE2_FALSE_POSITIVE | 121600 | 나노신소재 | failed_rerating | counterexample | customer ramp narrative had near-term MFE but later high MAE without volume conversion |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 3 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 278280 | source_proxy_only | electrolyte customer demand/call-off and ASP pressure risk | required before promotion |
| 393890 | source_proxy_only | separator customer contract/call-off and utilization risk | required before promotion |
| 121600 | source_proxy_only | CNT/silicon-anode customer ramp narrative but volume conversion absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | atlas/symbol_profiles/278/278280.json |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |
| 121600 | atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv | atlas/symbol_profiles/121/121600.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK | 4C-Protective | 2024-02-21 | 2024-02-21 | 95600 | electrolyte customer demand/call-off and ASP pressure risk |
| WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK | 4C-Protective | 2024-02-21 | 2024-02-21 | 45750 | separator customer contract/call-off and utilization risk |
| NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP | Stage2 | 2024-02-21 | 2024-02-21 | 134000 | CNT/silicon-anode customer ramp without volume conversion proof |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 278280 | 2024-02-21 | 95600 | 4.39 | -14.64 | 4.39 | -39.12 | 4.39 | -62.87 | 2024-02-21 | 99800 | -64.43 |
| 393890 | 2024-02-21 | 45750 | 8.00 | -19.34 | 8.20 | -35.96 | 8.20 | -61.29 | 2024-03-07 | 49500 | -64.22 |
| 121600 | 2024-02-21 | 134000 | 17.76 | -9.48 | 17.76 | -15.97 | 17.76 | -48.88 | 2024-02-22 | 157800 | -56.59 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 278280 | Stage2/4B-watch risk if call-off risk underweighted | very low MFE, severe MAE | current_profile_4C_too_late |
| 393890 | Stage2/4B-watch risk if contract route over-credited | low MFE, severe MAE | current_profile_4C_too_late |
| 121600 | Stage2 risk if customer ramp narrative over-credited | local MFE then large 180D drawdown | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C12 interpretation:

- Stage2A should require customer volume conversion, not only a contract or ramp narrative.
- Yellow/Green require confirmed pull-through, utilization, margin bridge, and revision.
- Call-off, utilization delay, ASP pressure, or demand slowdown should cap Stage2 and can route to protective 4C.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 278280 | 1.00 | 1.00 | weak follow-through / call-off risk | local relief peak needed hard 4C |
| 393890 | 1.00 | 1.00 | weak follow-through / utilization risk | local peak needed hard 4C |
| 121600 | 1.00 | 1.00 | customer-ramp price spike | spike was not Stage3 without volume conversion |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 278280 | hard_4c_success | customer demand/call-off risk protected against deep 180D MAE |
| 393890 | hard_4c_success | utilization/call-off risk protected against deep 180D MAE |
| 121600 | hard_4c_late | volume conversion absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = low_to_medium
```

Candidate:

> In L3 battery names, customer contracts and ramp narratives should not promote Stage2/Yellow unless customer pull-through is visible. If call-off risk, utilization delay, ASP pressure, or demand slowdown is present, cap the case at Stage1/Stage2-watch or route to C12 protective 4C.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
confidence = low_to_medium
```

Candidate C12 rule:

```text
C12_customer_pullthrough_bridge_required =
  customer_contract_or_ramp
  AND (volume_conversion OR utilization_confirmation OR confirmed_revision OR margin_bridge)

if customer_contract_or_ramp_narrative and pullthrough_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if call_off_risk OR utilization_delay OR asp_pressure:
    add C12_hard_4c_watch = true

if MFE_90D < 10 and MAE_90D < -30:
    classify_as C12_protective_4C_success

if near_term_MFE > 15 and MAE_180D < -40:
    classify_as C12_customer_ramp_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 10.12 | -30.35 | 10.12 | -57.68 | 1 | call-off bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 10.12 | -30.35 | 10.12 | -57.68 | 1 | over-credits customer/contract narratives |
| P1 sector_specific_candidate_profile | L3 | 2 protective + 1 guard | 6.29 | -37.54 | 6.29 | -62.08 | 0 | better after pull-through bridge gate |
| P2 canonical_archetype_candidate_profile | C12 | 2 protective + 1 guard | 6.29 | -37.54 | 6.29 | -62.08 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C12 guard | 2 protective + 1 guard | 6.29 | -37.54 | 6.29 | -62.08 | 0 | adds customer-ramp false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 278280 | protective 4C aligned; Stage2 would be false positive | current_profile_4C_too_late |
| 393890 | protective 4C aligned; contract route needed pull-through proof | current_profile_4C_too_late |
| 121600 | Stage2 false positive if ramp narrative not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | mixed C12 fine ids | 2 | 1 | 2 | 3 | 3 | 0 | 3 | 3 | 3 | true | true | 27 -> projected 30 rows; reaches minimum stability threshold |

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
  - current_profile_false_positive
new_axis_proposed: C12_customer_pullthrough_bridge_required|C12_hard_4c_call_off_watch|C12_customer_ramp_false_positive_guardrail
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
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
- Uses clean 180D windows.
- Uses C12 Priority 0 coverage gap.
- Uses three symbols not in the C12 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_customer_pullthrough_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"278280/393890/121600 show customer-contract or ramp narratives fail without pull-through evidence","blocks false Stage2 while preserving protective 4C","CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK|WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK|NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C12_hard_4c_call_off_watch,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"call-off/utilization/ASP pressure aligned with severe MAE in 278280 and 393890","routes customer-demand risk to protective 4C before Stage2 promotion","CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK|WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK",2,2,0,low_to_medium,canonical_shadow_only,"4C/protection calibration only"
shadow_weight,C12_customer_ramp_false_positive_guardrail,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"121600 shows near-term spike can fail if customer ramp lacks volume conversion","requires volume conversion/call-off resolution before Yellow/Green promotion","NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C12_CHUNBO_278280_2024_02_21_ELECTROLYTE_CUSTOMER_CALL_OFF_RISK","symbol":"278280","company_name":"천보","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"electrolyte/customer demand risk produced only ~4% local MFE before deep 180D MAE, validating C12 protective routing","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new C12 symbol versus top-covered list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C12_WCP_393890_2024_02_21_SEPARATOR_CUSTOMER_CALL_OFF_RISK","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"separator/customer contract route had weak follow-through and severe 180D MAE when call-off/demand risk dominated","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"393890 is top C13 but not top C12; this is C12-specific call-off risk evidence"}
{"row_type":"case","case_id":"C12_NANOMATERIALS_121600_2024_02_21_CNT_CUSTOMER_RAMP_STAGE2_FALSE_POSITIVE","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CNT_SILICON_ANODE_CUSTOMER_RAMP_CALL_OFF_LAG_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer ramp narrative produced near-term MFE but later collapsed as call-off/ramp risk reasserted","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C12 symbol versus top-covered list; counterexample for customer-ramp narrative without call-off/volume conversion proof"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK","case_id":"C12_CHUNBO_278280_2024_02_21_ELECTROLYTE_CUSTOMER_CALL_OFF_RISK","symbol":"278280","company_name":"천보","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":95600.0,"evidence_available_at_that_date":"source_proxy_only: electrolyte customer demand slowdown, contract call-off risk, and ASP/margin pressure narrative visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["electrolyte_customer_route","battery_materials_relief_rally"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_overhang"],"stage4c_evidence_fields":["customer_call_off_risk","ev_demand_slowdown","asp_pressure","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.39,"MFE_90D_pct":4.39,"MFE_180D_pct":4.39,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-14.64,"MAE_90D_pct":-39.12,"MAE_180D_pct":-62.87,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":99800.0,"drawdown_after_peak_pct":-64.43,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_relief_peak_aligned_but_customer_call_off_risk_required_hard_4C","four_b_evidence_type":["weak_follow_through","valuation_overhang"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_278280_2024_02_21_95600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK","case_id":"C12_WCP_393890_2024_02_21_SEPARATOR_CUSTOMER_CALL_OFF_RISK","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CUSTOMER_CONTRACT_CALL_OFF_DEMAND_RISK_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750.0,"evidence_available_at_that_date":"source_proxy_only: separator customer-contract demand risk, EV slowdown, utilization/call-off pressure; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["separator_customer_route","battery_contract_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_overhang"],"stage4c_evidence_fields":["customer_call_off_risk","utilization_risk","demand_slowdown","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.0,"MFE_90D_pct":8.2,"MFE_180D_pct":8.2,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.34,"MAE_90D_pct":-35.96,"MAE_180D_pct":-61.29,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":49500.0,"drawdown_after_peak_pct":-64.22,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"separator_relief_peak_failed_without_customer_call_off_resolution","four_b_evidence_type":["weak_follow_through","valuation_overhang"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_393890_2024_02_21_45750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP","case_id":"C12_NANOMATERIALS_121600_2024_02_21_CNT_CUSTOMER_RAMP_STAGE2_FALSE_POSITIVE","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CNT_SILICON_ANODE_CUSTOMER_RAMP_CALL_OFF_LAG_FALSE_POSITIVE","sector":"battery / EV / green mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":134000.0,"evidence_available_at_that_date":"source_proxy_only: CNT/silicon-anode customer ramp and long-term contract narrative visible, but call-off, utilization, and volume conversion proof absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["customer_ramp_narrative","silicon_anode_cnt_route","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["valuation_extension","call_off_risk_unresolved"],"stage4c_evidence_fields":["customer_volume_conversion_absent","call_off_risk","utilization_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv","profile_path":"atlas/symbol_profiles/121/121600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.76,"MFE_90D_pct":17.76,"MFE_180D_pct":17.76,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.48,"MAE_90D_pct":-15.97,"MAE_180D_pct":-48.88,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-22","peak_price":157800.0,"drawdown_after_peak_pct":-56.59,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"customer_ramp_price_spike_not_stage3_without_volume_conversion","four_b_evidence_type":["valuation_extension","customer_ramp_unverified"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_near_term_mfe_high_180d_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_121600_2024_02_21_134000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_CHUNBO_278280_2024_02_21_ELECTROLYTE_CUSTOMER_CALL_OFF_RISK","trigger_id":"CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive / 4C-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"4C-Protective, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Customer demand/call-off risk and ASP pressure should route to 4C before Stage2 credit.","MFE_90D_pct":4.39,"MAE_90D_pct":-39.12,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_WCP_393890_2024_02_21_SEPARATOR_CUSTOMER_CALL_OFF_RISK","trigger_id":"WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive / 4C-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"4C-Protective, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Separator customer-contract route lacked call-off resolution and utilization bridge; 4C protection aligned with price path.","MFE_90D_pct":8.2,"MAE_90D_pct":-35.96,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_NANOMATERIALS_121600_2024_02_21_CNT_CUSTOMER_RAMP_STAGE2_FALSE_POSITIVE","trigger_id":"NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP","symbol":"121600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable / Yellow-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Customer ramp narrative can produce near-term MFE, but without volume conversion/call-off proof it should not receive C12 Stage2 promotion.","MFE_90D_pct":17.76,"MAE_90D_pct":-15.97,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R3
completed_loop = 84
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

If this loop is accepted, C12 moves from 27 to a projected 30 rows and reaches the minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C12 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/278/278280.json
  - atlas/symbol_profiles/393/393890.json
  - atlas/symbol_profiles/121/121600.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
