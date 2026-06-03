# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R8
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R9
computed_next_loop: 71
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: C28_SECURITY_SOFTWARE_RETENTION_BRIDGE_GUARD
loop_objective: counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_rule_candidate
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

Current proxy remains `e2r_2_1_stock_web_calibrated`. Existing applied axes are stress-tested, not re-proposed globally:

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

## 2. Round / Large Sector / Canonical Archetype Scope

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`. This run uses `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`, because the No-Repeat snapshot shows C28 has substantial coverage but only 2 4C rows versus 20 4B rows, making C28 suitable for a bridge/guardrail residual rather than another positive-only software narrative.

Compression map:

| layer | id | definition |
|---|---|---|
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | platform/content/software/security |
| canonical | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | software/security contract retention, ARR/RPO/renewal, enterprise customer durability |
| fine | C28_SECURITY_SOFTWARE_RETENTION_BRIDGE_GUARD | event/security theme must bridge into retention/ARR/RPO or signed enterprise contract |
| deep | C28_EVENT_THEME_WITHOUT_RETENTION_FALSE_POSITIVE | price/policy/security theme without recurring evidence |
| deep | C28_ENTERPRISE_SAAS_STRATEGIC_CUSTOMER_CONVERSION | strategic customer/channel conversion with visible enterprise SaaS economics |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols are not in the C28 top-covered list shown in the No-Repeat snapshot (`012510`, `053800`, `263860`, `030520`, `131370`, `136540`), so this is a new-symbol expansion inside the same canonical archetype.

| case | symbol | duplicate status | reason |
|---|---:|---|---|
| EMRO SaaS strategic customer conversion | 058970 | new independent | not top-covered C28 symbol |
| Raonsecure mobile-ID / security policy theme | 042510 | new independent | not top-covered C28 symbol |
| Fasoo data-security theme without retention bridge | 150900 | new independent | not top-covered C28 symbol |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web manifest assumptions used in this MD:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Schema assumptions:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative rows:

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 6. Canonical Archetype Compression Map

C28 should not treat every cybersecurity, AI software, public-ID, or enterprise-software narrative as Stage2-Actionable. The real C28 bridge is closer to a subscription machine: ARR/RPO/renewal rate/customer contract quality are the gears. Price momentum alone is only the engine noise.

```text
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
required_bridge = one_or_more_of:
- signed enterprise software contract
- durable customer confirmation
- recurring software revenue / renewal / ARR / RPO proxy
- margin leverage after retention
- repeat order or retention expansion
```

## 7. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success | 058970 | 엠로 | Stage2-Actionable | 2023-02-27 | 22400 | enterprise SaaS strategic customer bridge worked |
| failed_rerating | 042510 | 라온시큐어 | Stage2-Actionable | 2024-01-26 | 2940 | mobile-ID/security event without retention bridge failed |
| failed_rerating | 150900 | 파수 | Stage2-Actionable | 2024-01-08 | 9750 | data-security theme without ARR/RPO bridge failed |

## 8. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 2
4C_case_count: 1
calibration_usable_case_count: 3
```

The positive case is not enough to loosen C28 Green. The two counterexamples argue the opposite: C28 needs a stricter non-price bridge before Stage2 bonus can travel upward into Yellow/Green.

## 9. Evidence Source Map

| symbol | evidence source status | evidence available at trigger date |
|---:|---|---|
| 058970 | source_proxy_only, evidence_url_pending | strategic enterprise SaaS/customer route and abnormal price/volume conversion |
| 042510 | source_proxy_only, evidence_url_pending | mobile-ID/security-policy theme and local price spike |
| 150900 | source_proxy_only, evidence_url_pending | data-security/security-software theme and local price spike |

## 10. Price Data Source Map

| symbol | profile | shard |
|---:|---|---|
| 058970 | atlas/symbol_profiles/058/058970.json | atlas/ohlcv_tradable_by_symbol_year/058/058970/2023.csv |
| 042510 | atlas/symbol_profiles/042/042510.json | atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv |
| 150900 | atlas/symbol_profiles/150/150900.json | atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_type | entry | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---:|---|---|---|
| R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER | Stage2-Actionable | 22400 | customer quality, SRM/SaaS route, relative strength | conversion, durable customer, visibility | later valuation blowoff |
| R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION | Stage2-Actionable | 2940 | policy option + relative strength | none | price-only local 4B, later thesis break watch |
| R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK | Stage2-Actionable | 9750 | security theme + relative strength | none | price-only local 4B, high MAE |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 058970 | 2023-02-27 | 22400 | 173.66 | 207.14 | 336.61 | -10.04 | -10.04 | -10.04 | 2023-07-20 | 97800 | -55.93 |
| 042510 | 2024-01-26 | 2940 | 4.25 | 4.25 | 4.25 | -21.09 | -22.62 | -42.55 | 2024-01-26 | 3065 | -44.89 |
| 150900 | 2024-01-08 | 9750 | 3.59 | 3.59 | 3.59 | -19.69 | -36.72 | -42.46 | 2024-01-08 | 10100 | -44.36 |

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 bonus too strong? | Yes for price/security-policy-only rows; no for enterprise SaaS customer bridge. |
| Yellow threshold 75 too loose? | Not globally; C28 should require retention bridge before Yellow. |
| Green threshold 87 / revision 55 too strict? | Correct. No Green loosening proposed. |
| price-only blowoff guard appropriate? | Yes, especially for 042510 and 150900. |
| full 4B non-price requirement appropriate? | Yes. Keep local watch separate from full 4B. |
| hard 4C routing late/early? | Slightly late for C28 when no retention bridge appears and MAE exceeds -35%. |

