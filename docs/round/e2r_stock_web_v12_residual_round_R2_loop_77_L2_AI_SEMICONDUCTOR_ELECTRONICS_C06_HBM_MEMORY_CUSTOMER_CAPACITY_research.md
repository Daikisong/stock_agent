# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 77
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_CUSTOMER_CAPACITY_MIX_ASP_REVISION_4B_WATCH
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

This loop adds 3 independent cases, 2 counterexamples, and 2 residual error types for R2/L2/C06.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

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

C06 is interpreted as HBM memory customer capacity, mix, ASP, and revision conversion. Broad memory beta is not enough. The bridge must connect customer capacity or HBM mix to margin, EPS revision, and FCF.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C06 current rows | 21 |
| C06 current symbols | 16 |
| C06 good/bad Stage2 | 6 / 4 |
| C06 4B/4C | 2 / 2 |
| C06 URL pending/proxy | 18 / 12 |
| top covered symbols | 005290, 036540, 080220, 222800, 353200, 000660 |

Selected symbols:

| symbol | company | status |
|---|---|---|
| 000660 | SK하이닉스 | C06 core HBM memory proxy; appears once in top-covered list, but this entry/trigger is not known hard duplicate |
| 005930 | 삼성전자 | new C06 symbol versus top-covered C06 list |
| 000990 | DB하이텍 | new C06 symbol versus top-covered C06 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary. `000660` should be rechecked by batch ingestion against the full representative rows because it appears once in the C06 top-covered list.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 000660 / 2024-02-22 | true | true | clean_180D_window | true |
| 005930 / 2024-03-20 | true | true | clean_180D_window | true |
| 000990 / 2024-06-20 | true | true | clean_180D_window | true |

Corporate-action notes:

- SK하이닉스 profile has corporate-action candidates only in 1998-2003; selected 2024 window is clean.
- 삼성전자 profile has corporate-action candidates in 1996, 1997, and 2018; selected 2024 window is clean.
- DB하이텍 profile has corporate-action candidates in 1997, 1999, and 2007; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_CUSTOMER_CAPACITY_MIX_ASP_REVISION_4B_WATCH | C06 | HBM customer capacity / mix / ASP route; 4B audit after rerating |
| HBM_CATCHUP_CUSTOMER_CAPACITY_EXECUTION_LAG | C06 | HBM catch-up narrative without enough execution bridge |
| NON_HBM_MEMORY_BETA_CUSTOMER_CAPACITY_BRIDGE_ABSENT | C06 | broad memory or semiconductor beta lacks C06 HBM capacity bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C06_SKHYNIX_000660_2024_02_22_HBM_CUSTOMER_CAPACITY_MIX_RERATING | 000660 | SK하이닉스 | 4B_overlay_success | positive | HBM customer capacity/mix bridge produced strong MFE |
| C06_SAMSUNG_005930_2024_03_20_HBM_CATCHUP_CAPACITY_LAG | 005930 | 삼성전자 | failed_rerating | counterexample | catch-up narrative produced mid-teens MFE then high MAE |
| C06_DBHITEK_000990_2024_06_20_MEMORY_BETA_NO_HBM_CAPACITY_BRIDGE | 000990 | DB하이텍 | failed_rerating | counterexample | broad memory/foundry beta lacked HBM capacity bridge and collapsed |

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
| 000660 | source_proxy_only | HBM customer capacity/mix/ASP route; revision bridge partial | required before promotion |
| 005930 | source_proxy_only | HBM catch-up narrative but customer/execution bridge incomplete | required; useful as counterexample |
| 000990 | source_proxy_only | broad semiconductor beta but no HBM capacity bridge | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json |
| 005930 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | atlas/symbol_profiles/005/005930.json |
| 000990 | atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv | atlas/symbol_profiles/000/000990.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 156500 | HBM customer capacity/mix/ASP route |
| SAMSUNG_005930_2024_03_20_STAGE2_FALSE_POSITIVE_HBM_CATCHUP_CAPACITY_LAG | Stage2 | 2024-03-20 | 2024-03-20 | 76900 | HBM catch-up narrative with execution lag |
| DBHITEK_000990_2024_06_20_STAGE2_FALSE_POSITIVE_MEMORY_BETA_NO_HBM_BRIDGE | Stage2 | 2024-06-20 | 2024-06-20 | 57100 | non-HBM memory/foundry beta without capacity bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 000660 | 2024-02-22 | 156500 | 21.73 | -2.49 | 55.27 | -2.49 | 58.79 | -7.54 | 2024-07-11 | 248500 | -41.77 |
| 005930 | 2024-03-20 | 76900 | 11.18 | -4.55 | 15.47 | -4.55 | 15.47 | -27.57 | 2024-07-11 | 88800 | -37.27 |
| 000990 | 2024-06-20 | 57100 | 3.15 | -18.04 | 3.15 | -38.35 | 3.15 | -38.35 | 2024-06-20 | 58900 | -40.24 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 000660 | Stage2A/Yellow possible; 4B after rerating | high MFE then large post-peak drawdown | current_profile_4B_too_late |
| 005930 | Stage2 risk if catch-up narrative is over-credited | mid-teens MFE then high MAE | current_profile_false_positive |
| 000990 | Stage2 risk if memory beta is mistaken for HBM bridge | tiny MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C06 interpretation:

