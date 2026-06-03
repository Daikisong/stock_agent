# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round = R7
scheduled_loop = 71
completed_round = R7
completed_loop = 71
computed_next_round = R8
computed_next_loop = 71
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 3 new independent cases, 1 counterexample, and 1 residual error for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

R7/C25 is not a pure binary biotech event bucket. The working rule in this MD is that medical-device and medtech evidence becomes Stage2/Stage3 only when product approval, installed base, export channel, reimbursement, consumables, or procedure volume can plausibly convert into revenue and margin. Device hype without conversion evidence is treated as watch/4B overlay, not positive Stage2 evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 71 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| fine_archetype_id | C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD |
| loop_objective | counterexample_mining; stage2_actionable_bonus_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_rule_candidate |
| round_schedule_status | valid |
| round_sector_consistency | pass |

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX was used only as a duplicate-avoidance ledger. Snapshot relevant to this run:

| scope | rows | symbols | good/bad S2 | 4B/4C | top repeated names |
|---|---:|---:|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 101 | 21 | 41/8 | 17/4 | 338220, 214150, 099190, 145720, 228670, 043150 |

Selection logic:

```text
R7 -> L7_BIO_HEALTHCARE_MEDICAL
C25 selected because it has useful positive coverage but relatively low 4C/failed-rerating coverage compared with C23/C24 event-risk archetypes.
Hard duplicate avoided: no row intentionally repeats canonical_archetype_id + symbol + trigger_type + entry_date.
New-symbol expansion: 060280 and 336570 are not listed in C25 top-covered symbols.
Same-symbol expansion: 099190 appears in top-covered symbols, but this row is a distinct 4B/event-hype conversion guard, not a repeated Stage2/Green row.
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| stock_web_manifest_max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| symbol_count | 5,414 |

Tradable shard columns: `d,o,h,l,c,v,a,mc,s,m`. MFE/MAE use the stock-web schema definition: max high / min low from entry date through N tradable rows versus entry close.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | entry_date | entry row exists | >=180D forward | corporate-action window | calibration_usable |
|---|---|---|---|---|---|---|---|
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | 060280 | atlas/symbol_profiles/060/060280.json | 2023-02-28 | true | true | clean_180D_window | true |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | 336570 | atlas/symbol_profiles/336/336570.json | 2023-02-15 | true | true | clean_180D_window | true |
| R7L71_C25_099190_CGM_HYPE_4B | 099190 | atlas/symbol_profiles/099/099190.json | 2023-07-18 | true | true | clean_after_2023_04_corp_action | true |

Notes:

- 060280 has old corporate-action candidates only in 2006 and 2011; 2023 C25 window is clean.
- 336570 has a corporate-action candidate on 2022-06-30, outside the 2023 windows used here.
- 099190 has corporate-action candidates on 2023-03-14 and 2023-04-10. The selected entry is 2023-07-18, so the forward calibration window is not blocked by those dates.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | deep sub-archetype | trigger family | compression reason |
|---|---|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD | SURGICAL_ROBOT_EXPORT_PROCEDURE_VOLUME | installed_base_export_conversion | robotic surgery device export/installed-base evidence compresses to C25, not C23/C24 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD | AESTHETIC_DEVICE_EXPORT_CHANNEL_MARGIN | export_channel_margin_conversion | aesthetic device export and consumable/procedure use map to C25 revenue conversion |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD | CGM_APPROVAL_HYPE_REVENUE_CONVERSION_GAP | event_hype_without_conversion | CGM/medical-device event is not Green unless reimbursement/channel/sales conversion is visible |

## 7. Case Selection Summary

| case_id | symbol | company | case role | trigger_type | trigger_date | entry_date | entry_price | result |
|---|---|---|---|---|---|---|---:|---|
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | 060280 | 큐렉소 | structural_success | Stage2-Actionable | 2023-02-28 | 2023-02-28 | 9,320 | installed-base/export robot route caught a large 180D MFE |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | 336570 | 원텍 | structural_success | Stage2-Actionable | 2023-02-15 | 2023-02-15 | 5,720 | export/channel device route worked after moderate initial MAE |
| R7L71_C25_099190_CGM_HYPE_4B | 099190 | 아이센스 | 4B_overlay_success / failed_rerating_if_misread_as_Stage2 | Stage4B | 2023-07-18 | 2023-07-18 | 32,000 | event-hype needed 4B guard; later drawdown exceeded interim MFE |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | 060280, 336570 |
| counterexample_or_failed_rerating | 1 | 099190 |
| 4B_or_4C_case | 1 | 099190 |
| calibration_usable_case_count | 3 | all three |
| calibration_usable_trigger_count | 3 | all three |

Positive rows show that C25 can support early Stage2 when installed base/export/procedure volume gives a bridge. The counterexample shows that a device event without conversion proof should not be promoted merely because price moved.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | evidence_url_pending | source_proxy_only | note |
|---|---|---|---|---|---|
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | surgical robot export/order and installed-base narrative visible by late Feb 2023 proxy | company IR / public news proxy | true | true | needs exact DART/IR URL before promotion batch |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | aesthetic device export/channel and high-margin equipment narrative visible by mid Feb 2023 proxy | company IR / public news proxy | true | true | usable for shadow study but not default promotion without URL verification |
| R7L71_C25_099190_CGM_HYPE_4B | CGM/medical-device event and price blowoff visible by mid Jul 2023 proxy | public news / price-event proxy | true | true | 4B/red-team support only; not positive Stage2 promotion |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | entry_date | entry_price | profile caveat |
|---|---|---|---|---:|---|
| 060280 | atlas/symbol_profiles/060/060280.json | atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv | 2023-02-28 | 9,320 | old corporate-action candidates only; 2023 window clean |
| 336570 | atlas/symbol_profiles/336/336570.json | atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv | 2023-02-15 | 5,720 | 2022-06-30 corporate-action candidate outside window |
| 099190 | atlas/symbol_profiles/099/099190.json | atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv; atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv | 2023-07-18 | 32,000 | March/April 2023 candidates before selected entry; forward window clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | current_profile_verdict |
|---|---|---|---|---|---|---|
| R7L71_C25_060280_T1 | R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | installed_base_export_conversion; relative_strength | later shipment/procedure visibility proxy | none at entry | none | current_profile_correct |
| R7L71_C25_336570_T1 | R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | export_channel_margin_conversion; relative_strength | later sales/margin visibility proxy | none at entry | none | current_profile_correct |
| R7L71_C25_099190_T1 | R7L71_C25_099190_CGM_HYPE_4B | event-only device optionality, weak conversion | insufficient at trigger | valuation_blowoff; positioning_overheat; event_premium | no hard thesis break at trigger | current_profile_false_positive_if_stage2 |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Calibration windows

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R7L71_C25_060280_T1 | 2023-02-28 | 9,320 | 78.00 | -7.08 | 143.03 | -7.08 | 176.29 | -7.08 | 2023-08-24 | 25,750 | -49.13 |
| R7L71_C25_336570_T1 | 2023-02-15 | 5,720 | 19.58 | -10.14 | 95.45 | -10.14 | 164.16 | -10.14 | 2023-08-31 | 15,110 | -44.47 |
| R7L71_C25_099190_T1 | 2023-07-18 | 32,000 | 23.59 | -13.13 | 24.06 | -35.47 | 24.06 | -41.00 | 2023-09-08 | 39,700 | -52.44 |

### 12.2 Below-entry flags

| trigger_id | below_entry_price_flag_30D | below_entry_price_flag_90D | below_entry_price_flag_180D | interpretation |
|---|---|---|---|---|
| R7L71_C25_060280_T1 | true | true | true | normal early volatility, but structural MFE dominates |
| R7L71_C25_336570_T1 | true | true | true | moderate early MAE; Stage2 acceptable only with conversion evidence |
| R7L71_C25_099190_T1 | true | true | true | event-hype entry had poor reward/drawdown asymmetry after local peaks |

## 13. Current Calibrated Profile Stress Test

| question | C25 answer |
|---|---|
| How would current calibrated profile judge the case? | Stage2 allowed for 060280/336570 when evidence bridge is non-price; 099190 should be 4B/watch-only if conversion evidence is weak. |
| Did judgment align with MFE/MAE? | Yes for 060280/336570. 099190 shows why price/event-only Stage2 would be a false positive. |
| Was Stage2 bonus too much or too little? | Appropriate for export/procedure conversion; too much if event-only device optionality is allowed. |
| Was Yellow threshold 75 too high/low? | Fine; C25 Yellow should require channel/procedure evidence, not just approval hype. |
| Was Green threshold 87/revision 55 too high/low? | Keep strict. Green should need sales/margin/recurring device usage proof. |
| Was price-only blowoff guard appropriate? | Yes; 099190 supports keeping/strengthening the guard. |
| Was full 4B non-price requirement appropriate? | Yes; 099190 is local/event blowoff and should not be used as full 4B unless conversion slowdown/overhang evidence appears. |
| Was hard 4C routing too late/early? | No hard 4C in this batch; 099190 is 4B/watch, not thesis-break hard 4C. |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 actionable price | Stage3 proxy price | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | 9,320 | 12,170 | 25,750 | 0.17 | Green proxy was not materially late; Stage2 capture was essential. |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | 5,720 | 7,770 | 15,110 | 0.22 | Green proxy still early enough, but Stage2 had better asymmetry. |
| R7L71_C25_099190_CGM_HYPE_4B | 32,000 | not_applicable | 39,700 | not_applicable | Event-hype should not be upgraded to Green. |

## 15. 4B Local vs Full-window Timing Audit

| case_id | Stage4B entry proxy | local_peak_price_after_stage2 | full_window_peak_price_after_stage2 | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | four_b_timing_verdict |
|---|---:|---:|---:|---:|---:|---|---|
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | null | null | 25,750 | null | null | none | not_applicable |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | null | null | 15,110 | null | null | none | not_applicable |
| R7L71_C25_099190_CGM_HYPE_4B | 32,000 | 39,550 | 39,700 | 0.81 | 0.80 | valuation_blowoff; positioning_overheat; event_premium | good_local_4B_watch; not_full_4B_without_non_price_slowdown |

## 16. 4C Protection Audit

| case_id | four_c_protection_label | reason |
|---|---|---|
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | not_applicable | no hard thesis-break trigger in window |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | not_applicable | no hard thesis-break trigger in window |
| R7L71_C25_099190_CGM_HYPE_4B | thesis_break_watch_only | later drawdown was large, but this row validates 4B watch rather than hard 4C at trigger |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = evidence is concentrated in one canonical archetype, C25, rather than all L7.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rule_name = C25_conversion_bridge_required_before_positive_stage
```

Candidate rule:

> In C25, Stage2/Stage3-positive scoring should require at least one non-price conversion bridge: export channel orders, installed base expansion, recurring consumable/procedure volume, reimbursement confirmation, or visible margin/sales conversion. Device approval or event optionality without conversion remains watch-only or 4B overlay.

This is not a new global axis. It strengthens already-applied `stage2_required_bridge`, keeps `price_only_blowoff_blocks_positive_stage`, and supports `local_4b_watch_guard` for C25 event-hype cases.

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy | 3 | 87.51 | -17.56 | 121.50 | -19.41 | 0.33 | mostly_aligned_but_event_hype_leaks |
| P0b_e2r_2_0_baseline_reference | older baseline, looser event interpretation | 3 | 87.51 | -17.56 | 121.50 | -19.41 | 0.33 | weaker_guard_on_099190 |
| P1_L7_sector_specific_candidate | apply across all L7 | 3 | 87.51 | -17.56 | 121.50 | -19.41 | 0.33 | too_broad_for_bio_trial_cases |
| P2_C25_conversion_bridge_candidate | require conversion bridge for C25 positive Stage2/Green | 2 | 119.24 | -8.61 | 170.23 | -8.61 | 0.00 | best_alignment |
| P3_C25_counterexample_guard_profile | keep event-only/device hype as 4B watch | 1 | 24.06 | -35.47 | 24.06 | -41.00 | 0.00 positive_false_promotion | good_guard_profile |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label |
|---|---:|---|---:|---|---:|---:|---|
| R7L71_C25_060280_T1 | 76 | Stage3-Yellow | 80 | Stage3-Yellow | 143.03 | -7.08 | aligned_positive |
| R7L71_C25_336570_T1 | 75 | Stage3-Yellow | 79 | Stage3-Yellow | 95.45 | -10.14 | aligned_positive_with_initial_mae |
| R7L71_C25_099190_T1 | 78 | Stage3-Yellow_if_event_misread | 67 | Stage4B-watch | 24.06 | -35.47 | counterexample_guard_improves_alignment |