## 14. Stage2 / Yellow / Green Comparison

```text
058970: Stage2-Actionable was useful; Stage3-Yellow allowed after customer/conversion bridge; Green should wait for confirmed retention/ARR or durable contract economics.
042510: Stage2-Actionable would be too early if policy/security theme is treated as evidence; should remain Stage1/Watch unless retention bridge appears.
150900: Stage2-Actionable would be false positive; security theme lacks ARR/RPO/renewal/customer conversion bridge.
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 058970 | 0.94 | 0.86 | good_full_window_4B_timing_with_non_price_customer_scale_evidence |
| 042510 | 1.00 | 1.00 | price_only_local_4B_rejected_as_full_4B_but_valid_watch |
| 150900 | 1.00 | 1.00 | price_only_local_4B_rejected_as_full_4B_but_valid_watch |

## 16. 4C Protection Audit

```text
042510: high-MAE deterioration after no retention bridge => hard_4c_late
150900: high-MAE deterioration after no retention bridge => thesis_break_watch_only
058970: no hard 4C in initial 180D; later 4B watch more important than thesis-break routing.
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate: false
reason: only one large sector tested; keep rule canonical-specific.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c28_requires_retention_arr_rpo_bridge
rule:
  For C28, do not promote Stage2 security/software event rows toward Stage3-Yellow/Green unless at least one non-price retention bridge exists:
  signed enterprise software contract, recurring revenue/ARR/RPO proxy, renewal/retention proof, customer expansion, or margin leverage after retention.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 71.66 | -23.13 | 66.7% | too generous to event/security themes |
| P0b e2r_2_0_baseline_reference | 3 | 71.66 | -23.13 | 33.3% | safer but misses SaaS structural bridge |
| P1 sector_specific_candidate_profile | 3 | 71.66 | -23.13 | 66.7% | no sector-wide patch |
| P2 canonical_archetype_candidate_profile | 3 | 207.14 selected positive | -10.04 selected positive | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 3.92 | -29.67 | 0% after demotion | useful guard |