- Stage2A can work when HBM customer capacity/mix/ASP bridge is visible.
- Yellow/Green require customer capacity, execution, revision, margin bridge, and FCF conversion.
- Broad memory beta or catch-up label without execution bridge should stay Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 000660 | 1.00 | 1.00 | valuation / positioning | good 4B audit after HBM capacity/mix rerating |
| 005930 | 1.00 | 1.00 | catch-up execution lag | peak without customer capacity bridge should not be Green |
| 000990 | 1.00 | 1.00 | price_only / non-HBM beta | local peak without HBM bridge is not full 4B |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 000660 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 005930 | hard_4c_late | HBM catch-up bridge absence should have capped Stage2 earlier |
| 000990 | hard_4c_late | no HBM capacity bridge should have blocked C06 Stage2 |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = low_to_medium
```

Candidate:

> In L2 memory names, Stage2A can be supported by HBM customer capacity, mix, and ASP evidence. However, Stage3-Yellow/Green requires execution and revision bridge. Broad memory beta, catch-up labels, or non-HBM semiconductor spikes should be capped at Stage1/Stage2-watch unless customer capacity and margin conversion are visible.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C06_HBM_MEMORY_CUSTOMER_CAPACITY
confidence = low_to_medium
```

Candidate C06 rule:

```text
C06_hbm_customer_capacity_bridge_required =
  hbm_customer_capacity
  AND (mix_shift OR asp_bridge OR confirmed_revision OR margin_bridge)

if memory_beta_or_catchup_label and customer_capacity_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 50 and drawdown_after_peak < -35:
    add C06_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 24.63 | -15.13 | 25.8 | -24.49 | 2 | useful but HBM bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 24.63 | -15.13 | 25.8 | -24.49 | 2 | over-credits memory beta |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 55.27 | -2.49 | 58.79 | -7.54 | 0 | better after bridge gate |
| P2 canonical_archetype_candidate_profile | C06 | 1 promoted + 2 guard | 55.27 | -2.49 | 58.79 | -7.54 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C06 guard | 1 promoted + 2 guard | 55.27 | -2.49 | 58.79 | -7.54 | 0 | adds HBM capacity bridge gate |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 000660 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 005930 | Stage2 false positive if catch-up bridge not enforced | current_profile_false_positive |
| 000990 | Stage2 false positive if memory beta is over-credited | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed C06 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | 21 -> projected 24 rows; still need 6 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
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
new_axis_proposed: C06_hbm_customer_capacity_bridge_required|C06_peak_proximity_4B_audit
existing_axis_strengthened:
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
- Uses clean 180D windows.
- Uses C06 Priority 0 coverage gap.
- Uses two symbols not listed among C06 top-covered symbols and one core C06 proxy requiring full-ledger duplicate check.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_hbm_customer_capacity_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"005930 and 000990 show memory beta/catch-up narratives can fail without HBM customer capacity bridge","blocks two false positives while preserving 000660 Stage2A","SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX|SAMSUNG_005930_2024_03_20_STAGE2_FALSE_POSITIVE_HBM_CATCHUP_CAPACITY_LAG|DBHITEK_000990_2024_06_20_STAGE2_FALSE_POSITIVE_MEMORY_BETA_NO_HBM_BRIDGE",3,3,2,low_to_medium,canonical_shadow_only,"not production; URL repair and full duplicate check required before promotion"
shadow_weight,C06_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"000660 HBM mix rerating still needed 4B audit after valuation extension","adds 4B audit after large C06 MFE without turning price-only peaks into full 4B","SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX",1,1,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C06_SKHYNIX_000660_2024_02_22_HBM_CUSTOMER_CAPACITY_MIX_RERATING","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_CAPACITY_MIX_ASP_REVISION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM customer capacity/mix bridge captured large MFE; later valuation drawdown requires C06 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"000660 appears once in C06 top-covered list, but this entry/trigger family is treated as independent unless ledger says hard duplicate; source_proxy_only evidence needs URL repair"}
{"row_type":"case","case_id":"C06_SAMSUNG_005930_2024_03_20_HBM_CATCHUP_CAPACITY_LAG","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CATCHUP_CUSTOMER_CAPACITY_EXECUTION_LAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"SAMSUNG_005930_2024_03_20_STAGE2_FALSE_POSITIVE_HBM_CATCHUP_CAPACITY_LAG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Memory beta and HBM catch-up narrative produced only mid-teens MFE before -27% MAE; customer capacity bridge was late/insufficient","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C06 symbol versus top-covered C06 list; counterexample for HBM catch-up narrative without execution/revision bridge"}
{"row_type":"case","case_id":"C06_DBHITEK_000990_2024_06_20_MEMORY_BETA_NO_HBM_CAPACITY_BRIDGE","symbol":"000990","company_name":"DB하이텍","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"NON_HBM_MEMORY_BETA_CUSTOMER_CAPACITY_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DBHITEK_000990_2024_06_20_STAGE2_FALSE_POSITIVE_MEMORY_BETA_NO_HBM_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Non-HBM memory/foundry beta spiked briefly but lacked HBM customer capacity bridge and collapsed into high MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C06 symbol; counterexample to prevent broad memory beta from being treated as C06 HBM capacity bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX","case_id":"C06_SKHYNIX_000660_2024_02_22_HBM_CUSTOMER_CAPACITY_MIX_RERATING","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_CAPACITY_MIX_ASP_REVISION_4B_WATCH","sector":"AI/semiconductor/electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":156500.0,"evidence_available_at_that_date":"source_proxy_only: HBM customer demand, capacity/mix shift, ASP/revision route, and relative strength were visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_customer_capacity_route","mix_shift_route","asp_revision_route","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","revision_bridge_partial","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.73,"MFE_90D_pct":55.27,"MFE_180D_pct":58.79,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.49,"MAE_90D_pct":-2.49,"MAE_180D_pct":-7.54,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500.0,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_HBM_capacity_mix_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_000660_2024_02_22_156500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SAMSUNG_005930_2024_03_20_STAGE2_FALSE_POSITIVE_HBM_CATCHUP_CAPACITY_LAG","case_id":"C06_SAMSUNG_005930_2024_03_20_HBM_CATCHUP_CAPACITY_LAG","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CATCHUP_CUSTOMER_CAPACITY_EXECUTION_LAG","sector":"AI/semiconductor/electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":76900.0,"evidence_available_at_that_date":"source_proxy_only: broad memory beta and HBM catch-up/customer capacity narrative existed, but execution/customer qualification/revision bridge was incomplete","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_beta","hbm_catchup_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["catchup_execution_risk","price_only_memory_beta"],"stage4c_evidence_fields":["customer_capacity_bridge_lag","revision_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.18,"MFE_90D_pct":15.47,"MFE_180D_pct":15.47,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.55,"MAE_90D_pct":-4.55,"MAE_180D_pct":-27.57,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800.0,"drawdown_after_peak_pct":-37.27,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"catchup_narrative_peak_without_customer_capacity_bridge_not_full_green","four_b_evidence_type":["execution_lag","price_beta"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_hbm_catchup_lag","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_005930_2024_03_20_76900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DBHITEK_000990_2024_06_20_STAGE2_FALSE_POSITIVE_MEMORY_BETA_NO_HBM_BRIDGE","case_id":"C06_DBHITEK_000990_2024_06_20_MEMORY_BETA_NO_HBM_CAPACITY_BRIDGE","symbol":"000990","company_name":"DB하이텍","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"NON_HBM_MEMORY_BETA_CUSTOMER_CAPACITY_BRIDGE_ABSENT","sector":"AI/semiconductor/electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":57100.0,"evidence_available_at_that_date":"source_proxy_only: broad semiconductor/memory beta and price spike, but no HBM customer capacity, mix, or ASP bridge","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["semiconductor_beta","price_spike","memory_cycle_sympathy"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","non_hbm_beta"],"stage4c_evidence_fields":["hbm_capacity_bridge_absent","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv","profile_path":"atlas/symbol_profiles/000/000990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.15,"MFE_90D_pct":3.15,"MFE_180D_pct":3.15,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-18.04,"MAE_90D_pct":-38.35,"MAE_180D_pct":-38.35,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":58900.0,"drawdown_after_peak_pct":-40.24,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_memory_beta_peak_without_HBM_capacity_bridge_not_full_4B","four_b_evidence_type":["price_only","non_hbm_beta"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_no_hbm_capacity_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_000990_2024_06_20_57100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SKHYNIX_000660_2024_02_22_HBM_CUSTOMER_CAPACITY_MIX_RERATING","trigger_id":"SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable with mandatory C06 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM capacity/mix bridge worked, but valuation score must decay after large MFE and peak proximity.","MFE_90D_pct":55.27,"MAE_90D_pct":-2.49,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SAMSUNG_005930_2024_03_20_HBM_CATCHUP_CAPACITY_LAG","trigger_id":"SAMSUNG_005930_2024_03_20_STAGE2_FALSE_POSITIVE_HBM_CATCHUP_CAPACITY_LAG","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":65,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1/Stage2-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Broad memory beta and catch-up narrative lacked confirmed customer capacity/revision bridge and later produced high MAE.","MFE_90D_pct":15.47,"MAE_90D_pct":-4.55,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_DBHITEK_000990_2024_06_20_MEMORY_BETA_NO_HBM_CAPACITY_BRIDGE","trigger_id":"DBHITEK_000990_2024_06_20_STAGE2_FALSE_POSITIVE_MEMORY_BETA_NO_HBM_BRIDGE","symbol":"000990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Non-HBM semiconductor beta should not receive C06 HBM customer capacity credit.","MFE_90D_pct":3.15,"MAE_90D_pct":-38.35,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"77","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 77
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted, C06 moves from 21 to a projected 24 rows. It remains below 30-row minimum stability, but the next run should re-read the latest No-Repeat Index before selecting another C06 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/000/000660.json
  - atlas/symbol_profiles/005/005930.json
  - atlas/symbol_profiles/000/000990.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