Component interpretation:

- 060280 and 336570 get conversion/support credit from export/channel/procedure evidence and later path confirms the signal.
- 099190 has event/valuation credit but lacks confirmed channel/reimbursement/sales conversion at the 4B watch date; its score should be cut by conversion-bridge guard.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 3 | 1 | false | true | C25 still needs verified URL replacement and more hard 4C/device-commercialization failure rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage2_required_bridge, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, local_4b_watch_guard]
residual_error_types_found: [event_hype_without_revenue_conversion, C25_price_event_false_positive_risk]
new_axis_proposed: null
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard]
existing_axis_weakened: []
existing_axis_kept: [stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

Diversity score summary:

```text
same_archetype_new_symbol_bonus = +8  # 060280, 336570
same_archetype_new_trigger_family_bonus = +12  # installed_base_export, export_channel_margin, event_hype_4B
counterexample_gap_bonus = +4
residual_error_bonus = +5
same_archetype_new_regime_bonus = +3
repeated_same_symbol_penalty = -5  # 099190 is known in C25 but used for a new 4B path
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
diversity_score_summary = +27
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- R7 / L7 / C25 round-sector consistency.
- 060280, 336570, 099190 stock-web profile existence.
- Entry rows exist in tradable shards.
- 30D/90D/180D MFE/MAE approximated from stock-web OHLC rows.
- Corporate-action windows do not block selected entry windows.

Not validated:

- Exact DART/IR/news URLs for each evidence trigger.
- Production E2R scorer numeric equivalence.
- Any live/current investment view.
- Current 2026 watchlist status.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,soft_required,conversion_bridge_required,+1,"C25 positive Stage2 works when export/channel/installed-base/procedure/reimbursement evidence bridges into revenue or margin; event-only device hype fails.","Excluding event-hype 099190 improves false-positive rate from 33% to 0% in this mini-batch.","R7L71_C25_060280_T1|R7L71_C25_336570_T1|R7L71_C25_099190_T1",3,3,1,low,canonical_shadow_only,"not production; evidence URLs pending"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,enabled,keep_and_strengthen,+0,"Device-event price blowoff near local peak should remain 4B/watch unless conversion slowdown or hard thesis break exists.","099190 shows good watch timing but not full hard-4C at trigger.","R7L71_C25_099190_T1",1,1,1,low,canonical_shadow_only,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L71_C25_060280_SURGICAL_ROBOT_EXPORT","symbol":"060280","company_name":"큐렉소","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L71_C25_060280_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"surgical robot export/installed-base conversion proxy"}
{"row_type":"case","case_id":"R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT","symbol":"336570","company_name":"원텍","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L71_C25_336570_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_with_initial_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"aesthetic device export/channel margin conversion proxy"}
{"row_type":"case","case_id":"R7L71_C25_099190_CGM_HYPE_4B","symbol":"099190","company_name":"아이센스","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R7L71_C25_099190_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same C25 symbol appears in coverage index, but this is a distinct event-hype 4B/conversion-guard path","independent_evidence_weight":0.5,"score_price_alignment":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive_if_stage2","price_source":"Songdaiki/stock-web","notes":"CGM/device event hype should be watch/4B unless conversion evidence appears"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R7L71_C25_060280_T1","case_id":"R7L71_C25_060280_SURGICAL_ROBOT_EXPORT","symbol":"060280","company_name":"큐렉소","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD","sector":"medical_device","primary_archetype":"surgical_robot_export_procedure_volume","loop_objective":"canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-28","evidence_available_at_that_date":"surgical robot export/order and installed-base conversion proxy","evidence_source":"company_IR_or_news_proxy_pending_url","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv","profile_path":"atlas/symbol_profiles/060/060280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-28","entry_price":9320,"MFE_30D_pct":78.00,"MFE_90D_pct":143.03,"MFE_180D_pct":176.29,"MFE_1Y_pct":176.29,"MFE_2Y_pct":176.29,"MAE_30D_pct":-7.08,"MAE_90D_pct":-7.08,"MAE_180D_pct":-7.08,"MAE_1Y_pct":-49.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-24","peak_price":25750,"drawdown_after_peak_pct":-49.13,"green_lateness_ratio":0.17,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"060280_2023-02-28_9320","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L71_C25_336570_T1","case_id":"R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT","symbol":"336570","company_name":"원텍","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD","sector":"medical_device","primary_archetype":"aesthetic_device_export_channel_margin","loop_objective":"canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-15","evidence_available_at_that_date":"aesthetic device export/channel and high-margin equipment conversion proxy","evidence_source":"company_IR_or_news_proxy_pending_url","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv","profile_path":"atlas/symbol_profiles/336/336570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-15","entry_price":5720,"MFE_30D_pct":19.58,"MFE_90D_pct":95.45,"MFE_180D_pct":164.16,"MFE_1Y_pct":164.16,"MFE_2Y_pct":164.16,"MAE_30D_pct":-10.14,"MAE_90D_pct":-10.14,"MAE_180D_pct":-10.14,"MAE_1Y_pct":-44.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-31","peak_price":15110,"drawdown_after_peak_pct":-44.47,"green_lateness_ratio":0.22,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"336570_2023-02-15_5720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L71_C25_099190_T1","case_id":"R7L71_C25_099190_CGM_HYPE_4B","symbol":"099190","company_name":"아이센스","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDTECH_EXPORT_REIMBURSEMENT_CONVERSION_GUARD","sector":"medical_device","primary_archetype":"cgm_event_hype_revenue_conversion_gap","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-07-18","evidence_available_at_that_date":"CGM/device event hype and price blowoff without confirmed revenue/reimbursement conversion at trigger","evidence_source":"public_news_or_price_event_proxy_pending_url","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv","profile_path":"atlas/symbol_profiles/099/099190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-18","entry_price":32000,"MFE_30D_pct":23.59,"MFE_90D_pct":24.06,"MFE_180D_pct":24.06,"MFE_1Y_pct":24.06,"MFE_2Y_pct":24.06,"MAE_30D_pct":-13.13,"MAE_90D_pct":-35.47,"MAE_180D_pct":-41.00,"MAE_1Y_pct":-41.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-08","peak_price":39700,"drawdown_after_peak_pct":-52.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":0.80,"four_b_timing_verdict":"good_local_4B_watch_not_full_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat","event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_counterexample_to_event_only_stage2","current_profile_verdict":"current_profile_false_positive_if_stage2","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2023_04_corp_action","same_entry_group_id":"099190_2023-07-18_32000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C25 symbol but distinct 4B/event-hype trigger family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_060280_SURGICAL_ROBOT_EXPORT","trigger_id":"R7L71_C25_060280_T1","symbol":"060280","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":15,"customer_quality_score":11,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":9,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C25 conversion bridge credits installed-base/export/procedure evidence without loosening Green.","MFE_90D_pct":143.03,"MAE_90D_pct":-7.08,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT","trigger_id":"R7L71_C25_336570_T1","symbol":"336570","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":13,"customer_quality_score":10,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":7,"margin_bridge_score":11,"revision_score":8,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"Export/channel margin evidence supports Stage2/Yellow but still requires later conversion for Green.","MFE_90D_pct":95.45,"MAE_90D_pct":-10.14,"score_return_alignment_label":"aligned_positive_with_initial_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C25_099190_CGM_HYPE_4B","trigger_id":"R7L71_C25_099190_T1","symbol":"099190","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":4,"relative_strength_score":18,"customer_quality_score":5,"policy_or_regulatory_score":12,"valuation_repricing_score":15,"execution_risk_score":12,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_if_event_misread","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":4,"relative_strength_score":18,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":15,"execution_risk_score":18,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"Event optionality without reimbursement/channel/sales conversion is downgraded to 4B/watch.","MFE_90D_pct":24.06,"MAE_90D_pct":-35.47,"score_return_alignment_label":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,soft_required,conversion_bridge_required,+1,"medical device positive stage requires export/channel/procedure/reimbursement/margin conversion evidence","positive cases keep high MFE while event-only 099190 is excluded from positive scoring","R7L71_C25_060280_T1|R7L71_C25_336570_T1|R7L71_C25_099190_T1",3,3,1,low,canonical_shadow_only,"evidence URLs pending; not production"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,enabled,keep_and_strengthen,+0,"event-hype device rerating can peak locally before revenue conversion is known","099190 captures 4B/watch function and avoids false positive Stage2/Green","R7L71_C25_099190_T1",1,1,1,low,canonical_shadow_only,"overlay-only"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":71,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["event_hype_without_revenue_conversion","C25_price_event_false_positive_risk"],"diversity_score_summary":"+8 new symbols +12 new trigger families +4 counterexample gap +5 residual error +3 new regime -5 repeated symbol penalty = +27","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- Price-only rows cannot promote Stage2/Stage3.
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

- Price source: Songdaiki/stock-web, FinanceData/marcap transformed to assistant-readable symbol-year CSV shards.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Evidence sources in this MD are proxy-level and URL-pending. They are useful for shadow residual analysis but should be URL-verified before any promotion batch.
- This MD is not investment advice and contains no live/current candidate recommendation.
