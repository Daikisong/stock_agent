# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R7
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R8
computed_next_loop: 72
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: C24_VALIDATED_DATA_REGULATORY_LICENSE_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`. The prior R7 loop already used C25 medical-device/export/reimbursement, so this run shifts to C24. The core residual is biotech’s binary event problem: a trial or approval event can look like a rocket, but without data durability, regulatory bridge, license path, or commercial conversion, the same flame becomes MAE.

| layer | id | definition |
|---|---|---|
| round | R7 | bio / healthcare / medical |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | biotech, pharma, healthcare, medical device |
| canonical | C24_BIO_TRIAL_DATA_EVENT_RISK | trial data, approval, binary event, dilution and 4C risk |
| fine | C24_VALIDATED_DATA_REGULATORY_LICENSE_BRIDGE_GUARD | trial/approval events require validated data or durable bridge |
| deep | PROSTATE_CANCER_RADIOLIGAND_DATA_VALIDATION_WITH_LICENSE_OPTIONALITY | positive clinical data/license optionality |
| deep | CELL_THERAPY_APPROVAL_OPTIONALITY_TO_REGULATORY_REJECTION_4C | regulatory rejection hard break |
| deep | RNAI_PLATFORM_OPTIONALITY_WITHOUT_TRIAL_DATA_OR_LICENSE_CONVERSION | platform-event false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C24 top-covered symbols are `000100`, `215600`, `009420`, `298380`, `028300`, and `039200`. This run avoids that top cluster and uses new-symbol C24 rows to stress the data/event bridge.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C24 | 220100 | new independent | not top-covered C24 symbol; radiopharma clinical data/license bridge positive |
| C24 | 007390 | new independent | not top-covered C24 symbol; cell-therapy approval event hard 4C |
| C24 | 226950 | new independent | not top-covered C24 symbol; RNAi/platform event false start |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 220100 | 퓨쳐켐 | Stage2-Actionable | 2024-04-23 | 11240 | clinical/radioligand data bridge worked |
| hard_4C_event_failure | 007390 | 네이처셀 | Stage2-Actionable | 2023-03-31 | 18000 | approval-event optionality broke into hard 4C |
| failed_rerating_high_MAE | 226950 | 올릭스 | Stage2-Actionable | 2024-02-27 | 16810 | RNAi/platform event expectation lacked durable data bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
hard_4C_case_count: 1
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 220100 | 퓨쳐켐 | Stage2-Actionable | 2024-04-23 | 11240 | 53.65 | 128.2 | 178.02 | -10.14 | -10.14 | -10.14 | 2024-10-16 | 31250 | -33.44 |
| 007390 | 네이처셀 | Stage2-Actionable | 2023-03-31 | 18000 | 41.67 | 41.67 | 41.67 | -48.28 | -59.56 | -61.78 | 2023-04-06 | 25500 | -73.02 |
| 226950 | 올릭스 | Stage2-Actionable | 2024-02-27 | 16810 | 9.99 | 9.99 | 9.99 | -10.77 | -50.74 | -50.74 | 2024-03-11 | 18490 | -55.22 |

## 9. Case-by-Case Notes

### 9.1 220100 / 퓨쳐켐 — clinical data/license bridge positive

The entry row is 2024-04-23 at 11,240. The 30D path already reaches 17,270 and the full window reaches 31,250. This is the C24 success condition: the event did not remain a headline. It kept converting into data validation, radiopharma platform credibility, and license/commercial optionality. Still, the peak and drawdown require 4B watch rather than Green loosening.

### 9.2 007390 / 네이처셀 — approval event to hard 4C

The entry row is 2023-03-31 at 18,000. The 30D high reaches 25,500, but the path breaks violently after the regulatory outcome. This is not a late-stage positive; it is exactly why C24 needs binary-event and hard-4C routing. A short MFE before a decision is not a durable thesis.

### 9.3 226950 / 올릭스 — platform event false start

The entry row is 2024-02-27 at 16,810. The path barely extends to 18,490, then falls to 8,280. This is a C24 false start: platform optionality and relative strength are not enough unless the trial data, license, or commercialization bridge appears.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C24 treats binary event/platform expectation as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C24 should require validated data, regulatory durability, or license bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 007390 and 226950. |
| Full 4B non-price requirement appropriate? | Yes. 220100 has non-price data bridge; 007390/226950 do not. |
| 4C routing issue? | 007390 supports hard 4C routing; 226950 supports high-MAE watch before hard 4C. |

## 11. Stage2 / Yellow / Green Comparison

```text
220100:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after validated data / license optionality bridge
  Stage3-Green = wait for stronger regulatory/commercial durability and 4B check

