# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
scheduled_round = R7
scheduled_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE
loop_objective = coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This research does not re-propose those global axes. It stress-tests whether C25 medical-device/export cases need an archetype-specific separation between real export/reorder/margin conversion and one-off channel, reimbursement, or customer-quality narratives.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 10 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| fine_archetype_id | MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE |
| allowed archetype family | medical devices, aesthetics devices, dental implants, reimbursed/regulated healthcare devices |
| excluded | pure drug trial binary events, FDA binary CRL events, platform-only healthcare AI without export/reimbursement bridge |

R7 is the healthcare/medical-device round. The selected canonical archetype is C25, not C23/C24. C23/C24 event-risk rows are intentionally not mixed into this file.

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed R7 calibration artifact reports `102` representative triggers and `27` unique cases, with Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, and four 4C-thesis-break rows already represented. The current loop therefore avoids repeating the general Stage2-vs-Green lesson and instead adds a C25-specific compression map for export/reorder/margin bridge versus reimbursement/channel false positives.

```text
new_independent_case_count = 4
reused_case_count = 1
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 0.80
```

Reused case: `R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING` reuses symbol `214150` but tests a different 4B-overlay trigger family. It is not counted as a new independent case.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
```

The Stock-Web manifest reports `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, and the calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | 180D forward window | corporate-action status | calibration_usable |
|---|---:|---|---|---|---|
| R7L10_C25_CLASSYS_2023_EXPORT_REORDER | 214150 | atlas/symbol_profiles/214/214150.json | available | corporate-action candidate only on 2017-12-28, outside window | true |
| R7L10_C25_PHARMARESEARCH_2023_REJURAN_EXPORT | 214450 | atlas/symbol_profiles/214/214450.json | available | no corporate-action candidate | true |
| R7L10_C25_DENTIUM_2023_CHINA_VBP_HIGH_MAE | 145720 | atlas/symbol_profiles/145/145720.json | available | no corporate-action candidate | true |
| R7L10_C25_DIO_2023_DENTAL_FALSE_POSITIVE | 039840 | atlas/symbol_profiles/039/039840.json | available | corporate-action candidate only on 2015-09-04, outside window | true |
| R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING | 214150 | atlas/symbol_profiles/214/214150.json | available | corporate-action candidate outside window | true, overlay_only |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

C25 should not be a bucket for every healthcare chart that rises. The compression proposed here is:

1. **C25-A: export/reorder/margin bridge** — device/equipment or procedure-linked consumable demand is visible, export channel is widening, repeat order or installed-base economics are visible, and margin/revision confirmation follows.
2. **C25-B: reimbursement/customer concentration watch** — sales story exists but reimbursement, channel concentration, single-country demand, or customer-quality risk makes Green too early.
3. **C25-C: post-vertical-rerating 4B overlay** — device winners can continue compounding after a local peak; a price-only local peak should not become full 4B without valuation/revision/supply-chain or margin slowdown evidence.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | new_independent_case | reuse_reason |
|---|---:|---|---|---|---|---|
| R7L10_C25_CLASSYS_2023_EXPORT_REORDER | 214150 | 클래시스 | structural_success | aesthetics-device export/reorder/margin bridge | true | null |
| R7L10_C25_PHARMARESEARCH_2023_REJURAN_EXPORT | 214450 | 파마리서치 | structural_success | medical-aesthetic product export/margin bridge | true | null |
| R7L10_C25_DENTIUM_2023_CHINA_VBP_HIGH_MAE | 145720 | 덴티움 | high_mae_success/counterexample | dental implant China demand/VBP risk | true | null |
| R7L10_C25_DIO_2023_DENTAL_FALSE_POSITIVE | 039840 | 디오 | false_positive_green | dental implant recovery without durable margin bridge | true | null |
| R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING | 214150 | 클래시스 | 4B_too_early | price-only vertical rerating overlay | false | same symbol, different 4B trigger family |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
```

Positive cases show that C25 can produce durable MFE when exports/reorders convert into margin and revision. Counterexamples show that dental/medical-device headlines without customer-quality, reimbursement durability, or margin bridge can produce either high-MAE success or outright false positives.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | Stage2 fields | Stage3 fields | 4B/4C fields |
|---|---|---|---|---|---|
| CLASSYS_2023 | 2023-05-15 | research proxy: public 1Q23 earnings/reorder/export narrative available by trigger date | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, repeat_order_or_conversion, low_red_team_risk | none |
| PHARMARESEARCH_2023 | 2023-05-15 | research proxy: 1Q23 earnings and medical-aesthetic export/product mix narrative | public_event_or_disclosure, customer_or_order_quality, relative_strength, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion | none |
| DENTIUM_2023 | 2023-05-15 | research proxy: dental implant export/China VBP recovery narrative | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | partial margin bridge, but reimbursement/channel risk unresolved | valuation_blowoff, margin_or_backlog_slowdown |
| DIO_2023 | 2023-05-15 | research proxy: dental implant recovery expectation without durable conversion | public_event_or_disclosure, relative_strength | weak/unsupported confirmed revision; weak customer-quality confirmation | margin_or_backlog_slowdown, thesis_evidence_broken |
| CLASSYS_4B_2024 | 2024-05-09 | price + vertical-rerating watch; not enough non-price 4B evidence | none | none | price_only_local_peak, valuation_blowoff watch |

## 10. Price Data Source Map

| symbol | company | price_shard_path used | profile_path | stock_web_manifest_max_date |
|---:|---|---|---|---|
| 214150 | 클래시스 | atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv; 2024.csv; 2025.csv | atlas/symbol_profiles/214/214150.json | 2026-02-20 |
| 214450 | 파마리서치 | atlas/ohlcv_tradable_by_symbol_year/214/214450/2023.csv; 2024.csv | atlas/symbol_profiles/214/214450.json | 2026-02-20 |
| 145720 | 덴티움 | atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv | atlas/symbol_profiles/145/145720.json | 2026-02-20 |
| 039840 | 디오 | atlas/ohlcv_tradable_by_symbol_year/039/039840/2023.csv | atlas/symbol_profiles/039/039840.json | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | trigger_outcome_label |
|---|---|---:|---:|---:|---|---|
| R7L10_C25_CLASSYS_2023_STAGE2A | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 23900 | current_profile_correct | durable_export_reorder_winner |
| R7L10_C25_PHARMA_2023_STAGE2A | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 102900 | current_profile_correct | durable_margin_revision_winner |
| R7L10_C25_DENTIUM_2023_STAGE3Y | Stage3-Yellow | 2023-05-15 | 2023-05-15 | 150400 | current_profile_too_early | high_mae_success |
| R7L10_C25_DIO_2023_STAGE3Y | Stage3-Yellow | 2023-05-15 | 2023-05-15 | 30400 | current_profile_false_positive | false_positive_green |
| R7L10_C25_CLASSYS_2024_4B | Stage4B-overlay | 2024-05-09 | 2024-05-09 | 48500 | current_profile_4B_too_early | price_only_local_4B_too_early |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CLASSYS_2023_STAGE2A | 23900 | 48.33 | -2.93 | 75.73 | -2.93 | 80.13 | -2.93 | 2025-05-12 | 74400 | -25.13 |
| PHARMA_2023_STAGE2A | 102900 | 41.69 | -5.73 | 53.74 | -5.73 | 53.74 | -5.73 | 2023-08-11 | 158200 | -45.13 |
| DENTIUM_2023_STAGE3Y | 150400 | 23.01 | -4.19 | 23.01 | -12.43 | 23.01 | -12.43 | 2023-06-02 | 185000 | -28.81 |
| DIO_2023_STAGE3Y | 30400 | 18.26 | -9.70 | 22.04 | -10.36 | 22.04 | -32.40 | 2023-07-24 | 37100 | -44.61 |
| CLASSYS_2024_4B | 48500 | 17.32 | -5.88 | 17.32 | -5.88 | 53.40 | -5.88 | 2025-05-12 | 74400 | -25.13 |

Notes: MFE/MAE use tradable raw OHLC and include entry date. The DENTIUM 180D/1Y path is treated as high-MAE success rather than pure failure because the peak was available after entry, but the post-trigger drawdown made a Green label fragile.

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | actual path | verdict | stress finding |
|---|---|---|---|---|
| CLASSYS_2023 | Stage2-Actionable → Green once margin/revision confirmed | MFE180 +80.13, MAE180 -2.93 | current_profile_correct | Stage2 bonus worked when export/reorder/margin bridge existed |
| PHARMA_2023 | Stage2-Actionable → Green once margin bridge confirmed | MFE90 +53.74, MAE90 -5.73 | current_profile_correct | C25 Green can be justified when product mix/reorder supports margin |
| DENTIUM_2023 | likely Stage3-Yellow/Green candidate if only dental export/recovery is used | MFE30 +23.01 but MAE90 -12.43 | current_profile_too_early | Green needs reimbursement/channel-risk drag |
| DIO_2023 | Stage3-Yellow if recovery headline and relative strength are overweighted | MFE180 +22.04, MAE180 -32.40 | current_profile_false_positive | Weak customer-quality and financial-visibility evidence should block Green |
| CLASSYS_2024_4B | local 4B watch | later full-window peak much higher | current_profile_4B_too_early | price-only local peak should stay overlay-only |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-actionable entry | Stage3-Green proxy entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| CLASSYS_2023 | 23900 | 32900 | 0.47 | Green somewhat late, but still captured material upside |
| PHARMA_2023 | 102900 | 134000 | 0.56 | Green late but not terminally late; still structural winner |
| DENTIUM_2023 | 150400 | not supported | not_applicable | Green should wait for channel/reimbursement durability |
| DIO_2023 | 30400 | not supported | not_applicable | Green should be blocked |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 base | 4B entry | local_peak | full_window_peak | local proximity | full-window proximity | verdict | evidence type |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CLASSYS_2024_4B | 23900 | 48500 | 56900 | 74400 | 0.745 | 0.487 | price_only_local_4B_too_early | price_only, valuation_blowoff watch |

The C25 lesson is the same shape as a medical device installed base: a local temperature spike is not the same as product failure. Without non-price evidence such as margin slowdown, export order deterioration, reimbursement cut, or customer-quality loss, the 4B label should remain overlay-only.

## 16. 4C Protection Audit

No hard 4C row is promoted in this MD. DIO receives a `thesis_break_watch_only` label because the price path behaved like a failed recovery, but the MD does not assert a dated hard 4C thesis-break event without a specific non-price break date.

```text
four_c_protection_label_CLASSYS_2023 = not_applicable
four_c_protection_label_PHARMA_2023 = not_applicable
four_c_protection_label_DENTIUM_2023 = thesis_break_watch_only
four_c_protection_label_DIO_2023 = thesis_break_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
proposal_type = sector_shadow_only
```

Candidate rule: In L7 medical-device cases, export/reimbursement/regulatory narratives should be scored as Stage2-Actionable only when at least one of the following bridge fields is present: repeat order, installed-base utilization, reimbursement durability, customer-quality confirmation, or reported margin/revision bridge. Otherwise, the narrative should remain Stage2/watch even if relative strength is strong.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

Candidate C25 shadow rule:

```text
if canonical_archetype_id == C25:
    require_export_or_reimbursement_bridge_for_green = true
    require_margin_or_revision_confirmation_for_green = true
    add_customer_quality_drag_when_customer_or_country_concentration_unresolved = true
    keep_price_only_local_peak_as_4B_overlay_only = true
