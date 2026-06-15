# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
selected_round: R5
selected_loop: 91
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: DEPARTMENT_STORE_INVENTORY_MARGIN_LOW_MAE_RERATING
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

This loop adds 3 new independent C19 rows and, after local loop 82, moves C19 from projected 27 rows to projected 30 rows.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C19:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R5 -> L5_CONSUMER_BRAND_DISTRIBUTION
C19 -> C19_BRAND_RETAIL_INVENTORY_MARGIN
```

C19 is the consumer-retail version of a warehouse audit. A discount valuation or brand recovery headline is only the store sign. The bridge is sell-through, inventory quality, OPM, working capital, channel productivity, and receivables discipline.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C19 rows | 24 |
| static C19 symbols | 12 |
| static C19 good/bad Stage2 | 5 / 4 |
| static C19 4B/4C | 3 / 3 |
| static C19 URL pending/proxy | 21 / 15 |
| static top covered symbols | 008770, 023530, 031430, 069960, 383220, 020000 |
| local C19 loop 82 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid both the static top-covered C19 list and local loop 82 C19 symbols `036620`, `093050`, and `298540`.

| symbol | company | status |
|---|---|---|
| 004170 | 신세계 | new C19 symbol versus static top-covered and local C19 loop |
| 139480 | 이마트 | new C19 symbol versus static top-covered and local C19 loop |
| 282330 | BGF리테일 | new C19 symbol versus static top-covered and local C19 loop |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated loop memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 004170 / 2024-01-29 | true | true | clean_180D_window | true |
| 139480 / 2024-01-29 | true | true | clean_180D_window | true |
| 282330 / 2024-01-29 | true | true | clean_180D_window | true |

Corporate-action notes:

- 신세계 has corporate-action candidates only before 2012.
- 이마트 has zero corporate-action candidates.
- BGF리테일 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| DEPARTMENT_STORE_INVENTORY_MARGIN_LOW_MAE_RERATING | C19 | retail margin/discount-floor route can support Stage2A if MAE remains controlled |
| OFFLINE_RETAIL_TURNAROUND_INVENTORY_OPM_BRIDGE_FAIL | C19 | turnaround narrative without OPM/working-capital bridge is false-positive risk |
| CONVENIENCE_STORE_SSSG_MARGIN_SLOWDOWN_FALSE_POSITIVE | C19 | defensive retail label fails without same-store/OPM productivity bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C19_SHINSEGAE_004170_2024_01_29_DEPARTMENT_STORE_MARGIN_STABLE_RERATING | 004170 | 신세계 | structural_success | positive | moderate MFE with controlled 180D MAE |
| C19_EMART_139480_2024_01_29_OFFLINE_RETAIL_TURNAROUND_MARGIN_FAIL | 139480 | 이마트 | failed_rerating | counterexample | single-digit MFE and deep MAE without OPM/working-capital bridge |
| C19_BGFRETAIL_282330_2024_01_29_CONVENIENCE_STORE_MARGIN_SLOWDOWN | 282330 | BGF리테일 | failed_rerating | counterexample | defensive retail label had almost no MFE and large MAE |

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

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 004170 | source_proxy_only | department-store margin stability and inventory discipline route | required before promotion |
| 139480 | source_proxy_only | offline retail turnaround narrative but OPM/working-capital bridge absent | required; useful as counterexample |
| 282330 | source_proxy_only | defensive convenience-store label but SSSG/OPM bridge weak | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 004170 | atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv | atlas/symbol_profiles/004/004170.json |
| 139480 | atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv | atlas/symbol_profiles/139/139480.json |
| 282330 | atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv | atlas/symbol_profiles/282/282330.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SHINSEGAE_004170_2024_01_29_STAGE2A_RETAIL_MARGIN_STABLE | Stage2-Actionable | 2024-01-29 | 2024-01-29 | 170700 | retail margin stabilization / inventory discipline |
| EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND | Stage2 | 2024-01-29 | 2024-01-29 | 80900 | offline retail turnaround without OPM/working-capital bridge |
| BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN | Stage2 | 2024-01-29 | 2024-01-29 | 144600 | defensive convenience-store label without SSSG/OPM bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 004170 | 2024-01-29 | 170700 | 11.48 | -6.27 | 11.48 | -9.20 | 11.48 | -9.49 | 2024-02-19 | 190300 | -18.55 |
| 139480 | 2024-01-29 | 80900 | 9.39 | -7.42 | 9.39 | -26.21 | 9.39 | -32.26 | 2024-02-02 | 88500 | -38.08 |
| 282330 | 2024-01-29 | 144600 | 1.73 | -7.95 | 1.73 | -19.43 | 1.73 | -30.84 | 2024-01-29 | 147100 | -31.27 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 004170 | Stage2A acceptable; Green waits for sell-through/OPM proof | moderate MFE, controlled MAE | current_profile_correct |
| 139480 | Stage2 risk if retail turnaround narrative is over-credited | single-digit MFE and high MAE | current_profile_false_positive |
| 282330 | Stage2 risk if defensive retail label is over-credited | almost no MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C19 interpretation:

- Stage2A can work if retail margin stabilization has low MAE and inventory/channel quality does not deteriorate.
- Yellow/Green require sell-through, OPM, working capital, receivables, and channel productivity.
- Discount valuation, turnaround, or defensive retail label without bridge must stay Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 004170 | 1.00 | 1.00 | moderate valuation repricing | Stage2A ok; Green blocked until OPM proof |
| 139480 | 1.00 | 1.00 | valuation bounce / weak follow-through | not Stage3 without OPM bridge |
| 282330 | 1.00 | 1.00 | defensive premium decay | not Stage3 without SSSG/OPM bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 004170 | thesis_break_watch_only | not hard 4C; controlled drawdown supports Stage2A watch |
| 139480 | hard_4c_late | OPM/working-capital bridge absence should have capped Stage2 earlier |
| 282330 | hard_4c_late | SSSG/OPM bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L5_CONSUMER_BRAND_DISTRIBUTION
confidence = medium
```

