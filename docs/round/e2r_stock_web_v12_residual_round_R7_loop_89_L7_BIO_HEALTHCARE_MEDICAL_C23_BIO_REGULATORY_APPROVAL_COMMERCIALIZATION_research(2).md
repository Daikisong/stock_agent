# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
selected_round: R7
selected_loop: 89
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: ONCOLOGY_DRUG_REGULATORY_APPROVAL_COMMERCIALIZATION_PARTNER_ROYALTY_4B_WATCH
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

This loop adds 3 independent cases, 2 regulatory/commercialization success paths, and 1 commercialization-premium false-positive counterexample for R7/L7/C23.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C23:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R7 -> L7_BIO_HEALTHCARE_MEDICAL
C23 -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

C23 is not simply “approval news.” It is the bridge from regulatory clearance or commercialization right into partner conversion, revenue, reimbursement/channel expansion, margin, revision, and cash generation. Approval is the key; commercialization is the door actually opening.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C23 current rows | 29 |
| C23 current symbols | 20 |
| C23 good/bad Stage2 | 11 / 7 |
| C23 4B/4C | 3 / 2 |
| C23 URL pending/proxy | 26 / 18 |
| top covered symbols | 000250, 086900, 145020, 068270, 326030, 003850 |

Selected symbols avoid the C23 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 000100 | 유한양행 | new C23 symbol versus top-covered C23 list |
| 207940 | 삼성바이오로직스 | new C23 symbol versus top-covered C23 list |
| 195940 | HK이노엔 | new C23 symbol versus top-covered C23 list |

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
| 000100 / 2024-01-29 | true | true | clean_180D_window | true |
| 207940 / 2024-01-29 | true | true | clean_180D_window | true |
| 195940 / 2024-01-03 | true | true | clean_180D_window | true |

Corporate-action notes:

- 유한양행 has corporate-action candidates only before 2021; selected 2024 window is clean.
- 삼성바이오로직스 has a corporate-action candidate in 2025-11 only; selected 2024 window is clean.
- HK이노엔 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ONCOLOGY_DRUG_REGULATORY_APPROVAL_COMMERCIALIZATION_PARTNER_ROYALTY_4B_WATCH | C23 | approval/commercial partner route can open Stage2A, but event crowding needs 4B audit |
| CDMO_REGULATORY_MANUFACTURING_CAPACITY_COMMERCIALIZATION_4B_WATCH | C23 | CDMO regulatory manufacturing and commercial batch route |
| DRUG_COMMERCIALIZATION_PREMIUM_WITHOUT_REVENUE_REVISION_BRIDGE | C23 | commercialization premium without revenue/revision conversion is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C23_YUHAN_000100_2024_01_29_LAZERTINIB_REGULATORY_COMMERCIALIZATION_RERATING | 000100 | 유한양행 | 4B_overlay_success | positive | regulatory/commercialization route produced extreme MFE and low MAE |
| C23_SAMBIO_207940_2024_01_29_CDMO_REGULATORY_MANUFACTURING_COMMERCIALIZATION | 207940 | 삼성바이오로직스 | structural_success | positive | CDMO/commercial capacity route produced controlled MFE/MAE |
| C23_HKINNON_195940_2024_01_03_DRUG_COMMERCIALIZATION_PREMIUM_REVISION_LAG | 195940 | HK이노엔 | failed_rerating | counterexample | commercialization premium had low early MFE and large MAE before bridge confirmation |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
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
| 000100 | source_proxy_only | oncology regulatory approval / partner commercialization / royalty route | required before promotion |
| 207940 | source_proxy_only | CDMO regulatory manufacturing / commercial batch conversion route | required before promotion |
| 195940 | source_proxy_only | commercialization/export narrative but revenue/revision bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json |
| 207940 | atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv | atlas/symbol_profiles/207/207940.json |
| 195940 | atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv | atlas/symbol_profiles/195/195940.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION | Stage2-Actionable | 2024-01-29 | 2024-01-29 | 60300 | oncology regulatory/commercial partner route |
| SAMBIO_207940_2024_01_29_STAGE2A_CDMO_COMMERCIALIZATION | Stage2-Actionable | 2024-01-29 | 2024-01-29 | 800000 | CDMO regulatory manufacturing / commercial batch route |
| HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM | Stage2 | 2024-01-03 | 2024-01-03 | 46500 | commercialization premium without revenue/revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 000100 | 2024-01-29 | 60300 | 33.33 | -4.64 | 38.31 | -4.64 | 176.78 | -4.64 | 2024-10-15 | 166900 | -8.03 |
| 207940 | 2024-01-29 | 800000 | 9.75 | -4.00 | 10.00 | -9.88 | 38.63 | -9.88 | 2024-09-25 | 1109000 | -13.62 |
| 195940 | 2024-01-03 | 46500 | 2.04 | -15.16 | 2.04 | -26.13 | 10.54 | -26.13 | 2024-09-23 | 51400 | -10.80 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 000100 | Stage2A/Yellow possible; 4B after regulatory event crowding | extreme MFE, low MAE | current_profile_4B_too_late |
| 207940 | Stage2A acceptable; Green waits for backlog/margin bridge | controlled MFE/MAE | current_profile_correct |
| 195940 | Stage2 risk if commercialization label is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C23 interpretation:

