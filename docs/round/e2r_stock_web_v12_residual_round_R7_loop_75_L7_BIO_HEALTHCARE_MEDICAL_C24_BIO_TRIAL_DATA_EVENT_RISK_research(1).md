# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R7
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R8
computed_next_loop: 75
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: C24_ENDPOINT_PARTNER_PIPELINE_REGULATORY_BRIDGE_GUARD
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

R7 maps directly to `L7_BIO_HEALTHCARE_MEDICAL`. The previous R7 loop used C25 medical-device/export/reimbursement, so this run rotates to C24 trial-data/event-risk. The branch is deliberately event-risk heavy: one platform/data positive-control row is paired with two clinical-event false positives where MFE did not convert into endpoint, regulatory, partner or cash-runway evidence.

| layer | id | definition |
|---|---|---|
| round | R7 | bio / healthcare / medical |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | biotech, pharma, healthcare, medical devices, clinical data |
| canonical | C24_BIO_TRIAL_DATA_EVENT_RISK | trial data, clinical event, binary-event risk |
| fine | C24_ENDPOINT_PARTNER_PIPELINE_REGULATORY_BRIDGE_GUARD | event signal must become endpoint/partner/pipeline/regulatory bridge |
| deep | ADC_PLATFORM_DATA_AND_PARTNERING_OPTIONALITY_TO_PIPELINE_VALUE_WITH_EVENT_DECAY_GUARD | ADC platform/data positive |
| deep | NT_I7_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_WITHOUT_ENDPOINT_REGULATORY_OR_PARTNERING_CONVERSION | immuno-oncology false positive |
| deep | VACCINE_OR_CELL_THERAPY_EVENT_SPIKE_WITHOUT_ENDPOINT_REGULATORY_PARTNERING_CASH_RUNWAY_CONVERSION | vaccine/cell-therapy event false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C24 top-covered symbols are `000100`, `215600`, `009420`, `298380`, `028300`, and `039200`. This run avoids that cluster and also avoids the previous R7/C25 representatives `214450`, `200670`, and `060280`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C24 | 141080 | new independent | not top-covered C24 symbol; ADC platform/data and partner validation bridge, entry after 2024-04-23 corporate-action candidate |
| C24 | 950220 | new independent | not top-covered C24 symbol; immuno-oncology trial optionality without endpoint/regulatory bridge |
| C24 | 299660 | new independent | not top-covered C24 symbol; vaccine/cell-therapy trial event spike without durable data/regulatory bridge, entry after 2024-08-23 corporate-action candidate |

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

Corporate-action caveat:

```text
141080 has a 2024-04-23 corporate-action candidate, so the selected 2024-06-20 entry is after the blocked date.
950220 has a 2025-09-30 corporate-action candidate, outside the selected 2024 representative window.
299660 has a 2024-08-23 corporate-action candidate, so the selected 2024-08-26 entry is after the blocked date; the next candidate is 2025-07-07, outside the representative 180D window used here.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| platform_data_success_then_4B_watch | 141080 | 리가켐바이오 | Stage2-Actionable | 2024-06-20 | 75500 | ADC platform/data and partner validation bridge worked, but 4B event-decay guard required |
| trial_optionality_low_MFE_high_MAE_counterexample | 950220 | 네오이뮨텍 | Stage2-Actionable | 2024-01-29 | 1696 | immuno-oncology trial optionality lacked endpoint/regulatory/partnering bridge |
| trial_event_spike_then_high_MAE_counterexample | 299660 | 셀리드 | Stage2-Actionable | 2024-08-26 | 7720 | vaccine/cell-therapy event spike lacked durable data/regulatory/cash-runway bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 141080 | 리가켐바이오 | Stage2-Actionable | 2024-06-20 | 75500 | 24.37 | 84.9 | 90.2 | -11.39 | -11.39 | -11.39 | 2024-11-11 | 143600 | -36.42 |
| 950220 | 네오이뮨텍 | Stage2-Actionable | 2024-01-29 | 1696 | 6.49 | 16.57 | 16.57 | -9.2 | -15.98 | -29.25 | 2024-03-25 | 1977 | -39.3 |
| 299660 | 셀리드 | Stage2-Actionable | 2024-08-26 | 7720 | 18.13 | 18.13 | 18.13 | -38.28 | -52.07 | -60.69 | 2024-08-26 | 9120 | -66.72 |

## 9. Case-by-Case Notes

### 9.1 141080 / 리가켐바이오 — ADC platform/data bridge

The entry row is 2024-06-20 at 75,500. The 30D path reached 93,900, the 90D path reached 139,600, and the wider window reached 143,600. This is a valid C24 positive, but only as guarded Yellow. The evidence family is platform/data and partner validation, not just biotech theme heat. The later post-peak low keeps 4B/event-decay watch active and blocks Green.

### 9.2 950220 / 네오이뮨텍 — immuno-oncology optionality without endpoint bridge

The entry row is 2024-01-29 at 1,696. The path reached 1,977, then fell to 1,200. The model should not promote this as durable Stage3 because endpoint data, regulatory conversion, partner validation and cash-runway bridge were not strong enough. The row is trial-event MFE turning into high-MAE protection evidence.

### 9.3 299660 / 셀리드 — trial event spike without durable data bridge

The entry row is 2024-08-26 at 7,720, after the 2024-08-23 corporate-action candidate. The local high was 9,120, but the later path fell to 3,035. This is the sharpest C24 counterexample in this set. A trial or vaccine/cell-therapy event spike can ignite price quickly, but without endpoint/regulatory/partnering/cash-runway conversion, it becomes 4B/4C watch, not Stage3 evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C24 treats biotech event/clinical optionality as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C24 needs endpoint/partner/pipeline/regulatory bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 299660 event spike and 950220 low-quality MFE. |
| Full 4B non-price requirement appropriate? | Yes. 141080 has non-price bridge evidence; 950220/299660 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
141080:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after ADC platform/data and partner validation bridge
  Stage3-Green = reject because event-decay and clinical-readout risk remain active

950220:
  Stage2-Actionable = acceptable only as trial/event watch
  Stage3-Yellow = reject without endpoint data, regulatory conversion, partner validation or cash runway
  Stage3-Green = reject despite MFE

299660:
  Stage2-Actionable = too generous if based only on vaccine/cell-therapy trial-event spike
  Stage3-Yellow = reject without durable endpoint, regulatory, partnering and cash-runway bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 141080 | 0.78 | 1.00 | ADC platform/data positive but full-window 4B event-decay watch |
| 950220 | 1.00 | 1.00 | trial optionality local 4B watch, not positive stage |
| 299660 | 1.00 | 1.00 | trial event spike local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c24_requires_endpoint_partner_pipeline_regulatory_bridge

rule:
  For C24 trial/data event-risk rows, do not promote biotech, trial,
  vaccine, immuno-oncology, cell-therapy, platform-data, or clinical-event Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  endpoint data quality, regulatory conversion, partner validation, pipeline-value bridge,
  cash-runway sufficiency, commercialization path, or earnings/cashflow bridge tied to the asset.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 39.87 | -26.48 | 66.7% | too generous to biotech event optionality |
| P0b e2r_2_0_baseline_reference | 3 | 39.87 | -26.48 | 33.3% | safer but may miss 141080 |
| P1 sector_specific_candidate_profile | 3 | 39.87 | -26.48 | 66.7% | no broad L7 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 84.9 | -11.39 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 17.35 | -34.02 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 141080 | current_profile_correct_but_no_green | data/partner/pipeline bridge aligned with MFE, but event-decay watch blocks Green |
| 950220 | current_profile_false_positive | immuno-oncology optionality produced MFE then high MAE |
| 299660 | current_profile_false_positive | vaccine/cell-therapy event spike produced severe high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | C24_ENDPOINT_PARTNER_PIPELINE_REGULATORY_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R7/C24 non-top-covered clinical event-risk residual reduced |

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
residual_error_types_found:
- trial event optionality without endpoint bridge
- ADC platform winner needs 4B watch
- vaccine trial event spike severe high-MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
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
- R7 direct L7 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact clinical trial or licensing announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_requires_endpoint_partner_pipeline_regulatory_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"C24 trial/data event-risk rows should not promote toward Stage3-Yellow/Green unless biotech event signal converts into endpoint data, partner validation, pipeline-value bridge, regulatory path, cash runway, or commercialization bridge","141080 survives only as guarded positive after ADC platform/data/partnering bridge; 950220 and 299660 are demoted because trial-event optionality lacked endpoint/regulatory/partnering bridge and printed high MAE","TRG_R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE|TRG_R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE|TRG_R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c24_bio_event_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,1,1,0,"Biotech platform winners and trial-event false starts can peak before endpoint/regulatory/partnering durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 141080 guarded positive while preventing 950220/299660 trial-event false positives","TRG_R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE|TRG_R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE|TRG_R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE","symbol":"141080","company_name":"리가켐바이오","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_ADC_PLATFORM_DATA_LICENSING_OPTION_VALUE_BRIDGE","deep_sub_archetype_id":"ADC_PLATFORM_DATA_AND_PARTNERING_OPTIONALITY_TO_PIPELINE_VALUE_WITH_EVENT_DECAY_GUARD","case_type":"platform_data_success_then_4B_event_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C24 trial/data/event-risk rows require endpoint data, regulatory conversion, partner validation, pipeline-value bridge, cash runway, or commercialization path; biotech event/theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE","symbol":"950220","company_name":"네오이뮨텍","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_WITHOUT_ENDPOINT_DATA_BRIDGE","deep_sub_archetype_id":"NT_I7_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_WITHOUT_ENDPOINT_REGULATORY_OR_PARTNERING_CONVERSION","case_type":"trial_optionality_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C24 trial/data/event-risk rows require endpoint data, regulatory conversion, partner validation, pipeline-value bridge, cash runway, or commercialization path; biotech event/theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE","symbol":"299660","company_name":"셀리드","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_VACCINE_TRIAL_EVENT_SPIKE_WITHOUT_DURABLE_DATA_REGULATORY_BRIDGE","deep_sub_archetype_id":"VACCINE_OR_CELL_THERAPY_EVENT_SPIKE_WITHOUT_ENDPOINT_REGULATORY_PARTNERING_CASH_RUNWAY_CONVERSION","case_type":"trial_event_spike_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C24 trial/data/event-risk rows require endpoint data, regulatory conversion, partner validation, pipeline-value bridge, cash runway, or commercialization path; biotech event/theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE","case_id":"R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE","symbol":"141080","company_name":"리가켐바이오","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_ADC_PLATFORM_DATA_LICENSING_OPTION_VALUE_BRIDGE","deep_sub_archetype_id":"ADC_PLATFORM_DATA_AND_PARTNERING_OPTIONALITY_TO_PIPELINE_VALUE_WITH_EVENT_DECAY_GUARD","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":75500,"evidence_available_at_that_date":"source_proxy_ADC_platform_partnering_clinical_data_pipeline_value_bridge_after_2024_04_23_corporate_action; evidence_url_pending","evidence_source":"source_proxy_ADC_platform_partnering_clinical_data_pipeline_value_bridge_after_2024_04_23_corporate_action; evidence_url_pending","bridge_summary":"ADC platform, partner validation and pipeline/data optionality converted into pipeline value and licensing bridge, but post-event valuation decay and clinical readout risk require 4B watch","stage2_evidence_fields":["ADC_platform_data","partner_validation_proxy","pipeline_option_value","relative_strength"],"stage3_evidence_fields":["data_to_pipeline_value_visibility","licensing_partnering_bridge","pipeline_risk_adjusted_value_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","clinical_readout_decay_risk","biotech_platform_crowding"],"stage4c_evidence_fields":["post_peak_decay_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv|atlas/ohlcv_tradable_by_symbol_year/141/141080/2025.csv","profile_path":"atlas/symbol_profiles/141/141080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.37,"MFE_90D_pct":84.9,"MFE_180D_pct":90.2,"MFE_1Y_pct":90.2,"MFE_2Y_pct":90.2,"MAE_30D_pct":-11.39,"MAE_90D_pct":-11.39,"MAE_180D_pct":-11.39,"MAE_1Y_pct":-11.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":143600,"drawdown_after_peak_pct":-36.42,"green_lateness_ratio":"0.42","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"ADC_platform_data_positive_but_full_window_4B_event_decay_watch","four_b_evidence_type":"non_price_data_partnering_pipeline_value_bridge","four_c_protection_label":"post_peak_decay_watch","trigger_outcome_label":"platform_data_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE","case_id":"R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE","symbol":"950220","company_name":"네오이뮨텍","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_WITHOUT_ENDPOINT_DATA_BRIDGE","deep_sub_archetype_id":"NT_I7_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_WITHOUT_ENDPOINT_REGULATORY_OR_PARTNERING_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1696,"evidence_available_at_that_date":"source_proxy_immuno_oncology_trial_optionality_without_endpoint_regulatory_partnering_bridge; evidence_url_pending","evidence_source":"source_proxy_immuno_oncology_trial_optionality_without_endpoint_regulatory_partnering_bridge; evidence_url_pending","bridge_summary":"immuno-oncology trial optionality produced a short MFE window, but endpoint data, regulatory path, partner validation and cash runway bridge did not become durable","stage2_evidence_fields":["immuno_oncology_trial_theme","clinical_data_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["trial_theme_peak","endpoint_data_bridge_absent","cash_runway_partnering_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_endpoint_or_regulatory_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv","profile_path":"atlas/symbol_profiles/950/950220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.49,"MFE_90D_pct":16.57,"MFE_180D_pct":16.57,"MFE_1Y_pct":16.57,"MFE_2Y_pct":16.57,"MAE_30D_pct":-9.2,"MAE_90D_pct":-15.98,"MAE_180D_pct":-29.25,"MAE_1Y_pct":-29.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":1977,"drawdown_after_peak_pct":-39.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"trial_optionality_local_4B_watch_not_positive_stage","four_b_evidence_type":"trial_event_theme_without_endpoint_regulatory_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"trial_optionality_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE","case_id":"R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE","symbol":"299660","company_name":"셀리드","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_VACCINE_TRIAL_EVENT_SPIKE_WITHOUT_DURABLE_DATA_REGULATORY_BRIDGE","deep_sub_archetype_id":"VACCINE_OR_CELL_THERAPY_EVENT_SPIKE_WITHOUT_ENDPOINT_REGULATORY_PARTNERING_CASH_RUNWAY_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-26","entry_date":"2024-08-26","entry_price":7720,"evidence_available_at_that_date":"source_proxy_vaccine_trial_event_spike_without_endpoint_regulatory_partnering_cash_runway_bridge_after_2024_08_23_corporate_action; evidence_url_pending","evidence_source":"source_proxy_vaccine_trial_event_spike_without_endpoint_regulatory_partnering_cash_runway_bridge_after_2024_08_23_corporate_action; evidence_url_pending","bridge_summary":"vaccine/cell-therapy trial event spike lacked durable endpoint data, regulatory conversion, partnering validation and cash-runway bridge, so the local MFE became high-MAE event-risk evidence","stage2_evidence_fields":["vaccine_trial_event_spike","clinical_event_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_local_peak","endpoint_regulatory_bridge_absent","cash_runway_bridge_absent"],"stage4c_evidence_fields":["severe_high_MAE_without_trial_data_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299660/2024.csv|atlas/ohlcv_tradable_by_symbol_year/299/299660/2025.csv","profile_path":"atlas/symbol_profiles/299/299660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.13,"MFE_90D_pct":18.13,"MFE_180D_pct":18.13,"MFE_1Y_pct":18.13,"MFE_2Y_pct":18.13,"MAE_30D_pct":-38.28,"MAE_90D_pct":-52.07,"MAE_180D_pct":-60.69,"MAE_1Y_pct":-60.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":9120,"drawdown_after_peak_pct":-66.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"trial_event_spike_local_4B_watch_not_positive_stage","four_b_evidence_type":"trial_event_theme_without_endpoint_regulatory_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"trial_event_spike_then_severe_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE","trigger_id":"TRG_R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE","symbol":"141080","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"endpoint_data_score":12,"partner_validation_score":13,"pipeline_value_score":12,"regulatory_commercial_score":7,"relative_strength_score":12,"event_risk_penalty":7},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"endpoint_data_score":14,"partner_validation_score":16,"pipeline_value_score":15,"regulatory_commercial_score":8,"relative_strength_score":9,"event_risk_penalty":11},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["endpoint_data_score","partner_validation_score","pipeline_value_score","regulatory_commercial_score","relative_strength_score","event_risk_penalty"],"component_delta_explanation":"C24 row is promoted only because platform/data evidence converts into partner validation and pipeline-value bridge; post-event decay/clinical risk blocks Green.","MFE_90D_pct":84.9,"MAE_90D_pct":-11.39,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE","trigger_id":"TRG_R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE","symbol":"950220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"endpoint_data_score":2,"partner_validation_score":1,"pipeline_value_score":3,"regulatory_commercial_score":0,"relative_strength_score":10,"event_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"endpoint_data_score":0,"partner_validation_score":0,"pipeline_value_score":1,"regulatory_commercial_score":0,"relative_strength_score":4,"event_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["endpoint_data_score","partner_validation_score","pipeline_value_score","regulatory_commercial_score","relative_strength_score","event_risk_penalty"],"component_delta_explanation":"C24 guard demotes trial/event theme rows when endpoint data, regulatory conversion, partner validation, cash runway and commercialization bridge are absent.","MFE_90D_pct":16.57,"MAE_90D_pct":-15.98,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE","trigger_id":"TRG_R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE","symbol":"299660","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"endpoint_data_score":2,"partner_validation_score":1,"pipeline_value_score":3,"regulatory_commercial_score":0,"relative_strength_score":10,"event_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"endpoint_data_score":0,"partner_validation_score":0,"pipeline_value_score":1,"regulatory_commercial_score":0,"relative_strength_score":4,"event_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["endpoint_data_score","partner_validation_score","pipeline_value_score","regulatory_commercial_score","relative_strength_score","event_risk_penalty"],"component_delta_explanation":"C24 guard demotes trial/event theme rows when endpoint data, regulatory conversion, partner validation, cash runway and commercialization bridge are absent.","MFE_90D_pct":18.13,"MAE_90D_pct":-52.07,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_requires_endpoint_partner_pipeline_regulatory_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"C24 trial/data event-risk rows should not promote toward Stage3-Yellow/Green unless biotech event signal converts into endpoint data, partner validation, pipeline-value bridge, regulatory path, cash runway, or commercialization bridge","141080 survives only as guarded positive after ADC platform/data/partnering bridge; 950220 and 299660 are demoted because trial-event optionality lacked endpoint/regulatory/partnering bridge and printed high MAE","TRG_R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE|TRG_R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE|TRG_R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c24_bio_event_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,1,1,0,"Biotech platform winners and trial-event false starts can peak before endpoint/regulatory/partnering durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 141080 guarded positive while preventing 950220/299660 trial-event false positives","TRG_R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE|TRG_R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE|TRG_R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["trial_event_optionality_without_endpoint_bridge","ADC_platform_winner_needs_4B_watch","vaccine_trial_event_spike_severe_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R7-specific handling

- R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`.
- This MD uses `C24_BIO_TRIAL_DATA_EVENT_RISK`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/biotech-event-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R7 direct L7 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C24 trial/data/event-risk rows cannot promote without endpoint data quality, regulatory conversion, partner validation, pipeline-value bridge, cash-runway sufficiency, commercialization path, or asset-linked earnings/cashflow bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R7
completed_loop = 75
next_round = R8
next_loop = 75
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
atlas/symbol_profiles/141/141080.json
atlas/symbol_profiles/950/950220.json
atlas/symbol_profiles/299/299660.json
atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv
atlas/ohlcv_tradable_by_symbol_year/141/141080/2025.csv
atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv
atlas/ohlcv_tradable_by_symbol_year/299/299660/2024.csv
atlas/ohlcv_tradable_by_symbol_year/299/299660/2025.csv
```

This loop continues loop 75 with R7 and adds 3 new independent C24 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R7/L7.