Candidate:

> In L5 consumer/retail names, valuation discount or defensive retail labels should not promote Stage2/Yellow unless same-store, OPM, inventory quality, working capital, or channel productivity evidence is visible.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C19_BRAND_RETAIL_INVENTORY_MARGIN
confidence = medium
```

Candidate C19 rule:

```text
C19_inventory_margin_bridge_required =
  brand_or_retail_recovery
  AND (sellthrough_evidence OR opm_bridge OR inventory_normalization OR working_capital_quality OR receivables_quality OR sssg_productivity)

if retail_turnaround_or_defensive_label and inventory_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D < 10 and MAE_90D < -20:
    classify_as C19_retail_turnaround_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 7.53 | -18.28 | 7.53 | -24.2 | 2 | useful but retail bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 7.53 | -18.28 | 7.53 | -24.2 | 2 | over-credits turnaround/defensive labels |
| P1 sector_specific_candidate_profile | L5 | 1 promoted + 2 guard | 11.48 | -9.2 | 11.48 | -9.49 | 0 | better after OPM/working-capital gate |
| P2 canonical_archetype_candidate_profile | C19 | 1 promoted + 2 guard | 11.48 | -9.2 | 11.48 | -9.49 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C19 guard | 1 promoted + 2 guard | 11.48 | -9.2 | 11.48 | -9.49 | 0 | adds retail false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 004170 | Stage2A aligned; Green block needed | current_profile_correct |
| 139480 | Stage2 false positive if OPM bridge not enforced | current_profile_false_positive |
| 282330 | Stage2 false positive if defensive label not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | mixed C19 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 2 | true | true | static 24 -> local projected 27 -> projected 30; reaches minimum stability threshold |

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
  - current_profile_false_positive
