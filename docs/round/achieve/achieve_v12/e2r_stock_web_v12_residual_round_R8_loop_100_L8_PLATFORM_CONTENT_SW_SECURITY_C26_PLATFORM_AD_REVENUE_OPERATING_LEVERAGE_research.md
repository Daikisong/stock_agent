# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R8
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are treated as baseline, not re-proposed globally:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop tests whether C26 needs a more explicit **platform monetization + operating leverage bridge** before advertising/platform vocabulary receives Stage2-Actionable treatment. The residual question is whether generic ad-spend recovery language is too weak unless it converts into ARPU, take-rate, ad inventory yield, margin, or confirmed platform traffic monetization.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE |
| scope logic | C26 belongs to R8/L8. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C26 as Priority 0 with 3 representative rows, 3 symbols, and top-covered symbols `035420`, `042000`, `237820`.

This loop avoids those symbols and adds three new C26 symbols:

| symbol | name at trigger date | novelty |
|---:|---|---|
| 067160 | 아프리카TV / SOOP | new symbol for C26; platform traffic migration and monetization bridge positive case |
| 089600 | 나스미디어 | new symbol for C26; digital ad agency recovery label false-positive / high-MAE counterexample |
| 216050 | 인크로스 | new symbol for C26; ad-tech recovery vocabulary without durable operating leverage counterexample |

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row intentionally repeats existing C26 symbols or trigger keys.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| universe | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

The stock-web manifest reports `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, `symbol_count = 5414`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`.

The schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m`, with MFE/MAE calculated from max high / min low over N tradable rows from the entry date.

## 5. Historical Eligibility Gate

All selected representative entries are historical, have entry rows in stock-web tradable shards, have at least 180 forward trading days before manifest max date, and have no corporate-action candidate in the 180D window.

| symbol | profile_path | corporate_action_window_status | calibration status |
|---:|---|---|---|
| 067160 | atlas/symbol_profiles/067/067160.json | clean_180D_window | usable |
| 089600 | atlas/symbol_profiles/089/089600.json | clean_180D_window | usable |
| 216050 | atlas/symbol_profiles/216/216050.json | clean_180D_window | usable |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression logic |
|---|---|---|
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | streaming_platform_traffic_migration_to_monetization | traffic migration is useful only when ad/paid-item monetization and platform operating leverage are visible |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | digital_ad_agency_recovery_label_without_margin_bridge | ad-spend recovery vocabulary alone can generate price-MFE but fails if margin/operating leverage do not follow |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | adtech_media_rep_rebound_without_durable_revenue_conversion | a short ad-tech rebound is weak when revenue conversion and OPM do not confirm |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger | entry | price |
|---|---:|---|---|---|---|---:|
| C26_R8L100_067160_20240108 | 067160 | 아프리카TV / SOOP | structural_success | Stage2-Actionable | 2024-01-08 | 98800 |
| C26_R8L100_089600_20240119 | 089600 | 나스미디어 | failed_rerating | Stage2 | 2024-01-19 | 23900 |
| C26_R8L100_216050_20240109 | 216050 | 인크로스 | failed_rerating | Stage2 | 2024-01-09 | 11660 |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |
| representative_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| new_trigger_family_count | 4 |

## 9. Evidence Source Map

| case_id | evidence family | evidence source status | evidence interpretation |
|---|---|---|---|
| C26_R8L100_067160_20240108 | streaming platform traffic migration, user/community concentration, monetization optionality | source_proxy_only / evidence_url_pending | non-price platform traffic migration thesis available before entry; requires later monetization and margin confirmation |
| C26_R8L100_089600_20240119 | digital ad recovery, media rep / ad agency rebound vocabulary | source_proxy_only / evidence_url_pending | price moved with ad recovery label, but not enough evidence of operating leverage durability |
| C26_R8L100_216050_20240109 | ad-tech rebound, advertising market normalization vocabulary | source_proxy_only / evidence_url_pending | early rebound was not supported by durable revenue/margin conversion |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry row |
|---:|---|---|---|
| 067160 | atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv | atlas/symbol_profiles/067/067160.json | 2024-01-08 c=98800 |
| 089600 | atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv | atlas/symbol_profiles/089/089600.json | 2024-01-19 c=23900 |
| 216050 | atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv | atlas/symbol_profiles/216/216050.json | 2024-01-09 c=11660 |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---|---|---:|---:|---:|---|
| T_C26_067160_STAGE2A_20240108 | Stage2-Actionable | 2024-01-08 / 98800 | 27.53 / -10.63 | 41.30 / -10.63 | 45.55 / -14.07 | current profile too late if it waits for fully confirmed platform margin leverage |
| T_C26_067160_STAGE4B_20240628 | Stage4B | 2024-06-28 / 131300 | 9.52 / -35.34 | 9.52 / -35.34 | 9.52 / -40.14 | local/full 4B risk overlay useful after platform spike |
| T_C26_089600_STAGE2_20240119 | Stage2 | 2024-01-19 / 23900 | 12.13 / -9.21 | 12.13 / -26.28 | 12.13 / -36.53 | generic ad recovery label false positive |
| T_C26_216050_STAGE2_20240109 | Stage2 | 2024-01-09 / 11660 | 5.15 / -7.89 | 5.15 / -29.67 | 5.15 / -47.51 | ad-tech rebound failed without operating leverage bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | trigger_type | entry_price | peak_date | peak_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | drawdown_after_peak_pct |
|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 067160 | Stage2-Actionable | 98800 | 2024-07-11 | 143800 | 27.53 | 41.30 | 45.55 | -10.63 | -10.63 | -14.07 | -40.96 |
| 067160 | Stage4B | 131300 | 2024-07-11 | 143800 | 9.52 | 9.52 | 9.52 | -35.34 | -35.34 | -40.14 | -45.34 |
| 089600 | Stage2 | 23900 | 2024-01-24 | 26800 | 12.13 | 12.13 | 12.13 | -9.21 | -26.28 | -36.53 | -43.40 |
| 216050 | Stage2 | 11660 | 2024-01-12 | 12260 | 5.15 | 5.15 | 5.15 | -7.89 | -29.67 | -47.51 | -50.08 |

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely verdict | actual price path alignment | residual error |
|---|---|---|---|
| C26_R8L100_067160_20240108 | Stage2 but potentially delayed until monetization proof | MFE180 +45.55 with tolerable MAE before a later 4B risk window | current_profile_too_late |
| C26_R8L100_089600_20240119 | Stage2 if generic ad recovery label is over-credited | MFE capped at +12.13 while MAE180 reached -36.53 | current_profile_false_positive |
| C26_R8L100_216050_20240109 | Stage2 if ad-tech rebound is over-credited | MFE capped at +5.15 while MAE180 reached -47.51 | current_profile_false_positive |

Existing axis assessment:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is created in this loop. C26 should not be Green-unlocked by traffic, advertising, or ad-spend recovery vocabulary alone.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Interpretation:

- SOOP-like platform migration may justify Stage2-Actionable when traffic migration and monetization route are already visible.
- Ad agency/media-rep cases need revenue growth, take-rate, OPM, or revision confirmation before Stage3-Yellow/Green.
- Generic ad recovery vocabulary is insufficient for Green and often insufficient even for Stage2-Actionable.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local peak proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| T_C26_067160_STAGE4B_20240628 | positioning_overheat, valuation_blowoff, platform event premium | 0.82 | 0.78 | good_full_window_4B_timing |

4B is treated as an overlay, not a standalone sell signal. The useful rule is: C26 platform spike after a Stage2-Actionable traffic migration event should move into 4B-watch when price is near full-window peak and valuation/positioning evidence is non-price-supported.

## 16. 4C Protection Audit

No hard Stage4C trigger is emitted in this loop.

```text
four_c_protection_label = thesis_break_watch_only
```

C26 4C should be reserved for evidence such as traffic collapse, advertiser demand cut, platform policy break, monetization failure, accounting/trust break, or confirmed margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
candidate = L8 platform/ad revenue Stage2 bridge should require monetization or operating leverage evidence, not ad recovery vocabulary alone.
```

L8 platform/content/SW/security cases are heterogeneous. C26 specifically needs a platform or ad-revenue conversion bridge. Traffic, MAU, streamer migration, and ad-spend normalization are only early signals until they connect to ARPU, ad inventory yield, take-rate, OPM, or EPS revision.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
candidate = C26_platform_ad_arpu_margin_bridge_required
```

Proposed C26 rule:

```text
If C26 case has platform traffic migration + monetization route + early operating leverage evidence:
    allow Stage2-Actionable watch.
If C26 case has only advertising recovery, ad agency rebound, or price momentum:
    cap at Stage2 watch or 4B/false-positive audit.
