# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_87_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
selected_round: R8
selected_loop: 87
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ERP_SAAS_CONTRACT_RETENTION_OPERATING_LEVERAGE_4B_WATCH
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

This loop adds 3 independent cases, 1 ERP/SaaS contract-retention success path, and 2 security-theme retention-bridge counterexamples for R8/L8/C28.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C28:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R8 -> L8_PLATFORM_CONTENT_SW_SECURITY
C28 -> C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

C28 is the software/security contract quality archetype. A security or software label is only the signboard; the calibration body is renewal, retention, ARR/RPO, churn control, contract conversion, and margin durability.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C28 current rows | 27 |
| C28 current symbols | 15 |
| C28 good/bad Stage2 | 6 / 7 |
| C28 4B/4C | 4 / 2 |
| C28 URL pending/proxy | 27 / 21 |
| top covered symbols | 053800, 030520, 136540, 047560, 060850, 356680 |

Selected symbols avoid the C28 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 012510 | 더존비즈온 | new C28 symbol versus top-covered C28 list |
| 203650 | 드림시큐리티 | new C28 symbol versus top-covered C28 list |
| 042510 | 라온시큐어 | new C28 symbol versus top-covered C28 list |

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
| 012510 / 2024-01-18 | true | true | clean_180D_window | true |
| 203650 / 2024-02-15 | true | true | clean_180D_window | true |
| 042510 / 2024-01-23 | true | true | clean_180D_window | true |

Corporate-action notes:

- 더존비즈온 has corporate-action candidates before 2010 only; selected 2024 window is clean.
- 드림시큐리티 has corporate-action candidates in 2017, 2019, and 2025 only; selected 2024 window is clean.
- 라온시큐어 has a corporate-action candidate in 2023-12 and 2025, but the selected 2024-01-23 forward window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ERP_SAAS_CONTRACT_RETENTION_OPERATING_LEVERAGE_4B_WATCH | C28 | ERP/SaaS contract-retention and operating leverage can support Stage2A |
| SECURITY_AUTH_THEME_WITHOUT_CONTRACT_RETENTION_BRIDGE | C28 | security/authentication theme without ARR/renewal retention is false-positive risk |
| IDENTITY_SECURITY_EVENT_PREMIUM_WITHOUT_RENEWAL_RETENTION | C28 | identity/security event premium without renewal/retention bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C28_DOUZONE_012510_2024_01_18_ERP_SAAS_CONTRACT_RETENTION_RERATING | 012510 | 더존비즈온 | 4B_overlay_success | positive | ERP/SaaS contract-retention route produced large MFE but later valuation drawdown |
| C28_DREAMSECURITY_203650_2024_02_15_SECURITY_AUTH_THEME_FALSE_POSITIVE | 203650 | 드림시큐리티 | failed_rerating | counterexample | security/auth theme had nearly no MFE and large MAE without ARR/renewal bridge |
| C28_RAONSECURE_042510_2024_01_23_IDENTITY_SECURITY_EVENT_FALSE_POSITIVE | 042510 | 라온시큐어 | failed_rerating | counterexample | identity/security event premium created local MFE but lacked retention bridge |

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
| 012510 | source_proxy_only | ERP/SaaS contract-retention and operating-leverage route | required before promotion |
| 203650 | source_proxy_only | security/authentication theme but ARR/renewal bridge absent | required; useful as counterexample |
| 042510 | source_proxy_only | identity/security event premium but renewal/retention bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 012510 | atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv | atlas/symbol_profiles/012/012510.json |
| 203650 | atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv | atlas/symbol_profiles/203/203650.json |
| 042510 | atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv | atlas/symbol_profiles/042/042510.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION | Stage2-Actionable | 2024-01-18 | 2024-01-18 | 40800 | ERP/SaaS contract retention, upsell, operating leverage |
| DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME | Stage2 | 2024-02-15 | 2024-02-15 | 4020 | security/authentication theme without ARR/renewal bridge |
| RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT | Stage2 | 2024-01-23 | 2024-01-23 | 2605 | identity/security event premium without renewal retention bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 012510 | 2024-01-18 | 40800 | 37.99 | -11.27 | 60.78 | -11.27 | 91.91 | -11.27 | 2024-07-08 | 78300 | -42.66 |
| 203650 | 2024-02-15 | 4020 | 1.37 | -11.07 | 1.37 | -27.86 | 1.37 | -43.16 | 2024-03-13 | 4075 | -43.93 |
| 042510 | 2024-01-23 | 2605 | 17.66 | -10.94 | 17.66 | -11.52 | 17.66 | -35.16 | 2024-01-26 | 3065 | -44.89 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 012510 | Stage2A/Yellow possible; 4B after SaaS rerating | high MFE then valuation drawdown | current_profile_4B_too_late |
| 203650 | Stage2 risk if security theme is over-credited | near-zero MFE and high MAE | current_profile_false_positive |
| 042510 | Stage2 risk if identity/security event is over-credited | local MFE then high 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C28 interpretation:

- Stage2A can work when ERP/SaaS or security software has visible contract retention, renewal, ARR/RPO, or operating-leverage bridge.
- Yellow/Green require renewal/churn quality, contract conversion, margin durability, and cash conversion.
- Security/authentication theme or event premium without retention bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 012510 | 1.00 | 1.00 | valuation / operating leverage | good 4B audit after ERP/SaaS rerating |
| 203650 | 1.00 | 1.00 | theme premium / weak follow-through | security theme was not Stage3 |
| 042510 | 1.00 | 1.00 | identity/security event premium | local spike was not Stage3 without renewal bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 012510 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 203650 | hard_4c_late | ARR/renewal bridge absence should have capped Stage2 earlier |
| 042510 | hard_4c_late | retention bridge absence should have capped Stage2 after event premium |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L8_PLATFORM_CONTENT_SW_SECURITY
confidence = low_to_medium
```

Candidate:

> In L8 software/security names, software label or cybersecurity theme is not enough. Stage2A requires renewal, ARR/RPO, contract retention, backlog conversion, or operating-leverage evidence. Without that bridge, event premiums should be capped at Stage1/Stage2-watch and routed to C28 false-positive or 4C-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
confidence = low_to_medium
```

Candidate C28 rule:

```text
C28_contract_retention_bridge_required =
  software_or_security_route
  AND (arr_growth OR rpo_backlog OR renewal_retention OR churn_control OR margin_bridge OR contract_conversion)

if security_theme_or_event_premium and retention_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 50 and drawdown_after_peak < -35:
    add C28_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_180D < -30:
    classify_as C28_retention_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 26.6 | -16.88 | 36.98 | -29.86 | 2 | useful but C28 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 26.6 | -16.88 | 36.98 | -29.86 | 2 | over-credits software/security themes |
| P1 sector_specific_candidate_profile | L8 | 1 promoted + 2 guard | 60.78 | -11.27 | 91.91 | -11.27 | 0 | better after retention bridge gate |
| P2 canonical_archetype_candidate_profile | C28 | 1 promoted + 2 guard | 60.78 | -11.27 | 91.91 | -11.27 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C28 guard | 1 promoted + 2 guard | 60.78 | -11.27 | 91.91 | -11.27 | 0 | adds retention false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 012510 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 203650 | Stage2 false positive if security theme not gated | current_profile_false_positive |
| 042510 | Stage2 false positive if event premium not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | mixed C28 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | 27 -> projected 30 rows; reaches minimum stability threshold |

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
new_axis_proposed: C28_contract_retention_bridge_required|C28_peak_proximity_4B_audit|C28_retention_false_positive_guardrail
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
- Uses C28 Priority 0 coverage gap.
- Uses three symbols not in the C28 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_contract_retention_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"203650 and 042510 show security/authentication themes can fail without ARR/renewal/retention bridge while 012510 works as ERP/SaaS Stage2A","blocks two false positives while preserving 012510 Stage2A","DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION|DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME|RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT",3,3,2,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C28_peak_proximity_4B_audit,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"012510 high-MFE ERP/SaaS rerating still needed 4B audit after valuation extension","adds 4B audit after large C28 MFE without converting price-only peaks into full 4B","DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION",1,1,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C28_retention_false_positive_guardrail,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"203650/042510 had weak or local MFE and high MAE after software/security event premium","requires ARR/RPO/renewal/churn bridge before Stage2/Yellow promotion","DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME|RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT",2,2,2,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C28_DOUZONE_012510_2024_01_18_ERP_SAAS_CONTRACT_RETENTION_RERATING","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_SAAS_CONTRACT_RETENTION_OPERATING_LEVERAGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ERP/SaaS contract-retention and operating-leverage route captured large MFE, but later valuation drawdown required 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C28 symbol versus top-covered list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C28_DREAMSECURITY_203650_2024_02_15_SECURITY_AUTH_THEME_FALSE_POSITIVE","symbol":"203650","company_name":"드림시큐리티","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_AUTH_THEME_WITHOUT_CONTRACT_RETENTION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"security/authentication theme had almost no MFE and later large MAE because ARR/renewal/contract retention bridge was absent","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C28 symbol; counterexample for security theme without renewal/retention proof"}
{"row_type":"case","case_id":"C28_RAONSECURE_042510_2024_01_23_IDENTITY_SECURITY_EVENT_FALSE_POSITIVE","symbol":"042510","company_name":"라온시큐어","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"IDENTITY_SECURITY_EVENT_PREMIUM_WITHOUT_RENEWAL_RETENTION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"identity/security event premium created local MFE but later collapsed without renewal, ARR, or contract-retention bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C28 symbol; 2024 window is outside 2023-12 corporate-action candidate"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION","case_id":"C28_DOUZONE_012510_2024_01_18_ERP_SAAS_CONTRACT_RETENTION_RERATING","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_SAAS_CONTRACT_RETENTION_OPERATING_LEVERAGE_4B_WATCH","sector":"platform / content / software / security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":40800.0,"evidence_available_at_that_date":"source_proxy_only: ERP/SaaS contract-retention, cloud/AI software upsell, and operating-leverage route visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["erp_saas_contract_route","retention_route","operating_leverage_route","relative_strength"],"stage3_evidence_fields":["recurring_revenue_bridge_partial","margin_bridge_partial","renewal_churn_check_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.99,"MFE_90D_pct":60.78,"MFE_180D_pct":91.91,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.27,"MAE_90D_pct":-11.27,"MAE_180D_pct":-11.27,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300.0,"drawdown_after_peak_pct":-42.66,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_erp_saas_retention_rerating","four_b_evidence_type":["valuation_rerating","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_012510_2024_01_18_40800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME","case_id":"C28_DREAMSECURITY_203650_2024_02_15_SECURITY_AUTH_THEME_FALSE_POSITIVE","symbol":"203650","company_name":"드림시큐리티","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_AUTH_THEME_WITHOUT_CONTRACT_RETENTION_BRIDGE","sector":"platform / content / software / security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":4020.0,"evidence_available_at_that_date":"source_proxy_only: security/authentication theme and event-driven relative strength visible, but ARR, renewal, and contract-retention bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["security_auth_theme","event_relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["theme_premium","weak_follow_through"],"stage4c_evidence_fields":["contract_retention_absent","arr_bridge_absent","renewal_quality_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv","profile_path":"atlas/symbol_profiles/203/203650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.37,"MFE_90D_pct":1.37,"MFE_180D_pct":1.37,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.07,"MAE_90D_pct":-27.86,"MAE_180D_pct":-43.16,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":4075.0,"drawdown_after_peak_pct":-43.93,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"security_auth_theme_not_stage3_without_arr_renewal_retention_bridge","four_b_evidence_type":["theme_premium","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_contract_retention_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_203650_2024_02_15_4020","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT","case_id":"C28_RAONSECURE_042510_2024_01_23_IDENTITY_SECURITY_EVENT_FALSE_POSITIVE","symbol":"042510","company_name":"라온시큐어","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"IDENTITY_SECURITY_EVENT_PREMIUM_WITHOUT_RENEWAL_RETENTION","sector":"platform / content / software / security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-23","entry_date":"2024-01-23","entry_price":2605.0,"evidence_available_at_that_date":"source_proxy_only: identity/security event premium and authentication theme visible, but contract renewal, ARR, and retention proof absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["identity_security_theme","authentication_event_premium","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","price_only_local_peak"],"stage4c_evidence_fields":["renewal_bridge_absent","contract_retention_absent","arr_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv","profile_path":"atlas/symbol_profiles/042/042510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.66,"MFE_90D_pct":17.66,"MFE_180D_pct":17.66,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.94,"MAE_90D_pct":-11.52,"MAE_180D_pct":-35.16,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-26","peak_price":3065.0,"drawdown_after_peak_pct":-44.89,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"identity_security_event_premium_not_stage3_without_renewal_retention_bridge","four_b_evidence_type":["event_premium","price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_local_mfe_high_180d_mae_retention_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_042510_2024_01_23_2605","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_DOUZONE_012510_2024_01_18_ERP_SAAS_CONTRACT_RETENTION_RERATING","trigger_id":"DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with C28 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"ERP/SaaS retention route worked, but C28 Yellow/Green should still require renewal/churn, ARR/RPO, and margin bridge before ignoring peak proximity.","MFE_90D_pct":60.78,"MAE_90D_pct":-11.27,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_DREAMSECURITY_203650_2024_02_15_SECURITY_AUTH_THEME_FALSE_POSITIVE","trigger_id":"DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME","symbol":"203650","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Security/authentication theme without ARR, renewal, or retention bridge had almost no MFE and high drawdown.","MFE_90D_pct":1.37,"MAE_90D_pct":-27.86,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_RAONSECURE_042510_2024_01_23_IDENTITY_SECURITY_EVENT_FALSE_POSITIVE","trigger_id":"RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT","symbol":"042510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive / event premium risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Identity/security event premium had local MFE but lacked renewal/ARR/retention bridge and then produced large 180D MAE.","MFE_90D_pct":17.66,"MAE_90D_pct":-11.52,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 87
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```

If this loop is accepted, C28 moves from 27 to a projected 30 rows and reaches the minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C28 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/012/012510.json
  - atlas/symbol_profiles/203/203650.json
  - atlas/symbol_profiles/042/042510.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
