# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R7_loop_86_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
selected_round: R7
selected_loop: 86
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: FDA_BINARY_EVENT_PREMIUM_CRL_HARD_4C_PROTECTION
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

This loop adds 3 independent cases, 1 protective binary-event case, 1 bounded platform/data rerating case, and 1 small-cap clinical-event false-positive for R7/L7/C24.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C24:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R7 -> L7_BIO_HEALTHCARE_MEDICAL
C24 -> C24_BIO_TRIAL_DATA_EVENT_RISK
```

C24 is the event-risk archetype for trial data, binary approval readouts, endpoint durability, and financing/runway pressure. In this archetype, price can glow like a lab vial before the result, but the calibration question is whether the result, partner validation, cash runway, and commercialization bridge actually hold.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C24 current rows | 27 |
| C24 current symbols | 17 |
| C24 good/bad Stage2 | 11 / 4 |
| C24 4B/4C | 3 / 3 |
| C24 URL pending/proxy | 27 / 18 |
| top covered symbols | 196170, 950220, 039200, 206650, 235980, 365270 |

Selected symbols avoid the C24 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 028300 | HLB | new C24 symbol versus top-covered C24 list |
| 298380 | 에이비엘바이오 | new C24 symbol versus top-covered C24 list |
| 115180 | 큐리언트 | new C24 symbol versus top-covered C24 list |

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
| 028300 / 2024-05-16 | true | true | clean_180D_window | true |
| 298380 / 2024-03-06 | true | true | clean_180D_window | true |
| 115180 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- HLB has corporate-action candidates before 2022; selected 2024 window is clean.
- 에이비엘바이오 has zero corporate-action candidates.
- 큐리언트 has corporate-action candidates in 2024-01, but the selected 2024-03-06 forward window does not overlap those candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| FDA_BINARY_EVENT_PREMIUM_CRL_HARD_4C_PROTECTION | C24 | binary clinical/regulatory outcome risk routes to protective 4C when unresolved |
| BISPECIFIC_ANTIBODY_DATA_PLATFORM_EVENT_RERATING_4B_WATCH | C24 | platform/data event can open Stage2A but needs clinical/partner/cash bridge |
| SMALLCAP_CLINICAL_DATA_EVENT_PREMIUM_WITHOUT_FINANCING_BRIDGE | C24 | small-cap clinical-event premium without runway/partner bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C24_HLB_028300_2024_05_16_FDA_BINARY_EVENT_RISK_4C | 028300 | HLB | hard_4c_protection_success | positive | binary event premium had severe drawdown risk |
| C24_ABL_298380_2024_03_06_BISPECIFIC_DATA_PLATFORM_RERATING | 298380 | 에이비엘바이오 | structural_success | positive | platform/data route produced delayed 180D MFE with bounded MAE |
| C24_QRI_115180_2024_03_06_CLINICAL_DATA_EVENT_FALSE_POSITIVE | 115180 | 큐리언트 | failed_rerating | counterexample | clinical-event premium lacked endpoint/partner/runway bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
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
| 028300 | source_proxy_only | FDA binary event premium and unresolved trial/regulatory outcome risk | required before promotion |
| 298380 | source_proxy_only | bispecific/platform data and partner-validation route | required before promotion |
| 115180 | source_proxy_only | clinical data event premium, but endpoint/partner/runway bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json |
| 298380 | atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv | atlas/symbol_profiles/298/298380.json |
| 115180 | atlas/ohlcv_tradable_by_symbol_year/115/115180/2024.csv | atlas/symbol_profiles/115/115180.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK | 4C-Protective | 2024-05-16 | 2024-05-16 | 95800 | FDA binary event premium and unresolved outcome risk |
| ABL_298380_2024_03_06_STAGE2A_BISPECIFIC_DATA_PLATFORM | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 27300 | bispecific/platform data and partner route |
| QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT | Stage2 | 2024-03-06 | 2024-03-06 | 4595 | clinical data event premium without financing/partner bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 028300 | 2024-05-16 | 95800 | 11.59 | -52.87 | 11.59 | -52.87 | 11.59 | -52.87 | 2024-05-16 | 106900 | -57.76 |
| 298380 | 2024-03-06 | 27300 | 11.72 | -19.41 | 13.55 | -19.41 | 41.03 | -19.41 | 2024-08-29 | 38500 | -31.69 |
| 115180 | 2024-03-06 | 4595 | 9.47 | -10.45 | 9.47 | -30.03 | 9.68 | -30.36 | 2024-08-19 | 5040 | -36.51 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 028300 | Stage2/4B-watch risk if binary event risk is underweighted | severe immediate MAE | current_profile_4C_too_late |
| 298380 | Stage2A acceptable; Green waits for validation bridge | delayed MFE with bounded MAE | current_profile_correct |
| 115180 | Stage2 risk if clinical data premium is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C24 interpretation:

- Stage2A can work for validated platform/data routes.
- Yellow/Green require endpoint durability, partner validation, cash/runway support, and commercialization path.
- Binary-event premium without outcome confirmation should route to 4B/4C watch, not Stage2/Yellow.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 028300 | 1.00 | 1.00 | binary event premium | local peak aligned; hard 4C needed |
| 298380 | 0.71 | 1.00 | delayed platform rerating | Stage2A ok; Green blocked until validation bridge |
| 115180 | 0.91 | 1.00 | small-cap clinical event premium | event premium was not Stage3 without financing/partner bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 028300 | hard_4c_success | unresolved binary event risk protected against severe MAE |
| 298380 | thesis_break_watch_only | not hard 4C; bounded MAE supports Stage2A watch |
| 115180 | hard_4c_late | endpoint/partner/runway bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L7_BIO_HEALTHCARE_MEDICAL
confidence = low_to_medium
```

