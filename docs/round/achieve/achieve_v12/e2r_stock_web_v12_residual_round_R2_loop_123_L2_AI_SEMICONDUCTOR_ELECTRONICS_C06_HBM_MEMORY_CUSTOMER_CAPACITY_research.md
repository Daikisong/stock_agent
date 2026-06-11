# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_123_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 123
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RECOVERY_4B_WATCH
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

This is the corrected valid run after a duplicate loop122 materialization path was discarded. Loop122 already used `000660`, `005930`, and `353200`; this loop uses new C06 symbol/trigger/date combinations only.

This loop adds 3 new independent C06 rows and moves C06 from static 21 rows to local projected 24 after loop122, then to projected 27 after this loop. It still needs 3 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C06:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C06 -> C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

C06 is the HBM memory customer/capacity archetype. The key question is whether “capacity” is a signed customer lane with mix, ASP, margin, revision and FCF, or just a signboard above an empty loading dock.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C06 static rows | 21 |
| C06 need to 30 | 9 |
| C06 need to 50 | 29 |
| C06 investigation point | 고객 CAPA, HBM mix, ASP/FCF 전환, cycle 반례 |
| local C06 loop122 projected rows | 24 |
| this loop projected rows | 27 |

Selected symbols avoid local C06 loop122 symbols `000660`, `005930`, and `353200`.

| symbol | company | status |
|---|---|---|
| 222800 | 심텍 | new local C06 symbol; package substrate recovery positive/4B |
| 356860 | 티엘비 | new local C06 symbol; memory module PCB counterexample |
| 007810 | 코리아써키트 | new local C06 symbol; package substrate event counterexample |

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
| 222800 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 356860 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 007810 / 2024-02-13 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |

Corporate-action notes:

- 심텍 has old corporate-action candidates in 2015/2020 only; selected 2024 window is clean. The 2024 KOSDAQ GLOBAL label switch is not treated as a corporate action.
- 티엘비 has old corporate-action candidates in 2022 only; selected 2024 window is clean.
- 코리아써키트 has old corporate-action candidates in 1999/2013 only; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RECOVERY_4B_WATCH | C06 | package substrate recovery can support Stage2A, but memory-cycle 4B audit is mandatory |
| MEMORY_MODULE_PCB_CAPACITY_PREMIUM_WITHOUT_CUSTOMER_CAPA_MARGIN_FCF_BRIDGE | C06 | module/PCB capacity premium without customer-capa/margin/FCF bridge is false-positive risk |
| PACKAGE_SUBSTRATE_CAPACITY_EVENT_WITHOUT_CUSTOMER_LOCK_FCF_BRIDGE | C06 | package substrate event premium needs customer lock and FCF bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C06_SIMMTECH_222800_2024_03_06_HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RERATING_4B | 222800 | 심텍 | 4B_overlay_success | positive | package substrate recovery produced 23.87% MFE and then deep drawdown |
| C06_TLB_356860_2024_03_06_MEMORY_MODULE_PCB_CAPACITY_PREMIUM_FAIL | 356860 | 티엘비 | failed_rerating | counterexample | memory module/PCB premium had short MFE and severe MAE |
| C06_KOREACIRCUIT_007810_2024_02_13_PACKAGE_SUBSTRATE_CAPACITY_EVENT_FAIL | 007810 | 코리아써키트 | failed_rerating | counterexample | package substrate event had short MFE and then large MAE |

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
| 222800 | source_proxy_only | package substrate customer capacity recovery / utilization / mix route | required before promotion |
| 356860 | source_proxy_only | memory module/PCB capacity premium but customer-capa/margin bridge absent | required; useful as counterexample |
| 007810 | source_proxy_only | package substrate event premium but customer lock/HBM mix/FCF bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 222800 | atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv | atlas/symbol_profiles/222/222800.json |
| 356860 | atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv | atlas/symbol_profiles/356/356860.json |
| 007810 | atlas/ohlcv_tradable_by_symbol_year/007/007810/2024.csv | atlas/symbol_profiles/007/007810.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SIMMTECH_222800_2024_03_06_STAGE2A_HBM_PACKAGE_SUBSTRATE_CAPACITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 29950 | HBM/package substrate customer-capacity recovery |
| TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MODULE_PCB_CAPACITY | Stage2 | 2024-03-06 | 2024-03-06 | 28200 | memory module/PCB capacity premium without bridge |
| KOREACIRCUIT_007810_2024_02_13_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_CAPACITY_EVENT | Stage2 | 2024-02-13 | 2024-02-13 | 19300 | package substrate event without customer lock/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 222800 | 2024-03-06 | 29950 | 15.03 | -7.51 | 23.87 | -7.51 | 23.87 | -63.51 | 2024-06-19 | 37100 | -70.54 |
| 356860 | 2024-03-06 | 28200 | 12.59 | -11.35 | 15.43 | -34.43 | 15.43 | -60.04 | 2024-05-09 | 32550 | -65.38 |
| 007810 | 2024-02-13 | 19300 | 15.28 | -8.65 | 15.28 | -23.26 | 15.28 | -48.86 | 2024-02-15 | 22250 | -55.64 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 222800 | Stage2A possible; 4B after package-substrate recovery | useful MFE but deep full-window drawdown | current_profile_4B_too_late |
| 356860 | Stage2 risk if memory PCB capacity premium is over-credited | short MFE and high MAE | current_profile_false_positive |
| 007810 | Stage2 risk if package substrate event is over-credited | short MFE and severe full-window MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C06 interpretation:

- Stage2A can work when HBM/package capacity is tied to customer lock, utilization, HBM mix, margin, revision, and FCF.
- Yellow/Green require non-price customer and mix evidence.
- Package/module PCB premium without that bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 222800 | 0.81 | 1.00 | package substrate recovery / memory-cycle peak | full-window 4B audit required |
| 356860 | 0.87 | 1.00 | module/PCB capacity premium / bridge absent | not Stage3 without customer-capa/FCF bridge |
| 007810 | 0.87 | 1.00 | package substrate event / bridge absent | not Stage3 without customer lock/HBM mix bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 222800 | thesis_break_watch_only | not hard 4C, but memory-cycle 4B cap needed after rerating |
| 356860 | hard_4c_late | customer-capa/margin/FCF bridge absence should have capped Stage2 earlier |
| 007810 | hard_4c_late | customer lock/HBM mix/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM/package capacity should promote Stage2A only when customer lock, HBM mix, utilization, ASP/margin, revision or FCF conversion is visible. Module PCB or package-substrate event premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C06_HBM_MEMORY_CUSTOMER_CAPACITY
confidence = medium
```

Candidate C06 rule:

```text
C06_hbm_customer_capacity_mix_bridge_required =
  hbm_memory_or_hbm_package_capacity_route
  AND (customer_qualification OR customer_lock OR capacity_lock OR hbm_mix_bridge OR asp_margin_bridge OR confirmed_revision OR fcf_conversion)

if module_pcb_or_package_substrate_premium and customer_capa_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 20 and drawdown_after_peak < -45:
    add C06_memory_cycle_4B_audit = true

if MFE_90D > 10 and MAE_90D < -20 and bridge_absent:
    classify_as C06_package_capacity_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 18.19 | -21.73 | 18.19 | -57.47 | 2 | useful but C06 package bridge too loose |