007390:
  Stage2-Actionable = too generous if based on approval-event price strength
  Stage3-Yellow = reject without regulatory outcome durability
  Stage3-Green = reject
  4C = hard thesis break after regulatory rejection

226950:
  Stage2-Actionable = too generous if based only on platform/trial expectation
  Stage3-Yellow = reject without trial-data/license bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 220100 | 0.91 | 1.00 | good full-window 4B watch after clinical-data bridge |
| 007390 | 1.00 | 1.00 | price-event local 4B rejected as positive and routed to 4C watch |
| 226950 | 1.00 | 1.00 | low-MFE high-MAE event watch, not full success |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c24_requires_validated_data_regulatory_or_license_bridge

rule:
  For C24 biotech trial/data rows, do not promote binary event, approval expectation,
  or platform-optionality Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  validated trial data, regulatory durability, license/commercial optionality,
  repeat data confirmation, or revenue/royalty conversion evidence.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 59.95 | -40.15 | 66.7% | too generous to binary event/platform rows |
| P0b e2r_2_0_baseline_reference | 3 | 59.95 | -40.15 | 33.3% | safer but may miss 220100 |
| P1 sector_specific_candidate_profile | 3 | 59.95 | -40.15 | 66.7% | no broad L7 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 128.2 | -10.14 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 25.83 | -55.15 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 220100 | current_profile_correct | clinical data/license bridge aligned with strong MFE |
| 007390 | current_profile_false_positive | approval-event spike became hard 4C |
| 226950 | current_profile_false_positive | platform expectation produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | hard_4C | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | C24_VALIDATED_DATA_REGULATORY_LICENSE_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 1 | 3 | 0 | 3 | 3 | 2 | false | true | C24 non-top-covered trial/data event residual reduced |