- Stage2A can work when regulatory approval/commercialization is tied to partner conversion, royalty/milestone, CDMO manufacturing conversion, or revenue bridge.
- Yellow/Green require revenue conversion, channel/reimbursement progress, margin bridge, revision, and cash conversion.
- Commercialization premium alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 000100 | 1.00 | 1.00 | event crowding / valuation rerating | good 4B audit after regulatory commercialization rerating |
| 207940 | 1.00 | 1.00 | capacity/backlog conversion pending | Stage2A ok; Green blocked until margin bridge |
| 195940 | 0.90 | 1.00 | weak follow-through / revision bridge absent | commercialization premium was not Stage3 |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 000100 | thesis_break_watch_only | not hard 4C, but 4B cap needed after event rerating |
| 207940 | thesis_break_watch_only | not hard 4C; controlled drawdown supports Stage2A watch |
| 195940 | hard_4c_late | revenue/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L7_BIO_HEALTHCARE_MEDICAL
confidence = low_to_medium
```

Candidate:

> In L7 healthcare names, regulatory approval or commercialization headlines can open Stage2A only when partner conversion, revenue bridge, reimbursement/channel expansion, or CDMO manufacturing conversion is visible. Without that bridge, commercialization labels should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
confidence = low_to_medium
```

Candidate C23 rule:

```text
C23_commercialization_conversion_bridge_required =
  regulatory_approval_or_commercialization_route
  AND (partner_conversion OR revenue_conversion OR reimbursement_channel_bridge OR margin_bridge OR confirmed_revision)

if commercialization_premium and conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 30 and event_crowding_or_valuation_rerating:
    add C23_peak_proximity_4B_audit = true

if MFE_90D < 15 and MAE_90D < -20:
    classify_as C23_commercialization_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 16.78 | -13.55 | 75.32 | -13.55 | 1 | useful but C23 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 16.78 | -13.55 | 75.32 | -13.55 | 1 | over-credits commercialization headlines |
| P1 sector_specific_candidate_profile | L7 | 2 promoted + 1 guard | 24.16 | -7.26 | 107.7 | -7.26 | 0 | better after conversion bridge gate |
| P2 canonical_archetype_candidate_profile | C23 | 2 promoted + 1 guard | 24.16 | -7.26 | 107.7 | -7.26 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C23 guard | 2 promoted + 1 guard | 24.16 | -7.26 | 107.7 | -7.26 | 0 | adds commercialization false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 000100 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 207940 | Stage2A aligned; Green block needed | current_profile_correct |
| 195940 | Stage2 false positive if conversion bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | mixed C23 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 2 | true | true | 29 -> projected 32 rows; reaches minimum stability threshold |

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
new_axis_proposed: C23_commercialization_conversion_bridge_required|C23_peak_proximity_4B_audit|C23_commercialization_false_positive_guardrail
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
- Uses C23 Priority 0 coverage gap.
- Uses three symbols not in the C23 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_commercialization_conversion_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"195940 shows commercialization premium can fail without revenue/revision bridge while 000100/207940 work as Stage2A","blocks 195940 false positive while preserving 000100/207940 Stage2A","YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION|SAMBIO_207940_2024_01_29_STAGE2A_CDMO_COMMERCIALIZATION|HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C23_peak_proximity_4B_audit,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"000100 extreme regulatory/commercial rerating required 4B audit after event crowding","adds 4B audit after large C23 MFE without converting price-only event crowding into Green","YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION",1,1,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C23_commercialization_false_positive_guardrail,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"195940 had low MFE and large MAE after commercialization premium","requires sales/channel/revision bridge before Stage2/Yellow promotion","HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C23_YUHAN_000100_2024_01_29_LAZERTINIB_REGULATORY_COMMERCIALIZATION_RERATING","symbol":"000100","company_name":"유한양행","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ONCOLOGY_DRUG_REGULATORY_APPROVAL_COMMERCIALIZATION_PARTNER_ROYALTY_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"regulatory approval/commercialization path captured extreme 180D MFE with small early MAE, but later event crowding requires 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C23 symbol versus top-covered C23 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C23_SAMBIO_207940_2024_01_29_CDMO_REGULATORY_MANUFACTURING_COMMERCIALIZATION","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CDMO_REGULATORY_MANUFACTURING_CAPACITY_COMMERCIALIZATION_4B_WATCH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"SAMBIO_207940_2024_01_29_STAGE2A_CDMO_COMMERCIALIZATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"CDMO/regulatory manufacturing and commercial capacity route produced 38% 180D MFE with controlled MAE, but Green still needs backlog/margin bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"new C23 symbol; clean 2024 window before 2025 corporate-action candidate"}
{"row_type":"case","case_id":"C23_HKINNON_195940_2024_01_03_DRUG_COMMERCIALIZATION_PREMIUM_REVISION_LAG","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DRUG_COMMERCIALIZATION_PREMIUM_WITHOUT_REVENUE_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"commercialization premium had only low MFE and large drawdown before revenue/revision bridge appeared","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C23 symbol; counterexample for commercialization label without sales/revision conversion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION","case_id":"C23_YUHAN_000100_2024_01_29_LAZERTINIB_REGULATORY_COMMERCIALIZATION_RERATING","symbol":"000100","company_name":"유한양행","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ONCOLOGY_DRUG_REGULATORY_APPROVAL_COMMERCIALIZATION_PARTNER_ROYALTY_4B_WATCH","sector":"bio / healthcare / medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":60300.0,"evidence_available_at_that_date":"source_proxy_only: oncology drug regulatory pathway, partner commercialization route, milestone/royalty leverage, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["regulatory_approval_route","partner_commercialization_route","royalty_milestone_route","relative_strength"],"stage3_evidence_fields":["commercial_revenue_bridge_partial","partner_conversion_partial","revision_bridge_pending"],"stage4b_evidence_fields":["event_crowding","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.33,"MFE_90D_pct":38.31,"MFE_180D_pct":176.78,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.64,"MAE_90D_pct":-4.64,"MAE_180D_pct":-4.64,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900.0,"drawdown_after_peak_pct":-8.03,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_regulatory_commercialization_rerating","four_b_evidence_type":["event_crowding","valuation_rerating"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_000100_2024_01_29_60300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SAMBIO_207940_2024_01_29_STAGE2A_CDMO_COMMERCIALIZATION","case_id":"C23_SAMBIO_207940_2024_01_29_CDMO_REGULATORY_MANUFACTURING_COMMERCIALIZATION","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CDMO_REGULATORY_MANUFACTURING_CAPACITY_COMMERCIALIZATION_4B_WATCH","sector":"bio / healthcare / medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":800000.0,"evidence_available_at_that_date":"source_proxy_only: CDMO regulatory manufacturing capacity, commercial batch conversion, backlog/margin leverage, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cdmo_regulatory_manufacturing_route","commercial_batch_conversion","capacity_backlog_route","relative_strength"],"stage3_evidence_fields":["backlog_conversion_partial","margin_bridge_partial","revision_bridge_pending"],"stage4b_evidence_fields":["valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.75,"MFE_90D_pct":10.0,"MFE_180D_pct":38.63,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.0,"MAE_90D_pct":-9.88,"MAE_180D_pct":-9.88,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-25","peak_price":1109000.0,"drawdown_after_peak_pct":-13.62,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"moderate_to_high_mfe_but_green_requires_backlog_margin_bridge","four_b_evidence_type":["valuation_rerating","capacity_backlog_conversion_pending"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_structural_mfe_controlled_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_207940_2024_01_29_800000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM","case_id":"C23_HKINNON_195940_2024_01_03_DRUG_COMMERCIALIZATION_PREMIUM_REVISION_LAG","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DRUG_COMMERCIALIZATION_PREMIUM_WITHOUT_REVENUE_REVISION_BRIDGE","sector":"bio / healthcare / medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":46500.0,"evidence_available_at_that_date":"source_proxy_only: drug commercialization/export narrative visible, but revenue conversion, reimbursement/channel expansion, and revision bridge were not confirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["drug_commercialization_premium","export_or_channel_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","revenue_revision_bridge_absent"],"stage4c_evidence_fields":["commercial_sales_bridge_absent","revision_bridge_absent","channel_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","profile_path":"atlas/symbol_profiles/195/195940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.04,"MFE_90D_pct":2.04,"MFE_180D_pct":10.54,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.16,"MAE_90D_pct":-26.13,"MAE_180D_pct":-26.13,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-23","peak_price":51400.0,"drawdown_after_peak_pct":-10.8,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"commercialization_premium_not_stage3_without_revenue_revision_bridge","four_b_evidence_type":["weak_follow_through","revenue_revision_bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_commercialization_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_195940_2024_01_03_46500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_YUHAN_000100_2024_01_29_LAZERTINIB_REGULATORY_COMMERCIALIZATION_RERATING","trigger_id":"YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable with regulatory/commercial 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Regulatory/commercialization route was highly profitable, but extreme event rerating should trigger 4B audit before Green.","MFE_90D_pct":38.31,"MAE_90D_pct":-4.64,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_SAMBIO_207940_2024_01_29_CDMO_REGULATORY_MANUFACTURING_COMMERCIALIZATION","trigger_id":"SAMBIO_207940_2024_01_29_STAGE2A_CDMO_COMMERCIALIZATION","symbol":"207940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable, Green blocked until backlog/margin bridge","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"CDMO commercialization route is structurally valid, but Green requires backlog conversion and margin/revision evidence.","MFE_90D_pct":10.0,"MAE_90D_pct":-9.88,"score_return_alignment_label":"stage2_good_green_block_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_HKINNON_195940_2024_01_03_DRUG_COMMERCIALIZATION_PREMIUM_REVISION_LAG","trigger_id":"HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM","symbol":"195940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Commercialization label without revenue/revision bridge generated drawdown before meaningful upside.","MFE_90D_pct":2.04,"MAE_90D_pct":-26.13,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 89
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C11_BATTERY_ORDERBOOK_RERATING, C14_EV_DEMAND_SLOWDOWN_4B_4C
```

If this loop is accepted, C23 moves from 29 to a projected 32 rows and reaches the minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C23 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/000/000100.json
  - atlas/symbol_profiles/207/207940.json
  - atlas/symbol_profiles/195/195940.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