If C26 case reaches local/full peak after platform migration rerating and non-price valuation/positioning evidence exists:
    allow Stage4B overlay, not hard 4C.
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible representative triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated baseline | 3 | 19.53 | -22.19 | 20.94 | -32.70 | 0.67 | mixed; still over-credits generic ad recovery |
| P0b e2r_2_0_baseline_reference | pre-calibrated reference | 3 | 19.53 | -22.19 | 20.94 | -32.70 | 0.67 | too loose on price/ad label vocabulary |
| P1 sector_specific_candidate_profile | L8 requires monetization/retention bridge | 2 | 23.23 | -19.18 | 25.34 | -25.30 | 0.50 | better but still broad |
| P2 canonical_archetype_candidate_profile | C26 requires ARPU/OPM/revision bridge | 1 | 41.30 | -10.63 | 45.55 | -14.07 | 0.00 | best alignment |
| P3 counterexample_guard_profile | ad agency rebound without OPM is capped | 1 | 41.30 | -10.63 | 45.55 | -14.07 | 0.00 | guardrail improves precision |

## 20. Score-Return Alignment Matrix

| case_id | raw component interpretation | before score / stage | proposed score / stage | alignment verdict |
|---|---|---|---|---|
| C26_R8L100_067160_20240108 | traffic migration + monetization optionality + RS, but margin still early | 66 / Stage2 | 70 / Stage2-Actionable | score aligned with high MFE after early platform migration |
| C26_R8L100_089600_20240119 | ad recovery label + RS, weak OPM/revision bridge | 64 / Stage2 | 56 / Stage1/Stage2-watch | avoids high-MAE false positive |
| C26_R8L100_216050_20240109 | ad-tech rebound, no durable op leverage bridge | 62 / Stage2 | 54 / Stage1/Stage2-watch | avoids high-MAE false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE | 1 | 2 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | 24 rows to 30 if accepted |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [current_profile_too_late, current_profile_false_positive, high_MAE_guardrail]
new_axis_proposed: C26_platform_ad_arpu_margin_bridge_required
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus | stage3_yellow_total_min | stage3_green_total_min | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Actual stock-web 1D OHLC rows were used for entry price and 30/90/180D MFE/MAE.
- Corporate-action candidate windows were checked through symbol profile metadata.
- Trigger rows use canonical Stage labels only.
- Representative rows use `dedupe_for_aggregate=true`; 4B overlay row is not representative.

Non-validation scope:

