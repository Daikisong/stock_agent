# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 71
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH | CGM_REIMBURSEMENT_HEADLINE_WITH_MARGIN_AND_ADOPTION_GAP | DENTAL_IMAGING_EXPORT_STAGNATION_WITH_LOW_REVISION | AESTHETIC_DEVICE_EXPORT_RERATING_TO_CONTROL_PREMIUM_CAP
output_file = e2r_stock_web_v12_residual_round_R7_loop_71_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
production_scoring_changed = false
shadow_weight_only = true
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

already_applied_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c
```

This MD does not re-prove the global Stage2 bonus. It stress-tests a narrower C25 condition: medical-device export/reimbursement headlines need a visible conversion bridge into reorder, consumables, margin, or reimbursement utilization before they deserve Stage2-Actionable or Yellow credit.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 71 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| round_sector_consistency | pass |
| selected objective | coverage_gap_fill / counterexample_mining / 4B_non_price_requirement_stress_test / canonical_archetype_compression |

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX was used only as a duplicate ledger. Current snapshot states representative rows 3148, validated rows 3667, unique cases 1971, unique symbols 473, positive cases 823, counterexamples 783, 4B cases 679, and 4C cases 261. For C25, the index already has 83 rows / 17 symbols with top covered names including 338220, 214150, 145720, 099190, 228670, and 335890. Therefore this loop avoids repeating the heavily-covered 338220/214150 pair and uses a new-symbol/new-trigger mix.

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows are treated as new independent cases because they use new symbol/trigger combinations inside R7/C25 and add a reimbursement-headline false-positive test.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price source | Songdaiki/stock-web |
| upstream | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| symbol_count | 5,414 |
| shard root | atlas/ohlcv_tradable_by_symbol_year |

Validated profile paths:

| symbol | company | profile path | status note |
|---|---|---|---|
| 336570 | 원텍 | atlas/symbol_profiles/336/336570.json | active_like; corporate-action candidate only at 2022-06-30, outside test window |
| 099190 | 아이센스 | atlas/symbol_profiles/099/099190.json | active_like; corporate-action candidates in 2023, outside 2024 test window |
| 043150 | 바텍 | atlas/symbol_profiles/043/043150.json | active_like; clean 2024 test window |
| 287410 | 제이시스메디칼 | atlas/symbol_profiles/287/287410.json | inactive_or_delisted_like; 4B overlay only because forward 180D is limited |

## 5. Historical Eligibility Gate

| case | entry | 180D forward | corporate-action status | calibration use |
|---|---:|---:|---|---|
| 원텍 2023-02-13 | 5,490 | available | clean 180D | representative |
| 아이센스 2024-01-10 | 29,500 | available | clean 180D | representative |
| 바텍 2024-03-08 | 30,800 | available | clean 180D | representative |
| 제이시스메디칼 2024-03-25 | 8,010 | limited by profile end | clean 90D, 180D limited | 4B overlay only |

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | canonical mapping | compression reason |
|---|---|---|
| aesthetic device export + consumable pull-through | C25 | device export is not enough; repeat consumable/reorder margin bridge is needed |
| CGM reimbursement headline without adoption/margin bridge | C25 | reimbursement optionality belongs to medical-device commercialization, but false positives require stronger bridge |
| dental imaging export stagnation | C25 | export channel exists, but weak revision and no reimbursement acceleration cap positive credit |
| aesthetic device rerating to control-premium cap | C25 plus 4B overlay | full 4B requires non-price event cap, not price-only local peak |

## 7. Case Selection Summary

| case | symbol | role | trigger | current profile verdict | reason |
|---|---|---|---|---|---|
| WONTECH export/consumable pull-through | 336570 | structural_success | Stage2-Actionable | current_profile_correct | export/channel plus margin conversion aligned with large 180D MFE |
| i-SENS CGM reimbursement headline | 099190 | failed_rerating | Stage2-Actionable | current_profile_false_positive | reimbursement optionality did not convert into margin/reorder; high MAE |
| Vatech dental export stagnation | 043150 | failed_rerating | Stage2-Watch | current_profile_false_positive | export recovery headline lacked revision and durable reimbursement bridge |
| Jsys control-premium cap | 287410 | 4B_overlay_success | Stage4B-Overlay | current_profile_4B_too_late | full 4B should wait for non-price event/control-premium cap |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_representative_trigger_count = 3
counterexample_search_incomplete = false
positive_case_missing = false
```