```

This is not a global rule. It is a C25 compression rule separating real export/reorder/margin compounders from dental/medical-device recovery narratives that lack durable conversion.

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | default | 4 representative | 43.63 | -7.86 | 44.73 | -13.37 | 0.50 | 0 | too permissive for C25 weak-bridge cases |
| P0b e2r_2_0_baseline_reference | rollback | 4 representative | 43.63 | -7.86 | 44.73 | -13.37 | 0.50 | 1 | weaker Stage2 capture for CLASSYS/PHARMA |
| P1 sector_specific_candidate_profile | L7 | 4 representative | 43.63 | -7.86 | 44.73 | -13.37 | 0.25 | 0 | improves weak-bridge filtering |
| P2 canonical_archetype_candidate_profile | C25 | 4 representative | 43.63 | -7.86 | 44.73 | -13.37 | 0.00 | 0 | best score-return alignment |
| P3 counterexample_guard_profile | C25 weak-bridge guard | 4 representative | 43.63 | -7.86 | 44.73 | -13.37 | 0.00 | 1 | too conservative if used without export/reorder exception |

## 20. Score-Return Alignment Matrix

| case | weighted_before | stage_before | weighted_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| CLASSYS_2023 | 84 | Stage3-Yellow | 90 | Stage3-Green | 75.73 | -2.93 | strong positive alignment |
| PHARMA_2023 | 82 | Stage3-Yellow | 88 | Stage3-Green | 53.74 | -5.73 | positive alignment |
| DENTIUM_2023 | 83 | Stage3-Yellow | 73 | Stage2-watch | 23.01 | -12.43 | guard improves risk alignment |
| DIO_2023 | 78 | Stage3-Yellow | 63 | Stage2-watch | 22.04 | -10.36 | guard prevents false positive |
| CLASSYS_4B_2024 | risk_overlay | 4B-watch | overlay_only | 4B-watch-only | 17.32 | -5.88 | avoids premature full 4B |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE | 2 | 2 | 1 | 0 | 4 | 1 | 5 | 4 | 2 | true | true | reduced; still needs explicit hard 4C C25 evidence in later R7 loops |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: weak_bridge_false_positive, high_mae_success, price_only_local_4B_too_early, customer_quality_gap
new_axis_proposed: null
existing_axis_strengthened: C25-specific export/reorder/margin bridge gate; C25 customer-quality drag; C25 price-only 4B overlay-only handling
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted basis
- profile availability and corporate-action candidate windows
- tradable OHLC rows for entry and forward windows
- representative trigger MFE/MAE 30D/90D/180D
- C25 positive/counterexample balance
- local 4B vs full-window 4B proximity split
```