- Evidence URLs remain `source_proxy_only / evidence_url_pending` and should be repaired later with company IR, DART filings, or dated platform/ad market documents.
- This MD is not a live candidate scan.
- This MD does not change production scoring.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_platform_ad_arpu_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"C26 positives require traffic/ARPU/OPM bridge; ad agency recovery labels had high MAE","keeps SOOP Stage2-Actionable; demotes Nasmedia/Incross false positives","T_C26_067160_STAGE2A_20240108|T_C26_089600_STAGE2_20240119|T_C26_216050_STAGE2_20240109",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C26_local_4b_overlay_after_platform_spike,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"SOOP post-rerating showed useful 4B overlay near peak with large subsequent drawdown","adds 4B watch overlay, not hard 4C","T_C26_067160_STAGE4B_20240628",1,1,0,low,guardrail_shadow_only,"needs more 4B examples"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C26_R8L100_067160_20240108","symbol":"067160","company_name":"아프리카TV / SOOP","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive high-MFE with manageable pre-peak MAE; later 4B overlay needed","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"platform traffic migration must still connect to monetization and operating leverage"}
{"row_type":"case","case_id":"C26_R8L100_089600_20240119","symbol":"089600","company_name":"나스미디어","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"low MFE and high MAE after ad recovery label","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"ad agency recovery vocabulary without OPM/revision bridge should be capped"}
{"row_type":"case","case_id":"C26_R8L100_216050_20240109","symbol":"216050","company_name":"인크로스","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"short MFE and deep MAE after ad-tech rebound label","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"ad-tech rebound lacks durable operating leverage bridge"}
{"row_type":"trigger","trigger_id":"T_C26_067160_STAGE2A_20240108","case_id":"C26_R8L100_067160_20240108","symbol":"067160","company_name":"아프리카TV / SOOP","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","sector":"platform / streaming / ad revenue / operating leverage","primary_archetype":"platform traffic migration to monetization","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":98800,"evidence_available_at_that_date":"streaming platform traffic migration and monetization route visible before entry; source_proxy_only","evidence_source":"source_proxy_only:evidence_url_pending:platform_traffic_migration_and_monetization_route","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.53,"MFE_90D_pct":41.30,"MFE_180D_pct":45.55,"MFE_1Y_pct":45.55,"MFE_2Y_pct":null,"MAE_30D_pct":-10.63,"MAE_90D_pct":-10.63,"MAE_180D_pct":-14.07,"MAE_1Y_pct":-21.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-40.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"platform_traffic_migration_stage2_actionable_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_067160_20240108_98800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C26_067160_STAGE4B_20240628","case_id":"C26_R8L100_067160_20240108","symbol":"067160","company_name":"SOOP","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","sector":"platform / streaming / ad revenue / operating leverage","primary_archetype":"platform spike 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-28","entry_date":"2024-06-28","entry_price":131300,"evidence_available_at_that_date":"post-rerating valuation/positioning overheat after platform migration price extension; source_proxy_only","evidence_source":"source_proxy_only:evidence_url_pending:platform_event_premium_positioning_overheat","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.52,"MFE_90D_pct":9.52,"MFE_180D_pct":9.52,"MFE_1Y_pct":9.52,"MFE_2Y_pct":null,"MAE_30D_pct":-35.34,"MAE_90D_pct":-35.34,"MAE_180D_pct":-40.14,"MAE_1Y_pct":-40.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-45.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"platform_spike_stage4b_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_067160_20240628_131300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same symbol but new 4B timing path after Stage2 platform migration","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C26_089600_STAGE2_20240119","case_id":"C26_R8L100_089600_20240119","symbol":"089600","company_name":"나스미디어","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","sector":"digital ad agency / media rep / ad recovery","primary_archetype":"ad agency recovery label false positive","loop_objective":"counterexample_mining | stage2_actionable_bonus_stress_test","trigger_type":"Stage2","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":23900,"evidence_available_at_that_date":"digital ad recovery and media-rep rebound vocabulary; source_proxy_only","evidence_source":"source_proxy_only:evidence_url_pending:digital_ad_recovery_label","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.13,"MFE_90D_pct":12.13,"MFE_180D_pct":12.13,"MFE_1Y_pct":12.13,"MFE_2Y_pct":null,"MAE_30D_pct":-9.21,"MAE_90D_pct":-26.28,"MAE_180D_pct":-36.53,"MAE_1Y_pct":-42.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-24","peak_price":26800,"drawdown_after_peak_pct":-43.40,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_peak_no_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"ad_recovery_stage2_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_089600_20240119_23900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C26_216050_STAGE2_20240109","case_id":"C26_R8L100_216050_20240109","symbol":"216050","company_name":"인크로스","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MONETIZATION_AND_DIGITAL_AD_AGENCY_MARGIN_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE","sector":"ad-tech / media rep / digital ad recovery","primary_archetype":"ad-tech recovery label false positive","loop_objective":"counterexample_mining | stage2_actionable_bonus_stress_test","trigger_type":"Stage2","trigger_date":"2024-01-09","entry_date":"2024-01-09","entry_price":11660,"evidence_available_at_that_date":"ad-tech rebound and advertising normalization vocabulary; source_proxy_only","evidence_source":"source_proxy_only:evidence_url_pending:adtech_recovery_label","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.15,"MFE_90D_pct":5.15,"MFE_180D_pct":5.15,"MFE_1Y_pct":5.15,"MFE_2Y_pct":null,"MAE_30D_pct":-7.89,"MAE_90D_pct":-29.67,"MAE_180D_pct":-47.51,"MAE_1Y_pct":-47.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":12260,"drawdown_after_peak_pct":-50.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_peak_no_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"adtech_recovery_stage2_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_216050_20240109_11660","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L100_067160_20240108","trigger_id":"T_C26_067160_STAGE2A_20240108","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"traffic migration plus monetization route deserves C26 Stage2-Actionable, but not Green without confirmed margin/revision","MFE_90D_pct":41.30,"MAE_90D_pct":-10.63,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L100_089600_20240119","trigger_id":"T_C26_089600_STAGE2_20240119","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage1/Stage2-watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"generic ad recovery label lacks ARPU/OPM bridge and had high MAE","MFE_90D_pct":12.13,"MAE_90D_pct":-26.28,"score_return_alignment_label":"demotion_aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L100_216050_20240109","trigger_id":"T_C26_216050_STAGE2_20240109","symbol":"216050","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage1/Stage2-watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"ad-tech rebound without durable revenue/OPM bridge produced low MFE and high MAE","MFE_90D_pct":5.15,"MAE_90D_pct":-29.67,"score_return_alignment_label":"demotion_aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","high_MAE_guardrail"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"Priority 0 C26 shortage fill; 3 new symbols; 4 trigger families; 2 counterexamples; 1 4B overlay"}
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
completed_round = R8
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was used as the execution procedure.
- `docs/core/V12_Research_No_Repeat_Index.md` was used only as the duplicate/coverage ledger.
- `Songdaiki/stock-web` manifest/schema/profile/shard paths were used for price-source validation and OHLC path calculations.
- Evidence URLs are deliberately marked `source_proxy_only / evidence_url_pending`; a later repair loop can add company IR, DART, or dated platform/ad-market source URLs.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 3
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