## 9. Evidence Source Map

This MD uses non-price evidence family labels as research proxies rather than live-source scraping. Evidence families are separated as follows:

| case | evidence family | use |
|---|---|---|
| 336570 | financial_actual / research_report / news | Stage2/Yellow positive evidence |
| 099190 | news / research_report | false-positive reimbursement headline stress test |
| 043150 | research_report / financial_actual | weak export-recovery counterexample |
| 287410 | news / disclosure | 4B event-control-premium overlay only |

## 10. Price Data Source Map

| symbol | price shard | profile |
|---|---|---|
| 336570 | atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv | atlas/symbol_profiles/336/336570.json |
| 099190 | atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv | atlas/symbol_profiles/099/099190.json |
| 043150 | atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv | atlas/symbol_profiles/043/043150.json |
| 287410 | atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv | atlas/symbol_profiles/287/287410.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | role |
|---|---|---|---|---|---:|---|
| TRG_R7L71_336570_S2A_20230213 | 336570 | Stage2-Actionable | 2023-02-13 | 2023-02-13 | 5,490 | representative |
| TRG_R7L71_099190_S2A_20240110 | 099190 | Stage2-Actionable | 2024-01-10 | 2024-01-10 | 29,500 | representative |
| TRG_R7L71_043150_S2WATCH_20240308 | 043150 | Stage2-Watch | 2024-03-08 | 2024-03-08 | 30,800 | representative |
| TRG_R7L71_287410_4B_20240325 | 287410 | Stage4B-Overlay | 2024-03-25 | 2024-03-25 | 8,010 | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| 336570 / Stage2-Actionable | +24.59% | -6.38% | +103.64% | -6.38% | +175.23% | -6.38% | 2023-08-31 | 15,110 |
| 099190 / Stage2-Actionable | +3.05% | -30.34% | +3.05% | -36.00% | +3.05% | -36.00% | 2024-01-12 | 30,400 |
| 043150 / Stage2-Watch | +2.76% | -3.57% | +2.76% | -12.50% | +2.76% | -28.57% | 2024-04-01 | 31,650 |
| 287410 / 4B-Overlay | +22.97% | -7.61% | +61.05% | -7.61% | n/a | n/a | 2024-10-18 | 12,900 |

## 13. Current Calibrated Profile Stress Test

| case | current profile judgment | outcome alignment | residual |
|---|---|---|---|
| 336570 | Stage2-Actionable / Yellow candidate | correct | keep positive bridge |
| 099190 | Stage2-Actionable if reimbursement headline over-weighted | false positive | require reimbursement utilization / margin bridge |
| 043150 | Watch should remain Watch; false if promoted | false positive if promoted | export channel alone is insufficient |
| 287410 | 4B should wait for control-premium event cap | 4B too late if only price-based | full 4B requires non-price event cap |

## 14. Stage2 / Yellow / Green Comparison

- C25 positive Stage2 works when export/channel evidence is paired with actual revenue/margin conversion.
- C25 Yellow should not trigger on reimbursement/product optionality alone.
- Green remains strict: confirmed revision, repeat order, reimbursement utilization, or consumable pull-through must be visible.
- In 099190 and 043150, Stage3-Green criteria should remain blocked because the upside was not enough and MAE was materially worse than the positive case.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 287410 | control_premium_or_event_premium / valuation_blowoff | 0.90 | 0.95 | good full-window 4B timing but overlay-only due forward-window limitation |
| 099190 | price_only / valuation_blowoff | 0.10 | 0.10 | price-only local 4B too early if promoted |
| 336570 | not 4B trigger | n/a | n/a | 4B not used for representative positive |
| 043150 | not 4B trigger | n/a | n/a | no full 4B evidence |