Candidate:

> In L7 biotech names, clinical data or approval-event visibility should not promote Stage2/Yellow unless endpoint quality, partner validation, financing runway, and commercialization bridge are visible. Binary event premiums should route to 4B/4C watch until the event is resolved.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C24_BIO_TRIAL_DATA_EVENT_RISK
confidence = low_to_medium
```

Candidate C24 rule:

```text
C24_trial_event_bridge_required =
  clinical_or_regulatory_event
  AND (endpoint_durability OR partner_validation OR financing_runway OR commercialization_bridge)

if binary_event_premium and event_outcome_unresolved:
    cap_stage = Stage1/Stage2-watch
    add C24_hard_4c_event_watch = true

if smallcap_clinical_event_premium and financing_partner_bridge_absent:
    cap_stage = Stage1/4C-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D < 15 and MAE_90D < -25:
    classify_as C24_event_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 11.54 | -34.1 | 20.77 | -34.21 | 1 | event bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 11.54 | -34.1 | 20.77 | -34.21 | 1 | over-credits binary/event premiums |
| P1 sector_specific_candidate_profile | L7 | 2 accepted + 1 guard | 12.57 | -36.14 | 26.31 | -36.14 | 0 | better after event bridge gate |
| P2 canonical_archetype_candidate_profile | C24 | 2 accepted + 1 guard | 12.57 | -36.14 | 26.31 | -36.14 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C24 guard | 2 accepted + 1 guard | 12.57 | -36.14 | 26.31 | -36.14 | 0 | adds binary-event and runway guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 028300 | protective 4C aligned; Stage2 would be false positive | current_profile_4C_too_late |
| 298380 | Stage2A aligned; Green block needed | current_profile_correct |
| 115180 | Stage2 false positive if event premium not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | mixed C24 fine ids | 2 | 1 | 2 | 2 | 3 | 0 | 3 | 3 | 2 | true | true | 27 -> projected 30 rows; reaches minimum stability threshold |

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
new_axis_proposed: C24_trial_event_bridge_required|C24_binary_event_4c_watch|C24_smallcap_event_false_positive_guardrail
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
- Uses C24 Priority 0 coverage gap.
- Uses three symbols not in the C24 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_trial_event_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"028300 and 115180 show event premium can fail without endpoint/partner/runway bridge while 298380 works only as Stage2A","blocks binary/smallcap false positives while preserving validated platform Stage2A","HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK|ABL_298380_2024_03_06_STAGE2A_BISPECIFIC_DATA_PLATFORM|QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C24_binary_event_4c_watch,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"028300 binary FDA/regulatory event premium aligned with severe drawdown","routes unresolved binary event premium to protective 4C before Stage2 promotion","HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK",1,1,0,low_to_medium,canonical_shadow_only,"4C/protection calibration only"
shadow_weight,C24_smallcap_event_false_positive_guardrail,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"115180 had low MFE and high MAE after clinical-event premium","requires financing runway/partner validation before Stage2/Yellow promotion","QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C24_HLB_028300_2024_05_16_FDA_BINARY_EVENT_RISK_4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FDA_BINARY_EVENT_PREMIUM_CRL_HARD_4C_PROTECTION","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"FDA binary-event premium had limited upside before CRL-type drawdown; protective 4C would have blocked Stage2/Yellow optimism","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new C24 symbol versus top-covered C24 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C24_ABL_298380_2024_03_06_BISPECIFIC_DATA_PLATFORM_RERATING","symbol":"298380","company_name":"에이비엘바이오","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BISPECIFIC_ANTIBODY_DATA_PLATFORM_EVENT_RERATING_4B_WATCH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"ABL_298380_2024_03_06_STAGE2A_BISPECIFIC_DATA_PLATFORM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"platform/data-event rerating produced delayed 180D MFE with bounded MAE, but Yellow/Green still require clinical validation and cash/partner bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"new C24 symbol; positive but not Green without trial/partner validation bridge"}
{"row_type":"case","case_id":"C24_QRI_115180_2024_03_06_CLINICAL_DATA_EVENT_FALSE_POSITIVE","symbol":"115180","company_name":"큐리언트","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"SMALLCAP_CLINICAL_DATA_EVENT_PREMIUM_WITHOUT_FINANCING_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"clinical/data-event premium produced only ~10% MFE before liquidity/cash-runway/event-risk drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C24 symbol; March entry avoids 2024-01 corporate-action candidate window"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK","case_id":"C24_HLB_028300_2024_05_16_FDA_BINARY_EVENT_RISK_4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FDA_BINARY_EVENT_PREMIUM_CRL_HARD_4C_PROTECTION","sector":"bio / healthcare / medical","primary_archetype":"bio_trial_data_event_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800.0,"evidence_available_at_that_date":"source_proxy_only: FDA binary-event premium, trial/regulatory event risk, and event-positioning crowding visible before decision; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["clinical_asset_event_premium","regulatory_binary_route","relative_strength_prior"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["binary_event_premium","positioning_overheat","valuation_peak"],"stage4c_evidence_fields":["trial_regulatory_event_failure_risk","crl_or_approval_failure_risk","cash_runway_or_financing_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900.0,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"binary_event_peak_aligned_but_hard_4C_required_for_trial_regulatory_failure_risk","four_b_evidence_type":["binary_event_premium","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C24_028300_2024_05_16_95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"ABL_298380_2024_03_06_STAGE2A_BISPECIFIC_DATA_PLATFORM","case_id":"C24_ABL_298380_2024_03_06_BISPECIFIC_DATA_PLATFORM_RERATING","symbol":"298380","company_name":"에이비엘바이오","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BISPECIFIC_ANTIBODY_DATA_PLATFORM_EVENT_RERATING_4B_WATCH","sector":"bio / healthcare / medical","primary_archetype":"bio_trial_data_event_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":27300.0,"evidence_available_at_that_date":"source_proxy_only: bispecific antibody / platform data route, partner validation narrative, and clinical event rerating visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["clinical_platform_data_route","partner_validation_route","relative_strength","event_pipeline_route"],"stage3_evidence_fields":["clinical_validation_partial","cash_partner_bridge_pending","commercialization_bridge_absent"],"stage4b_evidence_fields":["delayed_valuation_rerating","peak_proximity_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv","profile_path":"atlas/symbol_profiles/298/298380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.72,"MFE_90D_pct":13.55,"MFE_180D_pct":41.03,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.41,"MAE_90D_pct":-19.41,"MAE_180D_pct":-19.41,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-29","peak_price":38500.0,"drawdown_after_peak_pct":-31.69,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.71,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"delayed_platform_rerating_requires_4B_audit_but_not_hard_4C","four_b_evidence_type":["valuation_rerating","event_pipeline_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_delayed_mfe_bounded_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C24_298380_2024_03_06_27300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT","case_id":"C24_QRI_115180_2024_03_06_CLINICAL_DATA_EVENT_FALSE_POSITIVE","symbol":"115180","company_name":"큐리언트","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"SMALLCAP_CLINICAL_DATA_EVENT_PREMIUM_WITHOUT_FINANCING_BRIDGE","sector":"bio / healthcare / medical","primary_archetype":"bio_trial_data_event_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":4595.0,"evidence_available_at_that_date":"source_proxy_only: clinical data/event premium and small-cap bio rebound visible, but financing runway, partner validation, and endpoint durability bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["clinical_data_event_premium","smallcap_bio_rebound","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","financing_bridge_absent"],"stage4c_evidence_fields":["cash_runway_risk","endpoint_validation_absent","partner_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/115/115180/2024.csv","profile_path":"atlas/symbol_profiles/115/115180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.47,"MFE_90D_pct":9.47,"MFE_180D_pct":9.68,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.45,"MAE_90D_pct":-30.03,"MAE_180D_pct":-30.36,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-19","peak_price":5040.0,"drawdown_after_peak_pct":-36.51,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_clinical_data_event_premium_not_stage3_without_financing_partner_bridge","four_b_evidence_type":["event_premium","cash_runway_risk"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_data_event","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C24_115180_2024_03_06_4595","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_HLB_028300_2024_05_16_FDA_BINARY_EVENT_RISK_4C","trigger_id":"HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2 false-positive / binary event premium risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":3,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"4C-Protective, not Stage2","changed_components":["revision_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Binary clinical/regulatory event premium should route to protective 4C when approval/trial outcome bridge is unresolved.","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_ABL_298380_2024_03_06_BISPECIFIC_DATA_PLATFORM_RERATING","trigger_id":"ABL_298380_2024_03_06_STAGE2A_BISPECIFIC_DATA_PLATFORM","symbol":"298380","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-Actionable, Green blocked until validation/partner bridge","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Platform/data route can remain Stage2A, but Green requires clinical validation, partner cash bridge, and commercialization evidence.","MFE_90D_pct":13.55,"MAE_90D_pct":-19.41,"score_return_alignment_label":"stage2_good_green_block_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_QRI_115180_2024_03_06_CLINICAL_DATA_EVENT_FALSE_POSITIVE","trigger_id":"QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT","symbol":"115180","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":4,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":6,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Small-cap clinical-event premium without endpoint durability, partner bridge, or financing runway should not receive Stage2 promotion.","MFE_90D_pct":9.47,"MAE_90D_pct":-30.03,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 86
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN
```

If this loop is accepted, C24 moves from 27 to a projected 30 rows and reaches the minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C24 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/115/115180/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/028/028300.json
  - atlas/symbol_profiles/298/298380.json
  - atlas/symbol_profiles/115/115180.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