new_axis_proposed: C19_inventory_margin_bridge_required|C19_retail_turnaround_false_positive_guardrail
existing_axis_strengthened:
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
- Uses C19 Priority 0 coverage gap.
- Avoids static C19 top-covered symbols and local loop 82 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"139480/282330 show retail turnaround or defensive labels fail without OPM/working-capital/SSSG bridge while 004170 works only as Stage2A","blocks two false positives while preserving 004170 Stage2A","SHINSEGAE_004170_2024_01_29_STAGE2A_RETAIL_MARGIN_STABLE|EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND|BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C19_retail_turnaround_false_positive_guardrail,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"139480/282330 had low MFE and high MAE after retail turnaround/defensive label","requires OPM/sell-through/working-capital/SSSG bridge before Stage2/Yellow promotion","EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND|BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C19_SHINSEGAE_004170_2024_01_29_DEPARTMENT_STORE_MARGIN_STABLE_RERATING","symbol":"004170","company_name":"신세계","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_INVENTORY_MARGIN_LOW_MAE_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"SHINSEGAE_004170_2024_01_29_STAGE2A_RETAIL_MARGIN_STABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"department-store retail margin/discount-floor route produced moderate MFE with controlled 180D MAE; Green still requires OPM/channel proof","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"new C19 symbol versus top-covered and local C19 loop 82 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C19_EMART_139480_2024_01_29_OFFLINE_RETAIL_TURNAROUND_MARGIN_FAIL","symbol":"139480","company_name":"이마트","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"OFFLINE_RETAIL_TURNAROUND_INVENTORY_OPM_BRIDGE_FAIL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"offline retail turnaround and inventory relief narrative had only single-digit MFE before 30%+ 180D MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C19 symbol; counterexample for retail turnaround without OPM/working-capital bridge"}
{"row_type":"case","case_id":"C19_BGFRETAIL_282330_2024_01_29_CONVENIENCE_STORE_MARGIN_SLOWDOWN","symbol":"282330","company_name":"BGF리테일","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_SSSG_MARGIN_SLOWDOWN_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"convenience-store defensive retail narrative had almost no MFE and large 180D MAE when same-store/margin bridge weakened","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C19 symbol; counterexample for defensive retail label without SSSG/OPM bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SHINSEGAE_004170_2024_01_29_STAGE2A_RETAIL_MARGIN_STABLE","case_id":"C19_SHINSEGAE_004170_2024_01_29_DEPARTMENT_STORE_MARGIN_STABLE_RERATING","symbol":"004170","company_name":"신세계","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_INVENTORY_MARGIN_LOW_MAE_RERATING","sector":"consumer / brand / retail distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":170700.0,"evidence_available_at_that_date":"source_proxy_only: department-store discount floor, retail margin stabilization, inventory discipline, and channel-quality route visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["retail_margin_stabilization","inventory_discipline","discount_floor","channel_quality"],"stage3_evidence_fields":["opm_bridge_partial","sellthrough_pending","working_capital_check_pending"],"stage4b_evidence_fields":["moderate_valuation_repricing","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv","profile_path":"atlas/symbol_profiles/004/004170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.48,"MFE_90D_pct":11.48,"MFE_180D_pct":11.48,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.27,"MAE_90D_pct":-9.2,"MAE_180D_pct":-9.49,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":190300.0,"drawdown_after_peak_pct":-18.55,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"moderate_rerating_ok_but_green_requires_opm_sellthrough_working_capital_bridge","four_b_evidence_type":["moderate_valuation_repricing"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_moderate_mfe_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C19_004170_2024_01_29_170700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND","case_id":"C19_EMART_139480_2024_01_29_OFFLINE_RETAIL_TURNAROUND_MARGIN_FAIL","symbol":"139480","company_name":"이마트","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"OFFLINE_RETAIL_TURNAROUND_INVENTORY_OPM_BRIDGE_FAIL","sector":"consumer / brand / retail distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":80900.0,"evidence_available_at_that_date":"source_proxy_only: offline retail turnaround, inventory relief, and discount valuation narrative visible, but OPM, working-capital, and channel productivity bridge unconfirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["retail_turnaround_narrative","inventory_relief_theme","discount_valuation"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_overhang"],"stage4c_evidence_fields":["opm_bridge_absent","working_capital_bridge_absent","channel_productivity_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv","profile_path":"atlas/symbol_profiles/139/139480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.39,"MFE_90D_pct":9.39,"MFE_180D_pct":9.39,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.42,"MAE_90D_pct":-26.21,"MAE_180D_pct":-32.26,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":88500.0,"drawdown_after_peak_pct":-38.08,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"retail_turnaround_valuation_bounce_not_stage3_without_opm_working_capital_bridge","four_b_evidence_type":["weak_follow_through","valuation_overhang"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_single_digit_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C19_139480_2024_01_29_80900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN","case_id":"C19_BGFRETAIL_282330_2024_01_29_CONVENIENCE_STORE_MARGIN_SLOWDOWN","symbol":"282330","company_name":"BGF리테일","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_SSSG_MARGIN_SLOWDOWN_FALSE_POSITIVE","sector":"consumer / brand / retail distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":144600.0,"evidence_available_at_that_date":"source_proxy_only: convenience-store defensive retail label and valuation support narrative visible, but same-store, OPM, and franchise productivity bridge weak","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["defensive_retail_label","valuation_support_narrative"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","defensive_premium_decay"],"stage4c_evidence_fields":["sssg_bridge_absent","opm_bridge_absent","franchise_productivity_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv","profile_path":"atlas/symbol_profiles/282/282330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.73,"MFE_90D_pct":1.73,"MFE_180D_pct":1.73,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.95,"MAE_90D_pct":-19.43,"MAE_180D_pct":-30.84,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":147100.0,"drawdown_after_peak_pct":-31.27,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"defensive_retail_premium_not_stage3_without_sssg_opm_bridge","four_b_evidence_type":["defensive_premium_decay","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_defensive_retail","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C19_282330_2024_01_29_144600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_SHINSEGAE_004170_2024_01_29_DEPARTMENT_STORE_MARGIN_STABLE_RERATING","trigger_id":"SHINSEGAE_004170_2024_01_29_STAGE2A_RETAIL_MARGIN_STABLE","symbol":"004170","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Actionable, Green blocked until sell-through/OPM proof","changed_components":[],"component_delta_explanation":"Moderate MFE and low MAE support Stage2A, but this is not Green without sell-through, OPM, and working-capital proof.","MFE_90D_pct":11.48,"MAE_90D_pct":-9.2,"score_return_alignment_label":"stage2_good_green_block_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_EMART_139480_2024_01_29_OFFLINE_RETAIL_TURNAROUND_MARGIN_FAIL","trigger_id":"EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND","symbol":"139480","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Turnaround/valuation narrative without OPM and working-capital bridge produced single-digit MFE and deep MAE.","MFE_90D_pct":9.39,"MAE_90D_pct":-26.21,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_BGFRETAIL_282330_2024_01_29_CONVENIENCE_STORE_MARGIN_SLOWDOWN","trigger_id":"BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN","symbol":"282330","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Defensive retail label without SSSG/OPM bridge had almost no MFE and large 180D MAE.","MFE_90D_pct":1.73,"MAE_90D_pct":-19.43,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R5
completed_loop = 91
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION, C11_BATTERY_ORDERBOOK_RERATING, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

If this loop is accepted together with local loop 82, C19 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C19 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/004/004170.json
  - atlas/symbol_profiles/139/139480.json
  - atlas/symbol_profiles/282/282330.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
