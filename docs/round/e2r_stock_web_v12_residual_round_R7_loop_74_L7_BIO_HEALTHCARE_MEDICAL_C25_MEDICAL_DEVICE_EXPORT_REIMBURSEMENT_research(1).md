# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R7
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R8
computed_next_loop: 74
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: C25_EXPORT_REIMBURSEMENT_ORDER_MARGIN_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
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

R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`. The previous R7 loop used C23 approval/commercialization, so this run shifts to C25. The selected C25 set avoids the top-covered medical AI/device cluster and focuses on the boundary between actual export/channel/margin bridge and medical-device theme heat.

| layer | id | definition |
|---|---|---|
| round | R7 | bio / healthcare / medical |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | biotech, pharma, healthcare, medical devices, aesthetics |
| canonical | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | device/export/reimbursement/channel and margin bridge |
| fine | C25_EXPORT_REIMBURSEMENT_ORDER_MARGIN_CASHFLOW_BRIDGE_GUARD | device signal must become order/reimbursement/margin evidence |
| deep | REGENERATIVE_AESTHETIC_EXPORT_CHANNEL_TO_MARGIN_OPERATING_LEVERAGE | aesthetic export/channel positive |
| deep | AESTHETIC_CONSUMABLE_EXPORT_REORDER_TO_MARGIN_AND_CASHFLOW | consumable reorder/margin positive |
| deep | SURGICAL_ROBOT_INSTALL_BASE_OPTIONALITY_WITHOUT_REPEAT_ORDER_REIMBURSEMENT_MARGIN_CONVERSION | surgical robot false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C25 top-covered symbols are `338220`, `214150`, `099190`, `145720`, `228670`, and `043150`. This run avoids that cluster and also avoids the previous R7/C23 symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C25 | 214450 | new independent | not top-covered C25 symbol; medical aesthetic export/channel margin bridge |
| C25 | 200670 | new independent | not top-covered C25 symbol; medical consumable export/reorder margin bridge |
| C25 | 060280 | new independent | not top-covered C25 symbol; surgical robot/device theme without order/reimbursement bridge |

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
214450 has no corporate-action candidate dates.
200670 has no corporate-action candidate dates.
060280 has old corporate-action/name-transition candidate dates ending 2011, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 214450 | 파마리서치 | Stage2-Actionable | 2024-04-01 | 108000 | medical aesthetic export/channel margin bridge worked |
| structural_success_with_late_4B_watch | 200670 | 휴메딕스 | Stage2-Actionable | 2024-04-01 | 29250 | medical consumable export/reorder margin bridge worked late |
| failed_rerating_high_MAE_device_theme | 060280 | 큐렉소 | Stage2-Actionable | 2024-01-29 | 15540 | surgical-robot/device theme lacked order/reimbursement/margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 214450 | 파마리서치 | Stage2-Actionable | 2024-04-01 | 108000 | 38.52 | 45.74 | 147.22 | -8.7 | -8.7 | -8.7 | 2024-12-16 | 267000 | -7.87 |
| 200670 | 휴메딕스 | Stage2-Actionable | 2024-04-01 | 29250 | 26.32 | 27.18 | 57.95 | -5.98 | -5.98 | -12.82 | 2024-12-23 | 46200 | -9.42 |
| 060280 | 큐렉소 | Stage2-Actionable | 2024-01-29 | 15540 | 7.46 | 7.46 | 7.46 | -12.55 | -38.48 | -56.18 | 2024-01-29 | 16700 | -59.22 |

## 9. Case-by-Case Notes

### 9.1 214450 / 파마리서치 — medical aesthetic export/channel bridge

The entry row is 2024-04-01 at 108,000. The forward path reached 149,600 in the early window, 157,400 in the 90D area, and 267,000 later. This is a valid C25 positive because the signal was not just healthcare/aesthetic theme strength. The bridge was export channel, margin, utilization, and operating leverage. Still, the correct output is Yellow plus 4B watch, not Green loosening.

### 9.2 200670 / 휴메딕스 — consumable export/reorder margin bridge

The entry row is 2024-04-01 at 29,250. The first move was slower than 214450, but the full window reached 46,200. This is a useful late-MFE C25 positive: reorder/export channel and margin/cashflow bridge eventually carried the path. The late profile argues for 4B watch and against early Green.

### 9.3 060280 / 큐렉소 — device theme without order/reimbursement bridge

The entry row is 2024-01-29 at 15,540. The best forward high was only 16,700, while the later low reached 6,810. This is the C25 false-positive branch: surgical robot or medical-device optionality can make a story, but without repeat order, reimbursement, install-base monetization, margin, or cashflow bridge, the device has no commercial pulse.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C25 treats medical-device/robot theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C25 needs export/reimbursement/order/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 060280 and other device-theme local peaks. |
| Full 4B non-price requirement appropriate? | Yes. 214450/200670 have non-price bridge evidence; 060280 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
214450:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after export-channel / margin / utilization bridge
  Stage3-Green = wait for post-MFE 4B review and margin durability

200670:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after reorder/export-channel and cashflow bridge
  Stage3-Green = reject unless late MFE and early MAE risk are cleared

060280:
  Stage2-Actionable = too generous if based only on surgical-robot/device theme
  Stage3-Yellow = reject without repeat order, reimbursement, install-base monetization, margin or cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 214450 | 0.88 | 1.00 | good full-window 4B watch after medical-aesthetic export/margin bridge |
| 200670 | 0.81 | 1.00 | late full-window 4B watch after export/reorder margin bridge |
| 060280 | 1.00 | 1.00 | device theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c25_requires_export_reimbursement_order_margin_cashflow_bridge

rule:
  For C25 medical-device/export/reimbursement rows, do not promote medical device,
  surgical robot, aesthetic consumable, healthcare equipment, or export-optionality
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  export-channel quality, reimbursement adoption, repeat order, installed-base monetization,
  utilization, margin conversion, FCF/cash conversion, or earnings revision tied to those factors.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 26.79 | -17.72 | 33.3% | useful but can over-credit device/robot theme |
| P0b e2r_2_0_baseline_reference | 3 | 26.79 | -17.72 | 0% | safer but may miss 214450/200670 |
| P1 sector_specific_candidate_profile | 3 | 26.79 | -17.72 | 33.3% | no broad L7 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 36.46 | -7.34 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 7.46 | -38.48 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 214450 | current_profile_correct | export/channel and margin bridge aligned with strong MFE |
| 200670 | current_profile_correct_with_lateness_guard | reorder/export margin bridge worked later, requiring 4B watch |
| 060280 | current_profile_false_positive | device theme produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25_EXPORT_REIMBURSEMENT_ORDER_MARGIN_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C25 non-top-covered medical-device/aesthetic residual reduced |

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
- device theme without order/reimbursement bridge
- medical aesthetic winner needs 4B watch
- late MFE after export-margin confirmation
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
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
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
shadow_weight,c25_requires_export_reimbursement_order_margin_cashflow_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"C25 medical-device/aesthetic rows should not promote toward Stage3-Yellow/Green unless medical device or aesthetic signal converts into export channel, reimbursement, repeat order, install-base monetization, utilization, margin, or cashflow bridge","214450 and 200670 survive after export/channel/margin bridge; 060280 fails when surgical-robot/device theme lacks repeat order, reimbursement and margin bridge","TRG_R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_device_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,1,1,0,"Medical device/aesthetic winners and robot/device false starts can peak before order and reimbursement durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 214450/200670 positives while preventing 060280 device-theme false positive","TRG_R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDICAL_AESTHETIC_EXPORT_CHANNEL_MARGIN_BRIDGE","deep_sub_archetype_id":"REGENERATIVE_AESTHETIC_EXPORT_CHANNEL_TO_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C25 medical device/aesthetic rows require export channel, reimbursement, repeat order, install-base monetization, utilization, margin, or cashflow bridge; device/aesthetic theme alone is insufficient."}
{"row_type":"case","case_id":"R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE","symbol":"200670","company_name":"휴메딕스","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDICAL_CONSUMABLE_EXPORT_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"AESTHETIC_CONSUMABLE_EXPORT_REORDER_TO_MARGIN_AND_CASHFLOW","case_type":"structural_success_with_late_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_late","current_profile_verdict":"current_profile_correct_with_lateness_guard","price_source":"Songdaiki/stock-web","notes":"C25 medical device/aesthetic rows require export channel, reimbursement, repeat order, install-base monetization, utilization, margin, or cashflow bridge; device/aesthetic theme alone is insufficient."}
{"row_type":"case","case_id":"R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE","symbol":"060280","company_name":"큐렉소","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SURGICAL_ROBOT_DEVICE_THEME_WITHOUT_ORDER_REIMBURSEMENT_BRIDGE","deep_sub_archetype_id":"SURGICAL_ROBOT_INSTALL_BASE_OPTIONALITY_WITHOUT_REPEAT_ORDER_REIMBURSEMENT_MARGIN_CONVERSION","case_type":"failed_rerating_high_MAE_device_theme","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C25 medical device/aesthetic rows require export channel, reimbursement, repeat order, install-base monetization, utilization, margin, or cashflow bridge; device/aesthetic theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE","case_id":"R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE","symbol":"214450","company_name":"파마리서치","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDICAL_AESTHETIC_EXPORT_CHANNEL_MARGIN_BRIDGE","deep_sub_archetype_id":"REGENERATIVE_AESTHETIC_EXPORT_CHANNEL_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":108000,"evidence_available_at_that_date":"source_proxy_medical_aesthetic_export_channel_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_medical_aesthetic_export_channel_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"medical-aesthetic export/channel expansion and margin/operating-leverage bridge converted the signal into durable rerating rather than device/beauty theme only","stage2_evidence_fields":["medical_aesthetic_export","channel_expansion","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["export_channel_to_revenue_visibility","margin_operating_leverage","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","medical_aesthetic_export_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv","profile_path":"atlas/symbol_profiles/214/214450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.52,"MFE_90D_pct":45.74,"MFE_180D_pct":147.22,"MFE_1Y_pct":147.22,"MFE_2Y_pct":147.22,"MAE_30D_pct":-8.7,"MAE_90D_pct":-8.7,"MAE_180D_pct":-8.7,"MAE_1Y_pct":-8.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-16","peak_price":267000,"drawdown_after_peak_pct":-7.87,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_medical_aesthetic_export_margin_bridge","four_b_evidence_type":"non_price_export_reimbursement_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE","case_id":"R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE","symbol":"200670","company_name":"휴메딕스","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_MEDICAL_CONSUMABLE_EXPORT_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"AESTHETIC_CONSUMABLE_EXPORT_REORDER_TO_MARGIN_AND_CASHFLOW","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":29250,"evidence_available_at_that_date":"source_proxy_medical_consumable_export_reorder_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_medical_consumable_export_reorder_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"medical consumable/aesthetic channel recovery converted into reorder, export-channel, margin and cashflow visibility with late MFE","stage2_evidence_fields":["medical_consumable_export","aesthetic_channel_reorder","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["reorder_to_revenue_visibility","margin_cashflow_bridge","export_channel_quality_proxy"],"stage4b_evidence_fields":["late_MFE_peak_watch","aesthetic_consumable_rerating_after_margin_confirmation"],"stage4c_evidence_fields":["early_MAE_watch_before_late_MFE"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/200/200670/2024.csv","profile_path":"atlas/symbol_profiles/200/200670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.32,"MFE_90D_pct":27.18,"MFE_180D_pct":57.95,"MFE_1Y_pct":57.95,"MFE_2Y_pct":57.95,"MAE_30D_pct":-5.98,"MAE_90D_pct":-5.98,"MAE_180D_pct":-12.82,"MAE_1Y_pct":-12.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-23","peak_price":46200,"drawdown_after_peak_pct":-9.42,"green_lateness_ratio":"0.56","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_full_window_4B_watch_after_export_reorder_margin_bridge","four_b_evidence_type":"non_price_export_reimbursement_margin_bridge","four_c_protection_label":"early_MAE_watch","trigger_outcome_label":"structural_success_late_MFE_then_4B_watch","current_profile_verdict":"current_profile_correct_with_lateness_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE","case_id":"R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE","symbol":"060280","company_name":"큐렉소","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SURGICAL_ROBOT_DEVICE_THEME_WITHOUT_ORDER_REIMBURSEMENT_BRIDGE","deep_sub_archetype_id":"SURGICAL_ROBOT_INSTALL_BASE_OPTIONALITY_WITHOUT_REPEAT_ORDER_REIMBURSEMENT_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":15540,"evidence_available_at_that_date":"source_proxy_surgical_robot_device_theme_without_repeat_order_reimbursement_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_surgical_robot_device_theme_without_repeat_order_reimbursement_margin_bridge; evidence_url_pending","bridge_summary":"surgical-robot/device optionality did not convert into visible repeat order, reimbursement, install-base monetization, margin, or cashflow bridge","stage2_evidence_fields":["surgical_robot_theme","medical_device_export_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["device_theme_local_peak","repeat_order_bridge_absent","reimbursement_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_reimbursement_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/060/060280/2024.csv","profile_path":"atlas/symbol_profiles/060/060280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.46,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MFE_1Y_pct":7.46,"MFE_2Y_pct":7.46,"MAE_30D_pct":-12.55,"MAE_90D_pct":-38.48,"MAE_180D_pct":-56.18,"MAE_1Y_pct":-56.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":16700,"drawdown_after_peak_pct":-59.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"device_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"device_theme_without_order_reimbursement_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE","trigger_id":"TRG_R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE","symbol":"214450","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"export_channel_score":12,"reimbursement_or_order_score":11,"margin_utilization_score":12,"cashflow_bridge_score":10,"relative_strength_score":10,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":15,"reimbursement_or_order_score":13,"margin_utilization_score":15,"cashflow_bridge_score":13,"relative_strength_score":8,"risk_penalty":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["export_channel_score","reimbursement_or_order_score","margin_utilization_score","cashflow_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C25 row is promoted only because device/aesthetic signal converts into export-channel, margin, utilization and cashflow bridge.","MFE_90D_pct":45.74,"MAE_90D_pct":-8.7,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE","trigger_id":"TRG_R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE","symbol":"200670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"export_channel_score":11,"reimbursement_or_order_score":10,"margin_utilization_score":11,"cashflow_bridge_score":9,"relative_strength_score":9,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":14,"reimbursement_or_order_score":12,"margin_utilization_score":13,"cashflow_bridge_score":11,"relative_strength_score":7,"risk_penalty":8},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["export_channel_score","reimbursement_or_order_score","margin_utilization_score","cashflow_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C25 bridge works, but late MFE and early MAE require 4B watch and prevent Green loosening.","MFE_90D_pct":27.18,"MAE_90D_pct":-5.98,"score_return_alignment_label":"score_return_aligned_late","current_profile_verdict":"current_profile_correct_with_lateness_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE","trigger_id":"TRG_R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE","symbol":"060280","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"export_channel_score":5,"reimbursement_or_order_score":1,"margin_utilization_score":1,"cashflow_bridge_score":0,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":2,"reimbursement_or_order_score":0,"margin_utilization_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":40,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["export_channel_score","reimbursement_or_order_score","margin_utilization_score","cashflow_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C25 guard demotes medical-device/robot theme rows when repeat order, reimbursement, install-base monetization, margin or cashflow bridge is absent.","MFE_90D_pct":7.46,"MAE_90D_pct":-38.48,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_requires_export_reimbursement_order_margin_cashflow_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"C25 medical-device/aesthetic rows should not promote toward Stage3-Yellow/Green unless medical device or aesthetic signal converts into export channel, reimbursement, repeat order, install-base monetization, utilization, margin, or cashflow bridge","214450 and 200670 survive after export/channel/margin bridge; 060280 fails when surgical-robot/device theme lacks repeat order, reimbursement and margin bridge","TRG_R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_device_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,1,1,0,"Medical device/aesthetic winners and robot/device false starts can peak before order and reimbursement durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 214450/200670 positives while preventing 060280 device-theme false positive","TRG_R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE|TRG_R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"74","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["device_theme_without_order_reimbursement_bridge","medical_aesthetic_winner_needs_4B_watch","late_MFE_after_export_margin_confirmation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/device-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C25 medical-device/export/reimbursement rows cannot promote without export-channel quality, reimbursement adoption, repeat order, installed-base monetization, utilization, margin conversion, FCF/cash conversion, or earnings-revision bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R7
completed_loop = 74
next_round = R8
next_loop = 74
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
atlas/symbol_profiles/214/214450.json
atlas/symbol_profiles/200/200670.json
atlas/symbol_profiles/060/060280.json
atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv
atlas/ohlcv_tradable_by_symbol_year/200/200670/2024.csv
atlas/ohlcv_tradable_by_symbol_year/060/060280/2024.csv
```

This loop continues loop 74 with R7 and adds 3 new independent C25 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R7/L7.