## 16. 4C Protection Audit

No hard 4C row is proposed. 099190 and 043150 are thesis-break-watch examples, not hard 4C confirmations. The useful calibration lesson is earlier Watch/Stage2 blocking, not 4C routing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
candidate = C25 Stage2/Yellow bridge must require one of:
  - export growth + repeat consumable/reorder evidence
  - reimbursement approval + actual utilization or hospital adoption
  - medical-device revenue growth + margin conversion
  - verified customer/channel expansion with revision support

headline-only reimbursement/product optionality:
  - may support Watch
  - should not support Stage2-Actionable or Yellow without margin/reorder bridge
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
proposed_shadow_axis = require_reimbursement_or_export_to_margin_reorder_bridge
expected_effect = reduce high-MAE false positives while preserving strong export/consumable winners
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive rate | score-return alignment |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | +36.48% | -18.29% | 66.7% | mixed |
| P1 C25 bridge-required shadow | 3 | +103.64% on selected positive | -6.38% on selected positive | 0.0% among promoted rows | improved |
| P2 C25 headline-discount shadow | 3 | avoids 099190/043150 promotion | avoids high-MAE promotions | lower | improved |
| P3 4B event-cap guard | overlay only | n/a | n/a | n/a | improves 4B label quality |

## 20. Score-Return Alignment Matrix

| case | weighted_before | stage_before | weighted_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| 336570 | 77 | Stage2-Actionable | 84 | Stage3-Yellow | positive aligned |
| 099190 | 71 | Stage2-Actionable | 58 | Watch | false positive reduced |
| 043150 | 61 | Watch | 48 | Watch | Watch preserved |
| 287410 | 82 | Stage3/4B candidate | 78 | 4B overlay watch | 4B timing improved |

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH | CGM_REIMBURSEMENT_HEADLINE_WITH_MARGIN_AND_ADOPTION_GAP | DENTAL_IMAGING_EXPORT_STAGNATION_WITH_LOW_REVISION | AESTHETIC_DEVICE_EXPORT_RERATING_TO_CONTROL_PREMIUM_CAP","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":4,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":3,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C25 still needs more verified non-price 4B timing cases; this loop adds headline-false-positive counterexamples."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, full_4b_requires_non_price_evidence, stage3_green_revision_min
residual_error_types_found: current_profile_false_positive, current_profile_4B_too_late, headline_reimbursement_without_margin_bridge
new_axis_proposed: require_reimbursement_or_export_to_margin_reorder_bridge
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema/profile paths were checked.
- Entry rows are from tradable shards.
- Representative triggers use clean windows.
- Same-entry dedupe is applied.
- 287410 is not used as representative aggregate because forward 180D is limited.

Not validated:

- This MD does not patch stock_agent.
- This MD does not create live candidates.
- This MD does not use future runtime prices for live scoring.
- Evidence text is summarized as historical research proxy, not new web scraping.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,require_generic_non_price_bridge,require_export_or_reimbursement_to_margin_reorder_bridge,+1,"CGM/reimbursement headline and dental export recovery expectations failed without margin/reorder proof","reduces high-MAE false positives in 099190/043150 while preserving 336570 positive","TRG_R7L71_336570_S2A_20230213|TRG_R7L71_099190_S2A_20240110|TRG_R7L71_043150_S2WATCH_20240308",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,full_4b_overlay_candidate,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,price_only_or_late_4B,verified_non_price_control_premium_or_reimbursement_failure_4B,+1,"Jsys shows 4B should be full only when non-price control-premium/event cap appears","improves 4B timing but row is overlay-only due forward-window limitation","TRG_R7L71_287410_4B_20240325",0,1,0,low,sector_shadow_only,"not production; overlay-only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","manifest_tradable_row_count":14354401,"manifest_symbol_count":5414,"notes":"Raw/unadjusted OHLC. Corporate-action-contaminated 180D windows are blocked by default."}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L71_C25_WONTECH_EXPORT_CONSUMABLE_PULLTHROUGH_20230213","symbol":"336570","company_name":"원텍","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable / export-device revenue conversion with operating leverage","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_stage2_aligned_with_large_180D_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Representative positive: non-price export/channel and profit conversion evidence separates it from price-only medical device beta."}
{"row_type":"case","case_id":"R7L71_C25_ISENS_CGM_REIMBURSEMENT_FALSE_GREEN_20240110","symbol":"099190","company_name":"아이센스","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_REIMBURSEMENT_HEADLINE_WITH_MARGIN_AND_ADOPTION_GAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable / reimbursement-adoption headline","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline_score_failed_with_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: reimbursement/CGM optionality without durable margin/reorder proof caused high drawdown."}
{"row_type":"case","case_id":"R7L71_C25_VATECH_DENTAL_EXPORT_STAGNATION_20240308","symbol":"043150","company_name":"바텍","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMAGING_EXPORT_STAGNATION_WITH_LOW_REVISION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Watch / dental export recovery expectation","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"low_MFE_and_revision_gap","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: export channel exists, but without accelerated reimbursement/reorder or revision evidence, rerating did not validate."}
{"row_type":"case","case_id":"R7L71_C25_JSYS_TENDER_CAP_4B_20240325","symbol":"287410","company_name":"제이시스메디칼","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_RERATING_TO_CONTROL_PREMIUM_CAP","case_type":"4B_overlay_success","positive_or_counterexample":"overlay","best_trigger":"Stage4B-Overlay / tender-control-premium cap","calibration_usable":false,"is_new_independent_case":true,"reuse_reason":"4B overlay path; 180D forward window limited by inactive/delisted-like profile","independent_evidence_weight":0.5,"score_price_alignment":"good_4b_local_timing_but_not_representative_aggregate","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"4B overlay only: stock-web profile ends in 2024, so not counted as representative 180D aggregate despite useful control-premium cap evidence."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L71_336570_S2A_20230213","case_id":"R7L71_C25_WONTECH_EXPORT_CONSUMABLE_PULLTHROUGH_20230213","symbol":"336570","company_name":"원텍","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-13","entry_date":"2023-02-13","entry_price":5490,"evidence_available_at_that_date":"aesthetic device export/channel and profitability conversion visible enough for Stage2-Actionable research proxy","evidence_source":"historical public earnings/report/news proxy; non-price evidence family=research_report/news/financial_actual","stage2_evidence_fields":["export_channel_expansion","device_reorder","operating_leverage","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv","profile_path":"atlas/symbol_profiles/336/336570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.59,"MFE_90D_pct":103.64,"MFE_180D_pct":175.23,"MFE_1Y_pct":175.23,"MFE_2Y_pct":null,"MAE_30D_pct":-6.38,"MAE_90D_pct":-6.38,"MAE_180D_pct":-6.38,"MAE_1Y_pct":-6.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-31","peak_price":15110,"drawdown_after_peak_pct":-28.13,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4b_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"336570_20230213_5490","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L71_099190_S2A_20240110","case_id":"R7L71_C25_ISENS_CGM_REIMBURSEMENT_FALSE_GREEN_20240110","symbol":"099190","company_name":"아이센스","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_REIMBURSEMENT_HEADLINE_WITH_MARGIN_AND_ADOPTION_GAP","loop_objective":"counterexample_mining|residual_false_positive_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":29500,"evidence_available_at_that_date":"CGM/reimbursement adoption headline existed, but reimbursement-to-margin and reorder conversion remained unproven","evidence_source":"historical public reimbursement/product news proxy; non-price evidence family=news/research_report","stage2_evidence_fields":["policy_or_regulatory_optionality","reimbursement_optionality","relative_strength"],"stage3_evidence_fields":["component_unknown_or_not_supported:confirmed_revision","component_unknown_or_not_supported:margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","profile_path":"atlas/symbol_profiles/099/099190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.05,"MFE_90D_pct":3.05,"MFE_180D_pct":3.05,"MFE_1Y_pct":3.05,"MFE_2Y_pct":null,"MAE_30D_pct":-30.34,"MAE_90D_pct":-36.0,"MAE_180D_pct":-36.0,"MAE_1Y_pct":-36.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":30400,"drawdown_after_peak_pct":-36.32,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":0.1,"four_b_full_window_peak_proximity":0.1,"four_b_timing_verdict":"price_only_local_4B_too_early_if_promoted","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"099190_20240110_29500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L71_043150_S2WATCH_20240308","case_id":"R7L71_C25_VATECH_DENTAL_EXPORT_STAGNATION_20240308","symbol":"043150","company_name":"바텍","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMAGING_EXPORT_STAGNATION_WITH_LOW_REVISION","loop_objective":"counterexample_mining|yellow_threshold_stress_test|coverage_gap_fill","trigger_type":"Stage2-Watch","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":30800,"evidence_available_at_that_date":"dental imaging export recovery expectation, but no durable reimbursement or high revision bridge","evidence_source":"historical public report/news proxy; non-price evidence family=research_report/financial_actual","stage2_evidence_fields":["export_channel_visibility","relative_strength_weak"],"stage3_evidence_fields":["component_unknown_or_not_supported:confirmed_revision","component_unknown_or_not_supported:margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv","profile_path":"atlas/symbol_profiles/043/043150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.76,"MFE_90D_pct":2.76,"MFE_180D_pct":2.76,"MFE_1Y_pct":2.76,"MFE_2Y_pct":null,"MAE_30D_pct":-3.57,"MAE_90D_pct":-12.5,"MAE_180D_pct":-28.57,"MAE_1Y_pct":-28.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":31650,"drawdown_after_peak_pct":-28.91,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4b_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"043150_20240308_30800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L71_287410_4B_20240325","case_id":"R7L71_C25_JSYS_TENDER_CAP_4B_20240325","symbol":"287410","company_name":"제이시스메디칼","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_RERATING_TO_CONTROL_PREMIUM_CAP","loop_objective":"4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage4B-Overlay","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":8010,"evidence_available_at_that_date":"control-premium/tender-cap risk later became the dominant 4B overlay; not a new Stage2 positive","evidence_source":"historical public tender/control-premium news proxy; non-price evidence family=news/disclosure","stage2_evidence_fields":["export_channel_expansion","recurring_consumable_revenue"],"stage3_evidence_fields":["confirmed_revision"],"stage4b_evidence_fields":["control_premium_or_event_premium","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv","profile_path":"atlas/symbol_profiles/287/287410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.97,"MFE_90D_pct":61.05,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.61,"MAE_90D_pct":-7.61,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-18","peak_price":12900,"drawdown_after_peak_pct":0,"green_lateness_ratio":"not_applicable:4B_overlay_only","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_full_window_4B_timing_but_not_aggregate_due_forward_window","four_b_evidence_type":["control_premium_or_event_premium","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":false,"forward_window_trading_days":140,"calibration_block_reasons":["insufficient_forward_window_in_stock_web_for_180D_representative_aggregate"],"corporate_action_window_status":"clean_90D_window_forward_180D_limited","same_entry_group_id":"287410_20240325_8010","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"4B overlay path; inactive/delisted-like stock-web profile shortens 180D aggregate window","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_WONTECH_EXPORT_CONSUMABLE_PULLTHROUGH_20230213","trigger_id":"TRG_R7L71_336570_S2A_20230213","symbol":"336570","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":50,"margin_bridge_score":70,"revision_score":72,"relative_strength_score":85,"customer_quality_score":62,"policy_or_regulatory_score":20,"valuation_repricing_score":58,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":78,"relative_strength_score":85,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":58,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"C25 after-profile requires reimbursement/export channel to convert into margin/reorder evidence; headline-only policy optionality is discounted.","MFE_90D_pct":103.64,"MAE_90D_pct":-6.38,"score_return_alignment_label":"score_return_alignment_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_ISENS_CGM_REIMBURSEMENT_FALSE_GREEN_20240110","trigger_id":"TRG_R7L71_099190_S2A_20240110","symbol":"099190","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":74,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":58,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":5},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":35,"relative_strength_score":74,"customer_quality_score":30,"policy_or_regulatory_score":80,"valuation_repricing_score":58,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":5},"weighted_score_after":58,"stage_label_after":"Watch","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C25 after-profile requires reimbursement/export channel to convert into margin/reorder evidence; headline-only policy optionality is discounted.","MFE_90D_pct":3.05,"MAE_90D_pct":-36.0,"score_return_alignment_label":"score_return_alignment_false_positive_reduced_by_after_profile","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_VATECH_DENTAL_EXPORT_STAGNATION_20240308","trigger_id":"TRG_R7L71_043150_S2WATCH_20240308","symbol":"043150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":30,"revision_score":32,"relative_strength_score":42,"customer_quality_score":35,"policy_or_regulatory_score":15,"valuation_repricing_score":45,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":61,"stage_label_before":"Stage1/Watch","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":22,"revision_score":25,"relative_strength_score":42,"customer_quality_score":28,"policy_or_regulatory_score":15,"valuation_repricing_score":45,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":48,"stage_label_after":"Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"C25 after-profile requires reimbursement/export channel to convert into margin/reorder evidence; headline-only policy optionality is discounted.","MFE_90D_pct":2.76,"MAE_90D_pct":-12.5,"score_return_alignment_label":"score_return_alignment_watch_not_stage2","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_JSYS_TENDER_CAP_4B_20240325","trigger_id":"TRG_R7L71_287410_4B_20240325","symbol":"287410","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":45,"margin_bridge_score":65,"revision_score":68,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":10,"valuation_repricing_score":75,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":45,"margin_bridge_score":65,"revision_score":68,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":10,"valuation_repricing_score":85,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C25 after-profile requires reimbursement/export channel to convert into margin/reorder evidence; headline-only policy optionality is discounted.","MFE_90D_pct":61.05,"MAE_90D_pct":-7.61,"score_return_alignment_label":"4B_overlay_alignment","current_profile_verdict":"current_profile_4B_too_late"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_required_bridge","full_4b_requires_non_price_evidence","stage3_green_revision_min"],"residual_error_types_found":["current_profile_false_positive","current_profile_4B_too_late","headline_reimbursement_without_margin_bridge"],"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"diversity_score_summary":"new_symbol_bonus=+12,counterexample_gap_bonus=+8,residual_error_bonus=+15,repeated_same_symbol_penalty=0; net high","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R7L71_C25_JSYS_TENDER_CAP_4B_20240325","symbol":"287410","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reason":"4B overlay useful but 180D representative aggregate blocked by stock-web inactive/delisted-like profile end","price_source":"Songdaiki/stock-web","usage":"4B_timing_overlay_not_weight_calibration"}
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
completed_round = R7
completed_loop = 71
next_round = R8
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest/schema/profile/price shards:
  - atlas/manifest.json
  - atlas/schema.json
  - atlas/symbol_profiles/336/336570.json
  - atlas/symbol_profiles/099/099190.json
  - atlas/symbol_profiles/043/043150.json
  - atlas/symbol_profiles/287/287410.json
  - atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv
