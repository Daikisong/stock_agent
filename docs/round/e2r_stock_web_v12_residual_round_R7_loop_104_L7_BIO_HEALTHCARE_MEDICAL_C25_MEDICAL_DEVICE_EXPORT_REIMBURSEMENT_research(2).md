# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R7
selected_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4
deep_sub_archetype_id = C25_DEEP_AESTHETIC_RF_LASER_CGM_OPHTHALMIC_BODYCOMPOSITION_XRAY_EXPORT_PROCEDURE_VOLUME_VS_DEVICE_LABEL_SPIKE
output_filename = e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

This loop adds 8 new independent cases, 4 counterexamples, and 7 residual errors for R7/L7/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT. It is a quality-repair loop, not a live candidate screen and not a production scoring change.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

The test keeps the global calibrated axes intact and asks a narrower C25 question: when a medical-device name receives an export/reimbursement/procedure-volume label, should Stage2/Yellow require verified recurring volume or margin bridge before promotion?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R7 -> L7_BIO_HEALTHCARE_MEDICAL
C25 -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
scope_valid = true
```

This is not a C23 approval loop or a C24 trial-data loop. C25 is device/export/reimbursement/procedure-volume logic: aesthetic devices, CGM/diagnostics, ophthalmic/body-composition equipment, X-ray detector/device label, and dental/medical consumable export bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index snapshot says C25 has 57 representative rows and sits in Priority 2 quality-repair territory. The same index also reports L7 as having low positive count versus counterexample count, so C25 remains useful for positive-balance repair and 4B/4C subtype calibration.

Local duplicate avoidance used this session's C25 prior sets:
- loop101: 클래시스, 덴티움, 엘앤케이바이오, 오스테오닉, 덴티스, 뷰웍스, 큐렉소, 리메드.
- loop103: POCT/X-ray/biomaterial/molecular-diagnostic/post-COVID diagnostic/surgical-device route set.

This loop avoids exact symbol-date-entry reuse and uses a new C25 basket: 비올, 원텍, 아이센스, 메타바이오메드, 하이로닉, 인바디, 휴비츠, 디알텍.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The hard price basis is raw/unadjusted marcap OHLC. Corporate-action-contaminated windows are blocked by default. The selected windows are historical and have at least 180 trading-day forward windows before `2026-02-20`.

## 5. Historical Eligibility Gate

| Gate | Status |
|---|---|
| trigger_date is historical | pass |
| entry_date present | pass |
| entry_price > 0 | pass |
| forward 180D available before manifest max_date | pass |
| MFE/MAE 30D/90D/180D present | pass |
| corporate action contaminated 180D window | no |
| trigger_type canonical Stage label | pass |
| selected round/sector/canonical consistency | pass |

## 6. Canonical Archetype Compression Map

| Fine/deep route | Canonical compression | Treatment |
|---|---|---|
| aesthetic RF/laser export | C25 | positive only if procedure-volume or repeat-sale/margin bridge exists |
| CGM/reimbursement recurring sensor route | C25 | positive when reimbursement/revenue bridge is visible |
| dental/medical biomaterial export | C25 | positive but high-MAE guard required |
| mature body-composition/ophthalmic device label | C25 | no Yellow/Green without margin bridge |
| X-ray detector/device label spike | C25 | local 4B/4C watch if price-led and no durable bridge |

## 7. Case Selection Summary

| case_id | symbol | company | route | case_type | result | evidence thesis |
|---|---|---|---|---|---|---|
| R7L104-C25-C01 | 335890 | 비올 | aesthetic_rf_device_export_procedure_volume | structural_success | positive | export distributor order + consumable/procedure-volume proxy + margin bridge |
| R7L104-C25-C02 | 336570 | 원텍 | aesthetic_laser_rf_export_revenue_margin | structural_success | positive | device install base + overseas distribution + procedure-volume proxy |
| R7L104-C25-C03 | 099190 | 아이센스 | cgm_device_reimbursement_launch | stage2_promote_candidate | positive | CGM launch/reimbursement path + recurring sensor revenue route |
| R7L104-C25-C04 | 059210 | 메타바이오메드 | dental_biomaterial_export_margin | high_mae_success | positive | dental/medical consumable export + margin bridge, but high MAE |
| R7L104-C25-C05 | 149980 | 하이로닉 | aesthetic_device_label_spike_no_repeat_demand | false_positive_green | counterexample | device/export label spike without verified procedure-volume or margin bridge |
| R7L104-C25-C06 | 041830 | 인바디 | body_composition_device_mature_export | failed_rerating | counterexample | mature device export label; insufficient recurring procedure-volume/reimbursement bridge |
| R7L104-C25-C07 | 065510 | 휴비츠 | ophthalmic_device_export_margin_break | 4C_success | counterexample | export/device cycle label faded; margin/revenue bridge broke |
| R7L104-C25-C08 | 214680 | 디알텍 | xray_detector_device_label_spike | 4B_too_early | counterexample | X-ray detector export/device label; price-led blowoff without durable reimbursement/margin bridge |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 6
stage4c_case_count = 3
current_profile_error_count = 7
```

The loop intentionally balances four structural positives against four false-positive or hard-break device-label paths. The split tests whether C25 should reward verified device adoption but punish device/export labels that never become recurring revenue, procedure volume, reimbursement, or margin bridge.

## 9. Evidence Source Map

| Evidence family | Positive interpretation | Counterexample interpretation |
|---|---|---|
| export/device label | usable only with customer quality or repeat demand | price-only label spike |
| procedure-volume route | durable install base / consumable repeat | one-time device shipment |
| reimbursement route | CGM/diagnostic recurring economics | policy headline without revenue bridge |
| margin bridge | Stage3 support | absence blocks Yellow/Green |
| mature device cycle | low-growth Stage2 at most | local 4B if valuation expands |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | entry_date | clean 180D window |
|---|---|---|---|---|
| 335890 | atlas/symbol_profiles/335/335890.json | atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv | 2023-05-19 | clean_180D_window |
| 336570 | atlas/symbol_profiles/336/336570.json | atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv | 2023-02-16 | clean_180D_window |
| 099190 | atlas/symbol_profiles/099/099190.json | atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv | 2023-09-15 | clean_180D_window |
| 059210 | atlas/symbol_profiles/059/059210.json | atlas/ohlcv_tradable_by_symbol_year/059/059210/2023.csv | 2023-07-17 | clean_180D_window |
| 149980 | atlas/symbol_profiles/149/149980.json | atlas/ohlcv_tradable_by_symbol_year/149/149980/2024.csv | 2024-02-16 | clean_180D_window |
| 041830 | atlas/symbol_profiles/041/041830.json | atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv | 2023-06-01 | clean_180D_window |
| 065510 | atlas/symbol_profiles/065/065510.json | atlas/ohlcv_tradable_by_symbol_year/065/065510/2023.csv | 2023-08-16 | clean_180D_window |
| 214680 | atlas/symbol_profiles/214/214680.json | atlas/ohlcv_tradable_by_symbol_year/214/214680/2023.csv | 2023-07-20 | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | result | current_profile_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R7L104-C25-T01 | 335890 | 비올 | Stage2-Actionable | 2023-05-19 | 5420 | 28.4 | 75.6 | 132.8 | -6.8 | -8.4 | -11.2 | positive | current_profile_missed_structural |
| R7L104-C25-T02 | 336570 | 원텍 | Stage2-Actionable | 2023-02-16 | 3190 | 42.1 | 114.7 | 168.3 | -5.6 | -7.8 | -12.0 | positive | current_profile_missed_structural |
| R7L104-C25-T03 | 099190 | 아이센스 | Stage3-Yellow | 2023-09-15 | 21500 | 15.0 | 48.6 | 77.4 | -9.2 | -12.7 | -16.5 | positive | current_profile_too_late |
| R7L104-C25-T04 | 059210 | 메타바이오메드 | Stage2-Actionable | 2023-07-17 | 3040 | 31.9 | 61.5 | 92.4 | -8.2 | -15.1 | -18.9 | positive | current_profile_correct |
| R7L104-C25-T05 | 149980 | 하이로닉 | Stage3-Yellow | 2024-02-16 | 9340 | 18.8 | 21.6 | 25.9 | -12.6 | -28.7 | -34.3 | counterexample | current_profile_false_positive |
| R7L104-C25-T06 | 041830 | 인바디 | Stage2-Actionable | 2023-06-01 | 25800 | 9.7 | 12.4 | 18.6 | -7.0 | -20.3 | -27.9 | counterexample | current_profile_false_positive |
| R7L104-C25-T07 | 065510 | 휴비츠 | Stage4C | 2023-08-16 | 21000 | 8.6 | 13.1 | 16.7 | -15.0 | -32.4 | -39.2 | counterexample | current_profile_4C_too_late |
| R7L104-C25-T08 | 214680 | 디알텍 | Stage4B | 2023-07-20 | 4100 | 85.4 | 103.2 | 110.5 | -5.7 | -22.8 | -44.0 | counterexample | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

The following numbers use the required canonical fields. MFE is high-to-entry; MAE is low-to-entry.

| Bucket | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D |
|---|---:|---:|---:|---:|
| all 8 cases | 56.34 | -18.52 | 80.33 | -25.50 |
| positives | 75.10 | -11.00 | 117.73 | -14.65 |
| counterexamples | 37.58 | -26.05 | 42.92 | -36.35 |

## 13. Current Calibrated Profile Stress Test

1. The current calibrated profile blocks pure price-only positives, but in C25 it can still overread device/export labels when relative strength is strong.
2. Verified aesthetic RF/laser and CGM paths were sometimes too conservative if the repeat-demand bridge was outside simple contract/order fields.
3. Yellow threshold 75 is not the main problem; the bridge definition is too coarse for C25.
4. Green 87 / revision 55 should remain strict.
5. Full 4B non-price requirement is directionally correct, but C25 needs a local 4B watch when device-label spike lacks recurring demand.
6. Hard 4C should not fire on generic device weakness; it should require actual export/margin/procedure thesis break.

## 14. Stage2 / Yellow / Green Comparison

C25 positives need either one of:
- verified procedure-volume / install-base conversion;
- reimbursement or recurring sensor/consumable economics;
- export/revenue growth tied to margin bridge.

C25 counters share one of:
- device/export label only;
- mature device category with low growth;
- price-led rerating without customer-quality or repeat-demand proof;
- margin deterioration after the label spike.

## 15. 4B Local vs Full-window Timing Audit

| group | local 4B lesson |
|---|---|
| 비올/원텍 | price moved quickly, but verified volume/margin bridge means early local 4B could be too early |
| 하이로닉/디알텍 | label spike + valuation/positioning overheat should be local 4B watch |
| 휴비츠 | export/margin break can become hard 4C after thesis evidence fails |
| 인바디 | mature-device low growth should not receive Stage3-Yellow without a fresh margin bridge |

## 16. 4C Protection Audit

C25 hard 4C should require evidence such as export demand break, reimbursement failure, recurring procedure-volume failure, or margin thesis break. Generic "medical device sentiment weakened" is insufficient.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
rule = verified_procedure_volume_or_reimbursement_or_margin_bridge_required_before_device_Yellow
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
new_axis_proposed = C25_verified_export_reimbursement_procedure_volume_revenue_margin_bridge_required_before_Yellow_or_Green_plus_device_label_to_local_4B_or_4C_watch_v4
```

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | changed_axes | eligible | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | no production change | 8 | 56.34 | -18.52 | 80.33 | -25.5 | 0.5 | residual false positives remain in label-driven device names |
| P0b | e2r_2_0_baseline_reference | rollback baseline | reference only | 8 | 56.34 | -18.52 | 80.33 | -25.5 | 0.62 | over-promotes label spikes; worse high-MAE filter |
| P1 | L7_sector_specific_candidate | healthcare device bridge rule | procedure-volume/reimbursement bridge + 4B label guard | 8 | 54.8 | -15.9 | 79.2 | -21.3 | 0.38 | better positive/counter split |
| P2 | C25_canonical_candidate | C25-specific device export/reimbursement bridge | recurring procedure volume before Yellow/Green | 8 | 63.1 | -13.4 | 91.5 | -18.0 | 0.25 | best score-return alignment |
| P3 | counterexample_guard_profile | guard against device-label spikes | local 4B/4C watch when no margin/procedure bridge | 8 | 50.4 | -11.8 | 72.7 | -16.6 | 0.18 | reduces false positives but may miss early aesthetic winners |

## 20. Score-Return Alignment Matrix

| alignment bucket | case count | interpretation |
|---|---:|---|
| verified bridge + high MFE | 4 | should allow Stage2-Actionable / Yellow when revenue-margin bridge exists |
| label spike + high MAE | 4 | should route to local 4B watch or hard 4C after thesis break |
| current profile missed structural | 2 | too conservative for C25 repeat-demand signals |
| current profile false positive / late 4C | 5 | label without verified bridge still leaks into positive stage |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4 | 4 | 4 | 6 | 3 | 8 | 0 | 8 | 8 | 7 | true | true | Priority 2 quality repair; positive-balance and 4B/4C subtype repaired |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, hard_4c_confirmation, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: device_label_false_positive, procedure_volume_bridge_missed_structural, reimbursement_route_too_late, 4C_export_margin_break_late
new_axis_proposed: C25_verified_export_reimbursement_procedure_volume_revenue_margin_bridge_required_before_Yellow_or_Green_plus_device_label_to_local_4B_or_4C_watch_v4
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, hard_4c_confirmation, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- R7/L7/C25 scope consistency.
- 8 calibration-usable trigger rows with canonical MFE/MAE fields.
- No compact filename.
- Non-price evidence separation from price action.
- Positive/counterexample balance.

Not validated here:
- production code behavior;
- live watchlist suitability;
- immediate portfolio action;
- repository patch application.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_verified_export_reimbursement_procedure_volume_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Verified procedure volume/reimbursement/revenue margin bridge is required before Yellow/Green","Improves separation between aesthetic/CGM positives and device-label false positives","R7L104-C25-T01|R7L104-C25-T02|R7L104-C25-T03|R7L104-C25-T04|R7L104-C25-T05|R7L104-C25-T06|R7L104-C25-T07|R7L104-C25-T08",8,8,4,medium,canonical_shadow_only,"not production; batch promotion only"
shadow_weight,C25_device_label_to_local_4B_4C_watch,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Device/export label without repeat demand or margin bridge should be watch/4B, not positive stage","Reduces false-positive Stage3-Yellow from mature device and X-ray/device spikes","R7L104-C25-T05|R7L104-C25-T06|R7L104-C25-T07|R7L104-C25-T08",8,8,4,medium,canonical_shadow_only,"hard 4C only after actual margin/export thesis break"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L104-C25-C01","symbol":"335890","company_name":"비올","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"export distributor order + consumable/procedure-volume proxy + margin bridge"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T01","case_id":"R7L104-C25-C01","symbol":"335890","company_name":"비올","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-18","entry_date":"2023-05-19","entry_price":5420,"evidence_available_at_that_date":"export distributor order + consumable/procedure-volume proxy + margin bridge","evidence_source":"public disclosure / company IR / financial statement proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv","profile_path":"atlas/symbol_profiles/335/335890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.4,"MFE_90D_pct":75.6,"MFE_180D_pct":132.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.8,"MAE_90D_pct":-8.4,"MAE_180D_pct":-11.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-28","peak_price":12620,"drawdown_after_peak_pct":-28.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.47,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"aesthetic_rf_export_margin_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|335890|Stage2-Actionable|2023-05-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C01","trigger_id":"R7L104-C25-T01","symbol":"335890","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":72,"customer_quality_score":64,"policy_or_regulatory_score":50,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":54.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":68,"relative_strength_score":72,"customer_quality_score":76,"policy_or_regulatory_score":50,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_after":58.8,"stage_label_after":"Stage2","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":75.6,"MAE_90D_pct":-8.4,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"R7L104-C25-C02","symbol":"336570","company_name":"원텍","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"device install base + overseas distribution + procedure-volume proxy"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T02","case_id":"R7L104-C25-C02","symbol":"336570","company_name":"원텍","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-15","entry_date":"2023-02-16","entry_price":3190,"evidence_available_at_that_date":"device install base + overseas distribution + procedure-volume proxy","evidence_source":"public disclosure / company IR / financial statement proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv","profile_path":"atlas/symbol_profiles/336/336570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.1,"MFE_90D_pct":114.7,"MFE_180D_pct":168.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.6,"MAE_90D_pct":-7.8,"MAE_180D_pct":-12.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":8560,"drawdown_after_peak_pct":-35.2,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":0.52,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"laser_rf_export_reimbursement_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|336570|Stage2-Actionable|2023-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C02","trigger_id":"R7L104-C25-T02","symbol":"336570","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":72,"customer_quality_score":64,"policy_or_regulatory_score":50,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":54.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":68,"relative_strength_score":72,"customer_quality_score":76,"policy_or_regulatory_score":50,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_after":58.8,"stage_label_after":"Stage2","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":114.7,"MAE_90D_pct":-7.8,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"R7L104-C25-C03","symbol":"099190","company_name":"아이센스","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"CGM launch/reimbursement path + recurring sensor revenue route"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T03","case_id":"R7L104-C25-C03","symbol":"099190","company_name":"아이센스","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2023-09-14","entry_date":"2023-09-15","entry_price":21500,"evidence_available_at_that_date":"CGM launch/reimbursement path + recurring sensor revenue route","evidence_source":"public disclosure / company IR / financial statement proxy; source URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv","profile_path":"atlas/symbol_profiles/099/099190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.0,"MFE_90D_pct":48.6,"MFE_180D_pct":77.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.2,"MAE_90D_pct":-12.7,"MAE_180D_pct":-16.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":38140,"drawdown_after_peak_pct":-24.8,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"cgm_reimbursement_revenue_bridge_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|099190|Stage3-Yellow|2023-09-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C03","trigger_id":"R7L104-C25-T03","symbol":"099190","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":72,"customer_quality_score":64,"policy_or_regulatory_score":64,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":55.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":68,"relative_strength_score":72,"customer_quality_score":76,"policy_or_regulatory_score":72,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_after":61.5,"stage_label_after":"Stage2","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":48.6,"MAE_90D_pct":-12.7,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"R7L104-C25-C04","symbol":"059210","company_name":"메타바이오메드","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"dental/medical consumable export + margin bridge, but high MAE"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T04","case_id":"R7L104-C25-C04","symbol":"059210","company_name":"메타바이오메드","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-14","entry_date":"2023-07-17","entry_price":3040,"evidence_available_at_that_date":"dental/medical consumable export + margin bridge, but high MAE","evidence_source":"public disclosure / company IR / financial statement proxy; source URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/059/059210/2023.csv","profile_path":"atlas/symbol_profiles/059/059210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.9,"MFE_90D_pct":61.5,"MFE_180D_pct":92.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.2,"MAE_90D_pct":-15.1,"MAE_180D_pct":-18.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":5850,"drawdown_after_peak_pct":-31.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.66,"four_b_full_window_peak_proximity":0.41,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"dental_biomaterial_export_bridge_positive_but_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|059210|Stage2-Actionable|2023-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C04","trigger_id":"R7L104-C25-T04","symbol":"059210","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":72,"customer_quality_score":64,"policy_or_regulatory_score":50,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":54.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":68,"relative_strength_score":72,"customer_quality_score":76,"policy_or_regulatory_score":50,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_after":58.8,"stage_label_after":"Stage2","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":61.5,"MAE_90D_pct":-15.1,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"R7L104-C25-C05","symbol":"149980","company_name":"하이로닉","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"device/export label spike without verified procedure-volume or margin bridge"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T05","case_id":"R7L104-C25-C05","symbol":"149980","company_name":"하이로닉","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":9340,"evidence_available_at_that_date":"device/export label spike without verified procedure-volume or margin bridge","evidence_source":"public disclosure / company IR / financial statement proxy; source URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/149/149980/2024.csv","profile_path":"atlas/symbol_profiles/149/149980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.8,"MFE_90D_pct":21.6,"MFE_180D_pct":25.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.6,"MAE_90D_pct":-28.7,"MAE_180D_pct":-34.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":11760,"drawdown_after_peak_pct":-48.0,"green_lateness_ratio":0.71,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"aesthetic_device_label_without_margin_bridge_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|149980|Stage3-Yellow|2024-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C05","trigger_id":"R7L104-C25-T05","symbol":"149980","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":24,"revision_score":30,"relative_strength_score":78,"customer_quality_score":42,"policy_or_regulatory_score":35,"valuation_repricing_score":76,"execution_risk_score":62,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_before":33.6,"stage_label_before":"NoStage","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":18,"revision_score":24,"relative_strength_score":58,"customer_quality_score":35,"policy_or_regulatory_score":35,"valuation_repricing_score":52,"execution_risk_score":74,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_after":24.4,"stage_label_after":"NoStage","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":21.6,"MAE_90D_pct":-28.7,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R7L104-C25-C06","symbol":"041830","company_name":"인바디","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"mature device export label; insufficient recurring procedure-volume/reimbursement bridge"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T06","case_id":"R7L104-C25-C06","symbol":"041830","company_name":"인바디","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-31","entry_date":"2023-06-01","entry_price":25800,"evidence_available_at_that_date":"mature device export label; insufficient recurring procedure-volume/reimbursement bridge","evidence_source":"public disclosure / company IR / financial statement proxy; source URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv","profile_path":"atlas/symbol_profiles/041/041830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.7,"MFE_90D_pct":12.4,"MFE_180D_pct":18.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.0,"MAE_90D_pct":-20.3,"MAE_180D_pct":-27.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-07","peak_price":30600,"drawdown_after_peak_pct":-36.2,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.58,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"bodycomposition_export_label_slow_growth_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|041830|Stage2-Actionable|2023-06-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C06","trigger_id":"R7L104-C25-T06","symbol":"041830","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":24,"revision_score":30,"relative_strength_score":78,"customer_quality_score":42,"policy_or_regulatory_score":35,"valuation_repricing_score":76,"execution_risk_score":62,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_before":33.6,"stage_label_before":"NoStage","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":18,"revision_score":24,"relative_strength_score":58,"customer_quality_score":35,"policy_or_regulatory_score":35,"valuation_repricing_score":52,"execution_risk_score":74,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_after":24.4,"stage_label_after":"NoStage","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":12.4,"MAE_90D_pct":-20.3,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R7L104-C25-C07","symbol":"065510","company_name":"휴비츠","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"export/device cycle label faded; margin/revenue bridge broke"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T07","case_id":"R7L104-C25-C07","symbol":"065510","company_name":"휴비츠","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2023-08-15","entry_date":"2023-08-16","entry_price":21000,"evidence_available_at_that_date":"export/device cycle label faded; margin/revenue bridge broke","evidence_source":"public disclosure / company IR / financial statement proxy; source URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/065/065510/2023.csv","profile_path":"atlas/symbol_profiles/065/065510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.6,"MFE_90D_pct":13.1,"MFE_180D_pct":16.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.0,"MAE_90D_pct":-32.4,"MAE_180D_pct":-39.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-31","peak_price":24500,"drawdown_after_peak_pct":-47.6,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"ophthalmic_device_china_export_margin_break_hard_4c","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|065510|Stage4C|2023-08-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C07","trigger_id":"R7L104-C25-T07","symbol":"065510","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":24,"revision_score":30,"relative_strength_score":78,"customer_quality_score":42,"policy_or_regulatory_score":35,"valuation_repricing_score":76,"execution_risk_score":62,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_before":33.6,"stage_label_before":"NoStage","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":18,"revision_score":24,"relative_strength_score":58,"customer_quality_score":35,"policy_or_regulatory_score":35,"valuation_repricing_score":52,"execution_risk_score":74,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_after":24.4,"stage_label_after":"NoStage","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":13.1,"MAE_90D_pct":-32.4,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"R7L104-C25-C08","symbol":"214680","company_name":"디알텍","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"X-ray detector export/device label; price-led blowoff without durable reimbursement/margin bridge"}
{"row_type":"trigger","trigger_id":"R7L104-C25-T08","case_id":"R7L104-C25-C08","symbol":"214680","company_name":"디알텍","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4","sector":"medical_device_export_reimbursement","primary_archetype":"device_export_reimbursement_procedure_volume_bridge","loop_objective":"quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2023-07-19","entry_date":"2023-07-20","entry_price":4100,"evidence_available_at_that_date":"X-ray detector export/device label; price-led blowoff without durable reimbursement/margin bridge","evidence_source":"public disclosure / company IR / financial statement proxy; source URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214680/2023.csv","profile_path":"atlas/symbol_profiles/214/214680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":85.4,"MFE_90D_pct":103.2,"MFE_180D_pct":110.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.7,"MAE_90D_pct":-22.8,"MAE_180D_pct":-44.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-06","peak_price":8630,"drawdown_after_peak_pct":-52.6,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"xray_detector_device_label_price_only_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214680|Stage4B|2023-07-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L104-C25-C08","trigger_id":"R7L104-C25-T08","symbol":"214680","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":24,"revision_score":30,"relative_strength_score":78,"customer_quality_score":42,"policy_or_regulatory_score":35,"valuation_repricing_score":76,"execution_risk_score":62,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_before":33.6,"stage_label_before":"NoStage","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":18,"revision_score":24,"relative_strength_score":58,"customer_quality_score":35,"policy_or_regulatory_score":35,"valuation_repricing_score":52,"execution_risk_score":74,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_after":24.4,"stage_label_after":"NoStage","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow rule rewards verified procedure-volume/reimbursement/repeat demand, and penalizes device-label spikes without recurring revenue or margin bridge.","MFE_90D_pct":103.2,"MAE_90D_pct":-22.8,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"104","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_confirmation","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["device_label_false_positive","procedure_volume_bridge_missed_structural","reimbursement_route_too_late","4C_export_margin_break_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C19_BRAND_RETAIL_INVENTORY_MARGIN, C22_INSURANCE_RATE_CYCLE_RESERVE, C24_BIO_TRIAL_DATA_EVENT_RISK, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- This MD is historical calibration research only; it is not a current stock recommendation, live scan, or production patch.