Not validated:

```text
- production scoring code
- current/live candidate scan
- brokerage or trading execution
- exact production score values
- external API route discovery
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_export_reorder_margin_bridge_required_for_green,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"CLASSYS/PHARMA winners had repeat-order/margin bridge while DENTIUM/DIO had weaker durable conversion","reduced false positive risk without missing two structural winners","R7L10_C25_CLASSYS_2023_STAGE2A|R7L10_C25_PHARMA_2023_STAGE2A|R7L10_C25_DENTIUM_2023_STAGE3Y|R7L10_C25_DIO_2023_STAGE3Y",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_customer_quality_or_country_concentration_drag,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Dental/device recovery narratives with unresolved customer/country quality showed high MAE or false positive behavior","DENTIUM and DIO should remain Stage2/watch or Yellow rather than Green","R7L10_C25_DENTIUM_2023_STAGE3Y|R7L10_C25_DIO_2023_STAGE3Y",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_price_only_local_peak_is_overlay_only,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,1,1,0,"CLASSYS 2024 local peak was not full-cycle peak; existing full_4b_requires_non_price_evidence is kept","prevents premature 4B promotion","R7L10_C25_CLASSYS_2024_4B",1,0,0,medium,axis_strengthened,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L10_C25_CLASSYS_2023_EXPORT_REORDER","symbol":"214150","company_name":"클래시스","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L10_C25_CLASSYS_2023_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Export/reorder/margin bridge produced low-MAE high-MFE path."}
{"row_type":"case","case_id":"R7L10_C25_PHARMARESEARCH_2023_REJURAN_EXPORT","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L10_C25_PHARMA_2023_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment_with_drawdown_after_peak","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Product mix/export margin bridge produced strong 90D MFE; later drawdown warns against stale Green."}
{"row_type":"case","case_id":"R7L10_C25_DENTIUM_2023_CHINA_VBP_HIGH_MAE","symbol":"145720","company_name":"덴티움","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REIMBURSEMENT_CHANNEL_RISK","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R7L10_C25_DENTIUM_2023_STAGE3Y","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mfe_high_mae_misalignment","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Dental export/VBP recovery narrative had upside but high MAE and channel risk."}
{"row_type":"case","case_id":"R7L10_C25_DIO_2023_DENTAL_FALSE_POSITIVE","symbol":"039840","company_name":"디오","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_RECOVERY_WITHOUT_CUSTOMER_QUALITY_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L10_C25_DIO_2023_STAGE3Y","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_prevented_by_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Relative strength and recovery narrative failed to convert into durable price path."}
{"row_type":"case","case_id":"R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING","symbol":"214150","company_name":"클래시스","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_PRICE_ONLY_VERTICAL_RERATING_4B_OVERLAY","case_type":"4B_too_early","positive_or_counterexample":"overlay","best_trigger":"R7L10_C25_CLASSYS_2024_4B","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same symbol as positive case, different 4B trigger family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"score_price_alignment":"price_only_local_4B_too_early","current_profile_verdict":"current_profile_4B_too_early","price_source":"Songdaiki/stock-web","notes":"Local price peak was not full-cycle peak; full 4B requires non-price evidence."}
{"row_type":"trigger","trigger_id":"R7L10_C25_CLASSYS_2023_STAGE2A","case_id":"R7L10_C25_CLASSYS_2023_EXPORT_REORDER","symbol":"214150","company_name":"클래시스","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE","sector":"medical_device_aesthetics","primary_archetype":"export_reorder_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-15","entry_price":23900,"evidence_available_at_that_date":"1Q23 public earnings/export reorder narrative proxy","evidence_source":"research_proxy_public_earnings_and_analyst_summary","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":48.33,"MFE_90D_pct":75.73,"MFE_180D_pct":80.13,"MFE_1Y_pct":138.08,"MFE_2Y_pct":211.30,"MAE_30D_pct":-2.93,"MAE_90D_pct":-2.93,"MAE_180D_pct":-2.93,"MAE_1Y_pct":-2.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-05-12","peak_price":74400,"drawdown_after_peak_pct":-25.13,"green_lateness_ratio":0.47,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"durable_export_reorder_winner","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L10_C25_CLASSYS_2023_20230515_23900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L10_C25_PHARMA_2023_STAGE2A","case_id":"R7L10_C25_PHARMARESEARCH_2023_REJURAN_EXPORT","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_ORDER_MARGIN_BRIDGE","sector":"medical_aesthetic_product","primary_archetype":"export_product_mix_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-15","entry_price":102900,"evidence_available_at_that_date":"1Q23 earnings/product mix/export narrative proxy","evidence_source":"research_proxy_public_earnings_and_analyst_summary","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214450/2023.csv","profile_path":"atlas/symbol_profiles/214/214450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.69,"MFE_90D_pct":53.74,"MFE_180D_pct":53.74,"MFE_1Y_pct":53.74,"MFE_2Y_pct":null,"MAE_30D_pct":-5.73,"MAE_90D_pct":-5.73,"MAE_180D_pct":-5.73,"MAE_1Y_pct":-15.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-11","peak_price":158200,"drawdown_after_peak_pct":-45.13,"green_lateness_ratio":0.56,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"durable_margin_revision_winner","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L10_C25_PHARMA_2023_20230515_102900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L10_C25_DENTIUM_2023_STAGE3Y","case_id":"R7L10_C25_DENTIUM_2023_CHINA_VBP_HIGH_MAE","symbol":"145720","company_name":"덴티움","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REIMBURSEMENT_CHANNEL_RISK","sector":"dental_implant","primary_archetype":"export_reimbursement_channel_risk","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2023-05-15","entry_date":"2023-05-15","entry_price":150400,"evidence_available_at_that_date":"dental export/China VBP recovery narrative proxy","evidence_source":"research_proxy_public_report_summary","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["partial_margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv","profile_path":"atlas/symbol_profiles/145/145720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.01,"MFE_90D_pct":23.01,"MFE_180D_pct":23.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.19,"MAE_90D_pct":-12.43,"MAE_180D_pct":-12.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-02","peak_price":185000,"drawdown_after_peak_pct":-28.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L10_C25_DENTIUM_2023_20230515_150400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L10_C25_DIO_2023_STAGE3Y","case_id":"R7L10_C25_DIO_2023_DENTAL_FALSE_POSITIVE","symbol":"039840","company_name":"디오","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_RECOVERY_WITHOUT_CUSTOMER_QUALITY_BRIDGE","sector":"dental_implant","primary_archetype":"weak_customer_quality_recovery","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage3-Yellow","trigger_date":"2023-05-15","entry_date":"2023-05-15","entry_price":30400,"evidence_available_at_that_date":"dental implant recovery narrative proxy without durable customer-quality bridge","evidence_source":"research_proxy_public_report_summary","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039840/2023.csv","profile_path":"atlas/symbol_profiles/039/039840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.26,"MFE_90D_pct":22.04,"MFE_180D_pct":22.04,"MFE_1Y_pct":22.04,"MFE_2Y_pct":null,"MAE_30D_pct":-9.70,"MAE_90D_pct":-10.36,"MAE_180D_pct":-32.40,"MAE_1Y_pct":-32.40,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-24","peak_price":37100,"drawdown_after_peak_pct":-44.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L10_C25_DIO_2023_20230515_30400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L10_C25_CLASSYS_2024_4B","case_id":"R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING","symbol":"214150","company_name":"클래시스","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_PRICE_ONLY_VERTICAL_RERATING_4B_OVERLAY","sector":"medical_device_aesthetics","primary_archetype":"price_only_4B_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":48500,"evidence_available_at_that_date":"vertical price move; no hard non-price 4B thesis break","evidence_source":"stock_web_price_path_plus_research_proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.32,"MFE_90D_pct":17.32,"MFE_180D_pct":53.40,"MFE_1Y_pct":53.40,"MFE_2Y_pct":null,"MAE_30D_pct":-5.88,"MAE_90D_pct":-5.88,"MAE_180D_pct":-5.88,"MAE_1Y_pct":-5.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-05-12","peak_price":74400,"drawdown_after_peak_pct":-25.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.745,"four_b_full_window_peak_proximity":0.487,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"price_only_local_4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L10_C25_CLASSYS_2024_20240509_48500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as structural success but different 4B trigger family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L10_C25_CLASSYS_2023_EXPORT_REORDER","trigger_id":"R7L10_C25_CLASSYS_2023_STAGE2A","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":9,"revision_score":9,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":10},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score"],"component_delta_explanation":"C25 export/reorder/margin bridge supports Green rather than generic healthcare Yellow.","MFE_90D_pct":75.73,"MAE_90D_pct":-2.93,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L10_C25_PHARMARESEARCH_2023_REJURAN_EXPORT","trigger_id":"R7L10_C25_PHARMA_2023_STAGE2A","symbol":"214450","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":9},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","customer_quality_score","channel_reorder_score"],"component_delta_explanation":"Product-mix/export margin bridge supports C25 Green, but later drawdown requires 4B overlay after valuation expansion.","MFE_90D_pct":53.74,"MAE_90D_pct":-5.73,"score_return_alignment_label":"positive_alignment_with_later_4B_watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L10_C25_DENTIUM_2023_CHINA_VBP_HIGH_MAE","trigger_id":"R7L10_C25_DENTIUM_2023_STAGE3Y","symbol":"145720","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":4},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":2},"weighted_score_after":73,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C25 channel/reimbursement concentration drag prevents Green despite initial MFE.","MFE_90D_pct":23.01,"MAE_90D_pct":-12.43,"score_return_alignment_label":"guard_improves_risk_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L10_C25_DIO_2023_DENTAL_FALSE_POSITIVE","trigger_id":"R7L10_C25_DIO_2023_STAGE3Y","symbol":"039840","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":3},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":1},"weighted_score_after":63,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"Weak customer-quality and missing repeat-order bridge would have prevented a false Green/Yellow promotion.","MFE_90D_pct":22.04,"MAE_90D_pct":-10.36,"score_return_alignment_label":"false_positive_prevented_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L10_C25_CLASSYS_4B_2024_VERTICAL_RERATING","trigger_id":"R7L10_C25_CLASSYS_2024_4B","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":8},"weighted_score_before":null,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":8},"weighted_score_after":null,"stage_label_after":"Stage4B-overlay-only","changed_components":[],"component_delta_explanation":"Price-only local peak is not enough for full 4B because later full-window peak was higher.","MFE_90D_pct":17.32,"MAE_90D_pct":-5.88,"score_return_alignment_label":"price_only_full_4B_too_early","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"residual_contribution","round":"R7","loop":"10","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":4,"reused_case_count":1,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["weak_bridge_false_positive","high_mae_success","price_only_local_4B_too_early","customer_quality_gap"],"diversity_score_summary":"new_symbols=4; new_trigger_families=4; counterexample_gap_filled=2; residual_error_types=4; wrong_round_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 10
next_round = R8
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `reports/e2r_calibration/by_round/R7.md` was used only for coverage and duplicate-avoidance context.
- `atlas/manifest.json` was used for Stock-Web source validation.
- `atlas/symbol_profiles/214/214150.json`, `214/214450.json`, `145/145720.json`, and `039/039840.json` were used for symbol-level eligibility and corporate-action-window checks.
- `atlas/ohlcv_tradable_by_symbol_year/...` tradable shards were used for OHLC calculations. Raw shards were not used for quantitative calibration.
- This MD is historical calibration research, not investment advice and not a live candidate screen.