| P0b calibrated rollback | rollback | 3 | 18.19 | -21.73 | 18.19 | -57.47 | 2 | over-credits package/module capacity premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 23.87 | -7.51 | 23.87 | -63.51 | 0 | better after customer-capa/FCF gate |
| P2 canonical_archetype_candidate_profile | C06 | 1 promoted + 2 guard | 23.87 | -7.51 | 23.87 | -63.51 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C06 guard | 1 promoted + 2 guard | 23.87 | -7.51 | 23.87 | -63.51 | 0 | adds package/module false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 222800 | Stage2A aligned; 4B cycle audit needed | current_profile_4B_too_late |
| 356860 | Stage2 false positive if customer-capa bridge not enforced | current_profile_false_positive |
| 007810 | Stage2 false positive if customer lock/FCF bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed C06 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> projected 27; still need 3 to reach 30 |

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
new_axis_proposed: C06_hbm_customer_capacity_mix_bridge_required|C06_memory_cycle_4B_audit|C06_package_capacity_false_positive_guardrail
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
- Uses C06 Priority 0 coverage gap.
- Avoids local C06 loop122 symbols.
- Keeps 222800/356860/007810 with reduced weights because old corporate-action candidates are outside selected windows or because market-label switch is not treated as price-adjustment contamination.
- Discards the accidental duplicate loop122 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop122 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_hbm_customer_capacity_mix_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"356860/007810 show module PCB or package substrate premiums can fail without customer-capa/margin/FCF bridge while 222800 works only as Stage2A with 4B audit","blocks two false positives while preserving 222800 Stage2A","SIMMTECH_222800_2024_03_06_STAGE2A_HBM_PACKAGE_SUBSTRATE_CAPACITY|TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MODULE_PCB_CAPACITY|KOREACIRCUIT_007810_2024_02_13_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_CAPACITY_EVENT",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C06_memory_cycle_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"222800 package-substrate capacity recovery needed full-window 4B audit after MFE and drawdown","adds 4B audit after C06 package/memory-cycle MFE without converting price-only peaks into Green","SIMMTECH_222800_2024_03_06_STAGE2A_HBM_PACKAGE_SUBSTRATE_CAPACITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C06_package_capacity_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"356860/007810 had short MFE and high MAE after package/module capacity premiums without customer lock or FCF bridge","requires confirmed customer capacity, HBM mix, margin/revision, and FCF bridge before Stage2/Yellow promotion","TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MODULE_PCB_CAPACITY|KOREACIRCUIT_007810_2024_02_13_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_CAPACITY_EVENT",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C06_SIMMTECH_222800_2024_03_06_HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RERATING_4B","symbol":"222800","company_name":"심텍","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RECOVERY_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SIMMTECH_222800_2024_03_06_STAGE2A_HBM_PACKAGE_SUBSTRATE_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; 2024 KOSDAQ GLOBAL label switch is not price-adjustment contamination","independent_evidence_weight":0.95,"score_price_alignment":"HBM/package substrate customer-capacity recovery route captured 23.87% MFE, but full-window drawdown required C06 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol versus loop122; package substrate bridge positive/4B watch"}
{"row_type":"case","case_id":"C06_TLB_356860_2024_03_06_MEMORY_MODULE_PCB_CAPACITY_PREMIUM_FAIL","symbol":"356860","company_name":"티엘비","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_MODULE_PCB_CAPACITY_PREMIUM_WITHOUT_CUSTOMER_CAPA_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MODULE_PCB_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2022; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"memory module/PCB capacity premium produced a short MFE but then severe full-window MAE without customer-capa, margin, revision or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; module PCB capacity false-positive guard"}
{"row_type":"case","case_id":"C06_KOREACIRCUIT_007810_2024_02_13_PACKAGE_SUBSTRATE_CAPACITY_EVENT_FAIL","symbol":"007810","company_name":"코리아써키트","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PACKAGE_SUBSTRATE_CAPACITY_EVENT_WITHOUT_CUSTOMER_LOCK_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"KOREACIRCUIT_007810_2024_02_13_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_CAPACITY_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window","independent_evidence_weight":0.95,"score_price_alignment":"package substrate capacity event had a short MFE but then large MAE without customer lock, HBM mix, margin and FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C06 symbol; alternate 2024-02-13 trigger date avoids same-date crowding"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SIMMTECH_222800_2024_03_06_STAGE2A_HBM_PACKAGE_SUBSTRATE_CAPACITY","case_id":"C06_SIMMTECH_222800_2024_03_06_HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RERATING_4B","symbol":"222800","company_name":"심텍","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RECOVERY_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":29950.0,"evidence_available_at_that_date":"source_proxy_only: HBM/package substrate customer capacity recovery, substrate utilization/mix route, memory cycle recovery and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_package_substrate_capacity","substrate_utilization_recovery","memory_cycle_recovery","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["memory_cycle_peak_watch","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv","profile_path":"atlas/symbol_profiles/222/222800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.03,"MFE_90D_pct":23.87,"MFE_180D_pct":23.87,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.51,"MAE_90D_pct":-7.51,"MAE_180D_pct":-63.51,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":37100.0,"drawdown_after_peak_pct":-70.54,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"package_substrate_capacity_recovery_worked_as_stage2a_but_full_window_drawdown_requires_C06_4B_cycle_audit","four_b_evidence_type":["valuation_rerating","memory_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_label_switch_not_corporate_action"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_222800_2024_03_06_29950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MODULE_PCB_CAPACITY","case_id":"C06_TLB_356860_2024_03_06_MEMORY_MODULE_PCB_CAPACITY_PREMIUM_FAIL","symbol":"356860","company_name":"티엘비","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_MODULE_PCB_CAPACITY_PREMIUM_WITHOUT_CUSTOMER_CAPA_MARGIN_FCF_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":28200.0,"evidence_available_at_that_date":"source_proxy_only: memory module/PCB capacity premium and HBM/DDR recovery narrative visible, but customer capacity lock, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_module_pcb_capacity_premium","memory_cycle_narrative","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","customer_capacity_bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["customer_capa_lock_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv","profile_path":"atlas/symbol_profiles/356/356860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.59,"MFE_90D_pct":15.43,"MFE_180D_pct":15.43,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.35,"MAE_90D_pct":-34.43,"MAE_180D_pct":-60.04,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":32550.0,"drawdown_after_peak_pct":-65.38,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_module_pcb_capacity_premium_not_C06_stage3_without_customer_capa_margin_revision_fcf_bridge","four_b_evidence_type":["event_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_customer_capacity_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_356860_2024_03_06_28200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KOREACIRCUIT_007810_2024_02_13_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_CAPACITY_EVENT","case_id":"C06_KOREACIRCUIT_007810_2024_02_13_PACKAGE_SUBSTRATE_CAPACITY_EVENT_FAIL","symbol":"007810","company_name":"코리아써키트","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PACKAGE_SUBSTRATE_CAPACITY_EVENT_WITHOUT_CUSTOMER_LOCK_FCF_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":19300.0,"evidence_available_at_that_date":"source_proxy_only: package substrate capacity event premium and memory recovery narrative visible, but customer lock, HBM mix, margin/revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["package_substrate_capacity_event","memory_recovery_narrative","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","customer_lock_absent","full_window_drawdown"],"stage4c_evidence_fields":["customer_lock_absent","hbm_mix_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007810/2024.csv","profile_path":"atlas/symbol_profiles/007/007810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.28,"MFE_90D_pct":15.28,"MFE_180D_pct":15.28,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.65,"MAE_90D_pct":-23.26,"MAE_180D_pct":-48.86,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":22250.0,"drawdown_after_peak_pct":-55.64,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"package_substrate_capacity_event_not_C06_stage3_without_customer_lock_hbm_mix_fcf_bridge","four_b_evidence_type":["event_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_event_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C06_007810_2024_02_13_19300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_SIMMTECH_222800_2024_03_06_HBM_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_RERATING_4B","trigger_id":"SIMMTECH_222800_2024_03_06_STAGE2A_HBM_PACKAGE_SUBSTRATE_CAPACITY","symbol":"222800","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-watch with C06 4B cycle audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Package substrate recovery worked as Stage2A, but Green needs customer capacity lock, margin/revision and FCF conversion.","MFE_90D_pct":23.87,"MAE_90D_pct":-7.51,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_TLB_356860_2024_03_06_MEMORY_MODULE_PCB_CAPACITY_PREMIUM_FAIL","trigger_id":"TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MODULE_PCB_CAPACITY","symbol":"356860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / memory PCB capacity risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory module/PCB capacity premium without customer-capa/margin/FCF bridge produced short MFE and severe MAE.","MFE_90D_pct":15.43,"MAE_90D_pct":-34.43,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C06_KOREACIRCUIT_007810_2024_02_13_PACKAGE_SUBSTRATE_CAPACITY_EVENT_FAIL","trigger_id":"KOREACIRCUIT_007810_2024_02_13_STAGE2_FALSE_POSITIVE_PACKAGE_SUBSTRATE_CAPACITY_EVENT","symbol":"007810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / package substrate event risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Package substrate event without customer lock/HBM mix/FCF bridge produced short MFE and then high MAE.","MFE_90D_pct":15.28,"MAE_90D_pct":-23.26,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"123","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 123
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted together with local C06 loop122, C06 moves to projected 27 rows and still needs 3 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C06 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/007/007810/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/222/222800.json
  - atlas/symbol_profiles/356/356860.json
  - atlas/symbol_profiles/007/007810.json
- Rejected local duplicate C06 symbols:
  - 000660, 005930, 353200
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_122_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