## 20. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 058970 | current_profile_correct | non-price bridge aligned with strong MFE |
| 042510 | current_profile_false_positive | weak evidence produced high MAE |
| 150900 | current_profile_false_positive | security theme failed without retention bridge |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28_SECURITY_SOFTWARE_RETENTION_BRIDGE_GUARD | 1 | 2 | 2 | 1 | 3 | 0 | 3 | 3 | 2 | false | true | C28 4C/failed-rerating bridge gap reduced |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
residual_error_types_found:
- C28 event/policy theme without retention bridge
- price-only local 4B in software/security
- high-MAE Stage2 false positive after weak security narrative
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_requires_retention_arr_rpo_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"C28 event/policy/security theme rows fail when no ARR/RPO/retention or signed enterprise contract bridge exists","2 counterexamples show low MFE and high MAE; 1 structural success survives because customer/contract bridge exists","TRG_R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER|TRG_R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION|TRG_R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,1,1,0,"price-only software/security spikes should stay watch-only unless non-price 4B evidence appears","prevents treating early local peak as full 4B; preserves watch overlay","TRG_R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION|TRG_R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK",2,2,2,medium,existing_axis_kept,"strengthens existing watch behavior without new global delta"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER","symbol":"058970","company_name":"엠로","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ENTERPRISE_SAAS_STRATEGIC_CUSTOMER_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C28 runtime should require ARR/RPO/retention/customer-contract bridge before Stage3-Green; source proxy evidence is not used as production fact."}
{"row_type":"case","case_id":"R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION","symbol":"042510","company_name":"라온시큐어","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_MOBILE_ID_SECURITY_EVENT_WITHOUT_RETENTION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C28 runtime should require ARR/RPO/retention/customer-contract bridge before Stage3-Green; source proxy evidence is not used as production fact."}
{"row_type":"case","case_id":"R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK","symbol":"150900","company_name":"파수","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_DATA_SECURITY_CONTRACT_RETENTION_WEAK_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C28 runtime should require ARR/RPO/retention/customer-contract bridge before Stage3-Green; source proxy evidence is not used as production fact."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER","case_id":"R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER","symbol":"058970","company_name":"엠로","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ENTERPRISE_SAAS_STRATEGIC_CUSTOMER_CONVERSION","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-27","entry_date":"2023-02-27","entry_price":22400,"evidence_available_at_that_date":"source_proxy_public_strategic_customer_and_enterprise_SRM_SaaS_route; evidence_url_pending","evidence_source":"source_proxy_public_strategic_customer_and_enterprise_SRM_SaaS_route; evidence_url_pending","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058970/2023.csv","profile_path":"atlas/symbol_profiles/058/058970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":173.66,"MFE_90D_pct":207.14,"MFE_180D_pct":336.61,"MFE_1Y_pct":336.61,"MFE_2Y_pct":336.61,"MAE_30D_pct":-10.04,"MAE_90D_pct":-10.04,"MAE_180D_pct":-10.04,"MAE_1Y_pct":-10.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-20","peak_price":97800,"drawdown_after_peak_pct":-55.93,"green_lateness_ratio":"0.34","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_full_window_4B_timing_with_non_price_customer_scale_evidence","four_b_evidence_type":"valuation_blowoff|positioning_overheat|revision_slowdown_watch","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION","case_id":"R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION","symbol":"042510","company_name":"라온시큐어","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_MOBILE_ID_SECURITY_EVENT_WITHOUT_RETENTION","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":2940,"evidence_available_at_that_date":"source_proxy_mobile_ID_security_policy_theme; evidence_url_pending","evidence_source":"source_proxy_mobile_ID_security_policy_theme; evidence_url_pending","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv","profile_path":"atlas/symbol_profiles/042/042510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.25,"MFE_90D_pct":4.25,"MFE_180D_pct":4.25,"MFE_1Y_pct":4.25,"MFE_2Y_pct":4.25,"MAE_30D_pct":-21.09,"MAE_90D_pct":-22.62,"MAE_180D_pct":-42.55,"MAE_1Y_pct":-42.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-26","peak_price":3065,"drawdown_after_peak_pct":-44.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_rejected_as_full_4B_but_valid_watch","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK","case_id":"R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK","symbol":"150900","company_name":"파수","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_DATA_SECURITY_CONTRACT_RETENTION_WEAK_BRIDGE","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":9750,"evidence_available_at_that_date":"source_proxy_data_security_AI_security_theme; evidence_url_pending","evidence_source":"source_proxy_data_security_AI_security_theme; evidence_url_pending","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv","profile_path":"atlas/symbol_profiles/150/150900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.59,"MFE_90D_pct":3.59,"MFE_180D_pct":3.59,"MFE_1Y_pct":3.59,"MFE_2Y_pct":3.59,"MAE_30D_pct":-19.69,"MAE_90D_pct":-36.72,"MAE_180D_pct":-42.46,"MAE_1Y_pct":-42.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-08","peak_price":10100,"drawdown_after_peak_pct":-44.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_rejected_as_full_4B_but_valid_watch","four_b_evidence_type":"price_only|valuation_blowoff","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER","trigger_id":"TRG_R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER","symbol":"058970","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":11,"relative_strength_score":12,"customer_quality_score":16,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":12,"relative_strength_score":12,"customer_quality_score":18,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","customer_quality_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"enterprise software strategic customer bridge is rewarded, but Green still waits for retention/ARR confirmation","MFE_90D_pct":207.14,"MAE_90D_pct":-10.04,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION","trigger_id":"TRG_R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION","symbol":"042510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":11,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1-Watch","changed_components":["contract_score","customer_quality_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C28 guard removes event/policy-only boost when ARR/RPO/retention evidence is absent","MFE_90D_pct":4.25,"MAE_90D_pct":-22.62,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK","trigger_id":"TRG_R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK","symbol":"150900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":11,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1-Watch","changed_components":["contract_score","customer_quality_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C28 guard removes event/policy-only boost when ARR/RPO/retention evidence is absent","MFE_90D_pct":3.59,"MAE_90D_pct":-36.72,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_requires_retention_arr_rpo_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"C28 event/policy/security theme rows fail when no ARR/RPO/retention or signed enterprise contract bridge exists","2 counterexamples show low MFE and high MAE; 1 structural success survives because customer/contract bridge exists","TRG_R8L71_C28_058970_20230227_SUPPLYCHAIN_SAAS_STRATEGIC_CUSTOMER|TRG_R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION|TRG_R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,1,1,0,"price-only software/security spikes should stay watch-only unless non-price 4B evidence appears","prevents treating early local peak as full 4B; preserves watch overlay","TRG_R8L71_C28_042510_20240126_MOBILE_ID_PRICE_ONLY_NO_RETENTION|TRG_R8L71_C28_150900_20240108_DATA_SECURITY_RETENTION_WEAK",2,2,2,medium,existing_axis_kept,"strengthens existing watch behavior without new global delta"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["event_policy_theme_without_retention_bridge","price_only_local_4B_in_C28","high_MAE_after_Stage2_security_theme"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
current_round: R8
current_loop: 71
computed_next_round: R9
computed_next_loop: 71
next_large_sector: L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending scheduler branch
```

## 28. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/058/058970.json
atlas/symbol_profiles/042/042510.json
atlas/symbol_profiles/150/150900.json
atlas/ohlcv_tradable_by_symbol_year/058/058970/2023.csv
atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv
atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