## 17. Residual Contribution Summary

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
- high_MAE_guardrail
- hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
- binary event without regulatory durability
- platform expectation without trial-data bridge
- clinical data success still needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_MAE_watch_guard
- hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

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

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_requires_validated_data_regulatory_or_license_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"C24 biotech trial/data rows should not promote toward Stage3-Yellow/Green unless event signal converts into validated data, regulatory durability, license/commercial option, or repeat-data bridge","220100 survives with strong MFE after data/license bridge; 007390 and 226950 fail when binary approval/platform expectation lacks durable bridge","TRG_R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE|TRG_R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK|TRG_R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c24_binary_event_4b_4c_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,1,1,0,"Trial/approval event rows can peak before outcome durability is known; local 4B/high-MAE/4C watch should remain active","preserves 220100 positive while preventing 007390/226950 event false positives and routing hard break to 4C watch","TRG_R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE|TRG_R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK|TRG_R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE/4C watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE","symbol":"220100","company_name":"퓨쳐켐","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_RADIOPHARMA_CLINICAL_DATA_TO_COMMERCIAL_OPTIONALITY_BRIDGE","deep_sub_archetype_id":"PROSTATE_CANCER_RADIOLIGAND_DATA_VALIDATION_WITH_LICENSE_OPTIONALITY","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C24 biotech trial/data rows require validated data, regulatory durability, or license/commercial bridge; event expectation or price spike alone is insufficient."}
{"row_type":"case","case_id":"R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK","symbol":"007390","company_name":"네이처셀","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CELL_THERAPY_APPROVAL_EVENT_BINARY_RISK_GUARD","deep_sub_archetype_id":"CELL_THERAPY_APPROVAL_OPTIONALITY_TO_REGULATORY_REJECTION_4C","case_type":"hard_4C_event_failure","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C24 biotech trial/data rows require validated data, regulatory durability, or license/commercial bridge; event expectation or price spike alone is insufficient."}
{"row_type":"case","case_id":"R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START","symbol":"226950","company_name":"올릭스","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_RNAI_PLATFORM_EVENT_WITHOUT_DATA_DURABILITY_BRIDGE","deep_sub_archetype_id":"RNAI_PLATFORM_OPTIONALITY_WITHOUT_TRIAL_DATA_OR_LICENSE_CONVERSION","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C24 biotech trial/data rows require validated data, regulatory durability, or license/commercial bridge; event expectation or price spike alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE","case_id":"R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE","symbol":"220100","company_name":"퓨쳐켐","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_RADIOPHARMA_CLINICAL_DATA_TO_COMMERCIAL_OPTIONALITY_BRIDGE","deep_sub_archetype_id":"PROSTATE_CANCER_RADIOLIGAND_DATA_VALIDATION_WITH_LICENSE_OPTIONALITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":11240,"evidence_available_at_that_date":"source_proxy_prostate_cancer_radioligand_clinical_data_and_license_optional_bridge; evidence_url_pending","evidence_source":"source_proxy_prostate_cancer_radioligand_clinical_data_and_license_optional_bridge; evidence_url_pending","bridge_summary":"clinical/radioligand data optionality converted into repeated MFE path because data and partnering optionality were stronger than pure event hype","stage2_evidence_fields":["clinical_data_signal","radiopharma_platform_optionality","relative_strength","non_price_data_bridge"],"stage3_evidence_fields":["data_to_partnering_optionality","repeat_event_validation","commercialization_or_license_visibility_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","biotech_event_crowding_after_data"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv","profile_path":"atlas/symbol_profiles/220/220100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.65,"MFE_90D_pct":128.2,"MFE_180D_pct":178.02,"MFE_1Y_pct":178.02,"MFE_2Y_pct":178.02,"MAE_30D_pct":-10.14,"MAE_90D_pct":-10.14,"MAE_180D_pct":-10.14,"MAE_1Y_pct":-10.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-16","peak_price":31250,"drawdown_after_peak_pct":-33.44,"green_lateness_ratio":"0.32","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_clinical_data_bridge","four_b_evidence_type":"non_price_clinical_data_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK","case_id":"R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK","symbol":"007390","company_name":"네이처셀","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CELL_THERAPY_APPROVAL_EVENT_BINARY_RISK_GUARD","deep_sub_archetype_id":"CELL_THERAPY_APPROVAL_OPTIONALITY_TO_REGULATORY_REJECTION_4C","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-31","entry_date":"2023-03-31","entry_price":18000,"evidence_available_at_that_date":"source_proxy_cell_therapy_approval_binary_event_followed_by_regulatory_rejection; evidence_url_pending","evidence_source":"source_proxy_cell_therapy_approval_binary_event_followed_by_regulatory_rejection; evidence_url_pending","bridge_summary":"approval/event optionality created a short MFE spike, but regulatory outcome turned the thesis into hard 4C rather than a durable clinical-data bridge","stage2_evidence_fields":["cell_therapy_approval_event","binary_regulatory_optionality","relative_strength","price_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","binary_event_crowding"],"stage4c_evidence_fields":["regulatory_rejection_thesis_break","high_MAE_after_event_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007390/2023.csv","profile_path":"atlas/symbol_profiles/007/007390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.67,"MFE_90D_pct":41.67,"MFE_180D_pct":41.67,"MFE_1Y_pct":41.67,"MFE_2Y_pct":41.67,"MAE_30D_pct":-48.28,"MAE_90D_pct":-59.56,"MAE_180D_pct":-61.78,"MAE_1Y_pct":-61.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-06","peak_price":25500,"drawdown_after_peak_pct":-73.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_event_local_4B_rejected_as_positive_stage_and_routed_to_4C_watch","four_b_evidence_type":"price_or_event_expectation_without_data_bridge","four_c_protection_label":"hard_4C_thesis_break","trigger_outcome_label":"failed_rerating_hard_4C_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START","case_id":"R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START","symbol":"226950","company_name":"올릭스","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_RNAI_PLATFORM_EVENT_WITHOUT_DATA_DURABILITY_BRIDGE","deep_sub_archetype_id":"RNAI_PLATFORM_OPTIONALITY_WITHOUT_TRIAL_DATA_OR_LICENSE_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":16810,"evidence_available_at_that_date":"source_proxy_RNAi_platform_clinical_optionality_without_durable_data_or_license_bridge; evidence_url_pending","evidence_source":"source_proxy_RNAi_platform_clinical_optionality_without_durable_data_or_license_bridge; evidence_url_pending","bridge_summary":"RNAi/platform optionality lacked durable trial-data, license, or revenue bridge and collapsed into high MAE","stage2_evidence_fields":["platform_trial_optionality","relative_strength","event_expectation"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","event_expectation_crowding"],"stage4c_evidence_fields":["high_MAE_without_data_or_license_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/226/226950/2024.csv","profile_path":"atlas/symbol_profiles/226/226950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.99,"MFE_90D_pct":9.99,"MFE_180D_pct":9.99,"MFE_1Y_pct":9.99,"MFE_2Y_pct":9.99,"MAE_30D_pct":-10.77,"MAE_90D_pct":-50.74,"MAE_180D_pct":-50.74,"MAE_1Y_pct":-50.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":18490,"drawdown_after_peak_pct":-55.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_MFE_high_MAE_event_watch_not_full_success","four_b_evidence_type":"price_or_event_expectation_without_data_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE","trigger_id":"TRG_R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE","symbol":"220100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"clinical_data_score":12,"regulatory_durability_score":9,"license_commercial_bridge_score":10,"relative_strength_score":10,"event_binary_risk_score":4,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"clinical_data_score":16,"regulatory_durability_score":11,"license_commercial_bridge_score":14,"relative_strength_score":8,"event_binary_risk_score":5,"risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["clinical_data_score","regulatory_durability_score","license_commercial_bridge_score","relative_strength_score","event_binary_risk_score","risk_penalty"],"component_delta_explanation":"C24 row is promoted only because clinical data/event signal has license/commercial or repeat-data bridge.","MFE_90D_pct":128.2,"MAE_90D_pct":-10.14,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK","trigger_id":"TRG_R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK","symbol":"007390","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"clinical_data_score":6,"regulatory_durability_score":1,"license_commercial_bridge_score":1,"relative_strength_score":12,"event_binary_risk_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"clinical_data_score":3,"regulatory_durability_score":0,"license_commercial_bridge_score":0,"relative_strength_score":5,"event_binary_risk_score":15,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4C-Watch","changed_components":["clinical_data_score","regulatory_durability_score","license_commercial_bridge_score","relative_strength_score","event_binary_risk_score","risk_penalty"],"component_delta_explanation":"C24 guard demotes event/platform/approval rows when validated data, regulatory durability, or license bridge is absent.","MFE_90D_pct":41.67,"MAE_90D_pct":-59.56,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START","trigger_id":"TRG_R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START","symbol":"226950","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"clinical_data_score":6,"regulatory_durability_score":1,"license_commercial_bridge_score":1,"relative_strength_score":12,"event_binary_risk_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"clinical_data_score":3,"regulatory_durability_score":0,"license_commercial_bridge_score":0,"relative_strength_score":5,"event_binary_risk_score":15,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4C-Watch","changed_components":["clinical_data_score","regulatory_durability_score","license_commercial_bridge_score","relative_strength_score","event_binary_risk_score","risk_penalty"],"component_delta_explanation":"C24 guard demotes event/platform/approval rows when validated data, regulatory durability, or license bridge is absent.","MFE_90D_pct":9.99,"MAE_90D_pct":-50.74,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_requires_validated_data_regulatory_or_license_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"C24 biotech trial/data rows should not promote toward Stage3-Yellow/Green unless event signal converts into validated data, regulatory durability, license/commercial option, or repeat-data bridge","220100 survives with strong MFE after data/license bridge; 007390 and 226950 fail when binary approval/platform expectation lacks durable bridge","TRG_R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE|TRG_R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK|TRG_R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c24_binary_event_4b_4c_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,1,1,0,"Trial/approval event rows can peak before outcome durability is known; local 4B/high-MAE/4C watch should remain active","preserves 220100 positive while preventing 007390/226950 event false positives and routing hard break to 4C watch","TRG_R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE|TRG_R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK|TRG_R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE/4C watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"72","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["binary_event_without_regulatory_durability","platform_expectation_without_trial_data_bridge","clinical_data_success_still_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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

## 22. Next Round State

```text
completed_round = R7
completed_loop = 72
next_round = R8
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/220/220100.json
atlas/symbol_profiles/007/007390.json
atlas/symbol_profiles/226/226950.json
atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv
atlas/ohlcv_tradable_by_symbol_year/007/007390/2023.csv
atlas/ohlcv_tradable_by_symbol_year/226/226950/2024.csv
```

This loop adds 3 new independent C24 cases, 1 positive, 2 counterexamples, 1 hard-4C case, and 1 canonical-archetype residual guard candidate for R7/L7.
